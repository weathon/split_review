Now I have sufficient calibration. Let me write the consolidated review.

**Round 1 bracket:** Based on the calibration search, papers in the neural/differentiable feature selection space score between 2.0 and 5.0. The relevant band for this paper is approximately 3.0–5.0.

**Round 2 narrowing:** Within that band, the closest anchors are EntryPrune (3.0, same research area but less clean method), EffSelect (5.0, stronger empirical evaluation), and the GNN feature selection paper (4.0). AutoNFS sits between EntryPrune and EffSelect: cleaner than EntryPrune but with similar novelty concerns and evaluation gaps that prevent it from reaching the EffSelect level (5.0).

**Score: 4.0**

---

## Summary

AutoNFS proposes a fully differentiable neural feature selection method that uses Gumbel-Sigmoid gates with a cardinality penalty to automatically determine both which features to select and how many to retain. The architecture consists of a masking network that generates a soft mask from a learned embedding, applied to the input of a task network, all trained end-to-end. The method is evaluated on the Cherepanova et al. (2023) benchmark with three corruption scenarios across 11 OpenML datasets, plus 24 real-world metagenomic datasets.

## Strengths

- **Automatic feature count determination is a clean practical advantage.** The loss function (Eq. 2–3) includes a cardinality penalty term λ·ℒ_select that lets the model learn how many features to keep without manual tuning of a budget parameter. Table 1 confirms AutoNFS selects datasets-specific counts (e.g., 65 of 128 for AL, 5 of 8 for CH), while baselines require a pre-specified k. Algorithm 1 makes the end-to-end training procedure explicit and easy to implement.

- **Zero misselection errors on two of three corruption scenarios.** Figure 3a shows AutoNFS achieves a 0.0 fraction of wrongly selected features for both Random and Corrupted scenarios, and only 0.17 for Second-order features (where auxiliary features may carry information since they are multiplicative combinations of originals). This is better than all compared methods and directly demonstrates that the learned mask correctly identifies the relevant original attributes.

- **Strong performance on real-world metagenomic data.** Table 2 shows AutoNFS reduces features from 535 to 41 on average (7.7% of original dimension) while slightly improving MLP accuracy (0.588 → 0.596) and RF accuracy (0.685 → 0.697) across 24 datasets. Individual gains on some datasets are substantial (e.g., GuptaA_2019: MLP 0.812 → 0.938). This demonstrates the method transfers beyond synthetic benchmarks to challenging biological data.

- **Clear, well-structured exposition.** The method description (Section 3), including the architecture diagram, the Gumbel-Sigmoid formulation, the temperature annealing schedule, and Algorithm 1, is clearly presented and easy to follow. The paper is generally well-organized.

## Weaknesses

### Major

