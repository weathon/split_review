- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 5, 6
Now I have a thorough understanding of the paper. Let me synthesize the consolidated review.

---

## Summary

This position paper argues that No Free Lunch (NFL) theorems are practically irrelevant for real-world machine learning because both real-world data and neural network models share a preference for low Kolmogorov complexity. The paper presents: (1) a Kolmogorov-style NFL theorem linking incompressibility to learning impossibility, (2) compression experiments showing real datasets are compressible, (3) PAC-Bayes bounds demonstrating that CNNs' simplicity bias explains their generalization even on non-image tabular data, (4) experiments showing GPT-3 and even randomly initialized language models assign exponentially higher probability to low-complexity sequences, and (5) arguments for how model selection and single-model-at-all-sizes are feasible under simplicity biases.

## Strengths

- **GPT-3 and randomly-initialized LM experiments (Sections 3.3–3.4).** The paper carefully constructs expression trees to measure Kolmogorov complexity of sequences, then shows that GPT-3's log-probability decays exponentially with sequence complexity, with larger models showing stronger effects. The finding that even *randomly initialized* GPT-2 models generate sequences with significantly lower Kolmogorov complexity than uniform (with a hypothesis test on 100,000 samples) is a genuinely interesting result that directly supports the claim that simplicity bias is architectural, not just learned.

- **Connecting NFL theorems to Kolmogorov complexity (Theorem 1, Section 2.2).** Theorem 1 formalizes why NFL theorems are irrelevant for real data: if labels are incompressible (uniformly random), no bounded-complexity classifier can beat random chance, but real labels are compressible. This provides a clean complexity-theoretic framing of why the NFL's uniform-distribution assumption is the source of its seemingly dire conclusion.

- **PAC-Bayes bounds for CNNs on tabular data (Section 3.2, Figure 1 right).** The paper demonstrates that PAC-Bayes bounds using a universal prior nearly match the test error of CNNs trained on tabular data encoded as images. Even without baseline comparisons, this is a novel empirical demonstration that the simplicity bias of a vision architecture is sufficient to explain its generalization on non-vision domains — supporting the paper's central thesis that simplicity bias is broadly applicable.

- **Model selection bound (Section 4.1).** The calculation showing that cross-validation over 100 million models with a 20,000-point validation set yields a test error gap <3.4% with >99% probability is a clean, concrete refutation of the concern that benchmark overfitting from comparing many models is a serious problem, and it provides a theoretical explanation for the findings of Recht et al. (2019).

## Weaknesses

### Fatal

None.

### Major

None. The paper's core thesis is well-supported by multiple lines of evidence; the weaknesses below are about framing and presentation, not fundamental errors.

### Minor

- **Overstated novelty of Theorem 1 and contributions list.** The paper claims a "new no free lunch theorem" (contributions, line 29), but Theorem 1 is a straightforward implication of the relationship between cross-entropy and Kolmogorov complexity (Eq. 1): if labels are incompressible (high K(Y|X)), no bounded-complexity classifier can achieve low cross-entropy. This follows from basic information-theoretic reasoning and does not yield a genuinely new insight beyond what is implicit in the standard NFL — the value is in the *framing*, not in the theorem itself. The paper's contribution list also claims "the first cross-domain PAC-Bayes generalization bounds" which, as discussed below, is somewhat aspirational. The paper is strongest when read as a synthesis/position paper; it would benefit from adjusting the contribution claims to match this framing.

- **The "cross-domain" PAC-Bayes claim lacks baseline comparisons.** The paper claims that CNNs generalize on tabular data (Section 3.2, Figure 1 right) and that this is explained by simplicity bias. However, no test accuracy numbers or baseline comparisons (e.g., MLP, XGBoost, linear model) are provided for the tabular datasets. The PAC-Bayes bound nearly matching the test error shows the simplicity-bias *explanation* fits, but without knowing whether the CNN performs *well* in absolute terms or relative to simpler alternatives, the significance of this result is unclear. The bound could match a poor test error and still be technically correct. The paper would be substantially strengthened by reporting test accuracy and comparing to reasonable baselines.

- **Randomly initialized LM experiments report only p-values, not effect sizes.** Section 3.4 reports rejecting the null hypothesis with "an extremely low p-value" for the hypothesis test comparing Kolmogorov complexity of sequences from random LMs vs. uniform, using 100,000 samples per condition. With such a large sample size, even trivially small differences achieve statistical significance. Without reporting effect sizes (e.g., the mean difference in Kolmogorov complexity between conditions, or the full distribution), the practical magnitude of the simplicity bias remains unclear. This is addressable in a rebuttal.

