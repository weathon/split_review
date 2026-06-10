## Summary

This paper formalizes uncertainty estimation for LLMs as a supervised regression task where a random forest is trained to predict response quality (scores derived from Rouge-1/BLEU/accuracy) using features extracted from a "tool LLM" processing the prompt+response jointly. The key idea is that the tool LLM need not be the same model that generated the response, enabling three regimes: white-box (Wb-S, same model), grey-box (Gb-S, entropy/probability features only), and black-box (Bb-S, a different open LLM provides features for a black-box target). Results across QA, multiple-choice, and machine translation tasks show consistent AUROC improvements over unsupervised baselines, with the Bb-S regime achieving up to 0.925 on TriviaQA for LLaMA2-7B (vs. best unsupervised baseline at 0.773). OOD transfer experiments across MMLU subject groups and QA datasets show the approach retains most of its advantage under distribution shift.

## Strengths

- **Tool-LLM abstraction enabling black-box uncertainty estimation.** The paper identifies that any white-box LLM can process (x, y) jointly and its hidden activations encode information about response quality independently of the target LLM (Section 3.3, lines 85–88). This is genuinely novel: the Bb-S regime achieves strong results even when the target LLM is black-box (e.g., Gemma-7B evaluating LLaMA2-7B on TriviaQA yielding 0.925 AUROC, Table 1). No prior work demonstrates this specific capability.

- **Consistent large-margin improvements across diverse settings.** Across 9 dataset–LLM configurations (Tables 1–2), the proposed methods (Bb-S, Gb-S, or Wb-S) achieve the highest AUROC in all 9 cases. Many margins are substantial — e.g., on CoQA with LLaMA2-7B, Bb-S achieves 0.848 vs. the best unsupervised baseline (AvgE) at 0.600.

- **Ablation isolating the value of hidden activations.** The comparison between Wb-S (hidden activations + entropy/probability) and Gb-S (entropy/probability only) directly quantifies the contribution of internal states (Section 5.2, Table 2). For Gemma-7B on MMLU: Wb-S 0.833 vs. Gb-S 0.776. This is a clean experimental design choice.

- **Demonstrated OOD transferability.** The systematic cross-domain evaluation across MMLU subject groups and QA datasets (Table 3) shows the trained models retain most of their advantage under distribution shift — e.g., Wb-S for Gemma-7B on MMLU Group 2 achieves 0.804 (OOD) vs. 0.807 (in-distribution), while the best unsupervised baseline is only 0.721.

## Weaknesses

### Major

- **Overclaim in Contribution 2 ("sets an upper bound for unsupervised methods").** The paper states: "Leveraging supervised labels from the uncertainty metric, our approach sets an upper bound for the performance of all unsupervised methods, representing the highest achievable performance for these approaches" (line 41). This is not logically justified — a supervised method can perform arbitrarily badly if features are uninformative, and there is no argument that this particular approach or its feature set exhausts what any unsupervised method could, in principle, achieve. This claim should be retracted or substantially qualified.

- **Missing supervised baselines that isolate what the specific architecture contributes.** The main comparison is supervised vs. unsupervised methods. The paper acknowledges this ("the advantage of our method should be attributed to the supervised nature and the labeled dataset," line 234) but then continues to present the comparison as the headline result. To isolate what the proposed framework (tool-LLM + hidden activations + random forest) contributes beyond the mere availability of labeled data, the paper should compare against other supervised approaches using the same training data but different feature sets — e.g., a linear model or MLP on the same entropy/probability features. The Gb-S vs. Wb-S comparison partially addresses this, but without a non-random-forest supervised baseline, we cannot rule out that the random forest's capacity, rather than the hidden activations themselves, drives the gains.

### Minor

