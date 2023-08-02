import { Client } from '@notionhq/client';

const notion = new Client({ auth: process.env.NOTION_KEY });

export async function getTodoTasks() {
  
    // Dictionary for storing to-do information
    const data = {
        "Personal": [],
        "Occupation": [],
        "Others": []
    };

    // Query the database
    const response = await notion.databases.query({
        database_id: process.env.NOTION_DATABASE_ID,
        "filter": {
        "property": "Done",
        "checkbox": {
            "equals": false
        }
        },
        "sorts": [
            {
                "property": "Priority",
                "direction": "ascending"
            },
            {
                "property": "Deadline",
                "direction": "ascending"
            },
            {
                "timestamp": "created_time",
                "direction": "ascending"
            }
        ]
    });
    
    const results = response.results;
    // Organise the results that we want
    for(var i = 0; i < results.length; i++) {
        const result = results[i];
        const task = result.properties["Name"].title[0].plain_text;

        // Get all tags
        const tags = result.properties["Tags"].multi_select || []
        if (tags.length <= 0) {
            data["Others"].push(task);
        } else {
            for(var tag of tags) {
                const category = tag?.name || "Others";
                
                // Create list if it does not exist
                if (data[category] == null) {
                    data[category] = []
                }

                data[category].push(task);
            }
        }
    }

    return data;
}