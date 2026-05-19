- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6
Now I have a thorough understanding of the paper and can verify the reviewer claims directly against the text. Let me produce the final consolidated review.

## Summary

This paper proposes DGDK, a one-shot generative model for directed graphs. The encoder corrupts node representations via closed-form heat diffusion on the directed random-walk Laplacian, driving them toward a uniform noise matrix. A decoder (Set Transformer + edge MLP) is trained to reconstruct denoised node representations and the adjacency matrix. At inference, a random adjacency matrix (sampled under the training edge density) is diffused and decoded. Experiments are on synthetic directed graphs (Erdős–Rényi, SBM) with ≤21 nodes, comparing against GRAN.

## Strengths

- **Closed-form noising process enables one-shot generation on directed graphs**: The paper derives a nonhomogeneous heat equation with a closed-form solution (Equations 2–5, Proposition 1) that maps the input graph to a noisy representation in a single step, avoiding iterative noising. This is a principled and clean formulation, and existing one-shot models (Spectre, DiGress) cannot handle asymmetric adjacency matrices (Section 4). This is the paper's core contribution.

- **Quantitative outperformance of the autoregressive baseline on directed graph metrics**: On class-conditional generation of non-isomorphic test graphs, DGDK achieves lower squared MMD distances than GRAN on clustering coefficient and Laplacian spectrum (Table 1, Section 5.2), with 100% uniqueness/novelty scores. This demonstrates that one-shot global Laplacian dynamics can capture digraph structure more effectively than sequential local subproblems.

- **Empirical link between learned representations and Laplacian singular vectors**: Section 5.1 and Figure 3 show strong cosine correlation between the leading left singular vectors of \(e^{t\Delta^i}\) and \(e^{t\Delta^i}\mathbf{N}\), providing evidence that the learned node matrix \(\mathbf{N}\) preserves informative global spectral information of the graph.

- **Truncated SVD approximation and ablation on \(\gamma\)**: Section 5.2 shows that a rank-15 approximation of \(e^{T\Delta^i}\) (for n=21) still enables full edge reconstruction, providing a practical path to scaling (Section 5.2). The ablation in Section 5.3 demonstrates that the node decoder (controlled by \(\gamma\)) is necessary for loss convergence—a clean empirical check on the method's design.

## Weaknesses

### Fatal

None. The paper's core claims are not invalidated, though they are empirically undersupported.

### Major

- **Insufficient experimental evaluation**: (a) All experiments use only synthetic graphs (ER, SBM) with at most 21 nodes. No real-world directed graphs (citation networks, Web graphs, DAGs) are tested. (b) Only one baseline (GRAN) is compared against. While the paper explains why Spectre and DiGress cannot extend to digraphs, no simple baseline (e.g., random graph with matched edge density, an adapted GraphVAE, or a directed ER model) is used to contextualize the reported MMD values. (c) No statistical significance or variance is reported for any metric—not a single error bar, confidence interval, or multiple-seed run. It is impossible to assess whether the MMD gaps in Table 1 are reliable or cherry-picked.

- **Unsubstantiated RKBS claim in the abstract**: The abstract states: "Our approach generalizes a special class of exponential kernels...to the non-symmetric case via Reproducing Kernel Banach Spaces (RKBS)." The phrase "RKBS" (or "Reproducing Kernel Banach Space") appears **nowhere in the body of the paper**. If this connection is part of the claimed contribution, it must be developed in the paper; if it is merely a framing remark, it should be removed. Either way, the abstract and body are mismatched on a central claim.

