Now I have a good calibration picture. Let me construct the final review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper introduces Distributed Neural Architectures (DNAs), where tokens are dynamically routed through a collection of modules (transformer blocks, MLPs, attention) via learned routers rather than following a fixed feed-forward path. The authors train DNA models in vision (ImageNet, ViT-small scale) and language (FineWeb-Edu, GPT-2 Medium scale), demonstrating trainability and competitive performance, and analyze emergent properties: power-law path distributions, path specialization, and interpretable compute allocation.

## Strengths
- **Competitive performance demonstrated across two domains with explicit comparisons**: Top-2 DNA language model (433M active params) achieves lower validation loss than GPT-2 medium (2.674 vs 2.720) and outperforms it on 6 of 7 zero-shot benchmarks (ARC-E, BoolQ, HellaSwag, LAMBADA, PIQA, Wiki perplexity). In vision, Top-1 DNA (79.1%) and Top-2 DNA (78.8%) are within ~1% of ViT-small (79.8%). The paper is transparent about its exploratory scope (footnote 3: "not focused on beating SOTA models").

- **Emergent path specialization supported by complementary qualitative analyses**: Figure 3 shows frequent paths aggregating patches sharing high-level features (edges, flat color regions) while rare paths group specific concepts (brass instruments, puzzle pieces). The deep-dream reconstructions (Figure 4) trace feature emergence through routing steps. Language analysis (Section 4.2) demonstrates that router R₁ consistently sends semantically similar words (punctuation, plural nouns, verb variants) to the same modules across different example paragraphs.

- **Power-law path distributions characterized with a random-initialization baseline**: The paper documents that trained DNA models exhibit power-law path distributions (exponent -1 for vision, -1.2 for language) and compares this against a randomly-initialized DNA baseline (also power-law, exponent -1), using this contrast to argue that trained models' specialization is qualitatively different and non-trivial (Section 3.2, footnote 5).

- **Honest reporting of negative results**: The language parameter-sharing analysis (Section 4.3) concludes that module reuse "is most likely random in the language case," and the paper transparently reports the poor performance of the compute-skip language model. This scientific candor is commendable.

## Weaknesses

### Major
- **The "competitive" claim is undermined by unacknowledged total-parameter overhead.** In vision, Top-1 DNA has 34M total parameters vs. ViT-small's 22M (55% increase). In language, Top-1 DNA has 583M total vs. GPT-2's 406M (44% increase). The paper foregrounds "22M active" and "406M active" in the tables (Tables 1-2) as the relevant comparison metric but never acknowledges the storage/memory overhead of the extra parameters or compares against total-parameter-matched dense baselines. (Top-2 DNA vision at 18M total params is actually *smaller* than ViT-small, so the issue is not universal, but it applies to the primary Top-1 comparison which should be the fairest.)

- **The language compute-efficiency variant performs poorly and the analysis stops short.** The top-2 DNA (30% skip) model (Table 3) is worse than the GPT-2 (30% shallower) baseline on **every metric** (e.g., LAMBADA drops from 31.4 to 23.8, Wiki PPL from 38.0 to 52.6). The paper frames this as demonstrating "learned compute efficiency" but the learned skipping underperforms a simple uniform depth reduction with no analysis of *why*. This weakens the claim that DNAs "allocate compute intelligently" in the language domain.

- **No error bars or multi-seed results.** Results are reported as point estimates from "the best run of each model" found via grid search (Section 3.1, Section 4.1). The vision gap (79.1% vs 79.8%) and the language Top-1 loss gap (2.754 vs 2.720) are narrow enough that single-run comparisons make it impossible to assess significance. For a paper whose central claim is being "competitive" (i.e., close to a baseline), variance estimates are essential.

### Minor
- **Interpretability analysis is entirely qualitative.** The path specialization findings (Figures 3, 8) and compute-allocation analysis (Figure 5) rely on visual inspection of hand-selected examples. The paper itself acknowledges that random DNA models also exhibit clustering (Section 3.2), making it critical to **quantify** whether trained routing is meaningfully more interpretable—via metrics such as correlation with segmentation masks or POS tags, or a baseline comparison against random routing. The deep-dream visualizations (Figure 4) are suggestive but the reconstructions are classified with near-chance confidence (p=0.44–0.55); the paper notes this but does not fully reconcile it with the interpretability claims.

