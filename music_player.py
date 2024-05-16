
class Musicplayer:

  def __init__(self):
    #list of songlist
    self.songlist=[]
    #list for playlist
    self.playlist=[]
    #dict will show add to song to playlist
    self.addsongtoPlaylist={}
    self.userinput_rating={}
       
     
    #method to create playlist
  def create_playlist(self,name):
    if name not in self.playlist:
      self.playlist.append(name)
      print("successfully Playlist creation")
 
    return (self.playlist)
   

    #method to add song to playlist
  def add_song_playlist(self,playlist,song):

    for i in range(len(self.playlist)):
          
      if self.playlist[i].lower()=="sad_mode":
        self.addsongtoPlaylist={self.playlist[i]:song}
      elif self.playlist[i].lower()=="happy_mode":
        self.addsongtoPlaylist={self.playlist[i]:song}
      elif self.playlist[i].lower()=="party_mode":
        self.addsongtoPlaylist={self.playlist[i]:song}
     
      return self.addsongtoPlaylist
    # method to create songlist
  def  create_songlist(self,song):
    if song not in self.songlist:
      self.songlist.append(song)
      print("song is added in list")
    return self.songlist

    # method to search song from list
  def search_song(self,song):
    for i in range(len(self.songlist)):
      if song  in self.songlist:
            
        print("song is in our list")
        return self.songlist[i]
      else:
          return "sorry we do not have your song"
         
    #method to search playlist
  def  search_playlist(self,nameofplaylist):
    for i in range(len(self.playlist)):
      if nameofplaylist in self.playlist:
        print("This playlistname is there")
        return self.playlist[i]
      else:
        return "not in playlist"
    #method to add user rating of song
  def  indidiual_user_rating(self,song,rate):
    if song in self.songlist:
      self.userinput_rating={song:rate}
      print("rating of user1 of song")
      return  self.userinput_rating
          
    #method to calculate average rating of particular song
  def avg_rating(self,*rate):
    avg=sum(rate)/len(rate)
    return avg
#creating object of class musicplayer        
user1=Musicplayer()
print("Playlist is " + str(user1.create_playlist("happy_mode"))+"\n")
print("Playlist is " + str(user1.create_playlist("sad_mode"))+"\n")
print("added song to playlist " +str(user1.add_song_playlist("sad_mode","someone you loved"))+"\n")
print(str(user1.search_playlist("sad_mode"))+"\n")
print(str(user1.create_songlist("parindey"))+"\n")
print(str(user1.search_song("parindey"))+"\n")
print(str(user1.indidiual_user_rating("parindey",1))+"\n")
#creating another object of music player class
user2=Musicplayer()
print("Playlist is  "+str(user2.create_playlist("happy_mode"))+"\n")
print("Playlist is  "+str(user2.create_playlist("sad_mode"))+"\n")
print(str(user2.add_song_playlist("sad_mode","someone you loved"))+"\n")
print(str(user2.search_playlist("sad_mode"))+"\n")
print(str(user2.create_songlist("parindey"))+"\n")
print(str(user2.search_song("parindey"))+"\n")
print(str(user2.indidiual_user_rating("parindey",4))+"\n")
#creating rating object of music player class
rating=Musicplayer()
print("averge rating is " + str(rating.avg_rating(2,3,4,5)))










       
       
          
       
     
        

         
        
       
        
       
         

   


        