Now I have everything I need. Let me synthesize the final review.

## Summary

This paper identifies three fundamental limitations of static supervised causal learning (SCL)—distribution shift fragility, compositional generalization failure, and poor synthetic-to-real transfer—and proposes a test-time training framework (TTT-SCL) that dynamically generates training data aligned to each test instance. The concrete instantiation, TACTIC, uses an alignment-of-distribution (AD) metric plus sparsity constraints to search for high-quality candidate graphs, trains an SCL model on the resulting data, and infers \(G_{test}\). Experiments on synthetic benchmarks, pseudo-real SynTReN, and real Sachs data show TACTIC (Notears variant) achieving 78.9 AUROC on Sachs (next best: PC at 67.1) and strong results on other datasets.

## Strengths

1. **Novel and well-motivated framework.** TTT-SCL is the first framework to introduce test-time training—a technique successful in other ML domains—to supervised causal learning. The shift from "diversity" (static pre-training) to "concentration" (test-time generation) is clearly argued and logically follows from the three documented failure modes of static SCL.

2. **Strong real-world empirical results.** TACTIC (Notears) achieves 78.9 AUROC on Sachs, a substantial 11.8-point improvement over the best baseline (PC at 67.1), and 80.1 on SynTReN (next best: AVICI at 65.4). These gains directly validate that test-time training overcomes the synthetic-to-real transfer gap that the paper identifies as Issue 3.

3. **Clear stage-wise analysis separating search from SCL learning.** Table 4 tracks seed graph → highest-scoring graph → final SCL output (e.g., Sachs: 61.8 → 66.6 → 78.9). This decomposition shows that the SCL model adds value beyond what the score-based search alone provides, which is the paper's core mechanistic claim.

4. **Ablation confirming sparsity's necessity.** Table 3 shows that removing the sparsity penalty causes large drops (e.g., Sachs 78.9→63.5, Chebyshev_G 83.0→69.7), empirically validating that the sparsity constraint prevents degenerate dense solutions.

5. **Thorough evaluation across distribution shifts.** The paper systematically tests distribution shifts along three SCM dimensions (graph, mechanism, noise) plus compositional generalization, giving a rigorous characterization of where and why static SCL fails.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Sachs and SynTReN results lack variance estimates.** Table 2 reports standard deviations for synthetic datasets but not for Sachs or SynTReN. While single-run evaluation on real data is common, the margin of uncertainty on these key results—especially Sachs (78.9) where the paper's strongest claim rests—is unknown. This is addressable by reporting bootstrap confidence intervals or results across multiple seeds of the stochastic refinement.

2. **Compositional generalization evidence is uneven.** The "Component-mixed" vs. i.i.d. drops in Figure 2 range from 3 points (RFF_G_62.3: 90→86; Linear_U_62.3: 92→89) to 11 points (Linear_U_97.8: 100→89). No standard deviations or significance tests are reported for these Figure 2 results. While the overall pattern supports the claim of compositional failure, the modest 3-4 point drops in some settings weaken the "fundamental limitation" narrative. The paper would benefit from statistical significance estimates.

3. **Ensemble-of-top-graphs baseline would strengthen the SCL-value claim.** Table 4 shows the SCL model outperforms the single highest-scoring graph, which supports the two-stage pipeline. However, an ensemble averaging the top-\(k\) graphs' edge probabilities would be a natural stronger baseline—if the SCL model still outperforms it, that would more convincingly show that the SCL model learns causal structure beyond what the score captures. As presented, the improvement could partially reflect ensemble averaging of the \(K=200\) graphs rather than genuine causal representation learning.

4. **The SCL model training procedure is underspecified.** The paper states "An SCL model is then trained on this set" (Section 4.2) and references Appendix F for complexity analysis, but does not clarify in the main text whether training is from scratch, uses a pre-trained backbone as initialization, or employs a lightweight architecture. The computational cost trade-off is acknowledged (Appendix F), but the ambiguity makes it harder to assess practical feasibility from the main paper alone.

5. **No ablation of the AD metric itself.** The paper ablates the sparsity term but does not compare AD against an alternative similarity metric (e.g., simple graph-structure distance or mutual information). While AD is well-motivated, an ablation showing that AD is preferable to a naive alternative would strengthen the design-choices section.

### Trivial
- In Table 1, the AVICI row label reads "AVICI (sem-v0)" instead of "AVICI (scm-v0)" (typo).
- The paper would benefit from a qualitative example on Sachs showing the seed graph, a high-scoring search graph, and the final SCL prediction, so readers can inspect the structural improvements visually.

