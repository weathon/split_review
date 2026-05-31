## Summary

The paper introduces **Influence-Aware Time Series Forecasting (IATSF)**, arguing that the well-known performance plateau in TSF stems from the "self-stimulation" assumption—predicting the future from historical observations alone, ignoring external influences. The authors formalize this limitation via a control-theoretic error bound, propose a new benchmark with leak-free textual influences temporally synchronized to forecasting horizons, and develop FIATS, an LLM-free model with channel-aware sensitivity mechanisms (CASM and CAPS) that explicitly conditions forecasts on textual influence signals.

---

## Strengths

- **Theoretically grounded paradigm**: Propositions 2.1 and 3.1 rigorously prove that ignoring external influences imposes an irreducible error floor, and that incorporating even partial influence information reduces the error covariance. The linear-system fallback makes the theory concrete and verifiable.
- **Controlled toy validation**: The FM Toy experiment directly instantiates Proposition 2.1—FIATS achieves near-zero MSE (0.003–0.027), while large foundation models (Chronos-L, Time-MoE, MOIRAI-L) collapse to averaged outputs, providing unusually clean empirical confirmation of the theory.
- **Careful benchmark design**: The distinction between leak-free influences (independently evolving: holidays, weather forecasts, developer logs) and circular influences (which describe the target series itself) is a genuine methodological contribution. The multi-category design (synthetic, physics, market) enables granular evaluation.
- **Attribution via ablation**: The Zero News vs. Zero Desc ablations in Table 3 clearly isolate the contribution of influence signals from architectural complexity. FIITS scores in Table 1 align with Zero News scores in Table 3, confirming that performance gains originate from the influence conditioning, not the FIATS architecture itself.
- **Interpretability**: CASM attention maps provide human-interpretable sensitivity weights. Fig. 5 shows layers progressively shifting attention from temporal context to channel-specific influence signals, directly mirroring the control-theoretic motivation.

---

## Weaknesses

### Fatal
None.

### Major

1. **The comparison is structurally privileged**: FIATS receives future-aligned influence information ($U_f$) that all baseline models lack entirely. While this is the paper's core thesis—providing such information should help—the experimental framing conflates "the paradigm is useful" with "FIATS is a better model." A fair architecturally matched comparison would require giving equivalent influence information to a strong baseline (e.g., PatchTST extended to use the same text embeddings), to fully separate the contribution of the paradigm from that of the specific FIATS architecture. The "FIITS" ablation partially addresses this but is not highlighted as the definitive architectural comparison.

2. **Practical applicability is understated as a limitation**: For the benchmark to be useful in deployment, accurate future influence predictions must be available. The paper categorizes three input types (known events, expert predictions, hypothetical scenarios) but the evaluation on datasets like Atmospheric Physics effectively uses near-perfect weather forecast information. The performance gap between "perfect influence" and "predicted influence" (Fig. 6 shows degradation with noise) is real but not systematically characterized across the realistic forecasting setting where influence itself must be predicted.

3. **The "performance plateau" framing is overstated**: The paper claims self-stimulation is the *primary* cause of the TSF performance plateau and that IATSF is "the primary path forward for meaningful progress." However, standard benchmarks where the plateau has been observed (ETT, Exchange Rate, Weather, etc.) may genuinely lack accessible independent external influences. The paper provides no evidence that influential external factors for these benchmarks exist but are unused; the plateau may also stem from low signal content in those specific datasets.

### Minor

1. **"FIITS" is used in Table 1 without clear in-text definition**. It is only recoverable by cross-referencing ablation Table 3 ("Zero News"). This creates confusion for readers parsing the main results table.
2. **Gains on Electricity Utility are modest** (FIATS 0.124 vs. DLinear 0.140 at horizon 96), which is underwhelming for a dataset described as having "simple, discrete textual influences." The paper implies holiday indicators should be easy for IATSF, yet the advantage is small.
3. **FIATS is described as "LLM-free" but relies on the OpenAI Embedding API** as its best-performing configuration (Table 3). Framing as LLM-free is technically accurate (no generative LLM decoder) but may mislead practitioners about the external API dependency.

### Trivial
The full observability assumption ($X = Z$) in Proposition 2.1 is acknowledged but the extension to partial observability is deferred to the appendix.

---

## Nice-to-Haves

- Include an experiment with a strong multivariate baseline (e.g., iTransformer or TiDE) augmented with the same text embeddings as FIATS, to cleanly isolate whether the paradigm or the FIATS architecture drives the gains.
- A degradation curve showing FIATS performance as influence forecast quality degrades from perfect to climatological average would sharpen the practical contribution.
- GAUD results (12.6% improvement) could be analyzed further: the improvement is heterogeneous across games (Fig. 4 shows many near-zero or negative improvements), and the variance is unexplained.

---

## Novel Insights

The paper's most novel contribution is repositioning time series forecasting as dynamic system identification rather than pattern extrapolation, and formally proving via control theory that the standard "self-stimulation" training objective converges to the conditional expectation—producing the empirically observed "averaged output" artifact. This is not merely a restatement of the known usefulness of exogenous variables; it establishes a mathematical lower bound on error that cannot be crossed without external influence access, regardless of model capacity. The controlled FM Toy experiment, which shows billion-parameter foundation models collapsing to high error while a small FIATS achieves near-zero error, is a compelling instantiation of this insight. The CASM design, which operationalizes the channel-specific sensitivity term $c^i B^j$ from the linear system analysis as a cross-attention mechanism using natural language channel descriptions as queries, is a principled and interpretable architecture choice that flows directly from the theory.

---

## Suggestions

- Clarify "FIITS" in the main text at Table 1, and consider renaming it to "FIATS (no influence)" for clarity.
- Add a comparison against a simple baseline: PatchTST or DLinear concatenated with the same text embedding as a feature, as a cheap influence-aware ablation, to better isolate FIATS's architectural novelty.
- Provide empirical results with imperfect (predicted) influences for at least one real-world dataset to bridge the gap between benchmark evaluation and deployment.
- Temper the claim "the primary path forward" to "a necessary path forward when influence information is available."

---

## Score and Decision

The paper makes three concrete contributions: (1) a clean theoretical proof of irreducible error from self-stimulation; (2) a carefully designed, leak-free multimodal benchmark; (3) an interpretable, principled LLM-free model with strong ablation support. The FM Toy experiment alone is a memorable demonstration of the theory. The main weaknesses—overstated claims about TSF in general, structurally privileged comparisons, and understated practical deployment assumptions—are real but do not invalidate the core contributions. This is a solid, above-average paper with genuine intellectual contributions to both the theory and practice of multimodal time series forecasting.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>