- **No ablation of the routing mechanism itself.** The paper never compares learned routing against fixed, semantic, or random routing to isolate how much the learning contributes vs. what the architecture provides by default. Given the finding that random models also produce structured clustering, this ablation is needed to substantiate the claim that end-to-end training produces meaningful routing.

- **No wall-clock or throughput measurements for efficiency claims.** The paper claims compute efficiency (Section 3.3, Section 4.3) but provides no actual runtime measurements. Given the overhead of routers and dynamic attention grouping, it is unclear whether the parameter savings translate to real-world speedups.

### Trivial
None.

## Nice-to-Haves
- Multi-seed experiments with error bars for all main comparisons.
- A total-parameter-matched dense baseline (e.g., ViT with ~34M params for the Top-1 DNA vision comparison).
- Quantitative interpretability metrics (e.g., correlation of routing with ground-truth segmentation masks or POS tags, with a random-routing baseline).
- Wall-clock/throughput measurements for the compute-efficiency variants.
- An analysis explaining *why* the learned skips underperform uniform depth reduction in the language domain.

## Removed Points
The following points from the Harsh Critic were removed after verification:
- "The paper does not adequately discuss how DNAs differ from existing fully-routable architectures" → This is a related-work framing concern that cannot be verified as a missing gap without external knowledge of the full literature; the paper clearly positions itself relative to MoE, MoD, and parameter sharing in the introduction.
- "The subtraction term in Equation (1) is awkwardly explained" → The paper acknowledges and explains this design choice in footnote 4.
- "Deep-dream reconstructions are classified with near-chance probabilities (0.44–0.55)" → The paper explicitly reports these probabilities and notes that top-5 predictions capture the correct class hierarchy; this is acknowledged rather than concealed.
- "Scale is very small (ViT-Small / GPT-2 Medium)" → The paper explicitly states it is "not focused on beating SOTA models" and acknowledges the scale limitation.
- "The paper does not specify what happens when multiple tokens are routed to an attention module" → The Figure 1 caption clearly states: "the attention pattern is computed *only* between these tokens."
- Various formatting/style nitpicks, reproducibility complaints about missing appendix content (which the parser strips from all papers), and speculative concerns about training instability and router collapse without evidence from the text.
- Several strength-finder strengths that were generic or conflicted with verified weaknesses were also removed.

## Novel Insights
The most interesting observation that emerges from filtering the reviews is the interplay between the power-law path distribution and the random-initialization baseline. The paper documents that random DNA models also produce power-law distributions (exponent -1), which suggests the architecture itself imposes this structure regardless of training. What distinguishes trained models is the *qualitative nature* of the clustering—trained models group by semantic features, random models by superficial similarity (attributable to signal propagation theory, as noted in footnote 5). This is a nuanced finding that deserves more rigorous quantification than the current cherry-picked examples provide, and it raises an interesting open question: how much of the "emergent" structure in conditional computation architectures is truly learned versus architecturally determined?

## Suggestions
1. Add a total-parameter-matched dense baseline for the Top-1 DNA comparisons to properly support the "competitive" claim.
2. Provide multi-seed results with error bars for the main comparisons (vision accuracy, language loss/benchmarks).
3. Add a quantitative interpretability evaluation: for vision, correlate path assignments with semantic segmentation masks; for language, correlate routing with POS tags or syntactic roles. Include a random-routing baseline to demonstrate that trained routing is meaningfully better.
4. For the language efficiency model, analyze *why* learned skipping underperforms uniform depth reduction—this would turn a negative result into an informative one.
5. Report wall-clock inference times for at least one DNA configuration to substantiate compute-efficiency claims.

## Score and Decision

**Round 1 — Bracketing:** I searched calibration papers across three bands. Weak anchors (<3.5) included EfficientSkip (2.50, Reject) — very thin experiments, no baselines, poor presentation. Middle anchors (3.5–7.5) included Tight Clusters (7.00, Accept) — strong theory + experiments; More Experts Than Galaxies (5.67, Accept) — novel idea with implementation and evidence gaps; Mutual-Inform SMoE (5.75, Reject) — theoretical framing but limited empirical validation; Dynamic MoE (7.00, Accept) — good experiments, some weaknesses. Strong anchors (>7.5) included interpretability/mechanistic-analysis papers at 8.00 — not comparable in methodology. The broad bracket was **4.5–6.5**.

