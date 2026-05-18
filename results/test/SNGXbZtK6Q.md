Now I have all the verification I need from the paper. Let me produce the consolidated review.

## Summary

This paper studies out-of-distribution (OOD) problems through the lens of neuron activation coverage (NAC). The authors define a neuron activation state that combines raw neuron output with KL-divergence gradients (Input⊙Gradient formulation), then derive a coverage function from the probability density of these states over InD training data. They apply NAC to two tasks: (1) OOD detection (NAC-UE), where low coverage scores signal OOD inputs, and (2) model evaluation for OOD generalization (NAC-ME), where the integrated coverage serves as a proxy for robustness. NAC-UE achieves strong average SOTA across CIFAR-10, CIFAR-100, and ImageNet benchmarks; NAC-ME shows a consistent but modest positive correlation with OOD test accuracy that often exceeds simple validation accuracy.

## Strengths

- **Neuron activation state formulation yields large separability improvement.** The ablation (Fig. 4) shows that the proposed state (z ⊙ ∂D_KL/∂z) achieves 16.58% FPR95 on ImageNet layer4 versus 35.72% for raw neuron output alone — a 2.15× improvement. This directly supports the claim that the formulation eases InD/OOD separation.

- **NAC-UE establishes SOTA on average across three benchmarks, outperforming 21 prior methods.** On CIFAR-100 (Table 1), NAC-UE achieves 40.14 FPR95 (best) and 86.98 AUROC (best), beating the previous best method ViM (50.74 FPR95). On CIFAR-10, NAC-UE achieves 18.31 FPR95 and 94.60 AUROC, surpassing all 21 methods. On ImageNet (Table 2), NAC-UE achieves the highest average AUROC across three OOD datasets for both ResNet-50 (95.12) and Vit-b16.

- **NAC-UE is pluggable to existing training-time OOD detection methods.** Table 4 shows that combining NAC-UE with GODIN, ConfBranch, and RotPred training schemes substantially improves over each method's native detection baseline (e.g., GODIN: 50.87→26.86 FPR95), demonstrating general applicability without modifying training objectives.

- **Systematic hyperparameter analysis provides clear guidance.** Tables 7–9 examine α, r, and M with intuitive explanations for why extremes underperform (e.g., too-small r lets noise dominate; too-large M causes overfitting).

- **The paper identifies and validates a key limitation of rank correlation metrics.** Figure 5 shows on iWildCam (323 domains) that RC increases with the volume of OOD test data, confirming that low RC in some experiments is partly due to insufficient OOD data rather than a flaw in NAC-ME itself.

## Weaknesses

### Fatal
None.

### Major

- **The NAC formulation is heuristic and lacks theoretical grounding.** The neuron activation state (Eq. 3) combines neuron output and KL gradients via elementwise product — the paper justifies this choice post-hoc via ablation (it works better than either component alone) but provides no principled derivation. Similarly, the NAC function Φ(ẑ;r) = min(κ(ẑ), r)/r is a clipped density ratio; the paper states it is "inspired by system testing" but offers no argument for why this specific form (rather than, e.g., rank-based hardness, log-density, or quantile scores) is the correct way to measure coverage. The method works empirically, but the paper overclaims by saying it provides "insights into the fundamental cause" of OOD issues. Without a theoretical account of why these specific forms characterize OOD behavior, the contribution is weaker than the strong results suggest.

- **Computational cost of NAC-UE is not addressed, but is a practical limitation.** NAC-UE requires computing ∂D_KL/∂z for every test sample — a full backward pass through the network to the chosen layer(s). This is substantially more expensive than forward-pass-only methods (MSP, Energy, ODIN, ReAct, ASH, SHE, GEN) and costlier than methods requiring a single forward pass with trivial modifications (e.g., ViM). The paper never discusses runtime, FLOPs, or latency. For deployment in real-time or large-scale serving, this cost could be prohibitive. At minimum, wall-clock time comparisons on common hardware should be provided. The claim of "beating 21 methods" is incomplete without accounting for this trade-off.

- **OOD generalization gains (NAC-ME) are very small in absolute terms, and the evaluation is narrow.** Average ACC improvements over validation accuracy range from 0.17% (ResNet-50) to 1.07% (Vit-b16) in Table 3. On many individual dataset/backbone combinations, the gain is <0.5%. Rank correlation improvements are larger (up to 11.61%), but RC only indirectly measures the quality of the selected model. Moreover, NAC-ME is only compared against validation accuracy. Other natural criteria exist: validation loss, SWAD-style moving averages, gradient-norm-based early stopping, or ensemble diversity metrics. Comparing against at least one additional baseline would substantially strengthen the claim that NAC-ME adds value beyond the simplest alternative. The paper's own RC values are often modest (20–50%), meaning NAC-ME is a noisy predictor of OOD performance even when it beats the baseline.

