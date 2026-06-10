Here is my final consolidated review.

---

## Summary

This paper proposes Geometric Median (GM) Matching, a herding-style greedy algorithm for robust data pruning. The core idea is to select a k-subset whose empirical mean approximates the geometric median (rather than the empirical mean) of the potentially corrupted dataset, leveraging the GM's known robustness properties. The paper provides a breakdown-point analysis showing existing centroid-based pruning methods fail under arbitrary corruption, a convergence theorem, and experiments across CIFAR-10/100 and Tiny ImageNet with various corruption types.

## Strengths

- **Clean breakdown-point analysis (Lemma 1):** Formally shows that existing score-based and moment-matching pruning methods have asymptotic breakdown point 0 under the gross corruption model, while GM-based selection can achieve the optimal breakdown point of 1/2. This is self-contained, well-argued, and does not depend on the disputed convergence rate claim. It is a solid theoretical contribution.

- **Comprehensive empirical scope:** Experiments span 3 datasets (CIFAR-10, CIFAR-100, Tiny ImageNet), 5 architectures (ResNet-18/50, VGG-16, ShuffleNet, SENet, EfficientNet-B0), and 3 corruption types (image corruption, label noise, adversarial attacks), plus network/domain transfer ablations. This breadth is a genuine strength.

- **Strong clean-setting performance:** GM Matching outperforms prior methods by >2% on average even without corruption (lines 303–304), demonstrating that the robustness mechanism does not trade off standard performance — an important practical finding.

- **Network/domain transfer experiments (Section 5.4):** Shows that subsets selected by one proxy generalize to unseen architectures and under distribution shift — a practical concern many pruning papers do not evaluate.

## Weaknesses

### Major

1. **Theorem 1's stated bound does not support the claimed O(1/k) rate.** The theorem (lines 257–262) claims convergence "at the rate O(1/k)" but the explicit bound in Equation (259–261) contains no dependence on *k* — it depends only on |D_G|, |D_B|, the variance of clean samples, and the GM approximation error ε. A rate O(1/k) cannot be read from a bound that does not involve *k*. This is a structural problem: the paper's headline theoretical contribution (abstract line 4, introduction line 45, theorem statement) is unsupported by the theorem as presented. Since the convergence rate is advertised as a key differentiator from uniform sampling, this gap is serious.

2. **Baseline results are borrowed rather than reproduced.** Line 283 states: "We do not run these baselines... these baselines are borrowed from [xia2020robust]." Eight of the nine baselines in the main comparison are taken from prior published tables, while the paper's own GM Matching results come from the authors' own runs. Even if the "experimental setup is identical," uncontrolled variation (random seeds, data splits, training stochasticity, augmentation pipelines) can produce non-trivial differences. The reported ~12% label-noise improvement — an order of magnitude larger than gains in other settings (~2–3%) — is particularly vulnerable to this concern. The comparison would be substantially stronger if the leading baselines (Moderate, Herding, at minimum) were re-implemented in the same codebase.

### Minor

3. **Self-supervised learning claim contradicts actual experiments.** Lines 105–107 state: "our setting is to instead explore core-set selection strategies to improve the efficiency of self supervised learning." But all experiments in the paper are supervised image classification. No self-supervised learning experiments, contrastive learning results, or representation quality metrics are reported. This appears to be a drafting fragment from a different version and creates a coherence issue.

4. **"Promotes diversity" claim (line 249) is asserted without measurement.** The paper states GM Matching "promotes diversity" by exploring underrepresented regions, but it never measures the diversity of selected subsets (e.g., feature-space coverage, sample-type distribution). This claim should be supported or qualified.

5. **Corruption rates (ψ) are not stated for any experiment.** The α-corruption model defines ψ ∈ [0, 1/2), but the experimental sections (5.3) do not specify what ψ values were used for image corruption, label noise, or adversarial attacks. The reader cannot assess how gains scale with corruption severity or connect experiments to the theoretical guarantee.

### Trivial

6. The citation "[xia2020robust]" on line 283 may be a referencing error — the paper primarily builds on [xia2022moderate] throughout, and the intended reference for the borrowed baselines is unclear.

## Nice-to-Haves

- Report wall-clock time or FLOPs of GM Matching (Weiszfeld iteration + greedy selection) vs. simpler baselines, since computational overhead is relevant for a pruning method.
- Ablate the effect of GM approximation accuracy ε (number of Weiszfeld iterations) on downstream performance.
- Provide confidence intervals for borrowed baselines if available from the original papers, or note their absence.

## Removed Points

These points were flagged by the reviewers but removed after verification:

- **Harsh critic's claim about "O(1/k) vs O(1/√k) comparison asserted without proof":** Merged into Weakness 1 — it is the same underlying issue (the theorem's bound does not contain k).
- **Harsh critic's computational cost concern (Weiszfeld iteration, greedy selection complexity):** Moved to Nice-to-Haves. These are practical considerations the paper does not claim to address as a core contribution.
- **Harsh critic's criticism about missing appendix / proof:** Removed per instructions (parser-stripped content).
- **Strength Finder's claimed strength about O(1/k) convergence rate:** Removed because it conflicts with verified Weakness 1 (the bound does not support the claimed rate).
- **All formatting, typo, and parser-artifact criticisms:** Removed per instructions.

## Novel Insights

The reviews surface a structural disconnect between the paper's advertised theoretical contribution and what the theorem statement actually delivers — the O(1/k) rate is claimed but the bound lacks any dependence on k. This is a specific, verifiable problem that goes beyond generic "theoretical contribution is weak" complaints. The baseline-borrowing issue is also unusually consequential here because the largest claimed gain (12% under label noise) is an outlier relative to the paper's other results, making controlled comparison especially important.

## Suggestions

1. **Fix Theorem 1.** Either present a bound that genuinely depends on k and yields O(1/k), or remove the O(1/k) claim and present the theorem as a bound on the asymptotic neighborhood radius that is independent of k (which is still a valid result, just not a rate).
2. **Re-implement the strongest baselines** (Moderate, Herding) in the same codebase under identical settings, or clearly flag all quoted numbers and discuss the limitations of cross-paper comparison.
3. **State ψ explicitly** for each experiment so the reader can connect empirical results to the theoretical framework.
4. **Remove or correct** the self-supervised learning paragraph (lines 105–107) and the unmeasured "promotes diversity" claim.
5. **Clarify the convergence claim:** even without the O(1/k) rate, the breakdown-point analysis and the bound on the neighborhood radius are contributions worth presenting accurately.

## Score and Decision

This paper has a well-motivated core idea and an admirably broad empirical evaluation. The breakdown-point analysis of existing methods is clean and independently useful. However, two major issues prevent acceptance at a top venue: (a) the headline O(1/k) convergence rate is claimed but the theorem's stated bound does not contain k, making the central theoretical result unsupported as presented; and (b) the empirical comparison relies on borrowed baseline numbers, which undermines the reliability of the reported margins — especially the outlier ~12% label-noise gain. These are fixable in revision, but in their current form they leave the paper's main claims insufficiently established.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>