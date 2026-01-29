Use Case: Interview Transcription
=================================

**Scenario:** Transcribe recorded interviews for analysis or documentation.

**Actor:** Researcher, journalist, or interviewer

**Trigger:** Have pre-recorded interview audio file

.. usecase:: Interview Transcription
   :id: UC-WHISPER-003
   :status: approved
   :tags: whisper, interview, long-form

   Transcribe recorded interviews for analysis or documentation, handling longer audio segments.

   **Success Criteria:** Handle longer audio segments (up to 2 hours), accurate transcription of multiple speakers, history preserved for review and editing, workflow manageable without technical expertise.

Workflow
--------

1. Play interview audio through system audio
2. Use Cleanroom Whisper to record system audio output
3. Transcribe in sections (e.g., 5-10 minute chunks)
4. Review and copy each transcription
5. Compile full transcript in document editor

Success Criteria
----------------

- Handle longer audio segments (up to 2 hours)
- Accurate transcription of multiple speakers
- History preserved for review and editing
- Workflow manageable without technical expertise
