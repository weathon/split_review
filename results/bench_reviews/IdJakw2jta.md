Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG) and proposes ART-STVG, an autoregressive transformer that processes video frames sequentially with selective spatial/temporal memory banks and a cascaded decoder design. The authors extend the HCSTVG-v2 validation set to 1–5 minute videos and show that ART-STVG outperforms existing STVG methods (TubeDETR, STCAT, CG-STVG, TA-STVG) across all five length settings while using much less GPU memory (7.9G vs. 23–26G).

## Strengths

1. **First dedicated treatment of long-form STVG.** The paper correctly identifies a real gap: existing STVG research is confined to videos under one minute, while practical applications demand minute- or hour-long video grounding. Formulating LF-STVG as a distinct problem and creating extended benchmarks is a useful framing contribution that could catalyze future work.

2. **Autoregressive streaming design naturally suits long videos.** Unlike prior methods that process all frames in parallel (requiring 23–26G GPU memory and making long-video inference prohibitive), ART-STVG processes frames sequentially with only 7.9G memory (Table 8). The design is both conceptually clean and practically motivated.

3. **Memory selection strategies are well-validated by ablation.** The ablations (Tables 2, 3) provide clear evidence that: (a) using *all* temporal memories hurts performance (9.6 m_tIoU) compared to no temporal memory (16.7 m_tIoU), and (b) the proposed temporal memory selection recovers and surpasses both (23.0 m_tIoU). The spatial memory selection also provides additive gains. These ablations convincingly demonstrate that selective memory is necessary.

4. **Comprehensive ablation study across multiple design axes.** The paper systematically ablates temporal memory selection (Table 2), spatial memory selection (Table 3), cascaded vs. parallel decoder design (Table 4), number of selected memories (Table 5), and training video length (Table 6). This thoroughness allows readers to understand what each component contributes.

5. **Consistent outperformance on all five length settings.** ART-STVG achieves the best results on LF-STVG-1min through 5min across all metrics (Table 1). The performance gap generally widens for longer videos (e.g., +0.7% m_tIoU on 1min vs. +7.3% on 5min over TA-STVG), supporting the claim that the architecture is better suited for longer contexts. The method also shows competitive short-form performance (59.2 m_vIoU vs. SOTA 60.4).

6. **Honest failure analysis and limitation discussion.** Appendix D provides concrete failure cases with clear diagnoses (indistinct event boundaries, distracting backgrounds, extremely short events), and Section G openly acknowledges performance degradation on very long videos and the lack of real-time operation.

## Weaknesses

### Fatal
None.

### Major

1. **Evaluation protocol conflates "architecture suitable for long videos" with "robustness to distribution shift."** All methods (including ART-STVG) are trained exclusively on 20-second videos from HCSTVG-v2 and evaluated on 1–5 minute videos. This is a zero-shot generalization test, not an evaluation of long-form STVG as a trained capability. The paper acknowledges this (line 621–624: "all methods including ART-STVG are trained exclusively on the HCSTVG-v2 training set… for fair comparison"), and Table 6 partially addresses it by training on 40-second videos, but 40 seconds is still far from the claimed 1–5 minute regime. The central claim—that ART-STVG "can handle long videos"—would be significantly strengthened by training on actual long-form data. As it stands, the experimental design cannot distinguish between architectural suitability and differential robustness to distribution shift.

2. **The baseline (ART-STVG without memory) already outperforms prior SOTA methods on several benchmarks, weakening attribution to the claimed contributions.** On LF-STVG-3min, the baseline achieves 16.2 m_tIoU vs. the best prior method at 14.2 (STCAT/CG-STVG). On LF-STVG-5min, the baseline achieves 9.2 vs. 8.1 (CG-STVG). This means the autoregressive architecture alone—absent the memory mechanisms that the paper emphasizes—already surpasses existing methods on the most challenging settings. While ART-STVG with memory is consistently better than the baseline (by +6.8 on 3min, +5.8 on 5min), the paper does not adequately analyze *why* the baseline is already stronger, making it impossible to disentangle the effect of the autoregressive design from the memory mechanisms. This undercuts the narrative that the memory modules are the primary drivers of improvement.

