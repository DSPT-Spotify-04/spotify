# Spotify Song Suggester: Product Vision Document
This document shares the vision for the Spotify Song Suggester web application that we are building, as part of our Lambda School Part-Time Data Science build week (04) project. 

## Proposal
### What problem does your app solve?
Music listeners have their own preferences and tastes, but there are millions of songs to choose from. They need help discovering the songs that fit their preferences from the vast array to choose from.

### Be as specific as possible; how does your app solve the problem?
We first ask the user to provide a list of a few songs that they like, or show us a few playlists that they follow. We get granular data on each song using the Spotify API, then train a classifier model with that data. We then run that model to predict which songs in a pre-existing database consisting of many songs to identify songs that are similar to those that the user has offered us.

### What is the mission statement?
We aim to help listeners find the songs they’ll love faster and more easily, so they have a joyful experience using Spotify.

## Features
### What features are required for your minimum viable product?
1. Build a model to recommend songs based on similarity to user input (I like song x, here are n songs: like it based on these similar features.)
2. Create visualizations using song data to highlight similarities and differences between recommendations.

### What features may you wish to put in a future release?
Connect directly to a user’s account and use private playlists and previously played tracks. This will require a user authentication token.

### What do the top 3 similar apps do for their users?
Tidal, SoundCloud, and Apple Music likely do the same thing. The key innovations in song recommendation will always come down to memory and code efficiency in training models so that use diverse datasets for each recommendation.

## Frameworks - Libraries
### What 3rd party frameworks/libraries are you considering using?
Flask, SQLAlchemy, SKLearn

### Do the APIs you need require you to contact them to gain access?
Yes, the Spotify Developer’s API

### Are you required to pay to use said API(s)?
No

## For Data Scientists
### Describe the established data source with at least rough data able to be provided on day one.
We were not provided any data table. We have found our own data table and discovered the API online, which are formatted with the following features:
Valence, year, acousticness, artists, danceability, duration (ms), energy, explicit, id, key, liveness, loudness, mode, name, popularity, release date, speachiness, tempo

### Write a description for what the data science problem is. What uncertainty or prediction are you trying to discover? How could this data be used to find a solution to this problem?
We do not know which songs, from a larger dataset consisting of many songs, fit a given user’s preferences. We identify their preferences by having them enter songs that they like, and then using supervised machine learning to identify similar songs.
Our target variable is “is_recommended” (a new variable we will create), for which the songs that are input by the user will be set to 1. We will train a model using those songs, then run that model on a larger dataset consisting of many songs to identify those that fit the criteria and can be classified as “is_recommended”.

## Target Audience
### Who is your target audience? Be specific.
Music listeners across all demographics and geographies.

### What feedback have you gotten from potential users?
None yet.

### Have you validated this problem and your solution with a target audience? Describe how.
Not yet.

## Prototype Key Feature(s)
### How long do you think it will take to implement these features?
1-2 weeks.

### Do you anticipate working on stretch functionality after completion of a Minimal Viable Product?
Yes.



