Now I have a thorough understanding of the paper and the calibration landscape. Let me write the consolidated review.

---

## Summary

This paper argues that time series forecasting has plateaued because models rely solely on historical data ("self-stimulation"), ignoring external influences. The authors formalize this limitation through control theory (Propositions 2.1, 3.1), propose the Influence-Aware Time Series Forecasting (IATSF) paradigm, introduce a leak-free benchmark with temporally-synced textual influences spanning synthetic, physics-based, and market domains, and present FIATS — a lightweight model with channel-aware sensitivity modeling (CASM) and channel-aware parameter sharing (CAPS) that ingests textual influence embeddings. Experiments show FIATS dramatically outperforming self-stimulated baselines, including large foundation models, especially on a synthetic FM Toy dataset where it approaches the theoretical error bound.

## Strengths

- **Principled theoretical motivation.** The control-theoretic framing (Propositions 2.1, 3.1) provides a coherent argument for why ignoring external influences imposes an irreducible error floor, and why even partial influence information reduces it. While the mathematics is straightforward, it gives the paper a clear intellectual foundation that most contemporaneous text+TSF papers lack.

- **Well-designed benchmark.** The Temporal-Synced IATSF benchmark is explicitly constructed to be leak-free, using independently evolving influences with strict temporal synchronization. It covers three meaningfully different settings — controlled synthetic (FM Toy), physics-based real-world systems (Atmospheric Physics, NYC Traffic), and human-driven market data (GAUD) — addressing a genuine gap in multimodal forecasting resources.

- **Interpretable model architecture.** The CASM and CAPS mechanisms are well-motivated from the control-theoretic analysis. CASM explicitly models channel-specific sensitivity to textual influences via cross-attention with channel descriptions as queries, and CAPS addresses channel heterogeneity with minimal overhead. The attention-map visualizations (Figs. 3, 5) provide genuine interpretability, showing how different channels attend to different influence sentences and how the CAPS decoder exhibits distinct attention patterns per channel.

- **Strong controlled-experiment validation.** On the FM Toy dataset, FIATS achieves near-zero MSE (0.003 at pred_len 14), approaching the theoretical lower bound, while all self-stimulated baselines — including billion-parameter foundation models — produce substantially higher error. This cleanly demonstrates that influence information is necessary when the system is genuinely influence-driven.

- **Meaningful ablation evidence.** Removing influence input ("Zero News") degrades FIATS to self-stimulated performance levels, and removing channel descriptions ("Zero Desc.") significantly hurts performance, confirming that both influence information and channel-specific sensitivity modeling matter. Robustness to embedding model choice and graceful degradation under influence noise are also demonstrated.

## Weaknesses

### Major

- **Missing text-augmented baselines.** The experiments compare FIATS (which receives textual influences) against standard self-stimulated models that do not receive that text. The one multimodal baseline, TimeLLM, is substantially weaker than FIATS. However, no attempt is made to give the same textual influence data to a strong contemporary architecture (e.g., PatchTST or DLinear) through a straightforward mechanism — for instance, by concatenating text embeddings to patch embeddings or adding a simple cross-attention module. The "Zero News" ablation confirms that FIATS needs the text to perform well, but it does not show that FIATS's specific architectural choices (CASM, CAPS) are necessary rather than merely sufficient. Without this comparison, the claim that the IATSF paradigm and FIATS's specific design represent the *primary path forward* remains incompletely tested — the gains may partly reflect the availability of extra task-relevant information rather than the proposed modeling framework. This is the single most important experiment to add.

- **Claims exceed the evidence.** The paper's rhetoric — "the primary path forward for meaningful progress," "a hard, mathematical barrier," "critical performance plateau" — is stronger than the experimental design supports. The theoretical barrier is a restatement of the standard omitted-variable problem (variance of prediction error when conditioning on history alone). The experiments demonstrate that influence information improves forecasting, which is valuable, but they do not establish that this paradigm is *necessary for the field to progress* versus being one useful direction among several. The benchmark, while well-designed, covers five specific settings and does not itself demonstrate broad applicability.

### Minor

- **FIITS is undefined.** The variant "FIITS" appears in Table 1 alongside FIATS but is never defined or explained anywhere in the main text. Its relationship to FIATS (what is ablated or changed) remains unclear, which affects reproducibility and interpretability of the results.

- **No uncertainty reporting.** The main experiments report only point estimates (MSE) without standard deviations, confidence intervals, or any measure of statistical significance across runs. This matters particularly for the Electricity Utility dataset where margins between methods are small (e.g., 0.124 vs. 0.130 at pred_len 96).

- **Theoretical framing is oversold.** Propositions 2.1 and 3.1 are correct and useful as motivation, but describing them as a "hard, mathematical barrier" discovered through a "control-theoretic lens" overstates their depth. The results are essentially the law of total variance applied to a linear-Gaussian system, and the paper would benefit from positioning the theory as a principled motivation rather than a novel mathematical contribution.

- **Benchmark scope does not fully support generalizability claims.** The benchmark covers three domain categories with five datasets total, which is reasonable for an initial contribution but insufficient to support claims about a universal "paradigm shift" for time series forecasting. Settings where textual influences are unavailable, unreliable, or adversarial are not tested.

### Trivial

