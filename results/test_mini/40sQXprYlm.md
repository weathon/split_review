## Summary

The paper introduces Distributed Neural Architectures (DNAs), a framework that generalizes conditional computation (MoE, MoD, parameter sharing, early exit) into a unified paradigm where each token follows a learned, content-dependent path through a flexible collection of modules and routers. The authors train DNAs on ImageNet (vision) and FineWeb-Edu (language), showing competitive performance against dense ViT and GPT-2 baselines, and analyze emergent properties including power-law path distributions, interpretable routing specialization, and content-dependent compute allocation.

## Strengths

1. **Novel and unifying architectural framework.** DNAs generalize MoE, MoD, parameter sharing, and early exit into a single learnable routing space where tokens determine their own computation paths. This is a genuinely new perspective on conditional computation that goes beyond incremental improvements to existing MoE methods. The paper explicitly scopes itself as a feasibility demonstration, not a SOTA chase — "our work is *not* focused on beating SOTA models in any domain, but on showing that distributed models are *feasible* and on analyzing their emergent structure."

2. **Cross-domain validation (vision + language).** DNAs are trained and evaluated in two very different domains — ImageNet classification and language modeling on FineWeb-Edu — with consistent results. The top-2 DNA language model achieves lower validation loss (2.674 vs. 2.720) and outperforms GPT-2 medium on 4 of 7 zero-shot benchmarks (ARC-E, BoolQ, HellaS, PIQA) in Table 3. The top-1 DNA vision model reaches 79.1% accuracy vs. the ViT baseline's 79.8% (Figure 2).

3. **Emergent interpretable routing with semantic grouping.** In vision, patches following high-rank paths group semantically related concepts (brass instruments, puzzle pieces; Figure 3). In language, early routers consistently group tokens by semantic role (verbs to one module, punctuation to another, plural nouns to a third; Figure 8). This goes beyond coarse token-level routing seen in standard MoE and provides evidence that the learned structure is meaningful.

4. **Power-law path distribution as an emergent property.** Both vision and language DNAs exhibit path distributions that follow power laws (exponents −1 and −1.2). The paper also notes that random (untrained) DNAs show a power law with exponent −1, providing a null baseline — this is good scientific practice that the paper deserves credit for.

5. **Content-interpretable compute allocation.** The top-2 DNA vision model (25% skip) spends more compute on boundary-rich images and less on background-dominated images (Figure 5), and the analysis of low-compute documents in the language setting (HTML, bibliography markers, non-Latin scripts) shows that compute savings are driven by input content rather than being random.

## Weaknesses

### Fatal
None.

### Major

1. **Interpretability analysis is entirely qualitative, lacking any quantitative validation.** The paper's claims about path specialization (e.g., "rank-775 path groups brass instruments") and router grouping ("early routers group similar tokens") are supported only by anecdotal visual examples and cherry-picked figures. No quantitative metrics are provided — no clustering purity, no mutual information between path assignments and class labels, no correlation with ground-truth segmentation boundaries. The paper itself notes that "a randomly initialized DNA model... can also cluster images" but by a different similarity measure, which actually underscores the need for quantitative validation to distinguish learned structure from artifact. For a central claim in the paper, this is a significant gap.

2. **Dynamic attention grouping is a structural architectural limitation that is not analyzed.** When a module processes attention, it operates *only* on the tokens routed to that module (Figure 1b). Tokens assigned to different modules in the same step never attend to each other. The paper describes this as "dynamic sparsity" but provides no analysis of its impact on representational capacity — especially in vision, where patches of the same object may be routed to different modules and lose the ability to exchange information. No ablation isolates this effect (e.g., comparing to a variant that allows full attention before or after routing). This is inherent to the proposed design and may limit scalability to tasks requiring long-range dependencies.

3. **Evidence for learned compute efficiency is thin.** The compute-efficient models use predetermined skip rates (25% for vision, 30% for language), and the model only learns to *allocate* that fixed skip budget — not to determine *how much* to skip per input. In the language setting, the top-2 DNA with 30% skip performs worse than a shallower GPT-2 baseline on *every* metric (loss 2.784 vs. 2.772 at comparable active params, and lower on all benchmarks in Table 3). No FLOPs or wall-clock measurements are reported — only normalized module counts. The bias-update rule in equation (3) is a sign-based heuristic (not gradient-based) with no convergence analysis. The paper's claim that "compute efficiency can be learnt from data" is directionally supported but the evidence is not commensurate with the strength of the claim as stated in the abstract.

