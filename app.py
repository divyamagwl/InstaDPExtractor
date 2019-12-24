import requests
from bs4 import BeautifulSoup as bs
import os.path
 
print("\nWelcome to Instagram Profile Picture Extractor!!!")
insta_url = "https://www.instagram.com"
insta_username = input("\nEnter Instagram Username : ")

insta_user_id = requests.get(str(insta_url) + "/" + str(insta_username))

if insta_user_id.ok:
    html_page = insta_user_id.text
    soup = bs(html_page, 'lxml')
    soup = soup.text

    start_index= soup.find('profile_pic_url_hd') + 21
    remaining_text = soup[start_index:]
    end_index = remaining_text.find("requested_by_viewer") - 3
    unusable_url = remaining_text[:end_index]
    string_url = unusable_url.replace(r"\u0026","&")
    
    print("\nInstagram Profile Picture Link - " + string_url)
    print("\nDowloading.....")

    while True:
        filename = str(insta_username) + ".jpg"
        file_exists = os.path.isfile(filename)

        if not file_exists:
            with open(filename, "wb+") as f:
                insta_user_id = requests.get(string_url, stream = True)
                if not insta_user_id.ok:
                    print("There occured an error in downloading the image")
                else:
                    for content in insta_user_id.iter_content(1024):
                        if not content:
                            print("There occured an error in downloading the image")
                            break
                        f.write(content)
                    print("\nDownload completed.....")
            print("\nThank you for using the application")

        else:
            print("\nThere already exists an image for the given username\nDo you want to:")
            print("1. Replace the image")
            print("2. Quit the application")
            response = int(input("Enter 1 or 2 : "))
            if(response == 1):
                with open(filename, "wb+") as f:
                    insta_user_id = requests.get(string_url, stream = True)
                    if not insta_user_id.ok:
                        print("There occured an error in downloading the image")
                    else:
                        for content in insta_user_id.iter_content(1024):
                            if not content:
                                print("There occured an error in downloading the image")
                                break
                            f.write(content)
                        print("\nDownload completed.....")
                print("\nThank you for using the application")

            elif(response == 2):
                print("\nThank you for using the application")
                break
        break

else:
    print("\nUsername does not exist")
    print("Thank you for using the application")