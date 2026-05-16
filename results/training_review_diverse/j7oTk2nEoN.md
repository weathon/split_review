I've now carefully verified all claims against the paper. Let me construct the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

This paper introduces Gray-box fine-tuning, a paradigm where the backbone model's weights and architecture remain hidden but gradient propagation is permitted through lightweight input/output adapters (DGA) or intermediate token injections (LGA). The method trains only ~0.4% of the backbone's parameters, preserving the model's inference pipeline intact. Evaluated across text-image retrieval, text-video retrieval, image classification, and sketch retrieval using CLIP, BLIP, and DINOv2 backbones, DGA achieves results competitive with white-box methods like LoRA on in-distribution and near-distribution retrieval tasks, though gaps widen on domain-shifted tasks (sketch).

## Strengths

- **Novel and well-motivated problem framing.** The paper identifies an underexplored middle ground between black-box (no gradient access, output-only adaptation) and white-box (full weight access) fine-tuning. Table 1 systematically characterizes the spectrum of information exposure across methods, and the DGA/LGA variants are clean operationalizations of this setting. This framing is a genuine contribution — it gives the community a new interface design point for model adaptation.

- **Competitive accuracy on retrieval tasks with minimal parameter overhead.** On text-to-image retrieval (COCO: R@1 gap 0.38 to LoRA; Flickr30K: gap 2.1) and text-to-video retrieval (MSR-VTT: R@1 gap <1.0), DGA performs within striking distance of LoRA while adding only ~0.4% of backbone parameters and using no nonlinearities or per-architecture customization. The ablation (Table 8) cleanly isolates that both input and output adapters contribute positively, and jointly optimizing them yields the best result.

- **Comprehensive breadth of evaluation.** The paper tests DGA/LGA across three backbones (CLIP, BLIP, DINOv2), five task types, and multiple datasets including COCO sub-domains, Stanford-Cars, MSR-VTT, VATEX, ImageNet (16-shot), ImageNet-Sketch, and Sketchy. The honest documentation of failure modes (e.g., sketch domains where white-box methods dominate, lines 199–200, 210–211) strengthens the paper by identifying the boundary conditions of the approach.

- **Principled ablation study.** Section 5 systematically decomposes DGA into individual components (visual input adapter, textual input adapter, output adapters), showing that each contributes positively and that the combination outperforms any subset. This grounds the design choices empirically rather than relying on intuition alone.

## Weaknesses

### Fatal
None.

### Major

1. **Structural mismatch between motivated challenges and evaluation.** The paper frames itself around three practical challenges: (i) duplication of deployment/storage, (ii) optimization for edge devices, and (iii) privacy, safety, and IP concerns (lines 12–15). The contributions are stated as "balancing effectiveness, proprietary protection, safety, and efficiency" (line 35). The method is described as offering "efficient, and more secure solutions" (line 23) and "minimizing the risks associated with full model exposure" (line 21). **Yet the evaluation (Section 4) measures only task accuracy — R@1, top-1 accuracy, precision@K.** There are zero experiments measuring: resistance to model theft or gradient-based reconstruction, training or inference latency/compute overhead, memory footprint during adaptation, or any privacy guarantee. The security and efficiency advantages claimed are inherent plausibilities of the setting, not demonstrated properties. This gap would need to be addressed either by adding at least one experiment (e.g., comparing inference pipeline complexity vs. LoRA, measuring resistance to a basic gradient-based attack, or reporting relative training time) or by reframing the contribution as purely about accuracy-competitive fine-tuning under restricted access and dropping the unevaluated privacy/security/efficiency claims from the abstract and contribution list.

### Minor

1. **Absence of a controlled gradient-enabled baseline.** The paper compares against LP (black-box, no gradient) and LoRA (white-box). It lacks a baseline that uses gradient propagation through the backbone with a simpler input transformation (e.g., a learned additive perturbation in pixel/token space end-to-end trained via backprop + a linear probe on the output). Such a baseline would isolate whether the specific convolutional/textual-token adapter design provides benefit beyond the mere fact of having gradient access. Without it, it is unclear whether DGA's improvements over LP come from the adapter architecture or simply from having any gradient-trainable input mapping.

2. **Abstract overclaims relative to full result range.** The abstract states that "Gray-box approaches achieve competitive performance with full-access fine-tuning methods" without qualification. Across the full evaluation, the degree of competitiveness varies substantially: competitive on retrieval tasks (0.4–2.1 points behind LoRA), moderately behind on classification (2.5–9.0 points behind LoRA on ImageNet/Sketch), and far behind on sketch-to-image retrieval (30+ points behind white-box methods). While the paper honestly discusses these gaps in the body (lines 199–200, 210–211, 234), the abstract's unqualified claim overstates the generality of the result.

3. **No variance reporting or statistical significance.** All results appear to come from single runs without standard deviations, confidence intervals, or repeated trials. This is particularly concerning for the Stanford-Cars result (Table 4), where DGA/LGA substantially outperform all white-box baselines — the paper's explanation ("low number of samples") is plausible but, without error bars, the reader cannot assess whether this is a reliable phenomenon or an artifact of a single run.

