# import libraries
import urllib2
from bs4 import BeautifulSoup


SEEN = {}


global ROOT
ROOT = "https://lasthand.herokuapp.com"
page = urllib2.urlopen(ROOT)
soup = BeautifulSoup(page, 'html.parser')


def search_site(soup, iteration)
  for a in soup.find_all('a', href=True):
    page = urllib2.urlopen(ROOT+a['href'])
    soup = BeautifulSoup(page, 'html.parser')
    if a not in SEEN.keys():
      search_site(a, iteration + 1)


"""


gotcha: recursively, call stack, overflow, while loop instead

architecture:
how would you design an online game for chess, 2 players, matches, link up with other players, waiting room
websockets
routing: 
  homepage
  controller ...
  6 endpoints: create (POST /match), show (GET /match/{id}), delete (DELETE /match{id}) 
  security of game: hash the id of the game they're in, make it random
models:

data layer
  player, game, match
  meta data: join table for game id 

avoid: n+1 queries, lazy loading, eager load solves this
  
store in db

iterative testing for atomic values
abstract out logic from view so it can be tested



"""
