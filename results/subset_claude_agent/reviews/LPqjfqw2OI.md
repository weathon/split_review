Now I have enough context to draft the review. Let me call `draft_review` first, then proceed to calibration.Round 1 bracket: FM plausibly sits between 4.5 and 6.5. Let me read the most topically similar anchors.Round 1 bracket: **4.5 to 6.5**. FM is clearly above the weak anchors (2.33–3.0) and below the strong anchors (7.6–8.0). Topically, UltraMem (6.0) and GYk0thSY1M (4.0) are the tightest comparators. Now narrowing.Now I have enough anchors to finalize. Let me write the complete review.

**Calibration analysis:**
- RetNet (4.75, rejected): New RNN architecture competing with Transformer — similar class to FM, but had larger-scale experiments (1.3B–13B). FM has more novel architecture (sparse routing + kernels) but weaker evaluation breadth.
- UltraMem (6.0, accepted): Sparse memory architecture with scaling laws, 1.6B scale. FM is comparable in spirit but smaller scale and lacks the breadth of UltraMem's task evaluation.  
- MELODI (6.25, accepted): Memory compression with actual long-context datasets (not just perplexity). FM's long-context evidence is perplexity-only, which is notably weaker.
- fL4qWkSmtM (6.8, accepted): *Explicitly* argues perplexity is unreliable for long-context evaluation — directly undercuts FM's main claim.

**Round 2 bracket: 4.75–6.0.** FM is above RetNet (more novel mechanism, concrete kernel contribution) but below UltraMem (weaker evaluation) and clearly below MELODI (perplexity-only long context). FM sits closer to 5.0 given that its headline contribution (long-context superiority) rests entirely on perplexity curves that the community has specifically argued are insufficient for this purpose.

---

## Summary
Factorization Memory (FM) is a recurrent neural network architecture maintaining a multi-slot factorized memory with sparse top-k updates via a learned router, built on top of Mamba-2's parallel prefix scan for efficient training. The paper claims competitive short-context performance with Transformer and Mamba-2, superior long-context extrapolation, and a 35–40% inference speedup over Mamba-2 via custom CUDA/Triton kernels. An empirical study covers scaling laws, memory width ablations, and downstream benchmarks at 1B parameters.

---

## Strengths

1. **Sparse updates match dense at scale (Figure 5):** Updating only 25% of memory states achieves the same test loss as dense updates when m ≥ 128, while cutting compute by 75%. The paper shows this cleanly for both fixed-k=4 and proportional-25% sparse variants—directly validating the efficiency-capacity claim.

2. **Long-context extrapolation over Mamba-2 (Figure 3b):** FM's loss frontier continues to improve as training FLOPs increase when evaluated at 2048 tokens (2× the 1024-token training window), while Mamba-2's frontier plateaus. Since Mamba-2 is also a length-limit-free recurrent model, this is a meaningful architectural comparison.

3. **Concrete inference speedup with custom kernels (Figure 6):** A 35–40% faster generation rate than Mamba-2 across 16K-token prompts on H100, demonstrated with optimized CUDA/Triton kernels. This is a real engineering contribution.

4. **Controlled experimental setup:** All 1B models share identical training data, budget, and model depth/width. A DCLM reproduction validates results on public data.

---

## Weaknesses

### Fatal
None.

### Major

1. **Missing targeted long-context evaluation**: The paper's central claim is that FM "demonstrates superior generalization in long-context scenarios," but all long-context evidence is based on "loss-so-far" perplexity curves on web novel text (Figure 4). This is problematic for two reasons. First, a model that simply ignores context beyond 1024 tokens but degrades gracefully—without actively using long-range information—would produce identical perplexity curves; the paper offers no way to distinguish these hypotheses. Second, the community has specifically argued that perplexity is unreliable for assessing long-context capability (it averages over all tokens and obscures whether key long-range dependencies are captured). No needle-in-a-haystack, multi-hop retrieval, long-document QA, or any other recall-oriented long-context task is included. The paper's own caveat—"this increase rarely exceeds the uncertainty in predicting the first 128 tokens"—describes stability, not information retrieval from remote positions.

