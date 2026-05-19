- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 6, 3, 3
Now I have a thorough understanding of the paper and can verify the reviewer claims against the actual text. Let me produce the consolidated review.

## Summary
This paper proposes a drop-in replacement for linear layers in neural networks that reduces memory during backpropagation by storing a randomly projected version of the input activations ($X_{\text{proj}} = S^\top X$) instead of the full input. The random matrix $S$ is rematerialized from a seed in the backward pass. The authors provide a theoretical variance analysis connecting the randomized matrix multiplication (RMM) noise to the inherent SGD noise (Theorem 1), and evaluate the method by fine-tuning RoBERTa-base on GLUE tasks, reporting moderate accuracy retention at 5–10× compression of stored activations and 10–20% peak memory reduction.

## Strengths

- **Provable variance control connecting RMM noise to SGD noise.** Theorem 1 (Eq. 5) bounds the variance of the randomized gradient relative to the SGD variance via a ratio that depends on $\alpha = \|X^\top Y\|_F^2 / (\|X\|_F^2\|Y\|_F^2)$. Lemmas 1 and 2 give explicit closed-form variance expressions for both SGD and RMM. Figure 6 (variance ratio) shows this ratio remains bounded during actual training on CoLA, providing theoretical grounding for why moderate compression need not degrade convergence.

- **Consistent task performance across 8 GLUE tasks at 5–10× compression.** Table 2 (referenced in text, line 345–347) shows that compressing stored activations by a factor of 5–10 ($\rho=0.2$ to $\rho=0.1$) yields only moderate performance drops across diverse GLUE tasks, with some tasks showing minimal degradation. This demonstrates the method's viability on a standard benchmark.

- **Verified memory reduction with profiled measurements.** Table 3 and Figure 4 confirm near-linear scaling of peak memory with batch size under compression, and the paper honestly reports that 5–10× activation compression translates to 10–20% overall peak memory reduction (line 355), giving a concrete practical yardstick.

- **Robustness across different random projection distributions.** Table 4 compares Gaussian, Rademacher, DFT, and DCT projections on CoLA; all show similar degradation trends as $\rho$ decreases, demonstrating the method is not sensitive to the specific choice of random matrix distribution.

- **Counter-intuitive speedup at high compression.** Figure 4 shows relative throughput exceeding 1.0 for $\rho \leq 0.1$, meaning the randomized layer processes samples *faster* than the baseline despite additional matrix multiplications — a practical advantage not obvious from asymptotic complexity alone.

## Weaknesses

### Fatal
None.

### Major

- **Unsubstantiated claim in the introduction that the linear-layer memory challenge "has not been discussed, yet" (line 22).** The very next paragraph cites Adelman et al. (2021), which directly discusses randomized backpropagation through linear layers. While the authors differentiate their work (memory vs. speed), the claim of having "not been discussed" is clearly false on its face. This overstates the gap and should be corrected to accurately reflect prior work (e.g., "has not been addressed from a *memory-reduction* perspective").

### Minor

- **Evaluation limited to fine-tuning; generality for training-from-scratch not tested.** The paper consistently scopes its experiments to fine-tuning a pretrained RoBERTa model (abstract, line 32, line 322, line 502), and contribution #4 explicitly lists fine-tuning. However, the title and much of the framing describe a general-purpose method for "backpropagation through large linear layers" without qualifiers. Since fine-tuning starts from a good initialization with small gradients, the method's behavior under full training (where gradients are large and noisy) remains untested. The paper would benefit from acknowledging this scope limitation directly rather than leaving it implicit.

- **No error bars or confidence intervals on GLUE scores.** The method injects randomness from the projection matrices, so variance across seeds is expected. Table 2 reports single numbers per task without standard deviations or multiple runs. Since the reported accuracy drops are modest (e.g., MNLI 87.7 → 86.4 at $\rho=0.1$), confidence intervals are needed to assess whether these differences are statistically significant or within run-to-run noise.

- **Theoretical bound (Theorem 1) is not uniformly informative.** As the paper itself acknowledges (lines 249–264), parameter $\alpha$ can be arbitrarily close to zero, making the ratio bound vacuous. The paper provides a pathological example and argues this does not occur in practice, which is reasonable but means the bound serves as intuition rather than a robust design principle. A practical rule for selecting $B_{\text{proj}}$ from the variance estimates is not provided.

- **Variance ratio figure shown for only one layer on one task.** Figure 6 plots the variance ratio only for one FC layer during CoLA fine-tuning at $\rho=0.5$. The paper claims "for other layers the picture is very similar" (line 391) without showing the evidence in the main text (deferred to appendix). Given that the variance analysis is a core contribution, more extensive main-text evidence would strengthen the claims.

- **Peak memory savings are modest (10–20%) despite high compression ratios.** The paper reports this honestly (line 355), but the framing in the title and abstract emphasizes "Memory-Efficient Backpropagation" without conveying the limited practical impact in realistic transformer fine-tuning where linear-layer activations are not the sole memory bottleneck. A more nuanced discussion of *when* the method is impactful (e.g., models where linear layers dominate, or extremely long sequences) would improve the paper.

- **Training hyperparameters not fully specified in the main text.** The paper states it uses "the same training setting and model hyperparameters for RoBERTa model which are in Fairseq" (line 323). Key parameters (batch size, learning rate, optimizer, epochs) should be stated explicitly in the main text for reproducibility, especially since the method introduces a new hyperparameter (compression rate) whose interaction with learning rate is not discussed.

### Trivial
None.

## Nice-to-Haves
- Testing the method on training from scratch (e.g., a smaller Transformer or MLP where linear layers dominate memory) would substantially increase the contribution's significance.
- A memory profile breakdown showing which specific tensors are reduced would make the modest overall savings more interpretable.
- A brief comparison to gradient checkpointing (the standard memory-accuracy trade-off technique in backpropagation) would help readers situate the contribution.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Missing related work on gradient checkpointing.** *Removed per instruction: "DO NOT mention missing related works, as you do not have external sources to confirm their existence."* The paper was judged on what it cites, not on what it omits.
- **"Computational cost of regenerating dense Gaussian matrix is not negligible — complexity analysis provided but not empirically validated."** *Removed: this is partially addressed by Figure 4's throughput measurements showing the method can be faster at high compression.*
- **"No limitations section."** *Removed: the paper discusses limitations (e.g., the bound can be vacuous, future directions). The request for a dedicated limitations section is a formatting preference, not a substantive weakness.*
- **"Could the metric be measuring a proxy?"** and similar speculative framing from the harsh critic's methodology sweep. *Removed: not anchored to a specific sentence, equation, or figure in the paper.*

## Novel Insights
None beyond the paper's own contributions. The reviews did not surface observations about the method, its limitations, or its implications that are not already present or implicitly scoped by the paper itself.

## Suggestions
1. **Correct the overstated claim in the introduction** (line 22) — the linear-layer memory challenge has been discussed (Adelman et al., 2021, cited immediately afterward). Replace "has not been discussed, yet" with a more precise statement about the specific gap being addressed (memory reduction rather than speed).
2. **Add confidence intervals or multiple-seed results** to at least the key GLUE tasks where RMM is used, so readers can assess whether accuracy drops are statistically significant.
3. **Add a brief scope-discussion paragraph** explicitly noting that experiments are limited to fine-tuning and that full-training scenarios may behave differently.
4. **State key hyperparameters** (batch size, learning rate, optimizer, number of epochs) explicitly in the main text rather than deferring to "same as Fairseq."
