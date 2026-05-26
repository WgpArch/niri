# 🛠️ Installation

This configuration relies on specific directory structures and a quirk with how Niri handles Waybar configurations.

## Prerequisites

**Core:**
- `niri`
- `xwayland-satellite` (For X11 app support)
- `waybar`
- `swaync` (Notification center)

**Utilities & Daemons:**
- `awww` (Wallpaper daemon)
- `hyprlock` (Screen lock, triggered on lid close)
- `polkit-gnome` (Authentication agent)
- `brightnessctl` & `wpctl` (Hardware control)

## ⚠️ The Waybar Quirk

Unlike Hyprland or River, **Niri is stubborn about Waybar paths.** It strictly fetches the Waybar config from `~/.config/waybar`, not from a custom subdirectory. 

Because this setup uses a dual Waybar (Top status + Bottom dock), your `~/.config/waybar` directory must contain:
- `config` & `style.css` (Top Bar)
- `config-bottom` & `style-bottom.css` (Bottom Dock)
- `color.css` & `macchiato.css` (Theme includes)

## Deploying the Config

1. Clone the repository:
        
        git clone https://codeberg.org/WgpArch/niri.git ~/.dotfiles/niri

2. Symlink the Niri configuration:
        
        ln -sf ~/.dotfiles/niri/configs/niri ~/.config/niri

3. Symlink the Waybar configuration (Crucial step!):
        
        ln -sf ~/.dotfiles/niri/configs/waybar ~/.config/waybar

4. Ensure scripts are executable:
        
        chmod +x ~/.config/niri/scripts/*
