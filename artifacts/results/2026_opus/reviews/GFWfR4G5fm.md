Now I have a good understanding of the paper. Let me run calibration retrieval.Based on Round 1 anchors, this paper sits between 4 and 6. Let me narrow.## Summary
The paper diagnoses three failure modes of static Supervised Causal Learning (SCL) — fragility under distribution shifts, failure in compositional generalization, and a synthetic-to-real performance gap — and proposes a Test-Time Training framework (TTT-SCL) that dynamically generates a training set aligned with each test instance. The concrete instantiation, TACTIC, performs a stochastic search over DAGs scored by an "Alignment of Distribution" (likelihood) term plus an L0 sparsity penalty, forward-samples synthetic data from the resulting graphs, and trains an SCL backbone on it. Empirically, TACTIC outperforms AVICI and traditional baselines on the Sachs and SynTReN benchmarks.

## Strengths
- **Compositional generalization is empirically isolated.** Figure 2 shows that even when *all* individual mechanism/graph/noise components are seen in training, "Component-mixed" AUROC is consistently below i.i.d. across all six synthetic settings. This is a sharper diagnosis than the "missing component" framing in prior work (Section 3.2, Issue 2).
- **Substantial gains on real / pseudo-real benchmarks** (Table 2): TACTIC (Notears) reaches 78.9 AUROC on Sachs vs. 62.3 for AVICI (scm-v0) and 67.1 for PC, and 80.1 on SynTReN vs. 65.4 for AVICI. The absolute gap is large enough to support the central claim that test-time concentration helps on real data.
- **Sparsity ablation directly supports the design choice.** Table 3 shows large drops when the L0 penalty is removed (e.g., Chebyshev_G 83.0 → 69.7; Sachs 78.9 → 63.5), giving direct evidence that sparsity, not AD alone, is doing real work.
- **Stage-wise analysis (Table 4)** documents a consistent monotone improvement chain seed → highest-score → SCL output across four domains, anchoring the claim that the supervised-learning stage adds value beyond classical score-based search.

## Weaknesses

### Fatal
None.

### Major
- **The mechanism behind the "2→3" lift in Table 4 is not explained.** The paper's own central distinction from classical score-based search is that the SCL model trained on TACTIC-generated graphs (e.g., Sachs 78.9) outperforms the highest-scoring graph the search itself found (66.6). But the SCL model only ever sees forward-sampled data from graphs whose AUROC is in the 66–80 range; the paper does not state which of the obvious explanations (ensemble denoising over K=200 graphs, residual prior knowledge in the SCL backbone, score-correctness correlation, etc.) is operating. Section 4.4 frames this as the "fundamental distinction" yet offers no isolation of the mechanism, and the paper does not include the most natural controls (majority vote over the K graphs, simple aggregation, or argmax-score at matched compute). Without this, the headline result is suggestive rather than mechanistically supported.
- **The AD score is a standard conditional log-likelihood and the search is a standard MH-style move set.** Eq. (3) is a per-variable conditional log-likelihood, Eq. (4) is L0, and Section 4.2 describes add/delete/reverse moves accepted with a score-ratio probability. This is precisely the structure of likelihood + sparsity score-based search (GES-family). The novelty therefore rests on the SCL post-processing — which is exactly the part that is not isolated experimentally (see point above). The paper does not provide a head-to-head comparison against a likelihood+L0 search-only baseline using the same move set and compute, so the contribution of the SCL stage is not directly demonstrated.

