Now I'll construct the review. Let me also verify the claim about "Masegosa ensembles have somewhat better calibration than ν-ensembles":

Line 103 confirms: "Masegosa ensembles on the other hand have somewhat better calibration than ν-ensembles in most cases."

Now let me produce the final consolidated review.

## Summary

The paper introduces ν-ensembles, a method for improving deep ensemble calibration by assigning different random labels to unlabeled data for each ensemble member. The method maintains the simplicity and linear scaling of standard ensembles while showing consistent calibration improvements across architectures (LeNet, MLP, WideResNet22) and datasets (CIFAR-10/100) for small-to-medium training set sizes (1K–10K samples). A PAC-Bayes bound is presented to motivate the approach.

## Strengths

- **Extreme simplicity with clear calibration gains**: The method requires no architecture changes, no joint training, and no complex diversity objectives — each member independently trains on the labeled data plus its own randomly-labeled version of the unlabeled pool. Despite this simplicity, Table 1 and Figure 2 show consistent and sometimes large improvements across ECE, TACE, Brier Score, and NLL for all tested architectures. This is a genuine practical contribution: practitioners can drop in this method with minimal effort.

- **Improved calibration under distribution shift**: On CIFAR-10-C (15 corruptions × 5 severity levels), ν-ensembles maintain accuracy while improving calibration across all architectures, with the gap widening at higher corruption intensities (e.g., from 10% to 15% ECE improvement for ResNet22). This suggests the diversity induced by random labels provides meaningful robustness.

- **Lower overhead than competing diversity methods**: Standard and ν-ensembles have O(1) memory cost and linear training-time scaling (members trained independently/sequentially), whereas Masegosa ensembles (joint training, ≈2× compute) and Agree-to-Disagree (sequential greedy, O(K) cost) are substantially more expensive. Figure 4 confirms this empirically.

## Weaknesses

### Fatal

None.

### Major

- **Theory-algorithm mismatch and overclaimed guarantee in the abstract**: Theorem 1 presents a PAC-Bayes bound where the diversity term \(\hat{V}(\hat{\rho})\) is computed using **true labels** on the unlabeled set \(U\) (which is drawn from the joint distribution \(\mathcal{D}\), line 65). The algorithm, however, assigns **random labels** to \(U\) and never uses true labels there. The bound therefore does **not** directly guarantee anything about the random-label procedure. Yet the abstract states the bound "guarantees that for such a labeling we obtain low negative log-likelihood and high ensemble diversity on testing samples." This overstates what the theory actually supports. The bound motivates *why diversity on unlabeled data is valuable*, and random labels are a heuristic for achieving it, but this gap should be acknowledged explicitly rather than glossed over. A revised framing would significantly strengthen the paper's credibility.

- **Training objective and balancing hyperparameter are never specified**: The paper states that ν-ensembles "fit both the training data and the randomly labeled data" (line 160) and mentions "a single hyperparameter that is easy to tune" (line 50), but it never states the exact loss function (e.g., does each member minimize \(\mathcal{L}_{\text{labeled}} + \lambda \mathcal{L}_{\text{random}}\)? Is it a simple sum? Is there a separate weighting for each term?). What \(\lambda\) values were used? How was it tuned? Without this information, the method cannot be reproduced or assessed for sensitivity to this choice. This is a fundamental specification gap that must be addressed.

### Minor

- **Unlabeled set size is never varied**: Across all experiments, the unlabeled set size is fixed at \(m=5000\) regardless of training set size (1000 to 40000). Since the method's computational cost and behavior depend on \(m\), the paper should at least show one ablation varying \(m\) (e.g., for the 1000-sample training setup) to verify that performance is not brittle to this choice and to guide practitioners.