### Minor

- **NAC-UE is not uniformly best across all individual settings; averaging obscures this.** In Table 2 (ImageNet), ASH outperforms NAC-UE on iNaturalist with ResNet-50 (97.07% vs. 96.52%), on OpenImage-O with ResNet-50 (93.26% vs. 91.45%), and MDS/RMDS outperform NAC-UE on iNaturalist with Vit-b16 (96.01%/96.10% vs. 93.72%). The paper's claim that NAC-UE "consistently outperforms all of the SoTA methods on average performance" is technically correct but could mislead. A discussion of when and why NAC-UE underperforms relative to specific methods (e.g., ASH on ResNet-50, MDS on ViT) would give a more honest characterization.

- **No discussion of failure cases or limitations.** The paper has no limitations section. For example, on CIFAR-100 with Places365 as OOD, NAC-UE gets 73.57% FPR95 — substantially worse than RMDS (53.57%) and ReAct (55.30%). This is not discussed. Understanding why NAC-UE fails on certain OOD data would strengthen the paper's scientific depth. The paper should also explicitly note that NAC-UE requires gradient computation, per-neuron histograms (scaling with N×M), and tuning of α, r, and M.

- **Hyperparameter analysis is limited in scope.** The sensitivity analyses for α, r, and M (Tables 7–9) are conducted only on CIFAR-10 with a single layer (layer4). It is unclear whether optimal values transfer to other datasets or to the multi-layer setting, meaning the method may require per-dataset tuning that limits plug-and-play usability.

- **The marginal gain from using all layers vs. a single late layer is modest.** Table 5 shows that layer4 alone achieves 23.50% FPR95 on CIFAR-10 vs. 18.31% for all four layers — a 5.19% improvement at substantially higher memory and compute. The paper acknowledges this in passing but does not discuss the cost-benefit trade-off explicitly.

### Trivial

- The table numbering in the text is occasionally inconsistent (Tables 7–9 in the text do not match the actual table captions in the body of the paper — the parameter tables are not individually numbered with explicit captions matching the text references).

## Nice-to-Haves

- For NAC-UE applied to models trained with OOD-aware methods (Table 4), a comparison against other post-hoc SOTA methods (ViM, KNN, Energy, ASH) applied to the same trained models would be more informative than the current comparison against only each method's native detection baseline.
- For NAC-ME, the paper could explore using NAC as a training regularizer (maximizing coverage during training) rather than only as a post-hoc evaluation criterion, which would strengthen the causal claim.
- Providing per-dataset optimal hyperparameter values (or showing that a single configuration works across datasets) would improve practical utility.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The ablation in Figure 4 shows the product works better but that is an experimental observation, not an explanation"** — Retained as part of Major weakness 1 (heuristic formulation) rather than as a standalone criticism. The empirical nature of the ablation is standard for ML papers; the core issue is the absence of theoretical derivation, not the use of ablation per se.
- **"NAC-ME should be compared to 'virtually any reasonable metric' which will correlate positively"** — The claim that "virtually any reasonable metric will correlate positively" is an unsubstantiated assertion by the reviewer. The paper shows that validation accuracy, a very reasonable metric, often has lower correlation than NAC-ME. This framing was removed and replaced with the more precise criticism about narrow comparison baselines.
- **Suggestions about using NAC-ME as a training regularizer or for early stopping across multiple runs** — These are forward-looking suggestions, not weaknesses. Moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel synthesis that the paper itself does not already articulate.

## Suggestions

1. **Add a limitations section** explicitly discussing the computational cost (backward pass per sample), the heuristic nature of the formulation, the datasets/settings where NAC-UE underperforms, and the modest effect size of NAC-ME.
2. **Provide wall-clock timing comparisons** (seconds per 1K test samples) on a common GPU for NAC-UE vs. the most competitive methods (ViM, KNN, ASH, Energy) so readers can assess the cost-benefit trade-off.
3. **Compare NAC-ME to at least one additional model selection criterion** such as validation loss or SWAD-style moving averages, to strengthen the claim that it adds value beyond the simplest baseline.
4. **Discuss individual cases where NAC-UE loses to specific methods** (e.g., ASH on ResNet-50, MDS/RMDS on ViT) and offer a hypothesis for why — this would improve scientific depth and help users choose the right method for their setting.
5. **Extend the hyperparameter analysis** to at least one additional dataset and the multi-layer setting to demonstrate transferability of optimal values, or acknowledge that per-dataset tuning is expected.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>