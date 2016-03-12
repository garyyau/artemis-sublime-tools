# Artemis Sublime Tools
Artemis Sublime Tools is a plugin containining tools that were designed to be used in Sublime Text to help assist the Artemis project. Go to **Commands** for a full list of tools in this plugin.

## Installation
- **Open Jasmine Unit Test Command**
  1. Clone this project into your Sublime Packages Folder (Preferences > Browse Packages)
  2. Edit your .sublime-project file and add the `project_paths` setting object with paths the JavaScript src directory and Jasmine Unit Test spec directory

  **Example:**
  ```
  {
  	"project_paths": {
  		"jasmine_spec": "C:\\Sites\\artemis\\src\\SuperShotgun\\javascript\\src",
  		"javascript_src": "C:\\Sites\\artemis\\src\\SuperShotgun\\javascript\\spec",
      },
  }
  ```

## Commands
Press `Ctrl+Shift+P` and type one of the following commands

### Artemis: Open Jasmine Unit Test
Creates and opens a new tab in Sublime Text containing the Jasmine spec file of the JavaScript file that was active.

**Example:**

* Open `..\src\page_scripts\breakdowns\models\validator\breakdown_shot_validator.js`
* Press `Ctrl+Shift+P` and type in **Artemis: Open Jasmine Unit Test**
* `..\spec\page_scripts\breakdowns\models\validator\breakdown_shot_validator_spec.js` file will be created and opened on Sublime Text
  








         