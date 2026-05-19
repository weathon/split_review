- Decision: Reject
- Avg Score: 5.33
- Scores: 8, 3, 5
Now I have a thorough understanding of the paper. Let me write the consolidated review.

---

## Summary

This paper empirically compares two reinitialization schemes for maintaining plasticity in neural networks: reinitializing weights (via a proposed algorithm called selective weight reinitialization, SWR) vs. reinitializing units (continual backpropagation, CBP). Through experiments on permuted MNIST and incremental CIFAR-100 with feed-forward networks, ResNet-18, and vision transformers, the paper identifies two settings where weight-level reinitialization is more effective: (1) when the network uses layer normalization, and (2) when the network has few units. The work provides useful practical guidance for practitioners dealing with plasticity loss.

## Strengths

- **Empirically identifies precise failure modes of unit-level reinitialization.** Table 1 directly quantifies the change in activation statistics (sample average and standard deviation) after reinitialization for both CBP and SWR under different settings. The finding that CBP changes the sample average of layer 1 activations by 0.32 vs. SWR's 0.06 in the small network setting provides concrete evidence for why unit reinitialization disrupts layer normalization statistics — a specific, actionable mechanistic explanation.

- **Systematic comparison across four controlled settings isolates the advantage of weight reinitialization.** Figure 2(a–d) shows that SWR maintains stable accuracy across all four settings (large/small networks, with/without layer normalization), while CBP fails in three of the four. The experimental design cleanly separates the effects of network size and normalization, allowing the paper to draw specific conclusions about each factor.

- **Validation on modern architectures (ResNet-18 and ViT) with a realistic class-incremental benchmark.** Figure 3 extends the findings beyond toy settings: in vision transformers (which use layer normalization), SWR maintains plasticity while CBP loses plasticity (without LN resetting). The ViT result confirms that the layer normalization finding from the feed-forward experiments transfers to a practically relevant architecture.

- **Ablates design choices for the proposed algorithm.** Figure 1 systematically compares four combinations of utility functions (magnitude vs. gradient) and reinitialization strategies (initial distribution vs. mean). Only gradient utility with initial-distribution reinitialization fully prevents plasticity loss, giving clear implementation guidance.

- **Measures actual reinitialization rates, not just task performance.** Section 4 reports the number of weights reinitialized per update (CBP: 8.35, SWR: 1 in the small network; CBP: 0.084, SWR: 0.687 in the small network with layer norm), ruling out the trivial explanation that SWR simply reinitializes fewer weights overall.

## Weaknesses

### Fatal
None.

### Major
- **Vision transformer comparison confounds reinitialization level with architectural scope.** In the ViT experiment (Section 5), SWR is applied to *all* weight matrices and bias vectors (including attention layers), while CBP is applied *only to feed-forward layers* (line 120–121). The paper acknowledges this asymmetry but does not address its impact on the comparison. Since the two methods operate on different subsets of the network's parameters, the finding that "only selective weight reinitialization maintains plasticity" in ViTs conflates the choice of reinitialization level (weight vs. unit) with the scope of layers being reinitialized. The paper partially addresses this by observing that CBP with LN resetting works without touching attention layers, suggesting attention layers aren't the bottleneck. However, a controlled comparison — either extending CBP to all layers or restricting SWR to the same feed-forward subset as CBP — would be needed to cleanly attribute the advantage to weight-level reinitialization. As it stands, this confound weakens the evidence for the paper's central claim in this architecture.

### Minor
- **The claim that weight and unit reinitialization are "equally effective" in large networks without layer normalization lacks statistical support.** The abstract (line 11) asserts that "reinitializing weights and units are equally effective at maintaining plasticity when the network is of sufficient size and does not include layer normalization." The evidence for this is Figure 2a, where the SWR and CBP curves visually overlap. However, no formal statistical test (confidence intervals on the difference, equivalence test, or paired comparison) is provided. Given that the paper makes a specific claim about *equality* (not just "both maintain plasticity"), statistical backing would strengthen it. The claim could be softened to "both maintain plasticity in this setting," which is well-supported by the data.

