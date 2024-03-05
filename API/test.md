# NOT WORKING

## TEST

## test.py

This code imports the requests and bs4 modules from Python, which are commonly used for networking and web scraping tasks respectively. The url variable is set to a valid URL that contains information about a HackTheBox challenge, such as its ID or title.

The r variable is then created using the get() method of the requests module, which establishes a connection with the specified URL and returns the response data in string format. The soup variable is also initialized to a BeautifulSoup object that represents the HTML content returned by the server.

The challenge_id variable is then retrieved from the HTML using the find() method of the bs4 module, which searches for and extracts specific elements within the page based on their CSS class or ID. The text.strip() method is used to remove any whitespace characters from the element's text content before assigning it to the challenge_id variable.

Finally, the print() function is used to display the challenge ID to the user.
