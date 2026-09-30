# Vityarthi Sports Management Program

## Overview

A small command-line sports player scorecard manager written in Python. The menu lets a user add player details, list all players, search by name, update a score, show the highest scorer, and delete a player. Player data is held in memory while the program is running and is cleared when it exits.

## Features

- Add a player with name, sport, age, and score.
- View all players currently entered in the session.
- Search for a player by name (case-insensitive).
- Update a player's score.
- Display the player with the highest score.
- Delete a player by name.
- Interactive numbered menu with an exit option.

## Technologies and tools

- Python 3
- Python standard library only; no third-party packages are required.
- A terminal or command prompt to interact with the menu.

## Install and run

1. Install Python 3 if it is not already available. Confirm it is on your PATH by running `python --version` (or `py --version` on Windows).
2. Save `Sport Management Program.py` in a folder you can access.
3. Open a terminal in that folder.
4. Start the program:

   ```bash
   python "Sport Management Program.py"
   ```

   On Windows, this can also be run with:

   ```powershell
   py "Sport Management Program.py"
   ```

5. Enter a menu number and follow the prompts. Choose `7` to exit.

## Testing instructions

There is no automated test suite included. Verify the program interactively:

1. Start the program and choose `2` before adding anyone; confirm it reports that no players were found.
2. Choose `1` and enter a player, for example: `Asha`, `Tennis`, `20`, `15`.
3. Add another player with a lower score.
4. Choose `2` and confirm both players appear with the entered details.
5. Choose `3`, search for `asha` in lowercase, and confirm the player is found.
6. Choose `4`, update Asha's score, then choose `2` to confirm the change.
7. Choose `5` and confirm it displays the player with the larger score.
8. Choose `6`, delete a player, and choose `2` to confirm that player is gone.
9. Try searching for a name that does not exist and enter an invalid menu choice; confirm the program displays its not-found and invalid-choice messages.
10. Choose `7` to exit.

Age and score prompts expect whole numbers. The program currently does not validate non-numeric input, and its data is not saved between runs.