2. **Transformer long-context comparison is partly confounded by RoPE**: Figures 3b and 4 compare FM against a LLaMA-style Transformer trained at 1024 tokens using RoPE positional encodings, which are known to degrade outside the training window by design. The paper implicitly acknowledges this ("Mamba-2 generally achieves better long-context generalization than Transformers, likely due to its recurrent architecture") but does not flag this to the reader explicitly. This makes Transformer degradation appear as evidence of FM's architectural advantage when it largely reflects a property of positional encoding. The meaningful comparison for evaluating FM's architecture is FM vs. Mamba-2, not FM vs. an RoPE-limited Transformer.

### Minor

3. **No statistical significance for downstream results (Table 1)**: English downstream gaps are 1–2 percentage points (FM: 30.98, Transformer: 29.53, Mamba-2: 29.06) with a single seed and no variance or confidence intervals reported. At this scale and granularity these differences are plausibly within noise, and the claim of "outperforming" in the abstract is not credibly supported.

4. **Architectural constraint in memory write not discussed**: In Eq. (10), all m memory states receive the same projected input x̄_t = W_i x_t, differentiated only by routing weight θ_t[i]. The current write thus embeds a single d_memory-dimensional vector into all active states at different intensities; inter-state heterogeneity must emerge through historical divergence rather than write-time diversity. Section 4.1.3's claim that "each memory state encode distinct aspects of the input" holds only by way of history, not from the current time-step write. This constraint is central to understanding what "factorization" actually means and deserves explicit discussion.

5. **Routing collapse vs. specialization (Section 4.1.3)**: For fixed-k=4, the paper observes that "the router remained stationary across tokens" and interprets this as evidence of memory specialization ("each memory state encode distinct aspects of the input, achieving a non-redundant representation"). However, a stationary router is equally consistent with routing collapse (always selecting the same k states regardless of input). No routing entropy measurement or visualization is provided to distinguish desired specialization from degenerate collapse.

### Trivial

6. The related work section (Section 5) dismisses MoE as "orthogonal" because it sparsifies MLP layers while FM sparsifies memory states. FM's routing mechanism—softmax over m slots, top-k selection, renormalization—is architecturally near-identical to token-to-expert routing. A sentence acknowledging the conceptual connection and explaining the dimensional distinction would strengthen the discussion.

---

## Nice-to-Haves
- Even a small-scale needle-in-a-haystack or passkey retrieval experiment would provide direct evidence that FM is actually using long-range information, not merely failing gracefully.
- Ablate long-context advantage when Transformer is given extended RoPE training at matched lengths (4K/8K); this would isolate FM's architectural contribution from positional encoding artifacts.
- Routing analysis: entropy of γ_t over training steps and across input types to confirm specialization rather than collapse.
- Multi-seed evaluation or error bars for Table 1 to credibly support the performance differential claims.

---

## Removed Points
*These points were filtered; treat with caution.*

- **"Priority claim lacks 'to our knowledge'"** — REMOVED: factually wrong. The abstract reads "To our knowledge, this represents the first RNN architecture..." exactly.
- **"Inference benchmark at 16K is out-of-distribution"** — REMOVED: inference speed for RNNs is independent of training context length; this is not a valid concern for the speedup measurement.
- **Missing appendix proofs and details** — REMOVED per hard rule (parser strips appendix from all submissions).
- **Training data is proprietary** — REMOVED: a DCLM reproduction is explicitly provided in Section A.3; this is not a structural flaw.
- **"The model may need long-context training"** / comparison requiring matched long-context training for all models — MOVED to Nice-to-Haves; this is a suggested strengthening, not a fault in the current evaluation.

---

## Novel Insights
The most interesting empirical result in the paper is that sparse (top-k) routing actually matches or exceeds dense routing in test loss at the same total m (Figure 5), rather than merely approximating it. This suggests top-k selection acts as implicit regularization that sharpens memory specialization—analogous to how dropout or weight sparsity can *improve* generalization rather than merely maintaining it. The paper attributes this to lower-temperature routing behavior but does not investigate whether the mechanism is the selection itself (information bottleneck) or the renormalization of surviving weights. A follow-up study tracing this effect would be a substantive theoretical contribution.

