<div align="center">

  <img src="https://img.shields.io/badge/Arch_Linux-1793D1?style=for-the-badge&logo=arch-linux&logoColor=white" alt="Arch Linux">
  <img src="https://img.shields.io/badge/Wayland-00B4F0?style=for-the-badge&logo=wayland&logoColor=white" alt="Wayland">
  <img src="https://img.shields.io/badge/Niri-FFFFFF?style=for-the-badge&logo=linux&logoColor=black" alt="Niri">
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License">

  <br><br>

  Scrollable-tiling Wayland Compositor with KDL configuration.

</div>

---

## ✨ Features
- **Config:** Modular `config.kdl` and `keybinds.kdl` setup.
- **Scripts:** Custom bash/python utilities for power management, screenshots, and weather.
- **Launcher:** Rofi integration with custom themes (`launcher.rasi`).
- **Structure:** Clean separation of configs and scripts.

## 📂 Structure
```text
~/.config/niri/
├── config.kdl       # Main compositor configuration
├── keybinds.kdl     # Keybinding definitions
└── scripts/         # Utility scripts
    ├── launcher.sh  # Rofi launcher script
    ├── powermenu.sh # Shutdown/reboot menu
    └── weather.py   # Weather widget data

⚙️ Installation
git clone https://codeberg.org/WgpArch/niri.git ~/.config/niri
ln -sf ~/.config/niri/configs/* ~/.config/

## 📸 Screenshots
