Now I have sufficient information to write the final consolidated review. Let me compose it.

---

## Summary

This paper proposes Content-Aware Mamba (CAM), a Mamba-style SSM for learned image compression that replaces the standard fixed raster-scan with a content-adaptive token permutation (CTP) and overcomes strict causality via global-prior prompting (GPP). The resulting model, CMIC, achieves strong rate-distortion results (15.91% BD-rate reduction over VTM-21.0 on Kodak) while using substantially fewer parameters and FLOPs than prior Mamba-based compression models (69M vs 157M for MambaIC).

## Strengths

1. **Novel, well-motivated architectural contributions.** The paper identifies two concrete limitations of applying Mamba to image compression — content-agnostic scan order and strict causality — and introduces separately ablated mechanisms (CTP + GPP) to address each. The codebook-based clustering for content-adaptive permutation and the prompt-dictionary approach for mitigating causality are technically grounded and clearly described.

2. **Strong experimental validation with clean ablation.** Table 2 quantifies the individual contribution of each component: CTP alone gives 2.0% BD-rate improvement, GPP alone gives 1.0%, and their combination yields 2.7% over the vanilla Mamba baseline on Kodak. Table 4 further ablates alternative network structures (Conv, 2D Mamba, Attention-only, CAM-only), confirming that the full CMIC design outperforms all variants.

3. **Compelling qualitative evidence for the claimed effects.** Figure 9 visualizes the effective receptive field of a single Mamba layer under each configuration, showing (c) how GPP breaks strict causality, (d) how CTP reshapes the ERF toward semantically correlated regions, and (e) how the combination produces global, content-adaptive context. Figure 10 confirms that the clusters capture semantically meaningful groupings (red doors, feathers, sky). These visualizations directly support the paper's claims.

4. **Clear efficiency advantage over prior Mamba-based LIC.** CMIC uses 69.11M params vs MambaIC's 157.09M, 2.39 TFLOPs vs 5.56 TFLOPs, 4.44 GB peak memory vs 20.32 GB, and 0.405s decoding latency vs 0.669s (Table 1). The training throughput (22.05 samples/s) is substantially higher than MambaVC (6.55) and MambaIC (9.35) (Table 3). This demonstrates that the content-adaptive single-scan approach is more efficient than multi-directional scanning.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The framing overstates Mamba's limitations.** The paper argues that Mamba's rigid scan and strict causality are "fundamental challenges" that "hinder effective redundancy removal." Yet the vanilla single-scan Mamba baseline (both CTP and GPP disabled) achieves -13.26% BD-rate on Kodak — nearly identical to MLIC++ (-13.42%) and competitive with other SOTA methods. The improvement from the full model (-15.91%) is meaningful (2.65%) but the gap does not warrant the claim that vanilla Mamba is fundamentally unsuited for compression. A more measured framing would better reflect the evidence.

2. **Missing detail on gradient flow through hard clustering.** The paper uses argmax-based assignment (Algorithm 1, line 4: `g_i ← arg max_j Distance_{i,j}`) and a one-hot assignment matrix Γ (Section 3.4). The centroids are updated via non-gradient EMA. The paper does not state how gradients from the rate-distortion loss propagate through the discrete assignment to the encoder features (the standard VQ-VAE solution is a straight-through estimator). While the overall training pipeline is likely workable (permutation is a differentiable indexing operation; the mapping A(·) is explicitly described as differentiable), this omission creates a reproducibility gap that should be addressed. The paper would benefit from a brief statement clarifying whether a straight-through estimator, Gumbel-softmax, or gradient stopping is applied.

3. **Throughput and complexity measurements are on small patches.** Training throughput in Table 3 is measured on 256×256 patches with batch size 8. While this is a reasonable controlled ablation, it is unclear how this correlates with full-resolution performance. The paper already reports decoding latency on 2K images (0.405s), which partially addresses this, but a brief note on how the 22.05 samples/s figure scales to higher resolutions would strengthen the efficiency analysis.

### Trivial

1. Section 3.4 states that CTP and GPP together "mitigate" strict causality, which is accurate (the hidden state update remains causal; only the output is modified). The paper could clarify this more explicitly in the main text alongside the claim in the abstract.
2. The paper does not specify the exact number of training images in Flickr2W (typically ~1.8M in the original, but not stated here). While this is a common omission, including the count would improve reproducibility.

