I have verified all claims against the paper. Here is the consolidated final review.

---

## Summary

This paper presents Graph2Tac (G2T), a graph neural network for online theorem proving in Coq. G2T encodes the full Coq environment (definitions, theorems, proof states) as a single directed graph, enabling it to compute embeddings for never-before-seen definitions in real time via a novel definition embedding task. The model is integrated into the Tactician framework and runs on consumer hardware. On a benchmark of unseen Coq packages, G2T with the definition task solves 26.1% of test theorems (vs. 17.4% without it), and when combined with a k-NN solver it reaches 33.2%, demonstrating complementarity between learning from definitions and learning from proof scripts.

## Strengths

1. **Definition task yields a clear, substantial empirical improvement.** The model with the definition task (G2T-Anon-Update) solves 26.1% of test theorems vs. 17.4% for the variant without it (G2T-NoDef-Frozen), an 8.7 percentage-point gain on the challenging unseen-packages setting (Figure 5). This is a direct and meaningful comparison.

2. **Complementarity between G2T and k-NN is convincingly demonstrated.** The aggregate solver G2T-Anon-Update + k-NN proves 33.2% of theorems, exceeding both models individually (k-NN 25.8%, G2T-Anon-Update 26.1%). The Venn diagram (Figure 6) confirms that the two models solve largely disjoint sets of theorems, supporting the claim that learning from definitions (G2T) and learning from proof scripts (k-NN) provide orthogonal benefits.

3. **Faithful graph representation is well-motivated and technically sound.** The mono-graph encodes Coq terms with explicit dependency edges, shared subterms, and no name ambiguity (Section 2). This design allows the model to compute embeddings for new definitions in topological order and update them in real time during inference — a non-trivial engineering achievement.

4. **Comprehensive empirical evaluation for the Coq ecosystem.** The paper compares seven solver configurations (G2T variants, k-NN, CoqHammer, Transformer-CPU, Transformer-GPU, firstorder/auto) on a common benchmark, with analysis against both time and number of model calls. This provides a useful reference for future work.

5. **Practical system, available and reproducible.** G2T is integrated into the Tactician framework and runs on a single CPU without a GPU. The code, dataset, and trained models are released. This makes it one of the few neural theorem provers immediately usable by Coq end-users.

6. **Insightful model-speed analysis.** The per-call plot (Figure 5, right) shows that G2T-Frozen-Def performs similarly to the transformer baselines per model call, revealing that G2T's overall advantage comes from faster inference rather than strictly better prediction quality. This is a nuanced and honest observation.

## Weaknesses

### Fatal

None.

### Major

1. **The two-stage definition embedding design is not ablated against a simpler end-to-end alternative.** The method uses: (a) an embedding table that stores representations for definitions seen during training, then (b) a separate definition model trained via cosine similarity to mimic those embeddings. The paper never tests the natural alternative of skipping the embedding table entirely and training the definition model's output directly for the prediction objective (i.e., using the GNN output as the definition representation for *all* definitions, seen and unseen, trained end-to-end via backpropagation from the prediction loss alone). Under the current design, the definition model and the embedding table are never directly compared. The comparison G2T-Anon-Update vs. G2T-NoDef-Frozen does show that *something* about the definition task helps, but it does not isolate whether the improvement comes from (i) the specific two-stage distillation design, (ii) the extra parameters of the definition model, or (iii) simply having a larger loss term dominate training. Without this ablation, the claimed novelty of the "definition training task" as a specific design is not fully validated. This is the single most important methodological gap in the paper.

### Minor

1. **Loss weight 1000 is used without justification or sensitivity analysis.** The combined loss is ℒ = 1000 ℒ_def + ℒ_tactic (line 118). This factor is large enough to dominate the total loss. The paper reports no experiments varying this weight (e.g., 100, 1000, 10000) and no discussion of how the two tasks interact. While not invalidating the results, this omission weakens confidence that the reported gains are robust to this hyperparameter choice rather than an artifact of an over-weighted auxiliary loss. The fact that G2T-Named-Update (which makes the definition task easier via name embeddings) slightly underperforms G2T-Anon-Update further hints that the balance between tasks is delicate.

