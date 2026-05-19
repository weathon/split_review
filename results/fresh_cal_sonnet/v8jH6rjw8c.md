Now let me run the calibration search to anchor the score.Now I have enough to write the final review. Let me compile all findings.Now I have all the information I need to write the final review.

---

## Summary

This paper studies the underexplored joint problem of learning from noisily labeled, long-tailed data. The authors first present empirical evidence (Figure 2) that existing robust methods for either noise or imbalance individually produce disparate, often contradictory effects across sub-populations when both problems co-occur. Motivated by this observation, they propose a **Fairness Regularizer (FR)**: a Lagrangian penalty that equalizes prediction confidence gaps between sub-populations (FR(KNN): k-means clustering into K groups; FR(G2): pre-trained model split into 2 groups). Experiments on synthetic CIFAR-10/100 with varied noise/imbalance conditions, real-world CIFAR-10N/100N/20N, Animal-10N, and Clothing1M datasets show that FR consistently improves tail class accuracy and overall test accuracy across six base methods.

---

## Strengths

- **Novel disparate-impact analysis**: Figure 2 is the paper's most concrete empirical contribution. It directly demonstrates that standard robust methods (LS, PeerLoss, Focal, Logit-adj) produce heterogeneous and sometimes harmful effects on sub-populations under simultaneous noise and imbalance — e.g., LS causes near-zero accuracy on low-accuracy sub-populations while improving others. This observation is not established in prior work treating either problem in isolation.

- **Sub-population influence metrics**: Section 3 introduces two complementary metrics (population-level test accuracy change and sample-level confidence change when removing a sub-population), with box plots and distribution plots that quantify the elevated variability of tail sub-populations specifically in the noisy setting (Observations 1 and 2). This diagnostic contribution is useful beyond the proposed regularizer.

- **Plug-and-play applicability with broad coverage**: FR is validated as a drop-in regularizer across six distinct base methods (CE, LS, NLS, Focal, PeerLoss, Logit-adj), under two synthetic noise models (Imb and Sym), two noise rates, three imbalance ratios, and multiple real-world datasets. FR(G2) wins in 47/72 settings in Table 1, with gains occasionally exceeding 3 percentage points (e.g., CE+FR(G2) on CIFAR-100 Sym, ρ=0.5, r=100: 19.10 vs. 4.76 baseline — a dramatic rescue of a collapsed baseline).

- **Real-world dataset confirmation**: Table 3 confirms beneficial trends on CIFAR-10N, CIFAR-100N, CIFAR-20N, Animal-10N, and Clothing1M. On real-world noisy+long-tailed settings such as CIFAR-10N Worse (r=10), CE+FR(G2) improves from 71.83 to 74.67 (+2.84%), a non-trivial and consistent gain on genuinely heterogeneous human-annotated noise.

---

## Weaknesses

### Fatal

None identified. The paper's empirical results are real and reproducible across enough settings to demonstrate a genuine contribution.

### Major

- **Missing comparison to dedicated noise+imbalance methods**: The related work section explicitly cites methods designed specifically for the joint noise+imbalance problem (e.g., \cite{wei2021robust, karthik2021learning, zhong2019unequal}), which use decoupled treatments for head and tail classes in the presence of label noise. None of these appear as baselines in any table. The paper frames FR as a plug-in supplement to generic single-problem methods, but it never tests whether FR provides value *beyond* what architecturally integrated joint solutions already achieve. This is the most important evidential gap: the contribution's value above the prior-art frontier for the same joint problem cannot be assessed.

- **Semantic gap in the FR objective**: The core regularizer in Eq. (3.7) penalizes the gap in model confidence on the *noisy label* Ỹ: dist_i := |P(f(X)=Ỹ|G=i) − P(f(X)=Ỹ)|. However, the stated task (Section 2, task formulation) is to minimize expected loss under the *clean and balanced distribution* D. These are not the same quantity. Under the Imb noise model (Model 1), tail sub-populations are systematically more likely to be mislabeled as frequent head classes, so a tail group may have low P(f(X)=Ỹ|G=i) even when it is classified correctly on clean labels. FR would then push the model to equalize a quantity that may not correspond to the clean-label objective. The paper presents a binary Gaussian "observation" (in a box) claiming the fairness-constrained solution recovers the Bayes optimal classifier, but this is limited to a toy setting and does not cover the imbalanced noise regime most central to the paper's setup. The main text provides no argument bridging this gap.

### Minor

- **Paired t-test misapplication**: Table 2 applies a paired t-test to 12 data points per (method, dataset) combination, formed by crossing 2 noise types × 2 noise rates × 3 imbalance ratios. These 12 conditions are deliberately heterogeneous and are not exchangeable i.i.d. draws from a common distribution (ρ=0.2, r=10 and ρ=0.5, r=100 measure qualitatively different operating regimes). The resulting p-values (e.g., CE+FR(G2) on CIFAR-10: p=0.001) do not carry the standard frequentist interpretation invoked by the paper. The test shows FR tends to win across these diverse conditions but cannot properly support a claim of "significant improvement" within any specific condition. Notably, Logit-adj+FR(G2) on CIFAR-10 gives t=0.255, p=0.803 — not significant even under this pooled setup — and the paper is not transparent about which specific configurations it fails in.

