Now I have all the evidence I need. Let me produce the final consolidated review.

## Summary
The paper proposes PruMerge, an adaptive visual token reduction method for Large Multimodal Models (LMMs). It uses IQR outlier detection on CLS-attention scores to dynamically select important visual tokens per image, then applies k-NN clustering with key-vector similarity to merge pruned tokens into retained ones via weighted averaging. A variant, PruMerge+, adds spatial-uniform sampling to reduce performance loss. Experiments on LLaVA-1.5 show the method compresses visual tokens to 5.5% (PruMerge) or 25% (PruMerge+) of the original 576 tokens, with video generalization shown on Video-LLaVA.

## Strengths
1. **Adaptive token selection via IQR outlier detection (Sec. 3.2, Table 3).** Unlike fixed-budget pruning, the method dynamically determines the number of retained tokens per image based on the sparsity of CLS-attention scores. Table 3 confirms this adaptive strategy consistently outperforms sequential and spatial uniform sampling across all four benchmarks. Simpler images yield fewer tokens (~16 for ScienceQA) while text-rich images yield more (~40 for TextVQA) — a genuinely adaptive behavior.

2. **Token merging via key-similarity clustering (Sec. 3.3, Table 4).** Rather than discarding pruned tokens, the method merges them into selected tokens using k-NN on key vectors and weighted averaging by class attention. Table 4 shows adding this component (AITS + TS) improves MME from 1221.6 to 1350.3 over selection alone (AITS), demonstrating that supplementation meaningfully enhances retained token quality.

3. **Zero-shot generalization to video (Table 5).** Applying PruMerge to Video-LLaVA at inference time without retraining improves accuracy on MSVD-QA (+0.4) and ActivityNet-QA (+3.0) while using only 12.5% of visual tokens. This indicates the method captures cross-modal redundancy and even boosts performance on video tasks.

4. **Clear distinction from ViT-centric token reduction (Sec. 3.5).** The paper explicitly argues why methods designed for accelerating ViTs (e.g., ToMe) are insufficient for LMMs, where the LLM is the dominant bottleneck. PruMerge targets the LLM prefix tokens, not the ViT's internal computation.

## Weaknesses

### Fatal
None.

### Major
1. **Performance claims overstated for the 14× compression setting (Abstract, Table 1).** The abstract and introduction claim that compressing visual tokens by 14× (to 5.5%) achieves "comparable performance." Table 1 tells a different story for PruMerge on LLaVA-1.5 (7B): VQAv2 drops 78.5→72.0 (−6.5), POPE drops 85.9→76.3 (−9.6), and MME drops 1510.7→1350.3 (−160.4). These are substantial degradations, not "comparable" by any standard measure. The paper conflates PruMerge (14×, significant drops) with PruMerge+ (4×, smaller drops) under the same "comparable performance" banner, and never explicitly acknowledges the severity of the aggressive compression's degradation. PruMerge+ (25% tokens, 4× compression) delivers results that genuinely approach the baseline, and the paper would be better served by centering its claims on this variant.

2. **Missing comparisons to natural baselines (Table 3).** The ablation compares PruMerge to sequential and spatial uniform sampling — both weak baselines. The paper does not compare to: (a) taking the top-k tokens by CLS attention (a fixed-threshold counterpart that directly tests whether adaptivity via IQR matters), (b) random token pruning, or (c) other token reduction methods adapted for LMM prefix tokens. Since the core claim is that IQR-based adaptive selection is superior, the absence of a fixed top-k baseline leaves the benefit of adaptivity unsubstantiated.

3. **Efficiency claims rely entirely on theoretical estimates with no real runtime measurement (Table 2, Fig. 1 caption).** Table 2 reports FLOPs, prefill time, memory, and activation storage based on a roofline model (LLM-Viewer). The paper states this explicitly, but the headline claim of "around 4–10 times in FLOPs for LMM prefill" (Fig. 1 caption) cannot be verified with actual wall-clock measurements. Critically, the overhead of the pruning/merging step itself (IQR computation + k-NN search + weighted averaging) is never measured or reported. For a paper whose central contribution is efficiency, the lack of end-to-end latency results is a significant gap.

