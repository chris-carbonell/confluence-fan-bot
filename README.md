# Overview

# Confluence Fan Bot

<b>Confluence Fan Bot</b> posts comments (incl. GIFs or nearly any other type of attachment) to a Confluence page for you.

# Quickstart

<code>python -m praise_config ./config/confluence.json ./config/praise.json</code>

# Prerequisites

* Python 3.8.1
* Confluence API credentials
* (Optional) Attachments (e.g., [chris-carbonell/download-all-the-gifs](https://github.com/chris-carbonell/download-all-the-gifs))

# Process Overview

* With the proper credentials, this bot will loop through your defined praises (via <code>config/praises.json</code>).
* If you want to include attachments (e.g., GIFs) in your comments, the attachments must be uploaded to the page first and then the comment can refer to those attachments (see <code>confluence_tools.py</code>).

# How To

1. Update <code>config/confluence.json</code> with your Confluence email and accompanying API key.
2. Update <code>config/praise.json</code> with the details of the target page and how you want to comment.
	* <code>request_base</code> should be the base URL for your organization's Atlassian account (e.g., <code>https://<b>company</b>.atlassian.net</code>).
	* <code>target_page_id</code> should be the page ID for the target Confluence article (e.g., <code>https://<b>company</b>.atlassian.net/wiki/spaces/~<b>space_id</b>/pages/<b>page_id</b>/Test+Page</code>).
		* Refer to the Confluence documentation here: [link](https://confluence.atlassian.com/confkb/how-to-get-confluence-page-id-648380445.html).
	* <code>praises</code> contains a list of all the potential comments to be posted on the target Confluence page.
3. Praise the page with:<br>
<code>python -m praise_config ./config/confluence.json ./config/praise.json</code>

# Table of Contents

* <code>confluence_tools.py</code><br>
suite of tools to add comments to a Confluence page
* <code>praise_config.py</code><br>
main script which orchestrates the praising
	* includes random comments from [kanye.rest](https://kanye.rest/) and [api.chucknorris.io](https://api.chucknorris.io/)
* <code>praise_page.py</code><br>
advanced usage (not documented here)
	* requires <code>get_gifs.py</code> from [chris-carbonell/download-all-the-gifs](https://github.com/chris-carbonell/download-all-the-gifs

# Warranty

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# Resources

* How to Get the Confluence Article's Page ID<br>
https://confluence.atlassian.com/confkb/how-to-get-confluence-page-id-648380445.html
* Download GIFs from GIPHy
https://github.com/chris-carbonell/download-all-the-gifs