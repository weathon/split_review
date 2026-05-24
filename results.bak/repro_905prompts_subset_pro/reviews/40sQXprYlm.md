Now I have enough context. Let me compile the final review.

---

## Summary

This paper introduces Distributed Neural Architectures (DNA), a class of models where tokens are routed through an unstructured collection of computational modules via learned routers, with no fixed depth or feedforward ordering. The architecture naturally subsumes Mixture-of-Experts, Mixture-of-Depths, parameter sharing, and early-exit strategies. The authors train DNA models on ImageNet (ViT-scale) and on a language corpus (GPT-2 scale), demonstrating competitive accuracy/perplexity with dense baselines while also showing that compute efficiency can be learned via identity-module skipping. The most distinctive contribution is an analysis of emergent routing patterns, showing that token paths follow a power-law distribution and exhibit interpretable specialization (e.g., paths grouping edges vs. objects in vision, or punctuation vs. semantics in language).

## Strengths

- **Genuinely novel architectural paradigm**: The DNA framework — where tokens traverse an unstructured collection of modules through end-to-end learned routing — is a fresh departure from the fixed-depth, feedforward paradigm. The paper demonstrates this vision concretely in both vision and language domains, not merely as a proposal.

- **Competitive performance with dense baselines at non-trivial scale**: The top-1 DNA vision model reaches 79.1% ImageNet accuracy (vs. ViT-small at 79.8%) with matched active parameters (22M). The top-2 DNA language model achieves a validation loss of 2.674, outperforming GPT-2 medium (2.720) on the primary metric and on most downstream benchmarks (Table 3). These results credibly establish that distributed, learned routing does not inherently degrade task performance — the core feasibility claim the paper sets out to prove.

- **Rich, suggestive analysis of emergent routing structure**: The path-distribution visualizations (Figs. 1, 3, 8) reveal genuinely interesting patterns: vision paths specialize into edge-focused, background-focused, and object-focused routes; language routers group punctuation, word pieces, and semantically related tokens into different modules; and the compute-allocation analysis (Fig. 5) shows the model assigning more compute to images with intricate boundaries. These observations, while qualitative, are non-obvious and open interesting research directions.

- **Clear conceptual unification**: The paper shows how DNAs subsume MoE, MoD, weight sharing, and early-exit as special cases of a single routing framework (Section 2.1), and the flow diagrams (Figs. 2, 6 bottom) visually confirm that a mixture of these strategies emerges from training — a dense backbone that splits into distributed sparse subnetworks.

## Weaknesses

### Fatal

None. No single weakness invalidates the paper's core claims of feasibility and emergent structure.

### Major

- **Interpretability analysis is almost entirely qualitative, undermining the paper's most distinctive contribution.** The claim that routes are "human-interpretable" and that modules/paths "specialize" is supported only by hand-selected visualizations (Figs. 3, 4, 8) and anecdotal descriptions. There are no quantitative metrics: no mutual information between path identity and class label, no path-purity scores, no measurement of whether the observed specializations hold across the full dataset rather than selected examples. The power-law path distribution — presented as evidence of emergent structure — is explicitly shown by the authors to exist in randomly initialized models (Fig. 1c,d caption), which substantially weakens it as evidence for training-induced organization. A paper whose headline contribution is "interpretable emergent structure" needs quantitative evidence for that structure; qualitative examples are suggestive but not sufficient.

- **No comparison to existing sparse/dynamic architectures despite claiming to subsume them.** The paper motivates DNA as a generalization of MoE, MoD, parameter sharing, and early-exit models, but never compares against any of these. The sole efficiency baseline is a shallower GPT-2 (Table 3). Without showing that DNA's routing yields a better compute–accuracy trade-off than, say, a Mixture-of-Depths or MoE model with comparable active parameters, the claim that DNA represents a promising practical direction is not substantiated. The paper's explicit disclaimer that it is "not focused on beating SOTA" (footnote 3) limits but does not eliminate the need for at least one comparison to the methods it claims to generalize.

### Minor

