Now I'll produce the final consolidated review.

## Summary

This paper connects GNN expressive power for LPs to the distributed LP algorithm literature. It establishes a two-way equivalence between d-round distributed LP algorithms and d-depth GNNs, designs a new distributed algorithm (Algorithm 2) that handles dense rows/columns by deleting them and solving a reduced sparse sub-instance, and proves (Theorem 3) that constant-depth, constant-width GNNs suffice to approximately solve almost all sparse binary LP instances under a uniform-random-matrix average-case model, circumventing a worst-case lower bound. The theoretical contribution is a novel synthesis of distributed computing and GNN theory for LPs.

## Strengths

- **Principled two-way equivalence between distributed LP algorithms and GNNs (Section 2.2).** Prior work connected GNNs to specific optimization algorithms in only one direction. This paper establishes both directions: any d-depth GNN can be computed by a d-round distributed algorithm (giving Lemma 1's lower bound via the Kuhn et al. 2016 impossibility result), and any d-round anonymous distributed LP algorithm can be simulated by a d-depth anonymous GNN via universal approximation of MLPs. This framing enables importing a body of distributed LP results directly into the GNN analysis.

- **Novel distributed algorithm (Algorithm 2) with a complete correctness proof (Sections 3.2–3.3).** The algorithm introduces a two-phase strategy: detect γ-dense rows/columns, delete them along with intersecting columns to obtain a row-sparse column-sparse reduced instance, run Algorithm 1 on the reduced instance, and reconstruct the full solution. The correctness proof (Claims 1 and 2, equations 338 and 344) shows that the reconstructed primal and dual solutions achieve (1+ε)-approximation under the conditions of Lemma 2. This algorithm is not present in prior work and directly enables the main theorem.

- **Average-case probabilistic analysis with explicit concentration bounds (Lemma 2, Section 3.1).** The paper bounds binomial coefficient ratios to show Pr[Z_k^i] ≤ 2^{-(k-2β)} and then applies Markov's inequality to obtain high-probability bounds on the number of γ-dense rows, columns, and intersecting columns. This allows the paper to circumvent the worst-case impossibility result (Lemma 1) and prove that constant depth suffices for almost all instances — a distinction no prior GNN-for-LP work made.

- **Concrete depth and width bounds (Remark 3).** The paper provides explicit expressions for the GNN depth (e.g., depth ≤ 10γβ·log(γαβ)/ε²), with a worked numerical example. This shows the result is not purely existential and gives practitioners guidance on the theoretical guarantees.

## Weaknesses

### Fatal
None.

### Major

1. **Experiments overclaim validation of Theorem 3.** The paper states (line 351) that the experiments "validate our main theoretical results, namely Theorem 3." However, Theorem 3 is an *existence* claim about a GNN with hardcoded weights obtained by unrolling Algorithm 2. The experiments train a separate GNN with learnable parameters using Adam on 100 training samples — these are fundamentally different objects. Showing that a 5-layer GNN trained from random initialization achieves low training loss does *not* constitute evidence for the specific constructed GNN whose existence Theorem 3 asserts. The experiments test *learnability* of the architecture derived from Algorithm 2, which is interesting but different from validating the theoretical construction. To properly support Theorem 3, the paper should either instantiate Algorithm 2 as a fixed-weight GNN and test its approximation ratio, or honestly reframe the experiments as testing whether the architecture can be learned from data.

2. **Large gap between the proven constant depth and the notion of "shallow" GNNs the paper aims to explain.** Remark 3 gives an explicit bound of 54079 layers for a 2-approximation on 99% of instances where m=n and nnz(A)=20m. The motivating empirical phenomenon (Li et al., 2024a) uses a *4-layer* GNN. While 54079 is technically constant-depth (it does not grow with problem size), the paper's title and framing promise an explanation of why *shallow* (fewer than ten layers) GNNs work. The paper acknowledges this gap (line 146: "While the theoretical constants may be large") and appeals to the empirical 5-layer results — but as noted in point 1, those results come from a learned GNN, not the constructed one. The gap between 54079 and 4–5 layers is roughly four orders of magnitude, and the paper does not provide any argument or mechanism to bridge it.

### Minor

3. **The distributed-algorithm-to-GNN simulation argument is presented as an assertion without explicit justification of the constant-width claim.** The paper states (line 134) that "by utilizing the universal approximation property of MLPs, any d-round (anonymous) distributed LP algorithm can be simulated by a d-depth (anonymous) GNN." It then claims the resulting GNN has constant width. However, the universal approximation theorem guarantees existence of an MLP approximating a given function, but width can grow with the function's complexity. The paper does not discuss whether the specific algorithms' messages (which in the LOCAL model can be arbitrarily long in general) fit within a fixed-width architecture. For the algorithms actually used (Algorithm 1 and Algorithm 2), the message sizes happen to be bounded, so the concern is manageable — but the paper's general claim is stated without qualification, and the constant-width justification for the specific algorithms is not spelled out.

### Trivial

- The pseudocode of Algorithm 2 (lines 253–267) contains garbled formatting (the "sleep" flag is partially defined, the return statements refer to undefined variables like `sleep j∈Ni′ 1A′`). The prose description (lines 291–309) is clear enough to understand the intended algorithm, but the pseudocode should be cleaned up for the final version.

## Nice-to-Haves

- Running the fixed-weight construction from Algorithm 2 (with no learning) and reporting its approximation ratio on random sparse binary LP instances would cleanly separate the existence claim from the learnability question.
- Including standard deviations or confidence intervals across multiple random seeds in the experimental results would strengthen the empirical evaluation.
- Discussing whether the GNN needs global knowledge of the sparsity parameters γ, β, α or whether these can be estimated locally would clarify the practical implementation.

## Removed Points

These points from the input reviews were removed after cross-checking against the paper:

- **"Average-case model does not match empirical phenomenon"** (from Harsh Critic's Critical Issue 2): Removed. This is scope creep. The paper clearly delimits its scope to sparse binary LPs (line 32: "such sparse binary LPs can model the fractional versions of many basic combinatorial optimization problems"), and Remark 2 explicitly describes the chain of reductions from general LPs. Criticizing the model for not matching the PageRank example (which was only used as motivation) demands the paper address problems outside its stated scope.

- **"Only one baseline (GCN) compared"** and **"No comparison to prior GNN architectures from L2O literature"**: Partially removed. The paper's focus is theoretical; the experiments are secondary validation. While adding baselines would strengthen the paper, the absence is not a core flaw given the paper's nature.

- **"Experimental validation" as a claimed strength** (from Strength Finder): Removed because it conflicts with the verified major weakness that the experiments test learnability, not the theoretical construction.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the review process is the structural tension the paper exposes: the same constant-depth result that is a strength from a theoretical existence perspective becomes a weakness when evaluated against the empirical phenomenon it aims to explain. The paper proves that depth *does not grow with n*, which is a genuine theoretical advance over prior polynomial-depth lower bounds. But the price of this average-case circumvention is that the constants become large enough (54079) that the result explains "constant-depth works" but not "shallow works." This suggests that a genuinely explanatory theory for 4–5 layer GNNs may require a different kind of argument — perhaps one that leverages problem-specific structure beyond sparsity, or one that shows gradient descent on GNNs implicitly realizes a more efficient algorithm than the explicit construction.

## Suggestions

1. **Reframe the experiments.** Explicitly state that they test whether the *architecture* derived from Algorithm 2 can be effectively trained, not that they validate Theorem 3's existence claim. If feasible, also test the fixed-weight construction.
2. **Address the constant gap.** Either show that for realistic parameter regimes the required depth is much smaller than the worst-case bound 54079, or honestly acknowledge that the theory explains "constant depth suffices" rather than "shallow depth suffices" and discuss what additional assumptions could close the gap.
3. **Spell out the constant-width justification** for the specific algorithms used (Algorithm 1 and Algorithm 2), noting that their messages are bounded-length and the MLP operations are simple.
4. **Clean up Algorithm 2's pseudocode.**

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>