## Summary
# Final Review Report

## Summary

This paper investigates the relationship between two established phenomena in neural network training: (1) the early crystallization and stabilization of pruning masks, and (2) the early compression and stabilization of the top Hessian eigenspace. The authors propose a principled mathematical framework that casts both pruning masks and Hessian eigenvector matrices as elements of the same Stiefel manifold, enabling direct comparison via Grassmannian metrics. After systematically reviewing candidate metrics, they select the "overlap" measure for its favorable statistical and computational properties. Using a small MLP (7,030 parameters) trained on subsampled 16x16 MNIST, the authors demonstrate that the overlap between magnitude pruning mask subspaces and top Hessian eigenspaces is significantly above random chance throughout training, with the largest overlap at initialization.

The paper is well-written and addresses an interesting conceptual question at the intersection of pruning and optimization geometry. The mathematical development is sound and the Grassmannian metric analysis is thorough. However, the empirical validation is limited in several important ways that constrain the strength of the conclusions: single tiny model, no statistical uncertainty reporting, only one pruning criterion, and no direct validation of the claimed practical applications. The paper's main strengths are its clear conceptual framing and rigorous metric analysis; its main weaknesses are insufficient experimental scope and unsupported claims about practical utility.

## Strengths
**S1. Clear conceptual framing and research question.** The paper identifies a genuine and interesting gap in the literature: two independent lines of research (pruning mask stabilization and Hessian eigenspace compression) describe parallel phenomena, yet their relationship has not been systematically studied. The authors pose a well-defined research question and motivate it clearly.

**S2. Rigorous mathematical foundation.** The casting of pruning masks as orthogonal projection matrices on the Stiefel manifold is elegant and principled. The isomorphism (m, θ, H) → (̃m, ̃θ, ̃H) via permutation is mathematically sound, and the partitioning of the reordered Hessian in Eq. (2) meaningfully exposes the interaction between parameter subsets and the top eigenspace.

**S3. Thorough Grassmannian metric analysis.** Section 4 provides a comprehensive review of Grassmannian metrics and systematically evaluates them across synthetic data. The identification of "overlap" as the preferred metric is well-motivated by three criteria (informativeness, computational efficiency, and bijection to other metrics). Lemma A.1's analytical derivation of the expected overlap (k/D) under the null hypothesis is a nice theoretical contribution.

**S4. Transparent acknowledgment of experimental constraints.** The authors openly acknowledge the computational bottleneck of exact Hessian eigendecomposition (Page 7, lines 56-61), and they clearly state that they "do not prune but simply observe the potential pruning masks" (Page 8, lines 49-52), which is a principled design choice to avoid artificially boosting overlap.

**S5. Well-structured and well-written.** The paper is logically organized, the notation is consistent, and the mathematical exposition is generally clear. The figures effectively communicate the main empirical patterns.

## Weaknesses
**W1. Severely limited experimental scale (Must-fix).** The entire empirical evaluation relies on a single MLP with only 7,030 parameters trained on 16x16 subsampled MNIST. This is orders of magnitude smaller than typical modern networks. The Hessian structure of such a tiny model may not be representative of deeper networks with convolutional or attention mechanisms. The paper's central claim about a universal connection between pruning masks and Hessian eigenspaces cannot be reliably inferred from this single data point.

**W2. No statistical uncertainty quantification (Must-fix).** All overlap results (Figures 1, 4) are presented as single-trajectory curves without error bars, confidence intervals, or multiple-seed statistics. Given that the overlap values are modest (0.1–0.4 range), it is impossible to assess whether the observed patterns are statistically robust or driven by a particular random seed and initialization.

**W3. Unsupported practical claims (Must-fix).** Both the abstract and the introduction's final paragraph claim that the observed overlap "can be leveraged to approximate the typically intractable top Hessian subspace via parameter inspection, at only linear cost." No experiment validates this approximation claim. The paper only establishes correlation; it does not test whether pruning masks can actually *replace* Hessian computations in any practical sense.

