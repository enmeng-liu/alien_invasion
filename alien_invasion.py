import sys, pygame

def run_game():
  pygame.init()
  screen = pygame.display.set_mode((1200, 800))
  pygame.display.set_caption("Alien Invasion")
  
  # set background color
  bg_color = (200, 200, 200)

  # main loop
  while True:
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
    # 每次循环时重绘屏幕
    screen.fill(bg_color)
    # 让最近绘制的屏幕可见
    pygame.display.flip()

run_game()