Now I have a thorough understanding of the paper and the reviews. Let me produce the consolidated review.

## Summary

This paper introduces L2C (Learning to Complement), a framework for Few-Shot Test-Time Domain Adaptation (FSTT-DA) that keeps CLIP frozen and attaches a parallel CPNet to learn dataset-specific knowledge directly from the input space. The key idea is that relying solely on CLIP's feature space (as in prior work VDPG) limits performance, especially with smaller backbones. L2C complements CLIP's generalized features with a side network trained via revert attention, enhances text feature discrimination via greedy ensemble and refinement, and adapts both modalities using domain-aware fusion. Experiments on five benchmarks (DomainNet + 4 WILDS datasets) show consistent improvements over prior SOTA, with notable gains on challenging WILDS datasets using ViT-B/16 (e.g., +5.1 F1 on iWildCam, +3.1% WC Acc on FMoW).

## Strengths

1. **Novel and well-motivated approach to complement CLIP's feature space.** The paper correctly identifies that prior FSTT-DA methods (VDPG) are bottlenecked by CLIP's generalized knowledge for unseen downstream datasets. By introducing a parallel CPNet that learns directly from the input space and using revert attention to enforce complementary learning, the paper proposes a principled solution. This is supported by large gains in Table 3 (Index 1→2: +13.1 F1 on iWildCam, +13.8% WC Acc on FMoW from adding CPNet alone).

2. **Consistent and substantial empirical improvements across diverse benchmarks.** L2C outperforms VDPG on all WILDS metrics with both ViT-B/16 and ViT-L/14 (Table 1), and achieves best or second-best accuracy on 4/6 and 5/6 DomainNet domains (Table 2). The gains are especially pronounced on challenging real-world distributions (iWildCam, FMoW) and with the smaller ViT-B/16 backbone, directly supporting the paper's central thesis.

3. **Comprehensive ablation study validating each component.** Table 3 systematically ablates CPNet, revert attention, greedy ensemble, text refinement, uniformity loss, DAF, and domain-centric training, with the full method (Index 8) significantly outperforming all partial variants. Additional ablations on the domain prompt (Table 4), domain information aggregation (Table 5), CPNet depth (Fig. 4), and greedy ensemble (Table 6) provide thorough component-level validation.

4. **Efficient design that preserves CLIP's OOD capabilities.** The method freezes CLIP throughout, requires no gradient flow through CLIP, and the text encoder can be discarded after preprocessing. CPNet is lightweight (e.g., 3 transformer blocks for ViT-B/16 with 12 blocks), and the approach is compatible with black-box API usage of CLIP.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Missing uncertainty quantification (error bars) in main results.** Tables 1 and 2 report only point estimates without standard deviations or confidence intervals. Few-shot test-time adaptation involves stochasticity from support/query splits and domain composition, and the lack of variance reporting makes it impossible to assess whether reported gains are robust or within noise. This is standard practice in benchmark-focused papers in this area (VDPG also reports single runs), but given that the paper's central claim is superiority over prior methods, adding error bars (e.g., over 3 seeds) would substantially strengthen the empirical evidence. The large and consistent gains across 5 benchmarks partially mitigate this concern but do not eliminate it.

2. **No parameter count or FLOPs comparison with VDPG.** The paper frames its improvement over VDPG as a consequence of learning from the input space, but L2C adds non-trivial parameters (CPNet with transformer blocks, text refinement matrices, domain cache, cross-attention modules) that VDPG does not have. While CPNet is acknowledged as lightweight, the paper never reports the total parameter count or inference FLOPs for L2C versus VDPG, making it difficult to assess the computational trade-off. This is not a fatal confound — the extra parameters are the method, not an unfair advantage — but reporting these numbers would allow readers to judge the practical cost of the gains.

