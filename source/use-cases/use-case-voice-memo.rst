Use Case: Quick Voice Memo
==========================

**Scenario:** Capture quick thoughts, reminders, or ideas as text without typing.

**Actor:** Individual user working at computer

**Trigger:** Press global hotkey to start recording

.. usecase:: Quick Voice Memo
   :id: UC-WHISPER-001
   :status: approved
   :tags: whisper, voice-memo, quick-capture
   :links: FR-WHISPER-001; FR-WHISPER-003; FR-WHISPER-008; FR-WHISPER-019
   :release: v1.0

   Capture quick thoughts, reminders, or ideas as text without typing using global hotkeys.

   **Success Criteria:** Recording captured clearly, transcription accurate (>90%), available in clipboard within 10 seconds, no network usage.

Workflow
--------

1. Press ``Ctrl+Alt+R`` to start recording
2. Speak the memo (e.g., "Remember to follow up with client about proposal")
3. Press ``Ctrl+Alt+R`` to stop and transcribe
4. Review transcription in notification
5. Press ``Ctrl+Alt+C`` to copy to clipboard
6. Paste into notes app, email, or task manager

Success Criteria
----------------

- Recording captured clearly
- Transcription accurate (> 90%)
- Available in clipboard within 10 seconds
- No data sent over network
