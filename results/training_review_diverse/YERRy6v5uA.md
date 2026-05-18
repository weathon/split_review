Now I have a thorough understanding of the paper and can verify each claim against the actual text. Let me produce the final review.

## Summary

This paper critically re-evaluates the necessity of Graph Structure Learning (GSL) in GNNs. The authors propose a three-step decomposition of GSL (bases generation, structure construction, view fusion), provide theoretical analysis showing that graph convolution on GSL-constructed graphs does not increase mutual information beyond the GSL bases (a direct application of the data processing inequality), and conduct extensive ablation experiments. Their main empirical finding is that removing GSL from state-of-the-art methods does not degrade performance, while gains attributed to GSL actually come from pretrained bases (self-training) and structural encoding. The paper argues that GSL is largely unnecessary for node classification.

## Strengths

- **Unified three-step GSL framework that disentangles components.** The paper decomposes GSL into GSL bases generation, new structure construction, and view fusion (Section 3, Figure 2). This is more comprehensive than prior taxonomies that focus only on structure construction, and it enables the authors to isolate where performance gains actually come from. This framework is a useful conceptual contribution for future GNN research.

- **SOTA ablation experiments convincingly show GSL is not the source of gains.** Table 2 (SOTA-GSL) replaces the GSL-constructed graph with the original graph or with MLP layers in eight state-of-the-art methods. Removing GSL does not degrade performance — results are comparable or better. This is the paper's cleanest and most convincing empirical contribution, directly supporting the core claim.

- **Identification that pretrained GSL bases (self-training), not GSL graph reconstruction, drive performance.** Section 5.4 shows that pretrained representations (MLP(X), GCN(X,A)) significantly improve performance, while the GSL graph construction step itself contributes little. This correctly reframes future GNN design priorities away from GSL and toward self-training and structural encoding.

- **Synthetic experiments with controlled homophily provide clean controlled evidence.** Section 4.1 fixes the GSL bases and compares MLP(B), GCN(B,G), and GCN+GSL(B,G') across varying homophily levels. These experiments directly control for the GSL bases variable and show that MLP on the bases matches or exceeds GCN+GSL, consistent with the paper's theoretical analysis.

## Weaknesses

### Fatal
None.

### Major

- **The "best-performing GSL bases" reporting in Table 1 obscures the controlled comparison.** The paper states it trains all models on each of the five GSL bases (line 163) but reports results "using the best-performing GSL bases" (line 167). If GCN's winning choice is X and GCN+GSL's winning choice is MLP(X), the reader cannot tell whether the performance gap stems from GSL itself or from the different input representations. The paper later references "under the same GSL bases" (line 209) suggesting the per-base data exists and is consistent with the claims, but the table as presented does not let the reader verify this. **Why it matters:** this is the paper's headline experiment (Table 1). Without per-base transparency, this table does not cleanly isolate the effect of GSL. The SOTA-GSL experiments (Table 2) are cleaner and carry more weight, but the paper presents both as equivalent evidence. The authors should report per-base breakdowns or explicitly confirm that the winning bases are matched across conditions.

- **The scope claim ("GSL is unnecessary in most cases") is broader than the evidence supports.** All experiments are on node classification. There is no evaluation on link prediction, graph classification, or settings where structure is entirely missing (e.g., the WSGNN setting). **Why it matters:** this is the paper's central claim. While node classification is the primary evaluation task in GSL literature, the paper should either restrict its conclusion to node classification or provide evidence from other tasks. The current framing overgeneralizes.

### Minor

- **Theorem 2 is a straightforward application of the data processing inequality, not a novel theoretical result.** The paper states that B' (aggregated bases on the GSL graph) satisfies I(Y;B') ≤ I(Y;B) because B' is a deterministic function of B (averaging over neighbors). This follows directly from DPI and is not specific to GSL — the same inequality would hold for aggregation on any graph. The paper's framing ("both of our empirical experiments and theoretical analysis prove...") slightly inflates the theoretical contribution. The real value is in the empirical demonstration and the conceptual framework, not the information-theoretic bound. The paper should acknowledge this more explicitly.

