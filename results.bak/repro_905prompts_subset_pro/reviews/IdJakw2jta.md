Now I have a thorough understanding of the paper and its positioning. Let me synthesize.

**Round 1 Bracket:** Based on comparison with anchors, the paper falls between roughly 5.0 and 6.5. It's clearly stronger than the 4.60 anchor (AMViT, rejected for marginal gains and limited benchmarks) but has more gaps than the 6.75 anchor (TRACE, accepted with clear methodology and thorough evaluation).

**Round 2 Narrowing:** Compared to the 5.80 anchor (LongVA — criticized for limited novelty, missing training details), our paper has more technical novelty (selective memory strategies, cascaded decoder) and better ablations. Compared to the 6.25 anchors (ARLON — solid but with presentation issues; AntGPT — good methodology), our paper is comparable in contribution level but has the significant gap of unclear baseline inference protocols. The paper is better than 5.80 but the documentation gaps put it slightly below the clean 6.25-6.75 tier. 

**Final Score: 6.0**, borderline Accept.

Here is the final review:

---

## Summary

This paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG), a new problem setting where target spatio-temporal localization must be performed in videos of 1-5 minutes rather than the ~20-second videos used in prior STVG work. The authors propose ART-STVG, an autoregressive transformer that processes video frames sequentially with learnable spatial and temporal memory banks. Key innovations include text-guided spatial memory selection, event-boundary-based temporal memory selection, and a cascaded spatial-to-temporal decoder design. The paper extends the HCSTVG-v2 validation set to five longer-video benchmarks (1-5 minutes) and demonstrates that ART-STVG significantly outperforms existing STVG methods trained on the original short videos, while remaining competitive on short-form benchmarks.

## Strengths

- **First to tackle LF-STVG**: The paper identifies and formalizes a genuine gap in the STVG literature — all prior methods assume short (~20s) videos and process all frames at once, which is ill-suited to minute-scale real-world videos. This is a well-motivated and timely problem direction.

- **Thorough ablation studies**: Tables 2-5 provide clear, well-controlled ablations isolating the impact of selective temporal memory (13.4% m.tIoU gain, Table 2), selective spatial memory, cascaded vs. parallel decoder design (+1.5% m.tIoU, Table 4), and the number of selected spatial memories (Table 5). The ablation of using all temporal memories without selection actually *decreasing* performance (9.6% vs. 16.7% without any memory, Table 2) is a particularly informative result that validates the selection strategy.

- **Large and consistent performance gains across video lengths**: Table 1 shows ART-STVG outperforming all baselines on all five LF-STVG benchmarks, with the performance gap widening as videos get longer (e.g., +0.7% m.tIoU over TA-STVG at 1min vs. +9.1% at 3min vs. +7.3% at 5min). Figure 2 visualizes this trend clearly. The "Baseline (ours)" — a stripped-down version without memory — also consistently underperforms ART-STVG, strengthening the internal validity of the architectural choices.

- **Competitive short-form performance demonstrates generality**: Table 7 shows ART-STVG achieves 59.2 m.tIoU / 39.2 m.vIoU on the original HCSTVG-v2 validation set, only 1.2/1.0 points behind the best specialist model (TA-STVG) and well ahead of the memory-free baseline. This confirms the autoregressive design does not sacrifice short-form capability.

- **Training with longer videos experiment adds practical insight**: Table 6 shows that training all methods on 40-second videos improves performance, and ART-STVG remains best, demonstrating the approach benefits from and is robust to longer training data.

## Weaknesses

### Major

- **Baseline inference protocol on long-form videos is not specified.** The paper compares ART-STVG against TubeDETR, STCAT, CG-STVG, and TA-STVG on videos of 1-5 minutes (Table 1), but does not describe *how* these baselines — which are designed to process all frames simultaneously — were applied to videos 3-15× longer than what they were designed for. Did they process all frames and encounter memory issues? Were frames downsampled? Was a sliding window used? The paper states training used only 20-second videos (line 264-265) for fair comparison, but the inference protocol is left unspecified. The gains in Table 1 are large enough that they are unlikely to be *entirely* an artifact of inference differences, but without this detail, readers cannot fully assess the fairness of the comparison. This directly affects the interpretability of the paper's central experimental result.

- **Dataset extension details are too sparse for reproducibility.** The paper extends the HCSTVG-v2 validation set using original YouTube videos (line 258: "The extensions are based on original YouTube videos, not concatenated clips, and we manually review the extended videos to ensure their quality"), but does not specify: (1) how ground-truth temporal boundaries for the target event were mapped from the original ~20s annotations to the extended 1-5 minute videos, (2) what "manual review" entailed, and (3) any quantitative measures of annotation quality or number of annotators. The dataset is an evaluation-only resource and the basic approach (using real longer source videos) is sound, but these details are needed for the community to trust and build on this benchmark.

