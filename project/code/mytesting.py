import unittest
from dao.implementation import VirtualArtGalleryImplementation
import mysql.connector
from mysql.connector import Error

con=mysql.connector.connect(host="localhost",
                            user="root",
                            password="root",
                            port="3306",
                            database="virtualartgallery")
cur=con.cursor()
class MyTestCase(unittest.TestCase):
    virtual=VirtualArtGalleryImplementation()
    def test_searching_artwork(self):
        flag="Mona lisa"
        self.assertEqual(self.virtual.search_artworks(flag),True)
    def test_removing_artwork(self):
        flag = 1
        self.assertEqual(self.virtual.remove_artwork(flag), True)
    def test_update_artwork(self):
        result=self.update_artwork()
        self.assertEqual(result,True)
    def test_add_artwork(self):
        result=self.add_work()
        self.assertEqual(result, True)


    def update_artwork(self):

        title = "starry Night"
        description = "A famous night sky painting with swirling clouds and bright stars."
        creationDate = "1889-06-29"
        medium = "oil in poplar"
        query = "update artwork set title=%s,description=%s,creationDate=%s,medium=%s where artworkid= 1"
        cur.execute(query,(title,description,creationDate,medium,))
        cur.fetchall()

        return True

    def add_work(self):
        artworkid = self.virtual.get_unique_artworkid()
        artistid = self.virtual.get_unique_artistid()
        title = "roman"
        description = "a potrait of roman king"
        creationdate = "1870-05-15"
        medium = "oil in canvas"
        imageurl = "https://www.example.com/roman.jpg"
        artwork = {
            'artworkid': artworkid,
            'artistid': artistid,
            'title': title,
            'description': description,
            'creationdate': creationdate,
            'medium': medium,
            'imageurl': imageurl
        }
        self.createartist()
        query = "insert into artwork values(%s,%s,%s,%s,%s,%s,%s)"
        values = (
            artwork['artworkid'], artwork['title'], artwork['description'], artwork['creationdate'], artwork['medium'],
            artwork['artistid'], artwork['imageurl'])
        cur.execute(query, values)
        cur.fetchall()
        return True

    def createartist(self):
        artistid = self.virtual.get_unique_artistid()
        artworkid = self.virtual.get_unique_artworkid()
        name = "john"
        biography = "italian painter"
        birthdate = "1830-05-11"
        nationality = "italian"
        website = "https://collections.italianacademy.org/"
        contactinformation = "john@gmail.com"
        ca = {
            'artistid': artistid,
            'artworkid': artworkid,
            'name': name,
            'biography': biography,
            'birthdate': birthdate,
            'nationality': nationality,
            'website': website,
            'contactinformation': contactinformation
        }
        query = "insert into artist values(%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (ca['artistid'], ca['artworkid'], ca['name'], ca['biography'], ca['birthdate'], ca['nationality'],
                  ca['website'], ca['contactinformation'])
        cur.execute(query, values)
        cur.fetchall()

if __name__ == '__main__':
    unittest.main()

''' '''