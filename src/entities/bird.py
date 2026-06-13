"""
小鸟类
"""

import pygame
import math
import random
from src.entities.particle import Particle
from src.utils.constants import *

class Bird:
    """小鸟类"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = BIRD_RADIUS
        self.color = RED
        self.velocity_x = 0
        self.velocity_y = 0
        self.launched = False
        self.dragging = False
        self.start_x = x
        self.start_y = y
        self.trail_particles = []
        self.active = True  # 新增：标记小鸟是否活跃
        
    def draw(self, screen):
        """绘制精美的小鸟"""
        if not self.active:
            return
            
        # 主体
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        
        # 高光
        pygame.draw.circle(screen, (255, 150, 150), (int(self.x - 5), int(self.y - 5)), 8)
        
        # 眼睛
        pygame.draw.circle(screen, WHITE, (int(self.x + 8), int(self.y - 5)), 7)
        pygame.draw.circle(screen, BLACK, (int(self.x + 8), int(self.y - 5)), 3)
        
        # 眉毛
        pygame.draw.arc(screen, BLACK, (self.x + 5, self.y - 12, 10, 8), math.pi, 2 * math.pi, 2)
        
        # 嘴巴
        pygame.draw.polygon(screen, ORANGE, [
            (self.x + 15, self.y),
            (self.x + 25, self.y - 4),
            (self.x + 25, self.y + 4)
        ])
        
        # 绘制尾迹粒子
        for particle in self.trail_particles[:]:
            particle.update()
            particle.draw(screen)
            if particle.life <= 0:
                self.trail_particles.remove(particle)
    
    def update(self, gravity=GRAVITY):
        """更新小鸟位置"""
        if not self.active:
            return
            
        if self.launched:
            self.velocity_y += gravity
            self.x += self.velocity_x
            self.y += self.velocity_y
            
            # 添加尾迹粒子
            if random.random() < 0.3:
                self.trail_particles.append(Particle(self.x, self.y, YELLOW))
            
            # 边界检测 - 飞出屏幕后标记为非活跃
            if self.x < -50 or self.x > SCREEN_WIDTH + 50 or self.y > SCREEN_HEIGHT + 50:
                self.active = False
    
    def reset(self):
        """重置小鸟位置"""
        self.x = self.start_x
        self.y = self.start_y
        self.velocity_x = 0
        self.velocity_y = 0
        self.launched = False
        self.dragging = False
        self.trail_particles = []
        self.active = True
    
    def launch(self, power_x, power_y):
        """发射小鸟"""
        launch_power = 0.8
        self.velocity_x = power_x * launch_power
        self.velocity_y = power_y * launch_power
        self.launched = True
        self.dragging = False
        self.active = True
    
    def check_collision(self, sheep):
        """检测与小羊的碰撞"""
        if not self.active or not self.launched:
            return False
            
        distance = math.sqrt((self.x - sheep.x) ** 2 + (self.y - sheep.y) ** 2)
        return distance < self.radius + sheep.radius + 5