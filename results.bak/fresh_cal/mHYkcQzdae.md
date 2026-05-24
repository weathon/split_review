Here is the consolidated final review:

## Summary

This paper proposes a dual-stream micro-expression recognition (MER) network combining a Continuous Vertical Attention (CVA) block that models vertical facial muscle movement, a Facial Position Focalizer (FPF) based on Swin Transformer for position embedding, and Action Unit (AU) embeddings. The model is evaluated on CASME II and SAMM datasets, reporting 94.35% and 86.76% accuracy respectively.

## Strengths

- **Vertical attention direction validated through controlled comparison**: Table 3 compares vertical-only, horizontal-only, and both-direction attention while holding FPF and AU fixed, providing direct evidence that vertical attention outperforms the alternatives. This supports the design choice that vertical muscle movement is more discriminative for MER.

- **Swin Transformer vs. ViT comparison (Table 5)**: The paper systematically compares Swin Transformer against ViT as the backbone for the FPF module, with both using CVA and AU. The Swin-based variant outperforms ViT on both datasets, providing empirical support for the claim that Swin's shifted window mechanism better captures long-range dependencies for facial position encoding.

- **Continuous vs. independent attention comparison (Table 4)** and **dual-frame vs. single-frame input comparison (Table 6)**: These ablations isolate specific design decisions (using previous-layer attention maps and using both onset+apex frames), giving the reader confidence that these components contribute positively to the overall system.

- **Comprehensive ablation structure**: Across Tables 2-7, the paper systematically evaluates each module (AU, CVA, FPF, vertical vs. horizontal, continuous vs. independent, Swin vs. ViT, single vs. dual frame), providing a clear picture of how each design choice affects performance.

## Weaknesses

### Fatal

None.

### Major

- **Ground-truth AU labels create an unfair comparison that undermines the headline SOTA claims.** The paper inputs binary AU vectors (Section 3.3) from the dataset's ground-truth annotations (Section 4.1: "we utilized only the binary 01 information representing whether AUs were active or not") as input during both training and inference. This is oracle-level privileged information unavailable to baseline methods without external AU detectors. The ablation in Table 7 shows AU alone contributes ~4–5% accuracy improvement on both datasets. When the paper claims "outperformed MMNet by 6%" and "higher accuracy rates than μ-BERT ... with 1.98% and 10.87%," the comparison is fundamentally asymmetric if those baselines do not also receive ground-truth AU labels. The paper does not discuss this asymmetry. This is the most significant weakness: the SOTA comparison is not apples-to-apples unless the AU embeddings are either (a) removed from the comparison, (b) replaced with predicted AU from a jointly trained detector, or (c) the baselines are also augmented with oracle AU.

- **No variance estimates reported for any result.** The paper reports single-point accuracy and F1 values throughout without standard deviations, confidence intervals, or per-fold breakdowns. CASME II (255 videos, 26 subjects) and SAMM (159 videos, 32 subjects) are small datasets; under LOSO cross-validation, performance can vary substantially across folds. The reported improvements (e.g., the 0.62% difference between vertical and both-direction attention on CASME II, or the 1.98% improvement over μ-BERT on SAMM) are not interpretable without knowing whether they exceed the fold-to-fold variance. This is a basic expectation for any empirical paper making comparative claims.

### Minor

- **The ablation baseline (ResNet-18) is weak and the reported gains conflate multiple factors.** Table 2 shows adding all three components to ResNet-18 yields 13.23%/13.2% accuracy gains. However, this includes the AU oracle (~4–5% alone), and the ResNet-18 baseline's training configuration is not described. The paper would benefit from an additional ablation on a stronger backbone (e.g., the full model's Swin Transformer backbone without CVA/FPF/AU) to better isolate the contribution of each component beyond what a generic, potentially suboptimal baseline provides.

- **Inconsistent framing of improvement magnitudes.** The abstract states "improved by 6% and 1.98% compared to state-of-the-art models" (pairing 6%→CASME II, 1.98%→SAMM). The text later says the model beats μ-BERT by 10.87% on CASME II and 1.98% on SAMM, and MMNet by 6% on CASME II. The 10.87% figure is the largest improvement on CASME II but is omitted from the abstract. While these compare against different baselines, the abstract's framing is selective and could mislead a casual reader about the magnitude of gains.

- **"Facial Position Focalizer" description overstates the mechanism.** The FPF module feeds onset and apex frames through a Swin Transformer encoder and sums the resulting feature maps (Section 3.2). There is no explicit spatial localization or focalization mechanism beyond standard self-attention. The name suggests a dedicated localization module, but the actual operation is a standard Swin encoding + element-wise addition.

