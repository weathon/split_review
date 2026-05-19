- Decision: Reject
- Avg Score: 4.20
- Scores: 5, 3, 5, 3, 5
Now I have a thorough understanding of the paper and the reviewer inputs. Let me produce the final consolidated review.

## Summary
The paper introduces OrthSR, an orthogonal fine-tuning method for CLIP that injects Cayley-parameterized orthogonal matrices into the FFN layers of both image and text encoders, combined with a self-regularization (KL distillation from the frozen pretrained model) and attentive CutOut data augmentation. The method is evaluated on base-to-base/base-to-new generalization, cross-dataset transfer, and domain generalization across 11 datasets.

## Strengths
- **Strong novel-class generalization on standard benchmarks.** Table 1 shows OrthSR achieves 76.55% novel accuracy averaged over 11 datasets, outperforming all compared methods including CoOp (63.22%), CoCoOp (71.69%), MaPLe (75.14%), and PromptSRC (76.10%). The harmonic mean of 80.02% also surpasses all baselines. This is a concrete, reproducible result on widely-used benchmarks.
- **Self-regularization is empirically shown to be necessary.** The ablation in Table 4 (row 4) shows removing the KL-divergence loss drops novel accuracy by 1.46% (from 76.55 to 75.09) and HM by 0.94% (from 80.02 to 79.08). This provides clear evidence that the bypass-regularization strategy prevents harmful deviation from the pretrained manifold.
- **Inference efficiency matches lightweight baselines despite more trainable parameters.** Table 5 reports OrthSR achieves 645 fps, identical to CoOp and far exceeding CoCoOp (37 fps) and MaPLe (282 fps). This is because orthogonal matrices can be merged with frozen weights at deployment, adding no inference latency — a practically meaningful advantage.
- **Domain generalization consistently exceeds LoRA_CLIP.** Table 5 shows OrthSR surpasses LoRA_CLIP on all four out-of-distribution targets (ImageNet-V2, -Sketch, -A, -R) by margins of 1.1–10.6 points, suggesting orthogonal tuning better preserves distributional robustness than low-rank adaptation.

## Weaknesses

### Fatal
None.

### Major
- **Parameter count asymmetry undermines attribution of improvements.** OrthSR uses 43.45M trainable parameters while competing methods use orders of magnitude fewer: CoOp (2,048), CoCoOp (35,360), VPT (13,824), PLOT (8,192), and MaPLe (3.56M). The paper acknowledges the higher parameter count (Section 4.2: "though our approach needs the most number of trainable parameters"), but the central claim — that orthogonal fine-tuning is the cause of the improvements — cannot be separated from the simple effect of increased capacity. No experiment controls for parameter count, so the observed gains could partially or entirely reflect the extra model capacity. A parameter-matched non-orthogonal baseline (e.g., a full-rank unconstrained matrix of the same dimensions) is essential to isolate the effect of orthogonality.

- **No ablation isolating the orthogonal constraint.** The ablation study (Table 4) tests which encoder is used, whether KL loss helps, and whether cutout helps, but does not test whether the orthogonality constraint itself provides any benefit. Comparing OrthSR against a variant where the learnable matrix `A` is *not* constrained to be orthogonal (same dimensions, same loss, no Cayley parameterization) is needed to determine whether the norm-preserving property drives the results. Without this, the paper's argument that orthogonality is responsible for the improvements is speculative.

### Minor
- **LoRA_CLIP comparison is claimed in the base-to-base/new setting but not shown in any table.** The text (Section 4.2) states "our method surpasses the comparative LoRA_CLIP with 2.74%, 6.15% and 4.95% of base, novel and HM evaluation," but LoRA_CLIP does not appear in Table 1 (base-to-base/new). LoRA_CLIP appears only in the cross-dataset and domain generalization tables. The base-to-base/new comparison with LoRA_CLIP should be either tabulated or the text should clarify where these numbers come from.

- **"Gain" column in Table 1 is undefined.** The "Gain" column with Δ notation appears in Table 1 but the caption does not explain which baseline it is computed against. The values appear to be improvement over CoOp, but this is never stated, making the table harder to interpret.

- **Theoretical analysis is too generic to be informative.** Theorem 1 presents a generalization bound with undefined constants (`C''`), an unspecified term `λ^{2α}` where `α > 0` is not defined, and no proof. The bound does not connect to the specific structure of orthogonal fine-tuning — the same bound would apply to any method using a knowledge distillation loss. This section does not substantiate why orthogonality helps and reads more like a generic bound sketch than a meaningful theoretical contribution.

- **Attentive CutOut description has an ambiguity.** The method for computing the similarity map is described as "cosine similarity between image patch tokens and [CLS] text token" (Section 3.4). CLIP's text encoder uses `[SOS]` and `[EOS]` tokens, not `[CLS]`; the image encoder uses `[CLS]` for the class token. This ambiguity should be resolved for reproducibility.

### Trivial
- None that warrant mention here.

## Nice-to-Haves
- Report training cost details (GPU memory, time per epoch). With 43M trainable parameters vs. 2K for CoOp, this is material for practitioners evaluating the practical trade-off.
- Add hyperparameter sensitivity analysis for λ₁ and λ₂. The current values (1.5 and 1) are presented without justification or a sweep.

## Removed Points
The following points from the reviews were removed with justification:
- **"Parameter issue not acknowledged anywhere"** — The paper does acknowledge it (line 345: "though our approach needs the most number of trainable parameters"). The core concern about unfair comparison is retained as Major, but the "not acknowledged" claim is factually incorrect and removed.
- **"Motivation shift (HE preservation vs. minimization)"** — The paper's motivation is clear: orthogonality preserves pretrained hyperspherical energy. The method does not claim to reduce HE; it claims to preserve it. This is a misunderstanding.
- **"Method Section 3.2 — A applied to input vs. weights"** — The paper writes `W = A·W0` (line 97), which is applying A to the weight matrix. The critic's reading is incorrect.
- **"Statistical significance / error bars"** — Not reporting error bars is standard practice in this line of work (CoOp, CoCoOp, MaPLe, PromptSRC all follow the same convention). This is not a weakness specific to this paper.
- **"Abstract phrasing about boosting CLIP and CoOp"** — A minor phrasing issue that does not affect the paper's scientific content.
- **Training cost details** — Moved to Nice-to-Haves; the paper already reports parameters and inference fps.
- **Missing comparison with full fine-tuning** — Moved to Nice-to-Haves; not central to the paper's claims.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a perspective that meaningfully reframes or extends what the paper itself says.

## Suggestions
1. **Add a non-orthogonal parameter-matched baseline.** Replace the orthogonal matrix `A` with an unconstrained full-rank matrix of the same dimensions, trained with the same loss. If OrthSR outperforms this baseline, the orthogonal constraint is the cause. This single experiment would most directly address the central attribution question.
2. **Tabulate the LoRA_CLIP comparison for base-to-base/new** alongside the other baselines in Table 1.
3. **Define the "Gain" column** explicitly in the table caption.
4. **Either substantiate the theoretical analysis** with a proof that connects to the orthogonal structure, or remove it to avoid giving a false impression of rigor.
5. **Clarify the CutOut token reference** — specify exactly how the text embedding for patch-text similarity is obtained.
