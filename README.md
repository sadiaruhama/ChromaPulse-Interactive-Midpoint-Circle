# ChromaPulse: Interactive Midpoint Circle

A real-time, interactive graphics application built with Python and PyOpenGL. This project demonstrates the **Midpoint Circle Algorithm** and **Bresenham’s Line Algorithm**, featuring dynamic quadrant-based color shifting and pulsated animations.


## 🌟 Features

* **Midpoint Circle Implementation**: Efficiently renders circles using integer-based arithmetic.
* **Dynamic Pulsation**: The outer circle automatically expands and contracts.
* **Quadrant-Aware Coloring**: The circle's color changes dynamically based on its position within the four quadrants:
    * **Top-Right**: Yellow
    * **Top-Left**: Green
    * **Bottom-Left**: Red
    * **Bottom-Right**: Blue
* **Screen Wrapping**: The outer circle "wraps around" the screen edges, appearing on the opposite side when moved off-screen.
* **Dashed Axes**: Custom implementation of dashed lines to represent the Cartesian plane.

---

## 🎮 Controls

Take control of the visualization using your keyboard and mouse:

| Input | Action |
| :--- | :--- |
| **Spacebar** | Toggle pulsation animation (Start/Stop) |
| **Arrow Keys** | Move the circle center (Up, Down, Left, Right) |
| **Left Mouse Click** | Teleport the circle center to the clicked position |

---

## 🛠️ Installation & Setup

### Prerequisites
Ensure you have Python installed, along with the `PyOpenGL` and `PyOpenGL_accelerate` packages.

```bash
pip install PyOpenGL PyOpenGL_accelerate
