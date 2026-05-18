Now I have a comprehensive view of the paper. Let me synthesize the final review.

## Summary

This paper investigates uncertainty-based abstention in LLMs across three failure modes — correctness, hallucinations (unanswerable questions), and safety — using two families of uncertainty measures: statistical measures (predictive entropy, semantic entropy, negative log-likelihood) and a verbalized measure called In-Dialogue Uncertainty (InDU, a simple hedge-word count). It compares pretrained, instruction-tuned, and RLHF-aligned Llama2 models. The key findings are: (1) statistical uncertainty improves correctness by 2–8% when abstaining, (2) InDU detects ~50% of unanswerable questions at a 10% false positive rate, and (3) statistical uncertainty on RLHF models filters 70–99% of unsafe responses.

## Strengths

1. **Systematic joint study of two uncertainty types across three failure modes.** The paper is the first to evaluate statistical and verbalized uncertainty under a unified framework for correctness, hallucinations (unanswerable questions), and safety, showing that the optimal uncertainty measure differs per scenario. This scenario-dependent mapping goes beyond prior work that examines settings or metrics in isolation (Section 5, Tables 1–3).

2. **InDU as a zero-cost signal for unanswerable questions.** The paper introduces a simple hedge-word frequency count as a signal to detect unanswerable questions. On SelfAware, InDU achieves AUROC 0.75 (RLHF) and can identify ~50% of unanswerable questions while falsely refusing only 10% of answerable ones (Figure 3b, Section 5.2). This requires no additional model or prompting — only a word list — making it practically cheap.

3. **Substantial safety gains from statistical uncertainty on RLHF models.** On AutoDAN, abstaining the 10% most uncertain responses (via NLL) raises the safe response rate from 92.5% to 99.4%, filtering 99% of unsafe outputs (Section 5.3, Figure 3c). Importantly, the paper isolates the effect of alignment by comparing pretrained, instruction-tuned, and RLHF models, showing that only RLHF yields high AUROC for safety (e.g., NLL AUROC 0.99 on AutoDAN, Table 3).

4. **Empirical comparison of alignment methods for uncertainty awareness.** The paper compares base → instruction-tuned → RLHF along the same uncertainty metrics, demonstrating that RLHF not only improves safety rates but also makes the model's probability vectors informative about safety — a granular finding absent from prior safety studies.

## Weaknesses

### Major

1. **InDU conflates hedging style with genuine uncertainty; the mechanism behind its effectiveness is unclear.** The paper operationalizes InDU as a simple count of hedge words from a fixed list. While the paper acknowledges this is "not a perfect metric" (Section 3.2), it then treats InDU as evidence of "uncertainty awareness" (e.g., "RLHF finetuning enhances In-Dialogue Uncertainty awareness for unanswerable questions," Section 5.2). Because RLHF trains models to mimic human conversational patterns — including hedging — the higher InDU for unanswerable questions could reflect learned stylistic correlations rather than the model being aware of its own uncertainty. A model could be completely confident in a wrong answer and still hedge because its training data does so. Conversely, an uncertain model might not hedge. The paper does not disentangle these. The empirical finding that InDU correlates with unanswerability is useful, but the framing as "uncertainty awareness" overstates what a word-count measure can support. The authors should either validate InDU against human-annotated uncertainty or reframe it as a simple heuristic that happens to work for unanswerable questions.

2. **The safety results lack mechanistic analysis; the uncertainty signal may be detecting atypical responses rather than unsafety per se.** The RLHF Llama2 model already has a 92%+ safe response rate. The paper shows that most of the few unsafe responses have high statistical uncertainty. However, this could occur because unsafe responses are out-of-distribution for the RLHF-trained policy — the model internally "wants" to refuse but a small subset slip through, and those exceptional responses have high entropy due to internal conflict. The pretrained and instruction-tuned models produce many unsafe responses, and uncertainty fails to detect them, which is consistent with this explanation. The paper does not analyze what the high-uncertainty unsafe responses actually look like (e.g., do they contain partial refusals? are they linguistically atypical?). Without this analysis, it is unclear whether the uncertainty signal is detecting unsafety or merely detecting responses that deviate from the model's trained policy. This limits practical value: the method requires a highly safe base model, and an adversary could potentially adapt to produce low-entropy unsafe responses.

### Minor

1. **The "hallucination" framing is broader than what is actually studied.** The paper studies only *unanswerable questions* (from SelfAware) and equates abstaining from these with "reducing hallucinations." This conflates two distinct failure modes: (a) the model not knowing and hedging versus (b) the model confidently fabricating a plausible but false answer (e.g., on counterfactual or conflicting-fact questions). InDU will only help for case (a). The title and abstract use "reduces hallucinations" without this qualification, overclaiming the scope. A more precise framing would be "detects unanswerable questions," which is a different and arguably easier problem than detecting confident hallucinations.

