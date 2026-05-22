Now I have a good calibration picture. Let me write the review.

**Round-1 bracket:** Based on the round-1 calibration search, the weak band (<3.5) papers are about unrelated topics and are clearly reject-level. The middle band (3.5-7.5) contains papers like "State Chrono Representation" (4.75, Reject) and "Episodic Novelty Through Temporal Distance" (6.75, Accept) — both temporally-aware representation learning papers. The strong band (>7.5) papers are high-scoring but on dissimilar topics. My initial bracket is: **4.5–6.5**.

**Round-2 narrowing:** Looking at "State Chrono" (4.75, Reject) — its weaknesses include ad-hoc losses and unconvincing results. Our paper has cleaner, more principled losses and stronger quantitative evidence, so it's clearly better. "Episodic Novelty Through Temporal Distance" (6.75, Accept) is a temporally-aware contrastive method with extensive experiments and was accepted despite some concerns. Our paper has a similarly clean formulation and strong empirical grounding, but has the quasimetric-specification gap. Comparing against these anchors, I place the paper between them, closer to the 6.0 range.

---

## Summary

This paper proposes MadDist and TDMadDist, two self-supervised algorithms for learning the Minimum Action Distance (MAD) — the minimum number of actions needed to transition between states — from state-only trajectory data, without requiring rewards or actions. The key innovations are (1) a scale-invariant loss that prevents long-path pairs from dominating the objective, (2) the use of quasimetric embeddings (asymmetric distance functions) that can capture directional structure in environments with irreversible dynamics, and (3) a simple new quasimetric (d_simple). The paper also introduces a benchmark suite of environments with known ground-truth MAD, enabling systematic quantitative evaluation. Empirical results show that MadDist achieves higher correlation and lower ratio CV than QRL and Hilbert baselines across several environments, and attains near-perfect downstream planning success rates.

## Strengths

- **Strong, well-grounded empirical evaluation.** The paper evaluates MAD approximation accuracy using three complementary metrics (Spearman, Pearson, Ratio CV) across a diverse suite of environments with known ground-truth MAD — from grid worlds to continuous mazes, with both deterministic and stochastic dynamics. The presence of ground-truth MAD is a significant advantage over prior work and enables rigorous quantitative assessment. Figure 3 shows MadDist consistently achieving higher Pearson correlation (~0.9) and lower Ratio CV (~0.1–0.2) than baselines across KeyDoorGridWorld, CliffWalking, and OGBench PM Giant Navigate.

- **Clear downstream planning benefit.** Table 1 demonstrates that MadDist's learned distance translates to near-perfect success rates on OGBench PointMaze planning tasks (1.00±0.00 on 4 of 6 environments, 0.93–0.99 on the other two), decisively outperforming QRL, TDMadDist, and Hilbert. This shows practical utility beyond correlation metrics.

- **Principled loss design.** The scale-invariant loss (Equation 5: (d_θ/(j−i) − 1)²) is a clean technical improvement that prevents long-horizon pairs from dominating the gradient. The combination of path supervision (ℒ_o), contrastive separation (ℒ_r), and upper-bound constraints (ℒ_c) is well-motivated and each component serves a clear purpose.

- **Well-posed problem framing.** The paper clearly defines MAD (Equation 1) as the solution to a constrained optimization problem, connecting it to all-pairs shortest paths on the transition graph. This provides a solid foundation for the learning objectives.

## Weaknesses

### Fatal
None.

### Major
- **The quasimetric used in the main experiments (Figure 3, Table 1) is not specified.** The paper introduces three quasimetrics (d_simple, Wide Norm, IQE) and states that both algorithms "support any quasimetric formulation" (Section 6). However, the core experimental results never disclose which one was actually used for MadDist and TDMadDist. This is a structural omission: the paper claims in the introduction that d_simple "outperforms more elaborate quasimetrics in the existing literature," but without knowing which quasimetric generated Figure 3 and Table 1, the reader cannot evaluate this claim. If the results used IQE (the same as QRL), the advantage comes from the learning algorithm alone and the d_simple novelty is untested in the main paper. If they used d_simple, this must be stated and ideally accompanied by a direct head-to-head comparison in the main text rather than only in the (stripped) Appendix E. This gap undermines one of the three claimed contributions.

### Minor
- **The planning success rates of 1.00±0.00 across 4 of 6 environments raise a question about task difficulty.** While this could reflect genuinely excellent distance learning, the main text provides very little detail about the planning procedure ("Appendix H") — how the learned distance is used (as a heuristic for search? as a reward signal?), what algorithm converts distances into action sequences, and whether the perfect scores across all seeds indicate that the planning task may be somewhat coarse-grained as a discriminator once distances are reasonably accurate. The cross-environment variance (e.g., PM Giant Navigate: 0.93±0.17 vs. PM Large Navigate: 1.00±0.00) suggests the metric may saturate, which warrants discussion.

- **The claim that d_simple outperforms "more elaborate quasimetrics" is asserted in the introduction but only supported in a stripped appendix.** While an ablation in Appendix E (presumably) addresses this, the claim's prominence in the framing requires at least a summary comparison or a reference to a table in the main text showing d_simple vs. Wide Norm vs. IQE under otherwise identical conditions.

### Trivial
- None.

## Nice-to-Haves

