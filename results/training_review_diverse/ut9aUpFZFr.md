Now I have all the information needed. Let me write the final consolidated review.

## Summary

The paper introduces COINs (Community Informed graph embeddings), a method that uses community detection (Leiden algorithm) to accelerate link prediction and query answering on knowledge graphs by replacing the standard full-entity evaluation with a two-step procedure: first predict the target entity's community, then search only within that community. The approach is model-agnostic (tested with TransE, DistMult, ComplEx, RotatE), and experiments on three benchmark datasets (WN18RR, FB15k-237, NELL-995) show an average 6.4× reduction in evaluation cost with approximately 24% relative performance loss compared to full evaluation.

## Strengths

- **Model-agnostic pipeline with consistent empirical acceleration.** COINs is validated across four distinct KG embedding paradigms (Table 1) and achieves acceleration factors up to 10.3× on a single-CPU-GPU machine (Table 2), with an average reduction of 6.413±3.3587 across datasets. The method does not require distributed hardware, addressing a practical gap for low-resource scenarios.

- **Explicit analysis of how community structure influences scalability.** Figure 2 provides a clear joint visualization of how the Leiden resolution parameter affects both acceleration and overparametrization factors across datasets, with annotated chosen values. This allows practitioners to understand the trade-off and the paper contrasts Leiden with METIS, acknowledging alternative partitioning methods.

- **Proposition 1 gives exact complexity expressions that enable principled analysis.** The derived formula Σ(K+|C_k|)|E_k^test| and the associated bound 2N√|V|—while derived in sketch form in the main paper—provide a concrete target (K = O(√|V|)) for optimal acceleration that motivates the community-based approach beyond heuristic reasoning.

- **Explicit low-resource design goal that differentiates the work from distributed approaches.** The paper clearly positions COINs against PyTorch-BigGraph, DistDGL, SMORE, and tf-GNN, which all assume cluster availability. All experiments are conducted on a single machine.

## Weaknesses

### Fatal
None.

### Major

- **Proposition 2's tradeoff analysis uses a model that does not match the actual evaluation procedure.** The derivation frames H_k — the number of edges evaluated before a correct hit in top-k — as a geometrically distributed random variable with success probability Hits@k(1−ε). However, the COINs evaluation procedure (Algorithm 2, Section 2.3.1) is deterministic per query: exactly K community scores are computed, then all |C_k| entity scores in the predicted community. There is no sequential "trial-until-correct-hit" process, so the geometric distribution does not apply. The expected-cost comparison (E[T′H_k′] < E[TH_k]) is derived under assumptions that contradict the actual pipeline. The condition linking ε to the complexity ratio may be salvageable under a different formulation, but as presented this is a structural issue in the theoretical justification — the paper's abstract explicitly claims "theoretically justified criteria" for applicability, which this proposition is meant to provide.

- **Missing critical baseline: random sampling of the same budget.** The paper compares COINs only to the full baseline (no acceleration). This is necessary but insufficient. The central practical question for a low-resource user is: *given a fixed computational budget of K+|C_k| entity evaluations per query, which method yields the best accuracy?* Without comparing COINs to a simple random-sampling baseline that evaluates the same number of entities per query (K+|C_k| but drawn uniformly), the paper cannot rule out the possibility that the community structure contributes nothing beyond entity-count reduction. The claim of "superior scalability" is only partially substantiated.

- **Key hyperparameters unreported, impairing reproducibility.** The loss weight α in Algorithm 1 (controlling the balance between community-level and entity-level loss) is never specified for any experiment — it is only declared as α∈(0,1). The criterion for selecting the Leiden resolution parameter is described as achieving "optimal balance between scalability and performance" (Figure 2 caption) without stating whether this was based on acceleration, overparametrization, validation accuracy, or some combination. These are not trivial details: α directly affects the training objective, and the resolution choice strongly impacts both the acceleration factor (Figure 2) and downstream task performance, yet the paper does not report how resolution affects query answering metrics (only scalability factors in Figure 2).

### Minor

- **One-time cost of community detection not accounted for.** The Leiden algorithm's computational cost is never measured or even estimated. While this is a preprocessing step amortized over evaluation queries, for a truly low-resource setting this overhead could be significant and should be acknowledged.

- **Practical gap when K deviates from √|V|.** The theoretical optimum requires K ≈ √|V|, but for FB15k-237, K=19 while √|V|≈121. The paper documents this discrepancy (Table 2) but does not discuss how practitioners should intervene or adjust expectations when Leiden produces a far-from-optimal number of communities.

- **Proposition 1's main-paper derivation is a sketch.** The derivation states that "using the KKT theorem, one can prove that extremal configurations only occur when all groups are of equal size" and references Proposition 3 (appendix, stripped by the parser). As presented in the main paper, the derivation glosses over the dependence between |C_k| and |E_k^test| (communities with more nodes naturally have more test edges). While the full treatment likely exists in the appendix, the main paper's presentation risks misleading readers about the tightness and attainability of the lower bound.

### Trivial
None.

## Nice-to-Haves

- **Add a random-sampling baseline** as described above — this is the single most impactful addition to establish the contribution.
- **Report error bars for all metrics** across the 5 seeds mentioned in Section 3.4.3. The abstract's high standard deviation (0.2389 ± 0.3167 for relative error) already hints at problem-specific sensitivity that should be discussed explicitly.
- **Include a small study of resolution vs. query answering performance** for at least one dataset to clarify how the hyperparameter value was selected and how robust the results are to this choice.
- **Acknowledge and ideally measure the one-time cost of Leiden community detection** to give a complete picture of the method's resource requirements.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **SMORE implementation concern** (Harsh Critic, Section-by-Section notes): The reviewer questioned whether the paper adopts SMORE's sampling idea or relies on its implementation. The paper clearly states it applies "the efficient bi-directional rejection sampling algorithm of SMORE" — this is unambiguous about using the algorithm, not the distributed system. Removed as a strawman.
- **Table 3 baseline reproducibility concern** (Harsh Critic): The reviewer suggested the baseline numbers may not have been reproduced. The paper states they were "obtained from running the implementation by Sun et al. (2019)" and Table 3's caption specifies "comparison with baselines with equal hyperparameters." Removed as factually incorrect.
- **Proposition 1 lower-bound rigor criticism** (Harsh Critic, Critical Issue #4): The reviewer claimed the derivation is not rigorous and the lower bound may not be attainable. The paper explicitly states "Proposition 3 gives the details" and "Proposition 4 gives the details" — these full proofs are in the appendix (stripped by the parser). Per the hard rules, criticisms about missing appendix proofs are removed. The remaining concern about the main-paper sketch's clarity is kept in Minor.
- **Convexity claim criticism** (Harsh Critic, Section-by-Section): The reviewer wrote "it is unclear what is convex here." The final embedding refinement in Algorithm 1 (lines 176-178) uses a Softmax-weighted convex combination of embeddings, which is literally a convex operation. Removed as the reviewer misread the algorithm.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the work that the paper itself does not already provide.

## Suggestions

1. **Replace Proposition 2's geometric-distribution model** with a direct cost comparison that matches the actual two-step deterministic evaluation procedure. The condition for when COINs is beneficial can be derived from comparing the total evaluation cost per query (K + |C_k|) to the baseline cost (|V|), adjusted for the accuracy loss from incorrect community predictions — no geometric assumption is needed.

2. **Add a random-sampling baseline** for all dataset×model combinations: for each query, sample K+|C_k| entities uniformly at random and evaluate only those. This isolates the contribution of the community structure from the benefit of entity-count reduction.

3. **Report α explicitly** for each experiment. If α was tuned, describe the tuning procedure; if held constant, state the value and justify it.

4. **Measure and report** the one-time cost of Leiden community detection and discuss its significance relative to the overall computational savings.

## Score and Decision

This is a methods paper introducing a novel acceleration technique for KG inference. The core idea — using community structure for two-step evaluation — is sensible and the empirical results (6.4× average acceleration) are promising. However, the paper's main theoretical contribution (Proposition 2) has a structural flaw in its derivation that does not match the actual evaluation procedure, and the experimental evaluation lacks a critical control (random-sampling baseline) needed to substantiate the claim that the community structure itself drives the favorable tradeoff. These are not minor presentation issues; they affect the validity of the paper's central claims about theoretically grounded applicability and superior scalability. The paper would need substantial revision — particularly a corrected tradeoff analysis and a strengthened experimental comparison — before a case for acceptance can be made.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>