from datetime import datetime, timezone

from django.test import TestCase
from django.urls import reverse

from .models import Category, Comment, Post, User


class BlogPagesTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='tester',
            email='tester@example.com',
            password='hashed-password',
        )
        self.category = Category.objects.create(name='Programming')
        self.post = Post.objects.create(
            title='Introduction to Django',
            content='Sample blog content.',
            category=self.category,
            date_published=datetime(2023, 1, 1, tzinfo=timezone.utc),
        )
        self.comment = Comment.objects.create(
            post=self.post,
            user=self.user,
            content='Great introduction to Django!',
            date_posted=datetime(2023, 1, 2, tzinfo=timezone.utc),
        )

    def test_required_pages_load(self):
        urls = [
            reverse('main'),
            reverse('users'),
            reverse('blogs'),
            reverse('comments'),
            reverse('categories'),
            reverse('blogdetails', args=[self.post.id]),
        ]

        for url in urls:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_blog_list_links_to_detail_page(self):
        response = self.client.get(reverse('blogs'))

        self.assertContains(response, self.post.title)
        self.assertContains(response, reverse('blogdetails', args=[self.post.id]))

    def test_comment_page_shows_blog_id(self):
        response = self.client.get(reverse('comments'))

        self.assertContains(response, self.comment.content)
        self.assertContains(response, self.post.id)
