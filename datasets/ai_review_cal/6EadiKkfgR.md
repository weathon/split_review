- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper formalizes the connection between contrastive learning and semantic equivalence relations. It defines a probability-based notion of semantic equivalence (two symbols are equivalent if substituting one for the other does not change the label distribution given any context) and shows that, under a "distributional alignment hypothesis" (Definition 4.1) connecting the contrastive and downstream distributions, optimal models for a SimCLR-style InfoNCE objective must encode semantically equivalent symbols with the same vector. The authors prove this result for both a labeled variant and the unlabeled setting, and validate the theory on a controlled synthetic modular-addition task where the assumptions hold by construction.

## Strengths

1. **Formal definition of semantic equivalence in the contrastive learning context (Definition 2.1).** The paper provides a precise, probability-based definition of when two symbols are semantically equivalent for a downstream task: ∀ρ,y: p(y|u,ρ)=p(y|v,ρ). This definition is grounded in programming-languages semantics and gives the analysis a rigorous foundation that is rare in contrastive learning theory.

2. **Theorem 4.2 — InfoNCE optimality collapses conditionally equivalent symbols.** The theorem proves that if two symbols have identical context distributions (∀ρ: p(ρ|u)=p(ρ|v)) and a basis condition holds, then any optimal embedding function for the InfoNCE loss must map them to the same vector. This is a non-trivial connection between the contrastive objective and functional equivalence.

3. **Distributional alignment hypothesis (Definition 4.1) as a conceptual bridge.** This hypothesis formalizes the relationship between the label-dependent semantics of a downstream task and the label-free conditional equivalence of a contrastive task. It explicitly connects to the classic distributional hypothesis from linguistics, providing a clean conceptual framework for thinking about when pre-training helps a downstream task.

4. **Corollary 4.3 — unlabeled contrastive learning recovers downstream semantics under alignment.** By chaining the alignment hypothesis with Theorem 4.2, the paper shows that an optimal contrastive model encodes downstream semantic equivalence exactly (if and only if). This is a clear, testable prediction about when and why contrastive pre-training produces useful representations.

5. **Controlled synthetic experiment that satisfies all theoretical assumptions (Section 5).** The ModAdd/CModAdd setup is cleanly designed so that the alignment hypothesis and conditional equivalence hold by construction. Figure 2a directly validates Theorem 4.2 by showing that distances between semantically equivalent symbols decrease during training while distances between non-equivalent symbols do not. Figure 2b shows that the pre-trained embeddings accelerate downstream classification, confirming practical relevance in this controlled setting.

6. **Honest threats-to-validity discussion (Section 7).** The paper candidly acknowledges that its key assumptions (conditional equivalence, alignment hypothesis) are "often too strong for practical applications" and discusses the gap between theory and practice. This transparency strengthens the credibility of the theoretical contribution.

## Weaknesses

### Fatal
None.

### Major

1. **Strong assumptions limit practical applicability, and no relaxation analysis is provided.** The paper's core results (Theorems 3.1, 4.2, Corollary 4.3) rely on two very strong conditions: (i) exact conditional equivalence (∀ρ: p(ρ|u)=p(ρ|v)) and (ii) perfect distributional alignment (Definition 4.1). The paper acknowledges in Section 7 that these "are often too strong for practical applications" but does not analyze how the results degrade when the assumptions are partially violated. For instance, there is no bound on downstream error as a function of the divergence between context distributions or the degree of misalignment. Without such analysis, the theory makes no testable predictions for realistic scenarios where alignment is partial — which is almost every practical setting.

2. **Experimental validation is far too thin for the paper's broad title and claims.** The only experiment is on a synthetic modular-addition task with tiny parameters (N=16, k=8, d=8). The title "Contrastive Learners Are Semantic Learners" asserts a general property, but the paper provides no experiments on images (e.g., CIFAR-10/100, ImageNet), text (e.g., GLUE), or audio — the very modalities where contrastive learning is known to succeed. The alignment hypothesis is not tested on any standard benchmark, so it is entirely unclear whether this framework applies beyond the toy setting where the authors explicitly engineered the alignment. Furthermore, training runs for 10,000 epochs on this tiny dataset, raising the concern that the observed behavior is an artifact of near-perfect optimization on a trivial problem rather than a general property.

### Minor

3. **The labeled variant (Section 3) has unclear relevance to standard contrastive learning.** The architecture in Section 3 feeds labels as inputs to the encoder (E: P × 𝒴 → ℝ^d). This is an unusual setup — if labels are available, a standard classifier would be a more natural approach. The authors use it as a pedagogical stepping stone to the unlabeled case, but it is never tested empirically, and the paper does not justify why this particular construction (rather than a direct analysis of the unlabeled case) is needed.

4. **Potential off-by-one inconsistency in the experiment.** The paper states that symbols range over {0,…,N} where N=16 (so 17 symbols: 0–16), but the embedding matrix is specified as size N×d = 16×8. This suggests a possible off-by-one error in the implementation or a typo. At minimum, the relationship between N and the symbol vocabulary size should be clarified.

5. **Figure 2a lacks statistical reporting.** Figure 2a (embedding distances over training) does not report confidence intervals or the number of independent seeds used. Figure 2b correctly reports "mean and 95% confidence interval of 5 models," so this standard is already set — Figure 2a should follow the same protocol.

6. **Lack of deep engagement with prior theoretical work.** The Related Work section (Section 8) lists many prior theoretical analyses of contrastive learning (Arora et al., HaoChen et al., Wang & Isola, Tosh et al., etc.) but offers only a single-sentence differentiation: "Compared to these works, our analysis stems from the notion of semantic equivalence." The paper would benefit from a more substantive comparison — for example, showing how the alignment hypothesis relates to the latent-variable assumptions in HaoChen et al. or the downstream loss bound in Arora et al.

### Trivial

7. **Underspecified architecture details.** The encoder is described as a "3-layer transformer encoder" but the number of attention heads, hidden dimension, and activation function are not reported. These details matter for reproducibility.

## Nice-to-Haves

- Provide a bound or analysis showing how the embedding distance behaves when conditional equivalence holds only approximately (e.g., D_KL(p(ρ|u) ∥ p(ρ|v)) ≤ ε).
- Test whether the alignment hypothesis approximately holds on a standard dataset (e.g., CIFAR-10 augmentations for contrastive learning, class labels for downstream task) to demonstrate the theory's applicability beyond synthetic data.
- Compare the semantic-equivalence perspective to the latent-variable models of HaoChen et al. (2021) explicitly — for instance, show that the alignment hypothesis can be derived from a shared latent structure, which would unify the two frameworks.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The alignment hypothesis effectively assumes the conclusion."** The harsh critic claimed the core result is near-tautological. This overstates the case: Theorem 4.2 non-trivially shows that the InfoNCE objective's optimal solution collapses conditionally equivalent symbols, and the alignment hypothesis bridges a label-dependent relation to a label-free one. The hypothesis is a condition, not a concealed conclusion. The result is not tautological; it is conditional on a strong but clearly stated premise.
- **"Proofs are missing from the main text"** and **"paper references an appendix (stripped)"** — Removed per policy: the parser strips appendix content from all papers; these sections exist in the original submission.
- **"Figure 1b (not fully visible due to parsing)"** — Removed: parser artifact, not a paper flaw.
- **"The image examples are misleading because contrastive learning operates on whole images"** — The paper explicitly frames symbols as patches and contexts as the rest of the image (Section 2), so the critic misreads the setup. Removed.
- **"The notation inconsistency between Equation 2 and Equation 3"** — The paper explicitly says "Now, suppose we aim to minimize the loss in Equation 2 without access to the labels. Then we minimize the following:" making the switch clear. Removed.
- **"If labels are available, one would normally train a classifier directly"** — This is a comment about the labeled variant's motivation but ignores its role as a pedagogical stepping stone. Demoted but incorporated as Minor weakness #3 above rather than a standalone point.
- **"The paper does not specify whether the alignment hypothesis holds for ImageNet + SimCLR"** — This demands the paper solve a problem outside its stated scope (a theoretical paper with a controlled experiment). Removed.

## Novel Insights

The harsh critic's observation that the labeled variant (Section 3) is structurally disconnected from standard contrastive practice is insightful but not a novel observation — it is essentially a scope question. The strength finder's observations are mostly faithful restatements of the paper's own contributions. No genuinely novel insight emerges from the reviews beyond what the paper itself provides.

## Suggestions

1. **Add a relaxation analysis.** Derive a bound on the embedding distance (or downstream error) as a function of a divergence measure between context distributions, or the degree of misalignment. This would move the theory from "if-and-only-if under perfect conditions" to "approximately recovers semantics under approximate conditions."
2. **Validate on at least one standard benchmark.** Show that the alignment hypothesis approximately holds for, e.g., SimCLR on CIFAR-10 with downstream class labels, by measuring whether symbols (augmented views) that are conditionally equivalent under the contrastive distribution are also semantically equivalent for the class-label task.
3. **Tone down the title and framing** to match the experimental scope, e.g., "A Semantic Perspective on Contrastive Learning: Formalization and Conditions" rather than the categorical "Contrastive Learners Are Semantic Learners."
4. **Clarify the N=16 vs. symbol-count inconsistency** and add statistical rigor to Figure 2a (error bars, multiple seeds). Report transformer encoder hyperparameters (attention heads, hidden size, activation).
