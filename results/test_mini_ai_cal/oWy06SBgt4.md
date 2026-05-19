I have all the information needed for calibration. Now let me produce the final consolidated review.

---

## Summary

This paper makes a first attempt at 1-bit Fully Quantized Training (FQT), where weights, activations, and gradients are all quantized to 1-bit. The authors provide a theoretical analysis showing that SGD's regret scales as O(σ²) while Adam's scales as O(σ) under gradient variance, motivating variance reduction. They propose Activation Gradient Pruning (AGP), which prunes low-information gradient groups and allocates higher bitwidth to important ones while maintaining an average of 1-bit, and Sample-Channel joint Quantization (SCQ), which uses different per-group quantizers for weight and activation gradient computations to enable hardware acceleration. Experiments on transfer learning tasks (fine-tuning pre-trained binary models) show ~5% accuracy drop vs. full-precision gradient QAT, with up to 5.13× training speedup over FP32 PyTorch on CPU hardware.

---

## Strengths

1. **First demonstration of convergent 1-bit FQT (weights, activations, and gradients all at 1-bit).** Table 1 shows consistent convergence across six datasets and two architectures (ResNet-18, VGGNet-16), with average accuracy improvements of ~6% over 1-bit PSQ (the standard FQT baseline applied at 1-bit). On VGGNet-16 with b=4, the method achieves 69.97% average accuracy vs. 64.24% for 1-bit PSQ. This is a genuine empirical milestone — prior work stopped at 4-bit.

2. **Hardware-aware SCQ design (Section 5.3).** The paper identifies a real practical bottleneck: per-sample quantization (PSQ) cannot accelerate weight-gradient computation because one operand must first be dequantized to FP32. SCQ uses per-channel quantization for weight gradients and per-sample quantization for activation gradients, keeping both multiplications as 1-bit × 1-bit operations. This is a non-obvious engineering insight validated by the speedup measurements in Table 3 (e.g., SCQ-Basic at 8-bit achieves 0.19× vs. 0.07× for PSQ-Basic at the same precision).

3. **Convergence analysis linking gradient variance to optimizer sensitivity (Section 4.1).** The paper derives regret bounds showing SGD's per-iteration regret scales as O(σ²) while Adam's scales as O(σ). This theoretical distinction — beyond what prior FQT work provided — cleanly explains why Adam is preferred at low bitwidths and motivates the variance-reduction approach. The subsequent experiment (Fig. 3) validates the theory: PSQ at 1-bit with SGD diverges (near 10% accuracy), while the proposed method with SGD converges to ~80%.

4. **Real hardware speedup measurements on two platforms (Hygon CPU, Raspberry Pi 5) with a working PyTorch library (`binop`).** Table 3 reports speedups at multiple input resolutions. The "Ours-Basic" row (unoptimized implementation) already achieves 3.17× (VGGNet/Hygon avg) over PyTorch FP32, showing the speedup is not purely an optimization artifact. The 5.13× peak is a genuine speedup over PyTorch's optimized kernels.

---

## Weaknesses

### Fatal

None. The paper's core empirical claim — that 1-bit FQT can converge on transfer learning tasks — is supported by the main results table. The theoretical concerns are real but do not invalidate the empirical findings.

### Major

1. **The AGP variance bound (Eq. 24) ignores the mask variance from importance weighting, and the proof is deferred to an appendix that cannot be checked.** The paper defines the AGP quantizer as Q_g(∇) = Q^b_PSQ(M∇) with M = diag(m₁/p₁, …, m_N/p_N), m_i ~ Bern(p_i). The variance bound in Eq. 24 is stated as ≤ (D^{(l)})/(4B²) Σ_{i=1}^{N/b} R_i², which only accounts for the stochastic rounding variance of the PSQ component. The importance-weighting factor 1/p_i introduces additional variance (Var[m_i/p_i] = (1-p_i)/p_i, which grows large when p_i is small), and this term is not accounted for in the stated bound. Furthermore, the bound sums over precisely the groups with the *largest* ranges (since AGP selects the top N/b groups by R_i), so the claimed comparison to PSQ's variance ("significantly smaller") is not as straightforward as presented. The paper provides empirical variance measurements (Fig. 11) as supporting evidence, which partially mitigates this concern, but the central theoretical motivation for AGP is incomplete as presented. The proof is referenced as "given in" (line 236) but is not in the extracted text — if the full proof properly handles these terms, it should be brought into the main paper.

