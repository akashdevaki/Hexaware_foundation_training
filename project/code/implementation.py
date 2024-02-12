

import flag as flag

'''from dao import test_mytesting
from dao.test_mytesting import MyTestCase'''

from abc import ABC,abstractmethod
class IVirtualArtGallery(ABC):

    # Artwork Management
    @abstractmethod
    def add_artwork(self):
        pass

    @abstractmethod
    def update_artwork(self, artwork):
        pass

    @abstractmethod
    def remove_artwork(self, artwork_id):
        pass

    @abstractmethod
    def get_artwork_by_id(self, artwork_id):
        pass

    @abstractmethod
    def search_artworks(self, keyword):
        pass

    @abstractmethod
    def add_artwork_to_favorite(self, user_id, artwork_id):
        pass

    @abstractmethod
    def remove_artwork_from_favorite(self, user_id, artwork_id):
        pass

    @abstractmethod
    def get_user_favorite_artworks(self, user_id):
        pass
flag=0

import mysql.connector
from mysql.connector import Error

con=mysql.connector.connect(host="localhost",
                            user="root",
                            password="root",
                            port="3306",
                            database="virtualartgallery")
cur=con.cursor()

from myExceptions import *
class VirtualArtGalleryImplementation(IVirtualArtGallery,ArtWorkNotFoundException,UserNotFoundException):
    flag=0

    #test1=MyTestCase()
    def createartist(self):
        artistid = self.get_unique_artistid()
        artworkid = self.get_unique_artworkid()
        name = input("enter the artist name")
        biography = input("enter artist biography")
        birthdate = input("enter the bithdate of artist")
        nationality = input("enter the nationality of artist")
        website = input("enter the url of website")
        contactinformation = input("enter the gmail of artist")
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
        con.commit()


    def add_artwork(self):
        flag=0
        try:
            artworkid = self.get_unique_artworkid()
            artistid = self.get_unique_artistid()
            title= input("enter the title of the artwork")
            description = input("enter the description")
            creationdate = input("enter the creation date")
            medium = input("enter the medium")
            imageurl=input("enter the imageurl")
            artwork = {
                'artworkid': artworkid,
                'artistid': artistid,
                'title':title,
                'description': description,
                'creationdate': creationdate,
                'medium': medium,
                'imageurl':imageurl
            }
            self.createartist()
            v.add_artwork_to_db(artwork)
            con.commit()
            flag=1
        finally:
            con.commit()
        return flag

    def add_artwork_to_db(self,artwork):

        query = "insert into artwork values(%s,%s,%s,%s,%s,%s,%s)"
        values = (
        artwork['artworkid'], artwork['title'], artwork['description'], artwork['creationdate'],artwork['medium'],
        artwork['artistid'],artwork['imageurl'])
        cur.execute(query, values)
        cur.fetchall()
        con.commit()
        print("artwork was added Successfully")
        return True

    def update_artwork(self,artworkid):
        flag = 0
        try:
            query="select * from artwork where artworkid= %s"
            cur.execute(query,(artworkid,))
            output=cur.fetchall()
            if not output:
                raise ArtWorkNotFoundException(f"Error: artwork {artworkid} not found")
                return False
            print("select the below options to update:")
            print("1.title")
            print("2.description")
            print("3.creationdate")
            print("4.medium")
            choice = input("enter the option you want to change")
            if choice == "1":
                title = input("enter the title")
                query = "update artwork set title=%s where artworkid= %s"
                cur.execute(query, (title,artworkid,))
                cur.fetchone()
                con.commit()
                print("Artwork updated successfully")
                return True
            elif choice == "2":
                description = input("enter the description")
                query = "update artwork set description=%s where artworkid= %s"
                cur.execute(query, (description,artworkid,))
                cur.fetchone()
                con.commit()
                print("Artwork updated successfully")
                return True
            elif choice == "3":
                creationdate = input("enter the creationdate")
                query = "update artwork set creationdate=%s where artworkid= %s"
                cur.execute(query, (creationdate,artworkid,))
                cur.fetchone()
                con.commit()
                print("Artwork updated successfully")
                return True
            elif choice == "4":
                medium = input("enter the medium")
                query = "update artwork set medium=%s where artworkid= %s"
                cur.execute(query, (medium,artworkid,))
                cur.fetchone()
                con.commit()
                print("Artwork updated successfully")
                return True
            else:
                print("invalid choose from above option")
            query = "select * from artwork where artworkid=%s"
            cur.execute(query,(artworkid,))
            output = cur.fetchone

            con.commit()
        except ArtWorkNotFoundException as e:
            print(f"Error: {e}")
        return False

    def remove_artwork(self, artworkid):
        flag=0
        try:
            query = "select * from artwork where artworkid=%s"
            cur.execute(query, (artworkid,))
            output = cur.fetchone()
            query = "delete from artwork where artworkid=%s"
            cur.execute(query, (artworkid,))
            query1="delete from artist where artworkid=%s"
            cur.execute(query1, (artworkid,))
            if not output:
                raise ArtWorkNotFoundException(f"Error: artwork {artworkid} not found")
            for i in output:
                print(i)
            print(f"deleted the {artworkid} from database successfully")
            con.commit()
            flag=1
        except ArtWorkNotFoundException as e:
            print(f"Error: {e}")



        return flag

    def get_artwork_by_id(self, artworkid):
        try:
            query = "select * from artwork where artworkid=%s"
            cur.execute(query, (artworkid,))
            output=cur.fetchall()
            print(cur.fetchall())
            con.commit()
            if not output:
                raise ArtWorkNotFoundException(f"Error:artworkid {artworkid} not found ")
            for i in output:
                print(i)
        except ArtWorkNotFoundException as e:
            print(f"{e}")


        return artworkid

    def search_artworks(self, title):
        flag=0
        try:
            query = "select * from artwork where title=%s"
            cur.execute(query, (title,))
            output=cur.fetchall()
            if not output:
                raise ArtWorkNotFoundException(f"Error: artwork {title} not found")
            for i in output:
                print(i)

            flag=1
            return True

        except ArtWorkNotFoundException as e:
            print(f"{e}")
        return flag








    def add_artwork_to_favorite(self, userid, artworkid):
        try:
            query="select * from UserFavoriteArtwork where userid=%s"
            cur.execute(query,(userid,))
            output=cur.fetchall()
            if not output:
                raise UserNotFoundException(f"Error {userid} userid not found")

            self.userid=userid
            self.artworkid=artworkid


            fav = {
                'userid': userid,
                'artworkid': artworkid
            }
            query = "insert into UserFavoriteArtwork values(%s,%s)"
            values = (fav['userid'], fav['artworkid'])
            cur.execute(query, values)
            output = cur.fetchall()
            for i in output:
                print(i)
            print(output, " successfully inserted into database")
            con.commit()
        except UserNotFoundException as e:
            print(f"Error: {e}")

        return True

    def remove_artwork_from_favorite(self, userid, artworkid):
        try:
            query="select * from UserFavoriteArtwork where userid=%s"
            cur.execute(query,(userid,))
            output=cur.fetchall()
            if not output:
                raise UserNotFoundException(f"Error: {userid} userid not found")
            self.get_all_users()
            self.userid = userid
            self.artworkid = artworkid
            self.get_all_artwork()

            query = "delete from UserFavoriteArtwork where userid=%s and artworkid=%s"
            cur.execute(query, (userid, artworkid,))
            print("successfully deleted from the database")
            con.commit()
        except UserNotFoundException as e:
            print(f"{e}")

        return True

    def get_user_favorite_artworks(self, userid):
        try:

            self.get_all_users()
            userid = input("enter the userid")
            query = "select artworkid from UserFavoriteArtwork where userid=%s "
            cur.execute(query, (userid,))
            output = cur.fetchall()
            if not output:
                raise UserNotFoundException(f"Error: {userid} userid not found")
            query="select * from artwork join UserFavoriteArtwork on UserFavoriteArtwork.artworkid=artwork.artworkid where userid=%s"
            cur.execute(query,(userid,))
            res=cur.fetchall()
            for i in res:
                print(i)
            con.commit()
        except UserNotFoundException as e:
            print(f" {e}")

        return userid
    def all_artwork(self):
        query="select * from artwork"
        cur.execute(query)
        return cur.fetchall()
    def get_unique_artworkid(self):
        return len(self.all_artwork())+1
    def all_artist(self):
        query="select * from artist"
        cur.execute(query)
        return cur.fetchall()
    def get_unique_artistid(self):
        return len(self.all_artist())+1

    def get_all_users(self):
        query="select * from user"
        cur.execute(query)
        output=cur.fetchall()
        for i in output:
            print(i)

    def get_all_artwork(self):
        query="select * from artwork"
        cur.execute(query)
        output= cur.fetchall()
        for i in output:
            print(i)

    def feedback(self):
        self.get_gallaries()
        galleryid=input("enter the galleryid")
        userid=input("enter the userid")
        description=input("enter the feedback")
        query="insert into feedback values(%s,%s,%s)"
        cur.execute(query,(galleryid,userid,description))
        output=cur.fetchall()
        con.commit()
        print("Thanks for your feedback")

    def create_new_gallery(self):
        flag=0
        try:
            galleryid=self.get_unique_gallery_id();
            name=input("enter the gallery name")
            description=input("enter the description")
            location=input("enter the location")
            curator=input("enter the artistid or curator")
            openinghours=input("enter the opening hours")
            new={
                'galleryid':galleryid,
                'name':name,
                'description':description,
                'location':location,
                'curator':curator,
                'openinghours':openinghours
            }
            query="insert into gallery values(%s,%s,%s,%s,%s,%s)"
            values=(new['galleryid'],new['name'],new['description'],new['location'],new['curator'],new['openinghours'])
            cur.execute(query,values)
            output=cur.fetchall()
            for i in output:
                print(i)
            return True
        finally:
            con.commit()

    def update_gallery(self):
        self.get_all_gallaries()
        galleryid=input("enter the gallery id")
        try:
            query="select * from gallery where galleryid=%s"
            cur.execute(query,(galleryid,))
            output=cur.fetchall()
            if not output:
                raise GalleryNotFoundException(f"Error: artwork {galleryid} not found")
            name = input("enter the Name")
            description = input("enter the description")
            location = input("enter the location")
            openinghours = input("enter the openinghours")
            query = "update gallery set name=%s,description=%s,location=%s,openinghours=%s where galleryid= %s"
            cur.execute(query, (name,description,location,openinghours, galleryid,))
            output=cur.fetchall()
            for i in output:
                print(i)
            print("gallery updated successfully")
            '''print("select the below options to update:")
            print("1.Name")
            print("2.description")
            print("3.location")
            print("4.curator")
            print("5.openinghours")
            choice = input("enter the option you want to change")
            if choice == "1":
                name = input("enter the Name")
                query = "update gallery set name=%s where galleryid= %s"
                cur.execute(query, (name,galleryid,))
                cur.fetchone()
                con.commit()
                print("successfully updated gallery name")
            elif choice == "2":
                description = input("enter the description")
                query = "update gallery set description=%s where galleryid= %s"
                cur.execute(query, (description,galleryid,))
                cur.fetchone()
                con.commit()
                print("successfully updated gallery description")
            elif choice == "3":
                location = input("enter the location")
                query = "update gallery set location=%s where galleryid= %s"
                cur.execute(query, (location,galleryid,))
                cur.fetchone()
                con.commit()
                print("successfully updated gallery location")
            elif choice == "4":
                curator = input("enter the curator")
                query = "update gallery set curator=%s where galleryid= %s"
                cur.execute(query, (curator,galleryid,))
                cur.fetchone()
                con.commit()
                print("successfully updated gallery curator")
            elif choice =="5":
                openinghours = input("enter the openinghours")
                query = "update gallery set openinghours=%s where galleryid= %s"
                cur.execute(query, (openinghours, galleryid,))
                cur.fetchone()
                con.commit()
                print("successfully updated gallery openinghours")
            else:
                print("invalid choose from above option")'''
            '''query = "select * from gallery where galleryid=%s"
            cur.execute(query,(galleryid,))
            output=cur.fetchone'''
            con.commit()
            return True

        except GalleryNotFoundException as e:
            print(f"Error: {e}")




    def remove_gallery(self,galleryid):
        self.get_all_gallaries()

        flag=0
        try:
            query="select * from gallery where galleryid=%s"
            cur.execute(query,(galleryid,))
            output = cur.fetchall()
            if not output:
                print(f"Error: artwork {galleryid} not found")
            query = "delete from gallery where galleryid=%s"
            cur.execute(query, (galleryid,))
            print(f"deleted the {galleryid} from database successfully")
            con.commit()
            flag=1
            return True
        finally:
            con.commit()

    def search_gallery(self,galleryid):
        flag=0
        self.get_all_gallaries()
        #galleryid=input("enter the galleryid")
        try:
            query = "select * from gallery where galleryid=%s"
            cur.execute(query, (galleryid,))
            output=cur.fetchall()
            if not output:
                print(f"Error: artwork {galleryid} not found")
            for i in output:
                print(i)

            flag=1
            return True
        finally:
            con.commit()

    def get_all_gallaries(self):
        query="select * from gallery"
        cur.execute(query)
        return cur.fetchall()

    def get_unique_gallery_id(self):
        return len(self.get_all_gallaries())+1
    def get_gallaries(self):
        query="select * from gallery"
        cur.execute(query)
        output=cur.fetchall()
        for i in output:
            print(i)

# Package: dao

#from util import DBConnection


v=VirtualArtGalleryImplementation()

'''query="select * from artwork"
cur.execute(query)
output=cur.fetchall()
for i in output:
    print(i)'''