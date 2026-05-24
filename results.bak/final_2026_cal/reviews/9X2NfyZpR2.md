Now I have a good calibration. Let me write the final review.

**Bracket:** After round 1, the narrowest plausible range is [5.0, 6.5]. The weak anchors (~3.0–3.33) are clearly below this paper (withdrawn/rejected papers with serious flaws), while the strong anchors (~8.0) are on very different topics. The most comparable anchor is the action anticipation paper at 5.50 (uKFVZMPppq). After reading it fully in round 2, I see this paper is stronger on contribution (first weakly-supervised LTA paradigm vs. a new attention mechanism), broader evaluation (3 datasets), and more thorough ablation. However, it has real limitations (confirmation bias concern, weaker 50Salads results, progressive training not ablated) that put it above 5.5 but not above ~6.5. Final score: **6.0**.

---

## Summary

This paper introduces TbLTA, the first framework for dense long-term action anticipation (LTA) trained exclusively from video transcripts — ordered action lists without timing or boundary annotations. The method uses temporal alignment (ATBA) to generate frame-level pseudo-labels, cross-modal attention to ground video features with transcript semantics, and a suite of losses (CTC, CRF, duration) to supervise both segmentation and anticipation without any frame-level ground truth. Experiments on Breakfast, 50Salads, and EGTEA show that deterministic TbLTA is competitive with fully-supervised methods on Breakfast and outperforms prior (semi-)weakly-supervised baselines, establishing the first transcript-only benchmark for dense LTA.

## Strengths

- **First weakly-supervised dense LTA using only transcripts.** The paper correctly identifies that all prior LTA methods require at least some frame-level annotations (Zhang et al. 2021 still uses weak labels with temporal extent for the observed segment). TbLTA removes this requirement entirely, opening a practical direction for reducing annotation cost. This is a genuinely novel contribution.

- **Strong empirical results on Breakfast with thorough ablation.** On Breakfast at 30% observation, deterministic TbLTA achieves 29.03 avg MoC vs 28.45 for the best supervised method (ActFusion), and at the 10% horizon it reaches 40.28 vs 35.79. The ablation study (Tables 3–4) systematically isolates the contribution of each component — CTC loss, cross-modal attention, CRF, and duration loss — with clear degradation patterns that validate the architectural choices.

- **Competitive rare-class performance on EGTEA.** TbLTA achieves 60.11 mAP on rare classes, outperforming supervised Timeception (59.70) and Anticipatr (55.10). This is a concrete and interesting finding that transcript-based supervision may help mitigate data imbalance.

- **Well-motivated and modular architecture.** The cross-modal attention with local masking (Eq. 1–2) and gated residual fusion is cleanly designed, and the use of CTC to provide a transcript-consistency signal that is independent of the pseudo-label alignment is sensible.

## Weaknesses

### Major

- **Confirmation bias from pseudo-label supervision.** The ATBA module produces frame-level pseudo-labels from the transcript, and these same pseudo-labels supervise both the TAS head and the LTA decoder. If the alignment is systematically wrong (e.g., misordering actions in the future portion), the anticipation decoder will learn to reproduce those errors. The paper mentions CTC as an independent signal (it marginalizes over alignments), but the frame-level supervision for the LTA decoder still comes directly from the alignment pseudo-labels. The paper does not include an ablation that separates alignment quality from decoder capability (e.g., by comparing a frozen vs. end-to-end alignment). This reduces confidence that the decoder is learning genuine anticipation skills rather than reproducing alignment errors.

- **Larger performance gap on 50Salads is not adequately analyzed.** On 50Salads, deterministic TbLTA (20.92 avg) trails ActFusion (28.39) by 7.47 points — a much larger gap than on Breakfast. The paper attributes this to "longer videos, denser action distributions, and frequent transitions" but provides no breakdown (e.g., by action type, sequence position, or horizon) to substantiate this. Without error analysis, it is unclear whether the bottleneck is alignment quality, decoder capacity, or a fundamental limitation of transcript supervision for this dataset.

### Minor

- **Progressive training scheme is not ablated.** The training procedure uses three stages (pre-training with video-level classification → alignment+segmentation → full optimization), and each stage resets the optimizer and scheduler. This is a non-trivial design choice, and its contribution to final performance is never quantified. An ablation removing the pre-training stage would clarify whether the gains come from the architecture or from the training pipeline.

- **Stochastic vs. deterministic comparison could be clearer.** The deterministic variant (Ours TbLTA) is the fair comparison to supervised methods. The stochastic variants (*-Mean, *-Top1) use a different, easier evaluation protocol (sampling multiple futures and selecting the best match). The table is correctly labeled and the caption explains the distinction, but the bold/gray formatting still invites casual readers to compare stochastic Top1 numbers (e.g., 37.15 avg on Breakfast, which exceeds everything) against supervised numbers. Anchoring the "competitive with fully supervised" claim to the deterministic results more prominently would improve clarity.

- **CRF target source is not explicitly stated.** Section 3.2.3 refers to "the target anticipate transcript $\mathcal{Y}_{\text{LTA}}$" without specifying that this is the pseudo-label sequence for the future portion. While inferable from context, stating this directly would improve clarity.

### Trivial

