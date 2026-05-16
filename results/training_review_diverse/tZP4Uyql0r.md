Below is my consolidated meta-review after cross-checking every claim against the paper text.

---

## Summary

FedDFQ proposes a personalized federated learning method that uses a no-parameter Data Identity Extraction Module (DIEM) to generate metric proxies for quantifying data heterogeneity across clients. These proxies are intended to guide weighted global parameter aggregation and a gradient accumulation module (AGAM). The core idea—using simple pixel-level statistics to measure distributional similarity—is novel, but the method specification is critically incomplete, the theoretical justification is weaker than claimed, and the experimental evaluation lacks crucial details.

## Strengths

- **Parameter-free DIEM avoids learnable biases.** The DIEM operates via two simple averaging operations (channel-wise then spatial), deliberately avoiding the biases that learnable feature extractors introduce during initialization and training (Section 3.1, lines 56–58). This is a clean, principled design choice that directly addresses a real shortcoming in prior work.

- **Ablation confirms each module contributes.** Table 2 shows that adding DIEM to FedAvg improves accuracy by 3.13% on CIFAR-10 (from ~89.67% to ~92.80%), and the full model (All) outperforms all single-module configurations. This provides clear empirical evidence that the components are complementary rather than redundant.

- **Scalability demonstrated with increasing client counts.** Figure 3 shows FedDFQ's accuracy advantage over local training growing consistently as the number of clients increases (50→75→100), supporting the claim of favorable scaling behavior.

- **Robustness across multiple non-IID partitions.** Figure 4 evaluates FedDFQ under three distinct heterogeneous splits (Dirichlet, pathological, and class-imbalanced) and shows consistent superiority over compared methods, demonstrating generalization beyond a single data configuration.

## Weaknesses

### Fatal

1. **Section 3.3.1 (Global parameters aggregation) ends mid-sentence; the core weighting mechanism is never specified.** After describing DIEM and the metric proxies, Section 3.3.1 terminates with "Here is the introduction to the algorithm process:" and immediately jumps to Section 4 (Experiments) on the next line. The actual aggregation formula—how cosine similarities from DIEM are converted into per-client weights for global parameter aggregation—is entirely absent. For a methods paper, this is not a missing appendix; it is the central algorithmic contribution left unsaid.

2. **AGAM is mentioned throughout but never described.** The Automatic Gradient Accumulation Module is named in the abstract, introduction, method overview, and ablation study, yet no equation, pseudocode, or algorithmic description of its operation appears anywhere in the paper. The method section heading "3.3 Parameter and gradient integration" includes only the incomplete 3.3.1; there is no subsection for AGAM. The reader cannot determine what AGAM actually does.

3. **FELPA is used in experiments but never defined in the method section.** FELPA appears as an ablation condition in Section 4.3 and in the conclusion (line 175), where it is described as aggregating "weighted parameters of feature extractors according to metric proxies." However, the method section (Section 3) never introduces FELPA, explains what the acronym stands for, or describes its mechanism. This is a critical gap: the ablation study tests a component that was never defined in the proposed method.

**These three issues together mean that the paper's claimed methodological contribution is incompletely specified.** A reader cannot reproduce the method, cannot verify that the design is sound, and cannot assess the novelty of the aggregation and gradient accumulation strategies. This is a structural flaw that prevents acceptance.

### Major

1. **The theoretical justification for DIEM as a heterogeneity proxy is overstated.** The exact equivalence between similarity of data identifiers and similarity of class scores holds only in the trivial case where the classifier weights **W** = I and bias **b** = 0 (Appendix A.1, lines 220–224). The paper's claim to "theoretically prove that the similarity of data identifiers can represent the data heterogeneity" (line 107) conflates this degenerate-case algebraic identity with a general proof. The empirical Pearson correlation of r = 0.728 (Table 3) is moderate—suggestive but not strong enough to support the functional equivalence that the method requires for principled aggregation weighting. This weakens the core motivation for DIEM.

2. **Experimental evaluation protocol is underspecified for a method claiming SOTA.** The paper does not state: (a) whether accuracy is measured on a global held-out test set or per-client local test sets, (b) the Dirichlet concentration parameter α used in the main experiments (only mentioned as α_i = 1 in the d1 description, not the main results), (c) the model architecture (no ResNet, CNN, or other architecture is identified), (d) optimizer, learning rate schedule, batch size, or number of communication rounds. The "A.2 Experiment details setup" appendix heading has no content visible in the processed text. While some detail loss may be a parser artifact, the main text itself is missing these specifications, making the reported numbers difficult to interpret or reproduce.

3. **Several recent, directly relevant baselines from the paper's own reference list are not compared experimentally.** GPFL (Zhang et al., 2023a), FedGH (Yi et al., 2023), and FedCP (Zhang et al., 2023b) appear in the references but are not included in Table 1 or any experimental comparison. Since these are 2023 personalized FL methods closely related to the paper's approach, their omission weakens the claim of comprehensive SOTA comparison.

