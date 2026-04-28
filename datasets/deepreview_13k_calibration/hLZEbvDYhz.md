# UniAdapt: A Universal Adapter for Knowledge Calibration

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
Large Language Models (LLMs) require frequent updates to correct errors and keep pace with continuously evolving knowledge in a timely and effective manner. Recent research in {\it model editing} has highlighted the challenges in balancing generalization and locality, especially in the context of {\it lifelong model editing}. We discover that inserting knowledge directly into the model often causes conflicts and potentially disrupts other unrelated pre-trained knowledge. To address this problem, we introduce \tool, a \underline{uni}versal \underline{adapt}er for knowledge calibration. Inspired by the Mixture of Experts architecture and Retrieval-Augmented Generation, \tool~is designed with a vector-assisted router that is responsible for routing inputs to appropriate experts. The router maintains a vector store, including multiple shards, to construct routing vectors based on semantic similarity search results. \tool~is fully model-agnostic and designed for seamless plug-and-play integration. Experimental results show that \tool~outperforms existing lifelong model editors and achieves exceptional results in most metrics.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The main contribution of the paper is the development of UniAdapt, a universal adapter for lifelong model editing in Large Language Models (LLMs) that efficiently integrates new knowledge. The pursuit of lifelong model editing for LLMs is highly pertinent given the growing demand for adaptable AI systems. The concept is crucial for developing models that can continually learn and adapt without requiring full retraining.UniAdapt uses semantic similarity to route queries to the appropriate experts, significantly improving the model’s ability to adapt and generalize over traditional methods.

### Strengths
1. Lifelong model editing for LLMs is a promising research direction. The concept is crucial for developing LLM that can continually learn and adapt without requiring full retraining.

2. The experimental results demonstrate the effectiveness of the UniAdapt framework. By integrating a Mixture of Experts with the idea of  RAG, the paper shows improvements in model adaptability and performance on benchmarks designed to test these aspects.

### Weaknesses
 **Weakness 1**

The core motivation, as stated in the abstract:
>“We discover that inserting knowledge directly into the model often causes conflicts and potentially disrupts other unrelated pre-trained knowledge”

This motivation lacks novelty as reducing the disruption to pre-trained knowledge while inserting new information is a foundational objective of the entire knowledge editing field (*measured by the locality metric*), as extensively discussed in foundational papers such as “Fast Model Editing at Scale.”



**Weakness 2**

The paper’s primary contribution is applying the concept of a Mixture of Experts to the knowledge editing field. While technically sound, this application does not introduce many new insights into the field. Moreover, the implementation is described as complex and the overall concept may not engage the community due to its incremental nature rather than a groundbreaking innovation.


While the paper presents valid improvements in certain performance metrics for the chosen datasets, the novelty is somewhat limited, and the implementation is not elegant. Considering the high standards of ICLR, the paper could be seen as a borderline case. My overall score would be 5.5, reflecting a neutral to slightly positive evaluation but acknowledging the concerns regarding novelty and implementation complexity.

### Questions
Please refer to the previous section.

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
3

### Summary
The paper presents a novel approach to updating LLMs with new information without compromising existing knowledge. Traditional model-editing techniques often disrupt previous knowledge or fail to generalize well. UniAdapt addresses this by introducing a MoE architecture combined with a vector-assisted router, which selectively directs relevant queries to specific ``experts'' based on semantic similarity. This method allows seamless updates without altering the model’s core parameters, preserving unrelated knowledge effectively.

Experimental results on datasets such as zsRE and Counterfact demonstrate UniAdapt’s reliability in handling updates, generalizing edits, and maintaining unrelated knowledge compared to other methods. By keeping model stability high across thousands of sequential edits, UniAdapt emerges as a scalable, model-agnostic solution for maintaining LLMs with up-to-date knowledge, ideal for lifelong learning in dynamic environments.

### Strengths
1. UniAdapt's plug-and-play nature allows it to integrate with various LLMs without altering their original parameters, making it an adaptable and versatile solution for different base models.

