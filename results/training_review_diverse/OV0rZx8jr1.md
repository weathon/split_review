Now I have a thorough understanding of the paper and all review inputs. Let me construct the final consolidated review.

## Summary

This paper proposes PFP (Preference Feature Preservation), a framework that debiases online preference learning by explicitly maintaining the distribution of human preference features throughout iterative training. PFP extracts preference features from offline data using GPT-4o, trains a DeBERTa-v3-large classifier with a Sinkhorn-Knopp-based relabeling step to preserve the feature distribution, then conditions LLM response generation through preference-derived system prompts. The method is evaluated on Mistral-7B with UltraFeedback, showing improved AlpacaEval 2.0 LC win rate (15.24% vs. 13.13% for Iterative DPO) and MT-Bench (6.88 vs. 6.53), while nearly eliminating length bias growth over iterations.

## Strengths

1. **Novel and well-motivated approach to debiasing.** The idea of preserving the distribution of human preference features (not just conditioning on features) during online learning is novel and addresses a real problem — bias accumulation in iterative preference learning. Figure 4 directly demonstrates that PFP keeps feature-distribution KL divergence near zero across all iterations while baselines diverge substantially.

2. **Strong empirical results on standard benchmarks.** Table 1 shows PFP achieves the highest AlpacaEval 2.0 LC win rate (15.24%) and MT-Bench score (6.88) among compared methods, outperforming Iterative DPO (13.13%, 6.53), SELFEE (14.23%, 6.56), and DPO (9.93%, 6.34). These gains are on independent benchmarks not tied to the paper's KL-divergence diagnostic.

3. **Near-elimination of length bias without explicit length heuristics.** Figure 5(a) shows PFP's response length grows only from 1,138 to 1,187 tokens over 4 iterations, while Iterative DPO grows 1,418→1,709 and SELFEE 1,852→2,412. Table 4 further shows PFP controls length more effectively than explicit length penalty and R-DPO methods while also achieving higher win rates.

4. **Careful ablations validate each component's contribution.** Table 2 isolates the effect of the feature classifier (12.38→14.80) and the distribution-preserving relabeling (14.80→15.24) within the same system-prompt framework. Table 3 demonstrates that double sampling (12.73→13.78) and scheduling (13.78→15.24) each add clear gains. Critically, the "SP only" condition (random features + system prompts) achieves only 12.38, which is *below* SELFEE (14.23) — this rules out the alternative explanation that improvements come merely from adding system prompts rather than from feature preservation.

## Weaknesses

### Fatal

None.

### Major

1. **All results are from a single run without variance estimates.** No standard deviations, confidence intervals, or multiple seeds are reported for any experiment (Tables 1–4, Figs. 2–5). Online preference learning involves stochasticity from response sampling, LLM-based system prompt synthesis (with non-zero temperature), and classifier training. Without multiple trials, it is impossible to assess whether the reported advantages (e.g., AlpacaEval 15.24 vs. 14.23 for SELFEE) reflect reliable improvements or noise. This is the paper's most significant evidential gap.

### Minor

2. **KL divergence debiasing metric uses the same model family (GPT-4o) used for feature extraction during training.** The KL divergence diagnostic (Eq. 8, Figs. 4, 5(b,c)) uses GPT-4o to infer preference features from model responses — the same model used to extract features from the seed data to train the classifier. If GPT-4o has systematic biases in how it classifies features, both the training targets and the evaluation metric share those biases. This does not affect the paper's main benchmark results (AlpacaEval and MT-Bench are independent), but it weakens the supporting evidence for the core debiasing claim. An independent evaluation (e.g., using a different classifier or human annotation on a sample) would strengthen confidence.

3. **No human validation of GPT-4o's feature extraction.** The paper relies entirely on zero-shot CoT prompting of GPT-4o to infer which preference features drove human annotators' binary choices (Sec. 4.1). There is no inter-annotator agreement study or spot-check against human judgments. The quality of the entire pipeline depends on this step; a small error analysis would help.

4. **Generalizability is limited to one base model / dataset configuration.** All experiments use Mistral-7B + UltraFeedback + GPT-4o. It is unclear whether the approach transfers to other base models (e.g., Llama-3 8B), other preference datasets, or other LLM-based feature extractors. The classifier's ability to generalize to out-of-distribution instructions is not analyzed.

