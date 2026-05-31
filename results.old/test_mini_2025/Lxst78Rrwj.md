Now I have all the information I need to write the consolidated review. Let me formulate my analysis.

**Calibration summary:**

**Round 1 (Bracketing):**
- Weak anchors (<3.5): avg 3.0–3.4 — rejected causal papers with limited contributions. GLIDE is clearly above these.
- Middle anchors (3.5–7.5): scores 4–7 — mixed accept/reject.
- Strong anchors (>7.5): avg 8.0 — oral/poster level (e.g., "When Selection Meets Intervention", "Robust agents learn causal world models"). GLIDE is not at this level.

**Round 2 (Narrowing):**
- COSMO (avg 5.6, poster): Improved scalability for differentiable DAG learning; novelty concerns. GLIDE has stronger novelty.
- Meta-Learning Bayesian CD (avg 6.0, poster): Well-written with good experiments; novelty concerns. GLIDE has comparable contribution level.
- Intersort (avg 7.0, poster): Strong theory, first method for causal order from interventions; no real-world experiments. GLIDE has better real-world validation but weaker theoretical guarantee.

GLIDE sits at about 6.0 — above the acceptance threshold with genuine novelty and strong empirical results, but the one-directional invariance guarantee and some framing issues keep it from being higher.

---

## Summary

This paper proposes GLIDE, a causal discovery framework that exploits a novel invariance property: the conditional distribution P(effect|cause) is invariant to changes in the prior distribution of causes. The method (1) identifies "basis" variables as surrogates for source variables, (2) constructs augmented datasets with systematically varied source priors via a downsampling scheme, (3) tests candidate parent sets by measuring variance of estimated conditionals across augmentations, and (4) exploits Markov blankets and maximal-clique enumeration to restrict the search space to O(d) candidates per variable, yielding quadratic overall complexity. Experiments on synthetic (linear-Gaussian, non-linear non-Gaussian, categorical) and seven real-world benchmarks (including the 1041-variable Munin graph) show strong performance, often achieving the best SHD and spurious rate among baselines.

## Strengths

1. **Novel invariance principle for causal testing.** Theorem 1 formalizes a genuinely new test for causal relationships: non-zero variance of P(X|Z) across changes in source priors implies Z ≠ Pa[X]. This principle has not been exploited in prior constraint-based, score-based, or model-based causal discovery methods and opens a new direction for the field.

2. **Strong empirical results on large-scale graphs.** On the 500-node L-G synthetic graph (Figure 2), GLIDE achieves a 4.2% spurious rate versus the next best baseline at 11.75%. On the real-world Munin dataset (1041 variables, Table 2), GLIDE attains a spurious rate of 1.8% and SHD of 883.2, substantially outperforming GIES (42.4% spurious rate, 1235 SHD). These results convincingly demonstrate practical value.

3. **Quadratic overall complexity.** The combination of Markov blanket identification (Edera et al., 2014, O(d²)), basis identification (O(d²)), and maximal-clique enumeration on sparse augmented graphs (empirically p ≤ 13) yields O(md² + m|D| + m|B|) total complexity. This avoids the exponential search of constraint-based methods and the heavy optimization of score-based approaches.

4. **Versatility across diverse data models.** As shown in Table 1, GLIDE is the only evaluated method that works effectively on all four data-model categories (L-G, nL-nG, categorical synthetic, categorical real-world), whereas baselines like NOTEARS, DAS, and SCORE are limited to continuous data.

5. **Principled data-augmentation procedure.** Theorems 4 and 5 provide a closed-form expression for the minimal downsampling rate needed to realize a target source prior, and Theorem 6 characterizes the convex hull of admissible priors. This ensures the invariance test uses as much data as possible while inducing meaningful distribution shifts.

## Weaknesses

### Fatal
None.

### Major
1. **One-directional theoretical guarantee for the invariance test (verified from Section 4.1).** Theorem 1 proves V[P+(X|Z)] > 0 ⇒ Z ≠ Pa[X], but the converse (zero variance implies Z = Pa[X]) holds only in the limit of infinitely many source priors (m → ∞). In the finite-sample regime used throughout the experiments, the test is an empirically motivated heuristic. The paper acknowledges this ("might not be perfect but remains highly accurate") and the empirical results are strong, but the central test of the method lacks a finite-sample theoretical guarantee. This does not invalidate the contribution but limits the paper's conceptual crispness.

2. **The "up to 25× reduction in processing time" claim is selective (verified from Sections 1 and 5.1).** The 25× speedup appears in the nL-nG extreme setting (Figure 3) against NOTEARS/MLP-NOTEARS. On real-world categorical data (Table 2), GLIDE is substantially *slower* than GIES on every dataset — e.g., 6200 seconds vs 61 seconds on Munin (~100× slower). The abstract presents this speedup as a general advantage without qualification; the paper should frame its scalability claims more carefully to reflect the accuracy–runtime trade-off.

### Minor
1. **Ad hoc procedure for sampling source priors (Section 4.2.4).** The method samples 10⁴ Dirichlet vectors, clusters them with K-means, and uses the m centroids as source priors. No justification is given for why 10⁴, why K-means, or how sensitive the results are to the number of clusters m. While a practical heuristic can be acceptable, this step is not ablated or analyzed.

