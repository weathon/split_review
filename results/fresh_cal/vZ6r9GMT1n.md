Now I have all the information I need. Let me produce the final consolidated review after carefully cross-checking every claim.

---

## Summary

This paper proposes adding Gaussian noise to intermediate hidden features at inference time as a defense against query-based black-box attacks. The core intuition — supported by a heuristic theoretical analysis — is that feature-space noise disrupts gradient estimation more than input-space noise for the same clean-accuracy drop, because the gradient norm at deeper layers is often larger. The paper evaluates the method extensively across 6 models (CNNs and transformers), 5 attacks (score-based NES/Square/SignHunt and decision-based RayS/SignFlip), 2 datasets (ImageNet, CIFAR10), and includes adaptive EOT attacks. The defense consistently improves robustness in the majority of settings and combines well with adversarial training.

## Strengths

1. **Consistent empirical advantage across most settings, with notable exceptions.** On VGG19 (ImageNet and CIFAR10), feature defense substantially outperforms input defense across all attacks (e.g., Square at 10k queries on ImageNet: 22.2% vs 17.8%; SignHunt: 32.8% vs 27.1%). On ViT and ResNet50, feature defense wins on Square and SignHunt but is competitive or slightly behind on NES. The method is not universally dominant, but it wins in enough settings to be practically useful.

2. **Strong orthogonal benefit with adversarial training.** Combining feature defense with AT on CIFAR10/ResNet20 improves Square accuracy from 32.5% (AT alone) to 77.8% (Ours+AT). This is a striking result demonstrating that the defense complements existing approaches.

3. **Robustness to adaptive EOT attacks.** When the attacker averages M queries to cancel noise, feature defense still outperforms input defense in most model–attack combinations (e.g., VGG19 Square at M=5, 1000 queries: 53.0% vs 24.2%), showing the defense is not trivially bypassed.

4. **Extensive evaluation scope.** Experiments span 6 model architectures (VGG19, ResNet50, ViT, DeiT), 5 attacks (both score-based and decision-based), 2 datasets, multiple query budgets (1000–10000), controlled clean-accuracy drops, and dynamic attack-strength analysis. This scope exceeds what is typical for a defense paper in this area.

5. **Theoretical intuition connecting gradient norms to defense effectiveness.** Theorem 1 identifies the ratio (ν/μ)·(‖∇_h ℒ‖²/‖∇_x ℒ‖²) as the key quantity driving robustness, and the layer-wise experiments (Table 5) broadly validate that deeper layers with larger gradient norms yield higher robustness. While the analysis is heuristic, it provides useful design guidance.

## Weaknesses

### Major

1. **Missing specification of which layers are perturbed in the main experiments.** Algorithm 1 takes a set of layers H as input, but the main experimental tables (Table 1 on ImageNet, Table 2 on CIFAR10) never state which layer(s) were selected for any model. The layer-wise analysis (Table 5) separately shows that robustness varies dramatically by layer (e.g., VGG layer 4: 52.5% vs layer 12: 63.0% under Square). Without knowing H, no practitioner can reproduce the results or apply the method. This is the single most actionable gap — it must be resolved for the paper to function as a reproducible contribution.

2. **Noise variance calibration procedure is incompletely described.** The paper states (Section 3.5) that "the standard deviation that makes accuracy drop by 1% is proportional to the value at which 1% of the ratios in the dataset are smaller," and the evaluation protocol says ν is tuned to achieve a target clean-accuracy drop. But the actual calibration algorithm (grid search? analytical formula? per-model or per-layer?) is not specified. Combined with the missing layer selection, the method cannot be faithfully re-implemented from the current description.

### Minor

3. **Claims of "consistency" are somewhat overstated.** The paper states that "randomized feature defense consistently achieves better robustness" (line 214, for Square and SignHunt specifically) and "significantly better robustness" more broadly. In reality:
   - On decision-based SignFlip (Table 3), input defense outperforms feature defense (ResNet50: 85.5 vs 82.5; VGG19: 86.0 vs 76.5). The paper mentions this only in passing and does not analyze why.
   - On NES, results are mixed: on ImageNet ResNet50 at 10000 queries, input defense (41.5) beats feature defense (40.6); on DeiT, input defense wins on NES across all settings.
   - The paper selects favorable headlines and does not discuss failure modes. A more measured presentation (e.g., "feature defense often improves upon input defense, with the advantage being most pronounced on VGG and under Square/SignHunt attacks") would be more accurate.

4. **Gradient norm vs. robustness claim is not strictly monotonic.** The paper states "as the gradient norm increases, the robustness also increases" (line 386). Looking at the data in Table 5: VGG layer 15 (GradNorm 1.710) has lower GradNorm than layer 12 (2.514) but higher SignHunt robustness (37.4 vs 29.4); layer 15 also has higher GradNorm than layer 1 (1.710 vs 1.324) but lower Square robustness (50.6 vs 56.7). The relationship is a rough trend, not a strict monotonic one. The claim should be softened.

5. **Theoretical analysis is heuristic rather than rigorous.** Theorem 1 states that the "probability of opposite action positively correlates with arctan(...)" — a qualitative, uncalibrated statement rather than a formal bound or precise testable condition. The derivation is sketched but does not compute the actual distribution of the finite-difference estimate under feature noise. The paper presents this as "theoretical analysis" confirming the method, but the analysis is better described as intuition-motivating. This is not a fatal flaw (the empirical evidence is the main contribution), but the framing should be honest.

6. **No error bars or multiple-run statistics.** With 1000 test images (100 per class on CIFAR10), small differences (1–2 percentage points) could be noise. The paper reports single-run results throughout without variance estimates or confidence intervals.

### Trivial

7. **Definition 1 (attack success for randomized model)** uses the expectation of the model output, but evaluation queries single realizations. This mismatch is not discussed.
8. **Computational overhead** is described as "lightweight" but no runtime measurement is reported.

## Nice-to-Haves

- A rule of thumb for layer selection (e.g., "perturb the layer before the classifier" or "the deepest convolutional layer") would substantially increase practical value.
- A discussion of why SignFlip reverses the advantage (decision-based attacks relying on binary search may be less sensitive to output noise than score-based attacks).
- Reporting results over multiple random seeds or providing bootstrap confidence intervals for the main tables.

## Removed Points

- **Missing comparison with feature-level defenses (Xie et al. 2019, Liu et al. 2019, etc.):** Removed per the instruction that missing related works should not be mentioned since external sources cannot be verified.
- **Missing discussion of SurFree, GeoDA attacks:** Removed — the paper covers the main attack families; demanding coverage of every recent attack is scope creep.
- **Certification not provided:** Removed — the paper never claims certified robustness; demanding it is outside scope.
- **Assumption about mean of randomized model is unjustified:** Removed — the paper explicitly states this as an assumption (Assumption 1) and notes it holds when noise variance is small. This is standard practice.
- **Models finetuned from ImageNet is "unusual":** Removed — the paper clearly states this design choice; there is nothing wrong with it.
- **Theoretical analysis "does not add much beyond what an informed practitioner would guess":** Demoted — this is a qualitative opinion that discounts the analysis's genuine insight linking gradient norm ratios to defense effectiveness. The analysis is indeed heuristic, but that is captured in Weakness #5 with more precision.
- **Strengths about "important problem" and "interesting question":** Removed as generic.
- **Various formatting/style nitpicks and "parser error" artifacts:** Removed.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the paper's stated findings (feature noise helps, the gradient-norm ratio is a key factor, the method complements AT) and its limitations (missing implementation details, heuristic theory, overclaiming of consistency). An interesting subtlety that emerges from cross-referencing the strengths and weaknesses: the method's advantage is clearest on VGG19 (a deep CNN) and weaker on ResNet50 and DeiT — this pattern is not explained by the paper and could point to architectural factors (e.g., residual connections or attention mechanisms) that make the defense less effective.

## Suggestions

1. **Specify the layer set H** used in every main-table experiment, and describe the layer selection procedure (e.g., grid search on a validation set, or a fixed heuristic like "last convolutional block"). Include a sensitivity analysis showing how results change with different layer choices.
2. **Describe the ν calibration procedure** completely: is it grid search? Binary search on a validation set? How many ν values were tested? Is it done once per model or per model–attack combination?
3. **Tone down consistency claims** to match the evidence. Explicitly discuss the SignFlip failure and the mixed NES results, and offer a hypothesis for why input defense wins in those settings.
4. **Replace "as the gradient norm increases, robustness also increases" (line 386) with** "robustness broadly correlates with gradient norm, though the relationship is not strictly monotonic" — this is honest about the data in Table 5.
5. **Recalibrate the framing of the theoretical analysis** from "confirms effectiveness" to "provides intuition for why feature noise may outperform input noise, supported by empirical verification of the predicted trend."

## Score and Decision

**Score: 6.0** — The paper makes a genuine contribution with a well-studied method, extensive experiments, and useful practical insights. The two major weaknesses (missing layer selection and incomplete ν calibration) are addressable in revision and do not undermine the core finding that feature-space noise often beats input-space noise. The overclaiming and heuristic theory are issues but do not change the fact that the empirical evidence broadly supports the method's effectiveness.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>