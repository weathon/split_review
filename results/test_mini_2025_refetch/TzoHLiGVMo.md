Now I have all the information I need. Let me compile the final review.

---

## Summary

This paper introduces ODEFormer, the first transformer-based method for multidimensional symbolic regression of ordinary differential equations from observed (noisy, irregularly sampled) trajectories. It also contributes ODEBench, a curated benchmark of 63 ODE systems spanning 1–4 dimensions that addresses limitations of the existing Strogatz dataset. Across extensive experiments on both benchmarks, ODEFormer demonstrates consistent accuracy advantages over a broad set of baselines (GP methods, SINDy, ProGED, etc.), substantially improved robustness to noise and subsampling, and inference times on the order of seconds versus minutes for competing approaches.

## Strengths

1. **First transformer for multidimensional dynamical SR.** The paper delivers the first architecture capable of inferring symbolic ODE systems in multiple dimensions from a single trajectory, a genuine advance beyond the univariate-only method of Becker et al. (2023). The system handles up to 6 dimensions with a single pretrained model, no per-system retraining, and no need for finite-difference derivative approximations (Section 1, Section 4).

2. **Clear and consistent accuracy advantage on two benchmarks.** On both the Strogatz dataset and the new ODEBench, ODEFormer (especially with optional parameter optimization) achieves the highest average % accuracy (R² > 0.9) across all six noise levels and two subsampling rates. The advantage becomes decisive under noise and subsampling — e.g., at 5% noise + 50% subsampling on ODEBench, ODEFormer remains above ~40% accuracy while most baselines fall below 10% (Figure 4).

3. **ODEBench is a valuable community resource.** The paper identifies serious limitations in the existing Strogatz dataset (7 systems, all 2D, imprecise integration, misleading annotations) and introduces ODEBench: 63 curated ODEs (1D–4D) from real-world models with precise integration, two initial conditions per system for generalization evaluation, and public release (Section 1, Appendix A). This raises the evaluation bar for future work on dynamical SR.

4. **Fast inference without finite-difference derivatives.** ODEFormer performs inference in seconds after one-time pretraining, versus minutes for all baselines except SINDy (Figure 4). It also avoids finite-difference derivative approximations entirely — a key advantage on noisy/irregular data (Section 4).

5. **Generalization evaluation on unobserved initial conditions.** The paper goes beyond reconstruction accuracy by evaluating on trajectories from new initial conditions (Figure 5). This is a more stringent test of whether the inferred ODE actually captures the true dynamics, and is often absent in prior work. ODEFormer's advantage persists under this stricter metric.

## Weaknesses

### Fatal
None.

### Major

1. **Missing per-system failure analysis on ODEBench.** The paper reports only aggregate accuracy across all 63 ODEBench systems. Without a per-system breakdown, it is impossible to assess whether ODEFormer's successes and failures correlate with properties of the ground-truth ODEs. Specifically, ODEFormer's operator vocabulary is limited to {+, ×, sin, 1/x, x²} (lines 95–98). Real-world systems in ODEBench (e.g., from Strogatz (2000) and Wikipedia) likely involve exponentials, cos, logs, and other functions outside this set. If ODEFormer systematically fails on systems requiring these operators while succeeding on those within its vocabulary, the aggregate numbers could overstate its generality. A table or figure showing which ODEs are solved correctly vs. incorrectly — along with the operator coverage of ODEBench — would dramatically sharpen the paper's contribution and guide future work.

2. **No uncertainty quantification on accuracy numbers.** The primary accuracy metric (% of predictions with R² > 0.9) is reported as a single point estimate. With only 28 trajectories on Strogatz and 63 systems on ODEBench, a few case outcomes can swing the percentage substantially. Without bootstrap confidence intervals, error bars, or at least a discussion of variability, it is difficult to assess whether the observed differences between methods (especially on clean data where the gap is smaller) are reliable. The paper should report confidence intervals (e.g., via bootstrapping over systems) or include statistical significance tests.

### Minor

1. **Synthetic test set draws from the same generative distribution as training.** While the paper correctly notes that continuous constants and random initial conditions prevent exact overlap (Section 5, line 158), the test set still comes from the same generative process with the same operator vocabulary. The impressive synthetic results (Figure 3) thus primarily reflect in-distribution performance. The paper's presentation treats both synthetic and ODEBench results as equally informative, but the real evidence for generalization to novel ODE structures comes from ODEBench. The authors should be more explicit that synthetic results are an upper bound on in-distribution capability.

2. **Filtering statistics not reported.** The data generation section mentions discarding 90% of rapidly converging systems (line 109) and filtering out divergent ones (line 108), but does not report the total fraction of generated ODEs that are discarded. Without these statistics, readers cannot assess whether the filtering introduces a significant selection bias — e.g., toward oscillatory or unstable systems — that might affect performance on ODEBench's many stable fixed-point dynamics.

3. **Generalization results use approximate values in the table.** Figure 5 reports generalization accuracy with values like ~55, ~50, etc. (lines 219–231). While the accompanied chart provides a visual summary, the table should report exact percentages for a research paper.

### Trivial
None.

## Nice-to-Haves

