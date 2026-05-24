## Summary

This paper introduces a novel task — automatically discovering a learning-friendly order of decoder output tokens (i.e., "unraveling the chain of thought") for Transformers on arithmetic reasoning tasks. The method trains a small Transformer on a mixture of target sequences in different permutations, then identifies promising orders via early-stage loss profiling (exploiting easy-to-hard learning dynamics). To handle factorial search spaces, it proposes a hierarchical two-stage search (global block-level + local intra-block refinement). Experiments on three designed tasks (RELU, SQUARE-19, INDEX) and the PROD (multiplication) task show that the method recovers the known optimal order from billions of candidates, improving success rates from ~10% to near 100% on the main tasks, and also rediscovering the reverse-digit order known to be beneficial for multiplication (Shen et al., 2023).

## Strengths

- **Novel and well-motivated problem formulation.** The paper formalizes the underexplored problem of automatically finding a learning-friendly output-token order for arithmetic reasoning, which prior work handled only heuristically (e.g., manually choosing least-significant-digit-first for multiplication).
- **Clever use of training dynamics for efficient ranking.** Loss profiling (training one mixed model for 800–1,600 steps and ranking orders by validation loss) is elegant and empirically effective. Figure 5 demonstrates that the forward order achieves the lowest loss among 128 random permutations across all three tasks, and that loss rank correlates with eventual success rate for RELU and SQUARE-19.
- **Scalable hierarchical search.** The global–local pipeline enables pruning the factorial space to a tractable number of candidates. Table 2 shows recovery of the forward order for RELU and SQUARE-19 up to L=13 (13! > 6×10⁹ permutations), and Figure 6(b) extends to L=40 with structured initialization (10⁴⁷ candidate space).
- **Practical computational cost.** Each training run uses 800–1,600 steps, the full exploration takes 1–7 hours on a single A6000 GPU, and a 1-layer GPT-2 suffices for exploration while the discovered orders transfer to a 6-layer model for final training.
- **Rediscovery of a known result.** On the PROD task, the method automatically recovers the least-significant-digit-first order that Shen et al. (2023) previously reported as essential for multiplication — without being given any task-specific heuristics.

## Weaknesses

### Major

None.

### Minor

- **Success rates for discovered INDEX orders with the large model are not reported.** Table 2 shows that for INDEX at d=4 and d=8, the hierarchical search does not recover the forward (identity) order. The paper acknowledges the difficulty ("the INDEX task proves harder… flattens the loss landscape") but never reports the actual success rate achieved by training the 6-layer model on these discovered non-identity orders. Since the paper's headline claim ("~10% to ~100%") draws on the designed tasks including INDEX, this missing evaluation makes it impossible to assess whether the discovered orders for INDEX d=4,8 are genuinely beneficial compared to the reverse-order baseline (1.3% and 2.2% in Table 1) or only marginally better. This is the most significant gap in the evaluation.

- **The hierarchical search fails on harder INDEX configurations without analysis of why.** For INDEX d=4 and d=8, the loss profiling (Figure 5a) still identifies the forward order as lowest-loss, but the hierarchical search does not recover it (Table 2). This suggests that the greedy pruning in the global stage may discard the optimal permutation. The paper notes the flat loss landscape as the likely cause but provides no analysis — e.g., no comparison of whether the discovered non-identity orders outperform random orders, and no sensitivity analysis of the pruning threshold. This limits the reader's understanding of when the method can be expected to work.

- **No comparison against a random-search baseline.** The paper frames the problem as one where naive exhaustive search is intractable, which is correct, but it does not compare the proposed method against a simple alternative: randomly sample \(M\) permutations (same budget as the method explores), train a model from scratch on each, and pick the best. Figure 5 already shows that the forward order ranks first among 128 random permutations via loss profiling — this implicitly suggests the method is better than random, but a direct comparison of the cost-accuracy trade-off would strengthen the paper considerably.

- **The L=10 outlier on ReLU is not explained.** Figure 6(a) shows the discovered order for ReLU at L=10 yields only ~35% success rate while L=9 and L=11–13 yield ~100%. Table 2 confirms the discovered final order for L=10 is non-identity. The paper does not discuss why this happens or whether it is systematic. This is a concrete failure case that should be analyzed or at minimum acknowledged as a limitation.

### Trivial

- None.

