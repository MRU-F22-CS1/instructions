# instructions for all assignments and exercises

Instructions will be released as they are developed.

## Assignment Submission Summary
Assignment submission requires 3 steps:
1. you **push** your changes to GitHub, then
2. you **verify** your changes are now on GitHub, then
3. you **copy/paste** the URL of your GitHub repo into a D2L text box

## Git and GitHub Summary
Words in `<brackets>` are just placeholders - do not type the `<>`.
### To start an assignment
1. To start your assignment, click on the GitHub Classroom link in D2L and click "accept this assignment". Refresh the page to get your unique assignment URL.
2. On your computer, run the command `git clone <url>`, where `<url>` is your assignment URL (do not type the `<>`).

### Working on an assignment
1. Make sure your terminal (Git Bash or VS Code's integrated terminal) **working directory** is the same as your assignment directory.
2. Pull changes from GitHub, just in case:
   ```
   git pull
   ```
3. Make edits to your text file(s). Don't forget to save changes!
4. Add/commit/push changes:
   1. First, add the file(s) you want to commit to the staging area:
        ```
        git add <filename>
        ```
   2. Then, commit all the files with a message describing the changes you made:
        ```
        git commit -m "<message>"
        ```
   3. Push all your commits to GitHub
        ```
        git push
        ```
> You can add/commit/push as many times as you like up until you submit your assignment

### Final submission
1. When you are happy with the state of your code, add/commit/push one last time and go to your assignment repository URL. You can find this from the GitHub homepage after logging in.
2. Double check that the last commit on GitHub is the last one you made on your computer.
3. Copy and paste the assignment repository URL into the D2L assignment text box. This is your signal to your instructor that you are done the assignment. It should look something like:
    ```
    https://github.com/MRU-F22-CS1/assign-####-<github username>
    ```
    > There may be slight variations in how your instructor named your assignment repo

## Troubleshooting
For more details, you can also refer back to the [exercise 1](exercise1/intro_to_git_v1.md) instructions.

### Changes aren't showing on GitHub.com
Make sure that you have done all of the following:

 1. **Save the file** from your text editor.
 2. `git add <filename>`, where `<filename>` is the name of the file you are adding (e.g. `git add README.md`).
 3. `git commit -m "commit message"`, where `commit message` is a *useful* note about why you are committing the file.
 4. `git push`.

 If you still aren't seeing your changes on GitHub, make sure that you don't accidentally have multiple copies of your repo on your local computer. It's easy to accidentally edit one copy while git bash is open in another.

 And if you **still** still aren't seeing your changes, get in touch with an IA or your instructor.

### git commit opened a weird looking window
If you forget the `-m` flag and just execute the command `git commit`, git will launch a text editor. By default, this is a command-line editor called [vim](https://www.vim.org/). Command line editors are really useful and worth learning, but if you want to go back to where you were, do the following:
- Press `Esc` (escape, top-left corner of your keyboard)
- Type `:q!`. That's colon, lowercase "q", then exclamation mark.
- Press `enter`

### macOS GitHub Token
If you are using a Mac, you will need to generate a "Personal access token" from your GitHub account and then use it instead of your password. [Here](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) are GitHub's instructions, and [here's](https://www.youtube.com/watch?v=s-CN4RaNq8A) a video that walks through how to use it with the macOS Keychain Access tool. You'll need to check the "repo" box in Scope settings and set the expiry date for at least the end of the semester so you're not having to constantly regenerate it.

After generating a token you can use it instead of your GitHub password in the terminal. Copying and pasting is a bit odd as it will not actually show the text when you paste into a password prompt.

