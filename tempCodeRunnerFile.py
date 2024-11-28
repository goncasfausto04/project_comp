# no casino
def draw_button(color, hover_color, x_frac, y_frac, w_frac, h_frac, text, font):
    x = width * x_frac
    y = height * y_frac
    w = width * w_frac
    h = height * h_frac
    current_color = (
        hover_color if button_clicked(x_frac, y_frac, w_frac, h_frac, mouse) else color
    )
    pygame.draw.rect(screen, current_color, [x, y, w, h])
    text_rect = text.get_rect(center=(x + w // 2, y + h // 2))
    screen.blit(text, text_rect)


# nos credits


def draw_button(color, hover_color, x_frac, y_frac, w_frac, h_frac, text, font):
    """Draws a button on the screen with the given parameters."""

    x = width * x_frac
    y = height * y_frac
    w = width * w_frac
    h = height * h_frac
    current_color = (
        hover_color if button_clicked(x_frac, y_frac, w_frac, h_frac) else color
    )

    # Draw rounded rectangle for the button
    pygame.draw.rect(screen, current_color, [x, y, w, h], border_radius=10)

    # Draw border for the button
    border_color = white if button_clicked(x_frac, y_frac, w_frac, h_frac) else black
    pygame.draw.rect(screen, border_color, [x, y, w, h], 2, border_radius=10)

    # Draw the text on the button
    text_rect = text.get_rect(center=(x + w // 2, y + h // 2))
    screen.blit(text, text_rect)


# no interface


def draw_button(color, hover_color, x_frac, y_frac, w_frac, h_frac, text, font):
    x = width * x_frac
    y = height * y_frac
    w = width * w_frac
    h = height * h_frac
    current_color = (
        hover_color if button_clicked(x_frac, y_frac, w_frac, h_frac) else color
    )

    # Draw rounded rectangle for the button
    pygame.draw.rect(screen, current_color, [x, y, w, h], border_radius=10)

    # Draw border for the button
    border_color = white if button_clicked(x_frac, y_frac, w_frac, h_frac) else black
    pygame.draw.rect(screen, border_color, [x, y, w, h], 2, border_radius=10)

    # Draw the text on the button
    text_rect = text.get_rect(center=(x + w // 2, y + h // 2))
    screen.blit(text, text_rect)


# nas options


def draw_button(color, hover_color, x_frac, y_frac, w_frac, h_frac, text, font):
    x = width * x_frac
    y = height * y_frac
    w = width * w_frac
    h = height * h_frac
    current_color = (
        hover_color if button_clicked(x_frac, y_frac, w_frac, h_frac) else color
    )

    # Draw rounded rectangle for the button
    pygame.draw.rect(screen, current_color, [x, y, w, h], border_radius=10)

    # Draw border for the button
    border_color = white if button_clicked(x_frac, y_frac, w_frac, h_frac) else black
    pygame.draw.rect(screen, border_color, [x, y, w, h], 2, border_radius=10)

    # Draw the text on the button
    text_rect = text.get_rect(center=(x + w // 2, y + h // 2))
    screen.blit(text, text_rect)