- **The claim of "nearly constant computational overhead" is insufficiently supported and physically implausible as stated.** The paper claims near-constant runtime across D from 10² to 10⁵ (Figure 4a, α ≈ 0.08), but the masking network f: ℝ^{D_e} → ℝ^D must have an output layer with D units, and the task network g takes a D-dimensional masked input. Both involve computation that scales with D (at minimum O(D) per batch for the mask generation, and O(D·h) for the task network's first layer). The paper does not specify what is being timed, what architectures were used, what data were generated for the scaling experiment (synthetic? real?), or any training hyperparameters (epochs, batch size). Without this information the reader cannot verify the central efficiency claim. If the measurement includes only the masking network forward pass after training rather than the full training pipeline, it is misleading. *Note: the experimental setup detail likely resides in the stripped appendix, but the main text must stand on its own for a claim of this centrality.*

- **Missing comparison against the most closely related neural FS methods (STG, Hard-Concrete).** The paper cites Stochastic Gates (Yamada et al., 2020b) and Hard-Concrete (Louizos et al., 2017) in the related work but does not include them in the empirical comparison. These methods also use continuous relaxation with sparsity penalties to automatically determine the feature count. Without showing that AutoNFS outperforms these direct competitors, the empirical contributions are incomplete. The paper includes 10 baselines but omits the most relevant neural ones.

- **The evaluation asymmetry is acknowledged but not addressed.** The paper notes (page 6) that "all baseline methods select the same number of features as were in the initial representation (before corruption), whereas our method automatically chooses a much smaller subset." This asymmetry means that baselines are forced to include features that may be irrelevant or noisy, while AutoNFS can drop them. The comparison therefore conflates the advantage of automatic budget selection with the quality of the selection mechanism itself. The paper would be substantially strengthened by either (a) comparing methods at equal budget or (b) letting baselines also use automatic budget selection (STG and Hard-Concrete already support this). As it stands, the headline performance gap (Figure 2) cannot be attributed solely to better feature selection—it partly reflects the asymmetric experimental setup.

### Minor

- **Fixed λ = 1 across all datasets without sensitivity analysis.** The paper uses a single λ value for the sparsity penalty across all 11 OpenML datasets and all metagenomic datasets. The trade-off between sparsity and accuracy is critical to the method's usefulness, yet no ablation or sensitivity analysis of λ is presented in the main text (the paper defers this to Appendix F, which is stripped). A user needs guidance on how to set this hyperparameter.

- **No error bars or statistical significance on benchmark results.** Figures 2 and 3 report average ranks and feature metrics without any variance estimates or significance tests. While rank-based aggregation across datasets partially mitigates this, individual numbers in Tables 3–5 (appendix) ideally need error bars over multiple runs to assess result stability.

- **The masking network architecture is underspecified.** The paper defines f: ℝ^{D_e} → ℝ^D but does not describe its architecture (number of layers, hidden sizes, activations). This makes it impossible to assess the computational cost of the mask generation or to reproduce the method without guessing architectural details.

### Trivial

- Figure 4 caption refers to "GFSNetwork" rather than AutoNFS, a naming inconsistency from a previous iteration.

## Nice-to-Haves

- An ablation comparing the masking network f (learned embedding → mask) against a simpler per-feature logit baseline (direct w ∈ ℝ^D, no f) would clarify whether the network architecture provides meaningful benefits or is unnecessary complexity.

- A Pareto-style plot of accuracy vs. feature count (varying λ) would give a more complete picture of the sparsity-accuracy trade-off and help users calibrate expectations.

## Removed Points

These points are flagged to be removed; treat them with caution if reading the raw reviews.

1. Harsh critic's claim that the evaluation is "fundamentally biased" and that results are "artifacts of a rigged comparison" — **Removed.** The paper explicitly acknowledges the asymmetry. The comparison demonstrates AutoNFS's core advantage (automatic budget selection) versus fixed-budget methods. This is a feature, not a bug. A more careful analysis of this asymmetry belongs in the Minor weaknesses.

2. Harsh critic's claim that the constant-time claim is "physically improbable" and "cannot be accepted" — **Downgraded from Fatal to Major.** The claim is genuinely insufficiently supported in the main text, but it is not physically impossible (the masking network could be lightweight, and the timing methodology could be valid). The core issue is missing experimental details, not an inherent contradiction.

3. "Limited novelty relative to existing differentiable FS methods" — **Downgraded from a weakness to context.** The paper does not claim radical architectural novelty; its contribution is the combination of automatic budget selection + efficiency, evaluated on benchmarks. The omission of STG/Hard-Concrete from the comparison is the concrete problem, not the novelty claim itself.

4. Strength Finder's claim about "near-constant computational overhead" being a key strength — **Downgraded.** This claim is unverifiable from the main text. While it may be correct, the lack of supporting methodology prevents it from being a strength of the paper as presented.

5. Harsh critic's complaints about missing appendix content, hyperparameters not listed in main text, and reproducibility details — **Removed per instructions** (parser strips appendix sections from all papers).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Provide a detailed description of the computational complexity experiment methodology (architectures, data generation, hardware, what is being timed) directly in the main text. At minimum, state the architecture of f and g, and clarify whether the timing includes the full training loop or only the masking network forward pass.

2. Add STG, Hard-Concrete, and ideally Concrete Autoencoders to the baseline comparison. These are the most directly related methods and their inclusion is essential for positioning the work.

3. Either compare at equal budget (fix k for all methods including AutoNFS) or show a Pareto curve of accuracy vs. feature count across λ values. This would separate the quality of selection from the advantage of automatic budgeting.

4. Report variance over multiple random seeds for the main results, even if only for a subset of datasets/methods.

5. Show an ablation of λ (e.g., 5–7 values) on 2–3 representative datasets, with plots of accuracy vs. selected feature count, so users understand the trade-off.

## Score and Decision

### Calibration Anchors

**Round 1 (bracketing):**
| Anchor ID | Avg Score | Round | Comparison to Paper |
|-----------|-----------|-------|-------------------|
| eChWBrh9mc (EntryPrune) | 3.0 | R1 bracketing (low) | Similar area; AutoNFS has cleaner method but similar novelty concerns; slightly stronger |
| B6HnApgkP3 | 2.0 | R1 bracketing (low) | Notably weaker: post-hoc FSL with very limited evaluation |
| 1Rtcuzc7rN | 2.0 | R1 bracketing (low) | KAN-based FS; weaker evaluation and less convincing results |
| tm3K2omGNx | 1.5 | R1 bracketing (low) | Different problem (privacy), not comparable |
| oLl4zjx6rz | 4.0 | R1 bracketing (mid) | Adaptive GNN feature selection; comparable quality, different domain |
| ZxYkPHacJT | 4.0 | R1 bracketing (mid) | Unrelated topic (normalized spaces), not comparable |
| UYFanpQgqN | 4.0 | R1 bracketing (mid) | Multi-label feature selection; comparable quality |
| j8heF05dan (EffSelect) | 5.0 | R1 bracketing (mid) | Stronger evaluation and clearer contribution; paper under review is slightly weaker |
| kkBOIsrCXh | 8.0 | R1 bracketing (high) | Unrelated (embodied navigation); not comparable |
| nCsF3Bsn2n | 8.0 | R1 bracketing (high) | Unrelated (kernel methods); not comparable |
| DM0Y0oL33T | 8.0 | R1 bracketing (high) | Unrelated (multimodal reasoning); not comparable |
| VaS6xcDrTb | 8.5 | R1 bracketing (high) | Unrelated (rotation estimation); not comparable |

**Round 2 (narrowing within 3.5–5.5):**
| Anchor ID | Avg Score | Round | Comparison to Paper |
|-----------|-----------|-------|-------------------|
| oiZhPliETH (REFeat) | 4.0 | R2 narrowing | LLM-based feature discovery; comparable overall quality |
| UYFanpQgqN | 4.0 | R2 narrowing | Same as R1; comparable quality |
| oLl4zjx6rz | 4.0 | R2 narrowing | Same as R1; comparable quality |
| j8heF05dan (EffSelect) | 5.0 | R2 narrowing | Stronger evaluation, clearer empirical wins; paper under review is slightly weaker |

**Round 1 bracket:** 3.0–5.0  
**Round 2 narrowing:** The paper lands between EntryPrune (3.0) and EffSelect (5.0), closer to 4.0. It is cleaner than EntryPrune but has similar novelty constraints and evaluation gaps that prevent it from reaching the EffSelect level.

### Evaluation Summary

**Originality:** Moderate. Gumbel-Sigmoid + cardinality penalty is a straightforward combination of existing techniques (Hard-Concrete, STG, Gumbel-Softmax). The masking network architecture is a minor architectural variant.

**Importance of research question:** High. Automatic feature selection with minimal human intervention is practically valuable for high-dimensional tabular data.

**Claims support:** Mixed. The automatic feature count discovery claim is well-supported. The superior predictive performance claim is weakened by the asymmetric evaluation (baselines forced to a fixed budget). The near-constant computational overhead claim is insufficiently supported.

**Soundness of experiments:** Moderate. The benchmark evaluation is reasonable but missing key baselines (STG, Hard-Concrete) and error bars. The metagenomic evaluation is a genuine strength.

**Clarity of writing:** Good. The paper is well-organized and clearly written.

**Value to community:** Moderate. The method is simple and could be useful, but the evaluation gaps limit the paper's conclusiveness.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>