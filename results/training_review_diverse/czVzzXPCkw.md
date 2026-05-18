Now I have a thorough understanding of the paper and all the reviewer claims. Let me synthesize the final review.

---

## Summary

This paper tackles the underexplored problem of extrapolation in material property regression (MPR): predicting material properties beyond the range of training data. It curates a benchmark of seven tasks from four Matminer datasets with extreme-value splits, systematically evaluates existing deep imbalanced regression (DIR) and data augmentation (DA) methods, and proposes MEX (Matching-based EXtrapolation), which reframes regression as a material-property matching problem using cosine similarity and noise contrastive estimation.

## Strengths

1. **Identifies and formalizes an underexplored problem.** The paper clearly motivates why extrapolation matters for material discovery (finding materials with properties beyond existing records) and demonstrates that existing benchmarks use i.i.d. splits, leaving this critical scenario unaddressed. The evidence is concrete: prior CGCNN achieves 0.0452 MAE on Formation Energy under random split vs. the smallest MAE of 0.172 under the extrapolative split (Section 4.3).

2. **Curates a dedicated extrapolation benchmark with realistic splits.** Seven tasks from four datasets using top/bottom 15% splits aligned with real material design goals (e.g., low formation energy for stability). The splits (Table 1, Figure 3) provide a reproducible foundation that the community can build on — this is the paper's most robust contribution.

3. **Thorough evaluation of existing methods reveals their limitations.** The paper systematically tests four DIR methods and two DA methods under two backbones (PaiNN, EquiformerV2). The finding that no single DIR method outperforms ERM across all datasets, and that DA benefits depend on backbone quality, is a useful empirical result that supports the paper's motivation.

4. **Proposes a creative matching-based framework.** The idea of reframing regression as matching — learning a similarity function between material and label representations rather than a direct mapping — is novel for the MPR setting and well-motivated.

5. **Honestly acknowledges that extrapolation remains very hard.** The paper openly states that even MEX's best MAEs are substantially larger than random-split numbers and that Spearman correlations are weak (Section 4.3), which strengthens credibility.

## Weaknesses

### Fatal
None.

### Major

1. **Candidate label range uses test-set information, compromising the central comparison.** During inference (Section 3.2.2), MEX's candidate labels are "initially sampled uniformly from [[l],[u]], where l and u are the lower bound and upper bound of the *entire dataset* label range" (line 135, emphasis added). Since the benchmark splits use the most extreme 15% of values as the test set (Section 4.1), the "entire dataset range" necessarily includes the test label range. This means MEX knows the extent of the extrapolation region during inference, while no baseline (ERM, DIR, DA) has access to any test-range information. The paper's note that "this interval can be freely adjusted based on prior knowledge" acknowledges the design choice but does not resolve the experimental asymmetry: in the actual experiments, MEX benefits from information unavailable to baselines. This directly affects every quantitative claim in Tables 2, 3, and Figure 5. **Why this matters:** If the candidate range were restricted to the training range, MEX would literally be unable to predict values outside it (since prediction is argmax over the candidate set). The experimental comparison is therefore not a level playing field. This is the paper's most serious weakness and requires re-running experiments with a candidate range derived strictly from training data (e.g., [min_train − δ, max_train + δ] for a reasonably chosen δ).

2. **Uncontrolled model capacity.** MEX adds a label encoder (linear layer + activation) and a 4-layer MLP score module on top of the backbone encoder (Section 3.2, line 133). No baseline method includes equivalent extra neural network parameters. DIR methods (LDS, BalancedMSE, Ranksim, Conr) modify losses or reweighting schemes without adding network layers; DA methods (C-Mixup, FOMA) augment data without adding parameters. Without a control experiment where an MLP of comparable size is appended to the backbone and trained with ERM or the best DIR method, it is impossible to attribute MEX's gains to the matching formulation rather than increased capacity. The score-module ablation in Table 4 only compares MEX variants, not capacity parity with baselines.

### Minor

