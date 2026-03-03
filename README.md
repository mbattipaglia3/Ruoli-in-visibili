# Ruoli (in)visibili: bias di genere, traduzione automatica e il contributo dell’IA generativa

This repository provides domain-specific lexical terms (sport roles) and scripts used to support the analysis of gender-related phenomena in machine translation.

## Repository contents
- `data/`: lexical resources released under their original licenses (see [data/README.md](data/README.md) and per-file READMEs).
- `scripts/`: scripts to reproduce derived resources (e.g., list merging).

## Requirements
- Python 3.9+ (any recent Python 3 should work)
  
## Reproducibility
The unified list is **not** stored in the repository to avoid licensing ambiguity.
It can be regenerated locally with:

```bash
python scripts/merge_roles.py --wiki data/roles_sport_wiki.txt --fundeu data/roles_fundeuRAE.txt --out data/roles_fem_sport.txt
```
## Data availability

Files containing full article texts are not included for copyright reasons.

## Licensing

Code: MIT License (see [LICENSE](LICENSE)).

Data: released under their respective licenses (see data/README.md and per-file READMEs in data/).


Se vuoi aggiungere anche una riga “How to cite” (utile quando pubblichi il paper), possiamo mettere in fondo:

## How to cite
Please cite the associated paper (forthcoming) and this repository.
