
import webbrowser
import fresh_tomatoes

class Movie():
    def __init__(self,name,info,img_url,trailer_youtube_url):
        self.title=name
        self.storyline=info
        self.poster_image_url=img_url
        self.trailer_youtube_url=trailer_youtube_url

    def show_trailer(self):
       webbrowser.open(self.trailer_youtube_url)

toy_story= Movie("Toy Story","A story of a boy and his toys that comes to life",
                 "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0%2C0%2C300%2C450",
                 "https://www.youtube.com/watch?v=KYz2wyBy3kc")

print(toy_story.storyline)

kungfu_panda= Movie("KungFu Panda","When an obese Po the Panda, a kung fu enthusiast, gets selected as the Dragon Warrior, he decides to team up with the Furious Five and destroy the evil forces that threaten the Valley of Peace. ",
                 "http://www.impawards.com/2008/posters/kung_fu_panda.jpg",
                 "https://www.youtube.com/watch?v=PXi3Mv6KMzY")

print(kungfu_panda.storyline)


matrix= Movie("The Matrix","A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.\n",
                 "https://ia.media-imdb.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_QL50_SY1000_CR0,0,665,1000_AL_.jpg",
                 "https://www.youtube.com/watch?v=vKQi3bBA1y8")
print(matrix.storyline)


inception= Movie("Inception","A thief, who steals corporate secrets through the use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.\n",
                 "http://www.impawards.com/2010/posters/inception.jpg",
                 "https://www.youtube.com/watch?v=YoHD9XEInc0")

print(inception.storyline)


the_dark_knight= Movie("The Dark Knight","When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham. The Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.\n",
                 "http://www.impawards.com/2008/posters/dark_knight_ver5_xlg.jpg",
                 "https://www.youtube.com/watch?v=EXeTwQWrcwY")
print(the_dark_knight.storyline)


the_dark_knight_rises= Movie("The Dark Knight Rises","Eight years after the Joker's reign of anarchy, Batman, with the help of the enigmatic Catwoman, is forced from his exile to save Gotham City, now on the edge of total annihilation, from the brutal guerrilla terrorist Bane.\n",
                 "https://ia.media-imdb.com/images/M/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_QL50_.jpg",
                 "https://www.youtube.com/watch?v=GokKUqLcvD8")

print(the_dark_knight_rises.storyline)

interstellar= Movie("Interstellar","A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.\n",
                 "http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB",
                 "https://www.youtube.com/watch?v=3WzHXI5HizQ")

print(interstellar.storyline)

pulp_fiction= Movie("Pulp Fiction","The lives of two mob hitmen, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.\n",
                 "https://ia.media-imdb.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_QL50_SY1000_CR0,0,673,1000_AL_.jpg",
                 "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

print(pulp_fiction.storyline)

avengers_iw= Movie("Avengers: Infintiy War","The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe.\n",
                 "https://ia.media-imdb.com/images/M/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg",
                 "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

print(avengers_iw.storyline)

movies= [toy_story, kungfu_panda, matrix, inception, pulp_fiction, the_dark_knight, the_dark_knight_rises, interstellar, avengers_iw]
fresh_tomatoes.open_movies_page(movies)       
