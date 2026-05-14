Now I have enough context to write the final review and calibrate my score.

## Summary

The paper introduces Distributed Neural Architectures (DNAs), a new paradigm where each token independently routes through a collection of computational modules via learned routers — departing from fixed feedforward structures. The authors train DNA models in vision (ImageNet, ViT-small scale) and language (FineWeb-Edu, GPT-2 medium scale), showing they are trainable and achieve results close to dense baselines. The key contribution is the demonstration of emergent, interpretable routing patterns: low-rank paths capture generic features while high-rank paths capture specific concepts, and the model allocates compute differently based on input complexity. The paper is exploratory rather than state-of-the-art, honestly discussing its limitations while presenting a genuinely novel architectural direction.

## Strengths

- **Genuinely novel architectural paradigm.** The idea of distributed routing where each token traverses a learned sequence of modules — subsuming MoE, MoD, layer-skip, early exit, and weight sharing as special cases — is conceptually fresh and well-motivated. The formalization in Eq. 1-3 provides a concrete, extensible design that future work can build on.

- **Emergent path specialization is well-documented qualitatively.** The analysis of low-rank vs. high-rank paths (Figures 3, 8) reveals genuinely interesting structure: frequent paths aggregate patches sharing high-level features (edges, flat color), while rare paths capture specific concepts (brass instruments, puzzle pieces). The observation that this structure arises from end-to-end training without explicit regularization is a meaningful empirical finding. Similarly, the power-law path distribution (Figure 1c,d), persisting even in random models, is a curious and worth-reporting phenomenon.

- **Learned compute allocation correlates with input complexity in an interpretable way.** The vision DNA model allocates more compute to boundary-rich images and less to simple-background images (Figure 5). In language, low-compute documents are qualitatively distinct (HTML, bibliography, non-Latin scripts). This provides supporting evidence that the learned skipping is not random.

- **Honest framing of limitations.** The paper explicitly notes it operates in a "vastly underparametrized regime," does not use load balancing by design, and states it is "not focused on beating SOTA" but on showing feasibility. This transparency is commendable and the reader can trust the claims that are made.

## Weaknesses

### Fatal

None.

### Major

