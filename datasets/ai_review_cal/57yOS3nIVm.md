- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5
Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

The paper proposes **Divide and Conform**, which decomposes pre-trained ConvNet convolution filters into spatial atoms (spatial-only convolution) and atom-coefficients (channel combination), then fine-tunes *only the spatial atoms* (a few hundred parameters) using the SimCLR self-supervised objective on unlabeled target data — crucially, without requiring access to the base pre-training dataset. The method is evaluated on cross-domain few-shot learning (CD-FSL) benchmarks with ResNet backbones and shows competitive or superior accuracy relative to full fine-tuning and LoRA while fine-tuning fewer than 2% of backbone parameters.

## Strengths

1. **Extreme parameter efficiency with strong empirical results.** Tables 1 and 3 show that DC-9/DC-12 fine-tune <2% of backbone parameters yet outperform full SimCLR fine-tuning (which updates 100% of parameters) on 5 of 7 datasets for ResNet-18 (e.g., CropDisease 5-shot: 92.5% vs. 88.6%) and similarly on ResNet-50. This directly supports the core claim that spatial-atom-only adaptation is both efficient and effective.

2. **Competitive performance without base dataset access, rivaling base-dependent methods.** Table 4 demonstrates that in the Base-Free (BF) setting, DC methods outperform all BF baselines (SimCLR, LoRA, ConFeSS) on most datasets, and in several cases match or exceed methods that require the base dataset (STARTUP, DynDistill). On EuroSAT 5-shot, DC-9 (89.7%) substantially exceeds SimCLR (80.9%) and even the base-dependent STARTUP (85.4%). This validates the practical contribution of operating without base data.

3. **Ablation confirms the design choice of fine-tuning atoms rather than coefficients.** Table 6 compares fine-tuning only atoms, only coefficients, and both. On all four ablations, atom-only fine-tuning achieves the best accuracy-parameter trade-off (e.g., EuroSAT: 91.3% with 0.19M params vs. 87.5% with 11.14M params for coefficient-only). This provides clear empirical support for the proposed selective-update strategy.

## Weaknesses

### Fatal
None.

### Major

1. **Critically insufficient reporting of training details prevents reproducibility.** The paper provides no hyperparameters for the SimCLR fine-tuning stage: batch size, number of epochs, learning rate and schedule, optimizer, temperature, whether a projection head is used and later discarded, or data augmentations applied. The decomposition hyperparameters (number of optimization iterations, initialization strategy for **D** and **A**, stopping criterion, λ values tested and final choice) are also absent. The only quantity mentioned is "20% of target unlabeled samples" (Table 6 caption). Without these details, no independent researcher can reproduce or build on the results. This is the most significant barrier to the paper's impact.

2. **LoRA implementation for convolutions is unspecified.** The paper compares against LoRA at ranks 3/9/12 but never describes how LoRA — originally designed for linear layers in transformers — is adapted to convolutional kernels. Whether it acts on the full 4D weight tensor, per input channel, or via some other factorization is not stated. This makes the LoRA baseline results uninterpretable and unreproducible.

### Minor

3. **Decomposition fidelity is not validated.** The paper uses an iterative dictionary learning objective (Equation 4) with L1 sparsity regularization on **A** to decompose pre-trained filters into **D** and **A**. While line 86 correctly states that a perfect reconstruction K=**A·D** makes the two-step convolution exact, the optimization may introduce reconstruction error. No reconstruction error (e.g., MSE between original and reconstructed filters, or accuracy drop on the base dataset before vs. after decomposition) is reported. Without this, the starting point for fine-tuning is not characterized — gains could partly reflect recovery from decomposition-induced degradation rather than genuine domain adaptation.

4. **Theoretical motivation is overclaimed and the presented Insights are too weak to carry the argument they are used for.** Insights 1 and 2 in Section 3.3 are mathematically correct under their stated assumptions (Θ as scalar ℝ→ℝ; convolution equivariance to spatial transformations), but they only show trivial properties: scaling atoms scales the filter, and spatial equivariance carries through the decomposition. Neither establishes that *domain shifts are primarily spatial* — which is the hypothesis the paper uses them to support. The paper would be better served by presenting the method on purely empirical/parameter-efficiency grounds rather than claiming a theoretical foundation that the insights do not provide.

