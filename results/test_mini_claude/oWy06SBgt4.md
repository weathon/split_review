Now let me do calibration searches to find comparable papers.Based on my reading of the paper and the calibration anchors, I have enough to produce the final review.

## Summary
The paper proposes the first attempt at fully quantized training (FQT) with average 1-bit weights, activations, and gradients, evaluated in a transfer-learning / on-device fine-tuning setting. The contribution combines (a) a regret-style analysis arguing that Adam is more robust than SGD to gradient-quantization noise; (b) an algorithm pairing Activation Gradient Pruning (AGP) — keeping only N/b groups at b-bit precision so the average bitwidth is 1 — with Sample-Channel joint Quantization (SCQ) to make both weight- and activation-gradient matmuls binary-friendly; and (c) a PyTorch library `binop` with measured speedups up to 5.13× over FP32 on Hygon and Raspberry Pi 5.

## Strengths
- **First successful 1-bit-average FQT.** Table 1 shows convergence at (W,A,G)=(1,1,1) on six transfer-learning datasets with both ResNet-18 and VGGNet-16, beating 1-bit PSQ by ~6 percentage points on average (ResNet-18: 54.01% → 60.53%; VGG-16: 64.24% → 69.97%). This pushes the FQT precision frontier from the prior 4-bit state of the art.
- **Algorithmically clean AGP + SCQ design.** AGP achieves an unbiased estimator (Sec. 5.2, definition of M with $m_i \sim \text{Bern}(p_i)$, $p_i \propto R_i$) with a strict variance upper bound (Eq. 24: $\frac{D^{(l)}}{4B^2}\sum_{i=1}^{N/b}R_i^2$) lower than 1-bit PSQ. SCQ (Sec. 5.3) decouples PSQ for the activation-gradient path and PCQ for the weight-gradient path so both matmuls become hardware-friendly 1-bit multiplications via the lossless bit decomposition in Eq. on line 238.
- **Working systems implementation with measured end-to-end speedups.** Table 3 reports 5.13× peak (3.74× average) speedup on Hygon and 3.72× peak on Raspberry Pi 5 over FP32 PyTorch for VGG-16, and Table 5 shows the bit-decomposition overhead vs. pure 1-bit MM is small. This is a real engineering contribution rather than a paper-only proposal.
- **Empirical corroboration of the variance argument.** Fig. 11 shows the proposed quantizer has consistently lower variance than PSQ across datasets, and the lowest variance is on Flowers/Pets, which are precisely the datasets where the accuracy gap to QAT is smallest (Table 1) — the heterogeneity-→-utility story is at least partially supported.
- **Ablation on the retained-group bitwidth b.** Table 1 reports b ∈ {2, 4, 8}, identifying b=4 as optimal across both architectures and all six datasets, giving concrete deployment guidance.

## Weaknesses

### Fatal
None.

