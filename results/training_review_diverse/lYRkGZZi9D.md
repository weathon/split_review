Here is my consolidated final review.

## Summary

This paper analyzes why permutation-based weight matching (WM) produces linear mode connectivity (LMC) between independently trained neural networks. The central finding is that WM works not by significantly reducing L₂ distance between weights (only 6–20% reduction) but by aligning the directions of singular vectors associated with large singular values across models. This alignment ensures that the merged model retains functionality similar to the original models even when the weights remain far apart. The paper further shows that activation matching (AM) works via a similar principle, while the straight-through estimator (STE) achieves LMC through a fundamentally different mechanism that does not align singular vectors, disadvantaging multi-model merging.

## Strengths

- **Shifts the explanation for LMC from weight-space proximity to function-relevant structure.** Section 3 (Table 1) empirically demonstrates that WM reduces L₂ distance by only 6–20%, and a second-order Taylor expansion fails to predict the barrier — directly contradicting the intuitive assumption that closeness of weights is responsible. This negative result motivates the paper's positive contribution.

- **Provides a novel, mechanistically plausible explanation via singular-vector alignment.** Theorem 4.1 shows that WM is equivalent to maximizing inner products of singular vectors weighted by singular values. Figures 2–3 confirm that WM preferentially aligns singular vectors with large singular values (R values up to ~0.8 for MLP with γ=0.3), while unpermuted vectors are nearly orthogonal (R≈0). Theorem 4.2 together with Figure 4 (showing inputs predominantly activate directions corresponding to large singular values) provides a theoretical grounding for why this alignment matters for LMC.

- **Distinguishes WM from STE both in mechanism and in practical consequences for multi-model merging.** Section 6.2 shows STE produces nearly zero singular-vector alignment (R≈0) despite achieving low barriers. Section 6.3 shows that WM yields significantly lower barriers than STE when merging three or more models because WM indirectly aligns singular vectors across all pairs via the anchor model, whereas STE does not. This is a clean, practically relevant contrast.

- **Multiple architectures validated.** Key experiments are run on MLP, VGG11, and ResNet20, demonstrating that the findings are not specific to a single architecture family.

## Weaknesses

### Fatal
None.

### Major
None. The paper makes a genuine analytical contribution; no weakness undermines its core claims.

### Minor

- **The R metric would benefit from a more explicit justification, particularly regarding cross terms.** The metric R = Σ_{ℓ,i,j} (u_{ℓ,i}^{(a)})^T P_ℓ u_{ℓ,j}^{(b)} (v_{ℓ,i}^{(a)})^T P_{ℓ-1} v_{ℓ,j}^{(b)} / Σ_ℓ n_ℓ sums over all (i,j) pairs including i≠j. The paper does not explicitly argue why cross terms vanish under the correct permutation. (They are expected to be near zero because singular vectors of different indices are orthogonal, and the permutation maintains orthogonality — but this reasoning is left implicit.) The empirical observation that R≈0 without permutation supports the metric's behavior, but a direct justification would strengthen the exposition. This is a presentation gap, not a validity issue.

- **The causal role of singular-vector alignment is supported by theory and correlation but not by a controlled isolation experiment.** The paper provides Theorem 4.2 bounding output differences in terms of singular-vector alignment and shows that inputs predominantly activate large-singular-value directions (Figure 4). This establishes a plausible mechanism. However, the paper does not include an experiment that directly isolates alignment from other factors — e.g., comparing WM to a procedure that achieves the same L₂ reduction without preferentially aligning large singular vectors, or synthetically controlling alignment while holding other factors fixed. Such an experiment would strengthen the claim, but its absence does not invalidate the contribution given the theoretical argument and converging empirical evidence.

- **The AM analysis is suggestive but incomplete.** Section 5 provides a brief derivative argument and references appendix figures to claim that AM "likely" works via the same singular-vector alignment principle. While the numerical similarity to WM is noted, a tighter theoretical connection or a targeted experiment isolating the alignment mechanism for AM would be more convincing than the current treatment.

- **Experimental scope is adequate but not exhaustive.** The paper tests three architectures (MLP, VGG11, ResNet20). The datasets are implied by the table images to be CIFAR variants (likely CIFAR-10/100). For an analytical paper of this type, this is a reasonable empirical base — the focus is on mechanism, not benchmark performance — but generalizability to ImageNet-scale models or language-domain architectures (e.g., Transformers) remains unknown.

