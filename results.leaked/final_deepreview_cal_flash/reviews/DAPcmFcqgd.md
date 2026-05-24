Now I'll synthesize the final review.

## Summary

This paper proposes MoEP (Modular Expert Paths), a decoder-only architecture that combines layer-level parallelism with top-k Mixture-of-Experts gating to introduce sparsity while keeping the total parameter count fixed relative to a dense baseline. The method interleaves dense GPT-2 layers with a sparse stack of parallel blocks at reduced hidden dimension, using shrink/grow MoE projections to manage dimensionality transitions. Evaluated on the BabyLM strict-small track (~10M words, 28M parameters), MoEP achieves a macro average of 49.00 (excluding AoA), outperforming its primary GPT-2 baseline (48.10) by 0.9 points, and reaches 44.50 on the overall average (including AoA), which edges the GPT-BERT causal model's 41.20.

## Strengths

- **Novel architecture for fixed-parameter sparsity.** MoEP introduces a genuinely new way to apply layer-level sparsity without increasing total parameters. The design combines top-k routing over parallel blocks with MoE shrink/grow projections (Section 3, Figure 2), distinguishing it from prior layer-level MoE work that adds LoRA weights to a frozen model (MoLE). This is a clean, well-motivated architectural contribution.

- **Controlled, reproducible experimental setup.** All models share the same tokenizer, training data, seed, and evaluation pipeline (Section 4). Training is conducted on the same BabyLM strict-small data with identical pre-tokenization and checkpoint selection procedures. The authors release code and model weights, making the results attributable to architecture rather than uncontrolled confounds.

- **Training dynamics analysis provides insight.** Appendix A.3 shows that MoEP reaches its best fast-evaluation scores by the 30M-word checkpoint, while GPT-2 takes longer. This "early learning" characterization—though qualitative—offers a concrete behavioral difference between the sparse and dense architectures that goes beyond final scores.

- **Practical comparison of expert types.** The comparison between linear experts and SwiGLU experts (Table 1) yields a clear finding: lightweight linear projections outperform more complex SwiGLU projections at this scale. This is a useful design guideline for small sparse models.

## Weaknesses

### Major

