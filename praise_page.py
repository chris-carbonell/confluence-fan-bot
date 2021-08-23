# Overview
# - praise a page

# Prerequisites
# - config files set up as expected
# - page exists

# Dependencies

from datetime import datetime
import glob
import json
import sys

import get_gifs as gg
import praise_config as pc
import confluence_tools as ct


# Funcs

def date_log(comment: str):
    print(f"""{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}: {comment}""")


if __name__ == "__main__":

    # assume config

    date_log("loading config...")

    # confluence
    with open("./config/confluence.json", "r") as f:
        config_confluence = json.loads(f.read())

    # giphy
    with open("./config/giphy.json", "r") as f:
        config_giphy = json.loads(f.read())

    # praise
    with open("./config/praise.json", "r") as f:
        config_praise = json.loads(f.read())

    # get praise details
    # overrides whatever is in the config files

    target_page_id = sys.argv[1]

    if "-l" not in sys.argv:
        # no limit provided
        praise_limit = 100
    else:
        praise_limit = int(sys.argv[sys.argv.index("-l")+1])

    # get execution details
    # by default, assume only praise page
    # ie assume gifs already downloaded and uploaded

    bool_download = "-d" in sys.argv
    bool_upload = "-u" in sys.argv or bool_download  # if we have to download, we have to upload

    date_log("config loaded successfully")

    # download gifs
    if bool_download:
        date_log("downloading gifs...")
        gg.get_gifs_from_terms(config_giphy, config_giphy['search_terms'])
        date_log("gifs downloaded successfully")

    # upload gifs
    if bool_upload:
        date_log("uploading gifs...")
        ct.upload_attachment_list(
            config_confluence=config_confluence,
            target_page_id=target_page_id,
            ls_attachments=glob.glob(config_giphy['output_dir'] + "*.gif")  # ie all gifs in the output dir,
        )
        date_log("gifs uploaded successfully")

    # praise page
    date_log("praising page...")
    pc.praise_page(
        config_confluence=config_confluence,
        target_page_id=target_page_id,
        praise_limit=praise_limit,
        ls_gifs=glob.glob(config_giphy['output_dir'] + "*.gif")  # ie all gifs in the output dir
    )
    date_log("praised page successfully")

# Quickstart

# just praise page 100 times (ie no downloading, uploading)
# python -m praise_page 1234567890

# praise page 1000 times (ie no downloading, uploading)
# python -m praise_page 1234567890 -l 1000

# download and upload gifs then praise
# python -m praise_page 1234567890 -d