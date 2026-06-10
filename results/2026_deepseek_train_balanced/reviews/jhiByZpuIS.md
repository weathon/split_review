Here is my final consolidated review.

---

## Summary

MSfusion proposes a decentralized collaborative training framework that enables resource-constrained participants (each training only a sub-model with μ ≤ 0.5) to collectively train a large model without any participant holding the full model. Core innovations include a Double Shifting Splitting (DSS) scheme for model coverage across participants and rounds, overlap aggregation for communication efficiency, and a claimed contrastive objective to mitigate model drift.

## Strengths

- **Double Shifting Splitting (DSS) scheme is clearly defined and addresses a real limitation of prior work.** The inter-participant gap (Eq. 3) and inter-round gap (ζ=1) are mathematically specified, ensuring full global model coverage within a single round and uniform optimization across rounds. This is a concrete improvement over static splitting (HeteroFL, FjORD), round-rolling (FedRolex), and random splitting (Federated Dropout).

- **Quantified computation advantage over FedRolex at a target accuracy.** Figure 3 reports that to achieve 70% accuracy on CIFAR10, FedRolex requires ~45% split model size (116M FLOPs/participant/round) while MSfusion needs only 12.5% split size (9.83M FLOPs) — a >10× reduction. This is a specific, measurable efficiency claim.

- **Operates in a realistic regime where no participant ever holds the full model.** All experiments use μ_n ≤ 0.5 for every participant (Section 5, line 173), directly addressing the constraint that existing PT-based methods (HeteroFL, FedRolex) are not designed to handle.

- **Ablation study isolates component contributions.** Table 2 compares MSfusion against variants w/o contrastive objective, w/o dynamic overlap, and w/o both. The results confirm both techniques contribute, with the contrastive objective showing larger gains on NLP tasks.

## Weaknesses

### Fatal

- **The contrastive objective — presented as a core contribution — is never defined.** Section 4.3 is titled "CONTRASTIVE OBJECTIVE" but contains only one truncated sentence followed immediately by algorithm pseudocode. The algorithm (line 156) references "the contrastive loss (7)" but equation (7) does not appear anywhere in the paper. The abstract, introduction, and conclusion all highlight this as a key novel design for mitigating model drift. The ablation study in Table 2 evaluates a "w/o Con" variant, but the reader cannot know what is being ablated. A method paper whose claimed technical novelty includes a component that is never specified is fundamentally incomplete and cannot be evaluated, reproduced, or built upon.

### Major

- **Baselines evaluated outside their intended operating regime, a fact the paper itself acknowledges.** Section 2.3 states that HeteroFL and FedRolex "inherently assume the participation of participant possessing the complete model" and "without such participants these methods failed." Yet the experiments (line 173) set μ_n ≤ 0.5 for all participants with no full-model participant. The headline results in Table 1 thus compare MSfusion against baselines operating in a regime their design excludes. While showing MSfusion works where baselines fail is valid evidence, presenting this as a direct performance comparison overstates the evidence. A fair evaluation would either include a condition with a full-model participant (as the baselines assume) or frame the comparison explicitly as "MSfusion enables training without a full-model participant, a setting where existing methods fail by design."

- **Scalability experiment (Section 5.2) confounds participant count with total training data volume.** Each participant is assigned a fixed 1/20 portion of the training data. With 5 participants, only 25% of the dataset is used; with 20 participants, 100% is used. The claim that "as number of participants increases, the required split model size reduces significantly" conflates the splitting scheme's effect with the effect of seeing more total data. A proper scalability test would hold total training data constant while varying participant count.

### Minor

- **Overlap aggregation equation (5) contains an unclarified bias.** The equation θ*_{n,[l,i]} = 1/(S+1) Σ_{s_i∈S}(θ_{s_i}+θ_n) gives the local parameter θ_n weight |S|/(|S|+1) and each neighbor's parameter weight 1/(|S|+1). This is not a standard average, and the paper neither notes nor motivates this bias. The notation S is also used ambiguously for both the set and its cardinality.

- **Global model reconstruction is underspecified.** Each participant trains only a sub-model and does not store the full model. The paper mentions a "Global Model Combination step every 10 rounds" (line 220) for evaluation, but does not describe how sub-models are assembled into the global full model or how conflicting parameters from different participants are resolved.

- **No variance or statistical significance is reported.** Results appear to be from single runs without error bars, making it impossible to assess whether reported advantages are consistent or driven by noise.

### Trivial

None.

## Nice-to-Haves

- Clarifying whether the overlap aggregation bias in equation (5) is intentional and, if so, justifying it.
- Including error bars or multiple-seed results.
- Running a version of the scalability experiment with fixed total data.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Typos/grammar criticisms (e.g., "donates" → "denotes," "fliters" → "filters," "perofrmance"):** Per instruction, these are considered parser artifacts from PDF extraction, not author errors in the original submission.
- **Missing related works:** Cannot be confirmed without external sources; removed per instruction.
- **Reproducibility nitpicks about undisclosed hyperparameters or trivial implementation details:** Removed per instruction as standard practice for the venue.
- **Critique about tables/figures being embedded as images:** This is a parser limitation, not a paper issue.
- **Critique about missing appendix, missing proofs, or absent references:** The parser strips these sections from all papers; they exist in the original submission.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Define the contrastive loss completely.** Specify what representations are contrasted (model parameters? hidden states?), the loss formulation (NT-Xent? InfoNCE? other?), and how λ is set. Without this, the method is incompletely specified and cannot be accepted.
2. **Re-frame the baseline comparison.** Either run HeteroFL/FedRolex with a full-model participant present (their intended regime) and present both conditions transparently, or explicitly frame the comparison as "MSfusion enables training without a full-model participant, a setting where existing methods fail by design."
3. **Fix the scalability experiment** by holding total training data fixed while varying participant count, so observed trends are attributable to the splitting scheme rather than data volume.
4. **Clarify equation (5).** Either correct the aggregation formula to a standard average or explain and motivate the observed bias.
5. **Describe the global model reconstruction mechanism** used for evaluation.

## Score and Decision

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>