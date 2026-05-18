I have thoroughly verified each claim against the paper. Now let me produce the final consolidated review.

---

## Summary

This paper proposes QueRE, a method that extracts "black-box representations" from LLMs by querying the model with a fixed set of ~50 elicitation questions (e.g., "Do you think your answer is correct?") and using the probabilities of "yes"/"no" responses as feature vectors. A linear probe trained on these low-dimensional features is applied to three tasks: (1) predicting instance-level correctness of LLM generations, where QueRE often matches or exceeds white‑box probes using hidden states or full vocabulary logits; (2) detecting adversarially prompted models (e.g., GPT-3.5 with a system prompt to answer incorrectly); and (3) distinguishing between different model architectures and sizes (e.g., LLaMA2-7B vs. 13B vs. 70B) in a fully black‑box manner. The paper also studies sampling-based approximations for APIs that do not provide token probabilities, and reports an interesting finding that even random sequences of natural language yield informative features.

---

## Strengths

1. **Novel black-box representation extraction with strong empirical performance on multiple tasks.** The core idea—using the LLM's own probability distribution over responses to elicitation questions as features—is creative and practical. On adversarial detection (Figure 5) and architecture/size discrimination (Figure 4), QueRE achieves near-perfect AUROC (~0.97–0.99), convincingly outperforming all baselines including confidence scores, answer probabilities, and semantic uncertainty. These results are clean, well-evidenced, and independent of the white-box comparison debate.

2. **Adversarial detection and model identification in a fully black-box setting.** QueRE reliably detects adversarially influenced GPT-3.5 (both direct "answer incorrectly" prompts and subtle code-bugging prompts, Table 2) and distinguishes between model architectures/sizes with near-perfect accuracy—tasks where all other black-box baselines (confidence scores, answer probabilities, semantic uncertainty) perform at or near chance. This is the paper's strongest empirical contribution and has clear practical value for API monitoring.

3. **Useful ablation studies revealing robustness.** The sampling ablation (Figure 7) shows that replacing true token probabilities with as few as 10 MC samples drops performance by less than 2 AUROC points, which is practically valuable. The finding that random sequences of natural language can be nearly as informative as carefully designed elicitation questions (Table 4) is genuinely surprising and raises interesting questions about what these features capture—though the paper could explore this further.

4. **Well-calibrated predictors.** QueRE-based predictors exhibit substantially lower expected calibration error than answer-probability baselines (Figure 6), which is important for high-stakes applications where confidence calibration matters.

---

## Weaknesses

### Fatal
None.

### Major

