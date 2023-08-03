# notion-to-do-list

Populate your desktop wallpaper with your to-do list in Notion automatically using Notion API. Borrows from the [Bannerbear Guide](https://www.bannerbear.com/blog/how-to-set-your-notion-to-do-list-as-desktop-wallpaper-automatically-free-notion-template/).

## Setup

- Create a `.env` file and define `NOTION_KEY` and `NOTION_DATABASE_ID` variables, according to the [Notion Integration Guide](https://developers.notion.com/docs/create-a-notion-integration).
- Install necessary node modules with `npm install`.
- Add a `template.jpg` inside the `assets` folder to use as a template wallpaper.

## Usage

Inside the `scripts` folder.

- Run the `update.sh` shell script.
- Run the `update.ps` powershell script.

You can also automate the last two steps using your local task scheduler (like `taskschd.msc`).
