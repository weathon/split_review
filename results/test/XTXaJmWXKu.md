Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

This paper studies nonlinear Independent Component Analysis (ICA) in a continual/sequential setting where domains arrive one at a time rather than simultaneously. It theoretically shows that identifiability of changing latent variables progresses from subspace-level (with n_s+1 domains) to component-wise (with 2n_s+1 domains), and identifies the novel phenomenon that new domains can actually impair partial identifiability — an advantage that continual learning can exploit. The method adapts Gradient Episodic Memory (GEM) to a VAE-based ICA objective to prevent forgetting while incorporating new domains.

## Strengths

- **Empirical validation of the 2n_s+1 identifiability threshold.** In Figure 5a, with n_s=4 changing variables, MCC plateaus at 9 domains, exactly matching the theoretical requirement 2n_s+1 = 9. This direct confirmation of the theoretical prediction is the paper's strongest empirical result.

- **Demonstration that continual learning can outperform joint training when new domains impair partial identifiability.** The controlled experiment (Figure 6) shows that for a variable z_1 that is identifiable with fewer domains, joint training achieves MCC 0.68 while the continual method achieves 0.785 — a clear empirical advantage. This is a genuinely non-obvious finding that challenges the default assumption that joint training is always superior.

- **Novel theoretical insight about repeated distributions and partial impairment.** Remark 1 (|S_i| ≥ 3 for each variable to maintain component-wise identifiability) and the "New domains may impair" discussion in Section 3.2.2 are original contributions that go beyond simply restating prior identifiability results. They provide formal grounding for why sequential learning can be beneficial even when the same total data is available jointly.

- **Robustness to repeated distributions empirically shown.** Figure 5b demonstrates that when one changing variable has only 3 distinct distributions across all domains, the continual method outperforms both joint training and naive sequential training. This validates a practical advantage predicted by the theory.

- **Ablation on prior knowledge of n_s.** Table 1 shows graceful degradation when the assumed number of changing variables ˆn_s mismatches the true n_s, providing practical guidance for deployment.

## Weaknesses

### Fatal
None.

### Major

1. **The theoretical novelty boundary relative to prior work is not sharply drawn.** Lemma 1 is explicitly from Kong et al. (2022), and Theorem 1 uses the same identifiability framework (matrix of log-density derivatives) with the same assumptions. The paper's genuine theoretical contributions — Remark 1 (repeated distributions) and the partial-impairment insight — are presented as informal discussion rather than formal theorems. This makes it unclear to a reader how much of the theory is new vs. repurposed. The core claim that "model identifiability escalates from subspace to component-wise as new domains are involved" is a recombination of existing results (n_s+1 domains → subspace; 2n_s+1 → component-wise) into a progressive narrative. While this narrative is useful, the paper would benefit from a theorem that explicitly states how *sequential* presentation changes the identifiability guarantee compared to the standard joint setting.

2. **The connection between the identifiability theory and the GEM algorithm is heuristic rather than formally justified.** The paper argues that identifiability improves with more domains and that GEM prevents forgetting, but no formal link is established between GEM's gradient constraint (non-increasing loss on previous domains) and the algebraic matrix condition required for identifiability (invertibility of a matrix of log-density derivatives). The algorithm could likely work with any forgetting-prevention method, yet no comparison to alternatives (EWC, replay, distillation) is provided. This makes it impossible to tell whether GEM is necessary, sufficient, or merely convenient.

3. **The empirical evaluation, while supporting theoretical predictions, is too narrow to establish practical applicability.** All experiments use synthetic data with 2-layer MLP mixing functions. Key limitations:
   - No evaluation on real or semi-realistic data (e.g., dSprites, 3DShapes, rotating MNIST).
   - No comparison to other continual learning methods (only joint training and naive sequential).
   - No error bars or confidence intervals shown in any figure (the paper mentions 3–5 random seeds but does not visualize variance).
   - MCC for invariant variables z_c is not reported, even though the subspace identifiability claim (separating changing from invariant variables) is a core contribution.

