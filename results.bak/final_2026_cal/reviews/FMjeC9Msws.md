Now let me write the consolidated review.

## Summary

This paper presents a large-scale empirical study (400,000+ GPU-hours) of RL training compute scaling for LLMs. The authors propose a sigmoidal compute-performance curve (Eq. 1) that separates asymptotic performance (A) from compute efficiency (B), and use it to ablate design choices across off-policy architecture, loss functions, precision, normalization, filtering, and curriculum. Combining the best options yields SCALERL, a recipe whose performance at 100,000 GPU-hours closely matches a curve fitted on only the first 50,000 hours, demonstrating predictive scaling. The study is among the largest systematic RL recipe investigations to date and provides both a methodological framework and a practical recipe.

---

## Strengths

**1. Demonstration of predictive scaling to 100,000 GPU-hours (Figure 1a).** The paper fits the sigmoidal curve on the first 50k GPU-hours of an 8B-dense run and shows that the extrapolated curve closely matches the actual validation pass-rate when training continues to 100k GPU-hours. This is the single strongest piece of evidence and directly supports the central claim that RL scaling can be predicted.

**2. Large-scale systematic ablation spanning 400,000+ GPU-hours.** The study varies off-policy setup (PPO-off-policy vs. PipelineRL), loss functions (DAPO, GSPO, CISPO), FP32 precision fix, loss aggregation strategies, advantage normalization variants, zero-variance filtering, and curriculum (No-Positive-Resampling). For each ablation, the paper reports fitted A and B parameters, providing a principled decomposition into asymptotic performance vs. compute efficiency. This scale of controlled experimentation is substantially larger than prior RL recipe studies (the paper notes "6× larger than ProRL").

**3. Leave-one-out (LOO) ablations validate cumulative benefits.** Starting from SCALERL and reverting each design choice individually to its baseline counterpart (Figure 5), the paper shows that SCALERL consistently achieves the highest compute efficiency (slope B). Converting the sigmoidal fit to a linearized form makes efficiency differences directly visible, providing a rigorous attribution of improvements to individual components.

**4. Verification of predictive scaling across multiple compute axes.** The framework is shown to hold when scaling model size (8B dense vs. 17B×16 MoE, Figure 1), generation length (14k vs. 32k tokens, Figure 6a), and batch size (Figure 6c). In each case the extrapolated curve from half the target budget aligns with the extended training trajectory, demonstrating generalization beyond a single configuration.

**5. Cross-recipe comparison and downstream generalization.** SCALERL achieves higher asymptotic performance and compute efficiency compared to DeepSeek (GRPO), Qwen-2.5 (DAPO), Magistral, and MiniMax-M1 under the same evaluation protocol (Figure 2). Scaling trends on AIME-24 (Figure 1b) show that in-distribution improvements translate to a held-out benchmark.

---

## Weaknesses

### Fatal

None.

### Major

**1. No uncertainty quantification for fitted scaling curves.** Every fitted curve in the paper is drawn as a single line, and parameters A, B, C_mid are reported without confidence intervals or standard errors. For a paper that aims to establish a "scientific framework" for scaling, the absence of even basic uncertainty measures (e.g., bootstrap intervals over training steps, or standard errors from nonlinear least squares) undermines the reader's ability to assess whether the reported differences between methods — and indeed the extrapolation accuracy itself — are statistically reliable. The paper mentions that the sigmoidal fit is "robust and stable" (Section 2.1) and defers robustness discussion to Appendix A.7, but the main text lacks any quantitative support for this claim.

**2. The central predictive-scaling claim rests on a limited number of extrapolation checks.** The paper argues that RL performance can be *predicted* from early runs, but the direct evidence consists of: one extrapolation for the 8B dense model (50k→100k GPU-hours), one for the MoE model (16k→45k), a set of LOO variants (8k→16k), and a few scaling-axis checks. Each is a single trajectory without replication. While the consistency across settings is encouraging, and the compute cost makes replication prohibitive, the core claim would be substantially strengthened by a retrospective analysis on the 100k run (e.g., fitting at multiple early cutoffs and reporting how extrapolated A and B vary, or a bootstrap over training steps).

**3. Modest comparative overclaiming.** SCALERL shares its asymptotic pass rate (A=0.610) with MiniMax (Figure 2). The paper's claim that SCALERL "surpasses all other methods" is technically correct when considering both A and B (SCALERL has higher efficiency B=1.97 vs. MiniMax's B=1.77), but the shared asymptote means the superiority is in efficiency, not in ceiling performance. The "state-of-the-art" language in the introduction and abstract should be more precisely scoped to reflect this.

### Minor

**1. Baseline comparison setup lacks sufficient transparency.** The paper states that "further description of the individual recipes compared are given in Appendix A.17" (which was stripped by the parser), but the main text gives no detail on how baselines were configured — e.g., whether hyperparameters were tuned for the same 8B model and math dataset, whether the same PipelineRL asynchronous setup was used, or whether defaults from the original papers were applied as-is. This makes it hard to assess whether the reported gaps (A ranging from 0.490 for GRPO to 0.610 for SCALERL/MiniMax) reflect genuine algorithmic differences or implementation quality. The authors should describe the baseline setup in the main text or clearly state that all methods were run with their published recipe defaults without tuning.

**2. Single-run results throughout.** Every ablation, LOO experiment, and scaling-axis run is a single trajectory. While this is understandable given the compute cost (individual runs reach 16k GPU-hours), the paper occasionally interprets small differences in fitted parameters (e.g., B values differing by 0.1–0.2) without acknowledging that single-run variance could explain the gap. Differences that are internally consistent across multiple related comparisons (e.g., the LOO experiments) are more convincing, but isolated comparisons remain uncalibrated.

### Trivial

None.

---

## Nice-to-Haves

- A retrospective fit analysis on the 100k GPU-hour run: repeatedly fit the curve using the first K% of the run (25%, 50%, 75%) and report how the extrapolated A and B vary, and how well they predict the final value. This requires no additional runs and would concretely measure predictive stability.
- Extend the LOO analysis to include a version where *all* components from the baseline are changed at once, to better separate individual effects from interactions.
- Report the compute cost (GPU-hours or wall-clock time) more precisely for each baseline method, to rule out the possibility that methods with lower throughput simply appear less efficient.

---

## Removed Points

These points were flagged by one or both reviewers but are removed or weakened for the reasons given.

- **"Predictive power is demonstrated on too few instances" (weakened → Major weakness #2):** The harsh critic's framing undercounts the evidence — the paper shows extrapolation checks for the 8B dense model, MoE model, ~9 LOO variants, 3 scaling axes, and cross-recipe comparisons. The retained weakness focuses on the *lack of replication* for each check, which is the substantive concern.
- **"Baseline comparisons may be unfair" (weakened → Minor weakness #1):** The critic's claim that "baselines may not have been tuned fairly" is speculative; there is no evidence of unfair implementation. The retained weakness focuses on the *transparency* of the descriptions in the main text. The paper states that Appendix A.17 provides details, which the parser stripped, so the information exists in the original submission.
- **"GPU-hours conflates wall-clock time with hardware utilization" (removed):** The critic raises this concern but does not provide evidence that different methods had different throughput. All runs use the same hardware (Nvidia GB200 GPUs). Without evidence of a confound, this is speculative.
- **Strength Finder's claim about "release of curve-fitting code" (kept as minor supporting strength):** This is a nice bonus but is too minor to carry weight as a primary strength. I've kept it as part of the broader contribution framing rather than a standalone bullet.
- **"Many choices affect efficiency rather than asymptote" (removed as redundant):** This is a *finding* of the paper, not a weakness. The critic presents it as a correct observation, which it is.
- **Strength Finder's generic strengths about "important problem" and "timely question" (removed):** These are superficial and apply to any paper in a popular area. I have kept only concrete, evidence-backed strengths.
- **"Cross-recipe comparison shows MiniMax ties SCALERL in A" (kept as weakness #3 about overclaiming):** This is accurate and retained in a more precise formulation.

---

## Novel Insights

None beyond the paper's own contributions. The core novel finding — that different RL design choices primarily affect compute efficiency (B) rather than asymptotic performance (A), and that a sigmoidal curve can predict RL scaling from early data — is the paper's own contribution and is well supported by the experiments. The synthesis across reviews does not surface additional insights beyond what the paper already presents.

---

## Suggestions

1. **Add uncertainty estimates** for all fitted scaling-curve parameters. Specifically, use bootstrapping over training steps or a residual-based approach to obtain confidence intervals on A, B, and C_mid. This is feasible without any new GPU-hours and would meaningfully strengthen the methodological contribution.

2. **Perform a retrospective predictive-stability analysis** on the 100k GPU-hour run: fit the sigmoidal curve at multiple early cutoffs (e.g., 25%, 50%, 75% of the run) and report how the extrapolated final A varies. Complement this with one or two additional extrapolation targets (e.g., predict the 75k point from 50k data) to provide a richer picture of predictive reliability.

3. **Pin the "state-of-the-art" claim more precisely.** Acknowledge that SCALERL and MiniMax reach the same asymptotic A but that SCALERL achieves it with higher compute efficiency (B). Distinguish between ceiling performance and efficiency throughout.

4. **Provide baseline implementation details in the main text** (or at minimum a clear statement that all baselines were run with published defaults without modification, if that is the case), so readers can assess the fairness of the comparison without consulting the appendix.

---

## Score and Decision

### Comparison with calibration anchors

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| kFcP5facrQ (Charting the Frontier) | 4.50 | 1 | Weaker — narrower scope (nanoGPT only), methodologically similar but less ambitious |
| CJJ8VxOWbG (RL Grokking Recipe) | 5.20 | 1 | Weaker — synthetic benchmark contribution, smaller compute scale |
| TPTtWC0pGk (Can LMs Discover Scaling Laws?) | 6.67 | 1 | Comparable — different contribution type (LLM agent + scaling laws), similar quality tier |
| R0JM3BWP7W (Tricks or Traps?) | 6.00 | 2 | Weaker — similar empirical recipe-study approach but at smaller scale (Qwen-3 4B/8B, no predictive scaling framework) |
| SdHmA6BYVJ (On Predictability of RL Dynamics) | 5.50 | 2 | Weaker — focuses on parameter-rank analysis rather than compute scaling, less direct practical recipe output |
| Ym33xJYINV (Pretraining Scaling Laws for Generative Eval) | 6.00 | 2 | Comparable — similar scaling-law methodology but applied to pre-training not RL |
| mfIbSouoaZ (RL for MLE Agents) | 6.50 | 3 | Comparable — different domain (MLE agents), similar quality |
| IaEqjWXd1d (AceReason-Nemotron 1.1) | 6.50 | 3 | Comparable — similar SFT+RL empirical study, similar scale |

**Round-1 bracket:** Between approximately 4.5 and 7.0, with the paper above the weaker anchors (4.5–5.5) and below the strong anchors (7.5+).

**Round-2 narrowing:** Compared to "Tricks or Traps?" (6.00), the paper under review is stronger: larger compute scale (400k vs. ~160 GPU-hours), a novel predictive scaling framework (vs. purely empirical comparison), and demonstration at 100k GPU-hours. Compared to "On Predictability of RL Dynamics" (5.50), this paper has a more practical recipe deliverable but weaker theoretical depth. Compared to "AceReason-Nemotron" (6.50), this paper has a more systematic scaling framework but a narrower task focus. The paper sits comfortably in the 6.0–7.0 range.

**Final score:** 6.5. The paper makes a genuine empirical contribution at unprecedented scale for RL recipe studies and introduces a practically useful predictive scaling framework. However, the absence of any uncertainty quantification and the limited replication for the core predictive claim prevent it from reaching the 7+ tier. The contribution is solidly in the accept (poster) range.

## Score and Decision
MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>