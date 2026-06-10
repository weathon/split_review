## Summary

This paper proposes a method for training Binary Neural Networks (BNNs) without storing real-valued weights during training. Binary weights are updated via a stochastic "hypermask" whose flip probability is derived to match the expected behavior of real-space SGD in expectation. The authors define two principled properties (Expectation Matching Property / EMP and Matching Maximization Property / MMP), prove the corresponding mask distributions, and evaluate on MNIST, CIFAR-10, and CIFAR-100 in fine-tuning settings from ImageNet-pretrained backbones.

## Strengths

1. **Principled theoretical framework for binary-space updates.** The paper defines formal desiderata (EMP, MMP) and proves Theorems 1–3 showing the exact mask distributions needed to satisfy them. This provides a probabilistic grounding that goes beyond heuristic gradient approximations (STE, gradient quantization) commonly used in BNN training.

2. **First demonstration of CIFAR-100 fine-tuning without retaining real-valued weights.** Tables 3 and 4 show that EMP Mask achieves accuracy comparable to real-space methods (STE, BOP, ReSTE) on CIFAR-10 and CIFAR-100 when fine-tuning from ImageNet-pretrained backbones, while eliminating real-valued weight storage during the fine-tuning process. This is a practically relevant result for edge-device personalization.

3. **Thorough memory analysis with explicit accounting.** Section 4 and Table 2 provide a detailed breakdown of per-variable memory usage. The 33× bound is correctly stated as asymptotic ($L\to\infty$, $B\ll D_{\text{hid}}$) and concrete savings are given for practical settings (e.g., ~10× at $L=50$, ~27% of peak memory for the CNN fine-tuning in Table 4).

4. **Empirical validation that the EMP property holds.** Figure 3 shows close alignment between the EMP mask probability and the actual sign-flipping probability measured from real-space training on real data, confirming the theoretical guarantee translates to practice.

5. **Generalization to convolutional layers.** Table 4 demonstrates the method works on full CNN architectures (AdamBNN/MobileNetV1) when fine-tuning all layers, not just MLP headers.

## Weaknesses

### Major

1. **Abstract claims an experiment that does not exist in the paper.** The abstract states: "Our method yields test results on Tiny-ImageNet comparable to baselines that utilize real weights during training." However, the experiments section (5.1) evaluates only on MNIST, CIFAR-10, and CIFAR-100 — no Tiny-ImageNet experiment is presented. This is a factual error that would mislead readers. Separately, the contribution claim about CIFAR-100 is supported only by fine-tuning experiments on ImageNet-pretrained backbones, while the surrounding text contrasts with prior from-scratch discrete optimization work (Kurtz & Bah, 2021). The framing implies a stronger result (from-scratch training on CIFAR-100) than is actually demonstrated.

2. **Theoretical assumptions verified only on a small FCN on MNIST, not on the actual evaluation tasks.** Section 5.2 validates the Gaussianity and independence assumptions ($\Omega_{t-1}\perp\!\!\!\perp G_t$, Gaussian distributions) on a small fully-connected network trained on MNIST — the simplest possible setting. The correlation found ($r=-0.118$) is described as "small but not negligible." The method's main results (Tables 3–4) are on CNN architectures with batch normalization, residual connections, and ImageNet-pretrained features, where weight-gradient distributions may differ substantially. No analysis of robustness to assumption violations in those settings is provided, weakening the link between theory and reported performance.

### Minor

3. **Random mask competitiveness questions the value of gradient-derived probabilities.** In Table 5 (from-scratch MNIST), the random mask with cosine decay performs nearly as well as the EMP mask on the large MLP (2.45% vs. 2.44% test error). The paper notes this but does not analyze what it implies — if a mask that ignores gradient magnitudes entirely achieves similar results, the gradient-dependent probability modeling may not be the key mechanism. A controlled comparison on the CIFAR fine-tuning tasks would clarify whether the theoretical machinery provides measurable benefits over simpler scheduling.

4. **No hyperparameter sensitivity analysis for the initial temperature.** The method requires selecting $\sigma_0$ (equivalently the initial temperature $\tau_0$) which controls the entire update dynamics via Eqs. (15)–(17). No study of sensitivity to this parameter is reported, making it unclear how robust the method is to this choice.

5. **No wall-clock time comparison.** The method requires evaluating $\mathrm{erf}$ for each binary weight at each iteration. No training-time comparison (seconds per iteration or total training time) is provided, so the computational overhead of the erf computations relative to simpler alternatives is unknown.

### Trivial

None.

## Nice-to-Haves
- A from-scratch experiment on CIFAR-10 would strengthen the claim about dataset scale, though the paper scopes fine-tuning as the realistic use case.
- An ablation comparing EMP mask vs. random mask with matched effective flip rates on the CIFAR fine-tuning tasks would clarify whether gradient-magnitude information provides measurable benefits in the settings where the method performs best.

## Removed Points
- *"The method still requires real-valued gradients — memory savings are more limited than the 33× headline suggests."* **Removed because:** The paper explicitly acknowledges this limitation (Section 4: "our proposed method still needs real-valued gradients, which can be the bottleneck"), the 33× is qualified as asymptotic, and concrete practical numbers are provided. The paper is fully transparent about this.
- *"MMP mask underperforms consistently."* **Removed because:** The paper identifies and explains the failure mode (sign-flipping probability drops below 50% early, causing the mask to be always 0). This is a well-analyzed experimental finding, not a weakness of the paper.
- *"Gradient storage remains a bottleneck — this makes the contribution incremental."* **Removed because:** The paper acknowledges this in Section 6 and discusses gradient quantization as future work. The contribution is eliminating real-valued *weight* storage, which is the larger storage component in deep networks; the paper scopes itself honestly.
- *"The paper overclaims about CIFAR-100 (from-scratch)."* **Rephrased and merged into Major weakness #1:** the claim is technically about fine-tuning, which the paper is transparent about in Section 5.1, but the framing alongside from-scratch baselines is potentially misleading.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Remove or substantiate the Tiny-ImageNet claim in the abstract — if no such experiment was conducted, replace with the datasets actually evaluated.
2. Clarify in the abstract and contributions that the CIFAR-100 results are from fine-tuning ImageNet-pretrained backbones, and explicitly note the distinction from prior from-scratch discrete optimization work.
3. Add a controlled comparison (EMP vs. random mask with matched effective flip rates) on at least one CIFAR fine-tuning task to demonstrate the value of gradient-magnitude modeling beyond what a simple schedule provides.
4. Report wall-clock training time per iteration and total training time.
5. Add a sensitivity analysis for the initial temperature / $\sigma_0$ hyperparameter.

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Reject</decision>