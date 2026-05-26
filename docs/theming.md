# 🎨 Window Rules & Theming

Niri uses the KDL configuration language, allowing for highly readable and structured window rules. This setup includes extensive rules for a seamless desktop experience.

## Look & Feel
- **Layout:** Scrollable Tiling
- **Gaps:** 7px
- **Border Width:** 2px
- **Active Border:** `#cba6f7` (Catppuccin Mauve)
- **Inactive Border:** `#6c7086` (Catppuccin Surface2)
- **Focus Ring:** Disabled (Uses border instead)
- **Window Corners:** 8px radius, clipped to geometry.
- **Default Opacity:** 0.95 (Slight transparency)

## Window Rules Highlights
Window rules are defined in `config.kdl` to automatically handle sizing, floating, and opacity for specific applications:

- **Browsers (Floorp, Brave):** Set to a fixed wide width (1425px) to prevent jittering.
- **Media/OFFICE (OBS, OnlyOffice):** Set to a fixed comfortable width (1256px).
- **Floating Apps:** Seahorse, Galculator, NM-connection-editor, Xarchiver, Pavucontrol, Stacer, and Rofi automatically open floating.
- **Kitty tty-clock:** Opens tiled but sized to 30% and positioned top-right, acting like a desktop widget.

## Input Devices
- **Keyboard:** Layout `us` with `ctrl:nocaps` (Caps Lock acts as Ctrl). Repeat rate 30, delay 350.
- **Touchpad:** Tap-to-click, natural scrolling, flat acceleration, two-finger scroll.
- **Mouse:** Adaptive acceleration, middle emulation enabled.
- **Cursor:** Adwaita theme, size 25. Hides after 5 seconds of inactivity.

## Environment Variables
The config sets strict Wayland-first environment variables for Qt, GTK, SDL, and Clutter apps, forcing them to use Wayland natively while X11 apps fall back to `xwayland-satellite` (Display :1).
