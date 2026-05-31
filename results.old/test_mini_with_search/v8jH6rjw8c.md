Now I have sufficient context from the calibration anchors. Let me write the final consolidated review.

---

## Summary

This paper studies learning from long-tailed data with label noise. It first provides an empirical analysis showing that existing robust/long-tailed methods have disparate impacts on different sub-populations (improving some at the cost of hurting others), and that tail sub-populations exert disproportionate influence under label noise. It then proposes a Fairness Regularizer (FR) that penalizes the gap between the average predicted probability on different sub-populations. Experiments on CIFAR-10/100 (synthetic noise), CIFAR-10N/100N/20N, Animal-10N, and Clothing1M show that adding FR to several baseline methods (CE, LS, NLS, Focal, PL, Logit-adj) yields statistically significant improvements in most settings.

## Strengths

1. **Novel empirical analysis of disparate impacts under combined long-tailed and noisy settings.** Figure 1 (per-class accuracy scatter plots) clearly shows that methods like Label Smoothing and PeerLoss have opposite effects on high-accuracy vs. low-accuracy sub-populations when the data is both long-tailed and noisy. Section 3 further quantifies this with population-level and sample-level influence metrics (Eqs. 1–2), showing that tail sub-populations have disproportionately high influence on test accuracy under label noise (Observation 1) and prediction confidence (Observation 2). This is a genuinely informative analysis that goes beyond standard per-class accuracy reporting.

2. **Simple, well-motivated regularizer that is easy to plug into existing methods.** The FR (Eq. 4 with Lagrangian relaxation) is straightforward: it computes the absolute gap between per-sub-population average predicted probability on the observed label and the global average. The fixed-λ design (rather than dual ascent) is explicitly justified as preventing the trivial "reduce all to worst-group" solution. This simplicity means FR can be added to any loss function with minimal overhead.

3. **Extensive evaluation across many settings with statistical significance testing.** Table 1 covers 12 synthetic settings (2 noise types × 2 noise rates × 3 imbalance ratios) × 6 baselines × 2 FR variants, plus real-world noise in Table 3 and Clothing1M in Table 4. The paired t-test in Table 2 shows that FR(G2) yields positive statistics and p<0.1 in 11/12 settings across CIFAR-10 and CIFAR-100, providing rigorous evidence that the improvements are not due to chance.

4. **Real-world noise evaluation on multiple datasets.** Table 3 shows CE+FR(G2) improves over CE on 17/18 settings across CIFAR-10N (3 noise types), CIFAR-100N, CIFAR-20N, and Animal-10N, demonstrating transfer to human-labeled noise. Clothing1M results (Table 4) with a λ sweep show that most λ>0 improve over λ=0, supporting the claim of hyperparameter insensitivity.

## Weaknesses

### Fatal
None.

### Major

1. **The regularizer uses predicted probability on noisy labels as a proxy for sub-population accuracy, with no justification for why this translates to clean accuracy.** The constraint in Eq. 4 computes $f_{x_k}[\tilde{y}_k]$ — the model's predicted probability on the *observed noisy label*. When the noise rate is high, the model may assign high probability to the (wrong) noisy label while being wrong about the clean label. The paper never discusses this mismatch or provides evidence (e.g., calibration analysis, correlation with clean accuracy) that the proxy is reasonable. The brief mention of a binary Gaussian example (lines 192–197) is not developed. This is a conceptual gap at the heart of the method's theoretical justification.

2. **The G2 sub-population separation method is insufficiently specified.** The description (line 322) says "Generate the separation by referring to the direct prediction made by an (Image-Net) pre-trained model. … this method separates features into a head and a tail sub-population, and the ratio w.r.t. the amount of samples between two sub-populations is usually close to 5." It is unclear what "direct prediction" means (argmax class? confidence score?) or how it produces exactly two groups. Since FR(G2) consistently outperforms FR(KNN) and is the primary variant used in the paper, this lack of precision undermines reproducibility. The requirement of an ImageNet pre-trained model for CIFAR (32×32 images) is also a practical limitation that is not acknowledged.

