Now I have a thorough understanding of the paper. Let me construct the consolidated review.

## Summary

This paper develops a theoretical framework for data curation in high-dimensional binary classification, providing exact asymptotic test error formulas (Theorems 1-3) under label-agnostic and label-aware pruning oracles. The theory characterizes when "keep hard" vs "keep easy" strategies are optimal based on generator quality (ρ) and pruner quality (ρ*), and when aggressive pruning (keeping a fraction p<1) can outperform using all data. The framework is validated on synthetic Gaussian data, applied to ImageNet classification, and used to interpret recent LLM reasoning results.

## Strengths

1. **Theorem 2 (Optimal Pruning Strategy)** provides a clean, analytical resolution to the central question: when generator and pruner are both strong, "keep hard" is optimal; when generator is weak but pruner is strong, "keep easy" is optimal. This directly addresses the "less is more" vs "more is more" paradox with a precise, testable condition.

2. **Theorem 1 (Exact Test Error)** derives an exact asymptotic formula for test error under any symmetric pruning strategy, reducing the effect of curation to four summary constants (p, γ, β, β̃). This constitutes a rigorous scaling law for high-dimensional binary classification under data pruning, going beyond heuristic analysis.

3. **Synthetic validation (Figure 1)** cleanly demonstrates the match between theoretical predictions and empirical simulations across four regimes defined by data scale and generator quality. The bottom-left panel (abundant data + strong generator) confirms the "less is more" prediction with optimal p<1, and the agreement between theory (solid lines) and simulation (dashed lines) is strong.

4. **ImageNet crossover (Figure 2, left and middle panels)** empirically demonstrates that the optimal curation strategy depends on generator strength: with a weak generator (small n) "keep easy" is better, while with a strong generator (large n) "keep hard" is better. This validates Theorem 2's prediction about how the optimal strategy shifts with ρ.

5. **Model collapse mitigation (Figure 3)** provides empirical evidence that strategic "keep hard" curation maintains stable performance across rounds of iterative self-training, while training on all uncurated data degrades from ~30% to ~52% error. This extends the theory's practical relevance beyond one-shot efficiency to iterative training stability.

## Weaknesses

### Fatal

None.

### Major

1. **ImageNet experiments validate the crossover prediction but do not show that curated subsets outperform full datasets ("less is more").** The core "less is more" claim — that under certain conditions keeping a fraction p<1 of data yields lower test error than using all data — is cleanly demonstrated in the synthetic experiments (Figure 1, bottom-left) but is not shown in the ImageNet experiments. In Figure 2 (left two panels), both "keep hard" and "keep easy" curves decrease monotonically as more data is kept (p→1), meaning the optimal is at p=1 for both strategies. The ImageNet results validate a different prediction (which strategy is optimal given generator strength) rather than the "aggressive pruning beats full data" prediction. The abstract states "we validate these theoretical claims with empirical results on ImageNet" — this conflates two distinct claims and overstates the support. The paper would be stronger if it either (a) reframed the ImageNet experiments as validating the crossover prediction only, or (b) additionally tested whether p<1 can beat p=1 on some vision benchmark.

2. **The synthetic experiments (Figure 1) compare "keep hard" against "random" but not against "keep easy", missing a direct test of Theorem 2's central prediction.** Theorem 2 predicts that with a strong generator, "keep hard" beats "keep easy" (and vice versa for weak generator). The synthetic experiments only compare "keep hard" vs "random" selection. While this demonstrates the "less is more" effect (p<1 optimal), it does not test the keep-hard-vs-keep-easy prediction that is the centerpiece of Theorem 2. The ImageNet experiments do test this, but without the controlled setting of the synthetic experiments. A synthetic test of the full Theorem 2 prediction would strengthen the empirical link between theory and the crossover observed on ImageNet.

3. **The model collapse experiment (Figure 3) lacks essential details to be interpretable or reproducible.** The paper states: "We simulate model collapse by repeatedly re-training on the model's own pseudo-labels. Figure 3 shows that while training on all data causes performance to degrade, applying the 'keep hard' strategy at each step stabilizes performance." Critical details are absent from the main text: (i) What model architecture and dataset are used? (ii) How is "hard valid examples" defined operationally? (iii) How many rounds are conducted and how is the initial model trained? (iv) How are pseudo-labels generated? Even accounting for the appendix, the main-text description is too sparse for a reader to assess the validity of the results. The claim that "strategic pruning prevents model collapse" is substantively important and deserves a clearer experimental account.

4. **The LLM discussion (Section 4.2) is post-hoc interpretation, not empirical validation of the theory.** Tables 1 and 2 reproduce numbers from existing papers (LIMO, s1, Sun et al.) and argue they are consistent with the theory, but no new experiments are conducted, no quantitative measure of ρ is provided for the LLM setting, and the link between the Gaussian-linear model and chain-of-thought reasoning data is entirely conjectural. While such interpretive discussion enriches the paper, the abstract's phrase "connect them to recent large-scale results in LLM reasoning" overstates the evidential weight. This should be clearly demarcated as hypothesis-generation rather than validation.