### Minor

1. **The DIEM operation is described as mapping data into "high-dimension semantic space" (line 14), but the actual output is a low-dimensional vector of length W (image width)—e.g., 32 for CIFAR-10.** This is a simple pixel-row average, not a semantic embedding. The characterization is misleading about what the module does.

2. **Privacy claims for DIEM are unsubstantiated.** The paper asserts that uploading DIEM vectors is "privacy-friendly" and preferable to uploading model predictions, but provides no analysis of information leakage, no comparison to alternatives (e.g., differential privacy guarantees), and no discussion of what information these vectors reveal about local data distributions.

3. **There is no analysis of sensitivity to the DIEM design choices.** Why average along channel-dimension first then row-dimension, rather than column-dimension? Why not use a different aggregation (e.g., median, max pooling)? The design decisions for the DIEM are presented without justification.

### Trivial

- The paper inconsistently uses "IDEM" and "DIEM" (compare line 4 "DIEM" vs. line 175 "IDEM").
- The conclusion re-introduces "IDEM" as if it were a separate module when it is the same as DIEM.

## Nice-to-Haves

- Standard deviations over multiple runs and significance tests would strengthen the reliability claims for Table 1.
- An analysis comparing DIEM-based similarity to alternatives (e.g., penultimate-layer features from a fixed pretrained extractor) would help justify why raw pixel averaging is a better proxy for heterogeneity than learned representations.
- A formal privacy analysis or differential privacy guarantee would substantiate the claimed "privacy-friendly" nature of DIEM.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about typos, spelling, and grammatical errors** (e.g., "bechmark," "efifcient," "Tabel"): Removed per instructions — these are parser artifacts or formatting issues, not author errors in the original submission.
- **Criticism about missing experimental details that would have been in the appendix** (e.g., model architecture, hyperparameters): The appendix heading "A.2 Experiment details setup" exists but its content was stripped by the parser. Per instructions, missing appendix content is not a valid weakness. However, the main-text specification gaps (Dirichlet α, test-set construction, evaluation metric definition) remain as noted in Major #2.
- **Reviewer's claim that Table 1 reports 96.07% and 96.89% accuracy on CIFAR-10 and that these numbers are "implausibly high":** The table is an embedded image that cannot be read from the text. The numbers in the surrounding text (Local = 88.07% on CIFAR-10; DIEM + FedAvg gains of ~3%) suggest the actual CIFAR-10 numbers are in the low-to-mid 90s, which is less suspicious. This criticism is removed as unverifiable.
- **Reviewer's claim that GPFL, FedGH, FedCP are "cited in related work":** These papers appear only in the reference list, not in the related work section. The reviewer's phrasing is inaccurate. However, their absence from experimental comparison remains a valid point (kept in Major #3).
- **Generic strength about "addressing an important problem":** Removed — lacks specificity.
- **Strength about "theoretical + empirical validation" being a core contribution:** The theoretical part has a verified weakness (trivial-case proof), so this strength is downgraded. The empirical correlation (r=0.728) is kept as a qualified observation but not listed as a standalone strength.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any insight about the method or problem that the paper itself does not discuss.

## Suggestions

1. **Complete the method specification.** Provide the exact aggregation formula: how cosine similarities from DIEM translate into per-client weights for global parameter aggregation. Describe AGAM with full equations or pseudocode: what gradients are accumulated, how they are re-balanced, and how this module regularizes the classification layers. Define FELPA explicitly in Section 3. Without these, the paper is not a methods paper.
2. **Tone down the theoretical claims.** Replace the oversold "theoretical proof" with an honest statement: the exact equivalence holds only under W=I, b=0, and the empirical correlation of r=0.728 provides suggestive but not conclusive evidence that the approximation works in practice.
3. **Add standard experimental details to the main text:** model architecture, Dirichlet α parameter, how test accuracy is computed (global vs. per-client), communication rounds, and hyperparameters. Report standard deviations over at least 3 runs.
4. **Include comparison with GPFL, FedGH, and FedCP** in Table 1, since these are directly relevant personalized FL methods from 2023 that share similar goals.
5. **Provide a privacy analysis** for DIEM, or at minimum discuss why pixel-averaged vectors are less revealing than model predictions or learned features.

## Score and Decision

The paper identifies a real problem and proposes a genuinely parameter-free approach to heterogeneity quantification. However, the method section is critically incomplete: the core aggregation mechanism (Section 3.3.1) cuts off mid-sentence, AGAM is never described, and FELPA is never defined. For a methods paper, this is a fatal structural flaw that cannot be resolved in a rebuttal. The review is based on the paper as submitted.

MY FINAL SCORE: <pineapple>3.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>