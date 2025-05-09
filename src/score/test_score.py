import pytest
from unittest.mock import Mock, patch
from score import Scoreboard


@pytest.fixture
def scoreboard():
    """Фікстура для створення об'єкта Scoreboard з мокованими залежностями."""
    with patch("score.MongoClient") as mock_mongo, \
            patch("score.get_scores") as mock_get_scores, \
            patch("pygame.image.load") as mock_load, \
            patch("pygame.transform.scale") as mock_scale:
        mock_get_scores.return_value = [
            {"_id": 1, "name": "Player1", "score": 100},
            {"_id": 2, "name": "Player2", "score": 80},
            {"_id": 3, "name": "Player3", "score": 60}
        ]
        mock_mongo.return_value.racingDb.score.find.return_value.sort.return_value.limit.return_value = mock_get_scores.return_value  # noqa: E501
        mock_image = Mock()
        mock_load.return_value = mock_image
        mock_scale.return_value = mock_image
        scoreboard = Scoreboard()
        return scoreboard


@pytest.mark.init
def test_scoreboard_init_loads_scores(scoreboard):
    """Перевіряє, що ініціалізація Scoreboard завантажує результати з бази."""
    assert len(scoreboard.scores) == 3
    assert scoreboard.scores[0]["name"] == "Player1"
    assert scoreboard.scores[0]["score"] == 100
    assert scoreboard.scores[2]["name"] == "Player3"
    assert scoreboard.scores[2]["score"] == 60


@pytest.mark.save
@patch("score.random.random")
@patch("score.collection")
def test_save_score(mock_collection, mock_random, scoreboard):
    """Перевіряє, що saveScore додає новий результат до бази."""
    mock_random.return_value = 0.1234
    scoreboard.saveScore(50, "TestPlayer")

    expected_score_obj = {"_id": 1234, "name": "TestPlayer", "score": 50}
    mock_collection.insert_one.assert_called_once_with(expected_score_obj)


@pytest.mark.save
@patch("score.random.random")
@patch("score.collection")
def test_save_score_different_ids(mock_collection, mock_random, scoreboard):
    """Перевіряє, що saveScore генерує різні ID для різних викликів."""
    mock_random.side_effect = [0.1, 0.2]
    scoreboard.saveScore(50, "PlayerA")
    scoreboard.saveScore(70, "PlayerB")

    calls = mock_collection.insert_one.call_args_list
    assert calls[0][0][0]["_id"] == 1000
    assert calls[1][0][0]["_id"] == 2000
    assert calls[0][0][0]["name"] == "PlayerA"
    assert calls[1][0][0]["name"] == "PlayerB"


@pytest.mark.draw
@patch("pygame.display.set_mode")
@patch("score.font")
@patch("score.small_font")
@patch("pygame.Surface")
@patch("pygame.draw.line")
def test_draw_renders_correctly(
        mock_draw_line, mock_surface, mock_small_font, mock_font, mock_set_mode, scoreboard):
    """Перевіряє, що draw викликає правильні методи рендерингу."""
    mock_screen = Mock()
    mock_set_mode.return_value = mock_screen
    mock_font.render.side_effect = [
        Mock(get_rect=Mock(return_value=Mock(center=(400, 130)))),  # Title
    ]
    mock_small_font.render.side_effect = [
        Mock(get_rect=Mock(return_value=Mock(center=(400, 180)))),  # Player1
        Mock(get_rect=Mock(return_value=Mock(center=(400, 220)))),  # Player2
        Mock(get_rect=Mock(return_value=Mock(center=(400, 260))))   # Player3
    ]
    mock_overlay = Mock()
    mock_surface.return_value = mock_overlay

    scoreboard.draw(mock_screen)

    # Перевірка викликів screen.fill
    mock_screen.fill.assert_called_once_with((30, 30, 30))

    # Перевірка викликів blit
    assert mock_screen.blit.call_count == 6  # Фон, оверлей, заголовок, 3 записи
    mock_screen.blit.assert_any_call(mock_overlay, (100, 100))

    # Перевірка викликів font.render (для заголовка)
    assert mock_font.render.call_count == 1  # Тільки заголовок
    mock_font.render.assert_any_call("Top 10 Players", True, (255, 215, 0))

    # Перевірка викликів small_font.render (для записів)
    assert mock_small_font.render.call_count == 3  # 3 записи
    mock_small_font.render.assert_any_call("1. Player1    - 100", True, (255, 215, 0))
    mock_small_font.render.assert_any_call("2. Player2    - 80", True, (192, 192, 192))
    mock_small_font.render.assert_any_call("3. Player3    - 60", True, (205, 127, 50))

    # Перевірка викликів draw.line
    assert mock_draw_line.call_count == 2  # Лінії між 1-2 і 2-3


@pytest.mark.draw
@patch("pygame.display.set_mode")
@patch("score.font")
@patch("score.small_font")
@patch("pygame.Surface")
def test_draw_empty_scores(mock_surface, mock_small_font,
                           mock_font, mock_set_mode, scoreboard):
    """Перевіряє draw, коли список результатів порожній."""
    scoreboard.scores = []
    mock_screen = Mock()
    mock_set_mode.return_value = mock_screen
    mock_font.render.return_value.get_rect.return_value = Mock(center=(400, 130))
    mock_overlay = Mock()
    mock_surface.return_value = mock_overlay

    scoreboard.draw(mock_screen)

    # Перевірка, що рендериться фон, оверлей і заголовок
    assert mock_screen.blit.call_count == 3  # Фон, оверлей, заголовок
    mock_font.render.assert_called_once_with("Top 10 Players", True, (255, 215, 0))
    assert mock_small_font.render.call_count == 0  # Записи не рендеряться
