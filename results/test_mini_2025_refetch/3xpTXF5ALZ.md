Now I have sufficient calibration data. Let me produce the consolidated review.

## Summary

The paper proposes AI2TALE, a deep learning framework for phishing attack localization that predicts whether an email is phishing or benign while automatically identifying the single most important sentence that caused the classification. The method operates in a weakly supervised setting (using only email-level vulnerability labels, not sentence-level annotations) and combines three components: mutual information maximization between selected sentences and the label, an information bottleneck penalty to avoid selecting too many sentences, and a data-distribution mechanism to prevent the classifier from overfitting to the selection network. Experiments on seven real-world email datasets with five interpretability baselines are presented alongside a human evaluation.

## Strengths

- **Information bottleneck penalty addresses a known limitation of MI-based selection.** The paper identifies that maximizing mutual information between the selected subset $\tilde{X}$ and label $Y$ has no inherent penalty against selecting all sentences. Adding a term minimizing $\mathbf{I}(X,\tilde{X})$ (Eq. 4) with a closed-form upper bound (Eq. 7) that encourages sparse selection is a well-motivated adaptation of information bottleneck theory, going beyond methods like L2X that lack such a sparsity mechanism.

- **Data-distribution mechanism targets classifier overfitting to the selector.** The paper identifies that the classifier may learn to rely on the *identity* of selected features rather than their content, and proposes training the classifier separately with random Bernoulli masks (Eq. 9). This design, inspired by Jethani et al., is adapted to address a specific and plausible failure mode of joint selection-classification training.

- **Evaluation across seven diverse real-world datasets with multiple baselines.** The paper tests on seven email datasets (IWSPA-AP, Nazario, Miller Smiles, Phish Bowl Cornell, Fraud emails, Cambridge, Enron) and compares against five intrinsic interpretability baselines (L2X, INVASE, ICVH, VIBI, AIM). This scope of evaluation is substantially broader than many interpretability papers.

- **Human evaluation provides qualitative evidence.** A survey with 25 participants from diverse backgrounds found 81% agreed/strongly agreed that AI2TALE's top-1 selected sentences would affect users' decisions, providing independent evidence beyond automated metrics that the selected sentences are subjectively meaningful.

## Weaknesses

### Major

- **Label-Accuracy evaluation does not specify which classifier is used.** The paper defines Label-Accuracy as measuring "if this sentence can effectively predict the email's vulnerability" (Section 4.2) but never states whether each method's own classifier is used or a fixed classifier. If each method uses its own classifier, the metric conflates selection quality with classifier quality — a method with a better classifier but worse selection could score higher. Since the paper's central claim is about superior *selection*, this ambiguity is a structural concern. The baseline methods (L2X, INVASE, etc.) are intrinsic interpretability models with their own classifiers, making it unclear whether improvements come from better selection or better classification.

- **No ablation study isolating the three components.** The method has three trainable components: (i) MI maximization, (ii) the information bottleneck penalty (controlled by $\lambda$), and (iii) the data-distribution mechanism (Eq. 9). The paper presents no ablation showing the contribution of each piece. Without this, it is impossible to tell which components drive the performance gain, whether simpler variants (e.g., only MI + bottleneck) would work equally well, or whether the data-distribution mechanism is beneficial. Given that the method combines elements from L2X, VIBI, and Jethani et al., ablation is essential to demonstrate that the specific combination is effective.

- **No statistical significance or variance reporting.** All results in Table 1 are point estimates with no standard deviations, confidence intervals, or significance tests. At accuracy levels above 97%, a 1.4-percentage-point improvement over the best baseline could easily fall within one standard deviation. The paper does not report multiple runs with different random seeds. This omission is critical given the ceiling-level performance and small absolute differences.

### Minor

- **Human evaluation lacks comparison to baselines.** The human evaluation presents only AI2TALE's top-1 sentences; participants have no basis for comparison. The 81% agreement rate shows AI2TALE selects persuasive sentences, but does not demonstrate it selects *better* sentences than existing methods. A side-by-side comparison with at least one baseline would be needed to support claims of superiority.

- **Cognitive-True-Positive is a keyword-matching proxy.** The metric checks whether selected sentences contain keywords from predefined cognitive-trigger lists (Reciprocity, Scarcity, etc.). This is a bag-of-words heuristic that can reward sentences containing keywords like "urgent" or "limited time" even if they are not the actual phishing trigger. The paper does not validate whether this metric correlates with human judgments of phishing relevance.

- **The "disjointly" training description is imprecise.** Algorithm 1 updates the classifier $\beta$ twice per iteration — once with random masks $\mathbf{r}$ (step 4) and once with selection-network $\mathbf{z}$ (step 5). Since both updates use the same parameters $\beta$, describing the data-distribution training as "disjoint" (Section 3.2.2) is misleading; the classifier is trained jointly on both signals. The practical effect may be similar, but the terminology needs clarification.

