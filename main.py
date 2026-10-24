import pygame, sys
from algorithms import sort_steps

pygame.init()
W, H = 900, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("DAA | Sorting Lab")
clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 21)
small = pygame.font.SysFont("arial", 16)
title = pygame.font.SysFont("arial", 30, bold=True)

BG = (15, 23, 42)
PANEL = (30, 41, 59)
INK = (226, 232, 240)
MUTED = (148, 163, 184)
BLUE = (59, 130, 246)
CYAN = (34, 211, 238)
GREEN = (52, 211, 153)
RED = (251, 113, 133)
AMBER = (251, 191, 36)

names = ["Bubble Sort", "Selection Sort", "Insertion Sort",
         "Merge Sort", "Quick Sort"]
chosen = names[0]
typed = "8, 3, 5, 1, 9, 2"
frames, pos, running, frame_time = [], 0, False, 0
note, focused = "Choose a sort and click Visualize.", True


def label(s, x, y, color=INK, f=font):
    screen.blit(f.render(str(s), True, color), (x, y))


def panel(rect, color=PANEL):
    pygame.draw.rect(screen, color, rect, border_radius=10)


def btn(rect, name, active=False):
    panel(rect, BLUE if active else PANEL)
    pygame.draw.rect(screen, (71, 85, 105), rect, 1, border_radius=10)
    image = small.render(name, True, INK)
    screen.blit(image, image.get_rect(center=rect.center))


def start():
    global frames, pos, running, note
    try:
        nums = [int(n) for n in typed.replace(",", " ").split()]
        if not nums or len(nums) > 16:
            raise ValueError
        frames = sort_steps(nums, chosen)
        pos, running = 0, True
        note = "Sorting animation started!"
    except ValueError:
        note = "Enter 1-16 whole numbers separated by commas or spaces."


def draw_array():
    if not frames:
        label("Your animated array appears here.", 280, 325, MUTED)
        return

    values, action, ids, comps, moves = frames[pos]
    bw, gap = min(64, 730 // len(values)), 10
    x0 = (W - (len(values) * bw + (len(values)-1) * gap)) // 2

    for i, value in enumerate(values):
        color = GREEN if action == "Sorted" else BLUE
        if i in ids:
            color = AMBER if action == "Compare" else RED

        rect = pygame.Rect(x0+i*(bw+gap), 300, bw, 62)
        panel(rect, color)
        image = font.render(str(value), True, BG)
        screen.blit(image, image.get_rect(center=rect.center))
        label(i, rect.centerx-4, 369, MUTED, small)

    label("ACTION", 55, 410, MUTED, small)
    label(action, 55, 432, CYAN)
    label("COMPARISONS", 270, 410, MUTED, small)
    label(comps, 270, 432)
    label("MOVES / SWAPS", 480, 410, MUTED, small)
    label(moves, 480, 432)
    label(f"STEP {pos+1}/{len(frames)}", 690, 432, MUTED, small)


def draw():
    screen.fill(BG)
    label("SORTING LAB", 30, 22, CYAN, title)
    label("DESIGN & ANALYSIS OF ALGORITHMS", 32, 60, MUTED, small)

    panel(pygame.Rect(25, 95, 850, 135))
    label("01  SELECT ALGORITHM", 45, 110, MUTED, small)

    for i, name in enumerate(names):
        x, y = 45+(i%3)*265, 140+(i//3)*42
        btn(pygame.Rect(x, y, 235, 34), name, name == chosen)

    panel(pygame.Rect(25, 245, 850, 230))
    label("02  INPUT ARRAY", 45, 258, MUTED, small)

    box = pygame.Rect(45, 282, 810, 39)
    panel(box, BG)
    pygame.draw.rect(screen, CYAN, box, 1, border_radius=7)
    label(typed, 58, 290, INK, small)

    draw_array()

    btn(pygame.Rect(25, 490, 145, 42), "VISUALIZE", True)
    btn(pygame.Rect(183, 490, 115, 42), "PAUSE")
    btn(pygame.Rect(311, 490, 115, 42), "RESET")
    label(note, 25, 550, MUTED, small)
    label("ESC  EXIT", 770, 550, MUTED, small)
    pygame.display.flip()


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if e.type == pygame.KEYDOWN and focused:
            if e.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif e.key == pygame.K_BACKSPACE:
                typed = typed[:-1]
            elif e.key == pygame.K_RETURN:
                start()
            elif e.unicode in "0123456789,- ":
                typed += e.unicode

        if e.type == pygame.MOUSEBUTTONDOWN:
            x, y = e.pos
            focused = pygame.Rect(45, 282, 810, 39).collidepoint(x, y)

            for i, name in enumerate(names):
                r = pygame.Rect(45+(i%3)*265, 140+(i//3)*42, 235, 34)
                if r.collidepoint(x, y):
                    chosen = name
                    note = "Selected " + name

            if pygame.Rect(25, 490, 145, 42).collidepoint(x, y):
                start()
            elif pygame.Rect(183, 490, 115, 42).collidepoint(x, y):
                running = not running
            elif pygame.Rect(311, 490, 115, 42).collidepoint(x, y):
                frames, pos, running = [], 0, False
                note = "Reset complete."

    if running and frames:
        if pygame.time.get_ticks() - frame_time > 280:
            if pos < len(frames)-1:
                pos += 1
            else:
                running, note = False, "Sorting complete!"
            frame_time = pygame.time.get_ticks()

    draw()
    clock.tick(60)