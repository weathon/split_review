Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

CoreInfer proposes a sentence-level adaptive sparse activation framework for LLM inference that eliminates the need for per-token MLP predictors used in prior work (DejaVu, PowerInfer). The key insight is that "core neurons" (the top-activated neurons for a sentence) exhibit stability and semantic similarity: they remain nearly constant when sentence semantics are stable (long inputs), and semantically similar sentences activate similar neuron subsets. Based on these insights, CoreInfer uses two prediction strategies — stability-guided (reusing pre-filling core neurons during decoding) and similarity-guided (clustering training data by topic to predict core neurons for short/zero-shot inputs) — then fixes the activation map during the entire decoding stage. The paper reports up to 10.33× speedup on a TITAN XP GPU (OPT-6.7b) and 5.5× on an A100 (LLaMA2-70b) while maintaining task performance within a few points of the dense model.

## Strengths

1. **Novel sentence-level sparsity paradigm that removes MLP predictors.** CoreInfer is the first to define and exploit sentence-wise core neurons, enabling zero-cost sparse decoding by fixing the activation map after pre-filling. This directly addresses two limitations of prior token-wise methods: (a) the overhead of repeated MLP predictions per token, and (b) the frequent activation map changes that prevent memory-efficient execution. Table 3 verifies the practical benefit: DejaVu incurs 9.62ms predictor latency and 1.85GB predictor memory; PowerInfer incurs 15.96ms and 3.36GB; CoreInfer incurs none.

2. **Empirical discovery of stability and semantic similarity of core neurons.** The paper demonstrates (Fig. 3) that extending a 256-token sentence by 64 tokens changes core neurons by only ~6%, and that core neurons stabilize as sentences grow past ~200 tokens. On the semantic side, Spearman correlations between core-neuron similarity and semantic similarity reach 0.66 (LLaMA2-7b, STS-B) and 0.51 (LLaMA3.1-8b, SICK) across both ReLU and SiLU activation functions (Table "fig_sementic_simiar"), and clustering visualizations on ag_news (Fig. 4) show topic-based separation of core neurons across layers. These insights are novel relative to prior token-wise activation sparsity work.

3. **Significant and multi-faceted hardware speedups.** CoreInfer achieves 19.83 tokens/s (10.33× over HuggingFace Transformer, 2.71× over PowerInfer) on a TITAN XP for OPT-6.7b, with memory reduced from 12GB to 7.28GB (Table 3). On A100, speedups reach 5.5× over Transformer on LLaMA2-70b (Fig. 6). The combination of memory reduction (fitting models on GPUs that otherwise require CPU offloading), sparse computation, and elimination of the MLP predictor is clearly demonstrated across multiple hardware configurations.

4. **Model and task generality.** CoreInfer is evaluated on 5 models (OPT-6.7b/13b/30b, LLaMA2-7b, LLaMA3.1-8b) and 6 datasets spanning information extraction (Xsum, SQuAD), question answering (TruthfulQA, TriviaQA), and translation (wmt16-de-en, wmt16-ro-en). Performance degradation is generally within a few points of the dense model, and in some zero-shot cases performance improves (e.g., OPT-6.7b TruthfulQA zero-shot BLEU from 7.88 to 9.12), suggesting the approach is not confined to a specific architecture or activation function.

## Weaknesses

### Major