- **Temperature scaling asymmetry in comparisons**: Temperature scaling is applied to standard ensembles and ν-ensembles but not to Masegosa or Agree-to-Disagree baselines (line 103). The paper then reports ν-ensemble + temperature scaling as yielding "the best calibration." For a fair comparison, temperature scaling should be applied to all methods or acknowledged as an uneven comparison. (That said, the primary ν-ensemble vs. standard ensemble comparison does not rely on temperature scaling, so this does not affect the paper's core empirical claim.)

- **No explanation for the absence of accuracy gains**: The paper notes in Limitations (line 153) that calibration improved but accuracy did not, calling this "counterintuitive." This is interesting but receives no discussion. A brief hypothesis (e.g., random-label fitting acts as a diversity-inducing regularizer that trades off sharpness for calibration without affecting the Bayes-optimal decision boundary) would strengthen the paper.

### Trivial

- **Proposition 2 assumes ensemble members "perfectly fit" the random labels** — a standard theoretical simplification for the sampling-with/without-replacement comparison. Not a problem for the analysis but worth noting for completeness.
- **The OOD evaluation uses CIFAR-10-C, which is a within-distribution covariate shift** — this is a standard benchmark and perfectly acceptable, but the paper could be more precise about the type of distribution shift being tested.

## Nice-to-Haves

- An ablation varying the unlabeled set size \(m\) for a fixed small training set (e.g., 1000 samples) to show how calibration changes as \(m\) grows.
- A sensitivity analysis for the unspecified balancing hyperparameter on at least one configuration.
- A brief discussion of why accuracy does not improve — offering a plausible mechanism would enrich the narrative.

## Removed Points

- **Criticism that "the bound cannot justify the random-label procedure" as a structural/fatal flaw**: The critic frames this as a "structural flaw that affects the paper's central argument." While the theory-alignment gap is real, it does not invalidate the paper's core empirical claim (that ν-ensembles improve calibration). The bound motivates diversity on unlabeled data; random labels are a practical heuristic. The paper should be more careful, but this is a Major weakness, not a Fatal one.

- **"Masegosa and Agree-to-Disagree are not designed for the same setting"**: This is not a valid weakness — it is standard to compare new methods against existing approaches on the same benchmarks regardless of what setting each was originally designed for.

- **Criticism that Proposition 2's "perfectly fit" assumption "may not generalize to real training"**: This is a deliberate theoretical simplification for comparing sampling schemes, standard practice in analytical derivations.

- **Strength from Strength Finder about the PAC-Bayes bound offering "principled justification"**: This conflicts with the verified weakness (theory-algorithm gap) and is therefore moved here per the rule that "when a strength and weakness disagree, the weakness wins."

## Novel Insights

Beyond the paper's own contributions, the most interesting signal from the reviews is the observation that the theory-algorithm gap in this paper is a recurring pitfall in ML: authors present a bound that involves a particular quantity (here, variance on unlabeled data using true labels), then design an algorithm that targets a related but different quantity (here, variance induced by random labels), and lean on the bound for justification. The paper would be stronger if it explicitly characterized this as "the bound suggests diversity on U is beneficial; random labels are a simple way to induce such diversity" rather than claiming the bound "guarantees" the result. This is a lesson that applies broadly.

## Suggestions

1. **Revise the abstract and Section 4**: Acknowledge that Theorem 1 applies when true labels are available on \(U\) and that the random-label procedure is a practical heuristic inspired by, but not directly guaranteed by, the bound. Tone down the language from "guarantees" to "motivates" or "is consistent with."
2. **Specify the exact training objective**: State the per-member loss function explicitly. Report the balancing hyperparameter values used across all experiments and include a sensitivity analysis for it.
3. **Add an ablation on unlabeled set size**: For a fixed small training set (e.g., 1000 samples), vary \(m\) (e.g., 1000, 2500, 5000, 10000) and show how calibration and accuracy change.
4. **Apply temperature scaling to all baselines** or remove the "best calibration" claim that depends on this asymmetric comparison.
5. **Add a brief hypothesis for why accuracy does not improve** — this would turn a noted limitation into a useful discussion point.

## Score and Decision

This paper presents a genuinely simple and effective method for improving ensemble calibration, with clean empirical results across multiple architectures, datasets, and distribution shifts. The main weaknesses — an overstated theoretical justification and an underspecified training objective — are significant but addressable. The method's practical value is clear. With revisions to clarify the theory-algorithm relationship and specify the missing experimental details, this paper would be a solid contribution.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>