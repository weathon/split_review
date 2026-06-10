Here is the synthesized final review.

## Summary
This paper introduces DynMoE, a method that automates two critical hyperparameters of Sparse Mixture of Experts (SMoE): the number of experts activated per token (top-k) and the total number of experts. It does this via (1) a "top-any" gating mechanism using cosine similarity and per-expert learnable thresholds, (2) an adaptive process that adds/removes experts during training, and (3) a custom auxiliary loss for sparsity. Experiments span vision (DomainBed), language (GLUE), and vision-language (10 benchmarks × 3 LLM backbones).

## Strengths
- **Novel gating mechanism**: The top-any gating (Eq. 2–4) replaces fixed top-k selection with per-expert trainable thresholds and cosine-similarity scoring, allowing each token to activate a variable number of experts. This is a genuine architectural departure from standard SMoE gating (Shazeer et al., Switch Transformer, GShard).
- **Adaptive expert management**: Algorithm 1 describes a practical procedure for adding experts when tokens activate none and removing unused experts, run every 100–300 iterations. This is demonstrated across three backbone scales (StableLM-1.6B, Qwen-1.8B, Phi-2-2.7B).
- **Consistent efficiency gains**: Table 4 shows DynMoE achieves higher throughput than MoE-LLaVA across all three backbones (26 vs 19 tokens/s for StableLM, 23 vs 18 for Qwen, 18 vs 14 for Phi-2) with identical expert pools and GPU/memory configurations.
- **Cross-modality validation**: The paper evaluates on vision (4 datasets from DomainBed), language (5 GLUE tasks), and vision-language (10 benchmarks × 3 backbones), providing broad evidence of general applicability beyond any single modality.
- **Downstream architectural insights**: Section 4.4 reports that top MoE layers (closest to the LM head) tend toward single-expert activation while bottom layers activate all experts uniformly—a design insight that aligns with shared-expert architectures like DeepSeek-MoE and is empirically grounded across three different LLM backbones.

## Weaknesses

### Major
- **No variance/statistical reporting**: Every result (Figure 2, Tables 1–4, ablation tables) is reported as a single number with no standard deviations, error bars, or multiple seeds. Many performance differences are under 1% (e.g., Table 1: 72.4% vs 72.8%; Table 2: numerous 0.1–0.5% gaps). Without variance estimates, the reader cannot determine whether DynMoE is equivalent to, slightly better than, or slightly worse than baselines. When the paper attributes a 0.4% gap to "random fluctuation" (line 307), this is an assertion without supporting evidence. This does not invalidate the paper's contribution—the cross-backbone, multi-benchmark consistency provides some mitigations—but it substantially weakens confidence in the precise comparative claims.

### Minor
- **Overclaiming in select passages**: The conclusion (line 507) claims "comparable or even superior performance across various MoE model settings." The evidence supports *competitive*, not *superior*. In Table 2, DynMoE wins roughly half and loses roughly half of benchmarks against MoE-LLaVA depending on the backbone. Similarly, line 307 claims DynMoE "outperforms standard MoE" on vision, but Table 1 shows mixed results (wins on two datasets, loses on one). The honest and sufficient story is that DynMoE achieves competitive performance while automating hyperparameters—this alone is a real contribution and should be stated without overreach.
- **Partial auto-tuning**: While DynMoE automates top-k and total expert count during training, the user must still set the maximum number of experts (16 for vision/language, 4 for vision-language) and the initial expert count (6 for vision, 2 for vision-language). These are nontrivial design choices. The paper acknowledges this (line 230: "due to the device constrain, the maximum number of experts should be constrained") but the "auto-tuning" framing understates the remaining manual configuration burden.
- **No independent ablation of the auxiliary loss components**: The auxiliary loss (Eq. 7) combines a diversity term (‖W_g^T W_g − I‖₂, encouraging orthogonality) and a simplicity term (L2 regularization). Table 1 compares DynMoE with GShard loss vs. the proposed loss, but the two terms within the proposed loss themselves are not ablated independently. It is unclear whether both terms are necessary or whether one dominates.
- **Missing comparison against related routing-free methods**: Expert Choice routing (Zhou et al., 2022) and SoftMoE (Puigcerver et al., 2023) are discussed in Related Work as methods addressing similar MoE design challenges, yet neither appears as an experimental baseline. While they operate under different routing paradigms (expert-chooses-token, soft slot-based), including them would strengthen the claim that DynMoE offers a distinct advantage in hyperparameter automation.

### Trivial
- None.

## Nice-to-Haves
- Quantify how many tokens fall back to the top-1 fallback at test time (Eq. 5). This would validate whether the adaptive mechanism is working as intended or the fallback is doing most of the work.
- Ablate the adaptive process: what happens with top-any gating but without expert addition/removal? This would isolate the contribution of each component.
- Test sensitivity to the check interval (100–300 iterations) for the adaptive process.
- Report results from at least 3 random seeds with standard deviations for key comparisons.

## Removed Points
These points from the reviewers were considered and removed or demoted with justification:

- **"Comparing against average performance is the wrong baseline"** (Harsh Critic): REMOVED. The paper reports individual configuration results alongside the average (Figure 2) and states DynMoE "achieves the highest number of top-1/2 best performances." The average comparison is a reasonable summary measure, not a substitute for individual comparisons.
- **"Training/test gating discrepancy is a problematic hack"**: WEAKENED to Nice-to-Have. The paper describes the test-time fallback to top-1 for zero-activation tokens (Section 3.1, Eq. 5) as a practical engineering solution. Analyzing its frequency is a nice-to-have, but the design choice is reasonable and clearly explained.
- **"Diversity loss orthogonality may prevent beneficial co-adaptation"**: MERGED into the unablated loss criticism (Minor). This is a reasonable methodological question, but the paper does provide an ablation against GShard loss (Table 1, 72.2% vs 72.4%), which partially addresses it.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Add standard deviations or confidence intervals for key results by running multiple seeds.
2. Tone down comparative claims to match the evidence; present DynMoE as achieving *competitive* performance while saving tuning costs—this is sufficient and accurate.
3. Ablate the diversity and simplicity loss terms independently.
4. Include Expert Choice routing or SoftMoE as baselines if feasible.
5. Report the frequency of the test-time top-1 fallback to validate the adaptive mechanism.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>