3. **No analysis of settings where FR hurts performance, despite several such cases.** There are specific settings where FR decreases accuracy: e.g., Logit-adj + FR(G2) on CIFAR-100 Imb ρ=0.5 r=10 (27.57 vs 30.92), CE + FR(G2) on Animal-10N r=50 (51.88 vs 52.60), PL + FR(KNN) on CIFAR-10 Sym r=50 ρ=0.2 (79.42 vs 79.73). The paper reports these in tables but never discusses them. Understanding when and why FR fails is essential for the claimed generality that "fairness improves learning." The aggregated t-test, while useful, masks these individual failures.

### Minor

4. **Experimental gains are modest.** Improvements are typically 1–3 percentage points on CIFAR-10 and smaller on CIFAR-100 and Clothing1M (e.g., CE on Clothing1M: 72.68 → 73.10 Best, 72.22 → 72.58 Last). While consistent, the practical significance is moderate.

5. **"Best-achieved test accuracy" reporting is non-standard.** Reporting the best accuracy over training epochs (rather than the last epoch or a fixed checkpoint) can overstate improvements due to early-stopping variance. No error bars or standard deviations over multiple runs are reported for the main tables.

6. **Connection between the influence analysis (Section 3) and the regularizer is heuristic, not derived.** The paper shows tail sub-populations have higher influence under noise, then proposes a fairness regularizer. The link is plausible but informal: the regularizer is not derived from influence-based reasoning, and the paper does not show that the sub-populations with highest influence are precisely those that benefit most from FR. The binary Gaussian example is merely noted, not developed.

7. **FR(KNN) on CIFAR-100 is acknowledged to suffer from small batch sizes, but this limitation is not analyzed systematically.** The paper notes (lines 324–325) that 128/100 ≈ 1.28 samples per sub-population causes large variance, but does not explore mitigations (larger batches, gradient accumulation, EMA updates) or provide diagnostic evidence for this claim.

### Trivial
None.

## Nice-to-Haves

- Analyze the correlation between the noisy-label proxy used in the regularizer and clean accuracy across sub-populations, to directly address the proxy concern.
- Provide the exact algorithm for the G2 split (e.g., threshold on confidence from a pre-trained model, or clustering into two groups based on prediction agreement).
- Include error bars or standard deviations over multiple random seeds for the main tables.
- Include a comparison to at least one dedicated long-tailed + noisy method (e.g., Wei et al. 2021, Zhong et al. 2019, or Karthik et al. 2021, which are cited in related work) to situate FR among tailored approaches.

## Removed Points

- *"Connection between empirical study and proposed method is weak"* — The paper never claims to derive the regularizer from the influence analysis; it says the empirical study "motivates us to explore ways that will reduce the gaps." The connection is reasonable: observation → reducing gaps should help → propose gap-reducing regularizer. The narrative is coherent, even if not formally derived.
- *"Influence metrics require retraining the model" (computationally heavy critique)* — This is a descriptive statement about the methodology, not a weakness of the paper's approach. The analysis is what it is.
- *"The Lagrangian relaxation fixes λ constant — not solving a principled fairness constraint"* — The paper explicitly justifies this choice (lines 179–182: dual ascent would over-penalize the worst group). It is a deliberate design decision, not an oversight.
- *"Baseline numbers not stated whether reproduced or taken from prior work"* — The paper states "We fix the same training samples and labels for all methods" (line 320), indicating baselines are reproduced in the same setup.
- Several other format/style nitpicks and strawman claims that misread the paper are removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Address the noisy-label proxy gap.** Either add a theoretical justification (e.g., connect the regularizer to clean accuracy via a noise model), or provide empirical evidence that the regularizer's value correlates with clean accuracy gaps (e.g., using a small clean validation set). Without this, the method's theoretical motivation is incomplete.