1. **White-box comparison is confounded by dimensionality mismatch.** QueRE uses ~50 features while the white-box baselines (RepE ~4096 hidden-state dimensions; Full Logits ~50k vocabulary dimensions) operate in much higher-dimensional spaces. A linear probe trained on 5000 samples with 4096+ features is at serious risk of overfitting without strong regularization, whereas the ~50-feature QueRE probe is not. The paper does not report whether any regularization (L1/L2) was applied to the baselines, whether hyperparameters were tuned, or whether dimensionality reduction (e.g., PCA to match QueRE's dimension) was attempted. This makes it impossible to tell whether QueRE genuinely extracts *more informative* features than white-box representations, or simply benefits from a more favorable feature-to-sample ratio. The headline claim that QueRE "can often outperform white-box linear predictors" is therefore not adequately supported by the experimental design. The claim should either be reframed or the comparison should be controlled (via regularized probes and/or PCA-reduced baselines).

   *Verification: Paper lines 80–82 describe RepE as using "the hidden state of the LLM at the last token position" and Full Logits as using "the distribution over the LLM's entire vocabulary." No mention of regularization, hyperparameter tuning, or dimensionality reduction for these baselines appears anywhere in the paper (confirmed via grep for "regulariz" — no matches).*

### Minor

2. **Abstract overclaims a GPT-3.5 vs. GPT-4 experiment that is not conducted.** The abstract states that QueRE enables "identifying if GPT-3.5 is supplied instead of GPT-4." The experiments in Section 4.2 (Figure 4) only distinguish between different sizes of LLaMA2 and Mistral models; no GPT-3.5 vs. GPT-4 experiment is performed. While the general capability to distinguish model architectures is demonstrated, the specific example is an overclaim and should be corrected to match the actual evidence.

   *Verification: Abstract line 4 explicitly mentions this example. Section 4.2 experiments (Figure 4 caption, lines 77–78, 102–104) only cover LLaMA2 sizes and Mistral models.*

3. **Proposition 1's convergence rate appears suspect.** The claimed rate \(O(1/\sqrt{n} + \sqrt{n}/k)\) is unusual: for fixed \(k\), the \(\sqrt{n}/k\) term grows with \(n\), implying that adding more labeled data *increases* the error bound—which is the opposite of what one expects. Standard covariate measurement error results for logistic regression typically yield rates like \(O(1/\sqrt{n} + 1/\sqrt{k})\) or \(O(1/\sqrt{n} + 1/k)\). The derivation is only sketched in two sentences and is not convincing. Since the empirical results (Figure 7) already convincingly demonstrate that sampling works well, this theory neither adds value nor is clearly correct. The authors should either provide a full derivation or remove the proposition.

   *Verification: Lines 64–66 state the proposition and the sketch. The rate is presented as \(O(1/\sqrt{n} + \sqrt{n}/k)\).*

4. **Missing error bars on main results.** Figures 2, 3, 4, and 5 (the primary bar plots) do not report any measure of variability. Only Figure 7 (sampling ablation) mentions "over 5 random seeds" and Figure 8 shows shaded standard error. Without error bars, it is impossible to assess whether QueRE's improvements over baselines are statistically significant.

   *Verification: The captions and text for Figures 2–5 contain no mention of error bars, standard deviations, or random seeds. Figure 7 explicitly states "over 5 random seeds."*

5. **Training set sizes differ without justification.** Open-source models use 5000 training instances while GPT models use only 1000 (line 90). No explanation is provided for this discrepancy. The smaller GPT training set could favor QueRE if the high-dimensional baselines benefit more from additional data.

6. **Hyperparameter details for linear models are omitted.** The paper does not report regularization type/strength, solver, or any cross-validation procedure for the linear probes. While this is a common omission, it matters here because the white-box comparison's validity hinges on whether those probes were properly regularized.

7. **Table 3 (generalization bounds) lacks context.** The table presents bounds on accuracy but does not specify what bound is being computed (e.g., which PAC-Bayes or Rademacher bound), how tight it is relative to empirical accuracy, or what assumptions it relies on beyond a brief mention of independence. As presented, the table is uninformative.

8. **Calibration comparison is incomplete.** Figure 6 compares QueRE's ECE only against Answer Probs, not against RepE, Full Logits, or Semantic Uncertainty. Including these baselines would make the calibration claim more convincing.

### Trivial
- The statement that the paper "does not discuss" implications of the random sequences finding is slightly overstated by the critic — the paper does briefly address this in the discussion (line 187–188), albeit not deeply. The point that this could be explored further is fair but minor.

---

## Nice-to-Haves

- **Controlled white-box comparison**: As noted in Weakness #1, comparing QueRE against (a) regularized linear probes on white-box features and (b) probes on PCA-reduced white-box features (matched to QueRE's dimension) would cleanly resolve the dimensionality confound.
- **Cost/benefit analysis**: A practical analysis showing how few elicitation questions (or random sequences) are needed for strong performance would strengthen the practical case.
- **Clean accuracy reporting for adversarial detection**: Table 2 could report each method's accuracy on clean prompts to confirm that the methods behave normally when no bug insertion is instructed.

---

## Removed Points
These points are flagged to be removed; treat them with caution.

None applicable — all criticisms from the reviewers that were factually accurate and substantive have been retained in the Weaknesses section above (with appropriate severity downgrades where warranted).

---

## Novel Insights

The most interesting observation not foregrounded by the paper's own framing is that *random sequences of language* produce features nearly as predictive as curated elicitation questions. This finding, if robust, suggests that QueRE is not primarily capturing the LLM's *self-assessment* or *introspective* capabilities (as the "elicitation question" framing implies), but rather measuring a more diffuse statistical signature of the model's output distribution — possibly related to overall uncertainty, entropy, or output distribution shape. The paper acknowledges this briefly but does not explore the implications for interpretability, which is a missed opportunity. If QueRE works because any perturbation of the conditioning context reveals distributional information, the method could potentially be simplified and its mechanism better understood.

---

## Suggestions

1. **Reframe the white-box comparison** to acknowledge the dimensionality confound honestly, or add controlled experiments with regularized/PCA-reduced baselines.
2. **Correct the abstract** to remove the untested GPT-3.5 vs. GPT-4 example, or add that experiment.
3. **Either fully derive or remove Proposition 1** — the sketch is not convincing and the rate is questionable.
4. **Add error bars** to all main figures, at minimum over a small number of random seeds or bootstrapped confidence intervals.
5. **Justify or equalize the training set sizes** between open-source and GPT models.
6. **Report hyperparameters** (regularization, solver) for all linear models.

---

## Score and Decision

This paper introduces a genuinely novel and practical method for extracting black-box features from LLMs. The core contributions — adversarial detection and model identification in a fully black-box setting — are convincingly demonstrated and have clear practical utility. The finding about random sequences is interesting and potentially important. However, the central claim of outperforming white-box methods is undermined by an uncontrolled comparison that conflates feature dimensionality with informativeness, and the abstract overclaims an experiment that was not run. The theoretical result is questionable and adds no value. None of these issues are fatal — they are all fixable with additional experiments, reframing, or removal — but they do detract from an otherwise solid empirical paper.

Given that the paper's strongest contributions (adversarial detection, architecture discrimination, sampling robustness) stand independently of the white-box comparison debate, and given the novelty of the approach, I lean toward acceptance pending revisions.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>