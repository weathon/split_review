Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper introduces L2C (Learning to Complement), a method for Few-Shot Test-Time Domain Adaptation (FSTT-DA) with frozen CLIP. It proposes a parallel side network (CPNet) with revert attention to learn dataset-specific visual knowledge that complements CLIP's generalized features, enhances text feature inter-dispersion via greedy ensemble and refinement, and fuses both modalities through a domain-aware fusion mechanism guided by a learned domain prompt. Experiments on DomainNet and four WILDS benchmarks show consistent improvements over VDPG and other baselines, with notable gains on WILDS using the smaller ViT-B/16 backbone (+5.1 F1 on iWildCam, +3.1% WC Acc on FMoW).

## Strengths

- **Parallel CPNet with revert attention provides a principled way to learn dataset-specific knowledge that complements frozen CLIP features.** Section 4.1 defines the mechanism, and ablation Table 3 (Index 1 vs. 2) shows large gains from adding CPNet (e.g., +13.1 F1 on iWildCam), with revert attention providing additional improvement (Index 4 vs. 5). The design is well-motivated — CPNet focuses on information CLIP's generalized features miss — and ablation confirms its effectiveness.

- **Greedy text ensemble and lightweight refinement improve text feature inter-dispersion, benefiting downstream adaptation.** Section 4.2 describes the greedy selection algorithm and the refinement module with uniformity loss. Table 3 (Index 3 vs. 4) confirms gains from greedy ensemble, Table 6 shows its advantage over simple average pooling, and Figure 6 demonstrates the correlation between lower uniformity (higher inter-dispersion) and better accuracy.

- **Domain-aware fusion (DAF) with a learnable K-V cache and batch-level attention is a well-designed mechanism for adapting both visual and text features to a specific target domain.** Section 4.3 describes the construction of domain prompts from queried source knowledge and batch-aggregated domain information. Ablations (Table 3 Index 6 vs. 8, Table 4, Table 5) verify the importance of each design choice.

- **Strong empirical results on challenging WILDS benchmarks with the smaller ViT-B/16 backbone demonstrate practical value.** Table 1 reports improvements of +5.1 Macro F1 on iWildCam and +3.1% worst-case accuracy on FMoW over VDPG using ViT-B/16 — notable gains on benchmarks where CLIP's zero-shot performance is low and VDPG degrades significantly.

- **Domain-centric training scheme (Table 3 Index 7 vs. 8) properly aligns training with the test-time adaptation protocol, and extensive ablations (Fig 4, 5, Tables 3–6) systematically validate each design choice.** The thorough ablation study makes the contribution of each component transparent.

## Weaknesses

### Fatal

None.

### Major

- **Missing key training and architecture details for reproducibility.** The paper does not specify: (i) the batch size $B$ used during training or inference, (ii) the number of CPNet layers used for each WILDS dataset (only DomainNet is stated as 3 layers for ViT-B/16, line 67), (iii) the cache size $L$ for the K-V domain cache (defined in Eq. 5 but never given a value), and (iv) the exact architecture of the DAF module (number of cross-attention layers, hidden dimensions). For a method with as many tunable components as L2C — where design choices are acknowledged to be data-dependent (Fig. 4 shows sensitivity to CPNet depth per dataset) — these omissions are a genuine barrier to independent verification and use by other researchers.

- **No statistical significance or variance reporting.** All results in Tables 1 and 2 are reported as single numbers without standard deviations or confidence intervals. The improvements on DomainNet are modest (+1.4% with ViT-B/16, +2.2% with ViT-L/14), and without run-to-run variance estimates it is unclear whether these gains exceed typical noise. The strongest claims (e.g., WILDS improvements) would also benefit from error bars. While single-run evaluations are common in parts of this literature, they weaken the evidence for a paper that draws definitive conclusions from these numbers.

### Minor