- **The central "competitive" claim is not fully supported by the data.** The paper claims DNAs are "competitive with dense baselines," but the evidence is mixed. In vision, Top-1 DNA (79.1%) is 0.7% below ViT-small (79.8%) and Top-2 DNA (78.8%) is 1.0% below — gaps that are non-trivial on ImageNet. In language, Top-1 DNA (406M active params) is *worse* than GPT-2 (406M) on every metric except BoolQ. Top-2 DNA (433M active params, 7% more than GPT-2's 406M) beats GPT-2 on 5/7 metrics, but it is unclear how much of this comes from the architecture vs. the extra parameters. The "30% skip" variants, which are the paper's main compute-efficiency claim, show catastrophic degradation (LAMBADA: 33.8→23.8, HellaSwag: 40.5→35.5). The paper's headline framing as "competitive" is defensible only if interpreted generously as "close enough to be worth further study" — but the data more accurately supports "slightly worse at equal compute, with meaningful quality loss under compute-saving regimes."

- **The compute efficiency comparison is not properly controlled.** The paper compares top-2 DNA (30% skip) against "GPT-2 (30% shallower)" — a model with 30% fewer layers. A shallower GPT-2 is not the same kind of compute-saving mechanism as learned per-token skipping, and this does not control for total parameter count or FLOPs per token. The proper control would be a top-2 DNA *without* skip vs. a top-2 DNA *with* skip, at matched total compute budgets, to isolate whether the learned skipping is intelligently allocating compute rather than just reducing effective capacity. Without this, the paper cannot distinguish intelligent allocation from simple underperformance.

- **The interpretability analysis is primarily qualitative and lacks rigorous quantification.** The path specialization analysis (Figures 3, 8) is compelling but cherry-picked. The paper acknowledges that a randomly initialized DNA also clusters images, but dismisses this by claiming it uses a "very different similarity measure" without quantifying the difference (referencing an appendix removed by the parser). The claim that high-rank paths carry "context-specific information" is presented as speculation ("we hypothesize") without supporting evidence. The deep-dream reconstruction visualizations (Figure 4) produce images the model misclassifies (e.g., "papillon" instead of "Welsh springer spaniel"), and the defense that "all top 5 guesses are birds and dog breeds correspondingly" shows hierarchical label structure rather than anything specific about DNA routing. Standard interpretability baselines (e.g., probing, attention rollout) would have strengthened the analysis.

- **No statistical significance or variance reporting.** All experiments are single runs (no seeds reported for the main results). The language benchmark differences between GPT-2 and Top-2 DNA are small (e.g., 59.2 vs. 58.9 on ARC-E, 34.0 vs. 33.8 on LAMBADA). Without confidence intervals or multiple seeds, it is impossible to tell if these differences are meaningful.

### Minor

- **The language models are severely undertrained (21B tokens).** The paper acknowledges this ("vastly underparametrized regime"), which honestly qualifies the results but also means the observed language effects could be artifacts of severe underfitting. The interesting routing structure might not persist at scale.

- **Missing control: random routing.** The paper does not ablate whether learned routing matters vs. random routing (with the same module collection). This would directly test whether the learned routing decisions drive the results or whether the inductive bias of the module collection alone suffices.

- **The "unifying framework" claim is asserted but not demonstrated.** The paper claims DNAs "generalize" MoE, MoD, parameter sharing, etc., but never formally shows how these methods are special cases. This is a framing claim that is plausible but unsupported.

### Trivial

- The routing equation (1) motivation ("not overcounting skip connections") could be clearer, though the paper does footnote an explanation.

## Nice-to-Haves

- **Statistical significance tests or multiple-seed experiments** on the core comparisons would substantially strengthen the paper.
- **A controlled experiment** comparing a top-2 DNA with skip against a top-2 DNA without skip at matched total compute, to demonstrate intelligent compute allocation.
- **Quantifying the "very different similarity measure"** between trained and random DNA routing, rather than deferring to an appendix.
- Training at larger token budgets (100B+) for language to see if the gap to dense baselines closes.
- Including standard interpretability methods (probing, attention rollout) alongside the deep-dream reconstruction.

## Removed Points

These points were raised by reviewers but are either factually wrong, strawman, or violate the exclusion rules. They are listed here for completeness but should not weigh in evaluation.

- **Criticism that the paper does not show formal proof that DNAs subsume MoE/MoD/etc.** (Harsh Critic, Section 1). The paper claims "natural generalization" and sketches the relationship; formal proofs are not standard for a paper of this type. This is more of an embellishment claim than a core weakness. → Move to Removed.
- **Criticism that the routing equation (1) is "awkward" and the paper does not analyze whether alternatives were tried** (Harsh Critic, 2.2). The paper provides a clear motivation (not overcounting skip connections). The reviewer's demand for an analysis of abandoned alternatives is unreasonable. → Remove.
- **"Standard interpretability methods (e.g., attention rollout, integrated gradients, or probing) would be more informative"** (Harsh Critic, 3.2). This is a methodological preference, not a weakness. The deep-dream approach is a legitimate choice for this specific analysis. → Move to Nice-to-Have.
- **The claim that the paper should use different benchmarks or datasets** (implied in various places). The paper's scope (ImageNet, FineWeb-Edu) is appropriate for a feasibility study. → Remove as scope creep.
- **Strength Finder's claim about the "framework unifying multiple conditional-computation methods" being a core strength.** This is somewhat generic — the paper claims it but doesn't prove it formally. Weakened to Minor weakness territory instead.

## Novel Insights

The most interesting observation across the reviews is that the paper's core tension — between pioneering a genuinely new architectural paradigm and failing to deliver competitive performance — is actually the paper's honest signal. The reviewers correctly identify that the paper would be stronger if it restructured its narrative around the emergent structure findings rather than framing as a competitive alternative. The power-law path distribution appearing even in random models (noted by both the paper and reviewers) is a genuinely surprising finding that suggests properties of the routing mechanism itself rather than learned content — this is an insight worth deepening in future work. Similarly, the observation that vision and language DNAs exhibit different parameter-sharing behavior (language reuse appears "most likely random") is a useful negative result that hints at domain-specific architectural requirements.

## Suggestions

1. **Reorganize the paper's narrative.** De-emphasize the "competitive" framing and lead with the emergent structure and interpretability findings — these are the paper's strongest contributions. The feasibility claim ("DNAs can be trained") can be stated plainly without the competitive framing.

2. **Add the random-routing ablation.** Training a DNA with untrained (random) routers for the same number of steps would cleanly establish whether learned routing matters, directly addressing the most obvious question about the paper's mechanism.

3. **Report multiple seeds** or provide confidence intervals for the key comparisons (Table 3). This is essential given the small performance differences.

4. **Run the controlled compute-efficiency experiment:** top-2 DNA (no skip) vs. top-2 DNA (with skip), controlling for total FLOPs per token, to isolate whether the model learns intelligent compute allocation.

## Score and Decision

**Calibration anchor comparison:**

| Anchor Paper | Avg Score | Comparison |
|---|---|---|
| Coupling Experts & Routers (Oral) | 6.67 | More thorough experiments, cleaner results. DNA has higher conceptual novelty but weaker empirical support. |
| DiSRouter (Poster) | 5.50 | Similar routing theme. Comparable novelty. DNA is more architecturally ambitious but DiSRouter has cleaner experiments. DNA is slightly weaker. |
| Dr.LLM (Poster) | 5.00 | Dynamic layer routing. Similar contribution type. Dr.LLM shows accuracy *improvements* while DNA shows degradation. DNA is weaker empirically. |
| Cross-layer MoE Routing (Poster) | 5.00 | MoE interpretability with rigorous analysis. DNA has stronger architectural novelty but weaker analysis. Comparable overall quality. |
| Token-Complexity MoE (Reject) | 3.50 | DNA is clearly stronger — better method description, more interesting results, honest limitations. |
| Automated Architecture Synthesis (Reject) | 3.00 | Similar theme (emergent connectivity). DNA has more concrete experiments at realistic scale. DNA is clearly better. |
| Model Editing is Over (Reject) | 3.00 | Different type of paper. Not directly comparable. |

**Overall assessment:** This paper introduces a genuinely novel architectural paradigm with interesting emergent properties. The qualitative analysis reveals genuine structure, and the paper is honestly written about its limitations. However, the empirical evidence does not fully support the central "competitive" claim — the models are slightly worse at matched compute and substantially worse under compute-saving regimes. The interpretability analysis is compelling but qualitative. The paper sits at the borderline between accept and reject: its novelty and interesting findings warrant publication in a venue that values exploratory ideas, but the gap between claims and evidence is significant enough that a strong reject is also defensible. I judge it as a weak accept — the idea is worth sharing with the community, with the understanding that much more work is needed to make DNAs practically competitive.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>