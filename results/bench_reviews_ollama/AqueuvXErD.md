Now I have a thorough understanding of the paper and can evaluate the reviewer claims. Let me synthesize the final review.

## Summary

This paper challenges the prevailing assumption that classification robustness and explanation robustness in adversarially trained models are strongly correlated. Through loss landscape visualization, the authors observe that adversarial training flattens the input loss landscape w.r.t. classification loss but not w.r.t. explanation loss. They propose a training method (SEP) that adds a regularization term $\mathcal{L}_f = \|I(x + \zeta) - I(x)\|$ with positive or negative $\lambda$ to manipulate explanation loss landscape flatness. Experiments across 5 datasets, 4 architectures, and 3 explanation methods show that SEP can dramatically change explanation robustness while maintaining similar adversarial accuracy, suggesting the two forms of robustness can be decoupled.

## Strengths

- **Novel landscape asymmetry finding**: The observation that adversarial training flattens the classification loss landscape but not the explanation loss landscape (Figure 3) is genuinely novel and significant. This directly motivates the SEP method and provides new insight into why classification and explanation robustness may have different underlying mechanisms.

- **Demonstrable manipulation of explanation robustness via SEP**: The SEP method successfully modulates explanation robustness (both increasing and decreasing it) while preserving classification robustness in many settings. For instance, on CIFAR10 ConvNet (Table 2), SEP_pos achieves Expl at End = 1.269 vs. SEP_neg at 7.590 while maintaining identical adversarial accuracy (~35%). These cases where the start values are comparable show a clean and convincing separation.

- **Extensive experimental breadth**: The decoupling is tested across 5 datasets (MNIST, FMNIST, CIFAR10, CIFAR100, TinyImageNet), 4 architectures (ConvNet, ResNet18, Wide ResNet, MobileNetV2), and 3 explanation methods (Gradient, Gradient×Input, Guided Backpropagation), as well as cross-method training/testing and both MAT and TRADES adversarial training.

- **Cross-explanation-method generalization**: Figure 5 shows the SEP effect persists when training with one explanation method and testing with another, ruling out that the finding is an artifact of a single explanation method.

## Weaknesses

### Fatal
None.

### Major

- **The explanation robustness metric is confounded by explanation map magnitude, and the paper does not resolve this confound despite acknowledging it.** The paper measures explanation robustness as the absolute explanation loss after attack: $\|I(x_v + \epsilon) - I(x_t)\|$. Models producing explanation maps with larger norms will have higher absolute explanation losses both before and after attack, inflating the appearance of robustness. The paper itself acknowledges on p.336: "The different performance w.r.t. explanation loss at end for $SEP_{pos}$ and $SEP_{neg}$ is mainly induced by the difference in explanation loss at start." Yet no normalization is attempted. Computing relative reductions reveals the issue: on MNIST ConvNet, MAT reduces explanation loss by 20.0% (373.262→298.729), while SEP_neg reduces by only 18.5% (806.204→657.180) — meaning the attack is *more* effective in relative terms against SEP_neg, contradicting the paper's "strongest robustness" label. On CIFAR10 ResNet18, SEP_neg reduces by 48.3% vs. MAT's 31.5%, again showing the attack is *more* relatively effective. No normalized metric (relative reduction, cosine distance, or L2 on unit-normalized maps) is ever computed. This confound undermines interpretation of the "decoupling" in the most dramatic cases, though it is less severe in settings where start values are similar (e.g., CIFAR10 ConvNet: MAT start=16.9 vs. SEP_neg start=19.0).

- **Several $SEP_{neg}$ models show severe clean accuracy degradation, suggesting model degeneration rather than controlled manipulation.** On CIFAR10 ResNet18 (Table 2), SEP_neg drops clean accuracy from 67.22% (MAT) to 39.17% — a 28-point collapse — while Expl at Start explodes to $70.159 \times 10^{-7}$ vs. 31.959 for MAT. In Table 3 (Gradient, ResNet18), SEP_neg achieves only 49.38% clean accuracy (vs. 67.22% for MAT) with Expl at Start of $8282.990 \times 10^{-7}$. These are degraded models with potentially unstable gradient magnitudes, not models operating in a normal regime. The paper acknowledges the clean accuracy drop (p.338) but frames it as supporting evidence for decoupling rather than recognizing it may invalidate the comparison. When clean accuracy collapses by 20-30 points and explanation norms inflate by 10-100x, claiming "better explanation robustness" based on higher absolute explanation loss is not meaningful. This issue affects the most dramatic cases but not all settings (e.g., MNIST SEP_neg maintains 99.4% clean accuracy).

### Minor

- **The headline claim that classification and explanation robustness are "not strongly correlated" overstates what the evidence shows.** Table 1 (TRADES with varying α) demonstrates a clear monotonic correlation under standard training conditions. The SEP intervention breaks this correlation, but finding a targeted manipulation that decouples two quantities does not prove they are "not strongly correlated" — it proves the correlation is not *inherent* or *necessary*. The paper's language sometimes overclaims ("there is no inherent relationship," p.336), when the evidence more carefully supports: "the correlation can be broken by a specific regularizer targeting explanation loss landscape flatness." The conclusion (p.396) is more measured ("potential lack of a strong correlation"), which is better.

