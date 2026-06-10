## Summary

This paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG), a new problem setting that extends STVG from ~20-second clips to 1–5 minute videos. The authors propose ART-STVG, an autoregressive transformer that processes frames sequentially with spatial and temporal memory banks and a cascaded decoder design. On extended HCSTVG-v2 benchmarks, ART-STVG outperforms prior methods (TubeDETR, STCAT, CG-STVG, TA-STVG) across all video lengths, with the gap widening from +0.7% m.tIoU at 1 minute to +7.3% at 5 minutes, while remaining competitive on short-form STVG.

## Strengths

- **ART-STVG shows large and monotonically widening gains over all prior methods as video length increases (Tab. 1).** At 1 minute the lead over TA-STVG is 0.7% m.tIoU; at 5 minutes it grows to 7.3%. The same trend holds for m.vIoU and vIoU@R. This directly supports the core claim that the autoregressive streaming design is better suited for long videos.

- **Memory selection is convincingly shown to be *necessary*, not just helpful (Tab. 2).** Including all temporal memories *degrades* performance from 16.7% to 9.6% m.tIoU, while the text-tiling-inspired selection recovers to 23.0% — a 13.4-point swing. This cleanly validates the design rationale rather than merely showing an incremental gain.

- **The cascaded spatio-temporal decoder is cleanly ablated (Tab. 4),** yielding a 1.5% m.tIoU improvement over the parallel design. The paper also ablates spatial memory selection (Tab. 3, +0.9%) and the number of selected spatial memories (Tab. 5), providing a thorough understanding of each component.

- **The paper formulates LF-STVG as a new practically motivated problem and creates the first benchmarks for it,** filling a genuine gap between existing STVG datasets (20–35s) and real-world video durations. This provides a foundation for future work on long-video grounding.

- **Training on longer videos helps all methods, but ART-STVG maintains its advantage (Tab. 6).** When all methods are trained on 40-second videos (vs. the default 20s), ART-STVG reaches 28.3% m.tIoU on LF-STVG-3min versus 21.0% for the next best (STCAT), ruling out the explanation that ART-STVG simply benefits more from longer training.

## Weaknesses

### Fatal
None.

### Major

- **The annotation protocol for the extended LF-STVG datasets is critically underspecified.** The paper states only: "we manually review the extended videos to ensure their quality" (lines 199–200). It does not clarify (a) whether new temporal event boundaries were annotated for the extended videos or whether the original 20-second HCSTVG-v2 intervals were reused as ground truth, (b) what spatial (bounding box) annotations exist for frames outside the original 20-second segment in the 1–5 minute videos, or (c) how manual review ensured annotation quality (e.g., inter-annotator agreement). Since the quantitative results in Table 1 are the primary evidence for the paper's claims, the reader needs to know exactly what the ground-truth covers. Without this, the evaluation cannot be fully interpreted or reproduced. This is the single most significant weakness.

- **The paper does not disclose how existing STVG baselines were adapted to run on long videos.** Methods like TubeDETR and TA-STVG process all frames at once and likely cannot fit 960 frames (5 min @ 3.2 FPS) on a single GPU. The paper does not specify whether baselines subsampled frames, used sliding windows, reduced resolution, or employed other adaptations. This leaves a confound: part of ART-STVG's advantage at longer lengths could stem from feasibility constraints (baselines cannot process full-resolution long videos) rather than architectural superiority. A control experiment — e.g., giving baselines a comparable per-step frame budget — would substantially strengthen the central claim.

### Minor

- **No variance or statistical significance is reported.** All results in Tables 1–7 are single numbers without standard deviations, confidence intervals, or any measure of variability. Some improvements are modest (e.g., +0.7% m.tIoU at 1 minute), and with ~2,000 validation samples per benchmark, it is impossible to assess reliability. While this is common practice in STVG papers, it matters more here because the LF-STVG benchmarks are new and non-standard.

- **Inconsistent metric naming between Figure 2 and Table 1.** The Figure 2 caption mentions "m_Ap@1" and "m_Ap@5", but Table 1 reports m.tIoU, m.vIoU, and vIoU@R. The paper should clarify whether these are the same metrics under different names, or distinct evaluations.

### Trivial
None.

## Nice-to-Haves

- Ablations across multiple video lengths (currently only LF-STVG-3min) would show whether design choices generalize. The current setup leaves open the question of whether the same ablation patterns hold at 1 min and 5 min.
- A limitations section discussing why absolute performance at 5 minutes (15% m.tIoU) is still low would strengthen the paper's framing.
- Discussion of memory growth/bounding strategies for very long (e.g., hour-long) videos, since the current memory banks grow without bound.

## Removed Points

These points were raised in the inputs but removed or downgraded after verification against the paper:

- **"Autoregressive baseline (without memory) is worse than existing methods, undermining the narrative"** (Harsh Critic Issue 3): The baseline is an ablation, not a proposed method. The paper never claims the autoregressive architecture alone is superior — the full ART-STVG includes memory. Removing the memory components and showing worse performance is a standard ablation design that strengthens, not weakens, the paper.
- **"Zero-initialized queries are a weakness"**: Standard practice in DETR-style architectures; not a flaw.
- **"Loss function deferred to supplementary"**: Common practice at this venue to save space.
- **"Why not learnable attention instead of hard selection"**: A reasonable design alternative, not a weakness. The paper's selection mechanism is a deliberate design choice that is ablated and shown to work.
- **"The paper should train on longer videos (2–5 minutes)"**: The paper already shows training on 40-second videos helps (Tab. 6). Training on longer videos would require a non-trivial annotation effort and is beyond scope.
- **"Memory growth is problematic for hour-long videos"**: A valid concern but speculative — the paper evaluates on up to 5 minutes, and addressing hour-long videos is beyond the paper's scope. Moved to Nice-to-Haves.
- **Generic strengths from Strength Finder**: Dropped strengths that were generic ("addresses an important problem," "a reasonable first approach") or conflicted with verified weaknesses.
- **"Missing related works"**: Cannot be verified without external sources; removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The review process surfaces that the paper's most striking empirical finding — that adding *all* temporal memories *harms* performance (Tab. 2, ❷→❸), requiring active selection for any benefit — is not discussed as a fundamental limitation of the cross-attention mechanism. This observation could motivate future work on why attention over many memories fails and whether learnable weighting could replace hard selection.

## Suggestions

1. **Clarify the annotation protocol in full.** State explicitly: (a) what ground-truth temporal intervals and spatial boxes cover in the extended videos, (b) whether any new annotations were created for frames outside the original 20-second clip, and (c) what quality assurance steps were taken (e.g., inter-annotator agreement statistics).
2. **Disclose baseline inference details.** For each baseline and each video length, report: number of frames processed, resolution, whether any subsampling/chunking/sliding-window strategy was used, and whether the method fit on the same GPU as ART-STVG.
3. **Add variance estimates.** Report results over multiple runs or at minimum state the evaluation protocol (single-run vs. multi-run). For the marginal 0.7% gain at 1 minute, this is essential.
4. **Reconcile the metrics in Figure 2 and Table 1.** Clarify whether "m_Ap@1/m_Ap@5" is the same as or different from the metrics reported in Table 1.
5. **Add a limitations paragraph** acknowledging the low absolute performance on longer videos (15% m.tIoU at 5 minutes) and discussing when the approach would fail.

## Score and Decision

**Calibration report:**

*Round 1 bracket:* ~6.0–7.0, based on initial comparison to similar papers.

*Anchors retrieved:*

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|------------------------|
| hWlCc7Iksi.md (ARVideo) | 3.40 | R1-low | Far weaker; rejected for limited contribution |
| MI0UiWeqOl.md (Poly-AR) | 2.33 | R1-low | Not comparable; different task |
| BwQUo5RVun.md (Weakly supervised grounding) | 3.00 | R1-low | Far weaker; limited methodology |
| YGWxpOI6Y0.md (VideoGPT+) | 3.40 | R1-low | Far weaker |
| wkbx7BRAsM.md (Zero-shot Video Imitators) | 7.00 | R1-mid | Comparable; accepted, slightly higher novelty |
| xYzOkOGD96.md (Grounded Video Caption) | 3.83 | R1-mid | Weaker; rejected for overclaiming novelty |
| 8pusxkLEQO.md (ARLON) | 6.25 | R1-mid | Comparable; accepted. My paper has stronger ablations |
| 14fFV0chUS.md (TRACE) | 6.75 | R1-mid | Most relevant anchor. TRACE has similar strengths; my paper has stronger problem formulation but weaker method novelty |
| 9Cu8MRmhq2.md (Multi-granularity Corr.) | 8.00 | R1-high | Stronger than my paper; not directly comparable |
| 2dnO3LLiJ1.md (ViT Registers) | 8.00 | R1-high | Stronger; different domain |
| QWDFOOoV3U.md (ResidualViT) | 5.75 | R2 | Weaker; rejected, weaker problem formulation |
| exKHibougU.md (LVD) | 6.00 | R2 | Comparable; similar score level |
| QETk0lBdVf.md (Long Context Transfer) | 5.80 | R2 | Weaker; rejected for limited technical contribution |
| XYdstv3ySl.md (3D Spatial Memory) | 6.50 | R2 | Comparable; accepted. Different task |
| le4IoZZHy1.md (CG-Bench) | 6.20 | R2 | Comparable; accepted. Similar weakness profile (missing dataset construction details) |
| a1P5kh2oo8.md (Vinoground) | 5.75 | R2 | Weaker; rejected for limited novelty |
| fCi4o83Mfs.md (TVBench) | 6.75 | R2 | Comparable; accepted. Stronger benchmark contribution |
| liuqDwmbQJ.md (ViLMA) | 6.00 | R2 | Comparable; accepted. Similar level of contribution |

*Narrowing:* Round 2 anchors place comparable papers (CG-Bench 6.20, LVD 6.00, ARLON 6.25, TRACE 6.75) in the 6.0–6.75 range, all accepted. My paper sits near the lower end of this range due to the underspecified annotation protocol and undisclosed baseline adaptation — two evaluation-gap issues that need resolution. It is clearly stronger than the rejected anchors (5.75–5.80) which suffered from novelty or technical depth problems my paper avoids.

**Final score: 6.0**

This reflects a weak accept. The paper formulates a genuinely new problem, proposes a well-designed method with thorough internal ablations, and demonstrates consistent empirical gains. However, the evaluation is compromised by two significant exposition gaps: the annotation protocol for the extended datasets is not specified, and the inference setup for baseline methods is not disclosed. These are fixable in revision but prevent a higher score in the current form.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>