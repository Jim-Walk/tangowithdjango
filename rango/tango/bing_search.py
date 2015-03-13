import json
import urllib, urllib2

BING_API_KEY = "DqScL2uyk1r3tKTwJfGljWpA++RSHRy4VIubB9k62tU"


def run_query(search_terms):

    #First part of the url

    root_url = 'https://api.datamarket.azure.com/Bing/Search/'
    source = 'Web'
    results_per_page = 10
    offset = 0
    query = "'{0}'".format(search_terms)
    query = urllib.quote(query)

    #Second part of the url

    search_url = "{0}{1}?$format=json&$top={2}&$skip={3}&Query={4}".format(
        root_url,
        source,
        results_per_page,
        offset,
        query)

    # Setup authentication with the Bing servers.
    # The username MUST be a blank string, and put in your API key!
    username = ''


    # Create a 'password manager' which handles authentication for us.
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, search_url, username, BING_API_KEY)

    # Create our results list which we'll populate.
    results = []

    try:
        # Prepare for connecting to Bing's servers.
        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)

        # Connect to the server and read the response generated.
        response = urllib2.urlopen(search_url).read()

        # Convert the string response to a Python dictionary object.
        json_response = json.loads(response)

        # Loop through each page returned, populating out results list.
        for result in json_response['d']['results']:
            results.append({
            'title': result['Title'],
            'link': result['Url'],
            'summary': result['Description']})

    # Catch a URLError exception - something went wrong when connecting!
    except urllib2.URLError, e:
        print "Error when querying the Bing API: ", e

    # Return the list of results to the calling function.
    return results

# def main():
#     search_term = raw_input("Enter search term: ")
#     searchList = run_queary(search_term)
#     for search in searchList:
#         print search["link"], " - ", search["title"]
#
# if __name__ == '__main__':
#     main()