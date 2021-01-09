def tracklist(**music):
    for n, a in music.items():
        print(n)
        for album, track in a.items():
            print("ALBUM: " + str(album) + " " + "TRACK: " + str(track))



tracklist(Woodkid={"The Golden Age": "Run Boy Run",
                   "On the Other Side": "Samara"},
          Cure={"Disintegration": "Lovesong",
                "Wish": "Friday I'm in love"})
