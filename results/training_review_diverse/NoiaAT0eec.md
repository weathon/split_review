Now I have a thorough understanding of the paper and all the claims. Let me produce the final consolidated review.

---

## Summary

This paper proposes MI-MAE, which applies the information bottleneck (IB) principle to masked autoencoders (MAEs). The authors introduce two mutual information-based losses — a maximization loss (InfoNCE between latent features from multiple masks) and a minimization loss (CLUB-based upper bound between input and latent features) — intended to balance relevant and irrelevant information in the latent space. The paper claims that 400-epoch MI-MAE achieves 83.9% ImageNet-1K accuracy, surpassing the 1600-epoch MAE by 0.5%, and asserts improvements on detection and segmentation.

## Strengths

- **Novel application of the IB principle to MAEs with an explicit theoretical framework.** The paper formalizes MAE learning through information distortion (Definition 1), states a generalization bound (Theorem 2), and derives conditions for optimal latent features (Corollary 4). This goes beyond prior works that connected MAEs to contrastive learning only implicitly (e.g., Kong & Zhang 2023; Zhang et al. 2022).

- **Two well-motivated loss terms connected to identifiable conditions in the theoretical analysis.** The InfoNCE-based maximization loss (Eq. 7, Eq. 8) is linked to condition (1) of Corollary 4, and the CLUB-based minimization loss (Eq. 10) is linked to condition (2). The use of established MI estimators (InfoNCE, MINE/CLUB) makes the approach computationally grounded rather than ad hoc.

- **Claimed practical efficiency gain.** A 400-epoch MI-MAE model is reported to outperform the 1600-epoch MAE by 0.5% on ImageNet-1K, suggesting a 4× training speedup while improving accuracy — a practically meaningful result if verified.

## Weaknesses

### Fatal

None. While the extracted text lacks visible experimental results for detection and segmentation, this appears to be a parser-truncation issue rather than an intentional omission by the authors. The single reported ImageNet number (83.9%) provides at least partial evidence that experiments were conducted.

### Major

- **The connection between the theoretical framework and the proposed losses is asserted rather than derived.** The paper states Corollary 4, then writes "From the first condition... we can adopt InfoNCE" (line 114) and "for the minimization of MI, we use the Mutual Information Neural Estimator" (line 128). These are leaps, not derivations. Why InfoNCE specifically follows from condition (1) rather than any other MI lower bound is not justified. Similarly, the claim that "optimizing Eq. 10, the third condition in Corollary 4 is also satisfied" (line 140) is stated with zero justification. The paper would benefit from a clean IB Lagrangian formulation (e.g., min I(Z;X) - β I(Z;Y) with Y = X·m) and explicit showing of how each loss term approximates a term in this Lagrangian.

- **Key method details are underspecified, hindering reproducibility.**
  - "Mutually orthogonal masks" (line 103): what does "orthogonal" mean here? Disjoint pixel sets? Masks with zero overlap? Uncorrelated masking patterns? This is never defined.
  - The approximation network for the variational distribution q_θ(z_j|X_j) (line 128–134): its architecture (MLP? Transformer?), number of parameters, and whether it is trained jointly with the encoder or in alternating steps are not described. The loss L_approx (Eq. 9) is given but the training dynamics are absent.
  - The paper mentions N masks per image but does not state how N relates to the training cost or how the masks are sampled (random? fixed?).

- **The experimental section in the extracted text is too sparse to verify the claimed results.** The only concrete number visible is "83.9% accuracy on ImageNet-1K" from the abstract. No tables of classification accuracy across epochs, no COCO detection mAP, no ADE20K segmentation mIoU appear in the extracted main text. The experiments section (5.1) describes pre-training setup and then cuts off. While this is likely a parser artifact (image-based tables may have been stripped), it means the review cannot assess whether the empirical claims are substantiated. The paper needs tabular results in the body.

### Minor

- **The mathematical presentation contains unclear notation and missing justification steps.**
  - The overbrace notation (e.g., $\overbrace{X\cdot(1-m)}$) is used to denote the "simplest effective description" but is not clearly tied to standard IB notation. A reader unfamiliar with Tishby & Zaslavsky (2015) will struggle.
  - Theorem 2's bound uses $K_x$ (complexity), $|Y|$ (output size), and $n_x$ (sample size), but how these concretely connect to an MAE's encoder architecture or mask ratio is not explained.
  - The paper's central theoretical chain (Definition 1 → Theorem 2 → Assumption 3 → Corollary 4 → losses) is presented as a series of asserted results without derivations or even proof sketches. While full proofs likely belong in the appendix (stripped by the parser), the main text should at minimum sketch the reasoning.

