Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper introduces EReLELA, an architecture that uses emergent languages (ELs) from referential games to provide state abstractions for a simple intra-life count-based exploration method in reinforcement learning. The paper proposes that ELs — learned online and unsupervised alongside RL training — can substitute for natural language (NL) oracles, which are expensive to collect. It also introduces the Compactness Ambiguity Metric (CAM) to characterize the abstraction qualities of different languages. Experiments in MiniGrid environments (KeyCorridor-S3-R2, MultiRoom-N7-S4) show that EReLELA agents reach ~80% success rates, comparable to an agent using a synthetic NL oracle.

## Strengths

- **Novel connection between emergent communication and RL exploration**: The paper is the first to show that emergent languages from referential games can serve as state abstractions for count-based exploration in RL, opening a new research axis between Emergent Communication and Embodied AI.

- **EL abstractions achieve comparable success rates to synthetic NL abstractions**: Figure 2 shows EReLELA agents (e.g., Agnostic STGS-LazImpa-10-1) reach ~80% success in KeyCorridor-S3-R2, closely matching the SNLA agent that uses a synthetic NL oracle. This directly validates hypothesis H2.

- **The CAM metric provides a novel tool for analyzing language abstractions**: Section 3.2 introduces the Compactness Ambiguity Metric, which quantifies how different languages compress temporally-correlated observations. Figure 3 uses CAM to show that ELs' abstractions are closer to the shape-specific oracle in KeyCorridor (where shape is the critical feature for task success), providing evidence for meaningful abstraction learning (H3).

