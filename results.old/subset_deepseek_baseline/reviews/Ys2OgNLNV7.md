## Summary

The paper proposes using raw query-key (QK) dot-product scores from transformer attention heads as an internal signal for answer selection and correctness verification in LLMs, optionally combined with chain-of-thought (CoT) prompting. The method is evaluated on MCQA (MMLU-PRO, HLE-1/4), open-ended reasoning (MATH-500, GSM8K), and a hypothesis selection task. The authors claim that this white-box decision rule can match or exceed decoded choices and even surpass full-scale preference-optimized LLMs.

## Strengths

- The idea of leveraging internal attention signals (QK-scores) for selection and verification is interesting and could contribute to more interpretable and efficient reasoning in LLMs.
- The paper explores multiple tasks (MCQA, verification, hypothesis selection) and provides a calibration-based head selection procedure.
- Reporting permutation accuracy (PA) for MCQA is a good practice to address option-order sensitivity.

## Weaknesses

### Fatal

1. **Selective evaluation in hypothesis selection (Table 4) invalidates the core claim.** The experiment filters out questions where all 8 candidate chains are either all correct or all incorrect, evaluating only on a biased subset (182/259 questions). The baseline accuracy on this subset is only ~32%, which is not representative of overall performance. The reported QK-score improvements (e.g., 53.8% on MATH-500) are therefore not comparable to standard full-dataset evaluations and cannot support the paper’s broader claims.

2. **Unsupported overclaim of surpassing “full-scale, preference-optimized LLMs.”** The paper never compares against any preference-optimized model (e.g., RLHF-tuned, DPO-trained) or any state-of-the-art method (self-consistency, reranking, DoLa, CCS). All baselines are the same model’s own decoded output or a simple consistency baseline. This claim is entirely unsubstantiated and misleading.

3. **Verification experiment (Table 3) uses an extremely weak baseline.** The baseline accuracy for DeepSeek-R1-Distill-LLaMA-8B on MATH-500 is 2%, and for several models on HLE-1/4 it is 0%. This suggests the baseline (presumably the model’s own binary verdict) is essentially random or degenerate. The large QK-score improvements are therefore not surprising and do not demonstrate a meaningful advance without comparison to reasonable verification methods (e.g., self-consistency, process reward models, or even simple logit-based confidence).

### Major

4. **Lack of comparison to existing internal-signal and decoding-time methods.** The related work mentions CCS, DoLa, and select-and-copy heads, but the experiments never compare QK-score selection/verification against these approaches. Without such comparisons, the claimed advantages (e.g., “computation-efficient”, “white-box”) are not empirically supported.

5. **Methodology for QK-score computation is unclear and potentially inconsistent.** The description of which tokens serve as premise-representing and response-representing tokens is vague (e.g., “end-of-line tokens after each of the choices” for MCQA). It is not explained how multiple options are handled in a single forward pass—whether QK-scores are computed for each option separately or jointly. This lack of clarity makes the method difficult to reproduce.

6. **Head selection stability and sensitivity are not analyzed.** The paper selects a single best head on a calibration set but does not study how this selection varies across different calibration splits, model sizes, or tasks. The results could be highly dependent on this arbitrary choice.

### Minor

7. **The paper’s title and framing (“Think First, Then Select and Verify”) overstate the novelty.** The “think first” phase is simply standard CoT prompting; the core contribution is the QK-score selection/verification, which has been explored in prior work (Tulchinskii et al., 2024, 2025). The combination with CoT is incremental.

8. **The verification experiment uses a separate judge model (Qwen3-70B) to determine ground-truth correctness, introducing potential judge bias.** The paper does not report agreement rates or analyze cases where the judge might be wrong.

### Trivial

None.

## Nice-to-Haves

- Compare against self-consistency with majority voting and reranking baselines on the same tasks.
- Evaluate on the full dataset without filtering for hypothesis selection, or justify why filtering is necessary and report unfiltered results.
- Compare against other internal probes (e.g., CCS, DoLa) to contextualize the QK-score’s effectiveness.
- Provide an ablation on the choice of read positions (e.g., end-of-line vs. last token of each option).

## Novel Insights

None beyond the paper’s own contributions. The observation that QK-scores from a single attention head can correlate with answer correctness is already documented in prior work. The paper does not offer a new theoretical understanding or surprising empirical finding that would change how the community thinks about internal representations.

## Suggestions

- Remove or substantially tone down the claim about surpassing preference-optimized LLMs, as it is not supported.
- Re-run the hypothesis selection experiment on the full set of questions (without filtering) and report both filtered and unfiltered results with appropriate baselines.
- Clearly define the QK-score computation for each task, including token indices and how multiple candidates are scored.
- Add comparisons to self-consistency (majority voting) and at least one other internal-signal method (e.g., CCS or DoLa) on the same benchmarks.

## Score and Decision

**Score:** 3  
**Decision:** Reject  

The paper has a promising direction but suffers from fatal experimental flaws (selective evaluation, unsupported overclaims) and major methodological gaps (lack of comparisons, unclear procedure). The core claims are not convincingly demonstrated, and the contribution is not sufficient for acceptance at this venue.

MY FINAL SCORE: <score>3</score>  
MY FINAL DECISION: <decision>Reject</decision>