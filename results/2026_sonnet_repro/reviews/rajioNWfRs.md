Now let me run the calibration search to bracket the score.Now let me read one more anchor that's directly relevant to narrow my bracket:Now I have enough information to write the final review. Let me synthesize all findings.

---

## Summary
TNT (Two-stage Non-linear Training) introduces a training paradigm for deep memory modules (Titans, TTT) that decouples training efficiency from inference performance. The framework combines a hierarchical global+local memory architecture with periodic local state resets enabling context parallelism, plus a Q-K projection to resolve the compression-retrieval domain mismatch, followed by a brief fine-tuning phase at smaller chunk sizes. The paper demonstrates up to 17× faster training-to-quality over baseline Titans while simultaneously improving language modeling perplexity and common-sense reasoning accuracy.

---

## Strengths

- **Training acceleration is robustly demonstrated.** Table 1 shows TNT at $C_L = \{64\}$ reaches the target loss of 3.20 in 1.12 hrs vs. 19.48 hrs for Titans $C=8$, a 17.37× speedup. Figure 4 confirms linear runtime scaling vs. the quadratic growth of standard attention; at 32K context, TNT is 5.1× faster than Titans at equal chunk size. This is the central claim of the paper and it is well-supported.

- **Quality improvement alongside efficiency.** Table 2 shows TNT Stage 1 with four local modules achieves avg. perplexity 23.13 vs. the best Titans baseline at 25.07, while also outperforming the vanilla Transformer (23.58). Simultaneously beating the baseline on both speed and quality is a non-trivial result.

- **Ablation validates each component.** Table 3 isolates the contributions of the global memory (removal → PPL increases from 21.04 to 25.60), the Q-K projection (removal → PPL increases from 21.04 to 22.01), and multi-local-module scaling (step-wise PPL improvements from 21.04 → 20.74 → 20.47 → 20.15 as modules are added). These are meaningful quantitative differences confirming each component's role.

- **Q-K projection is a principled and validated improvement.** The ablation (21.04 → 22.01 PPL, Table 3) provides direct evidence that projecting queries onto the key subspace mitigates the compression-retrieval domain mismatch identified as Challenge 2.

- **Periodic reset enabling non-linear context parallelism is a novel contribution.** Enabling true context parallelism for non-linear recurrences (with LayerNorm between steps) that don't admit parallel-scan solutions is a long-standing challenge; the reset mechanism is a clean and practical solution.

---

## Weaknesses

### Fatal
None.

### Major

- **No long-context quality evaluation despite long-context being the stated motivation.** The abstract, introduction, and conclusion repeatedly frame TNT as enabling models to operate on "truly long sequences." Efficiency results (Figure 4, Table 1) show linear scaling up to 32K tokens. However, all quality evaluations (Table 2) are at 16K context on C4, FineWeb, PG19, PIQA, HellaSwag, ARC-Easy, and CSQA — none of which stress long-range dependency resolution. No needle-in-haystack retrieval, passkey recall, SCROLLS, RULER, or analogous long-context benchmark is included. The question of whether TNT's global memory actually improves long-range *understanding* — as opposed to just *speed* — remains open, creating a gap between the paper's stated motivation and its evidence. Comparable accepted works on long-context training (e.g., papers that also propose two-stage efficient training) include both efficiency *and* long-context quality benchmarks; TNT does not, which limits the paper's ability to substantiate its core claim.

- **Contribution attribution is complicated by inseparable architectural and paradigm changes.** The paper is framed as a training paradigm, but TNT also introduces new architectural components (hierarchical global+local memory, Q-K projection). The quality gains in Table 2 and Table 3 reflect both the training strategy (periodic resets) and additional memory capacity (N local modules + 1 global). The ablation in Table 3 shows removing the global memory raises PPL by 4.56 and removing Q-K projection raises PPL by ~1, but there is no controlled comparison: a Titans model with a matching global+local parameter budget trained at a fixed chunk size (no periodic reset), to isolate the periodic-reset mechanism from the added memory capacity. A reader trying to apply TNT to a new architecture cannot confidently determine whether quality gains come from the training schedule or the architectural additions.

### Minor

- **Stage 2's empirical contribution is marginal and framed as more significant than the numbers support.** In Table 2, Stage 2 reduces average perplexity by 0.04 (23.13 → 23.09) for the four-module case, and improves accuracy by 0.3% (40.6% → 40.9%) — within plausible noise at this evaluation scale, with no variance or significance statistics reported. The paper describes Stage 2 as "consistently lowers the average perplexity" and a full "performance-focused fine-tuning stage addressing Challenge 3," when the numbers support "cheap calibration step that marginally aligns inference chunk resolution." The 5% compute overhead is a genuine positive, but the actual quality benefit is not well-supported as a substantial stage.

- **Ablation uses a weaker Titans baseline.** Table 3 uses "Base Model (Titans)" with 23.53 PPL, which corresponds to Titans $C=256$ (Table 2). The best Titans configuration in Table 2 is $C=8$ (C4 PPL = 22.25, avg PPL = 25.07). Using the weaker Titans $C=256$ as the ablation starting point makes the incremental improvements from TNT components appear larger against a comparably weaker reference. The comparison is not misleading (Titans $C=256$ vs. TNT both use large chunk sizes), but it understates Titans' peak capability in the ablation context.

- **Inference behavior at generation time is underspecified.** Section 4.2 states "the local memory handles iterative decoding" and the system aligns with "the standard prefill-and-decode paradigm." But for sequences exceeding $S_L$ (set to 4096 in performance experiments), it is unclear whether the local memory resets mid-generation, what happens to the state continuity, and whether the model was fine-tuned to handle this case. This is a concrete operational gap for practitioners.

### Trivial

- Figure 2 uses a 550M-parameter model, while all subsequent experiments use 150M. The chunk-size sensitivity phenomenon (Challenge 3) is visually demonstrated at 550M but is never explicitly confirmed at 150M. The qualitative result likely transfers, but confirmation would be straightforward and strengthen the motivation section.

---

## Nice-to-Haves

- An experiment isolating the periodic-reset mechanism from the additional memory capacity: train Titans with N+1 modules at a matched total parameter budget, fixed chunk size, no resets, and compare quality and speed against TNT. This would cleanly establish whether the training paradigm itself (not just extra capacity) drives quality gains.

- Error bars or multi-seed variance on Table 2 accuracy numbers. The 1.3pp difference between TNT (41.0%) and Gated Transformer (39.7%) and the 0.3pp differences from Stage 2 are difficult to interpret without some estimate of evaluation variance.

- A gated (learned-weight) combination of global and local memory outputs in Eq. 7, with an ablation. The current equal-weight summation is arbitrary; a gating mechanism might improve performance and would justify the design choice with evidence.

- The Q-K projection is described as projecting onto "the subspace spanned by keys," but $\sum_\tau k_\tau k_\tau^\top / \|k_\tau\|^2$ is not an orthogonal projector in general (it is only idempotent when keys are orthonormal). A cleaner motivation — e.g., as a query regularization toward the key distribution, or in terms of minimizing a distributional objective — would strengthen the theoretical framing of Section 4.1.2.

---

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **"17× faster framing is misleading"** (Harsh Critic): The paper is transparent about the comparison in Table 1 and Section 5.2 explicitly notes "using an identical local memory chunksize of 8, TNT is already 7.7× faster." The headline comparison (same target quality, different chunk sizes) is a legitimate quality-adjusted metric, not a misleading one.

- **"Equal-weight global+local output is unmotivated — no ablation of gated combination"** (Harsh Critic): Moved to Nice-to-Haves. This is an architectural choice without ablation, but not a flaw that undermines the core claim.

- **"Stage 2's contribution is fatal/structural"** (Harsh Critic, "Stage 2 is not well-supported"): Downgraded to Minor. Stage 2 does consistently reduce PPL across all configurations in Table 2, even if modestly. The framing is overstated, but Stage 2 is a real (if small) improvement.

- **Strengths about "addressing an important problem" and "establishing a promising paradigm"** (Strength Finder): Removed as generic. Retained only strengths tied to specific tables, figures, or mechanisms.

- **Concern that the ablation uses Titans C=256 as the base unfairly**: This is kept as Minor since the paper does show both C=8 and C=256 in Table 2, so readers can calibrate, but the ablation table does selectively use the weaker baseline.

---

## Novel Insights

The periodic-reset mechanism for local memory is the paper's most transferable technical contribution: by training local modules with a fixed-interval state reset to a learned initialization, the sequential inter-shard dependency is broken, enabling true context parallelism without requiring linear state transitions. This is distinct from parallel-scan methods (which require linearity) and from chunked-attention hybrids (which change the architecture fundamentally). The insight that a non-linear RNN's training parallelism problem is equivalent to designing the model so that long-range context is fully handled by a separate module (the global memory), freeing the local module to be reset and parallelized, is conceptually clean and potentially applicable beyond Titans/TTT to any architecture with separable local/global processing needs.

---

## Suggestions

1. **Add at least one long-context quality benchmark** (e.g., passkey retrieval at 32K–128K, or a RULER sub-task) comparing TNT against Titans-$C=128$ (the only speed-comparable baseline). A single controlled result showing global memory retains long-range information that Titans-large-chunk drops would directly validate the motivational claim.

2. **Add an ablation isolating the periodic-reset mechanism from the extra memory capacity**: a Titans model with global+N-local modules at matched parameter count, trained without resets at a fixed chunk size, compared against TNT. This would cleanly establish what portion of the quality gain is attributable to the paradigm vs. the architecture.

3. **Clarify inference behavior beyond $S_L$**: Add a paragraph to Section 4.2 explaining what happens to local memory states during autoregressive generation when the generated sequence exceeds $S_L$, and whether the model is fine-tuned to handle this.

4. **Reframe Stage 2** as a "cheap inference-resolution calibration step" rather than a full stage addressing Challenge 3. Report variance on Table 2 accuracy numbers to establish whether Stage 2's 0.3pp accuracy changes are reliable.

---

## Score and Decision

**Round 1 bracket (from search):** Papers in the 3.5–7.5 range on similar topics (RNN parallelization, efficient sequence model training) span 5.0–6.5. The paper clearly exceeds the weak/rejected band (2–3) and does not reach top-tier (7.5+). Initial bracket: **5.0–7.0**.

**Round 2 narrowing:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Parallelizing non-linear sequential models (DEER) | E34AlVLN0v | 6.00 | R1 | Parallelizes non-linear RNNs via Newton's method; smaller-scale evaluation, no LM quality eval; TNT is stronger on all these dimensions |
| FlashRNN | l0ZzTvPfTw | 6.50 | R1 | Hardware optimization for LSTM/GRU; no accuracy comparison; TNT includes quality eval |
| MELODI (hierarchical memory compression) | TvGPP8i18S | 6.25 | R2 | Hierarchical memory for long contexts; limited to perplexity, no efficiency benchmarks; TNT has efficiency + quality together |
| A Little Goes a Long Way (LongGen) | TrKRpaOk8y | 6.40 | R2 | Two-stage efficient long-context training; includes BOTH efficiency and long-context quality benchmarks (Needle-in-Haystack, RULER); TNT lacks long-context quality eval |
| Were RNNs All We Needed? | GrmFFxGnOR | 5.00 | R1 | Revived LSTMs/GRUs with parallelization; TNT is more complete and tackles a harder problem |

**Final bracket narrowing:** TNT is clearly stronger than DEER (6.0) due to larger evaluation scale and quality metrics. It is comparable to MELODI (6.25) but stronger on efficiency evidence. It is weaker than LongGen (6.40) because LongGen validates long-context quality (the very thing TNT's motivation demands) while TNT does not. TNT approaches but does not reach FlashRNN (6.50), which lacks quality comparisons but has deeper hardware engineering.

The long-context quality gap is a genuine major weakness that prevents TNT from reaching 6.5+. The core efficiency contribution is solid and independently valuable. The paper sits between MELODI (6.25) and FlashRNN (6.50), closer to the lower end given the motivational-evidential gap.

**Originality:** Good — periodic reset for non-linear context parallelism is a novel contribution.  
**Importance:** High — addresses a genuine practical bottleneck in expressive RNN training.  
**Claim support:** Partial — efficiency claims fully supported; quality-at-long-context claims unsupported.  
**Experimental soundness:** Good for efficiency; adequate but incomplete for quality.  
**Clarity:** High — well-written, clearly structured.  
**Community value:** High for the deep memory module community.

**Final Score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>