Now I have everything I need. Let me produce the final consolidated review after carefully cross-checking each claim.

---

## Summary

This paper proposes GOttack, an adversarial attack framework for graph neural networks that uses graph orbits (specifically orbits 15 and 18) to identify candidate nodes for edge perturbations. The key idea is that nodes in these "periphery" orbits are effective targets for connecting to a target node, inducing misclassification. The method precomputes Graph Orbit Vectors (GOVs) once per graph, then restricts the candidate set to nodes whose top-two orbits are 15 and/or 18, reducing the search space to ~23% of all possible edge changes. Experiments across five datasets, three backbone GNNs, and four defense models show competitive misclassification rates while requiring roughly 55% of Nettack's runtime.

## Strengths

- **Principled observation about existing attacks.** The paper demonstrates (Table 5) that existing gradient-based attacks disproportionately target nodes in orbits 15/18 — e.g., 97.5% of Nettack's initial attacks on Polblogs involve these nodes, despite them comprising only 9.41% of all nodes. This provides a novel topological explanation for the effectiveness of prior attacks and grounds the design of GOttack in an empirical finding rather than pure intuition.

- **Consistent misclassification gains with lower computational cost.** GOttack achieves the highest overall misclassification rate (52.08% in Table 2 vs. 47.02% for Nettack, the second-best) across 15 attack settings, while requiring substantially less computation time (e.g., 147 seconds vs. 267 seconds on BlogCatalog, ~55% of Nettack's time per Table 4). The efficiency gain stems from the reduced candidate set and one-time orbit precomputation (0.17 seconds on Cora).

- **Effectiveness against defended models.** On four defense models (RGCN, GCN-Jaccard, GCN-SVD, MedianGCN), GOttack achieves the highest aggregate misclassification rate (33.07% vs. 32.5% for SGA), showing that the topological attack strategy remains potent even under robust training.

- **The precomputation design is practical.** Orbit vectors are computed once per graph as a preprocessing step and do not need to be recomputed per target node. This design choice makes the approach scalable: the candidate set is reduced to ~23% without per-target overhead.

- **Mechanistic insight via GNNExplainer.** Figure 5 provides a case study showing that GOttack-induced misclassification results from changes in edge importance within the computation graph, rather than from simple feature-space perturbations.

## Weaknesses

### Fatal
None.

### Major

- **Missing ablation against simpler candidate-selection heuristics.** The paper claims that orbits 15/18 are special, but never compares GOttack against straightforward alternatives that also shrink the candidate pool — e.g., selecting nodes with the lowest degree, highest betweenness centrality, or random nodes at the same pool size. Without these controls, the reader cannot tell whether GOttack's gains come from the specific orbit concept or simply from *any* heuristic that reduces the search space and focuses on peripheral nodes. The comparison against a "Random" baseline is mentioned (Section B.2, deferred to appendix) but a proper ablation isolating the effect of orbit-based selection from the effect of candidate-set reduction is absent from the main evaluation.

### Minor

- **Variance reporting is insufficient.** The paper averages over five random splits/initializations, but reports standard deviation only as a single global value in the table caption ("±1.1 for stds" for Table 2, "±.2 for stds" for Table 3). Without per-condition or per-cell variance, the reader cannot assess whether GOttack's numerical advantages (e.g., 52.08% vs. 47.02%) are statistically significant or within noise. This is especially relevant for the defense results where GOttack (33.07%) and SGA (32.5%) differ by only 0.57 percentage points.

- **The 33.07% vs. 32.5% margin on defenses is very small.** While GOttack achieves the highest overall rate against defenses, the gap over SGA is <1 percentage point. The paper's language ("highest misclassification rate") is technically correct, but the practical significance of this margin is unclear without significance testing.

- **Unclear sentence in the results section.** Line 190 states: "GOttack achieves the highest average rate of 0.58 over all budgets and datasets compared to the second best model of PRBCD and SGAttack with 0." The phrase "with 0" is nonsensical as written and obscures the intended comparison. This appears to be either a writing error or a parser artifact, and it undermines the clarity of a key quantitative claim.

- **Discrepancy between "155 tasks" (abstract) and visible counts.** The abstract claims "the highest average misclassification rate in 155 tasks." The body enumerates 15 settings (Table 2), 16 settings (Table 3), and 65 tasks from the budget experiments (Section D) — totalling 96 visible settings. While the appendix may contain additional experiments not visible here, the mismatch between the abstract and the counts a reader can verify is confusing and suggests sloppy cross-referencing.

### Trivial

- The time complexity formula on line 148 contains a formatting artifact ($O(|\dot{E}|\times d\bar{+}|V|\times d^{4})$), making it hard to parse precisely.
- Table 3's caption appears truncated mid-sentence at line 192 ("reduces the candidate set to about 23% Table 3..."), suggesting a layout issue.

## Nice-to-Haves

- **Test on heterophilous graphs beyond BlogCatalog.** The paper notes the orbit proxy works in a "weaker form" on heterophilous data, but only BlogCatalog is in this category among the five datasets. Additional heterophilous benchmarks would clarify the generality of the approach.
- **Ablation on single orbit vs. two orbits.** The paper states that using a single orbit gave "similar efficacy" with higher time complexity (line 207) but shows no data. Reporting this explicitly would strengthen the claim that the specific 15/18 combination is optimal.
- **Discussion of failure cases.** When GOttack fails to misclassify a target, is it because no 15/18 nodes are nearby, or because the selected perturbation is ineffective? Analyzing failure cases would deepen the understanding of when the orbit heuristic works.

## Removed Points

*These points are flagged to be removed per the reviewer instructions; treat them with caution.*

- **Criticism that Theorem 1 is unproven and no proof is referenced.** The paper references appendices (Sections B.2, D) which are stripped by the parser. The hard rule requires removing weaknesses about missing appendix content, as these exist in the original submission.
- **Claim that SGA originally used GCN and thus using SGC is unfair.** The paper transparently states "We use GCN as the surrogate model for the attack models except for SGA, which suggests SGC." This is a clear disclosure, not an error.
- **Speculation about PRBCD implementation mismatch.** The paper itself acknowledges that PRBCD gives "surprisingly low rates" (line 189). The critic's inference of an implementation error is unsupported speculation.
- **Criticisms about "universal attack" terminology.** The paper uses "universal" to mean applicable across architectures/datasets, not a single perturbation. This is a standard usage in the field and not misleading.
- **Criticism about the d⁴ time complexity for high-degree graphs.** The paper provides empirical evidence of fast runtime on real datasets (0.17s on Cora), which directly addresses this theoretical concern.
- **Request for more datasets / defenses.** The paper already evaluates on 5 datasets, 3 backbones + 4 defenses. This is within the standard scope for this venue.
- **Formatting/style nitpicks** (parser artifacts, term choices, etc.) per the hard rule.

## Novel Insights

The two reviewers do not produce any insight beyond what the paper itself contributes. The core tension — whether GOttack's orbit-based selection is genuinely superior to any heuristic that picks peripheral nodes — is legitimate but neither reviewer resolves it; they merely identify the gap. The finding that gradient-based attacks disproportionately target specific orbit categories (15/18) is the most interesting empirical observation that emerges from reading the reviews alongside the paper. This observation, rather than the attack method itself, may be the more durable contribution.

## Suggestions

1. **Add an ablation study** comparing orbit-based candidate selection against simple heuristics (lowest-degree nodes, random nodes at equal pool size, highest-betweenness nodes). This is the single most important experiment missing from the paper — without it, the claim that orbits 15/18 are uniquely suited cannot be separated from the trivial advantage of having a smaller candidate pool.
2. **Report per-condition standard deviations** or at least per-table error bars, and perform a paired bootstrap significance test for the comparison against the second-best method.
3. **Clarify the "with 0" sentence** and reconcile the "155 tasks" count in the abstract with the numbers reported in the body.
4. **Downgrade Theorem 1** to a conjecture or empirically-supported hypothesis if a formal proof is not provided, to avoid overclaiming theoretical rigor.

## Score and Decision

This paper presents a genuinely novel idea — using graph orbits to select adversarial perturbations — supported by reasonable empirical evidence across multiple datasets, backbones, and defenses. The core finding that existing attacks already exploit orbit-15/18 nodes is interesting and practically relevant. The main methodological weakness is the missing ablation against simpler heuristics, which prevents the reader from isolating the specific contribution of the orbit concept. The experimental reporting also has some clarity issues (variance, the "with 0" sentence). However, none of these issues are fatal: the paper's central claims are likely correct, and the gaps are addressable. I recommend acceptance with a request to add the ablation study and clarify the reporting.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>