- **No computational cost or runtime analysis despite efficiency claims.** The paper motivates the autoregressive design by arguing it "resolves the computational bottleneck" of processing all frames at once (line 90). However, it provides no GPU memory measurements, inference latency data, or scaling analysis to support this claim. Given that efficiency is presented as a key motivation, this omission weakens the practical contribution.

### Minor

- **The loss function is deferred to supplementary material** (line 248: "Due to limited space, please see our loss function in *supplementary material*"). Training details such as loss design are important enough that a brief specification in the main paper would improve readability.

- **The "Baseline (ours)" architecture is also deferred to supplementary material** (line 268-269). Since this baseline serves as the key internal ablation for the memory components, its architecture should be summarized in the main paper.

## Nice-to-Haves

- A computational profiling study (GPU memory vs. video length, latency vs. video length) comparing ART-STVG to prior methods would directly support the efficiency motivation and strengthen the paper.
- A detailed description of baseline inference protocols (frame count, sampling strategy, any windowing/truncation) in the appendix or main text.
- Release of the extended validation sets with documentation of the annotation adaptation process.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The claim that processing all frames at once is an inherent weakness of existing methods is asserted without evidence"** — REMOVED. The paper provides evidence through the experimental results (Table 1, Figure 2) showing existing methods degrade sharply as video length increases, with performance on 3-5 minute videos dropping to near-zero for vIoU@0.7. This is empirical evidence of the claim, not a bald assertion.

- **"Missing related work on long-form temporal grounding (moment retrieval)"** — REMOVED per hard rule: do not mention missing related works.

- **"The paper should discuss whether the video content beyond the target event introduces confounds"** — REMOVED. This is speculative; the paper states they manually reviewed the videos and used original YouTube videos. Without evidence of confounds, this is noise.

- **Strength Finder: "Autoregressive streaming design overcomes computational limitations"** — DEMOTED. This is a claim the paper makes, not a verified strength, since no computational profiling is provided. Reclassified as part of the motivation rather than a demonstrated strength.

- **Strength Finder: "Dataset extension fills a practical evaluation gap"** — RETAINED but caveated. The extension is valuable but the sparse documentation limits its immediate utility.

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs largely confirm the paper's self-assessment of its contributions without adding independent novel observations.

## Suggestions

- **Specify the baseline inference protocol:** For each compared method, state the number of frames processed, any downsampling strategy, whether sliding windows or truncation were used, and peak GPU memory. This single addition would most directly increase the credibility of Table 1.
- **Document the dataset extension:** Include how temporal annotations were adapted from the original HCSTVG-v2, the manual review criteria, and example statistics (e.g., distribution of target event positions within the extended videos).
- **Add a computational efficiency figure:** A plot of inference latency or GPU memory vs. video length for ART-STVG vs. one or two representative baselines would strongly support the efficiency claims with minimal additional experiments.

## Score and Decision

**Anchor comparison summary (all rounds):**
- `bEvI30Hb2W` (LVM-NET, 3.00, R1): much weaker — marginal gains, limited benchmarks, rejected. Our paper is substantially stronger.
- `hWlCc7Iksi` (ARVideo, 3.40, R1): weaker — different task, rejected. Not a close comparison.
- `1DEHVMDBaO` (AMViT, 4.60, R1+R2): similar topic (memory for long video) but weaker — marginal gains, only 2 benchmarks, poor ablations. Our paper has much more comprehensive experiments and larger gains.
- `O8FkMqNF1M` (Language Repository, 5.50, R1): somewhat relevant but different task. Our paper has stronger ablations.
- `QETk0lBdVf` (LongVA, 5.80, R2): comparable in having documentation gaps, but our paper has more technical novelty (selective memory strategies, cascaded decoder vs. "use longer context LLM"). Our paper is slightly stronger.
- `8pusxkLEQO` (ARLON, 6.25, R2): comparable in contribution level. Our paper has similar strengths (novel architecture) and weaknesses (some missing details).
- `Bb21JPnhhr` (AntGPT, 6.25, R2): comparable. Similar novelty level.
- `14fFV0chUS` (TRACE, 6.75, R1+R2): stronger — accepted with cleaner methodology. Our paper has more significant documentation gaps (baseline protocol, dataset details) that TRACE doesn't have.
- `wkbx7BRAsM` (VidIT, 7.00, R1+R2): stronger — accepted with novel zero-shot phenomenon. Our paper's gaps pull it below this tier.

**Round 1 bracket:** 5.0–6.5.
**Round 2 narrowing:** The paper sits between the 5.80 anchor (LongVA, which has similar documentation gaps but less novelty) and the 6.25 anchors (which have cleaner evaluations). Final placement: **6.0**, given the genuine novelty, strong ablations, and large performance gains, tempered by the three major documentation/analysis gaps.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>