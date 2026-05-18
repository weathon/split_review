Now I have all the information I need. Let me construct the final review.

**Round 1 Bracket:** Based on the first calibration search, I bracketed this paper between the weak anchors (~3.0, EfficientQAT) and the strong anchors (~5.25, Custom Gradient Estimators). The EfficientQAT paper was much weaker (limited novelty, unfair comparisons), while the Custom Gradient Estimators paper had stronger theoretical rigor but narrower scope.

**Round 2 Narrowing:** I pulled anchors in the 3.5–6.0 range. The Sub-8-Bit Integer Training paper (4.5) — a rejected paper with similar topic (low-bit training), real hardware results, but unclear presentation — is the most comparable. The Robust Training at Arbitrary Precision paper (4.0) is also relevant. The current paper sits between these two: it has clearer presentation and a more novel contribution (first average-1-bit FQT) than the Robust Training paper, but is weaker than the Sub-8-Bit paper due to the transfer-learning-only limitation and the theoretical gap.

**Final Score:** 4.0 — slightly lower than the Sub-8-Bit paper due to the scope limitation and framing gap, but higher than Robust Training due to stronger experiments.

---

## Summary

This paper proposes a method for pushing fully quantized training (FQT) to 1-bit *on average*. The key ideas are (1) **Activation Gradient Pruning (AGP)** — a random pruning scheme that retains only 1/b of gradient groups (with probability proportional to their range) and quantizes the retained groups to b bits, yielding an average bitwidth of 1, and (2) **Sample Channel joint Quantization (SCQ)** — using per-sample quantization for activation gradient computation and per-channel quantization for weight gradient computation so both backpropagation paths can be accelerated. The paper also provides a theoretical analysis of Adam vs. SGD in FQT (showing Adam is less sensitive to gradient variance) and demonstrates speedups of up to 5.13× on real hardware. The method is evaluated on transfer learning tasks with 1-bit weights/activations, showing ~5% average accuracy drop compared to full-precision gradient training.

## Strengths

- **First demonstration of average-1-bit FQT with real hardware acceleration.** The paper achieves average 1-bit gradient precision on real devices (Hygon CPU, Raspberry Pi 5) with up to 5.13× speedup over FP32 PyTorch (Table 3). The "Average 1-bit vs. 1-bit" comparison (Table 5) shows that the decomposition overhead of average 1-bit over true 1-bit is small, validating the practical viability of the approach.

- **Novel combination of gradient pruning and per-group quantization (AGP).** AGP uses random masking (with probability proportional to range) to discard low-information gradient groups and reallocates the saved compute to increase the precision of retained groups. The design preserves unbiasedness via the correction factor m_i/p_i. Table 1 shows AGP with b=4 consistently outperforms 1-bit PSQ by ~6% average accuracy across six datasets and two architectures.

- **Theoretical analysis linking optimizer choice to gradient variance sensitivity.** Theorems 1 and 2 derive regret bounds showing SGD convergence scales as O(σ²) while Adam scales as O(σ) with gradient standard deviation σ. This explains the well-known empirical observation that Adam outperforms SGD at low bitwidths and provides principled motivation for variance reduction — a level of analysis missing in prior FQT work.

- **SCQ addresses a practical bottleneck.** Prior FQT schemes could not accelerate weight gradient computation because dequantization was needed before multiplication. SCQ uses per-channel quantization for weight gradients, enabling both gradient computations to use 1-bit matrix multiplication. This is a clean engineering contribution that directly enables the reported speedups.

- **Transferability beyond CNNs.** Results on Faster R-CNN (1.66% mAP drop), MLP-Mixer (3.52% drop), and BERT (8.39% degradation) demonstrate the approach is not restricted to convolutional architectures.

## Weaknesses

### Fatal
None.

### Major

- **Variance bound (Eq. 24) does not match the random masking algorithm.** The variance bound in Eq. (24) sums over the N/b groups with the largest ranges, implying deterministic selection. However, the actual AGP algorithm (line 227) uses random Bernoulli masks with probability proportional to range — this means small-range groups may be retained and large-range groups may be dropped, potentially increasing variance beyond the claimed bound. The paper does not derive a variance bound that accounts for the random masking or the correction factor m_i/p_i, creating a gap between theory and method. This weakens the claim that the theory "inspired" AGP.

- **Framing of "1-bit FQT" overstates what is achieved.** The title and abstract claim "1-bit FQT" and "pushing the limit to 1-bit," but the method achieves *average* 1-bit precision by retaining 1/b of groups at b-bit precision and decomposing those into binary slices. The paper acknowledges this distinction internally (Section "Average 1-bit vs. 1-bit") but the title and framing imply uniform 1-bit arithmetic, which could mislead readers. A title like "Average 1-Bit FQT" or "Effective 1-Bit FQT" would be more precise.

- **Limited to transfer learning.** The paper explicitly acknowledges (line 456) that 1-bit FQT from scratch remains an open problem — even 3-bit FQT from scratch is unsolved. This is a significant scope limitation: the method only applies to fine-tuning a pre-binarized model, which narrows the claimed "ultimate limit of FQT" framing substantially.

### Minor