- **The mutual information estimator is cited but not described.** The paper uses a kNN-based MI estimator (line 69) for continuous features, but provides no description of its assumptions, biases, or parameter choices. Since MI plays a central role in Observations 1–3 and motivates the theoretical analysis, readers need a brief description to assess the reliability of Figures 3 and 4.

- **The quality-of-GSL-graphs section (5.3) is suggestive but not directly tied to performance.** The visual comparison shows that non-GSL methods (label-based graph construction) produce better intra-class connectivity than GSL graphs. While interesting, this does not directly demonstrate that GSL fails to improve performance when used in actual GNN training. The argument is correlational rather than causal.

### Trivial

- The paper uses "sightly" (line 146) instead of "slightly" — a minor typo.

## Nice-to-Haves

- A per-base breakdown for Table 1 (or a supplementary table showing which input achieved best performance for each model), so readers can verify the comparison is not confounded.
- A brief description of the kNN mutual information estimator and its key parameters.
- Explicit acknowledgment in the theorem statement that the bound follows from the data processing inequality and applies to any graph convolution, not just GSL.

## Removed Points

- **"The experimental design for the core comparison is confounded, undermining the paper's main empirical claim" (as Fatal).** Kept as Major, not Fatal. The paper states it trained models on each GSL base individually (line 163) and references "under the same GSL bases" (line 209). The data exists; the issue is that the table only reports the best aggregate without showing per-base results. This is a reporting/transparency problem, not a fundamentally confounded design. The SOTA-GSL experiments (Table 2) are clean and independently support the main claim.

- **"The theoretical analysis contributes less than the paper suggests" (as Major).** Kept as Minor. The reviewer is correct that Theorem 2 is just DPI, but the paper's value is in applying this insight to GSL and connecting it to empirical observations. The overclaim is mild, not structural.

- **Weakness about missing related works.** Removed per instructions: I cannot confirm existence of missing references without external sources.

- **Formatting nitpicks about missing appendix, proofs, etc.** Removed per instructions: the parser strips these sections.

## Novel Insights

The most interesting observation emerging from the reviews is the tension between the paper's clean decomposition/synthetic experiments and the opaque reporting of Table 1. The synthetic experiments (Section 4.1) actually do what the paper claims — fix the base B and compare MLP(B) vs GCN(B,G) vs GCN+GSL(B,G') — and they strongly support the claim. Yet the paper's real-world counterpart (Table 1) uses an aggregated "best-over-bases" reporting that invites the very confusion the synthetic experiments avoid. This suggests a simple fix: Table 1 should either (a) report per-base results, or (b) explicitly note that the same base was optimal for both GNN and GNN+GSL in each case, or (c) fix the base to X and compare GNN(X) vs GNN+GSL(X) as the primary analysis, with the best-over-bases as a secondary view. The paper would be notably stronger with this one clarification.

## Suggestions

1. **Fix Table 1 reporting.** Add a supplementary table showing per-base results for each model (GNN vs GNN+GSL), or explicitly state in the main text whether the winning GSL bases are the same across the with/without-GSL conditions for each backbone.
2. **Narrow the scope claim.** Replace "GSL is unnecessary in most cases" with "GSL is unnecessary in most node classification cases" unless additional task evidence is provided.
3. **Acknowledge Theorem 2 as DPI.** Add a sentence noting that the inequality follows from the data processing inequality and holds for any graph convolution, reframing the contribution as the application of this insight to GSL rather than a novel bound.
4. **Add MI estimator description.** A 2–3 sentence summary of the kNN-based estimator and its key assumptions would help readers assess Figures 3–4.
5. **Remove the "prove" language** from the contribution list (line 32). The paper's evidence is strong but empirical; "demonstrate" or "show" would be more accurate than "prove."

## Score and Decision

The paper addresses a timely and provocative question, provides a useful conceptual framework, and includes a strong SOTA ablation experiment (Table 2) that directly supports its core claim. The main weaknesses are (1) opaque reporting in Table 1 that makes the headline GNN+GSL comparison harder to interpret than necessary, and (2) scope overclaim beyond the evaluated tasks. Neither is fatal — both are addressable. The paper makes a genuine contribution to understanding when and whether GSL actually helps.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>