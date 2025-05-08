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

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

font = pygame.font.SysFont("Arial", 36)
small_font = pygame.font.SysFont("Arial", 24)

load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)
db = client.racingDb
collection = db.score

def get_scores():
    scores = collection.find().sort("score", -1).limit(10)  # Сортуємо за спаданням і беремо топ-10
    return list(scores)

class Scoreboard:
    def __init__(self):
        self.scores = get_scores()
        
    def saveScore(self, score, name):
        score_obj = {"_id": (int(random.random() * 10000)), "name": name, "score": score}
        collection.insert_one(score_obj)
        print(score_obj)


    def draw(self, screen):
        screen.fill(BLACK)

        title = font.render("Scoreboard", True, WHITE)
        title_rect = title.get_rect(center=(screen_width // 2, 50))
        screen.blit(title, title_rect)

        y_offset = 150
        for i, score in enumerate(self.scores):
            player_name = score.get('name', 'Unknown')
            player_score = score.get('score', 0)
            
            score_text = small_font.render(f"{i + 1}. {player_name}: {player_score}", True, WHITE)
            score_rect = score_text.get_rect(center=(screen_width // 2, y_offset))
            screen.blit(score_text, score_rect)
            y_offset += 40