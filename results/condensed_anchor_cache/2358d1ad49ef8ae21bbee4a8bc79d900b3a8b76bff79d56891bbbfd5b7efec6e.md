- Decision: Accept
- Scores: 5, 8, 5, 6

## Merged Review

### Summary

The paper introduces a graph generative model that reverses a hierarchical graph coarsening process. Starting from a single node, the model iteratively expands and refines the graph via denoising diffusion, building global structure first then local details. A local version of PPGN is used for efficiency, and spectral conditioning preserves the Laplacian spectrum across scales. Experiments on planar, SBM, tree, protein, and point cloud datasets show state-of-the-art or competitive performance, scaling to at least 5000 nodes, and the method is the first to successfully extrapolate to graphs outside the training distribution.

### Strengths

- **Novel and promising approach**: The idea of reversing graph coarsening for generation is novel and interesting.
- **Multi-scale generation**: The coarse-to-fine expansion captures both global structure and local details, enabling efficient and scalable generation.
- **Local PPGN architecture**: An efficient local version of PPGN is designed to parameterize the expansion and refinement, providing a trade-off between expressivity and computational cost.
- **Comprehensive method development**: The paper discusses and concretizes several design choices: spectrum-preserving coarsening, diffusion model improvements (SDE with pre-conditioning and self-conditioning), and the local PPGN architecture.
- **Strong empirical results**: The method achieves state-of-the-art or comparable results on standard benchmark datasets and scales to graphs with thousands of nodes (at least 5000). A reviewer (R2) rated the paper 8, praising the rigorous formulation and solid experimental results.
- **Extrapolation and interpolation experiment**: The designed experiment demonstrates that the sequential expansion approach outperforms one-shot generation on these tasks, showing better generalization.
- **Spectrum-preserving coarsening**: The design of constraining intermediate graphs to preserve spectral information is a good contribution, likely leading to improved extrapolation and interpolation.
- **Detailed configuration**: Hyperparameters are provided in detail, aiding reproducibility.

### Weaknesses

- **Missing comparisons to key baselines**:
    - The paper does not compare with several relevant scalable or hierarchical methods: **HiGen**, **GraphARM**, **EDGE**, **BiGG** (Dai et al., 2020), **GraphGen** (Goyal et al., 2022), **Graph Bandwidth** (Diamant et al., 2023), and the coarsening-based method of **Guo et al. (2022)**. On the Tree dataset, only two benchmarks are compared.
    - Missing comparison with earlier hierarchical/hierarchical flow models (e.g., *hierarchical normalizing flow for molecular graphs* [1]).
    - Evaluation using **random GNNs** (as in [5]) is recommended for a more comprehensive assessment.

- **Insufficient ablation studies and analysis of design choices**:
    - It is unclear where the performance gains come from due to many intertwined design choices. An ablation isolating the impact of **spectrum-preserving coarsening**, **diffusion model modifications**, and **Local PPGN architecture** is missing. For example:
        - How does performance change if a standard coarsening method is used instead of the spectrum-preserving one?
        - How do different diffusion formulations or pre-conditioning techniques affect results?
        - What is the performance difference between Local PPGN and other GNN architectures?
    - No ablation on the **spectral conditioning** component itself; it is only briefly described and a small experiment appears in the appendix. The connection to spectral graph theory and theoretical guarantees should be elaborated.
    - **Sensitivity to coarsening orderings** is not quantified (e.g., variance across random seeds), and the impact on generation quality is not discussed.

- **Lack of complexity analysis and runtime comparisons**:
    - The paper claims sub-quadratic runtime but does not provide a comprehensive complexity analysis.
    - No comparison of **sampling times** or **training times** with competing scalable methods (e.g., one-shot generation methods) under similar computational resources.
    - The inference step count is unclear: the method uses 256 diffusion steps per expansion step; total steps may be significantly larger than the 1000 steps used for one-shot generation (e.g., GDSS, DiGress). A fair comparison should control total steps.

