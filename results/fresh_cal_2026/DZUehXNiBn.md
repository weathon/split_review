## Summary

VISTA is a modular divide-and-conquer framework for large-scale causal DAG learning. It splits the problem into node-centered Markov Blanket subgraphs, applies any off-the-shelf base learner to each subgraph, and aggregates the resulting directed edges via a weighted voting scheme (with exponential decay penalizing low-support edges), followed by a Feedback Arc Set heuristic to enforce acyclicity. The method is model-agnostic (demonstrated across six base learners: NOTEARS, GOLEM, DAG-GNN, GraN-DAG, SCORE, CAM), yields consistent F1 and runtime improvements in both synthetic and real experiments, and comes with finite-sample and asymptotic theory. The key design is simple and practical: the aggregation is a one-pass O(|V|²) matrix operation, and hyperparameter sweeps are retraining-free.

## Strengths

1. **Model-agnostic design validated across diverse base learners.** VISTA integrates with six fundamentally different learners (differentiable score-based, combinatorial, nonlinear) without modifying their internals. Tables 1–2 show that VISTA-WV improves F1 over standalone baselines in nearly every setting, e.g., NOTEARS ER5 F1 from 0.76→0.79, GOLEM ER5 F1 from 0.35→0.60. This breadth convincingly demonstrates the framework's plug-and-play nature.

2. **Substantial and well-documented runtime improvements.** Table 3 shows runtime reductions that grow with graph size: e.g., NOTEARS at n=300 drops from 12,515s to 2,136s; SCORE becomes feasible at n=300 only with VISTA (225s vs. "—" for standalone). The parallelization claim is concrete: the per-node subgraph loop is embarrassingly parallel.

3. **Coverage guarantee (Proposition 3.1) is clean and principled.** The proof that every true edge appears in the union of Markov Blanket subgraphs is simple but foundational — it ensures the decomposition does not lose edges, which is the necessary precondition for the whole divide-and-conquer strategy to work. This property is independent of the specific MB estimator or base learner.

4. **Practical sensitivity analysis without retraining.** Since λ appears only in the final aggregation, the paper sweeps it by reusing cached votes and recomputing scores. The use of a single fixed operating point (λ=0.5, t=0.7) across all main tables demonstrates robustness and avoids per-dataset cherry-picking.

5. **Transparent framing of precision–recall trade-off (Figure 4).** The paper documents smooth precision–recall curves as λ varies, and the fixed operating point is a reasonable default.

## Weaknesses

### Major

1. **Asymptotic consistency (Theorem 3.5) assumes a scaling condition that cannot be satisfied in sparse graphs.** The theorem requires the number of local subgraphs per candidate edge to be m = C log n. However, for any given edge (X, Y), the number of subgraphs whose Markov Blankets contain both endpoints is bounded by the maximum Markov Blanket size. In a sparse DAG with bounded average degree h ∈ {3, 5}, this number is a small constant (e.g., 3–10), not a function that grows with n. Therefore the condition m = C log n is impossible to meet for most edges, and the stated asymptotic consistency guarantee does not apply to the actual algorithm in the regime the paper targets (large sparse graphs). This is not a minor tightening issue — the theorem's premise is contradicted by the algorithm's own structure. The paper does not acknowledge this gap and presents the theorem as a supporting guarantee.

2. **The independence assumption underlying all theoretical guarantees is acknowledged but the presentation overstates the theory's force.** Theorems 3.2–3.5 model votes as binomial draws *independent* across subgraphs. The paper acknowledges this after Theorem 3.2 ("the bound should be interpreted as a qualitative guide"), but the abstract and contributions section nonetheless state that VISTA "theoretically establish[es] finite-sample error bounds" and "prove[s] its asymptotic consistency under mild conditions" — language that conveys rigorous guarantees. In reality, the concentration inequalities used in the proofs cannot be invoked when votes from the same dataset are correlated through overlapping Markov Blankets. The theory is best understood as a heuristic sanity check for the weighted voting design, not a verifiable guarantee about the algorithm's behavior. Given the prominence of the theoretical claims in the paper's framing, this mismatch is a significant weakness.

### Minor

3. **Precision–recall trade-off is real but acknowledged incompletely.** VISTA-WV consistently improves F1, but often does so by reducing TPR (e.g., NOTEARS on ER5: TPR 0.74→0.68; GraN-DAG on Sachs: TPR 0.53→0.29). The paper's abstract and conclusion emphasize "improvements in both accuracy and efficiency," which could be read as monotonic gains. The paper discusses this trade-off in the main text, but the summary claims could better qualify that accuracy improvements are F1-driven and sometimes come at the cost of recall. A more precise framing (e.g., "improves structural accuracy as measured by F1, SHD, and FDR, with a controlled precision–recall trade-off") would be more accurate.

