# Weighted Multi-Prompt Learning with Description-free Large Language Model Distillation

- Decision: Accept
- Scores: 6, 6, 8, 6, 6

## Abstract
Recent advances in pre-trained Vision Language Models (VLMs) have shown promising potential through \textit{prompt learning} in effectively adapting to downstream tasks without requiring additional annotated paired datasets.
To supplement text information in VLMs dependently trained on correlation with vision data, new approaches leveraging Large Language Models (LLM) in prompts have been proposed, enhancing robustness to unseen and diverse data.
Existing methods query LLM for text-based responses (i.e., \textit{descriptions}) to utilize in prompts, but this approach has limitations: high variability and low reliability.
In this work, we propose \textbf{De}scription-free \textbf{Mul}ti-prompt Learning(\textbf{DeMul}) for image recognition task, a novel method that eliminates the process of extracting descriptions and instead directly distills knowledge from LLM into prompts.
By adopting a description-free approach, prompts can encapsulate richer semantics and still be defined as continuous vectors to optimize, thereby eliminating the need for discrete pre-defined templates.
Additionally, in a multi-prompt setting, we have empirically shown the potential of using prompt weighting to reflect the importance of different prompts during training.
Experimental results demonstrate that our approach achieves superior performance across 11 recognition datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper explores using large language models (LLMs) to enhance prompt learning for vision-language models. It proposes a description-free method to distill knowledge from LLMs into learnable prompts by directly aligning their embeddings. Additionally, a multi-prompt strategy is examined to improve performance. Experiments on few-shot learning benchmarks and ablation studies demonstrate the effectiveness of the proposed method.

### Strengths
1. The paper is well-crafted with clear expressions, making it easy to understand.

2. The description-free distillation approach for training learnable prompts is interesting, novel, and effective. It is also more cost-effective than description-needed methods, which require multiple queries to models like GPT for comprehensive descriptions.

3. The study on diverse semantics and the importance of multiple learnable prompts is well-motivated.

4. The extensive few-shot learning experiments and comprehensive ablation study effectively demonstrate the proposed methods and each module.

### Weaknesses
1. Although the paper demonstrates superior few-shot performance, the notable aspect is the open-vocabulary ability of CLIP. Since 2023, literature has focused on improving this aspect. Additional experiments on this topic are suggested.

2. The authors should discuss whether the proposed distillation method works when ground-truth training data is missing. Solely text-side fine-tuning may lead to misalignment with the visual side. If it doesn't work, this limitation should be addressed.

3. The computational costs, including time and memory during training and inference, should be compared to existing methods. This is especially important because multiple prompts can introduce substantial costs, particularly when dealing with a large number of classes, such as in ImageNet-1K.

4. The symbol $t$ is defined both as prompt embeddings (L198) and learnable prompt vectors (L202); these should be differentiated.

### Questions
In line 7 of Algorithm 1, why do the text embeddings $g(c_i)$ from the output of the CLIP text encoder go through the encoder again?

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
5

### Summary
The paper proposes to learn richer prompts for Vision Language Models (VLMs) by mapping them to the Embedding Endpoint of GPTs. They aim to capture meaningful semantics by directly distilling the pre-trained knowledge of GPT without the use of explicit description queries. The improvement in the quality of prompts is achieved by minimizing the distillation loss between the prompt embedding space and the LLM embedding space to better capture the class orientations. The authors have also used a multi-prompt setting to assess the best semantics from a weighted prompt pool. The authors use a multi-prompt setting with prompt weighting. The approach is shown to work well in few-shot image classification scenario.

### Strengths
1.	The paper looks into an interesting direction of enriching prompts using cyclic distillation from LLM embedding spaces. It mitigates the explicit description queries for the class-names of a given dataset.
2.	The description-free approach with multi-prompt weighting seems to be effective in few-shot image classification.
3.	The paper is well organized and easy to follow.