- **Overclaimed results in abstract and introduction.** The introduction states that "MoEP was able to outperform all BabyLM strict-small baseline models, including the GPT-2 and GPT-BERT models as well." This is only true on one of the two reported macro averages (the one including AoA, where MoEP scores 44.50 vs GPT-BERT's 41.20). On the excluding-AoA macro average—arguably the more standard metric since it matches the leaderboard convention—GPT-BERT achieves 54.10 vs MoEP's 49.00, a 5.1-point gap against MoEP. Section 5.1 correctly clarifies this qualification, but the abstract and introduction omit it, creating a misleading first impression. The core contribution does not need this overstatement—the paper already shows a defensible improvement over the GPT-2 baseline.

- **Missing standard MoE baseline.** The paper frames itself as improving upon the MoE paradigm, yet it never compares against a standard top-k FFN-level MoE (e.g., replacing the FFN sublayers with 4 experts, top-2 routing) matched for total parameters. Without this comparison, the reader cannot tell whether MoEP's double-gating mechanism (parallel-block routing + expert routing) is beneficial or harmful relative to a well-understood simpler MoE approach. This is the single most informative missing experiment.

- **No significance testing or multiple runs.** All results in Table 1 are single-run with no variance estimates. The 0.9-point advantage over the GPT-2 baseline (49.00 vs 48.10) is small, and individual tasks show 20+ point swings between configurations (e.g., Entity Tracking: 13.15 for GPT-2 vs 35.65 for MoEP—a 22.5-point difference that itself raises questions about metric stability). Without multiple seeds or confidence intervals, the robustness of the reported improvements cannot be assessed.

- **No efficiency measurements despite "Efficient" in the title.** The paper provides no FLOPs, activated parameter counts, throughput, or wall-clock time measurements. The claim of "efficient" sparsity is supported only by the parameter count being fixed, not by any direct efficiency metric. For a paper whose title includes "Efficient," this is a significant gap.

### Minor

- **The fixed-parameter sparsity relies on a hidden-dimension bottleneck (d_P=192 vs d_L=384) that is not ablated.** The paper acknowledges in the conclusion that this trade-off may not generalize to more complex data, but it does not explore the Pareto frontier of d_P vs. performance. A simple sensitivity study varying d_P (or the number of parallel blocks P) would substantially strengthen the empirical contribution.

- **MoEP-SwiGLU (38M params) breaks the fixed-parameter premise.** This variant is included in the primary comparison table without a correspondingly larger dense baseline. It should be either removed from the main table or given a matched baseline with comparable parameter count.

- **The training dynamics analysis is purely qualitative.** The claim that MoEP "extracts useful patterns earlier" (Appendix A.3) is based on visual inspection of learning curves. A quantitative measure (e.g., area under the early learning curve, or time to reach a threshold score) would substantiate this claim.

- **The load-balancing loss uses two separate auxiliary losses** (Equation 3: λ^block and λ^expert), but no ablation shows that both are necessary, or that the chosen coefficients are well-tuned.

### Trivial

- None that warrant mention.

## Nice-to-Haves

- Adding a standard top-k FFN MoE baseline with matched parameters is the most impactful experiment the paper is missing.
- Reporting results with at least 3 random seeds and standard deviations would address the most significant evidential weakness.
- Including wall-clock training time and inference throughput (or activated FLOPs) would justify the "Efficient" in the title.
- An ablation of the hidden-dimension ratio d_P/d_L would turn the paper's central trade-off from an acknowledged limitation into a studied design dimension.

## Removed Points

- **"Table 1 directly contradicts the abstract"** — This is removed because it mischaracterizes the situation. The abstract claims outperformance over GPT-2, which is supported on both metrics. The introduction's stronger claim about GPT-BERT is true on the including-AoA metric, so there is no contradiction, only a failure to qualify which metric is used. The criticism is retained in spirit but reframed as an overclaim weakness.
- **"Figure 1 is confusingly general"** — This is a presentation opinion with no concrete evidence that readers are confused. Removed as speculative.
- **"The 'outperforms all baselines' claim is false"** — Demoted from "false" to "overclaimed because the qualifier is omitted." The claim is supported on one of two reported metrics.
- **Missing related works references** — Removing per instructions (no external confirmation possible).
- **Formatting/style nitpicks** (e.g., "textbfAdamW") — Parser artifact, removed.
- **Speculation about appendix contents that may have been stripped** — Removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Restructure the narrative to center on what the paper actually demonstrates: a novel fixed-parameter sparse architecture that marginally beats a matched dense GPT-2 on BabyLM, with evidence of faster early learning. Drop the GPT-BERT "outperforms all" framing or qualify it precisely from the abstract onward.
2. Add a standard top-2 FFN MoE baseline with matched total parameters. This single experiment would clarify whether MoEP's architectural complexity is justified.
3. Run all experiments with at least 3 seeds and report variance. The 0.9-point gap over GPT-2 needs error bars to be interpretable.
4. Add efficiency metrics (activated parameters per token, wall-clock time, or FLOPs) to substantiate the "Efficient" claim.
5. Ablate the hidden-dimension ratio d_P/d_L to characterize the central trade-off of the method.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- *Low band (avg < 3.5):* MOEfication by Experts as Masks (3.40), NanoMoE (3.00), EfficientSkip (2.50) — all rejected. These papers have more severe flaws or less coherent contributions.
- *Middle band (3.5–7.5):* MoLEx (6.33, accept), SmalltalkLM (7.33, accept), Fantastic Experts (4.33, reject), More Experts Than Galaxies (5.67, accept), Q-Sparse (4.75, reject).
- *High band (7.5+):* OLMoE (8.67, accept), MoE++ (8.00, accept) — these are large-scale, thoroughly-evaluated works.

**Round 2 (Narrowing 4.0–6.0):**
- *Sparsing Law* (5.25, reject) — more comprehensive quantitative analysis but less architectural novelty. Similar evaluation scale.
- *COrAL* (5.75, reject) — more extensive experiments on iterative refinement. Comparable novelty level.
- *White-box LM* (4.33, reject) — interesting idea, weak evaluation. Comparable evaluation quality.
- *Q-Sparse* (4.75, reject) — similar issues with missing efficiency measurements and limited baselines. Similar evaluation maturity.

**Round-1 bracket:** `[4.0, 6.0]` — above the clearly-flawed weakest papers but below well-executed MoE studies.

**Narrowing:** The paper is comparable to Q-Sparse (4.75) in having a genuinely novel idea paired with a limited evaluation. It has more architectural novelty than Sparsing Law (5.25) but weaker quantitative analysis. On balance, it sits below the 5.5+ papers because the central claims are overblown and key baselines are missing. The architecture contribution is real but the evidence is too thin to accept.

**Final score: 4.5**

### Decision

**Reject**

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>