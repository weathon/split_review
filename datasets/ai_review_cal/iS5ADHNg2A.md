- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8
Now I have a thorough understanding of the paper. Let me compose the consolidated review, carefully verifying each claim against the paper text.

---

## Summary

This paper studies deceptive fairness attacks on graphs, formulating the problem as a bi-level optimization where the upper level maximizes a differentiable bias function (for a user-chosen fairness definition) and the lower level minimizes task loss (for deceptiveness). The authors propose FATE, a meta-learning framework that computes the meta-gradient of the bias function w.r.t. the graph to guide edge addition/deletion. They instantiate the framework for both statistical parity (via KDE + Q-function approximation) and individual fairness (via Laplacian regularization), and evaluate on three benchmark datasets.

## Strengths

- **Bi-level formulation that generalizes across fairness definitions and graph models.** Equation (1) cleanly formalizes the attack as a bi-level optimization, and the framework is instantiated for both group fairness (statistical parity, Section 4) and individual fairness (Section 5). This goes significantly beyond prior work (Hussain et al.) that only attacks group fairness via random edge injection without utility consideration.

- **Empirical evidence that FATE consistently amplifies bias while preserving utility for statistical parity.** In Table 1, across all three datasets and all perturbation rates, both FATE-flip and FATE-add increase the SP metric relative to the benign graph while achieving the highest or tied-highest micro F1 among all methods. Every baseline fails (decreased SP or degraded utility) in at least one setting (underlined entries). This supports the core claim for the group fairness instantiation.

- **Meta-gradient solver with first-order approximation enabling practical discrete attacks.** Equations (3)–(7) describe how to approximate the meta-gradient via unrolling the lower-level training, then select edges via a preference matrix (Eq. 8). This is more principled than random heuristics (Random, DICE-S) and is the only method in the evaluation that supports both edge flipping and edge addition.

- **Edge analysis reveals attack targets minority groups.** Figures 1 and 2 show that edges manipulated by FATE disproportionately connect nodes from the minority class and the protected group, providing interpretable evidence for how the attack exacerbates bias.

## Weaknesses

### Fatal
None.

### Major

1. **The statistical parity metric (ΔSP) is not explicitly defined in the main text.** Table 1 reports "$\spmetric$" (typeset as a LaTeX macro, likely ΔSP), and Section 4C describes how to estimate P[ŷ=1] and P[ŷ=1|s=1] via KDE and a Q-function approximation. However, the paper never states the formula for the reported metric — is it |P[ŷ=1] − P[ŷ=1|s=1]|? The absolute difference? Squared difference? The bias function used in the upper-level optimization (the KDE+Q-function estimate for differentiability) may differ from the metric reported in the table. Without a clear definition, the experimental claims for statistical parity are not fully interpretable. *Evidence: Table 1 caption and Section 4C describe how to estimate the two probabilities but never define the aggregate metric.*

2. **The conclusion overclaims "highest micro F1" without qualification, a claim not supported for the individual fairness instantiation.** The conclusion (line 294) states that FATE is "deceptive (achieving the highest micro F1 score)" without qualification. However, for individual fairness (Table 2), baselines sometimes match or exceed FATE's micro F1 (e.g., Pokec-n at 0.05: DICE-S micro F1 = 68.1±0.2 vs. FATE-flip 67.8±0.3; Pokec-z at 0.05: DICE-S 68.9±0.5 vs. FATE-flip 68.7±0.5). The individual fairness section itself uses more measured language ("comparable or even better utility"), but the unqualified conclusion is inconsistent with the full evidence. *Evidence: Table 2 rows show baselines outperforming FATE in several individual fairness settings; line 294 claims "highest micro F1" globally.*

3. **The first-order meta-gradient approximation is used without any analysis of its accuracy.** The paper adopts a first-order approximation of the meta-gradient (Eq. 4, citing MAML) to avoid the computational cost of full unrolling. No ablation compares this approximation against a full unrolled gradient (even on a small graph), so it is unclear whether the approximation degrades attack quality. *Evidence: Section 3A describes the first-order approximation but provides no empirical or theoretical analysis of its fidelity.*

4. **The evaluation is limited in scope for a paper claiming "any graph learning model" applicability.** Although the paper claims the framework works for any differentiable graph learning model and fairness definition, the main experiments only attack vanilla GCN as the victim. The paper states "More experimental results" for FairGNN and InFoRM-GNN (lines 219, 279) but these results are absent from the visible portion — if they were in an appendix that was stripped, this is noted. Nevertheless, the main body's claims of broad applicability rest on a narrow empirical base (GCN only). *Evidence: Tables 1 and 2 only evaluate GCN as the victim model.*

### Minor

1. **In the individual fairness experiments, FATE's bias increases are sometimes very small and baselines can be more deceptive.** For Pokec-z (Table 2), FATE's bias increases from 2.6 (benign) to only 2.9 at 0.15 perturbation, and DICE-S achieves higher micro F1 and bias in several settings. The paper acknowledges a "weaker correlation" for Pokec-n and Pokec-z (Section 6.2) but does not explain why the method struggles or whether this is a fundamental limitation. *Evidence: Table 2, Pokec-z and Pokec-n columns.*

