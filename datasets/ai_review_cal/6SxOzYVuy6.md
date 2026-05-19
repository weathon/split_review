- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 3, 5, 6
Now I have all the evidence needed. Let me compose the final consolidated review.

---

## Summary

DROSIA proposes a time series forecasting architecture that extracts a global sequential representation (via MLP over concatenated patch embeddings) and fuses it back to each individual patch embedding through concatenation+FFN, rather than using self-attention to aggregate information across time points. The method achieves O(C·L + C·H) complexity (linear in all key dimensions) and shows competitive or best results on 8 standard benchmarks, particularly on datasets with many channels when input length is sufficiently long.

## Strengths

- **Linear complexity maintained with competitive accuracy**: DROSIA is the only method among those compared that achieves complexity linear in input length, prediction horizon, AND number of channels (Table 3), yet it matches or beats quadratic-complexity Transformer models on 4 of 8 datasets at L=96 (ETTh2, ETTm1, ETTm2, Weather) and on ECL/Traffic when input length ≥ 192 (Table 2). This is a genuinely attractive property for large-scale deployment.

- **Ablation confirms both components contribute**: The ablation in Table 4 shows that the combined patch+sequential configuration ("P+S") consistently outperforms either component alone ("P" or "S") across datasets. This provides direct evidence that the sequential information extracted via DROSIA adds value beyond what patch embeddings alone capture, supporting the core claim that the decoupled design is beneficial.

- **Thorough hyperparameter analysis across variate scales**: Figure 3 systematically varies patch size, dimension ratio, model dimension, and encoder depth across datasets ranging from 7 channels (ETTm1) to 862 channels (Traffic). The analysis reveals interpretable scaling patterns (large-variate datasets benefit from higher capacity; small ones do not) and demonstrates robustness to patch size — a practical advantage.

- **Honest treatment of limitations**: The paper explicitly acknowledges that DROSIA underperforms channel-dependent methods (e.g., iTransformer) on large-variate datasets with short input (L=48–96), and positions its strength as emerging with longer input. The conclusion discusses the need for future work on inter-channel modeling rather than overclaiming universality.

## Weaknesses

### Fatal

None.

### Major

- **SOTA claim is broader than the evidence supports**: The abstract and contributions state that DROSIA "achieves state-of-the-art performance with only linear complexity." However, on the two largest-variate datasets (ECL with 321 channels, Traffic with 862 channels) at the standard input length L=96, DROSIA does not beat iTransformer. The authors need to increase input length to ≥ 192 to claim superiority. The SOTA framing should be conditioned on sufficient input length. Furthermore, **TimeXer** (Wang et al., 2024b) is discussed in the Related Work as "achieving promising results" and is directly relevant as a channel-independent+channel-dependent hybrid, yet it is never compared against empirically. Since TimeXer is cited and the paper criticizes its computational cost, an empirical comparison is necessary to support the performance and efficiency claims.

- **Efficiency claims lack empirical measurements**: The paper heavily emphasizes linear complexity, yet provides only theoretical big-O analysis (Table 3). No wall-clock time, peak memory usage, training speed, or inference latency comparisons are reported — despite stating that all experiments were run on a single NVIDIA 4090 GPU. Given that the method involves concatenating high-dimensional vectors and multiple FFN passes, actual runtime could deviate from idealized complexity. Empirical efficiency data would convert a plausible theoretical claim into a concrete practical strength.

- **The decoupling benefit over simpler alternatives is not isolated**: The ablation (Table 4) shows that using patch embeddings alone ("P") already performs well, and adding sequential information ("P+S") yields incremental gains on many datasets. The core question is whether the *decoupled concatenation+FFN* design outperforms simpler fusion mechanisms (e.g., adding the global vector to each patch, or a gated residual connection). Without an ablation comparing DROSIA's proposed concatenation+FFN against these simpler alternatives, it is unclear whether the architectural complexity is justified, or whether the benefit comes primarily from the presence of global context (which could be integrated more simply).

### Minor

- **Tensor operation in the fusion step could be clearer**: The paper states that the sequential representation \(R^j\) is "concatenated with the original patch embeddings" (line 71) and Figure 2's caption says it is "duplicated and combined." However, Equation (5) writes \(S^j \circ R^j\) without explicitly stating that \(R^j\) is broadcast/tiled to match the number of patches before concatenation. The dimension ratio (1:1) is specified, and Figure 2 clarifies the duplication, but a precise statement in the main text about the tensor shapes would make the method fully unambiguous for reproduction.

