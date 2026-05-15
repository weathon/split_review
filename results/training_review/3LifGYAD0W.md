I now have a thorough understanding of the paper and all reviewer claims, verified against the source text. Let me produce the final consolidated review.

---

## Summary

This paper proposes QueRE (Question Representation Elicitation), a black-box method for extracting representations from LLMs by querying them with elicitation questions and using the response probabilities (e.g., probability of "yes" to "Is your answer correct?") as feature vectors for simple linear predictors. The method requires only API-level access (top-k probabilities or even sampled outputs) and is demonstrated across three applications: instance-level performance prediction, detection of adversarially influenced models, and identification of model architectures/sizes. The paper also provides a theoretical analysis of how sampling-based approximations of token probabilities affect the downstream logistic regression estimator.

## Strengths

- **Novel and practical black-box representation extraction**: The core idea — using probability responses to simple self-query questions as features for downstream linear predictors — is simple, model-agnostic, and requires only API-level access. This opens up representation-based analysis for closed-source LLMs where internal states are unavailable. The method demonstrably works on GPT-3.5, GPT-4o-mini, LLaMA2, and Mistral across seven datasets.

- **Convincing results on adversarial detection and model identification**: QueRE achieves near-perfect accuracy in distinguishing clean GPT-3.5 from an adversarially prompted version that answers incorrectly (Figure 5), reliably detects subtle adversarial prompts that insert bugs into code generation (Table 2), and nearly perfectly classifies between LLMs of different sizes (Figure 4). These applications have clear practical value for API accountability and safety monitoring, and the claims here are well-supported.

- **Theoretical + empirical validation of sampling approximation**: Proposition 1 provides a convergence rate O(1/√n + √n/k) for the logistic regression estimator under sampling-based probability approximation, and Figure 7 confirms less than a 2-point AUROC drop with finite samples (over 5 random seeds). This combination of theory and experiment strengthens the method's applicability to APIs that do not expose token probabilities.

- **Comprehensive breadth of evaluation**: The paper evaluates on 7 datasets (NQ, SQuAD, HaluEval, BoolQ, DHate, CS QA, WinoGrande), covering open-ended and multiple-choice QA, across 6 model variants (LLaMA2-7B/13B/70B, Mistral-7B/MoE, GPT-3.5, GPT-4o-mini), lending support to the method's generality.

- **Well-calibrated predictors**: QueRE-trained models show substantially lower Expected Calibration Error than answer-probability baselines (Figure 6), which is important for high-stakes applications where confidence thresholds matter.

## Weaknesses

### Fatal
None.

### Major
- **Data splitting methodology lacks rigor for main results**: The paper uses the first 5,000 training instances and first 1,000 test instances from each dataset without shuffling (Section 4.1), and reports a single run for the main performance-prediction results (Figures 2, 3). This non-standard protocol risks ordering biases, and the absence of confidence intervals or standard deviations makes it impossible to assess the reliability of the reported AUROC values. (Only the sampling ablation in Figure 7 reports results over multiple seeds.) This is the most significant methodological shortcoming.

- **Missing white-box baselines in model architecture detection (Figure 4)**: For the open-source models used in the model-identification experiment (LLaMA2-13B, LLaMA2-70B), white-box methods (RepE, Full Logits) could be computed and should be included as baselines. The paper compares QueRE only against Answer Probs and Pre-Conf Confidence. Without the stronger baselines, the claim that QueRE is uniquely effective for this task is less well-supported than it could be.

### Minor
- **Abstract slightly overstates performance relative to white-box methods**: The abstract claims QueRE "can often outperform white-box linear predictors," but the body text (lines 18, 95) uses the more measured "often matches or outperforms," which better reflects the evidence. On open-source models where the comparison is fully fair (Full Logits is not approximated), the results are mixed — QueRE sometimes wins, sometimes is comparable, sometimes trails slightly. The abstract should be aligned with the body. The body's claim is accurate and well-supported; this is a calibration issue in the abstract only.

- **Proposition 1 is a standard consistency result with limited novelty**: The convergence rate O(1/√n + √n/k) is derived from prior work on covariate measurement error in logistic regression (Stefanski & Carroll, 1985) and is not used to inform any experimental design choices (e.g., what k to use in practice). The practical validation in Figure 7 carries the weight; the theoretical result itself adds modest insight. The paper's main methodological contribution is the feature extraction scheme, not this analysis.

- **Component-wise contribution not ablated**: The ablation study focuses on the number of elicitation questions (Figure 8) and random vs. meaningful text sequences (Table 4), but does not ablate the contribution of each feature group (elicitation questions, pre-confidence, post-confidence, answer probabilities) individually. Understanding which components drive performance would strengthen the paper.

