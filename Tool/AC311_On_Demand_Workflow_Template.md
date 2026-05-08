# AC311 On-Demand Workflow Template

This workflow is for an on-demand run, not a scheduled automation.
Run it manually whenever the user wants to begin or continue a target chapter.

## Quick Edit

Before running, update only these values:

- `TARGET_CHAPTER_NUMBER = 06`
- `TARGET_CHAPTER_LABEL = Chapter 6`
- `OUTPUT_PREFIX = chapter-06`

If you want a new chapter later, change those three values first and keep the rest of the workflow unchanged.

## Strict Workflow Mode

This template must run in `strict workflow mode`.

That means:

- work on exactly `one segment at a time`
- finish the full loop for that segment before touching the next one
- do not pre-generate later segments
- do not create the mock exam early
- do not create the HTML early
- do not batch the whole chapter into one pass

## Goal

Build a complete study package for `TARGET_CHAPTER_LABEL` through a repeated segment loop:

1. `AC311 tutor` teaches one segment of `TARGET_CHAPTER_LABEL` in high detail.
2. `AC311 tutor` gives a mini practice for that segment.
3. `AC311 tutor` provides the solution and explanation.
4. `Yuehua` reorganizes that segment into clean notes and appends it to the cumulative note set.
5. Repeat until all segments of `TARGET_CHAPTER_LABEL` are finished.
6. `AC311 tutor` creates a very difficult mixed-concept mock exam for the whole chapter.
7. `Yuehua` performs the final full-note consolidation pass.
8. `frontend developer` turns the consolidated content into an HTML lecture note.

## Required Skills

- `ac311-tutor`
- `yuehua`
- `frontend-skill`

## Working Directory

- `D:\Fogust\Workspace\College\AC311\Cheat Sheet`

## Output Files

- `D:\Fogust\Workspace\College\AC311\Cheat Sheet\segment-01.md`
- `D:\Fogust\Workspace\College\AC311\Cheat Sheet\segment-02.md`
- Continue the same pattern for later segments
- `D:\Fogust\Workspace\College\AC311\Cheat Sheet\OUTPUT_PREFIX-master-notes.md`
- `D:\Fogust\Workspace\College\AC311\Cheat Sheet\OUTPUT_PREFIX-mock-exam.md`
- `D:\Fogust\Workspace\College\AC311\Cheat Sheet\OUTPUT_PREFIX-frontend-brief.md`
- `D:\Fogust\Workspace\College\AC311\Cheat Sheet\OUTPUT_PREFIX-notes.html`

## Segment Loop Contract

For each segment, complete the following loop in order and do not skip ahead:

1. Determine the next untaught segment from `TARGET_CHAPTER_LABEL`.
2. Teach only that segment with exam-level depth in Thai, preserving English accounting terms.
3. Immediately create a mini practice for that same segment.
4. Immediately provide the worked solution with reasoning, calculations, and journal entries where relevant.
5. Save the raw segment teaching package as `segment-XX.md`.
6. Ask `Yuehua` to reorganize the raw segment into cleaner study-note form.
7. Append the refined content into `OUTPUT_PREFIX-master-notes.md` without overwriting earlier refined segments.
8. Only after step 7 is complete may the workflow move to the next segment.

Each `segment-XX.md` should contain:

- `Chapter Map Snapshot`
- `Current Segment`
- `Deep Teaching`
- `Mini Practice`
- `Solution`
- `Exam Watch`

## Completion Contract

When all segments of `TARGET_CHAPTER_LABEL` are complete:

1. Create `OUTPUT_PREFIX-mock-exam.md` with a hard mixed-concept exam.
2. Ask `Yuehua` to read all segment files, the cumulative notes, and the mock exam.
3. Save the final reorganized version as `OUTPUT_PREFIX-master-notes.md`.
4. Save a build brief for the HTML pass as `OUTPUT_PREFIX-frontend-brief.md`.
5. Create `OUTPUT_PREFIX-notes.html` based on the final brief and note set.

Completion gate:

- Steps in this section are forbidden until every segment has already completed the full segment loop.
- If even one segment is still unfinished, return to the segment loop instead of entering completion work.

## Visual Direction For HTML

The final HTML must follow this direction:

- minimal
- exam-focused
- warm but not sweet
- practical for revision without feeling cold

Design constraints:

- cream and light brown as the primary base
- gray-blue as the secondary information layer
- clear hierarchy for headings and summary boxes
- journal entry blocks should stand out but remain restrained
- subtle paper-like texture across the page
- use `TH Sarabun New` as the primary font for the whole page
- typography should feel soft, gentle, and easy on the eyes
- overall feel should balance `warm but not sweet` with `exam-ready but not rigid`

Font rule:

- Use `TH Sarabun New` for body text, headings, note blocks, and journal-entry sections.
- Do not switch to another display font unless the user explicitly asks.
- If a fallback is absolutely necessary, keep the fallback visually calm and close in spirit, but `TH Sarabun New` remains the target font.

## Operational Notes

- This workflow is intentionally on-demand because it should start only when the user explicitly calls for it.
- Do not wait for user approval between segment teaching and mini practice inside this workflow; the user already requested the full loop.
- Keep file names stable so future runs can resume from the latest completed segment.
- If existing segment files are present, resume from the next unfinished segment instead of restarting from segment 1 unless the user explicitly asks to restart.
- Strict means sequential, not batched. Never teach multiple new segments in one response or one production pass.
- After finishing one segment, the workflow must hand off to `Yuehua` before any teaching begins for the next segment.
- `segment-02.md` must not be created before `segment-01.md` is fully taught, solved, organized, and appended.
- The final mock exam, final consolidation, frontend brief, and HTML are end-of-workflow artifacts only.
