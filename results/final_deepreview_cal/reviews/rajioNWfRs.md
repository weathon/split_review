Now I have a solid picture of the paper and the calibration anchors. Let me compile the final review.

## Summary
This paper presents TNT, a two-stage training framework for deep memory modules (e.g., Titans) that decouples training efficiency from inference performance. The key ideas are: (1) a hierarchical memory with a global module handling long-range context on large chunks and local modules with periodic state resets enabling context parallelism; (2) a Q-K projection that aligns the compression and retrieval domains; and (3) a brief Stage-2 fine-tuning that adapts pre-trained models to small-chunk inference. On 150M-parameter Titans models, TNT achieves up to 17× training speedup while improving perplexity and downstream accuracy.

## Strengths
- **Hierarchical memory with periodic resets enables context parallelism for non-linear recurrences.** By resetting local memory states at shard boundaries, TNT breaks sequential dependencies that previously prevented parallelization of deep memory modules. This is directly evidenced by the linear runtime scaling in Figure 4, where TNT with C_L=128 outperforms even the highly optimized FlashAttention kernel at sequence length 32K.
- **Q-K projection resolves the compression–retrieval domain mismatch.** The paper correctly identifies that memory modules compress key→value mappings but are queried with queries, and proposes projecting queries onto the key subspace via a running-sum outer-product matrix. The ablation (Table 3) shows removing it raises perplexity from 21.04 to 22.01, confirming its substantial impact.
- **Stage-2 fine-tuning is efficient and effective.** A brief second stage using smaller chunks (costing only ~5% of pre-training compute, Section 5.3) adapts large-chunk pre-trained models to high-resolution inference, bridging a train–test mismatch that would otherwise require costly retraining (Challenge 3, Figure 2).
- **Multi-resolution local memories provide consistent gains.** Adding parallel local modules at different chunk sizes (e.g., {8,16}) improves perplexity and downstream accuracy over single-resolution variants (Table 2), showing that multi-scale temporal modeling is beneficial for deep memory architectures.

## Weaknesses

### Fatal
None.

### Major
- **Abstract overclaims evaluation scope ("Evaluated on Titans and TTT models").** The abstract states TNT is "evaluated on Titans and TTT models," implying TNT was applied to both architectures. In the actual experiments (Section 5), TNT is instantiated only on Titans; TTT appears solely as a baseline with its original training recipe (Table 2). This misrepresents the evidence for TNT's claimed generality and should be corrected.
- **Parameter counts across TNT configurations are not documented or controlled.** The paper states all models are "150M parameter models" (Section 5.1), but adding multiple local memory modules (N=2, 3, 4 in the ablation, Table 3) plausibly increases total parameter count through their own projection and fast-weight parameters. Without per-configuration parameter counts or a parameter-matched comparison, the quality improvements attributed to multi-resolution local memories (e.g., perplexity dropping from 23.53 to 20.15 with 4 local modules) cannot be confidently attributed to architectural design rather than increased capacity. The authors should report parameter counts for each TNT configuration and ideally include a parameter-matched Titans baseline.

### Minor
- **No full learning curves provided.** Table 1 reports time to reach a single target loss (3.20), which captures early-stage throughput but does not reveal whether TNT saturates at a higher or lower final loss than baselines, or how relative speedup evolves over full training. Loss-vs-wall-clock-time curves would give a more complete picture.
- **Q-K projection memory cost (O(d²)) not discussed.** The projection matrix is maintained as a running sum of outer products, which requires O(d²) memory per local memory module. For large model dimensions this could be significant, and the interaction with chunk parallelism and hardware is not analyzed.
- **Generality claim not validated.** TNT is presented as a "general training paradigm applicable to any deep memory module" (Section 1) and "model-agnostic" (Section 5), but experiments are limited to Titans. Applying TNT to TTT or another deep memory module would substantially strengthen this claim.

### Trivial
- The paper lacks a limitations section discussing, e.g., the O(d²) state from Q-K projection, reliance on tuned global/local chunk sizes, and the current absence of a custom kernel.
- Section 4.2 is slightly ambiguous about which parameters are updated in Stage 2; the abstract says "only the local memory modules," which should be stated explicitly in the main text as well.