- **Presentation and clarity issues**:
    - The method is **difficult to follow**; it lacks an intuitive explanation with visual aids. In particular, the transition between expansion and refinement steps is not clearly explained. (One reviewer (R3) found the presentation generally easy to follow, but others noted confusion.)
    - Notation problems: confusion between expansion vector **v** and nodes; dual use of _θ_ for coarsening distribution and model parameters; same symbol _F(G)_ for contraction family and contraction function; “autoregressive” is misused (better terms: recursive/iterative). 
    - Key model components are placed in the appendix, hurting self-containment. The statement “we found that the formulation proposed by Song et al. (2021), supplemented with enhancements from Karras et al. (2022), yielded the most promising results, similarly to the approach used in Yan et al. (2023)” is too vague.
    - A brief paragraph positioning the work with respect to SOTA and highlighting contributions is missing.

- **Equations and probabilistic formulation issues**:
    - Marginalization over expansion orders is incorrectly expressed: the likelihood should be \(P(G)=\sum P(G|\pi)p(\pi)\) rather than summing conditional likelihoods directly. This also affects equations (2) and (3). (R1, R3)
    - The equation after (1) combines two independent distributions, potentially losing information needed to predict \(v_l\); a joint formulation is more rigorous. (R3)
    - The importance sampling equation above (3) requires that the proposal distribution has positive support over all orderings; this condition should be explicitly stated and justified. (R3)
    - A Markov property assumption in the expansion sequence should be stated explicitly: \(P(G_{l-1}|G_l,\ldots)=P(G_{l-1}|G_l)\).

- **Limited evaluation and lack of real-world/molecular datasets**:
    - All datasets used are arguably **synthetic** (planar, SBM, tree, protein, point cloud). Real-world experiments such as **molecule generation** (e.g., QM9, ZINC) are missing. This raises concerns about scalability to datasets with millions of graphs (training time may become prohibitive).
    - No **visualization** of generated graphs is provided, which is important to assess quality (e.g., connectivity, indistinguishability from training data). (R1, R4)
    - For interpolation/extrapolation, only the fraction of valid, unique, and novel (V.U.N.) graphs is reported. Additional **MMD-based metrics** are recommended. (R4)
    - The claim that V.U.N. is the most important metric requires justification.

- **Limitations of the spectrum-preserving local expansion**:
    - The method uses a **fixed number of eigenvalues \(k\)** (principal Laplacian spectrum) during expansion, enforcing a constant global structure while graph size grows. Meanwhile, the local PPGN focuses on dense subgraphs. This may create a gap between the principal spectrum and local details, limiting expressivity for larger graphs.

- **Sensitivity and training cost concerns**:
    - The method depends on random coarsening orderings, which may introduce variance and require **longer training time** to converge compared to one-shot generation. (R3)
    - Handling **batching** across graphs with different coarsening sequences and across expansion steps is unclear and could increase computational burden. (R3)

- **Unresolved design choices and questions**:
    - Why is **SignNet** used for eigenvectors? It is sign-invariant and may be unsuited for edge prediction tasks; it is typically used for graph-level tasks. (R3)
    - The need for a multilevel coarsening that preserves the Laplacian spectrum is not fully justified; could other coarsening methods work? (R1)
    - The benefit of the **added source of randomness** in expansion sequences should be explained. (R1)
    - The relation between \(L=1\) (single expansion step) and existing one-shot diffusion models (e.g., Yan et al., 2023) should be clarified. (R1)
    - How does the **denoising process focus on local details?** Are only subsets of edges noised at each diffusion step? (R1)
    - For modeling \(p(v_t,e_t|G_t)\) as a diffusion process, high-level details are missing: are \(v\) and \(e\) treated as adjacency matrices? How does inverse diffusion work per expansion step? What is the impact on sampling time? (R2)
    - The definition of **edge and neighborhood contraction sets** and how they translate to an ordering is unclear. (R3)