## Nice-to-Haves

- A comparison against a VMamba-style 4-directional scan variant at comparable model size would directly test whether the proposed content-adaptive single scan is more effective than multiple fixed scans. This would strengthen the paper's central argument.
- A concrete visualization showing which spatially distant tokens become adjacent after permutation would intuitively illustrate how CTP works.
- An analysis of why CAM provides negligible gains in the entropy model (mentioned briefly in Section 4.5 but not explored) could yield insights about where content-adaptive Mamba is most beneficial.

## Removed Points

**These points are flagged to be removed, treat them with caution:**

- **"Unfair baseline comparisons — baselines trained on different datasets"**: This is standard practice in the LIC literature. Nearly all published LIC papers compare using numbers from original publications. Retraining all baselines on Flickr2W would be prohibitively expensive and is not standard practice. The critic's claim that "the reported superiority may be due to training data differences" is a generic concern applicable to virtually every LIC paper, not a specific flaw of this work. Moreover, CMIC substantially outperforms other Mamba-based models (MambaVC, MambaIC) that face the same training-data limitation.

- **"No error bars or multiple-run statistics"**: Single-run evaluation is the norm in learned image compression. This is not a weakness specific to this paper.

- **"Throughput measured on 256×256 patches"**: This is a standard ablation methodology for controlled comparison. The paper also reports decoding latency on full 2K images (Table 1), so the efficiency analysis is comprehensive.

- **Criticism about the paper claiming Mamba has "fundamental challenges" while the baseline performs well**: This is partially valid (see Minor weakness 1 above), but the critic overstates the issue. The 2.65% improvement from the components is meaningful — in compression, gains are measured in fractions of a percent.

- **Any criticism about missing appendix content, missing references, or absent proofs**: The parser strips these sections from all papers. They exist in the original submission.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a sentence clarifying how gradients pass through the hard clustering (e.g., "the argmax assignment is treated as a straight-through estimator, copying gradients from the reordered tokens back to the encoder features").
2. Tone down the framing of Mamba's limitations in the introduction to better match the empirical evidence (the vanilla Mamba baseline is already competitive).
3. Add a comparison against a 4-directional scan VMamba variant at similar model size to more directly demonstrate the advantage of content-adaptive scanning.
4. Include the exact training dataset size in the experimental setup.

## Score and Decision

**Calibration anchors** (all from the human-review corpus):

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| MambaVC (KgJwbsfN7G) — Mamba-based LIC, Reject | 4.80 | Weaker technical novelty (direct application of VSS block without compression-specific design); CMiC has clearer motivation and stronger results |
| Spatial-Mamba (iDe1mtxqK5) — Visual SSM, Accept | 7.00 | Strong general-purpose SSM contribution; CMiC is more domain-specific (compression) but with comparably novel components |
| Frequency-Aware Transformer (HKGQDDTuvZ) — LIC transformer, Accept | 6.00 | Similar scope and contribution level; CMiC has more thorough ablation and efficiency analysis |
| Lattice Transform Coding (Tv36j85SqR) — Compression theory, Accept | 7.20 | Stronger theoretical contribution; CMiC is more empirical/architectural |
| NCA Compression (gIrVoQEDQv) — Weak compression paper, Reject | 3.40 | Far weaker experiments and contribution; CMiC is substantially stronger on every axis |
| MambaQuant (KI45uDnmzv) — Mamba quantization, Accept | 6.25 | Similar level of technical contribution — both introduce carefully engineered Mamba extensions with thorough experiments |

CMiC is clearly stronger than lower-scored papers like MambaVC (4.80) and far superior to the NCA compression paper (3.40). Its technical contribution is comparable to the Frequency-Aware Transformer (6.00) — both introduce novel architecture components for LIC with solid experimental validation — and to MambaQuant (6.25). It is somewhat below the Spatial-Mamba (7.00) and Lattice Transform Coding (7.20) papers, which have broader scope or deeper theoretical contributions, but CMiC's contributions are well-targeted, the experiments are thorough, and the efficiency gains over prior Mamba-based models are substantial.

The two real weaknesses (overstated framing of Mamba limitations, missing gradient-flow detail) are minor and addressable. The paper makes a solid, well-evidenced contribution to learned image compression.

**Score: 6.5**

**Decision: Accept**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>