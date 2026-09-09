### SSH Bootstrap - SOC Access

The SOC disabled the browser terminal for this host. You must come in over SSH, inside tmux.

1. Locally (WSL or any terminal): `ssh-keygen -t ed25519`, copy `~/.ssh/id_ed25519.pub`.
2. pwn.college `Profile -> Settings -> SSH Key`, paste it.
3. `Workspace -> Start` this challenge, copy the `ssh hacker@...` command.
4. `ssh hacker@<instance>` then `tmux new -s ir`.
5. Run `/challenge/check` - it refuses browser and non-tmux.

Fallback: if you skipped WSL, use the browser terminal for steps 3-5 to learn tmux, then redo over SSH for the flag.

Solve: `SSH_CONNECTION` + `TMUX` env must exist. Talk point: IR is always remote + persistent.
