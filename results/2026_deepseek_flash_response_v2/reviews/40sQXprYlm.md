## Summary
This paper introduces Distributed Neural Architectures (DNAs), where tokens follow individualized paths through a collection of computational modules with learned routing — a generalization of MoE, MoD, parameter sharing, and early exits. The authors train DNA models for vision (ImageNet classification) and language (causal LM on FineWeb-Edu) at ViT-small and GPT-2-medium scales, showing they are trainable and broadly competitive with dense baselines. The main contributions are: (1) demonstrating that fully flexible, end-to-end learned routing is feasible at non-trivial scale, (2) analyzing emergent properties including path specialization and power-law path distributions, and (3) showing content-dependent compute allocation.

## Strengths
- **Fully flexible learned routing is shown to be trainable at non-trivial scale.** The top-2 DNA language model (433M active params) achieves lower validation loss (2.674 vs 2.720) than GPT-2 medium (406M) and outperforms it on 5 of 7 zero-shot benchmarks (ARC-E 59.2 vs 58.9, BoolQ 61.0 vs 60.5, HellaSwag 41.8 vs 40.5, LAMBADA 34.0 vs 33.8, PIQA 67.9 vs 66.9). This goes beyond prior constrained routing methods (MoE, MoD) that fix when/where routing can occur — DNA demonstrates that full topological freedom is trainable and can produce competitive results.

- **Qualitative interpretability analysis reveals genuine emergent specialization, with random baseline validation.** Path-level analysis (Figs. 3, 8) shows low-rank paths aggregate patches by high-level features (edges, color regions), while high-rank paths capture specific visual concepts (brass instruments, puzzle pieces). In language, early routers consistently send semantically similar tokens to the same modules. Crucially, the paper validates against random baselines (Section 3.2), showing random models also cluster but by a very different similarity measure, ruling out trivial architectural artifacts.

- **Honest reporting of negative results.** The paper transparently documents findings that don't fit a neat narrative: module reuse in language is "most likely random" (Section 4.3), and power-law structure also appears in random models (Fig. 1 caption). This scientific honesty is valuable and rare in conditional-computation papers.

- **Content-dependent compute allocation with interpretable patterns.** The analysis of compute allocation (Fig. 5) shows boundary-rich images require more compute while background-dominated images require less, with a roughly Gaussian distribution across the validation set. This demonstrates meaningful, input-dependent compute allocation.

## Weaknesses

### Major
- **No comparisons against any conditional-computation baselines.** The paper positions DNA as "a natural generalization" of MoE, MoD, Layer-skip, and early-exit methods (Section 1), yet every baseline in the experiments is a dense transformer/ViT. Without comparisons to existing conditional-computation approaches at comparable parameter/compute budgets, the reader cannot evaluate whether DNA's generalized routing provides any benefit over existing methods. This is the single most significant gap: a generalization whose special cases (MoE, MoD) are well-studied needs to be shown to match or outperform those special cases. The paper's central claim of being "competitive" cannot be properly contextualized without these comparisons.

### Minor
- **The "competitive" claim rests on a narrow evidence base with notable tradeoffs.** In vision (Table 1), top-1 DNA achieves 79.1% vs ViT-small's 79.8% — but has 34M total parameters (55% more than ViT's 22M). The top-2 DNA uses 18M total params but at 78.8%. In language, top-1 DNA (406M active params) trails GPT-2 medium on 5 of 7 metrics with clearly worse perplexity (38.7 vs 33.7), and top-2 DNA uses 433M active params (27M more than GPT-2) to achieve its edge. The paper's footnote 3 appropriately scopes the work as a feasibility study, but the abstract's unqualified "competitive" claim would benefit from more explicit caveats.

- **No variance or statistical significance reported for any result.** Tables 1–3 report single "best run" numbers from a hyperparameter grid search. Given that differences between DNA and baselines are often small (0.7% on ImageNet, 0.03–0.07 in loss), the absence of any variance information makes it impossible to assess whether these gaps are meaningful or within training noise. This is a standard expectation for empirical ML papers.

- **Interpretability analysis is entirely qualitative.** While visually compelling, the path specialization analysis (Figs. 3, 4, 8) relies entirely on hand-picked examples. There is no quantitative validation — no clustering metrics, no correlation with segmentation boundaries, no part-of-speech purity scores for language routing. Given that analyzing emergent structure is a stated goal, quantitative measures would significantly strengthen the evidence.

- **Language experiments at acknowledged insufficient scale.** The paper states models are "way too small to truly absorb" the 21B-token dataset and operate in a "vastly underparametrized" regime. This limits the generality of conclusions about DNA's language properties, especially given that interesting effects (power-law exponent shift, module reuse patterns) might change at scale.

- **Compute-efficiency analysis is preliminary.** The paper reports one operating point each for vision (25% skip) and language (30% skip), both with noticeable accuracy/performance penalties. There is no systematic Pareto sweep of the accuracy-compute tradeoff, no comparison to a shallower dense baseline at equivalent compute, and no wall-clock or FLOPs accounting for the dynamic sparse attention overhead.

### Trivial
- None.