- **Theoretical justification (Section 4.2) is loosely connected to the actual method.** Proposition 1 and Corollary 1 describe properties of Bayes-optimal classifiers under specific loss functions for binary classification. The paper's method is a random forest regressor predicting continuous quality scores. The corollary only shows existence of *some* distribution where conditional independence fails — a weak statement that does not guarantee it holds for LLMs. The intuition that "LLMs are trained with different losses → hidden activations carry extra information" is reasonable as conceptual motivation, but it is presented as formal theory that does not tightly connect to the regression-on-random-forests experimental setup.

- **Feature aggregation details are underspecified.** The paper states hidden-layer activations are extracted (line 112) but does not specify which layers are used or how activations across token positions are aggregated into a fixed-dimensional feature vector v_i. Similarly, entropy features "at each token" (line 116) — for variable-length responses, this would require either padding to a max length or aggregation; neither is specified. These details are necessary for reproducibility. (The paper notes layer choice is investigated in an appendix, but the methodology description in the main text is insufficient for replication.)

- **No error bars or confidence intervals.** All AUROC results are reported as single numbers without variance estimates, confidence intervals, or discussion of multiple runs (Tables 1–3). Given that several improvements are modest (e.g., 0.762 vs. 0.725 for G-7B on CoQA; 0.745 vs. 0.729 for L-8B on WMT-14), it is unclear whether these differences are statistically significant. Bootstrapping over test samples would be a lightweight remedy.

- **Label noise not discussed.** The regression targets z_i = s(y_i, y_{i,true}) are single-sample Monte Carlo estimates of the expectation E[s(y, y_true) | x, y] (since y_true is a random variable given x). This is unbiased but high-variance. The paper does not discuss the implications of label noise for the trained uncertainty estimator.

### Trivial

- **Threshold justification.** The paper uses Rouge-1 ≥ 0.3 and BLEU > 0.3 to binarize responses for AUROC evaluation (lines 191, 193) without providing a rationale for these particular thresholds.

## Nice-to-Haves

- A controlled experiment varying the tool LLM while keeping the target LLM fixed, to disentangle whether Bb-S improvements come from tool-LLM competence vs. genuine uncertainty-encoding properties of hidden activations.
- A comparison against trained verifiers or reward models as additional supervised baselines, if such exist for the tasks considered.

## Removed Points

The following points raised by reviewers were removed per filtering rules:

- **Calibration evidence missing from main text** — Calibration results are deferred to an appendix (cited as Section \ref{sec:calib}). Per rules, weaknesses about content that exists in the appendix but was stripped by the parser are removed. The causal-claim framing ("better uncertainty estimation leads to better calibration") is a reasonable finding to report; the evidence is in the original submission.
- **"Which-box" typo (line 89)** — Removed per rule: "remove any criticism about typos, spelling, grammar... The original submission does not have these issues."
- **Bb-S regime is "under-motivated"** — The paper explicitly argues (lines 85–88) that any LLM processing (x,y) jointly can extract features, and provides a separate justification for why hidden activations are informative (Section 4.2). The motivation is present, even if it could be strengthened with a controlled experiment. This is not an absence of motivation.
- **Missing related works on supervised confidence estimation** — Removed per rule: "do not mention missing related works."
- **Claim that the theoretical section is entirely disconnected from the method** — The section is loosely connected (kept as Minor), but the claim of no connection is overstated: the theory provides a conceptual analogy for why hidden activations carry information beyond output scores in settings where the training loss differs from the evaluation objective.

## Novel Insights

None beyond the paper's own contributions. The key insight — that a separate tool LLM's hidden activations can serve as features for black-box uncertainty estimation of another LLM — is the paper's core contribution and is well-supported by the experiments.

## Suggestions

1. Remove or substantially qualify Contribution 2's "upper bound" language.
2. Add a simple supervised baseline (e.g., logistic regression or MLP on the same entropy/probability features) to isolate what the hidden-activation features contribute beyond supervised training itself.
3. Specify which layers are extracted and how token-level activations are aggregated to fixed-dimensional features. Report the dimensionality of v_i.
4. Add bootstrapped confidence intervals or multiple-run statistics to the main tables.
5. Discuss the single-sample label issue and its implications for regression target noise.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>