### Trivial

None.

## Nice-to-Haves

- An evaluation of the feature classifier's accuracy on held-out instructions (comparing its predictions to GPT-4o-extracted or human-annotated features), to assess whether the Sinkhorn-Knopp relabeling is correcting genuine distribution shift or compensating for classifier errors.
- A comparison against a control that uses a generic fixed system prompt (rather than preference-derived ones) within the same double-sampling framework, to further isolate the effect of feature-specific conditioning. (The paper's "SP only" random-feature condition partially addresses this, but a fixed generic prompt would be even clearer.)

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Critic point #1 (confound between feature conditioning and system-prompt augmentation):** The critic claimed the paper lacks a control for whether improvements come from system prompts rather than feature preservation. However, Table 2's "SP only" condition (random features + system prompts) achieves only 12.38 AlpacaEval, which is **lower** than both SELFEE (14.23) and Iterative DPO (13.13). If system prompts alone explained the gains, this condition would not be the worst performer. The ablation already provides the requested control and shows that the distribution-preserving relabeling (not system prompts) drives improvement. Removed as factually incorrect / the paper already addresses it.

- **Critic point about length bias being largely due to system prompt conditioning (Fig. 3).** The critic claimed the paper does not control for system prompts when claiming PFP's iterative process eliminates length bias. However, Fig. 3 and its surrounding text explicitly analyze a one-step DPO (not the iterative process) to show that even at the initial step, feature-conditioned system prompts reduce bias. This is presented as supporting motivation, not as evidence for the iterative claim. The iterative length-bias evidence in Fig. 5(a) compares PFP against Iterative DPO and SELFEE, which also don't use system prompts. Removed as the paper separates these analyses clearly.

- **Critic's suggestion to add a control with random features within the same framework:** Already present as the "SP only" condition in Table 2 (12.38 AlpacaEval). The paper has this control. Removed as already present.

- **Critic's note about Sinkhorn-Knopp enforcing seed distribution which may not generalize:** This is a reasonable theoretical concern but is speculative — no evidence is presented that the seed distribution is inappropriate or that this causes harm. The empirical results show strong performance, so this concern is not substantiated by evidence. Demoted to Nice-to-Have at most.

- **Critic's note about scheduling heuristic lacking theoretical motivation:** While true that the decreasing-temperature schedule is heuristic, the ablation (Table 3) shows it works empirically. Many effective techniques in LLM alignment are heuristic. This is a generic concern that does not invalidate results. Removed.

- **Critic's demand for human evaluation of feature extraction on 50–100 examples:** This is reasonable but goes beyond what is standard for a conference paper using LLM-as-annotator. Many papers in this area use LLM annotation without human validation. Demoted to Nice-to-Have.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no perspective the paper does not already articulate about its method, though they do highlight methodological rigor gaps (single-run evaluation, circularity in the debiasing diagnostic) that the authors should address.

## Suggestions

1. **Report results over at least 3 random seeds** for the main experiments (Table 1 and key ablations) with means and standard deviations. This single change would substantially increase confidence in the reported gains.

2. **For the KL divergence debiasing metric, use an independent feature extractor** (e.g., a different LLM or a pre-trained classifier) that was not involved in the training pipeline, to break the potential circularity.

3. **Include a small human validation study** (50–100 examples) of the GPT-4o feature extraction step to establish annotation quality.

4. **Test on at least one additional base model** (e.g., Llama-3 8B) to demonstrate generalizability beyond Mistral-7B.

## Score and Decision

The paper proposes a novel and well-motivated framework for debiasing online preference learning, supported by strong empirical results on standard benchmarks and careful ablations that isolate each component's contribution. The primary weakness is the lack of statistical significance reporting (single-run results) and the use of GPT-4o for both training feature extraction and evaluation diagnostics. Neither weakness is fatal — the core performance claims rest on independent benchmarks, not the circular diagnostic — but they prevent full confidence in the reported margins. The paper represents a solid contribution to an important problem and should be accepted with the expectation that the authors address the robustness concerns.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>