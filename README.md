# Disclose
- Deployment - [https://disclose-locations.fly.dev/](https://disclose-locations.fly.dev/)
- Mapbox API - [https://docs.mapbox.com/api/overview/](https://docs.mapbox.com/api/overview/)

## Technologies Used
Django, PostgreSQL, Python, Javascript, HTML, CSS, CSS Flexbox, Mapbox API

## Description
Disclose is a social media platform that caters to the 'urban explorer' crowd. It allows users to share their favorite locations that are otherwise not well known. If you're traveling through an area you can check the app for the spots nearby that only the locals know about. 

## User Stories
- As a user I want to add a custom location to the map.
- As a user I want to be able to edit and delete my locations.
- As a user I want to see locations other people post onto the map.
- As a user I want to be able to read the details of all locations.
- As a user I want to be able to comment on other users posts.

## Wireframe
![wireframe](https://github.com/JCollinJones25/disclose/blob/main/main_app/static/images/wireframe.png?raw=true)

## ERD
![ERD](https://github.com/JCollinJones25/disclose/blob/main/main_app/static/images/ERD.png?raw=true)

## MVP Goals ✅
- CRUD functionality with PostgresQL database
- Map
- Styling

## Stretch Goals
- AUTH ✅
- Display location data on map ✅
- Map markers have pop up window with location info ✅
- Comments ✅
- Search bar ✅
- Profile page 
- User permissions

## Future Goals

- Many features on my site would be better implemented using a component based framework such as React so that things such as the comments or the search results can be rendered on the page without going to a new url or refreshing the browser.

- Did not get around to specifying user permissions so users can only update or delete their own locations or comments.

- I had an issue with getting the comments to be updated or deleted and I could not get the location pk to pass to the comment create page so the cancel button has to redirect to the home page. 

- The profile page is set up but does not have any functionality.

## Screenshots

![login](https://github.com/JCollinJones25/disclose/blob/6f22ce26610c10ab56c5389c7b62336e3bbaf519/main_app/static/images/.login.png.icloud)
![home](https://github.com/JCollinJones25/disclose/blob/6f22ce26610c10ab56c5389c7b62336e3bbaf519/main_app/static/images/.home.png.icloud)
![location](https://github.com/JCollinJones25/disclose/blob/main/main_app/static/images/location.png)
![comment-section](https://github.com/JCollinJones25/disclose/blob/main/main_app/static/images/comment-section.png)
![comment](https://github.com/JCollinJones25/disclose/blob/main/main_app/static/images/comment.png)
![search](https://github.com/JCollinJones25/disclose/blob/main/main_app/static/images/search.png)
![create](https://github.com/JCollinJones25/disclose/blob/main/main_app/static/images/create.png)
