Now I have a thorough understanding of the paper and all the claims. Let me compose the final review.

## Summary

This paper proposes **LoLoRA**, a method that replaces backpropagation-based training of LoRA's **A** matrix with local unsupervised updates (Hebbian PCA or autoencoder loss) computed from the forward-pass input. This avoids storing input activations for **A**, reducing memory. The paper also provides a theoretical analysis (Theorem 4.4) proving that, under a random regression model, the optimal **A** spans the top eigenspace of the input covariance matrix—providing formal justification for PCA-based initialization (EVA). Experiments on GLUE, MetaMathQA→GSM8K, and LLaVA fine-tuning compare LoLoRA against standard LoRA and LoRA-FA (frozen **A**) variants.

## Strengths

- **Clean theoretical characterization of optimal A (Theorem 4.4, 4.5).** Under the stated random‑regression assumptions, the paper proves that optimal **A** matrices are nonsingular linear transformations of the top‑\(r\) eigenvectors of the input covariance, and that **B** is insensitive to initialization beyond full rank. This result formalizes and extends prior empirical observations about PCA‑based initialization (EVA) and adapter asymmetry, and is the paper's strongest contribution.

- **Comprehensive ablation of local rules and initializations (Section 5.4, Tables 5‑6).** The comparison of six local update rules (HPCA variants, AE, SoftHebb) and four initializations (Uniform, Orthogonal, PiSSA, EVA) on TinyLlama‑1.1B provides useful guidance for practitioners. HPCA and AE consistently outperform naive frozen‑A baselines.

- **Broad evaluation across three domains.** Experiments cover NLU (RoBERTa‑large on GLUE), mathematical reasoning (LLaMA‑3.1‑8B on MetaMathQA), and multimodal understanding (LLaVA‑v1.5‑7B), demonstrating the method's generality.

- **Memory measurements reported alongside accuracy (Tables 3‑4).** The explicit breakdown of peak extra GPU memory allows direct assessment of the memory‑accuracy trade‑off and shows that LoLoRA reduces memory relative to standard LoRA (e.g., 26 GB vs 30 GB on LLaMA‑3.1‑8B).

## Weaknesses

### Fatal
None.

### Major

1. **Central claim is not supported by the evidence.** The paper argues that LoLoRA's local updates "mitigate" the performance trade‑off of freezing **A**. In practice, LoLoRA performs **essentially identically** to LoRA‑FA with EVA initialization—the strongest frozen‑A baseline—across all three experimental setups:
   - **GLUE (Tables 1‑2):** LoLoRA HPCA scores *lower* than LoRA‑FA (uniform) on 5 of 8 tasks (CoLA, RTE, MNLI, QQP, SST‑2), ties on one (STS‑B), and shows marginal wins on two (MRPC +0.1, QNLI +0.1). All differences are within confidence intervals.
   - **MathQA (Table 3):** LoLoRA HPCA and LoRA‑FA (EVA) both achieve **0.829**—identical.
   - **LLaVA (Table 4):** LoLoRA HPCA (2.93 perplexity) is slightly *worse* than LoRA‑FA (EVA) (2.92).
   
   The conclusion's framing—"HPCA consistently outperforms standard LoRA‑FA in two out of three experimental setups"—treats each broad setup as a binary win/loss, which aggregates away the within‑GLUE sub‑task breakdown where LoLoRA mostly underperforms. More importantly, the comparison with LoRA‑FA (EVA)—the most relevant frozen‑A baseline—shows no advantage for LoLoRA.

