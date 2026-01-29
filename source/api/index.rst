API Reference
=============

.. note::

   API documentation will be auto-generated from Rust source code once implementation begins.
   This page serves as a placeholder and integration guide for future developers.

Planned Architecture
--------------------

Based on :doc:`../design/sdd`, Cleanroom Whisper will consist of these modules:

Audio Module (``audio``)
~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose:** Audio capture and recording

**Key Components:**

- ``AudioRecorder`` - Main recording interface
- ``AudioDevice`` - Platform-specific audio device abstraction
- ``AudioBuffer`` - Circular buffer for audio data

Whisper Module (``whisper``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose:** Integration with whisper.cpp for transcription

**Key Components:**

- ``WhisperEngine`` - Wrapper around whisper.cpp binary
- ``ModelManager`` - Manages available whisper models
- ``TranscriptionJob`` - Represents a transcription task

Database Module (``db``)
~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose:** SQLite persistence for transcription history

**Key Components:**

- ``Database`` - SQLite connection and query interface
- ``Transcription`` - Data model for stored transcriptions
- ``HistoryManager`` - CRUD operations for transcription history

Tray Module (``tray``)
~~~~~~~~~~~~~~~~~~~~~~~

**Purpose:** System tray interface and hotkey management

**Key Components:**

- ``TrayIcon`` - System tray icon and menu
- ``HotkeyManager`` - Global hotkey registration
- ``Settings`` - User configuration management

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

