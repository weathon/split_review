Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper analyzes why weight-matching (WM) permutations achieve linear mode connectivity (LMC) between independently trained neural networks. It makes three main contributions: (1) empirically showing that WM reduces L₂ distance by only 6–20% despite achieving LMC, suggesting L₂ reduction is not the direct cause; (2) identifying that WM works by preferentially aligning the directions of singular vectors associated with large singular values across layers, supported by theoretical bounds (Theorem 4.2) and empirical evidence; (3) demonstrating that this mechanism differs fundamentally from the straight-through estimator (STE), giving WM an advantage when merging three or more models.

## Strengths

1. **Shows that L₂ distance reduction is not the direct cause of LMC.** Table 1 demonstrates that even when LMC holds, WM reduces L₂ distance by only 6–20%. The second-order Taylor approximation of the barrier fails to predict the actual barrier (differences highlighted as statistically significant). This directly challenges the prior intuition (e.g., Zhou et al. 2023) that LMC arises from making weights nearly identical via permutation.

2. **Identifies and provides evidence for singular-vector alignment as the mechanism behind WM-induced LMC.** Theorem 4.1 reformulates the WM objective as maximizing inner products between singular vectors of corresponding layers. Figures 2–3 show that WM preferentially aligns singular vectors associated with large singular values (γ=0.3 gives substantially higher alignment than γ=0). Theorem 4.2 then bounds layer-output differences in terms of singular-vector alignment and the input distribution. Figure 4 confirms that large-singular-value vectors have the largest inner products with layer inputs, explaining why their alignment is especially effective for preserving function. This combination of theoretical grounding (Theorems 4.1, 4.2) and empirical support is a genuine contribution.

3. **Reveals a fundamental difference between WM and STE with practical implications for multi-model merging.** Table 2 and the R-value analysis in Section 6.2 show that STE does not align singular vectors (R ≈ 0), while WM does. Section 6.3 (Table 3, Figure 5) demonstrates that this difference carries over to three-model settings: WM indirectly aligns π_b(θ_b) and π_c(θ_c), yielding lower barriers than STE. This insight—that the principle behind the permutation search method determines its suitability for multi-model merging—is non-obvious and practically useful.

4. **Theoretical grounding for the empirical observations.** Theorem 4.2 provides a quantitative bound on layer-output differences in terms of singular-vector inner products and the input distribution, formally linking alignment to the preservation of hidden-layer activations. The proof connects the SVD of weight matrices to the functional behavior of the network, going beyond a purely empirical study.

## Weaknesses

### Fatal
None.

### Major

1. **The central claim that singular-vector alignment is "the reason" LMC holds is established through strong correlational/mechanistic evidence but lacks direct causal intervention.** The paper shows that (i) WM aligns large-singular-value vectors, (ii) this correlates with low barriers, and (iii) Theorem 4.2 bounds output differences in terms of this alignment. However, no experiment directly tests the causal claim by, e.g., breaking the alignment of large singular vectors while preserving L₂ distance reduction, or independently aligning them without the WM objective. The paper's own language is somewhat guarded ("provide evidence that," "plays a crucial role") in the contributions section (line 20), but the abstract and conclusion frame the result more strongly ("thereby satisfying LMC"). This gap between "strong evidence for a mechanism" and "proven causal explanation" is the paper's most significant limitation. The evidence is far from empty—Theorems 4.1–4.2 and the R-value analysis constitute meaningful support—but the mechanism is not conclusively isolated. This is a major weakness because it directly concerns the paper's main claimed contribution.

### Minor

1. **The Taylor approximation argument in Section 3 is logically incomplete as a motivating observation.** The paper argues that because the Taylor expansion fails to predict the barrier, the models cannot be close enough for L₂ distance to explain LMC. The reviewer correctly notes that a failure of Taylor approximation could also occur even when models are close, due to the non-convexity of the loss landscape. The paper does not calibrate the Taylor approximation on a pair of known-close models (e.g., the same model with small perturbations) to verify it works there. This weakens the motivating narrative but does not undermine the paper's core SVD analysis, which stands on independent theoretical and empirical footing. (Section 3, Theorem 3.1, Table 1)

2. **The activation matching (AM) analysis in Section 5 is relatively shallow.** The paper states that the reason AM achieves LMC is "likely the same" as WM, but the connection drawn is indirect: it relies on the assumption that previous-layer outputs are already close under the permutation, and no rigorous derivation connects the AM objective (minimizing activation distance) to singular-vector alignment. The empirical similarity (Tables 1 vs. 4, Figures 15–16) is suggestive but not analytically established. Given that AM analysis is listed as part of contribution 2, the treatment feels perfunctory.