**W4. Correlation vs. causation ambiguity.** The paper repeatedly uses language suggesting a structural/mechanistic relationship ("largest parameter magnitudes tend to coincide with the directions of largest loss curvature"), but the evidence only establishes that the subspaces overlap beyond random chance. Alternative explanations (common initialization effects, Hessian block-diagonal structure, random amplification during training) are not discussed or ruled out.

**W5. Only one pruning criterion tested.** The paper only examines magnitude-based pruning masks, which select the top-k parameters by absolute value. Other pruning criteria (gradient-based, Hessian-based, randomization-based, Lottery-Ticket-style iterative pruning) are not compared. The claimed connection may be specific to magnitude pruning rather than a general property of pruning masks.

**W6. Modest overlap magnitudes.** While statistically significant, the observed overlap values (approximately 0.1–0.4 on a [0,1] scale) indicate that the majority of the subspace structure is *not* shared between pruning masks and Hessian eigenspaces. The paper's narrative emphasizes "striking" similarity without contextualizing the magnitude.

**W7. No discussion of alternative explanations.** The paper does not consider or test alternative hypotheses for the observed overlap, such as: the Hessian's eigenvector coordinates are not uniformly distributed across parameters (some parameters intrinsically have larger Hessian entries), or the training dynamics cause both masks and Hessian eigenvectors to align with the same low-frequency signal components.

## Key Issues
**K1. Single-model experiment undermines generalizability (Rank 1, Severity: Major).**
The paper's core empirical claim rests on a single MLP with 7,030 parameters. This is about 0.03% the size of a ResNet-50 and trained on 16x16 MNIST. The Hessian literature shows that spectral properties change qualitatively with depth, width, and architecture (Ghorbani et al. 2019, cited by the paper itself). Without experiments on additional architectures (even a small CNN), readers cannot assess whether the overlap phenomenon is a general property of neural network training or an artifact of this specific setup.

**K2. No multi-seed or uncertainty reporting (Rank 2, Severity: Major).**
The overlap values reported in Figures 1 and 4 are single trajectories. Standard practice for training dynamics studies is to report mean ± std over at least 3-5 seeds with different initializations. Without this, the observed patterns (rank 1 in severity by validity risk) cannot be distinguished from noise or seed-specific idiosyncrasies.

**K3. Speculative utility claims without validation (Rank 3, Severity: Major).**
The abstract claims that the overlap "can be leveraged to approximate the typically intractable top Hessian subspace via parameter inspection, at only linear cost." This is an implied practical contribution that is never tested. If removed or downgraded to a future-work speculation, the paper's contribution becomes purely observational—which is acceptable but must be clearly positioned.

**K4. Causal language mismatch (Rank 4, Severity: Minor-Major).**
The conclusion states "suggesting that in DL large parameters tend to coincide with directions of high loss curvature." The evidence supports correlation, not inherent structural coincidence. The wording implies a mechanistic discovery that the experiments do not establish.

**K5. Single pruning criterion (Rank 5, Severity: Minor).**
Testing only magnitude pruning limits the paper's scope. The relationship between pruning masks and Hessian subspaces might differ for gradient-based pruning, Fisher pruning, or random pruning. This limits the generalizability of the claimed connection.

```text
ASCII Diagram — Paper Structure & Evidence Map
================================================

[Research Question: Do pruning masks and Hessian eigenspaces overlap?]
        |
        v
[Theoretical Framework (Strong)]
   - Masks as Stiefel elements
   - Grassmannian metrics
   - Analytical null-distribution (k/D)
        |
        v
[Empirical Validation (Weak)]
   - 1 MLP (7030 params)
   - 1 dataset (16x16 MNIST)
   - 1 pruning criterion (magnitude)
   - 1 seed (no statistics)
   - No practical validation
        |
        v
[Conclusion Gap]
   - Claims: "striking similarity", "practical Hessian approximation"
   - Evidence supports: moderate correlation (overlap 0.1-0.4), single setup
```

## Actionable Suggestions
**A1. Add at least one larger-scale experiment.** The most impactful revision is to include a second model. A small CNN (e.g., 2-3 convolutional layers + 2 fully-connected layers, ~500K parameters) on full 28x28 MNIST or CIFAR-10 would dramatically strengthen generalizability. If exact Hessian computation is infeasible for larger models, use randomized SVD (Halko et al. 2011) to approximate the top-k Hessian subspace.

