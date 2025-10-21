"""
Uses Peewee as a lightweight ORM to create a blog post model, 
insert data, retrieve it, and update its status.
"""

from peewee import *

db = SqliteDatabase("blog_data.db")


class BaseModel(Model):
    class Meta:
        database = db


class BlogPost(BaseModel):
    title = CharField()
    content = TextField()
    is_published = BooleanField(default=True)


db.connect()
db.create_tables([BlogPost])


def handle_blog_posts():
    BlogPost.create(
        title="Lightweight ORM Guide",
        content="Why micro-ORMs are efficient.",
        is_published=True,
    )
    recent_post = BlogPost.get(BlogPost.title == "Lightweight ORM Guide")
    print(f"Retrieved Post: {recent_post.title}")

    recent_post.is_published = False
    recent_post.save()
    print(f"Published status: {recent_post.is_published}")


if __name__ == "__main__":
    handle_blog_posts()
    db.close()
    # Retrieved Post: Lightweight ORM Guide
    # Published status: False
