import pytest
import pygame
from unittest.mock import Mock, patch
from player import Player

@pytest.fixture
def player():
    """Фікстура для створення об'єкта Player з мокованим pygame.image.load."""
    with patch("pygame.image.load") as mock_load:
        mock_image = Mock()
        mock_load.return_value = mock_image
        mock_image.get_rect.return_value = pygame.Rect(0, 0, 90, 180)
        pygame.transform.scale = Mock(return_value=mock_image)
        player = Player()
        return player

@pytest.mark.init
def test_player_init_position(player):
    """Перевіряє, що початкова позиція гравця правильна."""
    assert player.rect.center == (400, 520)
    assert player.rect.width == 90
    assert player.rect.height == 180

@pytest.mark.init
def test_player_init_image(player):
    """Перевіряє, що зображення гравця ініціалізоване."""
    assert player.image is not None

@pytest.mark.move
@pytest.mark.parametrize("initial_x, keys, expected_x", [
    (400, {pygame.K_a: True, pygame.K_d: False}, 395),  # Рух вліво
    (400, {pygame.K_d: True, pygame.K_a: False}, 405),  # Рух вправо
    (400, {pygame.K_a: False, pygame.K_d: False}, 400),  # Без руху
    (165, {pygame.K_a: True, pygame.K_d: False}, 165),  # На межі ліворуч (rect.left = 120)
    (635, {pygame.K_d: True, pygame.K_a: False}, 635),  # На межі праворуч (rect.right = 680)
])
def test_player_move(player, initial_x, keys, expected_x):
    """Перевіряє рух гравця залежно від натиснутих клавіш і меж екрану."""
    player.rect.centerx = initial_x
    def key_pressed_mock():
        def getitem(self, key):
            return keys.get(key, False)
        return Mock(__getitem__=getitem)
    
    with patch("pygame.key.get_pressed", key_pressed_mock):
        player.move()
    
    assert player.rect.centerx == expected_x
    assert player.rect.centery == 520