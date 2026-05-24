Now I have all the information needed. Here is the consolidated final review.

---

## Summary

This paper introduces the Locally Connected Echo State Network (LCESN), a recurrent architecture that replaces the conventional fully connected ESN reservoir with a toroidal grid-based local topology (each neuron connects only to its K×K neighborhood) and adds a forced-memory mechanism that gives each neuron a direct shortcut to its own historical activation at a random delay. Four output-weight adaptation strategies (fixed, NLMS, periodic regression, full regression) are evaluated. On nine real-world time series datasets, LCESN variants achieve competitive results — best or second-best on the four longest datasets (ETTm1, ETTm2, Weather, Solar Energy) — and rank second and third overall among compared models.

## Strengths

1. **Local topology provably reduces asymptotic complexity.** The paper shows time and space complexity drops from O((NM)²) to O(NM K²) (Section 3.3), and reports a measured 15× speedup on a consumer GPU for an 80×100 network with a 7×7 kernel. This directly enables substantially larger reservoirs at the same computational cost.

2. **Forced memory is shown to decouple stability from memory capacity.** Figure 7 shows validation error on ETTm1 drops by roughly an order of magnitude when forced memory is enabled (H=100 vs. H=0). Figure 8 shows that increasing the memory horizon keeps the Lyapunov exponent negative (stable regime), providing direct quantitative evidence that the mechanism prevents the network from crossing into chaos while retaining long memory.

3. **Competitive results on real-world datasets.** Table 1 reports that LCESN variants achieve the best or second-best average MSE on four of the nine datasets (ETTm1, ETTm2, Weather, Solar Energy) and rank second and third overall across all models. The paper correctly identifies dataset length as a likely factor — all four successful datasets have >52,000 time points.

4. **Evidence-based reframing of a standard benchmark.** Figure 5 demonstrates that NARMA10 error drops by orders of magnitude as network size surpasses 1,000 neurons, with statistical significance tests (p<0.05) showing kernel size has diminishing returns. The paper's argument that NARMA10 is saturated for large networks is supported by these scaling plots.

5. **Practical feasibility demonstrated on consumer hardware.** Section 5 limits hyperparameter optimization to 2,000 evaluations (fitting within 24 hours on a GTX 2080 Ti), and Section 6.2 reports building the ETTh1 model from scratch took 20 hours total across five runs. This directly supports the stated objective of a model that can be constructed on consumer hardware.

## Weaknesses

### Major

- **Uncontrolled comparison with published SOTA numbers weakens the headline comparative claims.** Table 1 compares LCESN variants against published results from iTransformer, PatchTST, TimesNet, TSMixer, etc. — obtained under different computational budgets, hyperparameter tuning protocols, and hardware environments. The LCESN uses a fixed 40×50 (2000-neuron) reservoir; the SOTA baselines likely use architectures of very different scales and training budgets. The abstract claims LCESN is "even surpassing several state-of-the-art models" on some datasets, but the comparison is not apples-to-apples. The paper acknowledges this tension by stating "rather than aiming for top rankings" (Section 1.1) and noting it "adopted the results of third-party models" (Section 6.4), but the framing remains inconsistent — the modest goal statement and the strong comparative claim in the abstract are in conflict. This does not invalidate the architectural contribution, but it prevents the comparative results from being taken at face value without controlled replication.

### Minor

- **Final test results lack variance estimates.** Table 1 reports only point estimates (averages over four prediction horizons) with no error bars, confidence intervals, or run-to-run variability. ESNs are stochastic (random reservoir, random forced-memory delays), so test performance can vary significantly across random initializations. The paper mentions "fixed random seeds" (line 224) for deterministic single-run replication, but without multiple runs the reader cannot assess whether the reported improvements over baselines are statistically reliable. This is especially relevant for datasets where LCESN underperforms (Exchange, ETTh1, ETTh2), where the gap to SOTA might be within noise.

- **Missing control: forced memory not tested on a fully connected (conventional) ESN.** The ablation study (Section 6.3) compares conventional ESN without forced memory to LCESN with forced memory, but does not test conventional ESN *with* forced memory. This means the observed improvements could be attributed to the combination of local topology + forced memory, but it is not possible to determine whether forced memory alone would also benefit a fully connected reservoir. This is a cleanly isolable experiment that would strengthen the paper's causal claims about the memory mechanism itself.

- **NARMA10 saturation claim lacks external reference points.** Section 6.1 states that "the error on NARMA10 is below an interesting threshold, and it should no longer be used to compare state-of-the-art results in the Echo State Network literature." The paper shows that error drops with network size (Figure 5), but does not cite any published NARMA10 results from the ESN literature to establish what the existing SOTA error is. Without this context, the reader cannot judge whether the achieved error is genuinely "below an interesting threshold" compared to the best published numbers, or merely low in an absolute sense.

