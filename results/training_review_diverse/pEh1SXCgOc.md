Now I have sufficient information to verify each claim against the paper. Let me construct the consolidated review.

## Summary

This paper proposes DCoND (Divide-and-Conquer Neural Decoder) for brain-to-text decoding, which replaces direct phoneme decoding with diphone (two-phoneme transition) prediction followed by marginalization to obtain phoneme probabilities—motivated by coarticulation in neural speech representations. The approach is coupled with LLM-based refinement (GPT-3.5 via ICL or fine-tuning) that jointly processes phoneme and word candidates. On the Brain-to-Text 2024 benchmark, DCoND-LIFT achieves 5.77% WER versus 8.93% for the prior leading method (LISA), with consistent gains across PER and P-WER.

## Strengths

1. **Diphone-based divide-and-conquer decoding yields clear phoneme accuracy gains.** The proposed DCoND achieves a PER of 15.34% compared to 16.62% for the monophone baseline (NPTL, Table 1), and the latent-space visualization (Figure 4C vs. 4D) shows that diphone training produces more compact and separable clusters—directly validating the method's ability to reduce nonlinearity in phoneme decoding.

2. **Including phoneme sequences in the LLM ensemble produces a large WER improvement over prior SOTA.** DCoND-LIFT achieves 5.77% WER, substantially improving upon LISA's 8.93% (Table 1). The ablation in Figure 5 confirms that including predicted phonemes (DCoND-LIFT vs. DCoND-LIFT w/o P) is the key factor.

3. **Systematic ablation of alternative context representations.** The ablation study (Table 2) compares diphone against multiple triphone configurations (K=50,100,200) and a grouping method, showing that diphone achieves the best WER (8.06%) and that poorly chosen class definitions degrade performance. This thorough comparison strengthens the claim that diphone strikes the right balance.

4. **Two LLM modes with clear trade-off characterization.** The paper demonstrates both an ICL mode (DCoND-LI, 7.29% WER) and a fine-tuning mode (DCoND-LIFT, 5.77% WER), with Figure 5 showing that WER decreases monotonically as ICL context length increases. This provides practitioners a principled choice between resource efficiency and accuracy.

## Weaknesses

### Fatal

None.

### Major

- **Ambiguity in the training objective (Section 3, Eq. 3).** The paper defines $\mathcal{L}_c$ (single-phoneme CTC loss, using notation $p_m$) and $\mathcal{L}_s$ (diphone CTC loss, using $p$), then combines them as $\mathcal{L} = \alpha\mathcal{L}_c + (1-\alpha)\mathcal{L}_s$. The marginalization (summing diphone probabilities column-wise to obtain phoneme probabilities) is described for inference, but it is unclear whether $\mathcal{L}_c$ is computed from the marginalized diphone probabilities (making it a regularizer derived from the same output head) or from a separate monophone output head. The notation $p_m$ vs. $p$ hints at distinct distributions but this is never stated explicitly. This ambiguity directly affects understanding of whether the "divide-and-conquer" claim holds as stated or whether the method is better characterized as multi-task learning with a shared diphone representation. Authors should specify: (a) exactly which probabilities feed each CTC loss, (b) whether a separate output head exists, and (c) why both terms are needed if marginalization already yields phoneme probabilities.

### Minor

- **Single-subject evaluation without variance reporting.** All results come from a single subject (the standard Brain-to-Text 2024 benchmark dataset). While this is inherent to the dataset and common in BCI work, the paper reports no confidence intervals, standard deviations across training seeds, or significance tests. A WER improvement from 8.93% to 5.77% is substantial, but the reader cannot assess whether a single favorable initialization drives part of the gain. Reporting mean ± std over at least 3 random seeds for PER and WER would substantially strengthen reliability.

