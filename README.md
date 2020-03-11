# Blog API

This is a simple blog api which is based on Django REST Framework. The three main resource of this API is Post, Category and Tag. For authenticating user i'm using the Django REST Framework token auth. The api endpoints and sample request, response is given below.


# Endpoints
- api/v1/posts
- api/v1/posts/:id
- api/v1/categories
- api/v1/categories/:id
- api/v1/tags
- api/v1/tags/:id

## Sample API Request and Response
##### GET api/v1/posts
response body:
```json
[
	{
		"id": 1,
		"title": "This is psot title",
		"description": "This is post descripton",
		"image": "/media/post/mypic.png",
		"category": "category two",
		"tag": [
			"tag one",
			"tag two"
		]
	},
	{
		"id": 1,
		"title": "This is psot title two",
		"description": "This is post descripton two",
		"image": "/media/post/mypictwo.png",
		"category": "category one",
		"tag": [
			"tag two",
			"tag three"
		]
	},
]
```
##### GET api/v1/posts/1
```json
{
	"id": 1,
	"title": "This is psot title",
	"description": "This is post descripton",
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
	"title": "This is psot title",
	"description": "This is post descripton",
	"image": <imagefile>,
	"category": 2,
	"tag": [1, 2]
}
```
response body:
```json
{
	"id": 1,
	"title": "This is psot title",
	"description": "This is post descripton",
	"image": "/media/post/mypic.png",
	"category": "category two",
	"tag": [
		"tag one",
		"tag two"
	]
}
```
##### PUT api/v1/posts/1
This end point is dynamic that mean we can modify any of post field by requesting only those fields. We don't need to request with all post fields. As sample i'm modifying description and tag below.
request body:
```json
{
	"description": "The modified description",
	"tag": [2,3]
}
```
response body:
```json
{
	"description": "The modified description",
	"tag": [2,3]
}
```
##### DELETE api/v1/posts/1
this will delete post one and response back 204 not content

##### GET api/v1/categories
response body:
```json
[
	{
		"id": 1,
		"name": "caegory one"
	},
	{
		"id": 2,
		"name": "category two"
	}
]
```
##### GET api/v1/categories/1
response body:
```json
{
	"id": 1,
	"name": "caegory one"
}
```
##### POST api/v1/categories
request body:
```json
{
	"name": "caegory one"
}
```
response body:
```json
{
	"id": 1,
	"name": "caegory one"
}
```
##### PUT api/v1/categories/1
request body:
```json
{
	"name": "caegory one modified"
}
```
response body:
```json
{
	"id": 1,
	"name": "caegory one modified"
}
```
##### DELETE api/v1/categories/1
this will delete category one and response back 204 not content

##### GET api/v1/tags
response body:
```json
[
	{
		"id": 1,
		"name": "tag one"
	},
	{
		"id": 2,
		"name": "tag two"
	}
]
```
##### GET api/v1/tags/1
response body:
```json
{
	"id": 1,
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
	"id": 1,
	"name": "tag one"
}
```
##### PUT api/v1/tags/1
request body:
```json
{
	"name": "tag one modified"
}
```
response body:
```json
{
	"id": 1,
	"name": "tag one modified"
}
```
##### DELETE api/v1/tags/1
this will delete tag one and response back 204 not content
