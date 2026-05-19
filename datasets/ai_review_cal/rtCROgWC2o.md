- Decision: Reject
- Avg Score: 3.75
- Scores: 6, 3, 3, 3
I have thoroughly verified all claims against the paper. Here is the consolidated review.

---

## Summary

The paper proposes a hierarchical utilization-based framework for explaining how training data are encoded in AI computation graphs, applied to distinguishing clean from backdoor-poisoned models. The approach binarizes activations at zero to obtain "tensor-states," computes utilization statistics at each computation unit, and analyzes patterns at graph, subgraph, and node granularities. Experiments on TrojAI Challenge models (ResNet18/ResNet101) show identifiable utilization ranges and near-disjoint tensor-state sets that discriminate clean from poisoned models.

## Strengths

- **Hierarchical explanation across three granularity levels.** Section 4 presents evidence at the graph level (utilization ranges [16.0,18.0]∪[18.5,19.0] and [29.5,31.5] present only in poisoned ResNet18 models), at the subgraph level (the trigger breaking the pattern between layer1.1 and layer1.2 in ResNet101, Figure 5), and at the tensor-state level (only 35 overlapping high-frequency tensor-states out of thousands between clean and poisoned images in layer1.2.conv2, Figures 6–7). This multi-level evidence directly supports the paper's stated objective of explaining poisoned models at graph, subgraph, and node granularities.

- **Identification of specific computation units as poisoning fingerprints.** The paper pinpoints concrete units — maxpool, conv1, bn1, ReLU (range [16.0,18.0]∪[18.5,19.0]) and layer1.2.conv2, layer1.2.bn2 (range [29.5,31.5]) — that discriminate poisoned from clean models in ResNet18 (Section 4, Figure 4). This is more actionable than generic saliency or activation-based methods.

- **Post-hoc analysis without inserted modules or retraining.** Unlike concept whitening (Chen et al., 2020) or methods requiring architectural modifications, the proposed approach binarizes existing activations at zero and computes statistics directly from trained model outputs (Section 2). This reduces overhead and makes the analysis applicable to any trained computation graph.

- **Demonstrated feasibility on large-scale models.** The paper reports computational costs for ResNet101 (286 probes, 2,500 images): 24.46 minutes and up to 140.6 GB memory on an NVIDIA Titan RTX (Section 5). This demonstrates that the approach scales beyond toy models to architectures with millions of parameters.

## Weaknesses

### Fatal
None.

### Major

- **The core metric (utilization) is imprecisely defined and internally inconsistent.** The paper provides only a vague conceptual description: "utilization of any computation unit is related to a ratio of the number of different outputs (tensor-state values) activated by all training data points over the maximum number of possible outputs by the computation unit" (line 26). No equations, algorithms, or pseudo-code are given for computing utilization. Furthermore, the text in the introduction describes a ratio-based definition, while Figure 5's caption refers to "entropy-based utilization" ranging from 1% to 31% (line 74) — these are not the same concept, and the relationship between them is never explained. The paper claims "we defined a mathematical framework for computing three deterministic and statistical AI model utilization metrics" (line 96), but no such framework is presented in the paper. This makes the method neither reproducible nor fully evaluable as a technical contribution.

- **No quantitative evaluation of classification/detection performance.** The paper lists as objectives "classifying a large number of AI models as clean or poisoned" (line 26) and states that experiments are motivated by "evaluating our hierarchical utilization-based approach to classifying a large number of AI models" (line 68). However, zero classification accuracy, precision, recall, ROC curves, detection rate vs. false positive rate, or any other quantitative detection metric is reported. The results consist entirely of qualitative visual pattern descriptions for four models (Figure 4), two replicates (Figure 5), and two image pairs each (Figures 6–7). Without knowing false positive rates or detection accuracy, the claim that the method is useful for classifying clean vs. poisoned models is unsubstantiated.

- **No comparison to any existing method.** The paper positions itself within the explainable AI and backdoor defense literature, referencing network dissection, concept vectors, saliency methods, spectral clustering, and pruning-based defenses (Section 2). Yet it provides no experimental comparison — not even a simple baseline such as activation clustering, spectral signatures, or counting unique activations after a single layer. Without demonstrating that the proposed approach offers any advantage over existing techniques, the contribution remains hypothetical.