- **Missing implementation details needed for reproducibility.** The ViT setup (patch size, depth, training details) used in the Swin vs. ViT comparison (Table 5) is not described. The random seed is not reported. The weight decay of 0.6 is unusually high relative to typical values (0.0001–0.1) and is not justified. The learning rate schedule ("exponentially decayed during the first 50 epochs out of 75") is imprecise (no decay factor specified).

- **The activation function $F_{act}(x)=x\cdot ReLU(x+3)/6$ is introduced without motivation or citation** (Section 3.1). A brief justification of why this particular form was chosen would aid understanding.

### Trivial

- Section numbering has a formatting issue: Sections 3.1, 3.2, 3.3 appear under "3 METHOD" but are numbered as if they are subsections of Section 3; however "3.1" is also written as a separate \section command, creating redundancy.

## Nice-to-Haves

- Reporting per-fold accuracy with mean±std for the LOSO protocol would dramatically strengthen the evaluation.
- Including an experiment where AU is predicted (rather than oracle) from facial appearance would demonstrate practical deployability and close the fairness gap with baselines.
- Reporting parameter counts and FLOPs for the proposed model vs. baselines would help assess practical trade-offs.
- Attention map visualizations showing what the CVA module focuses on (vertical regions) vs. a baseline model would provide qualitative support for the vertical-attention claim.

## Removed Points

- **"Notation errors in CVA equation"** (Harsh Critic): The critic claims $P_M(Attn^{i-1})$ is problematic because "$Attn^{i-1}$ is a scalar map." However, $AttnY^{i-1}$ is defined as the attention map from the previous layer — a 2D spatial map — and $P_M$ is max pooling along height and width. The notation is coherent. **Removed: factually incorrect criticism.**
- **"ResNet-18 is poorly tuned"** (Harsh Critic): The critic speculates without evidence that the baseline is suboptimally configured. The 13% gain is largely driven by AU oracle. **Removed: speculative claim, not falsifiable from the paper.**
- **"No code or pre-trained models provided"** (Harsh Critic): The Hard Rules instruct removing nitpicks about reproducibility that involve artifacts impractical to include. Code release is a venue-specific policy expectation, not a scientific validity criterion. **Removed per Hard Rules.**
- **"Broader comparison to concurrent methods like OFF-ApexNet, CapsuleNet, etc."** (Harsh Critic): The Hard Rules prohibit mentioning missing related works as the reviewer cannot confirm their relevance without external knowledge. **Removed per Hard Rules.**
- **"Weight decay of 0.6 could indicate overfitting"** (Harsh Critic): This is speculative without evidence of overfitting (e.g., training vs. validation curves). **Removed: speculation.**
- **"SAMM class mapping needs justification"** (Harsh Critic): The paper states "Consistent with most other MER methods" — this is adequate justification for a standard experimental choice. **Removed: scope creep.**
- **Strength: "State-of-the-art results with quantified gains"**: This conflicts with the verified weakness about AU oracle making comparison unfair. **Removed per filtering rule that weakness wins when strength and weakness disagree.**

## Novel Insights

None beyond the paper's own contributions. The reviews surface the structural asymmetry introduced by ground-truth AU embeddings, but this is a straightforward observation once the paper's input setup is examined.

## Suggestions

1. **Remove or replace the AU oracle in the main evaluation.** The cleanest path is to present the full model (CVA + FPF + AU) as one variant and a version without AU as another, and compare *both* to baselines. Only the no-AU variant should be used for SOTA comparisons; the AU variant can be presented as an upper-bound ablation.
2. **Report per-fold accuracy (mean ± std) for the LOSO protocol** on all main and ablation experiments. This is essential for interpreting whether reported margins (e.g., 0.62%, 1.98%) are meaningful.
3. **Clarify the numerical claims in the abstract** to specify which baseline each improvement is measured against.
4. **Add the missing implementation details**: random seed, ViT configuration for the comparison experiment, learning rate decay factor, and the ResNet-18 training setup used in the ablation.

## Score and Decision

The paper proposes a reasonable dual-stream architecture with sound ablations that individually validate each design choice. However, the central evaluation is compromised by the use of oracle AU labels — the reported SOTA improvements cannot be attributed to the proposed CVA and FPF modules because the baselines do not receive the same privileged UI information. The lack of any variance estimates further weakens the comparative claims. These are not minor fixes; they require restructuring the experimental setup and re-running comparisons. The paper is not ready for publication in its current form.

**Score: 4.5**

**Decision: Reject**

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>