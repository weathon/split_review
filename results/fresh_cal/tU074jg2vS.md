Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes a hierarchical autoregressive transformer that processes text at two levels — a small character-level encoder maps each word's bytes to a single embedding, a causal backbone operates on the resulting word sequence, and a small decoder outputs next-character probabilities. The approach eliminates the need for a learned subword tokenizer while retaining the sequence-length compression of token-level processing. At scales up to 7B parameters, the hierarchical model matches a compute-matched BPE baseline on 17 zero-shot downstream tasks while showing substantially better robustness to input perturbations and superior adaptation during cross-lingual continued pretraining (1.9× faster, higher German scores, better English retention).

## Strengths

1. **Hierarchical architecture matches tokenizer-based baselines at 7B scale.** Table 1 reports performance across 17 zero-shot tasks at 1B, 3B, and 7B scales. The paper states "Across scales and evaluation tasks, both architectures perform similarly" — a claim well-supported by the data. The single large outlier (Lambada, +68% relative at 7B) favors the hierarchical model and does not undermine the match claim.

2. **Robustness advantage is clearly demonstrated and quantified.** Figure 4 shows the average accuracy drop across five tasks for four perturbation types (permute, randomize, delete, all-caps). The hierarchical model consistently degrades far less; for all-caps the baseline loses roughly 3× more accuracy. Table 3 provides concrete generation examples illustrating the effect.

3. **Cross-lingual continued pretraining shows a clear practical win.** Section 4.5 (Figure 5) demonstrates that on German continued pretraining, the hierarchical model achieves higher German evaluation scores while retaining more English knowledge. Because the BPE tokenizer fragments on German text, the hierarchical model trains 1.9× faster, seeing nearly twice as many examples at the same FLOP budget.

4. **Controlled comparison against MegaByte and fixed-split ablation.** Section 4.3 compares against MegaByte and an 8-byte-split variant of the proposed architecture. The hierarchical model with whitespace splitting outperforms both, showing that the architecture itself (not just the hierarchical design) contributes to performance and that semantic splitting provides a useful inductive bias.

5. **Systematic architecture sweep.** Section 4.1 sweeps encoder/decoder sizes across multiple backbone sizes, reporting both word and byte accuracy. The identification of a trade-off (byte accuracy favors larger modules, word accuracy favors larger backbone) and the transparent choice of word accuracy as the guiding metric are methodologically sound.

## Weaknesses

### Fatal
None.

### Major
- **Compute-matching formula is a known simplification that could benefit from empirical validation.** The paper matches models using the approximation FLOPs ∝ S·P (Section 2.3), which assumes feed-forward operations dominate attention. This is a *standard* simplification in the field and the paper explicitly acknowledges it as such. However, at 7B scale with sequence lengths up to ~4k tokens, attention FLOPs are non-negligible (roughly 25–33% of total FLOPs depending on sequence length). Moreover, the attention/FF ratio differs between the two architectures because the hierarchical backbone processes shorter sequences (words) than the baseline (tokens). Importantly, this means the linear approximation *overcounts* the hierarchical model's FLOPs relative to the baseline — if the matching is inaccurate, it likely favors the baseline, not the hierarchical model. That said, even a modest miscalibration (e.g., 10–15%) would not change the paper's qualitative conclusions. Providing wall-clock time per step or measured FLOPs as validation would substantially strengthen the fairness claim. The paper cites an appendix for additional methodology details, but the core concern — about the formula's accuracy — can be evaluated from the main text.

### Minor
- **The Lambada outlier is noted but not analyzed.** The hierarchical model outperforms the baseline by up to 68% relative on Lambada at 7B scale, which is far larger than any other task difference. The paper correctly reports this as a "notable win" but offers no discussion of *why* Lambada benefits so disproportionately. Lambada is a last-word-prediction task that operates at precisely the word-level granularity of the hierarchical model's decoder. A brief analysis — even a hypothesis — would help readers assess whether this reflects a genuine architectural advantage or a task-specific artifact. The core claim ("similar performance across tasks") does not depend on Lambada being representative, so this is a gap in exposition, not a threat to validity.

- **The architecture sweep relies on an unvalidated metric choice.** Section 4.1 selects encoder/decoder sizes based on word accuracy, "which we hypothesized to be a better predictor of model quality." The reasoning (byte accuracy can be improved by making the decoder better at completing words given the first few characters, without improving word accuracy) is sensible, but no downstream validation is provided to confirm that word accuracy ordering correlates with actual task performance. The paper is transparent about this being a hypothesis, which mitigates the concern, but a single sanity check (e.g., word accuracy vs. HellaSwag score across sweep configurations) would make the architecture decisions more convincing.

### Trivial
- Table 1's caption mentions "17 standard downstream tasks" but the main text lists only a few by name. A complete list (with evaluation settings) would improve readability.
- Footnote references in the extracted text appear truncated (e.g., "Details on the compute matching methodology may be" cuts off). Presumably these resolve in the full submission including the appendix, but in the main text the cross-references are slightly awkward.

## Nice-to-Haves
- **Inference speed measurements:** The paper discusses KV-cache parity and a caching scheme for word embeddings but provides no empirical measurements of inference throughput or latency. Including these would strengthen the practical adoption argument.
- **Per-task standard deviation or scatter plot:** A visualization showing the distribution of per-task differences (with Lambada highlighted) would allow readers to instantly see whether Lambada is the sole outlier or part of a broader pattern.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **"Hyperparameter and eval suite details are referenced to an appendix that is not present."** — Removed per rule: the parser strips appendices from all papers; these details exist in the original submission.
- **"Statistical significance: reporting confidence intervals or error bars."** — Removed: single-run evaluation on established benchmarks is the norm in large-scale LM pretraining, and this request goes beyond standard practice for this paper class.
- **"The compute-matching formula may give the hierarchical model more compute"** (specific framing from the harsh critic). — This claim is factually reversed: because the baseline's sequences are longer, it has proportionally more attention FLOPs, meaning the S·P approximation *underestimates* baseline compute relative to the hierarchical model. The criticism as stated is incorrect. The underlying concern (lack of empirical validation) is retained in Major Weaknesses above in corrected form.

## Novel Insights

The harsh critic's suspicion that the compute-matching formula's linearity assumption might systematically favor one architecture is reversed under analysis: attention FLOPs are a larger fraction of total FLOPs for the baseline (longer sequences), so the S·P approximation likely *overestimates* hierarchical FLOPs relative to the baseline, not the reverse. This means the comparison, if anything, is conservative — the hierarchical model matches the baseline with possibly less compute than the formula assumes. The Lambada outlier bridges to a deeper observation: word-level supervision from the backbone directly targets the operation needed for cloze-style last-word tasks, while the baseline's subword-level supervision must compose predictions across multiple tokens. This architectural alignment may explain not just the Lambada improvement but also a general advantage on tasks requiring precise lexical prediction.

## Suggestions

1. Add a brief paragraph analyzing the Lambada result — even a hypothesis (e.g., word-level supervision aligns better with last-word prediction than subword-level supervision) would substantially improve exposition.
2. Include a wall-clock time per step comparison (or measured FLOPs) for at least one scale to empirically validate the compute-matching formula.
3. Add a citation-free listing of the 17 evaluation tasks and their evaluation settings in the main paper.
4. Explicitly note in Section 4.1 that the word-accuracy metric choice, while motivated, was not validated against downstream tasks — and consider adding a simple correlation plot as a sanity check.

## Score and Decision

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>