Now I have all the information needed. Here is the consolidated review.

---

## Summary

NEPENTHE proposes an unstructured pruning method that reduces neural network depth by guiding the pruning budget toward layers with low neuron entropy. The paper defines a per-neuron entropy based on how often a rectifier-activated neuron is in its ON vs. OFF state, provides a theoretical derivation showing that magnitude pruning naturally reduces this entropy under Gaussian assumptions, and designs an entropy-weighted budget allocation that concentrates pruning on low-entropy layers to drive their average entropy to zero—making them linearizable and removable. Results are shown on ResNet-18, MobileNet-V2, and Swin-T across several datasets.

## Strengths

- **Novel entropy-guided framework for depth reduction.** Unlike prior entropy-based pruning that targets filters/channels (Luo 2017, Hur 2019) and unlike activation-level approaches such as Layer Folding (Dror 2021) that directly force activations to be linear, NEPENTHE uses unstructured pruning guided by a neuron-scale entropy measure to make entire layers linearizable. This is a genuinely new mechanism for depth reduction.

- **Theoretical analysis linking unstructured pruning to entropy reduction.** Section 3.2 derives that, under Gaussian assumptions on weights and inputs, increasing the magnitude-pruning threshold monotonically decreases a rectifier-activated neuron's output entropy (Eqs. 7–14, Fig. 2c). This formal insight—that unstructured pruning naturally drives neurons toward deterministic ON/OFF states—was not previously established and provides a principled motivation for the approach.

- **Clear empirical demonstration that NEPENTHE drives layers to zero entropy.** Table 1 shows that after NEPENTHE, three layers in ResNet-18 on CIFAR-10 reach exactly zero entropy while accuracy improves slightly (92.55% vs. 91.66% dense). In contrast, iterative magnitude pruning (IMP) at comparable sparsity reduces entropy across all layers but presses none to zero. This visually separates the method from vanilla pruning and directly supports the core claim.

- **Tested across diverse architectures and activation functions.** Results span CNNs (ResNet-18, MobileNet-V2) and a Transformer (Swin-T), across five datasets. Table 5 (activation analysis) shows the method works with ReLU, SiLU, PReLU, LeakyReLU, and GELU—all removing three layers with no performance drop. This breadth supports generality beyond a single architecture family.

- **Honest limitations section.** The paper explicitly acknowledges that the method fails on under-fitting architectures (e.g., ResNet-18 on ImageNet) and that the iterative procedure is computationally inefficient. This candor helps readers scope the contribution appropriately.

## Weaknesses

### Fatal

None.

### Major

1. **No measurement of practical efficiency gains from layer removal.** The paper repeatedly motivates depth reduction for real-time applications and edge devices (abstract, introduction), yet it provides no FLOPs, latency, or throughput measurements after removing zero-entropy layers. Showing that layers reach zero entropy is a necessary condition, but the paper never verifies that removing them actually reduces the critical path or speeds up inference. Without efficiency metrics, the practical impact claimed in the title and abstract is asserted, not demonstrated.

