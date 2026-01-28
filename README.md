# Stranger Things: A Text-Based Adventure Game

## Overview

**Stranger Things: A Text-Based Adventure Game** is a narrative-driven web application inspired by the *Stranger Things* universe. Built using **Flask** and **Jinja2**, the game places players in the role of **Mike Wheeler**, guiding them through a series of story-driven choices that affect health, allies, and ultimately the ending of the game.

The project focuses on immersive storytelling, clean UI design, and state-based game logic rather than traditional win/lose mechanics. Player decisions shape the experience, creating different narrative outcomes while maintaining a cohesive story flow.

This project was developed as a **CS50 final project** and demonstrates concepts such as session management, conditional rendering, and interactive UI design.

---

## Gameplay Description

The game begins in the familiar setting of Mike’s basement after a Dungeons & Dragons session with friends. Strange events begin to unfold, and the player must decide how to react. Each choice advances the story while modifying the player’s internal state.

Key gameplay elements include:

- **Health System**  
  Certain choices put the player at risk. Dangerous decisions reduce health, while cautious or strategic decisions help preserve it.

- **Allies System**  
  Characters such as Eleven can join or leave the player depending on choices. Allies directly affect the final outcome of the game.

- **Multiple Endings**  
  The game concludes with different endings based on health and allies. These endings range from victory to survival with consequences, or complete failure.

The game does not rely on random chance. All outcomes are deterministic and based on player choices, encouraging replayability and experimentation.

---

## Features

- Interactive, choice-driven narrative
- Player health tracking using Flask sessions
- Allies system that influences the ending
- Multiple narrative endings
- Typing text animation for immersive pacing
- Scene-specific background images
- Responsive and themed UI using Tailwind CSS and DaisyUI

---

## Technologies Used

### Backend
- **Python**
- **Flask** – Routing, session management, and game logic
- **Jinja2** – Dynamic HTML rendering and conditional logic

### Frontend
- **HTML**
- **Tailwind CSS**
- **DaisyUI**
- **JavaScript** – Typing animation and UI effects

---

## Project Structure

