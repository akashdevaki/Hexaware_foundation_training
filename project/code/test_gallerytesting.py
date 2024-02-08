import unittest
from dao.implementation import VirtualArtGalleryImplementation,flag


class MyTestCase(unittest.TestCase):
    virtual = VirtualArtGalleryImplementation()
    def test_search_gallery(self):
        galleryid=101
        self.assertEqual(self.virtual.search_gallery(galleryid),True)
    def test_removing_gallery(self):
        gallery_id=101
        self.assertEqual(self.virtual.remove_gallery(gallery_id),True)

    def test_update_gallery(self):
        self.assertEqual(self.virtual.update_gallery.flag, True)

    def test_add_gallery(self):
        self.assertEqual(self.virtual.create_new_gallery.flag, True)

if __name__ == '__main__':
    unittest.main()









'''
    def test_update_gallery(self):
        self.assertEqual(self.virtual.update_gallery.flag,True)
    def test_add_gallery(self):

        self.assertEqual(self.virtual.create_new_gallery.flag, True)'''