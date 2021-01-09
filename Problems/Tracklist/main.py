def tracklist(**music):
    for n, a in music.items():
        print(n)
        for i, v in n.items():
            print("ALBUM: " + str((i)))



tracklist(Woodkid={"The Golden Age": "Run Boy Run",
                   "On the Other Side": "Samara"},
          Cure={"Disintegration": "Lovesong",
                "Wish": "Friday I'm in love"})
