---
job_id: a3fff601-9110-48b2-998a-07ba72a6d4d6
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: mGeeRFToaW.pdf
paper: Fine-tuning Quantized Neural Networks with Zeroth-order Optimization
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on optimization, efficient training, quantization, and adaptation of large neural models.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including abstract, introduction, related work, methodology, experiments, quantitative results, ablations, and conclusion/discussion, and it provides enough empirical evidence to warrant full review despite some technical and presentation issues.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, manipulative instructions, or suspicious content targeting automated review systems in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper proposes Quantized Zeroth-order Optimization (QZO), a method for fine-tuning quantized neural networks, especially LLMs, by combining zeroth-order optimization with quantization. The key idea is to estimate gradients by perturbing continuous quantization scales rather than discrete quantized weights, and to stabilize training with a directional derivative clipping (DDC) mechanism. The paper evaluates QZO on several LLM families and NLP tasks under 4-bit and 2-bit quantization, with additional qualitative experiments on Stable Diffusion in the appendix.

## Strengths
The paper addresses a practically important problem, namely how to push memory-efficient adaptation beyond gradient-free training alone by also reducing weight storage through quantization. This is a meaningful systems-and-optimization contribution for the LLM fine-tuning setting.

The core idea is simple and reasonably well motivated. Perturbing continuous quantization scales instead of discrete weights is a natural way to reconcile SPSA-style updates with quantized models, and this design avoids repeated de-quantization and re-quantization during training.

The empirical memory savings are substantial and clearly communicated. **Figure 1** is particularly effective in making the paper’s central practical case: QZO reduces peak memory substantially relative to both full fine-tuning and MeZO across OPT-6.7B, Llama-2-7B, and Llama-3.1-8B. The reduction from around 14.8-20.4GB for MeZO to 4.8-6.2GB for QZO is not a cosmetic gain, it changes what hardware can run the method.

The main results are encouraging. In **Table 1**, QZO consistently improves over Zero-Shot-Q, which supports the claim that the proposed approach can actually fine-tune quantized models rather than merely preserve zero-shot performance. On some tasks, the gap to MeZO is also quite small despite the heavier quantization constraint, and on Llama-2-7B / SQuAD, QZO even exceeds MeZO. This makes the method interesting even when judged beyond memory savings alone.

The paper also does a decent job showing that QZO is not tied to a single quantization family. The experiments cover GPTQ-style 4-bit scalar quantization and AQLM-style 2-bit codebook quantization, which supports the “orthogonal to PTQ methods” pitch better than a single-setup evaluation would.

The ablation around DDC is useful. **Figure 2** gives a concrete diagnostic view of what the clipping is supposed to fix: without DDC, directional derivatives spike early and the loss becomes NaN around step 22. That figure is much more informative than simply reporting final accuracy with and without clipping. Likewise, **Figure 3** provides a reasonably interpretable sensitivity analysis of the clipping threshold.

The paper is generally readable, and the algorithmic description in **Algorithm 1** makes the training loop understandable at a high level.

## Weaknesses
1. **The theoretical justification around DDC is not convincing as written, and Theorem 1 appears incorrect or at least severely under-specified.**  
   The central theoretical claim in **Section 3.2.2, Theorem 1 on Page 5** is that the clipped estimator \(\hat{\nabla}_{\bm{\Delta}}\mathcal{L}'\) remains unbiased for the full gradient. For a clipped scalar directional derivative \(d'=\mathrm{clip}(d,-C,C)\), this is generally not true without strong symmetry assumptions on the joint distribution of \(d\) and \(\bm{z}\), and the paper does not state such assumptions. In fact, clipping a random variable usually introduces bias. The proof in **Appendix A, Eqs. (10)-(13), Page 13** is especially problematic: it splits the expectation into subsets indexed by whether \(d_i<|C|\) or \(d_i>|C|\), but then rewrites terms using different normalizations \(1/N\) and \(1/M\) without a valid derivation from the original dataset average. More importantly, the term for clipped samples is replaced by \(\frac{|C|}{M}\sum \bm{z}\), whose expectation is set to zero, but this does not establish unbiasedness of the full clipped estimator because the clipping event depends on \(d\), which itself depends on \(\bm{z}\). The dependence is exactly the thing that cannot be hand-waved away. This matters because the claimed variance reduction result in **Eq. (8)** relies on Theorem 1, so the theoretical story supporting DDC is much shakier than presented.

