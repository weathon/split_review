Now I have all the evidence I need. Let me compose the final consolidated review.

## Summary

AdaFisher introduces an adaptive second-order optimizer that replaces Adam's diagonal squared-gradient second-moment estimate with a diagonal block-Kronecker approximation of the Fisher Information Matrix (FIM). The method retains only the diagonals of Kronecker factors (justified via Gershgorin circle analysis on one layer), applies min-max normalization, and incorporates an EMA over Kronecker factors. The paper reports consistent accuracy gains over Adam, K-FAC, AdaHessian, and Shampoo across image classification (CIFAR-10/100, TinyImageNet, ImageNet) and language modeling (WikiText-2, PTB) benchmarks, along with a generic convergence guarantee.

## Strengths

1. **Consistent empirical improvements across diverse architectures and tasks**: AdaFisher achieves the highest accuracy among all compared optimizers on all 7 architectures on CIFAR-10/100 (e.g., ResNet-50 on CIFAR-100: 79.77% vs next-best 78.07%). On ImageNet with ResNet-50 (batch size 256), AdaFisher reaches 76.95% top-1 accuracy, outperforming Momentum (76.40%), K-FAC (70.96%), and Shampoo (72.82%). In language modeling, AdaFisherW reduces perplexity on WikiText-2 to 152.72 from AdamW's 175.06. The gains hold in transfer learning settings as well.

2. **Robustness to hyperparameter variations**: Stability analysis (Figure 4) shows AdaFisher maintains high accuracy across a range of learning rates and batch sizes, with less sensitivity than Adam, AdaHessian, and Shampoo. This reduces the practical burden of hyperparameter tuning.

3. **Low hyperparameter overhead**: AdaFisher introduces only one additional hyperparameter (damping factor λ=0.001) compared to Adam, which is fewer than K-FAC, AdaHessian, or Shampoo, while achieving better or comparable per-epoch training time (Figure 4, Panel D).

4. **Extension to normalization layers**: Proposition 1 provides explicit formulas for Kronecker factors of BatchNorm and LayerNorm layers, addressing a detail omitted by prior K-FAC-based works. This enables application to modern architectures that heavily use normalization.

## Weaknesses

### Fatal

None. While several issues are serious, none individually invalidate all core claims of the paper.

### Major

1. **Potentially incorrect derivation of Kronecker factors for normalization layers (Proposition 1, §3.2)**. The formulas compute the outer product of *summed* activations/derivatives rather than the sum of outer products. Specifically, $\mathcal{H}_i = (\sum_{\mathbb{B}}\sum_{\mathcal{T}}\bar{h}_i)^T(\sum_{\mathbb{B}}\sum_{\mathcal{T}}\bar{h}_i) / (M|\mathcal{T}|)^2$ yields the outer product of the mean activation vector (a rank-1 matrix), whereas the correct empirical Kronecker factor is the mean of outer products: $\frac{1}{M|\mathcal{T}|}\sum_{\mathbb{B}}\sum_{\mathcal{T}} \bar{h}_i \bar{h}_i^T$. For BatchNorm layers where activations are centered near zero, the paper's formula would give approximately zero while the correct formula gives the identity (for unit-variance activations). This discrepancy is not discussed or ablated. While normalization layers have few parameters and this error may not dominate empirical results, it is a genuine mathematical flaw in the method's derivation that needs clarification or correction.

2. **Unclear and potentially unfair comparison methodology, especially the ImageNet evaluation (§4)**. The paper states it uses a "Wall-Clock-Time (WCT) method with a cutoff of 200 epochs for AdaFisher's training" and for ImageNet "a 90-epoch WCT for Adam, which surprisingly matched AdaFisher's training duration." This description is ambiguous — it is unclear whether different optimizers ran for different numbers of epochs. The reported Adam top-1 accuracy on ImageNet (67.78%) is substantially below standard ResNet-50 performance (~76–77% with proper tuning), strongly suggesting either insufficient training or poor hyperparameters for the baseline. This single number undermines the paper's strongest headline claim. The comparison with Momentum at batch size 256 (76.40%) is fairer and shows a modest 0.55% gain, but the paper's presentation does not clearly flag that the Adam baseline is anomalously low.

### Minor

3. **Limited evidence for the diagonal dominance claim (§3.1)**. The analysis examines only the 37th convolutional layer of ResNet-18 on CIFAR-10, at two training steps. While the Gershgorin disc and eigenvalue perturbation analysis are illustrative, they fall short of being a comprehensive empirical demonstration of diagonal dominance across layers, architectures (CNNs vs. transformers), datasets, and training stages. The paper concludes "we empirically conclude the diagonal concentration property," which is too strong given the narrow evidence. However, the method's broad empirical success provides indirect validation — this weakness limits the *motivation* for the method rather than its results.

4. **Theoretical convergence analysis is generic and not specific to AdaFisher (§3.4)**. Proposition 2 states that the natural gradient update converges under convexity — this is standard and says nothing about AdaFisher's specific approximation. Proposition 3 provides a bound of $O(\log T/\sqrt{T})$ under assumptions that include a non-increasing preconditioner-to-step-size ratio, which is essentially the same as Adam-type convergence proofs. The bound does not depend on any property of AdaFisher's diagonal block-Kronecker approximation beyond boundedness of the FIM. This does not *harm* the paper, but it does not specifically justify why the approximation is effective.

