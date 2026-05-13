# Familiarity-Aware Evidence Compression for Retrieval-Augmented Generation

- Decision: Reject
- Scores: 5, 6, 3, 5

## Abstract
Retrieval-augmented generation (RAG) improves large language models (LMs) by incorporating non-parametric knowledge through evidence retrieved from external sources. However, it often struggles to cope with inconsistent and irrelevant information that can distract the LM from its tasks, especially when multiple evidence pieces are required. While compressing the retrieved evidence with a compression model aims to address this issue, the compressed evidence may still be unfamiliar to the target model used for downstream tasks, potentially failing to utilize the evidence effectively. We propose FaviComp (Familiarity-aware Evidence Compression), a novel training-free evidence compression technique that makes retrieved evidence more familiar to the target model, while seamlessly integrating parametric knowledge from the model. Specifically, FaviComp proactively composes the compressed evidence in a way to lower the perplexity of the target model by combining decoding probabilities from both the compression model and the target model to generate context that is more familiar to the target model. This approach balances the integration of parametric and non-parametric knowledge, which is especially helpful in complex tasks where the retrieved evidence set may not contain all the necessary information. Experimental results show that FaviComp consistently outperforms most recent evidence compression baselines across multiple open-domain QA datasets, improving accuracy by up to 23.91% while achieving high compression rates. Additionally, we demonstrate the effective integration of both parametric and non-parametric knowledge during evidence compression.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work introduces a training-free ensemble decoding algorithm named FaviComp for content compression in retrieval-augmented generation (RAG). It samples tokens from both the compression model and the target model to generate a summary of retrieved documents, aiming to filter out irrelevant information in retrieved documents and integrate external knowledge with the LLM’s internal parametric knowledge to improve accuracy. Experiments on five QA tasks show that the proposed FaviComp achieves competitive results compared to selected baselines.

### Strengths
- The idea of incorporating retrieved external knowledge with parametric knowledge via ensemble decoding is interesting.
- The proposed FaviComp is a training-tree method and can be easily applied to existing LLMs for content compression in retrieval-augmented generation (RAG).
- FaviComp achieves competitive performance compared to baseline methods across five QA benchmarks.

### Weaknesses
- Unfair comparison with baseline models. Despite using the same backbone model as the target model, the proposed FaviComp uses more advanced Llama3-8B-instruct/Mistral-7B-Instruct as the compression model, while the baselines use less capable models, such as T5-large or Llama2-7B, for compression. What is the rationale behind this inconsistent choice? Can we use the same backbone model (e.g., Llama3-8B-instruct/Mistral-7B-Instruct) for compression in both the baseline methods (e.g., LongLLMLingua, RECOMP) and FaviComp to facilitate a fair comparison? Otherwise, this discrepancy can lead to a nontrivial impact on the evaluation results, making the experimental findings less convincing—it is unclear whether the improvement is due to an advanced compression model or the method’s design of FaviComp.
- Unfocused problem setup and lack of justification for using compression in RAG. According to Table 1, almost all compression-based models consistently underperform the naive RAG method (namely, “Raw Document”), which simply takes raw documents as input without filtering or compression. Does this imply that compression may actually be unnecessary in your problem setting? Typically, compression is introduced to filter out irrelevant information for improved accuracy or to reduce redundant tokens in the prompt for more efficient inference without significantly compromising accuracy [1,2]. If efficiency is the priority, a problem setting with a larger number of retrieved documents (e.g., k=20) would make more sense than the current setting. However, in this work, only k=5 documents are used. Does this suggest that the role of compression here is primarily focused on denoising the retrieved documents? Unfortunately, there is no comparison with RAG works specifically focused on denoising [3,4,5] in the experiment section. Can you clarify the purpose of compression in this work and justify its effectiveness in a more focused setting (e.g., k=30 for long-context RAG to assess the compression ability of FaviRAG and/or comparing with denoising RAG methods to evaluate the denoising ability of FaviRAG)?

**References**
1. xRAG: Extreme Context Compression for Retrieval-augmented Generation with One Token. NeurIPS 2024.
2. Context Embeddings for Efficient Answer Generation in RAG. arXiv 2024.
3. Certifiably Robust RAG against Retrieval Corruption. arXiv 2024.
4. InstructRAG: Instructing Retrieval-Augmented Generation via Self-Synthesized Rationales. arXiv 2024.
5. Making Retrieval-Augmented Language Models Robust to Irrelevant Context. ICLR 2024.

### Questions
Please address the questions in Weaknesses.

Potential limitation: Does the method require the compression model and the target model to be from the same family, sharing an identical tokenizer? Otherwise, how would ensemble decoding be achieved if their vocabularies differ?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces FAVICOMP (Familiarity-aware Evidence Compression), a training-free model designed to make retrieved evidence more familiar to a target model. FAVICOMP compresses evidence by minimizing perplexity, combining decoding probabilities from both the compression model and the target model to generate context that aligns more closely with the target model’s familiarity. Experimental results indicate that FAVICOMP outperforms baseline approaches.

### Strengths
This paper presents a training-free solution for adapting retrieved evidence to a target model, an interesting and innovative direction. 