- **The paper claims that "architectures designed for a particular domain... can compress datasets on a variety of seemingly unrelated domains" (abstract)** but the compression experiments (Figure 1 left) use MLPs on tabular data — MLPs are not "designed for a particular domain" in the way that CNNs are designed for vision. The CNN compression experiments are on CIFAR images (their native domain). Only the PAC-Bayes experiment (Figure 1 right) truly tests a vision architecture on non-vision data. The abstract's phrasing creates an expectation that is not fully met by the experiments as presented.

### Trivial

- **Pagination of Figure 1.** The figure is placed as a float, making it unclear from the main text which datasets are tabular vs. which are images across the three panels. A callout in the text clarifying "left panel = MLPs on tabular, middle = CNNs on images, right = CNNs on tabular" would help.

- **Section numbering inconsistency.** The paper's contributions mention "cross-domain PAC-Bayes bounds" but this is presented in Section 3.2, not a separately numbered section. Minor organizational clarity issue.

## Nice-to-Haves

- For the GoogLeNet/ViT convex combination experiment (Section 4.2), it would be interesting to see the performance of a *single* flexible architecture trained with complexity regularization from scratch, rather than a post-hoc combination of two separately-trained models. The paper acknowledges this is a "demonstration of principle" (per the harsh critic's apt description), but further evidence would strengthen the claim.

- The discussion of transformers' limitations (Section 5, final subsection) is thoughtful but somewhat disconnected from the rest of the paper. Integrating this into the main argument about the role of simplicity bias would improve narrative flow.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"No test accuracy numbers are reported for tabular datasets"** (Harsh Critic, Weakness 1). The paper explicitly states "we show the generalization bounds on these models along with test error in Figure 1 (right)" (line 136) and the figure caption confirms test error is shown. The test error is visually presented in the figure, so this specific sub-claim is factually incorrect.

- **"Mode collapse" concern for random LMs** (Harsh Critic, Weakness 3). The claim that the observed simplicity bias "could be due to the model's failure to produce diverse outputs (e.g., mode collapse) rather than a structured simplicity bias" does not actually contradict the paper's thesis. If the model produces repetitive (low-complexity) sequences, that *is* a preference for low complexity. The paper's claim is about the outcome (preference for low-complexity sequences), not the mechanism. The mode-collapse explanation would support, not undermine, the paper's claim.

- **"Conflating compression of labelings with low-complexity bias of the model"** (Harsh Critic, Weakness 4). The paper clearly separates evidence for *data complexity* (Section 2: compression experiments showing datasets are compressible) from evidence for *model bias* (Section 3: GPT-3 and random LM experiments showing models prefer low complexity). The PAC-Bayes bound in Section 3.2 uses the universal prior over hypotheses — this is a legitimate way to connect compression to generalization via the model's simplicity bias, not a conflation. The paper's structure is logically coherent on this point.

- **Generic strengths** from the Strength Finder (e.g., "meta-learner selection bound with 100 million models" and "single learner effective across sample sizes" as *core* strengths). These are better classified as supporting evidence rather than primary contributions. They are retained in the summary above but at lower prominence.

## Novel Insights

None beyond the paper's own contributions. The reviews largely agree on the paper's contributions and weaknesses, with the primary tension being whether the novelty is overstated — a framing issue rather than a factual dispute. The harsh critic's observation that the paper would benefit from being "transparently presented as a synthesis with illustrative experiments" rather than claiming novel technical contributions is the most useful insight for improving the paper.

## Suggestions

1. **Add baseline comparisons** for the CNN-on-tabular experiment (MLP, XGBoost, logistic regression) and report absolute test accuracy. This would clarify whether the PAC-Bayes bound is explaining good, mediocre, or poor performance.

2. **Report effect sizes** (mean difference in Kolmogorov complexity, distribution plots) for the random LM hypothesis test, not just p-values.

3. **Reframe the contribution claims** to better match the paper's nature as a position paper / synthesis. Rather than claiming "a new no free lunch theorem," describe Theorem 1 as "a Kolmogorov-complexity reformulation of the NFL theorem that clarifies its assumptions" — this is accurate and avoids overclaiming.

4. **Clarify the "cross-domain" terminology** — the paper uses it to mean "architecture designed for one domain applied to another." Adding a brief definition (as done for other terms) would prevent confusion.

5. **Make the abstract more precise** about which experiments use domain-specific vs. domain-general architectures (e.g., clarify that the MLP compression experiments do not demonstrate domain-architecture mismatch).

---
