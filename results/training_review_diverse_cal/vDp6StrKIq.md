Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper introduces a framework for O(d)-equivariant message passing that combines local canonicalization with "tensorial messages." The key idea is to transform geometric node features between local frames during message passing using explicit tensor representations (Eq. 12), enabling consistent communication of directional information where prior local-canonicalization methods relied on scalar messages (Eq. 11) that lose directional content (Fig. 1). The authors demonstrate an O(3)-equivariant adaptation of PointNet++ and evaluate it on ModelNet40 normal regression, ShapeNet segmentation, and classification tasks.

## Strengths

- **Tensorial messages are a clear theoretical and empirical improvement over scalar messages in local-canonicalization frameworks.** The paper provides a rigorous mathematical generalization: Eq. (12) subsumes Eq. (11) by introducing the change-of-basis term \(\rho_{\mathrm{f}}(R_i R_j^{-1})\). Figure 1 illustrates the conceptual limitation of scalar messages, and Table 3 (the strongest empirical evidence in the paper) shows that tensorial messages outperform scalar messages (e.g., 0.917 vs. 0.844 cosine similarity on normal regression) even when both use the same learned local frames. Notably, tensorial messages with *random* frames also outperform scalar messages with *learned* frames, convincingly isolating the benefit of the tensorial mechanism from frame quality.

- **Rigorous theoretical derivation of invariance and equivariance.** Equations (7)–(10) formally prove that node features expressed in local frames are invariant under global O(d) transformations and that the final prediction is equivariant for any chosen output representation. The proofs are clean and correctly handle pseudotensors (Eq. 3) for reflection sensitivity.

- **Iterative refinement of local frames is a novel and well-motivated addition.** Section 4.3.1 proposes refining frames layer-by-layer using an MLP, with the feature transformation \(f_i^{(k)} \to U_i^{(k)} f_i^{(k)}\) to maintain consistency. The improvement over static frames (e.g., Table 1) is modest but the idea is architecturally sound and enables frames to benefit from the growing receptive field.

- **The framework enables a cleaner comparison between built-in equivariance and data augmentation than most prior work.** By setting all frames to the identity (or a random global rotation), the same architecture can be trained non-equivariantly, controlling for architecture and optimizer choices. This is a genuine advantage over specialized equivariant architectures that lack a non-equivariant counterpart.

## Weaknesses

### Fatal
None.

### Major

1. **The SOTA claim on normal regression rests on an uncontrolled comparison.** The paper states it uses "the resampled version of the dataset for which normal vectors at all points are available" (line 204), but cites baseline results "taken from (Luo et al., 2022)" (Table 1 caption) — and it is not established that Luo et al. used the same dataset version. If the resampled version differs in point density, sampling strategy, or normal computation, the reported gap (which the reviewer describes as 0.99+ vs. ~0.96 cosine similarity) could be an artifact rather than a genuine architectural improvement. The paper should either report results on the standard ModelNet40 version used by baselines, or explicitly note that prior results are not directly comparable and drop the SOTA framing. Since the paper's core contribution (tensorial > scalar) does not depend on the SOTA comparison, this is fixable but as-is it undermines a headline claim.

2. **The feature representation design is underspecified for reproducibility.** The paper states that node features \(f_i\) are treated as "a direct sum of multiple tensor and pseudotensor representations (see App. A)" and that \(\rho_{\mathrm{f}}\) defines the transformation behavior, but the main text never specifies how many feature channels are assigned to each tensor order (scalar, vector, higher-order), how this assignment varies across layers, or how \(\rho_{\mathrm{f}}\) is concretely implemented for the PointNet++ adaptation. The reader cannot determine whether the "tensorial messages" are mostly scalar-vector or use higher-order tensors, and cannot reproduce the architecture. While appendix details may exist, the main paper should convey the design principle.

