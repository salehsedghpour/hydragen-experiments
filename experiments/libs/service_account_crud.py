import logging.config
from kubernetes import client


def create_service_account(service_account):
    """
    This function will create a kubernetes service account
    :param service_account:
    :return:
    """
    try:
        api = client.CoreV1Api()
        resp = api.create_namespaced_service(body=service_account, namespace=service_account['metadata']['namespace'])

        logging.info("Service Account {} is successfully created. \n"
                     "\t Name \t\t Namespace\n"
                     "\t {} \t {}"
                     "".format(service_account['metadata']['name'],
                               resp.metadata.name,
                               resp.metadata.namespace,
                               )
                     )
    except client.ApiException as e:
        logging.warning("Service Account creation of {} did not completed, look at the following for more details".format(str(service_account['metadata']['name'])))
        logging.warning(e)