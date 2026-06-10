Here is my final synthesized review.

---

## Summary

This paper proposes the Simulation-Heuristics Model (SHM), a dual-process framework for intuitive physics in which people use mental simulation for short-duration predictions and switch to learned heuristics when simulation cost exceeds a threshold. Using a pouring-marble task with 54 conditions, the authors identify a switching boundary around 65° where error patterns shift from overestimation to underestimation, and show that a hybrid model combining a noisy physics simulator (IPE) with a linear heuristic fits human judgments better than either component alone.

## Strengths

- **Quantitative identification of a strategy-switching boundary.** The paper locates a specific threshold (~65° from human error patterns, ~68.2° from the fitted SHM) that separates two distinct error regimes. Prior work provided mainly qualitative evidence for strategy coexistence; this paper goes further by identifying a precise transition point with supporting statistical tests.

- **Systematic four-step hypothesis testing chain.** The paper sequentially tests (1) that error patterns switch, (2) that IPE explains overestimation (r=.890) but fails beyond 65°, (3) that a heuristic model captures underestimation beyond 65° (r=.841), and (4) that SHM combining both outperforms either alone across aggregate metrics (r=.834, RMSE=10.002) and in scenario-level breakdowns.

- **Interpretable heuristic coefficients.** The linear model (Table 1) provides specific, significant coefficients for each physical variable (e.g., V-shaped cups pour 11.528° earlier than H-shaped, full filling subtracts 19.955°; all p=.000), offering mechanistic insight into which features drive heuristic-like judgments.

- **Scenario-level generalization analysis.** SHM's performance is disaggregated by cup shape, object shape, size, and filling height (Section 5.4, Fig. 4), showing the hybrid advantage holds across diverse subpopulations — e.g., improving A-shaped cups from r=.461 (IPE alone) to r=.647, and full-filling from r=.377 (heuristic alone) to r=.673.

- **Well-controlled experimental design.** The 3×3×3×2 factorial design with 54 conditions, within-subjects counter-balancing, familiarization quizzes, and exclusion criteria addresses standard validity threats. Grayscale coloring eliminates material-property priors, and the marked-angle dial reduces perceptual bias.

## Weaknesses

### Major

- **Confound between angle and simulation time undermines the central claim.** The paper argues that simulation cost (time) drives strategy switching, but pouring angle and simulation time are perfectly confounded because tilting speed is held constant (line 133: "as the angular speed remains constant in our experiments, the simulation time is proportional to the degree of angle"). The independent variable that allegedly triggers the switch (simulation time) is monotonically tied to the variable being predicted (pouring angle). Without independently manipulating simulation cost (e.g., varying tilting speed while keeping target angle constant), the data cannot distinguish cost-based strategy switching from angle-dependent bias in a single process. The paper acknowledges this limitation indirectly (line 157: "Instead of relying on actual simulation time in humans, which is unavailable, we instead based the transition criterion in SHM on IPE's simulation time") but does not discuss how this confound affects the main conclusion.

- **Alternative explanations are not addressed.** The observed pattern — overestimate small angles, underestimate large angles — matches what a central tendency (contraction) bias in magnitude estimation would produce, a well-established psychophysical phenomenon. The paper does not discuss or rule out this explanation. Additionally, the IPE model itself shows angle-dependent bias (it has larger errors at larger angles, which the paper reports), so the finding that a second model helps at large angles could simply reflect IPE's intrinsic limitations rather than a human strategy switch.

- **The heuristic model is trained on physics, not human cognition, limiting its interpretive value for cognitive strategy claims.** The linear heuristic (Section 3.2) fits ground-truth physics data, not human judgments. Its correlation with human data (r=.841 beyond 65°) shows shared structure between physics and human responses, but does not demonstrate that humans use this specific linear function as a cognitive strategy. The paper conflates "model that predicts physics" with "model of human reasoning," over-interpreting the heuristic model's success as evidence for a heuristic strategy in humans (e.g., the abstract states it "replicated human prediction" and Section 5.3 frames it as supporting "the adoption of heuristic strategies").

- **Discrepancy between the two boundaries is not explained.** The error-pattern analysis yields a boundary of 65° (Section 5.1), while the SHM grid search yields 68.2° (Section 5.4). This 3.2° discrepancy is not discussed or explained. Since both are derived from the same dataset, their proximity carries less independent corroborative weight than the paper suggests.

### Minor

