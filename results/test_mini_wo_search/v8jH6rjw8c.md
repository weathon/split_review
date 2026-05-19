Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

## Summary

This paper proposes a Fairness Regularizer (FR) that penalizes accuracy gaps between sub-populations when learning from noisily labeled long-tailed data. The authors first demonstrate empirically that existing robust methods have disparate impacts on different sub-populations (tail classes especially), then introduce FR as a Lagrangian relaxation of fairness constraints that encourages equalized prediction confidence across groups. Extensive experiments on synthetic CIFAR datasets (two noise types, multiple imbalance ratios) and real-world noisy datasets (CIFAR-N, Animal-10N, Clothing1M) with six baseline methods show consistent improvements, particularly when using a two-group head/tail split (FR-G2).

## Strengths

1. **Extensive and systematic experimental validation**. Table 1 covers 6 baselines × 2 noise types × 2 noise rates × 3 imbalance ratios = 72 settings on CIFAR-10 and CIFAR-100, plus real-world experiments on CIFAR-10N/100N/20N, Animal-10N, and Clothing1M (Tables 2-4). The consistency of improvements with FR(G2) — e.g., CE on CIFAR-10 (Imb noise, ρ=0.2, r=100) rising from 60.03 to 65.12 — is well-documented.

2. **Per-class accuracy visualization (Figure 4)** directly shows that FR improves tail sub-populations. The scatter plots showing per-class accuracies with vs. without FR, with many tail-class points above the y=x line, provide direct evidence for the paper's central mechanism.

3. **Generalization across multiple real-world noisy datasets** (CIFAR-10N, CIFAR-100N, CIFAR-20N, Animal-10N, Clothing1M) demonstrates the regularizer works beyond synthetic noise settings. The hyperparameter sensitivity analysis on Clothing1M (Table 4) shows FR is not overly sensitive to λ.

4. **Clear motivation** via the empirical observation (Figure 2) that existing robust methods help some sub-populations while hurting others — this is the paper's strongest conceptual contribution and is well-illustrated.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The λ hyperparameter for synthetic CIFAR experiments is not stated.** The paper notes "For simplicity, we set all λ_i to a constant, i.e., λ_i = λ" (line 190) and mentions that real-world experiments use λ=2 for CE and λ=1 for Logit-adj (line 393), but the actual λ value used for the main synthetic CIFAR results in Table 1 is never specified. This is a reproducibility gap, albeit small since Clothing1M results show the method is not highly sensitive to λ.

2. **Per-class disparity analysis is qualitative, not quantitative.** While Figure 4 shows that tail classes improve, the paper does not report a formal disparity metric (e.g., head-tail accuracy gap, standard deviation of per-class accuracy, or worst-class accuracy). The claim that "fairness improves learning" would be strengthened by numerically demonstrating that disparity is reduced and that the reduction correlates with overall improvement.

3. **The paired t-test across 12 heterogeneous settings is non-standard.** The test treats 12 settings (2 noise types × 2 noise rates × 3 imbalance ratios) as independent replicates, which they are not — the differences come from systematically different conditions. This does not yield a valid p-value for the hypothesis "does FR help across settings?" The raw improvement counts and magnitudes are informative on their own; the statistical formalism adds little. This is a minor methodological presentation issue, not an evidential flaw, since the trend is clear from the raw data (FR-G2 improves in roughly 85% of Table 1 entries).

4. **The influence analysis (Section 3) does not lead directly to the FR design.** The analysis shows tail sub-populations have larger influence under noise, but FR is a generic disparity penalty that could be motivated without this analysis. The connection is not tight — the influence study shows that tail groups matter more, while FR addresses outcome equality. This is a presentational disconnect rather than a substantive flaw, but it adds length without proportional insight.

### Trivial
- The paper mentions a binary Gaussian theoretical result (line 192-196) but does not include it in the main text. Depending on whether it was deferred to an appendix, this may be a presentation issue.

## Nice-to-Haves
- Reporting a formal disparity metric (head-tail accuracy gap or per-class accuracy std) alongside overall accuracy would strengthen the claim that FR actually reduces disparity.
- A control experiment with random (non-informative) sub-population splits would help confirm the benefit comes from meaningful grouping rather than generic regularization.
- Specifying λ values for the synthetic CIFAR experiments in Table 1.

## Removed Points

These points are flagged to be removed — treat them with caution:

1. **"The paper never reports whether FR actually reduces disparity" (Harsh Critic Point 2).** This is factually incorrect — Figure 4 explicitly shows per-class accuracy comparisons (baseline vs. baseline+FR), with the discussion noting that tail classes (lower-left points) consistently improve. The paper does this qualitatively rather than quantitatively, but it does report it.

2. **"The best-performing variant (G2) undermines the generality of the approach" (Harsh Critic Point 3).** The paper openly discusses why KNN struggles on CIFAR-100 (batch size per cluster is ~1.28, causing high variance in Eq. 13) and presents G2 as an alternative. Finding that a coarser split works better under practical constraints does not undermine the general principle of disparity regularization — it is a practical finding about granularity. The paper's claim is about fairness constraints improving learning, not about which specific grouping works best.

3. **"The regularizer uses noisy accuracy... this is a structural flaw" (Harsh Critic Point 1, framing as fatal).** The regularizer uses the model's prediction probability on the given (noisy) label, which is a natural quantity to regularize during training. The paper provides extensive empirical evidence (Tables 1-4) that this improves clean test accuracy. Calling this a "structural flaw" that prevents the paper's contribution from standing is not supported by the evidence on the page. The empirical results directly answer "does equalizing this noisy proxy help clean accuracy?" A theoretical gap exists in explaining why, but the paper acknowledges a theoretical result (binary Gaussian) exists, and the empirical validation is thorough.

4. **"The influence analysis is disconnected from the method" as a "methodological gap" (Harsh Critic Point 5).** The influence analysis motivates the problem by showing tail populations have disproportionate influence under noise. This is standard motivational framing. Many papers include pre-method analyses to motivate their approach. Calling it a "methodological gap" is overblown — it is a mild presentational observation at worst.

5. **Strength Finder's generic/superficial strengths.** The finding that FR "generalizes to real-world noisy datasets" (Strength Finder's Supporting #3 in the original) is already covered in the main strengths. The "empirical analysis of disparate impacts using influence functions" as a standalone supporting strength is weak — the influence analysis is descriptive, not a contribution per se. These are subsumed by the main strengths above.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an unexpected perspective on the work that the paper itself does not already articulate.

## Suggestions

- Report the λ value used for Table 1 synthetic CIFAR experiments.
- Add a table showing a formal disparity metric (e.g., head-tail gap, per-class accuracy std) for a representative subset of settings to explicitly verify that FR reduces disparity as claimed.
- Replace or supplement the paired t-test with a more appropriate analysis (e.g., reporting mean improvement and standard deviation across settings, or a simple sign-test).

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>