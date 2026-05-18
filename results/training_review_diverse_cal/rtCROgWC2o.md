Now I have all the evidence I need. Let me produce the final consolidated review.

## Summary

This paper introduces a hierarchical approach to explaining poisoned AI models based on "utilization" measurements at graph, subgraph, and tensor-state (node) granularity levels. The core idea is to binarize activations at zero and compute the ratio of observed tensor-states to possible tensor-states at each computation unit, producing utilization-based "class encodings" and "AI model fingerprints." The paper illustrates this approach on ResNet18/101 models from the TrojAI Challenge (Rounds 1–4) by comparing clean and poisoned class encodings.

## Strengths

- **Novel concept and framing**: The idea of "utilization" as a ratio of observed to possible tensor-states — binarizing activations at zero and computing statistics over class activations — is a clean departure from threshold-based approaches (Fong & Vedaldi 2018, Bau et al. 2017) and does not require inserted modules like concept whitening. The hierarchical framing (graph → subgraph → node) provides a natural multi-granularity lens for analysis.

- **Multi-level evidence of encoding differences**: The paper traces utilization differences between clean and poisoned models from the graph level (Figure 4 shows distinct utilization ranges [16.0, 18.0]∪[18.5, 19.0] and [29.5, 31.5] present only in poisoned models) down to specific computation units (maxpool, conv1, bn1, ReLU, layer1.2.conv2, layer1.2.bn2) and to individual tensor-state visualizations (Figures 6–7 show near-zero overlap between clean and poisoned tensor-states in layer1.2.conv2 for the Kelvin filter trigger). This multi-level tracing is a genuine methodological contribution.

- **Scalability demonstration on realistic models**: The paper benchmarks the approach on ResNet101 (286 probes, 2500 images) from the TrojAI Challenge, reporting average inference time of 24.46 minutes and memory consumption up to 140.6 GB. This demonstrates the approach scales beyond the small models (LeNet/MNIST) typical of prior utilization/efficiency work.

- **Practical relevance**: The problem — explaining how hidden triggers are encoded in safety-critical AI models (e.g., traffic sign classifiers for self-driving cars) — is important and the TrojAI benchmark is a standard testbed.

## Weaknesses

### Major

- **The core method is never formally defined.** The paper's primary novelty is "definition, measurement design, and pattern searching" in utilization-based encodings, yet utilization is described only conceptually: "utilization of any computation unit is related to a ratio of the number of different outputs (tensor-state values) activated by all training data points over the maximum number of possible outputs by the computation unit" (line 26). No equation is given. "Maximum number of possible outputs" is never specified for different operation types (conv, batch norm, ReLU, pooling). Section 3 (Methods) promises to define utilization-based class encodings but instead describes only the TrojAI data creation pipeline. The Summary (Section 5) claims "a mathematical framework for computing three deterministic and statistical AI model utilization metrics," yet only one metric (ratio-based) is described and a second (entropy-based utilization) is mentioned once in a figure caption (line 74). The three metrics are never enumerated or defined. This makes the contribution irreproducible in its current form — a fatal gap for a paper whose novelty lies in definition and measurement design.

- **The evaluation is anecdotal, not systematic, and does not substantiate the claimed objectives.** The paper states three objectives (line 15), including "(3) to identify encoding patterns (motifs) that discriminate AI models without and with hidden classes." Yet the results analyze only **four models** (line 70), report no classification metrics (no accuracy, precision, recall, ROC curves, or any detection rate), include no baseline comparisons (no comparison to pruning-based defenses, spectral signatures, activation clustering, or any other backdoor detection method), and perform no systematic evaluation. The "patterns" are identified by manual visual inspection of color-coded computation graphs. The paper's own framing mentions "classifying a large number of AI models as clean or poisoned" (line 15, line 26, line 68) but never actually performs this classification. This gap between stated goals and delivered evidence is critical.

- **No causal analysis linking utilization patterns to trigger behavior.** The paper claims to "explain" poisoned AI models, but the evidence is purely correlational: some computation units show different utilization values in poisoned models. There is no ablation, no pruning intervention, no verification that the identified nodes are necessary or sufficient for the backdoor. A genuine "explanation" requires showing that altering those nodes changes the backdoor behavior — without this, the paper delivers only observation, not explanation.

- **No comparison to any existing backdoor detection or explanation method.** The paper positions itself against explainability methods (Network Dissection, Network 2 Vector, concept whitening) in the related work, but never compares against them experimentally. Even a simple comparison — e.g., do the identified computation units overlap with those found by pruning-based defenses (Liu et al. 2018)? — is absent. Without baselines, the reader cannot judge whether the utilization approach adds value over existing techniques.

### Minor

- **The three hierarchical levels are not systematically analyzed.** The graph-level analysis (Figure 4) covers 4 models; the subgraph analysis (Figure 5) visually compares 2 models; the node-level analysis (Figures 6–7) focuses on one computation unit (layer1.2.conv2). No quantitative summary states how many patterns were found at each level, how consistent they are across models, or how patterns relate across levels. The hierarchy is presented as a contribution but its operation is never evaluated as a method.

