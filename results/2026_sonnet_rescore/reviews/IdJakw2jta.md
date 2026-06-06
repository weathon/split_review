## Summary

This paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG) as a new sub-problem and proposes ART-STVG, an autoregressive transformer that processes video frames sequentially with selective spatial and temporal memory banks and a cascaded spatio-temporal decoder design. The paper also extends the HCSTVG-v2 validation set to create five LF-STVG benchmarks (1–5 minute videos). ART-STVG consistently outperforms prior parallel-processing STVG methods across all five long-form benchmarks while remaining competitive on the standard short-form setting.

---

## Strengths

- **Consistent and growing empirical advantage on LF-STVG (Table 1):** ART-STVG outperforms the best existing method (TA-STVG) by +0.7%, +6.5%, +9.1%, +6.2%, and +7.3% m.tIoU across the 1–5 minute splits, with the gap widening as video length increases. This trend is directly visible in Figure 2.

- **Selective temporal memory is transformative (Table 2):** Using *all* temporal memories actually degrades m.tIoU from 16.7% (no memory, row ❶) to 9.6% (all memory, row ❷), while selective memory raises it to 23.0% (row ❸) — a 13.4-point gain over full memory. This quantifies why naïve memory accumulation fails for long videos and strongly validates the paper's central design choice.

- **Cascaded decoder validated in ablation (Table 4):** The cascaded spatial→temporal design achieves m.tIoU 23.0 vs. 21.5 for the parallel variant, confirming that fine-grained spatial target features assist temporal boundary localization.

- **Robustness to training duration (Table 6):** When all methods are retrained on 40-second clips, ART-STVG still leads with m.tIoU 28.3 vs. 21.0 for the best competitor (STCAT), indicating architectural — not purely data-driven — advantages.

- **Competitive on short-form STVG (Table 7):** ART-STVG achieves m.tIoU 59.2/m.vIoU 39.2 on the original HCSTVG-v2 validation set, trailing only TA-STVG by 1.2%/1.0%, demonstrating no catastrophic trade-off for the standard short-form setting.

---

## Weaknesses

### Fatal
None.

### Major

- **Unspecified baseline inference procedure for long videos.** Section 4.1 states "all methods including ART-STVG are trained exclusively on the HCSTVG-v2 training set (average video length 20 seconds) for fair comparison," but says nothing about how parallel-processing baselines (TubeDETR, STCAT, CG-STVG, TA-STVG) handle test videos at inference. These methods are designed to ingest ~64 frames simultaneously; at 3.2 FPS, a 5-minute video yields ~960 frames. Whether baselines receive all 960 frames (likely exceeding GPU memory), a subsampled 64-frame subset, or a sliding window is never stated. If baselines are subsampled while ART-STVG processes all frames sequentially, Table 1 measures "sequential full-frame processing vs. severe temporal subsampling" rather than the streaming architecture advantage the paper claims. The monotonically widening performance gap in Figure 2 is entirely consistent with this artifact. This does not invalidate the paper's contribution, but it significantly weakens the strength of the headline comparative claim. The authors should document exactly how each baseline was run at inference on long videos, ideally including a sliding-window baseline that equalizes total frames seen.

- **No LF-STVG training split; all evaluation is out-of-distribution.** As stated in Section 4: "we extend only the validation set to lengths of 1 to 5 minutes." All methods are tested in a setting where they are trained on 20-second clips and evaluated on 1–5 minute videos. While Table 6 partially addresses this with 40-second training, the benchmark construction conflates two questions: which architecture is best at LF-STVG, and which architecture generalizes better across a 6× domain shift. This limitation is not acknowledged in the paper and should be discussed, along with what a purpose-built LF-STVG benchmark would require.

### Minor

- **Striking Table 2 result left unexplained.** The drop from m.tIoU 16.7% (no temporal memory) to 9.6% (all temporal memory) is not just a neutral zero-sum result — the unfiltered memory *actively harms* performance well below the no-memory baseline. The paper attributes this to "irrelevant information" (Section 4.2) but does not investigate whether this reflects optimization instability during training, attention pollution at inference, or both. The magnitude (−7.1 points) is large enough to warrant at least a brief diagnostic.

- **Spatial vs. temporal memory contribute asymmetrically but are treated symmetrically.** Table 3 shows spatial memory selection adds +0.9% m.tIoU (❷→❸), while Table 2 shows temporal selection adds +13.4% (❷→❸). The paper lists both as equal contributions in Section 1, but the evidence makes temporal memory far more important. Acknowledging this asymmetry would improve the discussion.