---

## Suggestions
1. Add a targeted long-context information retrieval benchmark (passkey retrieval, needle-in-a-haystack, or SCROLLS subset) to demonstrate that stable loss at 128K corresponds to genuine use of long-range information.
2. Report multi-seed variance or confidence intervals for Table 1 to credibly distinguish FM from baselines.
3. Add a section analyzing routing entropy and diversity across input types to validate the specialization interpretation of Section 4.1.3.
4. Discuss the shared-write-vector constraint in Eq. (10) explicitly, including what it implies for the "factorization" intuition and whether per-state W_i projections were considered.

---

## Score and Decision

**Axis evaluation:**
- *Originality*: Moderate. The sparse routing over RNN memory slots is a genuine architectural novelty; the idea of treating top-k routing in a temporal memory as analogous to MoE is underexplored. The method builds coherently on Mamba-2 without being incremental.
- *Importance of research question*: High. Efficient long-context RNNs with verifiable information retrieval capability is an active and important frontier.
- *Claims well-supported*: Weak for the central long-context claim (perplexity-only evidence, no recall tasks); stronger for the efficiency and sparse-vs-dense claims.
- *Soundness of experiments*: Moderate. Well-controlled comparison setup, but the headline evaluation is perplexity-based on proprietary data.
- *Clarity of writing*: Good. Architecture is clearly specified; equations are self-consistent; figure captions are informative.
- *Value to community*: Real: open kernels, DCLM reproduction, clear scaling study. But limited by weak long-context evaluation.

**Calibration summary:**
- Round 1 bracket: 4.5–6.5
- Round 2 anchors: RetNet (4.75, reject) — FM is above this due to more novel sparse mechanism and hardware contribution. UltraMem (6.0, accept) — FM is below this due to smaller scale, weaker task coverage, and absence of recall-type evaluation. MELODI (6.25, accept) — FM's long-context evidence is strictly weaker (perplexity only vs. actual long-context tasks).
- Narrowed bracket: 4.75–5.5, with FM sitting closer to the lower end because its headline contribution (long-context superiority) rests entirely on perplexity evidence that the community has specifically found unreliable for this purpose.

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| jp4pxKqCRW (Long-context extrapolation via periodic extension) | 2.50 | 1 | Clearly weaker than FM—rejected positional encoding work without new architecture |
| UU9Icwbhin (RetNet) | 4.75 | 2 | FM is slightly above: more novel sparse mechanism, hardware kernels, but weaker scale |
| cit3SNnZ6Q (Q-Sparse) | 4.75 | 2 | Different direction (activation sparsity in Transformer); FM has comparable rigor |
| B9XP2R9LtG (Sparsing Law) | 5.25 | 2 | Broader empirical study on an existing phenomenon; FM's contribution is more architectural |
| zjeHLSiNv1 (UltraMem) | 6.00 | 1 | FM is below: UltraMem evaluates on more tasks at larger scale |
| TvGPP8i18S (MELODI) | 6.25 | 2 | FM is below: MELODI uses actual long-context datasets, not just perplexity |
| fL4qWkSmtM (What is Wrong with PPL for Long Context) | 6.80 | 2 | Highly relevant; directly challenges FM's evaluation paradigm |
| Tzh6xAJSll (Scaling Laws for Associative Memories) | 7.60 | 1 | Far above FM: rigorous theory + extensive experiments |
| GRMfXcAAFh (LinOSS) | 8.00 | 1 | Far above FM: theoretical guarantees + universality proofs |

**Final score: 5.0.** FM sits above RetNet (4.75) on novelty and hardware contributions, but the headline claim is supported only by perplexity curves that the field has deemed insufficient for evaluating long-context capability. The major gap—absence of any targeted retrieval or recall experiment—is not a presentation issue but an evidential one, and it is the primary argument the paper rests on. The paper is not flawed in its methodology; it simply hasn't yet provided the evidence needed to support its central contribution at publication quality.

**Decision: Reject.** The work merits publication after demonstrating genuine long-context recall capability (needle-in-a-haystack, passkey retrieval, or equivalent) to complement the perplexity evidence, and providing statistical support for the downstream performance claims.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>