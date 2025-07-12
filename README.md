# 🎮 Tic-Tac-Toe GUI Game

A beautiful and interactive graphical tic-tac-toe game built with Python and Pygame! 🐍✨

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![Pygame](https://img.shields.io/badge/pygame-v2.0+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## 📋 Table of Contents
- [About](#about)
- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Controls](#controls)
- [Game Rules](#game-rules)
- [Technical Details](#technical-details)
- [Contributing](#contributing)

## 🎯 About
This is a modern, visually appealing tic-tac-toe game with a graphical user interface built using Pygame. Features smooth animations, colorful graphics, and intuitive mouse controls for an enhanced gaming experience!

## ✨ Features
- 🎨 **Beautiful GUI** with smooth graphics and animations
- 🖱️ **Mouse controls** - click to place symbols
- 🎯 **Visual feedback** for current player and game state
- 🏆 **Winner detection** with animated winning line
- 🤝 **Tie game handling** with full board detection
- 🔄 **Easy restart** functionality (press R)
- 🎪 **Smooth 60 FPS** gameplay
- 🌈 **Color-coded players** (X=Red, O=Blue)
- 💚 **Green winning line** highlight
- ✨ **Semi-transparent overlays** for game over screen

## 📸 ASCII Preview (Not the screenshot)

### Game Start
```
┌─────────────────────────────────────────────────────┐
│                                                     │
│              Player X's Turn                        │
│                                                     │
│        ┌─────────┬─────────┬─────────┐             │
│        │         │         │         │             │
│        │         │         │         │             │
│        │         │         │         │             │
│        └─────────┴─────────┴─────────┘             │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Game in Progress
```
┌─────────────────────────────────────────────────────┐
│                                                     │
│              Player O's Turn                        │
│                                                     │
│        ┌─────────┬─────────┬─────────┐             │
│        │    ╲    │         │    ○    │             │
│        │   ╱ ╲   │         │  ○   ○  │             │
│        │  ╱   ╲  │         │ ○     ○ │             │
│        └─────────┴─────────┴─────────┘             │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Winner Screen
```
┌─────────────────────────────────────────────────────┐
│                                                     │
│                Player X Wins! 🎉                   │
│                                                     │
│        ┌─────────┬─────────┬─────────┐             │
│        │    ╲    │    ○    │    ╲    │             │
│        │   ╱ ╲   │  ○   ○  │   ╱ ╲   │ ═══════     │
│        │  ╱   ╲  │ ○     ○ │  ╱   ╲  │ (winning)   │
│        └─────────┴─────────┴─────────┘             │
│                                                     │
│              Press R to restart                     │
│                                                     │
└─────────────────────────────────────────────────────┘
```

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- Pygame library

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/tic-tac-toe-gui.git
   cd tic-tac-toe-gui
   ```

2. **Install Pygame**:
   ```bash
   pip install pygame
   ```

3. **Run the game**:
   ```bash
   python tic_tac_toe_gui.py
   ```

## 🎲 How to Play
1. **Launch the game** - A 600x600 pixel window will open
2. **Click any empty cell** to place your symbol
3. **Take turns** - X goes first (red), then O (blue)
4. **Win condition** - Get three symbols in a row (horizontal, vertical, or diagonal)
5. **Restart anytime** - Press R to start a new game
6. **Quit** - Press ESC or close the window

## 🎮 Controls
| Key/Action | Function |
|------------|----------|
| 🖱️ **Left Click** | Place symbol in clicked cell |
| ⌨️ **R Key** | Restart the game |
| ⌨️ **ESC Key** | Quit the game |
| ❌ **Close Window** | Exit the application |

## 📖 Game Rules
- 🎯 **Objective**: Be the first to get 3 of your symbols in a row
- 🔢 **Grid**: 3x3 board with 9 cells
- 👥 **Players**: Two players alternate turns (X starts first)
- 🏁 **Winning**: Three in a row horizontally, vertically, or diagonally
- 🤝 **Tie**: All 9 cells filled with no winner
- 🔄 **Restart**: Press R key anytime to start over

## 🛠️ Technical Details

### Requirements
- **Python**: 3.6+
- **Pygame**: 2.0+
- **Operating System**: Windows, macOS, Linux

### Performance
- **Frame Rate**: 60 FPS
- **Resolution**: 600x600 pixels
- **Memory Usage**: < 50MB
- **CPU Usage**: Minimal (< 5%)

### Architecture
- **Object-Oriented Design**: Clean TicTacToeGUI class
- **Event-Driven**: Pygame event handling
- **Modular Functions**: Separate methods for drawing, logic, and input
- **Efficient Rendering**: Only updates when necessary

### File Structure
```
tic-tac-toe-gui/
├── tic_tac_toe_gui.py    # Main game file
├── README.md             # This file
└── requirements.txt      # Dependencies
```

## 🎨 Visual Elements
- **X Symbols**: Red diagonal lines with smooth anti-aliasing
- **O Symbols**: Blue circles with consistent thickness
- **Grid Lines**: Black lines with professional spacing
- **Background**: Clean white background
- **Winning Line**: Green highlight line through winning combination
- **Text**: Clear, readable fonts for game status
- **Overlays**: Semi-transparent effects for game over screen

## 🔧 Customization
You can easily customize the game by modifying these constants in the code:
- `WINDOW_SIZE`: Change window dimensions
- `SYMBOL_WIDTH`: Adjust symbol thickness
- `SYMBOL_MARGIN`: Modify symbol size
- Color constants: `RED`, `BLUE`, `GREEN`, etc.

## 🤝 Contributing
Contributions are welcome! Ideas for enhancements:
- 🤖 **AI opponent** with different difficulty levels
- 🎵 **Sound effects** for moves and wins
- 🏆 **Score tracking** across multiple games
- 🎨 **Theme selection** (dark mode, different colors)
- 📱 **Responsive design** for different screen sizes
- 🌐 **Online multiplayer** functionality

Feel free to:
- 🐛 Report bugs
- 💡 Suggest new features
- 🔧 Submit pull requests
- ⭐ Star the repository if you like it!

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎉 Acknowledgments
- Thanks to the Pygame community for excellent documentation
- Inspired by the classic tic-tac-toe game
- Built with ❤️ and Python

---

**Ready to play?** Install Pygame and start gaming! 🎮

```bash
pip install pygame
python tic_tac_toe_gui.py
```

*Click, play, and have fun!* 🎯✨

## 🔗 Related Projects
- [Command-Line Tic-Tac-Toe](../tic-tac-toe-console) - Text-based version
- [Web Tic-Tac-Toe](../tic-tac-toe-web) - Browser-based version