### Minor
- **Real-world claims rest on a thin evidence base.** The "static SCL fails on real data" diagnosis (Section 3.2, Issue 3 / Table 1) and the headline real-world wins (Table 2) rely on Sachs (11 nodes) plus SynTReN. No variance is reported for the Sachs/SynTReN entries (other columns include stddevs), and Sachs is well known to be sensitive to evaluation choices. Appendix G is cited for additional bnlearn graphs but the body's headline real-world claim is anchored on two datasets.
- **Coherence between motivation (Issue 2) and remedy is loose.** Section 3.2 frames compositional generalization failure as a primary motivation, but TACTIC does not teach compositional structure — it bypasses composition by re-fitting per-instance, with noise defaulted to N(0,1) (Section 4.2, Stage 3). The motivational arc would be more honest if it stated that TACTIC sidesteps composition rather than solves it.
- **The acceptance rule in Figure 3 is ill-defined for negative scores.** The score in Eq. (5) is `log-likelihood − λ·L0`, which can be negative; the displayed acceptance probability min[1, score(G_{k+1})/score(G_k)] is not a valid MH ratio over such a score. The paper does not state whether the actual rule uses exp(score), the raw score, or something else — a reproducibility-relevant ambiguity.
- **Eq. (3) notation is loose:** `log p(X_i | f_i^k)` conditions on a fitted function rather than on Pa_G(X_i); the regressor used in SIM (which controls how dense graphs score under AD) is not specified in the main text. This matters because flexible regressors will mechanically inflate AD for denser graphs, partially motivating the sparsity penalty.
- **Ablation breadth is limited.** Only the sparsity term is ablated in the main text; K, seed source (random vs. NOTEARS vs. PC), and SCL backbone choice are not varied in the body.

### Trivial
- Figure 2's bar labels of the form "RFF_G_62.3" / "RFF_G_97.8" conflate dataset + a numerical score, making it hard to map bars to model configurations from the text alone.
- The phrasing "state-of-the-art on all other datasets" is mildly overstated for Linear_U, where TACTIC (Notears) 86.3 vs. NOTEARS 82.0 sits within one stddev (Table 2).

## Nice-to-Haves
- A direct head-to-head baseline that runs TACTIC's stochastic search and returns either its argmax-score graph or a majority vote over its K=200 graphs (no SCL training), matched on compute. This would isolate what the SCL stage actually contributes.
- Seed-level variance for Sachs and SynTReN, and a main-text view in SHD/F1 alongside AUROC.
- An analysis of how often edges in the SCL output appear in the majority of the K=200 search-derived graphs, which would either confirm "ensemble denoising via a neural net" or surface that the SCL stage is doing something else.

## Removed Points
*These points are flagged to be removed; treat them with caution.*
- **Harsh critic's Section-by-section nitpick that "AVICI scm-v0's column for RFF_G (97.8) is bold while TACTIC (Notears) is bold elsewhere"** — this is in fact the appropriate bolding convention and the critic acknowledges as much; it is not a real weakness.
- **"Concentration implies re-training per test instance, which is a different cost-benefit profile"** as a stand-alone criticism — the paper does point at Appendix F runtime analysis, and the cost-benefit critique becomes scope-creep without a concrete claim that the cost is prohibitive.
- **Strength Finder's "competitive performance on in-distribution synthetic data without prior exposure"** — TACTIC (Notears) 91.8 vs. AVICI 97.8 on RFF_G is a 6-point gap; calling this "approximating SOTA" is mildly generous and conflicts with the equally valid reading that AVICI dominates its training distribution. Demoted.

## Novel Insights
None beyond the paper's own contributions. The paper's compositional-generalization framing (Issue 2) is genuinely a more crisp diagnosis than the "missing components" view, but no novel insight emerges from the merged review beyond noting that — given the paper's own data — the TACTIC search → SCL-fit pipeline is best understood as a form of ensemble denoising over K=200 noisy candidate graphs, a story the paper itself does not articulate.

## Suggestions
- Add a search-only baseline (argmax over the K=200 graphs, and majority vote across them) at matched compute. This is the single change that would most strengthen the contribution.
- State the MH transition rule precisely in Section 4.2 and fix Figure 3 so the acceptance probability is unambiguously defined on a score that can be negative.
- Specify the regressor used in SIM in the main text, since AD's behavior under denser graphs depends on this.
- Either (i) include a Table-1/2 result on additional real benchmarks (the bnlearn graphs cited in Appendix G) in the body with seed-level variance, or (ii) soften the "real-world applicability" claim to the two datasets actually evaluated.
- Reframe the compositional-generalization motivation so that the paper explicitly states TACTIC bypasses rather than solves composition.

