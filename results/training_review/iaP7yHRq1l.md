Here is the synthesized review.

## Summary

This paper presents a large-scale benchmark evaluating 12 causal discovery algorithms (including differentiable, constraint-based, score-based, and functional causal model-based methods) across 8 scenarios where model assumptions are violated (confounded, measurement error, unfaithful, heterogeneous, scale variation, missing data, mechanism violation, and autoregressive). The authors report results on over 70,000 experiments and find that differentiable causal discovery methods generally exhibit robustness across most misspecified scenarios, with the notable exception of scale variation. They also provide a theoretical analysis of linear differentiable methods' performance using noise ratio arguments drawn from Loh & Bühlmann (2014).

## Strengths

- **First systematic benchmark of differentiable causal discovery under diverse misspecifications**: The paper explicitly fills a gap identified in prior benchmarks (Montagna et al. 2023, Ng et al. 2024) by including gradient-based methods across eight misspecified scenarios. This is the most comprehensive evaluation of differentiable causal discovery under assumption violations to date and constitutes a useful community resource.

- **Large-scale, principled experimental design**: The benchmark covers 12 algorithms, 8 misspecified scenarios, multiple graph types (ER, SF, GRP), multiple node counts (10, 20, 50), and reports means and standard deviations over 10 trials per configuration. The scope (>70,000 experiments on >2,400 datasets) substantially exceeds prior work.

- **Documentation of a non-obvious empirical pattern**: The finding that linear differentiable methods maintain competitive performance under mechanism violation (when their linearity assumption is violated) is surprising and worth reporting. The follow-up MLP-based comparison revealing CAM's mechanism-dependent advantage is a thoughtful addition that strengthens the paper's conclusions.

- **Practical limitation on scale variation is explicitly acknowledged**: The paper clearly states that scale variation is the one scenario where differentiable methods fail, and cites Deng et al. (2024) as a path forward. This transparency is commendable.

## Weaknesses

### Fatal
None.

### Major

- **Ambiguous / potentially problematic hyperparameter tuning protocol (Section 3.3, Section 4)**. The paper states that hyperparameters are "determined as the optimal values relative to the specific dataset" without specifying the optimality criterion. The phrasing strongly suggests hyperparameters were selected using the true graph (oracle tuning), which would invalidate the practical conclusions the paper draws about method rankings — a practitioner cannot replicate this selection. The paper itself acknowledges the difficulty ("the ground truth of real data is unknown, making it difficult to effectively select hyperparameters"), but this acknowledgment does not mitigate the protocol if oracle tuning was used. This is the most significant weakness because the paper's central practical claim ("differentiable methods are robust for deployment") depends on rankings produced under an unrealistic selection regime. Even if the authors used a data-driven selection criterion (e.g., BIC), this should be stated explicitly. **The paper must clarify the selection criterion and, ideally, include an ablation with model-selection-based tuning for at least a subset of configurations.**

- **Theoretical analysis (Section 4.1.2) does not support the paper's comparative robustness claims.** The analysis uses noise ratios from Loh & Bühlmann to explain when linear differentiable methods' performance degrades (measurement error, unfaithful) or stays stable (missing). However, these are properties of least-squares-based estimation generally, not of differentiable methods specifically. The theory does not explain *why differentiable methods outperform constraint-based or score-based alternatives* in misspecified settings — which is the paper's central empirical finding. The claimed "theoretical explanations for the performance of differentiable causal discovery methods" thus do not differentiate differentiable methods from other least-squares approaches. The missing scenario analysis (scale variation, heterogeneity) further limits the scope of the theoretical contribution. The claims in the abstract and conclusion should be adjusted to match what the theory actually provides.

### Minor

- **Main text reports results only for 10-node ER-2 graphs.** The paper generates data for d ∈ {10, 20, 50} and multiple graph types (ER, SF, GRP), but the main text only shows 10-node ER-2 results, citing space limitations. Full results are relegated to the appendix (which was stripped by the parsing system). Since the paper's empirical conclusions derive almost entirely from this single configuration, the generality of the claims — especially the method rankings — cannot be verified from the main text alone. This is compounded by the fact that graph size and structure are known to interact strongly with algorithm performance.

- **Scale variation failure is downplayed relative to its practical significance.** The paper frames scale variation as a single exception to an otherwise robust pattern. However, standardizing variables is one of the most common preprocessing steps in real-world data analysis. While the paper acknowledges this limitation and cites a potential fix (Deng et al. 2024), the central "robustness" claim is substantially less impactful given this failure mode. The paper would benefit from a more balanced framing that honestly weights this limitation against the other scenarios.

- **CAM comparison tested only one alternative nonlinear mechanism (MLP).** The paper's claim that differentiable methods have "a significant advantage over CAM in all types of assumption violation scenarios except for scale variation" rests on NOTEARS-MLP outperforming CAM when the data-generating mechanism is an MLP. This is a single functional form; there are many possible nonlinear mechanisms, and CAM performs better under Gaussian process mechanisms. The claim should be scoped accordingly.

