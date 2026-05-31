## Summary

Thoughtbubbles is a GPT-2-style decoder-only transformer that learns adaptive parallel computation during pretraining using only language-modeling loss. Between selected transformer layers, a "forking" mechanism assigns keep/fork scores to every residual stream and uses a top-k judgment to duplicate high-scoring streams into a "bubble" of latent computation; low-scoring streams are pruned. Score-attenuated attention and residual updates couple the scoring signal to the model's actual computational needs, and the multiple surviving streams for each token are merged via score-weighted output averaging. The method is evaluated at 150M–772M parameters on OpenWebText and peS2o, consistently outperforming both parameter-matched and computation-matched (Copy-k) baselines on perplexity and most zero-shot benchmarks.

---

## Strengths

- **Genuinely novel mechanism.** Prior pause-token/thinking-token approaches (Goyal et al. 2024; Herel & Mikolov 2024; Sun et al. 2025) require externally deciding where to insert extra residuals before training begins. Thoughtbubbles internalizes this decision into the network itself and learns it from LM loss alone, which is a meaningful architectural advance.
- **Careful compute-matched baseline.** The Copy-k baseline (duplicating input residuals before running all transformer layers) is a good-faith effort to disentangle "more parameters" from "adaptive parallelism." The consistent gap—e.g., Copy-5 at 20.90 vs. Ours κ=4L at 19.74 on 772M OpenWebText—supports the claim that adaptivity, not mere extra compute, drives improvement.
- **Consistent scaling behavior.** Results across three parameter scales on two qualitatively different corpora (web text vs. academic papers) show the same ordering, suggesting the effect is robust rather than cherry-picked.
- **Interpretable computation allocation.** The entropy–forking analysis (Fig. 5) demonstrates that the model allocates computation at moderately uncertain tokens without any explicit supervision for this behavior. The additional finding of a concave relationship (highest-entropy tokens receive relatively less forking) is a scientifically interesting behavioral signature.
- **Attention to forked children (Fig. 4).** Showing that the parent "og" token attends an order of magnitude more to its forks than to unrelated tokens provides mechanistic evidence that the forked streams are genuinely useful, not merely decorative computation.
- **Cross-scale perplexity lift.** The 319M Thoughtbubbles model outperforming the 772M parameter-matched baseline on OpenWebText perplexity (20.23 vs. 21.22) is a striking result that concretely illustrates compute-efficiency gains.

---

## Weaknesses

### Fatal
None identified.

### Major

1. **Ambiguous FLOPs accounting.** The paper characterizes Copy-5 as "roughly FLOPs-matched" against κ=4L without reporting actual FLOPs counts. During training, the average effective sequence length in Thoughtbubbles depends on how many tokens are actually forked—a quantity that changes across training and differs by layer. Without reporting mean forked-token counts and resulting per-step FLOPs, it is impossible to verify that the comparison is fair. If Thoughtbubbles routinely runs at a fraction of κ=4L due to the top-k pruning, the training FLOPs may actually be lower than Copy-5; if near κ is routinely hit, they may substantially exceed Copy-5.

2. **BLiMP underperformance on peS2o is unexplained.** On peS2o (772M), Thoughtbubbles κ=4L scores 67.4 on BLiMP versus 71.6 for Copy-5 and 69.8 for the baseline—a meaningful regression on syntax understanding. The same pattern appears at 319M (68.6 vs. 71.8 for Copy-3). The authors explain this as "pruned dynamic parallel computation may not be as helpful for syntax," which is descriptive rather than explanatory. This divergence between perplexity improvements and BLiMP regressions suggests the model may be trading off syntax-level coherence for n-gram smoothness, and the paper does not investigate this.

3. **Autoregression requires non-trivial mitigation.** The paper acknowledges that naive token-by-token autoregression produces a distribution shift relative to blockwise scoring (Fig. 6) because the max forking budget is effectively much larger for short prefixes. The dynamic-budget mitigation is described in an appendix (removed from this copy). Until a lightweight, hardware-efficient autoregressive inference path exists, practical deployment of the method is non-trivial, and this limits real-world utility.

### Minor

1. **Forking layer placement lacks ablation in the main text.** Forking is placed before layers 3, 7, and 11 for all models. The choice is important (the paper notes that too much forking creates a gradient bottleneck), but the ablation is deferred to an appendix rather than presented in main results.

2. **Partial-rotation RoPE for forked tokens is ad hoc.** The position-embedding design for cloned streams (proportional partial rotation) is mentioned but not ablated, so it is unclear whether this specific design is necessary or whether simpler alternatives (same position, or fixed offset) would work comparably.

3. **Training scale is modest.** Training on 2.5B tokens at up to 772M parameters puts models in a significantly undertrained regime by modern standards; it is not clear whether the observed adaptive-computation signal would persist, strengthen, or weaken under Chinchilla-optimal training regimes.

### Trivial
None.

---

## Nice-to-Haves

- A FLOPs-per-step comparison table (training and inference) with exact token-count statistics (mean/median active block size) would make the compute-matched comparison rigorous.
- A brief investigation of why BLiMP degrades on peS2o while perplexity improves would sharpen the paper's understanding of what the forking mechanism is and is not good at.
- An ablation swapping the partial-rotation RoPE scheme for simpler alternatives would clarify how sensitive the method is to this design choice.

---

## Novel Insights

The most distinctly novel insight is that a transformer can learn to *self-generate* working memory in the form of cloned residual streams entirely from LM loss, without any external annotation of "hard" tokens. The emergent computational profile—more forking at moderate-entropy tokens than at maximum-entropy tokens—suggests the model has implicitly learned that high uncertainty caused by structural boundaries (clause edges, coreference) is not resolvable by extra computation, whereas high uncertainty caused by lexical ambiguity is. This concave entropy–forking relationship was not predicted by the design and constitutes a substantive empirical finding about how latent computation can self-organize in a language model.

---

## Suggestions

- Report mean active block size (relative to κ) per dataset/scale; this directly settles the FLOPs-matching question.
- Provide a dedicated investigation of BLiMP: compute cross-correlation between forking rate and syntactic dependency distance to test whether the architecture systematically deprioritizes syntax-critical tokens.
- Evaluate whether gradient noise during top-k (e.g., Gumbel-top-k or straight-through estimator) alleviates the gradient bottleneck identified in Limitations without the current restriction to early forking layers.
- Report wall-clock training time relative to the baseline to give readers a practical sense of overhead.

---

## Score and Decision

The paper introduces a genuinely novel unsupervised adaptive computation mechanism, validates it consistently across three scales and two corpora with a rigorous computation-matched baseline, and provides interpretable analyses of the learned behavior. The main weaknesses—imprecise FLOPs accounting, unexplained BLiMP regression on one corpus, and an autoregression challenge requiring non-trivial mitigation—are real but do not invalidate the core contribution. The method advances a clearly important open problem (pretraining-time adaptive compute) and opens a credible research direction.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>