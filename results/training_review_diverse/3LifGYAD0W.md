Now I have all the information needed to produce the final consolidated review. Let me synthesize everything carefully.

---

## Summary

This paper proposes QueRE, a method that extracts low-dimensional black-box representations from LLMs by feeding the model its own greedy output along with elicitation questions and recording the probability of "yes" responses. These features are used to train linear classifiers for three applications: predicting instance-level model correctness, detecting adversarially influenced system prompts, and distinguishing between model architectures/sizes. The method requires only top-k logprobs (or sample-based approximations), making it applicable to closed-source APIs.

## Strengths

- **Black-box features match or outperform white-box methods for predicting LLM performance.** Across six QA datasets (NQ, SQuAD, HaluEval, BoolQ, DHate, CSQA) and multiple model families (LLaMA2, Mistral, GPT-3.5, GPT-4o-mini), QueRE's AUROC often equals or exceeds RepE (hidden-state probe) and Full Logits (vocabulary distribution), both of which require white-box access (Figures 2–3). This is the paper's central empirical contribution.

- **Near-perfect detection of adversarially influenced system prompts in a black-box setting.** QueRE achieves >0.98 AUROC distinguishing clean GPT-3.5 from versions given harmful system prompts (Figure 5), detects subtle bug-introducing prompts in code generation (Table 2, AUROC=0.996), and generalizes to multi-class discrimination among several harmful vs. helpful prompts (Table 1, 99% accuracy). This extends white-box detection (MacDiarmid et al., 2024) to the black-box regime.

- **Accurate discrimination between model architectures and sizes using only black-box outputs.** A linear classifier on QueRE features achieves >0.98 accuracy distinguishing among LLaMA2-7B, 13B, 70B, and Mixtral-8x7B on BoolQ, while all baselines perform near chance (Figure 4). This directly addresses the practical problem of API model verification.

- **Theoretical and empirical validation of sampling-based approximation.** Proposition 1 provides a convergence rate for logistic regression when true probabilities are estimated from samples. Figure 7 confirms that approximating GPT-3.5's top-5 probabilities with 20–200 samples causes less than a 2-point AUROC drop, making the method applicable to APIs that do not expose logprobs.

- **Better calibration than standard confidence scores.** Figure 6 shows QueRE predictors have substantially lower ECE than models using only answer probabilities on HaluEval and SQuAD, which is important for high-stakes deployment.

- **Non-vacuous generalization bounds.** Table 3 reports lower bounds on accuracy (e.g., 91.5% for LLaMA2-7B on BoolQ) using PAC-Bayes theory, enabled by the low feature dimension.

## Weaknesses

### Fatal
None.

### Major

- **Main experimental results lack uncertainty estimates.** The headline results (Figures 2–5, Tables 1–2) report point estimates of AUROC and accuracy without error bars, confidence intervals, or replication across random seeds. Given the paper's central claim that QueRE "matches or outperforms" white-box methods, it is impossible to assess whether the observed differences are reliable or within noise. The authors demonstrate they have the machinery for uncertainty estimates (Figure 7 uses 5 random seeds; Figure 8 reports standard error), making its absence from the main experiments a significant omission. This weakness undermines the strongest claims but does not invalidate the overall contribution — the trends are consistent across many tasks and models.

### Minor

- **The generalization bounds rely on a strong independence assumption that is not empirically verified.** The paper acknowledges (line 150) that the bounds require representations to be independent of downstream task data, noting this is "verifiable via works in data contamination" or "valid on datasets released after LLM training." While this justification is reasonable, the paper provides no empirical check of whether the assumption actually holds for the settings in which the bounds are reported. Since the bounds are presented as "another added benefit" (line 145) rather than a core contribution, this is a minor issue.

- **Adversarial detection experiments use only one model (GPT-3.5).** While the paper tests several adversarial styles (harmful prompts, bug-introducing code prompts) and shows robustness to system prompt variation (Table 1), all adversarial detection uses GPT-3.5. Testing on additional model families would strengthen the generality claim.

- **The random-sequences finding could benefit from deeper analysis.** The paper reports (Table 4) that random GPT-4-generated text sequences can sometimes match or exceed meaningful elicitation questions. The finding is discussed and linked to interpretability pitfalls (line 187), which is appropriate. However, the paper does not analyze what properties of the random sequences drive performance (e.g., length, perplexity, diversity), leaving an interesting question unexplored. This is not a flaw in the method but a missed opportunity to deepen understanding.

### Trivial
None.

## Nice-to-Haves

- A brief discussion of computational cost (number of API calls per instance, practical guidance on choosing the number of elicitation questions) would help practitioners adopt the method.
- A comparison with simple black-box alternatives such as asking the model to rate its confidence on a Likert scale, or with an ensemble of few-shot prompts, would further situate QueRE relative to other black-box approaches.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Remarkably can often outperform" is too strong (Abstract).** The abstract uses "often outperform" which is appropriately qualified. The paper's own summary (line 95) says "often matches or outperforms." The results in Figures 2–3 support this qualified claim. REMOVED: the criticism overstates the issue.

- **Method section does not make multi-part design explicit.** The paper explicitly states at line 51: "In addition to these probabilities... we also append: (1) pre- and post-confidence scores... and (2) the distribution over possible answers." This is clearly described. REMOVED: the criticism misreads the paper.

- **RepE comparison asymmetry.** The paper states (line 80) that RepE and Full Logits "cannot be applied to black-box language models and should be seen as strong comparisons that assume more information than our approach." The asymmetry favors the baselines (they have more information), making QueRE's competitive performance more impressive, not less. REMOVED: not a valid weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews converge on the paper's central finding — that simple black-box queries can extract representations competitive with white-box probes — without adding a fundamentally new perspective. The main value of the review process is in identifying the evidential gap (lack of error bars) and confirming that the random-sequences finding is interesting but underexplored.

## Suggestions

- **Add error bars or confidence intervals to all main experimental figures (Figures 2–5).** Replicate the main experiments over at least 3–5 random train/test splits or seeds. This single change would substantially strengthen the paper's central claim.
- **Either remove the generalization bounds section or empirically verify the independence assumption** for the specific settings reported.
- **Expand adversarial detection to at least one additional model family** (e.g., LLaMA or Mistral) to support the generality claim.
- **Provide a brief analysis of the random-sequences finding** — at minimum characterize what kinds of random text work well (token diversity, perplexity, length) to clarify whether the benefit is driven by diversity or some other property.

## Score and Decision

This is a solid paper with a clever, practical method, broad experimental scope, and generally positive results across three distinct applications. The main weakness — absence of uncertainty estimates in headline results — is real but addressable and does not invalidate the contribution. The evidence is strongly suggestive and consistent across many settings. I recommend acceptance.

**Originality**: Good — the idea of using response probabilities to elicitation questions as black-box features is novel and well-motivated.

**Importance**: High — black-box interpretability is a timely and practically significant problem.

**Claims support**: Moderate — strong qualitative support but weakened by missing error bars on key comparisons.

**Soundness**: Good overall; the ablations and sampling analysis are well-executed.

**Clarity**: Good, though some organizational improvements would help.

**Value to community**: High — the method is simple, model-agnostic, and immediately usable by practitioners.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>