- The paper mentions "FIATS is LLM-free" but relies on fixed embeddings from pre-trained language models (OpenAI embeddings, MiniLM, mpnet). This is standard practice and not misleading, but the computational dependency on these embedding models could be stated more precisely.

## Nice-to-Haves

- Adding a baseline where PatchTST (or DLinear) receives the same textual influences through simple concatenation or a single cross-attention block would substantially strengthen the claim that CASM/CAPS are essential, not just that text is helpful.
- Ablating temporal-syncing and channel-specific mechanisms directly against simpler injection methods would help readers understand where the architectural value lies.
- Evaluating on settings where influences are sparse, conflicting, or adversarial would test robustness claims more thoroughly.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **"FIATS is LLM-free is slightly misleading"** — REMOVED. The paper clearly states it uses fixed text embeddings from pre-trained models. Using embeddings from a pre-trained model does not make an architecture "LLM-based"; this is standard practice and the distinction is meaningful (FIATS does not generate text, does not use LLM inference at runtime, and avoids the computational overhead of generative LLMs).

- **Harsh critic's claim that "the theoretical contribution does not provide a novel foundation" with reference to "standard in statistics or control theory"** — PARTIALLY REMOVED as a fatal criticism. The theory is indeed straightforward, but it successfully motivates the paradigm. Demoted to Minor rather than being treated as a fatal flaw.

- **Criticism about "the 'plateau' might have other explanations" and "motivation is overdrawn"** — REMOVED as speculative. This is a matter of rhetorical framing, not a verifiable error in the paper.

- **Criticism about "missing appendix, missing proofs"** — REMOVED. The parser strips appendices; they exist in the original submission.

- **The harsh critic's framing of the FM Toy result as "expected because the system is fully deterministic given the influence"** — PARTIALLY REMOVED as a criticism. The fact that it's expected is precisely the point of a controlled experiment: it validates the theory. This is a feature, not a bug.

## Novel Insights

The paper's most valuable insight is the reframing of cross-attention as an explicit control mechanism: queries model channel-specific sensitivity (via channel descriptions), keys filter relevant influences, and values translate textual embeddings into actionable influence effects. This operationalizes the control-theoretic insight that $X_f = AX_h + BU_t$ in a learnable, nonlinear architecture, and the attention maps genuinely reveal which textual cues drive which channel predictions. This is a more principled integration of text and time series than prior work that treats text as a generic conditioning signal.

## Suggestions

- Add a text-augmented PatchTST baseline (concatenating text embeddings to patch embeddings or using a simple cross-attention block preceding the standard encoder). If FIATS substantially outperforms this, it would directly validate CASM/CAPS and dramatically strengthen the paper.
- Define FIITS explicitly, or remove it from Table 1 if it is not a distinct contribution.
- Report standard deviation across at least 3 random seeds for key results.
- Tone down claims: replace "primary path forward for meaningful progress" with language like "a principled and effective direction" and "hard, mathematical barrier" with "fundamental limitation." The empirical results speak for themselves without rhetorical amplification.
- Clarify the relationship between FIATS and the embedding models — specifically, what is the inference cost of computing text embeddings and how does it compare to model inference.

## Score and Decision

**Calibration anchors considered:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| mfc6FKgtQA (TGForecaster / TGTSF) | 5.00 | R2 | Most similar paper — also proposes text-guided TSF with cross-attention and a benchmark. Our paper adds theoretical grounding and more principled architecture (CASM/CAPS), making it somewhat stronger. |
| 4F1a8nNFGK (CiK benchmark) | 5.00 | R2 | Benchmark-focused paper for text+TSF. Our paper includes a benchmark plus a model with theory, giving it broader contribution. |
| QE1ClsZjOQ (Dual-Forecaster) | 4.50 | R2 | Similar text+TSF model paper. Our paper is clearly stronger in theoretical grounding and architectural novelty. |
| uRXxnoqDHH (MoAT) | 5.00 | R2 | Text-augmented TSF with decomposition. Our paper's control-theoretic framing and CASM design are more principled. |
| 9EBSEkFSje (GIFT-Eval) | 5.25 | R1 | Broader benchmark but model-free. Our paper has a focused benchmark plus model contributions. |
| wMXH8tTQE3 (ProbTS) | 6.00 | R2 | Toolkit paper with broader scope. Our paper is more focused but has strengths in theory and model design. |
| lfPkGWXLLf (ForecastBench) | 6.67 | R2 | Clearly stronger — dynamic benchmark with rigorous evaluation. Our paper is not at this level. |
| TPZRq4FALB (READ) | 8.00 | R1 | Strong accept — different domain, clearly superior contribution. |

**Round 1 bracket:** 4.5–6.5, based on comparison against weak (2.5–3.0) and strong (8.0) anchors.

**Round 2 narrowing:** The paper sits above the 5.0 cluster (TGForecaster, CiK, Dual-Forecaster, MoAT) due to its theoretical grounding and more principled architecture, but below the 6.0+ papers (ProbTS, ForecastBench) due to the missing text-augmented baseline and overclaimed significance. The appropriate score is **5.5**.

The missing text-augmented baseline is a genuine methodological gap that prevents full confidence in the architectural contribution claims, and the rhetoric substantially overshoots the evidence. However, the theoretical motivation, carefully designed benchmark, interpretable model architecture, and clean controlled-experiment results constitute a real and valuable contribution that meaningfully advances the multimodal forecasting conversation.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>