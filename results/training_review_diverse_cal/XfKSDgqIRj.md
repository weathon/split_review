I now have a complete picture. Let me write the final consolidated review.

## Summary

This paper introduces COAT, a framework for FP8 training that quantizes both optimizer states and activations to FP8—something prior frameworks (TransformerEngine, FP8-LM) did not fully do. Two key innovations are proposed: (1) **Dynamic Range Expansion**, which per-group applies a power function $f(x)=\text{sign}(x)|x|^k$ to align optimizer state distributions with FP8's representation range before quantization (reducing MSE by $1.63\times$), and (2) **Mixed-Granularity Activation Quantization**, which applies per-group quantization ($1\times G$) to non-linear layers (RMSNorm, activations) and per-tensor quantization to linear layers, achieving $1.65\times$ activation memory reduction. End-to-end experiments show $1.54\times$ memory reduction and $1.43\times$ speedup over BF16 on Llama-7B/13B/30B, with nearly lossless accuracy on LLM pretraining, fine-tuning, and VLM training.

## Strengths

- **Dynamic Range Expansion is well-motivated and effective.** The paper identifies that optimizer states under-utilize FP8's representational range (Fig. 3a). The proposed expand function is cleanly derived from formalizing "dynamic range" and solving for the optimal $k = \log_{\mathcal{R}_X}(\mathcal{R}_{\text{E4M3}})$. Quantitatively, it reduces MSE of the effective update $\frac{m}{\sqrt{v}}$ from 20.10 (E4M3/E4M3) to 12.31 (E4M3+Expand/E4M3+Expand), a $1.63\times$ improvement (Table 1). The ablation in Table 6 further shows the method generalizes to DE8 quantization, improving MSE from 10.54 to 7.47 ($1.41\times$).

- **Mixed-Granularity Activation Quantization targets an overlooked source of memory.** The paper decomposes activation memory (Table 2) and shows non-linear layers (RMSNorm, activation functions) account for ~53% of activation memory in Llama-style models—a portion ignored by prior FP8 frameworks. The insight that quantizing across the token axis harms accuracy (Fig. 5a) and that per-group ($1\times G$) rather than per-block ($B\times B$) quantization avoids this is a clean contribution. The achieved $1.65\times$ memory reduction is close to the theoretical $1.69\times$ bound.

- **End-to-end memory and speed gains are demonstrated at practically relevant scales.** COAT reduces peak memory from 55.1 GB to 35.6 GB on Llama-2-7B (4 GPUs, $1.54\times$) and achieves $1.45\times$ speedup (Table 7). It enables full-parameter training of Llama-2-7B on a single GPU, Llama-2-13B on 2 GPUs, and Llama-30B on 8 GPUs—settings where both BF16 and TransformerEngine run out of memory. The speed/memory results cover 7B, 13B, and 30B models with varying GPU counts, providing a practical picture.

- **Nearly lossless accuracy across multiple tasks.** COAT matches BF16 within 0.3 percentage points on OLMo-1B pretraining (22B tokens, Table 3), Llama-2-7B math fine-tuning (Table 4), and VILA1.5-7B VLM SFT (Table 5). Training curves align closely with baselines. This is the strongest evidence that the aggressive FP8 quantization (both optimizer states and activations) does not degrade performance.

## Weaknesses

### Fatal
None.

### Major
1. **Expand function overhead and numerical stability are not evaluated.** The paper computes $k = \log_{\mathcal{R}_X}(\mathcal{R}_{\text{E4M3}})$ on-the-fly per quantization group per optimizer step, and then applies $|x|^k$ and its inverse to every element. For a 7B model with group size 128, this affects tens of millions of groups per step. The paper provides no wall-clock measurement of this overhead, no breakdown of how much of the claimed $1.43\times$ speedup is net of this cost, and no ablation comparing with/without the expand function. Additionally, when $\mathcal{R}_X$ is very close to 1 (which can happen for some groups in second-order momentum), $k$ becomes large and $|x|^k$ could overflow even FP32 intermediate values. The histogram in Fig. 3c shows $k$ up to ~15 for second-order momentum, but the paper does not discuss numerical safety margins or whether any group ever requires a $k$ that causes overflow. These gaps make it impossible to assess whether the expand function's overhead and risk are justified. The end-to-end speedup numbers include this overhead, but without an ablation the net benefit of the expansion itself is unclear.

2. **The 7B continue-pretraining experiment is too short to fully support the "nearly lossless" claim at the scales where the method's memory benefits are largest.** The OLMo-7B experiment runs for only 1000 steps (~4B tokens) from an existing checkpoint. While the 1B pretraining (22B tokens, from scratch) is more substantial, the paper's primary audience cares about 13B–30B models where memory savings are most impactful, yet no accuracy results are shown beyond 7B. The memory/speed benchmarks cover up to 30B, creating an asymmetric evidentiary gap. This does not invalidate the paper's claims—the 1B results and the fine-tuning/SFT experiments are convincing at their respective scales—but it limits the generality of the "nearly lossless" assertion for the largest models.

