import logging.config
from kubernetes import client
from kubernetes.client.rest import ApiException


def create_timeout(service_name, name_space):
    """
    :param service_name:
    :param name_space:
    :return:
    """
    try:
        timeout = "5s"
        api_instance = client.CustomObjectsApi()
        to = {
          "apiVersion": "networking.istio.io/v1alpha3",
          "kind": "VirtualService",
          "metadata": {
            "name": service_name +"-timeout"
          },
          "spec": {
            "hosts": [
              service_name+"."+ service_name +".svc.cluster.local"
            ],
            "http": [
              {
                
                "timeout":timeout,
              }
            ]
          }
        }

        api_instance.create_namespaced_custom_object(
            namespace=name_space,
            body=to,
            group="networking.istio.io",
            version="v1alpha3",
            plural="virtualservices"
        )
        logging.info("Timeout for service %s with value of %s is successfully created. " % (str(service_name), str(timeout)))
        return True
    except ApiException as e:
        logging.warning("Timeout creation for service %s is not completed. %s" % (str(service_name), str(e)))
        return False


