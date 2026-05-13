# Provence: efficient and robust context pruning for retrieval-augmented generation

- Decision: Accept
- Scores: 8, 3, 6, 8

## Abstract
Retrieval-Augmented Generation improves various aspects of large language models (LLMs) generation,  but suffers from computational overhead caused by long contexts, and the propagation of irrelevant retrieved information into generated responses. Context pruning deals with both aspects, by removing irrelevant parts of retrieved contexts before LLM generation. Existing context pruning approaches are limited, and do not present a universal model that would be both _efficient_ and _robust_ in a wide range of scenarios, e.g., when contexts contain a variable amount of relevant information or vary in length, or when evaluated on various domains. In this work, we close this gap and introduce Provence (Pruning and Reranking Of retrieVEd relevaNt ContExts), an efficient and robust context pruner for Question Answering, which dynamically detects the needed amount of pruning for a given context and can be used out-of-the-box for various domains. The three key ingredients of  Provence are formulating the context pruning task as sequence labeling, unifying context pruning capabilities with context reranking, and training on diverse data. Our experimental results show that Provence enables context pruning with negligible to no drop in performance, in various domains and settings, at almost no cost in a standard RAG pipeline. We also conduct a deeper analysis alongside various ablations to provide insights into training context pruners for future work.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents an encoder-based context pruning approach to enhance retrieval-augmented generation.
The proposed framework aims to identify and eliminate irrelevant portions of retrieved context to improve the accuracy of generated responses. 
Unlike previous methods that typically rely on LLM-like decoder models, the proposed approach leverages an encoder model to frame the problem as a sequence labeling task, similar to POS tagging and NER.
The authors generate training data (silver-standard datasets) using another LLM, such as LLaMA-3.2-8B, and evaluate the performance of context pruning techniques with LLMs serving as evaluators.
The experimental results demonstrate that the proposed method is both effective and efficient. 
A comprehensive set of analyses further validates the impact of the approach.

### Strengths
- The draft is well-structured, making it easy for readers to grasp the core concepts. I genuinely enjoyed reading it.
- Unlike previous approaches that employ LLMs, the proposed method is specifically optimized for the target task, allowing it to achieve both effectiveness and efficiency.
- A series of diverse experiments highlight the merits of the proposed approach from various angles, instilling confidence in readers about the method’s reliability.

### Weaknesses
 - Training and evaluation procedures rely heavily on the use of LLMs. This is a bit concerning for me, for the following reasons:
    - Firstly, if we already have a well-performing LLM capable of effective context pruning, why should we develop a separate model for this task? The strong performance of the existing LLM could suggest that it inherently possesses the ability to filter and focus on crucial information from the context. Rather than adding an external module, we might leverage advanced prompting techniques to enhance this functionality.
    - Secondly, the process of training and evaluation lacks human oversight. Can we be confident that a model trained and evaluated in this way will align well with human preferences? Although LLMs are initially trained on human-generated data, I wonder if there’s a risk of a “hacking” effect, where the model is tuned to satisfy only the evaluation metrics instead of genuinely aiming to achieve the intended goal.
- Figure 2’s main results are intuitive; however, this presentation style may open the door to different, subjective interpretations among readers. For instance, if a reader prioritizes compression rate, they may see RECOMP (abs) as the most appealing option. Thus, it may be helpful to introduce a unified metric that incorporates both compression ratio and LLM evaluation performance, potentially using a measure akin to AUROC.

### Questions
- Given the importance of both performance and compression rate, exploring a dynamic trade-off between the two could be beneficial. For instance, while one user may prioritize performance over compression, another might value compression more highly. A straightforward way to enable this dynamic trade-off could involve adjusting the threshold that determines the relevance of tokens. By fine-tuning this threshold, the model could flexibly adapt to user-specific preferences, optimizing either performance or compression as needed.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The work presents a context pruning technique, where during RAG, each sentence in the context is individually labeled as relevant or irrelevant to the query. The training is conducted by distilling from Llama-3-8B, where the model is instructed to output an extractive summary on the sentence-level of the context given some query. Note that though the labeling is on the sentence level, each token in the sentence will inherit the sentence's label during training. During inference, only sentences where +50% tokens are kept are considered kept/positive. In another variant, the pruning model is used to both output a binary judge mask and serve as a reranker by outputting a relevance score, though for this case the model needs to be initialized from pretrained reranker. The proposed model achieves competitive results on diverse QA tasks, most on par with strong baselines like RECOMP but with more compression ratios.

