Now I have all the information I need. Let me compile the final review.

## Summary

The paper proposes STBP, a framework for continual spatio-temporal forecasting that combines a frozen general backbone (frequency-domain network + linear graph attention) with an expandable contextual pattern bank. The core idea—isolating stable representations in a backbone while routing adaptation through node-level pattern parameters—is well-motivated, and the empirical results on large-scale traffic benchmarks (21 % MAE improvement over strong CSTF baselines on PEMS-Stream and CA-Stream) are genuinely strong. The ablation study is informative and generally supports the architectural choices.

## Strengths

1. **State-of-the-art forecasting accuracy on traffic benchmarks, convincingly validated.** Table 1 shows that STBP outperforms all nine baselines on every metric (MAE, RMSE, MAPE) at every horizon on PEMS-Stream and CA-Stream, with average MAE reductions of 21.44 % and 21.93 % over the best CSTF competitor (EAC). The magnitudes are large enough that confidence intervals are non-overlapping.

2. **Strong few-shot forecasting capability (10 % data).** Table 2 shows that STBP outperforms the best continual-learning baseline (EAC) by 15.8 % MAE on PEMS-Stream and 18.3 % on CA-Stream when only 10 % of training labels are available for new nodes. This directly validates the claim that the frozen backbone + pattern bank design leverages accumulated historical knowledge.

3. **Well-designed ablation and efficiency study.** Figure 4 systematically ablates the pattern bank (Retrain, Online variants), the backbone (w/o Backbone), and the DLGA module (w/o DLGA), with each removal causing a clear and substantial performance drop. Figure 8 confirms linear memory scaling in node count (STBP O(N) vs. STBP O(N²)) and competitive training time against prompt-based rivals like EAC.

4. **Qualitative evidence for pattern bank behavior.** The t-SNE visualizations in Figures 3 and 6 show that the pattern bank automatically learns meaningful node clusters (reflecting heterogeneity) that persist and extend when new nodes appear, providing interpretable evidence that the bank captures distinct spatio-temporal patterns.

## Weaknesses

### Major

None.

### Minor

1. **Missing standard continual-learning evaluation metrics.** The paper reports only the aggregate average MAE/RMSE across all incremental periods. This single measure cannot distinguish between *better adaptation to new data* and *genuine retention of old knowledge*—the very distinction on which the paper's central claim of mitigating catastrophic forgetting rests. The continual-learning community standardly reports per-task accuracy after the final stage and average forgetting. While the paper's frozen-backbone design definitionally prevents forgetting of old parameter sets, empirical evidence (e.g., performance on old nodes at the end of each period) would directly and powerfully validate the claim. The paper would be strengthened by adding a table showing per-period breakdown.

2. **Imprecise description of the Dual-Stream Linear Graph Attention mechanism.** Section 4.3 states the method uses a "random feature mapping‑based linear attention mechanism (Katharopoulos et al., 2020), with Softmax used for approximation in our implementation." This conflates two different attention families: Katharopoulos et al. uses a *deterministic* feature map φ(x)=elu(x)+1 (not random features) and does *not* approximate softmax, while random‑feature softmax approximation (Performer) requires a normalizer D⁻¹ that is absent from Equation (9). The equation itself follows the linear‑attention form consistently, so the mechanism is still implementable, but the verbal description is technically imprecise and the reference to Appendix A.3.1 is inaccessible in the extracted version. The authors should clarify which feature map φ is used and whether any normalization is applied.

3. **Unexplained domain gap between traffic and air quality.** The improvement over the best CSTF baseline drops from ~21 % MAE on traffic datasets to 2.35 % on AIR-Stream, where RMSE confidence intervals of STBP and EAC substantially overlap. The paper frames the backbone as "general" but offers no analysis of why the gain is dramatically smaller on air quality. Possible factors (sampling frequency, signal propagation vs. advection dynamics, number of incremental periods, graph expansion pattern) are not discussed. This gap does not invalidate the traffic results, but the paper's scope claims would benefit from an honest discussion of domain sensitivity.

4. **Missing ablation of the three pattern‑bank parameter groups (P^(0), P^(1), P^(2)).** Section 4.2 introduces three distinct parameter groups that interact with the backbone via residual scaling, post‑activation gating, and cross‑attention keys. The paper provides no ablation isolating the contribution of each group. For a design presented as central to the method, this is a notable evidentiary gap.

### Trivial

- The description of the baseline evaluation protocol in Section 5.1 is clear but could be more explicit about why different protocols (retrain vs. online) are used for different conventional STGNN baselines.

## Nice-to-Haves