**A2. Report multi-seed statistics.** Run the main overlap experiment (Section 5) with at least 3 random seeds (different weight initializations and data shuffles). Report mean overlap ± standard deviation in Figures 1 and 4. Add a statistical significance statement: "The overlap exceeds the random baseline k/D with p < 0.01 under a one-sided test."

**A3. Replace unsupported practical claims with bounded statements.** 
- **Abstract, Page 1 (lines 24-26):** Replace "can be leveraged to approximate the typically intractable top Hessian subspace via parameter inspection, at only linear cost" with "suggests a potential connection that could inform future Hessian approximation methods, though direct validation is needed."
- **Page 2 (lines 34-43):** Replace the three speculative utility points with language like "if the relationship is causal, it could enable... though this remains to be tested."

**A4. Add alternative explanations subsection.** In Section 5 or 6, add a brief paragraph discussing at least two alternative explanations for the observed overlap:
- **Initialization overlap:** At initialization, random parameters naturally have some structure, and Hessian eigenvectors at initialization are also random. The observed "largest at initialization" overlap may partly reflect this.
- **Hessian block structure:** The Hessian is approximately block-diagonal by layer; parameters within the same layer share curvature properties. The top-k magnitude parameters might cluster in layers with larger Hessian blocks, inflating overlap without per-parameter alignment.

**A5. Add a practical validation experiment (optional but recommended).** Use the pruning mask subspace as a proxy for the top Hessian subspace and measure: (a) how well it reconstructs the true top Hessian subspace (subspace distance), and (b) whether using the mask subspace for a downstream task (e.g., Hessian-based pruning) preserves performance. This directly tests the paper's most impactful claimed application.

**A6. Compare with at least one additional pruning criterion.** Add results for a random pruning baseline (randomly selecting k parameters) and, if feasible, a gradient-based pruning criterion. If the overlap is similar across criteria, the paper's contribution is about a general property; if different, the paper can claim magnitude-specific insights.

**Mentor Revised Version for Abstract (Page 1, lines 6-28):**
"Recent studies show that pruning masks and Hessian eigenspaces both emerge early during training and stabilize thereafter. Using Grassmannian metrics to compare these objects on a common Stiefel manifold, we find that their subspaces overlap significantly—above random chance—throughout training. The overlap is largest at initialization, then decays and stabilizes, offering a new perspective on early training dynamics. This correlation suggests a structural connection between parameter magnitudes and loss curvature, opening directions for future investigation of fast Hessian approximations."

## Storyline Options + Writing Outlines
### Current Storyline Assessment
The current narrative arc is: "Pruning masks stabilize early → Hessian eigenspaces stabilize early → They are connected via Grassmannian metrics → Here is the overlap evidence." This is logically coherent but has two weaknesses: (1) the gap/motivation is underemphasized until after the figure, and (2) the practical implications are overstated relative to the evidence.

### Recommended Storyline (Option A — Best)
**Narrative: "Correlation before causation: connecting two parallel phenomena in deep learning."**
- P1: Both pruning masks and Hessian eigenspaces undergo early crystallization. (Observation)
- P2: These two phenomena come from separate communities and have not been connected. (Gap)
- P3: We provide a framework to quantify their relationship and find significant overlap. (Solution + Key Finding)
- P4: This correlation invites mechanistic investigation but does not yet establish causality. (Caveat)
- P5: We contribute a mathematical framework, metric analysis, and empirical characterization. (Contributions)

### Abstract Outline (Complete)
**S1 (Problem + Domain):** "Recent studies have independently shown that both pruning masks and loss Hessian eigenspaces undergo early emergence and stabilization during neural network training."
**S2 (Gap):** "Despite this parallel behavior, their relationship has not been systematically characterized."
**S3 (Method):** "We cast magnitude pruning masks and top Hessian eigenvector matrices as elements of the same Stiefel manifold, enabling direct comparison via Grassmannian metrics."
**S4 (Key Result):** "Our analysis reveals that their spanned subspaces overlap significantly—well above random chance—throughout the full training trajectory, with overlap peaking at initialization."
**S5 (Bounded Implication):** "This correlation suggests a structural link between parameter magnitudes and loss curvature, providing a new perspective on early training dynamics and opening directions for future Hessian-efficient methods."

