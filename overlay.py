import pygame
import win32api, win32con, win32gui

class Overlay:
    def __init__(self, window_name=None):
        self.window_name = window_name
        self.clear = (255, 192, 203)

        # Init pygame
        pygame.init()
        pygame.font.init()

        self.overlay = pygame.display.set_mode((self.get_window()[2], self.get_window()[3]), pygame.NOFRAME)
        self.font = pygame.font.SysFont('Arial', 20)
        self.hwnd = pygame.display.get_wm_info()['window']

        pygame.display.set_caption('python-overlay')
        
        # Set window properties
        win32gui.SetWindowLong(self.hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(self.hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
        win32gui.SetLayeredWindowAttributes(self.hwnd, win32api.RGB(*self.clear), 0, win32con.LWA_COLORKEY) # Transparency

    def update_pos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)  

        # Update overlay pos according to target window
        win32gui.SetWindowPos(pygame.display.get_wm_info()['window'], -1, self.get_window()[0], self.get_window()[1], 0, 0, 0x0001)
        self.overlay.fill(self.clear)

    def get_window(self):
        try:
            hwnd = win32gui.FindWindow(None, self.window_name)
            rect = win32gui.GetWindowRect(hwnd)
        except:
            exit(f'Target window not found ({self.window_name})')  

        # Target window measurements
        x = rect[0]; y = rect[1]
        w = rect[2] - x; h = rect[3] - y

        return x, y, w, h, hwnd

    def update(self):
        pygame.display.update()

    # Render functions
    def draw_rect(self, color, x, y, w, h, thickness=1):
        pygame.draw.rect(self.overlay, color, pygame.Rect(x, y, w, h), thickness)

    def draw_text(self, text, color, x, y, size):
        self.overlay.blit(self.font.render(text, False, color), (x, y))

    def draw_line(self, color, x, y, thickness=1):
        pygame.draw.line(self.overlay, color, x, y, thickness)