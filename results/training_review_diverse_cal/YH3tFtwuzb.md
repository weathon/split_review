Now I have all the evidence I need. Here is my final consolidated review:

---

## Summary

This paper proposes DP-BiTFiT, a method for differentially private fine-tuning that trains only the bias terms (~0.1% of parameters) of pre-trained models. The key contribution is a complexity analysis showing that DP-BiTFiT's DP overhead is independent of the feature dimension \(T\) (unlike all weight-based DP methods), and empirical results demonstrating 2–30× speedups and 2–8× memory savings over DP full fine-tuning while maintaining competitive accuracy on transformer-based models across language and vision tasks.

## Strengths

- **Parameter efficiency (~0.1%) across diverse architectures**: Table 1 shows DP-BiTFiT trains only ~0.1% of total parameters on models ranging from VGG16, ResNet50, ViT, GPT2, to RoBERTa — substantially smaller than LoRA (0.94%) or Adapter (1.4%), and model-agnostic (no architecture modifications needed).

- **Compelling computational efficiency analysis and validation**: The complexity analysis in Table 2 reveals that DP-BiTFiT's DP overhead is \(O(Bp)\) per layer vs. \(O(BT^2)\) for ghost-clipped full fine-tuning. This is empirically validated in Figures 2–4, showing 2–30× speedup and 2–8× memory reduction over DP full fine-tuning as sequence length or image resolution increases. The paper also correctly notes (line 230) that total cost remains linear in \(T\).

- **Competitive accuracy on transformer architectures**: On GLUE (RoBERTa-large), DP-BiTFiT is within 1% of DP full fine-tuning (e.g., 94.5 vs 93.8 on SST2). On GPT2-large for E2E, DP-BiTFiT actually *outperforms* DP full fine-tuning on BLEU (65.21 vs 64.64). On CIFAR10/CIFAR100 with ViT-large, DP-BiTFiT matches or exceeds DP full fine-tuning, achieving 99.0% on CIFAR10 at \(\epsilon=8\).

- **Scalability insight**: The paper demonstrates that the accuracy gap between BiTFiT and full fine-tuning closes as model size increases (Remark 1), a genuinely interesting and practically important observation supported across multiple tasks and model families.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The "matches SOTA accuracy" claim is unqualified for CNN-based architectures.** On CelebA with ResNet18, DP-BiTFiT underperforms DP full fine-tuning by 2–3 percentage points (e.g., 88.17 vs 91.02 for Smiling; 86.87 vs 88.38 multi-label). The paper acknowledges this (line 396: "DP-BiTFiT needs extra attention for convolutional neural networks") and proposes DP-BiTFiT-Add as a partial mitigation. However, the abstract's claim that the method "matches the state-of-the-art accuracy for DP algorithms" is too broad without acknowledging this limitation for CNN backbones. This does not undermine the transformer results, where the method is genuinely competitive, but the paper should qualify the claim to reflect the architecture dependence.

- **Algorithm 1 leaves ambiguity about per-sample gradient storage.** The algorithm computes per-sample bias gradients and their norms in a per-layer loop (lines 52–58), then aggregates norms globally (line 60) and later computes the sum of clipped gradients (line 62). The paper claims \(+\!Bp\) space per layer, which suggests storing per-sample bias gradients for all layers simultaneously. The paper does not specify whether these are stored or recomputed, and the space complexity claim needs a brief justification. This is a reproducibility detail that should be clarified.

- **No ablation on the clipping threshold \(R\).** DP-BiTFiT uses the same clipping mechanism as full fine-tuning, but the optimal clipping threshold may differ for bias-only training, where gradient norms likely have a different distribution. An ablation (even on a single task) would strengthen the empirical analysis.

### Trivial
- The paper does not analyze the effect of training epochs on accuracy comparisons. Since DP-BiTFiT trains far fewer parameters, it may converge at different rates than full fine-tuning. Reporting accuracy vs. epoch curves for a representative task would clarify whether the fixed-epoch comparisons are fair.

## Nice-to-Haves
- A more systematic analysis of the scaling pattern (Remark 1), e.g., computing the accuracy gap as a function of model width/depth within a fixed architecture family rather than across qualitatively different model families.
- Reporting whether DP-BiTFiT's optimal learning rate adjustment was also investigated for the DP LoRA/Adapter baselines (whose numbers are taken from prior work).
- Evaluation of DP-BiTFiT-Add on at least one more architecture without inherent bias terms beyond ResNet18 on CelebA.

## Removed Points

These points were removed after verifying against the paper. They are flagged for caution but should not be considered valid weaknesses.

1. **"Activation-free claim is misleading"** — REMOVED. The reviewer argues that standard backprop still requires intermediate storage, but the paper's claim is specifically about not storing forward-cached activation tensors \(\{\a_l\}_l\) (the input activations to each layer), which constitute >95% of memory in deep networks (line 138, citing Jain et al. 2020). Bias gradients do not use \(\a_l\) (Eq. 13), so removing forward hooks eliminates this storage. The table's "storing activation" row refers to this specific tensor, not all autograd intermediates. The claim is accurate.

2. **"T-independence claim overstates practical difference"** — REMOVED. The paper explicitly includes the caveat "(though the total complexity is still linear in \(T\))" on line 230, and the footnoted claim on line 74 specifies "computation overhead" (the *additional* DP cost), not total training cost. The distinction is already present in the paper.

3. **"Comparison to LoRA/Adapter from prior work may not be tuned comparably"** — REMOVED. Using published baseline numbers is standard practice; the paper notes it increased learning rate for BiTFiT, which is a methodological detail about BiTFiT's optimal regime, not an unfair comparison.

4. **"Scaling pattern evidence is limited"** — REMOVED. This is an interesting observation, not a core claim. The paper does not overclaim on this point.

## Novel Insights

None beyond the paper's own contributions. The main novel insight — that bias-only DP training has a DP overhead independent of the feature dimension \(T\), unlike all weight-based methods — is the paper's own central contribution, clearly presented and empirically validated.

## Suggestions

1. **Qualify the "matches SOTA" claim.** In the abstract and conclusion, note that this holds strongly for transformer-based architectures and that on CNN backbones (e.g., ResNet) there is a small but consistent gap. This would make the paper more precise without weakening its overall contribution.
2. **Clarify Algorithm 1's memory management.** Specify whether per-sample bias gradients are stored across all layers or recomputed for the clipped gradient sum, and justify the claimed \(+\!Bp\) space complexity.
3. **Add a clipping threshold ablation** for at least one representative task (e.g., one GLUE dataset with RoBERTa-base) to show whether the optimal \(R\) differs for bias-only training.

## Score and Decision

The paper makes a solid empirical and analytical contribution: DP-BiTFiT is clearly valuable for differentially private fine-tuning of large models, with substantial efficiency gains (2–30× speedup, 2–8× memory savings) and competitive accuracy. The complexity analysis in Table 2 is itself a useful reference for the community. The weaknesses are minor — a too-broad accuracy claim and limited reproducibility details — and fully addressable. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>