- **No complexity-adjusted model comparison.** SHM has additional free parameters (at minimum the switching threshold θ, plus potentially different noise parameters in each regime), yet the paper reports raw correlations (IPE: r=.772, SHM: r=.834) without AIC, BIC, cross-validation, or adjusted R². The Δr ≈ 0.06 improvement is modest, and with extra parameters fitted to the same evaluation data, some improvement is expected by chance. The scenario-level breakdowns partially mitigate this concern but do not eliminate it.

- **Collected data left unanalyzed.** Participants' self-reported strategies from the feedback session (line 118) and total response duration (line 113) were recorded but never reported or analyzed. These data could provide convergent evidence for the dual-process claim; their absence is a significant missed opportunity.

- **Individual differences not investigated.** The paper implicitly assumes a uniform switching boundary across all 42 participants. The within-subjects design allows for per-participant analysis of the boundary or strategy consistency (e.g., do some participants show more simulation-like behavior across all conditions?), but this is absent.

- **Boundary optimization criterion is vague.** The 65° boundary is found by searching for what "best distinguishes between the two patterns" (line 129) — the exact objective function (maximizing separation in mean error? minimizing classification error? some other criterion?) is not specified.

### Trivial

None.

## Nice-to-Haves

- Independently manipulate simulation cost (e.g., vary tilting speed while keeping target angle constant) to directly test the cost-based switching account.
- Analyze the already-collected self-report feedback data and per-participant response times.
- Report complexity-adjusted model comparison metrics (AIC, BIC, or cross-validated RMSE).
- Re-fit the heuristic model to human judgments and compare its parameters to the physics-fitted version to assess whether human heuristics differ from physics-based ones.
- Analyze individual differences in the switching boundary.

## Removed Points

These points are flagged to be removed — treat them with caution:

- *Missing RMSE value for IPE* (line 159). This is a parser/formatting artifact; the original submission likely contained the value.
- *Broken SHM equation* (line 76–77, only one branch shown). Parser/formatting artifact.
- *Deterministic physics model results never appear* — The paper states these results appear in fig. 3 (which cannot be viewed from the extracted text). The individual baseline values likely appear in the figure.
- *Related work too brief / missing engagement with specific literature* — Per instructions, missing related works should not be flagged.
- *Section-by-section presentation notes* — Various formatting observations (brief introduction, etc.) are not substantive weaknesses.
- *Claim that IPE's full-dataset correlation is not reported* — It is reported at line 159 (r=.772).

## Novel Insights

Beyond the paper's own contributions, the review process reveals a recurring pattern in cognitive science papers: an interesting empirical regularity (a clean boundary separating two error regimes) that admits multiple competing explanations (dual-process strategy switching, central tendency bias, single-model angle-dependent error), but where the paper commits to the most theoretically ambitious interpretation without adequately ruling out alternatives. The key tension is between the paper's strength as a descriptive/phenomenological account of human judgment patterns and its weakness as a process-level cognitive model. The most impactful follow-up — independently manipulating simulation cost while controlling the predicted quantity — is precisely what would resolve this ambiguity, and the paper's current design cannot distinguish the accounts.

## Suggestions

1. Narrow the central claim: present SHM as a useful phenomenological model that captures aggregate human judgment patterns, rather than claiming it directly reflects cognitive strategy switching. The data support the former more strongly than the latter.
2. Explicitly discuss alternative explanations (central tendency bias, single-process angle-dependent error) in the limitations section.
3. Analyze the collected feedback and response time data to provide convergent evidence for the dual-process account.
4. Report complexity-adjusted model comparison (e.g., cross-validated RMSE or AIC) when comparing IPE, heuristic, and SHM.
5. Report the individual baseline performances (IPE full-data, heuristic full-data, deterministic physics model) from fig. 3 in the main text for completeness.

## Score and Decision

This paper addresses an interesting question with a well-designed experiment and produces a clear, novel empirical pattern. The SHM model fits human data well across diverse conditions. However, the central claim — that the switch in error patterns reflects a strategic shift between two distinct cognitive processes triggered by simulation cost — is not adequately supported by the experimental design, which confounds simulation time with the predicted angle and does not address simpler alternative explanations. The heuristic model is trained on physics rather than human cognition, further weakening the cognitive interpretation. Missing analyses of collected data (feedback, response times, individual differences) represent missed opportunities that could have substantially strengthened the case. At ICLR standards, the gap between the claims and the evidence is too large for acceptance in the current form. The paper would benefit from narrowing its claims and/or conducting the critical follow-up experiment that manipulates simulation cost independently.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>