### Minor

- **Limited experimental scope.** The detailed results focus on a single trigger type (Kelvin Instagram filter) applied to one traffic sign class, with brief mention of polygon triggers. The TrojAI Challenge (Rounds 1–4) includes many trigger types (e.g., corner patches, patterns, stickers), architectures, and 17 sign classes — a comprehensive study across these variations is needed to assess generalizability. The paper evaluates 4 models for graph-level patterns and 2 replicate models for subgraph patterns, which is too small a sample to draw robust conclusions.

- **Central conclusion is too strong given the evidence.** The paper concludes that "a poisoned AI model would have completely independent tensor-states for clean versus poisoned traffic sign images" (line 96). This claim is based on one architecture (ResNet101), one trigger type (Kelvin Instagram filter), and one sign class, examined at one layer (layer1.2.conv2). The claim about "completely independent" tensor-states is not validated across different architectures, trigger types, or layers, and 35 overlapping tensor-states (reported in Figure 7) are themselves a counterexample to "completely independent."

### Trivial
None.

## Nice-to-Haves

- Include equations or algorithmic steps for the utilization metric(s), making the method reproducible.
- Evaluate quantitative detection accuracy over a substantial set of models (dozens to hundreds) from the TrojAI Challenge.
- Compare against at least one baseline method (e.g., spectral signatures, activation clustering) to contextualize the approach.
- Add an ablation study removing one hierarchical level at a time to demonstrate each level's independent contribution.
- Cover more trigger types (e.g., corner patches, stickers, pattern triggers) beyond Instagram filters and polygons.

## Removed Points

These points were flagged for removal from the inputs; they are reproduced here for completeness but should be treated with caution.

*From Harsh Critic:*
- The criticism that "the maximum number of possible outputs for a binarized tensor-state with dimensionality rows × columns is 2^(rows*columns), making the ratio infinitesimal for any realistic layer" — this is a speculative extrapolation of a definition that the paper itself calls "conceptual" and describes as "related to a ratio" (not a formal mathematical identity). The reviewer extrapolates a strict ratio interpretation onto an intentionally vague statement. The core problem (imprecise definition) is retained above; the specific mathematical extrapolation is removed as speculative.
- Section-by-section notes (Section 1, 3, 4, 5 observations) are folded into the weaknesses above and do not constitute independent criticisms.
- "Strengthening the Paper on Its Own Terms" suggestions are moved to Nice-to-Haves above.
- Comments about missing appendix content: The paper's appendix was stripped during parsing. Criticisms about missing proofs/appendix content are disregarded per policy.
- The claim that "reproducibility... code availability for the utilization measurement pipeline is not stated" — the paper references the "Neural Network Calculator" tool (Bajcsy et al., 2021) and indicates code/tools exist, which satisfies the bar for a published reference.

*From Strength Finder:*
- "Demonstrated scalability" is retained as a strength but the 140.6 GB memory cost is also noted as a practical limitation. No strengths were dropped as generic/superficial — all were adequately specific.

## Novel Insights

None beyond the paper's own contributions. The reviewers' comments do not surface any insight about the approach that is not already stated or implied in the paper itself.

## Suggestions

1. **Provide a precise, operational definition of the utilization metric.** At minimum, an equation or algorithm specifying how tensor-state binarization, counting, and normalization are performed. Clarify the relationship between the "ratio" definition in the introduction and the "entropy-based utilization" appearing in Figure 5's color legend.

2. **Report quantitative detection results.** The TrojAI Challenge provides labeled clean/poisoned models. Report classification accuracy, AUC, or detection rate vs. false positive rate over a substantial number of models. This directly validates the stated objective of classifying models as clean or poisoned.

3. **Add at least one baseline comparison.** Compare against a simple baseline (e.g., counting unique activations at a single layer, or spectral signatures from the backdoor defense literature) to demonstrate that the hierarchical utilization framework provides value beyond simpler alternatives.

4. **Broaden the experimental scope.** Show results across multiple trigger types, architectures, and sign classes from the TrojAI challenge to support claims of generalizability.

5. **Tone down the conclusion.** Replace "completely independent tensor-states" with a more measured claim (e.g., "substantially different" or "largely disjoint") given the limited evidence base.
