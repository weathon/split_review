# Pooling And Attention: What Are Effective Designs For LLM-Based Embedding Models?

- Decision: Reject
- Scores: 5, 5, 3, 5

## Abstract
The significant advancements of Large Language Models (LLMs) in generative tasks have led to a growing body of work exploring LLM-based embedding models. While these models, employing different pooling and attention strategies, have achieved state-of-the-art performance on public embedding benchmarks, questions still arise about what constitutes an effective design for LLM-based embedding models. However, these models are often trained on different datasets, using different LLM base models or training settings. Moreover, evaluations on public embedding benchmarks often fail to report statistical significance, making it difficult to determine which designs truly contribute to final performance. This complicates the process for practitioners seeking optimal training recipes for LLM-based embedding models.
In this study, we conduct a large-scale experiment by training a series of LLM-based embedding models using the same training data and base model but differing in their pooling and attention strategies. The results show that there is no one-size-fits-all solution: while bidirectional attention and an additional trainable pooling layer outperform in text similarity and information retrieval tasks, they do not significantly surpass simpler designs like EOS-last token pooling and default causal attention in clustering and classification tasks.
Furthermore, we propose a new pooling strategy, \newmethod, which transforms the outputs of all hidden layers, rather than just the last layer, using a cross-attention network. This method proves to be statistically superior in text similarity and retrieval tasks compared to existing pooling methods.
Overall, this paper sheds light on effective training strategies for LLM-based embedding models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper conducts many experiments by training several LLM-based embedding models using the same training data and base model, but varying their pooling and attention strategies. The results indicate that there is no one-size-fits-all solution. Furthermore, the paper proposes a new pooling method called Multi-Layer Trainable Pooling. This method shows improvements in text similarity and retrieval tasks compared to the baseline, but offers no gains in classification and clustering tasks.

### Strengths
1. It conducts a large-scale experiment and reports statistical significance. 
2. The paper is clearly written and easy to understand.

### Weaknesses
1. The paper offers no surprises; it primarily conducts numerous experiments, and the proposed multi-layer trainable pooling method lacks novelty.
2. The improvement is negligible, and the proposed method does not show gains across all tasks.

### Questions
Could you explain further why the proposed method works well for text similarity and retrieval tasks, but not for classification and clustering? I believe the underlying reasons might be interesting.

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
This paper explores design choices in LLM-based embedding models, focusing on pooling and attention strategies. It fine-tuned different case models using the same dataset but different pooling and attention configurations. The experimental results indicate that bidirectional attention with an additional trainable pooling layer outperforms in STS and retrieval tasks but falls short in clustering and classification tasks. Finally, this study proposes Multi-Layers Trainable Pooling, which utilizes all hidden layers to capture richer semantic information.

### Strengths
- The authors identify the key factors (pooling and attention) to transform the decoder-only LLM to embedding models and conducted interesting ablation study.
- The proposed multi-layer trainable pooling is interesting idea, incorporating the semantic information from all layers.

### Weaknesses
See the question below.

### Questions
- While the paper shows interesting ablation studies, it is not convincing comparing the model with other leading models from MTEB leaderboard. To do that, can you provide the full MTEB evaluation results? 
- For training, only retrieval datasets are employed, but other embedding tasks (such as clustering and classification) datasets are not used. Training the model only on retrieval dataset can make the model overfitted to one task to decrease the accuracy of other tasks. This may be the reason why classification and clustering accuracy degrades in model 2 and 3 cases.
- Based on above observation, can you conduct the training adding the clustering and classification datasets for ablation studies?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the design space of attention and pooling for dense retriever models that are finetuned from an LLM. The paper studies bidirectional and causal attention masking. It also explores mean, last-token and trainable pooling types. For the trainable pooling types it studies the use of only last-layer representations and multiple-layer representations. The empirical results show that there is no one-size-fits-all solution and that various tasks have different optimal designs.

