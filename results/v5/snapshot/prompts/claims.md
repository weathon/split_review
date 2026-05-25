
## Claim Verification

Extract every main claim the paper makes, not every tiny details but the main contributions.
 
For each claim, assess:

1. **Evidence chain**: What evidence does the paper provide for this claim? Trace the chain from claim → experiment/analysis → result. Identify where the chain is solid, where it has gaps, and where it relies on unstated assumptions.

2. **Support level**: Classify as one of:
   - **Well-supported**: The evidence directly and sufficiently establishes the claim.
   - **Partially supported**: There is relevant evidence, but it does not fully establish the claim — e.g., the result holds on 2 of 4 datasets, or the ablation is incomplete, or confounders are not controlled.
   - **Unsupported**: The claim is made but the paper provides no meaningful evidence for it, or the evidence actually points elsewhere.
   - **Contradicted**: The paper's own results or reasoning work against this claim.

3. **Improvement path** (for claims that are not well-supported): Distinguish between:
   - **Writing fix**: The evidence may exist or be inferable, but the paper fails to present it clearly. Specify what the authors should make explicit — e.g., "the connection between Table 3 and the claim in Section 5.2 is never stated; the authors need to show that the improvement in row X corresponds to the mechanism described in Section 3."
   - **Methodological fix**: The evidence does not exist in the current submission and requires additional work. Be specific about what experiment, analysis, or control would close the gap — not "more experiments" but "an ablation removing component X to isolate its contribution to the Y% gain claimed in Section 5."

Do not list trivially true claims or restate the obvious. Focus on claims that carry argumentative weight — claims whose failure would weaken the paper's case.