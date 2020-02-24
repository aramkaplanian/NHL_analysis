"""
Code by Aram Kaplanian.
requires tools.py file in order to run.
"""

from functions import *

website = "https://www.corsicahockey.com/nhl/teams/nhl-team-stats"

cor = extractor(website)
cor.get_url()

# ensuring we get all plays rather than just the default 5v5
cor.select_drop_downs('game_state_select', 'any')
# cor.select_drop_downs('venue_select', 2)

# ensuring we only have on-ice data
cor.select_report()

"""
these seasons are inputed in thier manner to deal with bugs in the
corsica website
"""
# selecting the correct seasonal data
cor.open_season()
season_lst = ["2019-2020", "2019-2020", "2018-2019", "2017-2018"]
for i in season_lst:
    cor._click(i)
cor.open_season()

# getting the csv data to clipboard
cor.click_csv('.show-csv')
cor.click_csv('button.btn:nth-child(1)')

# saving data from clipboard
extractor.send_to_df()

cor.close_browser()
