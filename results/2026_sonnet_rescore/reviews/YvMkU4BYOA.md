## Summary

XBIC is a score-based causal structure learning method for purely discrete data that augments the standard BIC penalty with an edge-specific soft weight derived from aggregated Shapley attributions from per-node XGBoost classifiers. The core idea is that asymmetry in mean attribution magnitudes (|φ̄_{j→i}| vs. |φ̄_{i→j}|) provides directional evidence that biases hill-climbing search toward the true DAG within a Markov equivalence class. The method is evaluated on ten bnlearn benchmark networks (6–76 nodes) over seven sample-size regimes totalling 700 runs, reporting consistent (though variable) improvements in directed-edge F₁ over BIC-HC, PC, and a generalized-score GES variant.

---

## Strengths

- **Aggregate empirical gains are real and substantial for most networks.** Table 4 reports +5.6% (relative) over BIC-HC, +9.6% over GES, and +20.9% over PC across 700 runs. Table 2 confirms positive F₁ deltas for the majority of network × sample-size combinations, especially for medium/large graphs at moderate-to-large sample sizes. These numbers are reported across 10 repetitions per cell with significance tests.

- **Graceful degradation to BIC when evidence is weak.** Equation (2) analytically ensures that XBIC reduces exactly to BIC when SHAP(G) = 0 or w = 0, and the consistency remark shows the O(log N) penalty growth rate is preserved. Table 2 confirms this empirically: small-sample cells (e.g., Asia, Sachs, Survey at 0.125M²) show zero deltas, meaning XBIC does not harm performance when classifiers produce unreliable attributions.

- **Robustness to the confidence threshold is demonstrated.** Section 4.1 reports that varying τ from 0.7 to 0.95 changes downstream F₁ by < 1%, showing the main function of the filter is computational efficiency rather than a sensitive tuning decision.

- **Clear problem statement with code release.** The paper targets a well-defined and practical gap (directed-edge recovery for purely discrete BNs) and releases code, data splits, and scripts for reproducibility.

---

## Weaknesses

### Fatal
None.

### Major

- **The directional asymmetry claim lacks theoretical justification.** The paper's central mechanism, stated in Section 3.2, is: "if |φ̄_{1→2}| >> |φ̄_{2→1}|, the edge X₁ → X₂ has stronger directional support than X₂ → X₁." No theoretical argument is provided for why this asymmetry should hold in observational data from general discrete BNs. A classifier f_i trained on X_{∖i} assigns high Shapley values to any variable strongly predictive of X_i in the observational distribution — this includes parents, siblings (sharing a common parent), or descendants. There is no a priori guarantee that the Shapley magnitude of a true parent X_j in the f_i model exceeds the Shapley magnitude of X_i in the f_j model. The paper acknowledges in its Limitations that "formal analysis of the weighting mechanism … is an important direction," but presents the asymmetry as intuitive self-evidence. The consistency remark in Section 3 addresses only the preservation of the log N growth rate, not whether XBIC recovers the correct DAG in the limit — the relevant consistency question. The whole method rests on this directional claim, and the paper offers neither proof nor direct empirical validation of the asymmetry itself. This makes the contribution a heuristic with unclear scope of validity.

- **Random PDAG completion artificially inflates the PC comparison.** Section 4.1 states that for constraint-based methods returning a PDAG, the paper "complete[s] it to a DAG by randomly orienting undirected edges (while preserving acyclicity) before computing directed-edge metrics." This randomly degrades approximately 50% of PC's undirected edges to wrong orientations, since a PDAG encodes exactly those edges whose orientation *cannot* be determined by available CI evidence. As a result, the 20.9% relative F₁ improvement over PC is partly a methodological artifact rather than a reflection of XBIC's orientation power. Principled PDAG-to-DAG completion (e.g., completion by BIC scoring), separate reporting of skeleton vs. orientation F₁, or at minimum an explicit acknowledgment that this degrades PC's directed metrics, would be necessary to support the claimed magnitude of improvement over PC.