- **Hyperparameter values (τ, p) for each experiment are not reported.** The paper states that "a grid search" was used to tune hyper-parameters and acknowledges that "no single reinitialization strategy works best in all cases" (lines 86, 128), yet the selected values of the reinitialization frequency τ and proportion p are not listed in the main text or referenced to a specific table. This is a reproducibility gap — practitioners cannot implement the method without knowing the tuned configurations.

- **The ResNet-18 result where CBP outperforms SWR is acknowledged but not analyzed.** Figure 3a shows CBP achieving higher test accuracy than SWR over most tasks in ResNet-18. The paper notes this but does not investigate *why* — is the advantage due to batch normalization (which differs from layer normalization in how it handles reinitialization)? Is it the maturity threshold in CBP? The reader is left to speculate, and this result complicates the narrative that weight reinitialization is the more robust choice.

### Trivial
None.

## Nice-to-Haves

- A discussion of the computational overhead of computing the gradient utility (|w·g_w|) at reinitialization time. Gradients are already computed during training but may need to be stored or recomputed.
- A sensitivity analysis showing how performance varies with τ and p in each setting, which would help practitioners understand the robustness of the method.
- A brief discussion of how SWR relates to dynamic sparse training algorithms that also perform weight-level pruning and regrowth (e.g., SET, RigL), beyond the brief mention in the related work.

## Removed Points

These points from the reviewer inputs are flagged for removal with justification:

1. **"The utility functions are borrowed from pruning without argument for why they identify weights least useful for plasticity rather than for prediction"** — The paper's framing (lines 48–49) explicitly describes the motivation as restoring initial conditions that facilitate learning, and the empirical success of gradient utility validates the choice. This is a conceptual concern without evidence of a practical problem; the method demonstrably works.

2. **"The paper does not explain *why* SWR causes smaller changes in the small network setting (is it because fewer weights are changed per unit...?)"** — This is a speculative question the reviewer raises, not a verified weakness. The paper provides the reinitialization rate data (Section 4), which partially addresses this.

3. **"Missing comparison with other reinitialization methods (e.g., Regenerative Learning, Sokar et al. 2023)"** — The paper already cites Sokar et al. (2023) in the related work (line 23 and 28) and positions itself relative to existing work. The reviewer's claim that this is missing is incorrect.

4. **"The paper would benefit from a more nuanced discussion" of the ResNet-18 result** — Already captured as a Minor weakness; no need for duplication.

5. **"The Harsh Critic's Strengthening the Paper on Its Own Terms" sections on isolating the independent variable and characterizing failure modes** — These are suggestions, not verified weaknesses. The ViT scope confound is already captured in the Major weakness; the failure-mode characterization suggestion is a nice-to-have.

6. **Strength Finder's generic or superficial strengths** — The reviewer's mentions of "this paper addressed an important problem" and "targets an interesting question" are generic and removed. Only strengths with specific, verifiable grounding in the paper are retained.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Address the ViT confound.** Either extend CBP to all layers (including attention) or apply SWR only to the same feed-forward subset as CBP, then re-run the ViT experiment. If the confound cannot be resolved experimentally, clearly discuss how the asymmetry might affect the conclusions and temper the claim about SWR's superiority in ViTs accordingly.

2. **Add statistical support or soften the "equally effective" claim.** Provide confidence intervals, a paired comparison, or an equivalence test for the comparison in Figure 2a. Alternatively, rephrase to "both methods maintain plasticity in this setting," which is unambiguously supported.

3. **Report hyperparameter values.** Include a table (in the main paper or clearly referenced appendix) listing the tuned τ and p values for each architecture and algorithm configuration.

4. **Analyze the ResNet-18 result.** Add a brief discussion hypothesizing why CBP achieves higher accuracy than SWR in ResNet-18 — e.g., the interaction with batch normalization vs. layer normalization, or the effect of CBP's maturity threshold.

---