- **Notation inconsistency in CTC formulation (Sec 3.2.2).** The predicted action probabilities $\pi$ are defined as length $\alpha T$ (observed portion), but the CTC product in Eq. 4 runs to $T$ (full video). The same symbol $\pi$ is also overloaded for alignment path variables. This is confusing and should be harmonized.

- **Momentum buffer update mechanism unspecified.** The duration loss (Eq. 7) uses a momentum-based buffer $\hat{d}$, but the paper does not specify whether this is an exponential moving average, per-epoch average, or other mechanism, nor the update rate.

## Nice-to-Haves

- A simple baseline that predicts future actions directly from transcript subsequences (e.g., an LSTM on observed transcript items) would isolate the contribution of video features and cross-modal grounding.
- Reporting standard deviations across splits would strengthen the empirical claims, though this is not standard practice in LTA literature.
- An annotation-cost comparison (e.g., person-hours per video for transcript vs. frame-level labeling) would ground the practical motivation.

## Removed Points

These points were removed from the inputs for the following reasons:

1. *"No error bars / variance"* — Removed. Reporting standard deviations is not standard practice in the LTA benchmarks this paper evaluates on; none of the baselines report them either. This is a field-wide norm, not a paper-specific weakness.
2. *"Missing code / reproducibility concern"* — Removed. The paper states code will be released upon acceptance, which is appropriate for a double-blind submission.
3. *"Citation of Maté & Dimecicoli (2024) unclear / cannot verify"* — Removed per hard rules: the paper cites it, it exists.
4. *"Missing comparison to transcript-only baseline (LSTM)"* — Demoted to Nice-to-Have. This is a useful suggestion but not a weakness of the current evaluation, which already compares against established fully-supervised LTA methods and a prior semi-weakly-supervised method.
5. *"Grammar / formatting nitpicks"* — Removed per hard rules about parser artifacts.
6. *"Missing related works"* — Removed per hard rules (cannot confirm existence of unmentioned works).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add an ablation that freezes the ATBA alignment module during the full optimization stage, to isolate the decoder's learning from alignment-quality feedback loops.
2. Provide a per-class or per-horizon breakdown of 50Salads errors to clarify where transcript supervision falls short (alignment failures vs. capacity limitations on long sequences).
3. State explicitly in Section 3.2.3 that $\mathcal{Y}_{\text{LTA}}$ is derived from the pseudo-labels for the anticipation interval, and specify the momentum buffer update rule.

## Score and Decision

**Calibration anchors retrieved:**

| Anchor ID | Topic | Avg Score | Round | Comparison |
|---|---|---|---|---|
| azZZukIriZ | Scene graph anticipation | 3.33 | R1 (weak) | Clearly below this paper — withdrawn paper with serious flaws |
| 6SjmpmVKS2 | Weakly-supervised anomaly detection | 3.00 | R1 (weak) | Clearly below — withdrawn |
| vBFVaVf8aj | Robotic manipulation anticipation | 3.00 | R1 (weak) | Clearly below — withdrawn |
| lxAZ0ivDeB | Motion annotation | 3.00 | R1 (weak) | Clearly below — withdrawn |
| uKFVZMPppq | Action-guided attention for action anticipation | 5.50 | R1 (mid) | Comparable topic; this paper has a stronger contribution (first weakly-supervised LTA vs. new attention mechanism) and broader evaluation, but similar methodological concerns |
| SPE9gJfhB9 | Egocentric video understanding | 4.00 | R1 (mid) | Below — rejected |
| 8WS5nDWIWE | Long video generation | 6.00 | R1 (mid) | Different topic, similar score tier |
| ENwxBjOlAR | Weakly-supervised temporal action localization | 4.00 | R1 (mid) | Below — withdrawn |
| kI27Niy4xY | Text-to-3D generation | 8.00 | R1 (strong) | Different topic, clearly above |
| kkBOIsrCXh | Embodied navigation | 8.00 | R1 (strong) | Different topic, clearly above |
| DTQIjngDta | Visual geometry learning | 8.00 | R1 (strong) | Different topic, clearly above |
| oBXfPyi47m | RL with world models | 8.00 | R1 (strong) | Different topic, clearly above |
| 3lm8lWYxiq | LLM long-horizon execution | 6.00 | R2 (narrow) | Different topic, similar score |
| 3Genv8DQgf | Early action prediction | 5.00 | R2 (narrow) | Below — less comprehensive evaluation |
| c8r3lzyVTS | Video scene segmentation | 6.00 | R2 (narrow) | Different topic, similar score tier |
| zxito57J6x | Event segmentation | 6.00 | R2 (narrow) | Different topic |
| QQCrZXWG9s | Temporal video grounding | 6.00 | R2 (narrow) | Different topic, similar score tier |
| azcQJtcYTE | Spatio-temporal video grounding | 6.67 | R2 (narrow) | Above — stronger empirical results |

**Round 1 bracket:** [5.0, 6.5]  
**Round 2 narrowing:** Compared against uKFVZMPppq (5.50, the most topic-similar anchor), this paper has a stronger contribution (first weakly-supervised LTA paradigm vs. a new attention mechanism), more thorough ablation, and broader dataset coverage, placing it above 5.50. However, the confirmation bias concern and weaker 50Salads performance without analysis prevent it from reaching the 6.5+ tier.  
**Final score: 6.0**

<score>6.0</score>
<decision>Accept</decision>