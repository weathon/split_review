Now I have a complete picture of the paper. Let me write the consolidated review.

---

## Summary

This paper introduces a hierarchical approach to explaining poisoned AI models by measuring "utilization" — conceptually defined as the ratio of distinct tensor-state outputs over the maximum possible outputs at each computation unit. It analyzes clean vs. backdoored models from the TrojAI Challenge at three granularity levels: full computation graph, subgraph, and individual tensor-states. The paper presents qualitative evidence of discriminative utilization patterns (specific value ranges appearing only in poisoned models) and tensor-state analyses showing near-zero feature overlap between clean and poisoned images for a class with an Instagram-filter trigger.

## Strengths

- **Identification of specific, concrete utilization ranges that discriminate clean from poisoned models**: The experiments pinpoint precise utilization value ranges ([16.0,18.0] ∪ [18.5,19.0] and [29.5,31.5]) that appear in poisoned models but are absent in clean models, and map them to specific computation units (maxpool, conv1, bn1, ReLU, layer1.2.conv2, layer1.2.bn2). This provides an evidence-based, granular characterization of backdoor encoding. (Section 4, lines 70–72)

- **Tensor-state analysis revealing nearly disjoint feature representations**: The paper shows that clean and poisoned images share only 35 overlapping high-frequency tensor-state values out of 2500 images each in layer1.2.conv2 (Figure 6 vs. Figure 7, lines 84–89). This quantitative finding offers a mechanistic explanation for how backdoor triggers create independent feature encodings despite perceptual similarity — a non-trivial observation about Trojan encoding in deep networks.

- **Clear differentiation from prior work on concept-based explainability**: The paper explicitly contrasts its approach with Network Dissection (Bau et al.), concept whitening (Chen et al.), and saliency methods (Selvaraju et al.), noting that its binarization-at-zero rule, use of all computation units (not just convolutional layers), and absence of inserted modules are distinctive design choices (Section 2, lines 47–49). This positioning is specific and well-articulated.

- **Demonstrated scalability to large architectures**: The paper reports computational benchmarks on ResNet101 with 286 probes and 2500 images (24.46 minutes, 140.6 GB), showing the method is feasible for architectures beyond toy models (Section 5, line 96).

## Weaknesses

### Fatal

None.

### Major

- **Core method (utilization) is not formally defined, undermining reproducibility**. The paper gives a *conceptual* description of utilization ("ratio of the number of different outputs over the maximum number of possible outputs" — line 26) and states that tensor channel values are binarized at zero (line 13), but Section 3 ("METHODS") — which opens by promising a definition — immediately pivots to describing training dataset creation (lines 59–61). No algorithmic specification, mathematical formula, step-by-step procedure, or worked example is provided. The term "entropy-based utilization" appears in Figure 5's caption without any derivation (line 74). A reader cannot determine exactly what computation is performed at each graph node, how "class encodings" or "AI model fingerprints" are numerically constructed, or how the color coding in figures maps to the formulation. Since the paper's stated contributions include "definition, measurement design" (line 36), omitting this definition means the paper's central technical artifact is unavailable for scrutiny, reproduction, or extension. This is the most significant weakness.

- **No quantitative evaluation of detection capability despite claiming it**. The paper states that utilization-based class encodings are useful for "classifying a large number of AI models as clean or poisoned" (line 26) and that experiments evaluate this approach (line 68). Yet no detection accuracy, AUC, precision/recall, F1-score, or any other quantitative metric is reported. The evidence is purely qualitative: visual inspection of color-coded graphs and side-by-side tensor-state images. No baseline comparison is provided (e.g., Activation Clustering, Neural Cleanse, Spectral Signatures, or any published result from the TrojAI Challenge). Without quantitative validation, the central claim about classification utility is unsubstantiated. The qualitative observations are interesting but do not on their own demonstrate a working detection method.

- **Experimental scope is too narrow to support the paper's generalizations**. The deep tensor-state analysis (Figures 6 and 7) is anchored to a single class (c=25) with a single trigger type (Kelvin Instagram filter) on a single architecture (ResNet101). The graph-level analysis covers only four models from Round 4 (line 70). The paper draws conclusions about "completely independent tensor-states for clean versus poisoned traffic sign images" (line 96) from this narrow foundation, without characterizing variance across classes, trigger types (only two discussed: polygon and Instagram filter), architectures (ResNet18 mentioned in Figure 1 but not analyzed comparably), or poison rates. The reader cannot assess whether the observed patterns are robust and general or specific to the particular configuration examined.

- **Claim-practice gap in the Summary**. Section 5 states that the paper "defined a mathematical framework for computing three deterministic and statistical AI model utilization metrics" (line 96). No such framework or three metrics appear in the visible text. The Summary overstates what was actually delivered.

### Minor

- **"Entropy-based utilization" appears without definition or derivation**. Figure 5's legend references "entropy-based utilization" (line 74), but the paper never introduces or derives an entropy-based formulation. This leaves the reader unsure whether the color coding in Figure 5 corresponds to the same metric described conceptually in Section 1 or a different computation.

- **Limited rationale for model selection in the experiment**. The paper analyzes "four trained models in Round 4 holdout dataset" (line 70) without explaining how or why these particular models were chosen from the larger TrojAI pool. The description of the TrojAI datasets (number of models per round, trigger types, poison rates, architectures) is scattered and incomplete, making it hard to assess the breadth of the evaluation.

