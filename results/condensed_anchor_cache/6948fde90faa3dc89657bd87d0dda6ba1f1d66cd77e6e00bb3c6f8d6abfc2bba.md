- Decision: Reject
- Scores: 6, 3, 3, 5

## Merged Review

### Summary
The paper introduces the Pointwise Distance Distribution (PDD)—a continuous, generically complete isometry invariant for periodic point sets—into a transformer architecture (Periodic Set Transformer, PST). PST uses PDD rows as tokens (collapsing atoms with identical k-NN distance profiles), weights self-attention and pooling by PDD row weights, and augments the distance features with atomic property embeddings to incorporate composition. The model is tested on lattice energy prediction and on Matbench material property benchmarks. Reviewers are split: one finds the approach promising (score 6), two rate it weak (score 3), and one is moderate (score 5). Key criticisms include insufficient experimental validation, lack of novelty over k‑NN graph methods, missing baselines, unclear experimental details, and clarity issues.

### Strengths
- **Powerful invariant incorporated into neural networks.** The use of the PDD, which is Lipschitz continuous and generically complete, is a creative way to represent periodic crystals (Reviewers 1, 3, 4).
- **Tailored attention mechanism.** The PST modifies self‑attention (PDD‑weighted attention and pooling) to exploit the grouped-row structure of the PDD, which is a novel architectural contribution (Reviewers 1, 3, 4).
- **Competitive performance on some tasks.** The model shows strong results on certain Matbench properties and outperforms several graph‑based baselines (Reviewers 1, 2, 4).
- **Detailed formalization and derivation.** The paper carefully defines the PDD, the spatial encoding, and the transformer modifications (Reviewer 4).
- **Potential for further improvement.** The representation could be pre‑trained and used for crystal structure optimisation (Reviewer 4). (Note: One reviewer found the experiments small‑scale; see Weaknesses.)

### Weaknesses
- **Insufficient experimental validation and missing baselines.**
  - The method underperforms on formation energy (a key material property) compared to methods listed in the results table (Reviewer 2).
  - The Matbench experiments omit the state‑of‑the‑art baselines coGN (Choi et al.) and PotNet (Reviewers 2, 4). No comparison with ElMD (Hargreaves et al.), which also uses Earth Mover’s Distance for composition similarity, is provided (Reviewer 4).
  - The lattice energy experiments (Tables 1, 2) evaluate the PST model on the *training* set for the first two tasks, which is not standard practice and undermines confidence in the results (Reviewer 4).
  - The datasets used for lattice energy (T2, P1, S2, P2M) are never defined, making the results uninterpretable (Reviewers 3, 4).
  - The experiments lack error bars or statistical significance tests (Reviewer 3).
  - The ablation study does not clearly separate the four PDD‑specific components (using PDD rows as tokens vs. weighting attention vs. weighting pooling vs. the initial features). A critical missing ablation is testing a standard transformer on the raw atoms with the same k‑NN distance features and atomic properties, but without the PDD collapse and weighting (Reviewer 1).

- **Limited novelty and unclear distinction from existing methods.**
  - The main contribution appears to be adding composition to the prior PDD descriptor; this is incremental (Reviewers 2, 3).
  - The k‑NN distance matrix used in PST is conceptually similar to the adjacency matrices in graph neural networks (e.g., CGCNN, ALIGNN) that also use distance‑based edges and atomic features. The paper does not adequately justify why this representation offers a significant advantage over those GNNs (Reviewer 2).
  - The PDD representation is not clearly distinguished from other distance‑based structural descriptors, such as radial distribution functions (Reviewer 3).

- **Clarity and presentation issues.**
  - The notation in Section 3 is hard to follow (mixed upper/lower case, different bold fonts) (Reviewer 3).
  - Figures and tables are sparsely labeled, reducing readability (Reviewer 3).
  - The definition of isometry on page 2 appears inconsistent with the standard definition (\(d_S(a,b)=d_Q(f(a),f(b))\)) (Reviewer 4).
  - Definition 3.1 appears to contain an error: the coefficients \(c_i\) are said to be integers in \([0,1)\), which would force them to be zero (Reviewer 1).

- **Missing architectural and experimental details.**
  - It is unclear whether each transformer block includes an MLP (as is standard) or only self‑attention and normalization (Reviewer 1).
  - The details of the Gaussian process regression used in Section 4 (kernel, hyperparameter optimisation) are not provided (Reviewer 3).
  - The process for collapsing PDD rows (how identical rows are identified) and the ordering of rows are not explained (Reviewer 3).
  - No analysis is given of how often PDD rows are actually collapsed in practice, i.e., how much the token aggregation matters (Reviewer 1).
  - The choice of \(k\) (number of nearest neighbours) is a significant hyperparameter, but its selection is only briefly mentioned in the appendix (Reviewers 1, 3).
  - In the lattice energy experiment without composition, the model cannot distinguish two crystals with identical lattices but different compositions, yet the task includes different compositions. This raises doubts about the model’s practical applicability (Reviewer 4).
  - It is not explained why CrabNet (a transformer) cannot be used with PDD embeddings for a fairer comparison (Reviewer 3).

- **Omission of important citations.** The paper does not cite coGN [1] and PotNet [2], which are standard baselines on Matbench (Reviewer 2).