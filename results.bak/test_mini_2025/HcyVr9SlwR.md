Now I have all the information I need. Let me synthesize the final consolidated review.

---

## Summary

This paper proposes LNE-Blocking, a two-component method for data contamination in LLMs: (1) using Length Normalized Entropy (LNE) of the model's greedy output as a contamination detector, and (2) using the LNE score to adaptively control a "blocking" operation (suppressing the highest-probability token at the first *k* positions) to produce a less-memorized output for fairer performance evaluation. The method requires only two greedy inferences (one for detection, one for blocked generation), achieving a 25× computational savings over the prior sampling-based method TED. Experiments on code generation (HumanEval) and arithmetic reasoning (GSM8K) with up to four LLMs show that LNE-Blocking often achieves lower performance gap (PG) relative to the original model, especially on heavily contaminated models where TED fails.

## Strengths

- **LNE is a principled and effective contamination detector on mild contamination.** Table 1 shows LNE achieves F1=0.775 and AUC=0.758 on mild contamination, significantly outperforming Min-k% (0.706/0.717), Perplexity (0.627/0.728), and CDD (0.648/0.674) with p<0.01. This is a clean result because mild contamination is the hardest detection regime, and the improvement is statistically verified.

- **LNE-Blocking achieves strong mitigation with 25× lower inference cost vs. TED.** The method requires only two greedy passes compared to TED's 50 sampling rounds, while on most heavily contaminated models it achieves substantially lower PG (e.g., CodeLlama avg PG 0.037 vs. TED's 0.129; Llama 3.1 GSM8K heavy PG 0.065 vs. TED's catastrophic 0.694).

- **Ablation confirms adaptive LNE-based blocking outperforms fixed alternatives.** Table 4 shows LNE-Blocking (avg PG 0.037) beats all fixed blocking strategies (PG 0.041–0.097) and PPL-Blocking (PG 0.042), demonstrating that using LNE to adjust blocking intensity per sample is genuinely beneficial and not an artifact of simply adding a blocking step.

- **The method is clean and easy to implement.** The blocking operation and LNE computation are mathematically simple (Equations 1, 7, 10), requiring no dataset modification, no training, and no external models — unlike CleanEval (paraphrasing) or TED (50× sampling). This pragmatic engineering contribution is valuable for practitioners.

## Weaknesses

### Major

- **Contamination detection evaluated on only one model–task pair.** The detection experiments (Table 1) use only CodeLlama on HumanEval. The paper claims "SOTA performance for contamination detection" (abstract, Section 1), but this claim is unsupported for other models (CodeGen, Llama 2, Llama 3.1) and the GSM8K task. Without detection experiments on the same models used for mitigation evaluation, it is unclear whether LNE generalizes as a detector, and the detection claim is overbroad.

- **PG metric's ground-truth assumption is partially unverifiable.** The Performance Gap metric (Equation 12) defines ground truth as the original (pre-contamination-simulation) model's performance. For HumanEval, the paper asserts the datasets were "handwritten to ensure to be excluded from the training set" — this is reasonable. But for GSM8K, the paper itself notes (Section 5.1) that the original models are "possibly subjected to contamination by the test set of the GSM8K dataset." This means the PG metric for GSM8K measures restoration to a potentially *already-contaminated* baseline, not true generalization. The authors should discuss how this affects the GSM8K results.

- **No variance or confidence intervals reported for any mitigation result.** Tables 2 and 3 report point estimates without standard deviations, even though TED involves stochastic sampling (50 random draws) and could vary across runs. LNE-Blocking is deterministic given the random seed, but the comparison requires knowing whether the reported PG differences (e.g., 0.020 vs. 0.037 on Llama 2) are reliable. Without variance, the reader cannot assess significance.

- **Hyperparameters β and Threshold_Task lack sensitivity analysis.** β=2 is justified only as "works the best" with speculation about "even distribution." Threshold_Task (4 for code, 7 for math) is asserted to be task-dependent but model-independent without evidence. No sensitivity analysis is provided, so it is unclear how brittle the method is to these choices or whether the reported superiority over fixed blocking depends on tuning these parameters on the same evaluation data.

### Minor

- **No experimental comparison with CleanEval.** CleanEval (Zhu et al., 2023) is mentioned in related work as a paraphrasing-based mitigation method, but no experimental comparison is provided. The paper motivates LNE-Blocking partly as not requiring dataset modification, but including CleanEval would contextualize the practical trade-offs.

- **Different contamination simulation regimes across models.** CodeGen, Llama 2, and CodeLlama use LoRA weights from TED (mixing HumanEval test set with StarCoder at 1:1000), while Llama 3.1 uses continued pretraining with only the test set. These are different contamination mechanisms (LoRA adapter vs. full-weight continued pretraining) with different data mixtures. The paper should discuss whether the comparison across models trained under different regimes is apples-to-apples.

- **No discussion of the logit-access requirement.** LNE requires the full probability distribution over the vocabulary (Equation 1). Many API-based LLM services do not expose logits. The paper does not discuss this limitation, which restricts the method's applicability to open-weight models or local deployments.

- **Mild contamination case on Llama 3.1 GSM8K shows LNE-Blocking underperforms TED (PG 0.114 vs. 0.018).** The paper acknowledges this briefly but should discuss it as a known failure mode: on mild contamination, the adaptive blocking may over-apply and degrade performance more than sampling-based diversity helps.

