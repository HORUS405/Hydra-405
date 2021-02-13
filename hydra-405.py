'''
Made by  : HORUS-405
This program use for downloading movies and their subtitels from torrent and subscene
you must run he programe in 'yourpath'/Hydra-405(movies)/movie/ 
required libraries: pyqt5 , sys , time , random , tpblite , subsceneAPI , re
python3.9
used tools : npm ,webtorrent-cli
weborrent-cli : https://github.com/webtorrent/webtorrent-cli
npm : https://www.npmjs.com/
look at line 166 change save file dir 
very important note :
    1) this programe used on linux distributions only 
    2) it will be available on windows soon 
    3) you must run the script in movie folder <<<<<<<< important
    4) please remove your downloaded movie from movie folder when you finished <<<<<<<< important
                            thank you and i will develope my skills and the script  

14/1/2021
'''

# import libraries 
from PyQt5.QtCore import *

from PyQt5.QtWidgets import *

from PyQt5.QtGui import *

from PyQt5 import uic

from sys import argv

import random

from imdb import IMDb 

from tpblite import TPB

from tpblite import CATEGORIES, ORDERS

from subsceneAPI import subtitle

from tpblite.models.torrents import Torrents

from subprocess import call, check_call,check_output 

import os 

from re import search

from time import sleep
dir_path = argv[0].replace("hydra-405.py","")
path_2 = str(dir_path+"movie/")


