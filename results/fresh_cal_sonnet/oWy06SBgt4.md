Now let me run the bracketing calibration search.Now let me do a narrowing search within the 5-7 range:Now I have enough calibration data to write the final review. Let me synthesize.

---

## Summary

This paper makes the first attempt at 1-bit Fully Quantized Training (FQT), pushing beyond the current 4-bit frontier by simultaneously quantizing weights, activations, and gradients to an average of 1-bit precision. The authors provide convergence analyses for SGD and Adam under quantized gradients, show that Adam is more robust to the resulting gradient variance, and propose two algorithmic contributions: Activation Gradient Pruning (AGP), which prunes low-range gradient groups and reallocates bandwidth to higher-range ones, and Sample Channel joint Quantization (SCQ), which enables efficient 1-bit matrix multiplication for both weight and activation gradients. A hardware implementation demonstrates up to 5.13× speedup over FP32 PyTorch across vision transfer-learning tasks.

---

## Strengths

- **First 1-bit FQT with convergence guarantees:** The paper demonstrates that 1-bit FQT is achievable for transfer learning, a claim unambiguously supported by Table 1 (all configurations converge) and Fig. 3 (convergence curves). No prior work has achieved average 1-bit on all three tensors (W, A, G).

- **Adam vs. SGD theoretical analysis grounded in evidence:** Theorems 1 and 2 establish that SGD's regret grows as O(σ²) while Adam's grows as O(σ), predicting that SGD is more sensitive to gradient variance. This is directly confirmed in Fig. 3/1, where PSQ+SGD diverges entirely while PSQ+Adam converges, and the proposed method+SGD shows only a modest accuracy drop.

- **AGP variance reduction is concrete and empirically confirmed:** Equation (24) shows the variance bound is reduced from O(∑_{i=1}^{N} R_i²) under 1-bit PSQ to O(∑_{i=1}^{N/b} R_i²) under AGP, and Fig. 11 shows empirically that AGP quantizer variance is lower than PSQ across all six datasets. Table 1 shows AGP (all b values) consistently outperforms 1-bit PSQ on both architectures.

- **SCQ design is clearly motivated and practically necessary:** Section 5.3 correctly identifies why PSQ cannot accelerate weight gradient computation (the per-sample scale matrix must dequantize before binary multiplication), and SCQ's joint design (PSQ for activation gradients, PCQ for weight gradients) solves this at no theoretical cost to the unbiasedness argument.

- **"Average 1-bit vs. 1-bit" distinction is addressed:** Contrary to one reviewer's concern, the paper explicitly has a dedicated subsection and Table 5 comparing average 1-bit and 1-bit matrix multiplication runtime, showing minimal overhead, demonstrating this is a first-class concern the authors handle.

---

## Weaknesses

### Fatal
None.

### Major

- **Speedup comparison against unoptimized PSQ is methodologically asymmetric.** Section 6.2 claims "an average speedup of 32.28× and 45.28× over 8-bit PSQ on ResNet18 and VGG16." Inspecting Table 3, this is computed by dividing the authors' optimized 1-bit kernel speed (e.g., 3.74× for VGGNet-16) against PSQ-Basic (0.07×), which the paper itself labels as "unoptimized." Comparing an optimized kernel against an unoptimized baseline proves very little about the relative hardware efficiency of 1-bit vs. 8-bit arithmetic. The 5.13× figure over FP32 PyTorch (also unoptimized, but symmetrically so) is the only fair headline speedup result. The 32–45× claims should either be removed or replaced with a comparison against optimized 8-bit integer routines.

- **No ablation isolating AGP from SCQ.** In every experiment, "Ours" applies both AGP and SCQ simultaneously. The comparison to 1-bit PSQ therefore conflates two distinct contributions and cannot attribute accuracy or speedup gains to either component independently. A 2×2 ablation (AGP only, SCQ only, both, neither) on the main datasets would be straightforward and is necessary to assess the individual contribution of each component.

### Minor