### Introduction Outline (Complete)
**Paragraph 1 — Parallel observations.** Open with the key parallel: pruning masks emerge and stabilize early [Frankle & Carbin 2019; You et al. 2020]; Hessian eigenspaces also crystallize early [Gur-Ari et al. 2018]. State that this parallel has not been examined.
**Paragraph 2 — What is missing in prior work.** The OBD framework [LeCun et al. 1989] connects individual parameters to curvature only at convergence. Hessian analyses typically study global or layer-level structure [Papyan 2020]. Neither line of work addresses the training-sensitive, parameter-subset-aware connection between masks and eigenspaces.
**Paragraph 3 — Our approach and contributions.** Provide a compact contribution list: (1) Stiefel manifold characterization, (2) systematic metric comparison, (3) empirical evidence of significant overlap. Introduce the overlap metric as the preferred choice.
**Paragraph 4 — Implications and caveats (moved from end of intro).** Briefly state potential implications (new perspective on early phase, possible bridge between first/second-order methods) with appropriate hedging. End with a clear statement that these are suggested directions, not validated results.

### Title Suggestion
Current: "What Apples Tell About Oranges: Connecting Pruning Masks and Hessian Eigenspaces"
Alternative: "Connecting Pruning Masks and Hessian Eigenspaces: A Grassmannian Perspective on Early Training Dynamics"
- The alternative is more descriptive and signals both the method (Grassmannian) and the scope (early training dynamics) while keeping the poetic title as a subtitle.

## Priority Revision Plan
### P0 (Must-fix, before resubmission)

| Priority | Issue | Action | Effort | Impact |
|----------|-------|--------|--------|--------|
| P0-A | Single model/scaling concern | Add small CNN experiment (~500K params) on MNIST or CIFAR-10 with randomized SVD Hessian approximation | 1-2 weeks | High - establishes generalizability |
| P0-B | No uncertainty quantification | Re-run main experiment with 5 seeds; report mean±std overlap | 3-5 days (compute) | High - establishes statistical reliability |
| P0-C | Unsupported practical claims (Abstract + Intro) | Replace with bounded, correlational language | 1 day | High - claims-evidence alignment |
| P0-D | Causal language in conclusion | Replace "coincide" with "show significant overlap" | 1 hour | High - scientific accuracy |

### P1 (Strongly recommended)

| Priority | Issue | Action | Effort | Impact |
|----------|-------|--------|--------|--------|
| P1-A | Single pruning criterion | Add random pruning baseline + one alternative (e.g., gradient-based) | 1 week | Medium - scope completeness |
| P1-B | Missing alternative explanations | Add 1-2 paragraphs discussing possible confounders (init effects, block structure) | 1-2 days | Medium - intellectual honesty |
| P1-C | Modest overlap magnitudes contextualization | Add quantitative interpretation: "overlap 0.2-0.4 means 60-80% mass unshared" | 1 day | Medium - balanced narrative |

### P2 (Quality improvements)

| Priority | Issue | Action | Effort | Impact |
|----------|-------|--------|--------|--------|
| P2-A | Introduction narrative flow | Restructure to move gap statement before contributions list | 1 day | Medium - readability |
| P2-B | Contribution 2 framing | Reframe as methodological enabler rather than standalone contribution | 1 day | Low-Medium - positioning |
| P2-C | Title refinement | Consider more descriptive subtitle | 1 day | Low - discoverability |

