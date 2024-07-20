# Code completion in vim using anthropic's Claude
This plugin is designed to help vim user workflow by using anthropic's Claude generativeAI models to create code.
After using github's copilot I found it to be a little intrusive and expensive.

This plugin requires you to pay athropic per token, the cost depends on your usage.
As a benchmark I've invoked the plugin ~45 times per day, based on my usage this has so far equated to ~$0.11 per day.
Based on my usage this is more cost effective compared against githubs copilot.

This plugin has far less features than github's copilot and is not intended to be a competitor. 
This was created for my own use based on my preferences.


# Using the plugin
To invoke code generation ":C ...insert your request here..." into the vim status line. 
Code will be inserted into the file from the point the cursor is currently located.

# Setup
This vim plugin is configured to autoload when vim is run, a package manager is not used to install or manage this plugin.

The plugin is written in python and requires any version of vim that support python3.
On my mac with macOS Sonoma 14.5 I had to use brew to install the latest version of vim.

```
> brew install vim
> brew link vim
```

To use this plugin you will need to have an anthropic account and an API key.
The API key from anthropic will need to be stored as an environment variable.

## Plugin install steps:
1. Clone this repo to your vim plugin folder
   ```
   ~/.vim/plugin/
   ```

2. The plugin requires python and the anthropic library installed.
   ```
   > pip3 install anthropic
   ```
 
3. Create your anthropic API key and add it to an environment variable named "ANTHROPIC_KEY"
   ```
   > export ANTHROPIC_KEY=xxxxxxxxxxxx
   ```

4. run vim
   ```
   > vim test.py
   ```
   test out code completion
   ```
   :C create class for managing integration of numpy arrays
   ```

# Component versions
Developed and tested with the following versions:

OS:
macOS Sonoma 14.5

python:
python 3.12

Anthropic:
python library version 0.31.2

vim:
VIM - Vi IMproved 9.1 (2024 Jan 02, compiled Jul 18 2024 18:40:28)
macOS version - x86_64
Included patches: 1-600


