# Efficient Full-Context Retrieval for Long Documents

- Decision: Reject
- Scores: 6, 5, 6, 6

## Abstract
Long document question answering is challenging due to the quadratic computational cost of transformer-based LLMs. In resource-constrained environments, Retrieval-Augmented Generation (RAG) uses document chunking to maintain linear computational costs but often loses sight of the global context. We introduce the Mamba retriever 130M and Mamba retriever 1.3B retrievers, capable of processing entire long documents in linear time and integrating earlier context to retrieve relevant sentences for answering questions. Mamba retrievers outperform state-of-the-art embedding models across 41 long-document Q\&A benchmarks while maintaining speed and computational efficiency. Their performance is comparable to GPT-4o on long documents over 256k tokens while using significantly fewer tokens. Mamba retrievers are trained on synthetic data generated from our novel link-based method, which enhances the retrievers' ability to leverage long-range document connections. We further demonstrate the effectiveness of our link-based method over baseline synthetic data methods. All code, datasets, and model checkpoints are available at https://github.com/MambaRetriever/MambaRetriever

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes to find-tune a long-context Mamba model for the retrieval task, claiming that such a method is better than embedding-based retriever because the awareness of context. To train such a model, a data synthesis method is proposed, which is to generate query given two semantically relevant text chunks. In the experiments, the proposed method is compared with long-context model and standard RAG methods and shows strong performance.

### Strengths
- The paper studies an idea of fine-tuning long-context model as retriever. To gain efficiency for training, the Mamba model is used to save cost for training a Transformer model
- The performance shows the long-context discriminative model as retriever brings improvement to the retrieval performance.

### Weaknesses
 - The efficiency of proposed method is not studied. I can expect that with pre-built vector index, the standard RAG may be more efficient that the proposed method which needs to pass the entire textual data for each query. Although adding context for retrieval brings improvement, I am not sure whether it worth the cost if its non-trivial.
- I am not clear with the data split. What data is used for data synthesis and training and what for testing? The paper only mentions the test set so I am not sure if it is used for both.
- It is not clear to me what if the long-context model is directly trained to be a reader, i.e. generate the answer given a query. The data synthesis part can generate a query so can generate a corresponding answer as well. This should be a baseline and shows the necessity of training the model as a retrieval followed by another reader model.

### Questions
See the weaknesses raised above

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a retrieval model based on the Mamba architecture to improve long document understanding. By fine-tuning a Mamba checkpoint, the authors aim to handle entire document contexts without chunking, thus enhancing retrieval accuracy. The paper highlights synthetic data generation for training the model, including three methods—chunk-based, pair-based, and link-based. Experimental results indicate that the Mamba retriever performs comparably with existing large language models in various retrieval tasks while being more efficient. The model is evaluated on 41 QA benchmarks across multiple domains, demonstrating that the full-context Mamba retriever outperforms embedding-based retrievers, especially for long documents.

### Strengths
1. The paper introduces a novel adaptation of the Mamba architecture, focusing on processing entire documents without chunking, which may provide a more holistic context.
2. The paper addresses the scarcity of long-context retrieval data by developing synthetic data generation methods, specifically the effective link-based generation, which strengthens the retrieval model’s generalization.

### Weaknesses
1. The paper’s readability suffers due to numerous grammatical issues, ambiguous statements, and poorly constructed sentences. A thorough rewrite would significantly improve comprehension and presentation.
2. Many sections make assertions without proper references, undermining the credibility of the stated findings and comparisons.
3. The proposed method essentially fine-tunes Mamba for retrieval tasks without introducing substantial architectural innovation or unique methodological contributions.
4. The authors categorize datasets into four types but fail to clarify the rationale or methodology behind this categorization.
5. Given the method’s focus on long-context retrieval, comparisons with state-of-the-art long LLMs (such as Llama 3.1, ChatGLM, etc.) and leading retrievers from the mteb leaderboard would provide a more competitive and comprehensive evaluation.
6. Efficiency is critical in retrieval tasks, yet the paper omits a direct analysis of retrieval speed and computational resources, which would provide essential context on the practical applicability of the Mamba retriever.
7. The core contribution is described as 'finding the right model adaptation and generating effective training data,' which lacks a clear research direction and appears more like an engineering effort of combining existing models and datasets for performance gains.
8. Section 3, which introduces the method, is ambiguous and lacks a formal description. The explanation would benefit from equations and formulations to explicitly define the input, output, and the computation of the loss function. The current presentation reads more like a technical report than a research paper.
9. A recent paper, “Mamba Retriever: Utilizing Mamba for Effective and Efficient Dense Retrieval,” released this August, is not cited, despite the two approaches sharing similarities. A discussion of the differences between the two works is needed.

### Questions
1. What criteria were used to categorize datasets into four types, and how was this categorization verified or validated?
2. How does the efficiency of the Mamba retriever compare to traditional embedding-based models in terms of speed, memory usage, and computational cost?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
### Summary
1. A Mamba architecture based retriever is presented which is trained as a discriminator model
2. The retrievers are much smaller (130M and 1.3B) and outperform much larger open source (and non-finetuned) embedding based models
3. Efficacy of all retrievers is tested by plugging the retrieved chunks (or sentences) into a RAG pipeline