- **Inconsistent claim of "consistent gains" across all networks.** The abstract and Table 4 headline "+5.6% vs BIC" and "consistent gains." Table 2 tells a more qualified story. On Win95pts (76 nodes), the F₁ delta vs. BIC is 0.0 at 0.125M² and 0.25M², and **−0.09** at 8M². On Hepar2 (70 nodes), deltas vs. BIC are 0.01, 0.01, 0.01, 0.0, 0.0, −0.02, 0.0 — effectively no improvement and occasional harm. These two networks are the largest in the benchmark and the ones most relevant to the paper's stated application domains (healthcare, insurance). The paper attributes this to the confidence filter yielding few instances, but no empirical analysis of |S_i| sizes on these networks is provided to validate this explanation. Claiming "consistent gains" while the method provides zero or negative benefit on the two largest test cases is an overclaim that should be corrected.

### Minor

- **The hyperparameter w is selected post-hoc on the full test set.** The paper evaluates w ∈ {1, 2, 3}, picks w = 2 as the recommended setting based on highest aggregate F₁ over all 700 test runs (Table 4), but provides no prospective selection procedure (e.g., held-out validation or per-network tuning). Since w has material effect on the precision–recall trade-off (Figure 2), and since the best w is identified by inspecting the aggregate test-set metric, the advantage of w = 2 over w = 1 and w = 3 may reflect post-hoc optimization. Users running XBIC on a new dataset have no guidance on choosing w without repeating this selection process.

- **The GES comparison is only on GES-completed (i.e., easier) runs, but this is understated.** Section 4.5 notes that GES timed out on larger/denser networks and that the comparison retains only repetitions where GES completed. This subset consists of smaller networks and smaller samples — i.e., the subset where GES is most competitive and XBIC's advantage is most modest. The conclusion "XBIC achieves significantly lower SHD" refers to this favorable-for-GES filtered subset, a qualification that should be stated more prominently when discussing the GES comparison.

- **The use of absolute Shapley values is unexplained.** SHAP(G) in Eq. (3) uses |φ̄_{j→i}|, discarding sign information. SHAP values can be negative, indicating a feature decreases the predicted probability. No rationale is provided for why absolute values rather than signed values or some other aggregation are the right choice, despite sign potentially encoding meaningful directional information.

### Trivial
- None.

---

## Nice-to-Haves

- **Direct validation of the Shapley directional asymmetry.** Before using asymmetry as the justification for the method, the paper could compute |φ̄_{j→i}| and |φ̄_{i→j}| for all pairs in the benchmark networks and measure what fraction of the time the larger value correctly identifies the true causal direction. This would provide a principled empirical foundation for the method and clarify when and why it works.

- **Decomposing F₁ gains into skeleton recovery and orientation.** Since the stated motivation is resolving edge directions *within* Markov equivalence classes, reporting skeleton F₁ and orientation-within-equivalence-class F₁ separately would clarify what XBIC is actually contributing. It is currently unclear whether the gains come primarily from fewer spurious/missed edges or from better orientation among equivalent DAGs.

- **Per-network sensitivity to w.** Table 2 reports XBIC only at w = 2 per network; per-network w sensitivity is shown only for three networks in Figure 2 (Hailfinder, Alarm, Sachs). Full per-network results across all w values would strengthen the robustness argument.

- **MMHC as a baseline** for at least the larger networks (Alarm, Hailfinder, Win95pts, Hepar2), where it is a standard and competitive reference. The current justification ("MMHC targets large sparse graphs and is not the focus here") is weak given that four of the ten test networks are large sparse graphs.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic — "random PDAG completion" is "fatal" to all comparisons**: Partially retained but demoted to Major specifically for the PC comparison (which is the worst affected). For BIC, there is no PDAG completion issue since BIC-HC outputs a DAG. The core comparison (XBIC vs. BIC-HC) is unaffected.

- **Harsh critic — Section 3 SHAP(G) decomposability concern**: The critic notes that attributions are fixed pre-search and that adding edge j→i always increases SHAP(G) by |φ̄_{j→i}| regardless of the parent set context. This is an accurate description of the design but is an intentional computational tractability choice the paper acknowledges implicitly. It is not obviously a flaw unless one can show this causes incorrect decisions; the critic does not demonstrate this. Demoted to theoretical curiosity.

