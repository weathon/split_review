Now I have thoroughly verified all claims against the paper. Let me synthesize the final review.

---

## Summary

This paper proposes QueRE, a method that extracts black-box "representations" from LLMs by querying them with ~50 elicitation questions (e.g., "Do you think your answer is correct?") and using the resulting token probabilities as features for linear predictors. The authors demonstrate these representations can be used to predict instance-level model performance, detect adversarially influenced models, and distinguish between different model architectures/sizes — all without white-box access to model internals. A key finding is that QueRE often matches or outperforms white-box linear probes (RepE, Full Logits) across multiple tasks and models.

## Strengths

- **Black-box method that matches or outperforms white-box probes on performance prediction.** Across open-ended QA (Natural Questions, SQuAD) and MCQ tasks (HaluEval, BoolQ, DHate), linear predictors trained on QueRE features achieve AUROC comparable to or exceeding white-box baselines like RepE (hidden state probes) and Full Logits (vocabulary distribution), despite using only top-\(k\) token probabilities (Figs. 2, 3). This directly supports the paper's central claim.

- **Near-perfect detection of adversarially influenced LLMs in a completely black-box setting.** QueRE-based classifiers achieve AUROC close to 1.0 in distinguishing clean GPT-3.5 from GPT-3.5 affected by adversarial system prompts (e.g., "answer questions incorrectly") on BoolQ and DHate (Fig. 5), and on a subtle code-bug insertion task (Table 2). This extends prior white-box detection (MacDiarmid et al., 2024) to black-box access.

- **Reliably distinguishes between different model architectures and sizes.** Using QueRE features, a linear classifier achieves near-perfect accuracy in discriminating LLaMA2-7B/13B/70B and Mistral-7B/Mixtral-8x7B on BoolQ, far outperforming baselines (Fig. 4). This has practical value for detecting misrepresented models in APIs.

- **Works with sampling approximations when top-\(k\) probabilities are unavailable.** When approximating true probabilities via \(k\) samples, QueRE shows less than a 2-point AUROC drop on HaluEval and DHate (Fig. 7), demonstrating practical applicability to APIs that do not expose log-probs.

- **Predictors trained on QueRE are better calibrated than competing approaches.** QueRE achieves lower Expected Calibration Error compared to using answer probabilities on HaluEval and SQuAD (Fig. 6), an important property for high-stakes applications.

- **The finding that random sequences of natural language yield competitive results (Table 4) is genuinely interesting.** This suggests the diversity of prompts — rather than their semantic content — drives much of the predictive power, with practical implications for ease of deployment.

## Weaknesses

### Fatal
None.

### Major

- **Missing error bars / variance estimates on all main comparative results (Figs. 2, 3, 4, 5; Tables 1, 2).** Figures 2–5 and Tables 1–2 report AUROC and accuracy as single point estimates without any indication of variance, confidence intervals, or significance tests. The paper's central claim — that QueRE "often matches or outperforms" white-box baselines — cannot be rigorously evaluated without knowing whether observed differences are reliable or within noise. For example, in Figure 2 the gap between QueRE and Full Logits on SQuAD with Llama2-70B appears very small (~0.01–0.02 AUROC). Since the authors *do* report error bars in the ablations (Fig. 7, Fig. 8), this omission in the main results is a clear gap. This is the most significant weakness and directly affects confidence in the paper's headline contribution. *However, this is addressable: the authors could provide bootstrapped confidence intervals or multi-seed results.*

### Minor

- **Proposition 1 (theoretical convergence rate) is presented without sufficient support.** The convergence rate \(O(1/\sqrt{n} + \sqrt{n}/k)\) is stated as a formal proposition but neither derived nor traced to a specific theorem. The text says it "follows from relatively standard results" without elaboration. The citation to Stefanski & Carroll (1985) provides context for covariate measurement error but does not directly yield the claimed rate. Since the empirical demonstration (Fig. 7) already shows the sampling approximation works well, this theoretical section adds little; as presented, it is more of a sketch than a rigorous proposition.

- **Generalization bounds rely on an unverified independence assumption.** Table 3 presents generalization bounds computed under the assumption that QueRE features are "independent of the downstream task data." The paper acknowledges this limitation and notes it is "verifiable via works in data contamination" but does not actually verify it for the datasets used (BoolQ, SQuAD, HaluEval, etc.). Given that standard LLM pretraining data likely overlaps with some of these benchmarks, the assumption is not trivially satisfied. The bounds are not essential to the empirical contribution, but presenting them without verification weakens their force.

- **Limited diversity in adversarial detection prompts.** The main adversarial detection experiments (Fig. 5, Table 2) each use a single adversarial system prompt per task. While Table 1 tests six helpful/harmful prompts, the core detection results rely on one prompt each (e.g., "answer questions incorrectly" for QA, "secretly insert bugs" for code). The paper's claim of "robustness to variations in the system prompt" is based on Table 1 only. The results are strong, but generalizing to a broader distribution of adversarial prompts or more subtle manipulations is not fully demonstrated.

### Trivial
None.

## Nice-to-Haves

- **Add a discussion of computational cost.** Using ~50 elicitation questions per instance requires ~50× the forward passes compared to a single confidence score. A brief note on latency/throughput tradeoffs for deployment would strengthen the practical contributions.
- **Explore why random sequences of natural language work.** The finding in Table 4 is interesting but under-discussed. A brief exploration of whether this reflects a property of autoregressive models (any linguistic context probes the same latent uncertainty) would deepen the paper's contribution.
- **Expand adversarial detection to include a small held-out set of unseen adversarial prompts** (different phrasings, different types of misbehavior) to strengthen the generality claim.

## Removed Points

- **Strength 5 (Theoretical analysis as a core strength):** Removed because the verified weakness about insufficient support undermines treating this as a standalone strength. The empirical demonstration (Fig. 7) stands on its own.
- **"Clarify the RepE baseline" suggestion:** The paper already states "RepE (Zou et al., 2023a), which extracts the hidden state of the LLM at the last token position in its representation reading" — this is explicit enough; training a linear probe on extracted features is standard and does not need restatement.
- **"Full Logits presentation is misleading" observation:** The paper's Figure 2 caption already notes "full logits for the GPT models is an approximation of a sparse vector with nonzero values for the top-5 logits from the API," which adequately informs the reader. QueRE appending these same top-5 probabilities is transparent, and outperforming Full Logits is a valid ablation showing elicitation questions add signal.

## Novel Insights

The most interesting finding that emerges across the reviews is that the method's power appears to come more from *diversity of prompts* than from their semantic content. The result that random sequences of natural language sometimes outperform meaningful elicitation questions (Table 4) suggests QueRE is probing the model's latent distributional space in a way orthogonal to interpretable self-reflection. This raises deeper questions about what these "representations" actually capture — they may be encoding model uncertainty in a distributed manner across diverse linguistic contexts rather than through any specific introspective capability.

## Suggestions

1. **Add variance estimates** (bootstrapped confidence intervals or multi-seed runs) to all main comparative figures and tables. This is the single most impactful improvement.
2. **Either strengthen Proposition 1** with a proper derivation or a precise reference, or remove the formal proposition framing and present the convergence reasoning as a sketch.
3. **Acknowledge the independence assumption more transparently** in the generalization bounds section, and either verify it for the specific datasets or frame the bounds as conditional.
4. **Add a brief discussion** of why random sequences of language yield competitive representations — this could become a strength of the paper with deeper analysis.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>