### Contributions
1. The paper showcases how a Mamba architecture model could be finetuned to create an effective retriever for long context documents
2. Methodology and ablation for creating synthetic data is well studied and supported via ablation
3. Synthetic dataset would further research for long context document understanding (and retrieval)

### Strengths
1. This work presents a lightweight (small parameter) based retriever for long context documents
2. Complete training code and dataset is available on Github for reproducibility
3. New dataset would further research in the direction
4. Ablations presented help understand the impact of synthetic data generation process (link based) as well as effect of context size on RAG system performance

### Weaknesses
 1. The baseline retriever (open source embedding model) is weak as it has not seen any synthetic data. It is unclear whether gains seen by Mamba retriever is due to synthetic data or the model's ability to handle long context
2. The paper claims that Mamba is more efficient in handling long document context. No supportive results are given in terms of time taken. It's unclear how efficient the model is when compared to a retriever
3. Embedding based retriever has a different retrieval granularity (chunks) as compared to Mamba (Top 50 sentences)
4. The paper claims there is lack of synthetic data for long context documents, but ends up creating a dataset where maximum context length is 10k. Is my understanding correct?
5. (Minor issue) No qualitative examples are presented in the paper which highlight how Mamba retrieves more relevant context as compared to Embedding based models. Perhaps some examples can be added to the Appendix, if there

### Questions
1. (Lines 233 to 239) Why is the retriever setup different for Mamba and embedding based retrievers? Mamba fetches Top 50 sentences whereas embedding based retrievers fetch 5 chunks. How do embedding models perform when you have identical setup?
2. Why was the link based synthetic data not used to finetune an embedding model and compared as baseline? Perhaps the gains seen by Mamba retriever are due to synthetic data. A quick check would be to see how embedding retrievers perform (in terms of recall) on a held out set of the synthetic link based data. Maybe this number could be improved via finetuning and the finetuned embedding model tested as baseline
3. (Lines 198-200) What decontamination pipeline was used to ensure that there is no overlap between synthetic data documents and documents used in the 41 benchmarks. Did you look for exact match of document content? Are the domains completely different?
4. (Lines 230-232) How did you evaluate the quality of an answer using GPT-4o? Did you give some instructions in prompt on how to judge the quality of an answer? Did the model return a binary score (such as relevant or non-relevant)
5. How was BM25 setup? Did it also retriever chunks? What happens when it retrieves sentences (same as Mamba)
6. (Lines 204-207) Which hyper-parameters were optimized? How did you select the best checkpoint? How did you decide when to stop training?
7. (Minor comment): Figures 6-10 in the Appendix seem to have the same exact prompt. Was this intentional or done by mistake?
8. (Minor comment): Lines 89-90 say upto 256 k. Did the authors mean more than 256k?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors introduce a novel approach for long document understanding using the Mamba architecture as an efficient information retriever. Unlike traditional methods that rely on document chunking, this approach processes the entire document, maintaining important contextual dependencies that chunking-based methods may lose. To overcome the challenge of limited labeled datasets for training such a model, the authors employ synthetic data generation strategies—specifically chunk-based, pair-based, and link-based approaches—prompting an LLM to the training examples. The model, trained on both 130M and 1.3B parameter variants, is evaluated on 41 benchmark tasks, spanning domains such as financial documents, government reports, and creative works. The results demonstrate that their Mamba retriever consistently outperforms embedding-based retrievers and exhibits near-GPT-4-level performance on very long documents exceeding 256K tokens. Ablation studies further highlight the importance of using full-document context and the benefits of the link-based synthetic training dataset, which effectively improves retrieval accuracy compared to the other data generation strategies.

### Strengths
- The proposed approach effectively removes the need for document chunking, enabling a more comprehensive and uninterrupted representation of document context. This is particularly advantageous for handling long documents where preserving contextual relationships is crucial.
- The Mamba-2 model, available in both 130M and 1.3B parameter variants, demonstrates impressive performance, notably surpassing models significantly larger in size, such as GritLM-7B. This result underscores the efficiency of the model design, making it a valuable solution for environments with limited computational resources.
- To address the lack of annotated datasets for training their long-context models, the authors introduce diverse synthetic data generation methods, including chunk-based, pair-based, and link-based strategies. These approaches help to create high-quality training data that may enable effective model learning.
- The paper includes a well-executed analysis, supported by ablation studies that provide insight into the contributions of different model components and training strategies.

### Weaknesses
I found the proposed idea, experiments, and analyses conducted by the authors to be valuable, especially in terms of their potential impact on low-resource scenarios. However, for the paper to fully meet the ICLR standards, there are still areas that need additional work and detail. Below, I outline several key points for improvement. I would be pleased to substantially raise my scores if the authors address these suggestions and enhance the paper accordingly.