- **BERT/GLUE results in Table 2 lack a 1-bit PSQ baseline.** Table 2 reports BERT QAT at 63.20 and Ours at 54.81 (8.39% gap), but unlike the vision experiments in Table 1, there is no 1-bit PSQ result for BERT. Without this, it is impossible to know whether AGP+SCQ provide any benefit over the simplest 1-bit baseline in the NLP setting. The claim that results "indicate the potential of our approach to transfer to other architectures and tasks" is undersubstantiated in this column.

- **γ is undefined in Theorem 2.** The regret bound contains the factor $(1-\gamma)^2$ in the denominator (alongside $\beta_1$, $\beta_2$, $\lambda$), but γ is never defined in the theorem statement or the surrounding text. This is a notation gap that prevents readers from directly applying the bound.

- **The large accuracy gap on Cars should be discussed more candidly.** Table 1 shows that for ResNet-18 on Cars, the best configuration (b=4) achieves 37.88% vs. QAT's 50.81%—a 12.93% absolute gap. Section 6.1 asserts the gap is "acceptable considering the benefits," but the evaluation reveals a clear dataset-dependence: near-lossless on Flowers/Pets (variance ≤1%), substantially degraded on Cars and CUB. A brief discussion of what makes certain datasets more or less amenable to 1-bit FQT would help practitioners understand when the method is appropriate.

- **Convexity assumption of the theoretical analysis is not acknowledged as a limitation.** The paper adopts the online convex optimization framework of Zinkevich (2003) and explicitly states "the loss function $\mathcal{L}$ is convex" without noting this is a strong assumption that does not hold for binary neural networks. A single sentence acknowledging this limitation in the theory section would suffice.

### Trivial

- The sensitivity of the b hyperparameter is reported across three values (b=2,4,8), but no plot of quantizer variance vs. b alongside accuracy vs. b is provided to give readers a principled rule for selecting b in new settings.

---

## Nice-to-Haves

- An ablation comparing range-proportional pruning (p_i ∝ R_i) against uniform random pruning (which is also unbiased) would confirm that the importance weighting is necessary, not merely that *any* reduction in the number of active groups reduces variance.
- A more detailed discussion of why b=4 is optimal across both architectures: theory predicts a bias-variance tradeoff, but a joint plot would let practitioners generalize more easily.
- Expanding the BERT experiment to include per-task GLUE breakdown and 1-bit PSQ comparison would elevate the NLP claim to the same rigor as the vision experiments.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"Average 1-bit" framing concern (Harsh Critic §1):** The critic argues the paper conflates "average 1-bit" with "1-bit" without making it a first-class distinction. In fact, the paper has a dedicated subsection "Average 1-bit vs. 1-bit" in Section 6.2 and Table 5 benchmarking the two modes. This criticism is explicitly addressed and should not appear as a weakness.

2. **Theory applied at wrong level of abstraction (Harsh Critic §3):** The critic argues the theory motivates variance reduction in general but not AGP specifically. However, the paper's stated purpose for the theory is motivational—showing that Adam's O(σ) scaling enables 1-bit FQT where SGD's O(σ²) cannot. Using convergence theory as motivation rather than algorithm derivation is standard in the FQT literature and not a flaw.

3. **Criticism of SGD result as unfair or inflated:** Not applicable—both PSQ+SGD and Ours+SGD are tested, the comparison is symmetric and favorable to the baseline.

4. **Reproductibility concerns about training logs/hyperparameters:** Removed per hard rules on trivial implementation details.

5. **Speedup "potential" claim of 100x+ (Ours-Basic vs Basic):** The paper explicitly frames this as "acceleration *potential*" for future hardware—it compares unoptimized FQT vs. unoptimized FP32 baseline—and is transparent about this framing. It is not a misleading claim.

---

## Novel Insights

