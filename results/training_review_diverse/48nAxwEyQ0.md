Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper introduces FAVEN, an early-fusion architecture for audio-visual embodied navigation that uses learnable fusion tokens and multi-modal interaction blocks within a transformer backbone (extended with Mamba-based blocks). Unlike prior methods that process audio and visual streams separately and fuse at late stages, FAVEN concatenates learnable fusion tokens with modality-specific patches at the first layer and propagates them through the network, enabling cross-modal interactions throughout. Experiments on Replica and Matterport3D show improvements over prior methods (AV-Nav, AV-WaN, ORAN) in terms of SNA, SR, and SPL.

## Strengths

1. **Novel early-fusion architecture for embodied navigation.** The use of learnable fusion tokens that are concatenated with modality-specific patches and passed through the full network from the first layer is a genuine architectural contribution. This design is fundamentally different from prior audio-visual navigation methods that process modalities in separate streams and fuse only at the final decision stage (Section 3.2, Figure 3). The tokens aggregate modality-specific information via self-attention and then interact cross-modally in dedicated multi-modal blocks.

2. **Consistent performance improvements over prior methods on both benchmarks.** The tabular results (Tables 1 and 2) show that FAVEN outperforms AV-Nav, AV-WaN, and ORAN across all metrics (SNA, SR, SPL) on both heard and unheard sound conditions on both Replica and Matterport3D datasets. Gains like 9.3 SPL@Heard over ORAN on Replica and 11.3 SPL@Heard over AV-WaN on Matterport3D are substantive and consistent.

3. **Informative ablation study on fusion token count and fusion depth.** The analysis of how performance varies with the number of fusion tokens (peak at 3) and the number of early-fusion layers (peak at 9) in Tables 4a/4b provides practical design insights and validates that the architectural choices are not arbitrary.

## Weaknesses

### Fatal
None.

### Major

1. **Inconsistent performance claims between abstract and experimental results.** The abstract states FAVEN "reduces the search time by 93.6%," but Section 4.2 reports "up to an 88.8% decrease in search time on the Replica dataset" — a ~5% discrepancy, and the 93.6% figure is never justified anywhere else in the paper. More concerningly, the abstract claims SPL improvements of "10.4 and 6.5 on heard and unheard sounds," yet the paper's own per-dataset numbers are 9.3/3.6 (Replica vs ORAN), 11.3/14.8 (Matterport vs AV-WaN), and 9.9/4.9 (Matterport vs ORAN). None of these match 10.4 and 6.5. The source of the abstract numbers is untraceable. This is a factual inconsistency in the paper's central quantitative claims that undermines reader trust.

2. **No measures of variance reported.** The paper reports no standard deviations, confidence intervals, or number of trials for any metric. Audio-visual navigation on Matterport3D is known to have high variance across episodes. Without any indication of statistical spread, it is impossible to assess whether the reported gains are statistically significant or within the noise. This limits the reliability of the empirical contribution.

3. **Missing RL training details.** The paper states prior methods "primarily utilize reinforcement learning (RL) strategies" (Section 1) but never describes the RL algorithm, reward function, policy network architecture, or training procedure used for FAVEN itself. The implementation section (4.1) only mentions optimizer, learning rate, and epoch count. Without specifying whether the model is trained with RL, imitation learning, or something else, and how the baselines were retrained under a consistent protocol, the results cannot be reproduced or properly attributed to the architecture versus the training regimen.

4. **Real-world generalization claim rests on a single anecdotal trial.** Section 3.5 describes one scenario (one apartment, one sound source, one starting position) completed in 21 seconds. There is no baseline comparison under identical conditions, no statistical replication, no quantitative error metrics, and no supporting data for the claim that prior methods "failed to reach the sound source." This is insufficient to support the conclusion that FAVEN "demonstrates generalization to real-world settings" and should be presented as a qualitative proof-of-concept rather than evidence of generalization.

### Minor

5. **Limited baseline comparison.** The experimental comparison is restricted to four methods from the Chen et al. group (AV-Nav 2020, AV-WaN 2021, ORAN 2023) and Gan et al. (2020b). Given the current date (May 2026), the absence of any methods from other research groups or more recent approaches weakens the claim that FAVEN establishes a new "state-of-the-art." At minimum, the paper should acknowledge this limitation.

