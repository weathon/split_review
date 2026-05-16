Now I have thoroughly read the paper and verified each claim. Let me synthesize my findings into the final consolidated review.

## Summary

This paper proposes a drop-in replacement for linear layers in neural networks that reduces activation memory during backpropagation. The key idea is to store only a randomly projected version of the input activations ($X_{\mathrm{proj}} = S^\top X$) during the forward pass, rather than the full input $X$, and use this compressed representation to compute approximate gradients during the backward pass. The paper provides theoretical analysis bounding the additional gradient variance from the randomized matrix multiplication relative to the inherent SGD variance (Theorem 1), and empirically evaluates the method on RoBERTa fine-tuning across GLUE tasks.

## Strengths

- **Memory-reduction objective clearly distinguished from prior speed-focused work:** The paper explicitly identifies that Adelman et al. (2021) targeted speedup but required the same memory, and proposes a different algorithmic design (storing $X_{\mathrm{proj}}$ and a random seed instead of $X$) that targets memory reduction. This is a clear conceptual contribution supported by Algorithm 1 and Figure 1.

- **Theoretical variance bounds connecting RMM noise to inherent SGD noise:** The paper derives computable variance estimates for both SGD (Lemma 1) and RMM (Lemma 2) and bounds their ratio (Theorem 1), providing a principled framework for understanding when the additional gradient noise from compression is acceptable relative to the noise already present from minibatch sampling. This goes beyond prior work that only gave generic matrix-multiplication error bounds.

- **Empirical evidence of 5–10× memory compression with moderate accuracy loss on GLUE:** The experiments on RoBERTa base show that for most GLUE tasks (MNLI, QQP, etc.), even a compression rate $\rho=0.1$ (10× reduction in stored activations) leads to accuracy drops of only 0.1–0.5 points, while the memory usage table confirms this translates to 10–20% peak memory reduction at the model level.

- **Empirical confirmation of variance behavior during training:** Figure 4 shows that the variance ratio from Theorem 1 converges to a constant during fine-tuning, and both $D^2_{\mathrm{SGD}}$ and $D^2_{\mathrm{RMM}}$ evolve similarly, experimentally supporting the claim that the additional noise remains comparable to the inherent SGD noise.

- **Comprehensive evaluation across random matrix types and throughput:** Table 4 (referred to as Table 3 in the paper on comparison of randomized MatMuls) compares Gaussian, Rademacher, DCT, and DFT constructions, showing consistent accuracy at the same compression rates, and Figure 5 demonstrates that for small $\rho \leq 0.1$ the randomized layer is actually faster than the baseline.

## Weaknesses

### Fatal
None.

### Major

- **No statistical rigor in the main accuracy results (no multiple seeds, no confidence intervals):** The GLUE fine-tuning results (Table 1) report a single number per compression rate per task with no indication of multiple random seeds, standard deviations, or confidence intervals. Fine-tuning pretrained models on GLUE can vary noticeably with seed, learning rate, and initialization — especially on smaller tasks like CoLA, MRPC, and RTE (which are included in the evaluation). The paper claims that "compression in 5–10 times results in insignificant drop of performance" (line 347), but without any measure of variance, it is impossible to determine whether the reported differences are statistically significant or within the noise of a single run. This weakens the central empirical claim of the paper. At minimum, 3–5 seeds should be run for the baseline and key compression rates, with means and variances reported.

- **Missing comparison against standard memory-reduction techniques (activation checkpointing / gradient recomputation):** A well-established baseline exists for reducing activation memory: activation checkpointing (Chen et al., 2016), which recomputes activations during backward instead of storing them. For a linear layer, this would store no input activations at the cost of one extra forward pass. The paper never mentions or compares against any such baseline. Without this comparison, it is difficult to assess whether the RMM layer's memory–accuracy tradeoff is practically superior to a simpler off-the-shelf technique that can be applied to any layer. While the paper's contribution is not invalidated, a reader cannot judge where this method fits in the landscape of existing memory-saving approaches.

- **Only evaluated on fine-tuning (not training from scratch, and only one architecture):** All experiments are on RoBERTa-base fine-tuning on GLUE. The paper does not test the method on training from scratch, on other architectures (e.g., vision models where linear layers may be a larger memory bottleneck), or at larger scales. This limits the generality of the claims about the method's benefits.

### Minor

- **Modest total memory savings unaccompanied by a memory breakdown:** The paper reports that compressing linear-layer activations by 5–10× yields only a 10–20% reduction in total peak memory. While the paper acknowledges that "there are other solid memory consumers" (lines 351–352), it does not provide a memory breakdown showing what fraction of total allocated memory comes from linear-layer input activations in the baseline model, nor does it quantify the fraction of memory saved specifically in the linear layers. This would help readers understand when the method is most useful (e.g., very wide layers, large batch sizes, or models where linear layers dominate).

- **Theoretical connection to practice is underdeveloped:** Theorem 1 bounds the variance ratio in terms of $\alpha = \|X^\top Y\|_F^2 / (\|X\|_F^2 \|Y\|_F^2)$, but the paper does not measure $\alpha$ across layers and tasks during training to verify when the bound is tight, nor does it use the theory to predict which layers or tasks can tolerate more compression. Figure 4 shows the variance ratio for only one layer on CoLA at $\rho=0.5$. Connecting the theory more concretely to the observed accuracy retention would strengthen the paper significantly.

