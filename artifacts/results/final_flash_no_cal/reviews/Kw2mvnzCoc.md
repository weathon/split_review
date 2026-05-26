## Summary

TSPulse introduces a family of ultra-light (1M parameter) pre-trained models for time-series diagnostic tasks (anomaly detection, classification, imputation, similarity search). The key innovation is a pre-training framework with disentangled masked reconstruction across time, frequency, and semantic spaces, producing three complementary embedding views with distinct robustness properties. Post-hoc fusers (TSLens, Multi-Head Triangulation) selectively combine these views for task specialization. Despite its tiny size, TSPulse achieves strong results on 75+ datasets, outperforming models 10–100× larger while supporting CPU-only inference (0.387ms per embedding).

## Strengths

1. **Compact model with strong empirical performance across four tasks.** At only 1M parameters, TSPulse outperforms models 10–100× larger (MOMENT at 40M, Chronos at 46M, UniTS at 340M) on classification (Figure 5: +5–16% over VQShape/MOMENT/UniTS), anomaly detection (Figure 4: TSPulse-ZS at 0.48 VUS-PR vs. SubPCA at 0.42 and MOMENT-FT at 0.39), and similarity search (Figure 7: +25–100% over MOMENT/Chronos). The fine-tuned classification results (0.733 mean accuracy on UEA) are particularly clean comparisons since all methods are fine-tuned on labeled data.

2. **Disentangled representations validated through controlled sensitivity analysis.** Table 2 quantitatively confirms that temporal embeddings are phase-sensitive (130% distortion under time shifts), spectral embeddings are phase-invariant (21%), and semantic embeddings are most robust to noise (2.5%) and missing data (4.6%). This is direct evidence that the multi-head pre-training framework produces embeddings with distinct, complementary properties—a claim that is often asserted but rarely measured in time-series work.

3. **Hybrid masking strategy strongly justified through ablation.** Removing hybrid pre-training causes a 79% performance drop under hybrid-mask imputation evaluation (Table 1c), and the effect is cleanly isolated. This demonstrates that the masking diversity during pre-training, not just the architecture, drives the imputation gains.

4. **Multi-head triangulation for anomaly detection is well-motivated and validated.** Table 1(a) shows Head\_triang. outperforms the best single head by 9–14% (univariate) and 16% (multivariate). The framing—that different anomaly types manifest in different representational spaces (spikes in time, periodicity breaks in frequency)—is principled and backed by the sensitivity analysis.

5. **Efficiency gains are demonstrated, not just asserted.** CPU inference at 0.387ms (14× faster than MOMENT, 120× faster than Chronos), GPU at 0.050ms, and 40× smaller model size (Figure 7 table). These are directly measured and compared against the smallest variants of baselines, making the efficiency claims credible.

6. **Thorough ablation studies supporting design decisions.** Identity initialization for channel mixers (+9%), TSLens over pooling (+11–16%), dual-space learning (+7–8%), and the short/long embedding split (+8–10%) are all individually ablated in Table 1(b–c), giving confidence that each component contributes meaningfully.

## Weaknesses

### Fatal
None.

### Major

1. **Selective reporting of imputation baselines.** The paper claims "Compared to statistical interpolation methods, TSPulse shows 50%+ gains" (Section 4.3). However, Figure 6 shows that the "Interpol" baseline (a statistical interpolation method) achieves MSE 0.039, which is substantially better than TSPulse (ZS) at 0.074. The IMP(%) column for Interpol is left blank in the figure, and this result is never discussed or acknowledged in the text. This is a clear instance of selective reporting: the paper highlights gains over Naive and Linear but omits that the strongest statistical baseline outperforms TSPulse (ZS). The paper should (a) specify what "Interpol" is (which interpolation method), (b) discuss why it performs so strongly, (c) clarify whether the evaluation conditions are identical (same masked points, same masking patterns), and (d) honestly report that TSPulse (ZS) underperforms this baseline. The fine-tuned TSPulse (FT) matches Interpol at 0.039, which is noteworthy, but the zero-shot claim as currently phrased is misleading.

### Minor

2. **Zero-shot comparisons conflate architecture and pre-training strategy.** Section 3.1 states that TSPulse pre-training is specialized per task by "reweighting loss objectives to prioritize heads most relevant to the target task." This means TSPulse (ZS) for anomaly detection uses AD-specific loss weights, for imputation uses imputation-specific weights, etc. Meanwhile, baseline pre-trained models (MOMENT, Chronos) use general-purpose pre-training objectives. When TSPulse (ZS) is compared against MOMENT (ZS), the comparison conflates two variables: (i) the disentangled architecture and (ii) the task-specific pre-training strategy. This does *not* invalidate the results—the paper never claims the architecture alone drives the gains, and comparisons against non-pre-trained methods (SubPCA, CNN, etc. in Figure 4) are unaffected. But the paper does not acknowledge this nuance, and the abstract/introduction frame the architecture as the primary differentiator. A controlled experiment using a single TSPulse model pre-trained with equal loss weights across all heads would cleanly separate these factors.

