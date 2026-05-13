# ZeroTS: Zero-shot time series prediction via multi-party data-model interaction

- Decision: Reject
- Scores: 8, 6, 5, 3, 3

## Abstract
Time series forecasting (TSF) is a fundamental task in artificial intelligence, with applications ranging from weather prediction, stock market analysis to electricity demand forecasting. While existing models, particularly large language models (LLMs) tailored for TSF, primarily focus on improving accuracy and generalization through pre-training and fine-tuning, zero-shot prediction without task-specific fine-tuning, still remains underexplored. This limitation arises from the restricted scalability and flexibility of current LLMs for TSF, which struggle to fully capture the interactions between  data and model. In this work, we introduce ZeroTS, a novel approach that bridges open-world knowledge with inherent data regularities by constructing multi-party interactions between data and models. On the data side, we propose a TS-RAG (Retrieval-Augmented Generation for Time Series), which efficiently retrieves both meta and series information, enabling diverse domain-specific time series to be used as prompts. On the model side, we develop a reinforcement learning framework that treats ground-truth as environments, providing error feedback to optimize a smaller model and harnessing the capabilities of LLMs. This allows ZeroTS to incrementally approach inherent data regularities while iteratively refining its outputs. We validate ZeroTS via extensive experiments on zero-shot and long-horizon forecasting. ZeroTS achieves best or second best results with comparative parameters, 1/4 memory and 1/7 inference speed, demonstrating its efficiency and effectiveness. Our results highlight the potential of Data-LLM interactions for zero-shot learning with acceptable parameters, opening new avenues on research of this underexplored area.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents ZeroTS, a framework for zero-shot time-series prediction that integrates retrieval-augmented generation (RAG) with time-series data, addressing challenges in this area. The authors highlight the difficulties in adapting RAG for time series, including the need for an effective time-series-oriented database, optimization of the dual pipeline for high-quality outputs, and the construction of a lightweight module to integrate knowledge from both time-series data and large language models (LLMs): 

1. The authors utilize RAG for the time series prediction. ZeroTS is claimed to be the first framework to apply RAG to zero-shot time-series prediction, incorporating a meta-value structure to capture key information across time-series data. A modified high-speed nearest neighbor search (HSNSW) with hybrid affinity measurement enables efficient and targeted retrieval, enhancing prediction relevance. The authors also propose a distant metric that combines both the cosine similarity and Euclidean distance.

2. The authors propose a reinforcement scheme that refines the coherence between retrieved data and LLM output. This scheme leverages feedback from the ground-truth data to guide the LLM's predictions closer to factual trends, enabling the model to learn and adjust to real-world patterns dynamically.

3. ZeroTS is evaluated in both zero-shot and long-term prediction settings, demonstrating performance gains while outperforming comparable models with better space allocation and computational time.

### Strengths
1. The paper is written clearly. The organization of the paper is well understood and the authors illustrate their algorithms with decent figures. 

2. The authors utilize RAG for the time series prediction. Their way of constructing the retrieval database seems reasonable. In addition to RAG framework, the authors propose a reinforcement learning-based algorithm to use the retrieval dataset in an efficient way.  This combination enables the authors to make time series prediction in zero-shot. 

3. The authors conduct a reasonable amount of ablation studies to observe the effect of their algorithms. Additionally, the authors study the effect of their selection of hyperparameters: the number of retrieved time series, the representation dimension for the retrieval and target domains.

### Weaknesses
1. I think the reinforcement learning-based algorithm the authors propose has a similarity with the literature of reinforcement learning with human feedback (RLHF)[1] [2] in the sense that this proposed algorithm is trying to learn the policy based on the retrieved time series (feedback). It would be better to see the similarity and differences between the proposed algorithm and RLHF literature. I am aware that there is a page limit but this discussion can be performed in Appendix as well.

2. The authors present their results by averaging over prediction horizons. It would be more informative to include results for each prediction horizon in the appendix, allowing readers to assess model performance across specific horizons. This approach would also address any concerns about one horizon dominating and skewing the overall average.

