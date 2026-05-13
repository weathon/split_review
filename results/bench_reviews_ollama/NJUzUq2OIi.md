Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

The paper introduces Mamba retriever, a state-space model (SSM) based on Mamba-2 that performs sentence-level retrieval over full long documents in linear time, replacing chunk-based embedding retrievers in RAG pipelines. A binary classification head on sentence-final tokens labels relevance, and a novel link-based synthetic data generation method leverages natural connections between document chunks to produce training data. The 130M and 1.3B Mamba retrievers outperform top embedding baselines across 41 long-document QA benchmarks and approach GPT-4o's performance on documents exceeding 256k tokens while using far fewer compute resources.

## Strengths

- **Novel and well-motivated architecture**: Using an SSM's recurrent hidden state for full-document retrieval instead of independent chunk embeddings is a genuinely new approach. The discriminative classification head on sentence-final tokens is a clean and effective formulation (Section 3).

- **Strong context ablation evidence**: Figure 4 directly demonstrates that full-context processing helps—performance degrades as context is reduced—providing the paper's most convincing evidence that the architecture leverages long dependencies, not just local information.

- **Comprehensive benchmark coverage**: Evaluation across 41 benchmarks spanning educational, creative, official, and conversational document categories is extensive. The decontamination procedure (Section 4.3, filtering any synthetic data point with >1% sentence overlap with 2.4M test sentences) is rigorous.

- **Link-based synthetic data validated over baselines**: Table 4 shows link-based generation (59.4%) outperforms chunk-based (58.5%) and pair-based (55.3%), confirming the superiority of the proposed data generation strategy under controlled conditions (same model, same document sources).

- **Efficiency results**: Table 2 shows Mamba retriever 130M is considerably faster and uses far fewer FLOPS than embedding baselines, while 1.3B is comparable or slightly better, making a practical case for the approach.

## Weaknesses

### Fatal
None.

### Major

- **The "full-context" claim is not validated on the longest documents where it matters most**: The title and core pitch center on "full-context retrieval," but Section 5.4 discloses that for documents exceeding 120k tokens—the very regime where full-context processing should confer the greatest advantage—Mamba retrievers use a sliding window (120k window, 60k stride). The paper states this is "to ensure a fair comparison with GPT-4o," and the model *can* technically handle 256k tokens. However, the headline result in Figure 3 (comparable to GPT-4o at >256k tokens) therefore reflects a comparison of two sliding-window systems, not a demonstration of full-context superiority. The context ablation (Figure 4) validates the full-context advantage on shorter documents, but does not cover the >120k regime. Reporting full-context results for the 1.3B model on long documents without sliding windows—as the title promises—is essential to validating the paper's central claim.

- **The superiority claim over embedding models relies on comparisons against pretrained baselines, while fine-tuned embedding baselines show zero improvement and this is insufficiently investigated**: As reported in Table 1, fine-tuned GTE-Qwen2-1.5B and Contriever-110M on the same link-based data show no gains over their pretrained checkpoints. The paper attributes this to "Mamba retrievers learned more than superficial artifacts," but alternative explanations—suboptimal fine-tuning (one epoch, repurposing binary sentence labels for contrastive learning), mismatch between the classification-formulation data and contrastive objectives—are not ruled out. While the comparison against strong pretrained baselines (NV-Embed-v2-7B, Stella-1.5B) stands independently, the conclusion that the architectural paradigm rather than training methodology drives the advantage is not firmly established without properly optimized embedding fine-tuning.

### Minor

- **End-of-document performance degradation**: Section 7.5 notes "Mamba retrievers performed slightly worse when important information is located at the end of a long document." For a model whose primary advantage is full-document context, this suggests the recurrent hidden state may degrade over very long sequences—a potential architectural limitation worth further analysis.

- **The 1.3B model is trained on only 400k of 1M available examples**: The authors state that "we did not observe any improvements in the validation sets when training beyond this amount," but this could reflect undertrained models rather than data saturation, especially since the smaller 130M model was trained on the full 1M examples. Whether the 1.3B model could benefit from more data with additional hyperparameter tuning is unclear.

