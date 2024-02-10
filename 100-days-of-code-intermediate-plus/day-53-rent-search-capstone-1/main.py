from scraper import Scraper
from form_creator import FormCreator

# Program Requirements:


#

#
#
# Once all the data has been filled in, click on the "Sheet" icon to create a Google Sheet from the responses to the
# Google Form. You should end up with a spreadsheet with all the details from the properties.


scraper = Scraper()
listing_data = scraper.scrape()

form_creator = FormCreator()
form_creator.create_form(listing_data)