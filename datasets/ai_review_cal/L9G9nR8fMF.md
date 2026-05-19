- Decision: Reject
- Avg Score: 6.33
- Scores: 6, 5, 8
Now I have a thorough understanding of the paper. Let me synthesize the review.

## Summary

This paper proposes LayerAct, a family of activation functions that scale each element \(y_i\) by \(s(n_i)\) where \(n_i = (y_i - \mu_y)/\sqrt{\sigma_y^2 + \alpha}\) — using layer-dimension normalized statistics rather than the raw element value. This allows the saturation state to vary per-sample based on layer statistics, rather than being fixed at element-level thresholds. The authors claim this design bypasses the trade-off between one-sided saturation and zero-like mean activation, and provides superior noise-robustness. Experiments on CIFAR-10/100 and ImageNet with ResNets show competitive or better results, especially on corrupted (CIFAR-C, ImageNet-C) benchmarks.

## Strengths

- **Novel activation design.** The core idea — using layer-normalized inputs (rather than raw element values) to compute the activation scale — is a genuine conceptual departure from element-level gate mechanisms (SiLU, HardSiLU, etc.). It is clean, implementable, and well-motivated by the observation that element-level functions have a fixed input-output mapping that couples saturation and the ability to output negative values.

- **Empirical advantage on corrupted benchmarks is demonstrated.** Tables 1–3 show that LA-SiLU and LA-HardSiLU achieve top or near-top accuracy on CIFAR-10-C, CIFAR-100-C, and ImageNet-C. The paper reports that a statistical significance test (p < 0.05) was passed in 30 out of 36 experiments, lending credibility to the claim that the method's noise-robustness advantage is not偶然.

- **Theoretical bounding analysis provides some formal grounding.** Section 3.2 derives upper bounds on activation fluctuation for both element-level activations (Eq. 4) and LayerAct (Eq. 9), showing that \(\|s(\hat{n})-s(n)\| \le \sum_i K|\epsilon_i-\mu_\epsilon|/\sqrt{\sigma_y^2+\alpha}\). This provides a formal, if approximate, argument for why LayerAct can have lower activation fluctuation under small noise when \(\sigma_y\) is not too small.

- **Compatibility with BatchNorm is explicitly discussed and empirically adopted throughout.** All main experiments use standard BatchNorm-based ResNets, so the method is shown to work within the existing CNN+BN paradigm without requiring architectural changes.

## Weaknesses

### Fatal

None. The paper's core claims are not invalidated by any single irrefutable error.

### Major

- **Experimental reporting is incomplete for the number of claims made.** Only ResNet20 results for CIFAR-10/100 are shown in the main text tables (Tables 1, 2). The paper states that ResNet32 and ResNet44 were also trained and that "LA-SiLU outperformed in a significant majority" across 36 experiments, but the actual ResNet32/44 accuracy numbers are not presented. The U-Net / UNet++ experiments (Section 4.3) are mentioned as supporting broader applicability but contain **no quantitative results at all** — no accuracy, Dice score, or any metric. This makes parts of the experimental section an advertisement rather than evidence.

- **The "bypassing the trade-off" claim is asserted rather than formally justified.** Section 3.1 states that LayerAct "bypasses the trade-off between saturation and zero-like mean activation" but provides only a brief example (when \(\mu_y \ll 0\)). What "bypassing" means is never formalized: is it a strict Pareto improvement? An expansion of the achievable (saturation fraction, mean activation) region? The paper does not define the trade-off's terms rigorously, and the critic's counterargument — that saturation still zeros outputs in the saturated regime — is neither acknowledged nor refuted. The mechanism is genuinely interesting (layer-adaptive saturation), but the overblown framing ("bypasses the trade-off") creates an expectation of a formal proof that is not delivered.

- **The noise-robustness bound comparison has acknowledged gaps that are not addressed.** The derivation in Section 3.2 makes two key approximations: (i) \(\sigma_{\hat{y}} \approx \sigma_y\) and \(\mu_{\hat{y}} \approx \mu_y\) (small-noise assumption), and (ii) the simplification from the full expression to \(\sum K|\epsilon_i-\mu_\epsilon|/\sqrt{\sigma_y^2+\alpha}\). The paper notes "when input is not excessively large" but does not quantify this regime or analyze when the bound might fail (e.g., when \(\sigma_y\) is small, the denominator shrinks; the additive \(\alpha\) prevents divergence but the bound can still become looser than the element-level bound). The bound for \(\|s(\hat{n})\|\) is given as "\(\ll d\)" — a vague inequality that is not quantified, making it impossible to compare rigorously against the element-level bound of \(\le d\). These issues do not invalidate the method but weaken the theoretical support for the central claim of superior noise-robustness.

- **No ablation of the stability constant \(\alpha\).** The hyperparameter \(\alpha > 0\) is introduced in Eq. 6 for stability, yet its value is never reported in the experiments and no ablation study explores its effect on training or noise-robustness. Since \(\alpha\) directly affects the denominator \(\sqrt{\sigma_y^2+\alpha}\) in the bound and the normalized input \(n_i\), its value could meaningfully impact both saturation behavior and gradient dynamics.

### Minor

- **No discussion of computational overhead.** LayerAct requires computing \(\mu_y\) and \(\sigma_y\) per layer per forward pass, which is similar to LayerNorm. The paper does not report training time, inference time, or FLOPs relative to element-level baselines. This does not threaten the contribution but is an obvious practical consideration.

- **No standard deviations or error bars are visible in the text for any experimental result.** While the tables (which are images) may include some uncertainty information, the text mentions only mean accuracy over 30 runs without discussing variance. Given that the reported improvements on clean data are sometimes small (e.g., 91.50 vs 91.46), readers need to assess statistical reliability.

- **The gradient computation involves sums over all \(d\) elements** (Eq. 7), which could introduce gradient noise or affect convergence. The paper does not discuss training stability, convergence speed, or compare gradient norms.

### Trivial

- Definition 2.2 of activation fluctuation uses \(\|f(y+\epsilon)-f(y)\| \le c\) without specifying which norm is used; the subsequent derivations implicitly use \(\ell_1\). This should be stated.

## Nice-to-Haves

- **Ablation: LayerAct vs. element-level activation after a separate LayerNorm layer.** Comparing LA-SiLU to SiLU applied after a proper LayerNorm (i.e., \(n_i^{LN}s(n_i^{LN})\)) would isolate whether the advantage comes from the layer-direction normalization *within* the activation or simply from having normalized inputs. This is suggested in the harsh review and is a genuinely useful experiment for positioning the contribution.

- **Ablation on \(\alpha\)** over a range of values, showing its effect on clean/noisy accuracy and on the effective saturation fraction.

- **Empirical distribution of \(\sigma_y\) during training** for a real network, to ground the claim that the denominator \(\sqrt{\sigma_y^2+\alpha}\) is typically large enough for the bound to be favorable.

## Removed Points

These points were flagged by the harsh critic and/or strength finder but are removed after verification against the paper:

- **"The trade-off still exists — it is simply redistributed"** — This is a misinterpretation. The paper's mechanism genuinely changes the per-element saturation logic from fixed-threshold to layer-adaptive, which *does* alter the trade-off structure. The paper's framing is overblown (kept above as a Major weakness), but the critic's specific argument that the trade-off "still exists" in the same form is not correct.

- **"No comparison to GELU, Swish variants, or other recent activations"** — The paper compares against ReLU, LReLU, PReLU, Mish, SiLU, HardSiLU. This is a reasonable baseline set. Adding more baselines would strengthen the paper but its absence is not a weakness.

- **"The paper fails to engage with known limitations"** — Generic framing; the specific concerns about \(\sigma_y\) and gradient complexity are retained as Major/Minor weaknesses above.

- **"LayerAct does not replace BatchNorm"** — The paper explicitly states it works *with* BatchNorm ("While maintaining the batch-direction normalization methods..."). This is by design, not a flaw.

- **"Missing related works"** — Removed per instructions (cannot verify external sources).

- **"Missing appendix content"** — Appendices are stripped by the parser; they exist in the original submission.

- **Formatting/style nitpicks, typos, grammar issues** — Removed per instructions (parser artifacts).

- **Strength Finder strengths that are generic** (e.g., "this paper addressed an important problem") — Removed; only concrete, specific strengths are retained above.

## Novel Insights

None beyond the paper's own contributions. The review surfaces a consistent tension: the paper's core idea is genuinely novel and the noisy-benchmark results are promising, but the theoretical framing claims more than the analysis supports, and the experimental reporting is incomplete for the breadth of claims made. The most actionable insight is that the "bypassing the trade-off" claim needs either formalization (with a definition of the achievable region) or retraction to a more measured claim (e.g., "adaptively redistributes saturation to enable per-element negative outputs when layer statistics allow it").

## Suggestions

1. **Present all experimental results** — include tables for ResNet32 and ResNet44 on CIFAR, and either show U-Net results quantitatively or remove Section 4.3.
2. **Either formalize the "bypassing the trade-off" claim or soften it.** Define the trade-off as a set of achievable (saturation fraction, mean activation) pairs and show that LayerAct expands this set relative to element-level functions. Or simply state that LayerAct "adaptively redistributes saturation" — which is still an interesting contribution.
3. **Tighten the noise-robustness analysis.** Quantify the "\(\ll d\)" bound for \(\|s(\hat{n})\|\). Provide an empirical histogram of \(\sigma_y\) over layers during training to support the claim that the denominator is typically large.
4. **Report the value of \(\alpha\) used** and add a brief ablation over a range (e.g., \(\alpha \in \{1e^{-4}, 1e^{-3}, 1e^{-2}, 1e^{-1}, 1\}\)) showing clean and corrupted accuracy.
5. **Add a brief computational cost comparison** (training time per epoch or relative FLOPs) to help readers assess practical deployability.
