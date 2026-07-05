# NoSQL

This project covers the fundamentals of NoSQL databases using **MongoDB**, including
MongoDB command files (run through the `mongo` shell) and Python scripts using **PyMongo**.

## Learning Objectives

- What NoSQL means and the difference between SQL and NoSQL
- What ACID is
- What document storage is and the NoSQL types
- Benefits of a NoSQL database
- How to query, insert, update and delete information from a NoSQL database
- How to use MongoDB

## Requirements

### MongoDB Command Files
- Interpreted on Ubuntu 20.04 LTS using MongoDB (version 4.4)
- All files end with a new line
- The first line of every file is a comment: `// my comment`

### Python Scripts
- Interpreted on Ubuntu 20.04 LTS using `python3` (3.9) and `PyMongo` (4.8.0)
- All files end with a new line
- The first line is exactly `#!/usr/bin/env python3`
- Code follows the `pycodestyle` style (version 2.5.*)
- All modules and functions are documented
- Code is not executed when imported (`if __name__ == "__main__":`)

## Tasks

| File | Description |
| ---- | ----------- |
| `0-list_databases` | Lists all databases in MongoDB |
| `1-use_or_create_database` | Creates or uses the database `my_db` |
| `2-insert` | Inserts a document in the collection `school` |
| `3-all` | Lists all documents in the collection `school` |
| `4-match` | Lists documents with `name="Holberton school"` |
| `5-count` | Displays the number of documents in `school` |
| `6-update` | Adds an attribute to documents matching a name |
| `7-delete` | Deletes documents with `name="Holberton school"` |
| `8-all.py` | Lists all documents in a collection (Python) |
| `9-insert_school.py` | Inserts a new document in a collection (Python) |
| `10-update_topics.py` | Changes all topics of a school document (Python) |
| `11-schools_by_topic.py` | Returns the list of schools having a specific topic |
| `12-log_stats.py` | Provides stats about Nginx logs stored in MongoDB |

## Author

- **İzzət Məmmədov** – [izzooooooo](https://github.com/izzooooooo)
