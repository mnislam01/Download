import unittest
import download_images
import urllib.request

# The test cases against particular error messages are solved in the downlaod_images file. 
# So, running the test won't find error. Hence, running test module will give errors.



class TestDownloadImages(unittest.TestCase):

    def test_prepare(self):

        self.assertRaises(FileExistsError, download_images.prepare, 'images.txt', 'images')
        self.assertIsInstance(str, download_images.prepare('images.txt', 'images'))
    
    def test_download(self):

        self.assertRaises(urllib.error.ContentTooShortError, download_images.download, r'C:\Users\Nazrul\Desktop\task_two\images', ['https://images.unsplash.com/photo-1504610926078-a1611febcad3', 'https://images.unsplash.com/photo-1536825211030-094de935f680'])
        self.assertRaises(urllib.error.URLError, download_images.download, r'C:\Users\Nazrul\Desktop\task_two\images', ['https://images.unsplash.com/photo-1504610926078-a1611febcad3', 'https://images.unsplash.com/photo-1536825211030-094de935f680'])


