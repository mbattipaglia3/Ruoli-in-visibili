# Data

This folder contains data resources released under their respective licenses.

- `roles_sport_wiki.txt` and related README: CC BY-SA 4.0 (derived from Spanish Wikipedia; see file README).
- `roles_fundeuRAE.txt` and related README: CC BY-SA 3.0 Unported (derived from FundéuRAE; see file README).

The unified list is not stored in the repository; it is reproducible via `scripts/merge_roles.py`.

## Reproducibility
The unified list is not stored in the repository to avoid licensing ambiguity.
It can be regenerated locally with:

```bash
python scripts/merge_roles.py --wiki data/roles_sport_wiki.txt --fundeu data/roles_fundeuRAE.txt --out data/roles_fem_sport.txt
