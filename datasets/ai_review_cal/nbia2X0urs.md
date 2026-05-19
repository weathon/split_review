- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 8, 3, 3
Here is my consolidated review.

---

## Summary

This paper proposes BDGO, a multimodal protein function prediction method that integrates spatial structure features (PPI network, subcellular location, protein domains) with sequence features (amino acid sequences via ProtT5). The key architectural contributions are a Bidirectional Interaction Module (BInM) using dual-branch cross-attention between modality groups, and a Dynamic Selection Module (DSM) using hard-gated mixture-of-experts to adaptively select features for hierarchical multi-label classification. The method is evaluated on a human-protein dataset with 35–45 GO terms per ontology, comparing against 9 baselines.

---

## Strengths

1. **Consistent quantitative improvements on all three GO domains with replication.** Table 1 and Figure 3 show BDGO achieves the highest Fmax and m-AUPR across all three GO aspects. BDGO improves over CFAGO by 19.5% (Fmax, MFO) and 15.0% (Fmax, CCO). All results are reported with standard deviations from 5 random repetitions, and the improvements are consistent across multiple metrics.

2. **Quantitative feature quality evidence via Davies-Bouldin scores.** Figure 4 reports that the DSM embedding achieves the lowest (best) DB scores across all three GO aspects, with at least a 29.3% improvement in CCO over other feature representations. Lower DB scores indicate tighter intra-cluster and better inter-cluster separation, directly supporting the claim that the interaction and selection pipeline produces better protein representations.

3. **Informative ablation study.** Table 2 systematically ablates each component (MIL-Branch, BInM, DSM, spatial features, sequence features) with clear degradation in each case. For example, removing BInM reduces Fmax in BPO from 0.314 to 0.297, and removing DSM reduces it to 0.293. This confirms each proposed module contributes positively.

4. **Domain-specific architectural adaptation.** The BiMamba block adapts the Mamba selective-scan mechanism for protein spatial data by introducing bidirectional forward/backward scans (FSScan/BSScan), which is a nontrivial domain adaptation. The t-SNE visualizations in Figure 5 also provide a useful qualitative complement showing that the DSM embeddings yield clearer cluster separation than raw features or CFAGO's fused features.

---

## Weaknesses

### Fatal
None. The paper's core claims are supported by evidence; no verified finding invalidates them.

### Major

1. **Missing comparison against simpler architectural alternatives for BInM and DSM.** The ablation study (Table 2) only removes entire modules. It does not answer whether the proposed *specific design* of BInM (bidirectional cross-attention) is better than simpler alternatives such as: (a) single-direction cross-attention, (b) simple feature concatenation with shared layers, or (c) a linear projection fusion. Similarly, the DSM uses hard-gated MoE, but no comparison is made against soft-gated MoE, global average pooling, or standard feature concatenation without selection. Without these controlled replacements, the reader cannot tell whether the architectural complexity is justified, or whether a simpler multimodal fusion baseline would yield similar gains. The paper claims "state-of-the-art" architectural design but does not isolate *which designs* cause the improvement.

2. **Missing evaluation on multimodal baselines that the paper itself cites as relevant.** DeepFRI (Gligorijević et al., 2021) is discussed in the introduction as a multimodal protein function prediction method but is not included in the baseline comparison. The paper states it compares against "multimodal methods (Graph2GO, DeepGraphGO, CFAGO)," but omits DeepFRI—a directly relevant multimodal competitor also cited as prior work—without justification. This weakens the claim of outperforming existing multimodal approaches.

3. **No ablation of the pretraining stage.** The methodology includes a two-stage training paradigm: pretraining the PSSI and PSI encoder-decoders, then fine-tuning BDGO. However, the ablation studies never measure the impact of this pretraining. Was the pretraining stage essential? Could the encoders be trained end-to-end with the BDGO model? Without this control, the contribution of the pretraining stage (described in detail in Section 2.1) is unverifiable.

4. **No statistical significance testing.** The results in Table 1 report means and standard deviations from 5 runs, but no significance tests (e.g., paired Wilcoxon, bootstrapped confidence intervals) are provided to confirm that the reported improvements over CFAGO and other baselines are statistically significant beyond random variation.

### Minor

1. **Small label space limits generalizability claims.** The dataset has only 35–45 GO terms per ontology (versus thousands in full GO benchmarks). While all methods are compared on the same dataset, the paper's claim of "state-of-the-art" is only substantiated on this restricted label space. Scaling to larger GO hierarchies (e.g., CAFA-style evaluations with hundreds of terms) where label frequency imbalance and long-tail effects are more severe is not demonstrated. The paper acknowledges it is evaluated on human single-species data but does not discuss this as a limitation.

