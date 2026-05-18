Now I have a thorough understanding of the paper and can verify each of the reviewer's claims. Let me write the final consolidated review.

## Summary

This paper introduces MoSH, a framework for multi-objective optimization (MOO) that lets decision-makers specify preferences via piecewise-linear *soft-hard functions* (HSFs), encoding both strict hard bounds (below which utility is -∞) and soft desirable bounds (above which diminishing returns set in). The method proceeds in two steps: (1) MoSH-Dense densely samples the Pareto frontier using Bayesian optimization with random scalarizations over HSF-transformed objectives, with an asymptotic convergence guarantee for the expected Bayes SHF utility ratio; (2) MoSH-Sparse sparsifies the resulting set using the SATURATE algorithm for robust submodular optimization, with a near-optimality guarantee relative to the dense set. Experiments span synthetic functions, engineering design, LLM personalization, deep learning model selection, and a real cervical cancer brachytherapy case.

## Strengths

1. **Novel soft-hard preference encoding for MOO.** The SHF formulation (Section 2.2, Eq. 1) is a natural way to encode the ubiquitous practitioner intuition that each objective has both a "must reach" level and a "nice to exceed" level, with diminishing returns beyond the latter. This fills a genuine gap in existing MOO frameworks that lack such multi-level preference encoding.

2. **Theoretically grounded sparsification via robust submodular optimization.** Lemma 1 proves the HSF utility ratio is submodular, allowing SATURATE (Algorithm 2) to produce a compact set C from the dense set D with a near-optimal worst-case utility guarantee (Theorem 2, from Krause et al. 2008). This gives formal teeth to the sparsification step, which is often handled heuristically in prior work.

3. **Empirical validation across diverse, high-stakes domains.** The paper evaluates MoSH on five distinct problems (Branin-Currin, four-bar truss, LLM personalization, brachytherapy, neural network selection). The brachytherapy result — over 3% greater HSF-defined utility than the next best approach, with >99% of maximum utility reached within 5 validated points — demonstrates tangible practical value in a clinical setting where the stakes are high and DM time is expensive.

4. **New evaluation metrics for bounded-region coverage.** The four soft-hard metrics (fill distance, positive samples ratio, hypervolume, distance-weighted score) are sensible operationalizations of diversity and faithfulness within the soft and hard regions, and fill a gap in evaluation methodology for this setting.

## Weaknesses

### Fatal
None. The paper's core claims are supported and no errors invalidate the main contribution.

### Major

1. **Misalignment between the two steps' objectives is unaddressed.** Step 1 (Eq. 4, line 122) optimizes the *expected* HSF utility ratio under a prior over λ. Step 2 (Eq. 5, line 196) optimizes the *worst-case* (minimax) utility ratio over λ. These are fundamentally different criteria. The paper acknowledges the modification from minimax to Bayesian expected value (lines 119–123) but provides no argument that the expected-utility optimum D is suitable for worst-case sparsification. The SATURATE guarantee in Step 2 is relative to the fixed D from Step 1 — if D has poor coverage under some λ, the guarantee is of limited value. Without addressing this gap, the connection between the two steps remains a logical bridge the paper does not cross. The paper should either (a) align Step 1 with the minimax objective (e.g., via adversarial or uniform λ sampling), or (b) provide a uniform-convergence-style argument that a dense expected-optimal set also supports near-optimal worst-case sparsification.

2. **Step 1 experiments compare MoSH (which uses SHF information inside acquisition) against baselines that do not use the SHF, biasing the comparison.** MoSH-Dense optimizes an acquisition function built on the SHF-transformed objectives, while the baselines (EHVI, ParEGO, MOBO-RS, random) operate on raw objectives. The metrics (fill distance, positive samples ratio, hypervolume, distance-weighted score) all directly measure coverage of the soft/hard regions — i.e., exactly what MoSH-Dense's acquisition is designed to achieve. This creates a circular validation: the method that explicitly optimizes for SHF-region coverage does better on metrics that measure SHF-region coverage. To isolate whether the SHF framework itself is beneficial, the paper should compare against baselines that also *incorporate the SHF bounds in some reasonable way* — for instance, using the SHF to set reference points for a Chebyshev scalarization in MOBO-RS, or using a constrained BO approach with the hard bounds. Without such controls, the experiments do not show that MoSH-Dense is the best *method for SHF-bounded MOO*; they only show it is better than methods that ignore the bound information entirely.

### Minor

3. **Lack of sensitivity analysis and reporting for key SHF hyperparameters.** The SHF definition (Eq. 1) involves β ∈ [0,1] (fraction of slope retained in the soft-to-saturation region) and ζ (controlling the saturation point α_τ, set to 2.0). Neither β values used in experiments nor sensitivity to these parameters are reported. The choice ζ=2 is stated without justification. Practitioners would benefit from guidance on setting these knobs.

4. **Single clinical case limits generalizability of the brachytherapy result.** The brachytherapy study (Section 5.5) uses one patient case. While realistic, a single anatomy limits confidence that the claimed 3% utility improvement and >99% coverage within 5 points would generalize across patient anatomies and tumor geometries.

