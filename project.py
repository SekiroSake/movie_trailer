import movies
import adrian

# Create Director instances
francis_lawrence = movies.Person("Francis Lawrence", "Mar, 26", "http://ia.media-imdb.com/images/M/MV5BMTI4Mjc4MTMzNF5BMl5BanBnXkFtZTYwNjkzNzc4._V1_UY98_CR31,0,67,98_AL_.jpg")
wooping_yuen = movies.Person("WooPing Yuen", "Jan, 1", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Yuen_Woo_Ping.jpg/220px-Yuen_Woo_Ping.jpg")
don_hall = movies.Person("Don Hall", None, "http://ia.media-imdb.com/images/M/MV5BMTc4NDg2MzkxOV5BMl5BanBnXkFtZTgwNTA4MDQwMDE@._V1_UY317_CR131,0,214,317_AL_.jpg")
chris_williams = movies.Person("Chris Williams", None,"http://ia.media-imdb.com/images/M/MV5BMTcwMDM4NzM3OF5BMl5BanBnXkFtZTcwOTYwNzkyMg@@._V1_UY317_CR37,0,214,317_AL_.jpg")

# Create Actor instances
jennifer_lawrence = movies.Person("Jennifer Lawrence", "Aug,15", "http://ia.media-imdb.com/images/M/MV5BMTM4OTY2MDY1M15BMl5BanBnXkFtZTcwNDYyNDM3NA@@._V1_UX32_CR0,0,32,44_AL_.jpg")
josh_hutcherson = movies.Person("Josh Hutcherson", "Oct, 12", "http://ia.media-imdb.com/images/M/MV5BMTI4OTk0MjQ1OV5BMl5BanBnXkFtZTcwNTE3NjM3Mw@@._V1_UX32_CR0,0,32,44_AL_.jpg")
liam_hemsworth = movies.Person("Liam Hemsworth", "Jan, 13", "http://ia.media-imdb.com/images/M/MV5BMTQ5ODI0MDc4M15BMl5BanBnXkFtZTgwNTM5MDk3MTE@._V1_UX32_CR0,0,32,44_AL_.jpg")
donnie_yen = movies.Person("Donnie Yen", "Jul, 27", "http://ia.media-imdb.com/images/M/MV5BMTg0NTI0NDkzOF5BMl5BanBnXkFtZTcwMjYwMTIwNw@@._V1_UX32_CR0,0,32,44_AL_.jpg")
michelle_yeoh = movies.Person("Michelle Yeoh", "Aug, 6", "http://content6.flixster.com/rtactor/40/37/40372_pro.jpg")
harry_shum_jr = movies.Person("Harry Shum Jr.", "Apr, 28", "http://ia.media-imdb.com/images/M/MV5BMTc4ODM3OTY0NV5BMl5BanBnXkFtZTgwODk5MDY5MDE@._V1_UX32_CR0,0,32,44_AL_.jpg")
ryan_potter = movies.Person("Ryan Potter", None, "http://ia.media-imdb.com/images/M/MV5BMTQwMzY3NTA2N15BMl5BanBnXkFtZTcwMDY5MTA0OQ@@._V1_UX32_CR0,0,32,44_AL_.jpg")
scott_adsit = movies.Person("Scott Adsit", "Nov, 26", "http://ia.media-imdb.com/images/M/MV5BODM3MDI2OTA0OF5BMl5BanBnXkFtZTcwMDM0MzkzMg@@._V1_UX32_CR0,0,32,44_AL_.jpg")
jamie_chung = movies.Person("Jamie Chung", "Apr, 10", "http://ia.media-imdb.com/images/M/MV5BMjE4MzUxODgwOV5BMl5BanBnXkFtZTgwNjc2MDgyMDE@._V1_UX32_CR0,0,32,44_AL_.jpg")
hugh_bonneville = movies.Person("Hugh Bonneville", "Nov, 10", "http://content7.flixster.com/rtactor/44/18/44181_pro.jpg")
sally_hawkins = movies.Person("Sally Hawkins", "Apr, 27", None)

# Create Movie instances
the_hunger_games = movies.Movie(
    "The Hunger Games: Mockingjay - Part 2",
    ["Drama", "Adventure"],
    7.1,
    francis_lawrence,
    [jennifer_lawrence, josh_hutcherson,  liam_hemsworth],
    "http://ia.media-imdb.com/images/M/MV5BNjQzNDI2NTU1Ml5BMl5BanBnXkFtZTgwNTAyMDQ5NjE@._V1_SX214_AL_.jpg",
    "https://www.youtube.com/watch?v=KmYNkasYthg"
)
the_green_legend = movies.Movie(
    "Crouching Tiger, Hidden Dragon: The Green Legend",
    ["Drama", "Action & Adventure"],
    None,
    wooping_yuen,
    [donnie_yen,  michelle_yeoh, harry_shum_jr],
    "http://ia.media-imdb.com/images/M/MV5BMTA2MzM5NTk4NTBeQTJeQWpwZ15BbWU4MDk0NjgyNDcx._V1_SX214_AL_.jpg",
    "https://www.youtube.com/watch?v=WdhvxJZDqzU"
)
bighero = movies.Movie(
    "Big Hero 6",
    ["Animation", "Action","Adventure"],
    7.9,
    don_hall,
    [ryan_potter, scott_adsit, jamie_chung],
    "http://ia.media-imdb.com/images/M/MV5BMjI4MTIzODU2NV5BMl5BanBnXkFtZTgwMjE0NDAwMjE@._V1_SY317_CR0,0,214,317_AL_.jpg",
    "https://www.youtube.com/watch?v=d2S8D_SCAJY"
)


movies = [the_hunger_games, the_green_legend, bighero]

adrian.open_movies_page(movies)
