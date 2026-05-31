Now let me search the calibration set to bracket the score.Initial bracket: 4.5–6.5. Let me read two anchors to calibrate better.Round 1 bracket: **4.5–6.5**. Now narrowing.Now I have enough information to write the full review. Let me synthesize everything.

---

## Summary

WASI (Weight-Activation Subspace Iteration) combines Weight Subspace Iteration (WSI)—applying warm-started subspace iteration from Vogels et al. (2019) to model weight matrices—with an extended version of the authors' prior Activation Subspace Iteration (ASI), creating a unified on-device training framework for vision transformers. The method restricts both weight and activation tensors to stable low-rank subspaces during fine-tuning, aiming to reduce memory consumption and FLOPs. Experiments on ViT, SwinT (across five datasets), and TinyLlama demonstrate up to 62× memory reduction and 1.4× wall-clock speedup on a Raspberry Pi 5.

---

## Strengths

1. **Joint weight+activation compression with controlled information loss.** Unlike ASI (which only compressed activations) or SVD-LLM (which only structured weights), WASI simultaneously reduces both bottlenecks under a unified ε-controlled threshold. Fig. 5 shows WASI achieving up to 100× higher memory efficiency than SVD-LLM at comparable accuracy on ViT/CIFAR-10, and Fig. 6 shows 62× memory reduction at matched accuracy on SwinT across five datasets (Sec. 4.3).

2. **Real on-device hardware validation.** The Raspberry Pi 5 results in Fig. 8 confirm that WASI achieves ~1.4× faster training and inference per iteration versus vanilla training even at the most aggressive compression level (ε=0.9). This is concrete evidence that the theoretical efficiency gains translate to practice, distinguishing WASI from purely simulation-based efficiency papers.

3. **WSI outperforms repeated SVD at matched FLOPs.** Fig. 3b shows that reusing the subspace via WSI achieves the same accuracy with 1.36× fewer FLOPs, and at matched FLOPs outperforms recomputing SVD every step by ~35%. This validates the core hypothesis that subspace stability during fine-tuning can be exploited algorithmically.

4. **DP-based rank selection reduces search cost from exponential to linear.** The paper introduces a dynamic programming strategy (Sec. 3.3, Appendix A.2) to replace the brute-force budget search in ASI, a concrete improvement that makes the method more practical under fixed device budgets.

---

## Weaknesses

### Fatal
None.

### Major

**1. Algorithmic ambiguity in the weight update (Eq. 11 vs. Algorithm 1).** Equation 11 updates the product $L_i R_i \leftarrow L_i R_i + \eta \cdot \overline{\partial \mathcal{L}/\partial \mathcal{W}_i}$, but Algorithm 1 requires the *individual* factors $L_{i(t-1)}$ and $\mathcal{W}_{i(t)}$ at the next iteration (lines 6–7). After the combined-product update in Eq. 11, neither $\mathcal{W}_{i(t)}$ nor $L_{i(t)}$ is explicitly maintained. If the full product is reconstructed (i.e., $\mathcal{W}_{i(t)} = L_i R_i$ computed explicitly), this defeats the memory savings from storing only $(L_i, R_i)$. The paper does not state clearly what is stored or how the individual factors are recovered between iterations. This is the central algorithmic description of WSI, and its ambiguity prevents a careful reader from fully verifying the memory-savings claim.

**2. Headline claim ("up to 62×") applies only to MLP-block linear layers but is unqualified in the abstract.** Sec. 4.1 explicitly states comparisons "focus on linear layers within multi-perceptron blocks for fair comparison with previous methods." The 62× and 2× figures from the abstract are therefore localized to a single component of the model, while the actual wall-clock speedup is 1.4×—a gap of roughly 40× that is never explained. The mismatch between the peak component-level compression ratio and the end-to-end speedup is not disclosed in the abstract or introduction, which constitutes an overclaim in its current presentation. What drives the remaining overhead (subspace iteration cost, memory allocation, Python-level operations)? Answering this would substantially strengthen trust in the reported efficiency numbers.

