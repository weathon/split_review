## Summary

The paper proposes AdT-HyGCL, a hypergraph contrastive learning framework with three components: (1) noise-enhanced augmentation that adds random perturbations to node features, (2) a dual-level contrast mechanism operating at the node level and a "community" level (where community embeddings concatenate hyperedge embeddings with averaged node embeddings within each hyperedge), and (3) an adaptive temperature schedule that adjusts the contrastive temperature based on pairwise embedding distances among negatives. The method is evaluated on semi-supervised node classification across eight hypergraph datasets and robustness against graph attacks.

## Strengths

- **Strong and consistent empirical results across diverse benchmarks**: Table 1 shows AdT-HyGCL achieves the best or runner-up accuracy/Macro-F1 on all eight datasets spanning co-citation, co-authorship, UCI, CV, and e-commerce domains, outperforming six supervised HyGNNs and three prior hypergraph contrastive methods (HyperGCL, CHGNN, TriCL) under two contrastive loss formulations (NT-Xent and JSD). This is the paper's single strongest piece of evidence.

- **Demonstrated robustness under adversarial attacks**: Table 2 shows AdT-HyGCL suffers smaller performance declines than baselines under both minmax and nettack perturbations across four hypergraphs, providing evidence for the robustness claim that goes beyond what typical hypergraph contrastive papers evaluate.

- **The community embedding design is principled**: Proposition 1 provides a concrete worked example where two hyperedges from different augmented views share most of their nodes, showing why community embeddings (concatenating hyperedge embeddings with averaged node embeddings) can remain separable when hyperedge embeddings alone become confusable as a negative pair. This provides a clear architectural rationale for the community-level design.

- **Validated across two contrastive loss families**: Results with both NT-Xent and JSD losses show the framework is not tied to a specific loss function, unlike prior hypergraph contrastive work that typically evaluates only one loss.

## Weaknesses

### Major

1. **No component-level ablation study**: The paper introduces three distinct claimed contributions — noise-enhanced augmentation, dual-level (node+community) contrast, and adaptive temperature — but provides no ablation isolating any of them. Specifically missing: (a) node-level-only vs. community-level-only vs. full dual-level contrast, (b) with vs. without noise augmentation, (c) adaptive temperature vs. a properly swept fixed temperature or vs. a simple annealing schedule (e.g., τ = τ₀/(1+γ·t)). Without these ablations, the reported gains cannot be attributed to any specific claimed contribution. This is the most significant weakness, as it directly undermines verification of the paper's core claims at the standard expected by ICLR.

2. **Comparison against the most relevant prior work (TriCL) is asserted but not substantiated**: The paper claims TriCL "still fails to comprehensively depict the group-wise collective behaviors within hyperedges" (line 28) and characterizes TriCL's group-level mechanism as operating on hyperedge embeddings **Z** (line 89). However, Proposition 1 compares the proposed community embeddings **H** only to hyperedge embeddings **Z**, not to TriCL's actual group embeddings. The paper never demonstrates that TriCL's group embeddings are equivalent to **Z**, nor does it empirically compare community-level contrast against TriCL's group-level mechanism with all other components held fixed. This leaves the claimed advantage over the closest prior work unsubstantiated.

### Minor

3. **Adaptive temperature is not compared to simpler scheduling alternatives**: The temperature update in Equation 5 is a deterministic function of pairwise embedding distances with three additional hyperparameters (η, ρ, τ_low). Figure 4 compares it against only a few static τ values (without a systematic sweep) on three datasets, and a version without τ_low. No comparison is made to simple annealing baselines (cosine decay, exponential decay). Without this, it is unclear whether the complex pairwise-distance-based formula provides any benefit over a much simpler schedule.

4. **Noise augmentation module is underspecified for reproducibility**: The paper states noise δ_i is drawn from "a specific distribution (e.g., uniform distribution)" (line 68) but specifies neither the distribution type definitively nor its parameters (range, variance, or scale relative to feature magnitudes). Since this is applied to node attribute features across datasets with varying dimensionality and scale, the current description is insufficient for independent reproduction of a core method component.

5. **"Theoretical justifications" (Propositions 2–4) are not substantive novel contributions**: Proposition 2 (contrastive loss is hardness-aware) and Proposition 3 (temperature controls penalties on hard negatives) restate standard, well-known properties of the NT-Xent loss established in prior work. Proposition 4 demonstrates that the temperature in Equation 5 responds to embedding distances, which is true by construction. These do not provide theoretical justification for why the specific form of Equation 5 is optimal — they are better characterized as motivational analyses.

### Trivial

6. **Equation 5 labeling inconsistency**: The second line of Equation 5 is labeled τ_nd^(t) on the left-hand side but uses τ_cm^(t-1) on the right-hand side. It should presumably be τ_cm^(t). This should be corrected.

## Nice-to-Haves

- Sensitivity analysis for the three adaptive temperature hyperparameters (η, ρ, τ_low) would strengthen the empirical characterization of the adaptive module.
- Testing on downstream tasks beyond node classification would broaden the generalization claims, though this is not required given the paper's stated scope.
- Statistical significance testing (e.g., confidence intervals for the best-vs-second-best comparisons in Table 1) would clarify whether the reported improvements are reliable given the standard deviations.

## Removed Points

- *Criticism about the adaptive temperature being "not a learned parameter"*: Not a meaningful distinction — many effective mechanisms in deep learning are deterministic rather than gradient-based. The real issue (captured in weakness 3) is the absence of comparison to simpler alternatives.
- *Criticism that baselines may mix architecture differences*: The paper states "We adopt AllDeepSets as the encoder over all datasets" (line 180); the contrastive methods share a common backbone, and HyGNN baselines using their native architectures is standard practice.
- *Criticism about the Equation 5 label as a "parser error"*: Formatting/parser artifact.
- *Strength about noise augmentation being "grounded in a known principle"*: Generic; being "inspired by" a design principle is not a strength without evidence that the specific noise magnitude used creates meaningfully challenging augmentations.
- *Criticism about missing error bars in figures*: Table 1 reports mean±std across 5 runs; figures focus on qualitative trends, which is standard practice in the field.
- *Scope-creep criticisms about missing link prediction/graph-level tasks*: The paper scopes itself to node classification.
- *Criticism about statistical significance tests not being run*: Not a standard expectation for the types of visualizations (Figure 2-4) presented.

## Novel Insights

None beyond the paper's own contributions. The reviews converge on a clear gap between the paper's claimed contributions and the evidence provided, but do not produce a synthetic insight unavailable from reading the paper itself.

## Suggestions

1. **Run the three component ablations**: Compare full AdT-HyGCL against (i) node-level contrast only, (ii) community-level contrast only, (iii) without noise augmentation, and (iv) with a fixed optimal temperature or simple annealing schedule. This is the single highest-priority addition.
2. **Substantiate the TriCL comparison**: Empirically compare community-level contrast against TriCL's group-level mechanism using the same encoder and augmentation pipeline on at least a few datasets.
3. **Specify the noise distribution precisely**: Provide distribution type, parameters, and whether it is scaled per-dataset feature statistics.
4. **Compare adaptive temperature to simple baselines**: Add a systematic sweep of fixed τ values and at least one annealing baseline (cosine or exponential decay), with a sensitivity analysis of η and ρ.
5. **Correct Equation 5** so the second line reads τ_cm^(t) rather than τ_nd^(t).

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>