### Major
- **"1-bit FQT" framing is significantly looser than the title implies.** The method keeps 1/b of gradient groups at b-bit precision (best at b=4) and prunes the rest to zero. The "1-bit average" is real in storage/op-count terms (b-bit slices decompose losslessly into b binary planes), but informationally the gradient is sparse 4-bit on ~25% of groups, not a true 1-bit gradient. Table 1 itself shows b=8 underperforms b=4 on every dataset, confirming the contribution is "importance-weighted sparse mixed-precision with 1-bit kernels," not 1-bit gradients. The result is real and useful, but the framing oversells what was demonstrated. — *why it matters*: a reader comparing this to genuine 1-bit gradient algorithms (which the paper claims to be) will get the wrong impression of the algorithmic novelty vs. existing 4-bit FQT work.
- **The theoretical bounds do not actually justify the "Adam-vs-SGD at low precision" conclusion they are invoked to support.** The paper concludes (line 167) that $R^{SGD}/T = O(\sigma^2) + O(1)$ and $R^{Adam}/T = O(\sigma) + O(1)$. The non-vanishing $O(1)$ term means neither bound shows convergence to zero — both just give an asymptotic constant error. Separately, Assumption 1 (line 121) only requires $-e \le \mathbb{E}[\hat{\nabla}] \le e$ (a bias bound), but §3.2 (line 96) explicitly requires the quantizer to be unbiased, in which case $e=0$ and the $O(1)$ residual should disappear from both bounds. The current presentation is internally inconsistent on whether bias is zero, and the σ-vs-σ² gap is a worst-case parameterization artifact, not the rigorous license for the design choice that §4 claims it to be. — *why it matters*: this is the paper's sole theoretical contribution and the named motivation for choosing Adam; either tighten it or relegate it to motivation and let the empirical Fig. 1 / Fig. 3 carry the claim.
- **The 1-bit baseline comparison is thin and conflates two effects.** Only PSQ at (1,1,1) is compared in Table 1. Obvious alternative configurations of existing per-group quantizers at the matched 1-bit-average budget (e.g., importance-weighted but uniform-bit pruning, or non-pruned per-group with logarithmic gradients) are absent. The AGP variance bound (Eq. 24) compares against 1-bit PSQ on all groups, but this comparison conflates (i) spending more bits per retained group (increasing $B$ from 1 to $2^b-1$) with (ii) sample-weighted pruning. The natural ablation — importance-pruned uniform-bit PSQ at the matched budget — is missing, so the table cannot cleanly attribute the 6-point win to importance pruning vs. concentrating bits. — *why it matters*: as written, the experiments cannot distinguish "AGP+SCQ is the right design" from "any unbiased sparse mixed-precision scheme would work."
- **Accuracy gap is uneven across datasets and the headline number underweights this.** The "~5% drop on visual classification" claim (abstract, intro) is the b=4 VGG-16 average (4.85). For ResNet-18 at b=4 the per-dataset gap to QAT is Cars 50.81→37.88 (≈13 pts), CIFAR-100 65.82→56.83 (≈9 pts), and CUB 42.13→39.47 (≈3 pts). Fig. 11 shows the method's variance is lowest exactly on Flowers/Pets where it works best. The method's utility is plausibly bounded by how gradient-heterogeneous the downstream task is — that conditioning is real and important and deserves to be in the headline framing rather than being treated as "minimal loss on Flowers and Pets" cherry-picking. — *why it matters*: the "1-bit FQT is achievable" claim is a different claim from "1-bit FQT is achievable on heterogeneous-gradient tasks," and only the second is supported.

### Minor
- **Handling of $p_i > 1$ in AGP is unspecified.** The assignment $p_i = NR_i/(bR_{total})$ can exceed 1 when one group's range dominates. If you clip to 1 and renormalize, strict unbiasedness no longer holds without an explicit correction. The paper does not say what is done.
- **The activation-gradient tensor is quantized twice under SCQ** — once via PSQ for the input-gradient matmul and once via PCQ for the weight-gradient matmul — but this duplication of cost / storage and its impact on memory and accuracy are not discussed. The AGP variance bound in Eq. 24 strictly applies only to the PSQ path; the PCQ-pruned path is a different statistical object.
- **BERT/MLP-Mixer/Faster-RCNN results are reported as single numbers with no spread** (Table 2), and used to support "potential applicability to other architectures." For transformers in particular, gradient distributions differ substantially from CNNs, and the sample-dimension heterogeneity argument may not transfer. Adding seed variance would help; the current sentence overstates what one number per task can support.
- **The "100× over unoptimized FP32" framing is not the meaningful headline.** The honest comparison is optimized 1-bit vs. optimized FP32 (5.13× peak) or vs. optimized 8-bit SCQ (>10×), both of which are real and impressive. The unoptimized-vs-unoptimized number primarily reflects single-core PyTorch FP32 being slow.

### Trivial
None substantive.

## Nice-to-Haves
- A small table walking through per-layer compute and memory budget for AGP vs. PSQ-1-bit vs. 4-bit per-group, to disarm the "1-bit on average really means 4-bit on 25%" reading.
- A memory-footprint comparison alongside Table 3 — on-device fine-tuning is activation-memory bound and the binary forward pass is the real win there.
- An ablation directly comparing (i) importance-pruned uniform-bit PSQ at the 1-bit budget vs. (ii) AGP, to attribute the win to importance pruning vs. precision concentration.
- A correlation plot between dataset-level variance reduction (Fig. 11) and accuracy gap (Table 1) — would convert the Flowers/Pets-vs-Cars observation into a predictive claim about which tasks 1-bit FQT will work on.

