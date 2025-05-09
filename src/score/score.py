import os
import pygame
from dotenv import load_dotenv
from pymongo import MongoClient
import random

pygame.init()

screen_width = 800
screen_hight = 600
screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("Scoreboard")

back_picture = pygame.image.load("src/img/score_bcg.webp")
transform_back_picture = pygame.transform.scale(back_picture, (800, 600))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_BG = (30, 30, 30)
TRANSPARENT_GRAY = (50, 50, 50, 200)
GOLD = (255, 215, 0)
SILVER = (192, 192, 192)
BRONZE = (205, 127, 50)
LINE_COLOR = (80, 80, 80)

font = pygame.font.SysFont("Arial", 36)
small_font = pygame.font.SysFont("Arial", 24)

load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)
db = client.racingDb
collection = db.score


def get_scores():
    scores = collection.find().sort("score", -1).limit(10)
    return list(scores)


class Scoreboard:
    def __init__(self):
        self.scores = get_scores()

    def saveScore(self, score, name):
        score_obj = {"_id": (int(random.random() * 10000)),
                     "name": name, "score": score}
        collection.insert_one(score_obj)
        print(score_obj)

    def draw(self, screen):
        screen.fill(DARK_BG)

        overlay = pygame.Surface((600, 400), pygame.SRCALPHA)
        overlay.fill(TRANSPARENT_GRAY)
        screen.blit(transform_back_picture, (0, 0))
        screen.blit(overlay, (100, 100))

        title = font.render("Top 10 Players", True, GOLD)
        title_rect = title.get_rect(center=(screen_width // 2, 130))
        screen.blit(title, title_rect)

        place_colors = [GOLD, SILVER, BRONZE]
        default_color = WHITE

        y_offset = 180
        for i, score in enumerate(self.scores):
            name = score.get("name", "Unknown")
            points = score.get("score", 0)
            color = place_colors[i] if i < 3 else default_color

            text = small_font.render(f"{i + 1}. {name:<10} - {points}", True, color)
            text_rect = text.get_rect(center=(screen_width // 2, y_offset))
            screen.blit(text, text_rect)

            if i < len(self.scores) - 1:
                pygame.draw.line(
                    screen, LINE_COLOR, (150, y_offset + 25), (650, y_offset + 25), 1)

            y_offset += 40