#from terminal import check_size
moviesdb = IMDb() # init
t = TPB('https://tpb.party') #init 
#random quots
quotes = ["“Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.”\n\r― Albert Einstein ","“Logic will get you from A to Z; imagination will get you everywhere.”\n\r― Albert Einstein ","“Anyone who has never made a mistake has never tried anything new.”\n\r― Albert Einstein ","The way to get started is to quit talking and begin doing.\n\r-Walt Disney","Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking.\n\r-Steve Jobs","If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough.\n\r-Oprah Winfrey","“As you know, madness is like gravity...all it takes is a little push.”\n\r― The Joker - Heath Ledger ","“If you’re good at something, never do it for free.”\n\r― The Joker - Heath Ledger ","“Behind this mask there is more than just flesh. Beneath this mask there is an idea... and ideas are bulletproof.”\n\r― Alan Moore, V for Vendetta ","“Remember, remember the fifth of November of gunpowder treason and plot. I know of no reason why the gun powder treason should ever be forgot.”\n\r― Alan Moore, V for Vendetta ","“Great men are not born great, they grow great.”\n\r–Mario Puzo","“In this life, you don’t have to prove nothin’ to nobody but yourself. And after what you’ve gone through, if you haven’t done that by now, it ain’t gonna never happen. Now go on back.”\n\r–Fortune","“Sometimes it is the people who no one imagines anything of who do the things that no one can imagine.”\n\r–Alan Turing","“There should be no boundaries to human endeavor. We are all different. However bad life may seem, there is always something you can do, and succeed at. While there’s life, there is hope.”\n\r–Stephen Hawking"]
#top 250 movie in the world
movies = ['The Shawshank Redemption\n', 'The Godfather\n', 'The Godfather: Part II\n', 'The Dark Knight\n', '12 Angry Men\n', "Schindler's List\n", 'Pulp Fiction\n', 'The Good, the Bad and the Ugly\n', 'The Lord of the Rings: The Return of the King\n', 'Fight Club\n', 'The Lord of the Rings: The Fellowship of the Ring\n', 'Star Wars: Episode V - The Empire Strikes Back\n', 'Forrest Gump\n', 'Inception\n', "One Flew Over the Cuckoo's Nest\n", 'The Lord of the Rings: The Two Towers\n', 'Goodfellas\n', 'The Matrix\n', 'Star Wars\n', 'Seven Samurai\n', 'City of God\n', 'Se7en\n', 'The Silence of the Lambs\n', 'The Usual Suspects\n', "It's a Wonderful Life\n", 'Life Is Beautiful\n', 'Léon: The Professional\n', 'Once Upon a Time in the West\n', 'Interstellar\n', 'Saving Private Ryan\n', 'American History X\n', 'Spirited Away\n', 'Casablanca\n', 'Raiders of the Lost Ark\n', 'Psycho\n', 'City Lights\n', 'Rear Window\n', 'The Intouchables\n', 'Modern Times\n', 'Terminator 2: Judgment Day\n', 'Whiplash\n', 'The Green Mile\n', 'The Pianist\n', 'Memento\n', 'The Departed\n', 'Gladiator\n', 'Apocalypse Now\n', 'Back to the Future\n', 'Sunset Blvd.\n', 'Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb\n', 'The Prestige\n', 'Alien\n', 'The Lion King\n', 'The Lives of Others\n', 'The Great Dictator\n', 'Inside Out\n', 'Cinema Paradiso\n', 'The Shining\n', 'Paths of Glory\n', 'Django Unchained\n', 'The Dark Knight Rises\n', 'WALL·E\n', 'American Beauty\n', 'Grave of the Fireflies\n', 'Aliens\n', 'Citizen Kane\n', 'North by Northwest\n', 'Princess Mononoke\n', 'Vertigo\n', 'Oldeuboi\n', 'Das Boot\n', 'M\n', 'Star Wars: Episode VI - Return of the Jedi\n', 'Once Upon a Time in America\n', 'Amélie\n', 'Witness for the Prosecution\n', 'Reservoir Dogs\n', 'Braveheart\n', 'Toy Story 3\n', 'A Clockwork Orange\n', 'Double Indemnity\n', 'Taxi Driver\n', 'Requiem for a Dream\n', 'To Kill a Mockingbird\n', 'Lawrence of Arabia\n', 'Eternal Sunshine of the Spotless Mind\n', 'Full Metal Jacket\n', 'The Sting\n', 'Amadeus\n', 'Bicycle Thieves\n', "Singin' in the Rain\n", 'Monty Python and the Holy Grail\n', 'Snatch.\n', '2001: A Space Odyssey\n', 'The Kid\n', 'L.A. Confidential\n', 'Rashômon\n', 'For a Few Dollars More\n', 'Toy Story\n', 'The Apartment\n', 'Inglourious Basterds\n', 'All About Eve\n', 'The Treasure of the Sierra Madre\n', 'Jodaeiye Nader az Simin\n', 'Indiana Jones and the Last Crusade\n', 'Metropolis\n', 'Yojimbo\n', 'The Third Man\n', 'Batman Begins\n', 'Scarface\n', 'Some Like It Hot\n', 'Unforgiven\n', '3 Idiots\n', 'Up\n', 'Raging Bull\n', 'Downfall\n', 'Mad Max: Fury Road\n', 'Jagten\n', 'Chinatown\n', 'The Great Escape\n', 'Die Hard\n', 'Good Will Hunting\n', 'Heat\n', 'On the Waterfront\n', "Pan's Labyrinth\n", 'Mr. Smith Goes to Washington\n', 'The Bridge on the River Kwai\n', 'My Neighbor Totoro\n', 'Ran\n', 'The Gold Rush\n', 'Ikiru\n', 'The Seventh Seal\n', 'Blade Runner\n', 'The Secret in Their Eyes\n', 'Wild Strawberries\n', 'The General\n', 'Lock, Stock and Two Smoking Barrels\n', 'The Elephant Man\n', 'Casino\n', 'The Wolf of Wall Street\n', "Howl's Moving Castle\n", 'Warrior\n', 'Gran Torino\n', 'V for Vendetta\n', 'The Big Lebowski\n', 'Rebecca\n', 'Judgment at Nuremberg\n', 'A Beautiful Mind\n', 'Cool Hand Luke\n', 'The Deer Hunter\n', 'How to Train Your Dragon\n', 'Gone with the Wind\n', 'Fargo\n', 'Trainspotting\n', 'It Happened One Night\n', 'Dial M for Murder\n', 'Into the Wild\n', 'Gone Girl\n', 'The Sixth Sense\n', 'Rush\n', 'Finding Nemo\n', 'The Maltese Falcon\n', 'Mary and Max\n', 'No Country for Old Men\n', 'The Thing\n', 'Incendies\n', 'Hotel Rwanda\n', 'Kill Bill: Vol. 1\n', 'Life of Brian\n', 'Platoon\n', 'The Wages of Fear\n', 'Butch Cassidy and the Sundance Kid\n', 'There Will Be Blood\n', 'Network\n', 'Touch of Evil\n', 'The 400 Blows\n', 'Stand by Me\n', '12 Years a Slave\n', 'The Princess Bride\n', 'Annie Hall\n', 'Persona\n', 'The Grand Budapest Hotel\n', 'Amores Perros\n', 'In the Name of the Father\n', 'Million Dollar Baby\n', 'Ben-Hur\n', 'The Grapes of Wrath\n', "Hachi: A Dog's Tale\n", 'Nausicaä of the Valley of the Wind\n', 'Shutter Island\n', 'Diabolique\n', 'Sin City\n', 'The Wizard of Oz\n', 'Gandhi\n', 'Stalker\n', 'The Bourne Ultimatum\n', 'The Best Years of Our Lives\n', 'Donnie Darko\n', 'Relatos salvajes\n', '8½\n', 'Strangers on a Train\n', 'Jurassic Park\n', 'The Avengers\n', 'Before Sunrise\n', 'Twelve Monkeys\n', 'The Terminator\n', 'Infernal Affairs\n', 'Jaws\n', 'The Battle of Algiers\n', 'Groundhog Day\n', 'Memories of Murder\n', 'Guardians of the Galaxy\n', 'Monsters, Inc.\n', 'Harry Potter and the Deathly Hallows: Part 2\n', 'Throne of Blood\n', 'The Truman Show\n', 'Fanny and Alexander\n', 'Barry Lyndon\n', 'Rocky\n', 'Dog Day Afternoon\n', 'The Imitation Game\n', 'Yip Man\n', "The King's Speech\n", 'High Noon\n', 'La Haine\n', 'A Fistful of Dollars\n', 'Pirates of the Caribbean: The Curse of the Black Pearl\n', 'Notorious\n', 'Castle in the Sky\n', 'Prisoners\n', 'The Help\n', "Who's Afraid of Virginia Woolf?\n", 'Roman Holiday\n', 'Spring, Summer, Fall, Winter... and Spring\n', 'The Night of the Hunter\n', 'Beauty and the Beast\n', 'La Strada\n', 'Papillon\n', 'X-Men: Days of Future Past\n', 'Before Sunset\n', 'Anatomy of a Murder\n', 'The Hustler\n', 'The Graduate\n', 'The Big Sleep\n', 'Underground\n', 'Elite Squad: The Enemy Within\n', 'Gangs of Wasseypur\n', 'Lagaan: Once Upon a Time in India\n', 'Paris, Texas\n', 'Akira']

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # import ui 
        uic.loadUi(dir_path+"UI.ui",self)
        #identify the window 
        self.setWindowTitle("Hydra-405")
        self.setGeometry(400,200,1251,640)
        self.setFixedSize(1251, 640)

        # recognize on the buttons
        self.ent = self.findChild(QLineEdit,"lineEdit")
        self.btn = self.findChild(QPushButton,"pushButton")
        self.btn_2 = self.findChild(QPushButton,"pushButton_2")
        self.movie = self.findChild(QLabel,"label_8")
        self.combo_box_1 = self.findChild(QComboBox,"comboBox")
        self.combo_box_2 = self.findChild(QComboBox,"comboBox_2")
        self.qbox = self.findChild(QTextBrowser,"testBrowser_3")
        self.progressbar = self.findChild(QProgressBar,"progressBar")
        self.ent_2=self.findChild(QLineEdit,"lineEdit_2")
        self.btn_3=self.findChild(QPushButton,"pushButton_3")
        self.terminal = self.findChild(QTextEdit,"textEdit")

        #connect buttons with functions
        self.btn_2.clicked.connect(self.movie_information)
        self.btn_2.clicked.connect(self.movie_torrent)
        self.btn.clicked.connect(self.movie_torrent_2)      
        self.quotes = self.findChild(QTextBrowser,"textBrowser")
        self.information = self.findChild(QTextBrowser,"textBrowser_2")

        #show random quotes and movies on the window 
        self.quotes.setText(random.choice(quotes))
        self.movie.setText(random.choice(movies))

        


    # this function show information about movie and download movie subtitles

    def movie_information(self):
        QMessageBox.information(self,"searching","Searching please Wait.... ")
        global name 
        global y 
        try:
            name = self.ent.text()
            movies_1 = moviesdb.search_movie(name)
            id = movies_1[0].getID()
            movie_1= moviesdb.get_movie(id)
            self.information.append("     [+] Information About The Movie [+]")
            t = "Title : "+str(movie_1["title"])
            
            y = "initial release : "+str(movie_1["year"])
            d =movie_1["directors"]
            r = "Director : "
            self.information.append(t)
            self.information.append(y)
            for i in d:
                self.information.append(r+str(i))
            for genre in movie_1['genres']:
                self.information.append("Genre : "+genre)
            self.information.append("*****************Actors*****************")
            a = movie_1["actors"]
            for y in a :
                self.information.append(str(y))
            yt = self.combo_box_2.currentText()   
            if yt == "Arabic":
                obj =subtitle.search(title=str(name),year=str(movie_1["year"]),language="arabic",limit='1')
                obj.downloadZIP(dir_path)
            if yt == "English":
                obj =subtitle.search(title=str(name),year=str(movie_1["year"]),language="english",limit='1')
                obj.downloadZIP(dir_path)
            if yt == "German":
                obj =subtitle.search(title=str(name),year=str(movie_1["year"]),language="german",limit='1')
                obj.downloadZIP(dir_path)
            if yt == "French":
                obj =subtitle.search(title=str(name),year=str(movie_1["year"]),language="french",limit='1')
                obj.downloadZIP(dir_path)
            if yt == "Spanish":
                obj =subtitle.search(title=str(name),year=str(movie_1["year"]),language="spanish",limit='1')
                obj.downloadZIP(dir_path)
            if yt == "Italian":
                obj =subtitle.search(title=str(name),year=str(movie_1["year"]),language="italian",limit='1')
                obj.downloadZIP(dir_path)
            if yt == "Portuguese":
                obj =subtitle.search(title=str(name),year=str(movie_1["year"]),language="portuguese",limit='1')
                obj.downloadZIP(dir_path)
            if yt == "Turkish":
                obj =subtitle.search(title=str(name),year=str(movie_1["year"]),language="turkish",limit='1')
                obj.downloadZIP(dir_path)
        except Exception:
            QMessageBox.warning(self,"Data Error","Invalid word ")




    #this function scrab movie torrents from the pirated bay 
    def movie_torrent(self):
        try:
            movie_name = self.ent.text()
            global tor 
            tor = []
            global torrents ,torrent
            torrents = t.search(movie_name,page=1,category=CATEGORIES.VIDEO.HD_MOVIES)
            for torrent in torrents:
                self.combo_box_1.addItem(str(torrent))
                tor.append(str(torrent))
        except Exception:
            QMessageBox.warning(self,"Data Error","Invalid word ")




    #this function download the movie 
    def movie_torrent_2(self):
        try :
            combo_r = str(self.combo_box_1.currentText())
            result_2 = tor.index(combo_r)
            magnetlink = torrents[result_2].magnetlink
            downlaodlink  = magnetlink
            global title,byte
            title = torrents[result_2].title
            byte = torrents[result_2].byte_size
            
            output = check_call(["webtorrent "+str(magnetlink)],shell=True)
            sleep(30)

            while True:
                from terminal import check_size
                z = check_size()
                zz = int(z) *1000
                value = (zz/byte)*100  
                value_1 = int(value)
                self.progressbar.setValue(value_1)
                if value == 97 :
                    value +=2
                if value == 100:
                    QMessageBox.information(self,"Download","Download has been finished")
                    sleep(5)
                    e=self.ent.setText(" ")
                    self.progressbar.setValue(0)
                    self.information.setText(" ")
                    self.combo_box_1.clear()
                    break
        except Exception:
            QMessageBox.warning(self,"Data Error","Invalid word ")     

dir_path = argv[0].replace("hydra-405.py","")

app = QApplication(argv)
window = MainWindow()
window.show()
app.exec_()


