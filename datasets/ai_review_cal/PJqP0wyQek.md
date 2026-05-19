- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6, 6
Now I'll produce the final consolidated review.

## Summary

The paper introduces MS-Diffusion, a zero-shot multi-subject image personalization framework that incorporates explicit layout guidance. It proposes two main technical innovations: (1) a Grounding Resampler (GRS) that fuses entity text embeddings and Fourier box embeddings with learnable queries to extract subject features, and (2) a Multi-subject Cross-Attention (MCA) mechanism that uses attention masks to confine each subject's conditioning to its designated spatial region, with background dummy tokens to handle the "universal masking" problem. The training data is constructed from video frames to avoid copy-paste artifacts. Experiments on DreamBench and a newly introduced MS-Bench show leading performance on DINO, M-DINO, and CLIP-T, with competitive but slightly lower CLIP-I scores.

## Strengths

- **First framework to jointly support all five desiderata for multi-subject personalization**: Table 1 systematically compares prior P-T2I methods across zero-shot capability, multi-subject support, base model freezing, MLLM-free operation, and layout guidance. Only MS-Diffusion satisfies all five criteria. This is a genuine combinatorial contribution — prior methods each miss at least one of these capabilities.

- **Ablation study (Table 3) convincingly validates both technical components**: Removing the grounding resampler (w/o GRS) drops single-subject DINO from 0.671→0.646 and multi-subject DINO from 0.425→0.389. Removing multi-subject cross-attention (w/o MCA) drops multi-subject CLIP-T from 0.341→0.309 and M-DINO from 0.108→0.100. Replacing layout guidance with implicit attention-loss alternatives (IAL+TAL) yields strictly worse results (CLIP-T 0.316, M-DINO 0.093) despite training additional parameters. This provides clear quantitative evidence that explicit layout guidance is superior to implicit objectives for this task.

- **Substantial text-fidelity gains in multi-subject scenarios**: MS-Diffusion achieves multi-subject CLIP-T of 0.341, substantially ahead of the next-best zero-shot method (λ-ECLIPSE at 0.316). The gap is much wider than in single-subject comparisons, demonstrating that the proposed mechanisms specifically address the text-fidelity degradation that plagues prior multi-subject personalization.

- **Video-based data construction is a principled design choice**: The idea of using different frames from the same video sequence as reference and target (Section 3.2) directly addresses the "copy-and-paste" reconstruction bias noted in prior work (e.g., AnyDoor). This is a practical innovation that separates the reference from the ground truth without requiring paired multi-view data.

## Weaknesses

### Fatal
None.

### Major

