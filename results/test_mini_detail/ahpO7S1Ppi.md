Now I have sufficient calibration context. Let me write the consolidated review.

---

## Summary

This paper proposes Pctx, a personalized context-aware tokenizer for generative recommendation (GR). Unlike prior GR methods that assign each item a fixed semantic ID derived solely from item features, Pctx conditions tokenization on the user's historical interaction sequence, allowing the same item to receive different semantic IDs under different user contexts. The pipeline encodes user context via DuoRec, condenses representations via k-means++ clustering, fuses them with item features, quantizes via RQ-VAE, merges redundant IDs, and trains an autoregressive model with multi-facet generation. Experiments on three Amazon categories show up to 8.9% NDCG@10 improvement over non-personalized baselines, with thorough ablations isolating each component's effect.

## Strengths

- **First personalized tokenizer for GR with a clean, novel design.** The paper identifies a genuine limitation of existing GR tokenizers (fixed item-to-ID mappings) and proposes a principled solution: conditioning semantic ID generation on the user's interaction history. The architecture (DuoRec encoding → clustering → RQ-VAE quantization → redundant ID merging) is well-motivated, and the ablation study (Table 3) validates that each component contributes to the overall improvement. The case study on *StarCraft II* (Figure 4) concretely demonstrates how the same item receives different semantic IDs depending on user context (story-driven vs. RTS player).

- **Consistent, statistically significant improvements over strong baselines.** Pctx outperforms all baselines across all 12 metric-dataset combinations in Table 2, with improvements of up to 8.90% in NDCG@10 (Scientific) and 11.11% in NDCG@5 (Instrument). Statistical significance is reported via paired t-test (p<0.05). The gains hold against ActionPiece, the strongest context-aware tokenization baseline, which itself outperforms conventional GR methods.

- **Careful isolation of the personalization effect.** The paper goes beyond a simple end-to-end comparison. Variant (3.4) w/ Random Target controls for token diversity alone and underperforms Pctx, confirming that personalization *per se*—not merely having multiple tokens per item—drives improvement. The ensemble analysis (Table 4) shows that naively combining TIGER+SASRec or TIGER+DuoRec lags far behind Pctx, ruling out the concern that Pctx merely aggregates existing model strengths. The ablation on DuoRec vs. SASRec as the context encoder (rows 1.1–1.3) further demonstrates that the choice of context encoder matters.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The claimed limitation of static tokenizers is presented as a proven bottleneck rather than a motivating intuition.** The paper argues that static semantic IDs "implicitly enforce a universal item similarity standard across all users" (Section 1) because tokens sharing prefixes receive similar generation probabilities. However, the autoregressive model sees different *sequences* of semantic IDs for different users (since their histories differ), so it can assign different overall item probabilities even when each item maps to a fixed ID. Whether the fixed token routing is the *limiting factor*—as opposed to other aspects of the modeling pipeline—is asserted rather than demonstrated. The empirical success of Pctx shows that personalized tokenization *helps*, but the paper's causal framing ("static tokenizers limit personalization because...") overstates what the reasoning alone supports. This does not invalidate the empirical contribution, but the motivation would be stronger if softened to a plausible hypothesis supported by the empirical evidence.

- **The fairness of the ActionPiece comparison is underspecified.** The paper reports that ActionPiece is the strongest baseline and that Pctx improves on it. However, it is not clear from the main text whether the same underlying autoregressive model architecture (e.g., encoder-decoder Transformer) and training recipe are used for all GR baselines (TIGER, LETTER, ActionPiece, and Pctx). The paper states "we follow prior work" for baselines and defers details to the appendix (stripped), but this is insufficient for readers to confirm that tokenization is the only variable. Given that the improvement over ActionPiece is the paper's headline result, the authors should explicitly confirm that the base architecture and optimization are held constant, or at minimum disclose the architectures used. (The provided code mitigates reproducibility concerns but does not address the in-text clarity issue.)

- **Redundant SID merging is highly impactful and its sensitivity to τ is not analyzed.** Removing merging (variant 2.2) causes NDCG@10 to fall from 0.0341 to 0.0221 on Instrument—a catastrophic drop that exceeds even the gap between Pctx and TIGER. The paper explains this as sparsity-driven over-personalization, which is plausible, but the threshold τ that governs which IDs are pruned is not reported in the main text (deferred to the stripped appendix). A sensitivity analysis (e.g., NDCG vs. τ across a range) would help establish whether the method is robust or requires careful tuning.

- **Generalizability is demonstrated only on Amazon categories.** The three datasets (Instrument, Scientific, Game) are all Amazon product categories with similar sparsity (>99.96%) and short average sequence lengths (<9). While this is standard practice in the GR literature, the method's applicability to other domains (e.g., Yelp, MovieLens, or news recommendation) or denser interaction settings is not tested.

### Trivial

- The beam search width and length normalization settings used for multi-facet generation (Section 2.3) are not specified in the main text.
- The formula for choosing the number of cluster centroids C_{v_i} (Section 2.2.1) is described as "chosen proportionally" without even a rough range.

## Nice-to-Haves

- **Computational cost analysis.** The tokenization pipeline requires training an auxiliary DuoRec model, clustering context representations across the full dataset, and running RQ-VAE. This is substantially more expensive than static tokenization. A brief discussion of training time and memory overhead (even relative to TIGER) would help practitioners assess the cost-benefit trade-off.

- **Per-user entropy analysis of semantic ID assignments.** The case study (Figure 4) is illustrative. A quantitative analysis showing that for items with multiple SIDs, the model confidently assigns different SIDs to different users (e.g., higher entropy of the SID distribution across users compared to a random baseline) would strengthen the personalization narrative.

## Removed Points

These points were raised by reviewers but are removed from the main evaluation with justification:

- *Missing baselines (RECODE, LSQ)*: The paper cites these in related work; they address quantization rather than tokenization personalization and operate in a different paradigm. Per the scope of the paper's contribution, absence from the comparison table is not a weakness.
- *"Figure 1 illustrative not backed by data"*: Motivation figures are by nature illustrative. The empirical evidence for the method is presented in the experiments section.
- *Criticisms that rest on speculating about the stripped appendix content*: Several reviewer concerns (e.g., precise hyperparameter values, implementation details) are about material deferred to the appendix, which was stripped by the PDF parser. These reflect a formatting artifact, not a paper flaw.
- *Formatting/style nitpicks and grammar/typo concerns*: These are parser artifacts, not author errors.
- *"DuoRec analysis missing similarity distribution"*: A reasonable suggestion but a nice-to-have analysis, not a weakness of the paper as presented.

## Novel Insights

Both the harsh critic and strength finder agree on the paper's core value proposition—personalized tokenization is a genuinely new direction in GR—but they frame its significance differently. The harsh critic correctly notes that the paper's motivation logic is not airtight: the claim that static tokenization "implicitly enforces a universal similarity standard" conflates token-level probability constraints with the model's ability to learn user-conditioned item probabilities. This is an important nuance because it means the method's contribution is *empirically demonstrated* rather than *logically necessitated* by a flaw in static tokenizers. What is genuinely novel—and what the strength finder correctly identifies—is that the paper moves beyond this theoretical debate by providing strong empirical evidence through multiple controls (random target ablation, ensemble analysis, component ablations) that the personalization mechanism itself drives the gains. The paper would benefit from explicitly acknowledging this distinction: the contribution is not proving that static tokenizers are broken, but showing that personalizing tokenization *works*, and the paper's careful ablation design is what makes that claim convincing.

## Suggestions

1. In the camera-ready version, soften the motivation framing from "static tokenizers *enforce* a universal standard" to "static tokenizers *may limit* personalization because..." and let the empirical results carry the causal claim.
2. Add a sentence explicitly stating that all GR baselines use the same encoder-decoder backbone architecture (or, if not, disclose the differences and justify them).
3. Report the chosen τ (infrequent ID merging threshold) and add a brief sensitivity analysis (e.g., a line plot of NDCG@10 vs. τ for one dataset) to demonstrate that performance is stable over a reasonable range.
4. Include a table in the main text with key hyperparameters (α, γ, τ, beam width, number of codebook levels G).

