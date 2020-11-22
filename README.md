# python-overlay

transparent overlay with render functions made using pygame and pypiwin32

### features
* render functions (draw_text, draw_rect, draw_line)
* track over target window e.g. 'Untitled - Notepad'

### prerequisites
you will need to install these modules:
```sh
pip install pygame
pip install pypiwin32
```

### example usage
```py
from overlay import Overlay

overlay = Overlay(window_name='Untitled - Notepad') 

while True:
    overlay.update_pos()

    overlay.draw_rect((255, 0, 0), 200, 200, 155, 35, 5)
    overlay.draw_text('Hello world!', (179, 66, 245), 225, 205, 40)

    overlay.update() 
```