2. **The comparison between FATE-flip (addition+deletion) and baselines (addition only) is not fully controlled.** All baselines are restricted to edge addition, while FATE-flip can also delete edges. The paper includes FATE-add (addition only) as a fairer comparison, which partially mitigates this concern. However, the budget B counts additions and deletions equally even though the space of possible deletions is smaller than the space of additions, making the perturbation budget not directly comparable across operation types. *Evidence: Table 1 caption notes the asymmetry; no discussion of budget normalization across operation types.*

3. **No ablation of the meta-gradient against simpler gradient-based alternatives.** The paper does not compare FATE's meta-gradient (which unrolls through model retraining) against a simple gradient of the bias function w.r.t. the graph *without* unrolling (i.e., assuming the model is fixed). Such an ablation would isolate the benefit of the bi-level formulation and justify its additional computational cost. *Evidence: No such baseline appears in the experiments.*

4. **The number of attacking steps k and budget division are not specified.** The method uses iterative attacks with budgets δ₁,…,δₖ (Section 3B), but no experimental details are given for how k is chosen or how the total budget B is divided across steps. This affects reproducibility. *Evidence: Section 3B mentions δ₁,…,δₖ but no experimental setting is reported.*

### Trivial

1. The bandwidth parameter *a* for KDE (Section 4C, Eq. 6) is not stated in the main text; it should be specified for reproducibility.

2. The notation in Eq. (4) for the first-order meta-gradient — specifically, the term ∇_𝒢 Θ^(T) — requires the Hessian of the loss. The relationship between the MAML-style approximation and the actual gradient computation could be clarified.

3. The individual fairness oracle similarity matrix uses cosine similarity of adjacency matrix rows (Section 6.2); sensitivity to this choice is not discussed.

## Nice-to-Haves

- A statistical significance test (e.g., paired bootstrap) for micro F1 and bias differences would strengthen the "most deceptive" claim.
- A discussion and/or small-scale experiment on node feature attacks would demonstrate the framework's claimed generality.
- A brief complexity analysis or scalability discussion beyond the O(n²) space limitation noted in the paper would be helpful.

## Removed Points

These points were flagged by reviewers but are removed (with justification) from the main review:

- *"Metric definitions are absent"* — Kept but downgraded from major presentation issue (the core weakness stands: ΔSP is not explicitly defined). 
- *"Unfair comparison on perturbation scope" (as a fatal issue)* — Kept as minor (the paper includes FATE-add as a control, partially addressing this).
- *"First-order approximation with no analysis"* — Kept as major.
- *"Missing results for FairGNN/InFoRM-GNN"* — Removed: The paper states "More experimental results" on lines 219 and 279; the corresponding tables/figures were likely stripped by the parser, per the instruction that missing appendix/supplementary content should not be penalized.
- *"Effect sizes are small and confidence intervals overlap"* — Removed: Overlapping confidence intervals are typical for 5-seed experiments in this area. The pattern across multiple datasets and perturbation rates is consistent, which is how claims like "the most deceptive" are supported in practice without formal hypothesis testing.
- *"Attacker's goal not fully convincing"* — Removed: This is a subjective motivation critique not related to the paper's technical contribution. The paper's scenario (malicious banker amplifying bias while maintaining plausible deniability through utility preservation) is adequately motivated.
- *"No analysis of node feature attacks"* — Moved to Nice-to-Haves.
- *"KDE bandwidth not specified"* — Moved to Trivial.
- *"Edge analysis connection to meta-gradient not demonstrated"* — Weakened: The paper does show a plausible causal story; this is an interpretability analysis, not a core claim.
- All "Strengthening the Paper on Its Own Terms" suggestions from the harsh critic — Most are moved to Nice-to-Haves as they represent improvements beyond the paper's current scope.
- Strength Finder's generic/superficial strengths — Removed any that were generic ("addressed an important problem") and kept only concrete, evidence-grounded strengths.

## Novel Insights

None beyond the paper's own contributions. Both the harsh critic and strength finder converge on the same core assessment: the bi-level meta-learning formulation is the paper's primary novel contribution, and the experimental evidence supports its effectiveness for statistical parity attacks while being more mixed for individual fairness. No reviewer identified an unclaimed insight or reinterpretation of the results that the authors missed.

## Suggestions

1. **Define ΔSP explicitly.** Add a sentence or equation in Section 4C stating the metric formula (e.g., ΔSP = |P[ŷ=1] − P[ŷ=1|s=1]|, or whichever variant is used).

2. **Qualify the conclusion.** Replace "achieving the highest micro F1 score" with a more precise statement that separates statistical parity and individual fairness results.

3. **Add a meta-gradient ablation.** Compare the proposed meta-gradient against a standard gradient of the bias function w.r.t. the graph (without unrolling through retraining) on at least one dataset. This would justify the bi-level formulation's computational cost.

4. **Report the number of attacking steps** and how the budget is divided across steps in the experimental setup.
