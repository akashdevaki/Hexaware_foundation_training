import unittest
from dao.implementation import VirtualArtGalleryImplementation,flag
import mysql.connector
from mysql.connector import Error

con=mysql.connector.connect(host="localhost",
                            user="root",
                            password="root",
                            port="3306",
                            database="virtualartgallery")
cur=con.cursor()
class MyTestCase(unittest.TestCase):
    virtual = VirtualArtGalleryImplementation()
    def test_search_gallery(self):
        galleryid=101
        self.assertEqual(self.virtual.search_gallery(galleryid),True)
    def test_removing_gallery(self):
        gallery_id=101
        self.assertEqual(self.virtual.remove_gallery(gallery_id),True)
    def test_update_gallery(self):
        result=self.update_gallery()
        self.assertEqual(result, True)
    def test_add_gallery(self):

        result=self.add_gallery()
        self.assertEqual(result, True)

    def update_gallery(self):
        name = 'Artistic Haven'
        description = 'A contemporary art gallery'
        location = '123 Main Street, Cityville'
        openinghours = 'Mon-Fri: 10 am - 6 pm, Sat-Sun: 12 pm - 4 pm'
        query = "update gallery set name=%s,description=%s,location=%s,openinghours=%s where galleryid=101"
        cur.execute(query, (name, description, location, openinghours, ))
        cur.fetchall()
        return True

    def add_gallery(self):
        galleryid = self.virtual.get_unique_gallery_id();
        name = "art gallery"
        description = "a diverse collection of arts from various countries"
        location = 'kolkata'
        curator = 2
        openinghours = "mon-thurs 9am-4pm sat-sun 10am-6pm"
        new = {
            'galleryid': galleryid,
            'name': name,
            'description': description,
            'location': location,
            'curator': curator,
            'openinghours': openinghours
        }
        query = "insert into gallery values(%s,%s,%s,%s,%s,%s)"
        values = (
        new['galleryid'], new['name'], new['description'], new['location'], new['curator'], new['openinghours'])
        cur.execute(query, values)
        cur.fetchall()
        return True
if __name__ == '__main__':
    unittest.main()









'''
    def test_update_gallery(self):
        self.assertEqual(self.virtual.update_gallery.flag,True)
    def test_add_gallery(self):

        self.assertEqual(self.virtual.create_new_gallery.flag, True)'''