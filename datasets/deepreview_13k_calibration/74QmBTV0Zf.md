# Late Chunking: Contextual Chunk Embeddings Using Long-Context Embedding Models

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 3, 5

## Abstract
Many use cases require retrieving smaller portions of text, and dense vector-based retrieval systems often perform better with shorter text segments, as the semantics are less likely to be ``over-compressed" in the embeddings.
Consequently, practitioners often split text documents into smaller chunks and encode them separately. However, chunk embeddings created in this way can lose contextual information from surrounding chunks, resulting in sub-optimal representations.
In this paper, we introduce a novel method called ``late chunking", which leverages long context embedding models to first embed all tokens of the long text, with chunking applied \textit{after} the transformer model and just before mean pooling - hence the term ``late'' in its naming.
The resulting chunk embeddings capture the full contextual information, leading to superior results across various retrieval tasks. 
The method is generic enough to be applied to a wide range of long-context embedding models and works without additional training.
To further increase the effectiveness of late chunking, we propose a dedicated fine-tuning approach for embedding models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces late chunking for document embeddings, which suggests that instead of chunking the text and then computing the embedding for individual chunks, one can alternatively first compute the embeddings for the whole document (or a great portion of it containing the desired chunk, in their long late chunking method), and then extract the embeddings for that chunk. Experiments conducted on retrieval tasks show the effectiveness of the proposed method and many ablations are conducted.

### Strengths
The experiments are well designed and the paper is easy to understand. 
The performance of the method is consistently better than the compared baseline on almost all tasks & models experimented.

### Weaknesses
While the proposed method shows a good consistent, it seems to only work for an imaginary scenario --- Chunking methods are designed such that models can handle longer piece of text, but the proposed method only works if we can encode text longer than the chunk size. This limits the applicability of the method, as it does not address the core issue of embedding models' inability to handle very long sequences. The method's reliance on encoding longer sequences to extract chunk embeddings also introduces a computational overhead, as the entire document or a large portion of it needs to be processed even when only a small chunk is ultimately required. This contrasts with standard chunking approaches where each chunk is processed independently, potentially leading to significant inefficiencies in scenarios where only a few chunks are needed from a large document.

### Questions
About the weakness, the reviewer can still imagine that in some cases where the chunk size is much smaller than the model length, this method can be useful. The author should present more practical examples and arguments that shows current practice often overlook this design, and that the work can signal the importance of late chunking.

### Soundness
2

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
4

### Summary
This paper proposed a novel method called “late chunking”, which leverages long context embedding models to first embed all tokens of the long text, with chunking applied after the transformer model and just before mean pooling. The resulting chunk embeddings capture the full contextual information, leading to superior results across various retrieval tasks. The method is generic enough to be applied to a wide range of long-context embedding models and works without additional training. To further increase the effectiveness of late
chunking, the authors also proposed a dedicated fine-tuning approach for embedding models. They experimented their method on BeIR benchmark and the results showed that by using late chunking, they are able to improve the retrieval performance (measured by NDCG) on several datasets.

### Strengths
- The proposed method is intuitive and simple but yield decent performance across embedding models and tasks.
- The proposed method can be directly used off the shelf, which would benefit the research community a lot.
- The paper is well organized and presented.

### Weaknesses
 - I have some concerns regarding the results presented in Figure 3. In this figure, we observe that performance with late chunking declines across several datasets, including NarrativeQA (Chunk size > 128), 2WikiMultiHopQA (Chunk size > 16), SummScreenFD (Chunk size > 128), QMsum (Chunk size > 256), Needle-8192 (Chunk size > 4), and Passkey-8192 (Chunk size > 32). This pattern raises the question of whether the fusion of contextual information might actually lead to regression in fact-based retrieval tasks where extensive contextual information may be less relevant. The performance degradation on Needle and Passkey datasets is particularly concerning, given their design to test precise information retrieval within a long context. The fact that late chunking performs worse than naive chunking in these cases suggests that the method may not be robust to scenarios where the relevant information is sparse and surrounded by irrelevant context. This raises questions about the general applicability of the method, especially in tasks where pinpoint accuracy is needed.

- I am also concerned about the experimental setup, particularly the choice of the BeIR benchmark as the primary testbed. The motivation for this choice feels less justified. To make a strong case that late chunking enhances retrieval performance in scenarios where contextual information is beneficial, it would be ideal to use a dedicated dataset (or a subset of datasets) where contextual information is  necessary for optimal retrieval performance. This approach would allow for a more informative breakdown of performance in contexts that benefit from contextual information versus those that do not. However, with the datasets selected, it is unclear to me how much contextual information contributes to performance gains and whether it might cause regressions in other scenarios. The BeIR benchmark, while diverse, may not sufficiently isolate the impact of contextual information, making it difficult to ascertain the true benefits of late chunking in context-rich scenarios. A more targeted evaluation on datasets specifically designed to test the use of long-range dependencies would be more convincing.

