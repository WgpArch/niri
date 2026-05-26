# 📊 Waybar & Scripts

Because a single bar couldn't comfortably fit 11 workspaces alongside system metrics on a standard laptop screen, this setup uses a **Dual Waybar** approach, launched directly from `config.kdl`.

## The Dual Bar Setup

### Top Bar (Status Bar)
- **Config:** `~/.config/waybar/config` & `style.css`
- **Position:** Top Center
- **Modules:** The top bar uses only `modules-center` to create a clean, floating aesthetic.
  - Arch Linux Launcher, Clock, Weather, Tray, Temperature, CPU, Memory, Pulseaudio, Battery, Backlight, Network, Notifications, Power Profiles, Power Button.

### Bottom Dock (Workspace Bar)
- **Config:** `~/.config/waybar/config-bottom` & `style-bottom.css`
- **Position:** Bottom Center with 300px left/right margins, creating a floating "dock" effect.
- **Modules:** `niri/workspaces` only.
- **Icons:** Workspaces are mapped to Nerd Font icons based on intended use:

| WS | Icon | Intended App |
| :--- | :--- | :--- |
| 1 | 󰈹 | Browser |
| 2 |  | Mail |
| 3 | 󰎆 | Discord |
| 4 |  | Spotify |
| 5 | 󰖣 | Chat |
| 6 | 󰧮 | Games |
| 7 | 󰎄 | Video |
| 8 | 󰝚 | Music |
| 9 |  | Youtube |
| 10 | 󰎈 | Photos |
| 11 |  | Files |

## 📜 Key Scripts

Located in `~/.config/niri/scripts/`:

| Script | Description |
| :--- | :--- |
| `screenshot_niri.sh` | Custom screenshot utility. |
| `launcher.sh` | Rofi application launcher wrapper. |
| `powermenu.sh` | Rofi power/logout menu wrapper. |
| `weather.py` | Fetches weather data for the Waybar module. |
