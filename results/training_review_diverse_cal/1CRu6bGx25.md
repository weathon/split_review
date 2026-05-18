Now I have a thorough understanding of the paper and all the review claims. Let me produce the final consolidated review.

## Summary

This paper proposes FI (First-order local Influence), a stability measure for LLMs and VLMs grounded in information geometry, which quantifies how sensitive a model's output is to local perturbations in its inputs or parameters. The measure has a theoretical invariance property under reparameterization, which addresses scaling sensitivity issues of simpler gradient-based measures. The paper validates FI empirically through: (1) a case study on Qwen-VL showing that masking high-FI image pixels induces hallucination, (2) sparsification experiments where removing 2–3% of high-FI parameters in Qwen2-7B causes up to 75% accuracy degradation on MMLU (vs. negligible effects from random removal), (3) FI-guided channel protection improving quantization outcomes, and (4) FI-guided exclusion reducing forgetting in model merging.

## Strengths

- **Sparsification experiments provide strong causal evidence that FI identifies functionally critical parameters.** Sparsifying just 2–3% of top-FI parameters in Qwen2-7B reduces MMLU accuracy by up to 75%, while random sparsification at the same rate causes negligible degradation (Figure 3, Section 3.2). This sharp contrast is the single most compelling piece of evidence in the paper — it directly validates that FI captures parameters whose removal genuinely damages model behavior.

- **FI-guided protection yields practically meaningful improvements in quantization and merging.** Protecting high-FI channels under 1-bit quantization achieves a 50% accuracy improvement on MMLU-Business over protecting low-FI channels, with only 0.1 GB memory overhead at 5% protection (Section 3.3, Figure 5). For model merging, excluding top-10% FI parameters from arithmetic merging yields 15–20% improvement over random exclusion across multiple math benchmarks (Table 2). These demonstrate concrete utility of FI in real LLM optimization tasks.

- **The invariance property is theoretically well-motivated and clearly articulated.** Theorem 2.3 proves FI is invariant under diffeomorphic reparameterization (e.g., scaling), and the paper shows why this matters: ReLU networks have scaling symmetries that cause Jacobian norms and Cook's influence to vary arbitrarily, while FI remains stable (Section 2, lines 67–83). This is a genuine theoretical advantage over simpler measures.

- **The paper tests on multiple model families and sizes.** Experiments span Qwen2 (1.5B–7B), LLaMA2, LLaMA3, and DeepSeek models, demonstrating the measure's general applicability.

## Weaknesses

### Fatal
None.

### Major

- **Critical baselines are missing across all experiments, making it impossible to determine whether FI's invariance property yields practical advantages over simpler alternatives.** For sparsification (Section 3.2), the only baseline is random — no comparison against weight magnitude, gradient norm, diagonal Fisher information approximation, or Hessian-trace based importance. For quantization (Section 3.3), FI-guided protection is compared only against low-FI protection, not against GPTQ (Frantar et al., 2022), AWQ, or magnitude-based protection. For merging, no comparison against TIES-Merging, DARE, or task-vector-based methods. Since the paper's central claim is that FI is a *superior* measure (due to invariance), the lack of comparisons against existing measures leaves this claim unsubstantiated. A paper introducing a new salience measure for LLMs must benchmark against the existing ones.

- **The external perturbation experiments are anecdotal, not rigorous.** The VLM analysis (Section 3.1) is conducted on a single image from ScienceQA with qualitative FI maps and one example of masking top-10 pixels. There is no quantitative evaluation across multiple images, multiple VLMs, or against other attribution methods (e.g., GradCAM, integrated gradients). The paper frames this as a "case study" (line 137), which is honest, but it does not constitute the kind of empirical evidence needed to support claims about the measure's general usefulness for external perturbation analysis. Similarly, the cross-modal prompt analysis is shown on one example.

- **The computational approach for parameter-level FI at 7B scale is under-specified.** The paper provides the SVD-based closed form (Equation 4), which is mathematically sound, but it is not explained how FI is computed "for each element in the weight matrices across all layers" (line 159) at 7B scale without prohibitive cost. The notation is ambiguous about what ω represents at each granularity (single parameter vs. channel vs. weight matrix), and how the SVD approach scales when computing FI per element across billions of parameters. The paper also does not report actual compute time or FLOPs for the FI computation.

- **Overclaimed novelty relative to prior work.** The paper claims FI as a "novel influence measure" (line 21) and the framework as "novel" (line 27), but the mathematical core — perturbation manifold (Zhu et al., 2007, 2011), reparameterization invariance (Shu & Zhu, 2019), and the closed form $\nabla f^\top G^{-1}\nabla f$ — is a direct application of established methods from information geometry and local influence analysis. The paper cites these sources, so this is a framing issue rather than a citation failure, but it does overstate the contribution. The novelty lies in the *application* to LLMs and the empirical validation, not in the measure itself.

### Minor