- **Efficiency metrics are not defined in the main text.** The distinction between "active parameters" and "non-shared active parameters" (parenthetical values in Tables 1–2) is never explained in the body of the paper; the reader is directed to Appendix C (Section 3.3) for details that are stripped from the review copy. The numbers can be reverse-engineered (non-shared ≈ unique modules activated, active = total module invocations), but the lack of a clear definition in the main text makes the efficiency comparisons hard to evaluate. This also affects the language-model comparison: the top-2 DNA has 603M total parameters vs. GPT-2's 406M; while active parameters per token are similar (~433M vs 406M), the larger total parameter count gives DNA an advantage in memory and potential representational capacity that is not controlled for.

- **Training stability and convergence of routing are not discussed.** Figures 2 and 6 (top-right) show substantial fluctuations in the effective number of compute nodes — particularly for the top-1 DNA language model, which oscillates between ~1.5 and ~2.5 even late in training. The paper never addresses whether these fluctuations represent ongoing instability, a failure to converge, or benign variation. For a method that relies on learned routing to allocate compute, this deserves at least a brief discussion.

- **Bias-update hyperparameters unreported.** Equation 3 introduces two hyperparameters — the target skip ratio \(r\) and the update rate \(u\) — whose values are not given in the main text and whose sensitivity is not explored. Combined with the unusual sign-based update rule (rather than a standard auxiliary loss), this makes the compute-efficiency training procedure difficult to assess or reproduce from the main text alone.

### Trivial

- The mapping between model variants and figures is occasionally confusing (e.g., Section 3.2 references a "top-1 DNA model shown in Fig. 2" for path analysis, but Fig. 2 shows both top-1 and top-2; the 25%-skip model referenced in Section 3.3 is the top-2 variant but this is only clear from Table 1).

## Nice-to-Haves

- Quantify the association between paths and semantics: mutual information between path and class label (vision) or between path and part-of-speech/semantic category (language), with a random-model baseline. This would transform the interpretability section from suggestive to scientifically grounded.

- Measure actual wall-clock latency or FLOPs on representative hardware. The current "active parameters" metric does not capture the overhead of routing, sparse attention, or the fact that DNA modules process variable-sized token batches.

- Add at least one MoE or MoD baseline at matched active-parameter count, even if only for the vision domain, to contextualize DNA's efficiency.

- Acknowledge and ideally control for the total-parameter discrepancy in the language comparison (603M DNA vs. 406M GPT-2).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Ambiguous efficiency metrics — fundamental obstacle to evaluating claims" (from Harsh Critic):** The paper states that details are in Appendix C (stripped). The main-text numbers are interpretable with reasonable inference (non-shared = unique modules activated). Not a fundamental obstacle — demoted to Minor.

- **"Gradient flow through hard top-k is underspecified / not reproducible" (from Harsh Critic):** The paper describes the mechanism in Eq. 1 (using softmax probabilities \(\rho_i\) as combination weights), explicitly cites Roberts et al. (2022) and Doshi et al. (2023) for signal/gradient propagation choices, and this is a standard technique in the MoE literature. The description is sufficient for reproducibility.

- **"Power-law cannot be interpreted as training-induced phenomenon" (from Harsh Critic):** The paper explicitly states in the Fig. 1 caption that random models also exhibit power-law distributions. The paper is honest about this; the criticism reflects the paper's own disclosure.

- **"Cherry-picked examples" (from Harsh Critic):** Fig. 3 explicitly states "60 randomly selected patches that follow each path." The examples are randomly selected, not cherry-picked. The weakness is the qualitative nature of the analysis, not biased selection.

- **"Deep-dream visualizations have unclear scientific value" (from Harsh Critic):** The paper provides a clear explanation: they show how routing decisions develop across steps and reveal that early steps capture texture/edges while later steps capture larger-scale features. The scientific question they answer is stated.

- **"Missing related work / missing appendix proofs"** — REMOVED per hard rules. These are parser artifacts, not paper problems.

- **Strength Finder: "This paper addressed an important problem"** — REMOVED as generic/superficial. 

## Novel Insights

