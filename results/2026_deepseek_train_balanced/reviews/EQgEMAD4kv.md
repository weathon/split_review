Now let me produce the final review.

## Summary
CAKE introduces an adaptive KV cache eviction method that allocates cache budgets across transformer layers based on a "preference" score combining spatial attention entropy and temporal attention variance. The method features a cascading cache management procedure during prefilling (with a proof of equivalence to one-shot allocation) and an eviction indicator that augments mean-attention scoring with a temporal variance term. Experiments across 5 models on LongBench and NeedleBench show consistent gains over uniform and fixed-pattern allocation baselines.

## Strengths
- **Theorem 1 provides a formal guarantee that cascading allocation matches one-shot allocation (lines 126–132).** The paper proves that the staged, incremental eviction during prefilling produces exactly the same final cache as applying the eviction operation once on the full cache. This is a non-trivial theoretical property absent from prior work (e.g., PyramidKV, D2O) and ensures the practical memory-saving mechanism does not degrade allocation quality.
- **The eviction indicator explicitly models temporal attention variability (Eq. 9, lines 140–142).** Unlike H2O (cumulative attention) and SnapKV (clustered recent attention), CAKE's indicator I[n] = Mean(A[-S_w:, n]) + γ·Var(A[-S_w:, n]) captures both sustained importance and attention shifts. The ablation (Section 5.6) validates that the additive combination outperforms mean-only, variance-only, and multiplicative variants, confirming that the temporal-variance term adds measurable value.
- **Compatibility experiments show CAKE's allocation is a general plug-in (Section 5.5).** When CAKE's adaptive allocation is used as a front-end for H2O and SnapKV, it consistently improves both methods across nearly all LongBench tasks. This separates the contribution of the allocation strategy from the eviction indicator and demonstrates generality beyond a single indicator design.
- **10× decoding speedup over full-cache FlashAttention-2 at 128K (Figure 7).** On Mistral-7B, CAKE maintains near-constant decoding latency and achieves a >10× speedup over full-cache FlashAttention-2 for 128K-token inputs, measured against an optimized attention implementation. (This speedup is shared by any fixed-size cache method, but the measurement itself is clean and reproducible.)

## Weaknesses

### Fatal
None.

### Major
1. **Missing comparison against D2O, the most closely related prior work.** The paper cites D2O (Wan et al., 2024) in the related work (line 47) and explicitly critiques it as being "just based on the local layer attention" and lacking "a global perspective on layer preferences." D2O also performs dynamic, attention-adaptive cache allocation — making it the most directly comparable method to CAKE's allocation strategy. Yet D2O is entirely absent from all experimental comparisons (Tables 1, Figures 5–8, Section 5.1 baselines). The paper compares only against PyramidKV (fixed-pattern allocation), which is a substantially weaker benchmark than a method that also adapts dynamically. Without a D2O comparison, the central claim that CAKE's global preference-based allocation is superior to prior adaptive approaches is not substantiated.

2. **Hyperparameter values are never specified, with no sensitivity analysis.** The method introduces τ₁ and τ₂ (temperature parameters on entropy and variance in the preference score, Eq. 6, line 89), γ (weight on variance in the eviction indicator, Eq. 10, line 141), and S_w (the recent window size used to compute attention statistics, lines 89, 141). None of these values are stated anywhere in the paper. There is no sensitivity study, no ablation varying them, and no discussion of how robust the method is to their choice. This is a reproducibility gap and raises the question of whether reported performance depends on careful tuning to the specific evaluation settings.

### Minor
1. **No variance or confidence intervals for any result.** Across all 16 LongBench datasets, multiple models, and multiple memory budgets, the paper reports a single score per condition with no error bars, standard deviations, or significance tests. Many of these tasks exhibit inherent variance across prompts and seeds. Without variance estimates, it is impossible to assess whether CAKE's margins over closely matched baselines — which the paper itself notes are sometimes competitive — are meaningful or within noise.

2. **The 10× speedup is framed as a CAKE-specific achievement.** Section 5.4 (line 200) states "both uniform and non-uniform eviction methods exhibit comparable inference performance" on latency, then immediately states "CAKE demonstrates remarkable efficiency, achieving over 10× speedup" (lines 200–201). The speedup is an artifact of using *any* fixed-size cache, not of CAKE's specific design. The paper's actual throughput contribution — that CAKE's cascading management adds no overhead versus simpler methods — is valid but much weaker than the headline framing suggests.

