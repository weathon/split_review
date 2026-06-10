Now let me write the final review.

## Summary
LoLoRA proposes modifying LoRA fine-tuning by updating adapter matrix A using gradient-free local learning rules (Hebbian PCA / SNL or autoencoder loss) during the forward pass, while training B via standard backpropagation. This avoids storing A's input activations, reducing memory. The paper provides Theorem 4.4 showing that under a random regression matrix assumption, the optimal A is any nonsingular transformation of the top-r eigenvectors of the input covariance matrix, and experiments across RoBERTa-large/GLUE, LLaMA-3.1-8B/GSM8K, LLaVA-v1.5-7B, and ablations on TinyLlama-1.1B/Alpaca.

## Strengths
- **Rigorous theoretical characterization of optimal A initialization (Theorem 4.4):** Section 4 proves that the exact set of optimal A matrices is {A | ∃C∈R^{r×d}, V∈V : AΣ^{1/2}_{zz} = CV^T, rk(C)=d} — any nonsingular transformation of the top-r eigenvectors of the input covariance. This formally validates and generalizes the empirical EVA initialization (Paischer et al., 2024), extending it from one specific initialization to an entire equivalence class. The complementary Theorem 4.5 showing B has no preferred initialization (any full-rank B is equally optimal) cleanly establishes the A/B asymmetry.
- **Memory savings with maintained performance on reasoning (Table 3):** On LLaMA-3.1-8B → GSM8K Platinum, LoLoRA HPCA achieves 82.9% accuracy (matching LoRA-FA(EVA)) while using 26 GB peak extra memory vs. 30 GB for standard LoRA — ~13% memory reduction. This directly demonstrates the method's practical value on a reasoning benchmark.
- **Systematic ablations validate theoretical predictions (Tables 5–6):** All methods that converge to the PCA subspace of inputs (HPCA, AE, HPCA svd first) perform comparably and uniformly outperform SoftHebb (which does not converge to PCA), directly confirming the theory's key prediction. LoRA-FA with EVA initialization also performs well, consistent with Theorem 4.4.
- **Clean algorithmic specification (Algorithm 1):** The algorithm precisely shows where memory savings arise: line 6 (`FREE_MEMORY(z)`) frees the input activation immediately after the forward pass, retaining only u = Az for B's backward pass.
- **Honest reporting:** The paper acknowledges that "classical LoRA remains the strongest overall" on GLUE, that multimodal memory gains are limited, and the conclusion accurately bounds claims ("HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups").

## Weaknesses

### Fatal
None.

### Major
- **Abstract overstates empirical results:** The abstract claims "maintains performance comparable to standard LoRA while further reducing the memory." On GLUE (Tables 1–2), LoLoRA underperforms standard LoRA on 7/8 tasks (e.g., CoLA: 66.3 vs. 69.6, a 3.3-point gap). On LLaVA (Table 4), LoLoRA perplexity is 2.93 vs. LoRA's 2.90 (error bars ±0.01, non-overlapping). Only on GSM8K does LoLoRA match or slightly beat LoRA. The paper's own section summaries acknowledge this ("classical LoRA remains the strongest overall"), but the abstract creates a misleading expectation. The paper is really demonstrating a memory-performance *tradeoff*, not maintaining comparable performance.
- **Theoretical assumption is strong and unvalidated:** Theorem 4.4 assumes ΔW_0 has i.i.d. Gaussian entries (Assumption 4.1, line 150). Real fine-tuning weight changes are low-rank, task-specific, and structured. The paper does not show (a) how sensitive the result is to violations of this assumption, (b) whether empirical ΔW_0 from actual fine-tuning resembles a random matrix, or (c) under what practical conditions the approximation holds. The conclusion (PCA initialization is optimal for A) may still be correct, but the theoretical argument as stated is disconnected from the practical setting. A simple experiment measuring the alignment between empirical ΔW_0 and the theoretically predicted form would substantially strengthen Section 4.
- **Narrow baseline comparison set:** The only baselines are LoRA, LoRA-FA, and LoRA-FA(EVA). No comparison with GaLore, DoRA, LoRA+, rsLoRA, or other gradient-compression approaches. Given the paper's pitch is memory-efficient fine-tuning, the reader cannot judge whether LoLoRA's ~13% memory savings on GSM8K or ~2% savings on LLaVA are competitive with alternatives that achieve similar or greater savings through different mechanisms.

### Minor
- **GSM8K evaluation protocol may bias results:** The model is tested every 0.2 epochs and best result is reported for each method (line 265). This favors methods with more checkpoint variance across the evaluation grid. Reporting results at fixed intervals or at the final checkpoint would be more informative.
- **EVA initialization overhead is never measured:** The paper repeatedly frames LoLoRA as advantaged over EVA because it is "online" (lines 17, 328), but EVA's preprocessing cost is not quantified. If EVA's overhead is small, the practical advantage of online updates narrows substantially, and LoLoRA's niche shrinks to settings where input distribution shifts during training.
- **LLaVA memory savings are negligible:** Table 4 shows LoLoRA uses 24.1 GB vs. 24.6 GB for LoRA (~2% savings), attributed to the short textual component relative to image tokens (line 296). This significantly limits the method's applicability to multimodal settings, which is underexplored.
- **No wall-clock training time for main experiments except LLaVA:** Since LoLoRA adds local optimizer steps to the forward pass (Algorithm 1, lines 2–4), the time cost matters for the practical memory-compute tradeoff. Only LLaVA (Table 4) reports runtime.