3. **The claim of adapting "any existing message passing architecture" is unsubstantiated.** The paper states "We explicitly show how to adapt our framework to make any existing message passing architecture O(d)-equivariant" (line 20) and that the framework "can be integrated with any architecture without restrictions" (line 5). Yet only a single architecture (PointNet++) is adapted. The framework is theoretically general (Eq. 12 applies to any architecture of the form in Eq. 11), but the paper provides no evidence it can be applied to architectures with attention, global pooling, or non-MLP feature processors. A second adaptation (e.g., DGCNN or a simpler model) or a qualified claim is needed.

### Minor

1. **Data augmentation comparison has a parameter mismatch.** The paper claims "a fair comparison using the same hyperparameters" (line 176) but acknowledges parameter differences of up to 10.3% (line 216) because the equivariant model includes learned frame predictors while the augmentation baseline does not. The paper is transparent about this, but the "fair comparison" framing is overstated. Matching parameter counts or discussing how this gap might affect results would strengthen the comparison.

2. **The data efficiency experiment (Figure 4) is underanalyzed.** The paper notes that data augmentation can outperform built-in equivariance at small dataset sizes (line 231) but only briefly mentions this and cites related work. The result is interesting and counterintuitive — it suggests the learned frame predictor is itself data-hungry — and deserves deeper discussion about the practical trade-offs.

3. **Only one vector-output task (normal regression) is evaluated.** The paper demonstrates tensorial messages on one task requiring vector output and two invariant tasks (segmentation, classification). The benefit of tensorial messages would be more convincingly shown on additional orientation-dependent tasks (e.g., force/ dipole prediction). The segmentation/classification gains are modest, leaving the claim that tensorial messages matter for non-invariant tasks somewhat thin.

### Trivial
None.

## Nice-to-Haves

- Provide a table or diagram showing, for each layer, how many feature channels are assigned to each tensor order (scalar, vector, pseudovector, etc.) and how \(\rho_{\mathrm{f}}\) is implemented.
- Add a second architecture adaptation (e.g., DGCNN or a simple two-layer MPNN) on a simpler task to demonstrate the framework's generality.
- Report computational cost breakdown: how much overhead do the Einstein summations for tensor transformations add relative to the MLP computations?
- Include sensitivity analysis for the cutoff radius \(r_c\) and envelope function \(\omega\).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism about "missing appendix content"** — Rules forbid penalizing missing appendix content since the parser strips these sections. (Moved from the critic's claim that "the appendix may contain details, but the main paper should convey the design principle" — the latter part is kept as a valid Major weakness about the main text's underspecification.)
- **Criticism that "Table 1 reports a cosine similarity above 0.99"** — The exact numerical values in Table 1 cannot be verified from the text (the table is an image). The underlying concern about dataset version mismatch is kept as Major weakness #1; the specific numerical claim is removed as unverifiable from the extracted text.
- **Data augmentation comparison weakness framed as structurally unfair** — The paper acknowledges the parameter differences transparently. The concern is kept but downgraded to Minor, consistent with the rule against inflating ordinary methodological gaps into structural flaws.

## Novel Insights

The most insightful observation emerging from the reviews is the tension between the paper's two main narratives: the convincingly demonstrated internal improvement of tensorial over scalar messages (Table 3), and the questionable external SOTA comparison. The reviews collectively suggest that the paper's real strength — and what should drive its impact — is the clean ablation showing that tensorial communication matters even with randomly chosen frames. The SOTA claim is a distraction that invites scrutiny the core contribution does not need. This reframing would make the paper both stronger and more honest.

## Suggestions

1. **Fix or drop the SOTA claim.** Either report results on the standard ModelNet40 version used by prior work, or explicitly state that the resampled version is not directly comparable and remove "state-of-the-art" language. The main contribution does not depend on this comparison.

2. **Specify the tensor assignment in the main text.** Add a brief table or paragraph showing, for each message passing layer in the PointNet++ adaptation, the number of channels assigned to each tensor order and how \(\rho_{\mathrm{f}}\) is constructed from the frame matrix.

3. **Qualify the generality claim.** Replace "any existing message passing architecture" with "any message passing architecture of the form in Eq. (11)" or add a second architecture example.

4. **Expand the data efficiency discussion.** Analyze why data augmentation outperforms equivariance at small data sizes — is the frame predictor overfitting? This would make an already interesting result more impactful.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>