- **Ablation on dimension ratio is limited**: The sensitivity analysis in Figure 3 sweeps the dimension ratio \(r\) from 1/8 to 7/8, which is good. However, this is done only at a single fixed setting (input length 192) without a targeted analysis of how the ratio interacts with dataset scale or input length. A more focused study on a large dataset (e.g., ECL or Traffic) with performance plotted against ratio at multiple input lengths would strengthen the guidance for practitioners.

- **Missing comparison control for iTransformer with adjusted input length**: When the authors increase input length to show DROSIA surpassing iTransformer on ECL/Traffic (Table 2), they do not report whether iTransformer itself benefits from longer input in the same setting. Since iTransformer was originally evaluated at L=96, it is possible that it also improves with longer input. This control would make the comparison more rigorous.

### Trivial

- The sociological analogy (Fine 1993, Weigert 1991) in the Introduction is conceptually unnecessary for the technical contribution and occupies space better used for a more precise method statement.

## Nice-to-Haves

- **Empirical efficiency benchmarks** (wall-clock time and peak memory for a representative setting like ECL L=512) to convert the theoretical complexity claim into a practical one.
- **Ablation comparing DROSIA's decoupled concatenation+FFN** against simpler global-context integration (e.g., additive residual or gating) to isolate the contribution of the "decoupled" design.
- **Evaluation on univariate benchmarks** (ETTh/ETTm subsets) to complement the multivariate results and further test channel-independent modeling.

## Removed Points

These points are flagged to be removed; treat them with caution if reviewing the original reviews.

1. *"Method is ambiguously specified, compromising reproducibility (structural flaw)"* — REMOVED because the paper DOES specify the dimension ratio (1:1, i.e., d/2 for sequential, lines 113, 145) and Figure 2 caption explicitly states the global vector is "duplicated and combined" with each patch (line 74). The method is adequately specified for reproduction; some presentation polish would help but this is not a structural flaw.
2. *"Patch embedding follows PatchTST exactly — no innovation here"* — REMOVED because this is descriptive, not a weakness. Leveraging established components is standard practice.
3. *"Tables are images and cannot be directly evaluated"* — REMOVED (parser artifact, not an author error).
4. *"No evaluation on univariate forecasting"* — REMOVED as scope can be legitimately limited to multivariate forecasting.
5. *"Code not available at time of review"* — REMOVED per hard rules (cannot question cited references or availability).
6. *"No discussion of failure cases"* — REMOVED because the paper does discuss the Exchange dataset (second-best) and acknowledges when DROSIA underperforms (short-input, large-variate scenarios).
7. *Sociological analogy is unnecessary* — Downgraded to Trivial (it's a style concern, not substantive).
8. *"The specific decoupled design is not crucial"* / undermining claims from extraction method ablation (Table 5) — REMOVED because the paper does not claim the *extraction method* is the contribution; the contribution is the *decoupled architecture* itself, and the extraction method ablation is presented as evidence of robustness, not as a core claim.

## Novel Insights

The two reviews together surface a recurring tension: DROSIA's claimed novelty (decoupled representation) is technically sound and its linear complexity is genuinely attractive, but the empirical contribution is less dramatic than the framing suggests. The method is essentially a global-context residual on patch embeddings — a design that can be described as "PatchTST with a learned global vector instead of self-attention." The strongest evidence for DROSIA is not that it crushes all baselines on every metric (it doesn't on ECL/Traffic at L=96), but rather that it achieves comparable or better accuracy *with strictly less asymptotic complexity* and without cross-channel information. This positions DROSIA as a practical efficiency-first alternative rather than a new accuracy paradigm, which is an honest and useful contribution that the paper would benefit from emphasizing more directly.

## Suggestions

1. **Tone down the SOTA claim**: Replace unqualified "state-of-the-art" with a conditioned statement such as "competitive with or exceeding prior methods under sufficiently long input, while requiring only linear complexity." This would accurately reflect the results and preempt the most serious critiques.

2. **Add the missing TimeXer baseline** and, if feasible, 1–2 additional recent methods (e.g., TSMixer or a Mamba-based forecaster) to the experimental comparison. Since TimeXer is cited in the paper, omitting it creates a conspicuous gap.

3. **Report empirical efficiency** — even a single-table entry showing wall-clock time and peak GPU memory for one representative setting (e.g., ECL L=512) would substantially strengthen the efficiency claim.

4. **Add an ablation comparing DROSIA's concatenation+FFN fusion against additive residual fusion** (e.g., \(S + \text{MLP}_{\text{global}}\)) on a large dataset to isolate what the "decoupled" design specifically buys.

5. **Add a sentence clarifying the tensor operation**: e.g., "Note that \(R^j \in \mathbb{R}^{d/2}\) is tiled \(n\) times to match the number of patches before concatenation, so that the result has shape \((n, d + d/2)\)."
