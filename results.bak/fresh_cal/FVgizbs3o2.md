Now I have a thorough understanding of the paper and have verified the key claims. Let me compose the final consolidated review.

## Summary

This paper proposes TensorGPT, a training-free compression method for LLM embedding layers based on per-token Tensor-Train Decomposition (TTD). Instead of decomposing the entire embedding matrix, each token embedding vector is individually tensorized and factorized into Matrix Product State (MPS) cores, avoiding any fine-tuning or extra training data. The authors evaluate on GPT-2 and CerebrasGPT models across language modelling (perplexity on WikiText-2, WikiText-103, 1BW) and sentiment classification (IMDB), and measure on-device latency on a Raspberry Pi 5. The method achieves 39–65× compression of embedding layers and up to 46.89% parameter reduction of the full model, while maintaining or even slightly improving language task performance for larger models.

## Strengths

1. **Training-free embedding compression with validated parameter reduction (concrete and verified).** The paper demonstrates that TTD can compress GPT-family embedding layers by 39.38×–65.64× (Table 2) and reduce total model parameters by up to 46.89% without any fine-tuning or additional data. The per-token decomposition strategy (Section 3.1) is clearly motivated by the lookup-table nature of embedding layers and is algorithmically well-specified in Algorithm 1.

2. **Real low-end device latency measurements.** The paper provides per-token compression latency (≤2.148 ms on Raspberry Pi 5, Table 3) and per-text inference overhead with confidence intervals (Table 2), offering concrete evidence that the approach is practical for edge deployment. This goes beyond the typical GPU-only evaluations seen in related compression work.

3. **Systematic ablation on tensor order across multiple models.** The paper varies tensor order from N=2 to N=N_max across GPT-2 series models (Figures 3e–3j), identifying order-3 as empirically optimal. This ablation is broader than prior tensor decomposition work on LLMs and provides useful guidance for practitioners.

4. **Validated empirical bound on compressibility without performance loss.** The finding that embedding layers can be compressed 0.5×–2.0× without language task degradation is consistently observed across model sizes and datasets (Section 4.3), providing an actionable rule-of-thumb for deployment.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Missing training-free baseline comparison (truncated SVD).** The paper's central motivation is that existing low-rank approaches require extra training. However, the most natural training-free baseline — a simple truncated SVD of the embedding matrix (applied per-row or as a whole matrix, truncated to the same parameter budget) — is never evaluated. The comparison against Tucker decomposition (Figure 3k) is useful but insufficient to isolate the advantage of the TT structure over simpler matrix-level factorization. Adding such a baseline would substantially strengthen the claim that the per-token TTD structure is specifically beneficial. This is the most significant weakness.

2. **"Outperform uncompressed" claim for sentiment classification lacks statistical support.** The paper states (line 67) that compressed models "can even outperform" uncompressed models. For language modelling this is a deterministic computation and the results speak for themselves (some configurations yield slightly negative ΔlnPPL). However, for sentiment classification (Figures 3a–3d), the model is fine-tuned for sequence classification, which involves randomness; no error bars or multiple-run statistics are reported. The "outperform" observation for larger models in precision and F1-score would be more convincing with variance estimates.

3. **Latency trade-off for the compression-memory gains is underexplored.** For several configurations, compressed models have higher total inference latency (e.g., DistilGPT2 PPLα: 0.36s vs. 0.19s original; CerebrasGPT-256M PPLα: 1.01s vs. 0.71s original). The paper frames this as "induced latency ≤0.3s" (line 315), which is accurate, but the practical benefit of a memory saving that is modest for larger models (e.g., GPT-2-L: 774M → 734M, ~5% reduction) weighed against a latency increase deserves more explicit discussion. The paper acknowledges this partially in the conclusion but does not provide a systematic characterization of when the trade-off is favorable.

4. **Hyperparameter selection methodology is underspecified.** The paper candidly states that "due to the combination of tensor size and TT ranks exponentially exploding, we could not test all possible combinations" (line 303). However, for a given compression ratio, many (I_k, r_k) configurations yield the same parameter count. The paper does not describe how specific configurations were selected — whether via search, heuristic, or post-hoc selection of best-performing ones. A sensitivity analysis or a principled selection rule (e.g., based on singular value decay of the tensorized embeddings) would increase confidence that the reported results are representative rather than favored.

### Trivial
None.

## Nice-to-Haves

- An ablation comparing per-token TTD versus TTD of the full embedding matrix (reshaped into a 3D tensor across tokens) would directly validate the authors' claim that per-token decomposition "prevents damaging the individual information" (line 59).
- Reporting the fraction of total model FLOPs consumed by the reconstruction step would help contextualize the latency overhead.
- A simple simulation of dynamic vocabulary updates (the scenario motivating per-token compression in Figure 1) would strengthen the practical relevance claim.

## Removed Points

These points were flagged by reviewers but are removed with justification:

- **"Missing related work on matrix-based approaches"**: Removed per instructions (cannot verify external sources). The paper does discuss SVD, Kronecker, and block-diagonal approaches in its Related Work section (lines 361–368).

- **"Missing ablation on per-token vs. whole-matrix decomposition"**: Demoted from a weakness to Nice-to-Have. The paper motivates the design choice, but a direct comparison would be a nice addition rather than a missing necessity.

- **"Missing comparison to quantization, pruning, float16"**: Removed as scope creep. The paper is about low-rank tensor decomposition for embedding layers; demanding all possible compression methods as baselines is beyond the stated scope.

- **"Table 1 uses simplified notation"**: Removed. The paper explicitly notes "For simplicity" (line 168) and cites the appendix for the full derivation.

- **"46.89% claim in abstract is misleading"**: Removed. The paper says "theoretically results in" — this is a specific maximum case, not a guaranteed property, and the wording is appropriate.

- **"Code/hyperparameters missing from appendix"**: Removed per instructions (the appendix is stripped by the PDF parser).

## Novel Insights

None beyond the paper's own contributions. The main insight — that a per-token, training-free TTD can compress LLM embedding layers by 39–65× while maintaining performance on edge devices — is the paper's own finding. The reviewers did not surface a genuinely novel observation that the paper itself does not contain.

## Suggestions

1. **Add a truncated SVD baseline** — compress the full embedding matrix (or each row individually) via truncated SVD with the same parameter budget as the TTD configurations, and report perplexity and downstream performance. This directly isolates whether the per-token TT structure provides measurable advantages over simpler matrix-level low-rank approximation.

2. **Report variance for sentiment classification** — run the fine-tuning step for the classification head with at least 3 random seeds and report mean ± std for the performance differences shown in Figures 3a–3d.

3. **Add a systematic rule for hyperparameter selection** — describe how tensor dimensions {I_k} and TT ranks {r_k} were chosen for each reported configuration (e.g., based on factorizing d into near-equal factors, or using a sweep over a defined grid). For the configurations that yielded the same parameter count, show multiple examples to demonstrate robustness.

4. **Expand the latency trade-off discussion** — include a scatter plot of memory savings (%) vs. relative latency change for each model/config, and state explicitly the conditions under which the trade-off is favorable (e.g., embedding-dominated models vs. hidden-layer-dominated models).

## Score and Decision

This paper presents a novel application of Tensor-Train Decomposition to LLM embedding compression in a training-free setting, with thorough evaluation on multiple model scales and real edge hardware. The methodology is sound and clearly presented. The primary gap is the absence of a truncated SVD baseline, which would strengthen the contribution, and some secondary concerns about statistical rigor and trade-off characterization. These issues are addressable and do not undermine the paper's core contributions.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>