- **Substantial compute overhead not prominently discussed:** The complexity analysis (Section 2.4) and Figure 5 show that the method is only faster than baseline for $\rho \leq 0.1$, and has worse asymptotic complexity in batch size. This is an important practical tradeoff that should be discussed more prominently — for many memory-reducing regimes ($\rho = 0.5$), the method slows training while saving only modest total memory.

### Trivial
- The paper does not specify how memory was measured (e.g., `torch.cuda.max_memory_allocated()`), though this is a minor transparency issue.
- Some of the training hyperparameters (learning rate, number of epochs, optimizer settings) are deferred to the Fairseq reference rather than stated explicitly.

## Nice-to-Haves

- A memory breakdown quantifying the fraction of peak memory attributable to linear-layer activations in the baseline model, to clarify the practical scope of the technique.
- Comparison against activation checkpointing (gradient recomputation) for the same memory budget, to directly assess whether RMM provides a better accuracy–memory tradeoff than recomputation.
- Measuring $\alpha$ (from Theorem 1) across different layers and tasks to empirically validate when the theoretical bound is informative about practical compression tolerability.
- Evaluation on training from scratch and/or on architectures where linear layers dominate memory (e.g., wide MLP-based vision models).

## Removed Points

These points from the reviewer inputs are flagged to be removed or downgraded. Treat them with caution:

- **"SORS underperformed — paper should explain why"** → The paper already states SORS "accuracy drop is higher, so we leave this for future studies" (line 138). This is an adequate explanation for a minor experimental choice.
- **"Missing hyperparameter details (learning rate, epochs, etc.)"** → The paper states "We use the same training setting and model hyperparameters for RoBERTa model which are in Fairseq" (line 323), which is a standard and acceptable practice in ML papers. Moved from weaknesses.
- **"Connection to practice is weak" specifics about wanting measurement of α across all layers/tasks** → Downgraded from Major to Minor, as the paper does provide one measurement (Figure 4) and references additional experiments in the appendix (which exists in the original submission but was stripped by the parser).
- **"Vague language about variance ratio"** → The paper's description (lines 390–391) is reasonably precise for an empirical observation; the more substantive point is the limited scope (one layer, one task, one ρ), which is already captured in Minor weaknesses.
- **"Memory measurement method not disclosed"** → Downgraded from Minor to Trivial, as this is a minor transparency issue that does not affect the paper's conclusions.
- **Strength Finder claim about "5–10× memory compression"** → The paper's own text says "compression in 5–10 times cuts overall runtime memory by 10–20%" (line 355). The 5–10× refers to the layer-level compression rate, not total model memory compression. The strength as stated could be misleading but the underlying evidence is real; kept in Strengths with the clarifying dissociation between layer-level and model-level savings.
- **"The paper would be much stronger if it reported the memory breakdown"** → Moved to Nice-to-Haves, as this is a strengthening suggestion rather than a core flaw.

## Novel Insights

The key insight that emerges from combining the reviews is that the paper has a conceptually clean contribution (store a compressed projection, not the full activation) paired with elegant variance theory (relating the RMM noise to the already-present SGD noise), but its empirical evaluation falls short of the standard needed to convincingly demonstrate that this is a practically useful technique. The most novel observation across the reviews is that the method's usefulness depends critically on the ratio of linear-layer activation memory to total model memory — a quantity the paper acknowledges but never measures — and that the theoretical bound (Theorem 1) is most valuable not as a standalone result but as a tool practitioners could use to determine per-layer compression tolerances, a direction the paper only begins to explore. The paper would benefit from reframing its contribution around this practical diagnostic use of the theory.

## Suggestions

1. **Run all experiments with at least 3-5 random seeds** and report means and standard deviations, especially for the baseline and key compression rates ($\rho = 0.5, 0.2, 0.1$). Without this, the central claim that accuracy loss is "insignificant" is not supported.

2. **Include a memory breakdown** showing what fraction of total peak memory comes from linear-layer input activations in the baseline model, so readers can assess when this technique is worth applying.

3. **Add activation checkpointing as a comparison baseline** for at least one representative task (e.g., CoLA or MNLI), matching a target memory budget and comparing the resulting accuracy. This would directly address the question of whether RMM provides a better alternative to simply recomputing activations.

4. **Measure $\alpha$ (the alignment parameter from Theorem 1) across layers and tasks** to empirically validate when the theoretical bound predicts acceptable compression — turning the theory into a practical diagnostic tool.

5. **Reframe the narrative** to more prominently acknowledge the modest total memory savings and the compute overhead tradeoff, making clear that the method is most beneficial for models where linear-layer activations dominate memory (e.g., very wide layers) and for aggressive compression ($\rho \leq 0.1$) where both memory and speed benefits materialize.

## Score and Decision

This paper presents a clear and well-motivated idea with solid theoretical foundations. The algorithmic contribution (storing a compressed random projection instead of the full activation) is clean and the variance analysis connecting RMM noise to SGD noise is novel and principled. However, the empirical evaluation has two significant gaps: the absence of statistical rigor (no multiple seeds, no confidence intervals) and the lack of comparison against standard memory-reduction baselines (activation checkpointing). These gaps prevent the paper from convincingly demonstrating that the method is practically useful relative to existing approaches. The modest total memory savings (10–20%) and the compute overhead (the method is often slower) further limit the claimed impact. The paper would need substantial additional experiments to be competitive at a top-tier venue.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>