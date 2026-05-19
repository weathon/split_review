Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me organize my thoughts and produce the final review.

---

The paper proposes RAOQ, a QAT framework for mitigating ADC quantization in analog IMC. It contains three techniques: A-shift (converting unsigned activations to signed to maximize second moment), W-reshape (kurtosis regularization on quantized weights to increase weight variance), and BitAug (training with multiple ADC precision branches). The paper evaluates on ImageNet, COCO, SQuAD across diverse architectures and shows strong results.

Strengths verified from the paper:
1. **Principled analysis (Section 3, Figures 2c-2d)**: The paper empirically shows the proportional relationship between Var[Y] and E[X²]/Var[W], providing a rationale for manipulating activation/weight statistics to improve ADC SQNR. This grounds the techniques in an explicit analysis rather than heuristic.

2. **A-shift is simple, effective, and inference-cost-free (Section 4.1)**: The unsigned-to-signed conversion increases the second moment ~15× (3.89 → 57.9) and improves ADC interval utilization by ~5×. The offset is precomputable with zero inference overhead.

3. **Strong empirical results across diverse tasks and architectures (Tables 1, 2)**: On ImageNet with 8-bit ADC, RAOQ achieves top-1 accuracy within 0.3% of the no-ADC baseline (ResNet50: 77.0% vs 77.2%), far outperforming conventional QAT (75.1%). On COCO and SQuAD, similar trends hold. On CIFAR-10, RAOQ outperforms prior IMC-specific methods (Jin et al. 2022, etc.) across multiple memory technologies.

4. **Generalizability demonstrated (Tables 1, 2)**: Results span CNNs (ResNet, MobileNet, EfficientNet), object detection (YOLOv5s), and NLP (BERT-base/large), and multiple memory configurations (SRAM, ReRAM).

5. **Ablation isolating each technique's contribution (Table 3)**: Shows that all three techniques (A-shift, W-reshape, BitAug) individually improve accuracy, with A-shift and BitAug having the largest impacts.

Now for weaknesses, applying strict filtering:

**Criticism 1 (kurtosis rationale)**: Let me verify from the paper. The paper says kurtosis "encourages the majority of W-bar to be concentrated in the tails of the distribution (Moors, 1986)" and shows 4× variance increase in Fig 3a. The harsh critic argues this reasoning is flawed because kurtosis is scale-invariant and doesn't directly increase variance.

Is this valid? The paper does not claim kurtosis *directly* increases variance - it uses kurtosis to reshape the distribution toward the tails *within the fixed quantization grid*, and empirically observes variance increases. The critic's technical point about scale-invariance is correct in isolation but misses the context: within a fixed quantization range (e.g., {-7,...,7} for 4-bit symmetric), concentrating mass at the extremes *does* increase variance. The paper could be clearer about this mechanism, but the criticism that the "rationale is flawed" and "claimed mechanism is not supported" is too strong given the empirical evidence in Fig 3a.

I'll keep this as a Minor weakness - the theoretical connection could be more rigorous, but the empirical support is solid.