- **The claim of "surpassing existing models in both image and text fidelity" is overstated given the metric-dependent results.** In Table 1, MS-Diffusion leads on DINO and M-DINO but trails on CLIP-I (single-subject zero-shot: 0.792 vs. SSR-Encoder's 0.821 and Kosmos-G's 0.822; multi-subject: 0.698 vs. SSR-Encoder's 0.725). The paper's argument that DINO is more detail-sensitive while CLIP-I can be inflated by background overfitting (citing DreamBooth) is plausible but **not substantiated** — no human evaluation, per-subject breakdown, or analysis of where the metrics diverge is provided. The central claim about image fidelity would be materially strengthened by even a small-scale human preference study asking which image better preserves subject identity. Without it, the evidence for "surpassing...image fidelity" is incomplete: it surpasses on one metric but not the other.

### Minor

- **No ablation validating the video-based data construction.** The paper argues that using video frames (rather than independent image pairs) mitigates copy-paste artifacts and is a key design innovation (Section 3.2). However, there is no experiment comparing training on video-based samples vs. independent image pairs. The effectiveness of this design choice is assumed but not empirically supported — a simple comparison (e.g., training an otherwise identical model on image-pair data and comparing DINO/M-DINO) would directly validate or refute the claim.

- **No analysis of the grounding resampler's internal behavior.** The paper attributes the improvement of GRS over a standard resampler to the addition of grounding tokens (entity text + box embeddings), but provides no visualization or analysis of how these grounding tokens affect the resampler's attention. For example, do the learnable queries attend to different image regions when grounding tokens are present versus absent? Showing attention maps from the resampler would strengthen the mechanistic understanding of the method.

- **No discussion of inference cost or parameter count.** The grounding resampler adds \(n \times n_t\) tokens per subject, and the multi-subject cross-attention involves per-subject masking. The paper reports no runtime, memory usage, or parameter count comparisons. This omission makes it difficult for practitioners to assess the practical overhead, especially with many subjects.

### Trivial

- The CLIP-I gap in multi-subject settings (0.698 vs. 0.725) could be discussed more directly in the main text rather than only as a side note in the single-subject section. The current presentation emphasizes strengths without transparently addressing the one metric where the method trails.

## Nice-to-Haves

- **Per-subject success rate analysis**: M-DINO (product of per-subject DINO scores) is a good summary metric but hard to interpret. Reporting the fraction of generations where all subjects achieve a minimum DINO threshold, or a histogram of per-subject DINO scores, would make the results more actionable.

- **Failure analysis / characterization of remaining failure modes**: Under what conditions does MS-Diffusion still suffer from subject neglect or conflict? (e.g., heavily overlapping bounding boxes, semantically similar subjects, extreme aspect ratios). Acknowledging limitations would improve credibility.

- **Comparison with fine-tuning-based multi-subject methods**: While the paper targets zero-shot, including a fine-tuning baseline (e.g., Custom Diffusion with multiple learned tokens) on the same MS-Bench would contextualize how close zero-shot performance is to the fine-tuning upper bound. If the gap is small, that is a strong result worth reporting.

## Removed Points

These points were flagged for removal from the main body; they are listed here for completeness but did not influence scoring.

- **Criticism about proprietary dataset / MS-Bench not being publicly available** *(removed per hard rules: criticisms about release status or availability of cited datasets/benchmarks are not to be included)*.

- **Criticism about missing comparison with GLIGEN, Instance Diffusion, MIGC** *(removed: these are layout-conditioned generation methods, not personalization methods; the paper discusses them in related work and correctly scopes its novelty claim as layout-guided *personalization*, not layout guidance per se)*.

- **Criticism about data construction details being vague / deferred to appendix** *(removed per hard rules: the parser strips appendix content; the details exist in the original submission)*.

- **Strength about training data construction mitigating copy-paste artifacts** *(removed: the design rationale is sound, but the paper provides no direct evidence — no ablation — that the video-based approach actually mitigates copy-paste artifacts compared to an image-pair baseline, so this strength is unsupported by the evidence presented)*.

- **Criticism about code/data not being released** *(removed per hard rules)*.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely agree on the paper's strengths (novel combination of attributes, well-validated components via ablation) and weaknesses (metric-dependent fidelity claims, missing ablations on data construction, no human evaluation). The most actionable observation is that the paper's evidence for its central fidelity claim is incomplete by the authors' own framing — they assert DINO is the better metric for detail fidelity but provide no human judgment to resolve the CLIP-I vs. DINO disagreement.

## Suggestions

1. **Add a human evaluation study**, even a small-scale one (e.g., 100 comparisons on Amazon Mechanical Turk), asking raters to choose which image better preserves subject identity from a set of MS-Diffusion vs. baseline outputs. This would directly resolve the DINO vs. CLIP-I ambiguity and is the single most impactful additional experiment.
2. **Ablate the video-based data construction** by training an otherwise identical model on independent image pairs and reporting the same metrics. This would either validate or refute one of the paper's claimed innovations.
3. **Report per-subject DINO histograms** for multi-subject generations, showing the distribution of per-subject scores alongside the aggregate M-DINO.
4. **Report inference time and peak memory** for different numbers of subjects, so practitioners can assess the practical cost of the method.
