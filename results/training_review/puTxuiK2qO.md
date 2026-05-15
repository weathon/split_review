Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

AdaFisher proposes an adaptive second-order optimizer that replaces Adam's second-moment estimate with a diagonal block–Kronecker approximation of the Fisher Information Matrix (FIM). The method leverages an empirical observation that Kronecker factors (activation and pre-activation derivative matrices) are diagonally dominant, and retains only their diagonals, yielding an O(n) per-layer preconditioner. This is integrated cleanly into the Adam framework with only one additional hyperparameter. Experiments are conducted on image classification (CIFAR, TinyImageNet, ImageNet) and language modeling (WikiText-2, PTB).

## Strengths

- **Clean diagonal FIM approximation grounded in empirical analysis.** The Gersgorin disk analysis (Section 3.1, Fig. 2) provides visual evidence that Kronecker factors are diagonally dominant, motivating the diagonal simplification. This is a principled way to reduce the cost of second-order optimization.  
- **Practical integration into Adam with minimal overhead.** AdaFisher replaces Adam's squared-gradient second moment with the diagonal FIM, removes the square root, and introduces only one additional hyperparameter (γ₂). Algorithm 1 is straightforward and implementable.  
- **Extension of Kronecker factors to normalization layers.** Proposition 3.1 provides explicit formulas for BatchNorm and LayerNorm Kronecker factors, which enables AdaFisher to be applied to modern transformer architectures where prior K-FAC-style methods struggle.  
- **Consistent improvements on CIFAR and language modeling.** AdaFisher achieves 96.25% vs. Adam's 94.85% on CIFAR-10 ResNet-18 (Table 1) and reduces WikiText-2 perplexity from 175.06 (AdamW) to 152.72 (AdaFisherW) (Table 4). These are meaningful, reproducible-looking gains on standard benchmarks.  
- **Stability analysis (Fig. 4) suggests robustness** to learning rate and batch size variation, which is practically useful and a genuine advantage over methods requiring extensive hyperparameter tuning.

## Weaknesses

### Major

- **ImageNet Adam baseline appears severely undertuned, inflating the claimed improvement.** The paper reports Adam at 67.78% Top-1 on ResNet-50/ImageNet. Standard well-tuned Adam on this setting should reach ~75–76%. The cited Momentum baseline from Goyal et al. (76.40%) uses the same batch size and achieves ~8.6 pp higher than the paper's Adam. AdaFisher (76.95%) is only 0.55 pp above that standard Momentum baseline. This suggests the headline gap (AdaFisher 76.95% vs. Adam 67.78%, a ~9 pp improvement) is primarily an artifact of an undertuned Adam baseline, not a genuine superiority of AdaFisher over properly configured first-order methods. This undermines the paper's central claim of "outperforming SOTA optimizers."

- **Inappropriate inclusion of K-FAC and Shampoo on transformer architectures.** Table 2 explicitly marks K-FAC and Shampoo as "not applicable to Transformers" (✗). Yet Table 1 includes their results on Tiny Swin, FocalNet, and CCT — all transformer models — where they predictably fail (e.g., 34.45% and 30.39% on Tiny Swin CIFAR-100). Including methods known *by the paper's own admission* to be inapplicable creates a misleading impression of AdaFisher's advantage. The fair comparison on transformers is against Adam (which AdaFisher does beat, but by narrower margins).

- **Promised ablation studies are absent.** Section 4.3 states: *"We further conduct extensive ablation studies on additional components of AdaFisher, including the convergence efficiency, our novel approximation of the FIM, the significance of EMA for Kronecker factors, the impact of the square root, the stability across learning rate schedulers and the updated computation of the FIM for normalization layers."* **No such ablations appear anywhere in the paper.** The stability analysis (Fig. 4) tests batch size and learning rate — these are not ablations of the architectural choices listed. Without these, it is impossible to attribute performance to any specific component (e.g., the diagonal Kronecker factors vs. the EMA scheme vs. the removal of the square root vs. the Min-Max normalization). This is a significant omission for a paper whose main claim is introducing a novel approximation.

- **Unclear experimental protocol with WCT cutoff.** Table 1's caption states *"with a 200-epoch AdaFisher training cutoff,"* and the text says AdaFisher uses a 200-epoch Wall-Clock-Time (WCT) cutoff. It is never stated whether baselines are also limited to 200 epochs, the same wall-clock time, or allowed to run to convergence. For ImageNet, the text says *"90-epoch WCT for Adam, which surprisingly matched AdaFisher's training duration"* — but AdaFisher's epoch count and per-epoch time are not reported. Without this information, the reported accuracy differences could be artifacts of unequal training budgets.

- **No comparison against simple diagonal empirical Fisher (squared gradients).** Since AdaFisher's preconditioner is provably diagonal (Kronecker product of two diagonal matrices), it is conceptually similar to Adam's squared-gradient diagonal. The paper does not include an ablation comparing AdaFisher's diagonal against (a) Adam's second moment or (b) a simple EMA of squared gradients. Without this, it is unclear whether the Kronecker-factored diagonal offers any advantage over a simpler diagonal approximation — which would be the most natural baseline to establish novelty.

