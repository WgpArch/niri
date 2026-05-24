#!/bin/sh
# Full-screen screenshot for niri, saved to ~/Pictures/Screenshots/niri/

PICTURES_DIR=$(xdg-user-dir PICTURES)
[ -z "$PICTURES_DIR" ] && PICTURES_DIR="$HOME/Pictures"

SCREENSHOT_DIR="$PICTURES_DIR/Screenshots/niri"
mkdir -p "$SCREENSHOT_DIR"

grim "$SCREENSHOT_DIR/screenshot_$(date '+%Y-%m-%d_%H-%M-%S').png"
