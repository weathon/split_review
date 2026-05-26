Now I have verified all claims. Let me produce the final consolidated review.

---

## Summary

This paper proposes OML, a brain-inspired neural network for online multimodal learning. The architecture features a hierarchical modular structure with ascending/descending/lateral pathways, a reference extraction algorithm that identifies which feature dimensions a word refers to, and a conflict-detection mechanism with human-in-the-loop interaction. Experiments on small custom datasets (Fruits, HomeF) and their enhanced variants show that OML maintains stable accuracy in open-environment (sequential) settings and outperforms existing online methods (AEN, ART). The problem is well-motivated and the architecture is described in detail, but the evaluation has fundamental issues that prevent the paper from making a sound scientific contribution in its current form.

## Strengths

1. **Conflict detection and human-in-the-loop interaction** — The network explicitly checks whether current input conflicts with previously learned knowledge and generates appropriate questions to the user, updating itself based on the answer (Section 3.5). The paper reports that when 10% of word-image or word-taste pairs are intentionally mismatched, "OML is able to detect all conflicts and raise appropriate questions" (Section 4, last paragraph). This capability is unique among the compared online methods.

2. **Reference extraction algorithm for precise word-feature association** — Section 3.4 introduces a coefficient-of-variation-based method that autonomously identifies which feature dimensions a word refers to (e.g., distinguishing color-referring from shape-referring words). This enables OML to learn attribute-level referring expressions rather than treating all attributes identically. Table 2 shows OML achieves the highest accuracy on the enhanced E-Fruits and E-HomeF datasets, while offline methods drop significantly due to forgetting.

3. **Stable online learning in open environments** — In the open-environment experiments where classes are introduced sequentially (no replay buffer), OML maintains stable accuracy while offline methods (DAE, DBM, DJSRH, NRCH, FUME) degrade severely (Table 1). OML also outperforms the online baselines AEN and ART in this setting, supporting the claim that the architecture handles catastrophic forgetting better than existing online multimodal approaches.

4. **Demonstrated modal extension capability** — Table 3 shows OML integrating a new taste modality and correctly distinguishing whether a word refers to a taste concept or a visual concept, using its frequency-parameter (λ) routing mechanism. AEN, the only comparable online method supporting modal extension, cannot make this distinction.

## Weaknesses

### Major

1. **No ablation or simplification study** — The method introduces an elaborate set of mechanisms: Fourier-transformed activations (Eqs. 1, 6), Gaussian signal variables for descending pathways (Eqs. 2, 4), frequency-parameter routing, coefficient-of-variation reference extraction (Eq. 7), lateral connections, and threshold-based activation rules. Not a single component is ablated, simplified, or tested for necessity. The reader cannot determine whether the Fourier transform provides any benefit over an identity mapping, whether the Gaussian signal model is essential, or whether a simple multi-label objective could replace the reference extraction heuristic. **This is a critical gap** — without isolation experiments, the paper's core architectural contribution is scientifically uninterpretable.

2. **Unfair baseline comparison in the open environment** — The open environment (sequential class introduction) compares OML against offline methods (DAE, DBM, DJSRH, NRCH, FUME) without applying any continual learning techniques (replay, EWC, SI, knowledge distillation) to those baselines. The paper acknowledges these are "offline paradigms" that are "frozen after training," yet evaluates them in a sequential setting where catastrophic forgetting is guaranteed. Their degradation is expected and does not constitute a meaningful comparison. This inflates the apparent advantage of OML over what is already demonstrated by comparison with proper online baselines (AEN, ART). The claim that OML "handles catastrophic forgetting" should be based only on the comparison with AEN and ART, which is fair and shows OML ahead, but with margins of 2–4 percentage points rather than the dramatic 20+ point gaps shown with offline methods.

3. **Limited experimental scope cannot support general claims** — All experiments use tiny custom datasets (Fruits, HomeF — approximately 10–20 fruit classes each) with heavily hand-crafted features: Fourier descriptors for shape, mean RGB for color, MFCCs for audio. No experiments are conducted on standard large-scale multimodal benchmarks (Flickr30K, MSCOCO, AudioSet, VGGSound) or with end-to-end learned features. The "modal extension" experiment uses a taste dataset from prior work with similarly small scale. The paper's title, abstract, and conclusion claim to address "online multimodal learning" in a general sense, but the evaluation only demonstrates the method on a specific, engineered pipeline on toy-scale datasets.

