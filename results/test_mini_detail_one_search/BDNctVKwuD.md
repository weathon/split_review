## Summary

This paper identifies a theoretical limitation of HiResCAM explanations: they are not uniquely determined from the softmax probabilities and can shift by an arbitrary matrix M without changing predictions. The authors propose ContrastiveCAMs, which are invariant to this shift and provide class-versus-class explanations. Using ContrastiveCAMs, they show that models often rely on non-core regions, and introduce Core-Focused Cross-Entropy (CFCE), a modified loss that penalizes non-core contributions while encouraging attention on core regions. Experiments on Hard-ImageNet, Oxford-IIIT Pets, and PASCAL VOC show dramatic improvements in feature alignment (IoU from ~30%→93% on Hard-ImageNet) while maintaining competitive accuracy, with approximate masks (SAM, bounding boxes) being viable substitutes for ground-truth masks.

## Strengths

- **Theorem 3.2 identifies a genuine, non-trivial failure mode of HiResCAMs.** The proof that HiResCAMs can be additively shifted by an arbitrary matrix M while producing identical softmax probabilities is a novel theoretical contribution. This is not merely softmax shift-invariance recycled—the paper shows this invariance amplifies from a scalar a to a full matrix M in spatial dimensions, which is specific to how CAMs connect to logits (Eq. 3). Figure 1 provides a concrete illustration of the effect.

- **ContrastiveCAMs (Defs. 3.3, 3.4) are proven M-invariant (Theorem 3.5) and provide class-versus-class explanations.** This directly addresses the identified limitation, and the pairwise explanation format yields additional information not available from standard CAMs, as demonstrated qualitatively in Figure 2.

- **CFCE (Definition 4.5) is grounded in a constrained risk minimization objective (Definition 4.4) and proven consistent (Theorem 4.6).** Proposition 4.2 dissects cross-entropy into core/non-core contributions via ContrastiveCAMs, providing a clean theoretical basis for why standard CE can encourage reliance on non-core regions. The consistency theorem shows that optimizing the CFCE risk converges to the Bayes-optimal core-constrained risk in the realizable setting.

- **Large quantitative gains in feature alignment on Hard-ImageNet (Table 2).** CFCE+KL achieves ContrastiveCAM IoU of 93.39% (vs. 30.27% for CE w/ Arch) and Gray Mask accuracy drops to 45.49% (vs. 76.53% for CE w/ Arch), indicating the model has shifted from relying on non-core regions to core regions. These are dramatic improvements over strong baselines (CORM, DFR).

- **Approximate masks work competitively (Section 5.2).** CFCE with SAM-generated masks achieves IoU of 83.95% vs. 92.72% with ground-truth masks on Oxford-IIIT Pets binary setting, showing the method does not require expensive pixel-perfect annotations. Bounding boxes also work well, and the paper correctly notes KL regularization should not be used with boxes.

- **Downstream segmentation improvements (Section 5.3).** Backbones pre-trained with CFCE+KL consistently improve IoU on PASCAL VOC segmentation, particularly in the end-to-end setting, demonstrating that core-focused training transfers to dense prediction tasks.

## Weaknesses

### Fatal
None.

### Major

- **CFBCE — the multilabel adaptation used for PASCAL VOC — is not defined in the main text.** The PASCAL VOC table (lines 426-427) lists "CFBCE" and "CFBCE + KL" results, but the reader can only find the definition by consulting the appendix (which was stripped by the parser). How ContrastiveCAMs are aggregated for multiple positive classes is a non-trivial extension that deserves at least a brief description in the main paper. This hurts the paper's self-containedness for readers primarily interested in the multilabel setting.

- **ContrastiveCAMs are not quantitatively validated against HiResCAMs on faithfulness metrics.** The paper's central claim is that ContrastiveCAMs provide "more faithful attention maps" (abstract, line 68), but the quantitative experiments primarily evaluate the downstream CFCE training loss, not ContrastiveCAM itself. There is no comparison of, e.g., deletion/insertion curves, pointing-game accuracy, or any faithfulness metric that would directly demonstrate that the M-invariance translates into empirically more reliable explanations. The redundancy ratio γ (Table 1) shows the removed component is non-negligible (20-37%), but this does not establish that HiResCAMs are *actually* less faithful—only that there exists a redundancy that ContrastiveCAM removes.

### Minor

- **Framing of the HiResCAM limitation is slightly overstated.** The paper claims HiResCAMs "fail to guarantee a faithful interpretation" (line 148) and the spurious shift can "completely corrupt" explanations. For a *fixed trained model* with specific weights, the logits and resulting HiResCAMs are uniquely determined. The ambiguity is about the inverse mapping from probabilities to CAMs—which is a valid theoretical observation, but does not mean that the actual CAM computed from a given model is corrupted in practice. The ContrastiveCAM proposal is well-motivated regardless; this is a framing issue more than a technical one.

- **Hyperparameter values (λ₁, λ₂, λ₃) are omitted from the main text.** The regularized loss (Definition 4.7) introduces three hyperparameters whose values, sensitivity, or selection criteria are not discussed. While these are likely in the appendix, including a brief note or table would improve reproducibility and help readers assess how sensitive the method is to these choices.

- **No systematic study of sensitivity to mask quality.** The SAM and BBOX experiments are a good start, but there is no analysis of how performance varies with, e.g., SAM threshold values, or with controlled corruption of ground-truth masks. The gap between GT (92.72% IoU) and SAM (83.54% IoU) in the binary setting is non-trivial, and the paper does not investigate whether this gap is primarily due to mask quality or some other factor.

