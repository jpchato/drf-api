from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Game

class GameModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_game = Game.objects.create(
            player = test_user,
            title = 'Title of game',
            description = 'Description of the game'
        )
        test_game.save()

    def test_game_content(self):
        game = Game.objects.get(id=1)

        self.assertEqual(str(game.player), 'tester')
        self.assertEqual(game.title, 'Title of game')
        self.assertEqual(game.description, 'Description of the game')