**Criticism 2 (BitAug underspecified)**: Section 4.2 is truncated in the extracted text. The harsh critic read the full paper and found the description too vague. Since I can't verify section 4.2 content, I'll note this cautiously. However, since the critic is likely right that the section could use more detail (even in the full paper, it's just one subsection), I'll keep this as a Minor issue.

**Criticism 3 (weak baselines)**: The paper compares against conventional QAT (the same training pipeline without RAOQ) on all large-scale tasks, and against prior IMC-specific methods on CIFAR-10. This is reasonable. The paper also explains why prior methods haven't scaled. I'll remove this criticism.

**Criticism about hybrid system**: The paper transparently reports which layers are not mapped. This is not a weakness.

**Criticism about energy analysis**: The energy analysis is indeed based on modeled numbers from the literature, not from actual RAOQ hardware measurements. This is a limitation but is contextual/nice-to-have, not a core flaw.

Let me also evaluate the strength finder's claims:

- Strength 1: Verified from Section 3 and Figures 2c-2d. Keep.
- Strength 2: Verified. The paper does apply kurtosis to quantized weights (not FP) and shows empirical results. Keep.
- Strength 3: Verified. A-shift numbers are directly from the paper. Keep.
- Strength 4: BitAug's effectiveness is shown in Table 3 ablation. Keep.
- Strength 5: Verified from Table 1. Keep.
- Strength 6: Verified from Table 2. Keep.
- Strength 7: Verified from Section 6/Figure 5. Keep but note it's contextual.

Now let me write the final review.Now I have all the information I need. Let me produce the consolidated review, carefully verifying each criticism against the paper text.

## Summary

RAOQ proposes three techniques (A-shift, W-reshape via kurtosis regularization, and BitAug) to mitigate ADC quantization error in analog in-memory computing systems. The core idea is to reshape activation and weight statistics to improve the signal-to-quantization-noise ratio at the ADC input and to adapt models via multi-precision training. The paper evaluates across ImageNet classification, COCO detection, and SQuAD QA with multiple architectures, showing accuracy close to no-ADC baselines.

---

## Strengths

1. **Principled analysis linking ADC SQNR to weight/activation statistics (Section 3, Figs. 2c–2d).** The paper empirically establishes a proportional relationship between Var[Y] (ADC input variance) and the second moments of quantized activations E[$\overline{X}^2$] and weights E[$\overline{W}^2$]. This explicitly grounds the W-reshape and A-shift techniques in an analysis of the root cause of ADC quantization error, going beyond purely heuristic approaches.

2. **A-shift is simple, effective, and incurs zero inference overhead (Section 4.1, Eq. 4–5, Fig. 3a).** The unsigned-to-signed conversion increases the activation second moment by ~15× (from 3.89 to 57.9) and improves ADC interval utilization by ~5× (Fig. 3b). The offset $2^{b_x-1}\overline{w}_i$ is precomputable offline, adding no runtime cost — a practical advantage over activation scaling schemes that require per-layer calibration at inference.

3. **Strong and broad empirical results (Tables 1–3).** On ImageNet with 8-bit ADC, RAOQ recovers top-1 accuracy to within 0.3% of the no-ADC baseline (ResNet50: 77.0% vs. 77.2%), whereas conventional QAT shows a >2% drop (75.1%). This pattern holds across MobileNet, EfficientNet, YOLOv5s on COCO (mAP within 1% of no-ADC), and BERT-base/large on SQuAD (F1 within 0.5% at 8-bit ADC). On CIFAR-10, RAOQ outperforms prior IMC-specific methods (Jin et al. 2022, Sun et al. 2021, Wei et al. 2020) across multiple memory technologies and noise configurations (Table 2).

4. **Ablation isolating each technique's contribution (Table 3).** The ablation on BERT-base, MobileNetV2, and ResNet50 with 4b activations/weights and 8b ADC shows that each of A-shift, W-reshape, and BitAug contributes positively, with A-shift and BitAug having the largest individual impact. This provides clear evidence that all three components are functional.

5. **Generalizability across model scales and tasks.** The paper demonstrates results on image classification (ResNet18/50, MobileNetV2, EfficientNet-lite0), object detection (YOLOv5s), and NLP (BERT-base/large) — a breadth absent from prior IMC-aware QAT work, which was limited to CIFAR-10/100-scale tasks.

---

## Weaknesses

### Fatal
None.

### Major
None. The paper's central claims are supported by the experimental evidence.

### Minor

1. **Theoretical rationale for kurtosis regularization (W-reshape) is loosely argued and could be clarified (Section 4.1).** The paper motivates kurtosis by stating it "encourages the majority of $\overline{W}$ to be concentrated in the tails" (citing Moors, 1986), and then shows a 4× variance increase empirically (Fig. 3a). However, the connection between maximizing the *standardized* fourth moment (which is scale-invariant by construction) and increasing variance under a *fixed quantization grid* is not explicitly spelled out. A reader could reasonably ask why kurtosis is preferable to a direct variance penalty. The paper's claim would be strengthened by explaining that within the fixed quantization range, shifting mass to the extremes (high kurtosis) necessarily increases variance, and that kurtosis avoids the clipping that a naive variance penalty might cause by pushing values beyond the grid boundaries. As presented, the reasoning feels somewhat circular: the goal is to increase variance, kurtosis is used, and variance increases — but the causal chain is not fully articulated. The empirical result in Fig. 3a is convincing, but the theoretical framing needs tightening.

2. **BitAug method description is too brief for standalone reproducibility (Section 4.2, truncated in extraction).** The extracted paper does not contain the full Section 4.2. Based on the harsh critic's reading of the complete submission, the description amounts to "augment the network with multiple ADC bit precision branches and train them jointly" plus a mention of "column softmax in the output of the last ADC branch." No architectural details (how branches are attached, whether weights are shared, how losses are combined, how inference selects a precision) are provided in the main text. Given that BitAug shows substantial impact in the ablation (e.g., BERT-base F1 from 84.75 to 87.15, Table 3), the method should be clearly specifiable from the paper alone. *Note: Section 4.2 may have been present in the original submission but was truncated during PDF extraction; the criticism applies to what was described, not to an absent section.*

3. **Energy system analysis is qualitative and does not account for RAOQ-specific hardware overheads (Section 6, Fig. 5).** The energy efficiency analysis uses modeled ADC energy from the literature (Murmann; Lee et al. 2021a) and compares IMC to digital accelerators in terms of TOPS/W. While this provides useful context, it does not quantify any additional cost that RAOQ might introduce (e.g., the area/energy of supporting BitAug's multiple branches in hardware, or the overhead of the A-shift offset computation if implemented in the memory periphery). The analysis essentially shows the known ADC precision–energy trade-off and argues that RAOQ improves accuracy at the low-precision end, which is a qualitative claim. Quantitative energy-accuracy Pareto curves from actual RAOQ deployment would be stronger.

4. **Training cost of BitAug is not discussed.** The ablation shows that BitAug provides meaningful gains, but the paper never mentions the additional parameter count, memory footprint, or training time incurred by running multiple ADC-precision branches. For practitioners evaluating the method, this is relevant information.

### Trivial
None.

---

## Nice-to-Haves

- **BitAug rationale.** The paper does not explain *why* training with multiple ADC precisions helps adaptation to a *single* precision at inference. Is the mechanism analogous to stochastic depth, dropout, or a form of data augmentation in the precision dimension? A brief intuition would help readers understand when BitAug is likely to help.
- **Analysis of which layers are most affected by ADC quantization at low precision.** The results show small accuracy drops at 7-bit ADC, but there is no per-layer or per-operation breakdown. Such analysis could guide selective precision assignment.
- **Statistical variability.** The main results report single numbers without variance across runs. While single-run evaluation is common in this area, a note about observed run-to-run variation would improve confidence.

---

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Weak baselines — no comparison to prior IMC methods on large-scale tasks."** REMOVED. The paper compares against conventional QAT (same pipeline without RAOQ) on all large-scale tasks (Table 1), which is a strong and fair baseline. On CIFAR-10, it directly compares against prior IMC-specific methods (Jin et al. 2022, Sun et al. 2021, Wei et al. 2020) in Table 2. The paper explicitly notes that prior methods were demonstrated only on small datasets and their success has not transferred to larger tasks. Requiring reproduction of prior methods on ImageNet when those methods were never shown to work there goes beyond fair scope.

2. **"The reported accuracy reflects a hybrid system, not fully IMC-mapped."** REMOVED. The paper transparently reports which layers are excluded (depthwise convs at <7% of compute, BMM2 at <1.5%) and why. This is sound engineering judgment, not a flaw.

3. **"The analysis only considers first few layers"** and **"Analysis ignores correlation after training."** REMOVED. The paper explicitly acknowledges the independence assumption fails during training and positions the analysis as an empirical validation (Section 3: "Nonetheless, we postulate that a more narrow relationship holds..."). The limited-layer study is a tractable approximation, and the paper's claims are about the techniques' effectiveness, not a complete theoretical characterization.

4. **"Ablation only at 8b ADC."** REMOVED. A controlled ablation at a single precision setting is standard practice for isolating component contributions. The claim is not that the relative importance is invariant across all precisions.

5. **"No confidence intervals."** REMOVED. Single-run evaluation is standard practice for large-scale QAT benchmarks of this type. Requesting multi-run statistics is a methodological preference, not a standard requirement.

6. **"The paper claims state-of-the-art accuracy without evidence."** REMOVED. The evidence is directly in Tables 1 and 2: RAOQ consistently outperforms conventional QAT on large-scale tasks and prior IMC methods on CIFAR-10. The "SOTA" claim is bounded by the demonstrated comparisons and is reasonable.

7. **"First to demonstrate IMC for inference across various scales of models" is overstated.** REMOVED. The paper qualifies this with "to the best of our knowledge" and the claim is about approaches that *enable* IMC (via ADC quantization mitigation) across challenging tasks, not about demonstrating IMC hardware itself. In context, it is an appropriate statement of novelty.

---

## Novel Insights

None beyond the paper's own contributions. The two reviews generally agree on the paper's strengths and weaknesses, with the harsh critic overstating the severity of the kurtosis-rationale issue and the baseline criticism, while the strength finder accurately identifies the empirical breadth as the paper's core asset.

---

## Suggestions

1. **Strengthen the W-reshape rationale in Section 4.1.** Explicitly state that within a fixed quantization grid (e.g., $\{-2^{b_w-1}+1, \dots, 2^{b_w-1}-1\}$), maximizing kurtosis concentrates probability mass at the extreme grid values, which necessarily increases variance — and contrast this with a direct variance penalty, which would push values outside the grid and cause clipping. A brief toy example or a reference to the empirical kurtosis–variance correlation in Fig. 3a would suffice.

2. **Expand the BitAug description.** Provide details on branch architecture (do branches share weights up to the ADC quantization step?), loss composition (is the total loss a sum or weighted average across branches?), and inference behavior (is the best precision selected by validation performance, or is there a gating mechanism?). A diagram and pseudocode algorithm would be ideal.

3. **Add a brief discussion of training cost.** State the additional parameter count (if branches add parameters) or confirm that branches only differ in the ADC quantization step (no extra parameters). Report training time relative to conventional QAT.

---

## Score and Decision

The paper addresses a real and important problem (ADC quantization in analog IMC), proposes novel techniques grounded in an empirical analysis of SQNR, and demonstrates strong results across a broad range of tasks and architectures. The weaknesses are limited to presentation clarity (kurtosis rationale could be tighter, BitAug description could be more complete) and minor omissions (training cost, qualitative energy analysis). None of the verified weaknesses threaten the paper's core claims. The paper represents a solid contribution to the IMC literature.

**Score: 7.5**

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>