## Nice-to-Haves
- Reporting runtime (wall-clock time) for a typical \(d=10, n=1000\) test case in the main text would help readers gauge practicality. (Appendix F covers this; a brief summary in the main text would improve accessibility.)
- Testing on larger graphs (\(d > 20\)) to probe scalability boundaries.
- Sensitivity analysis for the number of generated training graphs \(K\).

## Removed Points
These were flagged in the input reviews but are removed after cross-checking against the paper:

1. **"Method is computationally infeasible / no analysis provided"** — The paper explicitly states in Section 4.2: "Complexity analysis and runtime variation with the number of nodes are detailed in Appendix F." The parser strips the appendix, but the analysis exists in the original submission. Per hard rule: remove criticisms about missing appendix content.
2. **"AD metric is equivalent to score-based discovery; no added value demonstrated"** — Factually contradicted by Table 4, which shows the SCL model consistently improves over the highest-scoring graph (e.g., Sachs: 66.6→78.9). The paper explicitly frames the pipeline as two-stage and provides evidence that the SCL phase adds value.
3. **"Missing SCL baselines (Dai et al., Ke et al.)"** — The paper compares against AVICI (scm-v0), described as "the strongest publicly available SCL baseline" and the most widely followed architecture. Comparing against every published SCL architecture is not a realistic expectation.
4. **"No discussion of L0 norm optimization / sparsity handling"** — The search is discrete (edge additions/deletions/reversals); L0 is trivially computed as edge count, not differentiated. The paper is correct as written.
5. **"NOTEARS hyperparameter tuning not discussed"** — Standard NOTEARS is used as a seed initialization; the hyperparameter concern applies equally to the NOTEARS baseline itself and is a standard implementation detail.

## Novel Insights
The most interesting observation that emerges from these reviews is that the two-stage separation (score-based search → SCL training) is both the paper's strongest contribution and its most under-tested claim. The harsh critic's suggestion of an ensemble baseline—comparing the SCL output against an ensemble of top-scoring graphs—would cleanly resolve whether the SCL model genuinely learns causal structure beyond what the score function already captures. This is a concrete, targeted experiment that would strengthen an already solid paper.

## Suggestions

1. Report bootstrap confidence intervals or multi-seed results for Sachs and SynTReN in Table 2.
2. Add an ensemble baseline: average edge probabilities from the top-\(k\) scoring graphs and compare against the SCL model's output.
3. Include a brief statement in Section 4.2 on whether the SCL model is trained from scratch or initialized from a pre-trained backbone.
4. Add statistical significance (confidence intervals, paired tests) to the compositional generalization results in Figure 2.
5. Show a qualitative case study on Sachs comparing seed graph, highest-scoring graph, and final SCL output.

## Score and Decision

Calibration anchors consulted (all from the deepreview_13k_calibration set):

| Anchor Path | Avg Score | Comparison to current paper |
|---|---|---|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/zgM66fu0wv.md` | 2.50 (IRIS - LLM-based CD) | Much weaker: poorly motivated, unclear methodology |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/JzFLBOFMZ2.md` | 3.20 (ILS-CSL - LLM+CSL) | Weaker: lacks theoretical grounding, poor presentation |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/T6pC0E2ziE.md` | 4.25 (PAIRE - SCL architecture) | Weaker: narrower contribution, less convincing experiments |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/lQYi2zeDyh.md` | 5.00 (Demystifying amortized CD) | Comparable: both are well-written, but current paper has broader scope and stronger empirical contribution |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ZXs3pkmrRG.md` | 5.50 (TICL - TTT for interventional CD) | Very similar topic; current paper is clearer in contribution and has stronger real-world results |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/eeJz7eDWKO.md` | 6.00 (Meta-learning Bayesian CD) | Comparable; current paper is stronger empirically |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/x3F8oPxKV2.md` | 6.25 (Zero-shot learning of causal models) | Similar quality; current paper has stronger practical motivation and fewer limiting assumptions |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/bMvqccRmKD.md` | 7.00 (Causality-guided RL) | Higher-scoring but different domain; similar level of contribution relative to respective fields |

The paper makes a genuine contribution: it identifies a real weakness in static SCL (compositional generalization + synthetic-to-real transfer) and proposes a principled, empirically effective solution. The experimental evidence is strong overall, the method is well-motivated, and the ablations support the design decisions. The weaknesses are addressable—missing variance on real data, an ensemble baseline suggestion, and minor underspecification of the training procedure. Relative to the anchors, the paper sits above the 5.50 TICL paper (clearer contribution, stronger results) and the 5.00 analysis paper, and is comparable to the 6.25 zero-shot causal models paper. A score of 6.5 reflects this positioning.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>