Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper proposes a dual-stream network for micro-expression recognition (MER) that incorporates three components: (1) a Continuous Vertical Attention (CVA) module that focuses on vertical facial muscle movements, (2) a Facial Position Focalizer (FPF) module based on Swin Transformer for spatial localization, and (3) AU embeddings as auxiliary input. The authors report state-of-the-art results of 94.35% on CASME II and 86.76% on SAMM. The work is an incremental but reasonable extension of the MMNet architecture.

## Strengths

- **Vertical attention is validated as beneficial**: The ablations in Tables 3-4 show that vertical-only attention outperforms horizontal-only and both-direction attention, and that continuous attention (using previous-layer maps) improves over independent attention. These comparisons control for other components, lending credibility to the CVA design choice.

- **Swin Transformer over ViT is empirically justified**: Table 5 shows that replacing ViT with Swin Transformer in the position embedding stream yields 3–4% accuracy gains, directly supporting the paper's architectural motivation about long-range dependency modeling.

- **AU embedding consistently improves performance**: Table 7 demonstrates that adding AU information raises accuracy and F1-score by 2–4% on both datasets, validating the design choice of using AU as auxiliary input.

- **Comprehensive component-level ablation**: Beyond the overall architecture, the paper provides ablations isolating the attention direction (vertical vs. horizontal vs. both), the continuous-attention design, the choice of transformer backbone (Swin vs. ViT), single vs. dual-frame input, and AU embeddings. This gives a reasonably complete picture of each design decision's contribution.

## Weaknesses

### Major

- **No uncertainty quantification on tiny datasets**: CASME II has 255 videos across 26 subjects; SAMM has 159 videos across 32 subjects. With leave-one-subject-out cross-validation, a single misclassification can swing accuracy by several points. The paper reports only point estimates with no confidence intervals, standard deviations, or per-subject performance breakdowns. The reported improvements (especially the 10.87% gap over μ‑BERT on CASME II) cannot be assessed for statistical significance. This is the most serious weakness: the reader cannot tell whether the claimed gains reflect genuine superiority or evaluation noise.

- **Baseline comparisons use published numbers without protocol verification**: Table 1 compares against prior methods using their published results, but Section 4.1 confirms that both datasets have multiple labeling schemes (SAMM was originally labeled with 8 classes, CASME II with 5, etc.). The paper does not verify that the compared methods used the same 5-class mapping, the same LOSO splits, the same preprocessing pipeline, or the same evaluation metric computation. Given the small dataset sizes, even minor protocol differences can produce large accuracy swings. Without controlled re-implementation, the superiority claims over MMNet, μ‑BERT, and others are not substantiated.

- **Architectural inconsistency in feature fusion**: The paper states that F_M has dimensions 512×14×14 (line 69) while the FPF output is reshaped to 196×14×14 (line 85), and that these are then combined (line 92: "after adding F_POS and F_M together"). The channel dimensions do not match (512 ≠ 196), making element-wise addition impossible as described. This is either a dimensional error in the paper or a critical architectural ambiguity that must be resolved.

- **Implausible hyperparameter and missing training details**: The paper reports a weight decay of 0.6 for AdamW (line 137), which is roughly 10–60× larger than typical values (0.01–0.05 for AdamW). Additionally, the loss function is never stated, and the learning rate schedule ("exponentially decayed during the first 50 epochs") is under-specified. These issues make the reported numerical results impossible to trust or reproduce as-is. Even if 0.6 is a typo, the paper does not provide the intended value.

- **Missing architectural details for reproducibility**: Several key specifications are absent: (1) Swin Transformer patch size, window size, and embedding dimension; (2) the MLP architecture and hidden dimensions for the AU fusion classifier; (3) the dimension of the flattened feature map before AU concatenation. Without these, a competent practitioner cannot implement the method.

### Minor

- **The "vertical movement is more important" claim lacks independent support**: The paper argues that "vertical facial muscle movement plays a more important role in MER than horizontal movement" (Section 2) but provides no anatomical, physiological, or prior literature evidence for this claim. The only support is the paper's own ablation (Table 3), which compares vertical vs. horizontal attention within the proposed architecture. This is circular — the claim motivates the design, and then the ablation is presented as evidence for the claim.

- **Ablation baseline mismatch**: Table 2 evaluates component contributions using ResNet-18 as the base architecture, but the full model does not use ResNet-18. The improvements measured on ResNet-18 may not transfer to the actual architecture, which uses stacked CVA blocks with convolutional layers. The paper does not acknowledge this limitation.

- **Overclaimed language**: The abstract states "We also proved that including AU can further enhance accuracy" — the word "proved" is inappropriate for a single ablation study on two small datasets. This is correlation, not proof.

### Trivial

- None.

## Nice-to-Haves

- Including per-class F1 scores and per-subject accuracy distributions would allow readers to assess which emotions benefit and whether gains are concentrated on a few subjects.
- A controlled re-implementation of MMNet (and μ‑BERT, if accessible) under the same preprocessing and evaluation pipeline would strengthen the comparison substantially.
- Attention map visualizations (e.g., Grad-CAM) comparing vertical vs. full 2D attention would substantiate the central motivation.
- Code release upon publication would address reproducibility concerns given the architecture's complexity.

## Removed Points

- **μ‑BERT missing citation**: The reviewer flags this as a weakness. Since the parser strips references and appendices, this is a parser artifact, not an author error. Removed per hard rules.
- **"Unclear how 2D attention map is pooled to scalar"**: The paper specifies P_M as "max pooling operations along both the height and width dimensions" (line 67), which is an adequate description. The reviewer's confusion is unwarranted. Removed per hard rules.
- **"Table 2 not available in parsed text"**: Tables are embedded as images in the paper. The parser strips them; the original submission contains them. Removed per hard rules.
- **"Code availability should be promised"**: Moved to Nice-to-Haves as a suggestion, not a weakness.
- **Criticism about generic Swin Transformer description**: The paper specifies depths [2,2,6] and heads [4,8,16] (line 135). The description is partly specified, though patch/window sizes remain missing (kept as a Major weakness about missing details, not a generic description complaint).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Resolve the dimensional mismatch (512 vs. 196 channels) in the F_M and F_POS fusion — either clarify the intended operation or correct the dimensions.
2. Provide confidence intervals or per-subject breakdowns for all main results.
3. Either re-implement baselines under a controlled protocol or clearly caveat that Table 1 comparisons use published numbers and may reflect protocol differences.
4. Clarify the weight decay value (0.6 seems implausible — was 0.06 intended?) and state the loss function explicitly.
5. Tone down overclaimed language ("proved") throughout.
6. Provide the missing Swin Transformer and MLP architectural specifications.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>