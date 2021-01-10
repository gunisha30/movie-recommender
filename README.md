# Content based recommendation engine
This type of recommendation systems, takes in a movie that a user currently likes as input. Then it analyzes the contents (storyline, genre, cast, director etc.) of the movie to find out other movies which have similar content. Then it ranks similar movies according to their similarity scores and recommends the most relevant movies to the user.

# Cosine Similarity
It is used as a score of similarity between two given vectors and is calculated as the cosine of angle between them. In this project, Cosine Similarity has been used to rank movies based on their similarity with a particular movie. 

# Deployment
The project has been deployed on the web using an AWS ec2 instance with the help of a framework called Flask.
