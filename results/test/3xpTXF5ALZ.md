Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper studies *phishing attack localization* — jointly predicting whether an email is phishing and identifying the single most important sentence that explains why. The authors propose AI2TALE, an information-theoretic method that adds an information bottleneck penalty and a data-distribution random-masking mechanism on top of a mutual-information-based selector-classifier framework (L2X-style). The method operates in a weakly supervised setting (only vulnerability labels, no ground-truth phishing sentence annotations). Experiments on seven email datasets show consistent 1.5–3.5% combined improvement over five interpretable ML baselines (L2X, INVASE, ICVH, VIBI, AIM) on Label-Accuracy and Cognitive-True-Positive metrics.

## Strengths

- **Practical problem formulation with a realistic weak-supervision setting.** The paper correctly identifies that ground-truth phishing annotations are almost never available in real-world datasets (Section 3.1) and proposes a method that uses only vulnerability labels during training. This distinguishes the work from detection-only approaches and addresses a genuine practical constraint.

- **Clear motivation for two corrective components and their theoretical grounding.** The paper identifies two limitations of vanilla mutual-information training for sentence selection — superset selection (all sentences can be selected) and label-encoding-via-selection-patterns — and proposes principled solutions: (1) an information bottleneck term (−λI(X,Ẋ)) that penalizes selecting too many sentences (Eq. 5–7), and (2) a data-distribution mechanism that trains the classifier on random sentence subsets to prevent it from learning selection patterns rather than content (Eq. 9). Both are motivated by clear reasoning about what could go wrong.

- **Consistent empirical advantage over strong baselines on seven diverse datasets.** AI2TALE outperforms L2X, INVASE, ICVH, VIBI, and AIM on both Label-Accuracy and Cognitive-True-Positive across all seven datasets (Table 1), with combined-average improvements of 1.5–3.5%. The diversity of datasets (IWSPA-AP, Nazario, Miller Smiles, Cornell, Fraud, Cambridge, Enron) and the consistent direction of improvement strengthen the evidence.

- **Human evaluation provides real-user validation.** A survey of 25 university students and staff found 81% agreement (55% Agree, 26% Strongly Agree) that the top-1 selected sentence from AI2TALE would affect users' decisions (Figure 2). The study design blinded participants to the source of the sentences.

- **Commitment to reproducibility.** Source code and data are released at an anonymous repository, supporting verification and future work.

## Weaknesses

### Fatal
None.

### Major

1. **No ablation study to validate the claimed contributions.** The paper argues that two specific weaknesses of vanilla mutual-information training (superset selection and label-encoding-via-selection-patterns) are addressed by two specific components (the −λI(X,Ẋ) bottleneck and the data-distribution mechanism). Yet the experiments compare only the full AI2TALE against external baselines; no variant removes either component individually. Without ablations, the claimed improvements cannot be attributed to the proposed innovations — they could stem from hyperparameter tuning, the specific architecture choices, or implementation details. This is the single most significant gap, because the paper's main narrative (*these are the limitations → these are our solutions*) remains untested. At minimum, the authors should evaluate: (i) without the information bottleneck term, (ii) without the data-distribution mechanism, and (iii) without both (a "vanilla MI" baseline equivalent to L2X-style training with the same architecture).

2. **No simple baselines to establish lower bounds or quantify task difficulty.** The paper does not report performance of trivial selection strategies such as picking the first sentence, the longest sentence, a random sentence, or using the full email. Since all methods (including baselines) achieve near-perfect scores (≥97% on most metrics), the reader cannot assess whether the problem is intrinsically saturated (most phishing emails have obvious trigger sentences) or whether the 1.5–3.5% improvement is meaningful. If a random-sentence baseline already achieves 95%+ on these metrics, the claimed advantage shrinks considerably.

3. **No error bars, confidence intervals, or significance tests.** There is no mention of multiple independent runs, random seeds, or any measure of variance. Without this, the reader cannot distinguish systematic improvement from noise. This is especially important because the reported improvements (1.5–3.5%) are measured in a compressed performance range (97–100%), where small fluctuations could alter conclusions. The authors should report means and standard deviations over at least 5 independent runs and run statistical significance tests for the improvement over the best baseline.

### Minor

1. **Potential metric saturation is not discussed.** Both Label-Accuracy and Cognitive-True-Positive approach 99–100% for most methods on most datasets. The paper claims this is "substantial advancement" without acknowledging that the performance range is compressed. The authors should report the base rate (what percentage of randomly sampled sentences from phishing emails would contain cognitive triggers? what is the Label-Accuracy of a majority-class baseline?) and discuss whether the task is inherently near-saturated given the nature of phishing emails.

2. **Limited human evaluation.** The user study (25 participants, 10 emails) evaluates only AI2TALE's selections, with no comparison against selections from baseline methods. While the paper carefully blinded participants to the source, a side-by-side blind comparison (e.g., "which of these two sentences is more convincing?") would provide much stronger evidence that AI2TALE's explanations are preferable. As presented, the study shows that AI2TALE's selected sentences are perceived as convincing in absolute terms, but not that they are *better* than alternatives.