### Weaknesses
1.	It seems that the pretraining has to be done on a dataset which covers all the category names in the evaluation. This would significantly limit the generalizability of the method. Also is class-names a good attribute for mapping the LLM embeddings?
2.	As mapping functions need to be pretrained, what is the computational cost incurred? Also, it seems that the comprehensive dataset required a lot of samples from a long list of class-names to cover all datasets. Such an approach is prone to noise and biases. The authors should clarify the function pretraining in detail and make their approach more generalizable.
3.	Considering Figure 3, the performance of DeMul is negligible in 6 out of 11 datasets compared to other approaches such as GalLoP. This significantly diminishes the efficacy of the approach.
4.	The major weakness of the paper is very limited evaluation. The authors have limited their approach to only few-shot image classification while all the recent relevant works [CoCoOp (Zhou et al., 2022a), GalLoP (Lafon et al., 2024), MaPLe (Khattak et al., 2023a)] show their efficacy on 1. Domain Generalization 2. Base-to-New Generalization and 3. Cross-Dataset Transfer in addition to few-shot downstream image classification. Without such comparison it is hard to judge the goodness of the proposed approach beyond the single task of few-shot downstream image classification.
5.	Distilling LLM text to learnable prompts and prompt weighting separately have been explored in some of the recent works. Such as [a] or [b]. The author should discuss these references in the related work section and explicitly explain how their work is distinct from these similar studies.

### Questions
The weaknesses are already given in the question form. In addition, here are a few additional questions.
1. How is the value of $\alpha$ chosen? Is there any sensitivity analysis on $\alpha$?
2. Are the experiments run for different random splits of training data? Then are the reported values the average over these?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a novel approach called DeMul for few-shot image recognition. The method leverages pre-trained VLMs and bypasses the need for extracting textual descriptions from LLMs by directly distilling knowledge from the LLM into learnable prompts. This description-free approach effectively addresses the variability and potential unreliability of LLM-generated descriptions in previous methods.

### Strengths
Originality: The description-free distillation is a novel concept that cleverly addresses a key limitation of existing LLM-enhanced prompt learning methods. The weighted multi-prompt learning strategy further enhances the originality of the approach.

Quality: The paper presents compelling empirical results across 11 diverse datasets, with DeMul consistently outperforming existing zero-shot and few-shot methods, including state-of-the-art techniques like GalLoP. The comprehensive experimental setup and ablation studies further strengthen the quality of the evaluation.

Clarity: The paper is well-organized and easy to understand. The motivation, methodology, and experimental results are presented clearly and concisely. The figures and tables are informative and effectively illustrate the key concepts and findings.

Significance: DeMul simplifies the prompt engineering process and improves the reliability of VLM-based image recognition by eliminating the need for textual descriptions. The significant performance gains in few-shot learning scenarios demonstrate its practical value. Furthermore, its core ideas could potentially be applied to other VLM tasks, broadening its impact.

### Weaknesses
Limited analysis of the mapping function: While the paper introduces the concept of a mapping function, the exploration of its properties remains superficial, lacking quantitative analysis to assess its effectiveness. Specifically, the paper does not delve into the mapping function's sensitivity to the size and diversity of the training data used to learn the mapping. The potential for the mapping to introduce biases or amplify noise present in the training data is also not addressed. Furthermore, the choice of the specific mapping architecture (e.g., MLP) is not justified with sufficient analysis, and alternative mapping strategies are not explored.

Dependence on training data distribution: The paper acknowledges the potential sensitivity of DeMul to the training data distribution but lacks an in-depth investigation of this sensitivity. The paper does not explore how variations in the training data distribution might impact the learned prompts and the overall performance of the model. This includes a lack of analysis on how the model performs when the training data is imbalanced or when the test data comes from a different distribution than the training data.

Shared learnable vectors: While improving memory efficiency, shared learnable vectors might limit the model's ability to capture class-specific prompt information. The paper does not provide a detailed analysis of the trade-off between memory efficiency and representational power. The potential for shared vectors to cause interference between different classes is not explored, and alternative approaches such as class-specific vectors or a hybrid approach are not considered.

Lack of theoretical support: The paper primarily focuses on empirical results and lacks a strong theoretical foundation to explain the effectiveness of the method. The paper does not provide any theoretical analysis to explain why the proposed distillation approach works, nor does it offer insights into the underlying mechanisms that contribute to the observed performance gains. This lack of theoretical grounding makes it difficult to generalize the results or understand the limitations of the method.

### Questions
1、Provide a more detailed analysis of the mapping function's properties and explore alternative mapping strategies.
2、Investigate the performance variations under different training data splits and explore data augmentation techniques to improve robustness.
3、Evaluate the memory savings from shared learnable vectors and explore alternative approaches to balance memory efficiency and representational power.
4、Attempt to provide some theoretical analysis to explain the observed performance gains.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes Description-free Multi-prompt Learning (DeMul), a method that enhances image recognition tasks by distilling knowledge directly from LLMs without needing descriptive text prompts. This method enables flexible prompt learning by mapping learnable prompts into the LLM embedding space and using weighted multi-prompt learning to adjust prompt importance dynamically. Experimental results across 11 datasets show that DeMul outperforms conventional description-based methods and other prompt optimization approaches.

