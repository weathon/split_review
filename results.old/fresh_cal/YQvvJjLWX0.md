## Summary

This paper proposes Semantic Entropy Probes (SEPs), linear classifiers trained on LLM hidden states to predict semantic entropy — a measure of model uncertainty over meanings. SEPs aim to combine the test-time efficiency of probing methods (single forward pass) with the robustness of sampling-based uncertainty quantification. The main empirical finding is that SEPs generalize substantially better to out-of-distribution (OOD) tasks than probes trained to directly predict accuracy, with OOD improvements of +2.2 to +10.5 AUROC points across 6 model–generation-length settings. The paper additionally shows that semantic entropy can be predicted from hidden states *before* any tokens are generated (TBG token), and provides a sanity-check experiment showing SEP predictions track ground-truth SE when a question is made easier by adding context.

---

## Strengths

- **SEPs reduce the inference cost of semantic uncertainty to a single forward pass.** Unlike semantic entropy (SE), which requires 5–10 model generations per query, SEPs train a linear probe on the hidden states of a single generation and make predictions at test time without additional sampling. This is a clean, practical contribution and is clearly supported (Section 4, "do not require sampling multiple responses from the model at test time").

- **SEPs generalize substantially better than accuracy probes to held-out tasks.** Table 2 reports the average AUROC difference (SEP minus accuracy probe) across 6 model–generation-length settings: all positive, from +2.2 to +10.5 percentage points. Figure 6 (right panel) visualizes this gap consistently favoring SEPs on BioASQ, NQ Open, SQuAD, and TriviaQA in the leave-one-out protocol. This is the paper's core empirical contribution and is well supported.

- **Semantic entropy can be predicted from hidden states *before* generating any output tokens (TBG position).** Figures 2 and 3 show AUROC values for the token-before-generation position reaching 0.7–0.9 in later layers. This is a stronger efficiency claim than the SEP setup itself — it enables uncertainty quantification in a single forward pass, without even generating a response.

- **Counterfactual context-addition experiment confirms SEPs capture genuine SE rather than spurious correlations.** Figure 5 shows the predicted high-SE probability distribution shifts from ~0.9 (no context) to ~0.2 (with context), tracking the ground-truth SE drop, despite the probe never being trained on inputs with context. This is a strong sanity check.

- **Systematic ablations across 5 models, 4 datasets, multiple layers, and two token positions (SLT and TBG).** Results cover Llama-2-7B, Llama-2-70B, Llama-3-70B, Mistral-7B, and Phi-3; short-form and long-form generation; in-distribution and OOD settings. The consistent upward trend in later layers supports the claim that hidden states encode semantic uncertainty.

---

## Weaknesses

### Fatal
None.

### Major

- **Generalization evaluation is limited to closed-book QA datasets.** The leave-one-out protocol uses TriviaQA, SQuAD, BioASQ, and NQ Open — all factual QA datasets of similar character. The paper's core claim that SEPs "generalize better to out-of-distribution data" and "generalize better to new tasks" is supported only within this single task family. Whether the finding transfers to free-form generation settings (e.g., biography generation, summarization, instruction following, dialogue) — where hallucinations are most practically concerning — remains untested. The paper acknowledges this scope only implicitly in the future-work section ("we relied on established QA tasks to train SEPs") but does not candidly state it as a limitation of the current evidence. This does not invalidate the results, but it narrows the breadth of the contribution claimed.

### Minor

- **No confidence intervals or significance tests for the OOD AUROC comparisons.** Tables 1 and 2 report standard errors computed *across tasks* (N=4 datasets), which captures task variance but not variance from train/test splits or probe initialization. The paper does not report whether the SEP-vs-accuracy-probe gaps are statistically significant (e.g., via bootstrapping or paired tests), making it difficult to judge reliability on individual tasks. Given the consistency of the positive trend this is unlikely to change the conclusion, but it would strengthen the presentation.

- **The "hallucination detection" framing conflates hallucination with factual incorrectness.** The evaluation uses model accuracy (match to ground-truth answer) as the gold standard. This is a standard practical proxy used by prior work, but the paper should be more precise: it detects *factual incorrectness*, not hallucinations in the broader sense of faithfulness to a source. This is a terminological looseness shared with much of the literature but worth noting.

- **Binarization threshold selection procedure could be more clearly scoped.** The threshold γ* is chosen on the training set by minimizing within-cluster variance (Eq. 4). While the evaluation is on held-out data (no leakage), the paper does not discuss whether the threshold is stable across training splits, or whether a separate validation set for threshold selection would change results. The reference to soft-labelling comparisons (deferred to appendix) suggests this was explored, but the main text leaves the reader uncertain.

### Trivial
None.

---

## Nice-to-Haves

- **Evaluate SEPs on a genuinely different task family** (e.g., FactScore biography generation, summarization faithfulness) to substantiate or delineate the generalization claim. This is the single most valuable extension and would transform a solid finding into a broadly impactful one.

- **Report SEP prediction quality on continuous (non-binarized) SE** — e.g., MSE or Spearman correlation between predicted probabilities and raw SE on held-out inputs. The paper trains SEPs on binarized labels but the logistic regression outputs probabilities that could be evaluated against continuous SE, which would provide direct evidence that hidden states encode fine-grained uncertainty rather than only a binary threshold.

- **Plot SEP performance as a function of training set size** to help practitioners understand the data requirements for the OOD advantage to materialize.

---

## Removed Points

*These points were flagged for removal; treat with caution if reading this section.*

1. **"AUROC on binarized SE is circular"** — The reviewer claimed evaluating SEPs on binarized SE is circular because SEPs were trained to predict binarized SE. This is incorrect: the evaluation is on held-out test data (different splits or datasets), making it a standard, non-circular supervised learning evaluation. **Removed: factually wrong.**

2. **"Cost framing underspecifies training cost"** — The reviewer argued the abstract's "almost zero" overhead could be misinterpreted. The paper is clear throughout that training requires SE computation (Section 4: "we sample N=10 responses... and compute semantic entropy"). The cost claim is about test-time overhead. **Removed: the paper already addresses this distinction.**

3. **"State-of-the-art claim is underspecified"** — The reviewer asked "cost-efficient relative to what?" The paper's context (comparing to accuracy probes, sampling-based SE, naive entropy) makes the comparison clear. **Removed: strawman.**

4. **"L2 regularization tuning could improve results"** — This is pure speculation without evidence that the default scikit-learn settings are suboptimal. **Removed: unsupported speculation.**

5. **"Chain of approximations bias not discussed"** — The paper explicitly describes each approximation: Monte Carlo sampling, discrete SE variant, and binarization. Discussing potential biases would add rigor but is not a weakness of the current content. **Removed: not a concrete weakness; moved to nice-to-have framing.**

6. **"What range of γ is searched"** — This is a practical detail likely found in the appendix (which was stripped by the parser). **Removed: parser artifact.**

7. **"The binarization uses a principled objective" (from Strength Finder)** — This is a description of a design choice, not a genuine strength. It does not constitute evidence supporting the paper's contributions. **Removed: not a substantive strength.**

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

- Add a candid limitations paragraph explicitly scoping the generalization results to QA-style factual tasks and discussing expected behavior in free-form generation.
- Report bootstrapped confidence intervals or significance tests for the key OOD AUROC differences in Table 2.
- Consider adding one experiment on a non-QA generation task (e.g., biography generation with FactScore or summarization faithfulness) to directly test the generalization claim outside the current task family.

---

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>