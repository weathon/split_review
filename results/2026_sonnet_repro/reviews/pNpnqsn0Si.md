Now let me run calibration searches to anchor the score.**Round 1 bracket: 5.0–7.0.** The paper has genuine novelty and consistent empirical results, comparable to CoTFormer (5.75) but weaker than top-tier transformer architecture papers (7.0+). Let me narrow within this range.Now I have sufficient calibration data. Let me compile the full review.

**Calibration Summary:**
- Round 1 bracket: 5.0–7.0 (CoTFormer at 5.75 is the closest topical anchor)
- Round 2 anchors: CoTFormer (5.75, accepted, adaptive computation architecture), Sparse Scaling (6.67, accepted, pretraining experiments with scaling analysis), Hyper-UT (5.00, rejected, synthetic task adaptive computation)

**Comparison reasoning:** Thoughtbubbles is stronger than CoTFormer on empirical scope (two datasets, three scales, outperforms computation-matched baseline on perplexity), but CoTFormer doesn't have the BLiMP degradation issue. Thoughtbubbles is weaker than the 6.67 paper (fewer configurations, no scaling law contribution, evaluation-motivation gap). It sits around **6.0**.

---

## Summary
Thoughtbubbles is a novel GPT-2-style transformer variant that learns, during standard language model pretraining, to fork or prune residual streams for adaptive parallel latent computation. Forking decisions are driven by a cumulative score mechanism trained entirely with cross-entropy loss; high-scoring tokens accumulate "bubbles" of cloned residuals for additional processing before merging into the final output distribution. The method consistently achieves lower validation perplexity than both parameter-matched and computation-matched (Copy-N) baselines across 150M–772M parameter scales on OpenWebText and peS2o, with interpretable entropy-correlated computation allocation.

---

## Strengths

- **Genuine architectural novelty with unsupervised training**: The forking/pruning mechanism in §2.3–2.5 learns to allocate parallel latent computation using only standard LM loss — no auxiliary objectives, no manual token insertion, no supervised trace labeling. This is a real contribution: the mechanism is clean, fully described, and the training recipe is transparent.

- **Consistent perplexity improvements across all scales and both datasets**: Table 1 and Figure 3 show the perplexity advantage holding across every (scale × dataset) combination tested — six settings total — and Figure 3 highlights the striking result that the 319M Thoughtbubbles model matches the 772M baseline perplexity on OpenWebText. Beating both parameter-matched and computation-matched baselines in this metric is a meaningful result.

- **Interpretable computation allocation via entropy correlation**: §5 and Figure 5 show that, without any explicit supervision, the model allocates more forks to tokens of moderate uncertainty (as measured both by its own entropy and by an independently trained baseline LM). This concave relationship — low forks at very low and very high entropy, peak forks at moderate entropy — supports the paper's core claim that the scoring mechanism learns meaningful allocation, not arbitrary duplication.

- **Autoregression consistency addressed empirically**: §5.1 and Figure 6 directly measure the distribution shift between block-wise scoring and autoregressive inference, and show that proportional budget scaling (dynamic forking) preserves the performance advantage. This is a non-trivial practical concern addressed concretely.

---

## Weaknesses

### Fatal
None.

### Major

- **BLiMP consistently below the computation-matched baseline**: Table 1 shows that in 10 out of 12 Thoughtbubbles entries, BLiMP scores fall below Copy-5 (the computation-matched baseline). The gap is especially stark on peS2o: at 772M, Ours (κ=4L) scores 67.4 vs. Copy-5's 71.6 — a 4.2-point deficit. The paper attributes this to "pruned dynamic parallel computation may not be as helpful for syntax" (§4, Results), but this is an ad hoc hypothesis, not a principled account. BLiMP is a core linguistic competence benchmark. The pattern suggests the adaptive allocation trades syntactic capacity for semantic prediction — a tradeoff that the paper's framing as a uniformly better architecture obscures. The discussion of this phenomenon should be much more prominent and should acknowledge it as a genuine limitation of the current approach.

- **Computation-matched baseline is too weak to support the adaptivity claim**: The central efficiency claim is that *adaptive* forking outperforms *non-adaptive* parallelism at the same compute budget. The paper's computation-matched comparison is against Copy-N, where input residuals are simply duplicated — the weakest conceivable instantiation of parallel latent computation (no learned gating, no selectivity). Simultaneously, §1 and §6 cite Goyal et al. (2024), Herel & Mikolov (2024), and Sun et al. (2025) as directly relevant prior work — pause-token and thinking-token methods that also attempt to allocate latent computation. None appear as baselines. Without comparing to at least one of these methods, the paper cannot cleanly establish that *adaptive* allocation — rather than simply *any* parallel expansion — accounts for the gains. The Copy-N design conflates these two hypotheses.

