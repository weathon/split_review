Now I have a thorough understanding of the paper and both reviews. Let me produce the final consolidated review.

---

## Summary

This paper introduces the problem of "concept forgetting" — modifying a pre-trained classifier so its predictions become independent of a specified concept (e.g., gender, digit identity) — and proposes Label Annealing (LAN), an iterative algorithm that redistributes labels within each concept subgroup to create pseudo-labels with zero concept violation, then fine-tunes on those pseudo-labels. The method is evaluated on MNIST, CIFAR-10, miniImageNet, and CelebA across binary-level and multi-level concept forgetting.

## Strengths

- **Clear problem definition and formal metric.** The paper formally defines concept neutrality (Definition 1) via demographic parity of predictions and quantifies violation via total variation distance (Definition 2), operationalizing a meaningful and under-explored goal. The distinction from machine unlearning is well-drawn and illustrated concretely with Figure 1.

- **LAN algorithm is well-motivated and computationally efficient.** The iterative two-stage procedure (label redistribution + fine-tuning) is intuitive. The paper demonstrates that a single iteration (E=1) suffices for substantial violation reduction, supporting the claim of low time complexity — a genuine advantage over fairness-regularization baselines that require many epochs.

- **Valid empirical evidence on CelebA.** The multi-level concept forgetting results on CelebA (Table 2: ~63.52% violation reduction; e.g., forgetting facial hair while classifying attractiveness) involve concepts genuinely separable from the target labels, making this the most convincing portion of the evaluation. The trade-off curves in Figure 3 show LAN achieving lower concept violation than FERMI, Continuous-Fairness, and Fairness-KDE at matched accuracy levels.

- **Ablation studies provide useful insight.** Table 3 (learning rate sweep) and Figure 4 (iterations E=1,2,4) demonstrate robustness and show that more iterations flatten the trade-off curve, which is consistent with the algorithm's design.

## Weaknesses

### Fatal

- **MNIST and CIFAR-10 class-forgetting results are mathematically impossible under the stated metric.** The paper defines concept violation (Definition 2) as the total variation distance between the marginal prediction distribution P(\hat{h}=y) and the per-concept-group prediction distribution P(\hat{h}=y|C(z)=c). For the MNIST "forget class-3" experiment (concept is binary: digit-3 or not), concept neutrality requires P(\hat{h}=3|C=1) ≈ P(\hat{h}=3). Since P(\hat{h}=3) ≈ 0.1 (10 roughly balanced classes), the model can predict class 3 on only ~10% of digit-3 samples — a collapse in per-group accuracy from ~97% to ~10%. Yet the paper reports accuracy rising from 97.3% to 97.5% while concept violation drops from 0.5452 to 0.0128. Standard algebra shows this is impossible: with digit-3 being ~10% of the data, even if accuracy on non-digit-3 reached 100%, the highest achievable overall accuracy under near-zero concept violation would be ~91%, not 97.5%. The same contradiction applies to the CIFAR-10 results (91.3%→91.4% accuracy, 0.6085→0.0084 violation). These results appear in the headline aggregate claims (abstract, contributions list, Table 1) and their inclusion fundamentally undermines the paper's empirical credibility. The paper offers no explanation — no reweighting, no alternative evaluation protocol, no acknowledgment that this specific forgetting setting is impossible to solve without accuracy degradation.

### Major

- **No error bars, variance reporting, or multi-seed results.** Every quantitative claim in Tables 1–3 and Figures 3–4 is presented as a single point estimate. Without standard deviations or confidence intervals (standard in this field, typically 3–5 seeds), the reader cannot assess whether the reported reductions are statistically significant or driven by a single favorable run.

- **Per-subgroup accuracy is not reported.** For the CelebA gender-forgetting experiment, the paper reports only overall test accuracy. Since the goal is to make predictions independent of gender, the paper should report accuracy on male and female test sets separately to demonstrate that the model performs well for both groups and has not collapsed to a degenerate solution.

### Minor

- **Definition 1's notation is ambiguous.** The expression `P_xy(\hat{h}=y|C(z)=c) = P_xy(\hat{h}=y)` uses `y` both as the marginalization variable (output class) and as part of the joint distribution subscript `P_xy`. A careful reader can disambiguate from the empirical formula (Eq. 3), but the abstract definition is easily misread as comparing accuracy across groups (which would be a different metric). This should be cleaned up.

