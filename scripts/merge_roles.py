import argparse
from pathlib import Path

def read_list(path: Path) -> list[str]:
    items = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if s:
                items.append(s)
    return items

def merge_unique(*lists: list[str]) -> list[str]:
    seen = set()
    out = []
    for lst in lists:
        for item in lst:
            key = item.lower()
            if key not in seen:
                seen.add(key)
                out.append(item)
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--wiki", required=True, help="Path to roles_sport_wiki.txt")
    ap.add_argument("--fundeu", required=True, help="Path to roles_fundeuRAE.txt")
    ap.add_argument("--out", required=True, help="Output path (e.g., data/roles_fem_sport.txt)")
    args = ap.parse_args()

    wiki = read_list(Path(args.wiki))
    fundeu = read_list(Path(args.fundeu))

    merged = merge_unique(wiki, fundeu)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8", newline="\n") as f:
        for item in merged:
            f.write(item + "\n")

    print(f"OK: {len(wiki)} wiki + {len(fundeu)} fundeu -> {len(merged)} unique entries written to {out_path}")

if __name__ == "__main__":
    main()