- **Circularity in the neural visualization alignment (Section 4, Fig. 4A).** The t-SNE visualization uses DTW to align ground-truth phonemes to neural segments "according to the timestamps obtained from the decoded phonemes." Because the alignment depends on the decoder under evaluation, the resulting clusters may partly reflect decoder biases rather than genuine neural structure. This does not invalidate the main results, but the claim about "context-dependent nature of phonemes in neural representations" would be stronger with an independent alignment method or an explicit acknowledgment of this limitation.

- **Missing α annealing schedule.** The paper states that α "is designed to be small at the beginning and gradually increase over the course of training" (line 127) but provides no schedule (e.g., linear ramp, start/end values, number of epochs). This is a nontrivial hyperparameter for a dual-loss setup. The final value is reported (α=0.6 from a grid search over static values), but the dynamics and whether the schedule ends at this value are unspecified.

### Trivial

- **Diphone sequence length example inconsistency.** The paper states $T'' = 2T'$ but the "hope" example (3 phonemes) yields 7 diphones, not 6—because the diphone representation includes leading SIL and self-transitions. The actual mapping appears to be $2T' + 1$. This does not affect the method but should be corrected.

## Nice-to-Haves

- A brief discussion of computational cost: diphone output (1600 classes) is much larger than phoneme output (40 classes). Reporting training time, memory usage, and any class imbalance handling would help practitioners.
- Confirming whether the reported results are the best known on the Brain-to-Text 2024 leaderboard (or discussing any other submitted methods beyond NPTL and LISA) would strengthen the SOTA claim.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Missing hyperparameter details (learning rate, batch size, optimizer, etc.)**: The parser strips appendix material from all papers; these details likely exist in the original submission. Removed per hard rule about missing appendix content.
- **P-WER formula negativity concern**: The formula is adopted from prior work (Metzger et al., 2023), all reported values are positive and well-behaved. The hypothetical scenario where WER_Whisper-P < WER_Whisper-GT would produce a negative P-WER, but this does not occur in the paper's results and is not a flaw in the paper's own analysis.
- **Demand for comparison with all benchmark methods**: The paper compares against the two leading prior methods (NPTL and LISA) recognized in the benchmark. This is a sufficient comparison set.

## Novel Insights

The most interesting structural observation emerging from the reviews is the tension between the "divide-and-conquer marginalization" framing and the actual dual-loss training objective. If $\mathcal{L}_c$ is computed from marginalized diphone probabilities, then the method is best understood as multi-task learning: the diphone loss ($\mathcal{L}_s$) provides fine-grained discriminative signal across 1600 classes, while the phoneme-level loss ($\mathcal{L}_c$) constrains the marginalization to produce accurate phoneme posteriors. This is a genuine innovation over pure phoneme CTC (NPTL) and over pure diphone CTC (which would require a separate decoding scheme), but the paper's framing as "divide-and-conquer marginalization" undersells the multi-task nature. Resolving this framing/implementation gap is the single most actionable revision.

## Suggestions

1. Clarify the training objective unambiguously. Provide a diagram or pseudocode showing whether the neural decoder has one output head (diphone) with marginalization feeding $\mathcal{L}_c$, or two output heads. If it is the former, explicitly state that the method is a multi-task learning approach where $\mathcal{L}_c$ regularizes $\mathcal{L}_s$ toward correct marginalization.
2. Report mean ± std over at least 3 random seeds for the primary metrics (PER, WER) in Table 1.
3. Provide the α annealing schedule (start value, end value, number of epochs, functional form).
4. Acknowledge the circularity limitation in the t-SNE alignment or use an independent alignment method.

## Score and Decision

The paper presents a novel, well-motivated decoding strategy (diphone marginalization) with strong empirical results on a realistic benchmark—outperforming the prior SOTA by a substantial margin (5.77% vs. 8.93% WER). The core contribution is clear and valuable. The main weaknesses are a genuine ambiguity in the training objective formulation and the absence of variance estimates, neither of which undermines the core empirical finding. These are addressable in revision. The paper is a solid contribution to the BCI/neural decoding community.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>