3. **Absolute performance on long videos is very low, raising questions about practical significance.** On 5-minute videos, ART-STVG achieves m_tIoU = 15.0%, m_vIoU = 10.0%, and vIoU@0.5 = 4.7%. While the paper correctly frames this as "significantly outperforming" other methods (which score even lower), the absolute numbers suggest the problem remains far from solved. The paper would benefit from a more measured discussion of whether these numbers constitute meaningful progress toward practical deployment or are merely a proof-of-concept first step.

### Minor

1. **Extended dataset construction lacks rigor.** The LF-STVG datasets extend the HCSTVG-v2 validation set from 20s to 1–5 minutes. The paper states these are "based on original YouTube videos, not concatenated clips" and "manually reviewed," but critical details are missing: no inter-annotator agreement statistics, no qualitative examples of extended videos, no analysis of whether the extended portions contain events relevant to the queries. Since the queries describe events from the original 20-second segment, the extra minutes are essentially irrelevant content by construction—which tests robustness to distractors but does not test whether a method can *track a target that changes over time*. A more rigorous validation protocol would strengthen the benchmark's credibility.

2. **Short-form performance falls behind TA-STVG (59.2 vs. 60.4 m_vIoU).** The paper describes this as "competitive," which is fair, but it reveals that the autoregressive design is not universally beneficial—it trades some short-form accuracy for long-video capability. This limitation should be stated more explicitly rather than minimized. The paper could also discuss whether design modifications could close this gap.

3. **All-temporal-memories setting degrades performance dramatically (9.6 vs. 16.7 m_tIoU).** The paper explains this as "using all temporal memories may introduce irrelevant information," which is plausible, but the severity of the degradation (7.1 points drop) warrants deeper analysis. Is the model's robustness fundamentally fragile? Under what conditions does the memory selection fail? A more detailed investigation would strengthen the paper.

### Trivial
- The paper defers several implementation details (loss function, baseline architecture) to the supplementary material. While acceptable, including the key equations in the main text would improve readability.
- Figure 3 (architecture diagram) is dense and hard to parse at small sizes.

## Nice-to-Haves
- Training a subset of methods on *actual* long-form data (even if only for a partial comparison) would substantially strengthen the evaluation.
- Statistical significance tests (e.g., confidence intervals) for the key results in Tables 1–4.
- Comparison with simpler temporal selection strategies (e.g., attention-weighted averaging) to better contextualize the temporal memory selection design.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Harsh Critic Issue 1 (evaluation protocol fundamentally invalid):** While the evaluation protocol limitation is real and is kept as a Major weakness above, the claim that it *invalidates* the central contribution is overstated. The paper explicitly acknowledges the limitation, and Table 6 provides a partial mitigation. The evaluation demonstrates that ART-STVG generalizes better to longer videos than alternatives, which is a meaningful empirical finding even if it is not a full validation of "long-form STVG." This criticism has been weakened and kept as Major weakness #1.

