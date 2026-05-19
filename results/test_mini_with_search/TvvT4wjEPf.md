Now I have a solid understanding of the paper and the calibration anchors. Let me write the consolidated review.

## Summary

This paper addresses the overflow problem that arises when evaluating large RNNs under the CGGI fully homomorphic encryption scheme with single-ciphertext quantization. The authors propose Overflow-Aware Activity Regularization (OAR), a training-time regularization technique that penalizes pre-activations lying in "incorrect" overflow regions of the modulus domain, encouraging them to shift into regions where the sign activation function yields correct results despite modulo wrap-around. On the encrypted MNIST benchmark, the method achieves 90.82% top-1 accuracy with 2.1s average latency for a 1.9M-parameter multi-layer RNN — representing a significant latency improvement over prior FHE-based RNN work, while recovering the accuracy lost to overflow.

## Strengths

1. **Novel regularization (OAR) demonstrably mitigates overflow and recovers accuracy in low-bit regimes.** Table 1 shows that with OAR, 5-bit models improve from 21.47% to 92.59% top-1 accuracy (+71% relative) and 6-bit models from 64.92% to 93.12% (+43% relative). This directly validates that OAR shifts pre-activations out of incorrect overflow regions, as also confirmed by the distribution histograms in Figure 4.

2. **State-of-the-art encrypted RNN latency with competitive accuracy.** Table 3 reports 2.1s average latency and 90.82% encrypted accuracy (0.17% from plaintext) for a 1.9M-parameter multi-layer RNN — the largest non-interactive FHE-based RNN demonstrated to date, with over two orders of magnitude latency improvement versus prior FHE RNN work (SHE).

3. **Systematic ablation across bit-widths and regularization rates.** Tables 1 and 2 explore bit-widths from 5 to 8 and regularization rates from 10⁻⁵ to 10⁻³, cleanly identifying where OAR is critical (5- and 6-bit) and where it is unnecessary (7- and 8-bit). This provides practical guidance for when the technique is needed.

4. **Validation on a substantially larger RNN (128 timesteps, 8.48M parameters).** Section 4.1.4 demonstrates 92.69% test accuracy on upscaled 128×128 MNIST inputs, confirming that OAR scales to longer sequences and larger models. Critically, the paper reports the model "does not train without using both OAR and ModSign," establishing necessity.

5. **Clear visual evidence of the mechanism.** Figure 4 presents histograms of pre-activation distributions for 5-bit and 6-bit models, showing concentration in correct overflow regions versus minimal mass in incorrect regions, directly supporting the claimed mechanism.

## Weaknesses

### Major

- **Single-dataset evaluation (MNIST only).** All encrypted experiments are on MNIST handwritten digit classification (28×28 or 128×128). While the paper shows that OAR solves the overflow problem on this task, the claim of advancing "practical large-scale privacy-preserving RNNs" is not supported by evidence on any other domain where RNNs are commonly used (e.g., speech recognition, language modeling, time-series forecasting). The paper's central comparison to SHE is further weakened because SHE evaluates on Penn Treebank (a language task), making cross-system comparisons even harder to interpret. Results on at least one additional dataset or task would substantially strengthen the generality claims.

- **Unfair comparison headline (274× latency vs. SHE).** The claimed 274× latency improvement over SHE (Lou & Jiang, 2019) compares different architectures (single-layer 180K-param RNN vs. multi-layer 1.9M-param RNN), different datasets (Penn Treebank vs. MNIST), different metrics (perplexity/word-level accuracy vs. MNIST top-1), and different FHE schemes (SHE/HEAAN vs. CGGI). The paper presents this number without acknowledging these confounding factors. While the overall direction of improvement is clear, the headline factor is not an apples-to-apples comparison and should be presented with caveats or decomposed into scheme, quantization, and architectural contributions.

### Minor

- **No direct encrypted ablation without OAR.** Table 1 provides plaintext comparisons with and without OAR, and Section 4.1.4 states the model "does not train without using both OAR and ModSign." This makes a direct encrypted without-OAR baseline impossible, but it also means the paper cannot fully decouple whether OAR's benefit is purely from overflow correction during encrypted inference or from improved quantization-aware training stability in general. An encrypted comparison on a simpler model that does train without OAR (e.g., at 7- or 8-bit where Table 1 shows OAR is unnecessary) would help isolate the two effects.

- **Limited analysis of OAR's failure regime.** The paper notes that "Below 5-bit, both settings fail to surpass random accuracy levels, suggesting potential limitations of OAR in lower bit-widths" but does not investigate why. Understanding this boundary condition would strengthen the paper's contribution and provide practical guidance.

