## Summary

This paper introduces Distributed Neural Architectures (DNAs), a framework where tokens follow input-dependent paths through a collection of computational modules (MLP, attention, transformer blocks) with end-to-end learned routing. DNAs generalize conditional computation methods (MoE, MoD, weight sharing, early exit) in a unified architecture where each token can traverse any series of modules in any order. The paper demonstrates feasibility in both vision (ImageNet, at ViT-Small scale) and language (FineWeb-Edu, at GPT-2 Medium scale), showing competitive performance with dense baselines, content-aware compute allocation, and emergent path/module specialization analyzed through qualitative interpretability studies.

## Strengths

**1. Novel framework unifying conditional computation approaches.** DNA generalizes MoE, MoD, weight sharing, and early exit into a single learnable routing architecture. While each of these ideas exists in prior work, the unified formulation — where tokens take arbitrary paths through a module bank with per-token variable depth — is a genuinely novel framing that opens new directions for emergent network design.

**2. Feasibility demonstrated in two domains.** DNA models train successfully in both vision (ImageNet, 300 epochs) and language (FineWeb-Edu, 21B tokens). Top-1 DNA achieves 79.1% on ImageNet vs ViT-Small's 79.8%; top-2 DNA achieves lower validation loss (2.674) than GPT-2 Medium (2.720). These results show the architecture is trainable and does not catastrophically underperform dense counterparts, which is non-trivial given the complexity of the routing space.

**3. Content-aware compute allocation supported by proxy measurements.** The top-2 DNA (25% skip) model allocates fewer module-executions to visually simple images (uniform backgrounds, single objects) and more to complex/textured images (Fig. 5). The compute distribution across ImageNet is roughly Gaussian (range ~0.60–0.80 normalized), and visual inspection confirms the assignment aligns with intuitive complexity. This supports the claim that DNAs learn input-dependent compute allocation, even if the measurement is a module-count proxy rather than FLOPs.

**4. Emergent specialization of paths and modules.** Flow diagrams (Fig. 2 bottom, Fig. 6 bottom) reveal that modules develop specialized roles over training, with some never activated. Path analysis (Figs. 1, 3) shows that low-rank paths aggregate patches with shared high-level features (edges, flat color) while high-rank paths group specific visual concepts (brass instruments, puzzle pieces). This specialization emerges without explicit supervision.

**5. Discovery of power-law path distributions.** The distribution of paths taken by tokens follows a power law in both vision (exponent −1) and language (exponent −1.2). The paper further shows that random (untrained) models also exhibit power-law distributions with exponent −1, providing a useful baseline that separates architecture-induced structure from learned structure. This empirical finding characterizes the emergent connectivity pattern.

## Weaknesses

### Major

**1. Compute efficiency claims lack direct FLOPs or wall-clock measurements.** The paper uses "effective number of compute nodes" and module-execution counts as proxies for compute. These proxies ignore (i) the substantial difference in per-module FLOPs (attention vs. MLP), (ii) overhead from the routing architecture (backbone + s_max steps × top-k selection), and (iii) the fact that top-2 routing can execute *more* module operations per token than a dense baseline of similar active parameter count. For vision, the top-2 DNA (25% skip) has 18M active parameters vs ViT-Small's 22M, but the routing architecture (1 backbone + 11 routed steps × top-2) could easily require more total operations than ViT's 12 uniform layers. Without FLOPs comparisons, the claim that DNAs provide an efficiency *advantage* over dense baselines (as opposed to merely learning input-dependent allocation) is unsubstantiated. The paper's stated scope ("not focused on beating SOTA") mitigates this somewhat, but the paper still claims "compute efficiency can be learnt from data," and the evidence for *efficiency* (as opposed to *variable allocation*) is weak without actual compute measurements.

**2. No comparisons against existing conditional computation methods.** The paper positions DNAs as a generalization of MoE, MoD, and LayerSkip, yet provides no empirical comparison against any of these methods at comparable scale. Without such baselines, the reader cannot assess whether DNAs offer any advantage — in accuracy-compute trade-off, training stability, or emergent interpretability — over these established sparse architectures. Including even a small-scale comparison (e.g., an MoE or MoD baseline with similar total modules and compute budget) would substantially strengthen the contribution.

