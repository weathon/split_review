Now I have sufficient calibration data. Let me synthesize the final review.

## Calibration Summary

**Round 1 (Bracketing):** My initial bracket was 4.0–6.0 based on comparing IRIS against the weak anchors (avg 2.0–3.33, very different topics) and the strong anchors (>7.5, not T2I-RL topics). The middle-band anchors (GoT-R1 4.50, IntDiff 4.50, From Broad Exploration 4.67, FocusDiff 5.00) are the most relevant comparisons.

**Round 2 (Narrowing):** I compared IRIS against GoT-R1 (4.50, Accept Poster), STAGE (4.50, Reject), FocusDiff (5.00, Reject), and From Broad Exploration (4.67, Accept Poster). IRIS has stronger novelty than all of these (first fully intrinsic reward for T2I), comparable evaluation breadth, and cleaner experimental design (no reward-evaluation confound as in FocusDiff). IRIS is clearly stronger than GoT-R1, STAGE, and comparable to From Broad Exploration but with a different angle. The weaknesses (limited model scope, 800-step training, Fig. 2 uncontrolled comparison) are real but not fatal.

**Final Score:** 5.5 — above the 4.5–5.0 cluster of similar papers, justified by the genuine novelty and thorough ablations, but not reaching 6+ due to limited model generality and stability analysis.

---

## Summary

This paper proposes **IRIS**, the first reinforcement learning framework for autoregressive text-to-image generation that uses **only an intrinsic reward** — specifically, Negative Self-Certainty (NSC), defined as the forward KL divergence between the model's token-level output distribution and a uniform distribution. The key insight is that minimizing self-certainty (maximizing uncertainty) improves T2I generation quality, in contrast to prior findings in text reasoning where maximizing self-certainty helps. Empirically, IRIS applied to Janus-Pro-1B/7B achieves results comparable to the external-reward baseline T2I-R1 across GenEval, T2I-CompBench, and WISE, with thorough ablations confirming each design choice.

## Strengths

1. **First fully intrinsic-reward RL framework for autoregressive T2I models.** IRIS requires no human labels, domain-specific verifiers, or external reward models — the reward is computed purely from the model's own output distribution. Table 1 shows Janus-Pro-1B + IRIS achieves overall GenEval 0.72, T2I-CompBench 0.3793, and WISE 0.37, competitive with T2I-R1 (0.75, 0.3820, 0.38) despite never seeing external rewards during training. This is a genuine advance in reducing supervision requirements for T2I alignment.

2. **Well-designed and informative ablation study.** Figures 5–9 systematically validate every design choice: CoT vs. no CoT, minimizing vs. maximizing image SC, minimizing vs. maximizing text SC, forward KL vs. backward KL (entropy), and RL vs. direct optimization. These ablations cleanly support the paper's core claims and provide strong internal validity.

3. **Identification and correction of a chat-template bug in the T2I-R1 baseline** (Section 4.1). Noting that the official T2I-R1 implementation used Janus (not Janus-Pro) chat templates for Janus-Pro models and correcting this improves evaluation integrity.

## Weaknesses

### Fatal
None.

### Major
- **Limited model generality and training duration.** All experiments use only the Janus-Pro model family (1B and 7B variants) for only 800 training steps. The paper does not demonstrate that IRIS transfers to other autoregressive T2I architectures (e.g., Show-o, VILA-U) or that it remains stable over longer training horizons (e.g., 2000+ steps). Figure 9 shows that direct NSC optimization collapses within 800 steps; whether IRIS itself would eventually collapse given more steps is unaddressed. This limits confidence in the method's generality and stability.

### Minor
1. **The motivating observation (Figure 2) compares across different models and tasks.** Figure 2 contrasts self-certainty of Qwen2.5-1.5B on math reasoning (text) with Janus-Pro-1B on T2I (image). Because the models, tasks, training data, and optimization dynamics all differ simultaneously, this comparison does not cleanly isolate the effect of modality on self-certainty behavior. The paper's core contribution (IRIS works for T2I) does not depend on this being a controlled experiment — the ablations provide the real evidence — but the framing of a "task-dependent role" overclaims relative to this single, uncontrolled observation.

2. **The baseline comparison lacks full transparency.** The paper identifies and corrects a chat-template inconsistency in T2I-R1 and reports only its re-run numbers. While the correction is principled, the original published T2I-R1 numbers are not reported alongside for comparison. A reader cannot assess the magnitude of the difference caused by the template fix. Adding the original numbers in a footnote or table would resolve this.

3. **No discussion of computational cost.** The GRPO setup generates 8 text strings × 1 image per query, requiring substantial image token generation per step. Reporting total GPU-hours or wall-clock time would help the community assess practicality.

4. **Error bars are absent from the learning curves** (Figures 3, 5–9). Table 1 reports standard deviations, suggesting multi-seed data exists, but the line plots show only point estimates. Adding variance shading would improve trust in the reported trends.

### Trivial
None.

## Nice-to-Haves
- A controlled experiment for Figure 2 (training the same model on both a text reasoning task and a T2I task with the same optimizer) would cleanly validate the modality-dependence claim.
- Analysis of how NSC correlates with standard image quality metrics (e.g., FID, diversity) during training would strengthen the claim that minimizing SC is the right signal.
- Testing on at least one additional autoregressive T2I architecture (e.g., Show-o) would strengthen claims of generality.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Undocumented re-implementation"** — The paper clearly documents the template fix and its impact. The re-implementation is documented; the issue is about transparency (original numbers not reported), not absence of documentation. Moved to Minor weakness #2.
2. **"Missing theoretical rationale for forward KL"** — The paper provides rationale (mode-covering vs. mode-seeking) and ablation evidence (Fig. 8). This is adequately addressed.
3. **"Ablation metrics are the same external rewards used to train T2I-R1"** — The paper explicitly acknowledges this (Section 4.3, line 215: "we never use these reward models in the training objectives") and notes they are used only for evaluation, not training. Not a weakness.
4. **"No analysis of what the model actually learns"** — The paper provides quantitative benchmark results, qualitative examples (Fig. 1, 4), and a discussion of which categories IRIS excels at (natural science vs. aesthetics/spatial). Adequate for the paper's scope.

## Novel Insights

The harsh critic's observation that the IRIS paper claims a **modality-dependent role for self-certainty** (maximizing for text, minimizing for images) but supports it with an uncontrolled comparison is a genuine insight that sharpens the boundary between the paper's motivating narrative and its actual empirical contribution. The paper's real strength is not the cross-modal comparison per se, but the demonstration that a purely intrinsic reward can drive meaningful T2I improvements — a finding that is empirically well-supported by the ablations even if the broader framing overreaches slightly. Additionally, the tension between this paper (which minimizes SC for T2I) and the concurrent "From Broad Exploration to Stable Synthesis" paper (which also uses entropy-based reasoning but reaches different conclusions about CoT entropy direction) suggests an interesting unresolved question in the field about precisely what uncertainty signal is optimal for T2I generation.

## Suggestions
1. Report the original T2I-R1 published numbers in Table 1 alongside the corrected re-run numbers, so readers can assess the impact of the chat template fix.
2. Add error bars / variance shading to the learning curves (Figures 3, 5–9).
3. Acknowledge the uncontrolled nature of Figure 2 explicitly and temper the claim from "RL alignment increases self-certainty for text but decreases it for images" to "in our experiments, self-certainty decreases during T2I training with external rewards."
4. Include GPU-hour estimates and discuss whether longer training (2000+ steps) would maintain stability.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>