3. **Pre-training variant not explicitly specified per evaluation.** The paper states "Details of the pre-trained model configurations are in Appendix A.9" (Section 4), but the main evaluation sections (4.1–4.4) do not state which loss-weighting configuration was used for each task. The reader must infer: AD-ZS uses AD-weighted pre-training, imputation-ZS uses imputation-weighted pre-training, etc. While this is a reasonable inference, the paper should be explicit (e.g., a simple table mapping each evaluation to its pre-training loss weights). This also affects the classification fine-tuning results (Section 4.2)—was the starting model pre-trained with classification-weighted or balanced losses?

4. **No variance or uncertainty reported.** All results are reported as point estimates (mean accuracy, mean MSE, VUS-PR) without standard errors, confidence intervals, or per-dataset breakdowns. Given the diversity of datasets (29 UEA datasets, 6 LTSF datasets, 40 TSB-AD datasets), knowing whether differences are consistent or driven by a few datasets would strengthen the evaluation.

5. **Ablation subset not justified.** The classification ablation (Table 1b) uses "a representative subset of 17 UEA datasets" without stating the selection criteria. If the subset is skewed toward easier or harder datasets, the magnitude of ablation drops could change. The criterion should be stated.

### Trivial
- The sensitivity analysis (Table 2) reports distortion percentages but does not discuss normalization—whether the baseline embedding is already near-zero distortion, which would inflate relative percentages.
- Table 1(c) shows the ablation for imputation is evaluated under zero-shot settings, but the caption could be clearer.

## Nice-to-Haves
- A controlled experiment comparing TSPulse with balanced vs. task-specific loss weighting in zero-shot would cleanly isolate architecture from pre-training strategy.
- Reporting per-dataset results (e.g., in a supplementary table) would allow readers to assess consistency.
- A brief definition of the distortion metric in the main text (even 2 sentences) would make Section 6 self-contained.
- Clarifying what "Interpol" is and discussing its strong performance would address the most significant transparency concern.

## Removed Points
These points from the inputs were removed with brief justifications:

- *Critic claim that the task-specific pre-training confound "invalidates" zero-shot comparisons* — removed because the paper is transparent about this approach (Section 3.1), comparisons with non-pre-trained methods are unaffected, and the claim is too strong. The confound is worth noting (kept as Minor weakness #2) but does not invalidate the results.
- *Criticism that "without any training on the target data" is misleading* — removed because this is standard zero-shot terminology and the paper accurately describes the setup.
- *Criticism about disentanglement not being "explicit" due to lack of mutual information loss* — removed because the architecture enforces disentanglement by assigning separate heads to separate embedding segments with distinct loss objectives, which is a valid form of explicit disentanglement. The sensitivity analysis (Table 2) provides supporting evidence.
- *Section-by-section nitpicks about distortion metric definition, ablation subset criteria, and missing appendix content* — the distortion metric is formally defined in Appendix A.3 (referenced), and the subset criteria concern is kept as Minor weakness #5. Nitpicks about missing appendix content are removed per rules (parser strips appendices).
- *Some generic strength descriptions from the Strength Finder* — generic phrasing like "addressed an important problem" removed. Only concrete, evidence-backed strengths retained.

## Novel Insights

Beyond the paper's own contributions, the most interesting cross-cutting observation from the reviews is the tension between *task-specific pre-training* and *architecture-driven zero-shot capability*. The paper provides a family of small, task-specialized models rather than one general-purpose model, yet still frames the results as zero-shot transfer. This suggests a productive design philosophy for time-series: because pre-training is cheap (1B samples in 1 day on 8×A100s), it may be more practical to pre-train several small task-specialized models than one monolithic foundation model. The community typically pursues larger general models, but TSPulse's results—especially its 40× size reduction with competitive or superior performance—challenge that assumption. Whether this pattern holds across more tasks and data modalities is an open question worth exploring.

## Suggestions

1. **Fix the Interpol reporting.** Clearly state what Interpol is, acknowledge that it outperforms TSPulse (ZS), and discuss whether the comparison is apples-to-apples (e.g., same masked points, same evaluation protocol). If Interpol uses true values in a way TSPulse cannot, that should be made explicit.

2. **Add a controlled ablation comparing balanced vs. task-specific loss weighting** for at least one zero-shot task (AD or imputation). If the balanced-weight variant still outperforms MOMENT/UniTS, this would strongly strengthen the architecture claim. If not, the paper should reframe the zero-shot claims as contributions of the task-specialization strategy.

3. **Add a concise table in Section 4** specifying for each evaluation (AD-ZS, AD-FT, Imputation-ZS, etc.) which pre-training loss weights were used, whether the backbone uses channel mixing, and which heads are active at test time.

4. **Report per-dataset results or confidence intervals** for the main benchmark figures, or at minimum note the variance across datasets.

5. **State the selection criterion** for the 17-dataset ablation subset in Table 1(b).

## Score and Decision

This paper makes genuine contributions: a well-designed architecture for disentangled time-series representations, extensive empirical validation across four tasks on 75+ datasets, thorough ablation studies, and compelling efficiency results. The main weakness is selective reporting of the imputation baselines (the Interpol issue), which is real but limited to one claim and does not undermine the paper's core contributions. The task-specific pre-training nuance is worth noting but the paper is transparent about its approach, and many comparisons (against non-pre-trained methods and fine-tuned baselines) are unaffected.

The paper has clear strengths (compact size, strong results, validated disentanglement, practical efficiency) that outweigh the identified weaknesses, which are addressable in revision.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>