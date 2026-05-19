Now I have all the information needed. Let me synthesize the final review.

## Summary

This paper proposes RaE (Replay across Experiments), a simple method for reusing prior experimental data in off-policy RL by mixing it with online data at a fixed ratio (50/50 in the main results). The method requires no algorithmic modifications to the base RL agent — only a second replay mechanism. The paper evaluates RaE across locomotion (DMPO), manipulation (SAC-Q), and RL Unplugged (CRR) benchmarks, comparing against fine-tuning, AWAC, and random weight resetting. The main empirical finding is that this simple mixing strategy matches or outperforms more complex approaches across diverse domains.

## Strengths

1. **Minimal, practical modification to existing RL workflows.** The method requires only a second replay mechanism that mixes prior and online data at a fixed ratio (Section 2.2). It is algorithm-agnostic and integrates with DMPO, D4PG, SAC-Q, and CRR without modifying the agent itself. This simplicity is a genuine advantage over prior work that introduces additional losses, multi-stage procedures, or domain-specific tuning.

2. **Broad empirical validation across multiple algorithms and challenging domains.** RaE is evaluated on locomotion (including an egocentric vision variant), manipulation stacking, and three RL Unplugged control tasks, using four different base algorithms. The vision-based soccer task (Locomotion Soccer Vision) is a notably challenging setting where RaE shows the clearest gains (Figure 2).

3. **Well-designed ablation study providing practical insights.** Table 1 systematically examines data type (high/mixed/low return), dataset size (1e4 vs 1e5 episodes), and mixing ratio (50–90% online) — all relative to the online-from-scratch baseline. Useful patterns emerge: low-return data is most beneficial in small-data regimes; expert-only data is the least beneficial; a 70–80% online mix works best across settings. This is more thorough than typical evaluations.

4. **Demonstrated robustness across seeds and iterative application.** Figure 4c shows that RaE works robustly even when reloading data from a mix of high- and low-performing seeds. Figure 4a shows that the method can be applied iteratively with diminishing but real returns.

## Weaknesses

### Fatal

None.

### Major

- **Online-from-scratch baseline absent from the main results figure (Figure 2).** The paper's central claim is that RaE *improves* controller performance. However, Figure 2 only compares RaE against other methods that also reuse prior data (fine-tuning, AWAC, random reset). The standard online-from-scratch baseline — i.e., running the base algorithm without any prior data — is the most important comparison for validating this claim. The ablation table (Table 1) does provide this comparison for one domain (Locomotion Soccer State), where it shows RaE exceeding 100% in most configurations. But this crucial reference point is not included in the main results figure, making it impossible for a reader of the main results to directly assess the absolute improvement from RaE without cross-referencing the ablations. This is a significant presentation gap that weakens the paper's central evidence.

- **Overclaimed robustness to hyperparameters.** The paper states that RaE "has very low sensitivity to hyperparameter choices across a range of diverse domains" and uses a single 50% mix for all main results (Section 3.2, final paragraph). However, Table 1 shows that with small datasets (1e4 episodes, ~2.5% of the full dataset) and high-return data, the 50% mix yields only **51%** of online-from-scratch performance, while 90% online yields 108% — a factor-of-2 swing driven purely by the mixing ratio. The paper does acknowledge "extreme settings" in the same sentence, but "low sensitivity" is an imprecise characterization when switching the ratio alone changes outcomes from catastrophic failure to substantial improvement in a practically relevant regime (small datasets). The claim should be scoped to the large-data, mixed-return setting where the single-fixed-ratio strategy actually works.

### Minor

- **Implementation detail ambiguity for the 50/50 mix.** The paper specifies "the availability of a second replay mechanism that allows replaying prior and online data with a particular fixed ratio" (Section 2.2) but does not describe how this ratio is enforced during training. Key design choices are unspecified: Are separate buffers maintained and sampled independently? Is the ratio maintained per minibatch or per epoch? How is the ratio kept constant as online data accumulates? While experienced practitioners can infer a plausible implementation, the lack of precision undermines reproducibility for a method whose primary selling point is simplicity.