- **Add a symmetric-Euclidean baseline with the same loss function.** Comparing MadDist against a version that replaces the quasimetric with Euclidean distance (while keeping the scale-invariant loss and trajectory supervision) would cleanly isolate the benefit of asymmetry from the benefit of the loss design. The Hilbert baseline is conceptually related but uses a different loss and training procedure, so the comparison is not apples-to-apples.
- **Add runtime comparisons.** The paper claims d_simple is "computationally efficient" but provides no wall-clock or per-step runtime comparison against Wide Norm or IQE.
- **Include standard deviations or confidence bands in Figure 3** instead of min-max shading, to give a clearer picture of result variability. The paper uses 3 seeds for Figure 3 and 5 seeds for Table 1 — harmonizing this would be cleaner.

## Removed Points

- **Garbled Equation (9) concern.** The harsh critic flagged Equation (9) as "syntactically nonsensical" and "unrecoverable." Examination confirms the parsed text (`(d_θ(s_i, s_{i+1} + d_{θ'}(s_{i+1}, s_r) - 12(9)))^2`) is a parser artifact from PDF extraction. The surrounding text clearly describes the intended objective: making d_θ(s_i, s_r) equal to 1 + d_{θ'}(s_{i+1}, s_r). Per the filtering rules, parser artifacts are not paper errors and are removed.

- **"Determination" terminology concern.** The critic notes the term "determination" is used without definition. The paper properly cites (Yoon et al., 2007), so this is a standard term-of-art with a reference. Removed.

- **Overstated literature gap.** The critic claims the paper overstates that "existing methods rely on symmetric approximations" since Wang et al. (2023b) already uses quasimetrics. However, the paper explicitly acknowledges Wang et al. (2023b) in the same paragraph (Section 2, lines 100–102), and the phrasing "many rely on symmetric approximations" (emphasis on *many*, not *all*) is accurate. Removed.

- **Missing baseline: Steccanella & Jonsson (2022).** The paper already cites this work as the closest prior symmetric MAD-learning method. Adding a direct experimental comparison would be informative but is not required, and the filtering rules caution against demanding non-standard baselines.

- **Speculative claim about zero-variance planning results being "suspicious."** The 1.00±0.00 results could be genuine — the method demonstrably works well — and without counter-evidence, labeling them "suspicious" is speculation. Demoted to a Minor concern about task discrimination rather than a fundamental validity threat.

## Novel Insights

The harsh critic's most incisive observation is about the quasimetric-specification gap: the paper presents three quasimetrics, claims superiority for one (d_simple), but never tells the reader which was used for the main results. This is a genuinely useful catch that goes beyond a presentation nitpick — it affects how the paper's contributions should be interpreted. The strength finder usefully highlights that the scale-invariant loss (Equation 5) is a technically clean contribution that deserves emphasis regardless of the quasimetric debate. The combination of these two perspectives yields a clear picture: the paper's strongest and best-supported contribution is the MadDist algorithm with its well-designed loss; the d_simple claim requires better evidentiary support in the main text to be evaluated on equal footing.

## Suggestions

- In the main experiments section, explicitly state which quasimetric was used for MadDist and TDMadDist (e.g., "For all main experiments, we use d_simple as the quasimetric, with α = 0.5; see Appendix E for a comparison across quasimetrics"). If space permits, include a small table or paragraph in the main text comparing d_simple, Wide Norm, and IQE.
- Add a brief discussion of the planning procedure in the main text (rather than only in the appendix), explaining how the learned distance is deployed and why the perfect success rates arise.
- Add a sentence acknowledging that the planning score may saturate (multiple environments hit 1.00) and discuss whether the more challenging Giant Navigate (0.93±0.17) is a better discriminator.

## Score and Decision

**Calibration anchors consulted:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| FjifPJV2Ol (Solving Schrodinger Bridge) | 3.40 | R1-weak | Unrelated topic; clearly weaker paper |
| 5AbtYdHlr3 (Stochastic Safe Action Learning) | 3.00 | R1-weak | Unrelated topic |
| oEzY6fRUMH (State Chrono Representation) | 4.75 | R1-mid + R2 | Similar topic (temporal state representation in RL); this paper has cleaner formulation and stronger empirical grounding — **MAD paper is better** |
| I7DeajDEx7 (Episodic Novelty Through Temporal Distance) | 6.75 | R1-mid + R2 | Similar topic (temporal distance via contrastive learning); well-executed with extensive experiments. MAD paper has comparable methodological quality but a presentation gap (quasimetric unspecified) — **MAD paper is slightly weaker** |
| skGSOcrIj7 (Neural Spacetimes for DAG Repr.) | 6.80 | R2 | Related (quasimetric embeddings) but different domain; stronger theory but similar evaluation depth — **comparable** |
| x7Q0uFTH2a (Weak Bisimulation Metric) | 3.75 | R1-mid | Lower-quality paper on a related topic — **MAD paper is better** |

**Final score rationale:** The paper makes genuine contributions — a well-designed scale-invariant loss for MAD learning, the first systematic benchmark suite with ground-truth MAD, and strong empirical results showing clear improvements over QRL and Hilbert. The main weakness is the failure to specify which quasimetric generated the primary results, which directly affects the ability to evaluate the d_simple claim. This is a fixable presentation gap rather than a fatal flaw. Compared against the round-2 anchors, the paper is clearly stronger than the 4.75 anchor (State Chrono) but slightly weaker than the 6.75 anchor (Episodic Novelty) due to this omission, placing it at 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>