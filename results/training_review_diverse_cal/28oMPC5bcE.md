Now I have a thorough understanding of the paper and the reviewer inputs. Let me write the final consolidated review.

## Summary

UNComp introduces matrix entropy (effective rank) as a measure of uncertainty to guide adaptive compression of both hidden states and KV cache across layers and attention heads in LLMs. The method groups layers and heads by their effective rank, assigning different context window sizes accordingly, all without additional training. Evaluated on 16 LongBench tasks across 4 models against 4 baselines, UNComp achieves strong performance at high compression ratios (down to 4.74% of original KV cache size), with notable prefilling-stage speedups of up to 1.6×.

## Strengths

- **Novel use of matrix entropy for adaptive, training-free compression**: The paper introduces effective rank as a principled measure to guide compression decisions across layers and heads, departing from uniform compression schedules or token-level importance scoring used in prior work. This is supported by analyses in Figure 1 (effective rank trends across layers) and Figure 3 (heatmap across layers and heads), showing systematic variation that the method exploits.

- **Training-free grouped-query attention**: Unlike MQA, GQA, or MLA that require retraining or fine-tuning, UNComp determines groups from effective rank computed on a small calibration set (Wikitext2), making it practical as a plug-and-play module. This is a meaningful practical advantage.

- **Competitive empirical results across diverse settings**: In the main table (Table 1), UNComp (Ours-group) achieves the highest average score on all four models (e.g., 40.21 on Llama3-8B vs next best 38.88) at the same KV cache size as baselines. The evaluation covers 16 tasks, 4 models, and 4 strong baselines (H2O, SnapKV, PyramidKV, CHAI).

- **Prefilling-stage speedup via hidden-state compression**: UNComp addresses an underexplored bottleneck by compressing hidden states before KV cache generation, achieving 1.58× prefilling speedup (Table 5). Most prior work compresses only after KV cache generation, leaving the prefilling stage's time cost unaddressed.

- **Effective token-selection mechanism**: The paper introduces a principled method (Section 3.4, Figure 4) using Pearson correlation between compressed and full KV cache entropy trends to determine the H/R token retention ratio, providing empirical grounding for token selection.

## Weaknesses

### Fatal
None.

### Major

1. **The conceptual link between effective rank and compression direction is inconsistently motivated for layers vs. heads.**  
   The paper uses the same statistic (effective rank) to drive *opposite* compression behaviors: for layers, higher effective rank → *more* tokens discarded (line 91); for heads, higher effective rank → *fewer* tokens evicted (line 91, item iii). The stated justification ("Tokens of the same head in different layers gradually share information as the layers deepen, while tokens of different heads do not share information") is asserted rather than derived and does not follow from the entropy measure itself. The method may work empirically, but the paper presents it as a theoretically grounded uncertainty measure when the link between entropy and eviction is at best heuristic. This weakens the claimed novelty — the core mechanism is effectively a schedule guided by a proxy statistic with two different and unprincipled behavioral rules.

2. **Key algorithmic hyperparameters are not specified or ablated.**  
   The grouping procedure depends on: the threshold ε (Equation 4) for inter-layer grouping; S_max and S_min for initial/final context sizes; and Δs_h (the step size between head groups). None of these are derived from the entropy analysis — they appear to be hand-chosen. No ablation study examines how performance varies with these parameters. Without this, it is unclear whether the entropy measurement or the specific parameter choices drive the reported improvements. A baseline applying the same per-layer/per-head compression rates *not* based on entropy (e.g., random or uniform grouping) is also missing.

### Minor

1. **The "1.41% performance loss" claim is ambiguously presented.**  
   The abstract and introduction state "only a 1.41% performance loss" at 4.74% compression. Examining Table 1 for the relevant setting (Llama3-8B at 4.74% compression): FullKV = 41.62, Ours-group = 40.21, a difference of 1.41 *points*. The relative loss is 1.41/41.62 ≈ 3.4%. Similarly, for Llama2-7B, the paper says "0.77% performance loss" (Section 4.2) where the actual drop is 0.77 points (33.34 → 32.57). The paper uses absolute score differences as if they were percentages, which is misleading — these are not accuracy percentages but aggregate scores across diverse tasks. A clarifying note on whether this is relative or absolute would resolve the confusion.

2. **Needle-in-a-haystack superiority claim is overstated.**  
   The paper claims UNComp "outperforms the full-size KV cache" in needle-in-a-haystack tasks. In Table 4, this holds only for Llama2-4k (Ours-group-stage: 98.80 vs FullKV: 98.70, a 0.1-point advantage), while for Llama3-8k, both variants are *below* FullKV (84.13 and 83.73 vs 84.99). No error bars or significance tests are provided. The paper would be better served by claiming parity rather than superiority.

3. **The prefilling speed comparison for Ours-group-stage is not apples-to-apples.**  
   Ours-group-stage compresses hidden states (reducing the number of tokens processed during prefilling), while baselines (H2O, SnapKV, etc.) process all tokens and only prune the KV cache *after* generation. The 1.4–1.6× prefilling speedup in Table 5 partly reflects input-length reduction rather than a novel KV cache innovation. The paper should isolate the effect of hidden-state compression by also comparing against a method that similarly reduces input token count, or clearly state that this speedup is attributable to input-length reduction.

