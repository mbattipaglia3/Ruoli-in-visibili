# Ruoli (in)visibili: nomina agentis sportivi e bias di genere in traduzione automatica

This repository provides domain-specific lexical terms (nomina agentis) and scripts used to support the analysis of gender-related phenomena in machine translation.

## Repository contents
- `data/`: lexical resources released under their original licenses (see [data/README.md](data/README.md) and per-file READMEs).
- `scripts/`: scripts to reproduce derived resources (e.g., list merging).

## Sources
Bibliographic metadata and source URLs are provided in [`data/ref.csv`](data/ref.csv).  
Full article texts are not redistributed for copyright reasons.

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

Data: released under their respective licenses (see [`data/README.md`](data/README.md) and per-file READMEs in data/).


## How to cite
Please cite the associated paper (forthcoming) and this repository.