## Nice-to-Haves

- A hyperparameter sensitivity study (varying the number of candidates \(T\), search depth \(K\), training epochs \(E\) for profiling, and the pruning threshold \(\lfloor T/(k+1) \rfloor\)) would help practitioners apply the method.
- The method description in Section 4 (global and local stages) would benefit from a compact pseudocode listing.

## Removed Points

- "The central claim is only partly supported by the evidence" (as framed by the harsh critic) — partially retained as the first Minor weakness above, but the harsh critic overstated this. The abstract's claim of 10%→100% is directly supported for RELU and SQUARE-19 (Figure 6). For INDEX, the paper clearly acknowledges the task is harder. The missing piece is simply not showing the large-model success rates for discovered non-identity INDEX orders.
- "Soft-permutation baseline comparison missing" — the paper explicitly shows soft-permutation fails (Figure 2) and explains why. Requesting additional baselines (genetic algorithms, evolutionary search) is scope creep.
- "Section 4 hard to follow" — style concern, not a substantive weakness.
- "Duplicate '1' in ReLU L=10 order" — likely a parser artifact or genuine table error; either way does not affect conclusions.
- "LLM writing assistance" — irrelevant to paper quality.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Report the actual success rates (with the 6-layer model) for every discovered non-identity order in Table 2, especially for INDEX (d=4, d=8) and ReLU (L=10). This single addition would directly validate or delimit the method's effectiveness on the hardest settings.
2. Add a comparison against a random-search baseline that samples the same number of permutations as the method evaluates, training a fresh model for each. This would quantify the value added by loss profiling over naive search.
3. Analyze the L=10 ReLU failure and the INDEX d=4,8 failures: does the discovered order actually outperform the reverse-order baseline? Why does the global stage prune the forward order in these cases? Even a brief analysis would significantly strengthen the paper's characterization of when the method works.

## Score and Decision

### Calibration

**Round 1 (bracketing).** Three queries on related topics:
- Anchor AaAbeUp7O4 (avg 3.00, Reject) — diffusion LM reasoning with order search. Clearly weaker: poorly scored, less clear contributions.
- Anchor ksWsF80beE (avg 3.33, Reject) — addition/subtraction in transformers. Less novel framing, no comparable method contribution.
- Anchor iOlXapkK6V (avg 5.00, Reject) — multiplication ICoT reverse-engineering. Closer in topic but premise was questioned by reviewers; this paper has a cleaner, more defensible premise.
- Anchor 0xmvlDKDTL (avg 4.00, Withdrawn) — composable CoT. Contrived synthetic tasks, limited novelty. This paper is stronger.
- Anchor aE1VU6Ui4M (avg 5.50, Accept Poster) — distributions over permutations. Comparable novelty, comparable experimental depth. This paper is roughly on par.
- Anchor 7QtKdabBP9 (avg 6.00, Accept Poster) — BO in permutation spaces. Comparable: clear motivation, solid method, some missing baselines, but contribution stands.
- Anchor J2peqXPQbB (avg 5.50, Accept Poster) — in-context algebra. Similar novelty level, also had some incomplete analysis questions.

**Round 1 bracket:** Between 4.5 and 6.5.

**Round 2 (narrowing).** Two queries in (4.5, 6) and (5.5, 7.5):
- Anchor aE1VU6Ui4M (avg 5.50, Accept Poster) — distributions over permutations. Stronger than this paper in theoretical grounding, weaker in practical applicability.
- Anchor 7QtKdabBP9 (avg 6.00, Accept Poster) — BO in permutation spaces. Comparable in having a clear method, moderate experimental evaluation, and some missing comparisons.
- Anchor 2FZC0c06jP (avg 6.50, Accept Poster) — proxy-model data curation. Higher score reflects thorough evaluation and clear practical impact; this paper is slightly below that standard.
- Anchor rxcbZb7fVC (avg 6.00, Reject) — three-phase dynamics of generalization. Interesting theory but less clear empirical impact.

**Final score:** 6.0. The paper has genuine novelty, a clever and practical method, and solid experimental support for its main claims. The evaluation gaps (missing success rates for discovered INDEX orders, no random-search baseline, unexplained L=10 outlier) prevent it from reaching the 6.5–7 range but do not undermine the core contribution. The paper compares favorably to accepted anchors at the 5.5–6.0 level.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>