#!/usr/bin/env bash
dir="$HOME/.config/niri/scripts"
theme='launcher'

rofi \
    -show drun \
    -theme ${dir}/${theme}.rasi \
    -hover-select \
    -me-select-entry "" \
    -kb-cancel Escape \
    -layer overlay \
    -me-accept-entry MousePrimary
