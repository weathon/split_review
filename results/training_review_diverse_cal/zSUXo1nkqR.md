Now I have the full paper content. Let me carefully verify each claim from the reviews against the actual paper text before writing my consolidated review.

---

## Summary

TreeX proposes a method for global-level GNN explanations that extracts graphical subgraph concepts by mining over the rooted subtrees naturally generated during message-passing (rather than enumerating subgraphs). The approach clusters node embeddings (as subtree representations) into local concepts, clusters those into global concepts, and learns per-class weights to produce global rules applicable to individual instances. The work addresses an important and under-explored problem—producing interpretable, graphical global explanations for GNNs—with a clever and well-motivated technical approach.

## Strengths

1. **Novel approach to global graphical explanations via subtree structure.** TreeX exploits the correspondence between L-layer node embeddings and full L-hop rooted subtrees in MPGNNs to avoid NP-hard subgraph enumeration or matching. This is a principled reduction: from searching over subgraphs to clustering over rooted subtrees (exactly N per graph with N nodes), which is a concrete algorithmic contribution that distinguishes TreeX from prior global methods that produce latent vectors or language rules.

2. **Theoretical justification for root-node-embedding-as-subtree-embedding.** Theorem 4.2 proves that for injective AGG and UPDATE functions (satisfied by maximally powerful MPGNNs like GIN), the l-th layer node embedding is a Perfect Rooted Tree Representation of the full l-hop subtree. This result, established via mathematical induction, provides a rigorous foundation for the method's core design choice and avoids the need for auxiliary subgraph re-encoding mechanisms used by prior explainers.

3. **First global GNN explainer producing clear subgraph concepts with dual global+local applicability.** On BA-2Motifs, TreeX correctly recovers the five-node cycle motif (Class 0) and house motif (Class 1) as global concepts, while existing global baselines (GLGExplainer, GCNeuron) produce only latent vectors or human-defined rules (Figure 3). Furthermore, TreeX provides an explicit algorithm (Section 4.3) to apply these global concepts to individual instances—a capability no prior global method supports—enabling fidelity evaluation that other global methods cannot produce.

4. **Strong empirical fidelity against state-of-the-art local explainers.** Tables 1 and 2 show TreeX achieves near-perfect AccFidelity (e.g., 1.000 on BA-2Motifs and BAMultiShapes) and the best ProbFidelity on Mutagenicity (0.055) and NCI1 (0.074), outperforming the leading local explainer EiG-Search on real-world datasets. This provides quantitative evidence that global concepts can faithfully reproduce GNN behavior at the instance level.

5. **Practical utility for diagnosing incorrect predictions.** Table 3 reports the rate of predicting true labels using TreeX's class-specific explanations for originally misclassified instances (e.g., 0.847 on BA-2Motifs). Figure 4 provides a concrete case study showing how Concept 2 causes a false negative—a capability not offered by existing explainers.

6. **Substantial efficiency advantage.** Table 4 shows TreeX runs 3 orders of magnitude faster than SubgraphX (0.003s vs. 2.856s per instance on BA-2Motifs) while being competitive with the most efficient local method, despite producing richer global-level explanations.

## Weaknesses

### Fatal

None. No identified flaw invalidates the paper's core claims.

### Major

1. **GNN architecture is not explicitly specified in the main paper, creating a gap between theory and practice.** The paper states its scope clearly ("we focus on explaining the maximally powerful MPGNNs," Section 4, line 54) and identifies GIN as the canonical example (Equation 2). Theorem 4.2 requires injective AGG/UPDATE. However, the main text's experimental setup (Section 5.1) does not explicitly state which GNN architecture, number of layers, hidden dimensions, or training procedure was used. Without this information, readers cannot verify that the experiments respect the theoretical condition, nor can they reproduce the results. While the appendix may contain some of these details (the parser strips appendix content), the main paper should at minimum state the architecture used and confirm it satisfies the injectivity condition. This is a significant reproducibility gap.

2. **No quantitative evaluation of global concept quality.** The paper's central claim is providing *graphical subgraph concepts* as global explanations, yet the evaluation of these concepts is entirely qualitative (Figure 3 and accompanying text). For synthetic datasets (BA-2Motifs, BAMultiShapes) where ground-truth motifs are known, metrics such as subgraph-level precision/recall, overlap (Jaccard on edges), or the fraction of runs where correct motifs appear among top-weighted concepts could and should be reported. The paper states that TreeX "accurately extract[s] the critical global motifs" but provides no quantitative backing for this claim. The fidelity metrics (Tables 1, 2) indirectly validate local faithfulness but do not measure whether the extracted *global concepts* themselves are correct, complete, or consistent.

### Minor

