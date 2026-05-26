## Summary

This paper proposes Augmented Intermediate Representations (AIR), a defense against indirect prompt injection attacks that injects instruction hierarchy (IH) signals into every decoder layer of an LLM via layer-specific trainable embedding tables — rather than only at the input layer as done by prior work (Delimiters, ISE). The core idea is simple, parameter-efficient (0.005% overhead), and consistently outperforms existing input-only IH injection methods by a large margin: 1.6× to 9.2× reduction in gradient-based attack success rate across three model scales (3B, 7B, 8B), two training procedures (SFT, DPO), and multiple evaluation benchmarks, with negligible utility degradation.

## Strengths

- **Consistent and large quantitative improvement across gradient-based attacks.** In Table 1, AIR achieves the lowest ASR in *every* model × training × attack configuration. For example, on Llama-3.1-8B with DPO, AIR obtains 2.8% GCG ASR vs. 4.0% (ISE) and 13.0% (Delim); on Astra, 1.0% vs. 1.2% (ISE) and 36.9% (Delim). These are not cherry-picked — the advantage is systematic and often dramatic (up to 145× for Astra SFT).

- **Thorough evaluation across multiple dimensions.** The paper compares three IH injection mechanisms (Delim, ISE, AIR) × two training methods (SFT, DPO) × three model families (Llama-3.2-3B, Qwen-2.5-7B, Llama-3.1-8B) × multiple attack types (static, GCG, Astra) × two evaluation datasets (AlpacaFarm, SEP). Prior work typically studied a single combination (e.g., Delim+DPO in SecAlign). This breadth makes the generalization claim credible.

- **Minimal parameter and compute overhead.** AIR adds ~0.4M parameters for an 8B model (0.005% increase) — one small embedding table per decoder layer. Inference cost is negligibly affected, making the defense practical for production deployment.

- **Utility is preserved.** Figure 6 shows that AIR's AlpacaEval win rate is comparable to or better than non-adversarially trained baselines (e.g., 84.0% vs. 83.2% for Llama-3.2-3B SFT, 92.0% vs. 90.7% for Qwen-2.5-7B DPO). The defense gains do not come at the cost of general instruction-following capability.

## Weaknesses

### Fatal
None.

### Major
- **Absence of attacks specifically adapted to the AIR mechanism.** The paper evaluates against GCG and Astra, which are strong white-box attacks with full gradient access. However, for an architectural defense, it is standard practice to also evaluate attacks that are explicitly designed to target the defense — e.g., optimizing a loss term that penalizes the model from attending to the IH embeddings, attempting to find tokens whose hidden representations cancel the injected IH vectors, or disrupting the privilege-level indexing. The existing evaluation shows AIR is robust against general-purpose attacks, but whether it withstands adversaries who know *how* AIR works and adapt their objective accordingly remains an open question. This does not invalidate the paper's comparative claims (AIR beats baselines under the same attacks), but it limits the strength of the absolute robustness claims.

### Minor
- **Figure 3 motivational analysis is uneven across IH mechanisms.** The cosine-similarity metric applied to the Delimiter baseline is conceptually different from its application to ISE and AIR. For ISE and AIR, the metric cleanly isolates how well an additive privilege signal is preserved through layers (comparing T+S_P0 vs. T+S_P1). For Delimiters, the "IH signal" is the token ID itself (e.g., [INST]), and the near-1.0 similarity across layers reflects a different phenomenon — it does not straightforwardly indicate "signal decay" in the same sense. The ISE vs. AIR comparison within Figure 3 is valid and informative (AIR maintains better separation), and the paper's main empirical results stand independently, but the framing overstates the rigor of this evidence for the Delimiter method.

- **Unclear whether AIR embedding tables are updated during LoRA-based DPO training.** The paper states that DPO uses "parameter efficient fine-tuning using LoRA" but does not specify whether the AIR embedding tables (or, for symmetry, the ISE embeddings / Delimiter token embeddings) are included in the trainable parameters. Standard LoRA adapts only low-rank projections of specific weight matrices (e.g., Q, V). If the embedding tables are frozen during DPO for AIR but trainable for baselines (or vice versa), this is a confound. The paper's claim that "all models undergo the same training procedure" suggests consistency, but the exact treatment of IH-related parameters during DPO should be stated explicitly for reproducibility. This applies equally to all methods, so the relative comparisons are likely fair, but the ambiguity should be resolved.

- **Single fixed target string for all attacks.** All robustness evaluations use the target phrase "hacked!". If the IH signals interact differently with higher-perplexity or multi-token targets, the reported ASR could be sensitive to this choice. While unlikely to change the *relative* ordering of methods, testing alternative target strings would increase confidence.

### Trivial
- The claim that "GCG's ASR against AIR is 1.6× to 9.2× lower compared to next best defense" is slightly rounded at the lower bound: for Llama-3.1-8B with DPO, the ratio is 4.0/2.8 ≈ 1.43×, below the stated 1.6×. This is a minor numerical imprecision.

## Nice-to-Haves

- **Analysis of *why* AIR makes gradient optimization harder.** The paper demonstrates that AIR works, but does not probe the mechanism beyond Figure 3. Showing that AIR increases the curvature of the loss landscape, creates gradient bottlenecks, or affects the attention patterns in specific ways would deepen the contribution. (This is clearly scoped out by the paper, so it is not a weakness.)
- **Testing with alternative target strings** (longer phrases, variable-length targets) to confirm that the reported ASR is not an artifact of the single target "hacked!".

## Removed Points
- **Missing related works**: Removed per policy (cannot confirm existence of unmentioned works).
- **Confidence intervals / statistical significance**: Removed — the ASR differences are large enough (e.g., 0.1% vs. 14.5%) that significance is self-evident, and point estimates with shaded regions in Figure 7 already communicate variance; requesting CIs is a generic methodological nitpick not standard for this evaluation paradigm.
- **Reproducibility concerns about undisclosed hyperparameters**: Removed — the paper discloses optimizer (AdamW), learning rates, epochs (3), LR scheduler (linear), and LoRA rank (not specified but standard). Remaining details are in the (parser-stripped) appendix.
- **"Could the metric be measuring a proxy?" / "Are confounders controlled?" style speculation**: Removed per filter — these are category-driven concerns without concrete anchors in the paper.
- **The harsh critic's Section-by-Section notes about RoPE analogy being "not rigorously defended" and "minor note, not a weakness"**: Already not framed as a weakness by the critic; included here only for completeness.

## Novel Insights

None beyond the paper's own contributions. The core insight — that injecting IH signals at every layer via additive embeddings dramatically improves robustness — is the paper's own contribution, not an emergent synthesis from the reviews. The reviews refine the evaluation of this contribution (noting the Figure 3 framing issue and the adaptive attack gap) but do not generate a new observation about the method or problem.

## Suggestions

1. Add an adaptive attack evaluation: even a simple variant of GCG that includes an auxiliary loss term explicitly penalizing the model's reliance on the AIR embeddings (e.g., maximizing the similarity between AIR and non-AIR hidden states) would substantially strengthen the security claims.
2. Clarify the training setup in Section 5.2 by stating whether the IH embedding tables (for AIR, ISE, and Delimiter tokens) are frozen or trainable during the LoRA-based DPO stage.
3. Either remove the Delimiter trace from Figure 3 or re-analyze it with a metric that operates uniformly across mechanisms (e.g., linear probe accuracy per layer for predicting token privilege level).
4. Correct the lower bound of the 1.6×–9.2× range in the GCG ASR claim to reflect the actual minimum ratio (~1.4×), or clarify the basis of the computation.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>