3. **The entropy-to-importance assumption is untested.** The preference score uses spatial entropy H(A) summed across rows (Eq. 3) to measure how evenly attention is distributed per query, then interprets higher entropy as needing more cache tokens. The implicit assumption that higher per-query entropy translates into more unique tokens being important globally is plausible but not directly validated. The paper does not test this link.

4. **Cascading management overhead is not benchmarked.** The cascading procedure (Algorithm 1) repeatedly recomputes TopK operations at each stage as budgets shrink. The paper claims this "can be parallelized… reducing the time complexity to that of a single iteration" (line 106), but no prefilling-time comparison against simpler methods (e.g., SnapKV) is provided. The practical overhead of the staged allocation is unquantified.

5. **The explanation for surpassing full cache on Single-Needle Retrieval is speculative.** Section 5.3 (line 189) reports that CAKE outperforms the full cache on this task and attributes this to "pruning specific cache information may eliminate superfluous details." This claim is not supported by any analysis — e.g., does random eviction produce the same effect? Is it a dataset artifact? If eviction can improve retrieval accuracy, the full-cache baseline is not the obvious reference, and the phenomenon warrants deeper investigation.

6. **Missing reverse ablation: CAKE's eviction indicator with uniform allocation.** The compatibility experiments (Section 5.5) show CAKE's allocation improves H2O and SnapKV, which convincingly separates the allocation contribution. However, the reverse experiment — using CAKE's eviction indicator with uniform allocation — is not shown. Without this, it is unclear how much of CAKE's overall gain comes from the allocation strategy versus the eviction indicator.

### Trivial
None.

## Nice-to-Haves
- A prefilling-time comparison quantifying the computational cost of the cascading management relative to simple eviction methods.
- Analysis of the Single-Needle Retrieval surpassing-full-cache result to determine whether it reflects a genuine property or a metric quirk.
- The reverse ablation (CAKE's eviction indicator + uniform allocation) to fully disentangle the two contributions.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **Abstract "overclaiming" accusation (Harsh Critic):** Claimed the abstract misleadingly implies CAKE outperforms full cache on accuracy. The abstract states "CAKE outperforms full cache with FlashAttention implementation, achieving 10× faster decoding" — the context makes clear this refers to latency/speed. Removed: misreading of the paper.
- **Multiplicative variance ablation concern (Harsh Critic):** Critic noted the additive combination outperforms multiplicative but the text describes this qualitatively. Reporting ablation results qualitatively with the table for exact numbers is standard practice. Removed: not a weakness.
- **"Random beats uniform" framed as underexplored (Harsh Critic):** The paper mentions this finding in the ablation to motivate why adaptive allocation is needed. It supports the paper's thesis rather than undermining it. Removed.
- **Proofs deferred to appendix (Harsh Critic):** The critic noted proofs of Proposition 1/Theorem 1 are not in the main text. The parser strips appendices from all papers; the original submission contains them. Removed per instructions.

## Novel Insights
None beyond the paper's own contributions. The reviews surface the expected tension between the paper's genuine contributions (the formal guarantee for cascading management, the temporal-variance eviction indicator) and the evaluation gaps (missing D2O baseline, undisclosed hyperparameters). No synthesis yields a fundamentally new observation about the work.

## Suggestions
1. Add D2O as a baseline across all experimental conditions. This is the single most important missing comparison to substantiate the claim that CAKE's global adaptive allocation outperforms prior adaptive approaches.
2. Disclose default values for τ₁, τ₂, γ, and S_w, and include a brief sensitivity analysis varying each by factors of 2 around the default.
3. Report variance estimates — either standard deviations across multiple runs or distributional statistics across tasks within each condition — for at least a representative subset of experiments.
4. Reframe the throughput results to clearly separate what is CAKE-specific (no overhead from cascading management) from what is shared by all fixed-size cache methods (the speedup itself).
5. Either remove or provide rigorous analysis for the claim about surpassing full cache on Single-Needle Retrieval.
6. Add the reverse ablation (CAKE eviction indicator + uniform allocation) to fully disentangle the allocation and eviction contributions.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>