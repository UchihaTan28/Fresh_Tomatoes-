
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


toy_story2= Movie("Toy Story","A story of a boy and his toys that comes to life",
                 "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0%2C0%2C300%2C450",
                 "https://www.youtube.com/watch?v=KYz2wyBy3kc")
print(toy_story.storyline)


kungfu_panda2= Movie("KungFu Panda","When an obese Po the Panda, a kung fu enthusiast, gets selected as the Dragon Warrior, he decides to team up with the Furious Five and destroy the evil forces that threaten the Valley of Peace. ",
                 "http://www.impawards.com/2008/posters/kung_fu_panda.jpg",
                 "https://www.youtube.com/watch?v=PXi3Mv6KMzY")

print(kungfu_panda.storyline)


toy_story2= Movie("Toy Story","A story of a boy and his toys that comes to life",
                 "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0%2C0%2C300%2C450",
                 "https://www.youtube.com/watch?v=KYz2wyBy3kc")
print(toy_story.storyline)


kungfu_panda2= Movie("KungFu Panda","When an obese Po the Panda, a kung fu enthusiast, gets selected as the Dragon Warrior, he decides to team up with the Furious Five and destroy the evil forces that threaten the Valley of Peace. ",
                 "http://www.impawards.com/2008/posters/kung_fu_panda.jpg",
                 "https://www.youtube.com/watch?v=PXi3Mv6KMzY")

print(kungfu_panda.storyline)



movies= [toy_story, kungfu_panda, toy_story2, kungfu_panda2, toy_story2, kungfu_panda2,toy_story2, kungfu_panda2,toy_story2, kungfu_panda2,toy_story2, kungfu_panda2]
fresh_tomatoes.open_movies_page(movies)       
