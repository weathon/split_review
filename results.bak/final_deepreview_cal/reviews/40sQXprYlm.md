Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper introduces Distributed Neural Architectures (DNAs), a framework where each token follows a learned, data-dependent path through a collection of transformer/MLP/attention modules connected by routers. DNAs generalize MoE, Mixture-of-Depths, early exit, and weight sharing within a single trainable framework. The paper evaluates DNAs on ImageNet (vision) and FineWeb-Edu (language) at moderate scale, finding competitive performance with ViT-small and GPT-2 medium baselines. Its main contributions are the feasibility demonstration, a set of interpretability analyses showing emergent specialization of paths and modules, and empirical findings such as a power-law distribution of paths and interpretable compute allocation.

## Strengths

- **Novel framework with conceptual unification.** The DNA formulation subsumes MoE, MoD, early exit, and weight sharing as special cases (Section 2.1), providing a clean and general perspective on conditional computation. This is not just rhetoric—the empirical analysis shows mixtures of all these strategies emerge from training.

- **Rich interpretability analysis with multiple techniques.** The paper goes beyond standard benchmark reporting with path-distribution visualizations (Figs. 1c–d), patch-level path specialization (Fig. 3), deep-dream routing reconstruction (Fig. 4), compute allocation heatmaps (Fig. 5), and qualitative router analysis (Fig. 8). These demonstrate that emergent routing patterns are human-interpretable—e.g., boundary-heavy images get more compute, punctuation tokens are grouped, verb variants cluster to the same module. This is the paper's strongest contribution.

- **Cross-domain validation with controlled vision experiment.** Vision experiments match active parameters carefully (ViT: 22M, top-1 DNA: 22M, top-2 DNA: 18M) and show the DNA is within ~1% of the dense ViT-small baseline (79.8% vs 79.1%/78.8%). The hyperparameter search is documented (learning rate × weight decay grid). This gives credibility to the feasibility claim in vision.

- **Discovery of power-law path distribution.** The finding that path frequencies follow a power-law (exponent −1 for vision, −1.2 for language), and that even random models exhibit exponent −1, is an original empirical observation that could inform future work on routing regularities.

## Weaknesses

### Major

- **Language comparison confounded by active parameter mismatch.** The top-2 DNA model (433M active parameters) outperforms GPT-2 medium (406M) on most benchmarks in Table 3, but this advantage is at least partly attributable to 6.6% more active parameters. The top-1 DNA (406M active, matched to GPT-2) performs *worse* than GPT-2 on most metrics (loss 2.754 vs 2.720, HellaSwag 38.6 vs 40.5). This weakens the claim that DNAs are "competitive with dense baselines" in the language domain. The vision experiments are properly controlled, so the inconsistency is notable. The authors should either train a parameter-matched top-2 variant or transparently caveat the language claim.

### Minor

- **Gradient flow through routing is underspecified.** The paper states "the routing decision is made by sampling with hard top-k" and Eq. (1) uses softmax probabilities *ρ* as weights on the selected modules' outputs. The mechanism is *inferable* —gradients flow through *ρ* (the softmax), and the hard selection gates which modules participate—but the paper never states this explicitly. The wording "sampling with hard top-k" and the citation to Bengio et al. (2013) (which discusses stochastic neurons) create ambiguity about whether straight-through estimation, REINFORCE, or simple softmax weighting is used. Since this is the core training mechanism, a clear sentence would resolve it.

- **Compute efficiency claim lacks a Pareto trade-off.** The paper trains one skip-target per domain (25% for vision, 30% for language) and reports performance at that single point. For vision, the 25%-skip top-2 DNA achieves 78.8% vs 79.1% for the non-skip top-1 (and 79.8% for ViT). For language, the 30%-skip model loses ~0.11 in loss vs the non-skip top-2 (Table 3). Without a sweep of skip rates and a compute-vs-accuracy Pareto plot, the claim of "minor effects on performance" is qualitative rather than quantitative. A single additional data point per domain would substantially strengthen this claim.

- **Missing experimental details.** (a) *s_max* (maximum token-processing steps) is described as a key hyperparameter but is never reported for any model—it must be inferred from *N_b* + *N_r*. (b) The module inventory is not specified: the paper says modules "can be chosen from the classic GELU-transformer block or its attention/MLP component" but does not state, for any trained model, how many modules are full blocks vs attention-only vs MLP-only. These details affect interpretability of the specialization analysis. Both may be in the stripped appendix but should be in the main paper.

- **No confidence intervals or multi-seed results.** All accuracy/loss numbers are reported from single runs without variance estimates. Given the stochasticity of routing, showing results over 2–3 seeds would strengthen the evidence, especially for the small gap claims.

### Trivial

- The "parameter sharing" terminology in Section 3.3 is a misnomer—the analysis measures module *reuse* (different tokens routed to the same module), not weight sharing across modules. The analysis itself is interesting; the label is slightly misleading.

## Nice-to-Haves

- A compute-efficiency Pareto plot for at least one domain (accuracy vs. average compute per token at multiple skip targets) would move the efficiency claim from qualitative to quantitative.
- Disentangling module type (full transformer vs. attention-only vs. MLP-only) from routing analysis would strengthen the specialization claims—is a module specializing because of its learned routing or because its architectural capacity is restricted?