Experimental results on LLaMA 3 8B Instruct and Mistral 7B Instruct demonstrate that the proposed solution outperforms trained ranker and compressor models.

### Weaknesses
While empirical results are provided, the intuitive design that relies on the perplexity of both the compressor and target models requires further justification. Given that target models often have limitations such as restricted knowledge and tendencies toward hallucination, it would be beneficial to address how these limitations impact the proposed approach’s effectiveness.

Missing discussion of related work:
Bridging the Preference Gap between Retrievers and LLMs

### Questions
What is the inference efficiency (in terms of computational cost) of the proposed solution?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes FAVICOMP, a training-free evidence compression technique that makes retrieved evidence more familiar to the target model, while seamlessly integrating parametric knowledge from the model.
FAVICOMP leverages the decoding probabilities of two LMs, a compression model and the target model. The compression model is instructed to summarize the raw evidential documents into a relevant context to the input, while the target model is instructed to generate relevant context without referencing the documents. 
By combining decoding probabilities from both the compression model and the target model, FAVICOMP can generate context that is more familiar to the target model.
Experiments on open-domain QA demonstrate that FAVICOMP shows better QA performance.

### Strengths
1. Compression-based RAG presents a promising research direction in terms of reducing inference latency and improving robustness to irrelevant retrieved evidence.

2. This paper proposes an interesting perspective of enabling the target model to become familiar with the compressed summary.

### Weaknesses
1. The motivation of compression-based RAG is to improve the latency of standard RAG. However, ensembling both the decoding probabilities of the compression model and the target model does not save the inference costs compared to standard RAG. I'm not sure whether FAVICOMP even consumes more computation than standard RAG.

2. I have doubts about the validity of the assumption that ensembling decoding probabilities under different conditions. The compression model is decoding under line 159: (Evidence Compression Instruction, input question, retrieved documents), while the target model is decoding under line 180: (Context Generation Instruction, input question). Although authors explain that both objectives ultimately share the goal of generating context relevant to the question, this is too inconsistent in formulation.

3. Since compression-based RAG is to improve the latency of standard RAG, the compression model should be more lightweight than the target model. For example, RECOMP adopts T5 (770M) as the compression model and Flan-UL2 as the target model (20B). However, the compression models are the same as the target models for FAVICOMP, which does not make sense.

4. Since FAVICOMP does not use a compression model of the same scale, the results in Table 1 are unfair. FAVICOMP would likely achieve better results, as it employs a more powerful compression model.

5. Reporting only the QA results in Table 1 is insufficient, as the compression rate is just as important as accuracy and F1. There’s a trade-off between compression rate and QA performance, so it would be better to combine Table 1 and Table 2. It’s difficult to assess the effectiveness of FAVICOMP without considering the compression rate.

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a training-free evidence compression technique named FaviComp. Specifically, FaviComp actively combines compressed evidence to reduce the perplexity of the target model by combining the decoding probabilities of the compression model and the target model to generate a more familiar context for the target model. Experimental results show that FaviComp consistently outperforms the state-of-the-art evidence compression baselines on multiple open-domain QA datasets.

### Strengths
1. An effective prompt compression method is proposed, which achieves the optimal compression ratio on multiple datasets while improving the performance indicators of the model.
2. No training is required, and compression is performed during inference, which reduces the training cost, but there is also a concern that the inference time will increase.
3. The paper is generally clear and the presentation is generally clear.

### Weaknesses
1. Some details need to be clarified. The theoretical basis and intuition of the motivation need to be further elaborated.
2. The novelty of the method is limited. In essence, it is more like an ensemble that generates different evidences at different prompts, using the target LLM to generate evidence and the original document to generate evidence.
3. Experimental ablation needs to be increased.

### Questions
1. What if the target LLM is considered during compression and the target LLM is in the form of an API or uncertain?
2. The author should rigorously define what is evidence that the target LLM is familiar with. In addition, if only the target LLM is familiar with it, does familiarity necessarily mean high compression quality? Does familiarity necessarily mean that the target LLM will use the compressed evidence to the greatest extent? What is the theoretical basis for the starting point?
3. Ablation: (1) Only allowing the target LLM to provide evidence (that is, only the formula of L181, that is, 2-time inference) will exceed the raw document in 2wikiMQA, which is inconsistent with other datasets. (2) What if the compression model is the target LLM? This situation implies that the compression evidence is familiar with the target LLM. In fact, referring to L231-L236, the target LLM and the compressed LLM are consistent (so I question the starting point of L49-L52. In essence, it is more like an ensemble in which the prompt generates different evidences at different times, using the target LLM to generate evidence and the original document to generate evidence respectively). (3) In the Llama model, have you ever tried the situation where the compressed LLM and the target LLM are inconsistent? The parameter size is inconsistent or the model source is inconsistent. (4) L307-L309, why can the performance of the model exceed the performance on the gold document after compression? Shouldn't this be the upper limit? What is the reason for this phenomenon? (5) How does the experiment of concating the compressed texts generated separately from the two parts perform?
5. Considering that the method uses the internal knowledge of LLM when regenerating evidence (which may increase the number of reasoning steps), I hope to see some analysis of the corresponding multi-document and multi-hop QA advantages.

### Soundness
2

### Presentation
3

### Contribution
2