**3. Key language baseline is poorly specified and the top-2 DNA comparison is confounded by total parameter count.** The top-2 DNA language model has 603M total parameters vs GPT-2 Medium's 406M. While active parameters are closer (433M vs 406M), the extra total capacity is a confound. The single controlled baseline ("GPT-2 (30% shallover)") achieves 38.0 Wiki perplexity vs the skip model's 52.6 — but this baseline is only documented in the (stripped) appendix, and its poor performance relative to GPT-2 raises questions about whether it is a properly tuned comparison. A stronger controlled evaluation would match both total parameters *and* inference FLOPs.

### Minor

**4. Interpretability analysis is qualitative only, without systematic validation.** The path specialization and routing analyses (Figs. 1, 3, 4, 8) rely on manually selected examples. There is no quantitative measurement of path-class purity, mutual information, or statistical significance of the observed clustering. The paper's own baseline — showing that random (untrained) models also cluster images, but with a different similarity measure — weakens the claim that trained specialization is meaningful. The deep-dream reconstructions (Fig. 4) are interesting but produce images classified as different classes from originals, acknowledged by the paper. Given the paper's stated emphasis on "analyzing emergent structure," the lack of quantitative interpretability metrics is a missed opportunity.

**5. No variance estimates or multiple seeds.** Results are reported from the best run after hyperparameter search, without variance across seeds. Given the small accuracy differences (~1% in vision), statistical significance is unclear. This is standard practice for large-scale experiments but limits confidence in the competitive claims.

**6. Skip regularization trade-off not compared against simpler alternatives.** When compute is explicitly reduced via skip regularization in language, performance drops substantially (LAMBADA 34.0→23.8; HellaSwag 41.8→35.5). The paper does not compare this trade-off against a shallower dense model with matched compute, making it unclear whether the dynamic nature of skipping provides any advantage over uniform depth reduction.

### Trivial

**7. CDF-based path ranking not clearly defined.** The paper refers to paths "colored by their corresponding CDF values" (Fig. 3, Section 3.2) and "CDF value of the path" (Section 4.2) without specifying what the cumulative distribution function is over (path frequency? probability?). This should be clarified.

**8. The Sign-based bias update rule (Eq. 3) is not analyzed for training behavior.** The Sign function in the bias update could cause oscillations. The paper does not discuss whether this occurs or whether the biases converge smoothly.

## Nice-to-Haves

- **FLOPs measurements** for all models, including the overhead of routers and the dynamic attention sparsity, would directly substantiate the efficiency claims.
- **Comparisons with MoE, MoD, and LayerSkip** at comparable scale would frame the contribution relative to prior conditional computation work.
- **A simple controlled baseline** matching the DNA skip model's average inference depth via a uniformly shallower dense model would clarify whether dynamic routing offers advantages over static depth reduction.
- **Quantitative interpretability metrics** (e.g., path-conditional class purity, POS-tag purity for language) would replace the current anecdotal evidence with rigorous confirmation.
- **Multiple seeds** for key experiments (at least 3) would establish whether ~1% accuracy differences are significant.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that "GPT-2 (30% shallover)" is undefined:** The paper states this baseline is detailed in Appendix A (stripped by the parser). Per review policy, missing appendix content cannot be penalized. The factual claim about "52.6 Wiki perplexity" attributing it to the shallover model is incorrect — 52.6 is the top-2 (30% skip) model's perplexity; the shallover's perplexity is 38.0. **Removed as factually wrong and appendix-dependent.**

- **Criticism about how gradients flow through hard top-k selection:** The architecture uses softmax probabilities ρ_i as differentiable weights in the output combination (Eq. 1), which is the standard approach for gradient propagation through routing decisions (analogous to MoE). This is implicit in the formulation and is standard practice. **Removed as a misunderstanding of the paper's technical approach.**

- **Criticism that identity module definition is missing:** The paper clearly states: "If a router sends a token to the identity module then nothing happens to the token (h^{(s+1)} = h^{(s)})." **Removed — the paper already addresses this.**

