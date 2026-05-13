Now let me check the Strength Finder's claim about "black-box applicability" — this conflicts with the Harsh Critic's concern. Let me verify what the paper actually says.

The paper says: "Our CPNet operates independently in parallel and complements the CLIP visual features only at the output, making the framework flexible for black-box settings." 

The Harsh Critic argues that accessing CLIP's full feature representations (l+1 tokens × d dimensions) is not black-box access. But the critical distinction is: the paper explicitly says it accesses CLIP's **output** features, not intermediate activations. Methods like HybridPrompt/ProD insert prompts into intermediate CLIP layers, which genuinely requires white-box access. Getting the final output of a model is more like what a feature-extraction API provides. This is a much weaker form of "black-box" than truly no-access, but it's a legitimate claim in the context of the comparison group, where "black-box" contrasts with methods requiring access to internal weights and intermediate activations.

The "black-box" claim is somewhat imprecise but not outright wrong — the paper contrasts with methods that modify internal layers, and CPNet only operates on CLIP's final output. This is a reasonable use of "black-box" in context, though it could be more precisely stated as "output-level only access." This is a minor presentation concern, not a fatal flaw.

Let me also verify the Eq. 1 ambiguity claim. The paper says:

> `A = 1 − softmax(CP(x^in) · I(x^in))`

Both CP(x^in) and I(x^in) are R^{1×(l+1)×d}. The paper says "We employ the Scaled Dot-Product Attention method" — this references the Vaswani et al. (2017) attention mechanism. In standard scaled dot-product attention, the similarity would be computed as Q·K^T/√d, producing a (l+1)×(l+1) attention matrix, with softmax along one dimension. However, here CP(x^in) acts as queries and I(x^in) as keys. The notation `CP(x^in) · I(x^in)` could mean:
- A matrix multiplication giving R^{1×(l+1)×(l+1)} (full pairwise)
- Or some other operation

The reference to "Scaled Dot-Product Attention" provides context but the exact dimensionality of the softmax remains ambiguous. This is a valid reproducibility concern but not fatal — the reference gives enough context to figure out the likely implementation.