## Axis Evaluation
- **Originality:** Moderate. The TTT-SCL framing is novel for observational causal discovery, but the search components (likelihood, L0, MH-style refinement) are standard, and a closely related test-time-training-for-SCL paradigm exists in the interventional setting.
- **Importance of research question:** Real and well-motivated — SCL really does suffer the synthetic-to-real gap the paper identifies.
- **Claim support:** Mixed. The "TTT-SCL beats AVICI on Sachs/SynTReN" claim is supported by the numbers; the "SCL post-processing is the key novel mechanism" claim is not directly isolated.
- **Soundness of experiments:** Adequate but not strong. Single-dataset point estimates for the headline real claim, no compute-matched search-only control.
- **Clarity:** Reasonable; Eq. (3) notation, Figure 2 labeling, and the Figure 3 acceptance rule each need fixing.
- **Value to the research community:** The diagnostic findings (especially the compositional failure on i.i.d.-trained SCL) and the TTT-SCL framing are likely to influence follow-ups, but the specific TACTIC mechanism is incompletely characterized.

## Score and Decision

Anchors retrieved:

| Path | Avg | Round | Comparison |
|---|---|---|---|
| AvXrppAS2o.md | 3.00 | 1 | Much weaker — clinical CSL with vague claims; paper under review is stronger. |
| JzFLBOFMZ2.md | 3.20 | 1 | Weaker — LLM-supervised CSL with limited validation. |
| TRHyAnInUC.md | 3.25 | 1 | Weaker — narrow regularization tweak. |
| fSxiromxAq.md | 3.00 | 1 | Weaker — sparse-CD method with thin support. |
| lQYi2zeDyh.md | 5.00 | 1/2 | Comparable — analysis of CSIvA SCL; thinner scope (bivariate only) but cleaner story. |
| T6pC0E2ziE.md | 4.25 | 1 | Slightly weaker — SCL paper with identifiability gaps. |
| ToveGL9vRN.md | 5.50 | 1 | Comparable — faithfulness-limits paper, more diagnostic depth than method depth. |
| cbFqqtJGtA.md | 4.25 | 1 | Weaker — perturbation targets via causal nets, narrow setting. |
| xByvdb3DCm.md | 8.00 | 1 | Stronger — theoretically grounded selection-bias paper. |
| 3cuJwmPxXj.md | 8.00 | 1 | Stronger — identifiability theory for intervention extrapolation. |
| Nx4PMtJ1ER.md | 8.00 | 1 | Stronger — full CI test theory for SDEs. |
| hrqNOxpItr.md | 8.00 | 1 | Stronger — theoretical depth. |
| ZXs3pkmrRG.md | 5.50 | 2 | Closest analog — Test-time SCL for *interventional* data; the paper under review has a similar empirical-but-thin-mechanism profile. |
| HBf6HFnpmH.md | 5.50 | 2 | Comparable — scalability/benchmark paper with mixed reviews. |
| nmvmPIi185.md | 6.25 | 2 | Slightly stronger — neural causal graph for interpretability, accepted. |
| x3F8oPxKV2.md | 6.25 | 2 | Slightly stronger — zero-shot SCM learning with broader framing. |
| eeJz7eDWKO.md | 6.00 | 2 | Slightly stronger — meta-learning Bayesian CD, more theoretical depth, accepted. |
| iaP7yHRq1l.md | 5.50 | 2 | Comparable — robustness benchmark for differentiable CD. |
| i5JfdnCob7.md | 4.40 | 2 | Weaker — narrow kernel-selection tweak. |

**Round 1 bracket:** between 4 and 6. The paper is clearly above the 3.0–3.3 anchors (it has a coherent framework and substantial empirical gains) but does not approach the 8.0 anchors (no theoretical contribution, central mechanism unexplained).

**Round 2 narrowing:** the closest analog is ZXs3pkmrRG (TTT for interventional SCL, 5.50, Reject) — same paradigm, similar mixed reception (large empirical wins, presentation and mechanism concerns from reviewers). The paper under review is roughly comparable in profile: strong empirical real-world numbers, but a key mechanism (the SCL stage's lift over search's own argmax) is asserted rather than isolated, and the real-world evaluation is thinner (2 datasets in body vs. 14 bnlearn in TICL). It is weaker than the 6.0 anchor (eeJz7eDWKO) which had genuine theoretical depth, and stronger than the 4.25 anchor (T6pC0E2ziE) which had identifiability gaps.

Settling near the ZXs3pkmrRG anchor but slightly below it (thinner real-data evaluation, less-isolated novel component): **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>