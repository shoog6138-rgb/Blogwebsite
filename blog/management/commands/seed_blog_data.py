from datetime import datetime

from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand

from blog.models import Category, Comment, Post, User


class Command(BaseCommand):
    help = 'Insert sample blog users, categories, posts, and comments.'

    def handle(self, *args, **options):
        comments = [
            (1, 2, 'Great introduction to Django!', '2023-01-02T09:00:00Z'),
            (1, 5, 'Very informative article.', '2023-01-03T10:30:00Z'),
            (2, 3, 'These tips are really helpful.', '2023-01-06T08:15:00Z'),
            (3, 7, 'I love traveling and exploring nature!', '2023-01-11T14:45:00Z'),
            (4, 4, 'Beautifully written article about photography.', '2023-01-16T16:00:00Z'),
            (6, 8, 'Healthy eating is so important for overall well-being.', '2023-01-26T11:25:00Z'),
            (7, 9, 'I enjoy reading different genres of books.', '2023-02-02T12:10:00Z'),
            (8, 10, 'Graphic design is such a creative field.', '2023-02-06T13:40:00Z'),
            (9, 6, 'Yoga and meditation have changed my life.', '2023-02-11T18:20:00Z'),
            (10, 1, "Positive thinking can make a huge difference in one's life.", '2023-02-16T07:35:00Z'),
        ]
        users = [
            ('johnsmith', 'johnsmith@example.com'),
            ('emilyjones', 'emilyjones@example.com'),
            ('davidwilson', 'davidwilson@example.com'),
            ('sarahbrown', 'sarahbrown@example.com'),
            ('michaelscott', 'michaelscott@example.com'),
            ('lisajohnson', 'lisajohnson@example.com'),
            ('alexturner', 'alexturner@example.com'),
            ('jessicabaker', 'jessicabaker@example.com'),
            ('matthewwright', 'matthewwright@example.com'),
            ('oliviawalker', 'oliviawalker@example.com'),
        ]
        categories = [
            'Programming',
            'Productivity',
            'Travel',
            'Art',
            'Technology',
            'Health',
            'Books',
            'Design',
            'Wellness',
            'Self-Improvement',
        ]
        posts = [
            ('Introduction to Django', 'Lorem ipsum dolor sit amet.', 'Programming', '2023-01-01T09:00:00Z'),
            ('Tips for Effective Time Management', 'Lorem ipsum dolor sit amet.', 'Productivity', '2023-01-05T09:00:00Z'),
            ('Exploring the Wonders of Nature', 'Lorem ipsum dolor sit amet.', 'Travel', '2023-01-10T09:00:00Z'),
            ('The Art of Photography', 'Lorem ipsum dolor sit amet.', 'Art', '2023-01-15T09:00:00Z'),
            ('Understanding Machine Learning Algorithms', 'Lorem ipsum dolor sit amet.', 'Technology', '2023-01-20T09:00:00Z'),
            ('Healthy Eating Habits for a Balanced Lifestyle', 'Lorem ipsum dolor sit amet.', 'Health', '2023-01-25T09:00:00Z'),
            ('Exploring the World of Literature', 'Lorem ipsum dolor sit amet.', 'Books', '2023-02-01T09:00:00Z'),
            ('Mastering the Basics of Graphic Design', 'Lorem ipsum dolor sit amet.', 'Design', '2023-02-05T09:00:00Z'),
            ('The Benefits of Yoga and Meditation', 'Lorem ipsum dolor sit amet.', 'Wellness', '2023-02-10T09:00:00Z'),
            ('The Power of Positive Thinking', 'Lorem ipsum dolor sit amet.', 'Self-Improvement', '2023-02-15T09:00:00Z'),
        ]

        for username, email in users:
            User.objects.update_or_create(
                username=username,
                defaults={'email': email, 'password': make_password('Password123!')},
            )

        for name in categories:
            Category.objects.get_or_create(name=name)

        for title, content, category_name, published in posts:
            category = Category.objects.get(name=category_name)
            Post.objects.update_or_create(
                title=title,
                defaults={
                    'content': content,
                    'category': category,
                    'date_published': datetime.fromisoformat(published.replace('Z', '+00:00')),
                },
            )

        for post_id, user_id, content, posted in comments:
            post = Post.objects.get(id=post_id)
            user = User.objects.get(id=user_id)
            Comment.objects.update_or_create(
                post=post,
                user=user,
                content=content,
                defaults={'date_posted': datetime.fromisoformat(posted.replace('Z', '+00:00'))},
            )

        totals = {
            'users': User.objects.count(),
            'categories': Category.objects.count(),
            'posts': Post.objects.count(),
            'comments': Comment.objects.count(),
        }
        self.stdout.write(self.style.SUCCESS(f'Sample data inserted: {totals}'))