1. **Equation (6) notation is ambiguous.** The expression `\hat{y}_i = Ψ(w_t K_i M)` uses an undeclared multiplication convention. `w_t` is a vector of length `\hat{m}`, `K_i` is a vector of counts (also length `\hat{m}`), and M is a stack of concept embeddings (size `\hat{m} × d`). The text's description ("weighted sum of the global graph concepts," line 103) clarifies the intent—a weighted combination producing a d-dimensional embedding fed to Ψ—but the notation as written is formally unclear. Additionally, the paper should specify the data split used for training the weights `w_t` versus evaluating fidelity, since training and evaluating on the same split would create circularity.

2. **Factual overstatement about subgraph enumeration complexity.** The paper claims there are "up to N! possible subgraphs" (lines 23, 112). The number of subgraphs (edge subsets) is at most 2^{|E|}, not N!. The core point—that subtree enumeration (O(N) per graph) is far more efficient than subgraph enumeration (exponential)—remains valid, but the specific number is incorrect and should be corrected.

3. **Hyperparameters and their sensitivity not reported.** The values of `k` (number of local clusters per graph), `m` (number of global clusters), and `λ` (L2 penalty coefficient in Equation 7) are not stated. A sensitivity analysis would strengthen the paper by showing how robust the method is to these choices. (If these details are in the appendix, they should be cross-referenced explicitly in the main text.)

4. **Efficiency complexity claim is not derived.** Section 5.3 claims the redundancy removal complexity is "less than O(e n k)" without a derivation. This should be briefly justified to make the claim credible.

### Trivial

None.

## Nice-to-Haves

- A quantitative metric for global concept quality on synthetic datasets (e.g., graph-edit distance or Jaccard overlap between top-weighted concepts and ground-truth motifs).
- An ablation showing fidelity with uniform weights versus learned weights `w_t` to disentangle the contribution of the concepts themselves from the learned re-weighting.
- A distribution of graph-edit distances between subtrees assigned to the same versus different local clusters, to validate that embedding-space clustering corresponds to structural similarity (a key assumption).

## Removed Points

- **Criticism about "theoretical foundation does not match experimental practice" in the strong form (accusing the paper of likely using non-injective GNNs without acknowledgment).** The paper explicitly states its focus on maximally powerful MPGNNs (Section 4, line 54). The omission is *specifying which architecture was used in experiments*, not a theoretical mismatch. The criticism was downgraded from "critical issue" to Major weakness #1 with the correct framing.
- **Criticism that Ψ cannot process the weighted concept embedding.** The paper describes Ψ as part of f(·) = Φ ∘ READOUT ∘ Ψ(·). A weighted sum of concept embeddings produces a d-dimensional graph-level representation that naturally replaces the READOUT output. This is architecturally plausible, not an error.
- **Criticism that high ProbFidelity "may conflate faithful explanation with a learned post-hoc weighting that overfits to the training data."** This is a reasonable concern (addressed in Minor weakness #1 as a request for data-split clarification), but the critic overstates it as a likely error.
- **Criticism about "clustering in embedding space corresponds to structural similarity" being an additional assumption.** For injective MPGNNs, Theorem 4.2 guarantees a bijection between embeddings and subtrees, so clustering in embedding space *is* clustering of subtree structures. The assumption only concerns whether Euclidean distance between embeddings reflects structural distance, which is standard practice in representation learning.
- **Several minor presentation nitpicks and formatting concerns** that are parser artifacts, not author errors.

## Novel Insights

The most consequential observation spanning the reviews is that TreeX occupies a unique position in the GNN explainability landscape: it is the only method that simultaneously (a) produces interpretable graphical subgraph concepts as global explanations, (b) provides a mechanism to apply these concepts to individual instances for fidelity evaluation, and (c) diagnoses incorrect predictions by revealing which global concepts drive misclassification. This three-way capability is not present in any prior work (GLGExplainer produces latent vectors only; GCNeuron requires human-defined premises; local explainers cannot produce global concepts). The key tension identified by the reviews is that this very novelty demands stronger evaluation—particularly quantitative validation of the global concept quality—which the paper does not fully deliver.

## Suggestions

1. **Explicitly state the GNN architecture, number of layers, and hidden dimensions used in all experiments** in the main paper, and confirm it satisfies the injectivity condition (e.g., "We use a 3-layer GIN with 64 hidden dimensions, whose AGG=sum and UPDATE=MLP are injective, satisfying the condition of Theorem 4.2").
2. **Add quantitative metrics for global concept quality on synthetic datasets:** compute the fraction of runs where the ground-truth motif appears among the top-k weighted global concepts, and report graph-edit distance or Jaccard similarity between top concepts and true motifs.
3. **Clarify the notation in Equation (6)** by using an explicit formulation such as `\hat{y}_i = Ψ(∑_j w_{t,j} K_{i,j} m_{g_j})` and specify the train/validation split used for optimizing `w_t` versus evaluating fidelity.
4. **Report hyperparameter values** for `k`, `m`, and `λ` (at least in a table) and include a brief sensitivity analysis showing how results vary with these choices.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>