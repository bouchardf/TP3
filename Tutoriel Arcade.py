import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITLE = "Tutoriel Arcade"

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)

arcade.set_background_color(arcade.color.SKY_BLUE)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 2, 0, arcade.csscolor.FOREST_GREEN)

arcade.draw_rectangle_filled(200, 600 / 2, 30, 70, arcade.color.DARK_BROWN)
arcade.draw_rectangle_filled(300, 500 / 2, 30, 60, arcade.color.DARK_BROWN)
arcade.draw_rectangle_filled(400, 625 / 2, 30, 50, arcade.color.DARK_BROWN)

arcade.draw_arc_filled(400, 625 / 2 + 20, 60, 100, arcade.csscolor.ORANGE_RED, 0, 180)

arcade.draw_triangle_filled(175, 325, 225, 325 , 200, 425, arcade.color.HUNTER_GREEN)

arcade.finish_render()



arcade.run()