6. **Mamba extension is underspecified.** Section 3.4 describes the Mamba-based fusion blocks in only ~7 sentences with no equations, no architecture diagram, and no analysis of how the state-space model replaces attention in practice. The ablation study (Table 3) includes "Mamba" as a component label, but the text does not discuss a dedicated "without Mamba" ablation condition, making it impossible to assess its independent contribution.

7. **Method notation has inconsistencies.** The operator φ_f^{\bar{v}} appears in line 68 but φ_f^v in line 72. The role of {̂f_i^a} and {̂f_i^v} is stated to "not be used as newly updated context tokens" (line 68), yet the subsequent multi-modal block introduces new {̂f_i} via Eq. (6) without clarifying the relationship. These notational issues make an already dense method section harder to follow than necessary.

8. **Depth information fusion is unspecified.** Depth features are extracted via a CNN encoder "for later fusion" (Section 3.1), but where and how they are fused into the architecture is never described in the method or shown in Figure 2. The real-world experiment (Section 3.5) uses a different depth estimator (Depth Anything), introducing an uncontrolled variable.

### Trivial
None.

## Nice-to-Haves

- A dedicated ablation comparing the full model against a version without Mamba blocks to isolate Mamba's contribution.
- Wall-clock inference latency or FPS measurements to support the "fast" claim beyond environment-step counts.
- Clarification of where and how depth features are integrated into the fusion pipeline.

## Removed Points

These points were flagged during review but are removed as they do not reflect genuine weaknesses in the paper:

- **"Tables are unreadable images"** — This is a PDF-parsing artifact; the original submission has proper tables.
- **"Review process cannot verify numbers"** — Same parser artifact issue.
- **Detailed notation garbling complaints** (e.g., specific symbol rendering issues) — Many notational artifacts are parser-induced; the underlying notational inconsistencies (kept in Minor #7) are the genuine concern.
- **"Missing related works"** — As per instructions, I cannot confirm the existence of missing citations.
- **"The paper does not report batch size or compute hardware"** — These are implementation details that, while nice to have, do not compromise the paper's claims.
- **"Early fusion explored in other tasks, claim overstated"** — The paper specifically claims first demonstration for *embodied navigation*, not in general, which is a defensible scope.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Align the abstract with the experimental results.** The abstract numbers (93.6%, SPL 10.4/6.5) must be either removed or clearly traceable to specific dataset-baseline pairs reported in the paper. Presenting unverifiable numbers in the abstract is the single most fixable and most damaging issue.

2. **Add standard deviations or confidence intervals** for all main results, or at minimum report the number of evaluation episodes and describe the variance across runs.

3. **Describe the training procedure completely**, including whether RL is used, the RL algorithm and reward function, or clarify if a different training paradigm is employed.

4. **Downgrade the real-world claim.** Present Section 3.5 explicitly as a qualitative proof-of-concept demonstration, not as evidence of generalization. Add multiple trials or remove the generalization language.

5. **Either substantially expand the Mamba description** (equations, architecture, dedicated ablation) or remove it from the main contribution if it is not independently validated.

## Score and Decision

**Originality:** Good — early fusion via learnable tokens for embodied navigation is novel.  
**Importance of question:** Good — faster audio-visual navigation has practical relevance.  
**Claims support:** Weak — abstract numbers are inconsistent with experimental results, which undermines trust.  
**Soundness:** Weak — no variance reporting, no RL training details, single-trial real-world demo.  
**Clarity:** Needs improvement — notation inconsistencies, underdescribed Mamba component, unspecified depth fusion.  
**Value to community:** Moderate — the architectural idea is worthwhile but the evidence needs strengthening.

The paper has a genuine architectural contribution and shows consistent improvements over prior methods, but the factual inconsistencies in the abstract's quantitative claims (93.6% vs 88.8%, untraceable SPL numbers) are a major credibility problem that must be resolved. Combined with missing variance reporting, absent RL training details, and an anecdotal real-world evaluation, the paper in its current form does not meet the standard for acceptance. These issues are fixable, and a substantially revised version with consistent reporting and proper experimental rigor could be a strong contribution.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>