5. **Missing a standard baseline: linear probing (full backbone frozen, only the final linear classifier trained).** Linear probing is the simplest parameter-efficient adaptation baseline and would isolate whether the benefit of DC comes from spatial-atom adaptation or from the combination of extreme parameter reduction plus self-supervised fine-tuning. The paper compares against full SimCLR fine-tuning and LoRA but omits this obvious baseline. (The reviewer's requests for BN-stat adaptation and last-block-only fine-tuning are additional suggestions but less standard; linear probing is the clear omission.)

6. **Ablation limited to only 4 of 7 datasets.** Table 6 covers EuroSAT, CropDisease, ChestX, ISIC, but not the other datasets used in the main tables. Extending the ablation to all datasets would strengthen the claim about spatial-atom superiority being universal.

### Trivial
None.

## Nice-to-Haves

- Reporting per-layer breakdown of where spatial atoms are deployed (all convolutional layers or a subset) would clarify the parameter efficiency analysis.
- A comparison against "randomly initialized spatial atoms with the same training" would help disentangle the benefit of pre-trained initialization from the benefit of selective spatial adaptation.
- Including a modern backbone beyond ResNets (e.g., ConvNeXt) would broaden generality claims.

## Removed Points

These points were raised by the reviewers but are removed with justification:

- **"Theoretical justification is mathematically unsound / fundamentally flawed"** — Removed as factually incorrect. The harsh critic claimed a translation operator would break the commutativity in Insight 1. However, the paper defines Θ as ℝ→ℝ (scalar linear transformation), not as a spatial operator. For scalar multiplication, Θ(A·D_B) = A·Θ(D_B) holds by basic linear algebra. The insights are weak (see weakness #4 above), but they are not mathematically wrong in the way claimed, and certainly not "fundamentally flawed."

- **"Insights are central to the paper's contribution"** — Removed as overstated. The paper explicitly says the hypothesis is "supported empirically (cf. Section 4.1) and by the following analysis" (line 111), relegating the insights to supplementary motivation, not core contributions.

- **"Comparison against meta-learning methods adds clutter"** — Removed. The paper acknowledges ML vs. TL methods are not directly comparable and provides the comparison only "to provide a comprehensive overview" (line 171). This is standard practice and not a weakness.

- **"Not fair to compare against STARTUP/DynDistill since they use base data"** — Removed. The paper explicitly separates BF and non-BF methods in Table 4 and marks them accordingly. The reviewer acknowledges this.

- **"Missing appendix content / λ analysis / broken garbled text"** — Removed. These are PDF extraction artifacts or content from the appendix (which the parser strips from all papers). The original submission contains this material.

- **"Needs more diverse backbones" and several other Nice-to-Have suggestions** — These are scope creep or exceeding standard evaluation practice for a conference paper.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the expected tension between the paper's clean empirical story (parameter-efficient spatial adaptation works) and its weak theoretical framing, but do not generate new observations about the method beyond what the authors present.

## Suggestions

1. **Provide complete training details** in the main paper or appendix: SimCLR hyperparameters (batch size, epochs, learning rate/schedule, optimizer, temperature, projection head architecture, augmentations), decomposition optimization (iterations, initialization, λ values selected), and unlabeled sample counts per dataset. This is the single most important change for acceptance.

2. **Specify the LoRA-to-convolution adaptation** clearly, or cite an established convention. Without this, the LoRA baseline is not interpretable.

3. **Report decomposition fidelity**: Top-1 accuracy of the decomposed model (pre-fine-tuning) on the base dataset compared to the original backbone, plus reconstruction MSE. This rules out the concern that DC's gains reflect recovering from decomposition damage.

4. **Add linear probing** as a baseline to Tables 1/3/4 for a cleaner separation of the contribution of spatial-atom adaptation vs. any self-supervised fine-tuning with few parameters.

5. **Either remove the theoretical Insights or reframe them** as intuitive motivation ("spatial atoms are a low-dimensional parameterization that reduces overfitting risk with limited unlabeled data") rather than attempting to prove that domain shifts are spatial. The empirical results are the paper's strength; the Insights as currently positioned invite scrutiny they cannot withstand.