**General Feedback**
- I noticed that the title of the paper does not match the one listed on OpenReview.
- The main text should indicate when additional detailed discussions are deferred to the Appendix for better reader guidance.

**Introduction**

- The Introduction lacks foundational references to support key claims. Both the second and third paragraphs would benefit from citations to strengthen the arguments. For instance, the statement: "This method eliminates the need for document chunking, *a common limitation in current retrieval systems that often results in loss of context and reduced accuracy*" needs a supporting citation to substantiate this point.
- The sentence: "Second, to be competitive with embedding approaches, a retrieval language model needs to be small" requires further justification. The authors should include in the paper a complexity analysis comparison discussing time and GPU memory consumption to support this assertion.

**Related Work**

- The sentence "Large Language Models are found to be inefficient processing long-context documents" should be rewritten for clarity, for example: "Large Language Models are inefficient when processing long-context documents."
- The statements "Transformer models suffer from quadratic computation during training and linear computation during inference" and "However, transformer-based models are infeasible to process extremely long documents due to their linear inference time" are incorrect. Transformers, as presented in "Attention is All You Need," scale quadratically in both training and inference.
- The statement regarding State Space Models (SSMs) having "linear scaling during training and constant scaling during inference" is inaccurate. SSMs have linear complexity for both training and inference. The term "constant scaling" implies no dependence on sequence length, which is incorrect.
- The Related Work section is lacking details. The paragraph on long-context language models should provide a more comprehensive overview of existing methods and their limitations, positioning SSMs appropriately. This includes discussing sparse-attention mechanisms [1, 2], segmentation-based approaches [3, 4, 5], memory-enhanced segmentation strategies [6], and recursive methods [7] for handling very long documents.
- Similarly, the paragraph on Retrieval-Augmented Generation should specify how prior works addressed different long document tasks. Examples include successful applications of RAG in long-document summarization [8, 9] and query-focused multi-document summarization [10, 11], which are closely aligned with the present work.

**Figures**
- Figures 1 and 2 are clear but need aesthetic improvements to meet the conference's standard presentation quality.

**Model Architecture**
- The description "a subset of tokens are specially designated, and the classification head is applied to these tokens. In the current work, the classification head is applied to the last token of each sentence, giving sentence-level resolution" is ambiguous. Clarify whether new tokens are added to the sequence or if existing tokens (e.g., periods) are used to represent sentence ends.

**Synthetic Data Generation**

- The "lost in the middle" problem when processing long documents [12] is not explicitly discussed. Have the authors considered the position of chunks during synthetic data generation? Ablation studies varying the position and distance between linked chunks would provide valuable insights into Mamba’s effectiveness in addressing this issue.
- More details are needed regarding the data decontamination pipeline, chunk size, and the relative computational cost of the link-based method versus other strategies.
- The authors claim that synthetic data generation is computationally expensive but provide no supporting quantitative evidence. Information such as time estimates and GPU demand would strengthen this argument and assess feasibility.
- There is no detailed evaluation of the synthetic data’s quality. An analysis of correctness and answer factuality would help validate the impact on retrieval performance beyond benchmark metrics.

**Training**
- This section is too brief. Consider merging it with Section 3, "Model Architecture," for a more cohesive presentation.
- What was the training time for the 130M model?

**Experimental Method**
- Fix minor formatting issues, such as adding a space after the comma in ",LVeval."
- Specify in Table 1 which datasets use free-form versus multiple-choice answers, including the number of answers and average answer lengths.
- Consider experimenting with GPT-4 as a retriever.
- Expand on "The accuracy of freeform answers is judged using GPT-4."
- Elaborate on the validation of the scoring pipeline, particularly regarding "0.942 macro F1." Clarify the data and method used for validation.
- Justify the selection of "50 sentences" for Mamba retrievers and explain chunk creation methods for embedding models. Did the chunks consist of 300 fixed-length segments, or was semantic chunking employed [3, 5]? Sentence-level embedding-based retrieval could be explored to align better with the Mamba setting.
- The assertion that "embedding models were allowed to retrieve more information than Mamba" implies an unfair comparison, but more context can sometimes degrade performance [12].
- Clarify the use of the sliding window approach for documents longer than 128k tokens, especially given the claim that Mamba could process up to 256K tokens directly.

**Results**
- Remove redundancy in Section 7.1.2, such as restating the synthetic data generation strategies.
- Expand the ablation studies to cover different input sequence lengths during training and varying the number of retrieved sentences to explore robustness to configuration changes.
- Highlight that using fewer training examples (500K vs. 1M) achieved comparable accuracy (i.e., 59.4 vs. 60.0, respectively).
- Why not train both the 130M and 1.3B models on a dataset size of 500K examples, but compare using 1M and 400K examples, respectively?

**Limitations**
- The high cost of generating synthetic training data is mentioned but lacks quantification. How computationally expensive is it in terms of time or resources?

**Appendix**
- Note that all figures in Appendices B and C are the same, suggesting an error that needs correcting.

### Questions
Please address the questions outlined in the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3
