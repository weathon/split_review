## Summary

This paper proposes a framework for automated code refactoring that combines contrastive pre-trained code graph embeddings with reinforcement learning. The encoder learns structural-invariant representations via self-supervised augmentation (subtree masking, edge rewiring, identifier shuffling), and these embeddings are fused with traditional code quality metrics into a composite reward for a PPO-trained graph attention policy. The claimed contribution is replacing purely hand-crafted reward functions with learned refactoring-aware representations, demonstrated on three datasets against rule-based and RL baselines.

## Strengths

- **Sensible research direction.** Combining contrastive self-supervised learning with RL to reduce dependence on hand-crafted rewards is a well-motivated direction. The three-phase pipeline (contrastive pre-train → RL fine-tune → inference) is clear and modular.
- **Multi-dimensional ablation study.** Table 2 systematically removes the contrastive pre-training, embedding rewards, semantic tests, and the exploration strategy, giving concrete evidence that each component contributes. The largest drop (−7.5% SI) upon removing pre-training is a meaningful quantitative finding.
- **Cross-language transfer experiment.** Table 3 evaluates a Java-trained model on Python and C++ without fine-tuning and compares against language-specific linters, showing a plausible generalization result.
- **Figure 2 correlation analysis.** Reporting Pearson r = 0.72 between embedding dynamics Δh and syntactic improvement SI is a concrete attempt to validate the hypothesis that the learned representation tracks meaningful refactoring signals.

## Weaknesses

### Fatal

**Reward component Δh_t is theoretically unsound.** The composite reward in Eq. (5) includes `α·tanh(β·Δh_t)` where `Δh_t = ||h_t − h_{t-1}||_2` (positive contribution). This directly incentivizes large movements in the latent space regardless of quality, which is not equivalent to achieving good refactorings — it could equally be satisfied by noisy or semantically destructive transformations. The paper justifies this with a post-hoc correlation (r = 0.72) in Figure 2, but correlation does not establish that maximizing Δh leads to maximizing SI; the correlation may merely reflect that larger refactorings happen to achieve more improvement. The causal direction is never established, and the reward design is not theoretically grounded.

**Figure 3 is inconsistent with the described reward function.** The reward (Eq. 5) is defined with fixed scalar weights α, β, γ. Yet Figure 3 shows the proportion of code-quality metrics decreasing from ~80% to ~20% and embedding dynamics increasing from ~10% to ~70% across 100 refactoring stages. This dynamic shift is impossible under a fixed-weight reward unless something is scheduled or adapted, which is never described in Section 4.6 or the implementation details. This suggests either the figure is illustrative/fabricated, or a non-trivial dynamic weighting mechanism exists that is entirely absent from the methodology.

### Major

**GraphRL baseline is a survey, not a refactoring method.** The citation "Darvari et al., 2024" (Table 1, baseline "GraphRL") is a survey paper titled "Graph reinforcement learning for combinatorial optimization: A survey and unifying perspective." Using a broad survey as a baseline comparison for code refactoring provides no meaningful competitive signal. If the actual system behind it is not described or publicly available, this baseline is invalid.

**Augmentation "identifier shuffling" is semantics-breaking.** Section 4.1 lists "Identifier shuffling: Permuting variable names within scope constraints" as a *syntax-preserving* transformation for generating positive pairs in contrastive training. Renaming `x→y` and `y→x` within a scope produces functionally distinct code (it swaps the roles of variables), breaking semantic equivalence. This means positive pairs in contrastive training may actually be *semantically different*, undermining the claim that the encoder captures semantic invariance.

**Exploration strategy (Eq. 6) is underspecified.** The prototype h* is described as a "running average of high-reward states," but no threshold, window size, or initialization for h* is given, nor how Σ is estimated reliably in early training when few high-reward states have been seen. This makes the method non-reproducible.

**No statistical testing of results.** Table 1 shows the proposed method outperforming all baselines on all five metrics simultaneously. No standard deviations, confidence intervals, or significance tests are reported. Given the large variation in methodological quality among baselines, this uniformity is suspicious and cannot be accepted without uncertainty estimates.

### Minor

- The two references to Palit & Sharma (2024a and 2024b) in Sections 2.3 and Table 1 map to the same arXiv report (arXiv:2412.18035), creating a spurious duplication.
- Several cited works are from non-archival sources (academia.edu, researchgate.net), which makes verifying the comparisons difficult.
- The definition of δ_t in Eq. (5) is a binary indicator (`𝕀[test = test]`), while Eq. (8) defines a continuous Hamming distance version. These are inconsistent; only one can appear in the actual reward.
- The statement that CodeSearchNet pre-training was on Java is inconsistent with the dataset description: CodeSearchNet covers 6 programming languages, so the claimed transfer scenario is conflated.

### Trivial

- Minor OCR artifacts in the abstract ("do last year," "lemon deep learning") and section numbering (Section 4 appears inside Section 5 for baselines).

## Nice-to-Haves

- Replace or properly implement the Δh reward term; e.g., use cosine similarity between the current state and a target embedding of "well-refactored" code rather than raw magnitude of movement.
- Introduce dynamic reward reweighting explicitly and validate it (e.g., curriculum schedule), which would explain Figure 3 and add a principled justification.
- Include statistical significance tests (e.g., paired t-tests or bootstrapped confidence intervals) for the key tables.

## Novel Insights

The idea of using embedding-space dynamics as a reward signal is interesting in principle — if the learned latent space captures refactoring quality, then navigating toward certain regions could be informative. However, as implemented, the reward term measures *displacement* rather than *direction toward quality*, which collapses a good idea into a flawed proxy. A stronger version would anchor movement toward specific learned "quality centroids" rather than rewarding movement magnitude per se.

## Suggestions

- Replace the Δh term in the reward with a directed similarity to a cluster centroid representing high-quality refactored code: `sim(h_t, µ_good) − sim(h_{t-1}, µ_good)`, making movement directional and theoretically grounded.
- Fix the contrastive augmentation: identifier shuffling (variable swap) should be replaced with semantics-preserving renames (e.g., alpha-renaming all instances of one variable uniformly) or dead-code insertion.
- Either remove GraphRL as a baseline and replace it with the actual best prior RL refactoring system, or clearly describe which architecture within the survey was re-implemented and provide ablation details.
- Report per-dataset results separately for Refactory, CodeRef, and BigCloneBench rather than aggregating, so readers can assess whether gains are consistent.

## Score and Decision

The paper addresses a relevant and well-motivated problem, and some of its components (ablations, cross-language transfer) are handled reasonably. However, two fatal-level issues are present: the core reward component (Δh) is theoretically unsound and can lead the agent to reward semantically harmful actions; and Figure 3, a key result showing how reward components evolve, is mathematically inconsistent with the described fixed-weight reward function. Together with a misrepresented baseline (a survey used as a method), the absence of significance testing, and underspecified exploration, the experimental claims are not sufficiently supported. These are not merely presentational issues but strike at the validity of the main contributions.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>