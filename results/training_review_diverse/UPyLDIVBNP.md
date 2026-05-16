Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

The paper proposes IDInit (Fully Identical Initialization), an initialization method for residual networks that preserves identity transitions in both main and sub-stem branches. It introduces: (1) a padded identity-like matrix (IDIτ) to handle non-square weight matrices and break rank constraints, (2) momentum to resolve convergence issues of identity initialization, (3) a patch-maintain reshaping strategy (IDICτ) for convolutional layers to improve feature diversity, and (4) IDIZε with small ε values to address dead neurons. The method is validated across image classification (ImageNet, CIFAR-10), text classification, and BERT pretraining, showing consistent improvements.

## Strengths

1. **Novel identity-maintaining initialization for both branches**: IDInit is the first approach (to the authors' knowledge) to use identity matrices for the non-zero weight W₁ in identity-control residual networks, whereas prior work (Fixup, ZerO) used random or Hadamard matrices that dilute the inductive bias. Figure 2 supports this advantage by showing IDInit achieves better convergence than random/Hadamard alternatives.

2. **Padded identity-like matrix (IDIτ) overcomes rank constraint for non-square weights**: The IDIτ scheme theoretically (Theorem 3.1) and empirically (Figure 4b) achieves higher weight rank than zero-padding during training. Figure 4b shows IDInit's rank reaches ~1500 versus <768 for zero-padding, supporting the claim of breaking the rank constraint.

3. **Consistent improvements on large-scale benchmarks**: On ImageNet (Table 3), IDInit achieves an average 0.55% accuracy gain over baselines and converges 7.4 epochs faster across ResNet-50/152, Se-ResNet-50, and ViT-B/32. On BERT-Base (Figure 9), IDInit claims an 11.3% FLOPs reduction during pretraining.

4. **Ablation study isolates individual contributions**: Table 4 cleanly decomposes the effects of IDICτ (+3.42%) and IDIZCε (+5.89%) on CIFAR-10, providing evidence that each component independently improves performance.

5. **Addresses the dead neuron problem concretely**: Figure 5 visually shows that IDIZε makes all weights trainable in a ResNet block, while Fixup/ReZero leave many weights frozen. The mathematical derivation (mean 0, variance → 0 with small ε) provides a principled basis for the approach.

6. **Broad empirical validation**: The method is tested across multiple domains (vision, NLP) and architectures (CNN, ViT, RNN, Transformer), demonstrating generality.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Convergence experiment is too small to be fully convincing (Section 3.1, Table 1)**: The experiment uses a 3-layer linear network with 10×10 weight matrices and 2000 samples to show that momentum resolves the convergence problem of identity initialization. While the conclusion (momentum helps) is unobjectionable, the setup is far simpler than the deep nonlinear networks that IDInit targets. The paper would benefit from a controlled study on deeper networks or with non-linear activations to strengthen this claim.

2. **Rank constraint argument contains confusing presentation (Section 3.2.1, Theorem 3.1)**: Theorem 3.1 states rank(θ̂⁽ᵏ⁾) ≥ D₀ with IDI₁ and claims this "breaks the rank constraint." However, since the constraint from ZerO is rank ≤ D₀, achieving ≥ D₀ (which could equal D₀) does not necessarily exceed the constraint at initialization. The paper then says ZerO's claim "is tenable in the initial state" and IDInit breaks it "after training for several steps," which seems to undercut Theorem 3.1's claim about initialization. Figure 4b convincingly shows that IDInit achieves higher rank during training, but the theoretical framing needs clarification. The gap between the theorem's lower bound and the actual claim of "breaking" should be resolved.

3. **CIFAR-10 ablation gains vs. ImageNet gains are not discussed (Section 4.4 vs. Section 4.3)**: The ablation on ResNet-20/CIFAR-10 shows large improvements (+5.89% from IDIZCε, +3.42% from IDICτ), while the ImageNet improvement is only 0.55% on average. The paper does not discuss this discrepancy. The CIFAR-10 gains may be specific to smaller architectures or datasets, and the paper should acknowledge this.

4. **Convergence metric choice not justified (Table 3)**: The paper reports "Epochs to 60% Acc" for ImageNet results without explaining why 60% was chosen. For ViT-B/32, 60% is far below final accuracy (~75%+), making this threshold potentially uninformative about convergence speed in the meaningful performance range. Reporting epochs to 70% or final accuracy would be more standard.

5. **FLOPs reduction claim lacks methodology (Section 4.6)**: The paper states "IDInit shows an 11.3% acceleration ratio in terms of FLOPs" for BERT pretraining without specifying how FLOPs were computed or estimated. Since this appears to be derived from comparing loss curves at different time steps, the estimation method should be clearly described.

6. **No variance/confidence intervals for ImageNet results (Table 3)**: The main ImageNet and CIFAR-10 results report only point estimates without standard deviations or significance tests. While single-run evaluations are common practice at this scale, the paper should at minimum acknowledge this limitation.

7. **Limitations section is empty**: Section 5 lists "Limitation." with no content. This is a missed opportunity to discuss the method's constraints (e.g., the discrepancy between CIFAR-10 and ImageNet gains, the limited convergence experiment, or the lack of isometry measurements in the main paper).

### Trivial
- The paper uses inconsistent formatting for some mathematical expressions (e.g., spacing issues in Theorem 3.1).
- Figure captions occasionally contain garbled punctuation (e.g., "Figure 2: Analyzing effect of initializing $W_{1}$ while $W_{2}\,=\,{\bf0}$ .4.").

## Nice-to-Haves

- A controlled experiment on deeper nonlinear networks to verify that momentum resolves the convergence problem of identity initialization in more realistic settings.
- Analysis of whether the specific subtraction construction in IDIZε is necessary, or whether simply adding small uniform noise to a zero weight would suffice.
- Inclusion of training loss curves alongside accuracy curves on ImageNet to separate convergence speed from final performance.
- Dynamical isometry measurements (currently deferred to Appendix C.4, which may be stripped) integrated into the main paper.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Incomplete baselines (missing Orthogonal, LSUV, DS Init, ProxInit)"**: The paper focuses on identity-control initialization methods (Fixup, ZerO, SkipInit, ReZero, Zeroγ). Orthogonal, LSUV, etc. are from different initialization families and are not required for a paper targeting identity-control schemes. The baseline set is appropriate for the paper's scope.
- **"Section 4.1 warm-up comparison is contrived"**: The paper shows results both with and without warm-up. The finding that IDInit works without warm-up is a genuine strength, not a contrived comparison. The critic misread the experiment.
- **"Patch-maintain convolution underspecified"**: The reshaping operation from [k×k×cin×cout] to [cout × kkcin] is clearly described in the text. The term "patch-maintain" is defined by its operation.
- **"ISONet dismissal is abrupt"**: The paper gives concrete reasons (requires SReLU, no batch normalization) that are legitimate technical critiques, not dismissals.
- **"Section 3.2 τ value not justified"**: The paper states τ values for different activations and references Appendix A for trainability analysis. This is standard practice.
- **"First successful trial is questionable given ISONet"**: The paper uses "To our knowledge" and explains that ISONet uses a Dirac function (zero-padding) rather than identity for non-square matrices, and imposes restrictive architectural constraints. The distinction is valid.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel perspective that the paper itself does not articulate.

## Suggestions

1. **Clarify the rank constraint argument**: Distinguish clearly between (a) the rank at initialization (where both IDInit and ZerO may have rank = D₀) and (b) the rank during training (where IDInit demonstrably exceeds D₀). Theorem 3.1 should either be revised to state a result about training dynamics rather than initialization, or its bound should be strengthened to show rank > D₀ at initialization.

2. **Report convergence at multiple thresholds on ImageNet**: Include epochs to 70% or 76% top-1 accuracy alongside the current 60% threshold. This would make the convergence speedup claim more robust.

3. **Describe FLOPs estimation methodology**: Clarify how the 11.3% reduction is computed—is it based on wall-clock time to reach a target loss, theoretical FLOPs saved by early stopping, or another method?

4. **Acknowledge the CIFAR-10 / ImageNet discrepancy**: Add a brief discussion of why the ablation gains on CIFAR-10 are much larger than the improvements on ImageNet.

5. **Fill the limitations section**: Even a few sentences acknowledging the scope of validation (e.g., single runs on ImageNet, small-scale convergence experiment) would improve the paper's credibility.

## Score and Decision

This paper proposes a novel and clearly motivated initialization method backed by consistent empirical improvements across multiple architectures and domains. The core contributions—using identity matrices for both residual branches, padding identity to break rank constraints, and practical fixes for dead neurons—are technically sound and practically useful. The main weaknesses are in presentation clarity (the rank constraint argument is confusingly framed) and missing experimental details (FLOPs estimation, variance reporting, convergence threshold justification). These are all addressable in revision. No fatal or truly major flaws undermine the method's validity.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>