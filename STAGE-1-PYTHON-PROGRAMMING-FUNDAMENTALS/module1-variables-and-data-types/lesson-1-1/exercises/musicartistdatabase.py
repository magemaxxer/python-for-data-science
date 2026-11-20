class MusicArtist:
    
    artist_record_label = 'Indepedent' # Default record label attribute
    
    def __init__(self,artist_name,artist_dob,artist_age,artist_genre,years_active):
       self.artist_name = artist_name
       self.artist_dob = artist_dob
       self.artist_age = artist_age
       self.artist_genre = artist_genre
       self.artist_years_active = years_active
      
    def display_info(self):
        print(f'Artist Name: {self.artist_name}')
        print(f'Date of Birth: {self.artist_dob}')
        print(f'Age: {self.artist_age}')
        print(f'Artist Genre: {self.artist_genre}')
        print(f'Record Label: {self.artist_record_label}')
        print(f'Years Active: {self.artist_years_active}')
    
    def is_over_30(self):
        if self.artist_age > 30:
            return 'Over 30'
        else:
            return '30 or Under'
        
    def change_genre(self, new_genre):
         self.artist_genre = new_genre
         
    def change_record_label(self, new_record_label):
        self.artist_record_label = new_record_label
        
    def display_career_status(self):
        if self.artist_years_active >= 20:
            return 'Veteran'
        
        else:
            
            return 'Emerging'
            
    
    

        
drake = MusicArtist ('Drake','24th October 1986',40,'RnB',20)    
drake.change_genre('Rap')
drake.change_record_label('YMCMB')
drake.display_info()
print(drake.is_over_30())
print(drake.display_career_status())

asap_ferg = MusicArtist ('A$AP Ferg','20th October 1988',38,'Hip-Hop',19)
asap_ferg.display_info()
print(asap_ferg.is_over_30())
print(asap_ferg.display_career_status())

pharrel = MusicArtist ('Pharrell Williams', '5th April 1973', 53, 'Hip-Hop',34)
pharrel.display_info()
print(pharrel.is_over_30())
print(pharrel.display_career_status())