### Minor
1. **The explanation for why joint training underperforms could be sharper.** The paper states that joint training "shuffles the data" and loses order information, but this conflates two distinct issues: (a) the theoretical identifiability guarantee with all domains together is genuinely weaker for individual variables (the matrix condition changes), and (b) even given the same theoretical guarantee, optimization may converge to a different solution. The paper's argument rests on (a), but the phrasing sometimes suggests (b). Making this distinction explicit would strengthen the argument.

2. **The sensitivity of GEM's gradient projection on the VAE's KL regularization is not discussed.** Since the ELBO includes KL terms, projected gradients that avoid increasing previous-domain loss might push the model into regions where the KL regularization behaves unstably. Whether the KL loss remains bounded across domains is not reported.

3. **No guidance on choosing the number of changing variables ˆn_s in practice.** The ablation (Table 1) shows the method degrades with mismatch, but the paper does not propose any heuristic or data-driven approach for estimating n_s. Given that this is acknowledged as "a major limitation," it deserves more treatment.

### Trivial
- The matrix in Lemma 1 has an apparent notational inconsistency in the k-th row: the φ′′ terms are indexed at (1,0) while the φ′ terms are indexed at (k,0). This should be harmonized (both should be at (k,0)) for clarity.
- Minor: the paper uses both "n" and "n_s" for dimensionality; the relationship between latent dimension n and changing-variable dimension n_s could be stated more cleanly upfront.

## Nice-to-Haves
- Evaluation on a non-synthetic benchmark (e.g., varying-color dSprites) would significantly strengthen claims of practical relevance.
- Comparison to at least one alternative continual learning method (e.g., EWC or replay) would help isolate whether GEM's specific gradient projection is needed.
- Reporting MCC for invariant variables z_c would complete the validation of the subspace-identifiability claim.
- A discussion of GEM's computational cost (storing gradients from all previous domains, scaling with T) is relevant for practitioners.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Criticism about "φ_i''(2n_s,0) when the index should refer to domain number, not 2n_s * n_s"**: 2n_s is a valid domain index (domain number 2n_s, giving 2n_s+1 total domains with reference domain 0). The critic misread this notation.
- **Criticism that the paper uses vague domain terminology**: The paper's use of "domain" to mean a specific value of u is consistent; references to "domain changes" are coherent within this framing.
- **Criticism that the paper "never states clearly what new theoretical insight it contributes"**: The paper does state these contributions (Remark 1, the partial-impairment insight, the subspace → component-wise escalation), though they could be presented more formally.
- **Notation/style nitpicks** (typos, "k appears in some places but not others"): These are parser artifacts or minor presentation issues that do not affect the scientific content.
- **Request for theoretical proof of sequential identifiability guarantee as a separate theorem**: This is a reasonable ideal but overstates the severity — the paper's theoretical contribution is valid even without this formalization, as the identifiability escalation and partial-impairment insights are the substantive novel elements.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Sharpen the theoretical contribution statement.** Clearly delineate which results are from prior work (Lemma 1 from Kong et al. 2022), which are new (Theorem 1, Remark 1, the partial-impairment analysis). Consider formalizing the partial-impairment insight as a proposition or corollary with clear conditions.
2. **Expand the experimental evaluation along three axes:** (a) add at least one real or semi-realistic benchmark, (b) include at least one alternative CL method (EWC is a natural choice), (c) add error bars/confidence intervals to all figures.
3. **Report MCC for invariant variables z_c** to validate the subspace-identifiability claim that changing and invariant variables can be separated.
4. **Add a brief analysis of the GEM gradient projection's effect on the VAE's KL term** to ensure stability.
5. **Clarify the explanation of why joint training underperforms** by distinguishing the theoretical guarantee argument from the optimization argument.

## Score and Decision

The paper addresses a novel and well-motivated problem (continual nonlinear ICA), makes genuine theoretical contributions (especially the partial-impairment insight and the repeated-distributions analysis), and provides empirical evidence consistent with its theoretical predictions. However, the experimental validation is too narrow (synthetic data only, one CL method, no error bars, no z_c evaluation) and the theory-practice gap (identifiability matrices → GEM gradients) is not bridged. The paper has clear merit and I expect it to influence future work, but the empirical case needs strengthening.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>