### Minor

- **Convergence analysis adds little new insight.** Proposition 4.3 derives an O(log T / √T) bound that matches Adam's regret, and the added condition (F̃_{D_{t-1}}/η_{t-1} ≤ F̃_{D_t}[j]/η_t) is non-standard and not shown to hold for AdaFisher in practice. The convex analysis (Proposition 4.2) is stated without proof. This section does not meaningfully distinguish AdaFisher from generic Adam-family methods.

- **EMA update with default γ₁=0.92, γ₂=0.0008 is unusual and potentially a typo.** The update (Algorithm 1) is `new_EMA = 0.92 * old_EMA + 0.9992 * batch_estimate`. The coefficients sum to 1.9192 ≠ 1, which is not a convex combination and would cause estimates to grow. Either the defaults are incorrect or the update rule is mis-specified. The paper should clarify.

- **No per-epoch runtime comparison.** The paper claims *"comparable memory and time requirements than the first-order methods"* but does not report per-epoch wall-clock time for each optimizer on a representative model (e.g., ResNet-50 with batch size 256). This claim is unverifiable without such data.

### Trivial

- The phrase *"Owing to global warming concerns"* (Section 4.2) as a motivation for transfer learning is out of place in a technical optimization paper.

- Propositions 3.1 (normalization layers) and 4.2–4.3 (convergence) are stated without derivation or proof. While proofs may be deferred to an appendix, their absence in the main text makes the theoretical claims hard to evaluate.

## Nice-to-Haves

- An ablation comparing AdaFisher's diagonal FIM against a simple EMA of squared gradients (the "pure diagonal empirical Fisher") would cleanly isolate the benefit of the Kronecker-factored structure.
- Reporting per-epoch runtime for each optimizer and the number of epochs used for each baseline would resolve the WCT ambiguity.
- A time-series visualization of diagonal entries of H_{D_i} and S_{D_i} across layers and training steps would strengthen the diagonal-dominance claim.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism that AdaFisher "never acknowledges" the diagonal collapse (Harsh Critic #3).** The paper repeatedly uses the term "diagonal block–Kronecker" and explicitly says it "retains only the diagonals of the Kronecker factors" (Section 3). The method is presented as a *diagonal* approximation, not a full-block one. This is adequately acknowledged.
- **Criticism that the Gersgorin analysis is insufficient (Section 3.1 note).** The analysis shows the Kronecker factors themselves are diagonally dominant. Since the method takes diagonals of these factors and takes their Kronecker product, the analysis is a reasonable motivation for the diagonal approximation, even if not a formal proof. This is a scope issue, not a flaw.
- **Criticism about "missing appendix, missing proofs."** The parser strips appendices. These may exist in the original submission.
- **"Global warming concerns" undermines scientific tone.** This is a stylistic nitpick. It is irrelevant to scientific evaluation and is moved to trivial.
- **Strength Finder claims about "theoretical convergence guarantee."** The convergence bound is indeed shared with Adam, but the paper does claim this as a strength. I downgrade this rather than removing it.

## Novel Insights

The reviews converge on a core tension: AdaFisher is a sensible and pragmatically motivated optimizer that achieves genuine improvements on CIFAR and language modeling tasks, yet its central experimental narrative — especially on ImageNet — collapses under scrutiny. The most interesting observation, not fully developed in the paper or the reviews, is that the *mechanism* by which AdaFisher helps remains unclear. The diagonal Kronecker approximation degenerates to a diagonal preconditioner, making it structurally similar to Adam's second moment. Yet AdaFisher outperforms Adam on several benchmarks. If this is real, the benefit may come from (a) the Min-Max normalization of the Kronecker factors, (b) the removal of the square root, or (c) the specific EMA scheme — none of which are ablated. The paper would be substantially stronger if it pinpointed *why* the Kronecker-derived diagonal differs from Adam's heuristic diagonal, rather than presenting the full system as a black box that happens to work.

## Suggestions

1. **Retune baselines on ImageNet.** Run Adam with standard hyperparameters (β₁=0.9, β₂=0.999, learning rate schedule typical for ImageNet) and report its actual performance. If Adam reaches ~76%, the paper's claimed advantage is marginal and must be reframed as such.
2. **Replace inappropriate baseline entries.** Either remove K-FAC/Shampoo results on transformers or clearly separate them with a note that these methods are known to be inapplicable.
3. **Deliver the promised ablations.** At minimum, ablate: (a) diagonal Kronecker vs. simple squared-gradient diagonal, (b) with vs. without Min-Max normalization, (c) with vs. without square root removal.
4. **Clarify the experimental protocol.** State explicitly: how many epochs for each baseline? Was it equal epochs or equal wall-clock time? What was the per-epoch time for each optimizer?
5. **Fix the EMA update or explain it.** If the asymmetric γ₁/γ₂ is intentional, provide justification. If it's a typo, correct it. Ensure the coefficients sum to ≤ 1.
6. **Report per-epoch wall-clock time** for each optimizer on a representative network to substantiate the "comparable time" claim.

## Score and Decision

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>