5. **LLM personalization experiment lacks details on objective measurement.** The paper describes how proxy tuning works (line 315) but does not specify how "conciseness" and "informativeness" are measured — are these automated metrics (e.g., length, perplexity, ROUGE) or human judgments? Are the objective functions cheap or expensive to evaluate? How do the soft/hard bounds translate to these metrics? This omission makes it impossible to interpret the experimental results for this application.

6. **Missing statistical significance.** Metrics are reported as mean ± std over 6 runs but no significance tests are performed. Given small sample sizes, the visual advantages of MoSH-Dense in some settings could be within noise.

7. **Theorem 1's practical relevance is limited.** Theorem 1 (lines 149–155) provides an asymptotic bound — the expected Bayes SHF utility ratio converges to 1 as T→∞. The proof follows Paria et al. (2020) but the adaptation to SHF-transformed objectives requires checking that the utility ratio denominator is well-behaved; this is not elaborated. Given experimental budgets of tens to hundreds of evaluations, an asymptotic guarantee is of limited practical import. A finite-sample bound would be far more informative.

### Trivial

8. **The SHF piecewise definition (Eq. 1) is somewhat baroque.** The normalization uses a 0.5 factor and the piecewise expressions use scaling by 2×, making the formulation harder to parse than a simpler alternative (e.g., linear from 0 at α_H to 1 at α_S, then linear with slope β to a plateau). The ζ=2 for the saturation point is stated without motivation.

## Nice-to-Haves

- An ablation replacing the piecewise linear SHF with a simpler functional form (e.g., linear + saturating) to show the precise piecewise definition is not critical to the framework's success.
- A controlled experiment on the Branin-Currin synthetic where baselines are also given SHF bound information (e.g., via constrained BO or reference-point scalarizations) to isolate the value of the SHF encoding itself.
- A discussion relating the SHF framework explicitly to reference-point methods (Wierzbicki), aspiration/reservation levels, and goal programming, with a concrete example showing where SHF solutions differ from these existing approaches.
- A finite-sample bound or convergence rate for Theorem 1 that is meaningful at realistic evaluation budgets.

## Removed Points

*Criticism that the SHF framework's novelty relative to reference-point methods is overstated* — The paper acknowledges this literature (Section 6: MOO Feedback Mechanisms) and claims the distinction is its "multiple levels of preferences without needing to specify exact numerical values." While the SHF shares elements with aspiration/reservation methods, the contribution is in the full pipeline (SHF + random scalarization BO + SATURATE sparsification), not the utility function alone. The critic's demand for a detailed comparison showing where the solutions differ would improve the paper but does not constitute a correctable weakness in the current submission. The paper's claims are scoped to the framework level and do not claim a fundamentally new scalarization theory.

*Criticism about the denominator max_{x∈X} being impossible to compute* — The paper addresses this for evaluation (line 285: denominator computed using offline precomputed D). For the algorithm itself, this approximation is standard practice in BO and not specific to this work.

## Novel Insights

The most interesting point the reviews surface is the fundamental tension in the two-step pipeline: Step 1 optimizes *expected* utility while Step 2 optimizes *worst-case* utility. This tension is actually revealing about the nature of the problem the paper is trying to solve. If the DM truly has hidden λ*, the minimax formulation of Eq. 3 is the right objective. The paper's retreat to expectation in Step 1 (Eq. 4) is a computational convenience — but the key insight is that in practice, D from Step 1 will be *dense enough* that the worst-case sparsification over D will approximate the true minimax optimum over X, because density implies coverage. The paper does not make this argument, but it is the natural defense of the pipeline and is likely correct in the large-budget regime. Making this explicit would strengthen the paper considerably.

## Suggestions

1. **Acknowledge and address the Step 1/Step 2 objective gap explicitly.** Either align Step 1 with the minimax objective (e.g., by sampling λ adversarially or uniformly rather than from a prior), or provide a density argument that a sufficiently dense D from expected-utility optimization will support near-optimal worst-case sparsification.

2. **Run at least one controlled experiment where baselines are also given SHF bound information.** For example, use the SHF bounds to set reference points for MOBO-RS with Chebyshev scalarization, or add the hard bound as a constraint in a constrained BO baseline. This would demonstrate that the specific combination MoSH uses (random scalarization + SHF + UCB) adds value beyond simply giving the bound information to existing methods.

3. **Report β values used and add a sensitivity analysis** for both β and ζ to guide practitioners.

4. **Add statistical significance testing** (e.g., Mann-Whitney U or bootstrap tests) for the main comparisons, or at minimum add per-run scatter plots to the bar charts so readers can assess variability.

5. **Clarify the LLM experiment setup** — specify how conciseness and informativeness are measured, the cost model for evaluation, and the soft/hard bound values used.

## Score and Decision

The paper addresses a practically important problem with a well-motivated framework and provides theoretical grounding for its sparsification step. The diverse experimental validation, including a real clinical case, is a genuine strength. However, the two major weaknesses — the unaddressed misalignment between the two steps' objectives and the biased experimental comparison — significantly weaken the contribution as presented. The first issue means the paper's theoretical narrative has a gap at exactly the point where the two steps connect. The second issue means the empirical results do not convincingly demonstrate that the SHF framework itself (as opposed to simply using bound information) provides an advantage. These are fixable weaknesses, but addressing them would require non-trivial changes to the paper's framing and experiments.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>