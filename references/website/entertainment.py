import media
import fresh_tomatoes


# Dhoni movie: movie title, storyline, posterimage and movie trailer
Dhoni = media.Movie(
    "MS Dhoni",
    "Story of boy from small town turning into one of finest cricketers",
    "dhoni2.jpg",
    "https://www.youtube.com/watch?v=6L6XqWoS8tw"
    )

# Padmaavat movie: movie title, storyline, posterimage and movie trailer
Padmavat = media.Movie(
    "Padmaavat",
    "About Rani Padamavati",
    "DKNVZk4UQAAmJmC.jpg",
    "https://www.youtube.com/watch?v=8YaF2m7hCx0"
    )

# Tiger Zinda Hai movie: movie title, storyline, posterimage and movie trailer
Tiger_Zinda_Hai = media.Movie(
    "Tiger Zinda Hai",
    "Raw agent and Isi agent love story",
    "tiger-zinda-hai-new-poster-081117.jpg",
    "https://www.youtube.com/watch?v=ePO5M5DE01I"
    )

# Special 26 movie: movie title, storyline, posterimage and movie trailer
Special_26 = media.Movie(
    "Special 26",
    "About real and fake CBI",
    "Special-26-poster.jpg",
    "https://www.youtube.com/watch?v=PiyQb28geOg"
    )

# Drishyam movie: movie title, storyline, posterimage and movie trailer
Drishyam = media.Movie(
    "Drishyam",
    "Men intelligence to save his family from big trouble",
    "67868_thumb_665.jpg",
    "https://www.youtube.com/watch?v=AuuX2j14NBg"
    )

# Mai Hoon Na movie: movie title, storyline, posterimage and movie trailer
Mai = media.Movie(
    "Mai Hoon Na",
    "Two step brothers story",
    "main-hoon-na.27049.jpg",
    "https://www.youtube.com/watch?v=7fRLWoyLFBk"
    )

# set movies that will be passed to media file
movies = [
    Dhoni,
    Padmavat,
    Tiger_Zinda_Hai,
    Special_26,
    Drishyam,
    Mai
    ]

# Open HTML file in a webbrowser via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
