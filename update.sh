#!/bin/sh
echo `date` : checking Notion database for updates
result=$(npm run start-windows);
echo "updating wallpaper"
python main.py "$result"
echo "saving wallpaper"