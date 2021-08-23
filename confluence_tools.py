# Confluence Tools

# Dependencies

import json
import os
import requests
from requests_toolbelt import MultipartEncoder
import time

# Constants

def get_parent_page(config_confluence: dict, page_id: str):
    '''
    get the dict of the details of the parent page from the id

    :param config_confluence: dict, confluence config dict
    :param page_id: str, page id

    :return: dict of page details
    '''

    r = requests.get(
        config_confluence['request_base'] + "/wiki/rest/api/content",
        params={'id': page_id},
        auth=(config_confluence['confluence_email'], config_confluence['confluence_api_token'])
        # does NOT have to be base64 encoded
    )
    return r.json()['results'][0]  # assumes result exists and it's the first one

def upload_attachment(config_confluence: dict, page_id: str, attachment_path: str, attachment_type: str = "image/gif"):
    '''
    upload an attachment to a confluence page by id

    :param config_confluence: dict, confluence config dict
    :param page_id: str, id for page in confluence
    :param attachment_path: str, path to attachment
    :param attachment_type: str, type of attachment

    :return: status code of post
    '''

    # get details
    url = f"{config_confluence['request_base']}/wiki/rest/api/content/{page_id}/child/attachment"
    attachment_filename = os.path.basename(attachment_path)

    mp_encoder = MultipartEncoder(
        fields={
            'file': (attachment_filename, open(attachment_path, 'rb'), attachment_type),
            'minorEdit': "true",
            'type': "image/gif"
        }
    )

    response = requests.post(
        url,
        auth=(config_confluence['confluence_email'], config_confluence['confluence_api_token']),
        # does NOT have to be base64 encoded,
        data=mp_encoder,
        headers={"X-Atlassian-Token": "nocheck", 'Content-Type': mp_encoder.content_type}
    )

    return response.status_code

def upload_attachment_list(config_confluence: dict, target_page_id: str, ls_attachments: list, sleep: int = 1):

    # define type based on extension
    dict_type = {
        ".png": "image/png",
        ".jpeg": "image/jpeg",
        ".jpg": "image/jpg",
        ".gif": "image/gif",
        ".bmp": "image/bmp",
        ".tiff": "image/tiff",
        ".svg": "image/svg+xml",
        ".xml": "image/svg+xml"
    }

    # upload each attachment
    for attachment_path in ls_attachments:
        upload_attachment(
            config_confluence=config_confluence,
            page_id=target_page_id,
            attachment_path=attachment_path,
            attachment_type=dict_type[os.path.splitext(attachment_path)[1].lower()]
        )
        time.sleep(sleep)
    return

def add_comment(config_confluence: dict, dict_parent_page: dict, str_comment: str = "", attachment_filename: str = None):
    '''
    add comment to the parent page

    :param config_confluence: dict, confluence config dict
    :param dict_parent_page: dict, response from get_parent_page
    :param str_comment: str, comment with HTML if you want

    :return: status code of post
    '''

    # prepare comment
    if attachment_filename is None:
        post_comment = str_comment
    else:
        post_comment = f"""{str_comment} <ac:image><ri:attachment ri:filename="{attachment_filename}"/></ac:image>"""

    # prepare page data
    dict_page_data = {
        'type': 'comment',
        'container': dict_parent_page,
        'body': {
            'storage': {
                'value': post_comment,
                'representation': 'storage'
            }
        }
    }

    r = requests.post(
        config_confluence['request_base'] + "/wiki/rest/api/content",,
        data=json.dumps(dict_page_data),
        auth=(config_confluence['confluence_email'], config_confluence['confluence_api_token']),  # does NOT have to be base64 encoded
        headers=({'Content-Type': 'application/json'})
    )

    return r.status_code