### Minor
1. **Key hyperparameter k (number of nearest neighbors in merging) is unspecified (Algorithm 1).** Algorithm 1 (line 208) uses "find the k most similar tokens" but the value of k is never stated anywhere in the paper. No ablation over k is provided. This makes the method incompletely specified for reproduction and leaves the robustness of the merging step unclear.

2. **Ambiguity in which layer's keys are used for similarity computation.** Line 161 states that class attention values from the *penultimate* layer are used for selection. Line 175 states that "the final layer's key vector serves as the representation" for similarity in merging. However, Algorithm 1's input declaration (line 198) takes "Key and Query matrices of ViT's penultimate layer" — creating an inconsistency about whether the merging step uses penultimate or final layer keys.

3. **No justification for using the penultimate layer (vs. the final layer) for CLS-attention scores (Sec. 3.2).** Line 161 specifies the penultimate layer but offers no explanation for this design choice.

4. **No error bars or variance reported for any experiment (Tables 1, 3, 5).** The video results in particular (Table 5) show small absolute improvements (e.g., +0.4 on MSVD-QA, +3.0 on ActivityNet-QA), which could be within noise.

5. **The IQR multiplier (1.5) is not ablated (Sec. 3.2).** While the paper states the 1.5× multiplier, it provides no sensitivity analysis for this choice.

### Trivial
None.

## Nice-to-Haves
- Adding a simple top-k by CLS attention baseline would directly test the adaptivity claim.
- Including end-to-end wall-clock latency measurements (with and without the pruning/merging overhead) would substantiate the efficiency claims.
- Reporting standard deviations or confidence intervals, especially for the video experiments where gains are small.
- Ablating the value of k (number of neighbors) and the IQR multiplier (1.5) to demonstrate robustness.

## Removed Points
- **"No comparison to existing token reduction methods for LMMs (e.g., FastV)."** The reviewer cited methods not present in the paper or that post-date it. The paper does cite and discuss ToMe and other ViT-focused token reduction methods in related work. The claim that no comparison to "existing LMM token reduction" methods is made is factually correct in that no such prior methods exist at scale, but the paper could still implement a ToMe-like prefix reduction. This point is partially retained in Major Weakness 2 (missing ToMe-based prefix reduction baseline) but the specific reference to "FastV" is removed as unverifiable.
- **"Missing related works."** Removed per instructions — external confirmation is not available.
- **"The paper should report variance across runs or splits."** Retained in Minor Weakness 4 but downgraded from the critic's emphasis since single-run evaluation is standard practice in this field.
- **Strength Finder Strength 3 ("Extreme compression with minimal performance loss").** This directly contradicts verified Major Weakness 1 (performance drops on PruMerge are substantial, not minimal). The weakness wins; this strength is removed.
- **Various formatting/typo nitpicks.** Removed per instructions (parser artifacts, not author errors).

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Reframe the paper to clearly separate the two regimes: PruMerge (aggressive 14× compression with acknowledged degradation) as an extreme case, and PruMerge+ (moderate 4× compression with minimal loss) as the primary contribution. The "comparable performance" claim should apply only to PruMerge+.
2. Add a top-k by CLS attention baseline to Table 3 to directly test whether the IQR-based adaptivity provides measurable benefit over a fixed threshold.
3. Report real end-to-end wall-clock latency on a GPU, including the overhead of the IQR computation and k-NN merging step.
4. Specify the value of k in Algorithm 1 and provide an ablation over k.
5. Resolve the ambiguity about whether the merging step uses penultimate-layer or final-layer keys, and justify the choice of layer for CLS-attention scores.

## Score and Decision

The paper tackles an important problem — reducing visual token count in LMMs — and proposes a reasonably designed method with adaptive selection and merging. The strengths are genuine: the adaptive selection via IQR is novel for this setting, and the merging component demonstrably improves over pruning alone. However, the paper significantly overstates the performance of the 14× compression regime (the headline claim), misses obvious baselines (top-k selection) that would substantiate the adaptivity contribution, and provides only theoretical efficiency projections without real runtime measurements. These are not fatal flaws — they are fixable — but they materially weaken the paper's claims as written.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>