- **Generalization bounds rely on strong independence assumptions**: The paper's non-vacuous generalization bounds (Table 3) require the assumption that LLM-extracted representations are independent of the downstream task data. This is acknowledged only in passing and is a strong condition that limits the practical applicability of the bound.

### Trivial
None.

## Nice-to-Haves
- t-SNE or PCA visualization of QueRE features for correct vs. incorrect examples would concretely illustrate the separability the linear probe exploits.
- Example-level analysis showing how specific elicitation questions differentiate correct from incorrect answers would ground the mechanism.
- Application to additional closed-source models (Claude, Gemini) where only sampled outputs are available would test the generality of the sampling approximation result.
- The finding that random sequences of natural language can sometimes outperform meaningful elicitation questions (Table 4) is intriguing but underexplored — analyzing the entropy or variance of the resulting probability distributions could reveal what information is being captured.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Criticism about the generalization bounds section being incomplete (type of bound unexplained)**: The bound details are likely in the appendix, which was stripped by the PDF parser. Per policy, missing-appendix complaints are removed.
- **Criticism that Queue "does not justify why these specific components are included" (pre-conf, post-conf, answer probs)**: This is a weak criticism — the components are standard LLM confidence signals (Xiong et al., 2023) and the paper's focus is on the elicitation-question features, not on justifying every feature component. The paper frames the simple baselines as ablations of their own representation.
- **Strength Finder's claim about "non-vacuous generalization bounds" being a core strength**: The bounds rely on a strong independence assumption acknowledged only in passing. This partially conflicts with the verified weakness above. The calibration results (Figure 6) are a genuine strength; the generalization bounds are more tentative.
- **Weakness implying reproducibility concerns because baselines like RepE "cannot be applied to GPT models"**: The paper is transparent about this limitation. This is a constraint of the API setting, not a methodological flaw, and does not support a weakness against the paper.

## Novel Insights

The most interesting observation from the reviews is the tension between the honest reporting of the random-sequences result (where meaningless text sometimes beats meaningful questions) and the paper's conceptual framing. The paper correctly notes that this "aligns with prior work describing flaws in existing interpretability frameworks," but this finding deserves deeper investigation: it suggests that the method may be capturing a high-dimensional "behavioral signature" of the model's output distribution rather than anything about the model's self-awareness or reasoning. This could be reframed as a strength — the method works *despite* requiring no semantic understanding from the elicitation prompts — rather than a puzzle to be explained away.

## Suggestions

1. **Add statistical rigor to main results**: Re-run the main performance-prediction experiments (Figures 2, 3) with at least 3-5 random train/test splits, reporting means and standard deviations. This would address the most serious methodological concern.

2. **Include white-box baselines in Figure 4**: For the open-source models used in model architecture detection, add RepE and Full Logits as baselines to demonstrate that QueRE adds value beyond what is captured in hidden states.

3. **Align abstract with body**: Change the abstract's "can often outperform" to "can often match or outperform" (as the body already says) to avoid overclaiming.

4. **Add a component ablation**: Decompose the QueRE feature vector into its constituent groups (elicitation questions, pre-conf, post-conf, answer probabilities) and report AUROC for each subset, to clarify which components drive the gains.

5. **Investigate the random-sequences finding**: Add a brief analysis of why random text sometimes outperforms meaningful questions — e.g., comparing the entropy, variance, or diversity of the resulting probability distributions across elicitation types.

## Score and Decision

**Originality**: 7/10 — The idea of using self-query probabilities as representations is genuinely novel and practically motivated.  
**Importance of research question**: 8/10 — Predicting and understanding black-box LLM behavior is a timely and important problem.  
**Claims supported**: 6/10 — The core claim that QueRE produces useful black-box representations is well-supported, but the "outperform white-box" claim is slightly overstated and the lack of error bars weakens support.  
**Soundness of experiments**: 6/10 — Breadth is good but the data-splitting methodology and absence of confidence intervals for main results are notable gaps.  
**Clarity of writing**: 7/10 — The method is clearly described and the organization is logical.  
**Value to community**: 7/10 — The method is simple, practical, and opens new evaluation capabilities for closed-source models.

The paper presents a genuinely novel and practically valuable technique. The main weaknesses — lack of statistical rigor in the evaluation and a slightly overstated abstract claim — are fixable and do not invalidate the core contribution. The adversarial detection and model identification experiments are convincingly demonstrated and have clear real-world utility.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>