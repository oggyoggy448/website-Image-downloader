"""
This project has been made to download all the images from the given website.
"""
import sys

import requests
from bs4 import BeautifulSoup


def get_valid_url():
    """
    get a valid url from a user.
    A valid url is a url which starts with http
    :return:  url: str
    """

    name = input("Enter a website name:").strip()
    while 1:
        if name.startswith("http"):
            print("URL is seen to be fine.Please wait...")
            return name
        else:
            print("Invalid website name.\nWebsite name always starts with http\ne.g"
                  "\nhttp://www.google.com   https://www.crummy.com")
            continue


def get_html_content(web_name: str):
    """
    This function is to get the html content from the website
    :param web_name: str
    :return: html_content
    """
    try:
        return requests.get(web_name).text
    except:
        print("There is an error while connecting with this website. Please check that following options"
              "\nDoes you network/internet allows you to connect with this website if not use vpn\n"
              "Is your network working properly?"
              "\nIs your network slow?\n"
              "Try the following options and try again ")
        print("*" * 100)
        sys.exit()


def get_all_images(html_c, web_name: str):
    """
    get all the images from a website
    :param web_name: str
    :param html_c: str

    :return: images
    """
    try:
        soup = BeautifulSoup(html_c, "html.parser")
        all_images = []
        for img in soup.find_all("img"):
            image = img.get("src")
            if image.startswith("//"):
                all_images.append(web_name + image[1:])
            elif image.startswith("/"):
                all_images.append(web_name + image)
        return all_images
    except:
        print("An error has occurred.The following options can be helpful \n"
              "Check your internet\n"
              "check that your internet is allowing to access the given website\n"
              "Use vpn if your internet is not allowing to access the given website")
        print("*" * 100)
        sys.exit()


def store_images_in_file(imgs_link: list):
    """
    This method is to store all the images in a file
    :param imgs_link: list
    :return: None
    """
    try:
        store_image = open("images.txt", "w")
        store_image.write("\n".join(imgs_link))
        store_image.close()
        print("All images links have been stored in a file")
        print("*" * 100)
    except:
        print("There is some error while writing data in a file\nplease re-run file again")
        print("*" * 100)
        exit()


def download_image(img_link):
    """
    This method is to download all the image
    :param img_link: list
    :return: count image:int
    """
    count_image = 0
    for img in img_link:
        file_name = img.split("/")[-1]
        open(file_name, "wb").write(requests.get(img, allow_redirects=True).content)
        print(file_name, "has been downloaded")
        count_image += 1
        print("*" * 100)
    return count_image


if __name__ == '__main__':
    while 1:
        # get url from the user
        url = get_valid_url()
        # to display the url entered by user
        # print(url)

        # get the html content
        html_content = get_html_content(web_name=url)
        print("All html has been achieved.Please wait for further processing...")
        print("*" * 100)
        # display all the html
        # print(html_content)

        # get all the images from a website
        images = get_all_images(html_content, url)
        print("All images URL have been achieved.Please wait for further processing.....")
        print("*" * 100)
        # print(images)

        # store all images links in a file
        store_images_in_file(images)

        # download all the images
        total_downloaded_images = download_image(img_link=images)
        print("Total downloaded images are:", total_downloaded_images)

        if input("Do you want to download images from other website?").strip().lower() == "yes":
            continue
        else:
            break