4. **Precise referring evaluation metric does not validate the claimed capability** — The paper states: "when we use word 'hóng sè' (red) to do recalling, [baselines] return all features (shape and color) of red objects (we count this as a correct result for them in Table 2)." The metric thus does not penalize imprecise retrieval, so the evaluation conflates "retrieving the correct object" with "precisely referring to the correct attribute." The paper's central claim that OML "learns precise references of concepts" is not properly validated by an accuracy metric that cannot distinguish precise from imprecise referring. A multi-label precision/recall metric or explicit attribute-level evaluation is needed.

5. **No statistical significance or variance reported** — All results in Tables 1–3 are single numbers without error bars, standard deviations, or information about number of experimental runs. For comparative claims on small datasets where individual sample order can affect outcomes, single-run reporting is insufficient. This also makes it impossible to assess the reliability of the reported advantages.

### Minor

6. **No hyperparameter sensitivity analysis** — Parameters (θ, T, ϑ, r) are set manually to single values (θ = quarter of weight norm, T = 150, ϑ = 0.8, r = 0.5) with no analysis of their effect on performance. For a system with multiple thresholds and tunable parameters, this is a significant omission.

7. **Human-in-the-loop interaction is thin** — The interaction consists of three hard-coded question templates with a default "yes" answer if no response is given. While this is a practical implementation choice for evaluation, the paper frames HIL interaction as a key contribution, yet the actual capability is rudimentary and far from the rich interactive learning suggested by the framing.

8. **Key conflict-detection claim lacks rigorous evaluation** — The statement that "when we randomly add 10% of word-image or word-taste data pairs with incorrect matches, OML is able to detect all conflicts and raise appropriate questions" appears only as a single prose sentence (Section 4, last paragraph) without a table, formal metric, false-positive/false-negative analysis, or evaluation protocol. This is insufficient to support the claim.

9. **Reference extraction heuristic depends on structured feature spaces** — The reference extraction (Section 3.4) assumes that referring dimensions (e.g., color) have lower variance than non-referring dimensions (e.g., shape) across samples. This heuristic depends on the feature space being pre-decomposed into separable semantic types (shape vs. color features in different "areas"). It is unclear whether this transfers to high-dimensional learned representations where semantic boundaries are not neatly separated.

### Trivial

- Line 240: "OLM" → "OML" (typo in the interaction timeout description).
- Figure 3 caption is extremely dense and difficult to parse.
- The method section would benefit from a forward-reference table summarizing notation (FNs, UANs, MANs, signal variables, etc.).

## Nice-to-Haves

- **Ablation study**: The single highest-impact improvement would be removing or simplifying each novel mechanism (replacing Fourier transform with identity, removing lateral connections, replacing reference extraction with a multi-label objective) on the Fruits dataset to establish what actually contributes.
- **Fair open-environment baselines**: Apply standard continual learning methods (experience replay, EWC, SI) to the offline baselines for a proper comparison.
- **Larger-scale evaluation**: Demonstrate the method on at least one standard multimodal benchmark (e.g., Flickr30K retrieval setting) with learned features.
- **Statistical significance**: Multiple random seeds with error bars for all main results.
- **Formal conflict-detection evaluation**: Precision, recall, and false-positive rate for conflict detection, with a proper experimental protocol.

## Removed Points

These points were flagged by the reviewers but filtered out as noise or misunderstanding. They are included here only for reference and should be treated with caution.

