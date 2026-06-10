Now I will write the final consolidated review.

## Summary

GROKFAST proposes a simple method to accelerate the grokking phenomenon (delayed generalization after overfitting) by treating gradients as discrete-time signals and amplifying their low-frequency components via EMA or moving-average filters. The method adds only a few lines of code to existing optimizers and reports up to 50× iteration savings on the modular arithmetic task where grokking was originally discovered.

## Strengths

- **Novel conceptual bridge between optimizer momentum and classical signal-processing low-pass filters.** The paper insightfully identifies that momentum in gradient-based optimizers can be interpreted as a size-1 low-pass filter (Section 4.1, lines 212–214), then generalizes this to non-trivial window sizes via the moving-average filter. This reframing connects optimization to signal-processing theory in a way that is genuinely distinct from prior grokking work focused on double descent, mechanistic interpretability, or loss landscapes.

- **Clean ablation confirming that both fast and slow gradient components are necessary.** Section 5, Q1 (Figure 9) directly tests whether the slow (filtered) component alone suffices and shows it leads to "much slower and unstable training," while the additive design (original gradient + amplified slow component) succeeds. This rules out a trivial alternative explanation and supports the design choice.

- **PCA-based parameter-space trajectory analysis gives unusual insight into how GROKFAST alters dynamics.** Section 5.1 (Table 2, Figure 12) projects the 423k-parameter model onto principal components, showing that GROKFAST reduces the distance from initialization to the final state by 16× relative to baseline and yields hundredfold smaller variance across runs. This quantitative evidence of altered optimization topology is rare in grokking papers.

- **Demonstrated generalization across four architectures and tasks.** The method is validated on Transformers (modular arithmetic), MLPs (MNIST), graph convolutional networks (QM9), and LSTMs (IMDb), showing the approach is not architecture-specific.

## Weaknesses

### Major

1. **No comparison against a carefully tuned momentum baseline, despite the paper's own framing.** The paper states that "momentum can be seen as a low-pass filter with window of size-1" (line 214) and that "the similarity between GROKFAST-EMA and momentum hyperparameters . . . implies an alternative interpretation of momenta" (line 214). Given this explicit conceptual connection, it is essential to compare GROKFAST against a baseline where the optimizer's momentum hyperparameter is grid-searched for grokking speed (e.g., SGD+momentum with β ∈ [0.8, 0.999]). The paper's baseline optimizer is never even named (it is simply called "baseline" throughout), making it impossible to determine whether GROKFAST's benefit comes from its novel signal-processing framing or from doing — more aggressively — what momentum already does. Without this comparison, the empirical contribution relative to existing optimization practice is ambiguous.

2. **Missing acceleration factors for 2 of 4 tasks, making the cross-task claims incomplete.** The paper reports acceleration factors for modular arithmetic (×50.49) and MNIST (×22.0), but provides no acceleration factor for QM9 (only qualitative "validation loss drops faster," Section 3.3, line 190) or IMDb (only "faster generalization" qualitatively, Section 3.4, line 206). Since the paper's central claim is quantitative acceleration of grokking, the omission of these numbers for half the evaluated tasks weakens the empirical picture.

3. **Single-run results without variance estimates for most main findings.** Grokking is known to be sensitive to random seeds (Power et al., 2022). The main results (Figures 4, 5, 6, 7, 8) appear to be single runs without reported variance. While the PCA analysis in Section 5.1 reports statistics over 5 instances, the core speedup claims lack error bars. This is a significant reliability concern for a paper making precise quantitative claims (e.g., "×50.49").

### Minor

4. **The headline "×50 faster grokking" overstates the representative result.** The ×50.49 figure is achieved on a single task (modular multiplication) with a specific hyperparameter combination (λ=5, w=100, wd=0.01) using the MA variant that incurs 2.4× per-iteration overhead, reducing wall-clock speedup to ×20.5 (line 336). The abstract and introduction feature "×50" prominently without caveats about the overhead or the fact that other tasks show substantially smaller gains (×22 on MNIST) or lack quantified factors. This is a presentation issue that should be corrected.

5. **The paper identifies a framing tension it does not resolve.** Section 5.1 shows that GROKFAST converges to a solution 16× nearer to initialization than the baseline and states "we cannot simply say that the states C of baseline and of GROKFAST belong to the same network state" (line 327). The paper then concludes that GROKFAST "provide[s] supervision towards an alternative optimum." This is transparent, but the paper still frames its contribution as "accelerating grokking" throughout, rather than acknowledging that it may be finding a qualitatively different (nearer, faster) solution that bypasses the characteristic delayed-generalization dynamics. This tension should be addressed directly.

### Trivial

- None.

## Nice-to-Haves

- Compare GROKFAST against a baseline with larger effective batch sizes, since Section 5 (Q1) acknowledges that the MA slow component alone is "equivalent to using larger, overlapping minibatches." An explicit larger-batch baseline would isolate whether the benefit is from low-pass filtering per se or from effective variance reduction.
- Report the baseline optimizer explicitly throughout (currently it is unnamed).
- Consider reframing the contribution as "Low-pass gradient filtering as a technique that shortcuts the grokking phase by steering the model toward a more accessible solution" to align the claim with the evidence.

## Removed Points

These points were considered but removed with justification:

- **"The paper does not establish that it accelerates grokking—it may instead converge to a different solution" (fatal framing).** The paper is transparent about the parameter-space differences (Section 5.1) and acknowledges the solutions are distinct. While this creates a framing tension, it does not invalidate the practical result — GROKFAST achieves high validation accuracy faster, which is the stated practitioner goal (line 15). Demoted to Minor weakness #5 above.
- **"MNIST accuracy is far from SOTA (89.8% vs ~99.7%)."** The model is deliberately undertrained to exhibit grokking, following the Omnigrok (Liu et al., 2022b) setup. This criticism misunderstands the experimental design.
- **"The momentum/low-pass filter characterization is imprecise (IIR vs FIR)."** The paper's claim that momentum is a "low-pass filter with size-1 windows" is a reasonable conceptual description for the intended audience. The mathematical treatment of the filters (Equations 5–8) is correct.
- **"Missing statistical rigor" was partially kept** as Major weakness #3 but the critic's broader complaint about all results being single-run was specific enough to keep.
- **"Two-stage experiment undermines the central claim."** This is essentially a restatement of the parameter-space tension (point #5 above). Merged.
- **"Figure 2 inference of two timescales from loss curves is an over-interpretation."** The paper presents this as its hypothesis (line 17: "suggests that"), not as proven fact. A paper is allowed to state its motivating hypothesis.
- All formatting/style/typo complaints (parser artifacts).

## Novel Insights

None beyond the paper's own contributions. The reviews recapitulate the paper's findings rather than adding novel analytical perspectives.

## Suggestions

1. Add a controlled experiment comparing GROKFAST against SGD+momentum with the momentum parameter grid-searched over β ∈ [0.8, 0.999], using the same base learning rate and schedule. This would directly address the most important missing baseline.
2. Report acceleration factors (iterations to threshold) with error bars over ≥5 random seeds for every task.
3. Report wall-clock speedup alongside iteration-count speedup for all tasks, not just the MA variant.
4. Clearly state the baseline optimizer (SGD? Adam? Which hyperparameters?) in every experiment.
5. In the abstract and introduction, caveat the ×50 claim with (a) the task it applies to, (b) the wall-clock factor after overhead, and (c) the range of speedups observed across tasks.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>