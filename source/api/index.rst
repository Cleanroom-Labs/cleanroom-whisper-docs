API Reference
=============

.. note::

   API documentation will be auto-generated from Rust source code once implementation begins.
   This page serves as a placeholder and integration guide for future developers.

Planned Architecture
--------------------

Based on :doc:`../design/sdd`, Cleanroom Whisper uses a flat 5-file architecture:

``main.rs`` -- Entry Point
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose:** Application entry point, event loop, tray setup

**Key Components:**

- Event loop coordinating audio, transcription, and UI
- Hotkey registration via ``global-hotkey`` crate

``audio.rs`` -- Audio Capture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose:** Record WAV from microphone using cpal + hound

**Key Components:**

- ``AudioCapture`` - Main recording struct (start, stop, elapsed, level metering)
- ``list_input_devices()`` - Enumerate available audio input devices

``whisper.rs`` -- Transcription
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose:** Subprocess invocation of whisper.cpp

**Key Components:**

- ``transcribe(whisper_binary, model_path, audio_path) -> Result<String>`` - Core transcription function

``db.rs`` -- Database
~~~~~~~~~~~~~~~~~~~~~

**Purpose:** SQLite persistence for transcription history and settings

**Key Components:**

- ``Database`` - SQLite connection with CRUD operations (open, save, list, get, delete transcriptions; get/set settings)
- ``Transcription`` - Data model for stored transcriptions

``tray.rs`` -- System Tray
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose:** System tray menu construction, icon state, and notifications

**Key Components:**

- ``TrayApp`` - System tray icon, menu, and state management
- ``AppState`` - Enum: Idle, Recording, Transcribing
- ``build_menu()`` - Menu construction from app state and recent transcriptions

Developer Resources
-------------------

See `Rust API Documentation Integration Guide <../../meta/rust-integration-guide.html>`__ for doc comment guidelines, sphinxcontrib-rust configuration, and traceability linking.

Future Enhancements
-------------------

When implementation begins:

- Add ``.. impl::`` directives for each major component
- Link implementations to requirements in traceability matrix
- Auto-generate API docs with sphinxcontrib-rust
- Add code examples to test cases for validation
- Update needflow diagrams to include implementation nodes

