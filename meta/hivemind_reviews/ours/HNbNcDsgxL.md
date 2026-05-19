## Summary
This paper proposes Delta, an inference-time contrastive decoding method that randomly masks input tokens and then subtracts the logits from the masked-forward pass from an amplified version of the unmasked logits, with the goal of reducing hallucinations in LLMs. Evaluated on Llama 3.1 8B Instruct across SQuAD v1.1/v2, TriviaQA, and Natural Questions, Delta shows consistent improvements, most notably a 14.53 percentage point gain on SQuAD v2's no-answer exact match score. The method is tested on context-free datasets (CommonsenseQA, MMLU) and correctly reports marginal performance declines, honestly scoping its applicability to context-rich settings.

## Strengths
- **Inference-only operation, no retraining needed.** Delta requires only two forward passes at inference time with no model fine-tuning or additional data collection (Section 1, Section 3). This distinguishes it from training-based approaches and makes the method straightforward to deploy.

- **Large and clinically meaningful improvement on SQuAD v2 no-answer EM.** The 14.53 pp gain on the "no answer" exact match score (Section 5.1) directly demonstrates the method's ability to prevent the model from fabricating answers when the context provides no support — the core failure mode Delta is designed to address.

- **Ablation study confirms robustness across hyperparameters.** Varying masking ratio (0.3–0.7) and logit ratio α (0.1–0.5) on SQuAD v1.1 yields standard deviations of only 0.66 (EM) and 0.21 (F1), with all configurations exceeding the baseline (Section 6, Figure 2). This supports the claim that Delta does not require extensive tuning.

- **Honest characterization of limitations via targeted experiments.** The paper explicitly evaluates Delta on context-free datasets (CommonsenseQA, MMLU), reports marginal performance drops (0.25 and 0.29 pp), and candidly states that the method is "best suited for applications where contextual information is critical" (Section 5.3). This strengthens rather than weakens the paper's overall credibility.

- **Non-trivial adaptation of contrastive decoding from vision to text.** The paper identifies that directly applying Gaussian noise (as in VCD) is infeasible for text, and instead introduces random token masking as a text-appropriate distortion mechanism (Section 1, Section 3.3). This is a clear methodological innovation relative to prior work.

## Weaknesses
### Fatal

None.

### Major

- **No comparison to existing inference-time hallucination mitigation methods.** The related work discusses CAD (Shi et al., 2024), VCD (Leng et al., 2024), and ICD — all contrastive decoding approaches that operate at inference time without retraining — yet none are included as experimental baselines. CAD is particularly relevant: it also amplifies the difference between context-conditioned and less-contextualized logits. Without an empirical comparison, the reader cannot determine whether Delta outperforms, matches, or falls short of existing methods. The paper claims Delta is "more generalizable" than CAD (Section 2), but this claim is untested. This is the single largest evidential gap and substantially weakens the case for Delta as a meaningful advancement over known techniques.

### Minor

- **Choice of EOS as the mask token is neither justified nor ablated.** The paper states "All experiments utilize the end-of-sequence (eos) token as the MASK token" (Section 4.2) with no rationale. The EOS token carries a specific semantic role (sequence termination), and replacing content tokens with it may produce logit artifacts that are not equivalent to using a dedicated [MASK] token, [UNK], or a neutral token. Without an ablation comparing mask-token choices, the method's behavior could be partially driven by this unexamined design decision.

- **Computational cost is asserted but not measured.** The paper claims Delta is "computationally efficient and easily deployable" (Section 1), but the method requires two autoregressive forward passes per generation step (one unmasked, one masked), effectively doubling inference cost. No wall-clock time, relative latency, or throughput measurements are reported, and there is no discussion of caching strategies (e.g., KV-cache sharing) that could amortize this cost. This omission weakens the practical significance claim.

- **Hyperparameter selection process is undocumented.** The parameters r_mask=0.7, α=0.3, β=0.1 are fixed across all experiments with no description of how they were chosen or validated (Section 4.2). While the ablation study (Section 6) shows low sensitivity on SQuAD v1.1, this single-dataset analysis does not establish that the chosen defaults are appropriate for the other benchmarks. A held-out validation set or cross-dataset tuning analysis would strengthen this.

- **No statistical significance or variance reporting.** Results are reported as point estimates without confidence intervals, standard deviations across runs, or significance tests (Table 1, Table 2). Given that some improvements are modest (e.g., ~2–3 pp in non-sampling settings), it is unclear whether these gains are statistically reliable.

### Trivial

- **Claim of greater generality than CAD is inconsistent with empirical findings.** The paper asserts Delta "could apply to all textual inputs" and is therefore "more generalizable" than CAD (Section 2), but then shows Delta does not improve performance on context-free tasks (Section 5.3). The theoretical applicability claim is trivially true (the masking operation can be applied to any text), but the practical implication of "more generalizable" is misleading given the method's demonstrated ineffectiveness without context. The text would benefit from tighter wording.

## Suggestions
1. **Add CAD as a baseline** on at least SQuAD v2 (especially the no-answer EM metric) and TriviaQA. CAD is the most directly comparable method — it also operates at inference time, uses contrastive decoding, and targets context-rich QA. Without this comparison, the paper cannot substantiate that Delta is a meaningful improvement over the closest existing approach.
2. **Ablate the mask token choice.** Compare EOS against [UNK], a neutral token like "the", and random word substitution on at least one dataset to confirm the method's behavior is not an artifact of the specific mask token.
3. **Report wall-clock time or tokens-per-second** for the baseline vs. Delta (and vs. CAD if added). This grounds the "computationally efficient" claim in data and lets readers evaluate the practical tradeoff.
4. **Describe the hyperparameter search or validation procedure** explicitly, or show that the chosen defaults are robust across datasets (beyond the SQuAD v1.1 ablation).
5. **Add confidence intervals** (e.g., bootstrap over examples) for at least the main results to establish that the observed gains are statistically reliable.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>

## Questions


## Decision
Reject
