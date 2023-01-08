import logging.config
from kubernetes import client


def create_service(service):
    """
    This function will create a kubernetes service
    :param service:
    :return:
    """
    try:
        api = client.CoreV1Api()
        resp = api.create_namespaced_service(body=service, namespace=service['metadata']['namespace'])

        logging.info("Service {} is successfully created. \n"
                     "\t Name \t\t Namespace\n"
                     "\t {} \t {}"
                     "".format(service['metadata']['name'],
                               resp.metadata.name,
                               resp.metadata.namespace,
                               )
                     )
    except client.ApiException as e:
        logging.warning("Service creation of {} did not completed, look at the following for more details".format(str(service['metadata']['name'])))
        logging.warning(e)