- **Ablation of inference-time rescaling.** The rescaling procedure (time to [1,10], normalizing initial conditions to unity) is a crucial preprocessing step (Section 4). An ablation showing performance without it would demonstrate its necessity.
- **Operator set comparison.** The paper could explicitly compare the operators supported by each baseline (e.g., which operators were provided to SINDy and GP methods) versus ODEFormer's vocabulary, to ensure fairness and clarify scope.
- **Statistical significance tests.** A paired permutation test between ODEFormer and the best baseline per condition would help quantify the reliability of observed differences.

## Removed Points

These points were raised by reviewers but are removed here for the reasons stated:

- **"First transformer" claim overstatement** — Removed because the claim is accurately qualified: "first Transformer trained to infer dynamical laws in the form of *multidimensional* ODEs" (line 49). The paper explicitly contrasts with Becker et al. (2023), which handles only univariate ODEs. The qualifier is present and correct.
- **Encoder/decoder asymmetry not ablated** — Removed because the paper cites Charton (2022) for this design choice and notes it was found empirically. This is a standard citation-based justification, not a missing analysis.
- **Generalization results as "rough chart"** — Removed because the table with ~ values may be a parser artifact from an image-based figure; the actual paper likely presents the data precisely. The chart gives the reader a visual overview.
- **Hyperparameter tuning cost for baselines not reported** — Removed because the paper clearly explains that baselines undergo per-equation hyperparameter optimization (Section 5, line 172). Reporting the exact compute time for baseline tuning would add bulk without changing the substantive result.
- **Missing related works** — Removed per protocol, as the reviewer lacks external sources to confirm existence of unmentioned works.
- **Formatting/presentation nitpicks** — Removed per protocol as parser artifacts.
- **Strength Finder's generic strengths** (e.g., "addresses an important problem") — Removed; only concrete, evidence-backed strengths are retained.

## Novel Insights

None beyond the paper's own contributions. The combination of the two reviews does surface a particular subtlety worth noting: ODEFormer's strong aggregate performance could conceal a significant operator-coverage gap. The paper's operator set (+, ×, sin, 1/x, x²) is quite narrow compared to the range of functions found in real-world dynamical systems (exp, cos, log, tanh, etc.). The fact that ODEFormer still achieves high trajectory R² on ODEBench despite this gap suggests either (a) many ODEBench systems happen to use operators within ODEFormer's vocabulary, or (b) approximate symbolic forms using the available operators can produce trajectories with high R² without capturing the true symbolic structure. The paper's drop from reconstruction to generalization accuracy (~50% relative reduction) is consistent with (b). This is a tension the authors should address directly rather than leaving for readers to infer.

## Suggestions

1. **Add a per-system success/failure table for ODEBench.** For each of the 63 systems, indicate whether ODEFormer (and key baselines) achieved R² > 0.9 on reconstruction and generalization. Color-code by operator type to visualize coverage gaps. This single addition would address the most significant evidential weakness.

2. **Report bootstrap confidence intervals for all accuracy numbers.** Even a simple percentile bootstrap over the 63 ODEBench systems (resampling with replacement) would give readers a sense of variability and make comparisons more credible.

3. **Provide exact numerical values for the generalization accuracy table.** Replace approximate values with the actual computed percentages.

4. **Clarify the scope of the synthetic test.** Add a sentence early in Section 5 stating that synthetic results constitute an in-distribution upper bound, and that all claims about generalization to novel ODE structures should be evaluated on ODEBench.

5. **Report data-generation filtering statistics.** State the fraction of generated ODEs discarded at each filtering stage, so readers can assess potential selection bias.

## Score and Decision

**Calibration anchor summary:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| KinFormer (nhrXqy5d5q.md) | 6.00 | R1, R2 | Less general (chemistry-specific), weaker evaluation, comparable task |
| MDLformer (ljAS7cPAU0.md) | 5.67 | R1, R2 | Functional SR, not dynamical; less comprehensive evaluation |
| Invariant Function Learning (TwMLUpPg8G.md) | 5.00 | R1, R2 | ODE-related but rejected; clarity and evaluation weaknesses |
| Hierarchical DSR (Vp2OAxMs2s.md) | 5.75 | R2 | Different approach (RNN-based); moderate split in scores |
| LLM-SR (m2nmp8P5in.md) | 8.00 | R1, R2 | Stronger unanimity and novelty perception; different paradigm (LLM-based) |
| Neural ODE Transformers (XnDyddPcBT.md) | 5.75 | R2 | Architectural analysis, not symbolic regression |
| Abstract Symbols (STUGfUz8ob.md) | 7.60 | R1 | Theoretical analysis, different domain |

**Round 1 bracket:** The paper sits well above weak anchors (~2–3.5) and below the strongest anchors (~8.0). The most comparable paper (KinFormer, avg 6.00) provides a clear lower bound — ODEFormer is more general, more thoroughly evaluated, and better presented.

**Round 2 narrowing:** ODEFormer is clearly stronger than KinFormer (6.00), MDLformer (5.67), and the ODE invariant learning paper (5.00). It is not at the level of LLM-SR (8.00, unanimous all-8 scores with Oral distinction) but the comparison is cross-paradigm. The paper's own merits — a new task formulation, a new benchmark, strong and consistent results, thorough baselines, clear writing — place it comfortably above the 6.0–6.5 range. The main evidential gaps (no per-system analysis, no confidence intervals) prevent it from reaching the 7.5+ tier.

**Final score: 7.0** — a strong paper with clear contributions that should be accepted. The identified weaknesses are addressable in a minor revision and do not undermine the core claims.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>