2. **Evaluation scope is limited to transfer learning while the title and framing suggest general training capability.** The abstract mentions "fine-tuning" and the limitations section is transparent, but the title "1-Bit FQT: Pushing the Limit of Fully Quantized Training to 1-bit" does not qualify "training" as fine-tuning. Phrases like "training can be implemented with binary operations" and "training speedup can reach a maximum of 5.13×" in the introduction imply full training capabilities. The limitation that training from scratch is not possible — and that "even the 3-bit FQT from scratch is still an open problem" — is buried in the last paragraph. This creates a gap between the paper's framing and its actual scope, which is fine-tuning pre-trained binary models.

### Minor

3. **Probability assignment p_i = NR_i/(bR_total) can exceed 1, but the paper does not specify how this edge case is handled.** The paper states p_i ∈ [0,1] (line 227), but for heterogeneous gradient ranges where a few groups dominate, p_i can exceed 1 (e.g., with batch size N=64 and b=4, the maximum possible p_i is N/b = 16). Bernoulli sampling with p_i > 1 is ill-defined. The paper does not discuss clipping or normalization of probabilities. This is a gap in the algorithm specification that affects reproducibility.

4. **No ablation study isolating AGP from SCQ.** The paper presents two components, but the main experiments (Table 1) combine them. Without an ablation showing accuracy with SCQ alone (varying only the quantization strategy) and AGP alone (without the SCQ modification), the reader cannot assess the individual contribution of each component. Similarly, the speedup contribution of SCQ vs. AGP is not disentangled.

