class Artist:
    def __init__(self, artistid, name,artworkid,biography,birthdate,nationality,website,ContactInformation):
        self.__artistid = artistid
        self.__name = name
        self.__artworkid=artworkid
        self.__biography=biography
        self.__birthdate=birthdate
        self.__nationality=nationality
        self.__website=website
        self.__ContactInformation=ContactInformation

    @property
    def getartist_id(self):
        return self.__artistid
    @property
    def getname(self):
        return self.__name
    @property
    def getartworkid(self):
        return self.__artworkid
    @property
    def getbiography(self):
        return self.__biography
    @property
    def getbirthdate(self):
        return self.__birthdate
    @property
    def getnationality(self):
        return self.__nationality
    @property
    def getwebsite(self):
        return self.__website
    @property
    def getContactInformation(self):
        return self.__ContactInformation

    @getartist_id.setter
    def setartist_id(self,artistid):
       self.__artistid=artistid
    @getname.setter
    def setname(self,name):
        self.__name=name
    @getartworkid.setter
    def setartworkid(self,artworkid):
        self.__artworkid=artworkid
    @getbiography.setter
    def setbiography(self,biography):
        self.__biography=biography
    @getbirthdate.setter
    def setbirthdate(self,birthdate):
        self.__birthdate=birthdate
    @getnationality.setter
    def setnationality(self,nationality):
        self.__nationality=nationality
    @getwebsite.setter
    def setwebsite(self,website):
        self.__website=website
    @getContactInformation.setter
    def setContactInformation(self,ContactInformation):
         self.__ContactInformation=ContactInformation

class Artwork:
    def __int__(self,artworkid,title,description,creationdate,medium,artisid,imageurl):
        self.__artworkid = artworkid
        self.__title = title
        self.__description = description
        self.__creationdate = creationdate
        self.__medium = medium
        self.__image_url = imageurl

    @property
    def getartworkid(self):
        return self.__artwork_id
    @property
    def gettitle(self):
        return self.__title
    @property
    def getdescription(self):
        return self.__description
    @property
    def getcreationdate(self):
        return self.__creation_date
    @property
    def getmedium(self):
        return self.__medium
    @property
    def getimageurl(self):
        return self.__image_url

    @getartworkid.setter
    def setartworkid(self, artworkid):
        self.__artworkid = artworkid
    @gettitle.setter
    def settitle(self, title):
        self.__title = title
    @getdescription.setter
    def setdescription(self, description):
        self.__description= description
    @getcreationdate.setter
    def setcreationdate(self, creationdate):
        self.__creationdate = creationdate
    @getmedium.setter
    def setmedium(self, medium):
        self.__medium = medium
    @getimageurl.setter
    def setimageurl(self, imageurl):
        self.__imageurl = imageurl

class user:
    def __int__(self,userid,username,password,email,firstname,lastname,dateofbirth,profilepicture):
        self.__userid=userid
        self.__username=username
        self.__password=password
        self.__email=email
        self.__firstname=firstname
        self.__last=lastname
        self.dateofbirth=dateofbirth
        self.profilepicture=profilepicture

    @property
    def getuserid(self):
        return self.__userid
    @property
    def getusername(self):
        return self.__username
    @property
    def getpassword(self):
        return self.__password
    @property
    def getemail(self):
        return self.__email
    @property
    def getfirstname(self):
        return self.__firstname
    @property
    def getlastname(self):
        return self.__lastname

    @property
    def getdateofbirth(self):
        return self.__dateofbirth
    @property
    def getprofilepicture(self):
        return self.__profilepicture

    @getuserid.setter
    def setuserid(self, userid):
        self.__usertid = userid
    @getusername.setter
    def setusername(self, username):
        self.__username = username
    @getpassword.setter
    def setpassword(self, password):
        self.__password = password
    @getemail.setter
    def setemail(self, email):
        self.__email = email
    @getfirstname.setter
    def setfirstname(self, firstname):
        self.__firstname = firstname
    @getlastname.setter
    def setlastname(self, lastname):
        self.__lastname = lastname
    @getdateofbirth.setter
    def setdateofbirth(self, dateofbirth):
        self.__dateofbirth = dateofbirth

    @getprofilepicture.setter
    def setprofilepicture(self, profilepicture):
        self.__profilepicture = profilepicture

class gallery:
    def __int__(self,galleryid,name,description,location,curator,openinghours):
        self.__galleryid=galleryid
        self.__name=name
        self.__description=description
        self.__location=location
        self.__curator=curator
        self.__openinghours=openinghours

    @property
    def getgalleryid(self):
        return self.__galleryid
    @property
    def getname(self):
        return self.__name
    @property
    def getdescription(self):
        return self.__description
    @property
    def getlocation(self):
        return self.__location
    @property
    def getcurator(self):
        return self.__curator
    @property
    def getopeninghours(self):
        return self.__openinghours

    @getgalleryid.setter
    def setgalleryid(self, galleryid):
        self.__galleryid = galleryid
    @getname.setter
    def setname(self, name):
        self.__name= name
    @getdescription.setter
    def setdescription(self, description):
        self.__description = description
    @getlocation.setter
    def setlocation(self, location):
        self.__location = location
    @getcurator.setter
    def setcurator(self, curator):
        self.__curator = curator
    @getopeninghours.setter
    def setopeninghours(self, openinghours):
        self.__openinghours = openinghours



from dao.implementation import VirtualArtGalleryImplementation

virtual=VirtualArtGalleryImplementation()
print(virtual.flag)

