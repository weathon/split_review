## Summary
This paper introduces Modality-Collaborated Federated Learning (MCFL), a new setting where clients hold only uni-modal data (e.g., some have images, others have text) and collaborate to improve performance on *each* modality — without requiring any multi-modal client or aligned multi-modal data. The authors propose FedCola, a framework built on a modality-agnostic transformer with three empirically-motivated design choices: attention sharing (shared self-attention layers across modalities), modality compensation (equalizing the contributor count per parameter group during aggregation), and modality warm-up (uni-modal pre-training within the FL round structure). Evaluated across two scenarios (low-correlation general tasks and high-correlation medical tasks) and multiple FL conditions (varying client counts, data heterogeneity, client availability), FedCola consistently and substantially outperforms both Uni-FedAVG (the uni-modal baseline) and CreamFL (adapted from multi-modal FL), with average accuracy gains up to 8.58%.

## Strengths
1. **Novel, well-motivated problem formulation (MCFL).** The paper identifies a genuine practical gap: existing Federated Multi-Modal Learning (FMML) requires multi-modal clients with aligned multi-modal data, but real deployments often have only uni-modal clients. The MCFL definition (Section 2) is clean, the contrast with prior work is clearly illustrated (Figure 1), and the three-axis framework (parameter-sharing, aggregation, temporal modality arrangement) structures the solution space effectively.

2. **Systematic, evidence-driven framework design.** Rather than proposing a monolithic method, the paper poses three specific research questions (Section 5) and answers each with targeted empirical studies. Table 1 identifies attention-sharing as the optimal sharing strategy; Section 5.2 introduces modality compensation to address aggregation misalignment (Figure 5); Table 3 determines that vision warm-up with heat-distribution helps in high-correlation settings. This design methodology directly yields the composite FedCola framework (Section 5.4), and the ablation study (Table 5) transparently decomposes the contribution of each component.

3. **Consistent and substantial performance gains across diverse FL scenarios.** Table 4 shows FedCola outperforming both baselines on *all* averaged accuracy metrics and nearly all uni-modal accuracies across 12 different settings (varying N_v=N_l ∈ {4, 16}, α ∈ {0.5, 0.1}, r ∈ {0.5, 0.25}). The improvements over CreamFL reach up to 8.58% in average accuracy. These results are the paper's strongest asset and convincingly demonstrate that parameter-sharing between uni-modal clients can be more effective than feature-alignment approaches requiring multi-modal clients.

4. **Resource efficiency.** Figure 6 shows FedCola incurs the same computation and communication costs as the simple Uni-FedAVG baseline, while CreamFL requires 1.97× computation due to public dataset feature extraction. The modality warm-up variant further reduces communication costs. This practical advantage is significant for resource-constrained FL deployments.

## Weaknesses
### Fatal
None.

### Major

- **CreamFL adaptation is underspecified, weakening the primary SOTA comparison (reproducibility).** The paper states only: "We adapt it to the MCFL with MS-COCO as the public dataset, which follows their original design." CreamFL (Yu et al., 2023) was designed for settings with multi-modal clients performing knowledge distillation. In MCFL, there are *no* multi-modal clients. The paper does not explain how the teacher-student setup, distillation loss, or training objective are adapted to this fundamentally different setting. Without this description, the reader cannot assess whether the adaptation is fair or whether CreamFL is at a systematic disadvantage. Since Table 4 prominently features CreamFL as a state-of-the-art comparison, this omission weakens the evidence for the claim "FedCola significantly outperforms existing solutions." The paper's core contribution does not depend on beating CreamFL (the Uni-FedAVG comparison already supports the main thesis), but the underspecified adaptation should be fully documented for the results to be verifiable.

### Minor

- **No variance reporting for main results.** Table 4 reports only single-run accuracy values. Federated learning experiments can exhibit non-trivial variance across runs due to client sampling and data partitioning. This is especially relevant for interpreting the smaller margins (e.g., modality compensation gains of ~0.5–1.5% in Table 5). Reporting mean and standard deviation over at least 3 runs would sharpen confidence.

- **Verification experiment (Figure 7) is vaguely described.** The paper claims to "enhance the model capability for one modality" and observe a positive correlation with the other modality's performance, but never specifies *how* capability is enhanced (e.g., adding more training data, increasing training epochs, increasing model capacity?). The experiment is too vague to be interpretable or reproducible. The paper's main evidence for modality collaboration already lies in the overall performance gains; this figure should either be clearly specified or removed.

- **Modality compensation justification is heuristic.** The paper motivates modality compensation by citing a generalization bound that depends on the number of training samples, and argues that copying missing-modality weights equalizes the number of contributing samples. However, the copied weights are not trained on new data, so the effective sample count per parameter group is not actually equalized in a statistically meaningful sense. The ablation study (Table 5) shows that modality compensation provides positive empirical gains, which is sufficient to justify its inclusion, but the formal justification as presented is incomplete. The paper should either provide a sounder theoretical grounding or explicitly reframe it as an empirical heuristic.

### Trivial

- **Inconsistent client count description (Section 6.1).** The text states "K=4 clients online in each round (the ratio r=0.5)" while describing the setting with N_v=N_l=16 (total N=32). With r=0.5, K should be 16, not 4. The K=4 value matches the smaller N_v=N_l=4 setting. This appears to be a copy-paste error that should be corrected.

- **No discussion of training hyperparameters.** The paper does not specify learning rate, optimizer, batch size, or any hyperparameter tuning procedure. While default configurations may have been used, this information should be stated for reproducibility.

## Suggestions
1. **Specify the CreamFL adaptation in full detail.** Describe the teacher-student setup, how knowledge distillation is performed without multi-modal clients, the distillation loss function, and the role of the MS-COCO public dataset. This is the single most important fix for the paper's verifiability.
2. **Report mean and standard deviation over multiple runs** (at least 3) for the main results in Table 4.
3. **Clarify or remove Figure 7.** If kept, specify how "model capability" was enhanced (e.g., training with additional modality-specific data, varying training epochs, etc.).
4. **Fix the K=4 client count inconsistency** in Section 6.1.
5. **Add training hyperparameters** (learning rate, optimizer, batch size, scheduler if any) to the experimental settings.
6. **Reframe modality compensation** as an empirical heuristic (which the ablation validates) rather than claiming formal theoretical grounding, unless a rigorous proof can be provided.

## Score and Decision

**Originality:** High — MCFL is a genuinely new problem setting that fills a practical gap.  
**Importance:** High — the setting motivates a line of work that better reflects real-world FL deployments.  
**Claims supported:** Mostly yes; the core claim (FedCola enables effective modality collaboration) is well-supported. The CreamFL comparison is partially compromised by missing adaptation details.  
**Soundness:** Good — the experimental design is thorough (12 settings, two scenarios, ablations), though variance reporting is absent.  
**Clarity:** Good — the problem definition, three-axis framework, and research-question-driven narrative are clear. A few ambiguities (CreamFL adaptation, Figure 7 methodology, client count).  
**Value to community:** High — provides a well-benchmarked baseline for a new and practical FL setting.

This is a strong paper with a novel problem setting and a well-designed, empirically validated solution. The weaknesses are real but addressable and do not threaten the core contribution.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept
