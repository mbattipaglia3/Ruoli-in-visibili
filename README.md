# Ruoli (in)visibili: _nomina agentis_ sportivi e _bias_ di genere in traduzione automatica

This repository provides domain-specific lexical terms (_nomina agentis_) and scripts used to support the analysis of gender-related phenomena in machine translation.

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
## Translations
Machine translations for the selected  sentences are provided in [`data/texts/`](`data/texts/`) (one file per system) and are linked to sources via ref.csv.

## Copyright
This repository is released for **non-commercial research** purposes.

Original articles are copyright-protected by their respective publishers and are **not** redistributed in full.

Where short excerpts and derived translations are provided (e.g., selected evaluation sentences), they are included solely for research transparency and are linked to the original sources via [`data/ref.csv`](data/ref.csv).

## Licensing

Code: MIT License (see [LICENSE](LICENSE)).
Data: released under their respective licenses (see [`data/README.md`](data/README.md) and per-file READMEs in data/).


## How to cite
Please cite the associated paper (forthcoming) and this repository.