None beyond the paper's own contributions. The paper's core insight — that a fully distributed architecture with learned routing can be trained end-to-end at non-trivial scale and develops interpretable computation patterns — is itself the novel contribution. The reviews did not surface additional insights beyond what the paper already claims.

## Suggestions

- The single highest-impact change would be to add quantitative metrics for path specialization (mutual information, path purity, class-conditional distributions) with appropriate baselines (random model, shuffled labels). This would convert the paper's most interesting section from "suggestive" to "convincing."

- Add a MoE or MoD baseline on the vision task. Since DNA claims to subsume these methods, showing that it can match or exceed them on a compute-efficiency curve would substantially strengthen the paper.

- Discuss the routing stability question explicitly, even if only to note that the fluctuations at end of training are within an acceptable range or that they decrease with more training.

## Score and Decision

**Round 1 bracket:** The paper sits above ar9tcnD4e9 (4.75, rejected — similar architecture-rethink paper but tiny-scale evaluation) and z1mLNhWFyY (5.25, rejected — novel routing but limited scale). It is below t7P5BUKcYv (8.00, accepted — MoE++ with thorough empirical validation) and nt8gBX58Kh (6.33, accepted — clean analysis method). Initial bracket: **[5.0, 6.5]**.

**Round 2 narrowing:** Compared against 1qq1QJKM5q (5.67, accepted — COMET, fixed routing, broad evaluation) and pEKJl5sflp (6.00, accepted — SMN, clean agreement router, smaller-scale experiments). The DNA paper has more ambitious experiments than SMN but less rigorous evaluation than COMET. It is comparable to — but slightly weaker than — COMET (5.67) due to the qualitative-only analysis and missing comparisons. Final score: **5.5**.

**Anchor papers retrieved:**
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| XVHXVdoV11 | 3.40 | 1 | Collective model intelligence — much weaker, different topic |
| 7DY2DFDT0T | 2.50 | 1 | EfficientSkip — weaker, narrower contribution |
| sTI75sFQkn | 3.25 | 1 | dFCExpert — much weaker, domain-specific |
| ZHTYtXijEn | 2.33 | 1 | DIRAD — much weaker |
| ar9tcnD4e9 | 4.75 | 1 | Neural Modules — similar spirit, DNA is clearly stronger (real tasks vs. UCI datasets) |
| Olb8JwUGZ3 | 4.25 | 1 | Modular networks — DNA has more ambitious scope |
| tI3eqOV6Yt | 5.00 | 1 | Adaptivity and Modularity — DNA has larger-scale validation |
| 1qq1QJKM5q | 5.67 | 1 | COMET — closest comparison; DNA slightly weaker |
| nwDRD4AMoN | 9.00 | 1 | Kuramoto — much stronger, different topic |
| t7P5BUKcYv | 8.00 | 1 | MoE++ — much stronger empirical validation |
| I4e82CIDxv | 8.00 | 1 | Sparse Feature Circuits — much stronger, different contribution type |
| xXTkbTBmqq | 8.67 | 1 | OLMoE — much stronger |
| thqPibDg6A | 4.40 | 2 | MoE cluster analysis — DNA is stronger |
| z1mLNhWFyY | 5.25 | 2 | Gradient Routing — DNA has larger scale and more ambition |
| uWvKBCYh4S | 5.00 | 2 | MoE of LoRA — different problem setting |
| UUZuwDv8iw | 4.33 | 2 | Expert sparsification — DNA is more novel |
| PPjpGTPG5K | 5.33 | 2 | PERFT — different problem, DNA is more novel |
| 5Qxx5KpFms | 6.00 | 2 | Breaking scaling laws with modularity — theory paper, not directly comparable |
| nt8gBX58Kh | 6.33 | 2 | Multifractal analysis — different contribution type, stronger execution |
| pEKJl5sflp | 6.00 | 2 | SMN — DNA has larger-scale experiments but less clean methodology; DNA slightly weaker |
| unE3TZSAVZ | 6.33 | 2 | Breaking scaling laws (duplicate) — same as 5Qxx5KpFms |
| qMUtej58Pc | 5.50 | 2 | Overconnectivity to sparsity — DNA has broader evaluation |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>