- **The phrasing "learning directly on the input space" is slightly imprecise.** CPNet operates on the patch token embeddings (`x^{in}` in the paper's notation), which are the output of CLIP's patch embedding layer — not raw pixels. The contrast with VDPG (which operates on CLIP's output features) is valid and clear in context, but the term "input space" could mislead readers into thinking CPNet processes raw pixels. This does not affect the method's validity but is a presentation issue.

- **The "gradient-free" characterization (Related Work, line 39) is somewhat oversold without qualification.** During test-time adaptation, L2C indeed does not require gradients through CLIP, which is a useful property. However, CPNet itself is trained with backpropagation on source domains, so calling the overall method "gradient-free" without distinguishing training from adaptation could be misleading.

### Trivial

- Some algorithm descriptions in the text (lines 137–139) appear truncated or garbled, likely due to PDF extraction artifacts. The authors should ensure clean pseudocode is included in the final version.

- The paper would benefit from explicitly stating the batch size used in experiments, and the number of CPNet layers per dataset in the main architecture description rather than leaving it implicit from Fig. 4.

## Nice-to-Haves

- **Sensitivity to support set size.** The paper fixes 16 images for adaptation but does not vary this (e.g., 4, 8, 16, 32). Evaluating robustness to this hyperparameter would strengthen the analysis.

- **Computational cost comparison.** Reporting adaptation time (seconds per domain) or FLOPs for L2C vs. VDPG would be helpful since the paper claims CPNet is lightweight (§4.1) but DAF involves multiple cross-attention operations.

- **Visualization of CPNet vs. CLIP features.** Attention maps or feature visualizations showing that CPNet captures complementary (e.g., domain-specific texture) information would strengthen the core claim.

- **Evaluation with additional backbones** (e.g., ViT-H/14, ResNet-based CLIP) would demonstrate generality beyond the two architectures tested.

## Removed Points

*These points were removed per hard rules; they should be treated with caution and not used for evaluation.*

- **Missing TPT comparison.** The harsh critic faulted the paper for not comparing against Test-Time Prompt Tuning (Shu et al., 2022). Per the reviewer guideline, missing related work comparisons are not included as weaknesses since external sources cannot independently confirm the applicability of every possible baseline to this specific setting. TPT operates at the instance level (single-image adaptation with augmentations), while L2C operates at the domain level (batch of unlabeled samples from a domain), making direct comparison non-trivial and protocol-dependent.

- **Criticism that "black-box" claim is misleading.** The reviewer argued CPNet requires access to patch embeddings. The paper's contrast is with methods that modify intermediate backbone layers, and CPNet operating in parallel on inputs and outputs is a reasonable use of "black-box" in this context.

- **Several section-by-section notes about missing appendix content and garbled pseudocode** — these are PDF parsing artifacts, not author errors.

- **"Related work does not differentiate L2C from side networks convincingly"** — the paper explicitly explains the difference (CPNet does not require intermediate feature access; line 41).

## Novel Insights

The most interesting insight from the reviews is the tension between the paper's core framing and its actual innovation. The paper presents itself as "learning from the input space," which the reviewers correctly identified as overclaimed (CPNet operates on learned patch embeddings, not raw pixels). However, the real contribution that emerges from reading the paper alongside the reviews is more nuanced: the revert attention mechanism provides a simple but effective inductive bias for a side network to learn *complementary* rather than redundant information relative to a frozen foundation model. This is a clean design principle — use 1−softmax(attention) to force the side network to attend to what the main network finds least relevant — and it is validated by ablation (Table 3 Index 4 vs. 5). The reviewers did not fully explore this design principle's potential applicability beyond FSTT-DA (e.g., to other settings where a small model should complement a large frozen one), but it is arguably the most transferable idea in the paper.

## Suggestions

1. **Add a reproducibility appendix** with batch size, cache size $L$, CPNet depth per dataset × backbone combination, and DAF architecture details (number of cross-attention layers, hidden dimensions). This is the most actionable fix.
2. **Report results with at least 3 random seeds** for the main tables, with standard deviations. If computational cost is prohibitive, at minimum run multiple seeds for the DomainNet experiments where gains are small.
3. **Clarify the phrasing** around "input space" (e.g., say "at the patch embedding level, before the CLIP transformer encoder") and qualify "gradient-free" to distinguish training from test-time adaptation.
4. **Include the support set size ablation** (4, 8, 16, 32) as a natural extension — it directly tests the "few-shot" claim and would add robustness evidence.
5. **Provide a computational cost comparison** (inference time per domain) with VDPG, since L2C adds a transformer side network and cross-attention fusion.

## Score and Decision

The paper presents a methodically designed approach with strong empirical results on challenging benchmarks, particularly for the practically important scenario of adapting smaller CLIP backbones (ViT-B/16) to difficult real-world domains. The ablations are thorough and the component contributions are convincingly isolated. The missing reproducibility details (batch size, cache size, CPNet depth per dataset) and lack of variance reporting are the most significant issues, but both are addressable in a revision. The core methodology is sound and the empirical gains on WILDS are meaningful.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>