3. **The three-model experiment (Section 6.3) is demonstrated on a limited set of architectures and implicitly one dataset.** The paper's tables consistently use MLP, VGG11, and ResNet20 on what appears to be the same dataset throughout (the dataset is not explicitly named in the extracted text). While this is a reasonable experimental scope, the claim that WM is "more advantageous for merging three or more models" would benefit from broader validation.

4. **The paper uses the Sinkhorn-based implementation of WM (Peña et al. 2023) without discussing whether the results generalize to the original layer-wise WM (Ainsworth et al. 2023).** The paper mentions this choice (Section 2.4) and justifies it ("potentially finds better solutions"), but does not test whether the singular-vector alignment effect is specific to this variant or is a general property of WM. This limits the generality of the claims somewhat.

### Trivial

- The three-model experiment's architecture/dataset setup for Table 3 could be more explicitly stated in the text rather than relying on table images.
- Some inline citations (e.g., footnote markers like "3" and "4" in the text at lines 200, 202) appear without corresponding footnote content in the extracted text, which may confuse readers (though this is likely a parser artifact).

## Nice-to-Haves

- **Causal intervention experiments**: After finding a WM permutation, apply an orthogonal transformation to the singular vectors that preserves L₂ distance but deliberately misaligns the top singular vectors. If the barrier increases, this would provide direct causal evidence for the proposed mechanism.
- **Validation of the Taylor approximation** on a pair of truly close models (e.g., same model + small noise) would strengthen the interpretation of Section 3.
- **A more rigorous connection between AM and singular-vector alignment**, either through a theoretical derivation or a targeted small-scale experiment, would convert the speculation in Section 5 into a genuine analysis.
- **Broader evaluation** of the three-model experiment on additional architectures and datasets would strengthen the practical claims.

## Removed Points

These points from the reviewers were considered but are removed or downgraded for the reasons stated:

1. *"The paper's central claim is not adequately supported by the evidence presented. The case is largely correlational, not causal."* — **Downgraded from "critical/fatal" to Major (see Weaknesses #1).** The reviewer's request for strict causal intervention is valid as a limitation, but the paper does provide substantial evidence: Theorem 4.1 (WM objective ↔ alignment), Theorem 4.2 (theoretical bound linking alignment to output differences), and empirical validation (Figures 2–4). The evidence goes well beyond simple correlation; it combines theoretical bounds with empirical support. The reviewer overstates the weakness by treating absence of intervention experiments as absence of evidence, when what the paper provides is a well-supported mechanistic explanation.

2. *"The Taylor approximation failure does not prove that L2 distance is not the cause."* — **Downgraded from a central critique to Minor (see Weaknesses #1 in Minor).** The reviewer's concern is methodologically valid, but this argument is a motivating observation, not a core proof. The paper's main SVD-based analysis is independent of this argument.

3. *"The three-model experiment is limited to one dataset and a single architecture (likely CIFAR-10 with VGG11 or ResNet20)."* — **Downgraded to Minor.** The paper consistently uses MLP, VGG11, and ResNet20 across all experiments, which is three architectures, and the setup is consistent with prior work (Ainsworth et al., Peña et al.). The core contribution is analytical, not a large-scale benchmark.

4. *"For AM, a direct derivation... would convert the speculation into a genuine analysis."* — **Retained as a Minor weakness and a Nice-to-Have.** The paper does attempt a connection (via Theorem 4.2), but the treatment is indeed shallow for a listed contribution.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Reframe the central claim from "revealing the reason" to "providing strong evidence that singular-vector alignment is the primary mechanism," which would better match the evidence presented.
2. Add a causal intervention experiment (as described in Nice-to-Haves) or, failing that, explicitly acknowledge in the abstract and conclusion that the evidence is mechanistic/correlational rather than strictly causal.
3. Strengthen the AM analysis with either a derivation connecting its objective to singular-vector alignment or a clearly stated limitation that the connection is speculative.
4. Specify the dataset and architectures explicitly in the text for each table (not just in embedded table images).

## Score and Decision

The paper makes a solid contribution to understanding why weight matching achieves linear mode connectivity. The key insight—that singular-vector alignment (not L₂ proximity) is the operative mechanism—is well-motivated, theoretically supported (Theorems 4.1, 4.2), and empirically demonstrated across architectures. The WM vs. STE comparison and the multi-model merging experiment add practical value. The main limitation is that the paper presents correlational/mechanistic evidence rather than causal intervention evidence for its central claim, which the authors could address by more carefully calibrating their language or adding targeted experiments. On balance, this is a strong analysis paper that advances understanding of an important phenomenon.

**Originality**: Good — the singular-vector perspective on LMC is novel and non-obvious.

**Quality**: Solid — experiments are carefully done, theory (Theorems 4.1, 4.2) supports the empirical findings.

**Clarity**: Generally clear, though the Taylor argument could be better contextualized.

**Significance**: Moderately high — understanding why WM works has implications for model merging, federated learning, and our theoretical understanding of SGD solutions.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>