## Nice-to-Haves
- Adding MoE and MoD baselines at comparable parameter/compute budgets (this is the single most impactful addition).
- Reporting results across multiple seeds (at least 3) for the main comparisons.
- Adding quantitative validation to the interpretability analysis (e.g., correlation with segmentation masks in vision, POS-tag purity in language).
- A compute-accuracy Pareto curve sweeping the skip ratio to characterize the tradeoff systematically.
- An ablation with random or uniform routing to isolate the contribution of learned routing from the increased parameter count.
- Wall-clock or FLOPs measurement for the dynamic sparse attention.

## Removed Points
The following points were extracted from the reviews but removed per filtering rules:

- **HC: "Power-law finding is substantially less interesting than it first appears."** Removed because the paper accurately reports the finding and the random-model comparison. The discovery that power-law distributions emerge in both trained and random models is itself an interesting architectural property, and the exponent shift in trained language models (-1 to -1.2) represents a genuine learned effect. The abstract does not oversell this finding.

- **HC: Method underspecification (backbone arrangement, identity modules, router architecture).** Removed because the paper provides adequate detail for a conference submission: backbone layers are described as the "first few modules" that process all tokens, routers are "linear (token-choice) classifiers" with softmax and top-k sampling, and identity modules are explained with the bias-trick training mechanism (Eq. 2–3).

- **Strength Finder: Generic strengths about the problem being important or the paper being well-written.** Removed per filtering rules. Only concrete, specific strengths were retained.

## Novel Insights
None beyond the paper's own contributions — the reviews largely concur with the paper's self-assessment. One observation worth noting: the Harsh Critic and Strength Finder agree on the core tension — the paper has a genuinely novel idea and thoughtful analysis, but the empirical evidence is substantially weaker than the claims require. The single most critical gap (no conditional computation baselines) is flagged by both.

## Suggestions
1. Add at least one conditional-computation baseline (a standard MoE) at comparable parameter/compute budget — this is necessary to establish that DNA's flexibility provides a benefit over existing approaches.
2. Report variance across 3+ seeds for the main comparisons (vision and language).
3. Add quantitative measures to validate the interpretability claims (segmentation correlations in vision, POS/semantic purity in language routing).
4. Include a compute-accuracy Pareto analysis sweeping the skip ratio across multiple values.
5. Qualify the "competitive" claim in the abstract to clarify the specific tradeoffs (parameter count, accuracy gaps).

## Calibration Anchors

**Round 1 — Bracketing:**
| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| Collective Model Intelligence Requires Compatible Specialization | 3.40 | R1 (weak) | Weaker — unclear contribution, weaker experiments |
| Directed Structural Adaptation | 2.33 | R1 (weak) | Much weaker — small scale, unclear method |
| Learning Successor Representations with Distributed Hebbian... | 3.00 | R1 (weak) | Weaker — niche method, limited empirical support |
| Modeling Divisive Normalization | 3.25 | R1 (weak) | Weaker — narrower scope, less convincing results |
| Tight Clusters Make Specialized Experts | 7.00 | R1 (middle) | Stronger — rigorous theory, comprehensive MoE experiments |
| Soft Merging of Experts with Adaptive Routing | 6.00 | R1 (middle) | Comparable — similar scale/significance issues, rejected despite good presentation |
| Theory on MoE in Continual Learning | 7.33 | R1 (middle) | Stronger — solid theoretical contribution |
| Self-MoE: Towards Compositional LLMs | 6.00 | R1 (middle) | Stronger — cleaner results (6.5% improvement), accepted |
| Interpreting Emergent Planning in Model-Free RL | 8.00 | R1 (strong) | Much stronger — rigorous methodology |
| CAX: Cellular Automata Accelerated in JAX | 8.00 | R1 (strong) | Much stronger — polished execution |

**Round 2 — Narrowing:**
| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| Gradient Routing: Masking Gradients to Localize Computation | 5.25 | R2 (narrow) | Slightly weaker — novel method but practical value unclear, rejected. Our paper has more thorough analysis. |
| A Theory of Initialisation's Impact on Specialisation | 6.00 | R2 (narrow) | Comparable — theoretical/empirical mix, clean results, accepted |
| More Experts Than Galaxies: COMET | 5.67 | R2 (narrow) | Comparable — similar ambition and limitations; accepted despite mixed reviews |
| Bootstrapping V-IP for Interpretable Classification | 5.75 | R2 (narrow) | Slightly weaker — narrower contribution |
| Circuit Component Reuse Across Tasks | 6.50 | R2 (narrow) | Stronger — focused, well-executed analysis |
| Causal Graphical Models for VL Compositional Understanding | 6.67 | R2 (narrow) | Stronger — novel framework with solid experiments |
| Interpreting and Editing VL Representations | 6.00 | R2 (narrow) | Comparable — similar empirical quality |

**Round 1 bracket:** The plausible score range was 4.5–6.5.

**Round 2 narrowing:** The paper is most comparable to COMET (5.67, accepted), Soft Merging of Experts (6.00, rejected), and Gradient Routing (5.25, rejected). It is clearly stronger than the ~3.0 weak anchors and clearly weaker than the ~7.0+ strong anchors. Within the 5–6 range, the paper's core idea has genuine novelty (full topological freedom is a meaningful step beyond MoE/MoD), and the analysis is more thorough than Gradient Routing. However, the missing conditional-computation baselines are a significant gap that Soft Merging of Experts and Tight Clusters do not share. **Final score: 5.5 — a borderline paper with a genuinely interesting idea and thoughtful analysis, but empirical support is substantially weakened by the absence of conditional-computation baselines and variance reporting.**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>