- Report standard CL metrics (final average accuracy, average forgetting) to directly substantiate the catastrophic forgetting claim.
- Ablate the three pattern‑bank parameter groups individually.
- Add a brief analysis or discussion of why the method's gains vary so much between traffic and air quality domains.

## Removed Points

These points were raised by reviewers but are removed after verification against the paper:

1. **"Unfair baseline evaluation (asymmetric protocol inflates gains)."** The critic claimed that retrain (used for GWNet/STID) underperforms online fine-tuning (used for iTransformer), and that this asymmetry inflates STBP's margins. **Verification:** Figure 4 shows the opposite — on all three datasets, Retrain (MAE ≈ 20/22/32 on PEMS/CA/AIR) **outperforms** Online (MAE ≈ 22/24/34). The protocol asymmetry thus favors the baselines, not STBP. The critic also claimed GWNet's adaptive adjacency matrices are "equally scenario‑agnostic" as iTransformer — a judgment call that does not change the empirical fact that retrain performs better in the controlled ablation. **Removed: factual error.**

2. **"Code release not stated."** Per the hard rules, concern about code/artifact availability is removed. The paper does not need to commit to code release for the review to be evaluable.

3. **"Formal significance tests for AIR‑Stream RMSE."** Requesting statistical significance tests beyond reported confidence intervals is reasonable but falls under a nice-to-have, not a weakness, given that confidence intervals are provided.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation that the DLGA description conflates two attention families (Katharopoulos deterministic linear attention vs. random‑feature softmax approximation) is a genuinely useful technical catch that went unnoticed in the strength finder, but it's an error in presentation, not a novel insight about the method itself.

## Suggestions

1. Clarify the DLGA attention mechanism: state explicitly which feature map φ is used (elu+1? random features? another?), whether normalization is applied to the linear attention output, and whether the "softmax approximation" language refers to a different variant in Appendix A.3.1.

2. Add a table of per‑period forecasting performance (MAE on all previously seen nodes at the end of each period) to empirically verify the forgetting‑mitigation claim.

3. Add a brief discussion of the performance gap between traffic and air quality datasets, explaining plausible reasons (e.g., sampling frequency, signal characteristics, graph expansion patterns).

4. Consider adding an ablation that isolates the three pattern‑bank parameter groups (P^(0), P^(1), P^(2)).

## Score and Decision

**Anchor calibration summary**

| Anchor | Avg Score | Source | Comparison |
|--------|-----------|--------|------------|
| `FRzCIlkM7I` (EAC) | 6.75 | round1-mid / round2 | Closely related prompt‑based CSTF method. STBP achieves much larger gains over EAC than EAC achieved over its baselines, but has more technical imprecision. Slightly weaker than EAC's best version. |
| `vJGKYWC8j8` (TFMoE) | 4.00 | round1-mid | Only one dataset, limited analysis. STBP is substantially stronger. |
| `5IvTw0qMKj` (C²INet) | 4.67 | round1-mid | Trajectory prediction, not directly comparable but same score band. STBP is stronger empirically. |
| `N0nTk5BSvO` (TESTAM) | 5.75 | round2 | Traffic MoE with small gains over baselines. STBP has larger gains and better analysis. STBP > TESTAM. |
| `akKNGGWegr` (STGKD) | 5.25 | round2 | KD for ST, missing baselines. STBP is stronger. |
| `kVlfYvIqaK` (DyGPrompt) | 6.00 | round3 | Prompt learning on dynamic graphs, accepted. Comparable quality to STBP. |
| `V6uxd8MEqw` (MISA) | 6.50 | round3 | GCL prompt method, accepted. Comparable quality. |
| `rjuZyMfLSd` (Learn sys dyn) | 6.25 | round3 | CL for system dynamics, accepted. Comparable quality. |

**Round‑1 bracket:** [5.0, 7.0]. The low‑band failures (scores ≤ 3.5) were papers with fundamentally flawed evaluations, single‑dataset studies, or missing proper baselines. STBP shares none of these failures. The high‑band papers (≥ 7.5) are exceptional contributions with flawless execution; STBP's technical imprecision and missing analyses prevent it from reaching that tier.

**Round‑2 narrowing:** Inside [5.0, 7.0], STBP clearly outperforms TESTAM (5.75) and STGKD (5.25) on empirical strength. It is comparable to EAC (6.75) in methodology but slightly weaker in presentation precision. DyGPrompt (6.00) and "Learning system dynamics without forgetting" (6.25) are fair comparators.

**Final score:** 6.0 — a solid paper with strong empirical contributions and well-supported core claims, held back from a higher score by technical imprecision in the DLGA description and the absence of standard CL evaluation metrics that would directly substantiate its main claim.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>