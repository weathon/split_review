Now I have a comprehensive understanding of the paper and the calibration landscape. Let me write the final consolidated review.

## Summary of calibration reasoning

**Round 1 bracket:** Between ~3.5 and ~6.0, based on topical similarity to anchors in the low (2.33–3.40) and mid (4.75–5.80) bands, plus weakness-anchored queries.

**Round 2 narrowing:** Pulled anchors in (4.5, 6.5). The paper is clearly stronger than "Automatic Organization of Neural Modules" (4.75) because DNAs trains at reasonable scale in two domains with working code and analysis. It is comparable to "Adaptivity and Modularity" (5.00, Reject) and "Gradient Routing" (5.25, Reject). It is slightly weaker than "More Experts Than Galaxies" (5.67, Accept) and "SMEAR" (6.00, Reject), both of which have more thorough baselines and quantitative evaluation.

**Anchors consulted:**
- XVHXVdoV11 — 3.40, round1-topic-low — Reject, similar topic, clear failure to demonstrate the core claim
- OovfCS4FYT — 3.25, round1-topic-low — Reject, exploratory bio-inspired method with limited evaluation
- fnO5h1CFyh — 3.00, round1-topic-low — Reject, limited empirical support
- ZHTYtXijEn — 2.33, round1-topic-low — Reject, serious methodological issues
- 1qq1QJKM5q — 5.67, round1-topic-mid — Accept, conditional MoE with broader experiments but some mixed reviews; stronger than DNAs
- ar9tcnD4e9 — 4.75, round1-topic-mid — Reject, modular neural nets with missing details; weaker than DNAs
- t7P5BUKcYv — 8.00, round1-topic-high — Accept, MoE++ thorough SOTA-oriented paper; much stronger
- T26f9z2rEe — 7.00, round1-weakness — Accept, DynMoE rigorous evaluation; much stronger
- QHzzAU7Qf9 — 6.00, round2 — Reject, SMEAR well-executed but small scale; stronger than DNAs
- z1mLNhWFyY — 5.25, round2 — Reject, Gradient Routing interesting but limited scope; comparable to DNAs
- tI3eqOV6Yt — 5.00, round2 — Reject, Hyper-UT adaptive computation; comparable to DNAs
- RQz7szbVDs — 6.00, round2 — Accept, theory paper less relevant
- aN4Jf6Cx69 — 4.50, round2 — Accept, very mixed reviews (1,1,8,8)

**Final score placement:** The paper is comparable to Gradient Routing (5.25) and Hyper-UT (5.00) — interesting ideas with meaningful evaluation gaps. It is weaker than SMEAR (6.00) and "More Experts Than Galaxies" (5.67), both of which have more thorough baselines. Score 5.0.

---

## Final Review — Paper 40sQXprYlm

## Summary

This paper introduces Distributed Neural Architectures (DNAs), where individual tokens/patchs are routed through a pool of transformer sub-modules (MLPs, attention, transformer blocks, identity) via learned linear routers rather than through a fixed feed-forward sequence. DNAs are trained in vision (ImageNet, ViT-small scale) and language (FineWeb-edu, GPT-2 Medium scale). The paper's main claims are: (i) DNAs are feasible to train and competitive with dense baselines, (ii) DNAs learn data-dependent compute allocation, and (iii) the emergent routing patterns and module specializations are interpretable. The paper explicitly states it is not focused on SOTA but on feasibility and emergent-structure analysis.

## Strengths

1. **Genuine conceptual novelty.** The DNA framework proposes a more flexible form of conditional computation than standard MoE or MoD: tokens are routed through modules that can include any transformer sub-component (attention, MLP, transformer block, identity) with sparse dynamic attention, all trained end-to-end. This is a distinct research direction that goes beyond existing conditional computation approaches in terms of architectural flexibility.