- **No FLOPs analysis supporting the "compute-matched" claim**: Table 1 states that κ=4L is "roughly FLOPs-matched against copy-5 baseline" — but this claim has no derivation or numerical support anywhere in the paper. Thoughtbubbles has non-trivial additional overhead (forking decision networks, fork embeddings, score accumulation, top-k operations, attention score modification). Without actual FLOPs counts per forward pass for each configuration, the computation-fairness claim cannot be verified, and the framing of the comparison in Table 1 is incomplete.

### Minor

- **Motivation-evaluation gap (acknowledged, but conclusion overclaims)**: The paper opens by invoking multi-step reasoning and bounded computation limits, and the conclusion states the method "allows our model to solve more difficult tasks that require scaling inference-time computation." The actual evaluations — perplexity, HellaSwag, LAMBADA, BLiMP, PIQA — are zero-shot language understanding tasks, not reasoning benchmarks. §8 explicitly acknowledges this gap (GSM8K requires multi-billion scale). The limitation is honest, but the conclusion language should be calibrated to match what the experiments actually test.

- **No variance estimates in Table 1**: For benchmarks like HellaSwag (1–2 pp headline gains) and LAMBADA, single-run point estimates with no confidence intervals or standard deviations make it impossible to assess statistical significance. This is particularly important for zero-shot evaluations where run-to-run variance is known to exist.

- **Top-k gradient bottleneck acknowledged but unaddressed**: §8 notes that hard top-k creates a gradient truncation issue for early high-scoring tokens that are later pruned, degrading the quality of the scoring function that drives adaptivity. No comparison to differentiable relaxations (Gumbel-softmax, straight-through) is provided, and the degree to which gradient truncation limits the scoring quality is not quantified. Since the scoring/attenuation mechanism is the key difference from Copy-N, knowing how much this degrades it is material.

- **Forking-layer placement discussed only in appendix**: The choice to place forking at layers 3, 7, and 11 — and the finding that too much early forking yields no further gains — is a significant design decision with direct implications for understanding when the mechanism works. The paper delegates this discussion to appendix B, making the choice appear arbitrary in the main text.

### Trivial
- The "first-known architecture" claim in §1 contribution 1 is slightly broad: Adaptive Computation Time (Graves, 2016) also learns per-step computation budgets without supervision. The specific novelty — *parallel* forking of residual streams during LM pretraining — is real and worth stating precisely.

---

## Nice-to-Haves

- An ablation comparing full Thoughtbubbles against a deterministic fork-every-token variant (no top-k, no scoring) would directly test whether *adaptive* allocation or simply *any* parallel expansion drives the perplexity benefit — this is the experiment that most directly addresses the key ambiguity in the current evidence.
- A single efficiency figure plotting perplexity vs. actual FLOPs as κ is swept would make the compute-efficiency story rigorous and concrete.
- Comparing against even a simple re-implemented thinking-token baseline (e.g., a version of Goyal et al. 2024 at 150M scale) would substantially strengthen the claim that unsupervised adaptive allocation specifically is what matters.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Attention scores are unreliable proxies for causal influence"** (from harsh critic, §5 analysis): The paper does not claim that Figure 4 proves causal influence — it uses the phrase "meaningfully influence" and pairs the attention analysis with the entropy correlation in Figure 5. The critic is correct that attention scores have limitations as causal proxies, but the paper's interpretive claim is appropriately hedged. Removed as speculative.

- **Asymmetry in score learning between original and forked tokens (Eq. 4 forced-maximum)**: The critic raises that forcing rightmost token keep score to 1 creates a gradient asymmetry. This is technically true but is also a deliberate design choice to ensure at least one residual survives per token, with explicit discussion in §2.3. Downgraded to resolved-by-design.

- **"Output averaging mixes distributions not logits, creating training instability"**: The paper uses the log-sum-exp trick (§2.5, Eq. 11) for numerical stability and explicitly notes scores are computed in log-space. The concern about training dynamics is speculative (no training curves to verify it) and the paper has mitigation in place. Removed as speculative.

- **"The first-known" claim conflicts with ACT/Universal Transformers**: Strictly, this is a minor overclaim (Graves 2016 and Universal Transformers exist), but the specific novelty of *parallel* forking in a decoder LM during pretraining with LM loss only is defensible as new. Kept only as a Trivial note.