```text
ASCII Diagram — Revision Strategy Roadmap
===========================================

[Current Submission]
        |
        v
[P0 Revisions (Must-fix)]
   ├── Add larger model experiment (generalizability)
   ├── Add multi-seed statistics (reliability)
   ├── Downgrade practical claims (honesty)
   └── Fix causal language (accuracy)
        |
        v
[P1 Revisions (Strongly recommended)]
   ├── Add alternative pruning criteria
   ├── Discuss alternative explanations
   └── Contextualize overlap magnitudes
        |
        v
[P2 Revisions (Polish)]
   ├── Restructure introduction narrative
   ├── Reframe Contribution 2
   └── Refine title
        |
        v
[Revised Submission]
   Stronger: multi-model, multi-seed, bounded claims
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|-----------|-------|---------|--------------|-----------------|-------------------|
| E1 | Synthetic metric comparison (Section 4.2) | Random matrices from O(D,k) and B(D,k) with varying D and r=k/D | dist_g, dist_c, dist_p, dist_a, overlap | Overlap is proportional, informative, and E[overlap]=k/D analytically | C2 (metric analysis) | Only empirical baselines for non-overlap metrics; no analytical E[dist] |
| E2 | Overlap during training (Section 5, Figures 1, 4) | MLP 7030 params, 16x16 MNIST, SGD lr=0.3, 50 epochs, steps t∈{0,5,...,2000} | Overlap, dist_g, dist_c,2, dist_c,F, dist_p,2, dist_p,F, dist_a | Overlap above random baseline; largest at init, then decays and stabilizes | C3 (overlap evidence) | Single model, single seed, no error bars, only magnitude pruning |
| E3 | Mask self-stability (Section 5, Figure 10) | Same MLP, pairwise IoU between masks at different training steps | IoU (masks) | Masks stabilize early (high IoU after ~100 steps) | Supports LTH/EBLT narrative | No comparison with other pruning schedules |
| E4 | Hessian eigenspace self-stability (Section 5, Figure 10) | Same MLP, pairwise overlap of top Hessian subspaces | Overlap (H_train), Overlap (H_test) | Hessian eigenspaces stabilize early; no substantial H_train vs H_test difference | Supports Gur-Ari et al. narrative | Only tested on one model size |
| E5 | Energy concentration (Section 5, Figure 9) | Same MLP, κ(θ) and κ(Λ) at training steps | κ(θ), κ(Λ_train), κ(Λ_test) | Small subset of params/eigenvalues contain most energy after few steps | Supports early collapse narrative | Only magnitude-based; no alternative sparsity measures |

### Research-Theme Gap Diagnosis

1. **New knowledge:** The paper contributes a correlation finding (pruning mask subspaces overlap with Hessian eigenspaces). This is genuinely new as a direct empirical observation. However, the paper does not explain *why* the overlap occurs, which limits its contribution to knowledge.
2. **Reproducibility:** The experimental setup is described clearly enough to reproduce, but the lack of multi-seed statistics means the reported overlap trajectories may not be reproducible in detail.
3. **Impact on practice:** The paper claims potential impact (fast Hessian approximation, bridge between first/second-order methods) but provides no validation. The actual impact on practice is currently zero until these claims are tested.

### Proposed Research Experiments (P0/P1/P2)

**Exp P0-A: Multi-architecture validation**
| Field | Value |
|-------|-------|
| Target Claim | C3: Overlap is a general property of neural network training |
| Hypothesis | The overlap phenomenon holds for convolutional and larger architectures |
| Minimal Design | Train a small CNN (2 conv + 2 FC, ~500K params) on MNIST (28×28, full) under the same protocol as Section 5 |
| Controls/Baselines | Compare with the original MLP result; verify overlap > k/D for multiple ρ values |
| Metrics | Overlap at t∈{0,5,10,...,2000} for ρ∈{0.005, 0.01, 0.05, 0.2} |
| Success Criterion | Overlap significantly above k/D (p<0.01) for at least 3 out of 4 ρ values |
| Estimated Cost | ~2 days (Hessian top-k via randomized SVD) |
| Expected Gain | High - establishes generalizability beyond single toy model |

**Exp P0-B: Multi-seed statistical analysis**
| Field | Value |
|-------|-------|
| Target Claim | C3: Overlap magnitude and temporal pattern |
| Hypothesis | Overlap patterns are consistent across random seeds |
| Minimal Design | Run the original MLP experiment with 5 different random seeds (different init, different data split) |
| Controls/Baselines | Report mean ± std overlap; compare to k/D ± std |
| Metrics | Overlap, dist_p,F - with confidence bands |
| Success Criterion | Standard deviation < 0.5× (overlap - k/D) at all training steps |
| Estimated Cost | ~3-5 days (5× the original compute) |
| Expected Gain | High - establishes statistical reliability of the core result |

**Exp P1-A: Alternative pruning criterion comparison**
| Field | Value |
|-------|-------|
| Target Claim | The overlap is specific to magnitude pruning vs. general to any pruning criterion |
| Hypothesis | Different pruning criteria show different overlap levels with the Hessian eigenspace |
| Minimal Design | Repeat the Section 5 experiment with: (a) random mask (baseline), (b) gradient-norm-based mask, (c) Fisher-information-based mask |
| Controls/Baselines | Magnitude pruning result as the reference |
| Metrics | Overlap curves for each criterion |
| Success Criterion | Identify whether different criteria produce meaningfully different overlap patterns |
| Estimated Cost | ~1 week |
| Expected Gain | Medium - clarifies whether magnitude pruning has a special connection to Hessian structure |

**Exp P2-A: Practical Hessian approximation test**
| Field | Value |
|-------|-------|
| Target Claim | "Pruning masks can be used for fast Hessian approximation" (currently unsupported) |
| Hypothesis | The mask subspace can approximate the top Hessian subspace with measurable accuracy |
| Minimal Design | Compute top-k Hessian eigenvectors (ground truth). Compute mask subspace. Measure subspace distance (principal angles) between them. Compare with random subspace baseline. |
| Controls/Baselines | Random subspace, k random parameter subset |
| Metrics | Overlap, largest principal angle, reconstruction error of H^{(k)} |
| Success Criterion | Mask subspace performs significantly better than random subspace (p<0.05) |
| Estimated Cost | ~1 week (mainly Hessian computation) |
| Expected Gain | High - validates (or refutes) the paper's key claimed application |

```text
ASCII Diagram — Experiment Upgrade Plan
=========================================

    P0-A: Multi-Architecture       P0-B: Multi-Seed Stats
    ┌──────────────────────┐       ┌──────────────────────┐
    │ MLP (7K params)      │       │ Seed 1 (current)     │
    │ CNN (500K params)    │       │ Seed 2-5 (new)       │
    │ Compare overlap      │       │ mean ± std overlap   │
    └──────────┬───────────┘       └──────────┬───────────┘
               │                              │
               ▼                              ▼
         [Generalizability]            [Statistical Reliability]
               │                              │
               └──────────┬───────────────────┘
                          ▼
                  P1-A: Alternative Criteria
              ┌──────────────────────────┐
              │ Magnitude (current)      │
              │ Random (baseline)        │
              │ Gradient-based (new)     │
              │ Fisher-based (new)       │
              └──────────┬───────────────┘
                         ▼
                   P2-A: Practical Test
              ┌──────────────────────────┐
              │ Mask subspace accuracy   │
              │ vs. true Hessian subspace│
              └──────────┬───────────────┘
                         ▼
                 Validated Contributions
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5 / 10**