- **"Three deterministic and statistical AI model utilization metrics" are claimed but never specified.** The Summary (line 96) states these metrics were defined, but the paper does not enumerate or formally define them anywhere. The term "entropy-based utilization" appears once (line 74), and the ratio-based utilization is described conceptually (line 26), leaving the third metric unknown to the reader.

- **No discussion of alternative explanations.** The paper attributes utilization differences to poisoning, but does not consider whether they could arise from class imbalance, random variation across model training runs, architectural randomness, or other confounds. This weakens the explanatory claims.

- **Section 3 is mislabeled.** It is titled "Methods" and begins by stating that "utilization-based class encodings are defined" but then immediately describes the TrojAI data creation pipeline without ever providing the promised mathematical definition of utilization.

### Trivial

- **Computational cost context**: The 140.6 GB memory figure (line 96) is reported for "one model" with "M=2500 images" and "286 probes," but it is unclear whether this is peak memory for a single forward pass or for the full analysis pipeline. A brief clarification would resolve this.

- **Table 2 parameters**: The paper references Table 2 (line 70) but the table is not present in the extracted text, making some experimental parameters unclear (how many total models? clean vs. poisoned distribution?).

## Nice-to-Haves

- Adding a comparison with smaller models (e.g., LeNet on MNIST) would strengthen the claim about scaling — although the paper's claim is satisfied by simply demonstrating on larger models, a direct comparison would quantify what is gained.
- A brief discussion of how "maximum possible outputs" is computed for each operation type would go a long way toward making the method reproducible.
- A simple classification experiment (e.g., threshold on utilization ranges) with precision/recall on a TrojAI holdout set would directly substantiate objective (3).

## Removed Points

These points were flagged by the reviewers but are not valid weaknesses of the paper:

- **"Figures are difficult to interpret"** — The paper's figures are embedded in the original submission; their absence from the extracted text is a parser artifact, not an author error.
- **"No comparison to smaller models to demonstrate what is gained"** — The paper's objective is to scale *beyond* small models; demonstrating on ResNet18/101 fulfills this. Asking for a LeNet comparison as proof of "what is gained" is scope creep beyond the stated contribution.
- **"Related work does not clearly identify a gap"** — The paper does contrast its zero-binarization approach with threshold-based methods (Fong & Vedaldi, Bau et al.) and with spectral clustering (Hod et al., Filan et al.), which identifies a clear methodological gap.
- **Various formatting/style nitpicks and requests for missing appendices** — These are parser artifacts or out of scope for a conference submission.

## Novel Insights

None beyond the paper's own contributions. The reviewer analysis largely confirms what the paper itself claims to deliver (a novel utilization metric and hierarchical analysis) and what it does not deliver (a formal definition and systematic evaluation). No reviewer identified a hidden strength or weakness that the paper's authors were unaware of.

## Suggestions

1. **Formally define the utilization metric(s) with equations.** Specify how "maximum number of possible outputs" is computed for each operation type (conv, batch norm, ReLU, pooling, etc.). Enumerate and define the "three deterministic and statistical" metrics claimed in the Summary.
2. **Run a proper classification experiment** on the TrojAI dataset: compute utilization fingerprints, define a simple classifier (e.g., threshold or similarity measure), and report precision/recall/ROC across a holdout set.
3. **Add baseline comparisons** to at least one existing method — e.g., compare identified units with those found by pruning-based defenses (Liu et al. 2018), or compare utilization-based fingerprints to spectral signatures or activation clustering.
4. **Add a causal verification step** — ablate or prune the identified computation units and measure whether backdoor accuracy drops. This would move the analysis from correlation to explanation.
5. **Restructure Section 3** to actually contain the method definition before the dataset description.
6. **Address false positive confounds** — discuss whether utilization differences could arise from class imbalance or random variation rather than poisoning.

## Score and Decision

This paper tackles an important problem (explaining poisoned AI models) with a genuinely novel concept (utilization as tensor-state statistics at hierarchical levels). The multi-level tracing of utilization differences from graph-level distributions down to individual tensor-state patterns is a methodological contribution that could be valuable to the community.

However, the paper in its current form suffers from two fundamental gaps that prevent acceptance: **(a) the core method is never formally defined** — no equations, no specification of how "maximum possible outputs" is computed for different operation types, and the claimed "three metrics" are never enumerated — making the contribution irreproducible; and **(b) the experimental evaluation is anecdotal** — only 4 models, no classification metrics, no baseline comparisons, no causal verification — leaving the paper's central claims entirely unsubstantiated by quantitative evidence. The gap between the stated objectives ("classifying a large number of AI models as clean or poisoned") and what is delivered (visual inspection of 4 models) is too wide for acceptance.

The paper reads as an interesting early exploration that could, with substantial revision, become a solid contribution. But in its current form, the weaknesses are structural and cannot be resolved in a rebuttal.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>