### Trivial

- Figure 1 uses a dual axis (ROUGE-L left, LNE right) with different scales, which is noted in the caption but could mislead a casual reader into comparing the absolute values directly.

## Nice-to-Haves

- A sensitivity analysis on β (e.g., {1, 1.5, 2, 2.5, 3}) and Threshold_Task (e.g., {2, 4, 6} for code, {3, 5, 7, 9} for math) showing PG variation.
- Detection experiments on at least one additional model–task pair (e.g., Llama 3.1 on HumanEval, or Llama 2 on GSM8K) to support the general-purpose detection claim.
- A practical discussion of how to set the detection threshold ξ (Equation 2) without access to labels (e.g., using a held-out set or a reference model).
- Analysis of failure cases where blocking produces invalid or degraded outputs (e.g., syntax errors from blocked function names).

## Removed Points

These points are flagged to be removed — treat them with caution.

- *"PPL is computed on the ground-truth answer, while LNE is computed on the model's own output"* — The paper defines PPL (in detection) as "the perplexity of the response generated by the model through greedy decoding" (Section 6.1). PPL-Blocking in the ablation replaces LNE with this same PPL score. The comparison is apples-to-apples; the criticism is based on a misunderstanding.
- *"Figure 1 would benefit from stating that the LNE axis is separate"* — The figure caption already describes the dual-axis setup explicitly ("ROUGE-L (left y-axis, 0.3 to 1.0) and Length Normalized Entropy (LNE) (right y-axis, 0.0 to 0.6)"). This is a presentation nitpick that does not affect evaluation.
- *"The decreasing trend for LNE as contamination increases is correct under the hypothesis"* — This is not a weakness; it is restating what the figure shows.
- *"Missing details about training hyperparameters"* — The paper already reports key training details: learning rate 1e-4, 20 epochs, single 4090 GPU, LoRA (Section 5.2). Additional hyperparameters (batch size, optimizer) are standard and can be found in the cited TED work.
- *Criticisms that question the existence or release status of models/tools* — These are not valid per the review guidelines.
- *Generic format/style nitpicks about citation formatting* — The guidelines explicitly remove these.

## Novel Insights

None beyond the paper's own contributions. The reviews surface known evaluation-compliance gaps (single-model detection evaluation, missing variance) but do not identify strengths or weaknesses that the paper itself does not discuss or imply.

## Suggestions

1. **Expand detection experiments** to at least one more model (e.g., Llama 3.1) and GSM8K, or narrow the SOTA claim to the CodeLlama/HumanEval setting where it is supported.
2. **Add standard deviations** (over multiple evaluation runs) to all mitigation tables so the reader can assess whether reported PG differences are reliable.
3. **Provide a sensitivity analysis** for β and Threshold_Task, or propose a principled way to set them (e.g., based on response length distribution).
4. **Discuss the GSM8K ground-truth issue explicitly** — acknowledge that if the original models already contain GSM8K in pretraining, the PG metric is relative to a contaminated baseline, and explain how this affects interpretation.
5. **Include CleanEval** as a baseline, or explain clearly why the comparison is omitted (e.g., it modifies the dataset, which is a different paradigm).

## Score and Decision

**Bracketing analysis (Round 1):** The three band searches returned:
- Weak band (avg < 3.5): Papers scored 2.0–3.0 — clearly reject, with incomplete or flawed methodology. The current paper is stronger.
- Middle band (3.5–7.5): Most relevant anchors — "Time Travel in LLMs" (7.0, spotlight), "To the Cutoff... and Beyond" (6.75, poster), "User Inference Attacks" (5.5, reject), "Online Detection" (5.25, reject), "Elephants Never Forget" (4.75, reject). The current paper sits between 4.75 and 7.0.
- Strong band (>7.5): Papers scored 7.6–9.5 — orals and top posters. The current paper is not at this level.

**Round 1 bracket:** 4.5–6.5.

**Narrowing analysis (Round 2):** Within (4.5, 6.5), additional anchors include "Self-Detoxifiers" (6.0, poster), "L-Eval" (6.0, reject), "Online Detection" (5.25, reject), "MAP's not dead yet" (5.25, reject), and "HelloBench" (4.75, reject).

- vs. "Self-Detoxifiers" (6.0, poster): That paper has strong multi-model, multi-dataset experiments with clear metrics. The current paper has a more limited evaluation scope, missing variance and detection breadth. Weaker overall.
- vs. "Online Detection" (5.25, reject): Both papers propose detection methods with evaluation gaps (missing baselines in that case, limited model coverage here). The current paper has a stronger ablation study and a clear speedup claim, making it slightly stronger.
- vs. "Elephants Never Forget" (4.75, reject): That paper had vague methodology descriptions and unclear validation. The current paper has a much clearer method and better ablation, making it stronger.

**Final score:** 5.0. The paper has a clean, novel idea and the ablation study is convincing, but the detection evaluation is too narrow to support the SOTA claim, the PG ground-truth issue is real, and the lack of variance reporting weakens the mitigation comparisons. These are structural gaps that prevent the paper from meeting the acceptance threshold in its current form.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>