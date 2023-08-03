#!/usr/bin/env node
import { getTodoTasks } from './notion.js';

async function update() {
    // Step 1. Get the To-do List from the Notion Database
    var result = await getTodoTasks();
    return result
}

function objToString (obj) {
    let str = '';
    for (const [p, val] of Object.entries(obj)) {
        str += `${p}::${val}\n`;
    }
    return str;
}
let result = await update()
console.clear();
let output = JSON.stringify(result);
console.log(output);