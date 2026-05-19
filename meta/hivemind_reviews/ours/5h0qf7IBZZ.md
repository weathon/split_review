## Summary
This paper proposes MiniLLM, a white-box knowledge distillation method for LLMs that replaces the standard forward KL divergence objective with reverse KL divergence. The authors derive a policy-gradient-based optimization for this objective and introduce three stabilization strategies: single-step decomposition, teacher-mixed sampling, and length normalization. Experiments across GPT-2, OPT, and LLaMA families (120M to 13B parameters) on five instruction-following datasets show consistent improvements over SFT, word-level KD, and sequence-level KD baselines on Rouge-L, GPT-4 feedback, and human evaluation.

## Strengths
- **Well-motivated diagnosis of forward KL's limitations for generative LLM KD.** The paper clearly identifies why standard forward KL minimization is suboptimal for generative language models — it forces a low-capacity student to overestimate low-probability void regions of the teacher's complex distribution. The toy experiment (Figure 2) provides concrete intuition, and the connection to mode-seeking behavior of reverse KL is convincingly argued (Section 2.1).

- **Consistent superiority across extensive controlled experiments.** Table 1 reports results across three model families (GPT-2, OPT, LLaMA), student sizes from 120M to 13B, and five evaluation datasets using both Rouge-L and GPT-4 feedback. MiniLLM outperforms all baselines (SFT, KD, SeqKD) in nearly every configuration (e.g., +9.3 GPT-4 points on SelfInst for OPT 1.3B; +4.2 GPT-4 points on DollyEval for GPT-2 760M; Rouge-L improvements that sometimes surpass the teacher model). The pattern holds across 20+ model/dataset combinations, providing strong cumulative evidence.

- **Validated optimization strategies that are essential for stable training.** The three proposed techniques — single-step decomposition, teacher-mixed sampling, and length normalization — are ablated in Table 5 and Figure 7. Omitting any one degrades performance substantially (e.g., Rouge-L on Dolly drops from 24.6 to 14.7 without length normalization). This evidence directly supports the claim that the optimization approach is effective and non-trivial.

- **Demonstrated reduction in exposure bias.** Figure 3 shows that MiniLLM's excess error (ExAccErr) remains flat near zero after ~150 tokens, while KD, SeqKD, and SFT accumulate error linearly. This directly validates the paper's claim that sampling from the student during training alleviates the training-inference mismatch.

## Weaknesses
### Fatal
None.

### Major

- **No estimates of training variability across runs.** All results in Table 1 come from what appears to be a single training run per configuration. The paper reports averages over 5 *decoding* seeds (line 188), which accounts for evaluation stochasticity but not for training stochasticity (data shuffling, initialization, optimization noise). Without multiple training seeds (3–5) and measures of dispersion (standard deviations or confidence intervals), it is impossible to assess whether the observed improvements — particularly the smaller Rouge-L margins of 1–3 points — are statistically reliable. While the consistency of gains across 20+ configurations partially mitigates this concern, the absence of training replicates remains the most consequential gap in the empirical evidence.

### Minor

- **GPT-4 evaluation metric is underspecified.** The paper states GPT-4 feedback "by asking GPT-4 to compare model-generated responses with the ground truth answers" and reports "the ratio of the total score" citing MT-Bench (line 185). The exact prompt template, scoring rubric, and normalization procedure are not provided. Since this metric accounts for three columns in Table 1, its opacity weakens reproducibility. (That said, MT-Bench is a known methodology, so this is a clarity issue rather than a fatal one.)

- **Ablation study limited to one small model pair (GPT-2 125M → 1.5B).** The effectiveness of the three optimization strategies is demonstrated only on the smallest configuration. It is plausible that their relative importance changes for larger models or larger vocabularies (e.g., the importance weight approximation could become more unstable with wider vocabulary distributions). While the main results show that the full method works at scale, the ablation does not verify that each component is necessary at those scales.

- **Calibration analysis evaluated on classification tasks, not generation.** The ECE evaluation (Table 2) uses SST-2 and BoolQ, which are text classification datasets. The paper's method and main experiments target open-ended instruction-following generation. The transferability of calibration findings across these distinct settings is not justified. Moreover, on BoolQ the teacher itself has ECE 0.356; MiniLLM's 0.502 narrows the gap relative to KD (0.682) and SeqKD (0.681), but the absolute calibration is still poor.

- **Diversity analysis does not directly measure multi-response diversity.** The paper reports Dist-4 and language modeling loss (Table 3) to argue that diversity is preserved, but does not measure per-prompt multi-response diversity (e.g., self-BLEU, number of distinct outputs across 10–20 samples per prompt). The paper's argument that "generating one correct response is sufficient" (line 342) is a reasonable design stance, but the evidence presented does not directly address the concern that reverse KL could cause mode collapse to a single response template.

- **The importance weight approximation $w_t \approx q_\theta(y_t)/\tilde{p}(y_t)$** (dropping the product over previous steps) is justified only by citations (lines 105–106). Its empirical impact on bias versus variance in this specific setting is not analyzed. An ablation isolating this approximation would strengthen confidence in the method.

### Trivial

- **The weight for the language modeling loss $\mathcal{L}_{\text{PT}}$ in the combined gradient update** is not reported. The algorithm adds gradients directly ($\nabla\mathcal{L}_{\text{Single}} + \nabla\mathcal{L}_{\text{Long}}^{\text{Norm}} + \nabla\mathcal{L}_{\text{PT}}$), which implies an implicit weight of 1. Whether this weight was tuned or fixed is unclear.

## Suggestions
1. **Add error bars to Table 1** by running 3–5 training seeds per configuration (at minimum for the core GPT-2 or LLaMA-7B setups) and reporting means and standard deviations. This is the single highest-impact improvement.
2. **Provide the GPT-4 evaluation prompt template and scoring rubric** in the appendix to ensure reproducibility of the metric.
3. **Extend ablation to at least one larger model pair** (e.g., LLaMA-7B → LLaMA-13B) to verify that the three optimization strategies remain necessary at scale.
4. **Add a self-BLEU or distinct-n analysis** over multiple samples per prompt to directly measure multi-response diversity.
5. **Clarify the $\mathcal{L}_{\text{PT}}$ loss weight** and report the hyperparameter search space for validation-Rouge-L-based tuning.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept
