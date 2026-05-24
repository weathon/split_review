Now I have all the information needed. Let me write the final consolidated review.

---

## Summary

This paper introduces INFO-SEDD, a method for estimating mutual information (MI), KL divergence, and entropy on high-dimensional discrete data using Continuous Time Markov Chains (CTMCs). The core idea is to bridge discrete diffusion models and information-theoretic estimation: by training a score model via the DWDSE loss on a CTMC with absorbing-state dynamics, the authors derive a tractable estimator (Equation 5) that avoids the "embedding trick" required by all competing methods. A single jointly-trained model suffices for both joint and marginal scores (Equation 6), and the estimator is accompanied by an explicit error decomposition (Equation 7). Experiments on synthetic data (where INFO-SEDD dominates 7 baselines at MI=10–50, D=10–50), text summarization (correlation with human consistency ratings r=0.74), and genomics (TATA-box motif discovery, label-randomization consistency tests) demonstrate the method's effectiveness.

## Strengths

1. **Sound theoretical framework with explicit error bound.** The derivation from CTMCs and Dynkin's formula to a tractable KL estimator (Equations 4–5) is rigorous and well-presented. Equation (7) provides an error decomposition separating estimation error (linear in score approximation error) from truncation bias (exponentially decaying in T), giving practitioners theoretical backing for the estimator's reliability.

2. **Strong empirical results on high-dimensional, high-MI synthetic benchmarks.** Table 1 is the paper's headline result: across MI=10–50 and D=10–50, INFO-SEDD produces nearly unbiased estimates (e.g., 9.92 ± 0.12 at true MI=10; 47.77 ± 1.18 at MI=50) while every competing method either severely underestimates, overestimates, or collapses. This directly addresses the known failure mode of variational estimators in high-MI regimes (McAllester & Stratos, 2020).

3. **Single joint model yields marginal scores via absorbing-state dynamics.** Equation (6) shows that with an absorbing-state CTMC, a model trained only on the joint distribution suffices for computing marginal score ratios. This is a genuinely clever property that reduces the number of required score networks from two to one and enables the sliding-window motif discovery application.

4. **Practical utility demonstrated in two distinct real-world domains.** In text summarization, INFO-SEDD's MI estimates correlate with human consistency ratings (Pearson r=0.740 for INFO-SEDD-C, Table 2), enabling model selection without custom embedding pipelines. In genomics, the method locates the known TATA-box motif in *Arabidopsis thaliana* promoters (Figure 5) via a sliding-window MI profile—a task that would require separate training runs per window with competing estimators.

5. **Comprehensive experimental methodology.** The paper includes synthetic ground-truth benchmarks, theoretically motivated consistency tests with label randomization, model-selection correlation analysis, and an entropy estimation experiment on Ising models (Appendix D). The use of identical backbones (MDLM-SMALL for text, CADUCEUS for genomics) across all methods ensures fair comparison.

## Weaknesses

### Fatal

None.

### Major

None. The identified issues are significant enough to warrant author attention but do not undermine the paper's core contribution.

### Minor

1. **Systematic bias at ρ=0 in the text consistency test is acknowledged but not analyzed.** When text-summary pairs are completely randomized (ρ=0), a correct estimator must yield MI≈0. INFO-SEDD-J produces estimates of roughly 100 nats and INFO-SEDD-C roughly 50 nats (Figure 1). The paper notes that INFO-SEDD-C is "closer to zero" but does not analyze the source of this positive intercept—whether it is dominated by the truncation bias term in Equation (7), score-model approximation error, or the omitted terminal term. The log-scale plot partially obscures the magnitude of this deviation. While the trend *slope* is captured, the failure to recover the zero-MI baseline reduces the strength of the consistency claim. A controlled experiment varying the diffusion horizon T could isolate the source.

