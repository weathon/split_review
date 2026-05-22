Alright, I now have a solid calibration picture. Let me synthesize the final review.

**Calibration Summary:**
- Round 1 bracket: between ~3.5 and ~7.5. The paper clearly sits above weak papers (scores 2-3) and below strong papers (scores 7.5+).
- Round 2 narrowing: anchors at 4.5-6.0 are the most relevant.
  - P6G1Z6jkf3 (6.0, accept): Egocentric video representation learning with unanimous 6s. Clean execution, clearer contribution. COAD is weaker due to unaddressed supervision assumption.
  - 1L52bHEL5d (6.0, accept): TTA for missing modalities. Well-scoped with clear limitations. COAD has a more significant framing gap.
  - Y7jJN0VQ4y (5.71, reject): Continual learning for video anomaly detection. Mixed reviews; similar pattern of a new task formulation with limitations in evaluation. COAD is comparable in strength.
  - JbPb6RieNC (5.8, accept): Streaming video benchmark + method. Mixed reviews (8,6,6,6,3). Benchmark contribution is strong.
- COAD's contributions (Ego-OAD benchmark, ablation study, consistent out-stream gains) are genuine, but the unaddressed supervision assumption and the weak baseline comparison are significant enough to prevent strong acceptance. The paper is around the 5.5 mark.

Here is the final review:

## Summary
This paper introduces Continuous Online Action Detection (COAD), a task formulation that enables OAD models to adapt in a single causal pass from streaming egocentric video, alongside a new large-scale egocentric OAD benchmark (Ego-OAD) curated from Ego4D. Three training strategies (state continuity, orthogonal gradient projection, non-uniform loss) are proposed and ablated. COAD yields consistent improvements on out-of-stream generalization (e.g., +6.9% Top-5 Recall on Ego-OAD with egocentric pretraining).

## Strengths
- **Ego-OAD dataset fills a clear gap.** The paper curates a large-scale egocentric OAD benchmark (87 classes, 263 hours, 22,991 instances) with multi-label temporal annotations from Ego4D MQ. This is a useful resource for a field that has mostly relied on EPIC-KITCHENS (single-domain) or exocentric datasets.
- **Thorough component-level ablation (Table 3).** Each proposed strategy (state continuity, orthogonal gradient, non-uniform loss) is ablated independently, providing clear evidence of which components drive which aspects of performance. The non-uniform loss from MiniROD proves to be the most influential component for out-stream mAP.
- **Consistent out-of-stream generalization gains across settings.** COAD improves out-of-stream Top-5 Recall under both egocentric and exocentric pretraining on Ego-OAD (6.9% and 6.5% respectively), while the w/o COAD baseline shows much smaller gains (2.5% and 2.3%). This demonstrates that the full combination of strategies is effective for generalization.
- **Clear framing of a relevant problem.** The motivation for bridging offline OAD training and online deployment on streaming video from wearable devices is well-argued and timely.

## Weaknesses

### Fatal
None.

### Major
- **Unaddressed supervision assumption conflicts with the claimed application scenario.** COAD requires ground-truth action labels at each training window's final frame during in-stream adaptation. The paper frames COAD as enabling "personalized egocentric AI systems" on wearable devices, but never discusses how such labels would be obtained during deployment — no human oracle or self-supervised proxy is proposed. This gap between the motivating use case and the actual experimental setup is significant. The paper should either acknowledge this as a best-case-scenario limitation or propose a path toward weaker supervision.

