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
        resp = api.create_namespaced_service_account(body=service_account, namespace=service_account['metadata']['namespace'])

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


def update_service_account(service_account):
    """
    This function will update a kubernetes service_account
    :param service_account:
    :return:
    """
    try:
        api = client.CoreV1Api()
        resp = api.patch_namespaced_service_account(body=service_account, namespace=service_account['metadata']['namespace'],
                                               name=service_account['metadata']['name'])

        logging.info("Service Account {} is successfully updated. \n"
                     "\t Name \t\t Namespace \n"
                     "\t {} \t {}"
                     "".format(service_account['metadata']['name'],
                               resp.metadata.name,
                               resp.metadata.namespace,
                               )
                     )
    except client.ApiException as e:
        logging.warning("Service Account update of {} did not completed, look at the following for more details".format(str(service_account['metadata']['name'])))
        logging.warning(e)


def delete_service_account(service_account):
    """
    This function will delete a kubernetes service_account
    :param service_account:
    :return:
    """
    try:
        api = client.CoreV1Api()
        api.delete_namespaced_service_account(namespace=service_account['metadata']['namespace'],
                                               name=service_account['metadata']['name'])

        logging.info("Service Account {} is successfully deleted.".format(service_account['metadata']['name']))
    except client.ApiException as e:
        logging.warning("Service Account deletion of {} did not completed, look at the following for more details".format(str(service_account['metadata']['name'])))
        logging.warning(e)