Now I have thorough context. Let me produce the final consolidated review.

## Summary

This paper introduces ART-STVG, the first framework for Long-Form Spatio-Temporal Video Grounding (LF-STVG). The core innovation is an autoregressive transformer that processes video frames sequentially (rather than all-at-once), augmented by spatial and temporal memory banks with selective retrieval strategies and a cascaded spatio-temporal decoder. The paper also contributes five extended benchmarks (LF-STVG-1min through 5min) built from HCSTVG-v2's source videos. Experiments show consistent and growing improvements over existing methods as video length increases.

## Strengths

1. **First work on long-form STVG with a well-motivated architecture.** The paper correctly identifies that existing STVG methods cannot scale to minute-long videos due to their all-at-once processing nature, and proposes a natural solution: streaming frame input processed autoregressively. This is a principled design choice for the task.

2. **Consistent and growing performance advantage across all video lengths.** Table 1 shows ART-STVG outperforms all prior methods at every length (1–5 min), with the gap widening on longer videos. On LF-STVG-3min, ART-STVG achieves m.tIoU 23.0% vs. the next best 14.2% (TA-STVG); on LF-STVG-5min the gap is 15.0% vs. 8.1%. The trend is consistent and monotonic across five benchmarks, not an isolated spike.

3. **Ablation evidence cleanly validates each design component.** Table 2 shows that using all temporal memories degrades performance (9.6% m.tIoU vs. 16.7% with no memory), while the proposed selection strategy recovers and exceeds both (23.0%). This is not a design flaw — it demonstrates that the selection mechanism is essential. Table 3 (spatial memory selection) and Table 4 (cascaded vs. parallel decoding) similarly isolate and validate each component's contribution.

4. **Attention visualization provides complementary qualitative evidence.** Figure 5 shows that with selective spatial memory, attention maps concentrate on the target region (the white-haired man), while without selection they are diffuse. This grounds the quantitative gains in an observable mechanism.

5. **Competitive on short-form STVG while designed for long-form.** On the original HCSTVG-v2 benchmark, ART-STVG achieves 59.2 m.tIoU vs. the SOTA 60.4 (TA-STVG), demonstrating that the long-form design does not sacrifice short-form performance.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Baseline inference protocol on long videos is under-described.** The paper evaluates existing methods (TubeDETR, STCAT, CG-STVG, TA-STVG) on 1–5 minute videos, which at 3.2 FPS would require processing 192–960 frames simultaneously — far beyond what these models were designed for. The paper states baselines were run using "their provided source codes" but does not describe whether frame subsampling, tiling, gradient accumulation, or other modifications were used. This makes it harder for readers to assess the fairness of comparison. The large and consistent gap across all lengths mitigates concern, but the protocol should be documented.

2. **Ablations reported only on LF-STVG-3min.** All ablation studies (Tables 2–5) are conducted on a single benchmark length. While 3 minutes is a reasonable middle point, reporting key ablations (especially the cascaded decoder and memory selection) on at least one other length (e.g., 1 min and 5 min) would strengthen confidence in the design choices' generality.

3. **No error bars or significance tests.** Performance differences in some ablations are small (e.g., Table 5: 22.7 vs. 23.0 vs. 22.5 for different `N_s` values). Without standard deviations or multiple runs, it is unclear whether these differences are meaningful.

4. **"Baseline (ours)" architecture description deferred to supplementary.** The baseline used to isolate the memory contribution is described as having a "similar architecture to our ART-STVG but without memory and memory selection modules" and is relegated to the supplementary material. A brief architectural description in the main paper would improve readability.

### Trivial
None.

## Nice-to-Haves

- Reporting the impact of autoregressive error accumulation (e.g., prediction accuracy on first vs. last 20 seconds of a 5-minute video) would strengthen the robustness analysis.
- Visualizing temporal memory selection behavior (e.g., which event segments are selected at different time steps) would complement the existing spatial attention visualization in Figure 5.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic #1 (benchmark annotations "not properly defined" / "invalidating all experimental results"):** This criticism is factually incorrect. The LF-STVG benchmarks extend the source YouTube videos to their original lengths (1–5 minutes) rather than concatenating clips. The ground-truth annotations from the original HCSTVG-v2 20-second clips describe a specific event that still occurs at the same temporal position within the longer video. Evaluating whether a model can locate that event in a longer context is precisely the intended evaluation. The claim that "all tables and figures reporting m.tIoU... are uninterpretable" does not hold — the relative comparison between methods is valid, and the annotations are meaningful. Removed as factually wrong.

