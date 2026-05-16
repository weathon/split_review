Now I have a thorough understanding of the paper and can verify all reviewer claims. Let me produce the final consolidated review.

## Summary

This paper introduces the Mamba Retriever (130M and 1.3B), a discriminative sentence-level retriever built from the Mamba-2 state-space model that processes entire long documents in linear time and selects relevant sentences conditioned on all prior context. It also proposes a link-based synthetic data generation method that leverages natural document connections to create training queries. The Mamba Retriever substantially outperforms state-of-the-art embedding models (NV-Embed-v2-7B, Stella-1.5B, GTE-Qwen2-1.5B) across 41 long-document QA benchmarks, maintains computational efficiency advantages, and shows strong length generalization — approaching GPT-4o's performance on documents exceeding 256k tokens despite being trained on only up to 10k-token documents.

## Strengths

- **Significant and consistent accuracy gains over all embedding baselines**: Mamba Retriever 1.3B achieves 60.0% average accuracy across 41 benchmarks, substantially outperforming the strongest embedding baseline NV-Embed-v2-7B at 48.1% (Table 1). The advantage is robust across three different LLM generators (GPT-4o, Llama-3.1-8B, Llama-3.1-70B) as shown in Table 3, and the comparison is conservative: embedding models and BM25 retrieve 5 chunks (~2000 tokens) while Mamba retrieves 50 sentences (~1600 tokens), a setting that the paper explicitly shows favors the baselines.

- **Impressive length generalization from limited training context**: The Mamba Retriever 1.3B, fine-tuned only on documents up to 10k tokens, maintains strong performance on documents exceeding 256k tokens and approaches GPT-4o's full-context performance (Figure 3). The context size ablation (Figure 4) confirms that full-document context, not just local information, drives this advantage, directly validating the paper's core motivation.

- **Link-based synthetic data generation shows clear benefits over alternatives**: Table 4 demonstrates that link-based generation trains substantially better Mamba retrievers than chunk-based or pair-based approaches (56.4% vs. 50.2% and 52.3% respectively on 500k examples using the 130M model), confirming that leveraging actual document-level connections produces higher-quality training data for learning long-range dependency retrieval.

- **Computational efficiency advantage**: Mamba Retriever 130M processes documents at 2.1k tok/s using 19 TFLOPS, compared to NV-Embed-v2-7B at 1.8k tok/s using 42 TFLOPS (Table 2), demonstrating that the linear-complexity architecture provides both speed and FLOP savings while achieving higher accuracy.

- **Discriminative retrieval strongly outperforms generative retrieval for this task**: Mamba Retriever 130M (discriminative) achieves 53.5% average accuracy, while fine-tuned Mamba-2-130M (generative) using the same training data achieves only 24.1% (Table 5), and larger generative models (GPT-4o, Llama-3.1-70B) also perform worse when asked to retrieve sentences directly.

## Weaknesses

### Fatal
None.

### Major

- **The link-based synthetic data contribution would benefit from stronger validation**: The link-based data is tested only on the Mamba 130M model in the ablation (Table 4), not on the 1.3B model, so it is unclear whether the benefit scales with model capacity. Additionally, the two embedding models fine-tuned on the same link-based data (GTE-Qwen2-1.5B, Contriever-110M) showed no improvement over their pretrained checkpoints. The paper frames this as suggesting "Mamba retrievers learned more than superficial artifacts," but this negative result equally admits the alternative explanation that the data format (sentence-level binary labels) is mismatched for contrastive learning in embedding models rather than being inherently high-quality. The paper does not explore which aspect of this mismatch causes the failure, leaving the generality of the link-based method's value somewhat undersupported.

### Minor

- **Lack of uncertainty quantification for the GPT-4o comparison**: Figure 3 and the associated claim that "Mamba retriever 1.3B approaches GPT-4o full context performance on context over 256k tokens" are presented without error bars, confidence intervals, or any estimate of variance across documents. While this is common practice in large-scale LLM evaluations, the convergence claim is central to the paper's narrative about length generalization and would benefit from at least bootstrapped intervals.

- **Sliding window logit averaging lacks justification**: When documents exceed 120k tokens (Section 5.4), sentences scored in multiple windows have their logit values averaged. The paper does not discuss or ablate whether averaging is preferable to alternatives (max, taking score from the most central window), which could affect retrieval quality on very long documents.

- **The ablation comparing synthetic data strategies is not extended to broader applicability**: The link-based improvement is demonstrated only for Mamba retrievers. Showing that the same data improves a non-Mamba retrieval architecture (e.g., a smaller cross-encoder with a similar binary classification objective) would strengthen the claim that the data itself, not just the Mamba architecture, is responsible for the gains.

