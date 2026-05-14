## Summary

This paper proposes EDPA (Embedding Disruption Patch Attack), a model-agnostic adversarial patch attack targeting Vision-Language-Action (VLA) models, along with an adversarial fine-tuning defense. The attack requires only access to encoder parameters (not full model architecture or action space knowledge), uses two objectives — a patch contrastive loss and an image-instruction alignment loss — to disrupt latent representations. Evaluated on three VLA models (OpenVLA, OpenVLA-OFT, π₀) across four LIBERO task suites, EDPA substantially increases failure rates (e.g., near 100% on OpenVLA). The defense reduces failure rates against EDPA (average 34.2% decrease) and also generalizes to prior attacks (UADA, UPA), though with high residual failure rates on harder suites.

## Strengths

- **Practical, less restrictive attack design**: EDPA requires only access to encoder parameters and does not need knowledge of the model's action space, LVLM backbone, or robotic manipulator. Table 1 systematically compares requirements with prior work (UADA, UPA), making the practical advantage clear. This is a genuine step forward for adversarial evaluation of VLA models.

- **Demonstrated effectiveness across diverse VLA architectures**: EDPA is tested on three distinct models (OpenVLA, OpenVLA-OFT, π₀) across four LIBERO task suites. On OpenVLA, EDPA achieves near 100% failure rates across all suites. On multi-camera models, it increases failure rates by 62.0% (OpenVLA-OFT) and 31.4% (π₀) on average. The consistent trends across models and suites provide a reasonable empirical picture.

- **Defense shows non-trivial robustness gains and transfers to other attack types**: The adversarial fine-tuning scheme reduces failure rates not only for EDPA (34.2% average decrease on OpenVLA) but also for UADA (19.1%) and UPA (36.0%), as shown in Table 2. Clean performance impact is modest (+1.6% average failure rate increase). That the defense improves robustness against attack methods it was not trained on is a meaningful result.

- **Insightful qualitative analysis of patch patterns**: Section 5 offers a grounded hypothesis linking patch appearance (resembling robotic manipulator structures) to visual encoder overfitting caused by limited datasets and restricted camera viewpoints. While speculative, this provides a useful framework for understanding differential robustness across models.

## Weaknesses

### Major

- **Defense claims are overstated relative to evidence**: The abstract and conclusion state the defense "effectively mitigates" the degradation, but Table 2 tells a more nuanced story. After defense on OpenVLA, residual failure rates against EDPA are: Spatial 39.4%, Object 58.6%, Goal 73.9%, Long 91.2%. On the Long suite, the defense barely moves the needle (from 100% to 91.2%). Describing a defense that leaves failure rates above 50% on three of four suites (and above 90% on one) as "effectively mitigating" is misleading. The defense is clearly beneficial on some suites (Spatial improvement from 100% → 39.4% is substantial) but the framing in the abstract and conclusion needs to be tempered with honest quantification of residual failures.

- **No ablation of the two loss components**: The core attack method combines a patch contrastive loss and an image-instruction alignment loss with α₁=0.8. The defense uses two L2 terms with α₂=0.5. Without ablating each component independently (α₁=0 or 1, α₂=0 or 1), there is no evidence that both objectives are necessary or that the specific weightings are justified. This is not a minor hyperparameter detail — the paper's methodological contribution rests on the claim that these two losses are "complementary." An ablation is essential to support this.

- **Defense evaluated on only one model**: The adversarial fine-tuning defense is tested exclusively on OpenVLA. The paper's justification (OpenVLA showed weakest robustness) is reasonable as a starting point, but the defense is presented as a general strategy. Without testing on at least one other VLA (e.g., OpenVLA-OFT), claims about generality are unsupported. This significantly limits the contribution of the defense half of the paper.

### Minor

- **No attempt to apply prior attacks (UADA/UPA) to OpenVLA-OFT or π₀**: The paper motivates EDPA partly by arguing that prior attacks are "difficult to transfer" to models beyond OpenVLA due to their stringent requirements. Table 1 makes the architectural requirements clear, which supports this claim logically. However, the practical advantage would be more convincing if the paper demonstrated attempted adaptation and reported the outcome, even if unsuccessful. As-is, the advantage is asserted rather than empirically shown.

- **Defense reduces random-noise failure rate below clean rate on Object suite**: After defense on Object suite, clean failure rate is 17.3% while random noise is 16.0% (Table 2). This inversion is suspicious — it suggests the defense may be making the encoder overly invariant to small perturbations in ways that could harm discriminative ability not captured by the clean failure rate alone. The paper does not discuss this.

- **Defense objective tension not discussed**: Equation (5) minimizes two L2 terms that both use the original encoder's clean embeddings as the target. This forces the fine-tuned encoder to match the *original* encoder's output for both clean and adversarial inputs. If (as the paper hypothesizes in Section 5) the original encoder overfits to the robotic arm appearance, anchoring to the original encoder's representations may preserve the very vulnerability being defended against. This tension is not addressed.

