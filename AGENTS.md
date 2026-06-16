# Agent instructions

use composer-2.5 for subagents, never use composer-2.5-fast for subagents


## After making changes

Run the smoke tests before finishing work on scene, enum, or generator changes:

```bash
python -m pytest
```

Install test dependencies first if needed:

```bash
pip install -e ".[dev]"
```

These tests catch common regressions such as invalid `OutfitType` or `LocationType` references in `src/scenes.py`, broken imports, and failures in basic scene or prompt generation.