- **FR(G2) reduces to a binary head/tail split without explicit comparison to conceptually related approaches**: The paper notes in Section 5.1 that FR(G2) "separates features into a head and a tail sub-population" (ratio ≈ 5:1) via an ImageNet pre-trained model. This means the working variant of FR is operationally a binary head/tail gap regularizer — conceptually close to the head/tail decoupling methods cited but not compared against. The fairness framing implies a general multi-group solution, but the effective working method is a specific two-group design. This matters because it narrows the contribution without the paper acknowledging the connection.

- **Inconsistent improvements in specific settings**: In Tables 1 and 3, several cells show FR hurting performance (non-highlighted), including: CE+FR(KNN) on CIFAR-10, ρ=0.5, r=50 (47.51→46.69); Logit-adj+FR(G2) on CIFAR-10N Agg at r=100 (71.35→70.39); Logit-adj+FR(G2) on CIFAR-10N Rand1 at r=50 (66.15→65.94); and Logit-adj+FR(G2) at r=100 on CIFAR-10N across multiple columns. The paper's win-counting convention and t-test framing obscure these cases without explanation. Particularly, Logit-adj+FR(G2) on CIFAR-100 at ρ=0.2 gives 41.21 vs. 47.28 (−6 points), a substantial degradation not discussed.

### Trivial

- **Influence analysis limited to 3 sub-populations**: Section 3 presents results for sub-populations i=52, 70, 91 on CIFAR-10. These are described as "randomly selected" but only three of the 17 tail sub-populations are shown. Aggregating or showing a broader sample would strengthen the evidential basis of Observations 1 and 2.

- **λ values not stated for Table 1**: The paper reports λ values for Table 3 (λ=2 for CE+FR, λ=1 for Logit-adj+FR), but does not specify what λ values were used for the CIFAR Table 1 experiments.

---

## Nice-to-Haves

- **Mechanistic explanation for the fairness-accuracy improvement**: The paper's most surprising claim is that adding a fairness penalty improves overall clean-label accuracy without tradeoff. Even an informal argument — e.g., that FR(G2) acts as an adaptive reweighting that prevents tail class collapse under noisy labels — would significantly strengthen the intellectual coherence of the contribution, beyond pointing to a binary Gaussian example.

- **Variance estimates across seeds**: Many improvements in Clothing1M (Table 4) are sub-0.5% (e.g., NLS: 74.46→74.50). Without standard deviations across training runs, it is not possible to assess whether these small gains are reliable or within training variance. This is especially important because "best-achieved" accuracy is reported rather than last-epoch or averaged.

- **Computational overhead of FR**: FR requires per-batch sub-population statistics and a pretrained feature extractor for G2 group assignment. A brief runtime or overhead analysis would aid practitioners evaluating whether FR is worth adopting.

---

## Removed Points

*These points were evaluated against the paper text and removed for the reasons listed. Treat with caution.*

- **Critic: "FR(KNN) failure on CIFAR-100 is evidence of structural fragility."** REMOVED (unfair to overstate — the paper itself explains this (Section 5.1: batch-level sparsity with K=100 groups) and proposes G2 as the working alternative. The authors acknowledge and address this).

- **Critic: "Counting convention overstates FR's wins."** PARTIALLY RETAINED as a Minor weakness. The Logit-adj+FR(G2) degradation on CIFAR-100 Imb ρ=0.2 (41.21 vs 47.28) is specifically worth flagging.

- **Strength Finder: "Statistical significance via paired t-test provides rigorous evidence."** REMOVED (the test is methodologically misapplied, as detailed in Minor weaknesses above; cannot be claimed as a strength).

