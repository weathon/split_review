Now I have all the information needed. Let me synthesize the final review.

---

## Summary

This paper introduces the Locally Connected Echo State Network (LCESN), an ESN variant with three modifications: (1) a locally-connected reservoir topology that reduces asymptotic complexity from O((NM)²) to O(NM K²), (2) a forced memory mechanism that gives each neuron a direct lookback connection to a historical state (decoupling memory length from chaotic instability), and (3) optional online weight adaptation strategies (NLMS filtering and periodic regression retraining). The method is evaluated on the NARMA10 benchmark and nine real-world multivariate time series forecasting datasets.

## Strengths

- **Local topology demonstrably reduces complexity without sacrificing accuracy (Section 3.3, Figure 5):** The paper shows that replacing the fully connected reservoir with a local K×K neighborhood lowers asymptotic complexity by orders of magnitude. On NARMA10, LCESN with a 7×7 kernel achieves orders-of-magnitude error reduction as reservoir size grows to 16,000 neurons, and a 19×19 kernel (approaching full connectivity) yields statistically significantly *worse* results on the two largest networks — a clear and non-obvious finding that contradicts the intuition that more connectivity is better. A 15× GPU speedup is measured for an 80×100 network.

- **Forced memory mechanism is well-motivated and empirically validated (Section 3.4, Figures 7–8):** The paper identifies a genuine tension in ESN design (long memory ↔ chaotic instability) and proposes a simple, principled solution: giving each neuron a direct connection to a randomly-timed historical state. Figure 7 shows that disabling forced memory or using short horizons (<50) yields high-variance, poor validation MSE on ETTm1, while H=50–100 consistently produces low MSE. Figure 8 confirms that longer forced memory horizons keep the Lyapunov exponent negative (stable regime) while providing long memory. This directly supports the claim that the mechanism resolves the identified limitation.

- **Competitive empirical results on real-world benchmarks (Table 1):** All four LCESN variants outperform a conventional ESN on every one of the nine datasets. LCESN-LR1 ranks second overall among all compared models (including TSMixer, iTransformer, PatchTST), and LCESN variants place first on the four longest datasets (ETTm1, ETTm2, Weather, Solar Energy). This supports the paper's central thesis that large, well-tuned random networks can be competitive with complex gradient-trained models.

- **Practical consumer-hardware feasibility demonstrated (Section 6.2):** The entire pipeline — including hyperparameter optimization limited to 2,000 evaluations — fits within a 24-hour deadline on an older GTX 2080 Ti. For a 40×50 network, evaluation takes under 40 seconds. Training on ETTh1 completes in ~20 hours total (five runs). This makes the approach accessible to researchers without large-scale compute resources.

- **Systematic comparison of weight adaptation strategies (Section 3.5, Table 1):** The paper compares four variants (LCESN → LCESN-LMS → LCESN-LR100 → LCESN-LR1) and shows that lightweight NLMS filtering improves results over static weights, while periodic retraining every 100 steps (LCESN-LR100) nearly matches the accuracy of per-step retraining (LCESN-LR1) at a fraction of the computational cost. This provides a practical trade-off analysis useful for practitioners.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Missing uncertainty quantification in Table 1:** The main comparison table reports only averages over four prediction horizons (96, 192, 336, 720) without standard deviations, confidence intervals, or significance tests. This makes it impossible to assess whether the observed differences between LCESN and the baselines are statistically reliable. The NARMA10 analysis includes a p-value; the real-world evaluation should as well.

- **No code repository URL in the paper:** The abstract states "we provide a GPU-based implementation as an open-source library," but no URL is given in the paper itself. While the paper mentions fixed random seeds and logs/checkpoints, the absence of a code link or seed values makes exact reproduction unnecessarily difficult for a paper whose contribution is a new method.

- **Forced memory horizon H=100 not tested for sensitivity across datasets (Section 3.4):** The choice H=100 is motivated by the ETTm1 analysis in Figure 7, but the paper then uses this value for all nine datasets without evaluating whether the optimal H differs. A brief sensitivity analysis on 2–3 other datasets (e.g., Weather, Solar Energy) would strengthen the claim that H=100 is a reasonable default.