1. **Detection metric has limited interpretability.** The recall metric in Section 4.4 defines a sample as "detected" if its *predicted* value falls within the extrapolation interval. This measures whether the model's output lands in the right ballpark, not whether it identifies the truly extreme *samples* accurately. As the reviewer notes, a model predicting a constant value near the boundary could achieve high recall while having terrible per-sample accuracy. The paper does report standard MAE and Spearman alongside (which mitigates the concern), but the detection claims in Figure 5 and the associated discussion ("identify cutting-edge materials") would benefit from a more cautious framing and/or an additional metric such as precision/recall at an absolute error threshold.

2. **No ablation of individual loss components.** The paper ablates the score module design (Table 4) and the trade-off parameter λ (Figure 6), but never shows results for ℒ_nce only (λ=0) or ℒ_abs only. Without these, it is unclear whether both losses are necessary or whether one dominates — especially important since the core claim is that the combination captures both "absolute" and "relative" matching relationships.

3. **No comparison of iterative inference vs. simpler alternatives.** The inference procedure uses 10 iterations of Monte Carlo optimization over 1500 candidate labels (Section 3.2.2). A comparison against a single argmax over a fixed candidate grid would clarify whether the iterative refinement is essential for performance or merely incidental.

### Trivial
- The Spearman correlation discussion in Section 4.3 contains a truncated value ("weak (0-0..."), likely a PDF extraction artifact.

## Nice-to-Haves
- Statistical significance discussion: many results in Tables 2/3 overlap within one standard deviation (e.g., Shear Modulus (top): MEX=32.7±1.2 vs BalancedMSE=32.5±0.7 for EquiformerV2). A brief statement on which differences are meaningful would strengthen the paper.
- Per-dataset sensitivity analysis for λ, rather than a single optimal value found via grid search.
- Discussion of how the candidate label range would be set in a real discovery scenario where the target property range is unknown.

## Removed Points
These are points from the reviews that were filtered as per the instructions:
- **Data leakage framed as "fatal" by reviewer:** Downgraded to Major. While the experimental comparison is compromised, the benchmark itself and the problem framing remain independently valuable. The method's concept is not invalidated, only the experimental setup.
- **"Only 7 tasks, not comprehensive":** Scope creep. 7 tasks from 4 datasets covering diverse properties is a reasonable benchmark for a conference paper.
- **Running time complaint (3× slowdown):** 0.006s vs 0.002s per sample is acceptable overhead; the paper's characterization as "comparable" is fair.
- **"Does not engage with theoretical limitations":** Standard for an empirical systems/benchmark paper; moved to Nice-to-Haves.
- **Pure formatting/style complaints:** Removed as these are parser artifacts.

## Novel Insights
None beyond the paper's own contributions. The reviews surface the experimental design flaw (candidate range leakage) and the capacity control gap, which are genuine methodological concerns, but do not produce new scientific insights about the problem.

## Suggestions
1. **Fix the candidate range setup:** Re-run all experiments with the candidate label range derived from training data only. A reasonable approach: set the range as [min_train − α·(max_train−min_train), max_train + α·(max_train−min_train)] for a small α (e.g., 0.2–0.5), or use a domain-informed extension. If MEX still outperforms baselines, the core claim holds.
2. **Add a capacity-controlled baseline:** Append an MLP of comparable size to MEX's label encoder + score module to the backbone and train with ERM or BalancedMSE. Compare against MEX to separate the effect of extra parameters from the matching formulation.
3. **Ablate the two loss components:** Report results for ℒ_abs only, ℒ_nce only, and their combination.
4. **Simplify the inference comparison:** Compare the full iterative inference against a single argmax over a fixed grid of 1500 candidate labels.
5. **Caveat the detection metric:** Add a sentence noting that the recall metric measures range-awareness, not per-sample accuracy, and consider reporting top-k recall of truly extreme samples as a complementary metric.

## Score and Decision

The paper addresses a genuinely important problem and contributes a useful benchmark. However, the central experimental comparison — the claim that MEX achieves state-of-the-art performance — is compromised by the candidate range including test-set information. This is not a fatal flaw in the method itself, but it means the experimental results as presented do not support the paper's strongest claims. The benchmark and problem formulation remain contributions, but the paper cannot be accepted in its current form.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>