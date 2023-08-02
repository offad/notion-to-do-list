import { getTodoTasks } from './notion.js';

async function update() {
    // Step 1. Get the To-do List from the Notion Database
    var result = await getTodoTasks();
    console.log(result);

    // Step 2. Update Sticky Notes
}

update();