2. **The quantization formulation is oversimplified and in places mathematically misleading.**  
   In **Eqs. (3)-(4), Page 4**, quantization is written as \(\bar{w}=\lfloor w/\Delta \rfloor\), \(w=\Delta\cdot \bar{w}\). This omits zero-points, clipping/saturation, rounding-to-nearest instead of floor, groupwise indexing, codebook assignment structure, and any dependence of \(\Delta\) on a group \(\mathcal{W}\). The text later says Q-SPSA is applicable to both scalar-based and codebook-based methods, but the formalism never really covers the AQLM case. For codebook quantization, the dequantization map is not simply \(w=\Delta\bar{w}\) in general; there are codebook lookups and additive reconstructions. So the method description currently looks cleaner than the actual object being optimized. This matters because the paper’s main claim is precisely that the method is broadly compatible with different PTQ schemes, but the mathematical formulation only matches a narrow scalar-quantization abstraction.

3. **There is a mismatch between the dimensional notation in Q-SPSA and the actual trainable parameterization.**  
   In **Definition 3.3, Eq. (5), Page 4**, the estimator is written for \(\bm{\Delta}\in\mathbb{R}^d\) and \(\bar{\bm{\theta}}\in\mathbb{R}^d\), suggesting one scale per weight element. However, the paper later states that in practice “all quantization scales within a linear layer are perturbed” and **Table 2** shows that QZO trains only about \(5\times 10^7\) parameters, which is around \(1\%\) of the full model parameters. So the actual object being perturbed is not clearly the \(d\)-dimensional vector from the equations. This is not a minor notation nit. The variance properties, computational cost, and effective optimization landscape depend heavily on whether the perturbation is elementwise, channelwise, groupwise, or layerwise. The paper should define the real parameterization explicitly, for example with layer/group indices \(\Delta_{l,g}\), because the current notation blurs the core algorithmic object.

4. **The empirical comparison is missing stronger zeroth-order baselines and therefore does not fully establish that QZO is the right ZO design rather than just a workable one.**  
   The main baseline in **Tables 1 and 2** is MeZO. That is a reasonable starting point, but for a paper whose selling point is a new ZO formulation plus a stabilization mechanism, I wanted broader comparison to stronger or more recent ZO optimizers, or at least to variants that could isolate whether the gain comes from optimizing scales, from clipping, or simply from drastically reducing the trainable parameter count. As currently designed, **Table 1** mainly tells me that “training quantization scales with ZO is better than doing nothing,” and “sometimes competitive with MeZO,” which is useful but not a complete positioning against the ZO literature.

5. **The experimental setup introduces several confounds that weaken some of the claimed takeaways.**  
   The paper repeatedly compares QZO to full fine-tuning, MeZO, and zero-shot models, but these methods are not matched in trainable parameter count or even optimization problem. **Table 2** explicitly shows that QZO trains only around \(5\times 10^7\) parameters while MeZO and full fine-tuning operate on roughly \(6.7\times10^9\) to \(8\times10^9\) parameters. So when the paper claims QZO is far more computation-efficient, part of that is simply because it is solving a much smaller problem, not because the estimator itself is intrinsically more efficient. That does not invalidate the method, but the interpretation should be more careful. A more apples-to-apples comparison would include PEFT-style methods in the main paper, not only in the appendix, or a MeZO variant restricted to a similarly small parameter subset.

6. **The reported memory profiling is useful but somewhat cherry-picked in scope.**  
   The memory claims rely on profiling on SST-2 with per-device batch size 1 during the first 100 optimization steps, as described in **Section 4.2, Page 7**, and visualized in **Figure 1**. This does demonstrate minimum VRAM feasibility, but it is a very favorable metric for methods whose main appeal is “can this run at all on a 24GB GPU?”. It says less about realistic throughput/memory tradeoffs at practical batch sizes, sequence lengths, or mixed activation settings. Since the paper also emphasizes end-to-end usability, broader memory profiling would have made the systems argument stronger.

7. **The 2-bit results are promising but too limited to support some of the stronger claims.**  
   **Table 3** reports only Zero-Shot-Q and QZO on Llama-2-13B at 2 bits. There is no comparison to MeZO, no first-order quantized baseline, and no ablation on which parameters are updated in the AQLM setup. Since the 2-bit case is used to support claims about “extreme quantization” and even “on-device learning scenarios for edge devices” on **Page 8**, this evidence feels thin. Improving over zero-shot by a moderate amount is nice, but it is not enough to conclude much about competitiveness.