4. **Uncontrolled baseline comparisons in language experiments.** The top-2 DNA language model has 433M active parameters vs. GPT-2 medium's 406M, plus additional routers and a larger module pool. The top-2 DNA outperforms GPT-2 medium on 4/7 benchmarks, but the comparison is not parameter-matched. A GPT-2 variant with the same active parameter count would be a more informative baseline. The paper does not discuss whether the small gains might be attributable to the extra capacity rather than the routing architecture itself.

5. **Language experiments are severely undertrained (21B tokens) and underparameterized.** The authors acknowledge this, calling the models "way too small to truly absorb it" and noting they operate in a "vastly 'underparametrized' regime." While the transparency is appreciated, it means the language results may not transfer to practical scales. Core findings (routing patterns, compute allocation) should be interpreted as preliminary.

### Minor

1. **No statistical significance or variance reported.** Accuracy/loss values are reported as point estimates without confidence intervals, standard deviations, or multiple-seed averages. This is common in large-scale experiments but limits the reader's ability to assess whether observed differences are meaningful.

2. **Power-law claim is based on visual inspection of log-log plots.** The paper states path distributions follow a power law based on eyeballing plots in Figures 1c-d with no goodness-of-fit test or alternative distribution comparison. The fact that a random (untrained) DNA also yields a power law with exponent −1 (as noted by the authors) suggests the power law may be a trivial consequence of the routing setup rather than a learned phenomenon — the paper does not rigorously disentangle these.

3. **The ad-hoc bias-update rule (equation 3) is justified heuristically.** The sign-based bias update for compute efficiency is borrowed from DeepSeek's load-balancing trick but repurposed for skipping. No convergence analysis, sensitivity study, or comparison to gradient-based alternatives is provided. While this is a practical design choice, it stands in contrast to the gradient-based training used for the rest of the model.

4. **"Active Params" definition could be clearer.** Table 1 reports "Active Params" with parenthetical "non-shared active params" but the distinction — whether module parameters are counted once per usage or once per forward pass — is not defined in the main text.

### Trivial
- Figure 1 caption text is duplicated in the parsed PDF (parser artifact).

## Nice-to-Haves
- Report FLOPs and wall-clock inference time for DNA vs. dense baselines, not just normalized module counts.
- Provide quantitative interpretability metrics (e.g., clustering purity between path assignments and class labels for vision, POS-tag alignment for language).
- Compare to a controlled dense baseline with identical active parameter count in the language experiments.
- Include training FLOPs/memory overhead of DNA vs. dense models.
- Ablate the effect of the dynamic attention grouping by comparing to a variant with shared/full attention.

## Removed Points

These points were identified by reviewers but are removed from the main evaluation because they are incorrect, nitpicky, or not applicable:

- **"Absence of gradient estimation for discrete routing decisions"** (Harsh Critic Weakness #1). REMOVED. The paper clearly specifies the mechanism in Section 2.2: softmax probabilities ρ = softmax(R(h)) are computed (differentiable), hard top-k selects modules, and the combination in equation (1) uses the differentiable ρ as weights. Gradients flow through ρ to router parameters. The paper explicitly states this builds on Roberts et al. (2022) and Doshi et al. (2023) "to ensure good signal and gradient propagation." This is the standard approach used in MoE routing and is not a missing detail.

- **Criticisms about deep-dream reconstructions being misclassified** (within Weakness #4). REMOVED. The paper acknowledges this and uses it as evidence of *hierarchical* classification (the model correctly identifies super-categories: birds vs. dogs, but struggles with fine-grained species). This is not a weakness — it is a meaningful observation the paper makes about the nature of learned routing.

- **"Missing related works"** and **"comparison to more recent baselines like DeiT-Small"**. REMOVED per the rules (no external sources to confirm, and the paper explicitly scopes out SOTA chasing).

- **Formatting nitpicks** (typos, garbled text, missing appendix references). REMOVED per rules (parser artifacts, not author errors).

- **"Cannot be independently verified"** style reproducibility concerns about cited entities. REMOVED per rules (cited works are assumed to exist).

- **Weakness about unfair comparison with baselines if asymmetry favors baselines.** REMOVED per rules (asymmetric comparisons favoring baselines are acceptable).

- **Strength Finder strengths that are generic or conflict with verified weaknesses** (e.g., "this paper addresses an important problem"). REMOVED kept only concrete, specific strengths grounded in evidence.

## Novel Insights

A genuinely novel observation emerges from the contrast between the vision and language settings. In vision, both the path distribution power law and the parameter-sharing patterns exhibit consistent, interpretable structure across images (reuse correlates with visual simplicity, path specialization aligns with semantic concepts). In language, by contrast, the parameter-sharing analysis finds "no correlation between two different DNA models" and the paper concludes that module reuse is "most likely random." This asymmetry is interesting and suggests that the nature of the routing structure learned by DNAs may be fundamentally different across modalities — vision inputs (patches of 16×16 pixels) have more consistent structural regularities than tokenized text, leading to more reliable emergent patterns. The paper notes this contrast in passing but does not develop it as a finding, which is a missed opportunity.

## Suggestions

1. **Add quantitative interpretability metrics.** For vision, compute the overlap between path clusters and ground-truth segmentation boundaries (e.g., using ImageNet-S segmentation masks). For language, compute clustering purity with part-of-speech tags or semantic role labels. This would transform the anecdotal observations into evidence.

2. **Run a controlled comparison.** Add a GPT-2 variant with the same active parameter count as the top-2 DNA (433M) by increasing the embedding/MLP dimensions. This would clarify whether the DNA's benchmark improvements come from the routing or from extra capacity.

3. **Report FLOPs or wall-clock time** for at least one setting. The "normalized compute" metric is fine for analysis, but practical efficiency claims need actual computational cost.

4. **Ablate the dynamic attention grouping** by training a DNA variant where all tokens are processed by a shared full-attention module before being redistributed. This would isolate whether the grouped attention harms representational capacity.

5. **Provide error bars across multiple seeds** for the key accuracy/loss numbers and for path-distribution statistics.

## Score and Decision

**Calibration procedure:**

**Round 1 (Bracketing):** Searched for "conditional computation mixture of experts dynamic routing emergent specialization" with score filters.
- Weak band (<3.5): Papers scoring 1.6–3.0 (e.g., "Sparsity and Superposition in MoE" at 2.0, "Reinforced Adaptive Routing" at 2.0) — these had fatal flaws or were deemed withdrawn. The current paper is clearly stronger.
- Middle band (3.5–7.5): Papers scoring 4.0–6.67 (e.g., "Improving MoE Performance" at 4.0, "Expert Divergence Learning" at 5.5, "Coupling Experts and Routers" at 6.67). The current paper sits in this band.
- Strong band (>7.5): Papers scoring 8.0 (e.g., LLM mechanistic analysis, embodied navigation) — these are well-executed papers on mature topics. The current paper is not at this level due to evidential weaknesses.
- **Initial bracket: 4.0–6.5**

**Round 2 (Narrowing):** Searched for "distributed architecture emergent specialization routing interpretability vision language" inside the bracket.
- "Understanding Cross-layer Contributions to MoE Routing" (5.00, Accept Poster) — purely analytical paper with a questionable metric. The current paper has higher novelty (new architecture vs. analysis tool) but weaker empirical validation. Comparable.
- "Multilingual Routing in Mixture-of-Experts" (5.50, Accept Poster) — strong empirical validation across 15+ languages with a practical intervention. The current paper is more novel (first to propose and train this architecture) but less rigorous.
- "Long-Tailed Distribution-Aware Router" (5.00, Reject) — incremental MoE improvement in vision-language models. The current paper has significantly higher novelty.
- **Narrowed bracket: 4.5–5.5. The paper is comparable to the 5.0–5.5 anchors in terms of overall quality, with higher novelty but weaker empirical support.**

Based on the calibration, the paper's genuine novelty (a genuinely new framework generalizing conditional computation) is weighed against significant evidential weaknesses (purely qualitative interpretability, weak compute efficiency evidence, uncontrolled comparisons, undertrained language experiments). This places it at the lower end of the accept zone at ICLR — a paper worth pursuing but needing substantial strengthening before acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>