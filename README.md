# Lab08 Part 2 (Bad practices)
This repository displays what NOT to do when using github with sensitive data.
Often sensitive data is found in <b>.env</b> files. In fact, the purpose of this file is to store variables exclusive to a user. If you see a <b>.env</b> file uploaded to github, it's likely a mistake. So how can we correct this mistake? The answer is to use a <i>.gitignore</i> file.
<br><br>
By including the filenames of the files you don't want uploaded in the .gitignore file, you can prevent them from ever touching github.