- **The heterogeneity evaluation uses a specific parameterization (noise variance shift across two domains).** This is a reasonable setup, but the paper should discuss whether the conclusions generalize to other forms of heterogeneity (e.g., distribution shifts in the causal mechanisms themselves).

### Trivial
None.

## Nice-to-Haves

- Report performance degradation relative to the vanilla scenario (e.g., ΔSHD = SHD_misspecified − SHD_vanilla) alongside absolute SHD. This would directly quantify robustness and address the concern that a method can be ranked "best" while still performing far worse than in the vanilla setting.

- Include a scale-invariant differentiable method (e.g., following Deng et al. 2024) in the benchmark to demonstrate that the scale variation issue is addressable rather than inherent.

- Include algorithms designed for specific misspecified scenarios (e.g., FCI for confounded settings) to contextualize how much robustness is lost relative to specialized solutions.

## Removed Points

These points were considered but removed for the reasons stated:

- **Criticism that the robustness definition is "incoherent"** — The paper adopts Montagna et al. (2023)'s definition ("ability to perform well in misspecified scenarios"), which is clear and standard. Absolute SHD/SID ranking is a valid operationalization. The suggestion to add ΔSHD is a nice-to-have, not a correction of an incoherent definition. **[Moved to Nice-to-Haves]**

- **Criticism that the heterogeneous scenario numbers contradict the "competitive" claim** — The critic cites specific numbers (PC=5.3, NOTEARS=12.6) from table images that cannot be verified through the text extraction. The paper's text notes that differentiable methods achieve "optimal or competitive" performance. Without access to the actual table values, this criticism cannot be evaluated and is removed. 

- **Criticism about missing appendix content** — The appendix was stripped by the parsing system; the authors are not responsible for this absence. 

- **Criticism that the paper should include FCI, MCAR-specific methods, etc.** — These demand extensions beyond the paper's stated scope, which is to evaluate how off-the-shelf methods perform under misspecification. The paper's goal is not to compare against specialized methods designed for each scenario. **[Moved to Nice-to-Haves]**

- **Criticism that the MLP mechanism is unrepresentative** — The paper explicitly motivates the MLP setting as a fairness check: since the GP mechanism favors CAM's assumptions, an alternative mechanism tests whether CAM's advantage is mechanism-specific. This is sound experimental design, not an unjustified choice. 

- **Criticism about MEC evaluation bias** — The paper follows standard practice (Zheng et al. 2018) in evaluating MEC outputs favorably. This is a well-known convention, not a flaw specific to this paper.

- **Several generic or superficial strengths from the Strength Finder** (e.g., "Consistency across multiple metrics and graph sizes" — unverifiable since results for larger graphs are in the stripped appendix; "Forward-looking practical insight on scale variation" — this is standard scholarly practice, not a distinctive strength).

## Novel Insights

The three reviews largely converge on the paper's main contributions (large-scale benchmark, documentation of differentiable methods' robustness across most scenarios) and weaknesses (hyperparameter tuning protocol, theoretical disconnect, selective main-text reporting). A genuinely novel observation that emerges is that the hyperparameter tuning concern is more structural than the paper's brief acknowledgment suggests: because differentiable methods (NOTEARS-MLP, GraN-DAG) have more tunable hyperparameters than simpler baselines (PC, GES), oracle tuning disproportionately benefits them. This compounds the practical relevance gap — the methods that look best under oracle tuning may be the very ones that are hardest to deploy without ground-truth knowledge. Additionally, while the harsh critic treats scale variation as a fatal limitation, the reviews collectively suggest it is a serious but circumscribed limitation that future work (already referenced by the authors) is actively addressing. The deeper unresolved question is whether "robustness" in a benchmark with oracle hyperparameter selection translates to robustness in practice.

## Suggestions

1. **Clarify the hyperparameter selection criterion immediately.** State explicitly whether tuning uses the true graph (oracle) or a data-driven criterion (BIC, validation loss, etc.). If oracle tuning was used, add an ablation with model-selection-based tuning for a representative subset of configurations (e.g., 10-node ER-2 under 3–4 misspecified scenarios). The paper's practical conclusions hinge on this.

2. **Add a ΔSHD / ΔSID table** showing each method's absolute performance degradation from the vanilla scenario. This would directly operationalize the robustness definition and reveal whether methods that rank well are genuinely robust or merely less-bad than alternatives.

3. **Re-frame the theory section** to acknowledge that the noise-ratio analysis applies to least-squares-based estimation broadly, not to differentiable methods specifically. Alternatively, add a brief explanation of why the differentiable optimization landscape or DAG constraint might confer advantages beyond what least-squares theory alone predicts.

4. **Include at least one summary table or figure for d=20 or d=50 in the main text** to support the generality of the conclusions. Even a single table in the main text would address concerns about selective reporting.

5. **Tone down the claim about CAM advantage** by noting that it was tested against only one alternative mechanism (MLP), and that CAM still performs better under Gaussian process mechanisms.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>