- **Baseline fairness constraints are underspecified.** The paper adopts FERMI, Continuous-Fairness, and Fairness-KDE from the fairness literature but does not state which specific fairness constraint (demographic parity, equalized odds, etc.) was enforced for each baseline. If the baselines were configured for a different notion than the paper's concept violation metric, the trade-off curves in Figure 3 are not an apples-to-apples comparison.

- **Theorem 1 is not validated against experiments.** The bound (accuracy loss ≤ 4·L·E·m·original violation) is not computed or compared to any of the reported results, limiting its practical value. It also applies only when the original model already has low violation — the regime where the problem is least interesting.

- **The label assignment rule in Algorithm 1 is described in prose rather than pseudocode or a formulaic condition.** The description ("until the no of samples in class-j* is less than b_{j*} * n_c / |D|") is ambiguous about off-by-one behavior when the count exactly equals or exceeds the target.

### Trivial

- None.

## Nice-to-Haves

- Including a simpler baseline (e.g., fine-tuning on a dataset where the concept-label correlation is artificially broken through reweighting) would help isolate the specific benefit of the label-annealing mechanism.
- Per-concept accuracy breakdowns would strengthen the evaluation.

## Removed Points

These points from the input reviews were filtered under the instructed rules; they should be treated with caution if referenced:

- **Criticism that class-forgetting experiments make the entire contribution not credible** (from Harsh Critic). While the MNIST/CIFAR-10 class-forgetting results are fatally flawed, the CelebA experiments (both binary-level gender forgetting and multi-level facial hair/hair color forgetting) involve concepts genuinely distinct from the target labels and are not affected by this issue. The core algorithm and its valid evidence are not entirely invalidated.

- **Criticism about notation being "more than cosmetic" and obscuring the metric** (from Harsh Critic). The notation is indeed ambiguous in Definition 1, but the empirical formula in Eq. 3 is unambiguous, and the algorithm description (line 149) correctly uses the demographic-parity interpretation. The notational issue is minor, not structural.

- **Critique that the theorem "is given more weight than it deserves"** (from Harsh Critic). This is a judgment call; the paper states the theorem and its limitation (applies when original violation is low) explicitly. The theorem is presented as a bound, not a tight guarantee, and is appropriately caveated.

- **Claim that the paper would be "substantially stronger" by removing MNIST/CIFAR-10 results entirely** (from Harsh Critic's strengthening suggestions). The paper's headline claims span all datasets; removing these results from the aggregated claims is indeed necessary, but the suggestion form (strengthening suggestion) is not itself a weakness.

- **Generic strengths from Strength Finder** (e.g., "clear distinction from machine unlearning", "generality across models and datasets") — kept when specific and evidence-grounded, filtered when generic or when they duplicate criticisms. The "generality across models" strength is retained because the paper does show results across MLP, MobileNetV2, DenseNet-121, and ResNet-50.

- **Criticism about "no statistical significance or variance reporting"** (from Harsh Critic) — merged into a single Major weakness rather than listed separately.

## Novel Insights

The most incisive observation from the reviews is that the MNIST/CIFAR-10 class-forgetting problem setting (making predictions independent of whether the input belongs to a specific target class) is fundamentally ill-posed when the concept coincides with the prediction target. Under the demographic parity definition, forcing the prediction distribution on "digit-3" samples to match the marginal distribution (~10% class 3 predictions) necessarily collapses accuracy on those samples. The paper treats this as an ordinary experiment rather than recognizing it as a boundary case that the definition cannot accommodate without accuracy degradation. This suggests the paper's own problem framing implicitly requires the concept to be distinct from the target label — a constraint that the paper never articulates and that its headline experiments violate.

## Suggestions

1. **Remove the MNIST and CIFAR-10 class-forgetting experiments**, or transparently reframe them as a stress test with the acknowledged consequence that accuracy on the forgotten class must drop (and report that drop honestly). Under no circumstances should these results appear in aggregated average-violation-reduction claims.

2. **Add standard deviations over at least 3 random seeds** to all tables and figures.

3. **Report per-subgroup accuracy** for all binary-concept experiments (e.g., accuracy on male vs. female test sets for the CelebA gender experiment).

4. **Specify the exact fairness constraint** used for each baseline and confirm it matches the concept violation metric (demographic parity of hard predictions).

5. **Clean up Definition 1's notation** and replace the prose algorithm description with concrete pseudocode.

## Score and Decision

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>