- **Harsh Critic #3 (memory failure as "pathological design flaw"):** The claim that a 42% relative drop when using *all* memories indicates a "design flaw" misunderstands the purpose of the ablation. Using all (unselected) temporal memories introduces irrelevant event information, which predictably hurts performance. The ablation cleanly demonstrates that the selection mechanism is essential — this is a valid experimental finding, not a flaw. The critic's framing of this as "the solution feels ad-hoc" is unjustified; the TextTiling-inspired selection strategy is well-motivated and validated. Removed as a misinterpretation.

- **Strength Finder strength about benchmark creation ("fills the gap in long-term benchmarks"):** While the benchmark contribution is real, the description of "manual review" is vague on annotation specifics. The strength is retained but the concern about clarity is captured in the Minor weakness section.

- **General complaints about missing related work, appendix content, formatting.** Removed per instructions (parser issues, scope outside verification).

## Novel Insights

None beyond the paper's own contributions. The reviews surface no genuinely novel observation about the paper that its authors did not already articulate. One observation worth noting: the paper's ablation showing that *all* temporal memories hurt performance (9.6% vs. 16.7% without any memory) is an unusually stark demonstration that naive memory augmentation can backfire in long-form settings, and reinforces that memory *selection* — not just memory — is the critical design choice. This is a useful methodological lesson for any future work on memory-augmented video understanding.

## Suggestions

1. Add a paragraph (or a short subsection) describing how existing methods were run on 1–5 minute videos: frame sampling rate, any tiling or chunking strategies, GPU memory consumption, and whether modifications were made to official codebases. This is the single most important clarification for experimental reproducibility.

2. Report key ablations (at least memory selection and cascaded decoder) on LF-STVG-1min and LF-STVG-5min in addition to LF-STVG-3min, to demonstrate consistency across lengths.

3. Include error bars (standard deviations over multiple runs or seeds) for the main results and key ablations.

4. Briefly describe the "Baseline (ours)" architecture (1–2 sentences) in the main paper rather than deferring entirely to the supplementary.

## Score and Decision

**Anchor calibration:**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| TA-STVG (WOzffPgVjF) — *Knowing Your Target: Target-Aware Transformer* | 7.50 | Directly comparable (same base task, same datasets). TA-STVG has cleaner evaluation on standard benchmarks; this paper tackles a harder problem (long-form) with its own novel contributions. Similar quality level. |
| ARLON (8pusxkLEQO) — *Boosting Diffusion Transformers with Autoregressive Models for Long Video Generation* | 6.25 | Different task but similar "long video + autoregressive" framing. ARLON has more competitive results on some metrics; this paper has cleaner ablation evidence for its components. Slightly stronger on evidence quality. |
| CoSPaL (yHj6EunfVQ) — *Contextual Self-paced Learning for Weakly Supervised STVG* | 5.50 | Same general domain (STVG). CoSPaL has more uneven supporting evidence and technical clarity concerns. This paper is stronger. |
| Adaptive Memory (1DEHVMDBaO) — *AMM for Long-form Video Understanding* | 4.60 | Similar memory-bank approach for long videos but with marginal improvements and limited baselines. This paper has stronger experimental evidence and cleaner ablations. |
| Grounded Video Caption (xYzOkOGD96) | 3.83 | Overclaimed novelty, insufficient comparisons, fundamental fairness concerns. This paper is substantially stronger. |
| Harry Potter OOD (3ZdGSTxKuy) | 2.00 | Minimal novelty, flawed experimental setup. This paper is orders of magnitude stronger. |

**Assessment:** The paper makes a genuine contribution — it is the first to systematically address long-form STVG, with a well-motivated architecture, strong ablations, and consistent experimental results across five benchmarks. The weaknesses are about missing experimental details, not fundamental validity. This places it above papers with marginal or overclaimed contributions (~4–5) but below flawless, game-changing work (~9–10). The closest anchor is TA-STVG (7.50), which has similar contribution ambition and evidence quality but works on a more standard task.

**Score: 7.0**

**Decision: Accept**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>