2. **No hyperparameter sensitivity analysis.** The DSM has hyperparameters (number of experts V, temperature τ=1) and BInM has 8 heads, but no analysis is provided of how these choices affect performance. The ablation study does not vary these values.

3. **No computational cost comparison.** The paper does not report training time, inference speed, or parameter counts relative to baselines, making it difficult to assess the practical trade-offs of the added architectural complexity.

### Trivial
- Some parser-induced formatting artifacts (e.g., Equation 7 notation) are present; these are likely non-issues in the original submission.

---

## Nice-to-Haves
- Replace BInM with a simpler fusion (concatenation, soft attention) and DSM with soft gating / average pooling to directly test whether the specific design choices matter.
- Compare against an additional baseline: ProtT5 embeddings + a linear classifier (without fusion), to isolate the contribution of the multimodal architecture beyond the sequence encoder.
- Report per-GO-term or label-frequency-stratified metrics to show that improvements are not concentrated on high-frequency terms.
- Include bootstrapped confidence intervals or paired significance tests for the main comparisons.
- Ablate the pretraining stage (train BDGO without pretrained encoders).
- Discuss the limitation of the small label space (35–45 GO terms) explicitly.

---

## Removed Points
These points are flagged as removed — treat them with caution.

- **"Absolute performance is low, suggesting the dataset may be trivial" (Harsh Critic §3).** The critic compares absolute Fmax values (0.282–0.421) to CAFA evaluations (>0.5). This is an invalid cross-dataset comparison. Different label sets, species, and label frequencies produce vastly different achievable scores; a lower absolute value on a restricted human dataset does not indicate triviality. The critic's claim that "any method that overfits slightly can appear better" is speculative and unsupported.

- **"Evaluation on a non-standard, extremely small dataset invalidates the claim" (Harsh Critic §1) — in the strong "invalidates" formulation.** The critic argues the dataset is "orders of magnitude smaller" than CAFA, but the paper constructs its dataset "with reference to CFAGO" — the same paradigm used by a key baseline. All methods are evaluated on the same dataset, so the comparisons are internally valid. The small label space is a genuine limitation (retained as Minor weakness #1 above), but it does not *invalidate* the method's demonstrated improvements. The claim is softened to Minor.

- **"Excessive algebraic detail that does not connect to why this choice helps" (Section-by-Section).** Subjective; the mathematical detail is standard for a method section.

- **"Equation (7) appears garbled."** Attributed by the critic to possible parser issues; the notation is standard asymmetric loss with focusing parameters. Not a genuine paper weakness.

- **"Code promised after acceptance" as a weakness.** Standard practice; the paper states code will be made public. Not a weakness.

- **"Omits many recent multimodal methods (e.g., DeepGO, DeepGOPlus, DeepGOZero)" —** The paper explicitly scopes its comparison to multimodal methods (Graph2GO, DeepGraphGO, CFAGO) plus unimodal baselines. DeepGO and DeepGOPlus are sequence-only methods, not multimodal fusion methods. The critic's listing conflates method categories. DeepFRI (a genuinely multimodal method) is missing — this is retained as a Major weakness.

- **"Missing related works."** Not verifiable without external sources; instruction states not to mention missing related works.

- **Strength Finder: "Novel bidirectional scanning mechanism adapted for protein spatial features" —** The BiMamba block is a bidirectional adaptation of an existing architecture (Vision Mamba). This is genuine domain adaptation but the strength claim of "novel" is somewhat overblown; I note it in strengths but as a domain adaptation rather than an architectural invention.

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation about the method, data, or problem that the paper itself does not already contain.

---

## Suggestions

1. Add a controlled experiment replacing BInM with simpler alternatives (concatenation, single-direction cross-attention) and DSM with soft gating / average pooling — this is the single most important control for substantiating the architectural claims.
2. Add DeepFRI as a multimodal baseline.
3. Evaluate on a larger benchmark with more GO terms (e.g., a CAFA-style evaluation or a full-GO human dataset — a natural extension given the CAFA evidence-code standards already used).
4. Ablate the pretraining stage to measure its contribution independently.
5. Add significance tests (bootstrapped confidence intervals or paired Wilcoxon) for the main comparisons.

---
