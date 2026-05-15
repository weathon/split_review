Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper proposes a hierarchical framework for explaining poisoned AI models by measuring "utilization" at three granularity levels (computation graph, subgraph, and tensor-state). Using models from the TrojAI Challenge, the authors analyze how clean and poisoned class encodings differ, identifying utilization ranges and tensor-state patterns that discriminate between the two. The key empirical finding is that, for a ResNet101 unit examined, clean and poisoned images produce largely disjoint tensor-state sets (only 35 overlapping values out of thousands).

## Strengths

- **Hierarchical framework operationalized at three granularity levels**: The paper concretely applies class encoding analysis at the graph level (Figure 4, utilization ranges distinguishing clean from poisoned models), subgraph level (Figure 5, pattern breaks between ResNet101 layers), and tensor-state level (Figures 6–7, visualization of disjoint feature sets). This multi-scale approach provides a structured way to localize where and how triggers affect model representations.

- **Empirical finding of disjoint tensor-state sets**: The paper quantifies that in layer1.2.conv2 of ResNet101, clean and poisoned images from the same traffic-sign class share only 35 high-frequency tensor-state values out of thousands (Section 4, Figure 7). This is a concrete, non-obvious observation that clean and poisoned classes occupy nearly orthogonal regions of representation space in the examined unit, supporting the feasibility of utilization-based analysis for detecting hidden triggers.

- **Extension to non-trivial architectures and datasets**: Unlike prior utilization/efficiency work (Schaub & Hotaling 2020; Bajcsy et al. 2021) that operated on small networks and 2D dot patterns, this paper works with ResNet18/ResNet101 and the TrojAI Challenge (Rounds 1–4) road-sign data with realistic triggers (polygons, Instagram filters). The computational benchmarks (24.46 minutes, 140.6 GB memory for ResNet101 with 286 probes and 2500 images) provide a practical reference.

- **Clear differentiation from related methods**: Section 2 explicitly distinguishes the approach from Network Dissection, Network 2 Vector, spectral clustering, and saliency-based methods, emphasizing the use of all computation units, binarization at zero, and analysis in tensor-state space rather than input space.

## Weaknesses

### Fatal
None.

### Major

- **The core utilization metric is not formally defined.** The paper provides a conceptual description ("ratio of the number of different outputs... over the maximum number of possible outputs," line 26) and mentions "entropy-based utilization" (Figure 5 caption) and "three deterministic and statistical AI model utilization metrics" (line 96), but it never gives a precise formula, algorithm, or pseudocode for any utilization metric. Without a formal definition, the method cannot be reproduced, and the numerical utilization values reported (e.g., ranges [16.0, 18.0], [29.5, 31.5]) are unmoored from any explicit computation. The Summary claims the framework was "defined" (line 96), but the Methods section (Section 3) does not deliver that definition.

- **No quantitative evaluation of the claimed classification capability.** The paper states that utilization-based class encodings are useful for "classifying a large number of AI models as clean or poisoned" (lines 26, 68), yet the experimental section reports zero classification metrics — no accuracy, AUC, precision, recall, F1, ROC curves, or any detection statistic. The evaluation is entirely qualitative: visual inspection of color-coded graphs (Figures 4–5) and tensor-state masks (Figures 6–7). No baselines are compared (e.g., spectral signatures, activation clustering, Neural Cleanse). The paper therefore does not demonstrate its capability to actually classify models, which is one of its stated objectives.

- **Section 3 (Methods) is a placeholder rather than a substantive description of the proposed technique.** The section dedicates most of its text to describing the TrojAI dataset creation pipeline (Figure 2), while the actual method — how utilization is computed from tensor-states, how class encodings are aggregated, how subgraphs are identified — is covered in a single vague sentence ("Utilization measurements of class encodings are defined by introducing tensor-states measured at the output of each component," line 59). This is not a stand-alone method section; a reader cannot reconstruct the approach from it.

### Minor

