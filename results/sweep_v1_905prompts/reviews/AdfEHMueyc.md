## Summary

This paper proposes a co-design algorithm for soft robots that uses Graph Attention Networks (GATs) as the policy representation, enabling principled weight inheritance across morphological mutations. The key idea is that modeling each robot as a graph (nodes = position sensors, edges = spatial adjacency) allows a GAT-based controller to handle varying numbers of sensors and actuators naturally, while the MAPWEIGHTS procedure (Algorithm 2) transfers learned parameters from parent to offspring in a topology-consistent way. Experiments on four EvoGym tasks show that GAT-based methods (with global or local feature transfer) consistently match or exceed MLP-based baselines in peak fitness and variance.

---

## Strengths

- **GAT-based policy with principled inheritance for variable morphologies**: The paper identifies a genuine bottleneck in soft-robot co-design — MLP controllers break when sensor/actuator layouts change — and proposes a clean solution. The MAPWEIGHTS algorithm (Algorithm 2) provides a well-defined procedure for copying shared GAT/message-passing layers intact, matching existing actuator outputs, randomly initializing new ones, and discarding removed ones. This is concretely described and directly addresses the fixed-dimension limitation of MLPs.

- **Consistent empirical advantage over MLP baselines across four tasks**: Figure 3 shows that both GAT variants (global and local transfer) match or outperform GA-MLP-PPO and GA-MLP-PPO-Transfer on Pusher-v1, Thrower-v0, Carrier-v1, and Catcher-v0, with notably lower variance on Catcher-v0. The gap is substantial on Thrower-v0 (~6.2 vs ~3.3 fitness) where GAT methods develop a two-actuator throwing motion that MLP methods do not discover (Section 5.2, Figure 4). This behavioral evidence strengthens the claim that graph-structured policies enable qualitatively different solutions.

- **Ablation of local vs. global feature construction within GATs**: Comparing global mean features (shared across all nodes) vs. localized node features reveals task-dependent preferences — local features excel on Pusher, Thrower, and Carrier (fine-grained coordination), while global features work better on Catcher (whole-body synchronization). This is a meaningful design insight, not just a checkmark comparison.

- **Standardized evaluation on EvoGym with published baselines**: Experiments use the established EvoGym benchmark with hyperparameters from Harada & Iba (2024), enabling direct comparison with both no-transfer (Bhatia et al., 2021) and Lamarckian-transfer (Harada & Iba, 2024) baselines.

---

## Weaknesses

### Major

