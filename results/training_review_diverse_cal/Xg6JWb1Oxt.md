Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper tackles Imitation learning from Observations (IfO), aiming to move beyond idealized bimodal data mixtures toward more realistic settings where background data contains policies of varying quality. It contributes (1) SIBench, a new offline benchmark where background data is generated from policies trained with varying numbers of demonstrations (rather than the standard expert-random mixture), (2) VfO, a simple algorithm with two variants (binary-reward VfO-bin and discriminator-based VfO-disc) that adapts offline RL value functions to the action-free observation setting, and (3) a self-improvement loop showing that VfO can bootstrap from low-quality data to near-oracle performance. The key insight is that existing IfO methods (SMODICE, DILO) succeed primarily as trajectory filters on bimodal data, while value-function-based approaches like VfO are more robust to the overlapping state distributions that arise in self-improvement scenarios.

## Strengths

1. **VfO achieves performance close to the ground-truth-reward oracle across multiple environments on SIBench.** In Figures 2 and 3 (Sections 4.3), VfO-bin and VfO-disc obtain returns near AWR (which uses true rewards) on Ant, HalfCheetah, and Walker2D, and VfO-bin matches or exceeds AWR on Robomimic tasks. SMODICE and DILO rarely improve over the background data, making this a genuine empirical finding.

2. **The SIBench benchmark is validated as predictive of online self-improvement.** Section 4.6 (Figures 6, 7) directly demonstrates that offline SIBench improvement trends predict the behavior of iterative self-improvement: wherever VfO-bin shows positive improvement on SIBench, the online self-collection loop leads to consistent improvement in policy returns. This validation of the proxy benchmark is a concrete methodological contribution.

3. **VfO enables bootstrapping from near-random data to near-oracle performance via self-improvement.** In Section 4.6, VfO-bin iteratively improves from low-quality initial data to match the AWR oracle across Ant, HalfCheetah, and Walker2D. This is a non-trivial result — the paper correctly notes that bootstrapping imitation learning from self-collected data starting near random is an open problem (Sun et al., 2017), and SMODICE fails in the same setting.

4. **Simple and reproducible algorithmic design for the primary variant.** The VfO-bin algorithm (binary rewards + advantage-weighted regression on the background dataset) is presented clearly in closed form in Algorithm 1, with explicit loss functions, making it easy to implement and extend.

5. **Comprehensive evaluation across domains and data configurations.** The paper evaluates on D4RL MuJoCo tasks (continuous control), Robomimic tasks (manipulation), and vision-based Robomimic, comparing two VfO variants against BC, BCO, SMODICE, DILO, and an oracle AWR. It further tests two distinct data configurations (SIBench and bimodal), revealing systematic differences in method behavior.

## Weaknesses

### Fatal
None.

### Major

1. **Discriminator training procedure for VfO-disc is underspecified.** The paper introduces VfO-disc as a core variant (appearing in Figures 2, 3, 4), stating it "use[s] a learned discriminator that performs a soft expert / background assignment of each state – thus adapting ORIL (Zolna et al., 2020) to our setting." However, the loss function, training data mixture, architecture, training schedule (joint with the value function or pretrained?), and update frequency are not provided. While ORIL provides a template, the adaptation to the state-only, offline-with-mixture-data setting raises non-trivial design choices. This gap does *not* invalidate the paper's core claims — which primarily rely on VfO-bin (fully specified) in the self-improvement experiments — but it does make a non-trivial portion of the experimental results (the SIBench and bimodal D4RL comparisons involving VfO-disc) harder to verify and build upon.

### Minor

2. **Baseline hyperparameter documentation is insufficient.** The paper compares against SMODICE and DILO without describing whether their hyperparameters were tuned on SIBench tasks or taken as defaults from prior work. This matters because both methods have sensitive hyperparameters (regularization coefficients, dual variable constraints) that could affect their SIBench performance. The concern is partially mitigated by the fact that the same implementations *do* work well on bimodal data (Figure 4), showing the implementations are correct and the SIBench underperformance is likely genuine rather than a tuning artifact. Nevertheless, a statement of tuning procedure — even "default hyperparameters from the original paper" — should be included.

3. **Self-improvement experiments lack error bars or multiple-seed statistics.** Figures 6 and 7 show single traces for each algorithm. While the evaluation averages over 1,000 episodes per iteration (giving reliable per-iteration estimates), the variability *across* independent runs of the self-improvement process is not characterized. The saw-tooth pattern and convergence behavior could be influenced by stochasticity in data collection and policy training. Multiple seeds would strengthen confidence in the claimed improvement trajectories.

4. **No ablation of mixture parameter α.** Algorithm 1 introduces a mixture parameter α controlling the relative sampling of expert vs. background data in the value function loss. Its value is not discussed, and no sensitivity analysis is provided. For a method that positions reproducibility as a strength, even a single-task ablation documenting the effect of α would be helpful.

