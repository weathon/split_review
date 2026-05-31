I have verified all the key claims from both reviewers against the paper. Now I will produce the final consolidated review.

---

## Summary

This paper proposes Hierarchical Side-Tuning (HST), a parameter-efficient transfer learning method for Vision Transformers that freezes the ViT backbone and trains a lightweight Hierarchical Side Network (HSN) to model multi-scale features from intermediate activations. The key technical contributions are: (1) a Meta-Register token inserted in each ViT block to extract task-specific global features, (2) a Transformation Bridge (T-Bridge) with dual-branch separation and linear weight sharing to connect ViT activations to the side network, and (3) cross-attention Side blocks with O(2Ld) complexity. HST is evaluated across image classification (VTAB-1K, FGVC), object detection (COCO), instance segmentation (COCO), and semantic segmentation (ADE20K), achieving 76.1% average Top-1 accuracy on VTAB-1K with 0.78M trainable parameters and competitive/superior results on dense prediction tasks.

## Strengths

1. **Novel architecture that genuinely extends PETL to dense prediction tasks.** Prior PETL methods (VPT, Adapter, LoRA) primarily target classification and struggle with multi-scale features needed for detection/segmentation. HST's Hierarchical Side Network, combined with the Meta-Register and T-Bridge, provides a principled way to extract and fuse multi-scale features from a frozen plain ViT. The cross-attention design with O(2Ld) complexity (Equation 3, Section 3.4) is clever and well-motivated.

2. **State-of-the-art results on VTAB-1K with extreme parameter efficiency.** HST-B achieves 76.1% average Top-1 accuracy across 19 tasks with only 0.78M trainable parameters (0.9% of backbone parameters), outperforming all compared PETL methods (SSF 73.10%, LoRA 72.25%, AdaptFormer 73.10%, NOAH 73.20%) — see Table 1 (Section 4.2). The method outperforms full fine-tuning on all 19 tasks on this benchmark.

3. **Competitive results on dense prediction tasks, including surpassing full fine-tuning in some setups.** On Cascade Mask R-CNN 3×+MS (Table 5, Section 4.3), HST achieves 49.5 AP^b vs. 48.7 AP^b for full fine-tuning and 46.9 AP^b for LoRA, while using only 68.4M total parameters vs. 151.4M for full fine-tuning. On Mask R-CNN and UperNet, HST substantially closes the gap between PETL methods and full fine-tuning.

4. **Thorough and well-designed ablation studies.** The component ablations (Table 7, Section 4.7) systematically isolate the contribution of each design choice: LN-tuning (+2.2% on VTAB-1K, +2.8 AP^b), linear weight sharing (reduces parameters while slightly improving accuracy), GlobalT integration, and Fine-Grained Injection. The Meta-Register ablation (Table 5) convincingly shows that a single token suffices, avoiding the prompt-length search required by VPT.

5. **Effectiveness across different pre-training schemes (ImageNet-21K and MAE).** Table 2 (Section 4.2) shows that while most PETL methods degrade significantly under MAE pre-training, HST maintains strong performance, often matching or exceeding full fine-tuning. This demonstrates practical versatility.

## Weaknesses

### Fatal

None.

### Major

1. **Abstract overclaims results that are only partially supported.** The abstract states that on COCO and ADE20K "HST outperformed existing PETL methods and **even surpassed full fine-tuning**." In reality, HST surpasses full fine-tuning on Cascade Mask R-CNN 3×+MS (49.5 vs. 48.7 AP^b) but **does not** surpass full fine-tuning on Mask R-CNN 1× or 3×+MS (43.9 vs. 45.1 AP^b), ATSS 3×+MS (46.0 vs. 46.7 AP^b), Semantic FPN (44.3 vs. 46.0 mIoU), or UperNet (47.0 vs. 49.5 mIoU). The introduction (line 29) is more measured — "achieve comparable performance" — creating an inconsistency. This is a factual error in the paper's framing that could mislead readers.

2. **Section 4.5 (Efficiency Analysis) is completely empty.** The section header `\subsection{Efficiency Analysis}\label{efficiency}` appears at line 376 with zero content before `\subsection{Visualizations}` at line 378. Parameter-efficient transfer learning is fundamentally motivated by computational efficiency, yet the paper provides no training time, GPU memory, throughput, or FLOPs measurements for HST compared to any baseline. This is a significant omission that hollows out a core motivation of the work.

### Minor

3. **The VTAB-1K full fine-tuning baseline (65.57%) is notably low and unexplained.** HST's 10.5% absolute gain over full fine-tuning is far larger than what other PETL methods show (e.g., SSF at 73.10% is +7.5% over FT). The full fine-tuning numbers are cited from the VPT paper, which may use a different training pipeline. While this does not invalidate HST's performance, the paper should at minimum acknowledge the situation and discuss whether the baseline reflects a weak training recipe. Without this, readers cannot assess whether HST's advantage is genuine or partly an artifact of baseline weakness.

4. **Parameter counts for dense prediction tasks are higher than some PETL baselines, yet the paper's narrative emphasizes extreme parameter efficiency without qualification.** For Mask R-CNN 1× (Table 4), HST uses 30.6M trainable parameters vs. LoRA's 28.4M and VPT's 28.4M. The abstract highlights "a mere 0.78M parameters," which applies only to classification. While the difference is modest (~2M), the paper would benefit from explicitly noting that the parameter savings relative to other PETL methods are smaller in dense prediction settings.

### Trivial

5. The t-SNE and Grad-CAM visualizations (Section 4.6) are qualitative and only weakly supportive — but this is standard for such visualizations and not a meaningful weakness.

## Nice-to-Haves

- Adding training time and peak GPU memory comparisons for at least one representative task (e.g., VTAB-1K or COCO detection) would substantially strengthen the paper's efficiency claims.
- Reporting variance/confidence intervals across multiple runs would improve reproducibility confidence, especially given the random initialization of Meta-Register tokens.
- An ablation of side network depth (the paper uses fixed 3,3,3,3 for ViT-B) would show whether the design is near-optimal.

## Removed Points

These points were flagged by reviewers but are removed after cross-checking:

- *"The abstract claims about surpassing full fine-tuning are contradicted by the paper's own tables (Mask R-CNN)"* — **Partially kept but downgraded.** The abstract is indeed overclaimed, but HST *does* surpass full fine-tuning on Cascade Mask R-CNN. The claim is not uniformly false; it is overstated. This is addressed in Major weakness #1 above.

- *"10.5% improvement on VTAB-1K is suspicious and undermines central claim"* — **Downgraded from fatal-sounding to Minor.** The full fine-tuning numbers are cited consistently from the VPT paper, which uses a standard protocol. The gap is large but not unprecedented for PETL methods on VTAB-1K (SSF also shows +7.5%). This is worth noting but does not threaten the core claim.

- *"No statistical significance or variance reported"* — **Moved to Nice-to-Have.** Single-run evaluation is standard practice for large-scale vision benchmarks; requesting variance is reasonable but not a core weakness.

- *"The side network depth is not ablated"* — **Moved to Nice-to-Have.** The paper already has extensive ablations; this is a secondary question.

- *"Cascade Mask R-CNN 3×+MS uses 68.4M params vs 151.4M for full fine-tuning"* is listed as a strength. This is accurate and kept.

- *"Parameter counts in dense prediction are higher than baselines, contradicting the 'fewer parameters' narrative"* — **Downgraded from a headline issue to Minor.** HST uses ~2M more params than LoRA on Mask R-CNN but still far fewer than full fine-tuning (30.6M vs 113.6M). On UperNet, HST actually uses *fewer* params than all PETL baselines (39.9M vs 41.4–42.4M). The claim is nuanced, not contradicted.

- *Strength Finder claimed "SOTA on VTAB-1K"* — kept but contextualized in the weaknesses (weak FT baseline issue).

- *Strength Finder claimed "surpassing full fine-tuning in dense prediction"* — kept but qualified: true for Cascade Mask R-CNN, not uniformly.

## Novel Insights

The two reviews provide opposing perspectives (harsh critic sees overclaiming and missing analysis; strength finder highlights genuine architectural novelty), but neither identifies a deeper insight beyond what the paper itself states. The most interesting observation that emerges from synthesizing both reviews is a tension: the paper's core technical contribution — a side network that models multi-scale features from intermediate ViT activations — is well-designed and convincingly ablated, yet the paper undermines itself by overselling results in the abstract and omitting a promised efficiency analysis. This creates a gap between the genuine quality of the method and the presentation's credibility that would be straightforward to fix. None beyond the paper's own contributions.

## Suggestions

1. **Fix the abstract.** Replace "surpassed full fine-tuning" with a precise statement (e.g., "achieves competitive or superior results, surpassing full fine-tuning on Cascade Mask R-CNN while closing the gap on other dense prediction benchmarks").
2. **Populate Section 4.5** with concrete efficiency measurements: training GPU-hours, peak memory, throughput, and parameter counts compared to baselines on at least one representative task.
3. **Acknowledge the VTAB-1K baseline issue** in the paper: note that the full fine-tuning numbers are from prior work's pipeline, and briefly discuss whether the advantage is robust across training configurations.
4. **Qualify parameter efficiency claims** in the abstract/introduction by noting they apply primarily to classification, and show the trade-offs explicitly for dense tasks.

## Score and Decision

### Round 1 — Bracketing

Round-1 bracket: **4.5–7.0**. The paper is clearly stronger than rejected/withdrawn PETL papers scoring 2–4 (Non-Deep ViT, Domain Adaptation PEFT at 3.0; ELSE at 4.0; APLA at 4.4; AdaRoute at 4.0) which suffer from limited novelty, incomplete evaluations, or weak motivation. But it is weaker than oral/posters scoring 8+ (Generative Universal Verifier, VIST3A, π³, NavFoM) which represent fundamentally different types of contributions. The most competitive anchors are in the 4–7 band.

### Round 2 — Narrowing

Round-2 anchors:
- **WIMFRIS** (avg 5.0, Accept Poster): Slightly lower quality — has incomplete sections, novelty concerns, and unfair comparison issues. HST has stronger novelty and better ablation coverage.
- **Token Selection SPA** (avg 6.0, Accept Poster): Comparable quality — clear motivation, strong experiments. HST has more architectural novelty but SPA has better efficiency measurements. Roughly matched.
- **Revisiting CLS and Patch Token** (avg 6.0, Accept Poster): Strong analysis paper; different type of contribution. HST is comparably solid.
- **Locality-Attending ViT** (avg 6.0, Accept Poster): Solid paper with clear contribution, comparable evaluation breadth.

HST is clearly above the 4–5 range papers and sits squarely at the level of the 6.0 anchors. The main factors preventing it from reaching 6.5–7.0 are: (1) the abstract overclaim, (2) the empty efficiency section, and (3) the unexplained VTAB-1K baseline gap.

### Final Score

After comparing against the anchors, the paper lands at **6.0**. It has a genuine architectural contribution with strong empirical validation, but the credibility-damaging issues (abstract overclaim, missing efficiency section) prevent it from reaching the 6.5+ tier. A corrected abstract and populated efficiency analysis would move this to 6.5–7.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>