The paper presents a mathematically rigorous framework and an interesting conceptual contribution, but the empirical validation is insufficient to support the strength of the claims. The single-model, single-seed, single-criterion experiment design limits generalizability, and the unsupported practical claims in the abstract and introduction misrepresent the contribution's maturity. The core idea (connecting pruning masks and Hessian eigenspaces via Grassmannian metrics) is novel and well-motivated, and the mathematical development is strong.

**Score Breakdown:**
- Novelty/Conceptual Contribution: 6/10 (good idea, but C2 is incremental)
- Technical Rigor (Math/Theory): 7/10 (sound mathematical framework)
- Empirical Validation: 4/10 (severely limited scale, no statistics)
- Reproducibility/Clarity: 6/10 (well-written, but multi-seed data missing)
- Practical Significance: 3/10 (claims not validated)
- Presentation Quality: 7/10 (well-organized, clear figures)

**Post-Revision Target: [6.5, 7.5] / 10**

If the authors address the P0 items (multi-model experiment, multi-seed statistics, bounded claims), the score could reach 6.5-7.0. With P1 items additionally resolved (alternative criteria, alternative explanations), the score could reach 7.0-7.5. The upper bound is constrained by the paper's primarily observational nature—without causal explanation or practical validation, the ceiling is moderate.