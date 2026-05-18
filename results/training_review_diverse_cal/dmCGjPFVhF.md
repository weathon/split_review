Now I have a complete understanding of the paper. Let me synthesize the final consolidated review, carefully cross-checking each reviewer claim against the actual paper.

---

## Summary

This paper introduces FACTS (FACTored State-space), a recurrent framework for world modelling that represents the hidden state as a graph-structured memory with multiple latent factors. FACTS uses an attention-based routing mechanism to assign input features to factors, and can be linearised (by substituting the evolving memory state with the initial state in the routing functions) to support parallel computation via associative scan. The paper provides theoretical proofs of permutation equivariance/invariance and evaluates FACTS on multivariate time series forecasting, object-centric world modelling, and graph-based node prediction, reporting competitive results.

## Strengths

- **Formal proof and empirical validation of permutation invariance**: Theorem 1 proves that the linearised FACTS (equation 20) is left permutation equivariant and right permutation invariant. Figure 2 provides compelling empirical evidence: when test features are randomly permuted, FACTS maintains its prediction accuracy across multiple datasets, while iTransformer and S-Mamba errors more than double (e.g., Traffic MSE roughly triples for S-Mamba). This directly validates a core claimed advantage over standard SSMs and Transformers.

- **Competitive or top performance across diverse benchmarks**: In multivariate time series forecasting (Table 1), FACTS achieves the best MAE on 6 of 9 datasets and is always top-2 on 7. On object-centric world modelling (Table 2), it attains the lowest LPIPS (0.09) and leads in FG-mIoU (48.11). On graph-based node prediction (Table 3, METR-LA), it achieves the best MAPE (9.08%). These results suggest genuine capability despite the confounding factors discussed below.

- **Flexibility across input modalities**: The paper treats inputs as sets of nodes, allowing the same framework to handle multivariate sequences, object slots, and graph-structured data. Consistent strong performance across diverse formats supports the claim of a general-purpose framework.

- **Linearisation with empirical robustness**: Section 3.1 derives a linear recurrence (using Z₀ instead of Z_{t-1} in the routing) that enables parallel scan. Figure 3 shows FACTS maintains stable performance across segment window sizes from 1 to 96 on Electricity, indicating the linearisation does not severely degrade accuracy.

## Weaknesses

### Fatal
None.

### Major

1. **Confounded comparison in time series forecasting (Table 1)**: The paper states it uses the exact same setup as prior work "with the exception of the pre- and post-processing modules... we replace these with set functions" (line 183). This means FACTS uses *different* embedders and projectors than the baselines whose results are cited. No ablation controls for this change, so we cannot attribute FACTS's strong performance to its core architecture rather than to better feature extraction/decoding via the set functions. An apples-to-apples comparison (same embedders/projectors across methods, or running baselines with the same set functions) is needed to isolate the contribution of the core FACTS recurrence.

2. **Overstated claim about dynamic, state-dependent routing**: The paper's core motivation is that existing SSMs impose rigid structural constraints, while FACTS "dynamically assigns input features to distinct latent state-space factors" using a routing mechanism that depends on the *evolving memory* Z_{t-1}. However, the actual implemented model (the "linearised" version, equations 17–20) replaces all occurrences of Z_{t-1} in the routing functions with Z₀ (the initial memory). This means the routing parameters Ā_t, B̄_t, U_t depend on (Z₀, X_t), not on the evolving Z_{t-1}. The paper acknowledges this substitution (line 119) but does not discuss what is lost: the routing can no longer adapt to changes in the memory state within a segment. The paper never trains or evaluates the full state-dependent version (equation 10). Even the "fully recurrent" mode (window size 1) still uses the linearised formulation with per-step Z₀ updates, not the Z_{t-1}-dependent routing. This gap between the claimed mechanism and the tested model is significant and not adequately addressed.

3. **Unverified permutation invariance of the full system**: The paper asserts "Dec is a permutation-invariant decoder" (line 91) and replaces standard pre/post-processing modules with "set functions" (line 183), but never specifies what these functions are, nor verifies that the *full* system (including embedders and decoder) preserves the theoretical invariance properties. Without this verification, the empirical robustness to permutation (Figure 2) could derive from the set functions rather than the core FACTS recurrence. The theoretical guarantees (Theorem 1) apply to the core module in isolation, but the paper does not show they extend to the complete system used in benchmarks.

### Minor

1. **No error bars for Table 1 results**: Standard deviations are reported for the permutation experiment (Figure 2) but not for the main forecasting results in Table 1 or the object-centric results in Table 2, making it impossible to assess statistical significance of the reported advantages.

2. **Object-centric results show small absolute differences**: In Table 2, LPIPS of 0.09 vs. next-best 0.10 and FG-mIoU of 48.11 vs. 47.23 are small margins. Without error bars, these may not be meaningful.

3. **Missing comparison to plain Mamba on non-time-series tasks**: The paper compares against S-Mamba on forecasting, but FACTS is motivated as improving over SSMs in general (object-centric, graph tasks). No comparison to an SSM baseline (e.g., Mamba adapted for these modalities) is provided for the object-centric or graph experiments.

