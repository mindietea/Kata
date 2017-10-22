from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())
import pymysql
import json


def get_curator_posts(curator):
	connection = pymysql.connect(host=str(os.environ.get("HOST")),
	                             user=str(os.environ.get("USER")),
	                             password=str(os.environ.get("PASSWORD")),
								 port=int(os.environ.get("PORT")),
								 database=str(os.environ.get('POSTS_DATABASE')),
	                             charset='utf8mb4',
	                             cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM posts WHERE curator = %s", str(curator))
		connection.commit()
		result = cursor.fetchall()
		return json.dumps(result)

def get_curator_post_ids(curator):
	connection = pymysql.connect(host=str(os.environ.get("HOST")),
	                             user=str(os.environ.get("USER")),
	                             password=str(os.environ.get("PASSWORD")),
								 port=int(os.environ.get("PORT")),
								 database=str(os.environ.get('POSTS_DATABASE')),
	                             charset='utf8mb4',
	                             cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM posts WHERE curator = %s", str(curator))
		connection.commit()
		result = cursor.fetchall()
		idArr = []
		for i in range(0,len(result)):
			idArr.append(result[i]['PostID'])
		return idArr


def get_all_posts():
	connection = pymysql.connect(host=str(os.environ.get("HOST")),
	                             user=str(os.environ.get("USER")),
	                             password=str(os.environ.get("PASSWORD")),
								 port=int(os.environ.get("PORT")),
								 database=str(os.environ.get('POSTS_DATABASE')),
	                             charset='utf8mb4',
	                             cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM posts")
		connection.commit()
		result = cursor.fetchall()
		connection.close()
		return json.dumps(result)

def get_post(postID):
	connection = pymysql.connect(host=str(os.environ.get("HOST")),
	                             user=str(os.environ.get("USER")),
	                             password=str(os.environ.get("PASSWORD")),
								 port=int(os.environ.get("PORT")),
								 database=str(os.environ.get('POSTS_DATABASE')),
	                             charset='utf8mb4',
	                             cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM posts WHERE PostID= %s",str(postID))
		connection.commit()
		result = cursor.fetchall()
		connection.close()
		return json.dumps(result)

def get_influencers(curator_id):
    connection = pymysql.connect(   host=str(os.environ.get("HOST")),
                                    user=str(os.environ.get("USER")),
                                    password=str(os.environ.get("PASSWORD")),
                                    port = int(os.environ.get("PORT")),
                                    database=str(os.environ.get("FOLLOWERS_DATABASE")),
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM followers WHERE Follower= %s", str(curator_id))
        connection.commit()
        result = cursor.fetchall()
        connection.close()
        return json.dumps(result)

def get_followers(curator_id):
    connection = pymysql.connect(   host=str(os.environ.get("HOST")),
                                    user=str(os.environ.get("USER")),
                                    password=str(os.environ.get("PASSWORD")),
                                    port = int(os.environ.get("PORT")),
                                    database=str(os.environ.get("FOLLOWERS_DATABASE")),
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM followers WHERE User= %s", str(curator_id))
        connection.commit()
        result = cursor.fetchall()
        connection.close()
        return json.dumps(result)


def get_image(postID):
	connection = pymysql.connect(host=str(os.environ.get("HOST")),
	                             user=str(os.environ.get("USER")),
	                             password=str(os.environ.get("PASSWORD")),
								 port=int(os.environ.get("PORT")),
								 database=str(os.environ.get('IMAGE_DATABASE')),
	                             charset='utf8mb4',
	                             cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM images WHERE POSTID= %s",str(postID))
		connection.commit()
		result = cursor.fetchall()
		connection.close()
		return json.dumps(result)

def get_product(postID):
	connection = pymysql.connect(host=str(os.environ.get("HOST")),
	                             user=str(os.environ.get("USER")),
	                             password=str(os.environ.get("PASSWORD")),
								 port=int(os.environ.get("PORT")),
								 database=str(os.environ.get('PRODUCT_DATABASE')),
	                             charset='utf8mb4',
	                             cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM products WHERE POSTID= %s",str(postID))
		connection.commit()
		result = cursor.fetchall()
		connection.close()
		return json.dumps(result)

def search_products(product_substring):
    productConnection = pymysql.connect(host=str(os.environ.get("HOST")),
	                             user=str(os.environ.get("USER")),
	                             password=str(os.environ.get("PASSWORD")),
								 port=int(os.environ.get("PORT")),
								 database=str(os.environ.get('PRODUCT_DATABASE')),
	                             charset='utf8mb4',
	                             cursorclass=pymysql.cursors.DictCursor)
    with postConnection.cursor() as cursor:
        cursor.execute("SELECT IF(INSTR(ProductName, %s), POSTID, 0) FROM products")
        result = cursor.fetchall()
        print(result.json())

def create_post(curator, date, title, description, inStock,sizes, productLink, productName, imageLink, imageName):
	postConnection = pymysql.connect(host=str(os.environ.get("HOST")),
	                             user=str(os.environ.get("USER")),
	                             password=str(os.environ.get("PASSWORD")),
								 port=int(os.environ.get("PORT")),
								 database=str(os.environ.get('POSTS_DATABASE')),
	                             charset='utf8mb4',
	                             cursorclass=pymysql.cursors.DictCursor)
	imageConnection = pymysql.connect(host=str(os.environ.get("HOST")),
	                             user=str(os.environ.get("USER")),
	                             password=str(os.environ.get("PASSWORD")),
								 port=int(os.environ.get("PORT")),
								 database=str(os.environ.get('IMAGE_DATABASE')),
	                             charset='utf8mb4',
	                             cursorclass=pymysql.cursors.DictCursor)
	productConnection = pymysql.connect(host=str(os.environ.get("HOST")),
	                             user=str(os.environ.get("USER")),
	                             password=str(os.environ.get("PASSWORD")),
								 port=int(os.environ.get("PORT")),
								 database=str(os.environ.get('PRODUCT_DATABASE')),
	                             charset='utf8mb4',
	                             cursorclass=pymysql.cursors.DictCursor)
	with postConnection.cursor() as cursor:
		cursor.execute("INSERT INTO posts (Curator, Date, Title, Description ) VALUES  (%s, %s, %s, %s);", (curator, date, title, description))
		postConnection.commit()
		cursor.execute("SELECT * FROM posts WHERE curator = %s;", curator);
		postConnection.commit()
		result = cursor.fetchall()
		currentID = int(result[len(result) - 1].get('PostID'))
		imageCursor = imageConnection.cursor()
		imageCursor.execute("INSERT INTO images (PostID, ImageLink, ImageName) VALUES (%s, %s, %s)", (currentID, imageLink, imageName))
		imageConnection.commit()
		productCursor = productConnection.cursor()
		productCursor.execute("INSERT INTO products (PostID, ProductLink, ProductName, InStock) VALUES (%s, %s, %s, %s)", (currentID, productLink, productName, inStock))
		productConnection.commit()


def create_post_array(curator, date, title, description, product):
	postConnection = pymysql.connect(host=str(os.environ.get("HOST")),
	                             user=str(os.environ.get("USER")),
	                             password=str(os.environ.get("PASSWORD")),
								 port=int(os.environ.get("PORT")),
								 database=str(os.environ.get('POSTS_DATABASE')),
	                             charset='utf8mb4',
	                             cursorclass=pymysql.cursors.DictCursor)
	imageConnection = pymysql.connect(host=str(os.environ.get("HOST")),
	                             user=str(os.environ.get("USER")),
	                             password=str(os.environ.get("PASSWORD")),
								 port=int(os.environ.get("PORT")),
								 database=str(os.environ.get('IMAGE_DATABASE')),
	                             charset='utf8mb4',
	                             cursorclass=pymysql.cursors.DictCursor)
	productConnection = pymysql.connect(host=str(os.environ.get("HOST")),
	                             user=str(os.environ.get("USER")),
	                             password=str(os.environ.get("PASSWORD")),
								 port=int(os.environ.get("PORT")),
								 database=str(os.environ.get('PRODUCT_DATABASE')),
	                             charset='utf8mb4',
	                             cursorclass=pymysql.cursors.DictCursor)
	with postConnection.cursor() as cursor:
		cursor.execute("INSERT INTO posts (Curator, Date, Title, Description) VALUES  (%s, %s, %s, %s);", (curator, date, title, description))
		postConnection.commit()
		cursor.execute("SELECT * FROM posts WHERE curator = %s;", curator);
		postConnection.commit()
		result = cursor.fetchall()
		currentID = int(result[len(result) - 1].get('PostID'))
		imageCursor = imageConnection.cursor()
		productCursor = productConnection.cursor()
		print(product)
		for i in product:
			imageCursor.execute("INSERT INTO images (PostID, ImageLink, ImageName) VALUES (%s, %s, %s)", (currentID, i['image'], i['title']))
			productCursor.execute("INSERT INTO products (PostID, ProductLink, ProductName, InStock) VALUES (%s, %s, %s, %s)", (currentID, i['link'], i['title'], i['status']))
		imageConnection.commit()
		productConnection.commit()
