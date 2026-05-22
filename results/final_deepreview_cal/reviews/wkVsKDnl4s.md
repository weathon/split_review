I have all the information I need. Here is the consolidated final review.

---

## Summary

HighClass replaces alignment-based metagenomic classification with hash-based token mapping, achieving O(|𝒯|) per-read complexity. On CAMI II, it delivers 85.1% F1 (within 1.5% of the state-of-the-art MetaTrinity at 86.6%) while providing 4.2× speedup and 68% memory reduction. The paper also presents a theoretical framework with generalization bounds (O(√(V|𝒴|/n))), concentration inequalities under α-mixing, and consistency guarantees. The empirical core — the architectural transformation from alignment to token mapping — is a genuine contribution, and the ablation study cleanly isolates each component's contribution.

## Strengths

- **Replacing alignment with hash-based token mapping is a genuine architectural transformation.** Table 5 shows HighClass eliminates containment search, seeding, and chaining (collectively 85% of MetaTrinity's runtime) and replaces them with token extraction + lookup + scoring totaling 1.9 ms/read vs. 8.8 ms/read — a verified 4.2× speedup. This is not an incremental optimization; it is a different computational paradigm.

- **Rigorous statistical validation exceeds typical practice in this area.** Results report 95% bootstrap confidence intervals (10,000 resamples), Wilcoxon signed-rank tests with Holm-Bonferroni correction, and Cohen's d effect sizes (runtime d=5.2, F1/hour d=4.8). The ablation study in Table 3 isolates each component contribution with uncertainty estimates.

- **Component contributions are cleanly disentangled.** Table 3 shows that variable-length QA-Token vocabularies contribute 6.8 pp over fixed k-mers (78.3% → 85.1%), quality weighting contributes 1.9 pp (83.2% → 85.1%), and sparsification enables memory reduction from 19.3 GB to 6.8 GB with minimal accuracy loss. The paper honestly notes that QA-Token + MetaTrinity alignment achieves 86.2% F1, demonstrating the vocabulary drives accuracy while the hash lookup drives speed.

- **Strong accuracy-efficiency Pareto improvement.** Table 6 shows HighClass achieves F1/hour = 170.2, which is 4.1× better than MetaTrinity (41.2) and better than both Kraken2 (140.0) and Centrifuge (9.6). This operational point is genuinely useful for throughput-constrained applications.

## Weaknesses

### Major

- **Numerical inconsistency in the sparsification accuracy-preservation claim.** The abstract and Section 1.3 state that sparsification "preserving 94% accuracy." Table 1 shows the full index at 85.8% F1 and the sparsified index at 85.1% F1 — a relative preservation of 99.2% (85.1/85.8). Section 5.4.3 claims "99.5% relative accuracy." These three figures cannot all be correct. The 94% figure appears nowhere in the experimental results and contradicts the reported data. This is not a formatting artifact; it is a direct inconsistency in how the paper's central trade-off is communicated. The authors must resolve which number is correct and ensure consistency between text and tables.

- **The claimed excess-risk bound of 0.021 is presented without derivation and its numerical value is implausible without explanation.** The bound is stated as derived from rate O(√(V|𝒴|/n)). Plugging in V=32,000, |𝒴|=100, n=10⁶ gives √(3.2) ≈ 1.79. To reach 0.021 requires an implicit constant of ≈0.012, which is orders of magnitude smaller than typical constants in Rademacher complexity bounds (usually 2–4). The paper does not sketch the derivation or explain what brings the constant down. While the full proof is in the appendix, a concrete numerical claim of this specificity in the main text should be accompanied by at least a sketch of the calculation. As written, the bound appears either miscalculated or presented without sufficient justification.

### Minor

- **The mixing analysis and the generalization bound are presented as parallel results without integration.** The paper advertises the theory as addressing token dependencies, but the main generalization bound (O(√(V|𝒴|/n))) is derived under standard Rademacher complexity (which assumes independence). The α-mixing analysis (variance inflation factor ≈31.7) is presented as a separate concentration result for token scores. The connection between these two analyses is not made explicit: does the bound change under dependencies? If not, what does the mixing analysis add to the generalization guarantee? The paper should clarify this relationship.

- **The method for empirically estimating γ≈0.15 is not described.** The paper states that mixing parameters C≈2.3 and γ≈0.15 are "empirically validated on CAMI II data" but provides no description of how these values were estimated (e.g., method-of-moments on autocorrelations, block bootstrap). This makes the mixing analysis difficult to reproduce or assess.

- **The learned sensitivity η=1.8 is presented as "optimal" without a sensitivity analysis.** While η comes from QA-Token, the paper claims it "optimally weights sequencing evidence" without showing any sweep or sensitivity study over η in the HighClass context.

- **The gradient-based sparsification procedure is not fully described regarding data separation.** The paper says sparsification masks are "pre-computed" and cites Alser et al. (2024), but does not clarify whether these masks are computed on the reference database alone or could inadvertently incorporate information from test reads. A brief statement confirming that masks are computed solely from the reference (or a held-out set) would rule out data leakage concerns.

### Trivial

- In Section 1.3 (line 97), the generalization bound notation in the text changes between O(√(V|𝒴|/n)) in Section 4.3 and O(√(V𝒴/n)) in the Discussion (line 374) — the latter drops absolute value notation around |𝒴|.

## Nice-to-Haves

- A sensitivity analysis over the quality sensitivity parameter η (e.g., F1 vs. η over [0.5, 3.0]) would confirm that 1.8 is a sensible choice within HighClass's pipeline.
- Including additional alignment-free baselines such as KrakenUniq or minimap2 in mapping mode would contextualize the accuracy-efficiency trade-off against a broader set of fast methods.
- A brief explanation of how γ is estimated from data (e.g., via autocorrelation decay or block bootstrapping) would make the mixing analysis self-contained.

## Removed Points

These points from the reviewers were removed (with justification):

- *"Novelty of HighClass is limited; the method is essentially a bag-of-tokens classifier"* — The paper clearly articulates that the contribution is the architectural transformation from alignment to hash-based token mapping, which is a genuine and non-obvious change. The synthesis of QA-Token, MetaTrinity, and sparsification into a single system with theoretical analysis is itself a contribution. This criticism is scope-creep.
- *"QA-Token+alignment nearly matches MetaTrinity, weakening the claim that speedup comes from replacing alignment"* — The paper itself makes this point honestly in the Table 3 caption. The claim is precisely that the speedup comes from replacing alignment (with minimal accuracy loss), which is exactly what Table 3 demonstrates.
- *"Missing related works"* — Hard rule: do not penalize for missing references, as external verification is not possible.
- *"Scoring function derivation deferred to appendix"* — Standard practice in papers with space constraints; the main text gives the key formula qualitatively.
- *"Formatting concerns, typos, appendix content"* — Parser artifacts or standard paper organization.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the numerical inconsistency**: Decide whether the sparsification preserves 94%, 99.2%, or 99.5% of accuracy (Table 1 strongly supports the 99% figure) and make all text consistent with the experimental data.
2. **Explain the 0.021 bound derivation**: Provide a brief sketch showing how the O(√(V|𝒴|/n)) rate yields 0.021 for the specific parameter values, or correct the number if it is miscalculated.
3. **Clarify the relationship between the mixing analysis and the generalization bound**: State explicitly whether the bound accounts for dependencies or is derived under independence, and what the mixing analysis adds.
4. **Describe the γ estimation procedure**: A 2–3 sentence description of how γ≈0.15 was empirically determined would make the mixing analysis reproducible.
5. **Clarify the sparsification mask computation**: Add a sentence confirming that importance masks are computed solely on the reference database, not on test reads.

## Score and Decision

**Round 1 bracket**: 4.5–6.5 (based on calibration anchors in weak, middle, and strong bands).

**Round 2 anchors examined**:
| Anchor | Avg. Score | Round | Comparison to this paper |
|---|---|---|---|
| FastLSH (BvQkjCnXXr) | 4.50 | 2 | Weaker: less complete evaluation, less practical contribution. Our paper is stronger. |
| DNABERT-S (9klRFLY2TT) | 5.67 | 2 | Similar: comparable breadth of experiments and concerns about component novelty. Our architectural contribution (alignment→hash) is more fundamental; our theory issues are more severe. |
| MeToken (noUF58SMra) | 5.80 | 1 | Similar: both have solid ablation and benchmarks. Our theory is more ambitious but also more problematic. |
| Tokenization Foundations (B5iOSxM2I0) | 6.50 | 1 | Weaker: pure theory paper with no empirical evaluation; our empirical contribution is substantial. |
| FastLSH (BvQkjCnXXr) | 4.50 | 1 | Weaker: theory flaws + limited experiments. Our paper is clearly better. |

**Final reasoning**: The paper's empirical core is genuinely useful — replacing alignment with hash-based token mapping is a real contribution with practical impact, and the statistical rigor (confidence intervals, effect sizes, corrected tests) is above typical standards for this area. However, the theoretical claims contain a clear numerical inconsistency (94% vs 99%+ accuracy preservation) and a plausibility gap in the excess-risk bound (0.021 from O(√(V|𝒴|/n)) without derivation). These issues do not invalidate the empirical contribution but they undermine the paper's headline claims and must be resolved. Relative to the calibration anchors, the paper is stronger than FastLSH (4.50) but has more serious presentation problems than the 5.5–6.0 range papers. The final score of 5.0 reflects a paper with genuine empirical contributions weighed down by verifiable inconsistencies in its theoretical claims.

<score>5.0</score>
<decision>Reject</decision>