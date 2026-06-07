## Summary

This paper proposes IDGNN, the first implicit neural network (deep equilibrium model) for dynamic graphs. The model formulates the sequence of graph snapshots as a coupled fixed-point system where node representations are propagated through both graph neighborhoods and across time stamps via a cyclic architecture. The paper proves well-posedness (unique fixed-point solution under norm constraints), and introduces a bilevel optimization training algorithm to avoid the computational cost of implicit differentiation. IDGNN is evaluated on 7 datasets (1 synthetic, 3 classification, 3 regression) against 9 baselines, achieving top-1 performance on 5 of 7 real-world benchmarks.

## Strengths

- **First implicit model for dynamic graphs with well-posedness guarantees.** The paper extends static implicit GNN theory (Gu et al., 2020) to the dynamic setting by vectorizing the coupled equilibrium equations into a single block-matrix system (Equation 4). Theorems 1 and 2 provide concrete, checkable conditions ($\|M_t\|_{op}<1$ and equivalently $\|W\|_\infty\|A\|_{op}<1$) that guarantee a unique fixed-point solution. This is a non-trivial architectural and theoretical extension — the fixed point must simultaneously satisfy constraints across $T$ time stamps with cyclic dependencies.

- **Controlled toy experiment directly demonstrates over-smoothing mitigation.** Section 5.1 constructs a challenging setting with cliques of 10 nodes across {5,10,15,20} snapshots where only the first snapshot carries class information. IDGNN achieves 100% accuracy at all depths, while GCN-GRU, TGCN, IGNN-GRU, and TIGNN all degrade due to over-smoothing. This provides direct, controlled evidence for the paper's central thesis — that an implicit architecture resolves the over-smoothing vs. long-range-dependency trade-off in the temporal setting.

- **Broad multi-task evaluation with competitive results.** IDGNN is evaluated on 7 datasets spanning classification (ROCAUC) and regression (MAPE) in both transductive and inductive settings, compared against 9 baselines. It achieves top-1 on 5 of 7 real-world benchmarks (Brain10, DBLP5, PeMS04, PeMS08, England-COVID transductive). The regression improvements on PeMS04/PeMS08 are described as "over 1%" MAPE reduction against the second-best method.

- **Bilevel training algorithm addresses a genuine computational bottleneck.** The paper correctly identifies that naive implicit-differentiation training for the coupled system has prohibitive $O(T^2 n d^4)$ per-iteration complexity (Section 4). The proposed single-loop algorithm (Algorithm 1) uses fixed-point updates for the lower-level and Hessian-vector products for the hypergradient, reducing complexity to $O(T n d^2 + T n^2 d)$ — this is a practically meaningful contribution for making dynamic implicit models trainable.

## Weaknesses

### Major

1. **The cyclic architecture (Z₁ depends on Z_T) creates a temporal causality problem that the paper never resolves for "general dynamic graphs."** The model's core design (Equation 2) is a cycle: embeddings at time 2 depend on time 1, ..., time T depends on time T−1, and **time 1 depends on time T**. The paper states it overcomes the fixed-point existence barrier "by first proving the existence of the fixed-point representations on periodic dynamic graphs and extending this result to design an implicit model for general dynamic graphs" (line 18). But no mechanism for this extension is ever described — the same cyclic architecture is applied directly to non-periodic benchmarks (traffic prediction, epidemiology) where a traffic model at time 1 should not depend on traffic at time T, nor COVID cases at week 1 on cases at week 52. The paper acknowledges "it does not naturally lend itself to inductive setting" (line 240) as a limitation, but the issue is more fundamental: the inductive bias embeds a circular time dependency that is physically incorrect for the non-periodic tasks on which the method is evaluated. The transductive results may benefit from the fixed-point blending information across all timestamps, but the paper frames the method as a general-purpose solution without explaining why the cyclic inductive bias is appropriate.

2. **The headline "up to 1600x speed-up" claim is unsubstantiated in the paper's body text.** This claim appears prominently in the abstract (line 4) and contribution list (line 21). However, Section 5.4 (line 233) begins discussing Brain10 with garbled text and immediately shifts to providing PeMS04/PeMS08 numbers: a speedup ratio of 0.72/0.29 = 2.48× and a theoretical ratio of (307/170)² = 3.26×. The 1600× figure is **never attached to a specific dataset, measurement protocol, or reproducible number in the readable text**. While an embedded image (Figure 3b) may contain this number, an extraordinary claim of this magnitude requires clear, quantified, text-based experimental demonstration. The only concrete speedup numbers the text provides are 2.48× and ~3.26×, making the abstract's 1600× claim appear misleading relative to what the body substantiates.

### Minor

