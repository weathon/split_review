Now I have sufficient context from the anchors. Let me synthesize the final review.

**Round 1 bracket:** Based on initial comparisons, I estimated the paper in the 3.5–7.5 range (middle band), with topical anchors at 5.25 (Gradient Routing, Reject), 5.67 (COMET, Accept), 4.75 (Automatic Organization of Neural Modules, Reject), and weakness-anchored papers ranging from 3.67–5.75. The low-band anchors (2.33–3.40) had fundamental methodology issues that this paper does not share.

**Round 2 narrowing:** Queries in (4.5, 6.5) and (4.0, 6.0) brought in Scalable Modular Network (6.00, Accept), Breaking Neural Network Scaling Laws with Modularity (6.00, Accept), Mutual-Inform SMoE (5.75, Reject), and Dense Backpropagation for MoE (5.50, Reject). The paper is competitive with these in breadth and core results, but weaker on baseline comparisons and overclaiming — placing it slightly below the accepted papers and on par with the borderline reject ones.

**Anchor list:**
- XVHXVdoV11 (3.40, Reject): Collective Model Intelligence — different topic, lower quality; not comparable.
- OovfCS4FYT (3.25, Reject): Divisive Normalization — different subfield; not comparable.
- fnO5h1CFyh (3.00, Reject): Hebbian Temporal Memory — substantially weaker; not comparable.
- z1mLNhWFyY (5.25, Reject): Gradient Routing — similar methodology paper; current paper has broader scope but shares weakness of missing baselines.
- 1qq1QJKM5q (5.67, Accept): COMET — similar cross-domain modular routing paper; current paper has more novel architecture but weaker quantitative efficiency analysis.
- ar9tcnD4e9 (4.75, Reject): Neural Modules — similar modular architecture paper; current paper has stronger experiments.
- QHzzAU7Qf9 (6.00, Reject): Soft Merging of Experts — stronger baselines and writing but rejected; current paper is more architecturally novel but weaker on comparisons.
- t7P5BUKcYv (8.00, Accept): MoE++ — much stronger efficiency paper with wall-clock measurements; not comparable.
- 5Qxx5KpFms (6.00, Accept): Breaking Neural Network Scaling Laws — theory-heavy; current paper is stronger on experiments.
- pEKJl5sflp (6.00, Accept): Scalable Modular Network — tested on simpler tasks; current paper has larger-scale experiments.
- eWNEqdH0vk (5.75, Accept): Layerwise Recurrent Router — MoE routing improvement; current paper has a more novel architecture.
- V7EiYG5DwZ (5.75, Reject): Mutual-Inform SMoE — had theory + experiments but rejected due to writing and limited baselines.
- huy8g3iKy0 (5.50, Reject): Dense Backpropagation for MoE — MoE-specific improvement.
- LyNsMNNLjY (4.25, Reject): LLM Routing — different problem (LLM selection).
- Qyp3Rni2g1 (5.25, Reject): Efficiency Pentathlon — different topic.
- v675Iyu0ta (5.60, Reject): Interpretability Illusions — different topic (interpretability methods criticism).

**What did the low-band anchors fail at, and does the paper under review share any of those failures?** The low-band anchors (2.33–3.40) failed due to fundamentally flawed methodology (e.g., experiments too small to support claims, theory disconnected from results, lack of any meaningful validation). The current paper does not share those failures: it has solid experiments at non-trivial scale (ImageNet, 21B tokens of language data), clear methodology, and competitive results with dense baselines. Its issues are about missing baselines and overclaiming, not about fundamental unsoundness.

Now let me write the review.

Score: Let me think about this more. The paper shares some weaknesses with Mutual-Inform SMoE (5.75, Reject) — both lack certain important baselines and overclaim. But the current paper has a more novel architecture and broader scope. It shares the "missing baselines" criticism with Gradient Routing (5.25, Reject) but has better experiments.

