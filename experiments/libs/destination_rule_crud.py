import logging.config
from kubernetes import client
from kubernetes.client.rest import ApiException


def create_circuit_breaker(service_name, name_space, max_requests):
    """
    :param service_name:
    :param name_space:
    :param max_requests:
    :return:
    """
    try:
        api_instance = client.CustomObjectsApi()
        cb = {
            "apiVersion": "networking.istio.io/v1alpha3",
            "kind": "DestinationRule",
            "metadata": {"name": service_name+"-cb"},
            "spec": {
                "host": service_name,
                "trafficPolicy": {
                    "connectionPool":{
                        "http": {"http2MaxRequests": max_requests}
                    }
                }
            }
        }
        api_instance.create_namespaced_custom_object(
            namespace=name_space,
            body=cb,
            group="networking.istio.io",
            version="v1alpha3",
            plural="destinationrules"
        )
        logging.info("Circuit breaker for service %s with value of %s is successfully created. " % (str(service_name), str(max_requests)))
        return True
    except ApiException as e:
        logging.warning("Circuit breaker creation for service %s is not completed. %s" % (str(service_name), str(e)))
        return False


def delete_circuit_breaker(service_name, name_space):
    """
    :param name_space:
    :param service_name:
    :return:
    """
    try:
        api_instance = client.CustomObjectsApi()
        api_instance.delete_namespaced_custom_object(
            namespace=name_space,
            group="networking.istio.io",
            version="v1alpha3",
            plural="destinationrules",
            name=service_name+"-cb"
        )
        logging.info("Circuit breaker for service %s is successfully deleted. " % str(service_name))
        return True
    except ApiException as e:
        logging.warning(
            "Circuit breaker deletion for service %s is not completed. %s" % (str(service_name), str(e)))
        return False


def patch_circuit_breaker(service_name, name_space, max_requests):
    """
    :param service_name:
    :param name_space:
    :param max_requests:
    :return:
    """
    try:
        api_instance = client.CustomObjectsApi()
        cb = {
            "apiVersion": "networking.istio.io/v1alpha3",
            "kind": "DestinationRule",
            "metadata": {"name": service_name+"-cb"},
            "spec": {
                "host": service_name,
                "trafficPolicy":{
                    "connectionPool":{
                        "http": {"http2MaxRequests": max_requests}
                    }
                }
            }
        }
        api_instance.patch_namespaced_custom_object(
            name=service_name+"-cb",
            namespace=name_space,
            body=cb,
            group="networking.istio.io",
            version="v1alpha3",
            plural="destinationrules"
        )
        logging.info("Circuit breaker for service %s with value of %s is successfully updated. " % (str(service_name), str(max_requests)))
        return True
    except ApiException as e:
        logging.warning("Circuit breaker update for service %s is not completed. %s" % (str(service_name), str(e)))
        return False