### Strengths
• Evaluated on diverse QA tasks, making the results/improvements less likely to be cherry-picked

### Weaknesses
• It is questionable for a non-instruction-tuned model like DeBERTa to understand slightly more complex relation definitions. For example, if the query asks DeBERTa to find sentences that support some point vs. refute the same point, chances are that DeBERTa is going to keep the same sentences.

•	Results figure (i.e., Figure 2) is not clear. Not clear what x- & y-axis represent. The caption should clearly state that, e.g., y-axis is compression ratio, etc...

•	Overall results figures are all hard to read, esp. Figure 4 where all symbols are superimposed on top of each other. Consider enlarging them or changing them to more informative tables.

• I don't quite get the model choices here. The silver labelings are obtained with Llama-3 models, where the generator is chosen to be Llama-2? Is there any justification for the versioning discrepancy?

### Questions
Suggestions:

• 181: using "silver labels" without defining the term first. From the context it seems to mean "auto-generated labeled data".

### Soundness
2

### Presentation
1

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
The paper proposed a context pruning method for retrieval augmented generation tasks by considering the context pruning task as passage reranking. The authors used a Deberta reranking model which is significantly smaller than large generative models to improve both efficiency and performance of retrieval augmented language generation.

Experiments show that when the compress rate is higher than 50%, the proposed method outperforms other strong baselines. The authors also provided comprehensive analysis and ablation studies.

### Strengths
The proposed method shows a good adaptation ability and efficiency on different tasks. When the compression rate is higher than 50%, the method still achieves a reasonable performance.

### Weaknesses
This work misses some relevant citations and does not compare to these methods, for example:

[1] DSLR: Document Refinement with Sentence-Level Re-ranking and Reconstruction to Enhance Retrieval-Augmented Generation.

[2] Dense X Retrieval: What Retrieval Granularity Should We Use?

[3] Phrase Retrieval for Open-Domain Conversational Question Answering with Conversational Dependency Modeling via Contrastive Learning

[4] Decontextualization: Making Sentences Stand-Alone

I'll adjust my score if the authors settles my concerns about missing these comparisons.

### Questions
what is the performance of the proposed method when the compress rate is less than 50%?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Provence, a context pruner for question answering that formulates context pruning as a sequence labeling task. Specifically, the authors fine-tune a pre-trained re-ranker (DeBERTa) using silver labels generated by Llama-3-8B. The claimed benefits of this approach are that the proposed approach operates without assuming a fixed compression ratio and can be applied out-of-the-box to various datasets. This approach improves the efficiency of RAG for QA without performance degradation.

### Strengths
- Provence is a novel approach that enables context compression without performance drop, outperforming baseline models.
- It offers practical advantages, including query-dependent, sentence-level, dynamic compression, and adaptability across multiple domains.
- The authors conduct extensive analysis to understand the properties of Provence and explore various design options to enhance its effectiveness.

### Weaknesses
 - Some hypotheses are presented without supporting results. For example: (1) Provence does not select any irrelevant sentences, and (2) leftmost and rightmost sentences are usually not deemed relevant and no explanation is provided for why catching “needle” sentences in these positions might be an exception.
- There is insufficient information to indicate that the experiments were designed for a fair comparison. The authors do not consider an adequate retrieval pipeline for comparison with existing approaches (as Splade + DeBERTa may introduce bias favoring Provence), and the impact of the hyperparameter k in retrieving the top-k relevant passages is not discussed.

### Questions
- Why is it useful to unify compression and reranking? In which parts of a RAG pipeline can rerank scores be effectively used? Does Provence outperform existing approaches in reranking?


-----
Raised my score 6-> 8 as author responses cleared most of my doubts.

### Soundness
3

### Presentation
2

### Contribution
3