- **The invariance property is not empirically demonstrated to matter in practice.** The paper argues theoretically that invariance is important (ReLU scaling symmetries, Section 2), but the experiments never compare FI against a non-invariant baseline (e.g., gradient norm) on a setup where scaling would cause problems. Without this comparison, the invariance property remains an unverified theoretical advantage.

- **No comparison against Koh & Liang's influence functions or other training-data influence measures**, which are the most closely related prior work on influence in deep learning. The paper distinguishes itself (it measures parameter/input perturbation sensitivity, not training data influence), but a brief positioning against this literature would help.

- **The notation "FI" is overloaded.** In Section 3.2 (line 169), the paper writes "average Fisher Information (FI)" — but FI is defined as "First order local Influence" (line 21). This is confusing and technically sloppy, since the quantity is not Fisher information.

- **The paper does not discuss limitations.** It acknowledges that "accelerat[ing] the computation of the metric" is future work (line 209), but does not discuss other known limitations: FI is data-dependent, may be unstable when predicted probabilities are very peaky (common in LLMs), and the SVD approach assumes a fixed set of output classes.

### Trivial

- Figure 4 is referenced as "Figure 4" in the caption (line 192) but the surrounding text refers to "Figure 5" — the figure numbering appears to be out of sync (and this may be a parser artifact).
- The paper uses "entropy" in line 139 but defines $f(x) = -\log P(y_{pred}|x,\theta)$, which is cross-entropy for the predicted class, not entropy.

## Nice-to-Haves

- Compare FI against gradient norm and weight magnitude as baselines for the sparsification experiments — this would isolate the effect of the invariance property.
- Include at least one cross-task generalization experiment: compute FI on one dataset and evaluate sparsification effects on a held-out dataset to show FI identifies parameters that matter generally, not just for a single task.
- Report compute time or FLOPs for computing FI at the 7B scale to give readers a practical sense of the overhead.
- For the external perturbation analysis, provide quantitative results across at least 50–100 images (e.g., accuracy drop from masking top-FI vs. random patches, averaged over multiple images and images from multiple datasets).

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Circularity between FI computation and evaluation on MMLU"** (Harsh Critic, Critical Issues #2): Removed because this misreads the experimental design. Computing importance on the same distribution you evaluate is standard practice for validating that a salience measure identifies the parameters that matter for that task. It is not circular — it's the intended validation. (The instruction-following experiment on Alpaca-eval already uses separate data for FI estimation and evaluation, partially addressing this concern.)

2. **"G_ω is of dimension d×d where d is the number of parameters, infeasible for 7B models"**: Removed because the paper presents an SVD-based computation (Equation 4) that factorizes $G_\omega = B_0^\top B_0$ where $B_0$ is $p \times K$ with $K$ being the number of classes (small, e.g., 4 for MMLU). The critic's concern about full-matrix inversion is addressed by the paper's approach, though the per-element computation detail remains under-specified (kept in Major).

3. **"Missing evaluation on adversarial perturbations (jailbreak prompts, adversarial images)"**: Removed as scope creep. The paper is about stability under general perturbations (masking, sparsification, quantization, merging), not specifically about adversarial robustness. Asking for adversarial experiments demands an additional paper direction.

4. **"The paper does not discuss whether FI-highlighted patches are ones a human would consider important"**: The paper does discuss this (line 141: "FI values around relevant objects, such as the kelp and starfish, are comparatively higher"). The critic's concern is partial and the paper's qualitative discussion is appropriate for a case study.

5. **Strength Finder's generic/fluff strengths**: Some claimed strengths were generic and removed. Remaining strengths are those with specific evidence cited from the paper.

## Novel Insights

The reviews collectively reveal a paper with a solid theoretical foundation (information-geometric influence measure with invariance) and one genuinely striking empirical finding (sparsifying 2–3% of top-FI parameters causes 75% accuracy loss), but the paper is held back by a systematic lack of competitive baselines that prevents the reader from assessing whether FI actually outperforms simpler alternatives. The core intellectual tension is that the invariance property — which is the paper's main theoretical selling point — is never tested in a head-to-head comparison where scaling symmetries would cause a non-invariant baseline to fail. Until that experiment is done, the paper reads as an application of a known measure to LLMs rather than as a validated advance in measuring LLM stability.

## Suggestions

1. Add comparison baselines to the sparsification experiment: weight magnitude, gradient norm, and a diagonal Fisher approximation. This directly tests whether FI's invariance yields practical advantages.
2. Demonstrate the invariance property empirically: construct scaling-equivalent parameterizations of a ReLU network and show FI is stable while Jacobian norm/gradient norm vary. Then evaluate whether this stability leads to more reliable saliency across training checkpoints.
3. Clarify the computational procedure for per-element and per-channel FI at 7B scale, including typical wall-clock time and memory, so readers can assess practical feasibility.
4. Expand the external perturbation evaluation to a quantitative study across multiple images and compare against at least one baseline attribution method (e.g., gradient × input).
5. Rephrase the contribution to accurately reflect that the novelty is in the application to LLMs and the empirical validation, not in the measure itself.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>