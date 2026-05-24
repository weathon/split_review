Now I have all the information needed to write the consolidated review.

## Summary

This paper identifies three fundamental limitations of static Supervised Causal Learning (SCL) — fragility under distribution shifts, failure at compositional generalization, and a performance gap between synthetic and real-world data — and proposes TTT-SCL, a framework that dynamically generates a customized training set for each test instance guided by a proposed Alignment of Distribution (AD) metric and sparsity constraints. TACTIC, the first instantiation, uses stochastic graph refinement seeded by a traditional method (e.g., NOTEARS) to construct aligned training data, on which an SCL model is trained at test time. Experiments on synthetic, pseudo-real (Syntren), and real-world (Sachs) data show strong performance across multiple settings.

## Strengths

- **Systematic empirical demonstration of three fundamental SCL limitations.** Section 3.2 (Figure 2 and Table 1) provides clean, quantitative evidence that static SCL pre-training fails under distribution shifts across graph structure, mechanisms, and noise; that models fail at compositional generalization even when all components have been seen individually; and that strong synthetic performance (AVICI at 97.8 AUROC on RFF_G) does not transfer to real-world data (62.3 on Sachs). This evidence directly motivates the paradigm shift and is the strongest part of the paper.

- **Novel TTT-SCL framework with a principled alignment objective.** The paper introduces test-time training to supervised causal learning, framing it as generating training data aligned with each test instance. The AD metric (Equation 3) is well-motivated — jointly capturing graph structure and mechanism similarity through likelihood — and the sparsity penalty (Equation 4–5) enforces causal minimality to prevent degenerate dense solutions. This is a clear conceptual advance over static pre-training.

- **Strong and consistent empirical results across diverse settings.** Table 2 shows TACTIC (Notears) achieving the highest AUROC on four of five settings (Linear_U: 86.3, Chebyshev_G: 83.0, Sachs: 78.9, Syntren: 80.1), with substantial margins over baselines on real data (78.9 vs. next-best PC at 67.1 on Sachs). The two-stage improvement analysis in Table 4 further decomposes gains into search improvement (seed → highest-score graph) and learning improvement (highest-score graph → final SCL output), cleanly distinguishing TACTIC from score-based methods.

- **Identification of compositional generalization failure as a distinct problem.** Section 3.2 (Issue 2) shows that SCL models fail on novel combinations of seen components, going beyond prior work focused only on unseen individual components. This reveals a more fundamental limitation of static pre-training than previously recognized and directly motivates test-time adaptation.

## Weaknesses

### Major

None. The paper's core claims are supported by evidence, and none of the identified issues invalidate the central contribution.

### Minor

- **The AD metric's contribution is not isolated by a direct ablation in the main text.** The paper claims that "AD and sparsity are indispensable and important elements" (line 231), but the ablation experiment (Table 3) only removes the sparsity term (λ=0). There is no control that replaces the AD-guided search with a naive alternative (e.g., random graph selection or selection based on sparsity alone). While the paper references Appendix E for further AD analysis, this gap in the main text weakens support for the central claim that AD-driven distributional alignment is what drives the improvement. The paper would be strengthened by showing that AD guidance matters beyond any generic search over plausible graphs.

- **Missing error bars for real and pseudo-real data in Table 2.** For Sachs and Syntren, TACTIC (Notears) results (78.9 and 80.1) and several baseline entries are reported as single values without standard deviations, while other columns include them. Without any measure of variance, the reader cannot assess whether the headline improvements on real data are statistically reliable.

- **Inconsistency in the acceptance rule description.** The text (line 177) says candidates are "accepted with probability proportional to its score," while Figure 3 shows the standard Metropolis acceptance ratio α = min(1, score(G_{k+1})/score(G_k)). These are different procedures. The paper should clarify the exact acceptance mechanism.

- **The AD likelihood formulation (Eq. 3) does not specify how the mechanisms f_i^k are estimated.** The paper says "regress the corresponding mechanisms" (line 150) without stating the regression method (linear regression? neural network? Gaussian process?). This matters for both reproducibility and understanding the computational cost, since each AD evaluation involves fitting mechanisms for all d variables. Additionally, forward-sampling uses standard Gaussian noise (line 178), which is inconsistent with the likelihood estimation if the latter uses noise variance estimated from regression residuals.

### Trivial

- The value of λ (the sparsity regularization coefficient in Eq. 5) is not stated in the main text; only λ=0 is used for the ablation.
- The number of refinement iterations and the cooling schedule (if any) are not specified in the main text.

## Nice-to-Haves

