Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper proposes a structured initialization for Vision Transformers (ViT) that initializes attention maps to approximate random impulse convolution filters. The idea is motivated by the observation that random spatial filters in ConvMixers achieve comparable performance to learned ones, supported by a theoretical condition (D ≥ kf²). The authors design a fast data-free optimization (Algorithm 1) using positional encoding as pseudo-input to solve for Q and K that yield impulse-structured attention maps. Experiments on CIFAR-10/100, SVHN, and ImageNet-1K show consistent improvements over Kaiming Uniform, Trunc Normal, and Mimetic initializations, with larger gains on wider models with more heads.

## Strengths

- **Novel conceptual connection between CNN architectural bias and ViT initialization.** The idea of reifying the ConvMixer spatial-mixing structure as an initialization constraint on ViT attention — rather than an architectural modification — is original and well-motivated. The paper traces a clear line from Proposition 1 (why random spatial filters suffice in ConvMixer) to the impulse initialization in ViT, unifying both architectures under a spatial-mixing-then-channel-mixing framing (Sections 3–4).

- **Consistent empirical improvement across diverse setups.** The proposed Imp.-3 and Imp.-5 methods outperform Trunc Normal on all small-scale datasets (by 2–4% on CIFAR-10, CIFAR-100, SVHN) and match or exceed Mimetic initialization. The improvement is not limited to tiny models: on ViT-S/h16 (Table 3), the gap over Trunc Normal reaches 8.15% on CIFAR-100, which is a substantial and non-trivial gain. The method also preserves large-scale performance on ImageNet-1K (74.40%), confirming flexibility is retained.

- **Pseudo-input design is practical and principled.** Algorithm 1 requires only ∼5 seconds of optimization using positional encoding as pseudo-input, with no real data, no pre-trained model statistics, and no architectural changes. The ablation study (Table 4) systematically evaluates nine pseudo-input configurations and identifies pure positional encoding as the best choice, providing concrete guidance for practitioners.

- **Validation on ConvMixer supports the theoretical condition.** Table 5 confirms that random and impulse filters perform within ∼1% of trained filters for kernel size 3, and that the gap grows with kernel size but shrinks when embedding dimension doubles — directly validating the D ≥ kf² condition. This cross-architecture support strengthens the paper's foundation.

## Weaknesses

### Fatal
None.

### Major

1. **Theoretical justification does not bridge ConvMixer (fixed spatial filters) to ViT (learned attention).** Proposition 1 shows that *fixed* spatial convolution filters in ConvMixer can achieve any output by learning only channel-mixing weights, provided D ≥ kf². The paper then initializes ViT attention maps to look like impulse convolution matrices and trains the full model normally. There is no formal or empirical argument that the initialized impulse structure acts as an *enduring* inductive bias (rather than being overwritten in a few gradient steps), nor does the ConvMixer theory — which assumes spatial filters are *held fixed* — directly apply to ViT where Q and K are updated throughout training. The attention map visualizations (Figure 4) partially address this by showing residual structure at deeper layers, but the paper does not track how quickly the impulse pattern decays. This gap weakens the central claim of "reinterpreting architectural bias as initialization bias."

2. **No variance or statistical significance reported.** Every experiment is reported as a single number with no standard deviations, confidence intervals, or multi-seed results. Many performance differences are small (e.g., Imp.-5 at 70.46% vs. Mimetic at 70.40% on CIFAR-100 in Table 2; Imp.-3 at 91.62% vs. Mimetic at 91.16% on CIFAR-10). Without error bars, these differences cannot be distinguished from noise. Given that all datasets are small enough to run multiple seeds easily, this is a significant omission that undermines the reliability of the headline results. The strength finder correctly notes the method achieves "state-of-the-art" but cannot verify statistical robustness.

3. **"State-of-the-art for data-efficient ViT learning" is not justified by the comparison set.** The paper compares against three initialization baselines (Kaiming Uniform, Trunc Normal, Mimetic). However, the term "data-efficient ViT learning" encompasses many methods — DeiT, TinyViT, distillation-based approaches, architectural modifications for small data — none of which are included. The experiments demonstrate that impulse initialization improves over *other initialization strategies*, not that it achieves SOTA among *data-efficient ViT methods* broadly. This overclaim should be corrected to reflect the actual scope of comparison.

4. **The pseudo-input optimization's convergence and the specific role of the impulse structure are not sufficiently analyzed.** The optimization (Algorithm 1) minimizes MSE against a target impulse matrix over 10k steps, but no convergence curves, final MSE values, or sensitivity to random seeds are reported. Moreover, Table 4 shows that several pseudo-input variants achieve very similar top-line accuracy (e.g., PE at 90.39% vs. G+PE at 90.27% — a 0.12% difference). Without ablations that *break* the impulse property (e.g., random binary matrices of the same sparsity, constant matrices, or matrices with the impulse structure scrambled), it is unclear whether the *specific* convolutional impulse pattern causes the improvement or whether any structured (low-entropy) initialization suffices. The paper does run a "box filters" ablation in the ConvMixer experiments (Table 5), but this is not done for ViT.

