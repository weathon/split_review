Now I have a thorough understanding of the paper and can verify the reviewer's claims against the actual text. Let me produce the consolidated review.

---

## Summary

Mirage proposes a model-agnostic graph distillation method for graph classification that avoids training on the full dataset—a limitation of prior gradient-matching approaches. The key insight is that message-passing GNNs decompose graphs into computation trees whose frequency distribution follows a power law. Mirage mines frequently co-occurring computation trees via FP-Growth and trains GNNs on the resulting tree sets instead of full graphs. Experiments across 7 datasets and 3 architectures show Mirage achieves top-2 accuracy in all 17 architecture–dataset combinations, 4–5× better compression, and ~150× faster distillation than prior methods.

## Strengths

1. **Well-motivated, novel approach that genuinely addresses limitations of prior work.** The paper clearly identifies two real problems with existing graph distillation: (i) reliance on full-dataset training (counter-objective to distillation's premise) and (ii) architecture/hyperparameter dependence. The shift from gradient-matching to compressing the input data itself (computation trees) via frequent pattern mining is creative and principled. As stated in Section 1: "Instead of replicating the gradient trajectory, Mirage emulates the input data processed by message-passing GNNs."

2. **Model-agnostic distillation validated across 3 architectures.** Mirage produces a single distilled dataset that works across GCN, GAT, and GIN without re-distillation. This is a clear practical advantage over baselines. Table 1 shows Mirage achieves top or second-best AUC-ROC in all 17 dataset–architecture combinations—the highest number of top rankings among all baselines (8 out of 17).

3. **Dramatic compression and efficiency gains are well-documented.** Table 2 shows Mirage achieves the highest compression in 5 of 6 datasets (e.g., 318 bytes for NCI1 vs. 26,822 for KIDD and 70,168 for DosCond). Figure 3 shows ~150× faster distillation than DosCond and ~500× faster than KIDD, despite running entirely on CPU.

4. **Clear problem formulation with explicit constraints.** Problem 2 formally defines graph distillation with three practical constraints (model independence, single synthetic dataset, no full-data model training) that prior methods fail to meet. This framing sharpens the contribution.

5. **The sufficiency experiment (Fig. 4a) provides evidence for the core claim.** The experiment—freezing weights trained on full data and comparing losses on full vs. distilled datasets—shows the loss difference approaching zero, supporting the claim that frequent tree patterns capture the essential information. The training loss comparison (Fig. 4b) further corroborates this.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by the experimental results.

### Minor

1. **The training procedure description, while conceptually coherent, lacks sufficient detail for precise reproduction.** The paper states (Sec. 3.4): "we sample a batch of frequent tree sets… utilize the Combine function (Eq. 7) on the embeddings of the root node within each tree." This conveys the core idea, but several details are absent: the exact number of tree sets sampled per batch, how tree-set labels are explicitly assigned (mining "from each class separately" makes this implicit but it should be stated), and the specific θ values used across datasets. The reference to Algorithm 1 (alg:dd_training) is present in the text but the algorithm block is missing from the extracted PDF—likely a parsing artifact. The authors should include a complete, self-contained description of the training loop.

2. **Missing ablation: training on all trees (θ=0) would isolate the effect of frequency-based pruning.** The paper's central claim is that frequent trees are *sufficient* for training. Without comparing against a baseline that trains on *all* computation trees (i.e., no frequency filtering), it is difficult to attribute the results to the frequency mining mechanism versus other aspects of the training setup. An ablation with θ=0 would clarify whether the pruning step is crucial, beneficial, or merely harmless.

3. **Node coverage analysis is absent.** The power-law plot (Fig. 2) shows the distribution of *tree types* across datasets, but it does not show what *fraction of nodes in each graph* belong to frequent trees. If frequent trees cover only a small fraction of nodes in typical graphs, the argument that they "capture a substantial portion of the distribution mass" (Sec. 3, Implications) is weakened. The paper should report, for each dataset, the median/mean percentage of nodes whose computation trees have frequency ≥ θ.

4. **Sensitivity analysis for θ is missing.** The paper notes that θ "may be selected based on the desired distillation size" (Sec. 3.5), but provides no experimental sweep showing how performance and compression vary with θ. A 2–3 panel figure for two datasets would substantially strengthen the paper.

5. **The sufficiency experiment description (Sec. 4.4) is underspecified.** The paper says "pass both the distilled dataset consisting of just the frequent tree patterns and the full dataset" through a frozen model, but does not explicitly state that the distilled tree sets are processed identically to training (Compute root embeddings per tree → Combine → graph-level prediction → loss). While this is inferable from Sec. 3.4, stating it explicitly would improve clarity and reproducibility.

6. **The training–test scale mismatch with SumPool readout is noted but not fully analyzed.** The paper acknowledges Random(sum)'s surprising strength (Sec. 4.2) and provides a plausible explanation (SumPool preserves magnitude differences in node/label counts). However, since Mirage trains on partial node sets (only trees that appear in frequent tree sets) but tests on full graphs, the SumPool readout could produce systematically different logit scales. The paper does not quantify or mitigate this mismatch. An analysis using normalized variants (e.g., MeanPool or comparing per-class logit distributions) would address this concern.

### Trivial

- None that aren't parser artifacts.

## Nice-to-Haves

- A concrete illustration (text or figure) showing exactly how one training batch of tree sets is constructed, how the GNN processes it, and how the loss is computed.
- Reporting the number of tree sets (training examples) in the distilled dataset for each benchmark dataset, alongside the byte sizes in Table 2.
- A brief discussion of whether the method extends to node classification (currently scoped to graph classification).
- A simple experiment on a heterophilous dataset (e.g., Chameleon, Squirrel) to test the limits of the power-law assumption, as acknowledged in the limitations section.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *"The training procedure is critically underspecified, preventing replication and undermining the method's claimed mechanism… Without this, the entire experimental section is uninterpretable."* — This overstates the problem. The paper clearly states the procedure: mine frequent tree sets per class, sample them, compute root embeddings via the GNN, aggregate via Combine (Eq. 7), and compute loss. The core concept is interpretable. The missing Algorithm block is a PDF parsing artifact. The reviewer's characterization as "fatal" is unwarranted.

- *"Algorithm 1 is referenced but not shown in the extracted text… The description 'sample a batch of frequent tree sets' is too vague."* — The absence of the algorithm block is a parsing artifact (removed by the "missing appendix/proofs" rule, since algorithms are commonly mangled by PDF extraction). The description, while concise, conveys the essential steps.

- *"The frequency definition (Eq. 4) counts a tree if it appears anywhere in a graph; this is a binary indicator per graph, not a count. Training later uses 'frequency of occurrence' for sampling—is this the same freq?"* — Yes, it is the same freq(T) from Eq. 4. The paper explicitly states "The probability of selecting a particular tree set for sampling is directly proportional to its frequency of occurrence." This is clear.

- *"Random(sum) is often competitive—the paper… does not explore whether Mirage is essentially learning to mimic a sum-pooled random baseline."* — The paper acknowledges and discusses the Random(sum) phenomenon (Sec. 4.2) and provides a reasonable explanation. In most dataset–architecture combinations, Mirage substantially outperforms Random(sum) (e.g., NCI1-GCN: 68.20 vs. 60.72; DD-GCN: 74.84 vs. 58.02). The concern is not supported by the evidence.

- *Strength Finder claims that are generic or unspecific: filtered.*

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's strengths (novel approach, strong empirical results) and correctly identify missing ablations as the main weakness. The observation that the sufficiency experiment is underspecified is valid but does not invalidate the paper's core claims. The most interesting insight from synthesis is that the paper's weaknesses are all *additive* (missing ablations, clearer exposition) rather than *subtractive* (no result is contradicted or overturned), which means the paper's contribution stands on its existing evidence.

## Suggestions

1. **Expand Sec. 3.4 (Modeling and Inference) into a full subsection** with a written step-by-step description of the training loop (or include the algorithm block explicitly in the main text): (i) mining tree sets per class, (ii) sampling a batch, (iii) computing root embeddings for each tree, (iv) aggregating via Combine, (v) computing loss against the class label, (vi) backpropagation. State the batch size and how labels are assigned.

2. **Add an ablation experiment with θ=0** (all computation trees, no frequency filtering) on 2–3 datasets to isolate the effect of frequency-based pruning.

3. **Add a node coverage analysis**: report for each dataset the mean/median fraction of nodes per graph whose computation trees satisfy freq ≥ θ. This directly addresses whether frequent trees dominate node counts, not just tree-type counts.

4. **Add a sensitivity sweep for θ** on 2 datasets (e.g., NCI1, ogbg-molbace), showing accuracy and compression vs. θ.

5. **Explicitly describe the sufficiency experiment** in terms of the same tree-set-to-graph-embedding pipeline used in training, so the connection is clear.

6. **Address the SumPool scale mismatch** by comparing training-time and test-time logit magnitudes, or by showing results with a normalized readout.

7. **Report the number of tree sets (training examples) in the distilled dataset** for each benchmark, alongside the byte sizes.

## Score and Decision

The paper presents a genuinely novel, well-motivated approach to graph distillation, with strong empirical validation across diverse settings. The weaknesses are presentation gaps and missing ablations, none of which invalidate the core claims. The paper makes a clear contribution to the field.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>