2. By combining MoE with a vector-assisted router, UniAdapt selectively routes updates to specific ``experts'', effectively preserving existing knowledge while incorporating new information. This selective routing maintains a balance between reliability and generality.

3. The paper provides experimental evidence to show that UniAdapt performs better than baseline methods. UniAdapt performs well in datasets like zsRE and Counterfact.

### Weaknesses
1. The experiments were limited to GPT2-XL and LLaMA2-7B, which may not be sufficient to generalize the results. It would be helpful to include results on state-of-the-art LLMs across a range of model sizes (e.g., 13B and 70B) for more comprehensive insights. The absence of results on larger models makes it difficult to assess the scalability of the proposed method and its applicability to the most widely used models in the field. Specifically, the performance of the vector-assisted routing and the MoE architecture might behave differently when scaled to larger parameter spaces.

2. Regarding the effect of the target layer, it would be interesting to explore the effects of editing multiple layers simultaneously. Since layer behaviors might differ across models, further investigation on other models would be valuable to confirm similar patterns. Without this, the generalizability of the findings may be constrained. The current study only focuses on single-layer editing, and it is not clear how the method would perform if edits were distributed across multiple layers. This is important because different layers capture different levels of abstraction, and editing multiple layers could potentially improve the capacity to store new knowledge and the robustness of the edits.

3. UniAdapt's vector-assisted routing adds complexity, which may increase computational overhead. It would be beneficial to provide cost analysis for both training and inference. The paper lacks a detailed analysis of the computational resources required for training the router and for performing inference with the MoE architecture. This information is crucial for assessing the practical applicability of the method, especially in resource-constrained environments. Furthermore, it would be helpful to compare the computational cost of UniAdapt with that of other model editing techniques.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes  a universal adapter for knowledge calibration (UniAdapt). The experimental results show that UniAdapt achieves the significantly improved performance on various models and datasets.

### Strengths
UniAdapt is fully model-agnostic and designed for seamless plug-and-play integration.

### Weaknesses
The experimental analysis is not sufficiently thorough:

- There is no analysis of the resource consumption of different methods, such as inference time and memory usage.
-  The baselines are inconsistent across different vanilla models. Specifically, in Table 2, different base models use different baselines—for example, WISE is only applied to LLaMA2-7B, and MEMIT only to GPT2-XL. Why did the author choose this experimental setup?
-  There is a lack of Out-of-Distribution evaluation.

### Questions
The author states that the proposed method primarily aims to address the conflicts caused by directly inserting knowledge into the model. Which experimental result in the paper demonstrates the mitigation of this issue?

### Soundness
3

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
The paper addresses the challenge of updating and maintaining Large Language Models (LLMs) in a timely and effective manner.  To mitigate the lifelong editing problem, they introduce UniAdapt, a universal adapter designed for knowledge calibration. UniAdapt leverages a Mixture of Experts (MoE) architecture and Retrieval-Augmented Generation (RAG) to route inputs to the most relevant experts based on semantic similarity. The router maintains a vector store with multiple shards to construct routing vectors, ensuring precise calibration of the model's output. The adapter is designed to be fully model-agnostic and plug-and-play, making it versatile for various LLMs. Experimental results demonstrate that UniAdapt outperforms existing lifelong model editors in most metrics, showcasing its effectiveness in balancing generalization and locality.

### Strengths
1. The experimental results are compelling, showing that UniAdapt outperforms existing lifelong model editors. The paper provides detailed metrics and comparisons, demonstrating the adapter's ability to memorize and generalize effectively.

### Weaknesses
 - The citation format in the paper is not correct, making the reading difficult.
- The baseline is not comprehensive, the author just compared it with the WISE but other MoE methods like MEMoE and LEMoE are not considered. I think this would weaken the discussion in Table 1 and the contribution of the work as MoE is not a novel thing and the contribution should be more clear.
- The vector store here would be extra parameters and when the number of edits grows this would lead to more memory requirement and time computing, which makes me concerned about the efficiency of the proposed method. It's better to show an Inference Time Analysis.

### Questions
- When scaling up to 6k, what's the MoE setting such as the TopK and number of the experts.

### Soundness
3

### Presentation
2

### Contribution
2
