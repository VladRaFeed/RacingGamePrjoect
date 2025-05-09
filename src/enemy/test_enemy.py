import pytest
import pygame
from unittest.mock import Mock, patch
from enemy import Enemy, screen_width

# Реєстрація тестових маркерів
pytestmark = pytest.mark.usefixtures("enemy")


@pytest.fixture
def enemy():
    """Фікстура для створення об'єкта Enemy з мокованим pygame.image.load."""
    with patch("pygame.image.load") as mock_load:
        mock_image = Mock()
        mock_load.return_value = mock_image
        mock_image.get_rect.return_value = pygame.Rect(0, 0, 100, 180)
        pygame.transform.scale = Mock(return_value=mock_image)
        enemy = Enemy()
        return enemy


@pytest.mark.init
def test_enemy_init_position(enemy):
    """Перевіряє, що початкова позиція ворога в межах екрану."""
    assert 120 <= enemy.rect.centerx <= screen_width - 120
    assert enemy.rect.centery == 0
    assert enemy.game_score == 0


@pytest.mark.init
def test_enemy_init_image_and_rect(enemy):
    """Перевіряє, що зображення та прямокутник ворога правильно ініціалізовані."""
    assert enemy.image is not None
    assert enemy.rect.width == 100
    assert enemy.rect.height == 180


@pytest.mark.move
@pytest.mark.parametrize("initial_y, expected_y, expected_score, reset_position", [
    (590, 600, 0, False),  # Нормальний рух вниз
    # Вихід за межі екрану, скидання позиції (rect.y = -90 через rect.centery = 0)
    (600, -90, 1, True),
])
def test_enemy_move(enemy, initial_y, expected_y, expected_score, reset_position):
    """Перевіряє рух ворога та оновлення рахунку."""
    enemy.rect.y = initial_y
    with patch("random.randint") as mock_randint:
        mock_randint.return_value = 300  # Фіксована x-координата для передбачуваності
        enemy.move()

    assert enemy.rect.y == expected_y
    assert enemy.game_score == expected_score
    if reset_position:
        assert enemy.rect.centerx == 300
        assert enemy.rect.centery == 0


@pytest.mark.move
@patch("random.randint")
def test_enemy_move_random_position_after_reset(mock_randint, enemy):
    """Перевіряє, що ворог отримує нову випадкову позицію після виходу за межі."""
    mock_randint.return_value = 400
    enemy.rect.y = 600
    enemy.move()

    assert enemy.rect.centerx == 400
    assert enemy.rect.centery == 0
    assert enemy.game_score == 1