**Round 2 — Narrowing within bracket:** I retrieved additional anchors in (4.5, 6.5) and (5.5, 7.0). Key comparisons:
- **How many tokens is an image worth?** (5.75, Accept) — stronger empirical validation (reconstruction metrics, FID, quantitative token-specialization analysis at 57.8 mIOU). DNA is weaker on experimental rigor. DNA < this anchor.
- **Gradient Routing** (5.25, Reject) — novel method with broader applications but weak baselines and marginal gains. DNA ≈ this anchor or slightly better conceptually, but comparable empirical rigor issues.
- **More Experts Than Galaxies** (5.67, Accept) — novel fixed-routing approach, tested across architectures, but implementation clarity and interpretability-evidence gaps. DNA ≈ this anchor.
- **A Theory of Initialisation's Impact on Specialisation** (6.00, Accept) — theory paper with experiments, different type but comparable in quality. DNA ∼ slightly below.
- **TC-MoE** (6.50, Accept) — stronger empirical validation. DNA clearly below this.
- **ElasticTok** (6.00, Accept) — clear empirical validation with reconstruction metrics. DNA below this.

**All anchor papers retrieved:**
| Path | Score | Round | Comparison |
|---|---|---|---|
| XVHXVdoV11.md | 3.40 | R1 | Rejected, thinner contribution |
| 7DY2DFDT0T.md | 2.50 | R1 | Very thin, poorly executed |
| nwDRD4AMoN.md | 3.00 | R1 | Different topic, weaker execution |
| vlOfFI9vWO.md | 3.00 | R1 | RL-based token selection, less developed |
| SrnTGdJKYG.md | 3.00 | R1 | VRP, not comparable |
| NSBP7HzA5Z.md | 3.00 | R1 | Inductive bias paper, weaker evidence |
| T26f9z2rEe.md | 7.00 | R1 | Stronger experiments, better empirical support |
| V7EiYG5DwZ.md | 5.75 | R1 | Similar quality, rejected on novelty/validation |
| Pu3c0209cx.md | 7.00 | R1 | Strong theory + experiments, clearly above DNA |
| QHzzAU7Qf9.md | 6.00 | R1 | Well-written but marginal improvements, rejected |
| 1qq1QJKM5q.md | 5.67 | R1 | Comparable: novel idea, evidence gaps |
| PPjpGTPG5K.md | 5.33 | R1 | MoE fine-tuning, thinner |
| DzGe40glxs.md | 8.00 | R1 | Mechanistic interpretability, not comparable |
| I4e82CIDxv.md | 8.00 | R1 | Interpretability, not comparable |
| 12B3jBTL0V.md | 5.00 | R2 | Vision modeling, weaker experimental design |
| qPTFzmXVLd.md | 5.50 | R2 | Visual token analysis, similar exploratory spirit |
| HiTg16qhxp.md | 5.50 | R2 | Dynamic activations, comparable exploratory quality |
| RQz7szbVDs.md | 6.00 | R2 | Theory paper, cleaner execution |
| z1mLNhWFyY.md | 5.25 | R2 | Gradient routing, comparable rigor issues |
| mb2ryuZ3wz.md | 5.75 | R2 | Adaptive tokenization, stronger empirical validation |
| tFV5GrWOGm.md | 6.00 | R2 | ElasticTok, stronger empirical validation |
| 6qUUgw9bAZ.md | 6.50 | R2 | Adaptive compute allocation, stronger evaluation |
| 8sSqNntaMr.md | 6.33 | R2 | LLM routing, stronger evaluation |
| dsP91M4hDL.md | 6.50 | R2 | TC-MoE, stronger empirical support |

**Final calibration:** The DNA paper sits between the 5.25 (Gradient Routing, Reject) and 5.75 (More Experts Than Galaxies, Accept / How many tokens, Accept) anchors — closer to the lower end of this range due to the unaddressed total-parameter confound and the entirely qualitative interpretability claims. On experimental rigor, it is clearly below the 6.0+ anchors (ElasticTok, TC-MoE, A Theory of Initialisation). The central ideas are interesting and the qualitative findings are genuinely novel, but the evidence base is systematically thinner than what ICLR expects.

**Score:** 5.5  
**Decision:** Reject

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>