- **Strength Finder: "better performance than both parameter-matched and computation-matched baselines"** — this is generically stated as a strength but needs qualification: it holds for perplexity, LAMBADA, and HellaSwag, but *not* for BLiMP vs computation-matched. Moved to Strengths with this qualification.

---

## Novel Insights

The most interesting observation in this paper — not found prominently in the cited prior work — is the *concave* relationship between token-level output entropy and computation allocation (Figure 5): the model forks moderately uncertain tokens most aggressively but reduces forking at the *highest*-entropy positions. The authors' hypothesis (high-entropy positions correspond to clause boundaries and coreferences where additional compute resolves nothing) is plausible and connects to mechanistic questions about where latent computation is genuinely useful. This is a concrete, surprising empirical finding that merits follow-up regardless of the paper's acceptance.

---

## Suggestions

1. **Add an ablation comparing full Thoughtbubbles vs. deterministic full-fork (no top-k, no score gating)** to directly isolate whether the scoring/adaptation mechanism or simply the extra parallel streams accounts for the perplexity gain.
2. **Provide per-configuration FLOPs counts** (or at minimum a formula) for all models and baselines in Table 1, so the "compute-matched" framing can be independently verified.
3. **Expand the BLiMP discussion** — quantify and analyze the systematic degradation (especially on peS2o), and consider whether the tradeoff is inherent to the score-based pruning or addressable through architectural changes.
4. **Move the autoregression mitigation (§E.1 dynamic forking)** to the main text — it is applied to all reported numbers and is non-trivial, so it belongs in the evaluation section.
5. **Calibrate conclusion language** to match the evidence: replace claims about solving "more difficult reasoning tasks" with the accurate claim of "better language modeling and zero-shot understanding at the same compute budget."

---

## Score and Decision

**Anchor comparisons:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `7igPXQFupX.md` (CoTFormer) | 5.75 | R1/R2 | Closest topical analog; Thoughtbubbles has stronger empirical coverage (2 datasets, 3 scales) and *does* beat its computation-matched baseline in perplexity, whereas CoTFormer explicitly does not. Thoughtbubbles is somewhat stronger. |
| `tI3eqOV6Yt.md` (Hyper-UT) | 5.00 | R1 | Narrower scope (synthetic tasks), rejected; Thoughtbubbles clearly stronger. |
| `ud8FtE1N4N.md` (Sparse Scaling) | 6.67 | R2 | Strong empirical coverage, novel scaling law, accepted; Thoughtbubbles is weaker (no scaling law, evaluation-motivation gap, BLiMP degradation). |
| `W8K8slZ73R.md` (Adaptive Transformer Programs) | 7.00 | R1 | Interpretability-focused, less directly comparable; Thoughtbubbles is weaker in experimental breadth. |
| `YkCjojDG3l.md` (PolySketchFormer) | 5.00 | R2 | Efficiency paper, not comparable; context anchor only. |
| `ngmEcEer8a.md` (Unreasonable Ineffectiveness Deeper Layers) | 6.50 | R2 | LM pretraining + scaling analysis; good empirical coverage, accepted; Thoughtbubbles is comparable or slightly weaker. |
| `KQALhPTAfj.md` (Adaptive ViT Training) | 3.75 | R1 | Rejected; Thoughtbubbles clearly stronger. |

**Round 1 bracket**: 5.0–7.0  
**Round 2 narrowing**: The paper is stronger than CoTFormer (5.75) on empirical coverage and computation-matched performance, but weaker than Sparse Scaling (6.67) and the Deeper Layers paper (6.50) due to the BLiMP degradation, absent FLOPs analysis, and weak baseline comparison. The paper lands between CoTFormer and Sparse Scaling, closer to Sparse Scaling's lower end.

**Evaluation on key axes:**
- *Originality*: High — the unsupervised parallel forking mechanism is genuinely novel.
- *Importance*: Moderate-high — adaptive inference-time compute is a timely and important problem.
- *Claims well-supported*: Moderate — perplexity claim is well-supported; efficiency/adaptivity claim lacks FLOPs analysis and stronger baselines; reasoning claim is unsupported at the tested scale.
- *Soundness of experiments*: Moderate — multi-scale, multi-dataset design is good, but no variance estimates and BLiMP degradation are real gaps.
- *Clarity*: Good — the mechanism is clearly described, figures are interpretable.
- *Value to community*: Moderate-high — released code, interesting entropy-forking finding.

**Final score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>