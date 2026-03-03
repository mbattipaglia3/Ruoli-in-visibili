```markdown
# Ruoli (in)visibili: bias di genere, traduzione automatica e il contributo dell’IA generativa

## Data
Data resources are in `data/` and are released under their respective licenses:
- `roles_sport_wiki.txt` (CC BY-SA 4.0; derived from Spanish Wikipedia; see `data/README_roles_sport_wiki.txt`)
- `roles_fundeuRAE.txt` (CC BY-SA 3.0 Unported; derived from FundéuRAE; see `data/README_roles_fundeuRAE.txt`)

## Reproducibility
The unified list is not stored in the repository to avoid licensing ambiguity.
It can be regenerated locally with:

```bash
python scripts/merge_roles.py --wiki data/roles_sport_wiki.txt --fundeu data/roles_fundeuRAE.txt --out data/roles_fem_sport.txt