5. **Min-max normalization of diagonal Kronecker factors (Eq. 7, §3.2) is introduced without motivation or ablation**. Rescaling each diagonal entry to [0,1] based on the current batch's min and max is an unusual step for curvature estimation — it introduces non-stationary, data-dependent scaling absent in standard K-FAC or Adam. No justification or ablation study is provided to show whether this helps, hurts, or is neutral. Given that this is a non-standard design choice, it needs empirical validation.

6. **Missing ablation results for key components**. The paper states "We further conduct extensive ablation studies on additional components of AdaFisher, including the convergence efficiency, our novel approximation of the FIM, the significance of EMA for Kronecker factors, the impact of the square root, the stability across learning rate schedulers and the updated computation of the FIM for normalization layers" (§4.4), but the actual results of these studies are not presented in the reviewed text. These are crucial for understanding which components of AdaFisher contribute to its performance.

7. **Poor baseline performance in language modeling experiments (§4.3)**. AdaHessian (PPL 407.69) and Shampoo (PPL 1727.75) perform far worse than random on WikiText-2, and K-FAC "was unable to train effectively." These results suggest hyperparameter tuning or implementation issues for baselines rather than inherent optimizer weakness. The paper should discuss tuning efforts and acknowledge that the comparison is on a skewed playing field.

8. **Contribution C5 (trajectory visualization and explainable FIM measure) is not substantiated**. The paper claims to "develop a new technique that visualizes trajectories across different optimizers" and "introduce an explainable FIM measure," but beyond a single figure in the introduction, these are not described, evaluated, or used in the paper. This contribution is stated but not delivered.

### Trivial

- Table 1 caption says "Trans. denotes Transformers" but the table uses "Trans." as an abbreviation without introducing it.
- The paper states "AdaFisher omits the square root and the traditional EMA applied over the second moment" — this is technically accurate since AdaFisher uses EMA over Kronecker factors instead, but the phrasing could mislead readers into thinking AdaFisher uses no EMA at all.

## Nice-to-Haves

- Add per-iteration complexity analysis (time and memory) comparing AdaFisher to Adam, K-FAC, and Shampoo with concrete numbers, not just qualitative claims.
- Run all baselines for the same number of epochs on ImageNet (e.g., 90 epochs for all) and report learning curves, so readers can assess relative convergence speed transparently.
- Provide the full convergence proof (currently deferred to appendix) and ideally show that AdaFisher's specific approximation satisfies the assumptions (e.g., positive definiteness and bounded condition number of $\tilde{F}_{D_t}$).
- If the normalization layer formulas in Proposition 1 are indeed computing something different from standard K-FAC, clarify the intended computation and justify it with an ablation.

## Removed Points

- **"Insufficient evidence for diagonal dominance" framed as a fatal error** — downgraded to minor because the paper's core validation comes from extensive empirical results, not just the diagonal dominance analysis. The diagonal dominance claim is motivation, not proof.
- **"The claim about omitting EMA is misleading"** — removed. The paper clearly says it omits the *traditional* EMA applied over the *second moment* because it uses a separate EMA on Kronecker factors. This is accurate and not misleading.
- **"Regret bound comparison not fleshed out"** — removed. This is a minor presentational detail that does not affect the paper's substance.
- **Pure formatting/style nitpicks and missing appendix/proof content** — removed per instructions (parser artifacts).

## Novel Insights

The synthetic reviews do not produce a genuinely novel observation about the paper beyond what the paper itself states. The core tension is clear: the method shows broad empirical promise, but several technical gaps (derivation of normalization-layer factors, unclear evaluation protocol, unsubstantiated contribution claims) prevent full confidence. No reviewer identified a previously unseen connection to other work or a counter-intuitive implication of the results.

## Suggestions

1. **Fix Proposition 1**: Correct the normalization-layer Kronecker factor formulas to compute the mean of outer products, not the outer product of means, or justify why the current formulas are intentionally different and validate with an ablation.
2. **Clarify and reform the evaluation protocol**: Remove the ambiguous WCT description. Report all baselines with equal-epoch comparisons AND equal-time comparisons side-by-side. Tune Adam properly on ImageNet (standard Adam with proper scheduling achieves ~76-77%).
3. **Provide all ablation results**: The paper claims extensive ablation studies but does not show them. Add results for (a) with/without min-max normalization, (b) with/without square root, (c) impact of EMA, and (d) corrected vs. current normalization-layer formula.
4. **Expand diagonal dominance analysis**: Add quantitative measures (ratio of diagonal to off-diagonal Frobenius norm, or similar) for multiple layers and at least one transformer architecture.
5. **Either deliver or retract C5**: If trajectory visualization and explainable FIM are genuine contributions, describe and evaluate them. Otherwise remove them from the contributions list.

## Score and Decision

The paper proposes a practical optimizer with consistently positive empirical results across multiple benchmarks, architectures, and modalities. However, the derivation error in Proposition 1, the unclear and potentially unfair ImageNet comparison methodology (with a suspiciously low Adam baseline), and missing ablation results are significant technical weaknesses that preclude acceptance in the current form. The core idea has merit, but the paper does not yet provide sufficient rigor in its method derivation and evaluation to support its claims.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>