2. **No confidence intervals or statistical tests.** Results (AUROCs, accuracy improvements) are reported as exact numbers without error bars, confidence intervals, or significance tests. Given the modest number of datasets and single-seed runs, some reported numbers (e.g., AUROC varying from 0.43 to 0.89 across datasets) could be unstable. The core findings are likely robust, but the paper would benefit from bootstrapped intervals or multi-seed runs for key results.

3. **No comparison against simple abstention baselines.** The paper compares uncertainty-based abstention against no abstention but does not compare against prompting the model to say "I don't know" or using a separate classifier/reward model as a filtering baseline. Such comparisons are standard in the abstention literature and would contextualize the reported gains. Moreover, the paper claims "almost no additional computational overhead" for statistical uncertainty, but predictive and semantic entropy require multiple samples and a bi-directional entailment model (Deberta-large), which is nontrivial overhead. A cost comparison would strengthen the claims.

### Trivial

None.

## Nice-to-Haves

- Evaluate on confident hallucination datasets (e.g., TruthfulQA, counterfactual QA) to test whether *any* uncertainty measure can detect non-hedged hallucinations. Even negative results would properly bound the claims.
- Analyze token-level probabilities on safe vs. unsafe responses for RLHF models to illuminate the mechanism behind the safety results.
- Provide a failure analysis with examples of high-uncertainty safe responses (false alarms) and low-uncertainty unsafe responses (missed detections).
- Report the specific hyperparameters (temperature, number of samples N, entailment threshold) in the main text if not already in the appendix.

## Removed Points

- **Criticism that correctness improvements (84.4% → 86.0% at 5% rejection) are "not impressive."** Remove: the paper is transparent about the trade-off via ARC curves; whether this is impressive is subjective and the 25% rejection case shows 8.2% absolute gain. The paper's claim is that uncertainty *can* improve correctness, which is supported.
- **Criticism about "abstention" being misleading (post-hoc filtering vs. built-in refusal).** Remove: Chow's rule (1970), which the paper cites, uses threshold-based abstention on classifier probabilities. The usage is standard and not misleading.
- **Criticism about fuzzy exact match being a weak evaluation.** Remove: fuzzy exact match is a widely used, defensible choice for free-form QA evaluation.
- **Criticism about missing hyperparameters (N, temperature, entailment threshold).** Remove per guidelines: these details are likely in the appendix, which the parser strips. They exist in the original submission.
- **Claim that the paper "does not discuss the cost of false refusals."** Remove: the paper reports the false refusal rate (e.g., 10% falsely refused answerable questions, Section 5.2) and shows full ROC/ARC curves, which explicitly characterize this trade-off.

## Novel Insights

The most interesting cross-cutting insight is that different model *training stages* yield uncertainty measures that are informative for different failure modes, and that the relationship is not monotonic: pretrained models have poor uncertainty for safety; instruction tuning improves safety rates slightly but does not make uncertainty informative; RLHF suddenly makes statistical uncertainty highly predictive of safety (AUROC 0.99). This suggests that RLHF does not merely calibrate the model but fundamentally restructures the output distribution such that safety-relevant information is encoded in token-level probabilities. This pattern — where a training method creates the very signal needed to detect its own failures — is worth deeper investigation and could inform the design of built-in abstention mechanisms.

## Suggestions

1. Reframe the hallucination claim from "reduces hallucinations" to "detects unanswerable questions" to match the actual scope of the experiments.
2. Conduct a mechanistic analysis of the safety results: examine token-level probability patterns in high-uncertainty unsafe vs. low-uncertainty unsafe responses to clarify whether uncertainty detects unsafety or merely out-of-distribution responses.
3. Add a prompting baseline ("answer 'I don't know' if uncertain") and a lightweight classifier baseline to contextualize the reported gains.
4. Validate InDU against human-annotated uncertainty on a small sample, or explicitly reframe it as a simple heuristic rather than evidence of "uncertainty awareness."

## Score and Decision

The paper provides a useful empirical mapping between uncertainty types, model training, and failure modes. The core findings — that InDU cheaply detects unanswerable questions and that statistical uncertainty on RLHF models substantially improves safety — are novel and practically relevant. The weaknesses are about overclaiming and insufficient mechanistic analysis, not about invalidity of the results. With revision (particularly reframing the hallucination scope and adding mechanism analysis for safety), the contribution is solid.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>