- **The Taylor approximation experiment could be slightly more thorough.** The paper evaluates the Taylor estimate at λ=1/2 (justified by citing prior work showing the midpoint typically gives the highest barrier). While reasonable, verifying this holds for the specific settings used would add confidence.

- **Training hyperparameters are not specified.** Learning rate, weight decay, batch size, number of epochs, and Sinkhorn iteration counts are not reported in the main text. This makes exact reproduction difficult, though the qualitative nature of the findings reduces the severity of this gap.

### Trivial

- The paper references "appendix" figures and proofs that are not present in the submission. Per parsing conventions, these exist in the original submission.

## Nice-to-Haves

- Sweeping the γ threshold continuously in the R analysis (beyond just γ=0 and γ=0.3) would give a more complete picture of how alignment varies with singular-value magnitude.
- Quantifying the variation in singular values across models (e.g., standard deviation per rank) would strengthen the claim that singular values are "very close" across models (Section 4.2).
- Reporting the number of singular vectors retained at each γ threshold would aid interpretability.
- Including confidence intervals or effect sizes for the key R-value comparisons (WM vs. no permutation, WM vs. STE) would align with best practices.

## Removed Points

- **"R metric sign-flipping concern"**: The critic claimed that if left and right singular vectors both point in opposite directions, the product of inner products still gives +1, making the metric ambiguous. In fact, in SVD, flipping both u_i and v_i simultaneously preserves the weight matrix (u_i s_i v_i^T = (-u_i) s_i (-v_i)^T). The metric correctly treats this as alignment because the functional effect is identical. This is a feature, not a flaw. **Removed (factually incorrect).**

- **"Limited to a single dataset (CIFAR-10)"**: The paper explicitly states "for all datasets" (para after Table 1) and the table structure implies multiple datasets (columns likely include CIFAR-10 and CIFAR-100). The table is embedded as an image so dataset names are not in the parsed text, but the paper's own language indicates breadth beyond a single dataset. **Removed (factually inaccurate — the paper uses multiple datasets).**

- **"No causal link is established" (framed as fatal)**: The paper provides Theorem 4.2 (a theoretical bound on output differences), Theorem 4.1 (showing WM maximizes singular-vector alignment), and empirical evidence (Figures 2–4). This is not "merely correlational" — it is a mechanistic explanation supported by both theory and experiments. The absence of a strict causal isolation experiment is a minor gap, not a fatal one. **Demoted to minor weakness (appropriate tier).**

- **"Missing reproducibility details" as a major concern**: While training hyperparameters are not fully specified, the paper's contribution is qualitative/analytical, not a benchmark that requires exact reproduction. The main claims are about mechanism, not numerical scores. **Downgraded to minor weakness (proportionate severity).**

- **"Missing appendix"**: Per instructions, appendix content is stripped by the parser; it exists in the original submission. **Removed.**

## Novel Insights

The reviews surface one genuinely novel lens not explicitly emphasized in the paper: the contrast between WM and STE illuminates a deeper distinction between *weight-space geometry* (WM exploits the linear-algebraic structure of individual layers) and *loss-landscape geometry* (STE directly minimizes the barrier via the loss function). This suggests that there exist qualitatively different classes of permutations that achieve LMC, which raises interesting questions about whether LMC is a single phenomenon or a family of phenomena with distinct underlying mechanisms. The paper's demonstration that the two approaches diverge in multi-model merging is the first empirical hint that this distinction has practical consequences.

## Suggestions

1. Add a brief explicit justification for why cross terms in R are negligible when the permutation correctly aligns singular vectors (orthogonal vectors paired by permutation have near-zero inner products).
2. Include a controlled experiment (e.g., synthetic alignment manipulation or comparing WM to an alternative that achieves the same L₂ reduction without aligning singular vectors) to more directly test the causal role of singular-vector alignment.
3. Report the training hyperparameters (learning rate, weight decay, epochs, batch size, Sinkhorn iterations) in a reproducibility statement.
4. For the AM analysis, provide either a stronger theoretical argument linking activation reconstruction to singular-vector alignment, or an ablation experiment that isolates the mechanism.

## Score and Decision

This is a solid analytical paper. The central claim (WM achieves LMC by aligning large-singular-value singular vectors, not by reducing L₂ distance) is well-motivated, theoretically grounded, and empirically supported across multiple architectures. The weaknesses are minor: some under-justified exposition in the metric, a lack of strict causal isolation (appropriate for an analytical paper), and modest experimental breadth. None threaten the core contribution. The contrast between WM and STE and the multi-model merging experiments add practical value beyond the core analysis.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>