## Summary
This paper makes the first attempt at 1-bit Fully Quantized Training (FQT), pushing the precision frontier from the prior 4-bit state of the art down to 1-bit for weights, activations, and gradients. The authors provide theoretical regret bounds linking FQT convergence to gradient variance (showing Adam is less sensitive than SGD), then propose Activation Gradient Pruning (AGP) — a stochastic pruning method that discards low-information gradient groups and reallocates bits to informative ones — and Sample Channel joint Quantization (SCQ), a hybrid quantization strategy that enables practical acceleration of both activation and weight gradient computations. Experiments on transfer learning (fine-tuning pretrained binary models) across six vision datasets, object detection, MLP-Mixer, and BERT show that 1-bit FQT converges with roughly 5% average accuracy drop compared to full-precision gradient training, with up to 5.13× speedup on CPU hardware.

## Strengths
1. **First demonstration of 1-bit FQT with convergence.** The paper provides the first successful evidence (Table 1) that FQT at 1-bit precision for weights, activations, and gradients can converge with acceptable accuracy (~5% average drop vs. QAT with 32-bit gradients on VGGNet-16 and ResNet-18 across six datasets). This pushes beyond the prior 4-bit frontier that had stood as the state of the art.

2. **Theoretical analysis linking optimizer choice to gradient variance.** Theorems 3.1 and 3.2 (Section 4) derive regret bounds showing SGD's convergence scales as \(O(\sigma^2)\) while Adam's scales as \(O(\sigma)\) in the presence of gradient variance. This provides a principled explanation for the empirical observation that Adam is more suitable for low-bitwidth FQT, and directly motivates the variance-reduction design of AGP. The theory is supported by Figure 3, which shows SGD diverging with PSQ but converging (with reduced accuracy) under the proposed method.

3. **Activation Gradient Pruning (AGP) with provable variance reduction.** The paper introduces a stochastic pruning strategy that reduces quantizer variance from \(\frac{D^{(l)}}{4}\sum_{i=1}^N R_i^2\) (1-bit PSQ) to \(\frac{D^{(l)}}{4B^2}\sum_{i=1}^{N/b} R_i^2\) (Eq. 24), and validates empirically (Figure 11) that the proposed quantizer achieves lower variance than PSQ across all tested datasets.

4. **SCQ enables practical acceleration of both gradient types.** The hybrid quantization strategy (per-sample for activation gradients, per-channel for weight gradients) resolves a key bottleneck in prior FQT where weight gradient computation could not be accelerated via 1-bit matrix multiplication. This is a concrete algorithmic contribution that directly enables the reported speedups.

5. **Demonstrated generalization across multiple architectures and tasks.** Beyond vision CNNs, Table 2 shows results on object detection (Faster R-CNN, 1.66% mAP drop), MLP-Mixer (3.52% accuracy drop), and BERT (8.39% degradation on GLUE), indicating the method transfers beyond the primary convolutional setup.

## Weaknesses
### Fatal
None.

### Major

1. **Missing ablation study isolating AGP and SCQ.** The paper compares the full method (AGP + SCQ) against PSQ, but does not provide ablations that disentangle the individual contributions. To attribute gains to AGP versus SCQ, the experiments should include: (i) PSQ alone at 1-bit, (ii) PSQ + AGP without SCQ, (iii) PSQ + SCQ without AGP, (iv) the full method. Without this, it is unclear whether accuracy improvements come primarily from variance reduction (AGP) or from the different quantization strategy (SCQ), and whether the speedup is driven by SCQ, AGP's sparsity, or both. This is the most significant experimental gap.

