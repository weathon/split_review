Now I have good comparator anchors. Let me compare TNT against them:

- **DEER (6.00)**: Parallelizing non-linear sequential models — most directly comparable topic. Limited empirical results (2 small tasks), cubic complexity bottleneck, reviewers question practical importance. TNT is substantially stronger: comprehensive LM experiments at 150M scale, 17× wall-clock speedup, clear ablation, well-motivated problem.

- **MELODI (6.25)**: Hierarchical memory compression — similar architectural territory. Decent experiments but limited context sizes, no fine-tuning. TNT has stronger empirical results (17× speedup + quality gains) and a more novel mechanism.

- **Flash Inference (6.83)**: Algorithmic contribution for inference speedup (1.6× end-to-end). More rigorous theory but weaker practical impact. TNT's 17× speedup on training is more impactful, with stronger empirical validation.

- **LongLoRA (7.00)**: Well-executed efficient fine-tuning paper with clear practical impact. TNT's contribution (periodic resets for non-linear recurrences) is more novel than LongLoRA's sparse attention, but TNT has methodological gaps that LongLoRA doesn't.

TNT sits clearly above the 6.0-6.25 band and is comparable to the 6.8-7.0 band but has real weaknesses pulling it down. I'd place it at **6.5** — a borderline accept where the novelty and empirical results are strong enough to warrant acceptance, but the architectural confound and missing specification prevent a higher score.

---

## Summary
TNT introduces a two-stage training paradigm for deep memory modules (like Titans) that decouples training efficiency from inference performance. Stage 1 uses a hierarchical memory architecture — a global module for long-range context plus multiple local modules for fine-grained processing — with periodic resets of local memory states to a learnable initialization, breaking sequential dependencies and enabling context parallelism for non-linear recurrences. Stage 2 is a brief fine-tuning phase that adapts local modules to smaller chunk sizes, resolving the train-test chunk size mismatch. TNT achieves up to 17× training speedup over the most accurate Titans baseline while simultaneously improving perplexity and reasoning accuracy.

## Strengths
- **Novel mechanism for parallelizing non-linear recurrences**: The periodic state reset (Eq. 6) is a genuine technical contribution. By resetting local memory states to a shared learnable \(W_{\text{init}}\) at segment boundaries, TNT breaks long-range sequential dependencies in non-linear RNNs, enabling context parallelism where none previously existed outside of Transformers and linear RNNs. Figure 4 empirically validates this: TNT runtime remains nearly flat from 2K to 32K sequence length while Titans (C=16) runtime grows 10×.

- **Empirical demonstration of the train-test chunk size mismatch**: Figure 2 provides concrete evidence that a Titans model trained at C=64 catastrophically degrades at other chunk sizes (PPL 36.45 at C=8 vs. 13.78 at C=64). This is a genuine empirical finding that motivates the two-stage approach and contradicts the natural intuition that smaller chunks at inference should always help.

- **17× wall-clock speedup with simultaneous quality improvement**: Table 1 shows TNT reaches target loss in 1.12 hours vs. 19.48 hours for Titans (C=8), a 17.37× speedup. Critically, this is not a speed-for-quality tradeoff — Table 2 shows TNT simultaneously achieves better perplexity (23.13 vs. 25.07) and better reasoning accuracy (41.0% vs. 39.0%).

- **Clean ablation validating each component**: Table 3 shows incremental value from each design choice: removing global memory severely degrades performance (PPL 25.60), removing Q-K projection hurts (22.01), adding more local modules monotonically improves (21.04 → 20.15 with 1→4 modules), and Stage 2 fine-tuning provides further gains.

## Weaknesses

### Fatal
None.

### Major
- **Architectural confound in the speedup claims**: TNT simultaneously changes both the training procedure (periodic resets, two-stage training) and the model architecture (hierarchical global+local modules vs. Titans' single memory module). The 17× headline speedup compares TNT with multiple memory modules against a single-module Titans baseline. Even at matched chunk size C_L=8 vs. C=8, where TNT shows 7.68× speedup, TNT has 1 global + 1 local module while Titans has 1 module. Without an iso-parameter ablation (e.g., a Titans model with comparable hierarchical structure but trained without resets), the paper cannot isolate how much of the speedup comes from the reset mechanism enabling parallelism versus from additional memory capacity. This does not invalidate TNT as a contribution — the architecture and training paradigm are inherently coupled — but it weakens the central claim that the training paradigm itself drives the improvement.

- **Multi-module aggregation unspecified in the main text**: The paper's best results use multiple local modules at different chunk sizes (e.g., C_L = {4,8,16,32}). Section 4.1.1 explicitly states the formulation is given for N=1 and defers the generalized formulation to Appendix E (stripped). The main text never explains how outputs from multiple local modules are combined — summed, concatenated, or otherwise aggregated. Since the multi-module configuration produces the paper's best numbers (23.09 PPL, 41.0% accuracy), this is a significant reproducibility gap. A reader cannot understand the central result from the main text alone.

### Minor
- **Abstract overclaims TTT evaluation**: The abstract states TNT is "Evaluated on Titans and TTT models," but the paper only instantiates TNT on Titans. TTT appears only as a baseline in Table 2, not as a host architecture for TNT.

- **Q-K projection theoretical justification is handwavy**: The paper frames the Q-K projection as resolving a "fundamental inconsistency," but projecting queries onto the span of past keys does not formally guarantee they lie in the distribution a non-linear network was trained on. The empirical benefit is real (PPL 21.04 → 22.01 upon removal, Table 3), but the theoretical framing overstates the rigor. Presenting it as a useful heuristic would be more appropriate.

- **"5% additional compute" claim is underspecified**: The paper claims Stage 2 requires "only an additional 5% of the original pre-training compute" (line 239) without clarifying whether this means steps, FLOPs, or wall-clock time. This claim references Table 4 in the stripped appendix.

- **No parameter allocation breakdown across modules**: When TNT uses 4 local modules, how many parameters does each have relative to the single Titans memory module? Without this, it is unclear whether perplexity gains from adding local modules reflect multi-resolution processing or simply more total capacity.

### Trivial
- **Figure 4 flat runtime for TNT (C_L=16) would benefit from a brief explanation**: The runtime is ~400ms from 2K to 32K. A sentence clarifying that shards are processed as an additional batch dimension would preempt reader skepticism.

## Nice-to-Haves
- An iso-parameter, iso-structure baseline (hierarchical Titans without periodic resets) to isolate the reset mechanism's contribution.
- Reporting variance for perplexity and accuracy at 150M scale.
- Clarifying the relationship between S_L (reset interval) and C_G (global chunk size) and whether their equality is deliberate.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh Critic: "Speedup claims are confounded; this is a structural evidential gap" (framed as fatal)** — Retained as Major but downgraded from fatal because the architecture and training paradigm are inherently coupled: the resets require hierarchical memory, and TNT is presented as the whole system. The paper never claims "resets alone" produce the speedup.
- **Harsh Critic: "Figure 4 runtime scaling is implausibly flat and insufficiently explained"** — The critic speculates about "two sequential waves" on an 8-chip pod without considering that context parallelism can batch shards as an additional dimension, making flat scaling expected. Downgraded to Trivial.
- **Harsh Critic: "Equation 6 notation is slightly confusing"** — Notation nitpick; the intended semantics are clear. Removed.
- **Harsh Critic: "TNT inside TTT footnote suggests TTT connection never developed"** — This is a joke footnote, not a serious claim. Removed.
- **Harsh Critic: "Challenge 2 domain mismatch is asserted rather than demonstrated"** — The ablation (Table 3) showing Q-K projection removal hurts performance IS the demonstration. Removed.
- **Harsh Critic: "Challenge 3 degradation magnitude suggests something more fundamental"** — Speculative, not a concrete weakness. Removed.
- **Harsh Critic: "Absence of TTT experiments is a gap given the abstract's claim"** — Already captured as Minor (abstract overclaim). Removed as duplicate.
- **Strength Finder: "Model-agnostic design validated across architectures"** — Only validated on Titans; TTT is only a baseline. This strength is aspirational, not validated. Removed.
- **Strength Finder: "Linear runtime scaling ... outperforms FlashAttention kernel at 32K"** — Merged into Core Strength 1; the runtime results support the parallelism claim. Removed as duplicate.
- **Strength Finder: Generic strengths about problem importance and motivation** — Removed as non-concrete.

## Novel Insights
The paper's observation that a Titans model trained at a specific chunk size C=64 exhibits catastrophic degradation at other chunk sizes (PPL jumping from 13.78 to 36.45 at C=8) is a genuinely interesting empirical finding that challenges the default assumption that smaller chunk sizes at inference should always help. The paper not only identifies this "over-specialization" phenomenon but demonstrates that relatively cheap fine-tuning (Stage 2) can resolve it, suggesting that the chunk-size sensitivity is a surface-level adaptation issue rather than a fundamental architectural limitation. This has implications beyond this paper for how we think about training deep memory modules.

## Suggestions
- Specify the multi-module aggregation mechanism in the main text (even a single sentence like "outputs from multiple local modules are summed" would resolve the major reproducibility gap).
- Either add an iso-parameter baseline or explicitly acknowledge the architectural confound, framing TNT as a unified architecture-plus-training contribution.
- Soften the Q-K projection framing from "resolves a fundamental inconsistency" to "provides an effective heuristic."
- Report how parameters are allocated across global and local modules for each configuration.

## Calibration Anchor Comparison

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| DEER (E34AlVLN0v) — Parallelizing non-linear sequential models | 6.00 | R2 | TNT is substantially stronger: comprehensive LM experiments vs. 2 small tasks, 17× wall-clock speedup, clear ablation |
| MELODI (TvGPP8i18S) — Hierarchical memory compression | 6.25 | R1 | TNT has stronger empirical results and a more novel mechanism (periodic resets) |
| HOMER (ulaUJFd96G) — Hierarchical context merging | 6.25 | R1 | TNT's contribution is more novel and better empirically validated |
| Flash Inference (cZWCjan02B) — Inference speedup for LCSMs | 6.83 | R2 | TNT has stronger practical impact (17× training vs. 1.6× inference speedup) but Flash Inference has more rigorous theory |
| HShare (Tb5PY5vwp6) — Hierarchical KV sharing | 6.80 | R2 | TNT's contribution is more novel and transformative; HShare is more incremental |
| LongLoRA (6PmJoRfdaK) — Efficient fine-tuning for long-context LLMs | 7.00 | R2 | LongLoRA is better executed with fewer methodological gaps; TNT has a more novel mechanism |

**Round 1 bracket**: 6.0–7.5. **Round 2 narrowing**: TNT is clearly above the 6.0–6.25 band (DEER, MELODI, HOMER) and sits near the 6.8–7.0 band (Flash Inference, HShare, LongLoRA). The two Major weaknesses (architectural confound, missing aggregation specification) pull TNT below the cleaner 7.0 papers but the novelty and empirical results keep it well above 6.0. Final score: **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>