The most genuinely novel observation surfaces from the combination of the Adam/SGD theoretical gap and the AGP design: the paper implicitly demonstrates that variance-adaptive pruning (retaining only the high-range groups) interacts synergistically with Adam's variance-insensitivity in a way that enables a regime (1-bit FQT) that was previously considered impossible. Specifically, AGP's O(∑_{top N/b} R_i²) variance bound is only meaningful when the R_i distribution is highly skewed—and Fig. 11 confirms this skew across all tested datasets. This suggests an implicit prerequisite: 1-bit FQT may be feasible only on tasks where gradient ranges are heterogeneous and skewed (transfer learning tasks), which aligns perfectly with the observed dataset-dependence (Flowers/Pets vs. Cars). The paper does not articulate this connection explicitly but it is the most informative take-away for practitioners.

---

## Suggestions

1. Replace or remove the "32–45× speedup over 8-bit PSQ" headline. Present Table 3 as a demonstration of *relative hardware efficiency across optimization levels*, and clearly state that the only apples-to-apples speedup is the 5.13× vs. FP32 PyTorch (both running unoptimized Python-wrapped kernels).
2. Add a 2×2 ablation table: AGP only, SCQ only, both, neither (= 1-bit PSQ) on at least CIFAR-10 and Cars for both architectures.
3. Define γ in Theorem 2 or reference the line where it is introduced.
4. Either add a 1-bit PSQ BERT baseline row in Table 2 or remove the NLP results from the main text and move to a discussion of future directions.
5. Add one sentence in the theory section acknowledging convexity as a simplifying assumption not expected to hold literally for binary networks.

---

## Score and Decision

**Calibration anchors retrieved:**

| Path | Avg Score | Round | Comparison to paper under review |
|------|-----------|-------|----------------------------------|
| `mJ8k81O5BF.md` (Data-free PTQ) | 3.00 | R1 | Much simpler contribution, no theory, no training |
| `orG37FHN4b.md` (Angle-DFQ) | 3.00 | R1 | Post-training quantization, far less novel |
| `6Mdvq0bPyG.md` (EfficientQAT) | 3.00 | R1 | Different regime, worse evidence quality |
| `wJ3GeGLFmc.md` (Sub-8-bit integer training) | 4.50 | R1 | Same family; paper under review is more novel and better theorized |
| `3j72egd8q1.md` (Custom gradient estimators as STE) | 5.25 | R1/R2 | Theory-only paper, no hardware; paper under review is broader |
| `oOwDQl8haC.md` (12-bit accumulators) | 5.75 | R1/R2 | Most comparable "first attempt at new bit-width with hardware"; similar quality |
| `lD9Kc22Wls.md` (Quantized optimistic dual averaging) | 5.50 | R2 | Different problem (distributed), comparable rigor |
| `TBJCtWTvXJ.md` (SoftSignSGD S3) | 6.20 | R2 | New optimizer with theory; weaker empirical scope than paper under review |
| `YaeZwhXJ4k.md` (BinaryDM) | 6.67 | R2 | Binary inference (not training); strong empirical |
| `wg1PCg3CUP.md` (Scaling laws for precision) | 8.00 | R1 | Far more comprehensive, scales to LLMs; clearly stronger |
| `MEbNz44926.md` (Flexible residual binarization) | 8.00 | R1 | Strong inference binarization; paper under review is more novel (training) but narrower |

**Round 1 bracket:** 5–7.

**Round 2 narrowing:** The paper under review is most comparable to `oOwDQl8haC.md` (5.75, first attempt at a new precision frontier with hardware impl.) and `TBJCtWTvXJ.md` (6.20, theory + empirical on optimizer design). Both are close. The paper under review has higher novelty than the accumulator paper (1-bit training vs. 12-bit accumulation) and a more concrete evaluation, but shares the flaw of undersubstantiated secondary claims. Against `TBJCtWTvXJ`, the paper under review has a hardware implementation and cleaner experimental setup, but the missing AGP/SCQ ablation is a genuine gap. The paper is slightly above `oOwDQl8haC.md` on novelty and slightly below `YaeZwhXJ4k.md` on experimental completeness. This places it at **6.0**, toward the lower end of "borderline accept."

The two major weaknesses (biased speedup comparison, missing component ablation) are real but not fatal—the core 1-bit FQT contribution and the 5.13× speedup vs. FP32 are solidly established. A minor revision to address these would not require new experiments of substance.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>