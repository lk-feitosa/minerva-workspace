---
name: maestri-computer
description: Control the user's computer using Maestri Computer Use. Use when the user asks you to operate external apps or use the computer for them.
user-invocable: true
---

# Maestri Computer Use

You're running inside Maestri, a spatial development workspace that connects AI agents, terminals, notes, and browser portals on a visual canvas.
The `maestri` CLI is a command-line executable pre-installed and available on PATH. If `maestri` is not found, use `"$MAESTRI_CLI"` instead; this environment variable always points to the full binary path.

`maestri computer` drives another app on the user's computer, the one running Maestri, in the background. The user's pointer never moves and the app isn't brought forward, so they keep working while you do. Name the app with `--app`, by name or app id. An app that isn't running starts in the background. Keys and clicks your terminal sends itself (SendKeys, SendInput) go to the window in front, with the user's own pointer and keyboard, so always go through `maestri computer`. If your terminal is on another machine, such as over SSH, the apps are still on the user's computer, not yours. `open` takes a path on their computer, and a screenshot's file arrives on your machine.

Every answer starts with `ok` (naming what it acted on, such as `ok: pressed checkbox "Bold"`), `warning:`, `error:` or `waiting for approval:`, and says what to do next when there is something to do. Read it before your next command. A command that needs the user's approval waits up to 20 seconds for it.

## Snapshot first

```
maestri computer snapshot --app "Media Player"
```

```
app: Media Player  window: "Media Player"  size: 1280x800pt  elements: 214
other windows: "Mini player" (pick one with --window "part of its name")
@e1 button "Back" [12,10 28x28]
@e2 search "Search" [60,52 180x24]
@e9 row "Song Title" [250,120 900x24] *focused*
```

- Only what's visible is listed. Scroll to reach the rest, or better, use the app's own search (`key "ctrl+f"`, then `type`).
- In the window you last read, an element keeps its ref while it's there; new elements get new refs, and a ref whose element is gone is refused. Snapshot again after anything that changes the window, and whenever an answer surprises you: another agent may be using the same app.
- A covered browser page may list only the browser's own controls, and snapshot warns when it does. If you need the page, `window --raise` brings it to the front and takes the keyboard from the user, so do it only then, and snapshot again.
- `--within @e6` reads just one element (a panel, a page's main column).
- Take a `screenshot` when the app draws its own content (a canvas, a chart) or to check how something looks. Its pixels are window points, the same x,y as a snapshot's, unless its answer gives a scale (a big window, or `--full` for every pixel). `--out shot.png` saves it there instead of a temp file.

## Windows

An app's windows are separate targets. Every command but `open` takes `--window "Title"`: the window named exactly that, else the only one whose name contains it. A window without a title goes by what the answers call it, such as `dialog "Save changes…"`. Several matches are refused with the names, never guessed. Without it, a command acts in the window your last action opened, else the one you last read: when an action opens a window or a dialog, the answer names it.

A ref acts in the window it was read from, even when another window is in front. An app keeps only your last snapshot's refs, so to switch windows, snapshot the other one and use its refs:

```
maestri computer snapshot --app Edge --window "Checkout"
maestri computer click --app Edge @e4
```

## Scripting

Commands are plain shell calls, so chain them when you know the steps:

```
maestri computer fill --app Outlook @e3 "Quarterly numbers" &&
maestri computer fill --app Outlook @e5 "Attached." &&
maestri computer key --app Outlook "ctrl+Enter"
```

Your commands to one app always run one at a time, in the order you sent them, even fired in parallel, and never interleave with another agent's. Different apps run side by side. Chain with `&&`: `error:` exits nonzero, so the script stops at the first failure. `warning:` and `waiting for approval:` exit zero, so read the output when the script ends. Snapshot again before a step that needs fresh refs.

## Commands

Each is `maestri computer <command> --app App [--window "Title"]`. A target is a ref (`@e3`) or `x,y` in the window's points. In PowerShell, quote refs and points (`'@e3'`, `'10,20'`): a bare `@e3` is PowerShell's splatting, and the ref never reaches `maestri`.

Pointer
- `click @e3|x,y [--button right|middle] [--count 2|3] [--modifiers ctrl,shift] [--hold ms]`. `double-click`, `right-click`: shortcuts. Pressing doesn't move keyboard focus.
- `move x,y`: hover
- `drag @e3|x,y @e5|x,y [--modifiers alt]`: sliders, splitters, shapes, inside one window even when it's covered. A drag-and-drop (files, rows, text) needs control mode.
- `scroll [@e3|x,y] [down|up|left|right] [--amount pages] [--dx px] [--dy px]`. `--amount 1` moves about 0.9 of a view, so an amount above 1 jumps past text you never saw: to read something through, use 1 or less.
- `pinch --scale 1.5 [--at x,y]`, `rotate --degrees 30 [--at x,y]`
- `draw x1,y1 x2,y2 ... | --svg "M 10 10 C ..." [--pressure 0.2-1] [--tilt x,y]`: one pen stroke per call

Keyboard
- `focus @e2`, `fill @e2 "text"` (replace), `type [@e2] "text"` (at the cursor)
- `key "Enter"|"ctrl+shift+s"`
- `key "ctrl+p" --then-type "name" --then-key Enter`: one sequence. Use it for palettes and quick open in VS Code and other Electron apps.
- `key --hold shift`: hold modifiers through your next pointer action

Menus, windows, apps
- `menu "File > Export…"`, `menu --at @e4 "Properties"` (context menu)
- `window --move x,y | --resize w,h | --minimize | --raise`
- `open [C:\path\to\file|url]`: start the app or open something in it, in the background. WSL is on the user's computer, so from WSL a Linux path works too, such as `~/report.pdf`. If Edge is already running, go to a page by filling its address bar and pressing Enter rather than with open: open can bring Edge forward and keep it from taking typed text.
- `wait --for @e7|"Done"|change [--timeout 15]`
- `apps`: running apps and which you may use

Files to the Recycle Bin: select them, then `key --app "File Explorer" "Delete"`. Pressing a button on File Explorer's toolbar brings its window forward for a moment. Right after clicking a row, `Delete`, `ctrl+x` and `ctrl+c` work without that, and `ctrl+v` can bring the window forward while it copies.

## Control mode: the whole computer

For when the user is away and only the real pointer and keyboard will do: the taskbar, the Start menu, the system tray's icons, system dialogs, or when the user asks. `maestri computer control` asks the user once. Then `click`, `drag`, `type`, `key` and the rest act without `--app`, on `screenshot [--display N]` pixels. If the user moves the mouse or types, control pauses (`paused:`); wait until they've left it alone before `control` again. One agent at a time. Always `maestri computer release` when you're done.