- **Harsh Critic Issue 2 (extended datasets not valid benchmarks):** The claim that the extended datasets "cannot support any conclusion about long-form STVG performance" is incorrect. Extending videos to include more irrelevant content around a target event is a standard and valid way to test robustness to temporal distractors—a core challenge in long-form understanding. The benchmark construction does have room for improvement (kept as Minor weakness #1), but the datasets are useful for their intended purpose.

- **Harsh Critic's claim that baseline "outperforms all prior state-of-the-art methods on LF-STVG-3min, 4min, and 5min"** is factually wrong for 4min (where the baseline at 9.9 m_tIoU is lower than STCAT at 10.4, CG-STVG at 10.6, and TA-STVG at 10.1). This factual error is removed; the partially correct observation is retained in Major weakness #2.

- **Harsh Critic's claim that "TubeDETR, STCAT, and CG-STVG operate on sampled frames… the distinction is about whether temporal modeling is parallel or sequential":** This is a pedantic framing issue. The paper's distinction (process-all-frames-at-once vs. streaming) is conceptually valid and practically meaningful regardless of sampling strategy.

- **Harsh Critic's claim that spatial memory selection is "standard cross-attention with a sparsity constraint":** Describing the mechanism in these terms is reductive but not a valid weakness. Many attention mechanisms in the literature can be described in such terms; what matters is whether the design is effective, which the ablations demonstrate.

- **Strength Finder's claim that "Significant outperformance across all long-video benchmarks"** is kept as a strength but reframed to acknowledge the low absolute numbers.

## Novel Insights

The most interesting observation from the reviews is the tension between the autoregressive architecture and the memory mechanisms as the true source of improvement. The baseline (autoregressive without memory) already outperforms prior non-autoregressive methods on the longer settings (3min, 5min), suggesting that the sequential processing paradigm itself carries significant benefits for distribution-shifted evaluations. Yet the memory selection mechanisms provide substantial additional gains (+6.8 m_tIoU on 3min). This suggests that the value proposition is cumulative: the autoregressive design provides a strong foundation, and the selective memory modules provide meaningful refinements on top. The paper would be strengthened by explicitly framing the contribution in these two-tier terms rather than foregrounding the memory mechanisms as the primary innovation.

Additionally, the finding that "all temporal memories" performs *worse* than "no temporal memory" (Table 2) is a striking result with broader implications for memory-augmented video understanding. It suggests that naive memory accumulation is actively harmful in long-video settings and that selection is not merely beneficial but *necessary*—a finding that could inform memory design in other long-video tasks.

## Suggestions

1. **Address the training/evaluation gap directly.** Either: (a) collect long-form training data (even a modest extension to 1 minute would be valuable), or (b) reframe the paper's claims from "a method for LF-STVG" to "a method that generalizes to longer videos," and discuss what additional training data would likely unlock.

2. **Analyze why the autoregressive baseline outperforms prior methods.** Provide an analysis (e.g., attention visualization, diagnostic experiments with controlled video lengths) that explains the source of the baseline's advantage. This would clarify the contribution attribution and strengthen the paper's scientific contribution.

3. **Provide more rigorous dataset documentation** for the extended benchmarks, including inter-annotator agreement, statistics on the relationship between queries and extended portions, and qualitative examples.

4. **Add a discussion of practical significance.** Acknowledge that 15% m_tIoU on 5-minute videos is a starting point, not a solution, and discuss what performance levels would be needed for practical applications.

5. **Investigate the "all temporal memories" degradation** in more detail to understand when and why memory accumulation fails, and whether simpler fixes (e.g., a learned gating mechanism) could mitigate the issue.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Comparison to this paper |
|---|---|---|
| `/home/.../BOFzC3xndr.md` (Video-in-the-Loop) | 4.67 | Similar long-video ambition, comparable quality of evidence; this paper has more thorough ablations but a weaker evaluation protocol |
| `/home/.../zuPxAZgT9F.md` (STVG-R1) | 4.67 | Same STVG domain; STVG-R1 has cleaner evaluation but less novel problem framing; comparable overall |
| `/home/.../8H1HmGH8ua.md` (LongVTG-R1) | 3.50 | This paper is notably stronger in evidence breadth and evaluation depth |
| `/home/.../vIecIscDJf.md` (HiTeA) | 5.50 | HiTeA is a more polished paper with cleaner evaluation; this paper is slightly below in overall quality |
| `/home/.../kyLS9EhPhY.md` (Nar-KFC) | 5.00 | Similar quality tier; both have clear contributions with some evaluation limitations |
| `/home/.../QQCrZXWG9s.md` (Invert4TVG) | 6.00 | Stronger paper with cleaner evaluation and clearer novelty attribution |
| `/home/.../WAk6tf8VkQ.md` (Vinoground) | 3.00 | This paper is significantly stronger overall |

Positioning: This paper sits between the 4.67 anchors (similar tier) and the 5.50–6.00 anchors (somewhat below). It has genuine contributions (first LF-STVG formulation, autoregressive design, selective memory) and solid experimental evidence, but the evaluation gap and strong baseline weaken the core narrative. Comparable to Nar-KFC (5.00) and slightly below HiTeA (5.50).

**Score:** 5.0 — The paper makes a useful contribution to an underexplored problem with a well-designed method and thorough ablations. The evaluation limitations are real but not fatal. The contributions are sufficient for a poster presentation.

**Decision:** Accept (Poster)

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>