- **No ablation study isolating the two losses.** The paper introduces two loss terms (max-mi and min-mi) but presents no experiments showing MI-MAE without one of them. This makes it impossible to know whether both terms are necessary or whether one dominates the improvement.

### Trivial

- The conclusion (Section 6) largely paraphrases the abstract rather than discussing limitations, failure cases, or future work directions specific to the method.
- The text contains "n;" (line 112) as an orphaned fragment, and the final loss formulation on line 142 ("our final loss becomes") is incomplete — though this may be a parser artifact.

## Nice-to-Haves

- An explicit Lagrangian formulation of the MAE information bottleneck: $\mathcal{L} = I(Z; X\cdot(1-m)) - \beta I(Z; X\cdot m)$ followed by an itemized derivation of how each proposed loss approximates a term, would resolve the core theoretical weakness.
- Results reported at the same total iteration budget (not just "1/4 epochs" adjusted for 4 masks) to show true computational efficiency rather than merely scaling-adjusted comparisons.
- Discussion of limitations: what types of images or tasks does MI-MAE not help? Is there a trade-off from the additional approximation network?

## Removed Points

- **"Theorem 2 is stated without proof"**: Proofs were likely in the appendix, which the parser strips. Removed per instructions.
- **"The number of masks is implied to be 4 but never explicitly stated"**: Line 155 explicitly says "our method samples four masks for every image." This criticism is factually incorrect.
- **"Corollary 4 references an equation number (l_i) that appears to be a typo"**: $l_i$ is defined on line 111 as $l_i = I(\hat{z}_i; X_0) + \sum ...$. It is a variable, not an equation-number typo. Removed as a misunderstanding.
- **"The method is evaluated across multiple downstream tasks" (from Strength Finder)**: This claimed strength conflicts with the verified weakness that experimental results are not visible in the extracted text. Dropped.
- **"The paper's connection of MAE to contrastive learning via the IB lens is not novel"**: This is an opinion, not a factual weakness. Prior works (Kong & Zhang, Zhang et al.) connected MAEs to contrastive learning; the paper's claim is to provide a *systematic* IB-based framework, which is a distinct contribution even if related.
- **"The final loss formulation is cut off mid-sentence"**: Likely a parser truncation artifact.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not identify any insight that the paper itself does not already claim.

## Suggestions

1. **Tighten the theory-to-loss connection.** Replace the current chain of loosely connected results with a clean IB Lagrangian: $\min I(Z; X\cdot(1-m)) - \beta I(Z; X\cdot m)$. Show explicitly how $\mathcal{L}_{\text{max-mi}}$ lower-bounds the positive term and $\mathcal{L}_{\text{min-mi}}$ upper-bounds the negative term, or vice versa. A one-paragraph derivation sketch in the main text would suffice.

2. **Define "orthogonal masks" clearly.** If they are disjoint (non-overlapping) masks, say so. If they are merely random masks that are uncorrelated on average, say that instead. This is a one-sentence fix.

3. **Describe the approximation network.** Even a single sentence — "a 2-layer MLP with hidden size 512, trained jointly with the encoder via the loss in Eq. 9" — would resolve the current gap.

4. **Add a results table to the main text.** A single table with ImageNet accuracy at 100/200/400 epochs, COCO detection AP, and ADE20K mIoU, compared to the MAE baseline, would make the empirical claims verifiable.

5. **Include a two-row ablation:** MAE baseline vs. MAE + $\mathcal{L}_{\text{max-mi}}$ only, vs. MAE + $\mathcal{L}_{\text{min-mi}}$ only, vs. full MI-MAE, on ImageNet at 400 epochs.

## Score and Decision

The paper presents an interesting angle (IB for MAEs) but the theoretical development is not rigorous, key method details are missing, and the experimental evidence cannot be properly assessed from the extracted text. The connection between theory and the proposed losses is asserted rather than derived, which undermines the paper's central claim of providing a "systematic" understanding. These issues are addressable in revision but are too substantial for the current submission.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>