2. **No explicit limitations section.** The paper does not discuss its reliance on causal sufficiency (no unobserved confounders), potential errors in Markov blanket identification (Edera et al., 2014), or the propagation of errors from pairwise independence tests used in basis identification (Theorem 3). These are real limitations that should be acknowledged in a revised version.

3. **Missing analysis of how errors in preprocessing propagate.** The basis identification (Theorem 3) and Markov blanket identification both rely on statistical tests whose errors could cascade into the invariance test. The paper does not analyze this error propagation.

### Trivial
None.

## Nice-to-Haves
- An ablation that isolates the contribution of the invariance test versus the Markov-blanket-based parent enumeration (e.g., replacing the invariance test with a simpler criterion like conditional mutual information).
- A controlled experiment showing that the variance of P(X|Z) for the true parent set is distinctively lower than for systematically varied false candidate sets (supersets, subsets, random sets).

## Removed Points
- *Criticism about missing pseudocode or algorithm details* — The Bron–Kerbosch adaptation is described in the paper (Section 4.3) and its appendix is referenced; the parser strips appendices. Similarly, missing bin width for continuous data will be in the appendix.
- *Criticism about missing newer baselines (2024+)* — The paper cites NOTEARS, DAS, SCORE (2022/2023), and the current date context makes this a moving target; the baseline selection is reasonable for the submission period.
- *"The paper should specify bin width for continuous data"* — This is a parser-induced artifact; implementation details would appear in the full appendix.
- *Several generic concern-sweep statements about "confounders not controlled" or "could the metric be measuring a proxy"* — These do not identify specific problems in the paper.
- *Strength about "addressing an important problem"* — Removed as generic/superficial.
- *Criticism about γ₀ not being in main text* — The paper states "Our ablation studies in Section 5 shows the impact of γ₀" and the appendix content is stripped by the parser.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Acknowledge more directly in the abstract and introduction that the 25× speedup is specific to continuous settings and that on real-world categorical data the method trades runtime for accuracy.
2. Add a limitations section explicitly discussing causal sufficiency, preprocessing error propagation, and the finite-sample gap in the invariance test.
3. Provide ablation on the K-means clustering step for source prior selection (sensitivity to m, justification of 10⁴ samples).
4. Include a controlled experiment showing variance discrimination between true parent sets and false candidates (supersets, subsets) to build trust in the invariance test.

## Score and Decision

**Calibration anchors used:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `etnG659OB9.md` (Causal Disentangled...) | 3.0 | R1-bracket(<3.5) | Much weaker — limited experiments, no real-world validation |
| `4u0ruVk749.md` (DFITE) | 3.0 | R1-bracket(<3.5) | Much weaker — different subfield, weaker results |
| `JzFLBOFMZ2.md` (LLM-supervised CSL) | 3.2 | R1-bracket(<3.5) | Much weaker — narrow scope, weaker baselines |
| `lk2Qk5xjeu.md` (Unifying CRL) | 7.0 | R1-bracket(3.5-7.5) | Stronger theory, similar level contribution; accepted poster |
| `0sO2euxhUQ.md` (Latent SCM) | 4.0 | R1-bracket(3.5-7.5) | Weaker — limited experiments, no real data; rejected |
| `or8wkKoBP4.md` (Minimal Dependence Faithfulness) | 4.0 | R1-bracket(3.5-7.5) | Weaker — no experimental evaluation, purely theoretical; rejected |
| `u63OVngeSp.md` (Intersort) | 7.0 | R1-bracket(3.5-7.5) | Stronger theory, uses interventional data; no real-world experiments; accepted poster |
| `xByvdb3DCm.md` (Selection Meets Intervention) | 8.0 | R1-bracket(>7.5) | Much stronger — oral-level theoretical+empirical contribution |
| `KwaNnvj0b3.md` (Permutation Rank Test) | 6.0 | R2-narrow(4.5-6.5) | Similar level — method + theory + experiments; rejected (score 6,6,6,6) |
| `lrQlLqQase.md` (Dynamical View of Why) | 5.5 | R2-narrow(4.5-6.5) | Comparable — accepted poster, similar evaluation scope |
| `KWO8LSUC5W.md` (COSMO) | 5.6 | R2-narrow(5.5-7.5) | Similar contribution level (scalable DAG learning); accepted poster with novelty concerns |
| `eeJz7eDWKO.md` (Meta-Learning Bayesian CD) | 6.0 | R2-narrow(5.5-7.5) | Similar level — well-executed but limited novelty; accepted poster |

**Round-1 bracket:** 4.0–7.0. The paper is clearly above weak papers (3.0-3.4) and below oral-level papers (8.0).

**Narrowing:** After reading COSMO (avg 5.6), Meta-Learning Bayesian CD (avg 6.0), and the Permutation Rank Test (avg 6.0), GLIDE compares favorably in novelty and empirical thoroughness. It has a genuinely new invariance principle, strong large-scale results, and works across diverse data models. However, the one-directional theoretical guarantee and the selective speedup framing prevent it from being as strong as Intersort (7.0).

**Final score: 6.0** — a solid accept with genuine novelty and strong empirical validation, despite some theoretical limitations and framing issues that could be addressed in revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>