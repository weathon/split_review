## Summary

Dynamic Nested Depth (DND) is a post-training method that enhances LLM performance by selectively reprocessing "critical" tokens through an additional forward pass of the same transformer layer. A lightweight linear router decides, per-token, whether to route it through a nested computation path (with weight sharing) and fuses the result with the vanilla pass using a soft gating mechanism. Two training-side innovations stabilize the selection: a dual-objective router controlling loss (score dispersion + distribution preservation) and a threshold control scheme (buffer proportional control + EMA synchronization). DND is applied to four pretrained models—Qwen3-1.7B, Llama3.2-1B, Gemma3-1B, and Qwen3-30B-A3B—yielding consistent average improvements of 1.88%, 2.61%, 2.50%, and 0.87% respectively with negligible parameter overhead.

## Strengths

- **Practical plug-and-play design.** DND is a post-training method that works directly on off-the-shelf pretrained models without any architectural change at the pretraining stage, making it immediately applicable to state-of-the-art open-source LLMs. Validated across three distinct architectures (Qwen3, Llama3.2, Gemma3) and MoE scale (30B).

- **Comprehensive benchmarking.** Results cover 17+ benchmarks spanning general knowledge, math/STEM, and coding/agent tasks. Gains are consistent across all tasks with zero performance regressions on the 30B MoE model, lending credibility to the core claim.

- **Minimal overhead.** Only ~0.03M parameters added to a 30B model; ~6% extra FLOPs; ~7–8% throughput reduction measured on real hardware (H100). The efficiency-performance trade-off is well characterized.

- **Insightful token analysis.** The correlation between selection frequency and logit entropy (Pearson r = 0.34, positive) and the entropy reduction after nested processing (Pearson r = −0.58, negative) provide principled evidence that the router is learning to identify genuinely uncertain tokens and that the nested pass reduces that uncertainty—not just a cherry-picked visualization.

- **Thorough ablation study.** Table 4 isolates the contributions of router control (RC) and threshold control (TC) individually and jointly, and sweeps the selection ratio (10/20/30%) and layer range. The ablations are decisive: combining RC + TC at 20% with the 4:23 layer range yields the best result, and each component contributes independently.

## Weaknesses

### Fatal
None.

### Major

1. **Uncontrolled compute comparison.** The headline comparison pits vanilla SFT against DND-augmented SFT, but DND increases per-step training FLOPs via the nested forward pass. The paper does not report training FLOPs or wall-clock training time per model. Without this, it is impossible to rule out that the gains come simply from more compute during training rather than from the architectural inductive bias. A fair baseline would be vanilla SFT trained for the same number of FLOPs (e.g., on more steps or with a marginally larger model), or uniform-depth augmentation (reprocessing *all* tokens instead of selected ones at matched FLOPs).

2. **Sparse competitor comparison.** ITT is the only method compared directly, and only on Qwen3-1.7B. Llama3.2-1B and Gemma3-1B results are presented only against their vanilla SFT baselines. The very closely related MOR (Bae et al., 2025) is discussed extensively in related work but never empirically compared, even though a post-training version or a smaller-scale reproduction would be feasible. This gap makes it difficult to assess whether DND's design choices (threshold control, dual loss, normalized fusion) are the source of gains versus the general idea of selective recurrence.

3. **Conceptual tension in the dual routing loss.** The score dispersion loss L_sd maximizes entropy over *normalized* routing scores to spread them apart, while the distribution preservation loss L_dp penalizes raw sigmoid outputs deviating from 0.5 to prevent saturation. Pushing scores toward 0.5 (L_dp) also pushes the normalized distribution toward uniformity, which simultaneously satisfies L_sd. The two objectives are therefore partially redundant rather than antagonistic "push-pull" forces as claimed. Conversely, when scores are truly dispersed (some near 0, some near 1), L_dp would penalize the high/low values and undo the dispersion L_sd worked to create. The paper does not analyze this interference, nor does the ablation (which only shows "with/without RC" jointly) disambiguate the individual roles of L_sd and L_dp.

### Minor

1. **No statistical significance reporting.** For the 30B MoE model, several per-task improvements are very small (BBH: +0.13, MATH: +0.15, MATH-500: +0.20). Only a single run per configuration is reported. Given the known variance of benchmark evaluations, some of these individual improvements may not be reliable. Reporting variance across multiple seeds or runs for at least one model would strengthen confidence.

2. **Training data opacity.** The dataset is described only as "1–2 million instances from human annotations and open-source materials." While industry constraints may apply, the fact that all four models share the same training pipeline means improvements could be partially attributable to data quality differences rather than the DND architecture alone. At minimum, reporting the domain mix would help.

3. **DND layer span sensitivity.** The ablation shows that the best configuration uses layers 4–23 (keeping 4 layers at each end fixed). However, the L_s and L_e indices differ across models (the 30B model has 42 layers vs. 24 for Qwen3-1.7B). It is unclear whether the same span ratio was used or whether the optimal span was tuned separately for each model, which would inflate the experimental effort required to reproduce results on new architectures.

### Trivial

None worth noting.

## Nice-to-Haves

- An analysis of whether DND's improvement scales predictably with the target selection ratio k_target (beyond the 10/20/30% ablation) would illuminate the efficiency-performance frontier.
- Reporting inference latency at batch size > 1 would be more representative of production deployment.
- A visualization of which types of tokens (numerals, operators, key verbs, common function words) get selected across different benchmark domains would complement Fig. 7b.

## Novel Insights

DND's token selection analysis offers a noteworthy empirical finding: not only do higher-uncertainty (high-entropy) tokens get selected more frequently, but the nested reprocessing specifically and reliably reduces their entropy (the selection-frequency vs. entropy-change correlation is −0.58, stronger in magnitude than the selection-frequency vs. initial-entropy correlation of +0.34). This asymmetry suggests that the nested pass acts as a targeted uncertainty-reduction mechanism rather than a generic representation enrichment step—an insight that generalizes the motivation for adaptive computation in transformers. The hierarchical observation that shallow nested layers preferentially select content nouns while deep nested layers preferentially select mathematical expressions and relational verbs is also independently interesting, hinting that the router learns a layer-specific notion of "difficulty."

## Suggestions

- Report training compute (FLOPs or wall-clock time) for DND vs. vanilla SFT, and add a "uniform extra-depth" baseline (reprocess all tokens once) at matched compute as a fairer ablation.
- Disentangle L_sd and L_dp individually in the ablation (currently only "with RC" and "without RC" are shown); an ablation with only L_sd or only L_dp would clarify whether both are necessary.
- Include at least one run with multiple seeds to estimate variance on benchmark scores, particularly for the 30B MoE model where some improvements are sub-0.5 points.

## Score and Decision

DND is a practical, well-motivated method with consistent positive results across four models and a comprehensive benchmark suite. The architectural design is clean and the analysis of token selection behavior is genuinely informative. The two principal concerns—uncontrolled compute comparison and incomplete competitor benchmarking—are legitimate but not fatal: the method still demonstrates value relative to its own ablation baseline, and the MoE result at 30B is in a regime where most competing methods have not been shown. The paper sits slightly above the ICLR borderline as a solid engineering contribution with meaningful, reproducible (modulo data) insights.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>