- **Asymmetric hyperparameter tuning complicates interpretation of comparisons.** Baselines (AWAC, fine-tuning, random reset) were swept over multiple hyperparameters and the best per-domain variant is reported (Section 3.2). RaE uses a single fixed 50% mix with no tuning. The paper frames this asymmetry favorably (it shows RaE's simplicity), which is fair. However, the reader cannot rule out that tuning RaE's mixing ratio per domain would widen the gap, nor that the baselines' advantage from per-domain tuning is already factored into the comparison. A brief acknowledgment of this asymmetry's directional effect on conclusions would strengthen the presentation.

- **The "state-of-the-art" claim in the contributions list (Section 1, bullet 1) is imprecise.** The paper compares against three baselines (fine-tuning, AWAC, random reset). While these are relevant, "SOTA" implies broader comparison (e.g., against more recent offline-to-online methods, REST, or other replay-mixing techniques). The empirical results are competitive but the SOTA framing over-promises relative to the evidence provided.

- **No error bars or variance information in the ablation table (Table 1).** The cells report percentages relative to the online-from-scratch baseline without standard errors across seeds. Some entries at 101% (colored blue, "above 100%") may be within noise of the baseline. The paper shows 5-seed results with CIs in the main figures, so this is an inconsistency in presentation standards.

- **The RL Unplugged data uses single-step trajectories while other domains use episode-level storage.** The paper notes this difference (Section 3.1) but does not discuss whether the 50% mixing ratio has a different operational meaning when data granularity differs (each "step" vs. each "episode" counting toward the ratio). This affects cross-domain comparability of the mixing strategy.

### Trivial

None.

## Nice-to-Haves

- A mechanistic analysis (e.g., critic loss, policy entropy, or state-distribution coverage during training with and without RaE) would strengthen the paper beyond simply adding more domains. The paper currently relies on ablation patterns and speculation ("the benefit of having a larger state distribution with mixed rewards") without direct evidence for the mechanism.
- Code release would greatly amplify the impact of a method whose core selling point is simplicity.
- An explicit discussion of when multiple iterative applications of RaE are worth the additional compute (Figure 4a shows plateau on the third iteration, but no compute-efficiency analysis).

## Removed Points

These points were raised by reviewers but removed or demoted under the filtering rules:

- **"Missing code release" mentioned as a weakness in the harsh critic** — This is treated as a nice-to-have, not a weakness. Code release is standard practice post-acceptance and not required during review.
- **"Related work conflates expert demos and offline datasets"** — The paper actually organizes related work to discuss both families, and the distinction is clearly stated. This is a stylistic choice, not a weakness.
- **"The SOTA claim not well-supported" in the original critic's section-by-section notes** — Merged into the Minor weakness above rather than treated separately.
- **Strength Finder point about "Practical applicability discussed in detail"** — This is generic and mostly restates the discussion section. Demoted.
- **"Confidence intervals wide, ranking not statistically clear"** — The paper does report 95% CIs averaged over 5 seeds (Figure 2). The critic's concern is valid but the community standard for empirical RL papers is learning curves with CI shading, not per-comparison significance tests. Demoted to an implicit limitation rather than a standalone weakness.
- **"Random weight resetting plus data reloading baseline"** — The critic suggests this would be a stronger baseline, but the existing random reset baseline is already revealing (it tests whether resets alone explain the gains). The suggested combined baseline isn't standard practice and the paper's decomposition is informative as is.

## Novel Insights

The key insight that emerges from collating the reviews — beyond the paper's own contributions — is that this paper would benefit from *adopting its own philosophy more thoroughly*. The method's strength is simplicity, but the paper's presentation adds complexity by spreading crucial comparisons across sections (online-from-scratch in ablations but not main results), making imprecise claims about robustness, and leaving implementation details to inference. The paper would be strongest if it aligned its presentation with its methodological message: clear, minimal, and self-contained.

## Suggestions

1. **Add the online-from-scratch baseline to the main results figure (Figure 2).** This is the single highest-impact change. It makes the paper self-contained and allows direct assessment of RaE's absolute improvement.
2. **Scope the robustness claim precisely** to the large-data, mixed-return regime. Replace "very low sensitivity" with a more accurate characterization: "sensitive in small-data or narrow-return regimes, but the 50% mix works robustly across diverse domains when data is plentiful and mixed-return."
3. **Specify the implementation of the mixing ratio** with a short sentence or pseudocode (e.g., "each minibatch samples B/2 transitions from the offline buffer and B/2 from the online buffer; the offline buffer is fixed while the online buffer grows").
4. **Add standard errors or confidence bounds to the ablation table** (Table 1) to match the statistical presentation in the main figures.
5. **Acknowledge the asymmetric tuning** explicitly: "Because RaE uses a fixed 50% ratio without per-domain tuning while baselines were optimized per domain, the comparison may underestimate RaE's peak performance and overestimate the baselines'."

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>