I'll set the score at 5.0. This reflects: a solid paper with interesting contributions that is held back by:
1. Missing MoE/MoD comparisons despite the framing
2. Compute claims without FLOPs/wall-clock measurements
3. Qualitative-only interpretability evidence
4. Slightly overreaching claims

At 5.0, this is a borderline paper — not clearly acceptable but not clearly rejectable either. It has genuine contributions but also genuine gaps.## Summary

This paper introduces Distributed Neural Architectures (DNAs), a framework where each token follows a content-dependent path through a collection of modules (transformer, MLP, attention, identity) controlled by learned per-step routers. The architecture subsumes aspects of MoE, MoD, parameter sharing, and early exit as special cases. The authors train DNA models at ViT-Small and GPT-2 Medium scale in vision (ImageNet) and language (FineWeb-Edu) domains, showing they are competitive with dense baselines: the top-1 DNA achieves 79.1% vs ViT-small's 79.8% on ImageNet, and the top-2 DNA (433M active params) outperforms GPT-2 medium (406M) on 6 of 7 zero-shot benchmarks. The paper further analyzes emergent path structure, interpretable routing decisions, and compute allocation patterns.

## Strengths

1. **Novel and well-motivated architecture.** The DNA framework genuinely extends prior conditional computation approaches by allowing tokens to traverse modules in learned sequences rather than being restricted to per-layer expert selection or depth-only skipping. The proto-architecture design (backbone layers + routers + modules + identity modules for skip) is clearly described and the formulation is general enough to subsume several prior methods architecturally.

2. **Competitive performance with dense baselines in two domains.** This is the paper's core empirical contribution. In vision, the top-1 DNA (79.1%) is within 0.7% of a properly retrained ViT-small (79.8%) on ImageNet under the same augmentation pipeline (Fig. 2 top-left). In language, the top-2 DNA outperforms GPT-2 medium on 6/7 benchmarks with lower validation loss (2.674 vs 2.720) (Table 3). These results demonstrate that the added routing flexibility does not fundamentally harm task performance — a non-trivial result for a first feasibility study.

3. **Emergent compute allocation correlated with input content.** The paper shows (Fig. 5) that the top-2 DNA (25% skip) allocates compute differentially: boundary-rich images receive more computation, while visually simpler images receive less. In language, documents with HTML or non-Latin characters receive substantially less compute (Section 4.3). This allocation is achieved via identity modules and a bias-trick adapted from DeepSeek, without explicit content-level supervision — providing evidence that the model learns meaningful compute allocation.

4. **Rich analysis of emergent path structure.** The paper documents that path distributions follow a power-law (exponent ≈ -1 in vision, -1.2 in language), demonstrates path specialization (Fig. 3 shows patches following the same path sharing visual features like edges or brass instruments), and shows that early-layer routing groups semantically similar tokens in language (Fig. 8). The analysis of random-model baselines (also power-law with exponent -1) provides an honest baseline for these observations.

5. **Cross-domain validation.** Demonstrating the approach in both vision (discriminative, ImageNet) and language (generative, FineWeb-Edu) strengthens the generality claim considerably more than a single-domain paper would.

## Weaknesses

### Major

- **Missing comparison to MoE/MoD baselines despite the generalization framing.** The paper positions DNA as "a natural generalization of the sparse methods such as Mixture-of-Experts, Mixture-of-Depths, parameter sharing, etc." and claims "a mixture-of-all-of-these-methods emerges from end-to-end training." Yet there is no empirical comparison to any standard MoE or MoD baseline at matched total/active parameter counts. A reader cannot assess whether DNA's flexible routing provides any benefit over a standard MoE transformer. This is a gap between the paper's framing and its evidence base. While the paper's stated goal is feasibility (not superiority), the generalization framing naturally creates this expectation, and the paper would be stronger either by including such comparisons or by clearly scoping the claim as architectural only.

### Minor