## Score and Decision

**Calibration report:**

I retrieved and compared against the following anchor papers from the human review corpus:

| Anchor | Avg Score | Round | Comparison to Pctx |
|---|---|---|---|
| dNMsieEiAc – Prompt2Rec | 3.20 | 1 (weak) | Clearly weaker: limited novelty, rejected paper with serious methodological issues. Pctx has stronger empirical validation and a clearer contribution. |
| gcEhF4nuYI – FTP (Token Pruning) | 3.00 | 1 (weak) | Clearly weaker: withdrawn paper about LLM token pruning, far from Pctx's scope and quality. |
| tKFZ53nerQ – TDRG (Comment Generation) | 2.00 | 1 (weak) | Clearly weaker: rejected, small-scale experiments, topical mismatch. |
| QE1LFzXQPL – ImageFolder | 6.25 | 1 (strong), 2 | Comparable: both are accepted papers with novel tokenization contributions. ImageFolder's contribution (semantic image tokenizer) is well-validated; Pctx's contribution (personalized GR tokenizer) is similarly strong and more original within its subfield. |
| mb2ryuZ3wz – Adaptive Length Tokenization | 5.75 | 1 (mid) | Slightly below: accepted poster with a novel idea (variable-length tokens) but limited baseline comparisons and reconstruction quality not outstanding. Pctx's ablations and controls are more thorough. |
| B5iOSxM2I0 – Foundations of Tokenization | 6.50 | 1 (mid) | Comparable but different in kind: a theoretical paper about tokenization formalism, not directly comparable on empirical grounds. |
| ZdjkRbtrth – Generative Retrieval with LLMs | 5.25 | 1 (mid), 2 | Weaker: rejected paper with limited novelty (prompting existing LLMs) and unfair baseline comparisons. Pctx has stronger novelty and more rigorous evaluation. |
| hJEMTDOwKx – LMINDEXER | 5.50 | 2 | Weaker: rejected paper about learning semantic IDs. Concerns about weak baselines and insufficient experimental analysis. Pctx has more thorough evaluation and clearer contribution. |
| medKq3cONT – MoC for Recommendation | 5.00 | 2 | Clearly weaker: withdrawn paper with insignificant improvements (~0.1%), missing baselines, components not always beneficial. Pctx shows much larger gains with well-isolated components. |
| o99Yn1wN9J – ECQL (RL for Rec) | 6.25 | 2 | Comparable: accepted poster for recommendation with good theoretical grounding but some reviewer disagreement (scores 8,6,3,8). Pctx has more consistent reviewer reception. |
| 6GATHdOi1x – PreferDiff | 5.75 | 2 | Slightly below: accepted poster. Novel ranking objective for diffusion recommenders, but the contribution is incremental (reformulating BPR). Pctx introduces a fundamentally new paradigm (personalized tokenization). |

**Round 1 bracket:** Initial bracketing placed Pctx between weak anchors (~2–3) and strong anchors (~8), narrowing the plausible range to approximately 4–7.

**Round 2 narrowing:** Within that bracket, Pctx is clearly stronger than papers scored 5.0–5.5 (LMINDEXER, MoC) and comparable to or slightly stronger than papers scored 5.75–6.25 (Adaptive Length Tokenization, PreferDiff, ImageFolder). The strongest evidence for the paper's quality is its novel first-of-its-kind contribution, thorough ablation design, and statistically significant gains.

**Final score:** 6.0 — a solid acceptance. The paper introduces a genuinely novel personalized tokenization paradigm for generative recommendation, backed by well-designed experiments that isolate the personalization effect. The main weaknesses (overstated motivation, underspecified baseline comparison details, unanalyzed hyperparameter sensitivity) are fixable and do not undermine the core empirical contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>