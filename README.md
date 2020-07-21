# Django Blog API

This is a simple blog api based on Django REST Framework. The three main resources of this API is posts, categories and tags and one sub resource of posts is comments. For authenticating user i'm using Django REST Framework token auth. Installation guide, api endpoints and sample request/response are given below.

## For installing this Application please do this following steps
```
1. Create a virtual environment and activate the environment
2. Clone this repository: git clone https://github.com/abdurraufraihan/blogapi.git
3. Then go to blogapi/blog directory: cd blogapi/blog
4. Install dependency: pip install -r requirements.txt
5. Run the app: python manage.py runserver
6. Then create a superuser: python manage.py createsuperuser
7. Now goto django admin with the superuser credential and add some post, comment, category, tag and test with your favorite api client
```

## Endpoints
- api/v1/posts
- api/v1/posts/:id
- api/v1/posts/:id/comments
- api/v1/categories
- api/v1/categories/:id
- api/v1/tags
- api/v1/tags/:id

## Sample API Request and Response
##### GET api/v1/posts
response body:
```json
{
	"totalPost": 17,
	"posts": [
		{
			"id": "a08bf8a3-5dbc-49b7-8cf4-395af88964a2",
			"title": "This is post title",
			"description": "This is post descripton",
			"image": "/media/post/mypic.png",
			"category": "category two",
			"tag": [
				"tag one",
				"tag two"
			]
		},
		{
			"id": "54e40b52-4ffb-4aa3-8200-b00a2f25336d",
			"title": "This is post title two",
			"description": "This is post descripton two",
			"image": "/media/post/mypictwo.png",
			"category": "category one",
			"tag": [
				"tag two",
				"tag three"
			]
		}, ......
	]
}
```
##### GET api/v1/posts/a08bf8a3-5dbc-49b7-8cf4-395af88964a2
```json
{
	"id": "a08bf8a3-5dbc-49b7-8cf4-395af88964a2",
	"title": "This is post title",
	"description": "This is post description",
	"image": "/media/post/mypic.png",
	"category": "category two",
	"tag": [
		"tag one",
		"tag two"
	]
}
```
##### POST api/v1/posts
request body:
```json
{
	"title": "This is post title",
	"description": "This is post descripton",
	"image": "<imagefile>",
	"category": "8240307c-db87-4107-83e3-2f7aeabf5c48",
	"tag": [
		"81dadc2d-4438-420e-8db7-81017260c710",
		"0e6f50cd-5ee7-4516-a9e2-557e107f3e08"
	]
}
```
response body:
```json
{
	"id": "a08bf8a3-5dbc-49b7-8cf4-395af88964a2",
	"title": "This is post title",
	"description": "This is post descripton",
	"image": "/media/post/mypic.png",
	"category": "category two",
	"tag": [
		"tag one",
		"tag two"
	]
}
```
##### PUT api/v1/posts/a08bf8a3-5dbc-49b7-8cf4-395af88964a2
This end point is dynamic that mean we can modify post by requesting only those fields which we want to modify. We don't need to request with all post fields. As sample i'm doing PUT request by modifying description and tag field below.
request body:
```json
{
	"description": "The modified description",
	"tag": [
		"81dadc2d-4438-420e-8db7-81017260c710",
		"31349f0c-8162-4919-96ae-f94f102598fb"
	]
}
```
response body:
```json
{
	"description": "The modified description",
	"tag": [
		"tag one",
		"tag three"
	]
}
```
##### DELETE api/v1/posts/a08bf8a3-5dbc-49b7-8cf4-395af88964a2
this will delete post one and response back a status 204 no content

##### GET api/v1/posts/a08bf8a3-5dbc-49b7-8cf4-395af88964a2/comments
response body:
```json
[
	{
		"id": "6dc7b702-9c04-402f-a4d1-246356ca0b47",
		"description": "This is comment of post one"
	},
	{
		"id": "4479c87e-bfeb-49d6-80d6-2f9fb41cce2b",
		"description": "This is another comment of post one"
	}
]
```
##### POST api/v1/posts/a08bf8a3-5dbc-49b7-8cf4-395af88964a2/comments
request body:
```json
{
	"description": "This is comment of post one"
}
```
response body:
```json
{
	"id": "6dc7b702-9c04-402f-a4d1-246356ca0b47",
	"description": "This is comment of post one"
}
```

##### GET api/v1/categories
response body:
```json
[
	{
		"id": "8240307c-db87-4107-83e3-2f7aeabf5c48",
		"name": "category one"
	},
	{
		"id": "bbd326a3-e8dd-42a7-9fb6-59de66371ced",
		"name": "category two"
	}
]
```
##### GET api/v1/categories/8240307c-db87-4107-83e3-2f7aeabf5c48
response body:
```json
{
	"id": "8240307c-db87-4107-83e3-2f7aeabf5c48",
	"name": "category one"
}
```
##### POST api/v1/categories
request body:
```json
{
	"name": "category one"
}
```
response body:
```json
{
	"id": "8240307c-db87-4107-83e3-2f7aeabf5c48",
	"name": "category one"
}
```
##### PUT api/v1/categories/8240307c-db87-4107-83e3-2f7aeabf5c48
request body:
```json
{
	"name": "category one modified"
}
```
response body:
```json
{
	"id": "8240307c-db87-4107-83e3-2f7aeabf5c48",
	"name": "caegory one modified"
}
```
##### DELETE api/v1/categories/8240307c-db87-4107-83e3-2f7aeabf5c48
this will delete category one and response back a status 204 no content

##### GET api/v1/tags
response body:
```json
[
	{
		"id": "81dadc2d-4438-420e-8db7-81017260c710",
		"name": "tag one"
	},
	{
		"id": "0e6f50cd-5ee7-4516-a9e2-557e107f3e08",
		"name": "tag two"
	}
]
```
##### GET api/v1/tags/81dadc2d-4438-420e-8db7-81017260c710
response body:
```json
{
	"id": "81dadc2d-4438-420e-8db7-81017260c710",
	"name": "tag one"
}
```
##### POST api/v1/tags
request body:
```json
{
	"name": "tag one"
}
```
response body:
```json
{
	"id": "81dadc2d-4438-420e-8db7-81017260c710",
	"name": "tag one"
}
```
##### PUT api/v1/tags/81dadc2d-4438-420e-8db7-81017260c710
request body:
```json
{
	"name": "tag one modified"
}
```
response body:
```json
{
	"id": "81dadc2d-4438-420e-8db7-81017260c710",
	"name": "tag one modified"
}
```
##### DELETE api/v1/tags/81dadc2d-4438-420e-8db7-81017260c710
this will delete tag one and response back a status 204 no content