- **Compute efficiency claims use only module-count proxies, not FLOPs or wall-clock time.** The paper measures "compute" as the number of modules used per token and "active parameters" as a proxy. This excludes router computation (each router applies a linear projection + softmax per step), the overhead of grouping tokens by their module assignments at each step (dynamic batching), and the implications of data-dependent sparse attention. The paper's stated motivation centers on inference efficiency, making the absence of any FLOPs estimate or wall-clock measurement a meaningful gap. This is an addressable issue — even an analytic FLOPs accounting would significantly strengthen the efficiency claims.

- **Interpretability claims are supported only by qualitative examples.** The paper states that "the paths taken by the tokens/patches and routing decisions are often human-interpretable" (abstract) and "the paths taken by patches are highly interpretable" (Section 3.2). The evidence consists of selected examples: 4 paths and 60 patches per path for Fig. 3, 3 deep-dream reconstructions for Fig. 4, and 2 paragraphs for Fig. 8. While these examples are genuinely interesting and worth reporting, the strength of the claim ("often") would warrant some systematic evaluation — e.g., measuring path-purity against class labels in vision or POS-tag agreement in language. The paper already has the data to compute such metrics; it is a missed opportunity.

- **The "mixture-of-all-methods" claim overreaches the evidence.** The paper asserts that MoE, MoD, weight sharing, and early exit all emerge from end-to-end training. The evidence supports: (a) weight sharing emerges (modules are reused), (b) MoD-like token skipping emerges (via identity modules), and (c) some path specialization emerges. However, no evidence of *early exit* (tokens terminating before the final step rather than passing through identity modules) is provided, and controlled evidence for MoE-like *expert specialization* (mutual information between module assignments and input features) is not given. This claim should either be systematically evaluated or scaled back.

- **Language experiments are at acknowledged insufficient scale.** The authors note that their models are "way too small to truly absorb" the FineWeb-Edu data. This limits the conclusions that can be drawn about the language setting. The comparison with "GPT-2 (30% shallower)" in Table 3 suggests that for language, the routing approach may be less effective than simply training a smaller dense model (top-2 with 30% skip performs worse than the shallower GPT-2 on all benchmarks). The paper acknowledges this but does not discuss the implications for the approach's viability in language.

### Trivial

- Equation (1) uses notation that is hard to parse; the superscript *t* on *M^t* refers to the t-th component of the output, but this is explained only in a parenthetical in the figure caption rather than in the main text.
- The "effective number of compute nodes" metric (Fig. 2 top-right) is confusingly labeled "top-k" on the axis but measures the number of *distinct* modules receiving tokens at each step — a measure of module utilization, not per-token compute or the top-k hyperparameter.

## Nice-to-Haves

- A training-time analysis of how the path distribution evolves (at initialization, early training, convergence) would strengthen the power-law analysis substantially, especially since the paper already notes that random models also exhibit power-law behavior.
- An ablation of proto-architecture design choices (e.g., number of modules, number of backbone layers, impact of removing identity modules) would help establish which design decisions matter.
- The deep-dream visualization (Fig. 4) is creative but the low classification confidence (0.44–0.55) and the lack of clarity about what "maximizing the total weight on all routing decisions" means make it hard to interpret. More explanation would help.

## Removed Points

*These points were surfaced by reviewers but are removed or demoted for the reasons stated below.*

- **"Power-law path distribution is not substantially different from random models"** — The paper already addresses this by noting that random models also show power-law behavior (exponent -1) and by reporting that trained models shift to different exponents (-1 for vision, -1.2 for language). The finding is presented as an observation, not as a claim of uniqueness. The paper even discusses in Appendix G.2 that this may relate to signal propagation in properly initialized random networks. This is handled responsibly, not as a weakness.

- **"The term 'distributed' is potentially confusing"** — A style nitpick. The paper defines the term clearly on first use.

- **"No discussion of training cost or convergence properties"** — The paper provides training curves (Fig. 2, 6) showing convergence behavior. While a deeper analysis would be nice, this is a nice-to-have, not a weakness.

- **"Missing related works"** — I cannot verify which related works are missing without external knowledge, per instructions.

- **Formatting/style nitpicks** — Removed per filtering guidelines.