4. **Misleading claim about head effective rank being "intrinsic" / "not data-dependent."**  
   Section 4.2 states "the effective rank of the heads is not data-dependent, as it is an intrinsic characterization." However, the effective rank is computed from the covariance matrix of the token sequence on Wikitext2 calibration data, which is data-dependent. The subsequent heatmap (Figure 3) showing consistent patterns across datasets suggests *low dataset dependence*, not that it is intrinsic. The statement as written is inaccurate.

### Trivial

- The sustained accuracy claim for extreme compression (Table 2) is too strong: Ours-delete-8-heads scores 22.28 vs FullKV 30.54 (a ~27% relative drop), yet the paper says it demonstrates "a high level of accuracy."
- Justification for truncating eigenvalues to top-k ("to avoid the positive semi-definite issue") is unnecessary — von Neumann entropy is well-defined for PSD matrices.

## Nice-to-Haves

- Add an ablation that applies the same non-uniform compression rates but with random grouping (i.e., not entropy-guided) to isolate the effect of the entropy measurement from the mere fact of non-uniform compression.
- Report the overhead of computing matrix entropy on Wikitext2 (time, data volume, computational cost).
- Add sensitivity analysis for the key hyperparameters: ε (threshold for layer grouping), Δs_h (step size between head groups), and the choice of S_max/S_min.
- The throughput comparison (6.4×) compares at different batch sizes (6 vs 32). While this reflects real-world gains from reduced memory, reporting throughput at a fixed batch size for isolation would also be informative.

## Removed Points

These points were raised by reviewers but are removed or downgraded per the consolidation guidelines:

- **"The core premise connecting entropy to eviction may be internally inconsistent"** — Kept as Major weakness #1, as the inconsistency is real.
- **"1.41% performance loss does not match table numbers"** — Kept as Minor weakness #1, but reframed as a presentation issue rather than a "significant reliability issue" or evidence of "selective reporting."
- **"The comparison is apples-to-oranges for hidden-state variant"** — Kept as Minor weakness #3. However, the claim that speedup is "not from a novel innovation" is removed — the paper's innovation includes hidden-state compression, which is legitimate. The issue is only that baselines don't do the same.
- **"Needle-in-a-haystack claim is overstated"** — Kept as Minor weakness #2, reframed to reflect the actual data (works for one of two models).
- **"Grouping procedures are under-specified"** — Kept as Major weakness #2.
- **"Effective rank is not data-dependent"** — Kept as Minor weakness #4.
- **"Eigenvalue truncation justification is weak"** — Moved to Trivial; the point is technically correct but carries no evaluation weight.
- **"Extreme compression 27% drop contradicts claim"** — Moved to Trivial.
- **"Missing baseline (entropy vs random grouping)"** — Moved to Nice-to-Haves.
- **"Overhead of matrix entropy not reported"** — Moved to Nice-to-Haves.
- **"Throughput claim based on different batch sizes conflates factors"** — Moved to Nice-to-Haves; different batch sizes are standard in throughput analysis and reflect real practical benefit.
- **"Paper does not discuss sequence length effect on entropy computation"** — Removed; the paper uses a fixed calibration set and groups are applied offline, so this is not a meaningful gap. The covariance matrix dimension is hidden_size (fixed), not sequence length.

## Novel Insights

The most interesting observation from the reviews is the unresolved tension in the paper's theoretical framing: the same entropy measure is used to justify *increased* compression for deeper layers but *decreased* compression for higher-entropy heads. This suggests the paper may be using effective rank as a useful heuristic without a unified theoretical account of why it works. One reviewer insightfully notes that alternative interpretations exist — e.g., high effective rank could indicate isotropic (redundant) representations making eviction safe, or low effective rank could signal dimensional collapse making each token irreplaceable. The paper currently mixes both directions without committing to a consistent rationale. Resolving this tension would significantly strengthen the contribution.

## Suggestions

1. Provide a single, consistent hypothesis for the relationship between effective rank and eviction safety. For example: if high effective rank indicates token representations are isotropically distributed (spherical covariance), then tokens are redundant and discarding them is safe. Or the reverse. But not both depending on whether one is talking about layers or heads.

2. Add an ablation study showing how performance changes when the threshold ε, step size Δs_h, and S_max/S_min are varied. This would demonstrate that the entropy measurement (not the specific schedule) drives the improvement.

3. Clarify whether the "1.41% performance loss" is relative to the FullKV score or an absolute point difference.

4. Add a baseline that uses the same non-uniform compression rates but with random (or uniform) grouping to isolate the effect of entropy-guided selection.

5. Commit to a single variant for the main comparison: Ours-group (KV-only) or Ours-group-stage (hidden-state + KV). Present the other as an extension. This avoids the fairness concerns in speed comparisons.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>