## Removed Points
These points are flagged to be removed, treat them with caution.

- *Harsh critic's "missing modern BNN comparators (ReActNet, IR-Net, distribution-rectified BNNs)" point* — soft scope creep; the QAT baseline (Bulat 2019) is a reasonable upper-bound reference and the paper's claim is about gradient quantization on top of any BNN backbone, not about beating SOTA BNNs.
- *"Compare against a 4-bit FQT baseline (Xi 2023) on the same tasks"* — a fair ask, but borders on asking the paper to do a different experiment; the 8-bit PSQ comparator in Table 3 already gives the relevant accuracy-vs-speed tradeoff.
- *Strength: "Comprehensive evaluation across architectures and domains"* — partly demoted because the Table 2 numbers are single-run, single-task per architecture, which the major-weaknesses section already flags; not a clean strength.
- *Strength: "AGP variance reduction bound is strictly smaller than 1-bit PSQ"* — kept above, but the comparison is partly mechanical (because $B$ differs between b-bit and 1-bit PSQ); the "strictness" of the bound is less informative than the strength-finder presented.
- *"Reproducibility / availability of cited systems"-style concerns* — none in the harsh review; nothing to remove on this axis.

## Novel Insights
None beyond the paper's own contributions. The bit-decomposition trick that turns b-bit per-group quantization into b stacked 1-bit matmuls (combined with PSQ-for-input-gradient / PCQ-for-weight-gradient asymmetry to keep both matmuls binary-kernel-friendly) is the paper's main insight, and the empirical observation that AGP's accuracy advantage tracks gradient heterogeneity (Flowers/Pets best, Cars worst) is suggestive of when 1-bit FQT is practically deployable. Both are credited to the paper.

## Suggestions
1. Reframe the title/abstract claim as "sparse mixed-precision FQT at an average bitwidth of 1 via bit decomposition" or similar, and be explicit in §1 that the operative configuration is "4-bit on 25% of groups." This removes the largest framing objection at almost no cost.
2. Either (a) tighten Theorems 1–2 under the unbiased assumption in §3.2 (which removes the $O(1)$ residual and produces honest $O(\sigma^2)$ vs $O(\sigma)$ bounds), or (b) downgrade §4 to motivation and lean on Fig. 1 and Fig. 3 empirically. Either route is acceptable; the current state is the worst of both.
3. Add an importance-pruned uniform-bit PSQ baseline at the matched 1-bit-average budget to Table 1, to cleanly isolate the contribution of pruning from the contribution of bit concentration.
4. Specify what happens when $p_i > 1$ in AGP and re-verify unbiasedness under that handling.
5. Report variance across seeds for the BERT, MLP-Mixer, and Faster R-CNN runs, and soften "potential applicability to other architectures" to match the evidence (one task, one number).
6. Replace the headline "100× over unoptimized FP32" with the optimized-vs-optimized number (5.13× over FP32; >10× over SCQ-INT8). The honest number is already impressive.

## Evaluation on the Standard Axes
- *Originality*: High. First reported 1-bit-average FQT, with a non-trivial algorithmic combination (importance-pruned per-group + dual-axis quantization + bit decomposition).
- *Importance of question*: Substantial. On-device fine-tuning is a real workload, and pushing FQT below 4 bits has clear hardware-design implications.
- *Claims well supported*: Partially. The empirical "convergence is achievable, with measurable speedup" claim is supported. The "theoretical-grounded design," "1-bit gradients," and "~5% drop" framings are oversold relative to what's on the page.
- *Soundness of experiments*: Reasonable for the main CNN tables (mean ± std over 3 seeds); thin for Transformers/MLP-Mixer/detection and missing one obvious 1-bit-budget ablation.
- *Clarity*: Adequate; the bit-decomposition mechanism and SCQ asymmetry are well explained.
- *Value to the community*: Real. The `binop` library and measured edge-device speedups make this immediately reusable.

## Score and Decision