- **Speculative concerns about dynamic batching overhead and sparse attention quality effects** — The harsh critic's concerns about dynamic batching overhead and whether sparse attention "may also reduce model quality" are speculative effects not demonstrated in the paper. The paper notes that the sparse attention is "dynamic sparsity" and presents competitive accuracy results that suggest quality is not severely impacted. These points are demoted from the main weakness list.

## Novel Insights

The most interesting observation beyond the paper's own contributions is the contrast between vision and language routing behavior: vision DNAs develop compute distributions that are roughly Gaussian and correlate with visual boundary complexity, while language DNAs show a more uniform compute distribution with only a long tail of low-compute documents (HTML, foreign characters). Additionally, parameter sharing correlates with image content in vision but appears "most likely random" in language. This inter-domain difference is under-explored in the paper but hints at fundamental differences in how routing mechanisms behave across modalities — a potentially fertile direction for future work.

## Suggestions

1. **Add an MoE or MoD baseline comparison** (even a simple one, e.g., replacing the routed module selection with a standard top-2 MoE at matched parameter count) to substantiate the "generalization" framing. If this is infeasible, retract the claim from the abstract and reframe DNA purely as a new architecture without asserting empirical connections to MoE/MoD performance.

2. **Provide an analytic FLOPs estimate** that includes router overhead. This does not require new training runs — just count operations in the forward pass (router linear projections + softmax, module computations, attention sparsity patterns) and compare to the dense baseline. The paper's efficiency motivation is weakened without this.

3. **Add a quantitative path-specialization metric** for vision: measure the purity of path-based clustering against ImageNet class labels or visual features (e.g., are patches on the same path more likely to belong to the same object category?). For language, measure mutual information between routing decisions and POS tags. This would transform the interpretability analysis from qualitative to evidential.

4. **Track the power-law exponent during training** (initialization → early training → convergence) to make the path-distribution analysis sharper. The paper already has all the checkpoints needed.

5. **Tone down or better support the "mixture-of-all-methods" claim.** Either provide evidence for the missing components (early exit, controlled expert specialization) or replace the claim with a more precise description of what actually emerges (parameter sharing, token skipping, path specialization).

## Score and Decision

**Calibration anchor summary:** The paper was compared against 15 retrieved anchors across two rounds. The most relevant topical anchors:
- Gradient Routing (5.25, Reject): similar methodology paper, missing baseline comparisons.
- COMET (5.67, Accept): cross-domain conditional computation, weaker on efficiency analysis.
- Scalable Modular Network (6.00, Accept): modular routing on simpler tasks.
- Soft Merging of Experts (6.00, Reject): strong baselines but rejected.
- Mutual-Inform SMoE (5.75, Reject): theory + experiments but missing baselines and overclaiming.
- Dense Backprop for MoE (5.50, Reject): MoE-specific improvement.
- Breaking Neural Network Scaling Laws with Modularity (6.00, Accept): theory-heavy with experiments on simpler tasks.

The paper under review sits between the accepted and rejected anchors. Its core results (feasibility, competitive performance with dense baselines, cross-domain analysis) are solid and on par with accepted papers like COMET and Scalable Modular Network. However, it shares the "missing important baselines" and "overclaiming" weaknesses that led to rejections for papers like Gradient Routing and Mutual-Inform SMoE. The net assessment places it at the boundary — not clearly acceptable due to the baseline gap and overclaiming, but not clearly rejectable due to the genuine architectural novelty and solid core experiments.

**Round-1 bracket:** 3.5–7.5. Low-band anchors (2.33–3.40) had fundamentally flawed methodology that this paper does not share. **Round-2 narrowing:** within 4.5–6.5, this paper is slightly below accepted 6.0 anchors due to missing baselines and overclaiming, but above the weakest rejected ones.

**What did the low-band anchors fail at?** Fundamentally flawed methodology (tiny experiments, theory disconnected from results, no meaningful validation). The paper under review does not share those failures — its core experiments are solid and its limitations are honestly discussed. Its issues are about framing-vs-evidence gaps, not unsoundness.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>