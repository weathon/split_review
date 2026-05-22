Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper identifies and experimentally demonstrates three key limitations of static pre-training in supervised causal learning (SCL) — fragility to distribution shifts, failure in compositional generalization, and a synthetic-to-real generalization gap. To address these, it proposes TTT-SCL, a framework that dynamically generates training data aligned to each test instance, operationalized via an Alignment of Distribution (AD) metric combined with sparsity constraints. The instantiation, TACTIC, uses stochastic graph refinement guided by AD + sparsity to construct test-specific training sets and then trains an SCL model, achieving strong results on synthetic benchmarks, the Sachs real-world dataset, and the Syntren pseudo-real dataset.

## Strengths

1. **Well-executed diagnosis of SCL limitations (Section 3).** The paper systematically demonstrates, through controlled experiments (Figure 2), that static SCL models degrade under graph/mechanism/noise shifts and, more fundamentally, fail at compositional generalization even when all individual components are seen during training. The "Component-mixed" condition is a genuinely informative experimental design that reveals memorization rather than modular understanding. This diagnostic contribution is valuable independent of the proposed method.

2. **TACTIC achieves strong results on the Sachs real-world dataset.** Table 2 shows TACTIC (Notears) reaching 78.9 AUROC on Sachs, substantially above all baselines (next best: PC at 67.1, AVICI at 62.3). This directly demonstrates that test-time alignment can bridge the synthetic-to-real gap diagnosed in Issue 3. The gain on Syntren (80.1 vs. AVICI's 65.4) provides corroborating evidence on a second, biologically-structured benchmark.

3. **Stage-wise analysis (Table 4) isolates the two-stage improvement.** The paper shows that TACTIC's final SCL output (91.8 on RFF_G, 86.3 on Linear_U, 83.0 on Chebyshev_G, 78.9 on Sachs) consistently outperforms both the seed graph and the highest-scoring graph from the search (e.g., 78.9 vs. 66.6 on Sachs). This provides _prima facie_ evidence that the SCL phase adds value beyond the score-based search, distinguishing TACTIC from classical score-based approaches.

4. **Sparsity ablation confirms the necessity of the constraint.** Table 3 shows removing the sparsity penalty drops performance sharply (e.g., Sachs: 78.9 → 63.5; Chebyshev_G: 83.0 → 69.7), validating that optimizing AD alone leads to degenerate dense graphs and that the joint formulation is critical.

## Weaknesses

### Major

1. **Missing controlled comparison against simpler test-time adaptation.** TACTIC's core claim is that the full two-stage pipeline (search + SCL training on generated data) outperforms static methods. But the paper does not include a baseline that also adapts to the test instance in a simpler way — for example, fine-tuning the pre-trained AVICI model on D_test (using the same likelihood-based objective), or simply using the highest-scoring graph from the search directly without the SCL step. Table 4 partially addresses this (comparing search output vs. SCL output), but the comparison to AVICI (scm-v0) conflates two differences: (a) test-time adaptation vs. static, and (b) the specific TTT-SCL mechanism vs. simpler forms of adaptation. Without a baseline like "AVICI fine-tuned on D_test data," we cannot tell whether the gains come from any form of test-time training or from TACTIC's specific design. This is the most significant gap in the evaluation.

2. **Limited real-world validation relative to the paper's claims.** The paper frames the synthetic-to-real gap as "the primary bottleneck for SCL" and claims TACTIC addresses real-world applicability. Yet the only real-world dataset with ground truth is Sachs (11 variables, 853 samples). Syntren is pseudo-real (simulated gene expression), and the bnlearn benchmarks mentioned in Appendix G are small (5–8 variables). This is thin support for sweeping claims about real-world applicability. Additional real-world datasets of moderate size would substantially strengthen the evidence.

### Minor

3. **The mechanism by which the SCL model improves over the highest-scoring search graph is not explained.** Table 4 shows that the final SCL output outperforms the highest-scoring graph found during search. The paper's explanation ("learns more accurate causal relationships") is vague. It could be simple ensembling of multiple candidate graphs, or it could be that the SCL model's inductive bias is beneficial. A controlled comparison against an ensemble of the top-K search graphs (e.g., averaging edge probabilities) would clarify whether the SCL model provides value beyond what a simple combination of candidates would achieve.

4. **No ablation of the number of generated training instances K.** K=200 is fixed without sensitivity analysis. The paper does not examine whether fewer instances suffice or whether performance continues to improve with more. This is a practical parameter that affects computational cost and should be characterized.

5. **No discussion of sensitivity to the noise distribution used for forward-sampling training data.** The method defaults to standard Gaussian noise for generating training data, even though test data may have non-Gaussian noise. The paper does not test whether this mismatch matters or discuss potential robustness.

6. **Technical concern about the iterative search refinements.** The MCMC-like refinement (Section 4.2) uses a Metropolis-style acceptance rule based on score ratios. But the score function (likelihood + sparsity) is not guaranteed to concentrate around the true graph — any DAG that fits the data well with few edges can score highly, including ones with incorrect edges that happen to have negligible effect on likelihood. The paper does not discuss whether the search could converge to high-scoring but structurally incorrect graphs and how this would affect the training data quality.

## Nice-to-Haves

- A comparison against an ensemble of top-K candidate graphs (averaged edge probabilities) to isolate whether the SCL model provides value beyond simple candidate aggregation.
- Sensitivity analysis on K (number of training graphs).
- A controlled variant where the pre-trained AVICI model is fine-tuned on the test data D_test using the same likelihood objective.
- A discussion of how the noise distribution used in forward-sampling (Gaussian by default) interacts with test data where noise is non-Gaussian.
- Runtime/scalability analysis (noted as in Appendix F, which was not available for review).

## Removed Points

These points were considered but removed from the main review:

- **"Unfair comparison — TACTIC has access to test data while baselines don't":** This is incorrect. All baselines (PC, GES, NOTEARS, etc.) also use D_test directly. TACTIC uses D_test more extensively, but this is the point of test-time training, not a flaw. The real issue (covered in Major #1) is the absence of a baseline that also spends extra test-time computation on adaptation.
- **"Conceptual circularity — the candidate graphs are already fits to test data":** This misinterprets the method. The candidate graphs are indeed evaluated on D_test, but the SCL model is trained on *generated* (forward-sampled) data, not D_test itself. Table 4 shows that this SCL training phase does improve over the candidate graphs.
- **"No discussion of identifiability":** The paper explicitly states in Section 4 that the method applies under standard identifiability assumptions (LiNGAM, ANM, PNL).
- **"No discussion of computational cost / complexity":** The paper references Appendix F for complexity analysis. The appendix was stripped during parsing.
- **"The sparsity ablation only confirms an expected result":** A negative result from an ablation is still informative. The magnitude of the drop (especially on Sachs) is useful evidence.
- **"Missing related works":** Hard rule prohibits this criticism.

## Novel Insights

The most insightful observation that emerges from this review is that the paper's strongest contribution may actually be its diagnostic work in Section 3 (the systematic documentation of SCL's compositional generalization failure) rather than the TACTIC method itself. The "Component-mixed" experiments reveal that SCL models memorize configurations rather than learning modular causal representations — a finding that has implications for how SCL training sets should be designed even independently of test-time adaptation. Meanwhile, the main methodological question the paper raises but does not fully resolve is: what exactly does the SCL model contribute beyond the search? Table 4 shows *that* it contributes, but the mechanism remains opaque. If the SCL model primarily serves as a denoising aggregator over the search trajectory's high-scoring graphs, then TACTIC is better understood as a hybrid method (score-based search → learned aggregation) than as a true test-time training approach.

## Suggestions

1. Add a controlled baseline where AVICI is fine-tuned on D_test (using the same likelihood-based objective or a simple fine-tuning loss) for a comparable amount of computation. This would directly test whether the improvement comes from test-time adaptation in general or from TACTIC's specific pipeline.
2. Add an "ensemble of top-K candidate graphs" baseline for Table 4 to isolate the SCL model's contribution.
3. Include at least one additional real-world causal discovery benchmark of moderate size (e.g., from the bnlearn or CauseMe suites) to strengthen the real-world applicability claims.
4. Add an ablation varying K (number of training graphs) from small (e.g., 10, 50) to larger (e.g., 500) to characterize sensitivity.
5. Discuss the noise distribution choice and its potential impact when test noise is non-Gaussian.

## Score and Decision

**Calibration summary:**
All retrieved anchors are listed below with their avg human score, retrieval round, and comparison to this paper:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| ZXs3pkmrRG (TICL) | 5.50 | R2 | Similar paper (also test-time causal learning). TICL was rejected for limited novelty and unclear contributions. This paper is stronger on problem diagnosis and novelty of the TTT-SCL framework, but shares the concern about missing simpler adaptation baselines. **This paper is moderately stronger.** |
| lQYi2zeDyh (Demystifying amortized CD) | 5.00 | R2 | Analysis-only paper limited to bivariate causal discovery. This paper has broader scope and proposes a method, making it stronger. |
| x3F8oPxKV2 (Zero-shot causal models) | 6.25 | R1/R2 | Novel amortized framework but rejected due to strong assumptions (needs noise samples) and limited evaluation. This paper has more practical evaluation but weaker theoretical grounding. **Comparable overall quality.** |
| pOoKI3ouv1 (Robust agents) | 5.75 | R1 | Pure theory paper (accepted despite no experiments). Different type of contribution, not directly comparable. |
| wmV4cIbgl6 (CausalRivers) | 7.33 | R2 | Large-scale real-world benchmark for causal discovery. Stronger evaluation but different contribution type. This paper has weaker real-world validation. |
| AvXrppAS2o, JzFLBOFMZ2, jFox1iMWUa, 4LiegvCeQD | 2.5–3.4 | R1 | Weak papers on related topics. This paper is clearly much stronger. |
| bMvqccRmKD, zwMfg9PfPs | 6.75–7.00 | R1/R2 | Accepted papers on causality-guided generalization. This paper is slightly weaker due to evaluation gaps. |

**Round 1 bracket:** 5.0–7.0 (weak anchors at 3.0 → this paper is clearly stronger; strong anchors at 8.0 → this paper is clearly weaker).

**Round 2 narrowing:** Anchors in the 5.0–7.5 range placed this paper near the 5.5–6.5 zone. The most directly comparable paper (TICL, 5.50) is weaker on diagnosis and framework novelty. The zero-shot causal models paper (6.25) is comparable in novelty but was rejected for assumptions and limited evaluation. This paper falls between them.

**Final score:** 6.0. The paper makes genuine contributions — the diagnosis of SCL limitations is strong and the TTT-SCL framework is well-motivated. But the evaluation has a significant gap (no simpler test-time adaptation baseline) that prevents the empirical claims from being fully substantiated, and the real-world validation is thin. With additional controlled experiments and real-world benchmarks, this could be a stronger paper.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>