3. **Label-Accuracy measures self-consistency, not explanation quality.** The classifier used to evaluate Label-Accuracy is the same classifier trained jointly with the selector. The metric therefore measures whether the classifier can predict the label from its own selected sentence — a self-consistency check rather than an independent measure of explanation quality. While this is not wrong, the paper should acknowledge this limitation and consider complementing it with an independent evaluation (e.g., having human judges or a separate held-out classifier predict from the selected sentences).

4. **False-positive/negative analysis is anecdotal.** The paper reports a false-positive rate of 0.451% and false-negative rate of 0.899% (Section 4.4) but analyzes only one representative false-positive example qualitatively. A systematic breakdown of false predictions across datasets and comparison with baseline misclassification patterns would strengthen the analysis.

### Trivial
None.

## Nice-to-Haves

- Report full-email detection accuracy (using all sentences) alongside localization metrics to show whether the sentence-level selection degrades email-level phishing detection.
- Include a keyword-based phishing baseline (e.g., sentences containing "urgent," "verify your account," "click here") to ground performance in domain knowledge.
- Analyze per-dataset difficulty: discuss which datasets are easier/harder and why, to add depth beyond aggregate scores.
- Provide a deeper analysis of the selection mechanism: e.g., how often does the top-1 sentence overlap with expert judgments on a small gold-standard set?

## Removed Points

- *"Cognitive-True-Positive metric is not adequately defined or validated"* — The computation details are in the appendix (stripped by the parser). The main text cites relevant references and names the six cognitive principles. Per the hard rule on missing appendix content, this criticism is removed. The related concern about metric saturation is retained under Minor Weaknesses.
- *"Label-Accuracy metric needs precise operational definition"* — The paper states that the classifier f(Ẋ;β) takes the selected sentences as input and predicts the label (Section 3.2.1), and that Label-Accuracy measures whether the top-1 sentence predicts the vulnerability (Section 4.2). The description is adequate for a research paper; the reviewer appears to have overlooked these passages.
- *"Technical novelty appears incremental"* — This is a subjective assessment of novelty, not a factual or methodological weakness. The paper's combination of techniques, problem formulation, and application to a new domain constitutes a reasonable contribution for its class.
- *Missing related works* — Per the hard rule, this cannot be verified without external sources.

## Novel Insights

The reviews surface an interesting tension: the paper's two proposed components (bottleneck and data-distribution mechanism) are well-motivated theoretically and could in principle address known limitations of L2X-style feature selection, yet the evaluation does not test whether they actually deliver on their promise. This is a case where the strength of the conceptual framing (identifying limitations → proposing solutions) creates a higher burden of proof for the experiments, because the narrative demands evidence that each component does what it claims. The near-ceiling performance across all methods also raises the question of whether phishing sentence selection is simply an easier task than comparable feature-selection problems in other domains (e.g., sentiment analysis), which would change how impressive the results should be considered.

## Suggestions

1. **Run a three-way ablation** removing the bottleneck term and/or the data-distribution mechanism, and report the results in the same table format as the main comparison. This directly tests the paper's core narrative.
2. **Add three simple baselines**: (a) random sentence, (b) first sentence, (c) majority-class prediction. Report these alongside the main results.
3. **Report means and standard deviations** over at least 5 random seeds for all methods and datasets. Add a statistical significance test (e.g., paired bootstrap or McNemar's test) for the AI2TALE vs. best-baseline comparison.
4. **Report the cognitive-trigger base rate**: what percentage of randomly selected sentences from phishing emails in each dataset contain cognitive principles? This contextualizes the Cognitive-True-Positive scores.
5. **Expand the human evaluation** to include a blind side-by-side comparison between AI2TALE's top-1 sentence and the top-1 sentence from a baseline method (e.g., AIM, the strongest competitor).
6. **Acknowledge the self-consistency limitation of Label-Accuracy** and consider adding an independent evaluation (e.g., using an off-the-shelf phishing classifier to predict from selected sentences).

## Score and Decision

The paper addresses a worthwhile and under-studied problem with a method that is both well-motivated and consistently effective across diverse datasets. The proposed components (bottleneck and data-distribution mechanism) are grounded in clear reasoning about the limitations of prior work. The evaluation covers seven datasets and includes a human study.

However, the experimental evaluation has three structural gaps that prevent the paper from being accepted in its current form: (1) no ablation study to validate the claimed contributions against the identified limitations, (2) no simple baselines (random, first sentence) to establish lower bounds and contextualize the near-perfect scores, and (3) no error bars or significance tests to quantify variability. These are all addressable in a major revision, but as presented, the reader cannot assess whether the proposed technical components drive the improvement, whether the task is meaningfully difficult, or whether the gains are statistically reliable.

**Originality:** Moderate — novel combination of existing techniques applied to a new problem, with some original theoretical motivation.
**Importance:** Good — the problem of explainable phishing detection is practically important and under-studied.
**Claims support:** Weak — claims about the two corrective components are unsupported by ablation; claims of superiority lack statistical validation.
**Soundness:** Moderate — the method is sound, but the evaluation has significant gaps.
**Clarity:** Average — writing is verbose and some details are deferred to the appendix; main text is adequate but could be more concise.
**Value:** Potentially good — the dataset compilation, problem formulation, and open-source release would be valuable to the community if the evaluation gaps are filled.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>