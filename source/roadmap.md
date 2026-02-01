# Project Roadmap

Build a transcription app you want to use. Share it with the world. See what happens.

<br>

**Guiding document:** [Principles](https://cleanroomlabs.dev/docs/meta/principles.html)

## v1.0.0 Release

**Release Goal:** This project will reach v1.0.0 as part of a coordinated release with AirGap Deploy and AirGap Transfer.

**v1.0.0 Scope:** The MVP features documented in this roadmap.

**Cross-Project Integration:** v1.0.0 validates the integrated transcription deployment workflow works end-to-end.

**Release Coordination:** See [Release Roadmap](https://cleanroomlabs.dev/docs/meta/release-roadmap.html) for cross-project timeline and integration milestones.

<br>

**Target:** Suite Milestone 5 (Month 10) — MVP Complete

**Note:** Development begins after AirGap Transfer is complete (Suite Milestone 5).

## Current Status

**Phase:** Preliminary Planning Complete

**Next:** Finalize plan and begin MVP implementation

Requirements, design, and test specifications need some minor adjustments and a final review.

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

**Target:** Suite Milestone 5 (early)

**Goal:** Tray icon appears.

- [ ] Create Cargo project with dependencies
- [ ] Create module files per SDD architecture
- [ ] Initialize system tray with placeholder icon
- [ ] Verify app runs and shows tray icon

**Done when:** Tray icon visible, right-click shows "Quit".

### Milestone 2: Recording

**Target:** Suite Milestone 5

**Goal:** Record voice to WAV file.

- [ ] List audio input devices
- [ ] Capture from default device
- [ ] Write samples to WAV (16kHz mono)
- [ ] Left-click tray toggles recording
- [ ] Tray icon changes when recording (red)
- [ ] Show recording duration in tray menu
- [ ] Configurable recording duration limit (default: 120 min)
- [ ] Audio input device selection in settings

**Done when:** Can record, find WAV file, play in system player.

### Milestone 3: Transcription

**Target:** Suite Milestone 5

**Goal:** Get text from whisper.cpp.

- [ ] Settings stored in SQLite
- [ ] Settings dialog for whisper binary path
- [ ] Settings dialog for model path
- [ ] Validate both paths exist
- [ ] Invoke whisper.cpp with configured paths
- [ ] Capture and parse stdout for transcription text
- [ ] Show notification with result preview
- [ ] Handle transcription errors with system notification

**Done when:** Record → notification shows text.

### Milestone 4: Persistence

**Target:** Suite Milestone 5

**Goal:** Save transcriptions, survive restart.

- [ ] Initialize SQLite in app data directory
- [ ] Create tables on first run (see SDD schema)
- [ ] Save transcription after whisper completes
- [ ] Load recent transcriptions into tray menu
- [ ] Click menu item copies text to clipboard
- [ ] "View History" opens native dialog with full list
- [ ] Delete transcription from history dialog
- [ ] Export transcription as .txt file from history dialog

**Done when:** Close app, reopen, history still there.

### Milestone 5: Hotkeys

**Target:** Suite Milestone 5

**Goal:** Control without touching mouse.

- [ ] Register `Ctrl+Alt+R` for toggle recording
- [ ] Register `Ctrl+Alt+C` for copy last transcription
- [ ] Settings dialog to change hotkeys
- [ ] Handle registration failures gracefully

**Done when:** Can record and copy without touching mouse.

### Milestone 6: Polish

**Target:** Suite Milestone 5 (Month 10) — MVP Complete

**Goal:** Comfortable daily use.

- [ ] First-run: prompt for whisper paths if not set
- [ ] Error notification when whisper not found
- [ ] Error notification when recording fails
- [ ] Show timestamp and preview on menu items
- [ ] Tray icon shows busy state during transcription
- [ ] Settings persist between runs
- [ ] Sanitize file paths (reject `..`)
- [ ] Use parameterized database queries
- [ ] Verify no network calls under any circumstance
- [ ] Offline build dependencies (cargo vendor)
- [ ] Single-directory deployment support

**Done when:** Use it for a week without frustration.

### Milestone 7: Testing & Documentation

**Target:** Suite Milestone 5 (Month 10) — MVP Complete

**Goal:** Comprehensive testing and documentation

**Unit Tests:**

- [ ] Audio recording (device selection, WAV format)
- [ ] Transcription (whisper.cpp invocation, output parsing)
- [ ] Database (CRUD operations, transactions, parameterized queries)
- [ ] Settings (persistence, validation, hotkey configuration)
- [ ] Security (path sanitization, no network calls)

**Integration Tests:**

- [ ] End-to-end: record → transcribe → save → retrieve
- [ ] Multi-platform testing (Linux, macOS, Windows via CI)
- [ ] Error scenarios (missing whisper binary, permission denied, disk full)
- [ ] History management (large databases, deletion, export)

**Documentation:**

- [ ] API documentation (rustdoc)
- [ ] User guide — Getting started, configuration, usage
- [ ] Developer guide — Architecture, contributing
- [ ] Deployment guide — Air-gap installation with AirGap Deploy

**CI/CD:**

- [ ] Run tests on Linux, macOS, Windows
- [ ] Clippy lints (deny warnings)
- [ ] rustfmt checks
- [ ] cargo-deny license checks
- [ ] Release automation (GitHub releases)

**Done when:** 80%+ code coverage, complete documentation, CI/CD pipeline.

## Definition of Done

MVP is complete when:

- [ ] Press hotkey → recording starts (tray icon changes)
- [ ] Press hotkey → notification shows transcription
- [ ] Press hotkey → last text copied to clipboard
- [ ] Recent transcriptions visible in tray menu
- [ ] Click menu item → text copied to clipboard
- [ ] Quit and reopen → history preserved
- [ ] 80%+ code coverage
- [ ] Zero clippy warnings
- [ ] All dependency licenses compatible with AGPL-3.0
- [ ] Documentation covers all use cases
- [ ] Use daily for one week without major issues

## What's NOT in MVP

Defer all of this until after shipping:

- Error recovery beyond "show notification"
- Accessibility
- Dark mode toggle (follow system is fine)
- Performance optimization
- Code signing (needed for distribution, not development)

## Key Documents

| Document | Purpose |
|----------|---------|
| [Principles](https://cleanroomlabs.dev/docs/meta/principles.html) | Design principles (read first) |
| [Requirements (SRS)](requirements/srs) | Functional and non-functional requirements |
| [Design (SDD)](design/sdd) | Architecture and component design |
| [Test Plan](testing/plan) | Test cases with traceability |

## See Also

- [Meta-Architecture](https://cleanroomlabs.dev/docs/meta/meta-architecture.html) — How Cleanroom Whisper fits in the AirGap suite
- [Specification Overview](https://cleanroomlabs.dev/docs/meta/specification-overview.html) — Project statistics and traceability overview
- [AirGap Deploy](https://cleanroomlabs.dev/docs/airgap-deploy/readme.html) — Deployment packaging tool
- [AirGap Transfer](https://cleanroomlabs.dev/docs/airgap-transfer/readme.html) — Large file transfer companion tool

## Progress Log

| Date | Activity |
|------|----------|
| 2026-01-28 | Created specification and documentation |
| 2026-01-31 | Updated roadmap to align with 6-milestone release plan |
