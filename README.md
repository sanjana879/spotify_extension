# Spotify Extension

This is a web-app built with Django that gives users information about an album on spotify. 
Using the Spotify API, it displays information about the album audio including
how danceable or focusable it is. Using NLP libraries to analyze the lyrics, it also displays 
the level of different moods/sentiments in the album (ex: anger, trust, etc). 

### Run Locally
```bash
 git clone https://github.com/sanjana879/spotify_extension2.git
 source venv/bin/activate
 python manage.py runserver
```
Navigate to localhost:8000

### How to Use 
Input the album name and select the correct album. A dashboard will appear with the information. 
All the audio features are ranked as an average of data points from each song. 
The lyrical analysis is done with vader_lexicon library and the NRC-Lex library that counts the number of words that map to specific emotion.