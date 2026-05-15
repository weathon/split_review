Here is my consolidated final review:

---

## Summary

This paper proposes DCoND (Divide-and-Conquer Neural Decoder), a framework for decoding attempted speech from neural activity. The key idea is to model phoneme probabilities by marginalizing over diphone probabilities (pairs of adjacent phonemes), motivated by neuroscientific evidence that neural representations of phonemes are context-dependent. The paper further augments an existing LLM-based ensemble method (LISA) by including decoded phoneme sequences alongside transcription candidates in the prompt to GPT-3.5. On the Brain-to-Text 2024 benchmark, DCoND achieves 15.34% PER (vs. 16.62% for the monophone baseline) and, when combined with LLM fine-tuning (DCoND-LIFT), achieves 5.77% WER (vs. 8.93% for LISA, the prior SOTA).

## Strengths

- **Novel diphone-marginalization strategy grounded in neural coarticulation**: The paper introduces a principled formulation where phoneme probabilities are obtained by summing over diphone probabilities, directly addressing the context-dependent nature of phoneme encoding. This is conceptually clean and architecture-agnostic — it can be plugged into any neural decoder. The t-SNE visualizations (Figure 4C–D) provide qualitative support that diphone-trained latent spaces form more condensed and separable clusters than monophone-trained ones.

- **Systematic ablation on context representations**: The paper compares diphone against triphone at multiple class sizes (K=50,100,200) and a grouping baseline (Table 2). This ablation helps explore the design space of context-dependent representations and reveals an interesting finding: triphone K=100 achieves better PER (15.02%) than diphone (15.34%) but worse WER (9.67% vs. 8.06%), suggesting that representation quality at the phoneme level does not always translate to better word-level decoding.

- **Resource-efficient ICL alternative**: DCoND-LI achieves 7.29% WER using only 25 ICL exemplars with no fine-tuning, providing a practical option when access to LLM fine-tuning is constrained.

- **Inclusion of P-WER metric**: The paper evaluates perceptual word error rate (P-WER) using speech synthesis + ASR, showing DCoND-L achieves 8.02% P-WER vs. 11.33% for NPTL — a meaningful measure of how improved phoneme decoding translates to intelligible speech.

## Weaknesses

### Fatal
None.

### Major

- **Uncontrolled capacity confound between diphone and monophone decoders**: The diphone decoder outputs 40² = 1,600 classes versus the monophone baseline's 40 classes, making the final linear layer roughly 40× larger. The paper attributes the PER improvement (16.62% → 15.34%) to "context-aware diphone modeling," but the comparison is confounded — the diphone model has substantially more parameters in its output layer. The paper claims DCoND-L uses the "same backbone, RNN decoder and LMs, as NPTL" (line 182), but this is only true for the recurrent hidden layers; the output projection is necessarily larger. Without a capacity-controlled baseline (e.g., increasing the monophone model's hidden size or adding layers to match parameter count), it is unclear how much of the improvement comes from the linguistic motivation versus simply having a larger model. That said, the triphone ablation partially mitigates this concern: triphone K=100 has an even larger output space yet achieves worse WER (9.67% vs. 8.06%), suggesting more parameters alone do not explain the diphone advantage. The paper would be substantially strengthened by adding a controlled comparison.

### Minor

- **LLM-based ensemble component is an incremental modification**: The headline WER result (5.77%) includes the GPT-3.5 fine-tuning step, which is a modest modification of the existing LISA method — adding phoneme sequences to the prompt. The paper honestly frames this as an "augment[ation]" (line 28), but the abstract and conclusion present the 5.77% WER as the primary result without clearly separating the diphone decoder contribution (8.06% WER without GPT-3.5) from the LLM contribution. The novel conceptual contribution is DCoND; the LLM part is an engineering improvement.

- **No statistical significance or variance estimates for PER**: The 1.28-point PER improvement (16.62% → 15.34%) is reported without confidence intervals, error bars, or significance tests. For a 1,200-sentence test set, this gap could be within the noise range. While single-run evaluation on a fixed benchmark is standard in this field, reporting bootstrap confidence intervals would substantially strengthen the claim.

- **t-SNE analysis of neural representations uses a semi-circular alignment procedure**: The paper aligns neural activity segments using DTW with timestamps from decoded phonemes (line 190), then shows that these aligned segments form context-dependent clusters. Because the alignment itself depends on the decoded outputs, the observation of clustered structure is somewhat tautological. This does not invalidate the main decoding results, but the neural evidence claim is weaker than presented.