- **Strength Finder: "Addresses the underexplored coupling of label noise and long-tail."** REMOVED as a standalone strength (generic problem importance framing without concrete evidence beyond the paper's own observations — the observation is already noted in the Strengths under disparate-impact analysis).

- **Critic: "Missing related works that should be compared."** REMOVED per hard rules (cannot confirm existence of specific works beyond what the paper already cites, and the paper does cite them in related works; the substance is kept as the "missing baselines" Major weakness).

---

## Novel Insights

The most genuinely novel observation in this paper — underappreciated even by both reviewers — is the directional asymmetry shown in Figure 2: different robust methods applied to the joint noise+imbalance problem tend to *hurt* disjoint sets of sub-populations. LS collapses accuracy on low-CE-accuracy sub-populations while helping high-accuracy ones; PeerLoss does the reverse. This systematic inversion is not a quantitative claim but a qualitative structural finding about the interaction between the two problems, and it gives FR's design a cleaner motivation than a generic "fairness improves performance" narrative. If the paper developed this observation further (e.g., showing that FR stabilizes the direction of improvement across both regimes), it would be a more compelling argument for why fairness regularization is specifically the right tool here.

---

## Suggestions

1. **Add dedicated noise+imbalance baselines**: Include \cite{wei2021robust} and \cite{karthik2021learning} in at least one main table. Even showing that FR further improves these stronger baselines would be valuable, and it would make the contribution's position in the landscape unambiguous.

2. **Replace or supplement the paired t-test**: Report per-configuration averages and standard deviations across training seeds. The current t-test across heterogeneous conditions conflates reliability with consistency — replacing it with per-configuration variance would make significance claims defensible.

3. **Investigate the noisy-label objective mismatch**: Test whether using model confidence on the *predicted* label (rather than the noisy label) as the FR signal changes results. This would address the semantic gap and could reveal when FR(G2) and FR(predicted) agree, giving insight into the mechanism.

4. **Discuss Logit-adj+FR(G2) degradation on CIFAR-100 Imb ρ=0.2**: The 6-point drop (47.28→41.21) in one combination is notable and unexplained. Understanding when FR hurts is at least as important as showing when it helps.

---

## Score and Decision

**Round 1 Bracket:** Based on topically similar anchors retrieved at different score bands:
- Score ≤3 anchors: Rejected papers with weaker methodology and narrower scope (RwiUmrEHgR, 6PGT9OJX5N).
- Score 4–7 anchors: 3GurO0kRue (6.50, Accept — subpopulation harmonizing with stronger theory), TjhUtloBZU (6.25, Accept — noisy label pre-training analysis), SwRlpDKrY9 (5.20, Reject — long-tail debias method), u1yvEwYfK9 (5.67, Reject — label shift correction for long-tail).
- Score ≥8 anchors: Papers on mostly different topics (learning-to-defer, partial-label learning).

**Initial bracket: 4.5–6.0.**

**Round 2 Narrowing:**
- x3lE88YkUl (5.20, Reject — SAM reweighting for noisy labels): A narrower plug-in modification for noisy labels only, with solid but limited experiments. The paper under review is broader (joint problem, more datasets) but has the missing-baselines gap.
- g5TIh84amg (5.50, Reject — curriculum view of robust losses): Provides an analysis lens for existing methods; comparable contribution scope to the FR paper but with less real-world validation.
- 3GurO0kRue (6.50, Accept — On Harmonizing Implicit Subpopulations): Stronger theoretical guarantees, cleaner framing, no label noise handled; scores higher partly due to theoretical rigor missing from the FR paper.
- u1yvEwYfK9 (5.67, Reject): Rejected for theoretical gap between method and its stated goal — directly analogous to the FR paper's semantic gap between the regularizer and the clean-label objective.

**Positioning:** The paper is better than x3lE88YkUl (5.20) and g5TIh84amg (5.50) in terms of breadth and dataset coverage, but is held back relative to 3GurO0kRue (6.50) by the missing dedicated baselines, the semantic gap in the FR objective, and the statistical testing issues. The analogy to u1yvEwYfK9 (5.67, Reject — rejected partly for a theoretical-empirical gap similar to FR's noisy-label objective mismatch) is instructive. The combined weight of (1) the missing dedicated joint-problem baselines and (2) the unresolved FR objective mismatch places this paper below the acceptance threshold. Final score: **5.0**.

| Anchor | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| 3GurO0kRue | calibration/.../3GurO0kRue.md | 6.50 | 1+2 | Accept; stronger theory, subpopulation harmonizing — above this paper |
| TjhUtloBZU | calibration/.../TjhUtloBZU.md | 6.25 | 1 | Accept; noisy labels + pre-training — different scope |
| u1yvEwYfK9 | calibration/.../u1yvEwYfK9.md | 5.67 | 1+2 | Reject; label shift correction — similar theoretical gap issue |
| SwRlpDKrY9 | calibration/.../SwRlpDKrY9.md | 5.20 | 1 | Reject; long-tail debias — narrower contribution |
| g5TIh84amg | calibration/.../g5TIh84amg.md | 5.50 | 2 | Reject; robust loss analysis — similar analytical scope |
| x3lE88YkUl | calibration/.../x3lE88YkUl.md | 5.20 | 2 | Reject; SAM for noisy labels — narrower plug-in contribution |
| SRn2o3ij25 | calibration/.../SRn2o3ij25.md | 4.67 | 2 | Reject; long-tail only, narrower — below this paper |
| RwiUmrEHgR | calibration/.../RwiUmrEHgR.md | 3.00 | 1 | Reject; cost-sensitive long-tail — weaker |
| 6PGT9OJX5N | calibration/.../6PGT9OJX5N.md | 3.00 | 1 | Reject; noisy data pruning — different topic |

**Originality:** Moderate. The coupling of fairness constraints and noisy+imbalanced learning is novel; the regularizer itself is a standard Lagrangian relaxation.
**Importance:** High. Joint noise+imbalance is ubiquitous in practice.
**Claim support:** Partial. Many results are strong, but key baselines are absent and the objective mismatch is unresolved.
**Experimental soundness:** Adequate breadth, but statistical testing is flawed and Clothing1M gains are marginal.
**Clarity:** Good overall; specific cells in tables where FR hurts are not discussed.
**Value to community:** Positive as a diagnostic tool and plug-in boost; limited as a standalone contribution without the missing comparisons.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>