4. **"Parallel vs Recurrent" analysis limited to one dataset**: Figure 3 only evaluates the effect of window size on Electricity. Generalizing the claim that "performance is stable across window sizes" would be stronger with evidence from additional datasets.

5. **No discussion of computational cost or runtime**: The paper motivates linearisation for parallel efficiency but provides no runtime or memory measurements, making the practical advantage unclear.

### Trivial
None that survive filtering.

## Nice-to-Haves

- An ablation comparing FACTS with standard (non-set-function) embedders/projectors against baselines with the same embedders, to isolate the core model's contribution.
- A comparison between the full state-dependent version (equation 10, even if trained with limited window sizes) and the linearised version, to quantify what is lost.
- Specification of what the "set functions" and the "permutation-invariant decoder" actually are, with verification of their invariance properties.
- Error bars for Tables 1 and 2.

## Removed Points

The following points from the reviewer inputs were removed with justification:

1. **"Theoretical analysis does not cover the implemented model"** (Harsh Critic): The critic claimed Theorem 1 (L.P.E./R.P.I.) is proven only for equation 10, not the linearised version. This is factually incorrect — Theorem 1 explicitly states "FACTS as defined in **equation 20** is L.P.E. and R.P.I." and equation 20 IS the linearised version. The paper's theory does cover the implemented model. *[Removed as factually wrong.]*

2. **"No comparison against the original Mamba (Gu & Dao, 2023)"**: The paper compares against S-Mamba, which is a time-series adaptation of Mamba and the appropriate baseline for the forecasting tasks. Demanding the original NLP-focused Mamba on these tasks is not reasonable. *[Removed — evaluates against wrong class of expectations.]*

3. **"Appendix contents (Figure 8, Table 7) missing"** / "claim about SAVi not supported by shown data": The parser strips appendix sections from all papers. These figures and tables exist in the original submission. *[Removed per rule about parser-stripped appendix content.]*

4. **Strength Finder: Generic/unverified strengths**: The Strength Finder's claims about "formal proof" and "empirical robustness to permutation" are kept as verifiable. Its generic phrasing about "competitive performance" is kept but contextualized with the pre/post-processing confound. No strengths were removed as they are all backed by evidence in the paper.

5. **"The attention-based routing is essentially cross-attention"**: While technically accurate, the paper presents this as a "routing mechanism" (which it is — it's cross-attention used for routing), not as a novel attention mechanism. The novelty is in how it integrates with the factored state-space recurrence. *[Removed as a framing nitpick that does not identify a real flaw.]*

6. **Strength Finder conflicts**: The Strength Finder says "Linearisation for efficient parallel computation" is a strength. The Harsh Critic says the linearisation abandons the core claim. These are not in direct conflict — the strength (parallel efficiency) is genuine, while the weakness is about the gap between claims and implementation. Both are kept in their respective sections since they address different aspects.

## Novel Insights

The most interesting tension revealed by the reviews is between the paper's theoretical framing (a recurrent, state-dependent routing mechanism) and its practical implementation (a fixed-initial-state-dependent routing with linear recurrence). This mirrors a broader tension in the SSM literature: the most expressive formulations (full state-dependent parameterisation) sacrifice parallelisability, while the efficient variants (input-dependent but not state-dependent) lose some adaptive capacity. The paper's Figure 3 suggests the linearisation is surprisingly benign on Electricity, but the mechanism for this robustness is unclear — it could be that the segmentation strategy provides sufficient adaptation, or that the Z₀-dependent routing already captures the structure needed. A deeper investigation into when and why the linearisation works would be a valuable contribution beyond this paper.

## Suggestions

1. **Add a controlled ablation** for the time series experiments: either run baselines with the same set-function embedders/projectors, or run FACTS with the standard TSLib embedders/projectors (if possible given architectural constraints). This would isolate whether FACTS's gains come from its core recurrence or from better pre/post processing.

2. **Reposition the paper's claims** to accurately reflect what is tested. The linearised version is a practical, efficient model with permutation-invariant properties. The state-dependent routing (equation 10) can be presented as a more expressive variant for future work rather than the main claimed contribution.

3. **Describe the set functions and decoder** used in experiments, and verify (theoretically or empirically) that the full system preserves permutation invariance. Alternatively, acknowledge if invariance comes from these components rather than the core recurrence.

4. **Add error bars** to Tables 1 and 2. Report statistical significance of the claimed improvements.

5. **Include runtime/memory comparisons** to quantify the parallel efficiency gained by linearisation.

## Score and Decision

The paper presents a genuinely interesting idea — a factored, permutation-invariant state-space memory with attention-based routing — and validates it across diverse tasks with competitive results. However, two issues prevent acceptance in current form: (1) the experimental comparison in Table 1 is confounded by non-standard pre/post processing that is not ablated, making it unclear whether the core FACTS architecture or the set functions drive the reported gains; (2) the paper's central framing of "dynamic, state-dependent routing" describes a model that is never trained or evaluated — the tested model uses a fixed-initial-state routing, a significant gap that is not adequately discussed. These issues can be addressed with substantial revisions, but as submitted they undermine the paper's ability to support its strongest claims.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>