2. **Multi-domain feasibility demonstration.** DNAs are trained and evaluated in both vision (ImageNet, 300 epochs) and language (21B tokens of FineWeb-edu), with results that are broadly competitive with dense baselines (Top-1 DNA 79.1% vs ViT-small 79.8% on ImageNet; Top-2 DNA achieves lower validation loss 2.674 vs GPT-2 2.720). The two-domain validation is stronger than many exploratory architecture papers.

3. **Power-law path distribution characterization.** The finding that path frequencies follow a power-law with exponents ≈ -1 (vision) and -1.2 (language), and that random models also exhibit power-law behavior with exponent -1, is a clean quantitative result that provides a baseline for future work.

4. **Interpretable compute allocation.** The qualitative analysis of compute per image correlates meaningfully with visual complexity (e.g., boundary-rich images receive more compute), and the language model's skipping patterns for HTML/non-Latin scripts suggest the model learns genuine content-dependent efficiency.

## Weaknesses

### Major

1. **Missing comparison against the conditional computation methods DNAs claim to generalize.** The paper states DNAs "are a natural generalization of the sparse methods such as Mixture-of-Experts, Mixture-of-Depths, parameter sharing, etc." and that the construction "includes feed-forward, MoE, MoD, weight sharing, early exit as particular cases." Despite this framing, the experiments compare DNAs *only* against standard dense baselines (ViT-small, GPT-2 medium). There are no experiments comparing DNAs against MoE, MoD, LayerSkip, or any other conditional computation framework at comparable scale. This gap means the paper cannot support the implicit claim that DNAs offer a *distinct* or *advantageous* trade-off over existing dynamic methods. While the paper explicitly disclaims SOTA-focus, the "generalization" claim sets an expectation that is not met by the evidence. This is the most significant weakness and the hardest to address post-hoc.

2. **No standard deviations, confidence intervals, or multi-seed reporting for any quantitative result.** All accuracy/perplexity numbers are reported as single values without variance estimates. Given that some comparisons are close (e.g., Top-1 DNA 79.1% vs ViT 79.8%; Top-2 DNA language validation loss 2.674 vs GPT-2 2.720), it is impossible to assess whether these differences are meaningful. Table 3's zero-shot results (ARC-E 59.2 vs 58.9, BoolQ 61.0 vs 60.5, etc.) are particularly affected. This is a standard methodological expectation for comparative claims; its absence weakens the quantitative evidence substantially.

### Minor

3. **Interpretability analysis is entirely qualitative without quantitative validation.** The claims about path specialization (brass instruments, puzzle pieces, verb variants, sentence boundaries) are supported only by cherry-picked examples. There are no quantitative metrics for concept fidelity, clustering purity, path-concept correlation, or statistical significance relative to random baselines. The comparison to random models for path clustering is mentioned but only cursorily explored. While qualitative analysis is valuable for an exploratory paper, the strength of the claims ("very clear *emergent* specialization") exceeds the rigor of the evidence.

4. **Key design choices are not ablated.** The method involves several non-trivial empirical choices: the soft fusion mechanism (Eq. 1), the backbone layers (N_b), the identity-module bias trick (Eqs. 2-3), routing frequency (every step vs. every layer), and module composition. None of these are ablated, making it impossible to determine which choices are essential and which are artifacts. The paper acknowledges these as "purely empirical design choices" but does not test their necessity or impact.

5. **Compute is measured only via active parameter counts, not actual FLOPs or wall-clock time.** The "compute" analysis counts module activations and active parameters, but does not measure actual FLOPs, latency, or throughput. The routing mechanism (linear classifiers), sparse attention patterns, and dynamic module selection all introduce overhead not captured by parameter counts. Without real efficiency measurements, the "learned efficiency" claim rests on a proxy metric.

6. **Parameter counts are not cleanly controlled between DNA and baseline models.** In Table 1, Top-1 DNA has 34M total params vs ViT-small's 22M (though 22M active). In Table 2, Top-2 DNA has 433M active params vs GPT-2's 406M — i.e., 6.7% more active parameters. The "30% shallower" GPT-2 baseline helps somewhat but is not a full substitute for proper scaling-law style comparisons. The comparison is reasonable given the exploratory nature but the asymmetry should be acknowledged more explicitly.