- **No error bars or per-dataset breakdowns in main results**: Average accuracy across 41 datasets without confidence intervals or per-dataset variance makes it difficult to assess the statistical reliability of observed differences, particularly for small categories like "Conversational" (707 points) and the >256k bucket in Figure 3.

### Trivial
None.

## Nice-to-Haves

- Report Mamba retriever 1.3B results on >120k documents in full-context mode (without sliding windows) as an additional data point, even if it means dropping the GPT-4o comparison for that specific ablation.
- Provide per-benchmark results (or at least per-category variance) in the main paper body rather than only in the appendix.
- More detailed analysis of what sentences Mamba retrieves differently from embedding models, to reveal whether full context actually changes retrieval behavior qualitatively.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **GPT-4o comparison is not apples-to-apples**: The harsh critic argues that comparing Mamba retriever + GPT-4o (generator) to GPT-4o (direct answerer) conflates different pipelines. However, the paper is explicit about this setup—it's comparing end-to-end QA performance, which is the practically relevant metric. The "160x fewer tokens" claim is about generator input tokens, which is precisely the point of RAG. This comparison is fair and informative, not misleading. Removed.

- **Sliding window averaging could degrade quality near boundaries**: This is speculative and not substantiated by evidence. The paper states scores are averaged for overlapping sentences; no empirical signal of problems is presented. Removed.

- **Binary yes/no evaluation by GPT-4o is coarse**: The paper reports 0.942 macro F1 on a held-out set of 180 human-annotated examples, which is a reasonable validation. GPT-4o-as-judge is standard practice in the field. Removed as generic criticism not grounded in evidence of bias in this specific evaluation.

- **Missing related work**: Per instructions, removed—no external sources to confirm existence of allegedly missing citations.

- **Abstract claims "across" benchmarks suggests consistent superiority**: This is a minor framing choice; the main table shows category-averaged and overall-averaged results. Treating as trivial nitpick rather than substantive weakness; removed to avoid inflating weakness count.

- **Formatting/presentation issues**: Per instructions, removed all formatting/style complaints.

- **1.3B model efficiency claims may not apply in constrained settings**: The paper is transparent about the 8×H100 setup. This is a standard experimental setup disclosure, not a methodological flaw. Removed.

- **Synthetic data cost >$1000 as limitation**: The paper already acknowledges this. Not a weakness to ding them for something they already cite as a limitation. Removed.

- **Generative vs discriminative comparison doesn't isolate architecture from formulation**: The paper's claim in Section 7.3 is specifically about "generative retrieval is often lossy," and includes GPT-4o and Llama-3.1-70B as generative baselines—not just Mamba. The comparison demonstrates the discriminative formulation advantage, which is a valid contribution. Removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Add a single experiment running Mamba retriever 1.3B on documents in the 120k–256k range in full-context mode (no sliding window), even if compared only to its own sliding-window results. This would directly validate the paper's central claim where it matters most.
- Conduct a more thorough fine-tuning of embedding baselines (multiple epochs, proper hard-negative mining, task-appropriate contrastive procedures) to either confirm that the zero-improvement result is robust or revise the interpretation.

## Score and Decision

The paper presents a genuinely novel idea—using SSMs for full-context retrieval—with solid evidence on shorter documents (the context ablation in Figure 4 is convincing) and thorough benchmarking. However, the central "full-context" advantage is not demonstrated on the longest documents (>120k tokens) where it should matter most, because the authors apply sliding windows there for fair comparison instead of additionally reporting full-context results. The fine-tuned embedding baselines showing no improvement is concerning but secondary—the main comparison against pretrained SOTA baselines stands. These are significant but addressable gaps, not fatal flaws.

Originality: The SSM-as-retriever formulation is novel and well-motivated.  
Importance: Long-document retrieval is an important and timely problem.  
Claims support: Good for shorter documents; incomplete for the headline claim on the longest documents.  
Experimental soundness: Comprehensive benchmarks; the main concern is about missing ablations, not flawed experiments.  
Clarity: Well-written and transparent about limitations.  
Value: A meaningful contribution that opens a promising research direction.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>