2. **Specify the G2 split precisely.** Provide the exact procedure: what "direct prediction" means, how it maps to a binary split, and the threshold used. This is critical for reproducibility since G2 yields the strongest results.

3. **Add a failure analysis section.** Discuss the specific settings where FR underperforms and hypothesize why (e.g., high noise + severe imbalance for Logit-adj, or domain mismatch for Animal-10N). This would strengthen the paper's claims by showing awareness of limitations.

4. **Report means and standard deviations over multiple runs** rather than (or in addition to) best achieved accuracy. This is standard practice and would make the results more trustworthy.

## Score and Decision

**Round 1 bracket**: I placed this paper between 4.0 and 6.5 after the initial bracketing pass. The most directly comparable anchor from round 1 was CARE (r3hc5aayC1.md, avg 4.0, Reject), which also addresses the long-tailed noisy-label problem. The current paper is stronger: it has a cleaner method, more extensive experiments (including Clothing1M), and statistical significance testing. The lower band (3.0) anchors were about less related topics and clearly weaker. The upper band (8.0) anchors were about completely different problems (RL, LLM scaling, kernel functions) and set a clearly higher bar.

**Round 2 narrowing**: I retrieved additional anchors in the 3.0–5.5 and 5.0–7.0 ranges. The SCER paper (Grb5AOs7WC.md, avg 5.0, Accept Poster) is the closest comparator: it also proposes a regularizer with modest improvements, extensive experiments, and some theoretical gaps. One reviewer gave SCER a 2, others 4, 6, 8. The current paper is comparable in quality and slightly stronger in the breadth of evaluation. The subgroup fairness anchor (17UDRTRLmp.md, avg 5.33, Accept Poster) provides an upper calibration point.

**Final calibration**: Against the SCER paper (5.0), this paper is slightly stronger — the empirical analysis of disparate impacts is novel, the experimental coverage is broader (more datasets and baselines), and statistical testing is included. Against the conformal prediction paper (6.0), this paper is weaker — that paper had cleaner mathematical grounding and the reviews were uniformly 6. I thus set the score at **5.5**, above the SCER anchor but below the conformal prediction anchor.

**Anchors used:**
- `/home/wg25r/review_agent/human_reviews_2026/r3hc5aayC1.md` (avg 4.0, round 1/2): CARE for long-tailed noisy labels. Rejected. This paper is notably stronger — simpler method, more baselines, statistical tests.
- `/home/wg25r/review_agent/human_reviews_2026/8L83ZbFDjk.md` (avg 6.0, round 1): Conformal Prediction for Long-Tailed Classification. Accepted Poster. This paper is cleaner and better-grounded theoretically; the current paper is weaker.
- `/home/wg25r/review_agent/human_reviews_2026/Grb5AOs7WC.md` (avg 5.0, round 2): SCER for worst-group robustness. Accepted Poster. Comparable paper — regularizer with modest gains, extensive experiments, some theoretical concerns. Current paper is slightly stronger.
- `/home/wg25r/review_agent/human_reviews_2026/17UDRTRLmp.md` (avg 5.33, round 2): Subgroup Fairness. Accepted Poster. Different topic but similar score band.
- `/home/wg25r/review_agent/human_reviews_2026/DX2POJEk8C.md` (avg 4.5, round 2): Long-tailed fine-tuning study. Rejected. Less relevant topic, lower execution quality.
- `/home/wg25r/review_agent/human_reviews_2026/v4Dmg30Ub5.md` (avg 3.0, round 1): Long-tailed classification. Withdrawn/rejected anchor for lower band.
- `/home/wg25r/review_agent/human_reviews_2026/RBktryANQ9.md` (avg 3.0, round 1): Label denoising. Withdrawn/rejected anchor for lower band.
- `/home/wg25r/review_agent/human_reviews_2026/RsCqOnkAKE.md` (avg 3.0, round 1): Fairness scaling. Rejected anchor for lower band.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>