1. **The similarity-guided prediction method is critically underspecified, compromising reproducibility.** This branch is used for all zero-shot tasks (zero-shot QA and translation — a substantial portion of the evaluation), yet the paper provides essentially no algorithmic detail. The description (Section 4.1, lines 238–240) states: "we cluster the training dataset based on this similarity, ensuring that sentences within each group are closely related semantically. Once the input sentence's group is determined, its core neurons are identified by selecting the top γ neurons that appear most frequently within that semantic group." Multiple essential details are missing:
   - **What "training dataset"?** For zero-shot tasks like TruthfulQA, there is no standard training set. Does the method use C4? A subset of the evaluation data? An external corpus?
   - **Clustering method and granularity.** What algorithm (k-means? agglomerative?)? How many clusters? Are cluster assignments per-layer or global?
   - **Inference-time group assignment.** Once trained, how is a test sentence assigned to a group during inference? Embedding similarity with a threshold? Nearest-neighbor? A trained classifier? What embedding model is used (Sentence-BERT? the LLM's own representations?)?
   - **Role of γ vs β.** Are γ and β determined independently? How does γ relate to the frequency threshold across cluster sentences?

   Because the paper does not specify these details, the similarity-guided prediction results (which cover all zero-shot experiments in Table 1) cannot be independently implemented or evaluated. The stability-guided prediction branch is well-specified; the similarity-guided branch is not. This is a significant gap for a core component of the proposed method.

2. **No task-level accuracy comparison against DejaVu or PowerInfer.** The paper's "Baseline" section (line 295) states that it compares CoreInfer with DejaVu and PowerInfer, but Table 1 (task performance) only compares CoreInfer against the original dense model (Ori). DejaVu and PowerInfer appear only in the hardware comparison (Table 3, Fig. 6). Since both DejaVu and PowerInfer also preserve task performance while achieving sparsity (DejaVu reports 93% activation prediction accuracy with negligible perplexity increase), the reader cannot assess whether CoreInfer's sentence-level sparsity achieves a comparable or better efficiency–accuracy tradeoff. It is possible that CoreInfer's semantic-guided prediction, while hardware-efficient, drops more task accuracy than token-wise MLP-based methods. Adding task-accuracy comparisons on a representative subset of datasets (e.g., TruthfulQA zero-shot and wmt16 translation) would substantiate the claim that CoreInfer's sentence-level approach does not suffer relative to baselines on output quality.

### Minor

3. **No direct prediction accuracy metric (recall of true core neurons).** The paper validates the core-neuron prediction indirectly through downstream task performance. While this is the ultimate metric of interest, reporting the recall of the predicted core neuron set relative to the "true" sentence-wise core neurons (computed from the full generated sequence) would provide a cleaner bridge between the stability/similarity insights and the final results. Without it, it is unclear whether the method's success stems from accurate prediction or from the model's robustness to arbitrary neuron dropping. The paper already has the necessary data (pre-filling computation gives the "true" set for the input; the predicted set is either the same or from a cluster); reporting this would require minimal additional effort and would significantly strengthen the paper.

4. **Thin empirical support for the stability insight.** The stability claim (Insight-1) is supported by one experiment: extending a 256-token sentence by 8 and 64 tokens, plus one visualization of a single sentence's core neurons over increasing length (Fig. 3, shown as "lower"). No statistics are reported across multiple sentences, multiple models, or different sentence lengths. While the resulting task-performance results (Table 1) indirectly validate the approach, the exploratory evidence that motivates the method would benefit from broader statistical characterization.

5. **Pre-filling overhead and end-to-end latency not reported.** CoreInfer requires computing core neurons during pre-filling, which involves a full forward pass on the input and top-k aggregation per layer. This cost is not reported anywhere in the paper. Since prior methods (DejaVu, PowerInfer) also run a forward pass during pre-filling (to compute activations for their MLP predictors), the comparison may be fair, but explicitly reporting pre-filling time would allow readers to assess the complete end-to-end cost, especially for short-generation tasks where pre-filling dominates.

6. **The 10.33× speedup on TITAN XP packages multiple sources of gain that are not disentangled.** The speedup over the HuggingFace Transformer baseline (Table 3) reflects at least three factors: (a) fitting the model entirely on GPU (7.28GB vs. 12GB for Transformer, which likely requires CPU offloading), (b) sparse FFN computation, and (c) elimination of the MLP predictor. The comparison against PowerInfer (2.71×) is fair and partially addresses this — PowerInfer also uses sparsity and offloading — but the paper's headline "10.33×" conflates the memory-fit effect with the algorithmic contribution. On the A100 (where models fit on GPU), the speedup drops to 1.5–5.5×, which is a more informative efficiency number. An ablation separating the memory-fit benefit from the sparse-computation benefit would clarify the contribution of each component.

### Trivial

- Minor presentation issues (e.g., "simantics" typo on line 207).
- The parameter β and γ are set per task group (0.2 for IE/QA, 0.4 for translation) based on Fig. 5, but the methodology for choosing these on a new task without a validation set is not discussed.

## Nice-to-Haves

- Compare against an "oracle" sparsity baseline that performs per-token top-k selection without prediction (to quantify how much accuracy is lost due to prediction error, separate from the intrinsic effect of sparsity).
- Report pre-filling time for CoreInfer vs. DejaVu/PowerInfer.
- Discuss failure modes of stability-guided prediction (e.g., when the generated continuation topic-shifts sharply from the input).
- Strengthen the claim of being "first to explore sentence-wise sparsity" with a brief discussion of how this differs from group-wise or input-dependent pruning in prior work.

## Removed Points

These are included for completeness but should be treated with caution; they are either not supported by the paper's text, reflect reviewer knowledge gaps, or are scope-creep demands.

- **Criticism about "no comparison with token-wise sparse inference without MLP" (the reviewer's suggestion to compare against per-token top-k with oracle).** This is a nice-to-have but is not a weakness — the paper's contribution is specifically about sentence-level prediction, and the oracle baseline would conflate oracle-knowledge advantages with the comparison.
- **Criticism that the Spearman correlations (0.42–0.66) are "modest" and "do not guarantee" reliable prediction.** The paper uses these correlations to demonstrate the *existence* of a relationship (not to claim that correlation equals causation), which is a reasonable use. The downstream task results (Table 1) are the real validation, and the correlations are presented as supporting evidence. This criticism overstates the role of the correlation numbers.
- **The harsh reviewer's point about "parameter selection for β and γ is task-specific" being a weakness.** The paper explicitly acknowledges this and provides Fig. 5 showing the parameter impact across tasks. This is standard practice for any method with task-dependent hyperparameters.
- **The suggestion that "stability-guided prediction assumes generated continuation has similar semantics to the input" is a failure mode.** The paper already scopes stability-guided prediction to tasks where this assumption holds (information extraction, few-shot QA, few-shot translation — tasks with long input prompts). This is a reasonable design choice, not an unacknowledged limitation.
- **The Strength Finder's strength about "performance within 2–3% of full model" is mildly imprecise (some drops are larger, e.g., LLaMA3.1-8b SQuAD: 54.3→49.7),** but the overall claim of "negligible performance loss" is supported by the majority of results. The difference is not material enough to discard the strength.

## Novel Insights

The most insightful observation that emerges from reading the reviews against the paper is that CoreInfer's two prediction strategies have fundamentally different levels of empirical support. The stability-guided method is well-specified and validated: the paper explains computationally how to aggregate token-wise core neurons into sentence-wise ones (via β-frequency thresholding), and the pre-filling computation is straightforward. The similarity-guided method, by contrast, is described only at the conceptual level — "cluster the training dataset" — and it takes all the weight for zero-shot tasks, which are arguably the more challenging and interesting scenario. This asymmetry means that the paper's claimed generality rests on a procedure the paper does not actually describe. Closing this gap — even with a simple design choice (e.g., k-means on Sentence-BERT embeddings of C4 sentences, with K=50, assigning test sentences by nearest-centroid cosine similarity) — would dramatically increase the credibility and impact of the work.

## Suggestions

1. **Fully specify the similarity-guided prediction.** Provide: the clustering algorithm and number of clusters, the dataset used for clustering (e.g., C4), the embedding model used for similarity, the inference-time group assignment rule, and how γ is determined. If possible, release the cluster assignments and core-neuron sets to enable independent verification.

2. **Add task-accuracy comparisons with DejaVu and PowerInfer** on at least 2–3 representative datasets (e.g., one zero-shot QA, one translation). This directly addresses the main evaluation gap and shows that sentence-level prediction does not sacrifice task fidelity relative to token-level MLP-based prediction.

3. **Report prediction accuracy (recall of true core neurons)** for both stability-guided and similarity-guided methods across tasks. This would directly validate the core insight independent of downstream task performance and would be cheap to compute from existing data.

4. **Add an ablation isolating the memory-fit benefit.** On a GPU where the dense model fits (e.g., A100), compare: (a) dense baseline, (b) CoreInfer with sparsity, and (c) a version that uses CoreInfer's memory management but computes full activations (if feasible). On a GPU where the model does not fit (e.g., TITAN XP), clarify the Transformer baseline's offloading strategy to help readers separate the memory-effect contribution.

5. **Report pre-filling latency** for CoreInfer and the baselines to complete the end-to-end picture.

## Score and Decision

**Overall assessment:** The paper introduces a genuinely novel approach to activation sparsity — sentence-level prediction without MLP predictors — and backs it with impressive hardware speedups. The stability-guided branch is well-specified and validated. However, two significant weaknesses prevent acceptance in the current form: (1) the similarity-guided prediction method is critically underspecified, making the results for zero-shot tasks non-reproducible, and (2) the paper lacks task-level accuracy comparisons with the very baselines it claims to improve upon. Additionally, the evidence for the core stability/similarity insights is thinner than the claims warrant, and pre-filling overhead is unreported. These issues are addressable with additional experiments and specification, but in their current form they leave the contribution incompletely supported.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>