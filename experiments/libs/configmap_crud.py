import logging.config
from kubernetes import client


def create_configmap(configmap):
    """
    This function will create a kubernetes configmap
    :param configmap:
    :return:
    """
    try:
        api = client.CoreV1Api()
        resp = api.create_namespaced_config_map(body=configmap, namespace=configmap['metadata']['namespace'])

        logging.info("Configmap {} is successfully created. \n"
                     "\t Name \t\t Namespace\n"
                     "\t {} \t {}"
                     "".format(configmap['metadata']['name'],
                               resp.metadata.name,
                               resp.metadata.namespace,
                               )
                     )
    except client.ApiException as e:
        logging.warning("Configmap creation of {} did not completed, look at the following for more details".format(str(configmap['metadata']['name'])))
        logging.warning(e)


def update_configmap(configmap):
    """
    This function will update a kubernetes configmap
    :param configmap:
    :return:
    """
    try:
        api = client.CoreV1Api()
        resp = api.patch_namespaced_config_map(body=configmap, namespace=configmap['metadata']['namespace'],
                                               name=configmap['metadata']['name'])

        logging.info("Configmap {} is successfully updated. \n"
                     "\t Name \t\t Namespace \n"
                     "\t {} \t {}"
                     "".format(configmap['metadata']['name'],
                               resp.metadata.name,
                               resp.metadata.namespace,
                               )
                     )
    except client.ApiException as e:
        logging.warning("Configmap update of {} did not completed, look at the following for more details".format(str(configmap['metadata']['name'])))
        logging.warning(e)