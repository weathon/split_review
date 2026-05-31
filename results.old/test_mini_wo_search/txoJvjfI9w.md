I have thoroughly verified all reviewer claims against the paper. Here is my consolidated review.

---

## Summary

This paper demonstrates that state-of-the-art LLMs (e.g., LLaMA-3-8B) are highly vulnerable to permutation-based attacks on in-context learning demonstrations, achieving >80% attack success rates. To address this, the authors propose PEARL, a framework that combines distributionally robust optimization (DRO) with a learned hard-permutation mining network (P-Net) based on optimal transport. The P-Net uses a Sinkhorn operator with Gumbel sampling to generate challenging permutations for adversarial training. Experiments on synthetic linear function learning and instruction tuning across multiple LLM families show consistent improvements in both average and worst-case performance.

## Strengths

1. **Well-motivated and clearly demonstrated vulnerability**: Section 3 and Figure 1 show that a simple exhaustive permutation search achieves >80% ASR at δ=50% threshold on LLaMA-3-8B, and a learned neural attacker approaches this upper bound. The "double-edged sword" observation — that adding more demonstrations improves average performance but worsens worst-case performance — is insightful and concretely documented.

2. **Novel application of DRO + OT to permutation robustness in ICL**: The paper formulates permutation robustness as a DRO problem over the convex hull of permuted distributions (Eq. 6–8), which is a principled departure from prior ERM-based training. The use of optimal transport (via the Sinkhorn operator) to parameterize the adversary's permutation search is technically novel in the ICL context and connects to established methods for learning permutations through neural networks.

3. **Consistent and substantial empirical gains across settings**: Table 2 shows PEARL improves worst-case performance on held-out instruction tuning tasks by 14–29% over ERM, while also improving average performance by 5.7–9.8% — contradicting the usual robustness-accuracy trade-off. Table 1 shows similar gains in the synthetic linear function setting, with worst-case relative performance drops reduced from 74.6–84.1% (baseline) to 65.5–73.6% (PEARL).

4. **Scalability to many-shot ICL**: Figure 5 shows PEARL trained with few shots generalizes to larger shot counts, achieving worst-case gains of 24–40% over ERM — suggesting the learned robustness transfers beyond the training distribution.

5. **Complementarity with inference-stage methods**: Table 2 demonstrates that combining PEARL with CurStable or Batch-ICL yields additional 3–5% improvements, showing the approach is not redundant with existing post-processing techniques.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **P-Net's interpretation of R_ij is unsupported**: The paper states (line 121) that R_ij represents "the potential increase in difficulty for the LLM if demonstrations i and j are swapped." However, R = g(H W H^T) is simply a learned bilinear function of hidden states with no explicit constraint or test verifying that it captures pairwise swap difficulty. This claim is speculative and should either be tested (e.g., by comparing P-Net's judgments to actual swap-induced loss changes) or softened.

2. **Missing ablation isolating the P-Net's adversarial component**: The core claim is that training against *hard* permutations (vs. random ones) drives the gains. The paper includes ERM+DS (random shuffling) as a baseline in instruction tuning, but in the synthetic linear function setting (Section 5), only ERM+CL is compared. Adding ERM+DS or a "random permutation augmentation" baseline in the synthetic setting would cleanly show whether the P-Net's learned adversarial sampling provides an advantage over simply seeing more random permutations. Without this, the contribution of the adversarial component is less cleanly isolated.

3. **DRO-to-practice gap not explicitly acknowledged**: The DRO formulation (Eq. 6) requires optimizing against a worst-case *distribution* from the convex hull of permuted distributions. The algorithm (Section 4.3) operationalizes this as a two-player game where the P-Net generates a *single* hard permutation per sample. This is a standard approximation in minimax/adversarial training, but the paper does not explicitly discuss the gap or provide justification for why optimizing against single permutations approximates the sup over distributions in Eq. 6. A brief acknowledgment and discussion would strengthen the theoretical framing.

4. **No variance or significance reporting**: Table 2 reports percentage improvements but no variance estimates or significance tests. Given that training loss plateaued within one epoch (suggesting possible sensitivity to checkpoint selection), some measure of variability across runs would help assess reliability. This is common in the field, but including confidence intervals would strengthen the empirical claims.

5. **"Entropy constraint" is terminologically imprecise**: The term L(φ)_ent = ∑ Π_ij(1-Π_ij) is called an "element-wise entropy constraint." This is not entropy (which would be -Π_ij log Π_ij). However, the *mathematical effect is correct*: since it is subtracted in Eq. 16 (φ^* = arg max(L(lm) - β L(ent))), minimizing it pushes Π_ij toward 0 or 1, encouraging hard permutations — consistent with the paper's stated goal. The name is a minor imprecision; the optimization direction is correct.

### Trivial
None.

## Nice-to-Haves

- An ablation comparing P-Net's generated permutations to a "greedy adversary" that selects the highest-loss permutation after K random trials. This would quantify the value of the learned OT-based adversary over a cheaper sampling alternative.
- Showing that P-Net's permutations actually induce higher LLM loss than random permutations during training (a simple diagnostic plot).
- More baselines in the synthetic experiment (e.g., ERM+DS, ERM+mixup) to strengthen the isolation of the adversarial component's contribution.

## Removed Points

- **Entropy constraint is "counterproductive to its stated goal" (Harsh Critic #1)**: REMOVED. This criticism is factually incorrect. The critic claims "maximizing this term encourages soft, uniform matrices," but Eq. 16 shows the term is *subtracted* in the maximization objective: φ^* = arg max(L(lm) - β L(ent)). Minimizing L(ent) = ∑ Π_ij(1-Π_ij) pushes Π_ij toward 0 or 1 — exactly the hard permutation matrices the paper intends. The critic overlooked the minus sign. The only valid sub-point (terminological imprecision of calling it "entropy") is retained as Minor #5 above.
- **ASR definition inflates numbers**: REMOVED. The paper defines ASR transparently in Eq. 3 using the average as baseline, and also separately reports absolute worst-case performance. This is a design choice, not a flaw.
- **Figure 5 not interpretable**: REMOVED. This is a parser artifact (the figure is in the original submission).
- **Missing appendix content, proofs, reproducibility details about undisclosed hyperparameters, missing baselines that are standard for other problem settings**: REMOVED per hard rules — parser strips appendix, hyperparameters are appropriately detailed, and the paper should not be evaluated against Y when it explicitly scopes to X.
- Several Strength Finder strengths were removed as generic or superficial (e.g., "the paper addresses an important problem," "this paper targeted an interesting question" — these lack specific content). Only evidence-backed strengths are retained.

## Novel Insights

The most interesting insight to emerge from cross-referencing the reviews is that the entropy constraint criticism — which the harsh critic presented as the paper's most serious flaw — is actually based on a misreading of Eq. 16. The critic assumed the regularizer was being maximized when it is in fact being subtracted (hence minimized). This is important because it demonstrates that the paper's mathematical formulation is internally consistent: minimizing ∑ Π_ij(1-Π_ij) does push toward hard permutation matrices, which aligns with the stated goal. The only real imprecision is terminological. Beyond this, the reviews do not surface genuinely novel observations beyond the paper's own contributions.

## Suggestions

1. Rename the "element-wise entropy constraint" to a more accurate term (e.g., "hardness regularizer" or "permutation sharpness penalty") to avoid terminological confusion.
2. Add a simple ablation in the synthetic setting comparing PEARL against ERM trained with random permutation augmentation to isolate whether the adversarial sampling drives the gains.
3. Acknowledge the approximation gap between the full DRO sup-over-distributions formulation and the single-per-sample adversarial training implementation.
4. Include variance estimates (or at minimum, multiple-seed results) for core tables.
5. Soften or remove the unsupported claim about R_ij capturing pairwise swap difficulty unless verified with an explicit diagnostic.

## Score and Decision

**Overall assessment**: This paper addresses a real and practically important vulnerability, proposes a technically sound and novel framework combining DRO, OT, and adversarial training, and provides consistent empirical evidence across synthetic and real tasks. The two most concerning-looking criticisms from the harsh review (entropy constraint mismatch, DRO-to-practice gap) turn out to be either a misreading of the paper (the former) or a standard approximation that would benefit from explicit acknowledgment but is not a flaw (the latter). The remaining weaknesses are minor and addressable. The contributions are significant and well-supported.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>