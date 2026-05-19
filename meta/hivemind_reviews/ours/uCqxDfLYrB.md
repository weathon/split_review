Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper conducts a large-scale empirical study of neural scaling laws for time series foundation models (TSFMs), examining how log-likelihood and MAPE scale with model size, compute, and data across both in-distribution (ID) and out-of-distribution (OOD) settings. It compares encoder-only and decoder-only Transformers trained on a common 15B-point corpus drawn from Lotsa, and additionally benchmarks two existing TSFMs (Moirai and Chronos) as case studies. The paper claims that (1) log-likelihood exhibits similar power-law scaling for ID and OOD, (2) encoder-only architectures scale better than decoder-only, and (3) architectural innovations in Moirai/Chronos improve ID performance but reduce OOD scalability.

## Strengths

- **First controlled comparison of encoder-only vs decoder-only scaling exponents in TSFMs.** The paper trains both architectures on the same corpus with the same training protocol (Section 2, Fig. 5), showing that the encoder-only Transformer consistently has higher power-law exponents for parameter scaling across both ID and OOD settings (Section 3.2: "the power law exponent of the encoder-only Transformer is consistently higher"). This is a clean, controlled experiment that provides a novel finding not available in prior TSFM scaling studies.

- **Extension of scaling law analysis to OOD data.** The paper demonstrates that for log-likelihood loss, encoder-only Transformer performance on ID and OOD test sets follows power laws with "close slopes" and a roughly constant offset for both parameter scaling (Fig. 2) and compute scaling (Fig. 3). Prior work (Edwards 2024, Shi 2024) examined only ID scaling, so extending the analysis to OOD is a meaningful step forward.

- **Identification of nuanced deviations from power-law scaling.** The discussion (Section 6.1, Fig. 8) documents specific OOD datasets (US births, NN5 daily, Australian electricity) where performance shows sharp improvements after a critical model size rather than smooth power-law behavior. While preliminary, this observation adds texture to the otherwise uniform power-law narrative and could motivate further study.

## Weaknesses

### Fatal
None.

### Major

- **OOD test-set overlap with training corpus is not verified.** The paper defines OOD evaluation using ETTh1-2, ETTm1-2, electricity, and weather datasets (Section 2.1), described as coming from "a widely recognized long-sequence prediction benchmark." However, the pre-training corpus is drawn from Lotsa, which includes 14 energy datasets and 2 climate datasets (Table 1). The paper never confirms that these specific benchmark datasets are absent from the training corpus. If any overlap exists, the observed "OOD scaling" is partially ID scaling, and the central claim that "log-likelihood loss exhibits similar scaling behavior in OOD and ID settings" (abstract) would need significant qualification. The paper must explicitly verify disjointness or use genuinely unseen domains (e.g., finance, if not in training).

- **Data-scaling experiments use a questionable evaluation protocol.** For data scaling (Section 3.1, Fig. 4), the paper trains 1B-parameter encoder-only models on subsets as small as 10M time points and reports "the averaged evaluation results during training" (line 150). Averaging evaluation metrics over training steps conflates early underfitting and later behavior, unlike the parameter and compute scaling experiments which report minimum loss. Training a 1B-parameter model on 10M time points also represents extreme overparameterization, where training dynamics may not reflect genuine data-scaling trends. The paper neither justifies this choice nor shows robustness to using minimum or final loss.

### Minor

- **Claim of "training to convergence" is questionable given only 10⁵ steps.** The paper states models were trained "to convergence" for parameter scaling (Section 3.1), but the training protocol uses only 100K total steps with a cosine schedule (Section 2.3). For a 300M-parameter model on a 15B-point corpus, 100K steps is unlikely to reach convergence. The "minimum loss" reported may be an intermediate checkpoint. This does not invalidate the results, but the "convergence" claim needs justification or relaxation.

- **No uncertainty quantification around power-law exponents.** The paper makes comparative claims (e.g., "encoder-only has better scalability than decoder-only," "Moirai shows a smaller slope") without reporting confidence intervals, goodness-of-fit measures, or results across multiple seeds for the exponent estimates. Given the visible noise in the figures, readers cannot assess whether reported exponent differences are statistically meaningful.

