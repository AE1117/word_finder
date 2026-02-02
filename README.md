## Word Finder

# Crossword-Engine
Procedural Word Placement System
This project is a constraint-driven crossword generation engine that blends deterministic word logic with procedural layout design.

The core idea is simple:
Words are meaningful,
but their spatial relationships are not random.
Instead of placing words freely, the system enforces strict structural rules that mimic real crossword puzzles and Wordscapes-style word games.

# Overview
The system is built around two independent layers:
- Presentation Layer (UI / Runtime)
  + Displays the crossword grid in a web interface
  + Renders letters and empty cells
  + Consumes structured JSON output
  + Contains no placement logic
- Generation Layer (Algorithm Engine)
  + Responsible for all word placement decisions
  + Ensures valid intersections only
  + Prevents meaningless letter adjacency
  + Normalizes grid geometry
  + Outputs deterministic coordinate data

This separation ensures that the UI remains simple while the algorithm evolves independently.

# Core Principles
The generator follows three fundamental rules:
- Intersection-Only Placement
  + Words may intersect only through matching letters.
  + No arbitrary overlaps are allowed.

- No Meaningless Adjacency
  + Letters from different words cannot touch unless they form a valid intersection.
  + This prevents accidental or unreadable word clusters.

- Structural Consistency
  + Every placed word must be spatially consistent with the existing grid.
These constraints transform the system from a random word placer into a real crossword engine.

# Grid Model
The crossword exists on an abstract coordinate grid:
- Each letter occupies a discrete (x, y) coordinate
- Words are placed horizontally or vertically
- The grid expands dynamically as new words are added
- After generation, the grid is normalized to eliminate negative coordinates
This model allows the engine to operate without predefined board limits while still producing compact layouts.

# Word Placement Strategy
- The engine uses a hybrid placement strategy:
- Greedy placement for fast generation
- Heuristic scoring based on intersection count
- Constraint validation before placement
- Best-position selection instead of random choice

Placement process:
1. Place the longest word as the structural backbone
2. Search for valid intersections with existing letters
3. Evaluate candidate positions
4. Select the position with the highest structural score
5. Reject words that violate adjacency constraints
This approach maximizes meaningful intersections while minimizing spatial noise.

Determinism vs Randomness
Although the engine explores multiple placement options, it is not purely random.
- Randomness is used only when multiple valid placements exist
- Structural constraints dominate placement decisions
- The same word set tends to produce similar but not identical layouts
The result is controlled procedural generation rather than chaotic randomness.

# Output Format
The generator produces a structured JSON output:
- Each letter is represented as:
  + x coordinate
  + y coordinate
  + character value
- The output is designed to be directly consumed by game engines or web interfaces
This makes the system suitable for:
- Word games
- Crossword generators
- Educational tools
- Puzzle engines

# Design Goals
- Avoid visually noisy word clusters
- Maximize meaningful intersections
- Prevent invalid letter contact
- Keep layouts compact and readable
- Separate algorithmic logic from presentation

# Future Work
If you would like to further develop the project, you can find;
- CEFR levels
- CEFR levels + length
- Raw data
in the attachments folder.

# License
This project is intended for experimentation, algorithmic exploration, and game development research.
Feel free to use, modify, and extend it.
