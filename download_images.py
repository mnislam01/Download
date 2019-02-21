import urllib.request
import os

def prepare(file_name, img_directory):

    '''
    file_name: the name of the text file
    img_directory: name of the folder where pictures will be saved

    
    i)   Create a folder in the scripts' root directory
    ii)  Open the link file and save them in a list
    iii) ASSUME the 'images.txt' and python script will be in the same directory

    return the folder path and the list of links
    '''
    
    
    CURRENT_DIR = os.getcwd()
    IMAGE_DIR_NAME = img_directory
    IMAGE_DIR_PATH = os.path.join(CURRENT_DIR, IMAGE_DIR_NAME)


    TEXT_FILE_PATH = os.path.join(CURRENT_DIR, file_name)

    
    try:
        os.mkdir(IMAGE_DIR_PATH)
    except FileExistsError:
        pass

    
    file = open(TEXT_FILE_PATH)

    links = []

    for link in file:

        # get links without the '\n' character
        links.append(link.split('\n')[0]) 
    

    return IMAGE_DIR_PATH, links
    


def download(path, links):
    '''
    links: a list containing links of images
    path: path of images directory
    
    i)   Download the images from 'links' and save them in 'path'
    ii)  Name the image files in ascending order
    iii) Save them in 'jpg' format

    return nothing
    '''

    os.chdir(path)


    i = 1
    for link in links:
    
        try:
            image_path = 'image(' + str(i) + ').jpg'
            urllib.request.urlretrieve(link, image_path)

        except urllib.error.ContentTooShortError:
            print("Network Interrupted")
        except urllib.error.URLError:
            print("Network not available or url might be broken")
        
        i += 1
        




if __name__ == '__main__':


    #Give the EXACT name of text file
    text_file = 'images.txt'
    #Give a name for image folder
    folder_name = 'images'
    
    # Prepare paths and links
    path, links = prepare(text_file, folder_name)

    # Now downlaod
    download(path, links)