Round 1 retrieved anchors:
- `6Mdvq0bPyG.md` (EfficientQAT) — avg 3.00, weak anchor; LLM QAT, different problem.
- `mJ8k81O5BF.md` (Low-bit PTQ data-free) — avg 3.00, weak anchor; PTQ, not FQT.
- `orG37FHN4b.md` (Angle-DFQ) — avg 3.00, weak anchor; data-free quantization.
- `XtXa6hoNrU.md` (DFRot) — avg 3.50, weak anchor; rotation for LLM quantization.
- `wJ3GeGLFmc.md` (Sub-8-Bit Integer Training, ShiftQuant) — avg 4.50, **closest sibling**; sub-8-bit training with theoretical analysis and hardware speedup, criticized for FP-baseline fairness and hardware practicality.
- `oOwDQl8haC.md` (Low-bit-width accumulators) — avg 5.75, Accept; quantizes accumulator only, well-targeted novelty.
- `3j72egd8q1.md` (Custom Gradient Estimators are STE in Disguise) — avg 5.25, Reject; theory-focused QAT.
- `OyAMxlDikl.md` (Bayesian Adaptive Quantization) — avg 4.00, Reject; different angle.
- `wg1PCg3CUP.md` (Scaling Laws for Precision) — avg 8.00, Accept; far broader, not a direct sibling.
- `TJo6aQb7mK.md` (Pretraining Ternary LMs) — avg 7.60, Accept; pretraining ternary, large-scale.
- `wJv4AIt4sK.md` (Sparsity × Quantization) — avg 7.50, Accept; clean theory + experiments.
- `E1EHO0imOb.md` (FP8 trillion-token training) — avg 7.50, Accept; massive empirical scale.

**Round 1 bracket**: Between 4.5 (Sub-8-Bit Integer Training) and 6.0 (just below "Cheaper Inference with Lower Bit-Width Accumulators"). The paper is more ambitious than ShiftQuant in scope (1-bit vs sub-8-bit) and has real hardware deployment, but it has framing issues and a thinner 1-bit baseline.

Round 2 retrieved anchors (narrowing):
- `Dm4qrBuFKH.md` (Training BNNs in Binary Weight Space) — avg 4.67, Reject; weights binary only, not gradients.
- `lGUyAuuTYZ.md` (BNN+SNN hybrid) — avg 5.67, Accept; different domain.
- `sYGNCscE9M.md` (Nearly Lossless Adaptive Bit Switching) — avg 5.75, Reject; bit-width switching for QAT.
- `JAnyCnK5In.md` (Online SNN training) — avg 4.75, Reject; different topic.
- `xNdE7RiRyP.md` (TinyTrain) — avg 5.25, Reject; on-device sparse-update training; similar deployment motivation.
- `myYzr50xBh.md` (Zeroth-order LLM fine-tuning) — avg 5.80, Accept; different angle.
- `xzSUdw6s76.md` (PalmBench) — avg 5.80, Accept; benchmark paper, different.
- `zcx6rIMbbR.md` (Three-Stage Optimization for QLLMs) — avg 5.40, Reject; not directly comparable.
- `Fj6Yv5rPRe.md` (Online learning meets Adam) — avg 4.25, Reject; theory-focused.
- `lD9Kc22Wls.md` (Quantized Optimistic Dual Averaging) — avg 5.50, Reject; distributed VI with adaptive quantization.

**Round 2 narrowing**: The closest siblings are ShiftQuant (4.50), Training BNNs in Binary Weight Space (4.67), TinyTrain (5.25), and Nearly Lossless Adaptive Bit Switching (5.75). The paper under review is more ambitious than ShiftQuant (truly 1-bit vs sub-8-bit) and has more substantial system implementation, but shares the same kinds of evaluation thinness and framing-overclaim issues that drove ShiftQuant to 4.50. It is more substantive than the binary-weight-space BNN paper (4.67), and on par or slightly stronger than TinyTrain (5.25) on engineering rigor but weaker on rigor of central claims. The framing/theory/baseline issues are real but the contribution (first 1-bit-average FQT with measured hardware speedups) is genuinely novel.

Placing relative to round-2 anchors: better than ShiftQuant (4.5) and the binary-weight-space BNN (4.67); about even with TinyTrain (5.25) but in different dimensions; clearly below "Cheaper Inference with Lower Bit-Width Accumulators" (5.75, Accept) because of the framing and theory issues. Best single-number placement: **5.0** — a borderline paper, real contributions with real framing/coverage issues that a rebuttal could partially but not fully resolve.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>