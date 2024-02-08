
import unittest

from dao.implementation import VirtualArtGalleryImplementation


class MyTestCase(unittest.TestCase):


    virtual=VirtualArtGalleryImplementation()

    def test_searching_artwork(self):
        flag=2
        self.assertEqual(self.virtual.search_artworks(flag),True)
    def test_removing_artwork(self):
        flag=1
        self.assertEqual(self.virtual.remove_artwork(flag),True)
    def test_update_artwork(self):

        self.assertEqual(self.virtual.update_artwork.flag,True)
    def test_add_artwork(self):

        self.assertEqual(self.virtual.add_artwork.flag, True)




if __name__ == '__main__':
    unittest.main()

