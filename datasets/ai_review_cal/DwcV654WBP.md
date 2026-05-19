- Decision: Reject
- Avg Score: 6.50
- Scores: 5, 8, 5, 8
Now I have a thorough understanding of the paper content. Let me synthesize the consolidated review.

---

## Summary

This paper identifies a previously under-explained degradation in video representations learned from CLIP-based video models: end-to-end fine-tuning of the text encoder on ASR transcripts causes it to overfit to transcript-specific language styles, distorting the supervision signal for the video encoder. The proposed fix—partially freezing the text encoder's shallow layers while keeping deep layers tunable—is simple, well-motivated, and effective. The resulting TVTSv2 models (up to 1B parameters) achieve state-of-the-art zero-shot retrieval and action recognition with frozen backbones, surpassing methods trained on more data or modalities.

## Strengths

- **Controlled empirical diagnosis of the degradation source (Table 1):** The paper systematically isolates the text encoder as the cause of performance loss. The ablation chain (M₁-FT → M₂-FT → M₂-FF → M₂-PF) convincingly shows that neither simply adding alt-text (M₂-FT) nor fully freezing the text encoder (M₂-FF) solves the problem, while partial freezing (M₂-PF) yields a dramatic improvement (MMS 0.340 vs. CLIP's 0.295, vs. M₂-FT's 0.234). This is a clean, replicable experimental design that directly supports the paper's central claim.

- **State-of-the-art results with frozen backbones across multiple benchmarks:** TVTSv2-H/14 achieves absolute SOTA on MSR-VTT (R@1 41.3 with DSL), DiDeMo (R@1 39.5), and LSMDC (R@1 20.0) for zero-shot retrieval, and on HMDB-51 (52.1), UCF-101 (78.0), K400 (59.6), and SSV2-MC (48.4) for zero-shot action recognition — all with a **frozen backbone** that supports out-of-the-box feature extraction. These results beat methods that use additional modalities (ImageBind's audio) or task-specific fine-tuning.

- **Scalable training enabling billion-parameter models:** The combination of tube masking (ρ≥50%) with the transcript sorting objective makes training a 1B-parameter model feasible on 80 V100 GPUs in one week. The ablation on masking ratio (Figure 2a) provides practical guidance for the efficiency-performance trade-off.

- **Clear differentiation from prior work:** The paper explicitly shows why CLIP-ViP and ActionCLIP degrade (overfitted text encoder) and why its solution differs from parameter-efficient tuning approaches that focus only on the visual side.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The text encoder overfitting claim lacks direct behavioral evidence.** The paper's thesis is that end-to-end tuning of the text encoder causes it to "overfit in terms of styles" and "lose its original generalization ability to capture the semantics of various language registers" (lines 9–10, 49–50). However, the evidence is entirely indirect: degraded downstream metrics under full fine-tuning and recovery under partial freezing. No direct analysis of the text encoder's representations is presented — no cosine similarity comparison of frozen vs. tuned text encoder outputs on held-out captions, no zero-shot text retrieval on out-of-domain queries, no probing of vocabulary coverage or style robustness. An alternative explanation consistent with the data is that partial freezing acts as a regularizer that prevents the text encoder from fitting noise, without any "preservation of generalization" mechanism being at play. Adding a direct analysis (e.g., measuring output similarity to original CLIP on varied-style inputs) would turn a plausible hypothesis into a verified mechanism. As it stands, the causal claim is under-supported, though the empirical result is clear.

- **The headline absolute-SOTA claim mixes DSL and non-DSL comparisons.** In Table 2, Ours-H/14† (with DSL post-processing) achieves 41.3 R@1 on MSR-VTT, underlined as absolute SOTA, while InternVideo (the closest competitor at 40.0) is reported without DSL. The paper does mark DSL results with † and states "using post-processing techniques like DSL further boosts performance" (line 413), and non-DSL results are also reported (Ours-H/14 at 38.2). However, the underlined SOTA claim relies on a technique not applied to the comparison baseline. This is a clarity issue rather than a deceptive omission — the non-DSL numbers are transparently available — but it means the strongest advertised result should be contextualized. Narrowing the primary comparison to non-DSL results or applying DSL uniformly would eliminate ambiguity.

- **Zero-shot action recognition comparison (Table 3) omits relevant contemporary baselines.** InternVideo — cited as a main competitor in the abstract and retrieval results — reports zero-shot K400 accuracy in its own paper (~58% for similar model sizes) but is absent from the zero-shot action recognition table. Similarly, for linear probing (Table 4), UMT is not included despite being a recent CLIP-based video model with language supervision. While the reported results are still strong against the included baselines, adding these comparisons would directly substantiate the SOTA claim and remove an easily-addressed gap in the evidence.

- **Ablation on tunable layers (Figure 2b) reports only a coarse sweep.** The ablation sweeps L_tune ∈ {0, 3, 6, 9, 12}, which amounts to four data points between the two extremes (fully frozen and full fine-tune). While the trend is clear, a finer-grained sweep (e.g., L_tune = 1, 2, 4, 5, etc.) would more precisely characterize the optimal freezing ratio and better support the heuristic of freezing the "first three-quarters."

- **Reproducibility: several training hyperparameters are missing from the main paper.** The implementation details (lines 403–408) specify the temperature (0.05), K=4, T=12, masking ratios, and input resolution, but do not report learning rate, optimizer, batch size, number of training steps, or learning rate schedule. Some of these may reside in the (stripped) appendix, but the core paper would benefit from at least stating the learning rate and batch size.

### Trivial

- In Table 1, the column headers "M₁" and "M₂" are defined only in the caption rather than in the table itself, requiring cross-referencing. A clarifying row header or footnote would improve readability.
- The "three-quarters frozen" description (line 196) is mathematically correct (freeze 9/12 layers → tune last quarter), but adding an explicit "(i.e., 3 of 12 layers tunable)" would prevent the misreading that occurred in review.

## Nice-to-Haves

- An ablation exploring alternatives to the binary stop-gradient choice (e.g., weaker gradient scaling for the text encoder) could deepen understanding of why the stop-gradient is specifically necessary (Table 5).
- Including linear probing results on SSV2 would further demonstrate temporal feature quality.
- Providing inference FLOPs alongside parameter counts would help readers assess efficiency more fully.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"Contradiction between 'three-quarters frozen' and ablation results"** — Removed because it is factually wrong. The paper states "freeze the first three-quarters of layers" (line 196), meaning 9 of 12 layers frozen (3 tunable). The ablation sweeps L_tune (tunable layers counting from the last layer), so L_tune=3 matches exactly. The critic misread "freeze three-quarters" as "tune three-quarters."

2. **"Wrapped table formatting makes it hard to read"** — Removed as a parser artifact. The original PDF would render the wrapped table correctly.

3. **"Column headings incomplete for M₁/M₂"** — Removed; the caption defines M₁ and M₂, which is standard practice for tables with constrained width.

4. **"Missing related works"** — Removed per instructions; cannot verify external completeness.

5. **"Reproducibility: undisclosed hyperparameters in appendix"** — Removed because the appendix was stripped by the parser. Reviewer notes about missing training details from the main paper are retained as a Minor weakness (learning rate, batch size) but elaborated speculation about appendix content is removed.

6. **"Generic 'could add more models / larger dataset' comments"** — Removed where they lacked a specific baseline to add.

7. **Strength Finder claims about "importance of the problem"** — Generic/superficial; removed.

## Novel Insights

None beyond the paper's own contributions. The key observation — that text encoder overfitting (not visual encoder overfitting) drives degradation in video CLIP-based models, and that shallow-layer freezing resolves it — is the paper's own insight and is already well-articulated. The reviews did not surface a genuinely novel interpretation beyond what the paper presents.

## Suggestions

1. Add a direct analysis of text encoder behavior: compute cosine similarity between original CLIP text encoder outputs and tuned encoder outputs on captions with varied styles (formal, colloquial, ASR-like). Show that full fine-tuning degrades similarity more than partial freezing. This would directly verify the claimed mechanism.
2. Include InternVideo and UMT in the zero-shot action recognition table (Table 3) to strengthen the SOTA claim.
3. Either restrict the "absolute SOTA" underline in Table 2 to non-DSL results or note that the baseline (InternVideo) does not use DSL. The current practice († marking DSL, reporting both numbers) is transparent, but the underlining of a DSL-assisted number as absolute SOTA invites confusion.
4. Clarify the "freeze the first three-quarters" heuristic by stating the exact number of tunable layers (e.g., "3 out of 12 layers") to avoid ambiguity.
5. Report key training hyperparameters (learning rate, batch size, optimizer, training steps) in the main paper.
