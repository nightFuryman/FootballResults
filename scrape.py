import mechanicalsoup

from utils import save_to_now


def single_pattern(urls_to_follow):
	# this pattern is a single table with 10 to 21 rows
	final_string = ""
	for web in urls_to_follow: 

		new_browser = mechanicalsoup.Browser() # creating a new browser page
		league = new_browser.get(web)

		rows = league.soup.findAll('tr') # get all the table lines
		name = league.soup.find('caption') # get the league name

		final_string += f'\n>> {name.text.strip()}\n'

		for i in range(1,len(rows)): # an iteration over table rows
			final_string += f'{i}.'
			try:
				link = rows[i].find('a')
				final_string += link.text.strip()
			except:
				try:
					team = rows[i].find('span')
					final_string += team.text.strip()
				except:
					final_string += 'NVFA'
			points = rows[i].find('b')
			final_string += f" : {points.text.strip()}\n"

	save_to_now(final_string) # saving the whole thing inside a text file


def tables_pattern(urls_to_follow):
	# this pattern is a multi table page that has 4 to 12 tables init
	final_string = ""
	for web in urls_to_follow: 

		new_browser = mechanicalsoup.Browser() # creating a new browser page
		league = new_browser.get(web)

		divisons = league.soup.findAll('div', {'class':'football__group'})
		name = league.soup.find('caption')

		final_string += f'\n>> {name.text.strip()}\n'

		for div in divisons: # scraping each table with row init
			final_string += f'{div.h4.text.strip()}\n'

			rows = div.findAll('tr')

			for i in range(1,len(rows)):
				final_string += f'    {i}.'
				try:
					link = rows[i].find('a')
					final_string += link.text.strip()
				except:
					try:
						team = rows[i].find('span')
						final_string += team.text.strip()
					except:
						final_string += 'NVFA'
				points = rows[i].find('b')
				final_string += f" : {points.text.strip()}\n"	

	save_to_now(final_string) # saving the whole thing inside a text file	