- **The claimed 1.5%–3.5% improvement range is presented without context.** The 3.5% improvement compares AI2TALE to the *worst* baseline (VIBI at 95.82%), while the improvement over the best baseline (AIM/INVASE at 97.75%) is approximately 1.4 percentage points (or ~1.4% relative). Presenting the range as 1.5%–3.5% without clarifying that one end of the range refers to the weakest competitor is potentially misleading.

### Trivial

None.

## Nice-to-Haves

- A simple baseline that always picks the first sentence, the last sentence, or the sentence with the highest phishing-keyword density would calibrate whether 99% Label-Accuracy is genuinely impressive or merely reflects easy dataset characteristics.
- A sensitivity analysis for the information bottleneck weight $\lambda$ (a plot of performance vs. $\lambda$) would be expected for a method relying on this hyperparameter.
- Reporting per-class accuracy and precision/recall for the phishing class would address potential class-imbalance concerns across the seven datasets.

## Removed Points

These points were considered but removed from the main review for the reasons given:

- **FPR/FNR inconsistency (Harsh Critic, Point 6):** The critic claims the reported FPR (0.451%) and FNR (0.899%) are inconsistent with the paper's framing and "suspiciously strong." This is speculative — the numbers are internally consistent with each other and with the reported Label-Accuracy (the total error rate depends on class distribution). The benign email example in Table 2 is simply one false positive; a low FPR does not imply zero false positives. No actual inconsistency exists in the paper's data.
- **Missing related works citations:** Removed per instructions (cannot confirm without external sources).
- **Missing appendix content, hyperparameters, proofs:** Removed per instructions (appendix stripped by parser; content exists in original submission).
- **Formatting, typographical, and presentation nitpicks:** Removed per instructions as parser artifacts or minor presentation issues.
- **Generic scope-creep criticisms** (e.g., "add more models," "larger dataset," "user study"): These are nice-to-haves, not genuine weaknesses given the paper's scope.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the Label-Accuracy evaluation protocol.** State explicitly whether a fixed classifier is used across all methods, or report results both with each method's own classifier and with a fixed classifier. This is the single highest-leverage improvement for resolving the paper's most significant ambiguity.

2. **Add an ablation study.** Report Label-Accuracy and Cognitive-True-Positive for: (a) full AI2TALE, (b) without the information bottleneck term ($\lambda=0$), (c) without the data-distribution mechanism, and (d) without both. This would demonstrate that the novel components contribute to the claimed advantage.

3. **Report variance and significance.** Run each method 5–10 times with different random seeds and report mean ± standard deviation. Include a significance test (e.g., paired bootstrap) comparing AI2TALE to the best baseline. This is essential given the small absolute improvements at ceiling-level performance.

---

**Score Calibration Details:**

**Round 1 (bracketing):** Three calibration searches on "phishing detection email deep learning localization explainability" anchored the score bands:
- Weak (score < 3.5): Anchors at avg 3.00, 3.00, 2.50, 3.00 — papers with fatal evaluation flaws (no baselines, anecdotal evidence only).
- Middle (3.5–7.5): Anchors at avg 4.67, 6.75, 6.25, 6.20 — papers with mixed evaluation quality.
- Strong (score > 7.5): Anchors at avg 8.00, 8.00, 8.00, 9.50 — papers with thorough evaluation and clearly novel contributions.

Initial bracket: **4.0 – 5.5**.

**Round 2 (narrowing):** Searched on "interpretable feature selection mutual information information bottleneck" within (4.5, 6.0) and (3.0, 4.8):
- INqLJwqUmc (avg 5.25, accepted poster): Information bottleneck for multimodal interpretability. Similar evaluation gaps (no statistical tests, limited ablation) but stronger theoretical contribution. The AI2TALE paper has broader evaluation (7 datasets vs 3, plus human eval) but weaker theoretical novelty and the additional ambiguity in Label-Accuracy. AI2TALE is slightly weaker than this anchor.
- TIjBKgLyPN (avg 5.50, reject): SAE methods for interpretability. Not directly comparable.
- CxwtuhU40F (avg 5.60, reject): Interpretable dimensionality reduction. Not directly comparable.
- FwlM1k4ODx (avg 4.25, reject): Information bottleneck in classifiers. Marginal improvements, lacking analysis. AI2TALE is stronger — clearer problem, broader evaluation, human study.
- w10KdRwcMk (avg 4.25, reject): Revisiting variational IB. Unclear novelty, weak experiments. AI2TALE is stronger.
- xtTut5lisc (avg 5.0, reject): Feature space optimization. Comparable evaluation breadth but presentation issues. AI2TALE is comparable but has different weaknesses.

**Final score: 4.5.** The paper addresses an important problem with a well-motivated method, and the evaluation is reasonably broad in terms of datasets and baselines. However, the absence of ablation, lack of statistical significance testing, and ambiguity in the Label-Accuracy metric are significant gaps that leave the central claims less than fully supported. The paper is below the acceptance threshold in its current form but could be strengthened to reach it with targeted revisions addressing these issues.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>