4. **No statistical significance tests.** Given the substantial standard deviations reported (e.g., NOTEARS SHD 208.80 ± 190.71; NOTEARS+VISTA-WV SHD 182.40 ± 16.03), the improvements may not all be statistically significant. Reporting confidence intervals or simple paired tests would strengthen the empirical claims.

### Trivial

5. The paper uses SID in Table 4 without defining it (beyond the citation Peters & Bühlmann). A brief definition in the caption or text would help readers.

6. Some table entries (e.g., NV variants with FDR ~0.87 and SHD 3,000+) produce degenerate results that make the baseline comparison hard to read. A brief explanation in the caption that NV is primarily a coverage check (not a viable standalone method) would improve clarity.

## Nice-to-Haves

- A comparison with a simple alternative: run the base learner on the full graph but with reduced budget (fewer epochs/iterations) to match VISTA's runtime, then compare accuracy. This would disentangle whether improvements come from the modular design or simply from a different compute-accuracy trade-off.
- An ablation with different MB estimators (e.g., IAMB vs. PCMB) to show robustness to that choice.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The MB identification algorithm is unspecified."** Removed because the parser strips the appendix, where this information likely resides (the paper mentions "comparison with DCILP... where we also implemented the MB solver used in that work" and "we also provide a flexible interface"). The hard rule states that missing appendix content should not be treated as a weakness.
- **"Missing related works."** The hard rule prohibits mentioning missing related works since external sources are not available to confirm existence.
- **Pure formatting/style nitpicks and request for more related work discussion.** Removed per the filtering rules.
- **Strength: "This paper addressed an important problem."** Removed as generic/superficial. The retained strengths are concrete and grounded.
- **"The model-agnostic claim is misleading because the MB solver must still be chosen."** The paper explicitly states "places no restrictions on the choice of Markov Blanket identification algorithm" (line 27) and "fully plug-and-play with respect to MB identification" (line 31). The claim is about model-agnosticism w.r.t. base learners, not about eliminating all user choices.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Revise the theoretical framing.** Either (a) drop the asymptotic consistency claim or explicitly state that m is bounded and analyze finite-m behavior (the actual operating regime); or (b) reformulate Theorem 3.5 as a statement about what *would* hold if m grew with n, clearly labeling it as a qualitative insight rather than a guarantee for the algorithm. The current presentation overpromises.
2. **Acknowledge the m = C log n issue explicitly** in the limitations or directly after Theorem 3.5.
3. **Adjust the summary language** — the abstract and conclusion should say "improves structural accuracy (as measured by F1, SHD, FDR) while substantially reducing runtime" rather than implying monotonic gains in all metrics.

---

## Score and Decision

### Calibration Anchors

**Round 1 (bracketing):**
- Weak anchors (0–3): `MHy7PnRcRO.md` (3.0), `tHKxko3j2m.md` (2.0), `2T5SpHS9QQ.md` (3.0), `vSAWV43kvs.md` (3.0) — all scores 3 or below, clearly weaker than the current paper.
- Middle anchors (4–7): `4XVczusV2K.md` (5.5), `WtbPaWO8lH.md` (6.0), `V7pT2ZRoTB.md` (4.5), `7K8mS5QNkf.md` (4.5) — most relevant comparison.
- Strong anchors (8+): `Ahdsg2nkNH.md` (8.0), `nCsF3Bsn2n.md` (8.0), `248ysaRatx.md` (8.0), `qOyF214xmg.md` (8.0) — unrelated topics (quantum computing, kernel methods, language models), not comparable.

**Round 2 (narrowing):**
- `WtbPaWO8lH.md` (6.0) — "Causal Discovery in the Wild": most structurally similar (voting aggregation for causal discovery with theoretical guarantees under independence assumptions). Accepted as poster. The VISTA paper has broader empirical coverage (6 vs. ~3 base methods, runtime analysis) but weaker theory (the m = C log n issue is more severe than CDW's acknowledged independence gap). VISTA is slightly below this anchor → score < 6.
- `V7pT2ZRoTB.md` (4.5) — "Theoretical Guarantees for Causal Discovery on Large Random Graphs": Accepted as poster but with concerns about practical relevance. VISTA has much stronger empirical validation and a practically deployable framework → score > 4.5.
- `N9RyL52z7y.md` (4.5) — "Efficient Ensemble CIT": divide-and-conquer for CIT, also with theory-practice gaps (e.g., subset size contradiction). Accepted as poster. VISTA has a broader contribution (full structure learning pipeline vs. a component) → score > 4.5.
- `7K8mS5QNkf.md` (4.5) — "Improving constraint-based discovery with LLM priors": Rejected. VISTA is stronger (cleaner design, more thorough evaluation) → score > 4.5.

**Bracket:** Round 1 placed the paper between 5 and 7. Round 2 anchors narrow this: VISTA is weaker than the 6.0 CDW anchor (due to the more structural theory gap) but stronger than the 4.5 anchors. Final score: **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>