3. Minor Weakness: In line 232, the authors claim that they adopt a hybrid distance metric by incorporating both cosine similarity for trend modeling and Euclidean distances for value discrepancy. I think the definition in (2) does not provide a distance notion, instead it provides a similarity notion. This is because this definition is positively correlated by the cosine similarity and negatively correlated by the Euclidean distance.

4. The authors keep saying that they utilize meta information. However, I think, the way of utilizing meta information in the paper is not clear. I asked questions about this weakness in the questions section.

### Questions
1. How do the authors utilize meta information during retrieval phase? In line 214-215, the authors write that "We select the
domain category, timestamps and spatial location or user identification as the meta information, and calculated mean and variance are also considered meta information for similarity-based retrieval.". However, I could not find any point in the retrieval that the authors utilize meta information other than mean and std statistics. Could the authors point out where they used domain category, timestamps and spatial location or user identification as meta information during the retrieval phase?

2. In figure 2, the authors illustrate their algorithms and there is open-world textualizing knowledge in the top-right of the figure. Similar to the previous question, I could not understand where the authors specifically utilize meta information in ReinLLM Adapter phase. In line 303, the authors write that "In detail, the meta information is tokenized and concatenated by textual attributes into $\tilde{X}_m$.". Specifically, which meta information do the authors concatenate? How do the authors obtain these meta information and tokenize them?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents ZeroTS, a novel zero-shot time series prediction model designed to operate without task-specific fine-tuning, addressing data scarcity and adaptation across multiple domains. It introduces a unique framework for zero-shot time-series forecasting by leveraging Retrieval-Augmented Generation (RAG) to retrieve relevant time-series data and combining this with reinforcement learning to optimize interaction between a smaller learnable module and a large language model (LLM). Key contributions include a hybrid retrieval framework to address similarities in time series data and an efficient ReinLLM adapter, which integrates error feedback for more accurate predictions. Experiments show that ZeroTS provides competitive zero-shot and long-horizon forecasting performance while remaining parameter-efficient and memory-friendly.

### Strengths
- The paper presents a novel combination of RAG and reinforcement learning for zero-shot time series forecasting, which is an interesting and promising direction.
- ZeroTS demonstrates strong empirical performance on various benchmark datasets, achieving state-of-the-art results in zero-shot forecasting and competitive results in long-horizon forecasting.
- ZeroTS exhibits superior efficiency compared to existing LLM-based methods, requiring significantly less memory and achieving faster inference speeds, making it more practical for real-world applications.
- The ablation study substantiates the contributions of key components such as RAG, the ReinLLM adapter, and learnable parameters, strengthening the overall argument for the system’s design choices.
- The case study provides an intuitive understanding of how retrieved series can help improve prediction accuracy and mitigate LLM hallucinations.

### Weaknesses
 - The use of GPT-2 as the LLM backbone might be considered outdated, given the rapid advancements in LLM technology. Using a more recent and powerful LLM could potentially further enhance performance. Specifically, the limited context window and representational capacity of GPT-2 could hinder the model's ability to capture complex temporal dependencies in long time series. 
- While the authors address the complexity of the retrieval process, it remains a potential bottleneck for the scalability of the system. The proposed ρ-ρ-cut-off strategy, while reducing the search space, may still be computationally expensive for very large datasets. Further investigation into more efficient retrieval strategies, such as approximate nearest neighbor search or hierarchical indexing, is warranted.
- The paper acknowledges that ZeroTS shows weaker generalization when transferring from longer to shorter forecasting horizons. This aspect needs further investigation and improvement. The model's difficulty in adapting to finer-grained temporal resolutions suggests a potential limitation in its ability to capture multi-scale temporal patterns.
- The reliance on extensive time-series data for retrieval raises concerns about scenarios where domain-specific data is scarce or unavailable, potentially impacting generalizability. The model's performance could degrade significantly if the retrieval pool does not contain relevant series, highlighting a potential vulnerability in its zero-shot capabilities.
- The algorithm description in Algorithm 1 could benefit from additional clarity and elaboration. Providing more specific details on the interaction between the policy and value networks within the ReinLLM adapter, including the exact update rules and reward function, would enhance understanding. The lack of detail makes it difficult to fully grasp the learning dynamics of the adapter.
- While a hyperparameter study is presented, a more comprehensive discussion of the impact of different hyperparameters on performance across various datasets would strengthen the paper. The sensitivity of the model to hyperparameters, such as the number of retrieved series or the learning rate of the ReinLLM adapter, should be thoroughly investigated and reported.

