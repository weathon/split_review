Here is my final consolidated review.

---

## Summary

This paper addresses the activity cliff (AC) problem in molecular property prediction — where structurally similar molecules have different properties, causing models to produce indistinguishable representations. The authors first empirically demonstrate that standard training fails to fit AC molecules (they have persistently higher training loss across multiple architectures). They then propose LAC, a training algorithm with two components: (1) a node-level curriculum learning scheme that weights AC molecules higher during sample selection, and (2) an edge-level pairwise ranking loss that directly pushes predictions of AC pairs apart. Experiments across classification (6 base models on 4 datasets) and regression (ChEMBL) tasks show consistent improvements.

---

## Strengths

1. **Well-motivated empirical diagnosis of training-stage AC difficulty.** Section 3 (Figures 2–3) provides clear evidence across four model setups (GIN, GraphGPS, 3D-PGT, Uni-Mol) that AC molecules have persistently higher training loss at convergence. This goes beyond prior work that analyzed inference-stage difficulty only, and grounds the method's motivation concretely.

2. **Sensible and novel combination of AC-weighted curriculum learning + pairwise ranking.** The node-level task (Equation 1) assigns higher weight to AC molecules during loss-based curriculum selection, so that among equally hard samples, AC molecules are prioritized. The edge-level task (Equation 2) directly optimizes prediction separation on AC pairs. Both components are straightforward individually but their combination is novel and directly targets the problem. Ablations (Tables 4–6) show each component contributes and the best results come from combining both.

3. **Model-agnostic integration across diverse backbones.** Table 2 demonstrates consistent ROC-AUC improvements when LAC is applied to GIN, GraphGPS, GraphMVP, 3D Infomax, 3D-PGT, and Uni-Mol — covering both randomly initialized and pre-trained models. This versatility is a genuine strength beyond what a single-architecture method would offer.

4. **Thorough ablation and hyperparameter sensitivity analysis.** Tables 4–8 systematically isolate each design choice: node vs. edge contributions, AC weight \(p\), curriculum on edges, schedule type \(R(t)\), and schedule hyperparameters \((\gamma, \lambda)\). This builds confidence that the method's improvements are not from a single fragile setting.

---

## Weaknesses

### Fatal
None.

### Major

1. **No reported variance or statistical significance for any experimental result.** All tables (2–8) report only single numbers with no standard deviations, confidence intervals, or multi-seed aggregates. Molecular property prediction datasets are often small and high-variance. Some reported improvements are very small (e.g., +0.001 ROC-AUC on MUV with GraphGPS, +0.002 on SIDER with GIN) and could plausibly be noise. Without variance information, the central claim that LAC "improves the final performance for all base models" cannot be properly evaluated. *Evidence: Tables 2, 3, 4, 5, 6, 7, 8 each show single columns of numbers; no mention of random seeds, standard deviation, or replication anywhere in the paper.*

2. **Ambiguity in how AC is defined and used in multi-task prediction.** The paper evaluates on Tox21 (12 binary tasks) and ToxCast. Definition 3.2 states AC is per-property, and Figure 4 correctly shows different AC patterns across properties. However, the node-level weighting (Equation 1) assigns a single scalar \(p_i\) per molecule based on whether "molecule i has activity cliff." For a multi-task dataset, a molecule may be AC for Task A but not Task B — how is this resolved into a single \(p_i\)? Is the model trained jointly across tasks or separately? Is AC defined as "AC for *any* task" or "AC for *all* tasks" or something else? The paper provides no description of the training loop that resolves this, making it unclear whether the method as described correctly applies to the primary classification datasets. *Evidence: Section 4.2, Equation (1); datasets described in Section 5.1 include Tox21 and ToxCast which have multiple binary tasks.*

### Minor

1. **"Node classification" framing is imprecise.** The paper repeatedly claims to "reformulate molecular property prediction as a node classification problem" on the molecule similarity graph (Section 4.1, abstract, contributions). However, the graph is only used to (a) define which pairs of molecules incur the edge-level loss and (b) visualize relationships. There is no message passing, graph convolution, or information propagation on this molecule-level graph. The method is better described as a weighted curriculum learning scheme plus a pairwise ranking loss that operates on a graph-defined set of pairs. This framing disconnect does not invalidate the method but is misleading and should be corrected. *Evidence: Section 4.1 defines graph; Sections 4.2–4.3 describe training, which uses standard molecular representations (not graph-structured representations over the molecule-level graph).*

