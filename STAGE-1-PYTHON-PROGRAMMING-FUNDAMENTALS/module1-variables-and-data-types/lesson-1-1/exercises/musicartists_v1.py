class MusicArtists:
    
 def __init__(self, artist_name, artist_age, artist_dob):
  self.artist_name = artist_name
  self.artist_age = artist_age
  self.artist_dob = artist_dob
  
drake = MusicArtists ('Drake',40,'Oct 24 1986')

print(drake.artist_name)
print(drake.artist_age)
print(drake.artist_dob)

asap_ferg = MusicArtists ('ASAP Ferg', 38, 'Oct 20 1988')

print(asap_ferg.artist_name)
print(asap_ferg.artist_age)
print(asap_ferg.artist_dob)