**3. Thin baseline set.** The paper compares against three baselines: vanilla training, ASI (from the same group), and SVD-LLM. SVD-LLM is demonstrably ill-suited to vision transformers (Sec. 4.3 explicitly notes it consumes *more* memory than vanilla at low compression), so including it primarily confirms WASI is better than an ill-suited method. Gradient-checkpointing—the simplest training-memory baseline—is not evaluated. GaLore-style approaches that reduce optimizer-state and gradient memory during transformer fine-tuning are not discussed. Providing at least one additional training-memory baseline that is genuinely applicable to transformers would allow readers to assess whether WASI's improvements are distinctive or whether simpler methods achieve comparable gains.

### Minor

**4. Stability evidence is thin for the central motivating assumption.** Fig. 3a shows singular-value stability for a single layer ($W_6$) on a single model (ViT), a single dataset (Pets), and a single ε value (0.8). This is the core empirical justification for the stable-subspace hypothesis underlying the entire method. Showing stability across all MLP layers (which Fig. 3a doesn't) and across at least one additional dataset would markedly strengthen this foundation, especially since the method is later applied to SwinT and TinyLlama where no analogous stability check is presented.

**5. TinyLlama experiment is too limited to establish LLM generality.** Only the last 5 layers are fine-tuned, ε is set to the most aggressive level (0.1), and BoolQ accuracy ranges from 64–66%—close to the majority-class baseline (~62%). The paper frames this as showing "broad applicability" (Sec. 4.3), but this particular setup makes it difficult to distinguish WASI's effect from the trivial observation that extreme compression of only 5 layers in a 1.1B-parameter model has a negligible effect on task performance. The experiment could be strengthened by fine-tuning more layers or using a less aggressive ε.

### Trivial

**6. Fig. 6 (SwinT multi-dataset) shows only WASI vs. vanilla in the main text.** The paper notes "additional baselines are in Appendix B.3," meaning the headline multi-dataset result cannot be compared against ASI and SVD-LLM in the main body. Moving at least one competitor into Fig. 6 would make the central empirical contribution self-contained.

---

## Nice-to-Haves

- A profiling breakdown of where the remaining runtime overhead (the gap between 62× theoretical and 1.4× wall-clock) originates would be highly informative for practitioners and would strengthen the paper's claims substantially.
- Singular-value stability plots for all layers (analogous to Fig. 3a's single-layer heatmap) across both ViT and SwinT.
- A direct comparison with gradient checkpointing as a simple floor-level baseline.

---

## Removed Points

*These points are flagged as removed; treat them with caution.*

- **"Incremental extension from the same group" as a fatal concern**: The harsh critic argues the contribution should be severely discounted because WSI extends ASI from the same group. While the relationship is acknowledged in the paper (Sec. 2 discusses ASI and Sec. 3.3 explicitly extends it), this is standard iterative academic work. The critic's framing that the "significance section should be calibrated" is reasonable as a presentation note, but does not rise to a fatal flaw. KEEP as context, demoted to background.

- **"WSI vs. SVD accuracy gap unexplained"**: The critic notes that warm-starting achieving 35% higher accuracy at the same FLOPs is surprising and unexplained. This is a legitimate curiosity, but the paper's purpose is to show WSI is not worse than repeated SVD—and it is demonstrably better. The paper does not need to fully explain *why* warm-starting is better, only that it is. REMOVE as a required fix; retain as a nice-to-have investigation.

- **"BoolQ accuracy near random guessing"**: The critic asserts 64–66% is essentially random (random=50%, majority baseline≈62%). However, the paper's TinyLlama experiment is making a resource-efficiency claim—WASI achieves 953× activation memory reduction at comparable accuracy—not an accuracy-maximization claim. The criticism misframes the experiment's purpose. However, the concern about whether this constitutes a meaningful demonstration of generality is retained as a Minor weakness.

- **"Not yet released / availability" concerns**: None raised. No criticisms of this type appear.

- **"Missing related works"**: Not raised. REMOVE per hard rule.

- **"Missing appendix content"**: The harsh critic references appendix-deferred proofs and DP details. Per hard rules, these are stripped from the reviewed text and cannot be used as weaknesses.

---

## Novel Insights

The most non-obvious empirical finding in the paper is that warm-started subspace iteration (WSI) achieves strictly *higher* accuracy than recomputing truncated SVD at each iteration when both are constrained to the same FLOPs budget (Fig. 3b, 35% accuracy gap). This suggests the warm-started subspace acts as implicit regularization during fine-tuning—an interesting side-effect that the paper does not analyze but that could motivate follow-on theoretical work on the geometry of fine-tuning dynamics. The broader joint-compression insight (that weight and activation subspaces can be simultaneously controlled under a single ε threshold without one harming the other) is validated empirically and represents a practically useful extension of prior work on compressed-domain training.

---

## Suggestions

1. **Clarify Algorithm 1 / Eq. 11 interaction**: State explicitly whether $L_i$ and $R_i$ are stored individually across iterations, and how the gradient in Eq. 11 (which is in the original space) is converted back to individual updates on $L_i$ and $R_i$. A single paragraph after Eq. 11 would resolve the ambiguity.

2. **Qualify the abstract claim**: Replace "reducing memory usage by up to 62×" with something like "reducing MLP-layer memory by up to 62×, translating to approximately 1.4× end-to-end wall-clock speedup on a Raspberry Pi 5." This is still a strong result and is unambiguously correct.

3. **Add one training-memory baseline**: Gradient checkpointing requires no methodological explanation and would serve as a clear floor. Showing WASI's advantage over it quantitatively would strengthen the empirical contribution.

4. **Expand stability evidence**: Show the singular-value stability heatmap for all layers (not just $W_6$) in the main text; this costs little space and would fully validate the method's central premise.

---

## Score and Decision

**Calibration anchors retrieved:**

| Path | Avg Human Score | Round | Comparison to WASI |
|---|---|---|---|
| `04RLVxDvig.md` (NanoMoE) | 3.00 | R1 weak | Much weaker—no hardware results, less principled |
| `eqKHuxIpp5.md` (On-device Transfer Learning) | 2.50 | R1 weak | Much weaker—limited method, poor evaluation |
| `ZTvUT49JjL.md` (Matrix Factorization) | 3.40 | R1 weak | Different topic, weaker empirically |
| `pAVJKp3Dvn.md` (Differentiable Structured Matrices) | 5.67 | R1 mid | Roughly comparable in scope, WASI more practical |
| `i0zzO7Hslk.md` (LORO) | 6.00 | R1 mid | More theoretically grounded; WASI has better hardware experiments but more incremental |
| `LvNROciCne.md` (AdaRankGrad) | 7.00 | R1 mid | Stronger theoretically and at larger scale |
| `DLJznSp6X3.md` (ReLoRA) | 5.75 | R1 mid | Similar scope, WASI more specific hardware angle |
| `TwJrTz9cRS.md` (HiRA) | 8.00 | R1 strong | Much stronger, broader impact |
| `xNdE7RiRyP.md` (TinyTrain) | 5.25 | R2 | Most topically similar; WASI more principled, better baselines, comparable hardware |
| `FK6T0U4Mg1.md` (SubZero) | 4.25 | R2 | Weaker on hardware evidence; WASI more focused |

**Round 1 bracket**: 4.5–6.5  
**Round 2 narrowing**: TinyTrain (5.25, rejected) is the most topically similar anchor. WASI is methodologically more principled than TinyTrain, has hardware results of similar strength, but is more clearly incremental relative to the same group's prior ASI. LORO (6.0, accepted) is more theoretically grounded and applied at larger scale. WASI sits just below LORO: the hardware experiments are comparably convincing but the contribution is more incremental and the baseline comparison thinner.

**Final score**: **5.0** (borderline reject). WASI makes a genuine practical contribution with real hardware evidence, but the incremental framing relative to same-group prior work (ASI), the unexplained gap between component-level and end-to-end efficiency, the thin baseline comparison, and the algorithmic ambiguity in the weight update collectively place it below the clear-accept threshold for ICLR. The paper would substantially benefit from the suggested fixes.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>