- **Decontamination details are incomplete**: The paper does not report how many synthetic examples were removed by the decontamination procedure, making it difficult to assess potential data scarcity or the effective training set size.

### Trivial

- The choice of using the last token of each sentence for classification (as opposed to first token, average pooling, or max pooling) is not ablated or justified beyond architectural consistency. An ablation would be straightforward and would strengthen confidence in the design.

- The paper notes that 500k vs. 1M training examples produce nearly identical performance (59.4 vs. 60.0) but does not investigate whether this saturation is due to model capacity limits or data diversity limits.

## Nice-to-Haves

- A comparison at matched token budgets in the main paper (embedding models with 50 sentences) would be a useful additional reference point, even though the paper shows this setting is weaker for baselines and reports it in the appendix.
- A discussion of whether the LLM-as-judge evaluation (0.942 F1) might have systematic biases toward certain answer styles could be informative, though this is standard practice.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Critical Issue 1 (unmatched granularity/token budget)**: The paper explicitly states (Section 5.2) that "5 chunks" (2000 tokens) achieves *higher* performance for embedding models than "50 sentences" (1600 tokens), and that the authors therefore report the stronger setting for baselines. Since this asymmetry favors the baselines, not the authors' method, per guidelines this criticism is removed. The Mamba Retriever wins despite retrieving fewer tokens, which strengthens rather than weakens the result.

- **Alleged 17.3% accuracy for pair-based generation**: This number does not appear in the paper's main text. The strength finder reports pair-based at 52.3% from Table 4 (the image of which is unavailable). If 17.3% exists in the appendix (which is stripped), it likely refers to a different evaluation (e.g., human-rated question quality), not retrieval accuracy, and the reviewer appears to have conflated the two.

- **Missing cross-encoder/reranker comparison and "compare against a similarly-sized transformer-based generative retriever"**: The paper's scope is comparing against embedding-based retrievers and BM25, which are the standard retrieval baselines for RAG. Demanding additional baseline types is scope creep.

- **Per-dataset results not in main text**: Standard practice to place fine-grained breakdowns in the appendix.

- **Missing comparison with human-authored QA data**: The paper's contribution is a *generation method*, not a dataset. Comparing against existing QA datasets would test a different question (data quality) and is not necessary to validate the method's effectiveness.

- **Claims about no non-embedding retriever comparison**: The paper compares against BM25 (a non-embedding retriever) and various embedding models. The claim that the Mamba is "the first successful transformation of a state-space model into a fine-grained, sentence-level retriever" is a novelty claim about the architecture class, not about non-embedding retrievers generally.

## Novel Insights

The harsh critic raises a genuinely interesting tension: the link-based synthetic data improves Mamba retrievers but fails to improve embedding models fine-tuned on the same data. While the paper spins this as evidence of Mamba learning "more than superficial artifacts," the more parsimonious interpretation is that the data format — binary sentence-level relevance labels — is naturally suited to the Mamba Retriever's discriminative classification objective but ill-suited to the contrastive objective used for embedding models (which needs dense representations of individual sentences). This suggests the method's value may be architecture-specific rather than a general-purpose data contribution. A controlled experiment varying the training objective for embedding models (e.g., training them with a binary classification head rather than contrastive loss) would resolve this ambiguity, but the paper does not attempt it. This is the review's most useful insight: the claimed generality of the link-based data is not yet demonstrated.

## Suggestions

- **Test the link-based data on at least one non-Mamba model with a matching binary classification objective** (e.g., a small transformer with a sentence-level classification head) to separate the contribution of the data from the contribution of the Mamba architecture. This is the single most impactful experiment the authors could add.

- **Report the link-based ablation on the 1.3B model** (or explain why it was not done) to show the benefit scales with model capacity.

- **Add bootstrapped confidence intervals or per-document variance to Figure 3** and qualify the GPT-4o comparison language with the actual measured gap rather than just "approaches."

- **Ablate the choice of last token vs. other pooling strategies** for sentence-level scoring.

- **Report the number of synthetic examples removed by decontamination** for transparency.

## Score and Decision

The paper introduces a genuinely novel retriever architecture that solves a meaningful problem (full-context sentence-level retrieval for long documents) with strong empirical results. The core claims — that Mamba Retriever outperforms embedding-based retrievers and generalizes to very long documents — are well-supported by controlled experiments with appropriate baselines. The weaknesses identified are addressable and do not undermine the paper's central contributions. The link-based data method, while showing clear benefits for Mamba, would benefit from broader validation, but this is a scope for future work rather than a fatal flaw.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>