- **Loss landscape flatness claims rely on visual inspection of a single random direction without quantitative measurement.** Figure 3 is the sole evidence that increasing explanation robustness does not flatten the explanation loss landscape. No curvature measurement, spectral analysis, or multi-direction evaluation is provided to substantiate this visual observation quantitatively.

- **The asymmetric hyperparameter values ($\lambda = +50000$ vs. $-3000$) are not explained.** This large asymmetry means $SEP_{pos}$ and $SEP_{neg}$ are not mirror-image manipulations of the same mechanism, complicating the clean interpretation of their comparison.

- **No standard deviations or multiple runs are reported.** Given the stochastic nature of adversarial training and the extreme hyperparameter values used, variance information would strengthen the reliability of the reported results.

### Trivial
None.

## Nice-to-Haves

- A normalized explanation robustness metric (e.g., relative reduction $\frac{\text{Start} - \text{End}}{\text{Start}}$, or cosine distance on unit-normalized explanation maps) would directly resolve the confound and make the core claim evaluable. This is the single most impactful improvement the paper could make.

- Quantitative flatness measurements (curvature, spectral properties, or multi-direction evaluations) would substantiate the landscape claims beyond visual inspection.

- Analysis of explanation map norms and visualizations for SEP_neg models in the degenerate regime (e.g., CIFAR10 ResNet18) would clarify whether the high explanation loss is genuine robustness or a scale artifact.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The clustering method for selecting 150 images is never validated"** — The paper provides qualitative evidence (Figure 2) that same-cluster images share similar explanations. While quantitative validation would be nice, the clustering is a practical evaluation efficiency tool, not a core contribution. This is scope creep relative to the paper's main claims. Demoted to nice-to-have.

- **"The choice to use random noise rather than min-max formulation... means the regularizer may be optimizing something different from landscape flatness"** — The paper justifies this choice on p.165 with a reasonable argument about computational cost and overfitting risk in the targeted setting. The justification is adequate for the paper's purpose, which is to provide a mechanism for landscape manipulation, not to prove equivalence with a theoretical ideal.

- **"Softplus instead of ReLU is not ablated"** — The paper states this is needed for the explanation attack method (p.223) and that softplus is close to ReLU. This is a reasonable engineering choice, not a methodological flaw.

- **"Only 25 training epochs"** — The adversarial accuracies are consistent across methods, suggesting reasonable convergence. If training were insufficient, it would affect all methods similarly and not bias the comparison.

- **"Parameter sensitivity only tests six values with a gap"** — Table 4 shows a smooth trend across the tested values. More values would be nice but the existing data is informative enough.

- **Strength removed: "Causal demonstration of decoupling"** — While the SEP method can manipulate explanation robustness relatively independently, calling it a "causal demonstration" overstates the case given the metric confound issue. The effect is real in some settings but the causal interpretation is undermined by the lack of normalized evaluation.

## Novel Insights

The most novel insight in this paper is the asymmetry between the classification and explanation loss landscapes under adversarial training: while AT flattens the classification loss landscape (a known result), it does not flatten the explanation loss landscape. This is unexpected because prior work assumed the mechanisms were coupled. The SEP training method exploits this asymmetry by directly regularizing the explanation loss landscape flatness. However, the paper's claim that this demonstrates the two robustnesses are inherently decoupled is weakened by the fact that the metric for explanation robustness (absolute explanation loss) conflates genuine robustness with explanation map scale — a confound the paper acknowledges but doesn't resolve. The landscape asymmetry observation itself is genuine and important regardless of whether the robustness metrics are confounded.

## Suggestions

- Add a normalized explanation robustness metric (e.g., relative reduction or cosine distance) and re-evaluate the core tables. If the SEP effect persists under normalization in most settings, the central claim is greatly strengthened; if it disappears, the claim needs to be substantially moderated.

- Moderate the language from "no inherent relationship" to "the correlation can be broken via targeted landscape manipulation" — this is what the evidence actually supports, and it remains an important finding.

- Flag and exclude from the comparison any SEP_neg models where clean accuracy drops more than ~5-10% below MAT, or explicitly discuss them as edge cases where model degeneration rather than controlled manipulation is likely occurring.

## Score and Decision

The paper identifies a genuinely novel and important asymmetry between classification and explanation loss landscapes under adversarial training, and proposes an interesting mechanism (SEP) to manipulate explanation robustness independently. However, the central empirical claim — that classification and explanation robustness can be fully decoupled — is undermined by two significant issues: (1) the absolute explanation loss metric confounds robustness with explanation map magnitude (acknowledged but not resolved), and (2) the most dramatic "decoupling" cases involve severely degraded models. In cleaner settings (CIFAR10 ConvNet, CIFAR100, TinyImageNet) where start values are comparable and clean accuracy is maintained, the decoupling is modest and convincing. The core landscape asymmetry observation is valuable regardless. The paper would be substantially improved by adding normalized metrics and moderating its claims, but the contribution is real.

**Originality**: Novel — the landscape asymmetry observation and SEP method are both new contributions.  
**Importance of research question**: High — the relationship between classification and explanation robustness is a fundamental question.  
**Claims well supported**: Partially — landscape observation is supported; robustness decoupling claim is partially undermined by metric confound.  
**Experimental soundness**: Broad but has evaluation metric issues in critical cases.  
**Clarity**: Adequate — core ideas are clearly presented.  
**Value to community**: Genuine contribution that opens a new research direction.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Borderline</orange>