- **Insufficient detail on how Moirai and Chronos were integrated.** The paper states "Leveraging this dataset, we trained ... two state-of-the-art TSFMs: Chronos and Moirai" (Section 2), implying training from scratch on the same data. However, no details are provided about whether the same optimizer, scheduler, training steps, and hyperparameter search protocol were used for these models as for the baselines. Moirai and Chronos have substantially different architectural components (any-variate attention, multi-scale patches, discrete tokenization) that may interact differently with training hyperparameters. Without this detail, the comparison is informative but not fully controlled.

- **"Emergent phenomenon" claim is preliminary.** The discussion (Section 6.1) describes three OOD datasets where performance deviates from power-law scaling. While interesting, the evidence is anecdotal — single examples per dataset with no statistical evaluation or repeated trials. The term "emergent abilities" carries specific connotations from LLM research that the current evidence does not fully support.

### Trivial

- None beyond standard formatting artifacts.

## Nice-to-Haves

- Reporting goodness-of-fit measures or confidence intervals around the fitted power-law exponents would substantially strengthen the comparative claims.
- The data-scaling experiments would be more interpretable if final loss (or loss at convergence) were reported alongside or instead of the average over training.
- The paper focuses on univariate forecasting (Section 2.3) and scopes out multivariate effects, which is a reasonable choice, but noting whether the findings are expected to transfer would help readers.

## Removed Points

- **"Moirai/Chronos comparison may use pre-trained checkpoints"** — The paper explicitly states "Leveraging this dataset, we trained ... two state-of-the-art TSFMs" (Section 2), contradicting the speculation. Downgraded to Minor about insufficient training detail.
- **"Design principles are generic"** — Subjective opinion; the principles are grounded in the experimental results even if they seem unsurprising in retrospect.
- **"Compute formula S undefined"** — The paper states: "$S$ is the number of parameter updates, i.e. the input sequence length" (line 134). The criticism is factually incorrect.
- **"No code release"** — Removed per policy: cited references and reproducibility logistics are not valid criticisms when the cited models/benchmarks are understood to exist.
- **"Missing discussion of context length/horizon"** — The paper explicitly acknowledges this as future work (Conclusion, line 244), so the criticism constitutes scope creep.
- **"Missing appendix/proofs"** — Removed per policy (parser strips appendix content from all papers).
- **Strength: "Design principles derived from cross-factor comparisons"** — The design principles are restatements of experimental findings without additional synthesis, making them a weak strength. Removed as not concrete enough.

## Novel Insights

The two reviewers' inputs produce one genuinely novel observation beyond the paper itself: that the encoder-only vs decoder-only scaling comparison (the paper's cleanest experiment) reveals a pattern where the architecture with simpler, bidirectional attention consistently achieves higher power-law exponents. The harsh critic dismissed this as "narrow," but in the context of a field moving rapidly toward decoder-only architectures for TSFMs (e.g., Timer, Lag-Llama), this finding has practical design implications that neither reviewer fully explored. Conversely, the strength finder's enthusiasm for the "design principles" section is misplaced — those principles are direct restatements of the experimental results, not independent insights.

## Suggestions

1. **Verify and document OOD disjointness.** Provide explicit evidence that each OOD test dataset is absent from the pre-training corpus. If overlap is found, re-evaluate on genuinely unseen domains or clearly state which datasets are partially seen and discuss the implications.
2. **Revise the data-scaling evaluation.** Report minimum (or final) held-out loss alongside or instead of the training average. Either justify the averaging or show that the power-law fit is robust to the choice of evaluation protocol.
3. **Add uncertainty quantification.** Provide confidence intervals for fitted power-law exponents, especially for the encoder-only vs decoder-only and Moirai/Chronos comparisons where claims of "better" or "worse" scalability depend on exponent values.
4. **Clarify Moirai/Chronos training protocol.** Specify whether the same hyperparameters, optimizer schedule, and compute budget were used for these models, or describe any differences and their potential impact on the comparison.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>