- A direct ablation comparing TACTIC (full) against a version that replaces AD with a random graph score (accept/reject uniformly or based solely on sparsity) would cleanly validate the AD metric.
- An analysis of sensitivity to seed quality (e.g., seeding with PC, random graphs of varying quality) would clarify whether the method can bootstrap from poor initializations.
- Wall-clock runtime for a typical test instance would contextualize the practical trade-off, especially since the paper claims applicability to "real-world settings."
- Additional baselines such as directly using the highest-scoring search graph (bypassing SCL training) or NOTEARS+thresholding would further clarify what the SCL model adds.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **Computational cost is "ignored" (from Harsh Critic).** The paper states "Complexity analysis and runtime variation with the number of nodes are detailed in Appendix F" (line 180–181). The appendix was stripped by the parser; the paper does acknowledge this issue. Downgraded to minor concern / nice-to-have.
- **"Missing discussion of limitations"** — This is standard in most papers and the appendix may contain it; the parser stripped it. Not a substantive weakness.
- **"Not discussing meta-learning for causal discovery"** — REMOVED per instructions about missing related works.
- **"Missing hyperparameter details (λ, iterations)"** — These are implementation details likely in the stripped appendix. Moved to trivial/nice-to-have.
- **"Reliance on seed graph raises questions about robustness"** — The paper transparently reports both random and NOTEARS seeds and discusses seed quality's role. The concern is real but overstated: the paper does not claim seed-independence and the stage-wise analysis (Table 4) shows consistent improvements from both seeds, just with different magnitudes.
- **"Strengthening the Paper on Its Own Terms" recommendations** — These are suggestions, not weaknesses. Several are reflected in Nice-to-Haves.
- **Strength Finder claims about "careful ablation isolating sparsity" and "compositional generalization identification"** — These are valid and retained.

## Novel Insights

None beyond the paper's own contributions. The review corpus does not surface a perspective on this paper that meaningfully extends what the paper itself says.

## Suggestions

1. Add a direct ablation of the AD metric: compare full TACTIC against a version with random (uniform) score assignment in the refinement step, keeping sparsity-based selection only. This would isolate whether AD-driven distributional alignment is responsible for the improvement over and above any structured search.
2. Report bootstrapped confidence intervals or standard deviations for the Sachs and Syntren results in Table 2.
3. Clarify the acceptance rule — stick to the Metropolis ratio shown in Figure 3 and update the text to match.
4. Specify the mechanism estimation method used in SIM (or reference the appendix where this is detailed).
5. State the value of λ used in experiments and the number of refinement iterations.
6. Provide wall-clock runtime in the main text or a clear pointer to where it appears, along with a brief qualitative discussion of the speed–accuracy trade-off.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing (all topics "supervised causal learning test time training causal discovery"):**

| Anchor | Score | Round | How it compares |
|--------|-------|-------|-----------------|
| AvXrppAS2o | 3.00 | 1 | Weak paper: marginal improvements over baselines, poor comparisons. Our paper is substantially stronger in motivation, method, and results. |
| JzFLBOFMZ2 | 3.20 | 1 | LLM-based CSL with limited novelty. Our paper has clearer contributions and broader evaluation. |
| fSxiromxAq | 3.00 | 1 | Limited-scope causal modeling paper. Not comparable in ambition or empirical scope. |
| TRHyAnInUC | 3.25 | 1 | Diffusion-based CD. Narrow contribution. Our paper addresses a broader problem with more comprehensive evaluation. |
| ZXs3pkmrRG (TICL) | 5.50 | 1 | **Most directly comparable.** Test-time learning for interventional causal discovery. Similar idea (TTT+SCL) but for interventional data. Our paper has stronger motivation (systematic OOD analysis), evaluates on real-world data (Sachs), and presents a cleaner framework. Similar gaps: missing details, unclear computational cost. Our paper is slightly stronger. |
| lQYi2zeDyh | 5.00 | 1 | Analysis paper on CSIvA (bivariate only). Limited scope. Our paper is a full method paper with broader experiments. |
| cbFqqtJGtA | 4.25 | 1 | Perturbation target prediction. Distant topic, lower quality. |
| 0sO2euxhUQ | 4.00 | 1 | Latent SCM learning. Different problem setting. |
| xByvdb3DCm | 8.00 | 1 | Top-tier theoretical causal discovery paper. Our paper is not at this level of theoretical depth. |
| Nx4PMtJ1ER | 8.00 | 1 | CI tests for stochastic processes. Different subfield. |
| 3cuJwmPxXj | 8.00 | 1 | Intervention extrapolation. Strong theoretical paper. |
| hrqNOxpItr | 8.00 | 1 | Theory of supervised learning. Different topic. |

**Round 2 — Narrowing (topics "test time adaptation causal discovery" and "causal discovery distribution shift"):**

| Anchor | Score | Round | How it compares |
|--------|-------|-------|-----------------|
| x3F8oPxKV2 (Zero-Shot SCM) | 6.25 | 2 | Zero-shot SCM inference. Strong idea but requires known causal graph and ANM assumption. Our paper addresses a harder problem (unknown graph) with fewer assumptions but has less thorough evaluation. Comparable quality. |
| bMvqccRmKD (CSR) | 7.00 | 2 | RL generalization via causality. Different domain, harder to compare directly. Higher score reflects stronger theoretical grounding and broader RL evaluation, but not directly comparable. |
| 22ywev7zMt | 5.67 | 2 | SSL OOD generalization. Different topic, lower relevance. |
| pOoKI3ouv1 | 5.75 | 2 | Theory paper on causal world models. Different domain. |
| FJjHQS2DyE | 5.67 | 2 | Domain adaptation. Different topic. |

**Round 1 bracket:** 5.5–7.0  
**Round 2 narrowed to:** 5.5–6.5, with the paper sitting between TICL (5.50) and Zero-Shot SCM (6.25), closer to the latter.

**Final score: 6.0.** The paper has a clear, timely contribution — the TTT-SCL framework is novel, the motivation is well-supported by empirical evidence, and the results on real-world data are compelling. However, the missing direct AD ablation in the main text, absence of error bars for real-data results, and a few unclear implementation details prevent it from reaching the 7+ tier. These are addressable issues that do not undermine the core contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>