- **No matched-capacity or controlled lookback-window comparison with feedforward baselines:** The feedforward baselines (PatchTST, iTransformer, etc.) use fixed-length input patches (typically 96–720 time steps), while LCESN uses the entire history up to the prediction point. The paper discusses this asymmetry (Section 3.5) but does not run a controlled experiment (e.g., limiting LCESN's history to the same window) to isolate whether LCESN's advantage comes from longer memory or other properties. This does not invalidate the results, but it leaves the source of the improvement partly uncharacterized.

### Trivial

- **Test vs. validation reporting could be more explicit:** The paper states it uses the same splits as Nie et al. (2023) and selects models on the validation set (lines 122, 183–184). Section 3.5 describes the evaluation on "testing data." This is reasonably clear but could state more explicitly in the caption of Table 1 that numbers are test-set results to eliminate any ambiguity.

- **The shared-kernel observation (line 95) references a stripped appendix:** The paper notes that using a shared convolutional kernel does not work as well, with a superscript reference likely to an appendix. Since appendices are stripped, this claim is unsupported in the main text. The observation is brief enough that a sentence or small figure in the main paper would help.

## Nice-to-Haves

- A controlled experiment where LCESN's input history is limited to a fixed window (e.g., 96 or 336 steps) matching the feedforward baselines would help isolate whether its advantage stems from longer context or from other architectural properties.
- Reporting the search ranges used by CMA-ES for each hyperparameter would aid reproducibility.
- Sensitivity analysis of forced memory horizon H on 2–3 additional datasets would increase confidence in the default value.

## Removed Points

The following points from the reviews are flagged for removal; treat them with caution:

1. **"The paper does not discuss the evaluation protocol asymmetry or attempt to control for it"** — REMOVED: The paper explicitly discusses this asymmetry in Section 3.5 (lines 122–128), describing how recurrent and feedforward evaluation differ and justifying the approach. The reviewer's claim is factually incorrect.

2. **"Cherry-picking stronger baselines"** — REMOVED: The paper states it opts for the *stronger* results from Nie et al. (2023) when both Nie et al. and Liu et al. are available (line 203). Choosing stronger baselines makes the comparison *harder* for LCESN, not easier. The reviewer has this backwards.

3. **"No data is shown for the shared kernel observation (appendix stripped)"** — REMOVED: Per meta-reviewer instructions, missing appendix content is a parser artifact, not an author error. The data exists in the original submission.

4. **"The ESN baseline's full connectivity is not typical ESN configuration"** — REMOVED: Conventional ESNs (Jaeger, 2001) use a fully connected reservoir matrix. The paper correctly compares against this standard configuration.

5. **Criticism that the paper "overpromises" and "claims to have beaten the state of the art"** — PARTIALLY REMOVED (downgraded from Critical Issue to Minor): The paper's actual language ("competitive results, even surpassing several state-of-the-art models," "competitive accuracy... even surpassing them on some of the longest tested datasets") is appropriately tempered and supported by Table 1, where LCESN-LR1 ranks second overall. However, the absence of error bars (kept as a separate Minor weakness) tempers confidence in these claims.

## Novel Insights

The review process surfaces an interesting tension: the harsh critic's strongest complaints (unfair comparison, cherry-picked baselines, undiscussed asymmetry) are all contradicted by direct textual evidence in the paper — the paper explicitly discusses the evaluation asymmetry, selects *stronger* baselines, and uses standard test/validation splits. The genuine weaknesses (missing error bars, no code URL, untested H sensitivity) are real but minor, and none threaten the core claims. The most insightful observation not fully explored in the paper is whether LCESN's advantage on long datasets stems primarily from the forced memory mechanism's ability to access the full history, rather than from architectural superiority per se — a controlled experiment varying the input window length could sharpen this understanding.

## Suggestions

1. Add standard deviations or confidence intervals to Table 1, or at minimum report per-horizon results alongside the averages.
2. Provide the code repository URL in the paper (or, if already posted, add a footnote; otherwise release it).
3. Run a controlled experiment that limits LCESN's input history to the same lookback window as feedforward baselines (e.g., 96/336 steps) on 2–3 datasets to characterize the source of improvement.
4. Report CMA-ES hyperparameter search ranges and final values for each dataset.
5. Add a brief sensitivity analysis of forced memory horizon H on at least one more dataset (e.g., Weather) to support the claim that H=100 is a reasonable default.

## Score and Decision

**Originality:** Good — local topology + forced memory is a novel combination not previously explored in ESN literature.  
**Importance of research question:** Moderate — ESNs are a niche but relevant area; showing they can compete with feedforward models is a notable result.  
**Claims well-supported:** Yes, with minor caveats — the main claims are supported by the evidence presented, though uncertainty quantification is missing.  
**Soundness of experiments:** Sound — the NARMA10 analysis is thorough, the computational benchmarks are concrete, and the real-world comparison, while having standard limitations, is within the norms for this type of paper.  
**Clarity of writing:** Good — the method is clearly described and motivated.  
**Value to the research community:** Moderate — provides a practical ESN variant that can be built on consumer hardware with potentially competitive results.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>