2. **"Adaptation to input distribution shifts" claim is untested.** The abstract asserts that LoLoRA "allow[s] it to adapt to input distribution shifts." No experiment in the paper actually tests this. A proper evaluation would require a setting with known distribution shift (e.g., sequential multi‑task fine‑tuning, curriculum learning, or time‑varying data) and measurement of whether LoLoRA tracks the optimal subspace more effectively than a fixed initialization. Without such evidence, this claimed benefit remains an unsupported assertion. (The paper acknowledges stationary targets as a limitation in the conclusion, but this acknowledgment sits at odds with the abstract's framing.)

3. **Theoretical contribution primarily justifies EVA, not specifically LoLoRA's online updates.** Theorem 4.4 characterizes the optimal **A** under a frozen‑A setting and validates PCA‑based initialization—which is exactly what the existing EVA method does. The HPCA updates converge to the same subspace; the experiments show they perform equivalently to initializing there and freezing. The theory thus provides formal support for a *baseline* (EVA) rather than uniquely justifying LoLoRA's online mechanism. The paper's narrative blurs this distinction, presenting the theory as support for LoLoRA when it equally (if not more strongly) supports the simpler EVA baseline.

### Minor

1. **Memory advantage is not unique to LoLoRA, and the abstract's phrasing is ambiguous.** The memory savings (avoiding storing input activations for **A**) are achieved by *any* method that does not backpropagate through **A**—including LoRA‑FA. LoLoRA actually uses *slightly more* memory than LoRA‑FA (Table 4: 24.1 GB vs 23.9 GB) due to optimizer state for the local updates. The abstract's "further reducing the memory required for fine-tuning" could mislead readers into thinking LoLoRA improves upon LoRA‑FA's memory footprint, when the reduction is relative to standard LoRA and is shared with LoRA‑FA.

2. **The stationary‑targets limitation is acknowledged but underemphasized.** The theory (Assumption 4.1 and the derivation of Theorem 4.4) assumes i.i.d. Gaussian \(\Delta W_0\), which abstracts away the structured, evolving nature of fine‑gradient targets in real models. The paper notes this in the conclusion but the claim about "adaptation to distribution shifts" in the abstract implicitly assumes the opposite. The gap between the idealized regression setting and practice is larger than the paper's framing suggests.

3. **Ablation ordering and comparison with Full LoRA.** Table 6 shows that Full LoRA (standard backprop through both **A** and **B**) consistently outperforms *all* LoLoRA variants across ranks—expected but worth emphasizing. The ordering among LoLoRA variants shows no clear winner (HPCA, HPCA‑svd‑first, and AE trade places across ranks), consistent with the view that all converge to the same subspace and do not meaningfully differ.

### Trivial

None.

## Nice-to-Haves

- **Subspace alignment measurement:** The paper could directly measure how well **A**'s row space aligns with the top eigenvectors of the input covariance matrix over training, for both LoLoRA and LoRA‑FA (EVA). This would verify that HPCA converges as claimed and test whether the frozen **A** in LoRA‑FA (EVA) stays in the initialization subspace or drifts.
- **Non‑stationary experiment:** An explicit test of the adaptation claim—e.g., sequential fine‑tuning on related tasks with different input distributions—would strengthen the motivation for online updates over fixed initialization.
- **Local update hyperparameter details:** The optimizer for **A** (Opt_loc in Algorithm 1) is not specified; an ablation on the local learning rate and momentum would be informative.
- **Broader comparison:** Including full fine‑tuning or other memory‑efficient methods (e.g., QLoRA) would better contextualize the contribution.

## Removed Points

These points from the inputs were removed after cross‑checking against the paper:

- **Forward/backward mismatch in Algorithm 1 (Harsh Critic Section‑by‑Section Notes):** The critic claimed that the backward pass gradient \(\partial L/\partial z = (W + BA)^T \partial L/\partial h\) would use the post‑update **A**, creating a mismatch. In standard autograd frameworks, the computation graph captures the pre‑update **A** used to compute \(u = Az\), so no mismatch occurs in practice. The critic acknowledges it is "likely negligible." Removed as a speculative implementation concern that does not affect the paper's validity.
- **Missing appendix content (memory conditions, hyperparameters):** The parser strips appendices from all papers; criticisms about absent appendix details are removed per the hard rules. The paper defers to Appendix C for hyperparameters and Appendix D for memory analysis, which exist in the original submission.
- **Generic "could be stronger" framing suggestions (Strengthening the Paper on Its Own Terms):** These are constructive suggestions, not weaknesses, and have been moved to Nice‑to‑Haves where appropriate.

## Novel Insights

None beyond the paper's own contributions. The key insight from the synthesis of reviews is that the paper's strongest asset (Theorem 4.4) provides formal theoretical backing for PCA‑based initialization (EVA), but the paper presents this as support for its online‑update method LoLoRA. Reframing the paper around this theoretical contribution—with LoLoRA positioned as an algorithmic alternative that avoids a separate PCA pass rather than as an improvement—would align the claims with the evidence.

## Suggestions

1. **Reframe the central claim.** The paper would be more credible if it presented LoLoRA as an *alternative* to LoRA‑FA (EVA) that avoids a separate PCA pre‑pass (as the ablation section already hints: "online methods have the advantage of not requiring a separate incremental PCA pass"), rather than as a method that "mitigates" a trade‑off the evidence shows does not exist between LoLoRA and a well‑initialized frozen baseline.
2. **Either test the adaptation claim or remove it from the abstract.** If the adaptation‑to‑distribution‑shifts claim is a core motivation, design an experiment that actually involves distribution shift (e.g., sequential fine‑tuning). Otherwise, remove or temper the claim.
3. **Add explicit comparisons to LoRA‑FA (EVA) in all result summaries.** The GLUE summary text already states that LoLoRA "achieves slightly better results than LoRA‑FA (EVA)"—but Tables 1‑2 show many tasks where LoLoRA is *worse*. A more balanced presentation would acknowledge that LoLoRA and LoRA‑FA (EVA) are essentially tied across all settings.
4. **Clarify the memory comparison point.** The abstract should make clear that the memory reduction is relative to standard LoRA and is shared with LoRA‑FA, and that LoLoRA's footprint is marginally larger than LoRA‑FA due to optimizer state.

## Score and Decision

The paper makes a genuine theoretical contribution (Theorem 4.4, 4.5) and proposes a well‑motivated method. The ablation study is thorough and informative. However, the central empirical claims are not supported: LoLoRA performs indistinguishably from the simpler LoRA‑FA (EVA) baseline, and the claimed "adaptation to distribution shifts" is untested. The narrative oversells the method's advantages relative to the evidence. A fundamental reframing is needed to bring claims in line with results.

**Score: 5.0**

**Decision: Reject**

<score>5.0</score>
<decision>Reject</decision>