8. **Some experimental details remain underspecified for reproducibility and fair comparison.**  
   The paper gives a single default hyperparameter configuration for QZO in **Section 4.1, Page 6-7**, but it is not clear whether these were tuned per model/task, or how sensitive the method is to \(\epsilon\), learning rate, batch size, and number of steps beyond the clipping threshold analysis. Similarly, MeZO is said to use the official code, but the exact tuning budget and whether it was retuned for the specific datasets/models here is unclear. This matters because zeroth-order methods are often quite sensitive to hyperparameters, and small tuning asymmetries can distort conclusions.

9. **The paper’s discussion of DDC overstates what the experiments show.**  
   **Figure 2** does support that DDC prevents catastrophic early divergence in the shown run. However, from a single trajectory plot one cannot conclude a general variance-reduction mechanism “through rectifying abnormal loss values,” as stated around **Page 5 and Page 8**. The paper would be much stronger with direct statistics such as empirical variance of the estimated directional derivative or gradient norm across seeds and steps, rather than one qualitative failure case and one threshold sweep in **Figure 3**.

10. **Presentation quality is decent overall, but there are enough notation and editing issues to hurt confidence.**  
   There are several typos and inconsistencies, for example “sclaes” in **Theorem 1**, the Llama-3 naming inconsistency between text and **Table 1**, and some malformed references in the bibliography. More importantly, the mathematical exposition does not consistently distinguish between weights, quantized integers, scales, and grouped parameters. This is fixable, but for a methods paper centered on a new optimization formulation, precision matters.

## Questions
1. The biggest technical issue for me is **Theorem 1**. Can the authors provide a corrected statement and proof, or explicitly state the assumptions under which clipping preserves unbiasedness? If the estimator is actually biased but lower-variance, please say so plainly and discuss the bias-variance tradeoff rather than claiming unbiasedness.

2. In the actual implementation, what is the precise trainable object for GPTQ and AQLM? Is \(\Delta\) layerwise, channelwise, groupwise, or something else? Please rewrite **Eq. (5)** and **Algorithm 1** with the real indexing scheme. This would substantially improve clarity and help assess computational complexity.

3. Can the authors provide a more explicit derivation for how Q-SPSA applies to codebook-based quantization, since **Eqs. (3)-(4)** only really describe scalar quantization? In particular, which parameters are updated in the AQLM experiments, and what is the exact forward map being perturbed?

4. How were hyperparameters selected for QZO and MeZO across tasks and models? Were the defaults fixed globally, or tuned on validation data per task/model? A concise tuning protocol would increase my confidence in the fairness of **Table 1**.

5. Could the authors add stronger empirical evidence for DDC beyond the single-run plots in **Figure 2**? For example, average training success rate across seeds, variance of directional derivatives, or final performance with/without DDC over multiple runs.

6. The main paper would be stronger with at least one additional baseline that controls for trainable parameter count, for example a parameter-matched MeZO variant or a PEFT-style method in the main table. Can the authors clarify whether the main conclusion is “QZO is a better optimizer,” or rather “QZO is a practical low-memory training recipe because it updates a much smaller quantization-scale parameterization”?

7. For the 2-bit setup in **Table 3**, can the authors clarify why no MeZO or first-order quantized baseline is included? Even a partial comparison would help interpret how strong the 2-bit result really is.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper focuses on memory-efficient fine-tuning methods for existing public models and standard NLP benchmarks. I do not see a paper-specific ethics issue that requires escalation based on the main submission.

## Soundness Rating
2: fair. The empirical results are reasonably supportive of the main practical claim, but the theoretical justification around clipping is not reliable as written, and some methodological details are under-specified.

## Presentation Rating
3: good. The paper is readable and the motivation is clear, but the mathematical exposition is looser than it should be, and several notation/precision issues need correction.

## Contribution Rating
3: good. The idea of adapting quantized models by perturbing continuous quantization scales is useful and practically relevant, and the memory savings are meaningful, even though the method is not fully nailed down theoretically.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper offers a practical and interesting idea with strong memory-efficiency appeal and solid empirical evidence that the method works, especially at 4-bit. However, the theory around DDC is shaky, the formulation is cleaner on paper than in the actual quantization setups, and the evaluation could position the method more rigorously against stronger baselines and better-controlled comparisons.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the main equations, algorithm, tables, and figures carefully, though I cannot fully verify implementation-level details from the paper alone.