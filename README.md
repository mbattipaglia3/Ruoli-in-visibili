# Ruoli (in)visibili: bias di genere, traduzione automatica e il contributo dell’IA generativa

This repository provides domain-specific lexical resources (sport roles) and scripts used to support the analysis of gender-related phenomena in machine translation.

## Repository contents
- `data/`: lexical resources released under their original licenses (see `data/README.md` and per-file READMEs).
- `scripts/`: scripts to reproduce derived resources (e.g., list merging).

## Reproducibility
The unified list is **not** stored in the repository to avoid licensing ambiguity.
It can be regenerated locally with:

```bash
python scripts/merge_roles.py --wiki data/roles_sport_wiki.txt --fundeu data/roles_fundeuRAE.txt --out data/roles_fem_sport.txt
```
## Data availability

Files containing full article texts (e.g., ruoli_*.csv) are not included for copyright reasons.

## Licensing

Code: MIT License (see LICENSE).

Data: released under their respective licenses (see data/README.md and per-file READMEs in data/).