- **Criticism that deep-dream reconstructions undermine interpretability claims:** The paper acknowledges: "The final image looks recognizable, but not the same as the original. Furthermore, the network can guess the group of classes correctly: birds and dogs, but has difficulty deciding the species and breed." This is presented as a finding about hierarchical classification, not as a failure. **Removed — the paper already addresses the observation.**

- **Criticism that random model baseline weakens interpretability:** The paper explicitly includes this baseline and discusses how trained models use a *different* similarity measure. Rather than weakening the claim, this controlled comparison strengthens it by showing training changes the clustering criterion. **Removed — the paper already addresses this and uses it constructively.**

- **Criticism about "not yet experimented with other modules" suggesting preliminary work:** This is a factual statement about current scope, not a weakness. The paper's title includes "Towards" and the scope is explicitly stated as feasibility and analysis. **Removed — not a valid weakness.**

- **Criticism about backbone layers limiting full emergence:** The paper states this as an empirical design choice to ensure trainability, not as a claim about the fully general framework. **Removed — the paper is transparent about this design choice.**

- **Strength about "Human-interpretable routing":** The supporting evidence is qualitative and does not meet the bar of a rigorously validated strength. The paper's analysis is suggestive but the interpretability claim is better treated as an observed phenomenon rather than an established strength. **Moved to Minor/observed findings rather than a core strength.**

- **Generic strength about addressing an important problem:** "This paper addressed an important problem" is superficial. **Removed.**

## Novel Insights

The most interesting observation is the power-law distribution of paths in both trained *and random* models (exponents −1 for random, −1.2 for trained language, −1 for trained vision). This suggests that the routing architecture's combinatorial structure induces a heavy-tailed path distribution even without learning, and training primarily shifts the exponent (for language) or preserves it (for vision). The fact that random models also cluster images (though by different criteria) is a useful baseline that future work on emergent specialization should control for. The finding that compute allocation in vision correlates with boundary complexity (Fig. 5) and that the model prioritizes "objectness" is empirically consistent with prior work on patch importance (Riquelme et al., 2021) — the paper's contribution here is showing this emerges from routing rather than being explicitly supervised. None of these individual findings is radically surprising, but their coherent demonstration within the DNA framework provides a novel birds-eye view of how distributed computation can organize itself.

## Suggestions

1. **Add FLOPs measurements** for all reported models. This is the single most impactful improvement. Report FLOPs per token (including router overhead) for the DNA models and all baselines. This will either substantiate or qualify the efficiency claims.

2. **Include at least one conditional computation baseline** (e.g., an MoE-style model with the same total modules and comparable active parameters, or an MoD-style router). This would frame the contribution relative to the methods DNAs claim to generalize.

3. **Provide accuracy × compute Pareto curves** for the vision skip models at multiple skip ratios, compared against a uniformly shallower ViT with matched inference FLOPs.

4. **Report results with multiple seeds** (3 runs) for key comparisons to establish statistical significance, especially given the small performance differences.

5. **Define the CDF-based path ranking explicitly** and consider adding quantitative metrics (e.g., average path purity for the top-K classes, or mutual information between path assignments and class labels) to complement the qualitative examples.

6. **Add a limitations section** discussing training overhead from routing, potential for router collapse, sensitivity to s_max/N_r/N_m, and the fact that backbone layers are currently hard-coded rather than fully emergent.

## Score and Decision

The paper introduces a genuinely novel framework for dynamic routing and demonstrates its feasibility across two domains with competitive performance. The emergent-structure analyses, while largely qualitative, offer interesting observations (power-law path distributions, content-aware compute allocation, module specialization) that open directions for future work. The paper is honest about its scope and limitations.

The main weaknesses are: (i) the absence of FLOPs measurements leaves compute-efficiency claims unsubstantiated, (ii) no comparisons against existing conditional computation methods (MoE, MoD), and (iii) the interpretability analysis is purely qualitative. These are real gaps but they do not invalidate the core contributions — the framework's novelty, feasibility demonstration, and emergent-structure characterization remain valuable. The weaknesses are addressable and the paper provides a solid foundation for follow-up work.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>