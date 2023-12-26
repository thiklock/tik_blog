from django.test import TestCase
from .models import Category, Post, Comment

class CategoryTests(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name="Django")
        self.assertEqual(category.name, "Django")
        self.assertEqual(str(category), "Django")

class PostTests(TestCase):
    def test_post_creation(self):
        category = Category.objects.create(name="Python")
        post = Post.objects.create(
            title="My first post",
            body="This is the body of my first post.",
            categories=[category]
        )
        self.assertEqual(post.title, "My first post")
        self.assertEqual(post.body, "This is the body of my first post.")
        self.assertEqual(post.categories.count(), 1)
        self.assertEqual(str(post), "My first post")

class CommentTests(TestCase):
    def test_comment_creation(self):
        post = Post.objects.create(
            title="Test Post",
            body="This is a test post for comments."
        )
        comment = Comment.objects.create(
            author="John Doe",
            body="This is a test comment.",
            post=post
        )
        self.assertEqual(comment.author, "John Doe")
        self.assertEqual(comment.body, "This is a test comment.")
        self.assertEqual(comment.post, post)
        self.assertEqual(str(comment), "John Doe on 'Test Post'")