### Strengths
1) The work introduces the novel concept of pooling across layer representations for LLM based dense retrieval models.
2) The work constructs and evaluates an architecture for multi-layer trainable pooling and it performs better than other pooling types in certain scenarios.
3) The work is well motivated: various related works cover various portions of the design space but they use different datasets, so it is important to study the design space while keeping the dataset constant.

### Weaknesses
This paper seems to be a rigorous study of the design space of dense embedding models rather than an attempt at the state-of-the-art, However, the experiments are not rigorous enough:
1) The evaluations (Tables 2-4) and discussion (Section 5) include classification and retrieval tasks. However, the training datasets (Table 6) do not include either of these tasks.
2) Bidirectional attention with mean-pooling is not evaluated with the reasoning in Section 4.1 that NV-Embed, a related work has shown that trainable pooling can outperform mean pooling. However, since the trainable last-layer pooling in this paper is not the same as in NV-Embed, this study should have included bidirectional attention with mean-pooling and NV-Embed style trainable last-layer pooling as baselines.
3) In section 3.1, experiment 2, it is observed that the EOS token from layer 0 of Mistral performs significantly better in retrieval than all later layers, which have nearly 0 scores. This seems unlikely since at layer 0, the EOS token is unlikely to have a strong representation of the text. Furthermore, why is EOS pooling used for this experiment when LLM2Vec has shown that mean pooling outperforms EOS pooling even for the causal Mistral model without any finetuning.

### Questions
1) If the importance of various layers is task-dependent, would the model perform better if trainable Q latent matrix was task dependent? One idea would be to produce the Q from a representation of the task instruction. Another experiment towards that idea would be to have a separate Q matrix for STS, Retrieval, Clustering, Classification and see if those improved results.
2) Why is the layer weight matrix needed if the cross-attention block is anyway weighing the layer representation using attention weights? What are the results if the layer weight matrix was not used?

Further ablations and datasets related to the weaknesses above would improve the rigor of the paper:
1) Include classification and clustering in the training data or exclude any conclusions for classification and clustering.
2) Compare with mean pooling+bidirectional attention and NV-Embed style last-layer trainable pooling.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Existing LLM-based embedding models employ various pooling methods (such as EOS-last token pooling, mean pooling, and trainable pooling layers) and attention mechanisms (causal vs. bidirectional), but are often trained on different datasets and base models, making it difficult to isolate the impact of these design choices.

To address this, the authors conduct a large-scale experiment where they fine-tune a series of LLM-based embedding models using the same training data and base model (Mistral-7B and Qwen2-0.5B), varying only the pooling and attention strategies. They evaluate these models on the Massive Text Embedding Benchmark (MTEB) and use statistical significance testing to assess the results.

They also propose a new pooling strategy called Multi-Layers Trainable Pooling, which leverages hidden states from all layers of the LLM (not just the last layer) and uses a cross-attention network to produce the final embedding. This method proves to be statistically superior in STS and retrieval tasks compared to existing pooling methods.

### Strengths
## Originality:
1. The paper presents a systematic and controlled study that isolates the impact of pooling and attention strategies on LLM-based embedding models. By training multiple models using the same base LLM and training data but varying only the pooling and attention mechanisms, the authors offer new insights into how these factors affect performance across different tasks.
2. Moreover, the introduction of multi-layers trainable pooling strategy based on hidden states from all layers of the LLM, not just the last layer, is novel. This approach aims to capture complementary information encoded at different layers

## Quality:
1. The authors ensure a fair comparison by using the same base models (Mistral-7B and Qwen2-0.5B) and training data across all experiments. This eliminates confounding variables and provide a nice study.
2. Employing the Wilcoxon Signed Rank Test to assess the results adds rigor to the evaluation, providing confidence that the observed differences are statistically meaningful rather than due to random chance.
3. The models are evaluated on the Massive Text Embedding Benchmark (MTEB), covering a wide range of tasks such as semantic textual similarity, retrieval, classification, and clustering. 

## Clarity:
1. I like how the paper is introducing notations and concepts in a gradual and comprehensible manner. Complex ideas are broken down and explained step by step, which helps in understanding.
2. Moreover, authors took care to use consistent notation throughout the paper, which helps prevent confusion and allows to follow the methodology and results more easily.
3. Finally, figures, tables, and diagrams are used to illustrate key points, such as the correlation between hidden states across layers and the architecture of the proposed pooling method.

## Significance:

1. Practical Insights - by revealing that there is no one-size-fits-all solution for pooling and attention strategies in LLM-based embedding models, the paper is valuable for practitioners. The findings suggest that the choice of strategy should be task-dependent.
2. The introduction of the Multi-Layers Trainable Pooling method contributes to the field by proposing a new way to utilize the rich information contained in the various layers of an LLM.

### Weaknesses
## Overemphasis on Technical Novelty over Practical Problem Solving

1. The paper focuses on the proposed method over problem understanding. The paper seems to prioritize introducing a novel technical method without fully addressing whether it effectively solves the underlying problem of improving embedding models. The connection between the proposed solution and the practical challenges in embedding generation is not thoroughly established.
2. It lacks a fundamental study on embedding models. The study does not delve deeply into fundamental aspects of what makes a good embedding model for specific tasks. Without this foundational understanding, it's difficult to assess whether the proposed method addresses the core issues in embedding generation. Without this, it seems like we are throwing random methods at the problem without increasing our understanding of what is the root cause and what impacts whether an embedding model is good.


## Insufficient Ablation Studies and Hyperparameter Analysis

1. No ablations on key hyperparameters are provided. The paper lacks ablation studies on important hyperparameters, such as the number of queries trained (r), and the inner dimension d' of the cross-attention block or LoRA rank. Exploring how these parameters affect performance would provide deeper insights into the robustness and effectiveness of the proposed method.

2. It seems there is a gap in models evaluated as comparison with simplified versions is lacking. Investigating simpler versions of the model, such as training the attention matrix (author's way) on only the last layer's output (similar to NV-embed), could help isolate the benefits of incorporating multiple layers. This comparison is essential to justify the added complexity of the Multi-Layers Trainable Pooling. From what I understand - it seems that the last-layer approach is technically different from the multi-layer approach, and thus, not directly comparable.




## Questionable Robustness and Generalizability of Results

1. The performance is mixed across tasks. The proposed method does not consistently outperform simpler baselines across all tasks. While it shows improvements in semantic textual similarity (STS) and retrieval tasks (Table 4), it underperforms in classification and clustering tasks. This inconsistency raises concerns about the robustness and generalizability of the method.
2. There is potential randomness in results. Without more extensive experimentation or replication studies, it's possible that the observed improvements are due to random chance rather than a fundamental advantage of the method. The limited scale of the study may not provide enough empirical evidence to draw firm conclusions. I am worried that simply changing the training horizon will impact the conclusions drawn by authors. The results on Mistral are not convincingly transferred to QWEN and the reason remain unclear. I think the lack of the fundamental study mentioned earlier takes it toll here.

### Questions
1. Your method shows improvements in semantic textual similarity (STS) and retrieval tasks but underperforms in classification and clustering tasks. Could you provide an analysis or explanation for this inconsistency? Is there an underlying reason why the proposed method benefits some tasks but not others? Understanding this could help practitioners decide when to apply your method.
2. Your findings suggest that we may not fully grasp how to optimize embedding models, and further exploration of this topic could provide valuable insights for the community.
3. To ensure that the observed improvements are not due to random chance, have you considered conducting experiments with multiple random seeds or on additional datasets? Providing more extensive empirical evidence would strengthen the validity of your conclusions.
4. How does your method compare with simpler variants, such as training the attention matrix on only the last layer's output (similar to NV-embed)? Including such comparisons would help isolate the benefits of incorporating multiple layers in your pooling strategy. An ablation study that progressively adds complexity could demonstrate the necessity of each component.

### Soundness
2

### Presentation
4

### Contribution
2
