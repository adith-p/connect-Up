# Connect-up
A social media api which will let the individuals connect with other profectional individuals 


## Core API Components

### Users:
GET /users/:user_id - Retrieve user information (name, bio, profile picture, etc.)
POST /users - Create a new user account
PUT /users/:user_id - Update user information
### Posts:
GET /posts - Get a list of posts (public feed, user's posts, etc.) with optional filters (by date, hashtag, etc.)
POST /posts - Create a new post (text, image, video)
GET /posts/:post_id - Retrieve details of a specific post
PUT /posts/:post_id - Update an existing post
DELETE /posts/:post_id - Delete a post (consider authorization here!)
### Comments:
GET /posts/:post_id/comments - Get a list of comments on a specific post
POST /posts/:post_id/comments - Create a new comment on a post
GET /comments/:comment_id - Retrieve details of a specific comment
PUT /comments/:comment_id - Update an existing comment
DELETE /comments/:comment_id - Delete a comment (consider authorization here!)
### Likes:
POST /posts/:post_id/like - Like a post
DELETE /posts/:post_id/like - Unlike a post
### Relationships (Follow/Following):
GET /users/:user_id/following - Get a list of users a specific user follows
GET /users/:user_id/followers - Get a list of users following a specific user
POST /users/:user_id/follow - Follow another user
DELETE /users/:user_id/follow - Unfollow a user