### Strengths
(1) Well-structured and clearly explains the limitations of existing description-based prompt methods.

(2) Extensive experiments across 11 datasets demonstrate the robustness and effectiveness of the proposed method.

(3) While the novelty in the method may be incremental, applying weighted multi-prompt learning without description reliance addresses the practical limitations of prior work.

### Weaknesses
1. Figure 1 highlights the variability in GPT-based descriptions, but this diversity can actually be beneficial in image classification. The goal of descriptions is to enrich the semantic variety within each class, helping the model handle diverse images within the same category, rather than strictly aligning with the class name. By dismissing this variability, the proposed approach might miss out on the robustness provided by diverse descriptions.

2. Mapping prompt descriptions to the GPT embedding space may reduce interpretability, as this space is abstract and lacks human-interpretable structure. The optimizations in this space might rely more on implicit semantic relationships rather than explicit, understandable features, which could obscure the interpretability of the learned representations.

3.The paper does not reference or explain Algorithm 1: Training process of DeMul, which leaves readers without guidance on understanding the step-by-step training procedure of the proposed method.

4. The description of Equation (4) suggests averaging classification probabilities across prompts, but the actual implementation seems to involve averaging the text embeddings of prompts instead. 

5.T he Preliminaries and Background section lacks appropriate citations, which limits the clarity.               

6. The paper specifies fixed values for the regularization weight  and the loss balance parameter, but does not provide ablation studies to justify these choices.

7. The Related Work section lacks a clear articulation of the limitations in existing methods and how the proposed approach addresses these gaps.

8.The paper claims that the weights \({w_{ij}}\) for each class are normalized, ensuring that \(\sum_{j=1}^{M} w_{ij} = 1\). However, in Figure 5, the sum of the weights for the five prompts appears to exceed 1, which contradicts this claim.

9. In the ablation study presented in Table 1, the difference in accuracy between "Ours w/o weighted" (85.2) and "Ours" (85.3) in the 16-shot setting is minimal

### Questions
See the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Description-free Multi-prompt Learning (DeMul), a new method for prompt learning in vision-language models that eliminates the need for descriptive text by directly distilling knowledge from large language models (LLMs) like GPT. The approach optimizes prompts in the LLM embedding space and incorporates weighted multi-prompt learning, allowing prompts to capture diverse semantics and improve few-shot classification performance. Experimental results across 11 datasets show that DeMul outperforms traditional description-based methods, simplifying prompt learning while preserving rich semantics.

### Strengths
1.The proposed method does not require text descriptions or specific prompt design, while still preserving rich semantic expression.  
2.The proposed Weighted Multi-Prompt Learning effectively captures the relative importance of different prompts, enhancing model adaptability and performance.

### Weaknesses
1.Figure 1 highlights the variability in GPT-based descriptions, but this diversity can actually be beneficial in image classification. The goal of descriptions is to enrich the semantic variety within each class, helping the model handle diverse images within the same category, rather than strictly aligning with the class name. By dismissing this variability, the proposed approach might miss out on the robustness provided by diverse descriptions.

2.Mapping prompt descriptions to the GPT embedding space may reduce interpretability, as this space is abstract and lacks human-interpretable structure. The optimizations in this space might rely more on implicit semantic relationships rather than explicit, understandable features, which could obscure the interpretability of the learned representations.

3.The paper does not reference or explain Algorithm 1: Training process of DeMul, which leaves readers without guidance on understanding the step-by-step training procedure of the proposed method.

4.The description of Equation (4) suggests averaging classification probabilities across prompts, but the actual implementation seems to involve averaging the text embeddings of prompts instead. 

5.The Preliminaries and Background section lacks appropriate citations, which limits the clarity.               

6.The paper specifies fixed values for the regularization weight  and the loss balance parameter, but does not provide ablation studies to justify these choices.

7.The Related Work section lacks a clear articulation of the limitations in existing methods and how the proposed approach addresses these gaps.

8.The paper claims that the weights \(w_{ij}\) for each class are normalized, ensuring that \(\sum_{j=1}^{M} w_{ij} = 1\). However, in Figure 5, the sum of the weights for the five prompts appears to exceed 1, which contradicts this claim.

9.In the ablation study presented in Table 1, the difference in accuracy between "Ours w/o weighted" (85.2) and "Ours" (85.3) in the 16-shot setting is minimal, with only a 0.1% improvement when using the proposed weighting mechanism. This marginal difference raises questions about the practical impact of the weighted approach.

### Questions
No questions or suggestions.

### Soundness
3

### Presentation
3

### Contribution
3