2. **No comparison to 4-bit FQT methods.** The paper repeatedly positions 4-bit FQT (Sun et al. 2020, Chmiel et al. 2021, Xi et al. 2023) as the current frontier and frames its contribution as pushing beyond that limit, yet no 4-bit FQT baseline is included. The paper states "there is no 4-bit format among the standard data types" (line 398) as justification, but a software implementation of 4-bit quantization (matching the approach of cited prior works) is feasible and standard in this literature. Without this comparison, the reader cannot assess the actual accuracy-efficiency trade-off of moving from 4-bit to 1-bit. The comparison to 8-bit PSQ confirms that 1-bit is worse than 8-bit (as expected), but the relevant comparison for the "pushing the limit" narrative is against the claimed 4-bit frontier.

### Minor

3. **Evaluation limited to transfer learning; scope broader than demonstrated.** The paper tests only on fine-tuning pretrained binary models on downstream datasets. The title, "Pushing the Limit of Fully Quantized Training to 1-bit," and the general framing in the abstract ("we make a first attempt to 1-bit FQT") imply broader applicability, but training from scratch — the harder and more practically important scenario — is not attempted. The paper does honestly acknowledge this limitation (Section 7, line 456) and the experimental section explicitly says "We evaluate our approach on transfer learning tasks" (line 273), which is commendable. However, the mismatch between the title's generality and the demonstrated scope is worth noting.

4. **Speedup measured against unoptimized baselines.** The reported speedups (up to 5.13×) compare the proposed implementation against naive FP32 PyTorch without optimization flags or library-level tuning (e.g., MKL). The paper acknowledges this ("Our implementation is not fully optimized," line 394), and the "-Basic" rows in Table 3 make the unoptimized nature transparent. However, the headline speedup numbers would be substantially reduced against an optimized FP32 baseline. The paper would benefit from reporting theoretical compute (e.g., binary operation counts) alongside wall-clock time to provide implementation-independent efficiency evidence.

5. **Per-task NLP results not reported.** Table 2 reports only a single average GLUE score (54.81 vs. 63.20 for QAT, an 8.39% degradation). Without per-task breakdown (e.g., MRPC, SST-2, QNLI, RTE), the reader cannot assess whether the method works uniformly across tasks or collapses on specific subsets. Given the 8.39% average drop is the largest degradation among all tested tasks, more granular reporting is warranted.

6. **Flowers anomaly underexplained.** On ResNet-18 with Flowers, the 1-bit method (b=4) achieves 79.28% vs. QAT at 78.85% — outperforming the full-precision gradient baseline. The paper attributes this to lower variance on Flowers (Figure 11), which is plausible, but a more detailed discussion of when and why quantization can act as a beneficial regularizer would strengthen the paper.

### Trivial

7. **The constant-factor comparison in the asymptotic analysis is incomplete.** The regret bounds show Adam as \(O(\sigma)\) vs. SGD as \(O(\sigma^2)\), but the Adam bound includes terms scaling with \(D^2 d / (2\alpha(1-\beta_1))\) and other constants that differ substantially from SGD's \(\alpha d/2\). The asymptotic dominance of Adam is directionally correct, but the "straightforward" comparison of constants (line 167) glosses over these differences.

## Suggestions
1. **Add a 4-bit FQT baseline** using the same PSQ framework (implement a software 4-bit PSQ quantizer). This single experiment would directly contextualize the 1-bit contribution against the claimed frontier and is the highest-impact addition.
2. **Run an ablation study** with four configurations: (a) 1-bit PSQ, (b) PSQ + AGP, (c) PSQ + SCQ, (d) PSQ + AGP + SCQ (the full method) on a fixed setting (e.g., ResNet-18 on CIFAR-10, b=4). Report both accuracy and wall-clock time to disentangle the contributions.
3. **Report per-task GLUE scores** (at least SST-2, MRPC, QNLI, RTE, CoLA) instead of or in addition to the average, to allow fine-grained assessment of NLP applicability.
4. **Include a theoretical compute analysis** — count the number of binary operations (XNOR + popcount) vs. FP32 multiply-adds — to provide an implementation-independent efficiency perspective alongside the wall-clock measurements.
5. **Add a brief discussion of the Flowers anomaly** (why 1-bit FQT can match or exceed full-precision gradient training on this dataset) in a future version.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept
