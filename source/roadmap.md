# Project Roadmap

Build a transcription app you want to use. Share it with the world. See what happens.

<br>

**Guiding document:** [Principles](https://cleanroomlabs.dev/docs/meta/principles/)

## v1.0.0 Release

**Release Goal:** This project will reach v1.0.0 as part of a coordinated release with AirGap Deploy and AirGap Transfer.

**v1.0.0 Scope:** The MVP features documented in this roadmap.

**Cross-Project Integration:** v1.0.0 validates the integrated transcription deployment workflow works end-to-end.

**Release Coordination:** See [Release Roadmap](/meta/release-roadmap) for cross-project timeline and integration milestones.

<br>

**Target Date:** June 27, 2026 (MVP Complete)

**Development Schedule:** May 26 - June 27, 2026 (5 weeks)

**Note:** Development begins after AirGap Deploy MVP is complete.

## Current Status

**Phase:** Planning Complete

**Next:** Begin MVP implementation

All requirements, design, and test specifications are complete. Ready to start Milestone 1.

<br>

**MVP Goal:** A working app you can use daily.

## MVP Scope

| Feature | Implementation |
|---------|----------------|
| Record audio | Microphone → WAV file |
| Transcribe | Shell to whisper.cpp |
| View result | Tray menu + notification |
| Copy text | Hotkey + menu click |
| History | SQLite, shown in tray menu |
| Settings | Native dialog (whisper path, model path, hotkeys) |
| Tray | Background operation, status indicator |

## Implementation Milestones

### Milestone 1: Skeleton

**Target Date:** May 30, 2026

**Goal:** Tray icon appears.

- [ ] Create Cargo project with dependencies
- [ ] Create module files per SDD architecture
- [ ] Initialize system tray with placeholder icon
- [ ] Verify app runs and shows tray icon

**Done when:** Tray icon visible, right-click shows "Quit".

### Milestone 2: Recording

**Target Date:** June 6, 2026

**Goal:** Record voice to WAV file.

- [ ] List audio input devices
- [ ] Capture from default device
- [ ] Write samples to WAV (16kHz mono)
- [ ] Left-click tray toggles recording
- [ ] Tray icon changes when recording (red)

**Done when:** Can record, find WAV file, play in system player.

### Milestone 3: Transcription

**Target Date:** June 13, 2026

**Goal:** Get text from whisper.cpp.

- [ ] Settings stored in SQLite
- [ ] Settings dialog for whisper binary path
- [ ] Settings dialog for model path
- [ ] Validate both paths exist
- [ ] Invoke whisper.cpp with configured paths
- [ ] Capture and parse stdout for transcription text
- [ ] Show notification with result preview

**Done when:** Record → notification shows text.

### Milestone 4: Persistence

**Target Date:** June 16, 2026

**Goal:** Save transcriptions, survive restart.

- [ ] Initialize SQLite in app data directory
- [ ] Create tables on first run (see SDD schema)
- [ ] Save transcription after whisper completes
- [ ] Load recent transcriptions into tray menu
- [ ] Click menu item copies text to clipboard
- [ ] "View History" opens native dialog with full list

**Done when:** Close app, reopen, history still there.

### Milestone 5: Hotkeys

**Target Date:** June 20, 2026

**Goal:** Control without touching mouse.

- [ ] Register `Ctrl+Alt+R` for toggle recording
- [ ] Register `Ctrl+Alt+C` for copy last transcription
- [ ] Settings dialog to change hotkeys
- [ ] Handle registration failures gracefully

**Done when:** Can record and copy without touching mouse.

### Milestone 6: Polish

**Target Date:** June 27, 2026 (MVP Complete)

**Goal:** Comfortable daily use.

- [ ] First-run: prompt for whisper paths if not set
- [ ] Error notification when whisper not found
- [ ] Error notification when recording fails
- [ ] Show timestamp and preview on menu items
- [ ] Tray icon shows busy state during transcription
- [ ] Settings persist between runs

**Done when:** Use it for a week without frustration.

## Definition of Done

MVP is complete when:

- [ ] Press hotkey → recording starts (tray icon changes)
- [ ] Press hotkey → notification shows transcription
- [ ] Press hotkey → last text copied to clipboard
- [ ] Recent transcriptions visible in tray menu
- [ ] Click menu item → text copied to clipboard
- [ ] Quit and reopen → history preserved
- [ ] Use daily for one week without major issues

## What's NOT in MVP

Defer all of this until after shipping:

- Tests
- CI/CD
- Documentation
- Error recovery beyond "show notification"
- Accessibility
- Dark mode toggle (follow system is fine)
- Performance optimization
- Code signing (needed for distribution, not development)

Build it. Use it. Then improve it.

## After MVP

**Personal Use** — Use it, iterate

**Share** — Post to HN, Reddit

**Sell** — $99 Apple Dev, Gumroad

**Grow** — LLC if revenue exists

## Key Documents

| Document | Purpose |
|----------|---------|
| [Principles](https://cleanroomlabs.dev/docs/meta/principles/) | Design principles (read first) |
| [Requirements (SRS)](requirements/srs) | Functional and non-functional requirements |
| [Design (SDD)](design/sdd) | Architecture and component design |
| [Test Plan](testing/plan) | Test cases with traceability |

## Progress Log

| Date | Activity |
|------|----------|
| 2026-01-28 | Created specification and documentation |