### Minor

1. **The theory's central quantities (ρ, ρ_∗, ρ_g) are not estimated for the ImageNet experiments**, so the link between theory and experiment remains qualitative. The paper controls generator strength by varying training set size (n), but never measures or reports the actual ρ values. Providing even a proxy measurement (e.g., test accuracy of the generator model) would strengthen the claim that the observed crossover aligns with the predicted ρ-dependent transition.

2. **The ImageNet figure description mentions both "Error Rate vs. Percentage of Data Kept" and "Error Rate vs Dataset Size" plots, but the rightmost plot appears inconsistent with the left two.** The right plot ("Error Rate vs Dataset Size") shows error decreasing with dataset size for both strategies, but it is unclear how this relates to the keep-fraction plots on the left. The paper states a "clear crossover point" but the right plot appears to show the two strategies converging, not crossing. This figure requires a clearer explanation of what each subplot demonstrates and how they jointly support the theory.

### Trivial

- The paper uses "w_p" (likely a typo for "w_o") in Theorem 2's premise.
- The figure numbering in the text references "Figure 4" (Section 4.1) which does not appear in the extracted paper.

## Nice-to-Haves

- A practical discussion of how to estimate ρ, ρ_∗, ρ_g from data would significantly increase the paper's impact for practitioners. Currently the theory identifies the regime-dependent optimal strategy but provides no guidance on how to determine which regime one is in.
- Testing the "p<1 optimal" prediction on a real-world dataset (e.g., using a simplified linearized setting like random features or NTK features on ImageNet) would bridge the gap between the synthetic validation and the large-scale experiments.
- Including statistical significance or variance estimates for the ImageNet and model-collapse results would strengthen confidence in the observed patterns.

## Removed Points

These points are flagged to be removed, treat them with caution:

- *"Insufficient experimental detail prevents reproducibility and assessment"* — Much of the experimental detail is likely in the appendix (which is stripped by the parser). The instruction forbids penalizing for missing appendix content. However, the main-text description remains sparse even for an extended abstract, which is why a reduced version of this concern appears as Major weakness 3 (specific to the model collapse experiment where the main-text description is unusually thin).
- *"The theory applies to a narrow setting far from practical systems"* — This is acknowledged in the paper's own limitations section (§6). The paper's contribution is primarily theoretical; the gap between Gaussian-linear theory and deep learning is a standard limitation that the authors explicitly flag. Criticizing this as if it were an oversight is not fair.
- *"No mention of statistical significance or variance"* — For large-scale image classification experiments, single-run evaluation is standard practice. This is a generic reproducibility nitpick rather than a specific identified problem.
- *Harsh critic claims the ImageNet experiments "only compare two fixed strategies at a default keep fraction"* — This is factually incorrect; Figure 2's x-axis is "Percentage of Data Kept," showing that keep fraction was varied. The curves span a range of p values.
- *Missing hyperparameters and training details* — These are standardly deferred to the appendix in conference submissions.
- *Strength Finder's claim that Section 4.2 "reconciles contradictory LLM reasoning results"* — While interesting, this is interpretive consistency-checking rather than empirical validation. The strength is retained but downgraded; the interpretive nature is noted in Major weakness 4.

## Novel Insights

The reviews collectively surface a genuine tension that the paper does not fully resolve: the theory makes at least two distinct predictions — (i) which strategy (keep-hard vs keep-easy) is optimal given generator strength, and (ii) that a smaller curated set (p<1) can outperform the full set (p=1). The paper presents evidence for both, but prediction (i) is validated only on ImageNet and prediction (ii) only in synthetic data. The reviews correctly identify that the ImageNet results do not support prediction (ii) — the curves are monotonic in p. This gap between the paper's two-pronged claim and the experiments that partially validate each prong separately is a more precise diagnosis than either "the experiments don't test the central claim" (Harsh Critic) or "the experiments support the theory" (Strength Finder) captures on their own. A stronger paper would either restrict its empirical claims to match the evidence or design experiments that jointly test both predictions.

## Suggestions

1. **Disentangle the two claims in the abstract and introduction.** The "less is more" (p<1 optimal) claim and the "optimal strategy depends on generator strength" (KH vs KE crossover) claim are distinct. The abstract should make clear which parts of the theory are validated by which experiments.

2. **For the ImageNet experiments, explicitly test whether any p<1 yields lower error than p=1 for the "keep hard" strategy.** If the monotonic trend holds, acknowledge this honestly and frame the contribution as validating the crossover prediction instead.

3. **Provide at least a proxy measure of ρ for the ImageNet experiments** (e.g., accuracy of the generator model on the test set) so readers can assess whether the observed crossover occurs at the expected ρ threshold.

4. **Expand the model collapse experimental description** to include the model architecture, dataset, definition of "hard valid examples", and number of rounds. Even a brief paragraph in the main text would substantially improve interpretability.

5. **Reframe the LLM section (4.2) explicitly as hypothesis generation / reconciliation rather than validation.** This would align the prose with what the section actually delivers.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>