### Trivial

None.

## Nice-to-Haves

- **Analysis of why VfO-bin matches AWR oracle in self-improvement.** The paper notes that VfO-bin (using only binary rewards from observations) matches AWR (using dense ground-truth rewards) in the self-improvement loop, calling it "highly non trivial." This striking result would benefit from diagnostic analysis: e.g., measuring the learned value function's correlation with true returns, or ablating reward granularity. Understanding *when* binary observation-based rewards suffice would strengthen the insight.

- **Analysis of the Walker2D hypothesis.** The paper attributes VfO-bin's underperformance on Walker2D to "lack of immediate reward on the background data which could impact its performance on cyclic tasks." This plausible hypothesis is not tested (e.g., by varying reward assignment or analyzing state visitation). A small diagnostic would turn speculation into evidence.

## Removed Points

The following points raised by reviewers were removed after verification against the paper:

- **"Large-scale" claim unsupported:** The paper's title is "*Towards* Large-Scale Imitation Learning via Self-Improvement" and the abstract says "moving closer to a paradigm" and "on a path to scalable behaviour learning." These are appropriately directional claims. The paper does not claim to have achieved large-scale learning; the "Towards" qualifier makes this explicit. The experiments are on standard benchmarks, consistent with the stated scope.

- **Parser artifact at "2022)" in related work:** The text "model-based approaches (Chang et al., 2021)" followed by "2022)" is a clear parser strippage artifact, not an author error.

- **Reproducibility concern about SMODICE/DILO implementations not existing / being unavailable:** The paper cites published methods with available code; the concern that "the reader cannot determine whether the results reflect genuine limitations or suboptimal configuration" is mitigated by the methods' correct behavior on bimodal data.

- **Missing appendix/implementation details for baselines:** A footnote (superscript 3 after the DILO citation) was likely stripped by the parser alongside other ancillary sections. Implementation provenance details that existed in the original submission are not author omissions.

## Novel Insights

The most interesting emergent observation across the reviews — beyond the paper's own claims — is the *inversion of relative performance* between VfO and prior methods (SMODICE/DILO) depending on data distribution. On bimodal data (distinct expert/background clusters), SMODICE/DILO excel while VfO struggles. On SIBench (overlapping distributions from policies of varying quality), the roles reverse completely. This suggests the IfO community's problem is not just algorithm design but *benchmark design*: the benchmark determines which approaches look strong, and the field may have been optimizing for a proxy (trajectory filtering on separable distributions) that does not align with the intended application (self-improvement on realistic, overlapping data). This finding — that the benchmark itself selects the "winner" — is more important than any individual algorithmic contribution and deserves emphasis.

## Suggestions

1. Add discriminator training details for VfO-disc (loss function, architecture, data mixture, training schedule) to the main text or appendix.
2. Include a statement of how SMODICE/DILO hyperparameters were configured for SIBench (even if simply "default parameters from the original implementation").
3. Run at least one multi-seed version of the self-improvement experiments (e.g., 3 seeds on 1-2 environments) to characterize variability.
4. Add an ablation of the α mixture parameter on at least one task.
5. Consider adding a diagnostic experiment for why VfO-bin matches AWR in self-improvement — e.g., correlating learned values with true returns over iterations.

## Score and Decision

**Originality:** Good. The SIBench benchmark addresses a genuine limitation in existing IfO evaluation, and the observation about data distribution effects is valuable. The VfO algorithm itself combines known components (SQIL/ORIL rewards + AWR-style value function) in a straightforward adaptation, which is more of a solid engineering contribution than a methodological novelty.

**Importance:** High. The problem of learning from mixed-quality, action-free data with self-improvement is timely and relevant to scaling behavior learning. The finding that existing benchmarks reward trajectory filtering rather than genuine imitation learning is important for the field.

**Claims Support:** Mostly well-supported for VfO-bin and the core self-improvement claim. Weaker for VfO-disc due to missing training details. The SIBench-as-proxy claim is well-supported by the self-improvement experiments.

**Soundness:** Adequate. The experimental design is reasonable and covers multiple domains. The main gaps are documentation (discriminator, baseline tuning) and statistical rigor (single seeds for self-improvement).

**Clarity:** Good for the main ideas. The algorithm is clearly presented. Some details are missing (discriminator, baseline tuning).

**Value:** The benchmark contribution alone has value for the IfO community. The empirical finding about benchmark-dependent method rankings is a useful cautionary result.

The paper has real contributions (SIBench benchmark, VfO-bin as a strong baseline for overlapping data, validation of SIBench as a proxy for self-improvement) and the weaknesses are addressable rather than structural. The missing discriminator details are the most serious gap but do not threaten core claims since the primary results use VfO-bin. I recommend acceptance with minor revisions.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>