3. **Baseline results for 4 of 7 datasets are taken from a single prior paper without protocol alignment verification.** Table 2's caption (line 207) states that baseline performances for Brain10, England-COVID, PeMS04, and PeMS08 are "taken from Gao & Ribeiro (2022)." The paper does not confirm that its train/validation/test splits, preprocessing, evaluation protocol, or number of runs match those of Gao & Ribeiro (2022). Given that the claimed improvement on PeMS04/PeMS08 is described as "over 1%" (line 205), protocol differences could materially affect whether these gains are genuine. Furthermore, for the remaining two classification datasets (DBLP5, Reddit4), the source of baseline numbers is not specified, creating an additional ambiguity.

4. **The bilevel optimization algorithm's theoretical grounding is imprecise.** The paper acknowledges that the lower-level problem $g(z,\omega) = \|z - \phi(z,\omega)\|^2$ is nonconvex in $z$ (line 159). It then asserts that fixed-point iteration is "akin to the effectiveness of gradient descent under strong convexity" (line 173) — an informal analogy, not a theoretical justification. The cited works (Hu et al., 2022; Qiu et al., 2022) assume the lower-level problem is strongly convex, which does not hold here. The algorithm may work well in practice (the experiments suggest it does), but the paper's attempt to borrow convergence guarantees from that literature is unsupported, and no formal convergence analysis for the nonconvex setting is provided.

5. **Missing reproducibility details.** The paper does not report: (a) how $\kappa$ (the contraction constraint strength) was chosen, (b) the number of fixed-point iterations used during training/inference for the bilevel method, (c) the number of random seeds/runs over which standard deviations are computed, (d) optimizer hyperparameters and learning rate schedules, or (e) model parameter counts for fair complexity comparison. These omissions hinder reproducibility assessment.

### Trivial

6. Minor garbled text and formatting issues in Section 5.4 (line 233) obscure the efficiency results for Brain10 — the specific runtime numbers for that dataset are not readable in the extracted text.

7. The paper states it uses "6 real-world datasets and one toy dataset" in the conclusion (line 240), but earlier text (line 184) mentions "three node classification datasets and four node regression datasets" — this is 7 real-world datasets, not 6.

## Nice-to-Haves

- An acyclic variant of the architecture (e.g., where Z_T does not feed into Z₁, with a corresponding well-posedness analysis) would substantially strengthen the paper's applicability to causal dynamic settings.
- A convergence analysis for the bilevel algorithm under the given contraction condition — even a linear rate — would replace the informal "akin to strong convexity" analogy with rigorous support.
- An ablation study on the effect of $\kappa$ (the contraction strength) on both convergence and final performance.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Algorithm 1 is unreadable/presented in garbled pseudo-code"** — Removed as a formatting artifact from PDF extraction. The original submission is not affected by this.
- **"The 'ablation study' promised refers only to runtime comparison"** — Removed because the contribution list explicitly says "ablation study to show that our proposed optimization algorithm is faster" (line 21), so this is exactly what was promised.
- **"Missing related works"** — Removed per instruction (cannot verify existence of missing citations).
- **"Missing appendix/proofs"** — Removed as the parser strips appendices from all papers.
- **"Nitpicks about typos, grammar, capitalization"** — Removed as formatting artifacts.
- Several generic weaknesses (e.g., "evaluation lacks rigor," "could the metric be measuring a proxy") from the harsh critic that lack specific anchors in the paper — removed.
- Strength Finder's strengths about "comprehensive multi-task evaluation" and the problem being "important/genuinely open" — partially retained but the generic framing was dropped. Specific claims with evidence were kept.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Either justify the cyclic architecture or scope the paper honestly.** The paper should either (a) provide a mechanism for extending from periodic to general dynamic graphs, or (b) clearly scope IDGNN as a model for cyclic/periodic dynamic graphs and provide an acyclic variant (or discuss when the cyclic assumption is reasonable). This is the paper's deepest conceptual issue.

2. **Anchor the 1600× claim in the body text.** Provide the actual Brain10 runtime numbers (in seconds or milliseconds for both methods) in the main text, not just in an image. Include the dataset name, configuration, and measurement protocol. Consider also reporting speedups for all datasets, not just the largest.

3. **Verify or replace the Gao & Ribeiro (2022) baseline numbers.** Run the baseline methods under the paper's own evaluation protocol (or explicitly confirm protocol equivalence) and state the number of random seeds used for all methods. Clarify the source of DBLP5/Reddit4 baseline numbers.

4. **Add key reproducibility details:** number of runs/seeds, value of $\kappa$, number of fixed-point iterations used, optimizer settings, and model parameter counts in a table.

## Score and Decision

The paper tackles a genuine open problem (extending implicit GNNs to dynamic graphs) with an interesting architectural idea and practically motivated training algorithm. The empirical results are competitive on most benchmarks. However, the cyclic architecture creates an unresolved temporal causality issue for the non-periodic tasks on which the method is evaluated, and the headline efficiency claim ("up to 1600x") is not substantiated in the body text — the only legible numbers are 2.48× and 3.26×. The combination of an overclaimed scope and an unsubstantiated flagship claim undermines trust. The core idea is salvageable, but the present version does not meet the evidentiary standard for a top venue.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>