- **Missing comparison with / discussion of 4-bit FQT.** The paper compares against 8-bit PSQ and 1-bit PSQ, but the current FQT frontier is 4-bit (Sun et al., Chmiel et al., Xi et al.). The paper says "there is no 4-bit format among the standard data types" (line 398), which is a practical limitation, but the paper would benefit from at least a conceptual discussion of what additional speedup is gained by going from 4-bit to average-1-bit and at what accuracy cost. Without this, readers cannot assess the practical trade-off.

- **Optimal hyperparameter b=4 is empirical without theoretical guidance.** The paper explores b ∈ {2, 4, 8} and finds b=4 is best (Table 1), explained qualitatively as a trade-off between variance reduction and information loss. A more principled approach (e.g., deriving the optimal b from the variance bound) would strengthen the contribution.

- **Theoretical analysis assumes convex losses.** The regret bounds (Theorems 1 and 2) adopt the standard online convex optimization framework. While this is common practice, the gap between convex assumptions and deep network training limits the direct applicability of the quantitative bounds. The qualitative insight (Adam < SGD sensitivity to variance) is useful but the theory does not explicitly model AGP's pruning mechanism.

### Trivial
None.

## Nice-to-Haves

- Ablation studies separating the contribution of AGP vs. SCQ. Currently the combined method is evaluated but individual contributions are not isolated.
- Convergence curves for more configurations (different b values, different architectures).
- Reporting absolute training times (seconds per iteration) alongside speedup ratios to aid reproducibility.
- Confidence intervals for speedup measurements (hardware benchmarks have run-to-run noise).

## Removed Points

These points are flagged to be removed; treat them with caution.

1. *"Speedup comparisons are misleading; Basic FP32 is a strawman."* — The paper clearly labels "Basic" as unoptimized FP32 and compares within the same optimization framework (Ours-Basic vs. Basic, SCQ-Basic, PSQ-Basic). This is a fair within-framework comparison. The paper also reports "Ours" (with additional optimizations) separately. The strong speedup claims (32–45× over 8-bit PSQ) explicitly compare unoptimized 1-bit against unoptimized 8-bit within the same framework, which is transparent.

2. *"The paper should provide optimized implementations for all baselines."* — This demands effort beyond the paper's stated scope ("Our implementation is not fully optimized, as the comprehensive hardware-algorithm co-design is beyond the scope," line 394). The paper is transparent about optimization levels.

3. *"The paper should discuss memory footprint or energy consumption."* — The paper focuses on speed, which is a valid single axis of evaluation. Energy/memory analysis would strengthen but is not required.

4. *"Doubling quantization overhead"* (critic's concern about PSQ for activation gradients AND PCQ for weight gradients quantizing the same tensor twice). — The paper clearly explains that PSQ is used for activation gradient computation and PCQ for weight gradient computation, which are different matrix multiplications involving the same gradient tensor but requiring different quantization axes for acceleration. This is by design, not an oversight.

5. *"Statistical significance for speedup numbers"* — Hardware benchmarks typically report mean over multiple runs; this is a nice-to-have.

6. Generic strengths from the Strength Finder about "addressing an important problem" — these lack specific evidence.

## Novel Insights

None beyond the paper's own contributions. The main novel observation from the reviews is that the variance bound (Eq. 24) implicitly assumes deterministic top-N/b selection rather than random masking, which is a technical gap the authors should address.

## Suggestions

1. **Reframe the title and contribution language** to "Average 1-bit FQT" or "Effective 1-bit FQT" to match what the method actually achieves.
2. **Derive a variance bound for the random masking case** (accounting for the Bernoulli masks and the m_i/p_i correction), or explicitly note that Eq. (24) applies to the expectation and explain why the bound still holds.
3. **Add a discussion of 4-bit FQT** to contextualize the practical trade-off between accuracy and speed.
4. **Consider ablating AGP and SCQ separately** to isolate the contribution of each component.
5. **Prominently state the transfer-learning-only limitation** earlier in the paper (abstract or introduction) to set expectations.

## Score and Decision

### Anchors Consulted

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| EfficientQAT (6Mdvq0bPyG) | 3.00 | R1 | Much weaker — limited novelty, unfair baselines |
| Angle-DFQ (orG37FHN4b) | 3.00 | R1 | Different topic (data-free PTQ), weaker |
| Sub-8-Bit Integer Training (wJ3GeGLFmc) | 4.50 | R1/R2 | Similar topic, stronger hardware eval but rejected; current paper is slightly weaker due to transfer-learning-only scope |
| Custom Gradient Estimators (3j72egd8q1) | 5.25 | R1/R2 | Stronger theoretical rigor but narrower scope (QAT only); current paper less rigorous theoretically |
| Robust Training at Arbitrary Precision (i880EAXJ2x) | 4.00 | R2 | Similar quality; current paper has clearer methodology and better experiments |
| FPTQ (ykhRO1mAg3) | 4.00 | R1/R2 | Different topic (LLM PTQ) |
| QAC for SNNs (D4sQzdMvcG) | 5.75 | R2 | Different topic; much higher score but on a different subject |

**Round 1 bracket:** 3.0 – 5.25  
**Round 2 narrowing:** The paper sits between the Sub-8-Bit Training (4.5, rejected) and Robust Training (4.0) papers. It is clearer and more novel than Robust Training but weaker than Sub-8-Bit due to the transfer-learning-only scope and the theoretical gap.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>