### Trivial
None.

## Nice-to-Haves
- Validate the theoretical assumption by measuring the effective rank and entry distribution of empirical ΔW_0 from actual fine-tuning runs.
- Focus experiments on settings where LoLoRA actually helps (deeper GSM8K investigation with more ranks/tasks/models).
- Report training throughput across methods to clarify the memory-compute tradeoff.
- Supplement GSM8K results with final-checkpoint performance to rule out checkpoint-selection bias.

## Removed Points
These points are flagged to be removed, treat them with caution.
- The harsh critic's criticism about Definition 3.1 listing "W_q, W_k, W_o, W_o" (duplicate W_o) — this is a formatting/parser artifact, not a paper problem.
- The strength finder's "Multi-domain evaluation" strength — while the paper does evaluate across domains, the evaluation is narrow (only 3 baseline methods) and results are mixed across domains, conflicting with the verified weakness about narrow comparison set.
- The harsh critic's claim about LLaVA validation being "in-distribution" as a significant flaw — while technically true (deferred portion of same pool), this is a common evaluation practice and the paper is transparent about it. Demoted to nice-to-have.

## Novel Insights
The key novel insight from this paper is the formal proof (Theorem 4.4) that under random regression assumptions, the optimal A for frozen-A LoRA is any nonsingular transformation of the top-r eigenvectors of the input covariance — providing theoretical grounding for EVA's empirical observation that PCA-based initialization helps. The complementary Theorem 4.5 showing B has no preferred initialization (any full-rank B works equally) establishes a clean asymmetry between adapters. The integration of this theory into an online local-update framework (LoLoRA) that avoids storing activations while converging to the same PCA subspace is a genuine algorithmic contribution, though the practical benefit over simply using EVA initialization remains unclear.

## Suggestions
- Revise the abstract to accurately characterize the performance tradeoff (e.g., "achieves performance competitive with LoRA on reasoning tasks while reducing memory, with some cost on NLU benchmarks").
- Add at least one comparison to a non-LoRA memory-efficient method (e.g., GaLore or gradient checkpointing) to contextualize the memory savings.
- Measure EVA's preprocessing cost to quantify the practical advantage of LoLoRA's online approach over one-shot initialization.
- Validate the random matrix assumption by measuring properties of empirical ΔW_0 from actual fine-tuning runs.

## Calibration Report

**All retrieved anchors:**

| Round | Paper | Avg Score | Path |
|-------|-------|-----------|------|
| 1 | ALLoRA | 3.33 | 7X65yoKl3Y |
| 1 | HoLoRA | 3.00 | igGeaxOiFM |
| 1 | UnoLoRA | 3.00 | 49ti6LOUw5 |
| 1 | L-MSA | 3.00 | xi3sDtf8A0 |
| 1 | LoRA-FA | 5.33 | RbKThNNFxr |
| 1 | ReLoRA | 5.75 | DLJznSp6X3 |
| 1 | Maintaining Structural Integrity | 5.75 | OALIb8oNfl |
| 1 | LoRAM | 6.20 | s7DkcgpRxL |
| 1 | HiRA | 8.00 | TwJrTz9cRS |
| 1 | Training on Test Task | 8.00 | jOmk0uS1hl |
| 1 | Dimensional Collapse | 8.00 | f4gF6AIHRy |
| 1 | Small-scale proxies | 8.00 | d8w0pmvXbZ |
| 2 | EVA | 4.75 | DM6Q45HWSk |
| 2 | ROSA | 6.00 | cgCKm5DOnu |
| 2 | Quest for Winning Tickets | 5.20 | PxYhHF6FNH |
| 2 | GeoLoRA | 6.25 | bsFWJ0Kget |
| 2 | AdaRankGrad | 7.00 | LvNROciCne |
| 2 | LoRAM (repeat) | 6.20 | s7DkcgpRxL |
| 2 | ReLoRA (repeat) | 5.75 | DLJznSp6X3 |
| 2 | Fira | 5.75 | lR7rqLtsXZ |

**Round 1 bracket:** 5.5 – 6.5. LoLoRA is clearly better than LoRA-FA (5.33) and EVA (4.75) due to its theoretical contribution and local updates, but weaker than GeoLoRA (6.25) and AdaRankGrad (7.00) due to mixed experiments and narrow baselines.

**Round 2 narrowing:** Within the bracket, LoLoRA is comparable to ROSA (6.00, Reject) — both have genuine theoretical contributions but limited practical demonstration. LoLoRA has a cleaner theory but narrower experiments. It's slightly below GeoLoRA (6.25, Accept) which has stronger convergence guarantees, adaptive rank, and more convincing results. It's clearly below AdaRankGrad (7.00, Accept) which has a formal proof about gradient rank, convergence analysis, and broader experiments.

**Final score: 6.0** — The paper has a genuine theoretical contribution (Theorem 4.4) that formally justifies PCA-based A initialization, clean ablations that validate the theory, and a practical memory-saving result on GSM8K. However, the abstract overstates results, the theoretical assumption is unvalidated, the baseline set is narrow, and experiments show mixed performance (underperforms LoRA on most GLUE tasks, negligible LLaVA savings). The score positions it comparable to ROSA (6.00) and slightly below GeoLoRA (6.25), reflecting a paper with solid theoretical insight but insufficient empirical validation.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>