### Questions
- How would the performance of ZeroTS be affected by using a more recent and powerful LLM, such as GPT-3 or Llama-3?
- What are the limitations of the proposed ρ-ρ-cut-off strategy for reducing retrieval complexity? Are there alternative strategies that could be explored for further efficiency improvement?
- What are the specific reasons behind the weaker generalization observed when transferring from longer to shorter prediction horizons? Are there potential modifications to the model architecture or training procedure that could address this issue?
- Could you provide a more detailed explanation of Algorithm 1, specifically focusing on the interaction between the policy network, the value network, and the update process of the series representations within the ReinLLM adapter?
- Could you elaborate on the choice of hyperparameters and their impact on performance across different datasets? Were there any specific challenges encountered during hyperparameter tuning?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes ZeroTS, a zero-shot time series forecasting approach that combines open-world knowledge and data regularities through multi-party data-model interactions. ZeroTS utilizes a TS-RAG (Retrieval-Augmented Generation) module to retrieve meta and series information, allowing domain-specific time series data as prompts. Additionally, the framework introduces a reinforcement learning-based adapter that uses ground-truth feedback to optimize a smaller model iteratively. Extensive experiments show ZeroTS obtains competitive results with reduced memory and inference speed, demonstrating its effectiveness and efficiency in zero-shot and long-horizon forecasting scenarios.

### Strengths
1. The paper attempts to bridge the gap between large language models and time series data, which is a relatively unexplored area. This integration could pave the way for new research directions and applications.

2. The proposed method is straightforward and intuitive, and the experiments shown in the paper are comprehensive. 

3. The readers can easily understand the proposed method and follow the content of the paper.

### Weaknesses
1. One challenge this paper addresses is constructing a time-series-oriented database for RAG construction. However, the authors did not compare their proposed methods with existing fully open-sourced time-series-oriented databases, such as TD-Engine [1]. It is strongly recommended to include this comparison to demonstrate the effectiveness and efficiency of their approach in time-series prompt retrieval.

2. The pre-trained structure of LLMs is heavily reliant on vast amounts of textual training data, which inherently limits their depth of understanding text input. This paper claims to address this limitation by extending LLMs' capabilities to encompass time-series data. However, the input to the LLM remains a sequential representation, making it still difficult for the model to fully capture the input without any further training. The method does not fundamentally address the limitation of LLMs being primarily trained on textual data, and thus the sequential representation might not be the most effective way to represent time-series data for an LLM.

3. Compared to other LLM-frozen baselines, such as Time-LLM, the performance improvements of ZeroTS are incremental and not substantial. A significance test should be conducted to further validate the effectiveness of the model for time series forecasting. The lack of a significance test makes it difficult to ascertain if the improvements are statistically meaningful or simply due to random variation.

4. In figure3, the paper shows they incorporate Llama2 as the LLM backbone in the paper. However, I did not find any experimental results shown in the paper. This discrepancy between the method description and experimental results raises concerns about the completeness and accuracy of the reported findings.

5. The paper overstates its contributions. Constructing a retrieval pipeline for RAG cannot be equated to building a database, as it lacks the fundamental structures, management capabilities, and persistence mechanisms inherent to databases. Properly distinguishing between a retrieval pipeline and a database system is essential to clarify the paper's actual contribution.

### Questions
Please refer to the weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper addresses the challenge of zero-shot time series prediction by introducing TS-RAG, a retrieval-based model that leverages an external database to enhance prediction performance. The authors begin by constructing a key-value database for retrieval-augmented generation  and subsequently design a retrieval scheme known as HSNSW. Additionally, they propose a reinforcement learning framework that incorporates both a policy and a value network to facilitate interaction between the data and the model, ultimately refining the output.