### Trivial

None.

## Nice-to-Haves

- A formal algorithmic definition (pseudocode or equations) for utilization computation, including: (1) the binarization rule for tensor channels at zero, (2) per-image tensor-state extraction, (3) aggregation over training images in a class (count of unique states, or ratio), and (4) any entropy normalization applied. A brief worked example on a small toy network would greatly aid reproducibility.
- Quantitative detection results on the TrojAI holdout set (e.g., threshold-based classifier on the identified utilization ranges, or a simple classifier on fingerprint vectors), reported as accuracy/AUC with confidence intervals.
- A systematic evaluation across multiple classes, trigger types (polygon, Kelvin, other filters), and architectures (ResNet18, ResNet101, and any others in the TrojAI dataset) to establish generalizability of the observed discrimination patterns.
- A comparison to at least one established backdoor detection baseline to contextualize what utilization adds.

## Removed Points

These points from the reviews were excluded for the following reasons:

- *"Related work does not clearly position the proposed utilization metric against existing explainability approaches"* — The paper explicitly contrasts with Network Dissection, concept whitening, saliency maps, and modular partitioning approaches, describing specific differences (binarization at zero, no inserted modules, all computation units, tensor-state space vs. input space analysis). The positioning is present and clear.
- *"No description of the number of runs, random seeds, data splits, or statistical significance"* — These are desirable but not standard for a primarily qualitative/visualization paper of this kind. The paper's main evidence is visual pattern analysis, not hypothesis testing.
- *"The paper references a tool ('Neural Network Calculator tool') that is not standard"* — The paper cites it as a tool used for efficiency simulations; its non-standardness is not a weakness unless the paper's claims depend on it being standard, which they do not.
- *"Table 2 is referenced but not shown"* — The parser strips tables; they exist in the original submission.
- *"The paper should include a limitations paragraph"* — The paper does include a limitation statement (line 96), though it is brief.

## Novel Insights

The reviews do not surface any genuinely novel insight beyond the paper's own content. The key observation — that backdoored class encodings produce nearly disjoint tensor-state sets in mid-network layers despite perceptual input similarity — is the paper's own contribution. However, one cross-review observation worth noting: the paper's combination of qualitative richness and quantitative incompleteness places it in an awkward epistemic position. The tensor-state visualizations are compelling evidence that *something* is different about how poisoned classes are encoded, but without a formalized metric or detection protocol, the work cannot move from "there is a difference" to "here is how to use that difference." The paper would be stronger if it explicitly acknowledged this gap and framed itself as a preliminary characterization rather than a deployed method.

## Suggestions

1. **Provide a complete algorithmic specification of utilization in Section 3**, including: (a) the exact formula (e.g., U_c(n) = |unique_tensor_states(n, D_c)| / max_possible, with any entropy variant defined separately), (b) the binarization rule for tensor channels at zero, (c) how tensor-states are aggregated across images in a class, and (d) how "class encoding" vectors and "AI model fingerprints" are constructed from per-node utilization values. This is the single highest-priority fix.

2. **Add a quantitative detection experiment**: Use the identified utilization ranges (e.g., [16.0,18.0] ∪ [18.5,19.0] and [29.5,31.5]) as features for a simple threshold-based or one-class classifier on a held-out set of TrojAI models. Report accuracy and AUC. Even a modest result would substantially strengthen the paper's central claim.

3. **Expand the evaluation to cover more classes, trigger types, and architectures** in the TrojAI dataset, or explicitly scope the paper's claims to the configuration studied and frame the results as initial evidence rather than validated generalization.

4. **Fix the claim-practice gap in the Summary**: Either remove the reference to "three deterministic and statistical AI model utilization metrics" or define them explicitly in Section 3.

5. **Define "entropy-based utilization"** wherever it first appears (likely in a figure caption) — either derive it or clarify whether it is the same as the utilization metric described conceptually.

## Score and Decision

The paper introduces an interesting conceptual framework and presents compelling qualitative evidence that utilization-based tensor-state analysis can reveal differences between clean and poisoned model encodings. The specific observations — utilization ranges [16.0,18.0] ∪ [18.5,19.0] and [29.5,31.5] that discriminate clean from poisoned models, and the near-zero tensor-state overlap (35/2500) between clean and poisoned images — are genuine empirical contributions.

However, the paper has two structural weaknesses that prevent it from being accepted in its current form. First, the core method is not formally defined: Section 3 ("METHODS") does not contain the method specification, and a reader cannot reproduce the approach. Second, there is no quantitative evaluation: the paper claims utility for classifying clean vs. poisoned models but provides no detection metrics, baselines, or held-out evaluation. The experimental scope (one class, one trigger type for deep analysis) is too narrow to support the paper's generalizations. These are not minor presentation issues; they affect whether the contribution can be evaluated and built upon.

The paper's ideas are worth pursuing, but the submission as it stands does not deliver a substantiated, reproducible contribution. I cannot recommend acceptance.

**MY FINAL SCORE: <pineapple>4.5</pineapple>**
**MY FINAL DECISION: <orange>Reject</orange>**