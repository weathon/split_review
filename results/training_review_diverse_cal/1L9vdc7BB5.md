Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper proposes Adapt, a deep continuous prompting method for vision-language models (CLIP) that uses iterative pruning (based on saliency criteria like Snip) to automatically determine heterogeneous context lengths across layers and between image/text branches. The method replaces the fixed-context-length constraint of prior prompt tuning approaches (CoOp, VPT, MaPLe) with an adaptive, pruning-driven allocation. Experiments on 11 datasets show an average accuracy gain from 79.83% (best baseline MaPLe) to 81.70%, with peak gains of 9.63% on Aircraft, while reducing trainable parameters by over 50% with minimal accuracy loss.

## Strengths

- **Clear empirical improvement across diverse benchmarks.** Adapt raises average test accuracy from 79.83% to 81.70% across 11 datasets, with a performance gain of 9.63% on Aircraft and 6.13% on EuroSAT (Table 1). This breadth of validation across domains strengthens the generality of the method.

- **Novel application of network pruning to determine prompt structure.** Adapt is the first work to use iterative pruning (Snip-based saliency) to automatically determine per-layer context lengths, rather than requiring manual design of prompt depth and width. The resulting binary masks (Figure 3) confirm that context lengths are highly heterogeneous across layers and between branches, fulfilling the paper's core design goal.

- **Substantial efficiency gains with minimal accuracy regression.** Reducing τ_target from 128 to 64 cuts trainable parameters by 52.37% with only a 0.60% accuracy drop; further reduction to 32 yields a 77.16% parameter decrease with a 0.61% drop (Table 2). This validates that the pruning mechanism effectively eliminates redundant tokens.

- **Principled motivation from surgical fine-tuning.** The paper grounds its design in the observation (Lee et al., 2022) that different layers deviate differentially from optimal weights depending on the distribution shift type, providing a conceptual rationale for why heterogeneous prompt lengths could be beneficial.

## Weaknesses

### Fatal

None. The method as a whole produces clear empirical gains, and no fundamental error invalidates the results.

### Major

1. **The paper does not isolate whether heterogeneous allocation is the source of improvement.** Adapt differs from its baselines (VPT, MaPLe, CoOp) in multiple dimensions beyond heterogeneity: (a) Adapt inserts prompts only into key and value projections, whereas VPT and MaPLe insert prompts into query, key, and value; (b) the total number of trainable prompt tokens varies; (c) the pruning process itself may act as a regularizer. A controlled ablation that keeps the same KV-only insertion and the same total token budget (τ_target) but distributes tokens uniformly across layers (rather than adaptively) is essential to test whether heterogeneity specifically drives the gains. Without it, the improvements could stem from removing the query prompt, from the pruning-induced regularization, or simply from having a different total token count. The paper's framing rests on heterogeneity being the mechanism, but the experiments do not isolate it.

2. **Missing random-pruning baseline.** Three saliency criteria (Snip, gradient norm, l₂-norm) produce nearly identical results (81.70%, 81.65%, 81.60% average accuracy). This near-equivalence suggests that the specific importance score may not matter much — what matters is that *some* pruning occurs. A random-pruning baseline with the same budget and schedule is essential to determine whether the saliency criterion is actually driving the benefit. Without it, the paper overclaims the role of the saliency criterion as a distinguishing feature of the method.

### Minor

1. **Key algorithmic parameters are absent from the main text.** The accumulation period (n_k) and pruning rate (r_p) are defined but their numerical values are not stated in the main text (line 111). While these may appear in the appendix, the main text should give the reader enough information to understand the pruning schedule without consulting supplementary material. Warmup length (5 epochs) is given, but the number of pruning steps and the step interval (per batch? per epoch?) are not specified.

2. **Internal inconsistency in prompt insertion description.** Line 97 states that Adapt "inserts continuous prompts only for query and value," but the equations (lines 100-101) and Figure 2(c) caption both show that prompts are actually inserted for key and value (Q=f_q(x) with no prompts; K=f_k([P,x]), V=f_v([P,x])). This is a textual error — the method correctly uses KV-only insertion as confirmed by the equations — but the inconsistency is confusing.

### Trivial

None.

## Nice-to-Haves

- A visualization (e.g., a heatmap or table) showing the final context-length distribution across the 12 layers for several representative datasets would give readers useful intuition about what patterns Adapt learns.
- The "Adapt (Adaptive τ_target)" variant uses the validation set to select τ_target per dataset — a form of dataset-specific tuning that the fixed-τ_target baselines do not receive. Although Adapt with fixed τ_target is already provided, the paper should acknowledge this fairness asymmetry explicitly.
- Reporting sensitivity of results to the pruning hyperparameters (n_k, r_p) would strengthen reproducibility.

## Removed Points

- **Criticism that three saliency criteria producing similar results invalidates the approach**: Retained but downgraded to Major weakness #2 because the issue is real (a random-pruning baseline is missing), not that the saliency criteria are meaningless.
- **Criticism about "GLOPS" should be "FLOPs"**: Removed — pure formatting/spelling nitpick per instructions.
- **Criticism about "Snip!·" formatting artifact**: Removed — parser artifact, not an author error.
- **Criticism about missing appendix details (n_k, r_p)**: Downgraded from a major omission to Minor #1, as the appendix presumably contains these values, but the main text is indeed underspecified.
- **Criticism that Adapt's KV-only insertion "confounds comparison"**: Kept substantively in Major #1 (the core issue is the absence of a uniform-allocation ablation controlling for this design difference), but removed the framing that this alone is fatal — it is one of several confounds that together motivate the need for a controlled ablation.

## Novel Insights

The most useful insight that emerges from the intersection of all reviews is that the Adapt paper has a genuine contribution (a novel pruning-based method for automatic prompt length determination that works well empirically) but a framing gap: the paper claims heterogeneity is the mechanism, while the experimental design does not actually isolate heterogeneity from other design choices (KV-only insertion, pruning regularization, different token budgets). The near-identical performance of three different saliency criteria further suggests that the specific choice of importance metric may be less critical than having a principled budget-constrained pruning process. This distinction matters because it shifts what the paper's actual contribution is: not "heterogeneity helps" (unproven), but "pruning-based prompt allocation is an effective way to determine prompt structure without manual tuning" (well-supported).

## Suggestions

1. **Add a uniform-allocation ablation**: Keep KV-only insertion and the same τ_target budget, but distribute tokens uniformly across layers. Compare Adapt (heterogeneous) against this uniform baseline. If Adapt wins, the heterogeneity claim is directly supported. If not, reframe the contribution around the pruning-based allocation process.
2. **Add a random-pruning baseline**: Same total budget and schedule, prune based on random scores. This will clarify whether the saliency criterion matters or whether any budget-constrained pruning suffices.
3. **State n_k, r_p, and the pruning step interval explicitly in the main text** (even if just one sentence), and consider including a sensitivity analysis for these hyperparameters.

## Score and Decision

The paper presents a plausible new method for deep prompt tuning with clear empirical gains and a novel connection to network pruning. The missing ablations (uniform-allocation control, random-pruning baseline) are real and prevent full attribution of the mechanism, but they do not invalidate the empirical contribution — the method works, it is efficient, and the idea is original. The paper can be strengthened substantially with these additions.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>