2. **The "lightweight" and "efficient" framing overstates computational parsimony.** The abstract and conclusion characterize INFO-SEDD as "lightweight" and "efficient." In practice, the method requires training a discrete diffusion model under the DWDSE loss, which is a heavier procedure than training the simple neural networks used by variational competitors (MINE, SMILE, KL-DIME, etc.). The paper claims faster convergence in epochs (Appendix C.1.3) but provides no wall-clock or GPU-hour comparison. For practitioners choosing between a quick variational estimator and a diffusion-based one, the accuracy–cost trade-off is the primary consideration. The contribution is genuine and important, but reframing or providing a cost analysis would better match reader expectations.

3. **The genomics consistency reference relies on an unstated Bayes-optimality assumption.** The reference MI curve in Figure 4 is constructed by setting H(Y|X) = H_b(Acc.), where Acc. is the accuracy of a CADUCEUS-based classifier. This equality holds exactly only if the classifier is Bayes-optimal (or near-optimal). The paper hedges ("approximate order-of-magnitude and slope") but does not discuss whether the classifier meets this requirement, making the reference a plausible lower bound rather than a verified ground truth. This weakens but does not invalidate the genomics consistency evidence.

4. **The sliding-window motif discovery claim would benefit from direct validation.** The paper claims INFO-SEDD "natively supports MI estimation between subsets of DNA sequences" and uses this property to compute a MI profile for TATA-box identification (Figure 5). While Equation (6) provides theoretical justification that marginal scores can be extracted from the joint model, the practical generalization of the score model to the out-of-distribution masking patterns at inference time is not experimentally validated. A sanity check—comparing the sliding-window estimate from the full-sequence model against a model trained directly on a specific window—would either confirm the claim or reveal its limits. As presented, the MI profile is an interesting qualitative observation rather than a fully validated result.

5. **Variance not reported for real-world experiments.** Standard deviations over independent training runs are reported for the synthetic benchmark (Table 1, 10 seeds) but not for the text and genomics applications. Given the inherent stochasticity of diffusion training, reporting variance estimates for the real-world results would strengthen the evaluation.

### Trivial

- The paper would benefit from explicitly noting that the error bound in Equation (7) is not empirically evaluated for tightness. This is a natural follow-up experiment.
- Minor: the figure labels in Figures 2 and 3 appear to have rendering artifacts (model identifiers M5–M100 overplotted on the axes).

## Nice-to-Haves

- A wall-clock or GPU-hour comparison between INFO-SEDD and the baseline methods on the synthetic benchmark would directly address the "lightweight" framing concern.
- An empirical evaluation of the tightness of the error bound in Equation (7) on synthetic data would add significant value.
- The sliding-window motif discovery would be strengthened by a comparison against a baseline of training separate models per window (or validating against a known-masked synthetic dataset).

## Removed Points

These points were raised by reviewers but are removed or demoted after verification against the paper:

- **"Unvalidated Assumption Underlying the Motif Discovery Experiment" as a fatal flaw:** The paper provides theoretical justification (Equation 6, Appendix A.3) for why marginal scores can be extracted from the joint model. The concern about distribution shift at inference time is a reasonable experimental validation gap but not a theoretical flaw. Demoted from major to minor (see Weakness #4).
- **"The paper does not discuss the error bound tightness" (from harsh critic's missing parts):** This is a nice-to-have rather than a genuine weakness. Every paper has unexplored extensions. Moved to Nice-to-Haves.
- **"Competitors also require neural network training" (counterpoint to the lightweight critique):** While true, the paper's claim of being "lightweight" is relative to methods requiring the embedding trick, not to all methods. The framing issue remains valid as stated.
- **"Missing related works":** The rule prohibits mentioning missing related works as a weakness.
- **"Formatting/style nitpicks":** Removed per parser artifact rules.

## Novel Insights

None beyond the paper's own contributions. The review process surfaced a useful synthesis: INFO-SEDD's core innovation is the recognition that the absorbing-state CTMC used in discrete diffusion models has a fortuitous side-effect—it makes the score ratios for any marginal subset directly computable from a single joint model (Equation 6). This property, combined with the Dynkin-formula-based KL estimator, transforms the standard discrete diffusion training pipeline into a general-purpose information estimator. The paper's main limitation is not in the method itself but in the gap between the theoretical coverage of this property (which is well-founded) and the empirical validation of its practical robustness under heavy masking.

## Suggestions

1. **Analyze the ρ=0 bias.** Decompose the positive intercept in the text consistency test by varying the diffusion horizon T. This would reveal whether the bias is dominated by truncation (and can be reduced with larger T) or by score-model approximation error.
2. **Provide a computational cost table.** Add a comparison of training time (GPU hours or wall-clock) for INFO-SEDD vs. each baseline on the synthetic benchmark. This directly addresses the "lightweight" framing concern and helps practitioners assess the accuracy–cost trade-off.
3. **Validate the sliding-window approach.** Either (a) train INFO-SEDD on a specific windowed dataset and compare to the sliding-window estimate from the full-sequence model, or (b) run a synthetic experiment with known subset structure to demonstrate unbiasedness under masking. This would elevate the motif discovery from a qualitative observation to a validated result.
4. **Report variance for real-world experiments.** Run the text and genomics experiments over multiple seeds and report standard deviations.
5. **Clarify the genomics reference construction.** Explicitly state the Bayes-optimality assumption underlying the classifier-based reference, and discuss whether the CADUCEUS classifier is plausibly near-optimal for this task.

## Score and Decision

### Calibration

**Round 1 (bracketing):**
- Weak band (< 3.5): Retrieved 4 anchors (all scored 3.00). Topics include "Deficit of New Information in Diffusion Models," "DFITE," "No MCMC Teaching," "DynamicsDiffusion." These are clearly weaker papers (rejected, with evident flaws). INFO-SEDD is far above this band.
- Middle band (3.5–7.5): Retrieved 4 anchors. Key comparable papers: **MINDE** (6.50, Accept) — the closest relative, a diffusion-based MI estimator for continuous data by the same research group. **Convergence of Score-Based Discrete Diffusion Models** (7.00, Accept) — pure theory, no experiments. **Scalable Discrete Diffusion Samplers** (6.00, Accept). **Probing Latent Hierarchical Structure** (6.50, Accept). INFO-SEDD sits solidly in this band, outperforming the closest methodological relative (MINDE) in experimental breadth and addressing the harder discrete-data setting.
- Strong band (> 7.5): Retrieved 4 anchors (all scored 8.00). Topics include permutation learning, progressive compression, time-lagged IB, and influence functions. These papers have either broader impact or more polished execution. INFO-SEDD is not at this level due to the validation gaps identified above.

**Round 2 (narrowing, 5.5–7.5):**
- Retrieved **MINDE** (6.50) as the strongest comparator. Comparing directly: INFO-SEDD presents a cleaner theoretical derivation, stronger synthetic experiments (7 baselines vs. MINDE's 5, with clearer margins), real-world applications (MINDE has synthetic-only + MNIST consistency), and an explicit error bound. However, INFO-SEDD shares some of MINDE's weaknesses (no computational cost analysis, some validation gaps). INFO-SEDD is a clear advance over MINDE in scope and evidence.
- Retrieved **f-DIME / Data Derangement** (5.60, Reject) — a variational MI estimator that is clearly weaker than INFO-SEDD.
- Retrieved **Convergence of Score-Based Discrete Diffusion** (7.00) — a different type of contribution (pure theory).
- Retrieved **Bayesian Experimental Design via Contrastive Diffusions** (7.33) — a diffusion-for-information paper of similar quality but different topic.

**Final score determination:** INFO-SEDD is better than MINDE (6.5) in experimental rigor and scope but has similar unresolved issues (computational cost, some validation gaps). It is not as polished or thoroughly validated as the 8.00 anchors. The paper's core theoretical advance is sound, the synthetic experiments are convincing, and the real-world applications demonstrate genuine utility. The identified weaknesses are addressable and do not threaten the central claim. Score: **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>