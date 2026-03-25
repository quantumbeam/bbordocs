## Document source
- Source files are all located in the docs directory.
- Texts should be basically written in |TEXT_NAME| syntax, and they are substituted on building by actual texts in /docs/vars/ja.rst(en.rst) using the include and substitute directives.
- The en.rst 


## Build 
- HTML files are built automatically with github actions on pushing to the main branch, or built locally with the command ```make ja/en```.
- The auto-rebuild-reload.py keeps observing source files, and automatically re-build HTML files when changes detected. It also launches a web server at localhost:3000 and reload the contents automatically when HTML files built.