### Trivial
None.

## Nice-to-Haves

- An ablation study that removes the absolute-value non-core suppression term, or replaces the KL divergence with a simpler L₂ penalty, would clarify which component of CFCE drives the alignment improvement.
- Including an explanation faithfulness baseline (e.g., Right-for-the-Right-Reasons or saliency-map regularization) would further contextualize the improvements.
- A quantitative faithfulness comparison of ContrastiveCAM vs. HiResCAM (e.g., deletion/insertion on Hard-ImageNet) would directly validate the claim that M-invariance produces more reliable explanations.
- The "CE w/ Arch" baseline zeroes the bias of the final linear layer. While the paper does mention this (line 225), making this more explicit where the baseline is first introduced would improve clarity.

## Removed Points

These points were raised by reviewers but are removed after verification against the paper:

- **"The 'w/ Arch' architectural modification is not described."** — *Removed.* The paper explicitly states at line 225: "By zero-ing the final bias vector (i.e., b := 0_C for h only)."
- **"Missing comparison to Right-for-the-Right-Reasons or saliency-map regularization."** — *Removed.* The paper already compares against CORM and DFR, which are the most relevant baselines for core-risk minimization. The cited methods operate in a different paradigm (regularizing input gradients rather than feature-attribution maps).
- **"The loss is ad-hoc and not derived from a principled framework."** — *Removed.* The loss is explicitly derived from the Core-Constrained Risk Minimization objective (Definition 4.4) and a consistency theorem (Theorem 4.6) is provided. The absolute-value modification is a natural relaxation of the constraint in Eq. (14).
- **"Missing details about CFBCE in the main text."** — *Retained above as a Major weakness.* This is a genuine omission; the other parts of the criticism were more generic.
- **Strength Finder: "addressed an important problem," "targeted an interesting question."** — *Removed.* These are generic/superficial and lack specific evidence.

## Novel Insights

None beyond the paper's own contributions. However, one observation emerges from the intersection of the two reviews: the paper's theoretical analysis (HiResCAM non-uniqueness → ContrastiveCAM → CE-core/non-core decomposition) is genuinely novel as a chain, but the empirical validation focuses almost entirely on the last link (CFCE improves alignment). The intermediate link (ContrastiveCAM is more faithful than HiResCAM) is argued theoretically but not empirically tested. This suggests a natural extension: a direct head-to-head faithfulness comparison would complete the chain and significantly strengthen the paper's narrative.

## Suggestions

1. **Define CFBCE explicitly in the main text** — even a one-sentence description of how ContrastiveCAMs are aggregated over multiple positive classes for multilabel BCE would suffice.
2. **Add a quantitative faithfulness experiment** comparing ContrastiveCAM vs. HiResCAM on a standard metric (e.g., deletion/insertion on Hard-ImageNet) to directly validate the M-invariance claim.
3. **Report hyperparameter values** (λ₁, λ₂, λ₃) in a brief table in the main paper, and consider a small sensitivity analysis varying λ₁.
4. **Tone down the characterization of the HiResCAM limitation** — the theoretical observation is valid and well-motivated, but describing it as causing HiResCAMs to "fail to guarantee a faithful interpretation" risks overstatement. The paper's own experiments show HiResCAM-based IoU at 30.27% (CE w/ Arch baseline) can be a useful signal.

## Score and Decision

**Anchor Papers (calibration batch):**

| Paper | Avg Score | Comparison |
|---|---|---|
| Unlearning-based Neural Interpretations (PBjCTeDL6o) | 8.00 | Stronger experimental breadth across multiple models and faithfulness metrics; our paper has slightly more novel theoretical contribution but narrower empirical validation |
| Interpreting CLIP (5Ca9sSzuDp) | 8.00 | Deeper mechanistic analysis of model internals; our paper addresses a different problem with less analytical depth but more practical training intervention |
| How to Probe (57NfyYxh5f) | 6.25 | Similar topic area (training-layer effects on explanations); our paper has stronger theoretical grounding and a more extensive empirical evaluation of the proposed method |
| Simple Interpretable Transformer (bkdWThqE6q) | 6.00 | Comparable paper quality; our paper provides more theoretical novelty (theorems with proofs) while the anchor has a different contribution (architecture design) |
| Learning Causal Alignment (ozZG5FXuTV) | 6.00 | Similar structure of using explainability to guide training; our paper's theoretical contribution (M-invariance) is more specific and provable |
| Conceptualize Any Network (wZiH43e5Ah) | 3.00 | Much weaker empirical validation and less clear contribution; our paper is substantially stronger |
| Counterfactual Image Generation (WYsLU5TEEo) | 2.50 | Poorly motivated, unclear writing, very limited experiments; our paper is far superior in all dimensions |

The paper makes a genuine theoretical contribution (HiResCAM non-uniqueness, ContrastiveCAM M-invariance), grounds the training loss in a constrained optimization framework with consistency guarantees, and demonstrates large empirical improvements across three datasets. The weaknesses are about missing details (CFBCE definition, hyperparameters) and a missing empirical link (ContrastiveCAM faithfulness validation) rather than any fatal flaw. Relative to the calibration anchors, the paper sits clearly above the 6.0-6.25 papers in theoretical novelty and empirical strength, but below the 8.0 papers in experimental breadth and depth.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>