"""
 pyOSRS: A python module to help easily obtain information from the Old School RuneScape Hiscores and Grand Exchange.
    Copyright (C) 2017  Aaron Thomas

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
import mechanicalsoup
br = mechanicalsoup.Browser()

'''
this is old code, pretty sure this will be replaced by PersonalHiscore class
keeping it JSUT IN CASE!
commenting it out so people have to read this and uncomment it before trying to run it
(it doesn't even really do what it was probably supposed to)
def hiscore_player(rsn,skill=None):
    url = "http://services.runescape.com/m=hiscore_oldschool/hiscorepersonal.ws?user1={}".format(rsn)
    page = br.get(url)
    content = page.soup.find_all("div", attrs={"id": "contentHiscores"})[0]
    content = content.find_all("tr")
    return content
    '''

skill_template = {
    'rank': 100000,
    'experience': 0,
    'level': 1
}

bh_template = {
    'rank': 100000,
    'kills': 0
}

clue_template = {
    'rank': 100000,
    'completed': 0
}

lms_template = {
    'rank': 100000,
    'complete': 0
}


class PersonalHiscore:
    '''
    Has:
        rsn (associated runescape name)
        the rsn's hiscores data (@todo(aaron): figure out how to organize this)

    list of hiscores data we'll want:
        time of query
        skilling:
            [rank, experience, level] of each skill
        bounty hunter:
            [rank,kills] of Huter and Rogue
        clue scrolls:
            [rank, clues completed] for easy, medium, hard, master, all
        lms:
            [rank,score]

        rank is first so people can always do [0]
        for skilling there's three so if it was last it'd be [2] there and [1] elsewhere
        we could put it in [1] but exp and total levl should be adjacent indices


    '''

    def __init__(self, rsn):
        url = "http://services.runescape.com/m=hiscore_oldschool/hiscorepersonal.ws?user1={}".format(rsn)
        page = br.get(url)
        content = page.soup.find_all("div", attrs={"id": "contentHiscores"})[0]
        content = content.find_all("tr")
        skill_indicies = [i+3 for i in range(24)]
        ''' the first four tr in the page are junk
        the next 23 tr in the page have skillsng info, just what we need!
        one for the total level, then 23 for the individual skills'''
        content = [content[i] for i in skill_indices]

    #@todo(aaron): code this