### Trivial

- The paper states that "we do *not* use load-balancing because our objective is to let models develop the structures they need." This is a defensible choice for an exploratory study, but the potential impact on the observed specialization patterns (e.g., some modules being rarely used, making specialization analysis easier) is not discussed as a limitation.
- Figure notation: the "flow" diagrams (Fig. 2 bottom, Fig. 6 bottom) are visually engaging but underspecified in the caption — the reader must infer the meaning of circle size, absence, and connectivity from the text.

## Nice-to-Haves

- Ablations of the key design choices (Eq. 1 fusion vs. simpler aggregation, the backbone, router topology) to validate robustness.
- Quantitative path-specialization metrics (e.g., probing module representations, clustering metrics like NMI).
- FLOPs or wall-clock time measurements alongside active parameter counts.
- A comparison against at least one conditional computation baseline (e.g., an MoE or MoD model at the same scale) to contextualize the "generalization" claim.

## Removed Points

The following criticisms from the harsh reviewer were filtered:

- **"Missing comparisons against dynamic baselines invalidate the core contribution (Structural)"** — Retained as Major (not Fatal). The paper's core empirical contribution is feasibility and analysis, not outperforming MoE/MoD. The "generalization" framing creates an expectation gap but does not invalidate the paper's stated goals.
- **"Overclaimed generality, under-specified implementation"** — Removed. The method is described at reasonable detail for a conference paper; the specific choices are acknowledged as "purely empirical design choices" with many deferred improvements. The "Towards" framing and explicit disclaimers temper the generality claims.
- **"Vision Top-1 DNA results are presented as competitive, which is a stretch"** — Removed. 79.1% vs 79.8% is within 0.7%, which reasonably qualifies as "competitive" for an exploratory method.
- **"The omission of load-balancing is not discussed as a limitation"** — Removed. The paper explains the rationale for not using load balancing. The potential impact is a reasonable discussion point but not a substantive weakness.
- **"Figures are difficult to interpret"** — Removed as a trivial presentation nitpick; some complexity is inherent in visualizing routing patterns.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's framing of DNAs as better positioned as an "empirical study of emergent structure" rather than a "new method" paper is a useful meta-observation but is already implicit in the paper's explicit disclaimers.

## Suggestions

1. **Re-frame the contribution as an empirical study of emergent routing structure** rather than as a "new class of architectures" that generalizes MoE/MoD. This aligns the claims with the evidence and removes the pressure to outperform existing methods.

2. **Add at least one conditional-computation baseline** (MoE, MoD, or LayerSkip at comparable scale) to contextualize the results and ground the "generalization" framing.

3. **Report training runs with 3 seeds and include standard deviations** for all quantitative metrics, especially the zero-shot evaluation results in Table 3 where differences are small.

4. **Add quantitative specialization metrics** — at minimum, measure path-cluster purity or NMI, and show that trained models have higher specialization than random-initialization baselines beyond the power-law analysis.

5. **Measure actual FLOPs or runtime** for the skip/efficiency experiments to validate that active parameter savings translate to real compute savings, given the overhead of sparse attention and routing.

## Score and Decision

**Score: 5.0** — Borderline. The paper introduces a genuinely interesting idea for flexible conditional computation and provides a multi-domain feasibility demonstration with interesting qualitative analysis. However, the evaluation has significant gaps: no comparison against the conditional computation methods DNAs claim to generalize, no error bars on any quantitative result, purely qualitative interpretability claims without validation, and no ablations of key design choices. These weaknesses prevent the paper from being a strong accept but do not negate the value of the underlying idea.

**Decision: Reject** — In its current form, the paper's evidence does not adequately support its framing and claims. The core idea has merit and could form the basis of a stronger submission with the suggested revisions.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>