2. **Ablation study does not isolate the entropy-weighting contribution.** Table 4 shows that adding components (entropy weighting, don't-care state, neuron filtering) progressively improves accuracy. However, the baseline row ("no entropy") is simply the dense model—not a version that performs the same iterative pruning with a uniform or magnitude-only budget allocation across layers. Without this comparison, it is impossible to tell whether the entropy reweighting is responsible for driving layers to zero entropy, or whether any aggressive pruning schedule in the same layers would achieve similar results. This is the most informative ablation that is missing.

3. **No error bars or variance reporting.** Given the iterative nature of the algorithm, results could vary across seeds. No confidence intervals, standard deviations, or multi-run statistics are reported for any experiment. This is a standard expectation for empirical ML papers and is especially important here because the performance gap between methods is sometimes small (e.g., 92.55 vs. 91.90 for Layer Folding on CIFAR-10).

### Minor

- **The theoretical derivation is loosely coupled to the actual algorithm.** The theory (Sec. 3.2) shows that magnitude pruning reduces neuron entropy under an idealized Gaussian model. But NEPENTHE's contribution is the *entropy-weighted budget allocation* (Eq. 6–7), not magnitude pruning itself. The theory supports the observation that pruning reduces entropy, but it does not explain why the specific entropy-weighting mechanism in Eq. 6–8 is superior to simpler alternatives (e.g., pruning more aggressively in low-entropy layers via magnitude alone). The paper states "driven by the promising theoretical results" (line 226), but the jump from the theory to the specific score design is not formally motivated.

- **No hyperparameter sensitivity analysis.** The hyperparameter ζ (fraction of parameters pruned per iteration) is set to different values per architecture (0.5 for ResNet-18, 0.25 for Swin-T, 0.1 for MobileNet-V2) with no analysis of how this choice affects the number of layers removed or final accuracy. The stopping threshold θ is mentioned but never discussed. Understanding sensitivity to these parameters is important for practical use.

- **No convergence or iteration analysis.** The paper does not report how many pruning iterations are needed to reach zero-entropy layers, or how the method behaves with more/fewer iterations. This makes it hard to assess the computational cost of the method.

- **Computational overhead of entropy computation is not discussed.** Calculating neuron entropy requires a full forward pass over the training set at each pruning iteration (line 259). For large models, this is non-trivial. The paper does not discuss this cost or compare it against potential savings.

- **The post-pruning handling of zero-entropy layers is underspecified.** The algorithm (Alg. 1) continues iterating after layers reach zero entropy, but it is unclear whether these layers are subsequently skipped in the pruning budget computation. The score function (Eq. 6) implicitly assigns ℛ_l = 0 for zero-entropy layers, which prevents further pruning there, but this is not explicitly stated.

### Trivial

None.

## Nice-to-Haves

- Additional depth-reduction baselines (e.g., DepthShrinker, channel-wise non-linearity removal methods mentioned in Sec. 2) would strengthen the empirical positioning, though the comparison to Layer Folding and IMP is already reasonable.
- A larger-scale experiment (e.g., CIFAR-100 with ResNet-18 or a moderately sized task beyond small-domain datasets) would increase confidence in the method's generalizability.
- The theoretical derivation (Sec. 3.2), while elegant, could be condensed or moved to an appendix to free space for more experimental analysis without loss of narrative flow.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Overstates that most approaches are unable to reduce layers" (Harsh Critic):** The paper's claim that "most of the approaches are unable to reduce the number of layers in a DNN" (line 29) is factually accurate about the broader compression literature (quantization, width pruning). The paper later discusses depth-reduction works in Related Works. The statement is not overreaching. → **Removed as factually correct characterization, not a weakness.**

- **"The theory should be moved to appendix":** A preference about paper organization, not a weakness. → **Removed as a formatting/style preference.**

- **"The 'don't care state' handling is ad hoc":** The handling is clearly explained (Eq. 3) and follows naturally from the definition. No genuine flaw. → **Removed as a nitpick.**

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a structural flaw or overlooked implication that the authors themselves missed. The main tension identified—that the theory motivates pruning for entropy reduction but not the specific weighted budget allocation—is a real but expected gap between a theoretical motivation and a heuristic algorithm design, not a novel observation.

## Suggestions

1. **Add FLOPs, latency, or throughput measurements** for the post-removal model (after physically removing or folding zero-entropy layers). This is the single most impactful addition and directly addresses the motivating framing of the paper.

2. **Add a proper ablation:** Compare NEPENTHE against the same iterative pruning schedule but with uniform budget across layers, and with magnitude-only budget allocation. This would isolate the effect of the entropy weighting and directly answer the most important question about the design.

3. **Report error bars** (mean ± std over at least 3 seeds) for the main results, especially where performance differences between methods are small.

4. **Add a hyperparameter study** showing how ζ and θ affect the number of layers removed and final accuracy, at least for one representative architecture/dataset pair.

## Score and Decision

The paper introduces a genuinely novel and well-motivated idea for neural network depth reduction, with a clear theoretical motivation and encouraging preliminary evidence that the method can drive layers to zero entropy. However, the experimental validation has significant gaps: no efficiency measurements despite practical framing, an ablation that does not isolate the core design choice, and no statistical rigor. These gaps prevent the paper from convincingly supporting its claims in its current form. The core contribution is real and the path to a stronger paper is clear.

**Score:** 5.0

**Decision:** Reject

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>