# Confluence Fan Bot

# Dependencies

import glob
import json
import os
import random
import requests
import sys
import time

import confluence_tools as ct

# Funcs

def praise_page_config(config_confluence: dict, config_praise: dict, ls_attachments: list = None):

    # praise page
    praise_page(
        config_confluence=config_confluence,
        target_page_id=config_praise['target_page_id'],
        praise_limit=config_praise['praise_limit'],
        ls_attachments=ls_attachments
    )

    return

def praise_page(config_confluence: dict, target_page_id: str, praise_limit: int, ls_attachments: list = None, sleep: int = 1):

    # Get Target Page by ID
    dict_parent_page = ct.get_parent_page(config_confluence, target_page_id)

    # Add Comments

    # submit comments until limit
    for i in range(praise_limit):

        # random float
        flt_random = random.random()

        # just gif
        if flt_random <= 0.8:
            ct.add_comment(
                config_confluence,
                dict_parent_page,
                attachment_filename=os.path.basename(random.choice(ls_attachments))
            )

        # kanye
        elif flt_random <= 0.9:

            # get kanye quote
            kanye_quote = None
            while kanye_quote is None:
                kanye_quote = requests.get("http://api.kanye.rest/").json()['quote']
                if any(word in kanye_quote for word in ["fuck","shit"]):
                    kanye_quote = None

            # add comment
            ct.add_comment(
                config_confluence,
                dict_parent_page,
                str_comment=kanye_quote
            )

        # chuck norris
        else:

            # get chuck norris joke
            r = requests.get("https://api.chucknorris.io/jokes/random", verify=False)

            # add comment
            ct.add_comment(
                config_confluence,
                dict_parent_page,
                str_comment=r.json()['value']
            )

        # sleep
        time.sleep(sleep)

if __name__ == "__main__":

    # Get Config

    # confluence
    with open (sys.argv[1], "r") as f:
        config_confluence = json.loads(f.read())

    # praise
    with open(sys.argv[2], "r") as f:
        config_praise = json.loads(f.read())

    # Praise Page
    praise_page_config(config_confluence, config_praise)