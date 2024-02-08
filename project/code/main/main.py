from dao.implementation import VirtualArtGalleryImplementation
from dao import test_mytesting


crime=VirtualArtGalleryImplementation()
def main():
    crime=VirtualArtGalleryImplementation()

    while True:
        print("choose the options from given below")
        print("1.add_artwork")
        print("2.update_Artwork")
        print("3.remove artwork")
        print("4.get artwork by id")
        print("5.search artwork")
        print("6.add artwork to favorite")
        print("7.remove artwork from favorites")
        print("8.get user favorite artwork")
        print("9.exit")
        choice=input("enter the option you have choosen")
        if choice=="1":
            crime.add_artwork()

        elif choice=="2":
            artworkid=input("enter the artworkid")
            crime.update_artwork(artworkid)
        elif choice=="3":
            artworkid = input("enter the artwork_id")
            crime.remove_artwork(artworkid)
        elif choice=="4":
            artworkid=input("enter the artwork_id")
            crime.get_artwork_by_id(artworkid)
        elif choice=="5":
            artworkid=input("enter the artwork_id")
            crime.search_artworks(artworkid)

        elif choice=="6":
            crime.get_all_users()
            userid = input("enter the userid")
            crime.get_all_artwork()
            artworkid = input("enter the artworkid")

            crime.add_artwork_to_favorite(userid,artworkid)
        elif choice=="7":
            crime.get_all_users()
            userid = input("enter the userid")
            crime.get_all_artwork()
            artworkid = input("enter the artwork_id")
            crime.remove_artwork_from_favorite(userid,artworkid)
        elif choice=="8":
            userid = ("enter the userid")
            crime.get_user_favorite_artworks(userid)
        elif choice=="9":
            print("exiting the system \n Thank you")
            break
        else:
            print("invalid option choose from above given options")


main()


'''crime.search_gallery(101)
crime.remove_gallery(101)'''