- **Investigation of linguistic structure (ZLA) effects on RL exploration**: The comparison between STGS-LazImpa (which induces Zipf's Law of Abbreviation) and Impatient-Only loss functions reveals that ZLA-abiding ELs yield better sample efficiency (Section 4.2, Figure 5 reference), offering insight into how NL-like structural properties improve downstream RL performance.

- **Online, unsupervised EL acquisition demonstrated**: The agnostic (non-shared-weight) EReLELA agents learn ELs in parallel with RL training without human annotation, demonstrating a practical pipeline where language abstractions emerge from interaction data alone.

## Weaknesses

### Fatal
None.

### Major

- **No comparison to standard exploration baselines (RND, NGU, or simple count-based)**: The paper claims to "put into perspective" complex exploration algorithms like RND and NGU (Section 4.1) and argues that count-based methods are simpler. Yet it never compares EReLELA against even a simple pixel-level count-based method, RND, or NGU using the same RL backbone. The only comparison is against (a) the SNLA oracle agent and (b) the RANDOM ablation (a random speaker with no RG training). The RANDOM ablation already achieves ~70% success, and EReLELA's improvement over it is modest (~80%). Without a comparison to standard exploration baselines, the central positioning claim — that language abstractions make count-based methods competitive with more complex approaches — is experimentally unsupported.

- **CAM distance metric is not specified for reproducibility**: The paper describes how to build CAM histograms from trajectories (Section 3.2, pseudocode) but never specifies how the *distance* between two CAM histograms is computed. Figure 3 reports "CAM distances" to SNL, color-specific, and shape-specific languages, and the Y-axis is labelled "CAM distance," but the underlying metric (histogram intersection? KL divergence? Earth mover's distance?) is never defined. This makes the central quantitative evidence for H3 irreproducible.

### Minor

- **Statistical evidence is thin**: All results use only 3 random seeds (line 121). For RL in procedurally-generated environments with stochastic policies, this is insufficient to draw reliable conclusions about statistical significance or sample efficiency. The paper asserts that "final performance are not statistically-significantly distinguishable" for agnostic agents (Section 4.1) but reports no actual statistical test. The error bars in Figure 2 are also not explained (standard deviation? standard error?).

- **"Cheap and readily-available" claim is not quantified**: The paper motivates ELs as addressing NL's expense (abstract, Section 1), but the comparison is only against a *synthetic* NL oracle (which is also cheap by construction). The RG training itself incurs cost: a speaker-listener pair trained every 32K steps on 8192 observations. No wall-clock time, sample cost, or computational overhead comparison is provided, so the claimed cost advantage over NL is asserted rather than demonstrated.

- **Shared-weight interference identified but not investigated**: The paper reports that shared encoder weights between RL and RG "interfere" and cause degraded performance (Section 4.1), and that the shared STGS-LazImpa-10-1 agent fails entirely (Section 4.2). This is a potentially important finding, but the paper offers no analysis of *why* (gradient conflict, representation collapse, etc.) or any mitigation strategy, leaving a significant methodological gap unaddressed.

- **Modest improvement over RANDOM ablation**: The RANDOM agent (randomly initialized speaker, no RG training) achieves ~70% success, while EReLELA reaches ~80%. The paper does not discuss whether this ~10% absolute improvement justifies the additional complexity of training RGs online. This is particularly relevant in 2D environments, where simple exploration methods are already known to work reasonably well.

### Trivial

- The CAM algorithm pseudocode (Section 3.2) references variables not explained in the main text (e.g., δ, partition hyperparameters λᵢ), and the final histogram construction is not shown clearly.

## Nice-to-Haves

- A sensitivity analysis on the reward mixing coefficients (λ_int=0.1, λ_ext=10.0) would strengthen confidence in the results.
- The paper could discuss why STGS-LazImpa-10-1 shared fails while the agnostic version succeeds, beyond the generic "interference" explanation.
- A wall-clock time comparison between EL acquisition (RG training) and the SNL oracle (which requires no training) would substantiate the "cheap" claim.

## Removed Points

These points were flagged in the reviewer inputs but are removed or weakened for the reasons given:

- **"Missing comparison to standard exploration baselines" framing as fatal**: Kept as Major (it is a real gap) but downgraded from fatal because the paper's core contribution (ELs as abstractions for exploration) is still partially validated by the SNLA comparison.
- **"CAM metric is circular" (harsh critic)**: Removed. The paper has a clear, falsifiable hypothesis (H3) about which oracle language ELs should align with in each environment, and tests it. Shape is a priori important in KeyCorridor, and the paper justifies this from the task structure. This is not circular.
- **"Formatting errors" and "missing Table 1"**: Removed per instructions — these are parser artifacts, not author errors.
- **"R2D2 choice not justified"**: Removed — the paper's contribution is about exploration, not the RL backbone. R2D2 is a standard choice.
- **"Completeness introduced without definition"**: Removed — the paper defines "complete" in the same sentence in Section 5, as part of a future-work discussion, not as a finding.
- **"MultiRoom results not in main paper"**: Removed — the paper references them, and page limits are a reasonable constraint.
- **"Error bars unlabeled — speculation about figure quality"**: The paper does not describe what the error bars represent. But the reviewer's speculation about what they might be is removed; the factual gap (no description) is folded into the Minor weakness about thin statistics.
- **Formatter nitpicks (typos, punctuation, garbled text)**: Removed per instructions — these are parser errors, not author errors.

## Novel Insights

The harsh critic observes something the strength finder misses: the RANDOM ablation's ~70% success rate tightly brackets the value added by RG training. The critic rightly points out that the ~10% gap between RANDOM and full EReLELA in this 2D setting is modest, and that the paper does not address whether this gap would persist or widen in 3D environments where count-based methods face harder challenges. This is an important point: the paper's contribution would be more convincingly established if the marginal benefit of RG-trained ELs over a random network were larger, or if the gap were shown to grow with environment complexity.

## Suggestions

1. **Add at least one standard exploration baseline** (e.g., episodic count over hashed pixels, or RND with the same R2D2 backbone) using the same experimental setup. This directly addresses the largest gap in the evidence.

2. **Explicitly state the distance metric used for CAM in Section 3.2** (e.g., "We compute the L1 distance between the normalized histograms"). This is essential for reproducibility.

3. **Increase seeds to at least 5–10 per condition** and report proper confidence intervals or a statistical test (e.g., Mann-Whitney U) to substantiate claims of statistical significance.

4. **Quantify the cost of RG training** relative to RL training (wall-clock time or sample efficiency impact) to support the "cheap and readily-available" claim.

5. **Analyze the shared-weight interference** by examining gradient alignment or representation similarity between RL and RG encoders — even a simple diagnostic would turn this limitation into insight.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>