- **Enlarged model OAR metric of 70.57% is not explained.** Section 4.1.4 notes that the FF(1024) layer has only 70.57% OAR metric (meaning ~30% of pre-activations remain in incorrect regions), but the model still achieves 92.69% accuracy. The paper dismisses this as "complete correction may not be necessary" without analyzing why or under what conditions. This is a gap in understanding the method's behavior.

### Trivial

- The training hyperparameters (batch size, optimizer choice, temperature scale schedule details) are partially specified but could be more complete. The paper states a learning rate of 10⁻⁵, temperature scale s=4, and ternarization scale t=1.5, but optimizer choice (SGD vs. Adam) is not stated, and the 1000-epoch training budget is unusually large without justification.

## Nice-to-Haves

- **Worst-case error analysis.** Instead of averaging MAE/PD across the entire test set, showing per-sample histograms of activation errors or highlighting the fraction of samples where encrypted sign disagrees with plaintext sign would directly measure the phenomenon OAR is designed to fix.
- **A discussion of limitations and failure modes.** The paper does not discuss what happens when the OAR metric is low (<50%), how OAR interacts with activation functions beyond sign, or its applicability to gated RNN architectures like LSTMs or GRUs.

## Removed Points

- **Criticism about anonymous prior work (Point 2 from Harsh Critic).** The rule system requires removing any criticism that questions the existence or availability of cited references. The anonymous citation [Anonymous, 2025] is a reality of double-blind review, and the paper describes the quantization procedure sufficiently for the OAR contribution to be understood independently.
- **Criticism about unsubstantiated security parameter claims (Point 5).** The paper references Table 5 for parameter sets and states λ ≥ 128. Parameter sets from established FHE libraries like Concrete-Core follow standard security estimators. Weaknesses about missing appendix content are removed per the rules.
- **Criticism that plaintext ablation is insufficient because "FHE noise introduces additional errors beyond overflow."** The encrypted results (Table 3) show only a 0.17% accuracy drop between plaintext and encrypted with OAR, directly demonstrating that FHE noise is well-controlled by the chosen parameters. The plaintext ablation for overflow correction is the appropriate methodological design.
- **Strength Finder claims about the paper being the "first practical large-scale encrypted RNN."** While kept as a strength, this is calibrated: the paper does demonstrate the largest and fastest FHE-based RNN to date, which is a genuine contribution.
- **Generic strengths about the problem being "important" or "timely."** These are too generic to retain as specific strengths and were removed from the strengths list.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the core tension well: the paper has a genuinely clever and novel regularization technique with compelling evidence on MNIST, but the single-dataset evaluation leaves the generality claims unsubstantiated.

## Suggestions

1. **Add at least one non-MNIST evaluation.** Even a smaller-scale experiment on a language modeling task (e.g., a character-level Penn Treebank model or a simple sentiment analysis task) would dramatically improve the paper's external validity. The fact that prior work (SHE) uses Penn Treebank makes this particularly natural.
2. **Restructure the SHE comparison.** Present the 274× number with explicit caveats about architectural, dataset, and scheme differences, or decompose the gains into quantization-driven, scheme-driven, and architecture-driven components.
3. **Add a histogram of per-sample encrypted activation errors** to directly visualize the effect OAR has on preventing catastrophic sign flips during encrypted inference.
4. **Document the optimizer and full training configuration** (batch size, learning rate schedule, optimizer type) to improve reproducibility.

## Score and Decision

**Bracketing (Round 1):** Anchors at the low end (2–3) like DESIGN (3.0) — clearly worse than this paper. Middle anchors (4–5.5) like the Privacy-Preserving ResNet paper (4.5), HeLutNet (4.5), and ULD-Net (5.0) — this paper is comparable. High anchors (8+) are on unrelated topics.

**Narrowing (Round 2):** Compared to Privacy-Preserving ResNet (4.5, Reject): that paper evaluated on CIFAR-10/100 (multiple datasets) with solid theory but was criticized for narrow scope. The current paper has a more novel core contribution (OAR rather than polynomial approximations + structural optimizations) but weaker evaluation breadth (MNIST only). Compared to HeLutNet (4.5, Reject): evaluated on 20 datasets but used very simple LUT models. The current paper has a deeper architecture and more meaningful contribution but narrower evaluation. Compared to ULD-Net (5.0, Accept): that paper scales to ImageNet and ViT, a much stronger evaluation. The current paper does not match that breadth.

The paper's core contribution (OAR) is novel and cleanly motivated. The empirical evidence on MNIST is strong and the latency results are impressive. However, the single-dataset evaluation is a meaningful limitation that prevents higher scores, and the SHE comparison is inflated. This puts the paper in the 4–5 range — slightly above the Rejected PPML papers at 4.5 (which had broader evaluation) but below clearly Acceptable papers like ULD-Net at 5.0 (which demonstrated ImageNet-scale results).

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>