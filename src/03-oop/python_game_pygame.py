import pygame


def main():
    """
    使用Pygame开发游戏
    :return:
    """
    # 初始化pygame
    pygame.init()
    # 初始化窗口的标题
    screen = pygame.display.set_mode((800, 600))
    # 初始化窗口标题
    pygame.display.set_caption("大鱼吃小鱼")
    # 设置窗口背景色，使用三原色进行设置
    screen.fill((242, 242, 242))
    # 绘制圆形，参数分别为：屏幕，颜色，圆形，半径，0代表填充整个圆
    pygame.draw.circle(screen, (255, 0, 0), (100, 100), 30, 0)
    # 刷新当前窗口
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()
