from bs4 import BeautifulSoup
from common import dates, http, releaserlog
from common.git import Git

"""Fetch released versions from docs.chef.io and retrieve their date from GitHub.
docs.chef.io needs to be scraped because not all tagged versions are actually released.

More context on https://github.com/khulnasoft/release-perser/pull/4425#discussion_r1447932411.
"""

with releaserlog.ProductData("chef-infra-server") as product_data:
    rn_response = http.fetch_url("https://docs.chef.io/release_notes_server/")
    rn_soup = BeautifulSoup(rn_response.text, features="html5lib")
    released_versions = [h2.get('id') for h2 in rn_soup.find_all('h2', id=True) if h2.get('id')]

    git = Git("https://github.com/chef/chef-server.git")
    git.setup(bare=True)

    versions = git.list_tags()
    for version, date_str in versions:
        if version in released_versions:
            date = dates.parse_date(date_str)
            product_data.declare_version(version, date)
