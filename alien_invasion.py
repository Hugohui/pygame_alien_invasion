import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建用于存储统计信息的实例
    stats = GameStats(ai_settings)

    # 开始按钮
    play_button = Button(ai_settings, screen, "Play")
    
    # 创建一艘船
    ship = Ship(ai_settings, screen)

    # 创建用于存储子弹的编组
    bullets = Group()

    # 创建外星人编组
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 游戏主循环
    while True:
        # 事件监听
        gf.check_events(ai_settings, stats, screen, ship, aliens, bullets, play_button)
        if stats.game_active:
            # 更新船
            ship.update()
            # 更新子弹
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            # 更新外星人
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        # 更新屏幕
        gf.update_screen(ai_settings, stats, screen, ship, aliens, bullets, play_button)

run_game()