1. **Missing GAT-without-inheritance ablation, despite claiming "ablations isolating the effects of graph policies and inheritance."** The paper compares GAT+Transfer vs. MLP+Transfer vs. MLP-no-Transfer, but never evaluates a GAT *without* inheritance (i.e., training each offspring's GAT from scratch). Without this condition, we cannot tell how much of the GAT advantage comes from the graph architecture vs. the inheritance mechanism. The MLP no-transfer baseline is not a fair proxy because MLPs and GATs have different capacities, parameter counts, and convergence speeds. The contribution list on page 2 explicitly promises "ablations isolating the effects of graph policies and inheritance," but no such ablation for the GAT is performed.

2. **Insufficient statistical evidence for fine-grained claims.** All results are based on 3 independent runs with no significance tests. This is especially consequential for the local-vs.-global analysis (Section 5.1): the claim that local features are better for "part-level coordination" and global features for "whole-body coordination" rests on small differences that may not be robust (e.g., on Thrower-v0 the two GAT variants are close; on Carrier-v1 all methods saturate). With only 3 runs and overlapping error bars, these distinctions are not convincingly supported.

3. **Critical method details are underspecified, harming reproducibility.** The graph construction is described only in general terms: nodes "combine global properties (e.g., orientation) with local information (e.g., coordinates, voxel type, and velocity)" — no exact feature vector is listed. Edge connectivity is "spatial adjacency" among vertices, but what adjacency threshold or criterion is used? The paper also does not describe how the MLP inheritance baseline (GA-MLP-PPO-Transfer) handles dimension mismatches when morphology changes — a crucial detail for fair comparison, since the paper's argument is that MLP inheritance is fragile. The MLP baseline is simply cited to Harada & Iba (2024) without even a summary of its weight-mapping strategy.

### Minor

1. **Task description inconsistency in Section 5.2.** The paper's own Section 4 correctly describes Thrower-v0 as "The robot must throw a box that is initially positioned on top of it." But Section 5.2 states the task is to "catch a falling box and throw it as far as possible." This is a clear textual error (the Catcher-v0 task involves catching falling objects, not Thrower-v0). While this is likely just a description mistake rather than an evaluation error (the environment is the standard EvoGym), it erodes the reader's confidence and must be corrected.

2. **Algorithm 1 contains a pseudocode bug.** The algorithm requires "population size p, max generations n," but the outer loop is written as "for g = 1 … p do" instead of "for g = 1 … n do." This is a minor bug — the intention is clear — but it suggests insufficient proofreading of a central algorithmic description.

3. **Local-vs.-global interpretation is overclaimed relative to evidence.** The paper asserts that "local attention excels in tasks dominated by detailed part-level interactions, while global attention is more effective for behaviors requiring whole-body coordination." With 3 runs, no significance testing, and tasks where the two variants are nearly tied (Thrower-v0, Carrier-v1), this reads more as a post-hoc story than a robust finding. The evidence supports that both GAT variants beat MLPs; it does not strongly support the finer-grained architectural comparison.

### Trivial

- Algorithm 1 line 2 uses `p` instead of `n` for the generation loop counter.
- The exact dimensionality of node features and edge features is not reported (minor for reproducibility).
- Training time / computational cost of GAT vs. MLP is not discussed.

---

## Nice-to-Haves

- A GAT variant trained from scratch each generation (no inheritance) would cleanly isolate architecture vs. inheritance effects.
- Reporting statistical significance (e.g., Mann-Whitney U or confidence intervals) on the 3-run data would strengthen the local-vs.-global conclusions.
- A brief description of how the MLP baseline handles dimension mismatches during inheritance (even just summarizing Harada & Iba's approach) would make the comparison more transparent.
- Reporting wall-clock time or parameter counts would help calibrate the GAT vs. MLP trade-off.

---

## Removed Points

These points were raised by reviewers but are removed for the reasons stated:

- **"NerveNet (Wang et al., 2018) is a missing related work"** — The paper explicitly discusses NerveNet in Section 6.2: "NerveNet learns policies on graphs of body parts Wang et al. (2018)." The critic's claim is factually wrong.
- **"The MLP inheritance baseline's lack of description is a fairness concern that could bias the comparison"** — This is partially valid (see Weaknesses Major #3), but the harsh critic overstated it as a "methodological gap that undermines comparison fairness." The baseline is a published method (Harada & Iba 2024, GECCO); readers can look it up. The concern is real but minor, not structural.
- **"Section 5.2 task error 'casts doubt on the entire evaluation'"** — The textual error in Section 5.2 is real (see Minor #1) but it is a description mistake, not evidence that the evaluation was run incorrectly. The EvoGym environment is standardized; the paper uses the standard environment. The critic inflated this into a "structural problem."
- **"GCN-without-attention ablation" and "sensitivity analysis on hyperparameters"** — These are speculative nice-to-haves, not weaknesses. The paper's scope is to introduce the GAT+inheritance method, not to exhaustively ablate every design choice.
- **"Pure formatting/style nitpicks" and "missing appendix content"** — Removed per hard rules.
- **Generic strengths about the importance of the problem** — Removed from strengths. Only concrete, paper-specific strengths are retained.

---

## Novel Insights

The paper's core insight — that graph-structured policies with attention can serve as a natural interface for Lamarckian controller inheritance in evolving morphologies — is genuinely useful. The observation that evolved morphologies converge to similar task-specific designs regardless of controller type (Section 5.3) while the controller architecture primarily affects learning speed and robustness is an interesting piece of evidence: it suggests that the task constrains morphology more than the policy class does, and that the GAT's advantage is in *how efficiently it gets there* rather than *where it ends up*. This decoupling deserves more analysis than the paper currently gives it.

---

## Suggestions

1. **Add a GAT-without-inheritance condition** to the comparison. This single ablation would resolve the main evidential gap and directly measure the benefit of MAPWEIGHTS for GAT controllers.
2. **Either increase runs to 10+ or add statistical tests** (e.g., Mann-Whitney U comparing final-generation fitness distributions) to support the local-vs.-global analysis.
3. **Fix the task description in Section 5.2** and the Algorithm 1 pseudocode bug.
4. **Specify the exact feature dimensions and edge-construction criteria** for the graph representation (even briefly in the main text).
5. **Briefly describe how the MLP baseline handles dimension mismatches** during inheritance, to let readers assess comparison fairness without cross-referencing Harada & Iba.

---

## Score and Decision

### Round 1 Bracket

The initial bracketing pass placed the paper between the weak band (avg scores 2.5–3.4 — papers on crude evolutionary optimization with no embodied/co-design component) and the strong band (avg scores 7.5+ — well-executed geometry-aware RL, differentiable simulation). The plausible range was **4–6**.

### Round 2 Narrowing

The second pass retrieved anchors specifically on soft-robot co-design, morphology-behavior co-evolution, and EvoGym-based evaluation. The most informative comparisons:

| Anchor | Avg Score | Round | Comparison to this paper |
|--------|-----------|-------|-------------------------|
| Subequivariant Morphology-Behavior Co-Evolution (MueN6LyTmS) | 5.20 | R1/R2 | Rejected. Similar quality of core idea (injecting structure into co-evolution policies), similar evaluation gaps (limited baselines, no significance tests). This paper has a clearer methodological contribution (GAT + MAPWEIGHTS) but slightly weaker experiments. Comparable overall. |
| Differentiable Physics for Soft Robots (pUKJWr5zOE) | 5.00 | R2 | Rejected. More thorough experiments/ablation, but the ML contribution is less novel (existing components). Roughly comparable tier. |
| MeMo: Modular Controllers (VZTFUtldbC) | 4.75 | R2 | Rejected. Addresses a related modular-control problem. Reasonably characterized but smaller scale. Comparable quality. |
| Meta-Evolve (RthOl4jHw5) | 6.00 | R1 | **Accepted.** Cleaner evaluation (clearer problem statement, more runs, baselines). Clearly stronger than this paper. |
| HERD: Hyperbolic Embeddings (q9jQPA6zPK) | 6.50 | R2 | **Accepted.** Thorough evaluation on 15 tasks, clear novelty framing. Clearly stronger than this paper. |

This paper is most comparable to the Subequivariant (5.20) anchor and slightly above MeMo (4.75) and the Differentiable Physics paper (5.00). It is below Meta-Evolve (6.00) and HERD (6.50). The evaluation gaps (missing GAT ablation, 3 runs, underspecified method details) prevent it from reaching the acceptance tier, but the core contribution is well-motivated and worth developing.

### Final Score

**5.0** — A borderline paper with a solid core idea and clear motivation, but the evaluation has notable gaps that prevent acceptance in the current form. The missing GAT-without-inheritance ablation is the most consequential gap; the task description error and insufficient runs further weaken confidence. The paper has a clear path to improvement.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>