### Minor
1. **Missing ablation: no experiment separates activation quantization error from optimizer quantization error.** The paper does not compare (a) optimizer quantization only vs. (b) activation quantization only vs. (c) both combined. Without this, it is impossible to attribute any observed degradation to one source or the other, and the paper cannot show that the novel activation quantization (the mixed-granularity scheme) is independently lossless. Since TransformerEngine already handles linear-layer FP8 computation, a "COAT without activation quantization" baseline would cleanly isolate the two contributions.

2. **RMSNorm memory saving (4U → 1U) is not fully explained.** In Table 2, RMSNorm goes from 4U (BF16) to 1U (COAT), a 4× reduction. Simple FP8 quantization (halving precision) would yield 2U. Achieving 1U suggests the paper also stores fewer tensors (e.g., only the FP8 input instead of all four intermediate tensors). The paper's caption attributes the saving purely to "quantizing them to FP8" without clarifying the algorithmic change. This matters because the claimed $1.65\times$ activation memory reduction may partially reflect a different recomputation strategy rather than strictly quantization. The authors should decompose how much of each saving comes from precision reduction vs. reduced storage of intermediate values.

3. **No ablation on quantization group size.** The paper uses group size 128 for optimizer states and $1\times16$ for non-linear layer activations but provides no sensitivity analysis. Group size directly affects both the overhead of computing $k$ (for optimizer states) and the accuracy of quantization. Showing that results are robust to varying group size by, e.g., $\pm 2\times$ would strengthen the paper.

4. **Group Scaling vs. Delayed Scaling:** Figure 5b shows Group Scaling is timing-competitive with Delayed Scaling (~0.36 ms vs ~0.38 ms), but no precision comparison (e.g., validation loss or gradient error) is provided to justify the claim that Group Scaling "could be even better in precision." This is a minor omission—the timing equivalence is the main result—but the precision claim remains unsupported.

### Trivial
None.

## Nice-to-Haves
- A wall-clock breakdown of the expand function overhead vs. other quantization/dequantization operations.
- Offline measurement of the MSE of $\frac{m}{\sqrt{v}}$ and gradient error from activation quantization at 13B/30B scale (requires only checkpoints, not full training).
- Group size sensitivity study for both optimizer and activation quantization.

## Removed Points
- **"DE8+Expand for both orders gives MSE of 7.47" (from Harsh Critic):** Factually incorrect. Looking at Table 6 (expand_quant_and_DE8), the MSE of 7.47 is for *mixed* formats (DE8+Expand first order, E4M3+Expand second order). DE8+Expand for *both* orders gives MSE 15.81. The paper's main configuration (E4M3+Expand for both) gives MSE 12.31. The broader concern about MSE being non-negligible is also contradicted by actual training results showing no degradation, so this entire sub-point is removed.
- **"The speedup comparisons conflate memory capacity with raw compute speed":** The harsh critic themselves acknowledge this is reasonable ("the comparison is fair"). Not a weakness.
- **"Group Scaling vs Delayed Scaling timing shows they are nearly identical":** This is presented as a missing precision comparison. The timing comparison itself is the claimed contribution—Group Scaling is simpler and avoids delayed-scaling heuristics. The precision claim is noted above as Minor weakness 4, not a structural issue.

## Novel Insights
The reviewer's primary insight—that the paper's accuracy validation is asymmetric relative to its memory/speed claims—raises a genuine question about scope of evidence in systems papers. COAT's memory savings are most valuable at scales where full-precision training is infeasible (e.g., Llama-30B on 8 GPUs), but accuracy validation stops at 7B. This is a common tension in ML systems research (validating at affordable scales, claiming at practical ones). What makes COAT's case stronger than typical is that the 1B pretraining is a full from-scratch run (22B tokens), and the MSE analysis (Table 1) provides supporting evidence that quantization error at the optimizer-state level is bounded. However, the missing ablation separating activation from optimizer quantization error is a notable gap—without it, the paper cannot attribute its losslessness to the right component, which matters for future work building on either technique independently.

## Suggestions
1. **Add an overhead breakdown for the expand function** — measure the fraction of total step time spent computing $k$, applying $|x|^k$, and applying the inverse. This can be done with simple CUDA event timing.
2. **Run an ablation separating activation quantization from optimizer quantization** — compare (a) BF16, (b) BF16 + COAT's optimizer quantization only, (c) BF16 (but save FP8 activations) + COAT's activation quantization only, (d) full COAT. Even on 1B for a shorter run, this would cleanly attribute any degradation.
3. **Add an offline error analysis at 13B scale** — take BF16 checkpoints from a 13B training run (or train one briefly), apply the COAT quantization pipeline in a static pass, and measure the MSE of $\frac{m}{\sqrt{v}}$ and the gradient perturbation from activation quantization. This would bridge the gap between the 7B accuracy validation and the 30B memory claims without requiring a full 30B training run.
4. **Clarify the RMSNorm memory accounting** — explain which tensors are saved in BF16 vs. FP8 and which are recomputed, so readers can distinguish the roles of quantization vs. recomputation in the reported savings.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>