## Removed Points

- **"Vision skip model accuracy is never reported"** —This is factually incorrect. Figure 2 reports Top-2 DNA (the 25% skip model from Table 1) at 78.8% accuracy. The critic's claim is invalid and removed.
- **"Compute-efficiency claim lacks supporting data (vision)"** —See above. The accuracy is reported. The critique about the lack of a multi-point Pareto curve is kept (as a Minor weakness), but the stronger claim that accuracy is entirely absent is removed.
- **"Formatting/style/strawman issues"** —Several minor criticisms about font, appendix references, and ambiguity in figure captions that are parser artifacts or misreadings were removed per protocol.
- **"Missing related works"** —Removed per hard rules.
- **"Bias update time window unspecified"** —The paper says counts are accumulated "from the Autograd as in Liu et al. (2024)," which is a reference to a published method. This is standard practice and not a meaningful omission.

## Novel Insights

The most interesting observation across the reviews is the tension between the paper's stated goal (feasibility + interpretability) and the implicit expectation that SOTA-level rigor is needed to support that claim. The harsh critic treats missing evaluation controls (language active-param mismatch, missing Pareto curves) as potentially fatal; the strength finder treats the interpretability analysis as the core contribution. The resolution is that the paper's real contribution is the *analysis toolkit* (path visualization, deep-dream reconstruction, router specialization) applied to a reasonably novel architecture, not the architecture's raw performance. The strongest evidence for this framing is that the vision experiment is properly controlled and the interpretability findings are genuinely novel, while the language experiment's parameter confound cuts against the "competitive" framing but does not invalidate the qualitative analysis. A revision that reframes the language results more modestly and adds the missing experimental details would make the paper's true contribution cleaner.

## Suggestions

1. Clarify gradient flow: state explicitly that gradients flow through the softmax probabilities *ρ* and the hard top-*k* selection is treated as a non-differentiable gate (standard in MoE), or describe any additional gradient estimation technique used.
2. Retrain or add a footnote for the language experiment: either train a GPT-2 variant with matched active parameters (~433M) or transparently reframe the claim from "competitive" to "competitive at comparable total parameter count, with small active-parameter advantages when capacity is added."
3. Add a compute-efficiency Pareto plot for at least one domain with 3–4 skip targets.
4. Report *s_max* explicitly in the hyperparameter tables and specify the module-type composition for each trained model (how many full transformer, attention-only, MLP-only modules).
5. Add variance estimates over 2–3 seeds for the main accuracy/loss numbers.
6. Rename "parameter sharing" to "module reuse" or "parameter reuse" throughout Section 3.3 and Section 4.3.

## Score and Decision

I now perform calibration to determine the final score.

**Round 1 bracket:** After reading the paper and reviewing calibration anchors, my initial bracket was 4–6 (below Tight Clusters at 7.0, above the weak MoE papers at ~3.0).

**Round 2 narrowing:** I read anchors SMEAR (6.0, rejected), COMET (5.67, accepted), Learning How Hard to Think (6.5, accepted), and γ-MoD (6.67, accepted) in full. The current paper's interpretability analysis is stronger than SMEAR and COMET, but its experimental controls are weaker than Learning How Hard to Think and γ-MoD. The active-parameter confound in the language experiment is a clear gap relative to all four anchors.

**Calibration anchors retrieved (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| XVHXVdoV11 (Collective Model Intelligence) | 3.40 | R1 | Weaker — poorly executed model combination paper |
| KaYXsoCxV7 (ViMoE) | 3.00 | R1 | Weaker — vision MoE with routing issues |
| sTI75sFQkn (dFCExpert) | 3.25 | R1 | Weaker — domain-specific MoE for fMRI |
| 1qq1QJKM5q (COMET) | 5.67 | R1 | Similar ambition, similar rigor; current paper has stronger interpretability but weaker language control |
| QHzzAU7Qf9 (SMEAR) | 6.00 | R1/R2 | SMEAR is cleaner method-wise but narrower; current paper broader but less rigorous |
| Pu3c0209cx (Tight Clusters) | 7.00 | R1/R2 | Stronger — has proofs, cleaner experiments |
| huy8g3iKy0 (Dense Backprop) | 5.50 | R1 | Similar-level MoE routing paper |
| t7P5BUKcYv (MoE++) | 8.00 | R1 | Much stronger — SOTA results with clear efficiency gains |
| xXTkbTBmqq (OLMoE) | 8.67 | R1 | Much stronger — full open-source MoE LLM |
| q44uq3tc2D (γ-MoD) | 6.67 | R2 | Stronger — cleaner evaluation, focused contribution |
| 6qUUgw9bAZ (Learn How Hard to Think) | 6.50 | R2 | Stronger — cleaner experiments, more rigorous |
| fmWVPbRGC4 (Local vs distributed) | 5.67 | R2 | Similar quality — interpretability-focused paper with mixed reception |
| qPTFzmXVLd (Visual Tokens) | 5.50 | R2 | Similar quality — analysis paper with interesting findings but limited evaluation |

The paper is closest to COMET (5.67) and SMEAR (6.0) in overall quality, but the active-parameter confound in the language experiments pulls it slightly below those. I place it at **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>