Now I have a thorough understanding of the paper and the calibration anchors. Let me write the final consolidated review.

---

## Summary

This paper introduces TbLTA, the first framework for dense long-term action anticipation (LTA) trained exclusively from video transcripts — ordered lists of action labels without timing or duration information — eliminating the need for costly frame-level annotations. The method combines a temporal alignment module (ATBA) that generates dense pseudo-labels from transcripts, a cross-modal attention mechanism that grounds video features in transcript semantics, CTC-based alignment losses, and a CRF-augmented anticipation decoder. Experiments are reported on Breakfast, 50Salads, and EGTEA benchmarks, with TbLTA showing competitive performance against fully-supervised baselines on 50Salads.

## Strengths

- **First transcript-only LTA framework**: The paper genuinely establishes a new weakly-supervised paradigm for dense LTA. Prior work (Zhang et al., 2021) still required some frame-level labels for the observed segment; TbLTA is the first to use only ordered action lists. This is a meaningful reduction in annotation cost and a novel problem setting.

- **Coherent multi-component architecture**: The integration of ATBA-based temporal alignment, CTC loss, cross-modal attention with local masking, and a CRF decoder is well-motivated. Each component addresses a specific challenge in the weakly-supervised setting (pseudo-label generation, transcript consistency, semantic grounding, sequence coherence).

- **Clear ablation evidence for key components**: The paper reports that removing the cross-modal attention drops accuracy by ~5.7 points on Breakfast and ~1.3 points on 50Salads, and removing CTC supervision drops accuracy by ~0.6–0.8 points (Section 4.3). These results support the contribution of the proposed architectural choices.

- **Competitive results on 50Salads**: TbLTA achieves an average MoC of 28.5 on 50Salads, which is essentially tied with the fully-supervised ActFusion (28.39) in the deterministic setting — a notable result given the absence of frame-level annotations.

- **Demonstration that transcript supervision helps rare classes**: On EGTEA Gaze+, TbLTA proves competitive on rare action classes, suggesting that high-level semantic supervision from transcripts can mitigate class imbalance without dense labels.

## Weaknesses

### Fatal
None.

### Major

- **ATBA uses future video features to generate training targets for the anticipation decoder — implications not discussed.** During training, the ATBA module operates on the *full* video (including future frames) to partition the transcript and produce per-frame pseudo-labels for both the observed and future intervals. These future-interval pseudo-labels are then used to supervise the LTA decoder, which at training time takes only *observed* encoder features as input (Section 3.1, lines 260-262: "operates on the fused encoder output, defined as F̃ ∈ R^{Tobs × dTAS}"). While this is akin to teacher-student distillation (ATBA-as-teacher sees the full video; the decoder-as-student sees only observed frames), the paper does not acknowledge or discuss this asymmetry. The concern is not that the method is invalid — knowledge distillation from a more-informed teacher is a legitimate training strategy — but that it complicates claims of being "competitive with fully supervised methods," because the training targets for the future are aligned with the benefit of future visual evidence. The paper should discuss this design choice, justify why it does not constitute an unfair advantage relative to supervised baselines, and ideally include an ablation comparing ATBA alignment on full video vs. ATBA alignment restricted to observed features only.

- **TbLTA results on Breakfast are absent from the main comparison table (Table 1).** Table 1 shows supervised baselines (Cycle Cons., FUTR, ActFusion) and the semi-weak baseline WS-DA on both 50Salads and Breakfast, but TbLTA's own numbers appear only for 50Salads (line 589). The paper's headline claim — "On Breakfast, TbLTA exhibits a pronounced gain at 30% observation, outperforming all supervised baselines" (lines 509-510) — is therefore unverifiable from the data presented in the main body. While these numbers may exist in an appendix (which the parser strips), the main comparison table is the natural home for the paper's central results, and their absence is a significant evidential gap. Including TbLTA's Breakfast results in Table 1 is essential.

### Minor

- **Ablation tables referenced in text but not visible.** Tables 3 (TAS ablation) and 4 (LTA ablation) are discussed in Section 4.3 (lines 537-540) but do not appear in the main body. The EGTEA results table (Table 2) appears truncated (only Timeception and Anticipatr are shown before the text breaks into Section 4.4). These are likely parser/appendix artifacts, but in the main body they leave claims of "consistent hierarchy" and cross-attention benefits unsubstantiated.

- **The duration-loss ablation shows a marginal gain.** On 50Salads, removing the duration loss changes the average MoC from 28.5 to 28.3 — only 0.2 points (lines 584-591). This is a tiny effect and does not strongly justify the complexity of the affinity-based duration buffer. The paper should discuss whether this component is pulling its weight or whether the gain is within noise.

- **No discussion of soft-target effects.** ATBA generates soft pseudo-labels (line 236: "soft per-frame pseudo-labels that preserve boundary uncertainty"). Training on soft vs. hard targets can affect model calibration and confidence. While evaluation is against ground-truth hard labels (so the metric is not directly inflated), the effect on what the model learns is worth a brief discussion.

### Trivial
- Some table formatting is inconsistent (e.g., the EGTEA table fragment blends into narrative text).

## Nice-to-Haves

- An ablation where ATBA is restricted to observed features only (with the future transcript still used as a symbolic target but aligned without benefit of future video) would directly quantify the effect of the full-video alignment on the decoder's training signal.

- Reporting TbLTA's performance when evaluated against hard ground-truth labels with hard-label training (i.e., a fully-supervised variant of the same architecture) would help isolate how much of the competitive performance comes from the architecture vs. the weakly-supervised training regime.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

1. **"Information leakage from future-derived pseudo-labels is fatal / structural."** (Harsh Critic, Issue 1) — Removed as a *fatal* classification. The ATBA module uses future video features for alignment, but ATBA is itself weakly supervised (transcript-only). Using a teacher model with more information to generate training targets for a student is standard knowledge distillation and does not invalidate the core method. However, the asymmetry is a real concern that the paper should discuss; elevated to Major (see above).

2. **"Results cannot be trusted as evidence for transcript-based LTA."** (Harsh Critic) — Removed as overstatement. The decoder genuinely predicts from observed features only at both training and inference time. The "leak" is in the training targets, not in the model inputs.

3. **"Unfair comparison due to softer pseudo-label targets artificially inflating MoC."** (Harsh Critic, Issue 3) — Weakened and moved to Minor. MoC is computed against ground-truth hard labels at test time, not against the pseudo-labels used during training. Soft training targets do not directly inflate the evaluation metric. However, the effect on model behavior is worth discussion.

4. **"Missing results for Breakfast and incomplete ablation evidence."** (Harsh Critic, Issue 2) — Partially retained. The Breakfast results genuinely do not appear in Table 1 (the main comparison table), which IS a significant gap. But the claim that "no numbers are provided in the table to support this" could be a parser issue if results are in the appendix. Kept as Major but framed as a presentation/evidential concern rather than a fatal evidential gap.

5. **Strength Finder claim about "clear outperformance over WS-DA"** — This claim is valid; TbLTA is clearly better than WS-DA on 50Salads. Retained.

6. **Strength Finder claim about "pronounced gain on Breakfast outperforming all supervised baselines"** — This claim cannot be verified from the main-body data. Flagged under Major weakness above.

7. **Missing ablation tables (Table 3, 4)** — Likely parser/appendix artifact. Noted under Minor.

8. **"No significance testing"** (Harsh Critic) — Valid minor point but not central. Noted implicitly via the close-results concern.

## Overall Assessment

TbLTA makes a genuine contribution: it is, to my knowledge, the first method to tackle dense long-term action anticipation using only video transcripts as supervision, eliminating the need for frame-level annotations entirely. The architecture is modular and well-motivated, and the results on 50Salads demonstrate that transcript-based LTA is feasible and can approach fully-supervised performance.

However, the paper has two notable issues that prevent a stronger recommendation. First, the use of ATBA on the full video (including future frames) to generate training targets for the anticipation decoder is an asymmetry that should be acknowledged and discussed — it is not fatal, but it complicates claims of direct equivalence with fully-supervised training. Second, the Breakfast results for TbLTA are absent from the main comparison table (Table 1), leaving the paper's strongest claim unverifiable from the main body. The EGTEA table is also truncated.

These issues are addressable: the Breakfast numbers can be added to Table 1, the ATBA design choice can be discussed and (ideally) ablated, and the missing tables can be restored. The core contribution — demonstrating that LTA is possible from transcripts alone — remains valid and significant.

**Score: 4.5** (borderline; would lean toward acceptance if the Breakfast results were verifiable and the ATBA concern was addressed in rebuttal).

**Calibration note**: This score sits below EAST (5.0, accepted poster — cleaner empirical presentation with stronger, verified results) and AGA (5.50, accepted poster — novel mechanism with thorough ablations), but above LAF (4.0, rejected — contradictory results, heavy reliance on pretrained modules) and OOTSM (3.33, rejected — limited technical novelty despite novel problem). TbLTA's novelty as first transcript-only LTA is comparable to EAST's practical contribution, but the evidential gaps (missing Breakfast numbers in the main table) and the unaddressed methodological concern pull the score down.