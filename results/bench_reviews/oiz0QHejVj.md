Now I have a thorough understanding of the paper and calibration anchors. Let me write the final review.

---

## Summary

CLIP-Map proposes a **mapping-based** alternative to the dominant **select-based** paradigm for CLIP model compression. Instead of pruning parameters and retraining, the method learns Kronecker-factored transformation matrices that map a large pretrained CLIP model into a smaller one via matrix multiplication (width compression) and linear layer combinations (depth compression). A **Diagonal Inheritance Initialization** scheme preserves pretrained weight structure and stabilizes optimization. The mapped model is then retrained with knowledge distillation. The paper demonstrates competitive or better zero-shot retrieval and classification performance compared to TinyCLIP at matched parameter counts, while requiring fewer training epochs.

## Strengths

- **Novel paradigm shift from select-based to mapping-based compression**: The paper reframes CLIP compression as learning transformations that preserve pretrained information rather than discarding parameters. This is a conceptually clean and well-motivated inversion of model-growth techniques like LiGO, applied to the compression direction. Table 1 shows CLIP-Maptiny (1.0% size) achieves 15.8 TR@1 on MSCOCO vs. 10.5 for TinyCLIP of identical parameter count.

- **Diagonal Inheritance Initialization is simple, theoretically motivated, and empirically decisive**: The variance analysis (Eqs. 5–8) explains why random/Kaiming/Xavier initialization of Kronecker factors causes distribution shifting and optimization failure. The diagonal initialization fixes this cleanly. Table 5 quantifies the dramatic impact: mapping-stage accuracy jumps from 4.4% (Kaiming) to 28.9% (Diag Init) on ImageNet-1K, and the loss curves (Fig. 6) confirm faster, more stable convergence. This is a genuine insight applicable beyond this paper.

- **Significantly reduced training cost**: Table 11 shows CLIP-Maptiny completes in 21h50m (5 mapping + 25 retraining epochs) vs. TinyCLIP's 49h33m (3-stage progressive, 75 epochs). The mapping stage replaces expensive multi-stage progressive compression with a single 5-epoch optimization of lightweight mapping matrices. This efficiency argument is well-supported and practically meaningful.

- **Unified width and depth compression in a single differentiable pipeline**: Both dimensions are handled simultaneously via Kronecker-factored width mappings and learned linear layer combinations for depth, reducing engineering complexity compared to multi-stage pruning pipelines.

- **Generalizability demonstrated across architectures and pretrained weights**: Results are shown for ViT-based and ResNet-based vision encoders, and for OpenCLIP and MetaCLIP teacher models, indicating the approach is not tightly coupled to one backbone.

## Weaknesses

### Fatal

None.

### Major

- **Table 6 contains a contradictory architectural specification for CLIP-Maptiny**: The table lists CLIP-Maptiny's vision encoder as width=512, depth=12, with 0.8M parameters. A ViT at width=512 and depth=12 would have approximately 37M parameters, not 0.8M — and the reported 0.21 GFLOPs (Table 12) is also incompatible with this architecture. The correct dimensions are presumably closer to TinyCLIP's width=128, depth=4, but the table was not updated. This is a documentation error rather than evidence of fraudulent experiments (the param counts and FLOPs are internally consistent), but it creates genuine confusion about what architecture was actually evaluated and undermines trust in the reported configurations.

### Minor

- **"Manual Drop" baseline in Table 4 is never defined**: The mapping-duration ablation includes a "Manual Drop (0 epoch)" entry with 41.1% IN-1K accuracy, but the paper does not describe how this subnetwork is selected. Without this description, the reader cannot interpret what this baseline actually tests or how it relates to the mapping approach.

- **Multi-head attention and architectural details are underspecified**: Section 3.2.2 and Appendix A.3 describe how F matrices are applied to attention and FFN weight blocks, but the paper does not clarify whether the number of attention heads changes, how LayerNorm parameters are handled, or how residual connections are affected after dimension reduction. These are standard operations in this line of work and can be inferred, but explicit discussion would improve reproducibility.

- **Non-TinyCLIP comparisons rely on numbers from original papers with different training setups**: Table 3 compares against MoPE-CLIP, CLIP-KD, and MobileCLIP, and Appendix Table 7 against UPop, EfficientVLM, and DynaCLIP, but these are cited from the original papers where datasets, teacher models, and training budgets differ. The paper acknowledges this limitation (A.4). This weakens the strength of the cross-method comparison but does not invalidate the direct TinyCLIP comparison, which is the paper's primary empirical claim.

- **The loss-weighting ablation (λ=1.0) is conducted only on CC3M with CLIP-Mapsmall**: The finding that λ=1.0 is optimal is then applied to all experiments (YFCC-15M, all model sizes). While λ=1.0 (pure distillation) is a common and reasonable default, the ablation does not demonstrate that the finding generalizes across datasets and model scales. This is a minor concern since pure distillation is a standard choice.

### Trivial

- None worth noting beyond the parser-related formatting artifacts present in the extracted text.

## Nice-to-Haves

- **A deterministic low-rank compression baseline** (e.g., truncated SVD of each weight matrix) would directly test the value of learned mapping over a static optimal projection. The paper's core claim that mapping preserves information better than selection would be strengthened by showing that the learned mapping matters, not just the low-rank structure.

- **Analysis of what the learned F matrices converge to** (e.g., comparing their structure to the SVD of the original weights) would provide insight into whether the mapping stage discovers a genuinely different compression strategy or simply approximates a standard subspace projection.

