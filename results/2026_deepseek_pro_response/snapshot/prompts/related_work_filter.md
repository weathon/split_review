You are given a paper and a list of potentially related works found by a \
search agent. Your job is to FILTER this list:

1. REMOVE any work that is ALREADY CITED in the paper. Check the references \
   section and in-text citations carefully. If the paper already mentions it \
   (even by a different abbreviation or partial title), remove it.
2. REMOVE any work that is only TANGENTIALLY related — if the connection is \
   a stretch or requires multiple leaps of logic, drop it.
3. KEEP only works that are genuinely relevant AND not already cited.

For each kept work, briefly explain why it's a potentially missed reference.

Output format (strictly follow):
## Potentially Missed Related Work

(These are suggestions, not definitive omissions. The authors may have \
intentionally excluded them or been unaware of them.)

1. **Title** — Authors (Year, Venue).
   Why potentially missed: ...

If all works are already cited or not relevant, say:
"No significant potentially missed related work identified."