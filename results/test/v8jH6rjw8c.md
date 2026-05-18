Now I have all the information needed to synthesize the final review. Let me produce it.

## Summary

This paper studies the coupling of long-tailed distributions and label noise, empirically demonstrating that existing robust/long-tailed methods have disparate impacts on different sub-populations (helping some while hurting others). It proposes a Fairness Regularizer (FR) that penalizes absolute differences in average prediction confidence between sub-populations, and shows that adding this regularizer improves overall accuracy across six baseline methods on both synthetic and real-world noisy long-tailed datasets.

## Strengths

1. **Identifies and empirically documents a previously understudied problem**: The paper provides clear evidence (Figure 2) that existing methods for noisy labels or long-tailed distributions treat sub-populations heterogeneously — some improve at the expense of others. This coupling effect between label noise and population imbalance is a genuine problem worth addressing.

2. **Simple, broadly applicable regularizer with mostly positive results**: FR is a lightweight additive term that can be plugged into any loss function. Table 1 shows that FR (especially the two-group variant G2) improves test accuracy in the large majority of settings across 6 baselines, 2 noise types, 3 imbalance ratios, and 2 datasets. On CIFAR-10 with imbalance noise, FR(G2) improves CE from 60.03→65.12 at r=100 and from 37.44→39.69 at r=50 ρ=0.5.

3. **Demonstrates that fairness constraints can improve overall accuracy, counter to typical fairness-accuracy trade-offs**: The paper shows that reducing performance gaps between sub-populations does not necessarily hurt average performance — it often helps, which is a non-trivial finding.

4. **Validated on real-world noisy long-tailed datasets**: Beyond synthetic noise, results on CIFAR-10N, CIFAR-100N, CIFAR-20N, and Animal-10N (Table 3) confirm that FR improves CE and Logit-adj across multiple imbalance ratios, with gains sometimes exceeding 2 percentage points.

## Weaknesses

### Major

1. **Unsubstantiated theoretical claim about Bayes optimality**: The Observation box in Section 4 states: "When solving the risk minimization on the noisily labeled long-tailed data under the introduced fairness constraints returns the Bayes optimal classifier." The paper mentions a "binary Gaussian example" but provides no proof, derivation, formal statement, or even a sketch. This is presented as a theoretical result but is entirely unsupported. If the authors have a formal result, it must be stated and justified; otherwise this claim is misleading and should be removed.

2. **The regularizer's formulation lacks a clear mechanism connecting it to clean-label accuracy**: The FR (Eq. 9) penalizes differences in the model's *prediction probability on the observed noisy label* across sub-populations. The paper does not provide a convincing argument for why minimizing gaps in noisy-label confidence translates to better clean-label accuracy for tail groups. High confidence on a noisy label often indicates memorization — minimizing gaps in this quantity could in principle make the model equally wrong rather than equally accurate. The paper relies entirely on experiments to make this case, but the conceptual gap weakens the contribution's foundation.

### Minor

1. **Inconsistent improvements and scope of results**: While FR(G2) helps in most settings, some configurations show non-improvements (e.g., CE+FR(KNN) on CIFAR-100 Imb r=50 ρ=0.2: 31.44→31.03; Logit-adj+FR(G2) on CIFAR-10 Sym r=100 ρ=0.5: 27.32→21.93). The paired t-test aggregates across only 12 samples per dataset, and several p-values are borderline (e.g., LS+FR(G2): p=0.091, 0.080; PL+FR(G2): p=0.092). Per-configuration analysis and effect sizes would be more informative than an aggregated test.

2. **Mismatch between stated assumption and actual usage**: Section 2.2 states "we do not assume the knowledge of the sub-population information during training," yet FR requires computing indicator functions I(g_k=i) for each training sample. While the paper clearly describes how these assignments are obtained (KNN clustering or a pre-trained model), the phrasing is slightly misleading — sub-population information is inferred and used at training time, which is a different claim.

3. **No direct visualization of gap reduction**: Figure 3 shows per-class accuracy changes but does not directly display the gap between head and tail accuracy before vs. after FR. The paper's central claim is that performance gaps are reduced, but this is not explicitly quantified.

### Trivial

- The claim "We have also adopted a binary Gaussian example and theoretically show" (line 192) is a dangling reference — no such example or analysis appears in the paper.

## Nice-to-Haves

- Direct head-vs-tail accuracy gap plots before and after applying FR, to explicitly quantify gap reduction.
- Ablation on the choice of λ for the main CIFAR experiments (not just Clothing1M), since the regularizer's effect size is modest and likely depends on this hyperparameter.
- Analysis of sensitivity to the quality/accuracy of sub-population assignments, particularly for the KNN variant where poor clustering harms results on CIFAR-100.

## Removed Points

- **Logit-adj + FR(G2) decrease on CIFAR-10 (critic's claim)**: The critic states Logit-adj + FR(G2) on CIFAR-10 r=50 ρ=0.5 gives 51.51→49.23. This is factually wrong — the table shows 51.51→55.09 for FR(G2) (an improvement). The 49.23 is for FR(KNN), a different variant. Removed due to factual error.
- **"Influence analysis not tightly connected"**: The influence analysis in Section 3 is a motivating empirical study, not a derivation of FR. The paper frames it as motivation for why sub-population-aware treatment matters, which is a reasonable and standard use of such analysis. Not a weakness.
- **Missing recent baselines**: The critic's suggestion of additional baselines is a taste-based request. The six baselines (CE, LS, NLS, Focal, PL, Logit-adj) are standard and representative. Adding more would not change the evaluation's validity. Moved here as scope-creep.
- **Cherry-picking "best" λ metric on Clothing1M**: The paper reports results across 8 λ values for each method, and the claim is that non-zero λ typically outperforms λ=0. Reporting the best λ per method is standard and the full sweep is transparently shown. Not cherry-picking.
- **Formatting/style nitpicks**: Removed per hard rules.

## Novel Insights

The most valuable insight from the reviews is that the paper would be significantly strengthened by directly answering the question "why should minimizing gaps in noisy-label prediction confidence improve clean-label accuracy?" — either through a simple generative model where this holds provably, or through empirical analysis showing that FR actually reduces the gap in *clean-label* accuracy (not just noisy-label confidence). The current paper provides the empirical pattern but stops short of closing this loop.

## Suggestions

1. Either provide a proof/sketch of the Bayes optimality claim, or remove it entirely. Presenting an unsupported theoretical result weakens rather than strengthens the paper.
2. Add a direct comparison of head vs. tail accuracy with and without FR, to explicitly demonstrate gap reduction rather than just overall accuracy improvements.
3. Discuss the scope conditions under which FR may not help (e.g., CIFAR-100 with many sub-populations where KNN clustering yields tiny groups), and use these to guide practitioners on when to apply the method.
4. Replace or supplement the aggregated t-test with per-configuration comparisons showing the proportion of settings where FR helps and the average effect size.

## Score and Decision

The paper identifies a genuinely important problem and provides a simple, broadly applicable solution with mostly positive experimental evidence. However, two major weaknesses — an unsupported theoretical claim and an insufficiently justified mechanism — prevent the contribution from being fully convincing. The empirical results are promising but not airtight. With revisions to address the theoretical claim and a clearer articulation of the method's mechanism and scope conditions, the paper could be strong. In its current form, it is a borderline contribution.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>