- **Limited model scope for the claimed general patterns.** The graph-level analysis covers only 4 models (Table 2, Figure 4), and the subgraph/tensor-state analysis is demonstrated on one architecture (ResNet101) with one trigger type (Kelvin Instagram filter). While the overlap quantification (35 tensor-state values) is computed over 2500 images per condition, the paper does not evaluate across multiple architecture families, random seeds, or trigger types to establish generalizability. The paper acknowledges this ("The limitation of the current work is in visual analyses," line 96) but the gap between the broad claims (e.g., "poisoned AI models would have completely independent tensor-states") and the evidence remains substantial.

- **No ablation of the binarization threshold.** Tensor channel values are binarized at zero (line 13), but the paper provides no analysis of sensitivity to this choice. Since binarization directly determines what counts as a "tensor-state value," the threshold could significantly affect the utilization metric and the observed patterns.

### Trivial

None.

## Nice-to-Haves

- Reporting per-class and per-model variability across multiple training runs and random seeds would strengthen confidence that the observed utilization patterns are systematic rather than idiosyncratic.
- A formal definition of the utilization metric (with a formula) and the entropy-based variant used in Figure 5 would make the paper self-contained and reproducible.
- Quantitative detection experiments (e.g., accuracy of a simple threshold classifier based on the identified utilization ranges) would directly substantiate the claimed classification use case.

## Removed Points

These points are flagged to be removed; treat them with caution.

- The harsh critic's claim that the conceptual definition of utilization is "vacuous" because the maximum possible outputs for binarized tensors would be 2^(c×h×w). This is a mathematical observation about an edge case, but the paper uses utilization as an empirically computed statistic on actual data, not as a theoretical bound. The conceptual definition suffices for the qualitative pattern analysis presented. However, the core criticism (lack of precise formula) remains and is kept in Major weaknesses above.
- The strength finder's claim about "286 probes and 160 billion parameters" conflates two separate statements: the 286 probes are for ResNet101 (line 96), while the 160 billion parameters are cited from Trask et al. (line 30) as a general scale reference. The strength about scaling beyond toy models is valid but the specific number is misleading.
- The strength finder's generic framing about "addressing important problems" — this is too generic to retain as a specific strength. Dropped.

## Novel Insights

None beyond the paper's own contributions. The main empirical observation — that in a specific ResNet101 unit, clean and poisoned images produce nearly disjoint tensor-state sets (35 overlapping out of thousands) — is the paper's most striking finding. The hierarchical framing (graph → subgraph → node) provides a useful organizational lens, but it is the empirical result that gives the approach its plausibility.

## Suggestions

1. **Formalize the utilization metric.** Provide a precise formula (e.g., U = (number of unique binarized tensor-states observed) / (total number of possible states, or some normalization)), clarify what "entropy-based utilization" means, and specify how statistics are aggregated across images in a class. This is necessary for reproducibility.

2. **Add a quantitative detection experiment.** Use the identified utilization ranges or tensor-state overlap to classify held-out models as clean vs. poisoned, and report standard detection metrics (accuracy, AUC). Compare against at least one simple baseline (e.g., neuron coverage, activation clustering) to calibrate the difficulty of the task.

3. **Expand the model sample in the evaluation.** Show results across multiple architectures (at least 3–4 families), multiple trigger types, and multiple training seeds to demonstrate that the observed patterns are not artifacts of a single configuration.

4. **Restructure Section 3** to focus on the proposed method (how utilization is computed, how class encodings are formed, how subgraphs are identified) before discussing the dataset.

## Score and Decision

The paper presents a conceptually interesting hierarchical framework and a genuine empirical finding. However, two major issues prevent acceptance: (1) the core metric is never formally defined, making the method unreproducible, and (2) the paper claims classification capability but provides no quantitative evaluation. These gaps are structural and cannot be addressed by minor revisions. The paper would need a thorough rewrite with formal definitions and a proper experimental evaluation to be publishable at a competitive venue.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>