- **Patch contrastive loss direction could confuse readers**: Equation (2) presents a standard InfoNCE loss, but the optimization in Equation (4) maximizes it (rather than minimizing it, as is typical). The paper should explicitly clarify that this pushes positive pairs apart, since readers familiar with contrastive learning will expect minimization.

### Trivial

- The paper reports hyperparameters and references Appendix C for sensitivity analysis (which was stripped by the parser, but the reference exists in the original submission).

## Nice-to-Haves

- Ablation studies of the two loss components for both attack and defense (α₁ and α₂).
- Defense evaluation on at least one additional VLA model (e.g., OpenVLA-OFT).
- Analysis of why the Long suite's residual failure rate remains so high (91.2%) — e.g., longer horizon, more steps.
- Attempt to adapt UADA/UPA to OpenVLA-OFT or π₀, even if approximations are needed, to empirically ground the claimed practical advantage.
- t-SNE/PCA visualization of embeddings from the fine-tuned encoder to directly show the defense reduces clean-adversarial representation discrepancy.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism that "model-agnostic" claim is overstated because EDPA requires encoder access**: The paper explicitly defines "model-agnostic" as not requiring knowledge of architecture, action space, or robot platform — not as full black-box access. Table 1 clearly shows what EDPA requires vs. what prior attacks require. The paper is precise about this. (Removed: misreading of the paper.)

- **Criticism about ambiguous expectation in Equation (4) and universal vs. per-sample patch**: Algorithm 1 clearly shows δ is initialized once and iteratively refined — it is a universal patch. The text also states "universal adversarial patch." (Removed: critic missed Algorithm 1.)

- **Reproducibility concerns about missing appendix content, patch placement details, number of patches per camera**: The parser strips appendix sections; they exist in the original submission. The paper references Appendix C for hyperparameter sensitivity analysis. (Removed: parser artifact.)

- **Criticism that π₀ results should temper "highly effective" claim**: EDPA increases π₀ failure rate from ~14.7% average clean to ~46.1% (31.4% increase), and from ~19.4% random to ~46.1%. This is a substantial and consistent effect across all four suites. The claim is reasonably supported. (Removed: not a valid concern — the numbers speak for themselves.)

- **Criticism about missing related works and references**: I do not have external sources to confirm what the paper should have cited. (Removed: per instructions.)

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Temper the defense claims in the abstract and conclusion**. Replace "effectively mitigates" with precise language, e.g., "reduces failure rates by X% on average but with high residual rates on longer-horizon tasks." Acknowledge the Long suite limitation explicitly upfront.

2. **Add ablation experiments for α₁ and α₂** (or at minimum for the two attack loss components). Show failure rates with only patch contrastive loss (α₁=1), only alignment loss (α₁=0), and the combined setting. This is necessary to justify the "complementary" claim.

3. **Run the defense on at least one additional model** (OpenVLA-OFT would be the natural choice given the data already exists). Even a single additional data point would substantially strengthen the generality claim.

4. **Discuss the suspicious inversion** where random-noise failure rate drops below clean rate after defense, and the potential tension of anchoring to the original encoder's representations.

5. **Attempt to apply UADA/UPA to OpenVLA-OFT and π₀** (even with approximations or reporting that the methods cannot be adapted). This would empirically ground the claimed practical advantage of EDPA.

## Score and Decision

**Anchors used for calibration** (from human review corpus):

| Anchor | Score | Comparison |
|--------|-------|------------|
| FreezeVLA (zdvlLxRWSn.md) | 3.00 | Similar topic (adversarial attacks on VLA). Weaker threat model, no defense contribution. Current paper is stronger. |
| VLA-Risk (31EjDFwFEe.md) | 2.50 | Benchmark paper with limited methodological novelty. Current paper has stronger methodological contribution. |
| Clean-Action Backdoor (QQdn8nNqgi.md) | 3.50 | Backdoor attack on π₀ only, narrow evaluation. Current paper evaluates more models and has a defense. Current paper is stronger. |
| BEAT (OwinX7PI83.md) | 5.50 | Backdoor attack with novel contrastive learning, good evaluation. Comparable scope to current paper, which has a practical attack advantage but weaker defense evaluation. |
| RobustVLA (cS6xizdYD5.md) | 6.00 | Broader robustness study (17 perturbations), includes real-world validation. Current paper is narrower and lacks real-world experiments. Current paper is weaker. |

The paper's attack contribution is solid and practically motivated — EDPA's reduced requirements relative to UADA/UPA are a genuine advance for adversarial evaluation of VLA models. The evaluation across three models is reasonably broad. However, the defense is weaker than claimed (high residual failure rates, tested on only one model), and the missing ablations undermine confidence in the methodological design choices. The paper's contributions are sufficient to warrant acceptance if the defense claims are tempered. Score positioned relative to anchors: stronger than the rejected papers (2.5-3.5 range) and comparable to BEAT (5.5) but weaker than RobustVLA (6.0).

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>