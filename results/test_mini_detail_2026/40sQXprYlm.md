Now I have a thorough understanding of the paper and the calibration landscape. Let me write the final consolidated review.

## Summary

This paper introduces Distributed Neural Architectures (DNAs), a family of models where each token/patch follows a data-dependent path through a collection of modules (transformer, MLP, attention, identity, etc.) selected by learned routers. DNAs generalize mixture-of-experts, mixture-of-depths, parameter sharing, and early-exit under a single framework. The authors train vision models on ImageNet (ViT-Small scale) and language models on FineWeb-Edu (GPT-2 Medium scale), compare against dense baselines, and analyze emergent routing patterns. The core findings are: (i) DNAs are competitive with dense baselines in both domains, (ii) compute efficiency (module skipping) can be learned from data, and (iii) the resulting routing patterns exhibit interpretable specialization and a power-law path distribution.

## Strengths

- **Genuinely novel architectural framework.** The DNA formulation subsumes multiple conditional computing paradigms (MoE, MoD, parameter sharing, early-exit) under a single learned-routing mechanism. Treating connectivity as emergent rather than hard-coded is a conceptually clean contribution that goes beyond any single router tweak.

- **Competitive performance demonstrated across two domains.** The top-2 DNA language model matches or exceeds GPT-2 Medium on 5 of 8 metrics (Table 3), including lower validation loss (2.674 vs. 2.720) and higher HellaSwag (41.8 vs. 40.5). In vision, the top-1 DNA reaches 79.1% ImageNet accuracy against ViT-small's 79.8% (Figure 2). The shallower GPT-2 baseline (30% fewer layers) provides a reasonable compute-efficiency comparator.

- **Emergent power-law path distribution.** Figures 1(c–d) show that path probabilities follow a power-law (exponent −1 for random, −1.2 for trained). This is a genuinely novel empirical finding about the emergent connectivity structure that could spur further theoretical work.

- **Qualitative interpretability analysis is compelling and visually rich.** Path specialization (Figure 3) demonstrably groups semantically related patches (edges, color regions, brass instruments, puzzle pieces). The deep-dream reconstructions (Figure 4) show hierarchical feature development across routing steps. The random model baseline check (Appendix G.2) adds appropriate caution.

## Weaknesses

### Major

- **No comparison against the conditional computing methods DNAs claim to generalize.** The paper positions DNAs as a generalization of MoE, MoD, and early-exit, but provides no direct comparison to any of these. Evaluating against only dense baselines (ViT-small, GPT-2 medium) does not test whether the *flexibility* of heterogeneous routing provides benefits over simpler conditional architectures. An MoE baseline with matched total parameters or an MoD model with a comparable skip target would directly test the value of the DNA framework's generality. Without these, the paper's core positioning as a generalization is conceptually stated but empirically untested.

- **Efficiency savings are reported only as module counts, with no accounting for routing overhead or actual runtime.** The paper measures "normalized compute" as the fraction of modules activated per token. While this is a valid first-order proxy, the routers themselves consume compute (softmax, top-k selection), and the sparse attention patterns (attending only among tokens routed to the same module) may be less efficient in standard implementations. The paper provides no FLOPs estimate, no wall-clock measurements, and no analysis of how routing overhead scales. The efficiency motivation is prominent in the introduction, making this gap consequential.

### Minor

- **Interpretability analysis is entirely qualitative.** The path-specialization claims (e.g., "rank-775 path clusters brass instruments") are supported by example images but not quantified. There is no clustering purity metric, no inter-annotator agreement, and no statistical test beyond the single random-model baseline comparison. The analysis is suggestive and well-presented but does not constitute strong evidence.

- **Only one seed reported per configuration.** For a paper making comparative claims (competitive with baselines, compute allocation patterns), even a small number of seeds with variance bars would meaningfully strengthen the evidence.

- **Language models trained for only 21B tokens on FineWeb-Edu.** The paper acknowledges this limitation and the models are described as "vastly underparametrized." This is acceptable for a proof-of-concept but limits the generalizability of findings about routing behavior in language.

- **Parameter sharing analysis for language models relies on informal evidence.** The claim that module reuse is "most likely random" in the language case is based on "no correlation" between two model runs, but no correlation metric is reported. The analysis in the vision case is more thorough.

### Trivial

- None beyond what is already listed as Minor.

## Nice-to-Haves

- Adding FLOPs estimates for the full forward pass (including routers and attention) would directly address the efficiency question.
- A comparison to a standard MoE or MoD model with matched parameters would test whether DNA's flexibility adds value over simpler conditional architectures.
- A quantitative component for the interpretability analysis (e.g., clustering purity on path assignments) would strengthen the specialization claims.
- Reporting variance across multiple seeds would improve the statistical credibility.

## Removed Points

These points were identified by reviewers or the system but removed after verification:

- **"The bias trick is taken from DeepSeek and should be acknowledged more explicitly."** — The paper does cite Liu et al. (2024) for this trick. The reference is present.
- **"The top-1 DNA has a 12M parameter gap in total parameters (34M vs 22M) which may give an unfair advantage."** — The paper reports both active and total parameters and explicitly compares on active parameters (Table 1). The active parameter count is matched (22M). The total parameter gap is disclosed transparently. This is not an unfair comparison; it reflects the nature of sparse models.
- **"No load-balancing makes the model harder to compare to standard MoEs."** — The paper explicitly states this is intentional: "We do not use load-balancing because our objective is to let models develop the structures they need." This is a design choice, not an oversight.
- **"25% skip target is not verified."** — The paper states "normalized compute" is centered around 0.75 (Figure 5 histogram), which corresponds to 25% skipping. This is consistent with the target.
- **"Power-law finding is not used."** — The power-law is presented as an empirical observation about emergent structure, which is itself a contribution. Not every finding needs to be "used."
- **Missing related works concerns.** — Removed per instructions (no external sources to verify).
- **Grammar/formatting nitpicks.** — Removed per instructions (parser artifacts).

## Novel Insights

The calibration revealed an interesting tension: while the paper's closest comparison class (conditional computing papers like DirMoE, DARE) are scored for their incremental improvements to specific routing mechanisms, the DNA paper takes a fundamentally different approach — instead of improving an existing mechanism, it proposes a meta-framework where the routing structure itself is learned. This difference in ambition makes the paper harder to evaluate against standard anchors: its contribution is broader but its evaluation is less focused. The most valuable insight from synthesizing the reviews is that the paper's biggest weakness (missing MoE/MoD baselines) is also the most easily fixable — adding such comparisons would directly validate the framing without requiring new methodology. The interpretability analysis, while qualitative, goes substantially beyond what is typical in conditional computing papers and is a genuine differentiator.

## Suggestions

1. **Add MoE and MoD baselines.** This is the single most impactful addition. Train an MoE model with the same total module count as the DNA and top-2 routing (all modules are transformer blocks), and an MoD model with comparable skip targets. This directly tests whether DNA's heterogeneous module structure adds value.
2. **Estimate FLOPs for the full forward pass.** Count multiply-adds for routers (softmax + top-k), attention (under dynamic sparsity patterns), and MLP modules. Even with rough estimates, this would support or qualify the efficiency claims.
3. **Add a quantitative interpretability experiment.** For example, measure clustering purity of path assignments against ImageNet class labels or a set of visual categories. Even a simple metric would strengthen the specialization claims.
4. **Run 3 seeds per configuration** and report mean ± std for key metrics.

## Score and Decision

**Calibration Summary:**

| Anchor Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| TAR Token Adaptive Routing | 3.00 | R1 (weak) | Weaker — limited experiments, tenuous claims |
| Subjective Depth Transformers | 3.00 | R1 (weak) | Weaker — similar routing idea but weaker results |
| Automated Architecture Synthesis | 3.00 | R1 (weak) | Weaker — similar ambition, less empirical work |
| Selective Deferred Routing | 3.33 | R1 (weak) | Weaker — narrower scope |
| DirMoE | 5.33 | R1 (mid) / R2 | Similar novelty level, stronger evaluation (MoE baselines present), smaller scale (185M vs two domains) |
| MoE Trilemma (cluster+compress) | 4.00 | R1 (mid) / R2 | Weaker — limited baselines, overclaimed |
| DARE Dynamic Routing | 4.50 | R1 (mid) / R2 | Weaker — limited expert count, missing efficiency measurement |
| MoE Quantization | 5.33 | R2 | Methodologically tighter, narrower contribution |
| ERC Loss (MoE coupling) | 6.67 | R2 | Stronger — thorough evaluation at scale (15B params), cleaner experiments |
| Universal Model Routing | 6.50 | R2 | Stronger — cleaner experimental setup with theory |

**Round 1 bracket**: 3.5–6.0 (above weak papers at ~3.0, below strong papers at 7.0+)

**Round 2 narrowing**: Compared against DirMoE (5.33, Accept) and DARE (4.50, Reject) and MoE Trilemma (4.00, Reject), the DNA paper is stronger than DARE and the Trilemma paper in terms of contribution breadth, but weaker than DirMoE in evaluation coverage (missing MoE baselines). The ERC Loss (6.67, Accept Oral) is clearly stronger in experimental rigor. The DNA paper sits between DirMoE and the Trilemma paper — roughly 5.0.

**Final score**: 5.0 — The paper has a genuinely novel and ambitious framework with promising initial results and interesting emergent-phenomena analysis, but the evaluation has two significant gaps (missing MoE/MoD baselines, no accounting for routing overhead in efficiency claims) that prevent the evidence from matching the ambition.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>