### Minor

1. **Motivation for impulse filters rests on a single paper.** Section 4.1 cites Tarzanagh et al. for the claim that softmax attention "tends to select a single related feature." This is a limited basis for concluding that impulse filters are "the most straightforward and suitable choice" — many works show multi-modal attention patterns. The choice is still reasonable and the empirical results support it, but the theoretical justification is thinner than presented.

2. **The ViT-T baseline modification (average pooling + sinusoidal PE) yields a 4% gain (81.23 → 85.30 on CIFAR-10), but the paper does not quantify how much of the *total* improvement from the proposed method is additive to this strong baseline.** Since all methods share the same configuration, the comparison is fair, but the presentation could be clearer about the building-block nature of these gains.

3. **Attention map visualizations are averaged over data and shown for only 3 of 12 layers** (Figure 4). The paper acknowledges the structure becomes "less visible" in deeper layers but does not show per-image or per-head examples, making it hard to assess how well individual heads retain the impulse pattern.

### Trivial
None.

## Nice-to-Haves
- A few per-head, per-image attention map examples at initialization and after 1, 5, 50 training steps to visualize whether the impulse structure persists or decays rapidly.
- Convergence metrics (final MSE loss, variation across optimization seeds) for Algorithm 1.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Proposition 1 omits non-linearities, residual connections, and batch norm"** — The paper explicitly states this simplification on line 116 ("For clarity and simplicity, we have omitted activations..."). This is a standard theoretical choice, not a hidden flaw.
- **"The BCCB matrix description is standard and unnecessary in the appendix"** — Pure formatting/subjective style opinion with no bearing on the paper's contribution.
- **"The tension about pseudo-input being lightweight pre-training is not addressed"** — The paper addresses this directly (lines 253–254): "this optimization does not count as a pre-training step since no real data is involved ... converging in just a few seconds (~5s)." This is a reasonable addressal.

## Novel Insights

The most interesting finding from the reviews is the contrast between the method's robust empirical success on larger models (ViT-S/h16: 8.15% gain) and the fragility of its theoretical grounding. The paper's experiments show that impulse initialization shines precisely when the number of heads is large, which aligns with the D ≥ kf² rank argument — yet the argument itself applies to *fixed* spatial filters, while the ViT setting involves *learned* attention that can diverge from the initial pattern. This tension suggests that the real mechanism may not be the preservation of impulse structure but rather that initializing Q and K to produce impulse-like attention maps imposes a favorable geometry in parameter space that facilitates optimization — a different claim than the paper's framing of "reinterpreting architectural bias as initialization bias." The reviews do not resolve this, but they point to a potentially more interesting story than the paper currently tells.

## Suggestions

1. **Report mean ± std over at least 3 random seeds for all main tables (Tables 2 and 3).** This is essential for small-scale datasets where differences are narrow. Without it, the empirical contribution is impossible to evaluate confidently.

2. **Add an ablation that breaks the impulse structure in ViT:** initialize attention maps with random binary matrices (same sparsity as impulse), a constant matrix, or impulse matrices with permuted rows. Compare final accuracy to isolate whether the *specific* convolutional pattern or just *any structured (low-entropy)* initialization drives the improvement.

3. **Tone down the "state-of-the-art" claim** to something like "competitive with or better than existing initialization strategies for data-efficient ViT training." The current claim overreaches the comparison set.

4. **Track attention map similarity to the target impulse matrix over training** (e.g., cosine similarity or MSE between the attention map and H_impulse at initialization, epoch 1, epoch 5, etc.). This would directly address whether the inductive bias persists or is transient, and would strengthen the paper's core narrative.

5. **Clarify in Section 3 that Proposition 1 applies to the scenario where spatial filters are fixed** (only channel mixing is learned) and note that the ViT extension relies on initialization, not structural invariance. Add a sentence acknowledging that the translation from ConvMixer theory to ViT practice is heuristic.

## Score and Decision

**Originality:** High — reinterpreting architectural bias as initialization bias is a genuinely novel framing.  
**Importance of research question:** Moderate-to-high — enabling ViT on small data is practically valuable.  
**Claims well supported:** No — missing variance, overclaimed SOTA, and insufficient ablation of the impulse structure itself.  
**Soundness of experiments:** Moderate — consistent improvements across many settings, but single runs and narrow baseline set reduce confidence.  
**Clarity of writing:** Good — the exposition is coherent and the method is clearly described.  
**Value to the research community:** Moderate — the method is practical and fast, but the theoretical gaps limit its impact.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>