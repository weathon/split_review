- Decision: Accept
- Avg Score: 6.33
- Scores: 6, 5, 8
Now I have all the information needed. Let me write the consolidated review.

## Summary

The paper proposes Dec-ODE, a framework for Marked Temporal Point Processes (MTPP) that decouples the influence of individual events and models each event's continuous dynamics using Neural ODEs. In the linear variant evaluated, these independent influence trajectories are aggregated via summation to predict the ground intensity and mark distribution. The framework enables parallel computation of event influences and provides interpretability by exposing how each event contributes over time.

## Strengths

- **Parallel training yields substantial speedup**: Table 2 (Section 5.3) demonstrates 2–5× per-iteration speedup for the parallel scheme over sequential propagation (e.g., Reddit: 15.5s vs 78.7s; ratio 0.20), directly validating a key claimed advantage of decoupling.
- **Interpretability via decomposed influence functions**: The decoupled framework naturally produces per-event influence trajectories. The qualitative analysis on Retweet data (Figure 5) reveals plausible patterns (e.g., slower decay for high-follower posts, same-type self-influence) that align with domain intuition. This is a genuine strength of the approach even though it is not quantitatively validated.
- **Unified ODE integration for multiple quantities**: Equation (8) formulates a multi-dimensional ODE system that simultaneously computes hidden states, the compensator, cumulative distribution, and expected time in a single forward pass, eliminating the need for separate numerical integration or sampling steps required by prior methods.

## Weaknesses

### Fatal
None.

### Major
- **SOTA claim is overstated given the evidence**: The paper's contribution list asserts "state-of-the-art performance" (line 63), but Dec-ODE never achieves the best NLL on any of the five datasets — IFL outperforms it on MOOC and MIMIC-II, ANHP on Reddit, Retweet, and Stack Overflow — sometimes by substantial margins (e.g., MOOC NLL: IFL −2.895 vs Dec-ODE −2.289). While Dec-ODE does well on RMSE (best on 4/5 datasets) and ACC (best or second-best on all 5), several of these RMSE margins overlap within one standard deviation (e.g., MOOC: 0.467±0.012 vs ANHP 0.470±0.019; Stack Overflow: 1.018±0.011 vs RMTPP 1.017±0.011). No statistical significance tests are reported. The blanket SOTA claim is not supported across all metrics, and the paper would benefit from qualifying which aspects (prediction accuracy, efficiency, interpretability) it improves.

- **No comparison with ODE-based TPP methods**: The related work cites NJSDE and STPP — methods also using Neural ODEs/differential equations for TPP — but the experimental comparison (Section 6.1) includes only THP, IFL, and ANHP, none of which use ODEs. The paper neither includes these directly comparable methods nor explains why they are excluded (e.g., different task scope, missing code). This omission weakens the empirical case for the decoupling contribution relative to the most relevant competitors.

### Minor
- **THP evaluation is broken on two datasets without sufficient caveats**: The paper reports that THP's thinning algorithm failed on Reddit (RMSE 6.151) and MIMIC-II (RMSE >10), yet includes these results in the main table. While the issue is mentioned (Section 6.2, line 462), the inclusion of demonstrably broken results inflates Dec-ODE's relative RMSE standing. These entries should either be excluded or accompanied by stronger discussion of how their exclusion changes the comparison.

- **Interpretability claims are purely qualitative**: The explainability analysis (Section 6.3, Figure 5) provides interesting qualitative observations but no quantitative evaluation (e.g., alignment with human judgments, consistency checks). The conclusion claims "significant potential for applications such as out-of-distribution detection and survival analysis" (line 557) — this is not supported by the evidence presented.

- **Missing ablation and analysis**: (a) No ablation of ODE solver type or hidden state dimension, which can substantially affect accuracy and speed. (b) No discussion of how variable-length ODE integration ranges interact with minibatching — events with vastly different durations require different integration intervals. (c) The standard deviation for Dec-ODE's MOOC NLL is 0.191, roughly 5–6× larger than baselines (e.g., IFL: 0.031, ANHP: 0.043), suggesting instability or high variance across runs, but this is not addressed.

### Trivial
- **The parallel computing comparison (Table 2) is a self-comparison** between parallel and sequential propagation within Dec-ODE, not a comparison against other ODE-based TPP methods. The paper frames it as validating the optimization scheme, which is fine, but this could be stated more clearly to avoid potential misinterpretation.

## Nice-to-Haves

- **Statistical significance tests** (e.g., paired bootstrap or permutation tests) for the RMSE and ACC improvements would help establish which differences are meaningful.
- **Inference latency** should be measured and reported, as the paper focuses on training efficiency but does not assess whether parallelization benefits inference as well.
- **A comparison of the linear version with a more complex aggregation** (e.g., Transformer-based Φ_λ, Φ_k) would clarify whether the linear choice is a limiting factor or a negligible simplification. The paper correctly notes that the framework supports richer aggregation (line 260), but does not explore this.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The ODE solver must integrate coupled equations; the paper does not discuss solver accuracy/stiffness"** (from Harsh Critic's Section 3.2 notes). This is a misunderstanding. Equation (8) defines a standard coupled ODE system where all derivatives are explicit functions of the current state; ODE solvers handle this routinely. The complaint describes standard practice as if it were a special concern.
- **"The linear aggregation contradicts the motivation of flexible modeling"** (Harsh Critic's Section 4 notes). The paper explicitly states (line 260) that the combining functions can range from simple summation to complex neural networks (e.g., Transformers). The linear version is a deliberate instantiation for efficiency and interpretability, not a limitation of the framework.
- **"State-of-the-art predictive performance"** (from Strength Finder #1). This conflicts with the verified weakness about overstated SOTA claims. The paper's results are competitive on RMSE and ACC but not on NLL, and the blanket SOTA claim is unsupported.

## Novel Insights

The harsh critic correctly identifies a core tension in the paper: the decoupling framework — which is the genuine novelty — is best demonstrated through the parallel efficiency and interpretability results, yet the paper foregrounds SOTA performance which is not uniformly achieved. The strength finder highlights that the parallel speedup (2–5×) is a genuinely measurable advantage that does not depend on SOTA claims, making it the cleanest evidence for the contribution. A useful reframing would be to position the method as offering a favorable trade-off (competitive prediction with added efficiency and interpretability) rather than blanket superiority.

## Suggestions

1. **Reposition the contribution away from blanket SOTA claims.** Emphasize the favorable trade-off: competitive predictive accuracy with the added benefits of parallel computation (2–5× training speedup) and interpretable influence trajectories. Qualify which metrics Dec-ODE excels at (RMSE, ACC) and where it trails (NLL).

2. **Add statistical significance tests** (paired bootstrap or permutation) for the key RMSE and ACC improvements over the strongest baselines. This is standard practice and would substantially strengthen the empirical claims.

3. **Compare against at least one ODE-based TPP method** (NJSDE or a simplified Neural ODE baseline without decoupling) to isolate the contribution of decoupling itself. If this is not feasible (e.g., different problem scope), state the reasons explicitly.

4. **Address the THP evaluation issue** by either excluding the broken entries from the main table (with a footnote) or reporting an alternative metric that does not depend on sampling for those datasets.

5. **Provide a computational budget for the high-variance result** (MOOC NLL std = 0.191): report results from multiple random seeds and discuss whether this reflects sensitivity to initialization, sequence length, or other factors.