### Strengths
1. The problem addressed in this paper is significant, and the approach of exploring RAG in the context of time series prediction is novel.
2. The experimental results demonstrate a substantial improvement over other baseline methods.

### Weaknesses
1. The presentation of the paper requires refinement. For instance, the subcaptions in Figure 1 are encoded within the image and are too small to read. Additionally, the light green font used for references is difficult to see.

2. While the idea of incorporating external knowledge to enhance time series forecasting is noteworthy, it is not entirely new. Moreover, the paper introduces two key component, TS-RAG and LR for adaptation, but these elements are presented in isolation, which makes the overall contribution feel fragmented.

3. The choice of retrieval database is crucial for the practical application of this algorithm, yet this aspect is not addressed in the paper. The potential impact of varying the database remains unclear, which undermines the technical soundness of the approach.

4. The organization and writing of the paper need improvement. For example, $ W_c $ is introduced in Equation (1), but it is not referenced or explained in the following content, leading to confusion. Many notations and model details are unclear. For instance, what are HSNSW and HNSW, and are there any references that explain these concepts?

### Questions
1. You utilize three retrieval databases that do not overlap with the target datasets. How were these datasets chosen—was it based on expert knowledge? Is there a necessity for any relationship between the retrieval database and the inference dataset, such as sharing the same domain? Additionally, are there specific requirements regarding the scale of the databases?

2. Could you provide a clearer explanation of ReinLLM? What constitutes the action space of the policy network—does it only include kernel size? Besides, the whole adapter functions an additional component separate from the LLM. If so, why not simply use an additional network specifically for fine-tuning instead?

3. Recent studies on time series foundation models have focused on training across various domains of time series datasets. In this context, I have concerns about the impact of your work. What would happen if you trained a cross-domain model using your retrieval database in conjunction with the training dataset, or even just used the training dataset for fine-tuning?

I would consider increase my score if you can address my concerns about the choice of database and the necessity of your RL adaptor.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the use of large language models (LLMs) for zero-shot time series forecasting. To address scalability and flexibility, it proposes a solution using data-model interaction, including a TS-RAG data prompt and a reinforcement learning framework. Extensive experiments on zero-shot and long-term forecasting validate the effectiveness of the approach.

### Strengths
This paper proposes a TS-RAG data solution and a reinforcement learning framework. Extensive experiments demonstrate its effectiveness, and the code is provided.

### Weaknesses
1. The writing can be significantly improved. "TIME SERIES PREDICTION,"should be changed to "forecasting." ; Be better to use more common "TSF" instead of "TS" as the abbreviation for time series forecasting. Additionally, some expressions, like "While existing models, particularly large language models (LLMs) tailored for TS," are confusing. As far as I know, no LLMs are specifically tailored for time series, making this statement difficult to understand.

2. The motivation is not very clear and lacking a discussion of related work and comparision with key baselines. Many foundational time series models [1-5] have already been proposed, demonstrating strong zero-shot TSF capabilities with fewer parameters than LLMs. Furthermore, studies [6] have validated that LLMs are not useful for TSF, i.e. not  better than random initialization. In this context, the paper aims to use LLMs for zero-shot TSF, which raises questions about the motivation, both in terms of effectiveness and efficiency. The authors should discuss and Explicitly compare with foundational time series models; Directly address the findings from [6] about LLM effectiveness for TSF and explain how your approach differs or overcomes these limitations.

3. In addition, the zero-shot forecasting setting in this paper involves transferring from domain A to domain B. I acknowledge that this is also referred to as zero-shot in some literature. However, I am curious whether the paper could consider the more practical zero-shot setting used in [1-5], more "out-of-the-box", already well-supported by foundational time series models. Please expand evaluations to include this more practical zero-shot setting.

4. Allowing time series from different domains to serve as prompt may cause potential information leakage. Such as use data from other domains but in the future time period.

### Questions
Please check limitations

### Soundness
2

### Presentation
1

### Contribution
2