5. **No comparison to 4-bit FQT methods (the current state of the art).** The paper compares against 1-bit PSQ, 8-bit PSQ, and QAT (32-bit gradients), but does not compare against any 4-bit FQT method (e.g., Sun et al. 2020, Chmiel et al. 2021, Xi et al. 2023) in terms of accuracy. The authors note that "there is no 4-bit format among the standard data types" (line 398) for speed comparison, but an accuracy-only comparison on the same architectures and datasets would contextualize whether the 1-bit extreme is worth the ~5% accuracy drop. If a simple 4-bit method achieves, say, 64% on CIFAR-100 (vs. the paper's 56.83% at b=4), the practical value of the 1-bit approach would need qualification.

6. **Additional results (Table 2) are single-run, single-baseline, and lack depth.** The Faster R-CNN, MLP-Mixer, and BERT experiments each report only one number per method with no variance, no learning curves, and no comparison to any FQT baseline (only QAT with 32-bit gradients). The BERT GLUE score drops from 63.20 to 54.81 (8.39% degradation), which is substantial, and the paper does not discuss this. These results feel like a token attempt at broader evaluation.

### Trivial

None. The paper is adequately written for a conference submission; any formatting issues are parser artifacts.

---

## Nice-to-Haves

- Add an ablation study decomposing AGP vs. SCQ contributions to accuracy.
- Compare against 4-bit FQT methods on accuracy, even if speed cannot be compared (different hardware).
- Specify how p_i > 1 cases are handled (clipping, normalization, or a different selection mechanism).
- Add variance plots with labeled axes and statistical testing (mean ± std over runs).
- Report wall-clock time to reach a target accuracy, not just per-iteration speedup.

---

## Removed Points

These points were raised by reviewers but are removed or demoted, with brief justification:

- **"Speedup measurements are inflated by an unfairly slow baseline"** (Harsh Critic, Critical Issue #3): REMOVED. The critic claimed "Ours" (5.13×) is compared to the authors' own slow FP32 implementation. This is incorrect — the table caption states "The baseline is FP32 PyTorch." The "Basic" (0.03×) row is a separate illustration of naive implementation overhead, not the baseline for "Ours." The 5.13× is a direct comparison to PyTorch's optimized kernels. The criticism is factually wrong.

- **"PSQ at 1-bit is a strawman baseline"** (Harsh Critic): REMOVED. PSQ (per-sample quantization) is a standard FQT method from prior work (Chen et al. 2020). Applying it at 1-bit is a natural and informative baseline — it shows what the standard method achieves when pushed to the same extreme. This is standard practice, not a strawman.

- **"Theoretical regret bounds add nothing beyond standard analyses"** (Harsh Critic): REMOVED. While the bounds follow from standard regret analyses, applying them to FQT and deriving that SGD scales as O(σ²) vs. Adam's O(σ) is a non-trivial insight that directly motivates the paper's algorithm. The analysis is not the paper's deepest contribution, but it is not vacuous.

- **"Fig. 11 Y-axis is unlabeled"** (Harsh Critic): REMOVED per formatting/nitpick rule. This is a presentation detail that may also be a parser artifact.

- **"No comparison to prior FQT methods at 4-bit"** is kept as a Minor weakness (see above) rather than the Major issue the critic claimed, because the paper's central claim is about pushing to 1-bit — the comparison to 4-bit is an important contextual question but not a direct invalidation of the core result.

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an observation about the paper that the authors themselves do not make.

---

## Suggestions

1. **Fix the AGP variance analysis.** Either (a) provide a complete variance derivation that accounts for the mask stochasticity (the 1/p_i factor) and the selection bias (retained groups have the largest R_i), or (b) clearly state the bound as an approximation under simplifying assumptions and rely on the empirical validation (Fig. 11) instead. The current presentation gives the impression of a rigorous proof that does not fully exist.

2. **Add ablation studies separating AGP and SCQ.** Run experiments with (a) SCQ only (no pruning, using per-channel + per-sample quantization at 1-bit) and (b) AGP only (pruning + PSQ without the SCQ modification). This would clarify the individual contribution of each component.

3. **Add a 4-bit FQT accuracy comparison.** Even a single comparison on a standard setting (e.g., ResNet-18 on CIFAR-100) using numbers from published papers would help readers assess the trade-off.

4. **Address the p_i > 1 edge case explicitly.** Specify what happens when a group's range is large enough that p_i = NR_i/(bR_total) exceeds 1. Options: clamp to 1, renormalize, or use a different selection mechanism.

5. **Quality the title/framing more precisely.** Consider rephrasing to indicate that the method targets transfer learning/fine-tuning, not training from scratch. The current limitations paragraph is honest but too late.

---

## Score and Decision

**Round 1 bracketing:** The paper sits above weak anchors (2.5–3.0: papers with fundamental flaws) and below strong anchors (7.6–8.0: papers with clean, well-supported contributions). Initial bracket: 4.5–6.0.

**Round 2 narrowing within bracket:** Compared to anchors at 4.75 (FP8 robustness paper — interesting findings, but overclaims scope relative to evidence), 5.25 (FeedSign — clever 1-bit communication idea, decent experiments, imprecise claims), 5.40 (QB-Net — strong ablations, real hardware, missing critical baselines), and 6.00 (COAT — clean contributions, broad validation, well-supported). The current paper is most comparable to FeedSign (5.25) and QB-Net (5.40): it has a genuinely ambitious goal with interesting algorithmic components, real hardware measurements, and recognizable limitations. However, the theoretical gap in the central variance-reduction claim (Major weakness #1) is more central to the paper's story than comparable gaps in those anchors, and the evaluation scope (transfer learning only) narrows the contribution. The paper falls slightly below those anchors.

**Final score: 5.0** — a paper with a genuine contribution (first 1-bit FQT convergence) and interesting practical ideas (AGP, SCQ), held back by a significant theoretical gap in the variance analysis that motivates the core algorithm, and an evaluation scope narrower than the framing suggests. The empirical results are sufficient to demonstrate feasibility but not to fully substantiate all claims.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>