- **Multimodal generation evaluated only qualitatively**: Section 5.3 (a key showcase of the model's capability) provides no quantitative metrics—no MMD, uniqueness, novelty, or mode coverage scores. The entire discussion is based on anecdotal visualization (Figure 4) and informal parameter commentary. For a claimed contribution of generating from multimodal distributions, quantitative evaluation is essential.

### Minor

- **No hyperparameter sensitivity analysis**: The hyperparameters \(T\), \(\alpha\), \(d\), and \(\gamma\) are all acknowledged as important (e.g., \(\alpha=2.3\) gives ~90% noise, \(\gamma \in [1,100]\) works), but no systematic sensitivity study is provided. This weakens reproducibility and understanding of the method's robustness.

- **No scalability demonstration despite SVD approximation claim**: Section 3.2 proposes a truncated SVD to "scale our method to large graphs" and reduce memory, but the largest graph tested has 21 nodes (with \(s=15\)). No experiment on larger graphs (n=50, 100, or more) is conducted, so the scalability advantage is asserted but not demonstrated.

- **Sampling algorithm not validated against alternatives**: Algorithm 1 (described in Section 3.3) uses Bernoulli sampling at the training edge density \(\mu\) as the prior. The paper mentions Dirichlet sampling does not work for multimodal distributions (citing Vignac et al., 2023) but provides no empirical comparison in their setting. It is unclear whether the Bernoulli heuristic would generalize to distributions with non-uniform or structured sparsity.

- **Data augmentation not ablated**: Edge perturbation (Ding et al., 2022) and permutation augmentation are described but never ablated. The paper claims "we experimentally show that using this kind of data augmentation technique does not have a negative impact" (line 110), but no empirical results for this claim appear in the visible portion of the paper.

### Trivial

None.

## Nice-to-Haves

- A simple baseline such as a random directed graph with matched edge density would help calibrate the MMD values in Table 1.
- An ablation replacing the learned \(\mathbf{N}\) with a fixed random matrix would strengthen the claim that learning \(\mathbf{N}\) is beneficial.
- A failure-case analysis (e.g., does the method work for highly modular or hierarchical directed graphs?) would improve understanding of the method's limitations.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Reverse process is not actually used" (Harsh Critic, Critical Issue 3)**: The paper derives the reverse process (Equation 6) and then explicitly states "the decoder does not have access to \(\Delta\) at inference time" (line 72). This is transparent about the design choice. The heat kernel is used to define the noising process, which is the role advertised by the paper's framing. Demoted from "Critical" to removed—the paper does not overstate this connection.
- **"The choice β=0 simplifies"**: This is an acknowledged modeling choice in the paper (line 66: "we consider \(\beta=0\), but our approach can be generalized to any \(\beta\geq0\)"). The criticism does not identify a flaw.
- **"Proposition 1 is stated without proof"**: Proofs would be in the appendix, which was stripped by the parser. Not an author error.
- **"Only synthetic graphs" is repeated as both "experimental evidence too weak" and "missing parts"**: Merged into one weakness above.
- **"No comparison to VAE-based directed graph model"**: The paper already explains why existing one-shot methods cannot be easily adapted (Section 4). Requesting a novel baseline the authors would need to implement from scratch exceeds reasonable evaluation scope for a first paper on this specific method.
- **"Does not discuss directed graph generative models from other communities (e.g., Bayesian network structure learning)"**: This is scope creep; the paper is positioned in the ML graph-generation literature.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a clear pattern: the paper's technical contribution is genuinely novel (closed-form heat diffusion on the directed Laplacian for one-shot generation), but the experimental evaluation is an order of magnitude too thin for the claims made. The main meta-observation is that the disconnect between the ambitious abstract (RKBS, general kernel extension) and the modest experiments (synthetic ≤21 nodes, one baseline) is the paper's most significant weakness—not any flaw in the method itself.

## Suggestions

1. **Expand evaluation substantially**: Add at least one small real-world directed graph dataset (e.g., a citation network, a food web, or a synthetic DAG dataset). Include at least one more baseline (even a simple directed random graph with matched degree distribution). Report all metrics with error bars over multiple seeds.
2. **Quantify the multimodal experiment**: Report per-mode MMD, mode coverage/uniqueness scores, or a similar quantitative measure for the four-mode experiment in Section 5.3.
3. **Either substantiate or remove the RKBS claim**: If the RKBS connection is substantive, add a paragraph or theorem explaining it in the main paper. If it is not, remove it from the abstract.
4. **Add a hyperparameter sensitivity study**: Systematically vary \(T, \alpha, d, \gamma\) on a small validation set and show how performance changes.
5. **Demonstrate scalability**: Run an experiment with n ≥ 50 (even a timing/memory comparison between full SVD and truncated SVD would greatly strengthen the paper's claims about the low-rank approximation).