2. **"First to investigate" claim is slightly overstated.** Contribution 1 claims "first to investigate why existing models fail." While the empirical analysis of training-stage AC difficulty (Section 3, Figures 2–3) is useful and goes beyond prior inference-stage analysis, it is fundamentally an observation — showing that AC molecules have persistently higher training loss — rather than a deeper mechanistic investigation (e.g., gradient norm analysis, representational similarity analysis, phase transition analysis). The novelty of the paper lies in the proposed training algorithm, not in the diagnosis. The claim should be softened. *Evidence: Lines 19–22, Section 3.*

3. **Regression experiments limited to a single architecture (MLP+ECFP).** For classification, the method is tested with 6 diverse backbones including GNNs and transformers. For regression (Section 5.2), only an MLP with ECFP fingerprints is used. The paper states this follows prior practice (van Tilborg et al., 2022) and that MLP performs best on those datasets, but this asymmetry weakens support for the claim that the method generalizes to regression with more sophisticated backbones. *Evidence: Section 5.2, Table 3.*

4. **Missing reproducibility details for graph construction.** The paper references Dablander et al. for the definition of matched molecule pairs (Definition 3.1) but does not specify the implementation — e.g., software (RDKit?), exact chemical transformation rules, parameters for bond cutting, and thresholds. This is essential for replication. *Evidence: Definition 3.1, Section 4.1.*

5. **No discussion of limitations or computational cost.** The paper lacks a limitations section. The molecule graph construction and pairwise loss scale as O(N²) in the number of molecules, which could be prohibitive for large datasets. The method also depends on a specific structural similarity definition (matched molecule pairs via common substructure), which may miss ACs arising from other similarity notions. These are worth acknowledging. *Evidence: Paper has no limitations/failure cases section.*

### Trivial
None.

---

## Nice-to-Haves

- A multi-seed (≥5) experiment on one or two representative datasets (e.g., Tox21 with GraphGPS) reporting mean and standard deviation would resolve the most critical weakness.
- Clarifying the multi-task AC handling with a precise description of the training loop (including how \(p_i\) is computed per molecule) would address the second major concern.
- Extending regression experiments to at least one GNN backbone would strengthen generality claims.

---

## Removed Points

- **Harsh critic's point about Proposition 4.1 being "standard"/"not adding theoretical depth"**: Removed. The proposition is a straightforward gradient expression — it is presented as a helpful derivation, not as a deep theoretical contribution. Criticizing it as insufficiently deep is not a genuine weakness.
- **Harsh critic's point that Table 1 is "weak evidence"**: Removed. The paper explicitly states the results are limited and uses them to motivate the need for a more refined strategy. The paper does not overclaim from this experiment.
- **Strength Finder's "First empirical demonstration" strength framing is kept but the "first to investigate" weakness is already noted as overstated.** No removal needed — the strength (empirical observation) and weakness (overclaimed novelty) can coexist at different granularities.
- **Harsh critic's suggestion to "remove the 'node classification' framing"**: Moved to Nice-to-Haves / Minor weakness rather than treated as a fatal flaw. The framing is imprecise but does not invalidate the contribution.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface the same main observations: the method is sensible and well-evaluated in breadth, but the absence of error bars and the multi-task ambiguity are real concerns that limit confidence.

---

## Suggestions

1. **Report error bars.** Run all main experiments (Table 2, Table 3) with at least 5 random seeds and report mean ± std. This is the single highest-impact revision.
2. **Clarify multi-task AC resolution.** Describe exactly how \(p_i\) is computed per molecule for multi-task datasets (e.g., is a molecule AC if it is part of an AC pair for *any* task? Is training done per-task or jointly?). Add a sentence or pseudocode snippet.
3. **Reframe the "node classification" language.** Describe the method accurately from the start: an AC-weighted curriculum learning and pairwise ranking approach that operates on a molecule similarity graph, not a graph neural network on that graph.
4. **Add a limitations paragraph.** Acknowledge the O(N²) cost of pair construction, dependence on the matched-molecule-pair definition, and the scope of current regression evidence.

---

## Score and Decision

The paper addresses a real and important problem with a well-motivated, sensible method. The experimental coverage is broad and the ablations are thorough. The core issues are: (a) no variance reporting, which prevents proper evaluation of claimed improvements, and (b) ambiguity in how the method handles multi-task AC. These are significant but addressable. The paper's contributions — the AC-weighted curriculum and pairwise ranking loss — are novel, the motivation is solid, and the empirical trends are consistent. With variance reporting and multi-task clarification, this would be a strong paper. In its current form, the missing evidence for statistical reliability and the methodological ambiguity hold it back from being fully convincing.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>