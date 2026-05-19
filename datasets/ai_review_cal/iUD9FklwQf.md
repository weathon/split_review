- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5
Now I've verified the paper content thoroughly. Let me produce the consolidated final review.

## Summary
G4SATBench is the first comprehensive benchmark for GNN-based SAT solving. It provides a large, diverse collection of SAT datasets spanning 7 problem families across 3 domains (random, pseudo-industrial, combinatorial) at 3 difficulty levels, along with a unified evaluation framework that re-implements multiple GNN architectures (NeuroSAT, GCN, GGNN, GIN) on refined graph encodings (LCG*, VCG*) across three prediction tasks and multiple training objectives. Beyond leaderboard-style results, the paper conducts diagnostic experiments that reveal GNNs learn a strategy analogous to greedy local search (GSAT) but fail to internalize CDCL backtracking.

## Strengths

- **Large-scale, diverse, and principled dataset construction.** The benchmark assembles 7 problem families across 3 domains with 3 difficulty levels each, generating 80k training pairs per easy/medium set. Generator parameters are carefully chosen (e.g., phase-transition region for 3-SAT, expected-number-of-cliques = 1 for k-Clique) to avoid trivial instances. This directly addresses prior work's limitations of "limited domains (less than 3 generators), small size (less than 10k instances), or easy difficulty."

- **Unified evaluation framework enabling fair comparisons.** The paper re-implements NeuroSAT, GCN, GGNN, and GIN on both LCG* and VCG* graph encodings with a common interface, and evaluates them on satisfiability prediction, satisfying assignment prediction, and unsat-core variable prediction under supervised and two unsupervised losses. This removes the reproducibility barrier noted in prior work.

- **Rigorous experimental protocol.** Hyperparameters are grid-searched per model, results are averaged over 3 random seeds, and the total compute budget (~8000 GPU hours) is documented. This level of thoroughness exceeds typical practice in the GNN-for-SAT literature.

- **Insightful diagnostic experiments that advance understanding.** Section 6 goes beyond reporting accuracy to probe *how* GNNs solve SAT: clause-learning augmented instances show GNNs fail to capture CDCL; random initialization experiments show GNNs learn a structural procedure rather than fixed embeddings; and the trajectory analysis of predicted assignments (Figure 3) directly visualizes greedy-local-search-like behavior converging to minimal unsat clauses. The finding that NeuroSAT trained only for satisfiability prediction also implicitly searches for satisfying assignments (NeuroSAT*) is a genuine, non-obvious insight.

- **Clear justification for refined graph encodings (LCG*, VCG*).** The paper explicitly identifies information loss in standard representations (LIG/VIG lose clause information; LCG/VCG fail to distinguish literal polarities) and adopts LCG*/VCG* as standard inputs with consistent use across all baselines.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Heuristic comparison limited to two random-CNF datasets.** The central claim that "GNNs develop a solving heuristic similar to greedy local search but fail to learn CDCL" is supported by experiments on only SR and 3-SAT (both random CNF generators). While these are natural choices, the paper does not test whether the same LS-like behavior holds on combinatorial datasets (e.g., k-Clique, k-Domset) or pseudo-industrial ones (CA, PS), where the graph structure differs qualitatively. The conclusion may well be correct, but the evidence base is narrower than the claim's scope. This is a clear direction for future work and is not a fatal flaw — the experiments already conducted are well-designed — but it limits the generality of the headline finding.

2. **No variance or confidence measures reported for main results.** Tables 1, 3, and 4 report averages over 3 seeds but include no standard deviations, error bars, or confidence intervals. Given that performance differences between models are often small (e.g., 0.2–0.5%), it is unclear which gaps are meaningful versus noise. The paper states variance was "negligible" via the grid search protocol, but explicit numbers would strengthen the benchmarking claims.

3. **UNS₁ training instability noted but not analyzed.** The paper reports that UNS₁ loss leads to training failures ("–" in Table 3) for some model/dataset combinations but provides no analysis of the failure mode (loss explosion? saturation? specific datasets where it fails?). A brief description of observed patterns or recommended mitigations would help future users of the benchmark avoid this pitfall.

### Trivial
None.

## Nice-to-Haves

- **Runtime or scalability data.** The benchmark focuses entirely on accuracy metrics. A table of average inference time per instance (ms) per model/dataset, or a comparison to a traditional solver (e.g., MiniSAT) on the same instances, would help practitioners gauge the practical trade-offs. The paper's value as a *benchmark* would be strengthened by including efficiency as a supplementary axis, though this is not required for the paper's core contribution of understanding GNN capabilities.

- **Expand Section 6 to one non-random dataset.** Adding even one combinatorial dataset (e.g., k-Clique) to the trajectory analysis and augmented-instance experiments in Section 6 would substantially strengthen the claim that the LS-like behavior is a general property of GNNs rather than an artifact of random CNF structure. The authors already have trained models for these datasets from Section 5, so the additional compute cost would be modest.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Missing dataset statistics (average instance sizes).** The harsh critic claimed the paper does not report average instance sizes. The paper explicitly states "we compute several statistics of the SAT instances across difficulty levels" — this content likely appeared in a table/figure stripped during text extraction. Dataset size ranges (e.g., 10–40 variables for easy SR) are reported in the text.

2. **Contrastive pretraining experiment being a "single negative data point."** The critic suggested the experiment would benefit from additional conditions (larger corpus, different objectives). The paper already acknowledges this is a single approach and cites relevant prior work (gnnmayfail) to contextualize the negative result. Requesting a broader exploration of contrastive methods is scope creep for a paper whose primary contribution is the benchmark itself, not exhaustive pretraining studies.

3. **Various presentation/formatting nitpicks and missing MLP configuration details.** These reflect either parser artifacts or details appropriately deferred to standard supplementary material. The paper's level of implementation detail is appropriate for its class.

## Novel Insights

The most interesting observation that emerges from the synthesis of the reviews — beyond the paper's own contributions — is the interplay between the random initialization experiment (Table 6) and the trajectory analysis (Figure 3). The random initialization experiment shows that learned embeddings are not essential: GNNs with random initializations perform nearly identically. The trajectory analysis then reveals *what* those randomly-initialized GNNs do across message-passing iterations: they perform a multi-variable-flipping greedy search that progressively reduces unsat clauses, qualitatively matching GSAT. Taken together, these two findings imply that the GNN architecture itself — independent of the specific embedding values learned during training — encodes a structural prior that biases the model toward local-search-style iterative improvement on CNF graphs. This suggests that the inductive bias of message-passing on bipartite literal-clause graphs is surprisingly well-aligned with local search, and is perhaps *too rigid* to accommodate the dynamic graph modifications required by CDCL. This is a clean, falsifiable hypothesis that future work could test by varying the MPNN architecture while keeping the graph representation fixed.

## Suggestions

1. For the final version, consider adding a single additional dataset (e.g., k-Clique) to the Section 6 experiments to broaden the generality of the claim about GNNs learning LS-like behavior. The trajectory analysis plots in Figure 3 already provide the template for this.

2. Add standard deviations or min/max ranges to the main result tables (Tables 1, 3, 4) to help readers assess the significance of small performance differences.

3. Include a brief paragraph in the Limitations section or in Section 4.1 acknowledging that runtime comparison with traditional solvers is outside the current scope but would be a valuable direction for future benchmarking work.
