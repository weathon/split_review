- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6
I have now verified all claims against the paper. Let me produce the final consolidated review.

---

## Summary

TempMe proposes a progressive multi-granularity framework for video temporal token merging in text-video retrieval, combining intra-frame token merging (ImgMe, adapted from ToMe) with novel cross-clip and intra-clip merging (ClipMe). The method reduces output tokens by up to 95% relative to parameter-efficient baselines while simultaneously improving accuracy — a combination not achieved by prior token compression methods. Experiments across four benchmarks (MSRVTT, ActivityNet, DiDeMo, LSMDC), multiple backbones (ViT-B/32, ViT-B/16), and training paradigms (parameter-efficient, full fine-tuning, video foundation models) show consistent improvements in both efficiency and retrieval accuracy.

## Strengths

- **95% token reduction with simultaneous accuracy gain across multiple settings.** On MSRVTT with ViT-B/16, TempMe reduces tokens to 1×127 (5% of LoRA's 12×197), cuts GFLOPs by 42% (121.4 vs. 211.3), and raises R-Sum by 5.3 points (206.7 vs. 201.4). This combination of massive token compression *and* accuracy improvement is unprecedented among efficient fine-tuning and token-compression methods (Table 1 & Table 2).

- **Full fine-tuning variant achieves 7.9% R-Sum improvement with 1.57× training speedup and 75.2% GPU memory.** Adding TempMe to CLIP4Clip raises R-Sum from 202.3 to 210.2, reduces training memory from 70.1GB to 52.7GB, and accelerates training by 1.57× (Table 4). This demonstrates the method is not restricted to parameter-efficient settings.

- **Well-designed ablations disentangle the contributions of temporal modeling and token reduction.** Table 7 (function ablation) shows that temporal modeling alone achieves 199.7 R-Sum (54.3 GFLOPs), token reduction alone drops R-Sum to 188.8 (34.7 GFLOPs), and their combination recovers accuracy while maintaining low cost (198.6 R-Sum, 34.8 GFLOPs). This provides clear evidence that the progressive merging design is critical — pure token reduction harms accuracy, but the temporal modeling in ClipMe recovers it.

- **Consistent superiority across four diverse benchmarks.** TempMe outperforms all compared methods on ActivityNet (~6-point R-Sum gain over DGL), DiDeMo, and LSMDC (Table 3), demonstrating generalization beyond a single dataset.

- **Applicability to video foundation models (UMT) with significant efficiency gains.** Plugging TempMe into UMT4Clip achieves 51.1 R@1 (close to UMT's 51.0) while cutting GFLOPs from 210.1 to 111.5 and training time from 4.8h to 3.5h (Table 5).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No statistical variance reported for main retrieval results.** Tables 2 and 3 (the primary comparisons that establish TempMe's superiority) report single numbers without standard deviations or confidence intervals. While single-run reporting is common practice in this field, some of the improvements over strong baselines are modest (e.g., 46.1 vs. 44.6 R@1 over DGL on MSRVTT ViT-B/32), and the reader cannot assess whether these differences are meaningful or could arise from random seed variation. The paper does report 5-run results for the full-fine-tuning experiments (Table 4), which sets a good precedent that should be applied to main results as well.

- **No sensitivity analysis of merging hyperparameters.** The method introduces several key hyperparameters: the per-layer merging rate *r* (2 or 10), the cross-clip retention ratio *R_c*, and the intra-clip retention ratio *R_I*. The paper selects specific values that achieve 95% token reduction but does not analyze how performance and complexity trade off as these parameters vary. A sensitivity sweep would strengthen claims about the method's robustness and help practitioners apply it to new settings. The paper does perform component-level ablations (Tables 6–7), which partially address this, but a direct sweep of the retention ratios is absent.

- **Transparency concern in computational overhead comparison with VoP and DGL (Table 4).** The paper states that "prompt generation in VoP and DGL is omitted when evaluating throughput and complexity" for fairness, because LoRA/DiffRate/ToMe/TempMe can have tunable weights merged at inference. This omission makes VoP and DGL appear more efficient than they actually are in deployment, which makes TempMe's comparison *more conservative* (not inflated). However, the paper should either report the full-cost numbers (including prompt generation) or provide a clearer justification for this omission, since a reader could reasonably expect the reported GFLOPs and throughput to reflect the full inference pipeline.

- **Notation ambiguity in the ClipMe description.** In the intra-clip merging step, the paper compresses $\mathbb{R}^{1 \times N \times D}$ into $\mathbb{R}^{1 \times (N \times R_I) \times D}$, where $N$ here refers to the token count *after* cross-clip merging. However, earlier in the section $N$ is used to denote the token count *before* any merging (within a single frame). The reuse of $N$ across different stages can cause confusion when reading the method.

### Trivial
None.

## Nice-to-Haves
- **Quantify temporal redundancy directly.** A simple analysis (e.g., cosine similarity between corresponding patch tokens in adjacent frames before and after TempMe) would ground the paper's central motivation.
- **Add a baseline using ToMe per frame followed by temporal mean pooling.** This would isolate whether TempMe's improvement comes from the specific progressive merging process or from aggressive aggregation.
- **Discuss failure cases.** When would temporal merging be harmful? Rapid motion, scene cuts, or dynamic backgrounds could cause dissimilar tokens to be merged — acknowledging these would improve credibility.
- **Ablation of merging order.** The paper uses ImgMe then ClipMe. An ablation that swaps this order or applies ClipMe first would test the dependency.

## Removed Points
- **"Unfair comparison with VoP/DGL undermines central claim."** → Removed (and downgraded to the minor transparency concern above). The omission of prompt generation makes the baselines look *more* efficient than they are, not less — this conservative choice strengthens rather than undermines TempMe's efficiency claims. The paper is also transparent about the omission.
- **"Motivation not quantified."** → Removed. Figure 1(a) provides clear visual motivation, and the experimental results themselves validate the temporal redundancy premise. Quantifying it further is a nice-to-have, not a weakness.
- **"UMT4Clip not described in detail."** → Removed. The paper states (p. 10): "we introduce a new baseline UMT4Clip, where UMT handles frames separately." This is sufficient description for a baseline variant.
- **"Qualitative results need quantification."** → Removed. The visualization (Figure 4) is illustrative support, not an evidence claim. It successfully shows that TempMe merges across frames while ToMe does not.
- **"Code release" criticism.** → Removed. The paper states "code will be released" — this is standard practice.
- **"Missing related works."** → Removed per policy (cannot verify external sources).

## Novel Insights
The reviews surface one observation beyond the paper's own contributions: the progressive multi-granularity framework can be seen as learning a hierarchical video representation *implicitly* through token merging — clips at different granularities (single-frame → short clip → full video) correspond to different levels of abstraction. This perspective, which the paper touches on but does not fully develop, suggests that the method may have broader applicability beyond efficiency (e.g., as a way to learn temporally structured representations without explicit temporal modules). The ablation in Table 7 (Temporal Modeling alone achieving 199.7 R-Sum vs. LoRA's 193.0) confirms that the ClipMe design contributes accuracy gains beyond what token reduction alone provides, supporting this view.

## Suggestions
1. Report variance (e.g., standard deviation over 3–5 seeds) for the main retrieval results in Tables 2 and 3.
2. Add a sensitivity analysis sweeping *R_c* and *R_I* to show how performance and GFLOPs trade off.
3. Clarify the notation in the ClipMe section by using distinct symbols for token counts before and after cross-clip merging.
4. Provide the full-cost comparison for VoP and DGL (including prompt generation) either in the main text or supplementary materials to eliminate the transparency concern.
5. Consider adding the ToMe+global-pooling baseline and discussing failure cases to further strengthen the paper.
