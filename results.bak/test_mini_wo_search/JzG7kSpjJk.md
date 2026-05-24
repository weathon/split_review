Now I have a thorough understanding of the paper and can cross-check all claims. Let me produce the final review.

## Summary

This paper proposes per-input-channel (per-IC) quantization for weight-only LLM quantization, motivated by the observation that activation outliers affect the input dimension of the weight matrix. Per-IC grouping isolates outliers within a single quantization group rather than spreading their effect across all groups (as in standard per-output-channel grouping). The paper further introduces AdaDim, an adaptive framework that selects per-IC or per-OC per layer by minimizing reconstruction error on a calibration set. Experiments augmenting RTN and GPTQ with AdaDim show consistent improvements across LLaMA-V2 base models, Vicuna, and WizardLM instruction-tuned models on MMLU, commonsense reasoning, math (GSM8k), and code (HumanEval) benchmarks, with reported gains up to +4.7% on MMLU and +10.3% on HumanEval.

## Strengths

1. **Novel per-IC quantization is well-motivated and mechanically sound.** The observation that activation outliers affect the input dimension of the weight matrix, and that grouping along that dimension isolates the outlier effect, is clearly explained (Figure 1, Section 3.2). This is a genuine departure from the standard per-OC grouping convention and is a simple yet non-obvious insight.

2. **Adaptive dimension selection (AdaDim) outperforms heuristic and fixed schemes.** Table 2 empirically demonstrates that the optimization-based selection (minimizing reconstruction error, Eq. 1) gives superior MMLU scores compared to a heuristic-based approach that fixes per-IC application based on offline observation. This confirms that adaptation is more effective than a pre-specified rule.

3. **Consistent gains across diverse models and tasks.** The paper shows improvements not only on LLaMA-V2 base models (Figure 3) but also on instruction-tuned Vicuna (Table 3) and task-specialized WizardLM models for math and code (Table 4). The gains are demonstrated for both RTN and GPTQ augmentation, and across multiple precision/group-size configurations (Figure 4).

4. **Mechanistic analysis supports the core claim.** Figure 6 shows that under per-IC grouping, GPTQ's weight updates are localized to a small number of input channels, whereas per-OC spreads updates across many channels. This provides direct evidence that outlier isolation reduces harmful side effects during quantization, strengthening the paper's explanatory narrative.

## Weaknesses

### Fatal
None.

### Major

1. **Headline 4.7% MMLU claim lacks precise numeric verification in the paper.** The central result — that RTN-ada yields a +4.7% MMLU boost on LLaMA-V2-7B at INT3, surpassing both AWQ and GPTQ — is presented only via Figure 3 (a bar chart) with no corresponding text-based table reporting the exact numeric values for FP16, vanilla RTN, RTN-ada, GPTQ, GPTQ-ada, and AWQ. The exact baselines from which the 4.7% improvement is computed cannot be read precisely from the bar chart. Given that a 4.7% absolute MMLU gain from an already low RTN baseline would bring the quantized model close to or above FP16 performance — an unusually large improvement — the paper should provide a clear numeric table for these results. (The paper does provide numeric tables for Vicuna (Table 3) and WizardLM (Table 4), but not for the base models in Figure 3.)

### Minor

2. **GPTQ adaptation is described only briefly.** Section 3.3 states that "using our per-IC variant simply requires executing the quantization step 1) with per-IC RTN." While this is understandable — the key change is the grouping scheme, not GPTQ's algorithm — the description would benefit from clarifying how the Hessian-based weight updates interact with per-IC grouping and whether the quantization order changes. A short pseudocode or step-by-step description would improve reproducibility.

3. **Calibration set size is not reported.** The paper states "a small calibration set" (Section 3.3) and "we use a small calibration set from the Pile" (Section 4.1) but does not specify the number of samples or sequence length used. Standard practice in the quantization literature (e.g., GPTQ uses 128 sequences of length 2048) and stating this explicitly would aid reproducibility.

### Trivial

4. **No explicit discussion of whether per-IC and per-OC with the same group size (128) yield the same effective precision per weight.** The paper uses group size 128 uniformly, but the number of quantization groups differs between the two schemes (input_dim/128 vs. output_dim/128). The effective bit-width per weight is the same in both cases, but stating this explicitly would preempt questions about fairness of comparison.

## Nice-to-Haves
- Reporting results with statistical uncertainty (e.g., multiple calibration set seeds) would strengthen the credibility of the large gains (+10% on HumanEval), though single-run evaluation is the current norm in this field.
- A quantitative correlation measure between activation outlier magnitude and weight sensitivity (Fisher information) would strengthen the claim that "activation outliers do not dictate quantization difficulty," which is currently supported only by qualitative visualization (Figure 2).

## Removed Points
- "No comparison to SpQR or channel-wise scaling in AWQ" — Removed per rules about missing related work.
- "Section 2.2 discussion is tangential" — Subjective opinion, not a concrete weakness.
- "Computational cost of AdaDim's dimension search not mentioned" — The paper already notes it requires "a very small number of forward passes"; this is adequately addressed.
- "No statistical uncertainty" — Standard practice in the field; moved to Nice-to-Have.

## Novel Insights
None beyond the paper's own contributions. The two reviews present standard critical analysis; no reviewer identified a pattern, connection, or implication not already surfaced by the paper itself.

## Suggestions
1. **Add a numeric table for Figure 3.** Provide a table in the main text (or as a supplementary) with exact MMLU and CSR scores for FP16, RTN, RTN-ada, GPTQ, GPTQ-ada, and AWQ for LLaMA-V2-7B and 13B at w3g128. This would directly address the main weakness.
2. **Expand the GPTQ per-IC description** with a brief algorithmic sketch or pseudocode showing how the quantization order and Hessian-based updates work under per-IC grouping.
3. **Report calibration set size explicitly** (e.g., "128 sequences of length 2048 from The Pile").

## Score and Decision
MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>