import logging.config
from kubernetes import client


def create_deployment(deployment):
    """
    This function will create a kubernetes deployment
    :param deployment:
    :return:
    """
    try:
        api = client.AppsV1Api()
        resp = api.create_namespaced_deployment(body=deployment, namespace=deployment['metadata']['namespace'])

        logging.info("Deployment {} is successfully created. \n"
                     "\t Name \t\t Namespace \t Image \n"
                     "\t {} \t {} \t {}"
                     "".format(deployment['metadata']['name'],
                               resp.metadata.name,
                               resp.metadata.namespace,
                               resp.spec.template.spec.containers[0].image
                               )
                     )
    except client.ApiException as e:
        logging.warning("Deployment creation of {} did not completed, look at the following for more details".format(str(deployment['metadata']['name'])))
        logging.warning(e)


def update_deployment(deployment):
    """
    This function will update a kubernetes deployment
    :param deployment:
    :return:
    """
    try:
        api = client.AppsV1Api()
        resp = api.patch_namespaced_deployment(body=deployment, namespace=deployment['metadata']['namespace'],
                                               name=deployment['metadata']['name'])

        logging.info("Deployment {} is successfully updated. \n"
                     "\t Name \t\t Namespace \t Image \n"
                     "\t {} \t {} \t {}"
                     "".format(deployment['metadata']['name'],
                               resp.metadata.name,
                               resp.metadata.namespace,
                               resp.spec.template.spec.containers[0].image
                               )
                     )
    except client.ApiException as e:
        logging.warning("Deployment update of {} did not completed, look at the following for more details".format(str(deployment['metadata']['name'])))
        logging.warning(e)