1. **"Fourier transforms in activation functions appear arbitrary"** — This is a speculative claim; the paper provides a rationale (frequency-based routing via the λ parameter for matching descending pathways, Section 3.3). Without evidence that this design choice causes a problem, this is not a valid weakness.
2. **"Method section reads as a collection of threshold-based rules rather than a unified system"** — This is a subjective characterization of presentation style, not a concrete weakness. Biologically-inspired architectures naturally use threshold-based activation rules.
3. **"The evaluation inflates the apparent advantage of OML" (w.r.t. precise referring)** — This specific framing is factually incorrect: counting imprecise baseline outputs as correct would deflate OML's advantage, not inflate it. The valid concern (retained as Major weakness #4) is that the metric fails to validate the claim of precise referring, not that it inflates OML's scores.
4. **"Missing related works" (general)** — Per protocol, I do not critique missing related works without external verification of the relevant literature.
5. **"Missing appendix / proofs in appendix"** — The PDF parser strips appendix content; these exist in the original submission.
6. **Formatting/style nitpicks** — Parser-induced artifacts are not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface observations that significantly reframe or extend the paper's content beyond what the authors already state.

## Suggestions

- **Conduct a systematic ablation study** on the Fruits dataset, removing or simplifying each novel mechanism one at a time (Fourier transform → identity, remove lateral connections, replace reference extraction with simple multi-label objective, replace Gaussian signal model with fixed weights). Report the accuracy impact in the open environment. Without this, the paper's core architectural contribution cannot be scientifically evaluated.
- **Reconstruct the precise referring evaluation** using a metric that actually measures precision (e.g., per-attribute retrieval precision/recall, or a multi-label metric that separately scores whether the retrieved features match the queried attribute). Report baseline and OML scores on this metric.
- **Apply standard continual learning techniques** (experience replay with a small buffer, EWC, or SI) to DAE/DBM/DJSRH/NRCH/FUME and re-run the open-environment comparison. Alternatively, frame the open-environment comparison using only AEN and ART as baselines, which are proper online methods.
- **Run at least 5 random seeds** for all main experiments and report mean ± std.
- **Test on at least one standard multimodal benchmark** (e.g., a subset of Flickr30K or VGGSound) with learned features, even if the method requires adapting the feature extraction pipeline.

## Score and Decision

**Calibration Anchors** (all retrieved from human-review corpus):

| Anchor | Avg Score | Bucket | Comparison to this paper |
|--------|-----------|--------|--------------------------|
| Pa6SiS66p0 — "Beyond Unimodal Learning" | 4.33 | Topic-mid | Multimodal CL paper rejected for weak baselines and limited scope; similar evaluation issues but slightly stronger empirical grounding. |
| gNoqEdT2wO — "Multimodal Class-Incremental Learning benchmark" | 2.33 | Topic-low | Very weakly reviewed (minimal contribution: existing datasets split into tasks). Current paper has more architectural novelty but similar scope limitations. |
| G9Ea7mlqGO — "CLIP model is an Efficient Online Continual Learner" | 3.80 | Topic-mid | Online CL paper rejected for limited novelty and small datasets. Comparable to current paper in evaluation quality and scope. |
| fwJeVYGcbz — "Multiple Modes for Continual Learning" | 4.00 | Topic-mid | CL method paper with moderate scores; criticized for missing baselines and unclear presentation. |
| Pin2kdWloe — "Is multitask learning all you need in continual learning?" | 5.75 | Topic-high | Stronger theoretical grounding and more extensive experiments; paper under review is clearly worse. |
| WM5G2NWSYC — "Projected Subnetworks Scale Adaptation" | 2.00 | Weakness-low | Poorly reviewed (presentation, unsupported claims); current paper is better but shares evaluation shortcomings. |

**Comparison to low-band failures**: The low-scoring topic anchors (gNoqEdT2wO at 2.33) failed due to minimal contribution and insufficient evaluation. The paper under review has stronger architectural novelty but shares the same fundamental evaluation issues — unfair baselines, no ablation, tiny scope, no statistical rigor. Its score must reflect this.

**Final determination**: The paper addresses a well-motivated problem and describes an interesting architecture, but the evaluation is fundamentally flawed: (a) no ablation study makes the architectural contribution uninterpretable, (b) the open-environment comparison uses a strawman setup against offline methods without CL techniques, (c) the "precise referring" metric does not actually measure precision, and (d) the scope is limited to toy datasets with hand-crafted features. These issues are not individually fatal, but collectively they prevent the paper from making a sound scientific contribution. The paper needs major revisions to substantiate its claims.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>