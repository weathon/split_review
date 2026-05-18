Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper presents a probabilistic graphical model (PGM) interpretation of attention-based Sparse Mixture of Experts (SMoE), framing attention-MoE as a point estimate of a 3-layer hierarchical mixture of experts regression. From this PGM lens, the paper identifies that expert selections are conditionally independent across tokens given the input—a structural property it argues contributes to routing fluctuation (up to 33% of tokens switching experts between late training epochs). To address this, the paper proposes **Mutual-Inform SMoEs**, with two variants: **Similarity-Inform SMoE** (routing decisions are influenced by token-token similarity computed from MoE-layer embeddings) and **Attention-Inform SMoE** (routing decisions leverage attention-head posteriors). The paper provides an entropy analysis (Proposition 1) bounding the entropy of the final routing decision and reports empirical results on Wikitext-103 language modeling and ImageNet classification, claiming improved perplexity/accuracy, reduced routing fluctuation, and enhanced robustness.

## Strengths

1. **Novel PGM framing for understanding MoE routing.** The paper derives attention-MoE as a point estimate of a 3-layer hierarchical mixture of experts (Section 2), revealing the conditional independence structure (e_i ⟂ e_j | X) in the standard setup. This formal lens provides a principled vocabulary for thinking about why tokens may make inconsistent routing decisions and offers a clear theoretical motivation for introducing inter-token dependencies.

2. **Both Mutual-Inform variants demonstrably reduce routing fluctuation.** Figure 2 (Left) shows that both Similarity-Inform and Attention-Inform SMoE achieve substantially lower token-switching rates than the baseline SMoE across all layers. Figure 2 (Right) shows corresponding reductions in routing-score entropy. These results are a clear empirical success that directly supports the paper's central claim.

3. **Performance and robustness improvements across two domains.** On Wikitext-103 language modeling and ImageNet classification, both variants show improvements over baseline SMoE/GLAM/V-MoE models on clean data and on adversarially perturbed/out-of-distribution datasets. The methods improve both perplexity (language) and accuracy (vision) while simultaneously improving robustness metrics (ImageNet-C, -A, -R, -O).

4. **Orthogonal approach to existing stability methods.** The paper correctly notes that its core idea—letting tokens influence each other's routing via similarity—is not addressed by prior work on routing stability (StableMoE, SMoE-dropout, Z-loss, hash layers, linear assignment), making the contribution complementary and potentially combinable with these techniques.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-motivated, theoretically grounded, and empirically supported.

### Minor

1. **The entropy bound's theoretical guarantee weakens under the practical relaxation.** Proposition 1 defines J_i = {j | H(e_j) ≤ H(e_i)} and shows that as τ→0 or σ→0, H(p_i) ≤ H(e_i). However, the paper states "In practice, we relax constraints by letting J_i = {1, ..., N}" (line 250), meaning the final decision p_i can incorporate tokens with *higher* entropy than token i. The theoretical guarantee H(p_i) ≤ H(e_i) no longer strictly holds under this relaxation. While the empirical results in Figure 2 (Right) show entropy reduction in practice, the formal connection between the theory and the deployed algorithm is looser than claimed. The paper should analyze the gap between the constrained theoretical bound and the relaxed practical setting.

2. **No computational complexity analysis.** The similarity matrix computation in Similarity-Inform SMoE requires O(N²) per MoE layer, and the posterior computation in Attention-Inform SMoE involves per-head per-token computations. For long sequences (e.g., 2048+ tokens), this overhead could be significant. The paper does not discuss the added FLOPs, wall-clock time, or memory cost relative to the baseline, which is essential for judging practicality.

3. **No empirical comparison with prior routing-stability methods.** The paper surveys related work on routing fluctuation mitigation (StableMoE, SMoE-dropout, Z-loss, hash layers, linear assignment) and claims orthogonality, but provides no empirical comparison against any of them. While the methods are conceptually orthogonal, the community would benefit from seeing whether Mutual-Inform provides additive gains on top of, say, Z-loss or StableMoE.

4. **The Attention-Inform approximation is drastic and under-justified.** The full posterior from Lemma 1 involves all H attention heads, but the practical method selects only the single head with lowest average entropy, discarding the multi-head integration that is a key strength of Transformers. The justification is computational cost, but no complexity numbers are given to quantify the savings vs. the full posterior, nor is there an ablation showing how much quality is lost by this approximation.

5. **No ablation isolating the similarity mechanism from the PGM framing.** An ablation using a simple heuristic (e.g., averaging routing scores of neighboring tokens without the PGM interpretation) would help establish whether the PGM framing is necessary for the observed gains or whether a simpler weighted-averaging approach suffices.