- **Scaling experiments on larger datasets** (LAION-2B, DataComp-1B) to test whether the mapping-retraining pipeline remains beneficial with stronger teachers. The authors acknowledge this as future work (A.9).

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Harsh critic's claim that "none of the experimental claims can be taken at face value" due to the Table 6 error** — REMOVED as overstatement. The Table 6 error is a genuine documentation problem (moved to Major), but the param counts and FLOPs are internally consistent across all tables, and the comparison against TinyCLIP at matched sizes establishes credibility for the core results. The error affects clarity, not experimental validity.

2. **Harsh critic's claim that the only select-based competitor is TinyCLIP** — REMOVED as factually incorrect. The paper also compares against MoPE-CLIP, CLIP-KD, UPop, EfficientVLM, DynaCLIP, and MobileCLIP (Tables 3, 7). The criticism about cross-paper comparison setups is valid and retained as Minor.

3. **Harsh critic's claim about "no non-learned mapping baseline" making it impossible to demonstrate superiority of mapping over selection** — REMOVED as scope creep. The paper's primary claim is mapping vs. selection (not learned vs. non-learned mapping). The Diagonal Inheritance initialization itself functions as a non-learned mapping baseline (zero mapping epochs). The SVD suggestion is moved to Nice-to-Haves.

4. **Strength Finder claims about "thorough ablation studies" and "generalizability across architectures" that are generic** — Qualified rather than removed. The ablations are mostly thorough but the Manual Drop issue weakens this somewhat. The generalizability claim is supported by the ViT/ResNet results.

5. **Harsh critic's formatting and typo complaints** — REMOVED per hard rules; these are parser artifacts.

6. **Harsh critic's note about the Kronecker factorization being "standard"** — REMOVED. Even if standard in other contexts, its application to CLIP compression with diagonal initialization is the novel contribution.

## Novel Insights

The most genuinely novel insight from this work is that **the distribution-shifting problem caused by Kronecker-factored mappings can be elegantly solved by diagonal initialization, which simultaneously provides weight inheritance from the pretrained model**. This is not just an engineering trick — the variance analysis (Eqs. 5–8) provides theoretical grounding, and the empirical gap (4.4% → 28.9%, Table 5) is large enough to suggest this is a fundamental observation about Kronecker-structured transformations in neural networks. The insight bridges model growth literature (LiGO, LeTs) with model compression, revealing that the mapping direction can be reversed if the initialization problem is properly addressed.

## Suggestions

- **Fix Table 6**: The CLIP-Maptiny architecture dimensions should be updated to match the actual model evaluated (likely width=128, depth=4 for vision, matching the 0.8M parameter count). All three model variants in that table should be double-checked for consistency between reported dimensions, parameter counts, and FLOPs.

- **Define "Manual Drop"**: Add 1–2 sentences in Section 4.3 explaining what subnetwork selection strategy is used for the no-mapping baseline in Table 4. If it is random selection or TinyCLIP-style importance-based pruning, state this explicitly.

- **Clarify attention head handling**: Add a brief note in A.3 stating whether head count is preserved (with per-head dimension scaling proportionally) or adjusted, and confirm that LayerNorm parameters scale with the mapped dimensions.

- **Add an SVD-based projection baseline** would substantially strengthen the paper, but this is suggested as future work rather than a requirement for acceptance.

## Score and Decision

### Calibration anchor comparison:

- **/home/wg25r/review_agent/human_reviews_2026/RQUwj3HdUm.md** (avg 2.50, Reject): Task Matrices — interesting idea but very limited evidence, couldn't reproduce. CLIP-Map is substantially stronger with thorough experiments.
- **/home/wg25r/review_agent/human_reviews_2026/UGCgt3cvcC.md** (avg 4.00, Reject): Adaptive MLP Pruning — decent method but limited novelty and some concerns. CLIP-Map has more novelty and stronger empirical demonstration.
- **/home/wg25r/review_agent/human_reviews_2026/Fxz0aaGSNY.md** (avg 4.80, Reject): Multi-modal dataset distillation — creative approach but reviewers found theoretical simplifications unjustified. CLIP-Map's methodology is better justified.
- **/home/wg25r/review_agent/human_reviews_2026/mp67iSM7qn.md** (avg 5.00, Accept Poster): InherNet — uses SVD-based initialization for model compression, similar spirit. CLIP-Map is comparable in contribution level, with a more complete pipeline.
- **/home/wg25r/review_agent/human_reviews_2026/CVXpkc3bXc.md** (avg 5.20, Reject): Kronecker SAEs — related technique but mixed reviews. CLIP-Map is comparable in technical contribution but has more application-oriented results.
- **/home/wg25r/review_agent/human_reviews_2026/i36E5Ezm0H.md** (avg 5.50, Accept Poster): PruneSID — solid method with good results. CLIP-Map is at a similar level but has the Table 6 error that reduces confidence slightly.
- **/home/wg25r/review_agent/human_reviews_2026/Wa9Bg9b50B.md** (avg 6.00, Accept Poster): CompoDistill — very clean analysis, well-motivated. CLIP-Map is somewhat weaker due to the documentation issues and missing baselines.
- **/home/wg25r/review_agent/human_reviews_2026/kI27Niy4xY.md** (avg 8.00, Accept Oral): Model stitching — truly novel paradigm with strong results. CLIP-Map is clearly below this level.

CLIP-Map sits at the borderline. The core idea (mapping-based compression with Kronecker factorization and diagonal initialization) is genuinely novel and well-motivated, and the results against TinyCLIP are compelling. However, the Table 6 architectural specification error, the undefined "Manual Drop" baseline, and the underspecified architectural details collectively reduce confidence. The paper is stronger than the 4.0–4.8 rejected papers and comparable to borderline accepts at 5.0–5.2. I score it **5.0** — a weak/borderline accept that requires the identified issues to be addressed.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>