- Another issue with the experimental setting is that only retrieval performance is measured not the downstream performance. Ultimately, downstream performance is what people care about. It is unclear whether improvements in retrieval performance translate into meaningful gains in downstream tasks. The paper lacks an analysis of how the improved retrieval performance translates into improvements in downstream tasks such as question answering or summarization. Without this, it is difficult to assess the real-world impact of the proposed method. It is crucial to demonstrate that the gains in retrieval are not just an artifact of the evaluation metric but lead to tangible improvements in practical applications.

- Section 4.5 feels somewhat incomplete. Rather than providing a systematic comparison, it functions more as a case study, which, in my opinion, adds less weight to the paper's central argument. I suggest reallocating this section’s space to address the concerns outlined above.

### Questions
In table 2, it's quite interesting to see the results show different trend on different datasets and different embedding models. For example, on TRECCOVID, late chunking helps least on Jv2 while on NFCorpus, it helps most on Jv2 and less on Jv3 and No. Do you have an idea what causes the differences?

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
5

### Summary
The paper propose a late-chunking strategy for text embeddings, where the texts are firstly past through a text encoder and then the pooling are done at chunks of the output token embeddings to form chunk embeddings. Experiment results show the proposed late chunking strategy performs better that naive chunking on the BEIR benchmark.

### Strengths
1. Chunking is an important problem in applying text embeddings in practical applications such as RAG.
2. The paper is clearly written and well presented.
3. The proposed solution is simple to implement for practitioners.

### Weaknesses
1. For naive chunking, the standard practice is to have some overlapping strides between chunks, and to include meta information such as document title in every chunks when available. It is unclear whether the author of this paper follows this practice in implementing the baselines.
2. The paper uses a relative small chunk size (up-to 512) in the experiments when the embeddings studied support 8k context length. As shown in the ablation, the gains from late chunking diminish when the chunk size goes from 16 up to 512. It is unclear whether it is still effective when the chunk size approaches the embedding length limit of 8k, where the benefit of chunking is most useful.

### Questions
NA

### Soundness
2

### Presentation
3

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
This paper introduces a novel technique called "late chunking" for improving text embeddings in retrieval tasks by leveraging long-context embedding models. Unlike traditional chunking methods that split text before encoding, late chunking first encodes the entire document and then applies chunking, thereby preserving full contextual information within each chunk. This paper evaluates this approach on multiple retrieval datasets and demonstrates that late chunking consistently outperforms naive chunking methods across various chunking strategies (fixed-size, sentence-based, semantic) and models.

### Strengths
1. This paper proposes a late chunking technique that utilizes a long-context retriever to encode the full text before performing chunking, which reduces information loss caused by direct chunking.
2. This paper conducts extensive analytical experiments to explore the technical details of late chunking.

### Weaknesses
1. The experiments are not comprehensive enough. As only a subset of the BEIR benchmark is used in Section 4.1, limiting the assessment of the effectiveness of late chunking. The choice of datasets seems arbitrary, and a more systematic evaluation across the full BEIR benchmark would be necessary to fully validate the claims.
2. The proposed method needs high computational resources: Late chunking requires encoding the entire input with a long-context LLM before chunking, whereas standard chunking only encodes each chunk separately, resulting in shorter sequence lengths and reduced attention computation costs. As noted in Section 4.1, "splitting documents into smaller chunks increases the computational effort of the evaluation." This computational overhead is a significant practical limitation, especially when dealing with large document collections or real-time applications. The paper does not adequately address the trade-offs between performance gains and increased computational cost.
3. When dealing with longer texts, a sliding-window approach is still required, which could still lead to the loss of long-range dependency information. While the method does encode the full text before chunking, the sliding window approach inherently limits the context available to each chunk, potentially hindering the retrieval of information that spans beyond the window size. This limitation is not sufficiently discussed in the paper.

### Questions
1. In Table 2, it seems that late chunking aims to better segment chunks, yet the use of sentence boundaries and fixed-size boundaries indicates that both late chunking and naive chunking methods are dividing chunks in the same way. Then why does late chunking still can generate higher-quality embeddings and achieve better performance?
2. Do the authors believe that late chunking could yield better results with LLM retrievers employing causal attention mechanisms?

### Soundness
2

### Presentation
3

### Contribution
3