## Nice-to-Haves
- Full training curves (loss vs. wall-clock time) for the main TNT and baseline configurations would better characterize whether the speed advantage persists to convergence.
- A comparison against Titans with moderate chunk sizes (e.g., C=64) in the time-to-quality table, not just C=8 and C=16, would strengthen the fairness argument.
- Discussion of how the periodic reset mechanism affects tasks that require long-range dependencies spanning shard boundaries (beyond S_L=2048/4096 tokens).

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh critic's claim that "the baseline Titans uses the smallest chunk size (C=8), which is known to be extremely slow" as inflating the speedup.** REMOVED — Table 1 includes Titans with multiple chunk sizes (C=8, 16, 32, 64, 128), not just C=8. The speedup of 17.37× is measured against the most accurate Titans configuration (C=8, ppl=25.07 in Table 2), and TNT with C_L={64} is 4.67× faster than Titans with C=64. The critic's claim is factually wrong.
- **Harsh critic's demand that the paper "ensure they are comparable to the 150M-parameter baseline models" by matching parameters or adjusting model width/depth.** PARTIALLY REMOVED — the demand for an explicit parameter-matched experiment is kept as a minor-to-major concern, but the critic's framing that this "almost certainly introduces additional parameters" is speculative. The paper may have adjusted other dimensions to maintain 150M total. The retained weakness asks for documentation and control, not an assumption of guilt.
- **Strength Finder claim that "Stage-2 fine-tuning adapts large-chunk pre-trained models to small-chunk inference with minimal overhead" is a core strength.** KEPT as a strength but noted as a supporting one — the Stage 2 mechanism is well-evidenced but largely complementary to the core hierarchical memory contribution.
- **Harsh critic's claim that the "missing parameter counts make it impossible to judge" (fatal).** DEMOTED from fatal to major — the speedup results (the paper's primary claim) do not depend on parameter control. The quality improvement claim is the one affected, and even that has some support from the 1-local-memory vs. Titans comparison in Table 2.
- **Strength Finder's claim that "TNT was evaluated on Titans and TTT models."** REMOVED — this is contradicted by the evidence (TTT is only a baseline, not TNT-enhanced). Kept instead as a major weakness (abstract overclaim).

## Novel Insights
None beyond the paper's own contributions. The key insight — that periodic state resets enable context parallelism for non-linear deep memory modules — is genuinely novel and well-motivated. The Q-K projection as a solution to compression–retrieval domain mismatch is also a clean, practically useful observation.

## Suggestions
- Correct the abstract to accurately reflect that TNT is evaluated on Titans; if TNT was also applied to TTT, add those results; otherwise remove the "and TTT" claim.
- Report per-configuration parameter counts (Table 3 and Table 2) and ideally include a parameter-matched Titans variant to isolate architectural effects from capacity effects.
- Add a brief limitations paragraph addressing the O(d²) Q-K projection state, hyperparameter sensitivity, and the current lack of a custom kernel.

## Score and Decision

### Calibration anchor comparison (all rounds):

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| N581Nje6fH (Episodic Decision Making) | 1.50 | 1 | TNT is far stronger — genuine technical contribution and empirical validation |
| 73dhbcXxtV (LoLaMeMe) | 3.00 | 1 | TNT is substantially stronger — clear problem, clear solution, solid experiments |
| JIlIYIHMuv (LVLM-CL) | 2.50 | 1 | TNT is much stronger — well-scoped contribution with concrete speedups |
| JOBokGDcX0 (Sequence Segmentation) | 2.50 | 1 | TNT is much stronger — addresses a harder problem with more technical depth |
| e1Z4NCQ146 (ProTrain) | 5.25 | 2 | TNT is slightly stronger — more novel architecture, better-motivated problem, but ProTrain has more thorough systems evaluation |
| DfTWrTwLzD (Context Window Extension) | 5.00 | 1+2 | TNT is comparable — both have clever ideas with evaluation gaps |
| ulaUJFd96G (HOMER) | 6.25 | 1 | TNT is slightly weaker — HOMER has slightly more thorough evaluation across tasks; TNT has the abstract overclaim |
| TvGPP8i18S (MELODI) | 6.25 | 1+2 | TNT is slightly weaker — MELODI has comprehensive ablation studies and no overclaim issues |
| TrKRpaOk8y (Partial Contexts) | 6.40 | 2 | TNT is slightly weaker — better evaluation completeness in the anchor |
| fMbLszVO1H (LongMamba) | 6.75 | 2 | TNT is weaker — LongMamba has more thorough analysis and no overclaim |
| cZWCjan02B (Flash Inference) | 6.83 | 2 | TNT is weaker |
| E4Fk3YuG56 (Cut Cross-Entropy) | 8.50 | 1 | TNT is clearly weaker — top-tier paper with flawless execution |
| OfjIlbelrT (FlexPrefill) | 8.00 | 1 | TNT is clearly weaker |
| tyEyYT267x (Interpolating AR/Diffusion) | 8.00 | 1 | TNT is clearly weaker |

**Round 1 bracket:** 4.5–7.0 (between weak middle and strong papers)

**Round 2 narrowing:** TNT sits between ProTrain (5.25) and MELODI/HOMER (6.25). The abstract overclaim and undocumented parameter counts pull it below the 6.0 line. The genuine technical novelty, well-motivated problem, and impressive speedup results (even under generous assumptions) pull it above the 5.0 line. 

**Final score: 5.5** — a borderline paper with real contributions that is held back by correctable evaluation and presentation issues.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>