4. **Missing implementation details.** No learning rate, optimizer, batch size, training epochs, or convergence criteria are reported for any experiment. Parameter counts are given for DGA (~0.4%) but not for the LoRA or output-adapter baselines. Without these, the results are not independently reproducible.

5. **Top-2 claim in Table 3 is unverifiable from the text.** The statement that "DGA and LGA together achieve top-2 performance in 63.89% (23/36) of cases" (line 174) is presented as a summary claim. The table itself is an image, and the paper does not enumerate which 23 of 36 cases. This should be verifiable from the presented data.

6. **Visual adapter architecture underspecified.** The visual input adapter is described as "learned 2D convolutional layers" that form an "affine transformation" (line 84), but the paper does not specify the number of layers, kernel sizes, stride, padding, or how the dimensionality is matched to the backbone's expected input shape. This is a small but unnecessary gap in reproducibility.

### Trivial

- The visual adapter's lack of activation function is described as noteworthy, but without specifying the number of layers and kernel sizes, the reader cannot reason about the effective receptive field or parameter count.

## Nice-to-Haves

- A comparison against a gradient-enabled baseline with matched parameter count but different architecture (e.g., a learned additive perturbation + linear probe) would strengthen the claim that the specific adapter design matters.
- A discussion of when the approach fails — e.g., what is the minimum training set size for DGA to be useful, or what task properties make input-space adaptation fundamentally insufficient — would improve the limitations section.
- Reporting the relative training time or inference latency of DGA vs. LoRA would directly support the efficiency motivation (DGA preserves the inference pipeline intact, unlike LoRA's separate flow).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism about checkmark in Table 1 for DGA under "No structural info revealed":** The paper transparently states in line 21 that dimensionality is revealed (not architecture/weights). The checkmark is about architecture/weight information, and the paper is consistent. Removed as factually wrong.
- **Criticism that DGA "still needs to know the input and output dimensionalities":** The paper acknowledges this in line 21. Not a weakness — it's a stated feature of the setting. Removed.
- **Criticism that "FT is better than LoRA on COCO contradicts the common finding":** This is the reviewer's speculation, not a demonstrated flaw. The paper simply reports results. Removed.
- **Criticism about the shift-token design (why not per-token shifts):** Design choice honestly reported; the ablation shows it has minimal effect and the paper acknowledges this. Removed.
- **Criticism about the model-theft paragraph in Section 6 being generic:** The paragraph provides context about model theft risks; it's not claiming this is a novel contribution. The paper already notes (line 55) that weight theft from gradients is not currently practical. Removed as not a valid weakness.
- **Criticism that LGA/DGA fail to achieve top-2 in many cases of Table 3:** The paper's claim of 23/36 is specific; without being able to see the table image, this criticism cannot be verified. However, kept the related minor point about verifiability.

## Novel Insights

The reviews surface a genuine tension: the paper makes claims about privacy, security, and efficiency in its motivation that it never tests, and the abstract overstates how "competitive" the results are across the board. However, the reviewers converge on the core novelty being valid — the Gray-box setting is real and underexplored, the accuracy on retrieval tasks is legitimately close to white-box methods, and the honest documentation of failure on sketch domains is a useful boundary condition. The most actionable insight is that the paper would be significantly stronger if it either (a) added a single experiment on a claimed motivation (model theft resistance, inference latency) or (b) cleanly scoped its contribution to accuracy under restricted access and dropped the unevaluated claims.

None beyond the paper's own contributions.

## Suggestions

1. **Address the motivation-evaluation gap directly.** Either add a simple experiment demonstrating DGA's practical advantage on one of the claimed dimensions (e.g., measure inference latency vs. LoRA, test resistance to a basic gradient-based reconstruction attack following Horwitz et al. (2024), or report the storage overhead of maintaining separate LoRA weights vs. a single DGA backbone), or reframe the contribution as "accurate fine-tuning under gradient-only access" and remove the unsupported privacy/security/efficiency claims from the abstract and contribution list.
2. **Add a controlled gradient-enabled baseline:** Train a learned additive perturbation (e.g., a single learnable vector in pixel/token space) end-to-end via gradient propagation through the backbone, combined with a linear output probe. Compare its accuracy to DGA to isolate whether the specific adapter design matters or merely having gradient access.
3. **Report variance** (standard deviations over at least 3 runs) for key results, especially the surprising Stanford-Cars outperformance.
4. **Disclose all standard training hyperparameters** (learning rate, optimizer, batch size, epochs, any scheduler) and parameter counts for all baselines.
5. **Calibrate the abstract** to reflect the scope where DGA is competitive (in-distribution and near-distribution retrieval) and acknowledge the larger gaps on domain-shifted tasks.

## Score and Decision

The paper introduces a genuinely novel and timely problem setting (Gray-box fine-tuning with gradient-only access) and provides a reasonable initial architecture (DGA/LGA) with promising accuracy on retrieval tasks. The ablation study is well-structured, and the breadth of evaluation is commendable. However, the paper suffers from a significant mismatch: it motivates itself with privacy, security, and efficiency challenges, but evaluates only task accuracy, leaving its central motivational claims unsubstantiated. The abstract also overstates the generality of the results. These issues are addressable through targeted revisions — adding one experiment on a claimed motivation, a controlled gradient-enabled baseline, and recalibrated claims would substantially strengthen the contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>