- **The "w/o COAD" baseline strips state continuity, making it weaker than a natural streaming baseline.** The paper defines the baseline as training on in-stream data without any of the three proposed strategies — including *state continuity*, which means the RNN hidden state is reset at each window boundary during training. In a real streaming deployment, any reasonable training procedure would maintain the hidden state (since that is how the model will be used at inference). This inflates the relative gains attributed to the full COAD method. The ablation in Table 3 partially addresses this (Row 4, which removes state continuity, achieves 25.9/36.7 vs. full COAD's 26.0/36.8), showing the effect is modest — but the baseline design remains suboptimal and should be improved.

### Minor
- **EPIC-KITCHENS results are mixed and reveal generalization limitations.** On action-level mAP, COAD improves out-of-stream (9.9 vs. 8.6) but degrades in-stream (7.9 vs. 9.6) compared to the pretrained-only model. The paper attributes this to fine-grained annotations, but the same concern applies to Ego-OAD which also has fine-grained classes. This suggests the method's effectiveness is dataset-dependent and not as robust as the main results imply.

- **Novelty is primarily in task formulation and engineering, not algorithmic innovation.** The three training components — state continuity, orthogonal gradient projection (Han et al., 2025), and non-uniform loss (An et al., 2023) — are all adapted from prior work. The main contribution is combining them within a new task formulation (continuous OAD) and demonstrating their combined effectiveness. The paper should temper claims of being a "new paradigm" and more accurately frame this as a well-engineered training pipeline.

- **In-stream mAP vs. Top-5 Recall trade-off is under-discussed.** On Ego-OAD (Ego pretrain, in-stream), COAD achieves lower mAP than the baseline (36.8 vs. 39.0) but higher Top-5 Recall (89.3 vs. 86.7). The paper states COAD "maintains robust performance across both domains," which understates this trade-off. A clearer discussion of why this happens and whether mAP or Recall is the more appropriate metric for this setting would strengthen the paper.

### Trivial
- The abstract states "up to 20% in top-5 accuracy" when Table 1 shows an improvement of 22.5 *percentage points* (from 57.5 to 80.0). This should be clarified as percentage points, not percent.

## Nice-to-Haves
- The orthogonal gradient projection uses only the immediately preceding gradient. A brief justification of this design choice (e.g., why not a longer history or gradient buffer) would strengthen the method section.
- A class-frequency analysis and per-class mAP breakdown for Ego-OAD would help assess whether gains are concentrated in specific action types.
- Comparing against alternative continual learning strategies (e.g., EWC, replay-based methods adapted to the streaming constraint) would further contextualize the results, even if only as a discussion of why they are unsuitable under the single-pass, no-storage constraint.

## Removed Points
- Criticism about "87 classes being a small vocabulary" — removed as subjective and not a meaningful weakness for an OAD benchmark; 87 fine-grained classes with multi-label annotations is reasonable.
- Criticism about the split sizes being "heavily skewed" — the paper explicitly states that most data is allocated to the in-stream split to assess continuous learning, which is a deliberate design choice consistent with the protocol of Carreira et al. (2024).
- Criticism about the method being "essentially an application of single-pass continual learning to OAD" — this is what the paper transparently claims; the paper cites Carreira et al. directly and frames COAD as adapting these principles to OAD. This does not make the contribution less valid.
- Strength Finder's point about "novel task formulation" — retained as it is a genuine contribution, but tempered in the weaknesses section above.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Add a stronger baseline that maintains state continuity** but omits the other two strategies (orthogonal gradient, non-uniform loss). This would directly isolate the value added by the specific COAD strategies beyond the natural streaming setup.
2. **Acknowledge the supervision limitation explicitly** in the main text — state clearly that COAD assumes labels are available during deployment (e.g., from a human-in-the-loop or a downstream task that provides them), and discuss what would be needed to relax this assumption.
3. **Clarify the mAP/Recall trade-off** on in-stream performance with a dedicated discussion. If the claim is that Top-5 Recall is the more meaningful metric for this setting (following EPIC conventions), state this explicitly and justify why.

## Score and Decision

**Calibration anchors used:**

| Anchor ID | Avg Score | Round | Comparison |
|---|---|---|---|
| P6G1Z6jkf3 | 6.00 | 1, 2 | Egocentric video representation learning (accept). Cleaner execution; COAD has larger framing gaps. COAD is weaker. |
| 2HdZPEQUig | 3.00 | 1 | Object-centric video learning (reject). COAD is clearly stronger. |
| 7L2bpe7lfm | 4.50 | 1 | Video continual learning (reject). COAD has stronger benchmark contribution and clearer evaluation. COAD is stronger. |
| jawV7vhGHw | 4.25 | 1 | Real-time video classification (reject). COAD is better structured and more clearly motivated. COAD is stronger. |
| 1L52bHEL5d | 6.00 | 2 | TTA for missing modalities (accept). Unanimous 6s; well-scoped. COAD is weaker due to unaddressed supervision gap. |
| Y7jJN0VQ4y | 5.71 | 2 | Continual learning for video anomaly detection (reject). Similar pattern of new task + limitations. COAD is comparable. |
| JbPb6RieNC | 5.80 | 2 | Streaming video understanding benchmark (accept). Mixed reviews; strong benchmark contribution. COAD is slightly weaker. |
| oO3oXJ19Pb | 4.80 | 2 | Online action-augmented dense captioning (reject). COAD has better evaluation and clearer contributions. COAD is stronger. |

Round 1 bracket: 3.5–7.5. Round 2 narrowed to 4.8–6.0. COAD sits between the weaker rejected papers (~4.5–4.8) and the cleaner accepted papers (~6.0), closer to the 5.5–5.8 range. The unaddressed supervision assumption and baseline fairness issues prevent a higher score, but the genuine dataset contribution and well-structured evaluation keep it above the outright reject level.

**Final Score:** 5.5

**Decision:** Reject (borderline; could become an accept with major revisions addressing the supervision assumption and baseline fairness)

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>