- **Explanation for triphone's better PER but worse WER is hand-wavy**: The paper attributes triphone's lower WER to "distribution mismatch with the 5-gram model" (line 246), but provides no analysis of the output phoneme distributions (e.g., entropy, per-class confidences) to support this. The non-monotonic relationship between PER and WER across representations (diphone, triphone) merits deeper investigation.

- **Limited justification for why only the *preceding* phoneme is sufficient context**: The formulation in Equation 1 uses a general context variable S, but the work concretizes S as the immediately preceding phoneme (diphone). The paper does not argue why longer-range dependencies (e.g., following phoneme, word boundaries) are not needed, beyond an empirical comparison with triphone. This is an acceptable design choice, but the paper overclaims the neuroscientific grounding for this specific operationalization.

### Trivial

- The α ablation results (Table: α=0.2→8.47% WER, α=0.4→8.70%, α=0.6→8.06%, α=0.8→8.64%) are non-monotonic, suggesting sensitivity to noise in single-run evaluation. The paper treats α=0.6 as clearly optimal without commenting on this variance.

- The exact WER of the "DCoND-LIFT w/o P" ablation (Figure 5) is not reported in the text, making it hard to quantify the marginal benefit of phoneme inputs in the LLM prompt.

## Nice-to-Haves

- **Capacity-controlled baseline**: Adding an experiment where the monophone decoder is given a matched-parameter output stage (e.g., larger hidden size or an additional layer to compensate for the smaller output) would cleanly separate the effect of diphone representation from increased model capacity.

- **Bootstrap confidence intervals on PER**: Even a simple 1,000-sample bootstrap over the test set would help establish whether the 1.28% PER gap is statistically reliable.

- **Deeper analysis of triphone vs. diphone behavior**: Examining output phoneme distributions (entropy, per-phoneme accuracy breakdowns) could clarify why triphone achieves better PER but worse WER when decoded through the same 5-gram LM.

## Removed Points

*These points are flagged to be removed — treat them with caution.*

- "LISA does not report PER or P-WER, so the comparison is incomplete": Removed because this is a limitation of the baseline paper, not a flaw in the current paper. The authors report all available metrics for all baselines.
- "Confusion matrix claims 'accuracy greater than 80%' but these are diagonal entries": Removed — this is standard usage of confusion matrix terminology; the paper reports PER as the aggregate metric, which is standard for the field.
- "CTC loss on diphone and monophone sequences have different lengths which is not treated": Removed — CTC is designed to handle alignments of arbitrary lengths; the paper explicitly defines T'' = 2T' and CTC handles this naturally.
- "Marginalization notation is ambiguous": Removed — the paper clearly defines the context variable S as the preceding phoneme and the marginalization as summing over diphone joint probabilities column-wise (Figure 2A, line 112).
- "ICL vs. fine-tuning comparison is not controlled for data volume": Removed — the paper explicitly acknowledges these are different operating regimes for different resource constraints (line 261).
- "The paper does not give exact WER for DCoND-LIFT w/o P": This information is in Figure 5, which is a figure; the text describes the trend. Minor presentation choice.
- Various formatting and stylistic nitpicks: Removed as they are parser artifacts.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation that the paper itself missed — they primarily sharpen methodological concerns about experimental controls and attribution of improvements.

## Suggestions

1. **Add a capacity-controlled baseline**: Train a monophone decoder with a wider hidden layer or an additional projection layer to match the parameter count of the diphone decoder's output stage. If the gap narrows or disappears, the claim of diphone superiority weakens; if it persists, the core claim is substantially reinforced.
2. **Report statistical significance**: Add bootstrapped 95% confidence intervals for PER and WER on the test set to show the 1.28% PER gap is reliable.
3. **Separate the two contributions more clearly**: State explicitly in the abstract and conclusion which results come from DCoND alone (8.06% WER) versus DCoND + LLM fine-tuning (5.77% WER), so the reader can appraise the diphone decoder's standalone value.
4. **Provide a deeper analysis of triphone's PER-WER discrepancy**: Compute per-phoneme accuracy and output distribution entropy for diphone and triphone models to better understand why triphone's better PER does not translate to better WER.
5. **Report the exact WER for DCoND-LIFT w/o P** in the text or table, so the marginal contribution of phoneme inputs in the LLM prompt can be precisely quantified.

## Score and Decision

The paper introduces a novel and principled diphone-marginalization strategy for brain-to-text decoding and achieves SOTA results on a meaningful benchmark. The main weaknesses are (a) a capacity confound in the core comparison that prevents clean attribution of the PER improvement to diphone modeling, and (b) an LLM component whose novelty is incremental. The former is partially mitigated by the triphone ablation. Overall, the contribution is real but the central claim needs stronger experimental support.

**Score**: 6.0

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>