### Trivial

- **NLMS justification is present but minimal.** The paper states NLMS was chosen "as a minimalist baseline" (line 136) and acknowledges other methods exist (FORCE, BPDC), but does not discuss why NLMS might be preferable to these alternatives for the specific setting of ESN online adaptation. This is a very minor gap; the paper scopes this out explicitly.

## Nice-to-Haves

- **Systematic efficiency comparison against at least one SOTA model** (e.g., DLinear, TSMixer, or iTransformer) on the same hardware, reporting training time, inference time, and memory. This would directly support the paper's efficiency value proposition. Figure 6 compares LCESN variants only against the conventional ESN, leaving the efficiency comparison to SOTA models unaddressed.

- **Statistical significance test across datasets** (e.g., Friedman + Nemenyi post-hoc) for the rankings in Table 1 would strengthen the claim that LCESN variants rank second and third overall, rather than weighting each dataset equally.

- **Analysis of why LCESN underperforms on short datasets** (ETTh1, ETTh2, Exchange): a diagnostic experiment (e.g., training on a truncated version of a long dataset) could clarify whether the effect is due to data quantity, hyperparameter convergence, or something else.

## Removed Points

These points were raised by reviewers but are removed following the filtering rules:

- **"Open-source library not linked"** — The abstract mentions an open-source library (line 11). Repository links are commonly omitted in double-blind submissions, and the parser may have stripped appendix content. Following the rule that missing appendix content is a parser artifact, this point is removed.
- **"Train/val/test split verification for SOTA baselines"** — The paper explicitly states (line 122): "we have used the same training/validation/testing split and the same data normalization technique (Nie et al., 2023)." The criticism is factually incorrect.
- **"Training time of SOTA models not reported in Figure 6"** — The paper's scope is building on consumer hardware, not comparing training speed to SOTA models. This is scope-creep; the efficiency comparison against the conventional ESN baseline is appropriate for the paper's stated goals.
- **"Joint hyperparameter optimization for adaptation variants"** — The paper acknowledges this design choice (line 140) and notes the adaptation methods still improve performance, demonstrating robustness. The criticism is valid in principle but is explicitly addressed and scoped.
- **"Hyperparameters for SOTA baselines not reported"** — The paper adopts published results from standard benchmarks (Nie et al., 2023; Liu et al., 2024; Chen et al., 2023), which is standard practice in the field. Requiring re-implementation of every baseline under identical conditions is beyond what is expected for a comparison of this scale.
- **"Statistical test for rankings (Friedman + Nemenyi)"** — This is a nice-to-have improvement, not a weakness. It has been moved to Nice-to-Haves.
- **"GPU speedup claim is from a single measurement"** — The paper reports the measurement with specific parameters (80×100 network, 7×7 kernel), which is standard practice for reporting hardware speedups. This is a specific, reproducible result, not a vague claim.

## Novel Insights

None beyond the paper's own contributions. The key insight that emerges from the reviewer discussions is the tension between the paper's modest framing ("not aiming for top rankings") and its comparative evaluation structure, which presents SOTA-comparison results as headline evidence. This tension is real but does not undermine the paper's technical contribution; rather, it points to a mismatch in rhetorical strategy that could be resolved by reframing the comparative results as complementary evidence of practical viability rather as a primary argument for acceptance.

## Suggestions

1. **Add variance information to Table 1**, even if only from multiple runs with the same discovered hyperparameters but different random seeds. For a stochastic model like an ESN, this is essential for interpreting the reported numbers.
2. **Conduct the missing control experiment**: test conventional (fully connected) ESN with forced memory, to isolate whether forced memory's benefit is topology-dependent.
3. **Reconcile the abstract's comparative claims with the paper's modest framing.** Either de-escalate the claim ("LCESN often matches SOTA on long datasets despite far lower computational cost") or provide controlled head-to-head efficiency comparisons to justify the stronger framing.
4. **Provide external context for the NARMA10 claim** by citing published SOTA NARMA10 errors, so readers can evaluate whether the achieved error is genuinely below an "interesting threshold."

## Score and Decision

The paper makes a solid and well-supported architectural contribution (local topology + forced memory for ESNs) with clear internal validation experiments. The main weakness is the uncontrolled nature of the SOTA comparison, which limits the strength of the comparative claims but does not invalidate the core contribution. The paper is clearly written, the method is well-motivated, and the practical feasibility claims are backed by concrete measurements. I recommend acceptance with minor revisions focused on variance reporting, the missing control experiment, and better calibration of comparative claims.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>