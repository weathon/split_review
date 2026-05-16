Now I have a thorough understanding of the paper and can verify all claims against the actual text. Let me construct the consolidated review.

## Summary

This paper proposes a hierarchical framework for explaining how clean and poisoned training data are encoded in AI models by measuring the diversity of binarized activation patterns (tensor-states) at each computation unit, and using those statistics to characterize class encodings at node, subgraph, and graph levels. The approach is demonstrated qualitatively on a small set of ResNet models from the TrojAI Challenge, with visual comparisons of utilization patterns between clean and backdoored models.

## Strengths

- **Multi-resolution explanation framework**: The paper defines and evaluates class encodings at three hierarchical levels (graph, subgraph, tensor-state/node), which goes beyond the single-level analyses common in prior work. Section 4 demonstrates this explicitly: Figure 4 shows graph-level utilization distributions, Figure 5 shows subgraph pattern changes (e.g., broken patterns between layer1.1 and layer1.2), and Figures 6–7 show node-level tensor-state comparisons.

- **Identification of specific discriminatory computation units**: The paper pinpoints concrete layers whose utilization values differ between clean and poisoned models — e.g., maxpool, conv1, bn1, ReLU show utilization in ranges [16.0, 18.0]∪[18.5, 19.0] only for poisoned models, and layer1.2.conv2/bn2 show values in [29.5, 31.5] (Section 4, paragraph 2). This provides localized, actionable diagnostic information.

- **Novel observation of tensor-state divergence despite perceptual similarity**: Figures 6–7 demonstrate that at the tensor-state level (layer1.2.conv2 of ResNet101), clean and poisoned images share only 35 high-frequency tensor-state values out of thousands, despite appearing perceptually similar. This is a genuinely interesting finding about how backdoor triggers alter internal representations even when the input images look nearly identical.

- **Application to non-trivial architectures**: The method is applied to ResNet101 with 286 probed computation nodes using 2500 images, and Section 5 reports concrete computational costs (avg. 24.46 min inference, up to 140.6 GB memory), demonstrating feasibility beyond toy models.

## Weaknesses

### Fatal

- **Core utilization metrics are not formally defined.** The Summary claims "We defined a mathematical framework for computing three deterministic and statistical AI model utilization metrics" (Section 5), but the Methods section (Section 3) contains no equations, no formal definitions of the three metrics, no algorithm for constructing class encodings or AI model fingerprints, and no specification of how "utilization" is computed. The only description is a conceptual statement: "utilization of any computation unit is related to a ratio of the number of different outputs... over the maximum number of possible outputs" (Section 1). The term "entropy-based utilization" appears in a figure caption (line 74) but is never defined. Without formal definitions, the paper's core methodological contribution cannot be assessed, verified, or reproduced. This is a fatal flaw that prevents the paper from being accepted as a methods contribution.

### Major

- **No quantitative validation of the central claim.** The paper's stated objective includes "to identify encoding patterns (motifs) that discriminate AI models without and with hidden classes" (Section 1), and the experiments are "motivated by evaluating our hierarchical utilization-based approach to classifying a large number of AI models" (Section 4). However, no classification experiment is performed — no accuracy, precision, recall, AUC, or detection rate is reported. All evidence is purely visual pattern observation for 4 models (Figure 4) and 2 replicates (Figure 5). While the observed pattern differences are suggestive, the paper does not demonstrate that utilization fingerprints can *reliably* separate clean from poisoned models in a quantitative sense.

- **Extremely limited experimental scope without statistical rigor.** The analysis is restricted to 4 models from one TrojAI round (Round 4), plus 2 replicate models of one architecture (ResNet101). No error bars, confidence intervals, or statistical significance tests are provided. The observation that specific utilization ranges are "present in the poisoned models but are missing in the clean model" (Section 4) is based on a single clean model. Without replication across more architectures, trigger types, and training conditions, there is no evidence that the observed patterns generalize.

### Minor

- **No comparison to any baseline method.** The Related Work section identifies several relevant approaches (network dissection, activation clustering, spectral methods, modular partitioning), but the paper never compares its utilization fingerprints against any of them — neither quantitatively (e.g., detection accuracy comparison) nor qualitatively (e.g., does the hierarchical explanation reveal insights other methods miss?). This makes it difficult to assess what the proposed approach adds over existing techniques.

- **The paper claims more than it delivers.** The phrase "three deterministic and statistical AI model utilization metrics" is only introduced in the Summary, after the Methods and Experiments sections where they should have been defined and used. The Introduction claims the approach supports "classifying a large number of AI models as clean or poisoned" (Section 1), but no classification is performed. The paper's own limitation statement ("visual analyses of subgraph patterns... is the topic of our future work") reinforces that the work is preliminary, yet the framing suggests completed contributions.

### Trivial

- The Methods section (Section 3) is inappropriately structured — it is labeled "METHODS" but contains only a description of dataset creation, with no methodological definitions. Readers expecting the method's formal specification will not find it there.

## Nice-to-Haves

- A simple classification experiment (e.g., nearest-centroid or threshold-based detector using the utilization fingerprints as features) would directly test the central claim and would substantially strengthen the paper without requiring a fundamentally different approach.
- A comparison against at least one existing backdoor detection method (e.g., activation clustering, spectral signatures, or neural cleansing) would help the reader understand what the utilization-based approach adds.
- Statistical tests (e.g., permutation tests comparing utilization distributions) would lend credibility to the visual pattern observations.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic's claim that "no classification experiment is actually performed" is kept (it is factually correct), but the critic's framing of it as a "structural issue" is accurate and is preserved under Major weaknesses above.**
- **Critic's complaint that the paper "does not identify any quantitative baseline" in Related Work** — This is a fair observation that is subsumed under Minor weaknesses as a missed opportunity to frame the contribution more sharply. Kept as Minor.
- **Strength Finder's claim of "scalability to complex, real-world architectures"** — This is somewhat generous: 140.6 GB memory for one model is not obviously "scalable." However, the basic feasibility data (24.46 min, 286 probes) is still a useful data point. Downgraded from supporting strength to a factual observation noted in Strengths (last bullet).

## Novel Insights

The most genuinely novel insight emerging from these reviews is that the paper's core problem — understanding *how* backdoor triggers alter internal model representations at multiple levels of the computation graph — is worthwhile and underexplored. The observation that clean and poisoned images produce almost entirely disjoint sets of high-frequency tensor-state values despite near-perceptual identity (Section 4, Figures 6–7) is the paper's most striking result and could motivate useful future work. However, this insight is the paper's own contribution; the reviews do not add novel observations beyond it.

## Suggestions

1. **Formally define the utilization metrics.** Provide equations for how utilization is computed at each node (e.g., normalized count of distinct binarized tensor-state values, or entropy of the distribution of tensor-states). Specify what the "three deterministic and statistical metrics" are and how they differ. Define the algorithm for constructing class encodings and AI model fingerprints. This is the single most important fix — without it, the contribution is unverifiable.

2. **Add a basic classification experiment.** Even a simple threshold-based detector or nearest-centroid classifier operating on utilization fingerprints across many TrojAI models would provide the quantitative validation the paper currently lacks and directly support the claim that the encodings can discriminate clean from poisoned models.

3. **Expand the experimental evaluation** to include more models, architectures, and trigger types from TrojAI Rounds 1–4 (since the paper claims to cover them). Report variability across replicates with error bars or effect sizes.

4. **Restructure the Methods section** to actually describe the method. Move the dataset creation description to an appendix or a separate subsection, and devote the main Methods content to the utilization framework, class encoding construction, fingerprint computation, and hierarchical analysis procedure.

## Score and Decision

MY FINAL SCORE: <pineapple>3.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>