3. **Missing pure ablation of DAF with ERM training.** Table 3 compares Index 6 (no DAF, ERM training) to Index 8 (DAF, domain-centric training), which confounds two changes. Index 7 vs. 8 does provide a clean DAF ablation under domain-centric training, which is the actual training scheme used. The missing condition (DAF + ERM) would isolate DAF's contribution without the training scheme change. This is a modest gap — the paper shows DAF helps with the intended training scheme — but a fully controlled ablation would be cleaner.

4. **Limited analysis of what CPNet actually learns.** The revert attention mechanism is designed to force CPNet to learn knowledge complementary to CLIP. The paper shows that removing RT hurts performance (Table 3, Index 4 vs. 5), which provides quantitative support. However, no qualitative evidence (attention maps, nearest-neighbor analyses, error pattern correlation) is presented to concretely demonstrate what "complementary" knowledge CPNet captures. The claim is plausible and quantitatively supported but would benefit from visual or analytic validation.

5. **Text refinement module design receives insufficient explanation and ablation.** The bilinear transformation in Eq. 4 (two matrices M_c and M_d adjusting along label and feature dimensions) is described only briefly. The paper does not explain why this particular factorization is chosen, nor does it ablate design alternatives (e.g., single learned bias, standard MLP, per-class refinement vectors). Since text refinement contributes to gains (Index 2→3 in Table 3), the mechanism deserves more scrutiny.

### Trivial

- The greedy ensemble cost claim ("less than 0.01% of total cost") would benefit from an absolute time or FLOPs figure for clarity, though the intuition is clear.

## Nice-to-Haves

- Sensitivity analysis for support set size (currently fixed at 16 — how robust is performance to various shot sizes?).
- Comparison of L2C against VDPG augmented with a similarly-sized adapter or prompt generator, to better isolate whether the benefit comes from input-space learning vs. added capacity.
- Analysis of potential failure modes (e.g., when target domain is highly novel and source cache is unhelpful).

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Typo in Eq. 4 (LHS writes \(\tilde{\mathbf{I}}^{gre}\) instead of \(\tilde{\mathbf{T}}^{gre}\))**: Removed — this is a formatting/OCR artifact from PDF extraction; the original submission does not have this issue. The broader point about insufficient design rationale for the text refinement module is retained as a Minor weakness.
2. **Black-box compatibility clarification**: The paper describes the method as operating "in parallel" with CLIP and complementing "only at the output" — this is an accurate characterization. The critic's concern about needing CLIP's output representations is already consistent with standard black-box API usage.
3. **Generic/superficial strengths from Strength Finder**: The strength "Strong empirical results across diverse benchmarks" is kept as a genuine strength. The strength "Efficient design without compromising CLIP's OOD abilities" is kept but integrated into Strengths.

## Novel Insights

The reviews collectively surface a meaningful tension between the paper's framing and its experimental design. The paper claims that learning from the *input space* (rather than CLIP's feature space) is the source of improvement, but because L2C adds a non-trivial parallel network, it is impossible to fully disentangle whether the gains come from the *approach* (input-space learning) or simply from added parameters. A properly controlled experiment — comparing L2C against VDPG augmented with an equivalently-sized prompt generator or adapter — would be needed to resolve this. Additionally, the missing error bars are a genuine concern but their severity is partially mitigated by the consistency and magnitude of the gains: +5.1 F1 and +3.1% are large margins on challenging benchmarks, making it unlikely the improvements are purely noise. The paper's comprehensive ablation study (Table 3) is its strongest methodological asset.

## Suggestions

1. Add error bars (standard deviations over 3 random seeds with different support/query splits) to all main tables.
2. Report total parameter counts and approximate inference FLOPs for L2C vs. VDPG to enable a fair assessment of the computational trade-off.
3. Add a qualitative analysis of CPNet's learned representations (e.g., attention map visualizations or nearest-neighbor comparisons) to make the "complementarity" claim more concrete.
4. Include the missing ablation variant (DAF + ERM training) in Table 3 to fully isolate DAF's contribution.
5. Clarify the design rationale for the bilinear text refinement module (Eq. 4) and consider ablating simpler alternatives.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>