### Trivial
None of note.

## Nice-to-Haves

- An analysis or ablation showing how performance/complexity trade-offs vary with sequence length, number of experts, and number of attention heads.
- Empirical comparison against at least one prior routing-stability method (e.g., Z-loss or StableMoE) to demonstrate additive gains.
- A discussion of whether the O(N²) similarity matrix can be approximated (e.g., via locality-sensitive hashing or top-k sparsification) for longer sequences.

## Removed Points

- **"Conditional independence claim is incorrect" (Harsh Critic, Critical Issue #1)**: The critic argues that e_i and e_j are not conditionally independent given X because the attention mechanism involves interactions. However, in the PGM G1 as defined, the independence *does* hold: given X (observed), the variables z_i, u_i, and e_i are independent across positions because each token's generative path (X → z_i → u_i → e_i) depends on X only through independent conditional draws. The critic conflates the actual distributed attention computation with the PGM *interpretation* of that computation. The paper is clear that this is a point-estimate interpretation of a generative model—the conditional independence is a *property of the PGM*, not a claim about the raw computation. This criticism is factually incorrect when assessed against the paper's own framework.

- **"Practical algorithms do not follow from the PGMs" (Harsh Critic, Critical Issue #2)**: The paper explicitly derives the weighted-averaging scheme from the PGM through the optimal regression function. Equation (6) (deterministic copying) is a step in the *generative process*, but the *optimal prediction* (Equation 7 and surrounding derivation, lines 139–149) marginalizes over the latent variables, yielding P(d_i = k | U) = sum_j P(e_j = k | u_j) P(s_i = j | U)—exactly the weighted average used in Definition 1. This is standard Bayesian regression. The critic's claim that the PGM "would produce a single expert assignment" misses the distinction between the generative process and the optimal regression/prediction.

- **"Experimental results not evaluable from provided text" (Harsh Critic, Critical Issue #4)**: The tables (Tables 1 and 2) are rendered as image placeholders due to parser limitations in the extracted text. The original submission contains these tables with full numerical results. This is a formatting artifact, not a paper flaw.

- **"33% of tokens claim has no supporting figure"**: The paper states this number in Section 2.2 as empirical motivation and references the full fluctuation analysis in Section 4 (Figure 2 Left), which is present in the original.

- **Notation/style nitpicks**: The minor variation between "Attention-Informed" (used once at line 102) and "Attention-Inform" (elsewhere) and formatting inconsistencies in the LaTeX source are trivial and do not affect understanding.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface an insight not already present in the paper.

## Suggestions

1. **Analyze the gap between the constrained theoretical bound and the practical relaxation.** When J_i is relaxed to include all tokens, state what conditions on the similarity distribution would still guarantee entropy reduction, or provide an empirical analysis showing that the entropy reduction observed in practice is not merely correlational.

2. **Add a complexity analysis table** showing the per-layer FLOPs, memory footprint, and wall-clock overhead of Similarity-Inform and Attention-Inform relative to the baseline SMoE for at least one representative configuration.

3. **Include at least one ablation** that uses simple attention-weighted averaging of routing scores without the PGM derivation, to isolate whether the PGM framing is necessary or whether the empirical gains come from the weighted-averaging heuristic alone.

4. **Empirically compare against one prior stability method** (e.g., Z-loss or StableMoE) on at least the Wikitext-103 benchmark. Even if Mutual-Inform is orthogonal, showing that it provides additive gains on top of an existing technique would substantially strengthen the paper.

5. **Provide the full numeric data** from Tables 1 and 2 in the text (beyond the image) for accessibility, including standard deviations or confidence intervals.

## Score and Decision

This paper makes a solid contribution. The PGM interpretation offers a fresh theoretical perspective on a known problem (routing fluctuation in SMoE), and the proposed Mutual-Inform methods are clean, principled, and empirically effective across two domains. The harsh critic's two main structural criticisms are based on misunderstandings of the paper's PGM framework—both are invalid when checked against the actual paper text. The remaining weaknesses (lack of complexity analysis, limited baseline comparisons, no ablation for the PGM framing, and the weakened theoretical guarantee under practical relaxation) are genuine but minor—they suggest directions for strengthening a revision, not fatal flaws.

The paper's originality is moderate (the PGM lens is novel; the similarity-based routing idea is a natural extension), the claims are well-supported by the presented theory and empirical evidence, and the value to the community is clear: the methods are simple, potentially combinable with existing stability techniques, and could see practical adoption.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>