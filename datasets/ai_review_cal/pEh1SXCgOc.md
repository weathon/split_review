- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3
Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Final Consolidated Review

---

## Summary

This paper introduces a divide-and-conquer neural decoder (DCoND) for brain-to-text decoding. The core insight is that neural representations of phonemes are context-dependent (coarticulation), so the authors propose to first decode diphones (two-phoneme sequences) and then marginalize over the diphone distribution to obtain phoneme probabilities. On the Brain-to-Text 2024 benchmark (single participant with ALS), DCoND with a 5-gram+OPT language model achieves 15.34% PER and 8.06% WER, improving over the monophone-based NPTL baseline (16.62% PER, 9.46% WER). When combined with a fine-tuned GPT-3.5 ensemble that includes predicted phoneme sequences alongside transcription candidates, WER drops further to 5.77%, outperforming the prior best LISA system (8.93% WER). An in-context learning variant provides a resource-efficient alternative with 7.29% WER.

## Strengths

- **Controlled comparison isolates the diphone contribution.** DCoND-L uses the exact same RNN backbone, 5-gram model, and OPT re-scorer as NPTL (line 182: "DCoND-L uses the same backbone, RNN decoder and LMs, as NPTL"). The PER improvement from 16.62% → 15.34% and WER improvement from 9.46% → 8.06% are therefore directly attributable to the diphone marginalization strategy, not to architectural confounds. This is clean, controlled evidence for the paper's central claim.

- **Ablation of phoneme inputs in the LLM ensemble cleanly demonstrates their value.** The paper tests DCoND-LIFT (fine-tuned GPT-3.5 with phoneme inputs) against DCoND-LIFT w/o P (without phoneme inputs). The text states this "further boosts the WER from 8.06% to 5.77%" (line 140), isolating the contribution of providing phoneme sequences to the LLM — a clear ablation that supports the novelty of the ensemble method.

- **Systematic comparison against alternative context representations (triphone) justifies the diphone design choice.** Table "Alternatives for context-dependent phoneme representations" tests triphone at K=50, 100, 200 and a pronunciation-based grouping. While triphone K=100 achieves slightly better PER (15.02% vs. 15.34%), its WER (9.67%) is substantially worse than DCoND-L (8.06%), providing empirical grounding for diphone as the design sweet spot.

- **ICL variant offers a practical, documented trade-off.** DCoND-LI25 achieves 7.29% WER without any weight updates, with systematic scaling from 5 to 25 ICL exemplars. This provides a useful resource-accuracy trade-off point for deployment scenarios where fine-tuning GPT-3.5 is infeasible.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by controlled experiments and clear ablation studies; no verified flaw undermines the central contribution.

### Minor

1. **Absence of variance or confidence intervals across runs.** The paper reports single-point PER and WER values with no indication of variability across training runs, random seeds, or cross-validation splits. The PER gap of 15.34% vs. 16.62% (~1.3 pp) is modest, and without variance estimates the reader cannot assess whether this difference would replicate across runs. This is a common practice on this benchmark (NPTL and LISA also report single values), so it does not invalidate the results, but it weakens the statistical grounding of the "state-of-the-art" claim. The paper would be strengthened by reporting means and standard deviations over multiple seeds.

2. **Alpha annealing schedule is underspecified.** The paper states that α in the combined CTC loss "is designed to be small at the beginning and gradually increase over the course of training" (line 127) but provides no details on the schedule (linear? stepwise? at which epochs? final value?). This is a reproducibility gap for the core training procedure.

3. **Generalizability not discussed.** The evaluation is on a single participant with ALS from a single recording site (ventral premotor cortex). While single-subject evaluation is standard in BCI research, the paper does not acknowledge this as a scope limitation or discuss how the method might transfer to other participants, recording modalities, or speech-production tasks. The abstract and conclusion present the results as a general advance without this caveat.

4. **LISA comparison is system-level, not component-controlled.** The paper states DCoND-LIFT achieves 5.77% WER vs. LISA's 8.93% (a large improvement), but notes only that LISA "also uses RNN as phonemes decoder" (line 180) without specifying whether LISA's RNN architecture matches DCoND's. The paper's primary controlled comparison is DCoND-L vs. NPTL (same backbone), which is properly handled. The LISA comparison is a full-system leaderboard result — legitimate but not isolating which component (diphone decoder, phoneme-augmented ensemble, or both) drives the gap. An ablation applying the LISA-style ensemble to DCoND's neural decoder would cleanly separate the contributions.

5. **t-SNE evidence of latent-space separation is qualitative.** The paper claims diphone-trained representations are "significantly more condensed and well-separated" (line 194) based on t-SNE visualizations without a quantitative clustering metric (e.g., silhouette score, Davies–Bouldin index). This is acceptable as supporting analysis but should not carry the weight of primary evidence.

### Trivial
- The paper says DCoND-L outperforms "9.46% WER of NPTL and 8.93% of LISA" (line 182) — but LISA's WER comparison to DCoND-L is not a fair comparison since LISA uses a different (GPT-3.5) architecture. This sentence conflates the two comparison types; it should be rephrased to clarify that the 8.93% reference is a system-level benchmark result, not a controlled comparison.

## Nice-to-Haves
- Provide the α schedule (e.g., linear from 0.2 to 0.8 over epochs 1–50) and other key hyperparameters (learning rate, GRU hidden dimension, batch size) in a table for reproducibility.
- Include inference-speed or cost comparison between the ICL and fine-tuning LLM variants to contextualize the resource-accuracy trade-off.

## Removed Points
- *"PER not reported for LISA in Table 1"* — This is a descriptive observation about the table, not a weakness of the paper. LISA's PER simply was not published.
- *"Compare against the full set of published methods on this dataset"* — The paper names the two leading methods on the benchmark; whether others exist cannot be verified externally.
- *"Triphone K=100 achieves better PER"* — The paper already acknowledges and discusses this (line 246): "triphone with appropriate class size achieves comparable PER as the diphone counterpart... However, triphone modeling underperforms diphone modeling in terms of WER." The authors provide a reasonable explanation. Not a weakness.
- *Code/checkpoint availability* — Standard for this venue; not a weakness of the research.
- *Harsh critic's speculative Figure 5 value (~6.35%)* — The reviewer was guessing values from a figure without exact labels; the paper text indicates DCoND-LIFT w/o P achieves 8.06% WER (line 140), making the exact guess irrelevant.

## Novel Insights
None beyond the paper's own contributions. The reviews did not surface a perspective that meaningfully reframes or extends the paper's findings beyond what the authors already present.

## Suggestions
1. Report mean and standard deviation over at least 3 random seeds for all key metrics (PER, WER) for DCoND-L, DCoND-LI, DCoND-LIFT, and the main baselines. This single addition would substantively address the most significant evidential gap.
2. Specify the α annealing schedule explicitly (function form, start/end values, epoch boundaries) to enable reproduction.
3. Add a brief limitations paragraph discussing the single-subject scope and outlining directions for multi-subject validation.
4. If the LISA paper (benster2024cross) specifies its neural decoder architecture, cite those details; otherwise, note that the comparison is system-level rather than component-controlled.