2. **Definition-task-only ablation does not fully isolate the contribution of the two-stage design.** As described in Major point 1, the model G2T-NoDef-Frozen removes the definition task entirely, but it still uses the embedding table for seen definitions (trained via the prediction loss). This is a useful comparison but does not answer whether the two-stage distillation design — with its separate embedding table and cosine-similarity loss — is necessary, or whether a simpler architecture where the definition model's output directly serves as the representation for all definitions and is trained end-to-end would work equally well. This limits the internal validity of the claimed methodological contribution.

### Trivial

1. **Minor naming inconsistency.** The text defines "G2T-NoDef-Frozen" (line 124) but Figure 5 and the surrounding text use the label "G2T-Frozen-Def" (line 157). It is clear these refer to the same model, but the inconsistency makes the empirical section slightly harder to follow.

2. **"First comprehensive comparison" is slightly overstated.** The paper claims "To our knowledge, we give the first comprehensive comparison of many symbolic and machine learning solvers in Coq (or any ITP for that matter)" (line 47). While the comparison is genuinely broad, the "first" claims are unnecessary — the empirical work stands on its own merits. The "To our knowledge" qualifier makes this defensible, but it invites unnecessary skepticism.

## Nice-to-Haves

- Report the average inference time cost of computing embeddings for new definitions via the definition model. If a new package introduces hundreds of definitions, this startup cost is relevant to the practical-usability claim.
- Clarify or illustrate with a brief example how the model handles mutually inductive definitions with multiple root nodes. The paper notes that the pooled embedding is concatenated with each root node's embedding separately (line 108), which resolves the question, but it would benefit from a sentence making this explicit.

## Removed Points

These points were raised by reviewers but removed or downgraded after verification against the paper:

- **"Aggregate solver is discussed as if it were a concrete system."** The paper clearly states on line 151 that these are "artificially aggregated solvers" that "simulate running n solvers concurrently." The single use of "combination solver" on line 164 is in the context of discussing results of the simulation, not misrepresenting it. This concern is adequately addressed in the paper.
- **"Transformer baseline should note that larger pre-trained LMs are not applicable."** This is not a weakness; the paper already justifies training from scratch by noting that the setting requires a model compatible with the online inference setup. The reviewer's own framing concedes this is a reasonable choice.
- **"Missing discussion of mutually inductive definitions."** The paper explains at lines 65, 90, and 108 that mutually inductive definitions have multiple root nodes and that the pooled embedding is concatenated with each root node embedding separately, then passed through an MLP to produce a per-root output. The mechanism is described, albeit concisely. This is a clarification issue at most, not a missing discussion.

## Novel Insights

None beyond the paper's own contributions. The reviewers' analysis confirms the paper's main empirical findings (definition task improves performance, complementarity with k-NN) and identifies a methodological gap (two-stage design not ablated against end-to-end alternative) that the authors should address, but does not contribute a new perspective not already present in the paper.

## Suggestions

1. **Add an ablation comparing the current two-stage design against an end-to-end variant.** Train a model where the definition GNN output is used directly as the representation for *all* definitions (no separate embedding table, no definition loss), and the definition model is trained solely via gradients from the prediction task. If performance is similar, the distillation design is unnecessary; if it drops, the current design is convincingly motivated. This is the single most important experiment to add.

2. **Report sensitivity of the combined loss to the weight 1000.** Vary the weight (e.g., 100, 1000, 10000) and report results on the validation set. This would significantly strengthen the defense of the method.

3. **Harmonize model naming.** Use consistent labels between the text and figures (e.g., always use "G2T-NoDef-Frozen" instead of mixing with "G2T-Frozen-Def").

4. **Qualify the contribution scope more precisely.** Instead of "first comprehensive comparison," state "a broad comparison" or "one of the most comprehensive comparisons" — the empirical work is strong enough that it does not need the novelty claim.

## Score and Decision

The paper makes a genuine empirical and systems contribution: G2T is a practical, online GNN-based theorem prover that adapts to new definitions, with thorough benchmarking and a clear finding of complementarity with k-NN. The core weakness is that the claimed methodological novelty (the two-stage definition task) is not ablated against a simpler end-to-end alternative, making it unclear whether the specific design is necessary or merely sufficient. This is a significant methodological gap but not a fatal one — the empirical finding that *something* in the definition task helps is robust, and the system-level contribution (graph representation, online adaptation, integration, benchmarking) stands regardless. The paper would benefit from a rebuttal or revision adding the missing ablation.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>