Now let me assess the claim about CPNet being "lightweight" and the concern about missing parameter/FLOPs comparison. The paper says CPNet uses "only 3 transformer blocks" (matching CLIP's dimension of 768). For ViT-B/16, this means approximately 3 × ~7M = 21M parameters, compared to prompt-tuning methods that may add only a few hundred thousand. This is a valid concern about the claim of "lightweight" and whether the gains come from capacity or mechanism.

However, the ablation in Table 3 (Index 2 vs. 5) shows that adding RT to CPNet gives incremental gains — but the big jump is Index 1 (zero-shot) → Index 2 (CPNet without RT). The Harsh Critic's concern that this conflates "having a side branch" with "learning complementary knowledge via RT" is partially valid, but the paper does show Index 4 vs. 5 for RT contribution, which is meaningful.

Let me also verify the "gradient-free" claim in Section 2. The paper says "Our work introduces a practical, gradient-free adaptation method, enabling model deployment in black-box environments." But CPNet is trained with gradients. This appears in the Related Work section, so it might be describing VDPG's approach rather than L2C's. Let me re-read.

Looking at the context: "However, these prompts are inserted into various layers and require access to the weights of the base model. Therefore, they incur additional computational costs and pose challenges in scenarios where privacy concerns or proprietary models limit flexibility (An et al., 2022). Our work introduces a practical, gradient-free adaptation method, enabling model deployment in black-box environments."

This is in Section 2 (Related Work) and clearly claims gradient-free adaptation. But L2C trains CPNet with gradients! This is a misleading claim. Wait — "gradient-free" might refer to not computing gradients through the frozen CLIP model. But CPNet still requires gradient computation via backpropagation through CPNet itself. The term "gradient-free" is misleading.

Actually, re-reading carefully: the statement is "gradient-free adaptation method." At test-time inference, the domain prompt is generated and used to adapt features — possibly the adaptation step is gradient-free (using the pre-trained generator rather than gradient-based updates). But during training, CPNet is clearly trained with gradients. "Gradient-free" is misleading without qualification. This is a presentation issue.

Let me now write the consolidated review.

## Summary
The paper introduces L2C, a framework for few-shot test-time domain adaptation (FSTT-DA) that complements frozen CLIP features by attaching a parallel network (CPNet) that learns from the input space via a revert attention mechanism. It also proposes greedy text ensemble and refinement to enhance text feature inter-dispersion, and domain-aware fusion to adapt both modalities toward target domains. The method achieves substantial improvements over prior SOTA (VDPG) on WILDS benchmarks, particularly with smaller ViT-B/16 backbones (+5.1 F1 on iWildCam, +3.1% WC Acc on FMoW).

## Strengths
- **Empirically grounded motivation and meaningful improvements**: The paper is motivated by VDPG's failure on smaller backbones (ViT-B/16), a concrete and practically important problem. The gains on WILDS benchmarks (Table 1) are substantial and consistent, directly validating the core thesis that input-space complementation helps when feature-space-only methods falter.
- **Sound core idea for complementarity**: The revert attention mechanism (Eq. 1) is a principled approach to enforce that CPNet learns information not already captured by CLIP, rather than redundant knowledge. The ablation in Table 3 (Index 4 vs. 5) confirms it provides measurable gains.
- **Comprehensive ablations**: Table 3 provides progressive 8-row ablations isolating CPNet, revert attention, text refinement, greedy ensemble, L_uni, DAF, and training scheme. Tables 4–6 and Figures 4–6 further analyze domain prompt composition, aggregation methods, and hyperparameter sensitivity.
- **Practically efficient text processing**: The greedy text ensemble as a preprocessing step that allows discarding the text encoder entirely during training (Section 4.2, Algorithm 1) is a practical and effective design choice.
- **Consistent gains across benchmarks**: Beyond WILDS, Table 2 shows improvements on 4/6 and 5/6 DomainNet domains with ViT-B/16 and ViT-L/14 respectively, demonstrating generalizability.

## Weaknesses

### Fatal
None.

### Major
- **No parameter count or computational cost comparison**: The paper claims CPNet is "lightweight" (using 3 transformer blocks at 768d on ViT-B/16, ~21M params) and introduces text refinement matrices M_c ∈ R^{|C|×|C|} that scale as O(|C|²). Yet no comparison of total trainable parameters, FLOPs, or inference time is provided against baselines (whose only trainable component is often a small prompt generator). The large performance jump from Index 1→2 in Table 3 (zero-shot → CPNet) could partially reflect added model capacity rather than the proposed mechanisms. Without these comparisons, it is difficult to assess whether the gains stem from the methodological innovations or simply from adding a trainable side branch with substantial capacity. — This matters because it directly affects whether the paper's core claim (that revert attention, text refinement, and DAF are the key innovations) is supported.

- **Ablation does not cleanly isolate the contribution of revert attention from raw capacity**: In Table 3, CPNet without revert attention (Index 2) adds an entirely new trainable parallel network. The jump from Index 1→2 (+13.1 F1 on iWildCam) could be largely explained by capacity rather than the specific complementary learning mechanism. While Index 4→5 shows gains from adding RT, the fundamental comparison should be CPNet+RT vs. an equivalent-capacity network trained without RT using the same domain-aware fusion and training scheme. Without this control, it remains unclear whether RT's complementarity enforcement or simply having trainable parameters drives performance. — This weakens the paper's core contribution claim about revert attention.

### Minor
- **Imprecise "black-box" framing**: The paper repeatedly characterizes the method as suitable for "black-box environments" (Sections 1, 2) and claims it does not intervene in CLIP's internal processes. While it is true that CPNet accesses only CLIP's final output features (not intermediate activations like HybridPrompt/ProD), accessing the full output representation R^{1×(l+1)×d} requires at minimum a feature-extraction API, which is not a pure black-box interface. The framing should be clarified as "output-level access only" rather than "black-box" — the contrast with internal-layer methods is valid, but the terminology overclaims.

- **Equation 1 (revert attention) has ambiguous dimensionality**: Both CP(x^in) and I(x^in) are R^{1×(l+1)×d}. The notation `softmax(CP(x^in) · I(x^in))` does not specify the dimension over which softmax operates (per-token yielding (l+1) scalars, or as full scaled dot-product attention yielding (l+1)×(l+1) matrix). The reference to Vaswani et al. (2017) provides context, but as the central mechanism, exact specification would improve reproducibility.

- **M_c matrix scales quadratically with class count**: The text refinement M_c ∈ R^{|C|×|C|} (Eq. 4) scales as O(|C|²), which becomes expensive for datasets with large label spaces. This is not acknowledged as a limitation.

### Trivial
- The "gradient-free" claim in Section 2 ("Our work introduces a practical, gradient-free adaptation method") is misleading — CPNet is trained with gradients through the side branch. What is gradient-free is adaptation at inference time (the domain prompt is pre-computed), but this distinction is not made clear.

## Nice-to-Haves
- Comparison with recent parallel side-network / adapter methods (e.g., Ladder Side-Tuning, LPFT) beyond prompt-based baselines, since the architecture resembles side-tuning approaches.
- Visualization of revert attention patterns showing which image regions/tokens CPNet attends to when CLIP doesn't, making the complementarity claim more tangible.
- Sensitivity analysis on the number of unlabeled target samples (fixed at 16 throughout experiments), which would better characterize the "few-shot" aspect.

## Removed Points
*These points are flagged to be removed, treat them with caution*

- **Claim that the "black-box" framing is incorrect/fatal**: The harsh critic calls this a structural error that undermines a stated contribution. While the "black-box" terminology is imprecise, the paper's actual claim is that CPNet operates on CLIP's output features only, not requiring access to intermediate layers. This legitimately contrasts with HybridPrompt/ProD which inject prompts into internal layers. The claim is over-claimed but not fundamentally wrong — the method requires only output-level access, which is a meaningful distinction. Downgraded from fatal to minor.

- **Claim that CPNet can be "discarded after" domain prompt generation**: The harsh critic notes CPNet is used throughout training and inference. However, the paper actually says the K-V cache "can be discarded" after domain prompt generation at inference (Section 4.4/Algo 2), not CPNet itself. This is a misreading. Removed as factually incorrect.

- **O(m²l²) complexity of batch reshaping**: The harsh critic claims quadratic attention over ~3,152 tokens is "expensive and not discussed." Table 5 actually shows this outperforms alternatives, and the b=16 images with l=197 patches is bounded. The computational concern is valid but the paper discusses and empirically justifies the design. Moved to nice-to-have.

- **"Not yet released" or reproducibility concerns about cited models**: Per hard rules, these are removed.

- **Missing related works**: Per hard rules, cannot confirm existence of suggested works.

- **Strength Finder's "black-box applicability" strength**: Conflicts with the verified weakness about imprecise framing. Removed.

- **Strength Finder's generic strengths** like "addresses an important problem" — removed as superficial.

## Novel Insights
The paper's insight that VDPG's feature-space-only approach fails on weaker backbones (ViT-B/16), and that supplementing with input-space learning (CPNet) specifically benefits these scenarios, is well-motivated and empirically supported. The revert attention mechanism is a clean idea for enforcing complementarity without modifying the frozen model, though its practical advantage over simpler alternatives is under-verified.

## Suggestions
- Add a parameter count and FLOPs comparison table against all baselines. Report total trainable parameters for L2C including CPNet, DAF, text refinement, and K-V cache.
- Include an ablation that replaces CPNet+RT with an equivalent-capacity parallel network (same number of transformer blocks) trained without revert attention but with the same domain-aware fusion and domain-centric training. This would isolate the contribution of the complementarity enforcement mechanism.
- Tighten the "black-box" terminology to "output-level access only" throughout the paper, clarifying that this means no access to intermediate CLIP activations or weights.
- Clarify Equation 1 by explicitly specifying the matrix operations and softmax dimension.

## Score and Decision

The paper makes a solid contribution with meaningful empirical improvements on challenging benchmarks, motivated by a clear failure mode of prior work. The revert attention concept is sound. However, the two major weaknesses — (1) no parameter/FLOPs comparison making it impossible to distinguish mechanistic contributions from capacity gains, and (2) an ablation that doesn't cleanly isolate RT from raw capacity — together materially weaken the paper's core claim. These are addressable with additional experiments but are significant gaps as-is.

**Originality**: Moderate — the idea of parallel side-networks with complementarity enforcement is incremental from existing side-tuning literature, but well-adapted to the FSTT-DA problem.

**Importance of research question**: High — FSTT-DA with weak backbones is practically important and under-addressed.

**Claims well supported**: Partially — empirical results are strong, but the specific contribution claims (RT, text refinement) are not cleanly separated from capacity effects.

**Soundness of experiments**: Adequate but with the capacity gap in ablations.

**Clarity**: Generally clear, with some ambiguity in Eq. 1 and over-strong "black-box" framing.

**Value to community**: Solid — practical improvements on real-world benchmarks with a clean framework design.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>