- **SF-STVG baseline gap not discussed.** The Baseline (46.2% m.tIoU in Table 7) underperforms all prior methods by a substantial margin (>7 points below TubeDETR). The paper does not discuss why the autoregressive architecture incurs this penalty on short-form video, which slightly undercuts the architecture's generality story.

### Trivial
None beyond parser artifacts in the extracted text.

---

## Nice-to-Haves

- A plot of inference memory footprint or latency vs. video length would ground the practical deployment claims. The paper notes that "we update the memory bank by simply adding the query as a new memory, without removing any existing memories" (Sec. 3.3); at 5 minutes this grows to ~960 entries per decoder partition. Showing that inference remains tractable at these lengths would strengthen the streaming deployment argument.
- An analysis of performance by temporal position of the target event within the long video (early vs. late) would help isolate whether streaming's advantage comes from seeing more frames or from better event isolation.
- A qualitative failure analysis beyond the single positive example in Figure 6 would add credibility to the temporal event segmentation mechanism.
- Table 6 currently covers only one duration step (40 seconds). Extending this to 1–2 minute training splits would more directly address the out-of-distribution concern.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Loss function deferred to supplementary (Harsh Critic):** Section 3.5 explicitly notes the loss function is in the supplementary material. Per the review rules, the parser strips supplementary from all papers; this is not an author choice to hide information. Removed.

- **Baseline architecture deferred to supplementary (Harsh Critic):** Similarly, Section 4.1 notes the baseline architecture is in supplementary. The parser removes these sections uniformly; this cannot be held against authors. Removed.

- **Circular dependency in temporal memory during early training (Harsh Critic):** The claim that temporal queries "may not yet encode reliable event structure" early in training is speculative. There is no evidence in the paper that this is a practical problem; the ablation results (Table 2) show the system converges to strong performance with temporal selection. Removed as speculative-fatal demoted.

- **Memory bank unbounded growth as a fatal concern (Harsh Critic):** Treated as Nice-to-Have rather than Major. The paper is an empirical systems contribution; its primary claim is that selective memory streaming improves LF-STVG, which is well-supported by Tables 1–6. The practical deployment analysis is desirable but not a validity threat.

- **Strength Finder: "Autoregressive processing avoids bottleneck" (generic):** Too generic; folded into the more specific Table 1 empirical claim.

---

## Novel Insights

The most genuinely novel observation in this review (beyond what the paper itself says) is the conjunction of two findings: (1) unfiltered temporal memory actively harms performance by >7 points below the no-memory baseline (Table 2), and (2) unfiltered spatial memory mildly helps (+0.8 points, Table 3). This asymmetry implies that temporal context in long videos is specifically toxic when undifferentiated — likely because temporal queries accumulate cross-event signal that confuses event-boundary detection — while spatial appearance context is more compositionally beneficial. The TextTiling-inspired boundary detection is thus not merely a convenience but appears to be a prerequisite for the temporal memory to function at all. This has implications beyond STVG for any streaming architecture that maintains temporal state in multi-event settings.

---

## Suggestions

1. **Document baseline inference procedures explicitly** (a table or paragraph in experiments stating: TubeDETR receives X frames via [subsampling/sliding window/truncation], STCAT receives…, etc.). This is the single highest-leverage fix.
2. **Include a sliding-window baseline** for at least one competing method so that "sequential processing" can be isolated from "full-frame processing."
3. **Acknowledge the validation-set-only benchmark as a limitation** in Section 5 or a Limitations section, and outline what a proper LF-STVG training benchmark would require (e.g., annotating longer clips from scratch).
4. **Add a brief diagnostic for the Table 2 anomaly** — even a training loss curve comparison between the "all memory" and "selective memory" models would help.
5. **Discuss the SF-STVG baseline penalty** (46.2% vs. 53.9%+): if autoregressive processing inherently sacrifices some parallel inter-frame context, quantifying this trade-off helps readers understand where ART-STVG is and is not the right architecture.

---

**Axes:**

- **Originality:** High. LF-STVG is a well-motivated new problem formulation; the autoregressive streaming approach with event-boundary-driven temporal memory is genuinely novel in this space.
- **Importance:** High. Bridging the gap between 20-second benchmarks and real-world multi-minute video retrieval/surveillance is practically relevant.
- **Claims supported:** Moderate. Core comparative claims in Table 1 are undermined by the unspecified baseline inference procedure; ablations (Tables 2–5) and Table 6 are well-supported.
- **Soundness:** Moderate. Method design is principled and internally consistent; the experimental design has the notable gap described above.
- **Clarity:** Good. The method is clearly presented; the evaluation section is thin on procedural detail.
- **Community value:** High. The five extended benchmarks fill a genuine gap, and the code/model release commitment adds reproducibility value.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>