- **Harsh critic — Introduction framing mismatch (XBIC modulates all edges, not just CPDAG-undirected ones)**: Technically correct, but the practical effect of modulating all edges is to prefer orientations consistent with Shapley evidence, which does help with equivalence-class resolution. The framing is slightly loose but not misleading. Removed.

- **Strength Finder — "Thorough head-to-head comparison with GES"**: Partially removed. The GES comparison is limited to runs GES completed (a favorable filtering for GES). The comparison is honest but not "thorough" — it is a best-case scenario for GES, which is acknowledged in the Minor weakness above.

- **Strength Finder — "Computational cost is manageable"**: Partially removed. Table 5 shows XBIC is 191× slower than BIC-HC for Asia (74.78s vs. 0.39s), 600× for Survey (54.21s vs. 0.09s). "Manageable for offline discovery" is defensible but not obviously a strength. The runtime overhead is a real practical concern, retained as context rather than a strength.

---

## Novel Insights

The most genuinely novel observation in the synthesized reviews — not stated in the paper itself — is the suggestion to directly measure the Shapley directional asymmetry as a standalone empirical fact before using it as the mechanism for a causal discovery method. If |φ̄_{j→i}| > |φ̄_{i→j}| reliably tracks the true causal direction (as opposed to merely the stronger predictor direction), this would be a finding worth reporting in its own right and would substantially strengthen the method's justification. The fact that XBIC works empirically on most networks but fails on the two largest suggests that this asymmetry may be sample-size and density dependent in ways the current paper does not characterize.

---

## Suggestions

1. **Validate Shapley directionality directly**: Compute the fraction of true causal edges (j→i) for which |φ̄_{j→i}| > |φ̄_{i→j}| in the ground-truth graphs. Report this for each network and sample-size regime to demonstrate when the directional signal is reliable.

2. **Fix the PDAG completion for PC**: Use principled PDAG-to-DAG completion (e.g., by BIC re-scoring of the undirected edges) rather than random orientation, or report skeleton F₁ alongside directed-edge F₁. Revise the PC comparison accordingly.

3. **Clarify the "consistent gains" claim**: Acknowledge explicitly in the abstract or results that XBIC does not consistently improve over BIC on Win95pts (76 nodes) and Hepar2 (70 nodes), and characterize when the method is expected to help vs. not.

4. **Provide a prospective w-selection rule**: Describe a procedure users can apply on new data to select w — e.g., via cross-validated BIC comparison or a small held-out validation set — so the method is practically actionable without post-hoc tuning.

5. **Separate skeleton and orientation F₁**: Report these separately per method to clarify whether gains stem from better skeleton recovery or orientation within equivalence classes.

---

## Evaluation on Key Axes

- **Originality**: Moderate. Using Shapley attributions from per-node predictive models to modulate a scoring criterion is a novel combination in the discrete BN setting, though the idea of using predictive asymmetry to inform causal direction has precedent in continuous settings.
- **Importance of research question**: Good. Discrete causal discovery is underserved relative to continuous methods, and improving BIC-HC (the dominant practical method) has clear applied value.
- **Claims supported by evidence**: Partial. The BIC comparison is well-supported empirically; the PC comparison is compromised by random PDAG completion; the theoretical claim underpinning the directional mechanism is unsubstantiated.
- **Soundness of experiments**: Moderate concerns. 700 runs across 10 networks is commendable, but the PDAG completion issue, post-hoc w selection, and the "consistent gains" overclaim undermine the evaluation.
- **Clarity of writing**: Good. The method is compactly described, the pipeline figure is informative, and the paper is generally easy to follow.
- **Value to the research community**: Moderate. The method is a drop-in upgrade to BIC-HC with released code, which lowers adoption barriers, but its failure mode on the largest networks limits its appeal for real-world applications where large graphs are the target.

---

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>3</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>4</clarity>
<community_value>3</community_value>
</subscores>