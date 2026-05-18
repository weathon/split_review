- Decision: Reject
- Scores: 3, 3, 5, 5

## Merged Review

### Summary

The paper introduces SparseDiff, a diffusion-based graph generation model that leverages sparsity during training by using a noise model that preserves sparsity, a sparse message-passing transformer that predicts only a subset of edges per forward pass, and a loss computed on a sampled subset of node pairs. During sampling, the model iteratively covers all node pairs, so complexity remains O(N²). All reviewers agree the paper addresses an important scalability issue in graph diffusion models, but opinions are split on the novelty and thoroughness of the evaluation. Reviewers with lower scores (3) find the contributions incremental and the empirical analysis incomplete; reviewers with higher scores (5) find the method reasonable and the results competitive, but still raise concerns about incremental novelty, missing theoretical justification, and insufficient scalability validation.

### Strengths

- The paper identifies a real open problem – scalability of diffusion models for graph generation – and proposes a method (subgraph/edge-wise sampling + sparse MPNN) to mitigate it during training.
- The core concept of sampling a fraction of node pairs to include in message‑passing and loss computation is sensible and directly addresses training‑cost bottlenecks.
- The development of the model is described clearly; architectural choices (PNa, FiLM, computational graph construction) are demonstrated in detail.
- The related work section is comprehensive, covering both graph generation and sparse/probabilistic techniques.
- The text is generally grammatical and clear (with some exceptions noted in Weaknesses).
- The method shows competitive generation quality on small (molecular) datasets and on large datasets (up to 500‑node community graphs), indicating versatility.

### Weaknesses

- **Incremental novelty.** The noising process is directly taken from DiGress; the idea of performing sparse prediction at each denoising step is taken from EDGE. The paper does not adequately explain how these components are adapted or improved for sparse graph generation, nor what novel insights are gained by combining them. (R1, R2, R3). One reviewer (R2) considers the extension “trivial.”
- **No theoretical guarantees for uniform sampling.** Unlike EDGE’s degree‑informed sampling, SparseDiff uses uniform sampling of node pairs; there is no proof or lower‑bound analysis showing that this sampling strategy can adequately learn the reverse diffusion process. (R3, R4 also note lack of theoretical characterization.)
- **Missing time/efficiency analysis.** The paper claims scalability but provides no runtime comparison (training or sampling) against baselines, nor a theoretical complexity analysis that distinguishes SparseDiff from dense models. Empirical training/generation time on large graphs is absent. (R1, R3)
- **Sampling complexity remains quadratic.** Even though training exploits sparsity, generation still requires O(N²) edge predictions. The method therefore does not scale to very large graphs (e.g., >1000 nodes) without further assumptions. (R1, R4)
- **Incomplete and inconsistent experimental evaluation.**
    - No comparison with GraphARM and SaGess on large graphs, which are the most parallel diffusion‑based scalability‑focused methods. (R2)
    - Baselines are used inconsistently across datasets (e.g., some methods omitted without explanation). (R3)
    - Several results are incorrectly bolded: in the Ego dataset, SparseDiff’s RBF MMD is not significantly better than EDGE; in Table D.6, DiGress has better RBFMMD on Protein and EDGE has better FID on Ego, yet SparseDiff is bolded in both cases. (R3)
    - Reported metrics for EDGE and HiGen on the Ego dataset appear inaccurate; the high normalized MMD of Deg. for EDGE and DiGress requires further explanation. (R1)
    - The benefit of training on large graphs is not demonstrated: can SparseDiff trained on a mix of large and small graphs outperform DiGress trained only on small graphs when the test set mostly consists of small graphs? (R2)
- **Limited scalability validation.** The largest dataset tested (community graphs up to 500 nodes) is still relatively small; the paper’s claim of scalability would be stronger with experiments on graphs with >1000 nodes. (R1, R3). Using QM9 (small molecules) does not support the scalability motivation. (R3)
- **Presentation and clarity issues.**
    - The paper has no appendix, leaving architectural details (e.g., use of PNa and FiLM) and algorithms unclear. (R1, R4)
    - Several typos and grammatical errors (e.g., “Since the noise model is markovian, ~~there~~ the noise does not need”; “We denote by k the edge ratio ~~ratio~~”; “We then evaluate or models”; uncapitalized “markovian”; quotation marks around “no edge”). (R1, R4)
    - Notation is undefined: α^t, β^t in the main equation on page 4 are not defined. (R4)
    - The method is described in pieces; a step‑by‑step algorithm is deferred to a missing appendix, reducing clarity. (R4)
    - The margins may violate formatting guidelines; citations do not link properly when clicked. (R4)
- **Missing discussion of exchangeability** – a concept related to sampling of sparse graphs. (R4)
- **Cannot create continuous node/edge features** – the method is limited to discrete categorical features. (R4)
- **Distribution shift concern.** The method is designed to avoid distribution shift between training and sampling, but it is not explained why exploiting sparsity only during training (predicting “non‑edge” for all pairs at sampling) does not itself cause a distribution shift. (R4)