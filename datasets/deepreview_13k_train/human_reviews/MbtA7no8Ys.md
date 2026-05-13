# Deciphering and Enhancing Commonsense Reasoning in LLMs from the Perspective of Intrinsic Factual Knowledge Retrieval

- Decision: Reject
- Scores: 5, 6, 3, 6

## Abstract
Commonsense reasoning in large language models (LLMs) bridges the gap to physical world, thus allowing them to think and behave more like humans. Previous research has shown that LLMs acquire the underlying factual knowledge from extensive training corpora and store it within their parameters. However, how LLMs apply this knowledge during the inference phase remains unclear. This lack of transparency makes it difficult to determine whether shortcomings in LLMs are due to a lack of factual knowledge or insufficient reasoning capabilities.
In this work, we aim to decipher the commonsense reasoning process into human-understandable steps. By interpreting the hidden states in different transformer layers and token positions, we uncover a specific mechanism by which LLMs execute reasoning.
Our extensive experiments indicate: 1) both attention head and multi-layer perceptron (MLP) contribute to the generation of factual knowledge from different perspective. 2) The process of commonsense reasoning in LLMs involves a clear sequence of knowledge augmentation, knowledge retrieval and answer generation, akin to retrieval-augmented generation.
Building on these findings, we have discovered that LLMs often contain relevant facutal knowledge but fail to retrieve the correct knowledge at top. To address this issure, we selectively fine-tuned the key heads and MLPs, resulting in notably improvements in reasoning performance in both in-domain and out-of-domain settings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates how Large Language Models (LLMs) perform commonsense reasoning by deciphering their internal mechanisms. The researchers discovered that LLMs execute reasoning through a five-stage process similar to Retrieval-Augmented Generation (RAG): knowledge augmentation, recall, re-ranking, rationale conclusion, and answer generation. The study found that both attention heads and multi-layer perceptrons (MLPs) contribute to factual knowledge generation from different perspectives. When LLMs fail at commonsense reasoning tasks, it's often due to incorrect knowledge retrieval rather than a lack of knowledge. To address this, the researchers developed a selective fine-tuning approach targeting specific attention heads and MLPs crucial for knowledge retrieval, which improved reasoning performance while modifying less than 10% of the model's parameters. The study was conducted using Llama2 and Gemma models, focusing on a standardized template for commonsense reasoning questions to ensure controlled experimentation.

### Strengths
1. This paper studies the internal mechanism for LLMs to conduct commonsense reasoning. The authors split the reasoning processes into 5 stages and find that the retrieval stage is the main source of reasoning errors. This paper provides insightful discovery of the underlying mechanism of LLMs.
2. Based on the new discovery, this paper also proposed a fine-tuning method that only focuses on top-K attention heads.
3. Extensively experimental results show the effectiveness of the methods.

### Weaknesses
1. The evaluation is limited to a small scope. The authors conduct their experiments solely on yes or no questions in the commonsense domain. More datasets with diverse formats should be included, like WinoGrande and SocialIQA. This eliminated scope impairs the conclusion of this paper and raises the doubt of generalization in more formats and more domains.
2. The evaluation of the paper heavily relies on GPT-4 for both data synthesis and analysis verification. The accuracy of GPT-4 on those tasks remains unclear, and the authors need to provide more experiments to show the agreement between GPT-4 and human experts.
3. The authors just used others' methods for efficient fine-tuning without any modification. In Section 3.3, the authors only use a single paragraph to finish the description of their methods for efficient tuning. Meanwhile, this methods is just a copy of previous method from the paper "Interpreting and improving large language models in arithmetic calculation."

### Questions
No

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
This paper investigates the commonsense reasoning capabilities of large language models (LLMs). The authors aim to make the reasoning process of LLMs more transparent and understandable by dissecting it into human-comprehensible steps. Through the analysis of hidden states in different transformer layers and token positions, the paper uncovers a mechanism by which LLMs execute reasoning. The commonsense reasoning process in LLMs is found to involve a sequence of knowledge augmentation, retrieval, and answer generation, similar to retrieval-augmented generation. The paper also identifies that LLMs often contain relevant factual knowledge but fail to retrieve it correctly. To address this, the authors selectively fine-tune key heads and MLPs, leading to improvements in reasoning performance.

### Strengths
-	The proposed approach provides a understanding of the inner workings of LLMs during commonsense reasoning.
-	The paper introduces a selective fine-tuning strategy that targets less than 10% of the model's parameters, leading to notable performance enhancements. It is particularly effective for out-of-domain settings.

### Weaknesses
 - The experiments are mainly conducted on specific models like Llama2-7B and Gemma2-9B. It would be better to expand the coverage of the experiments to include a wider range of model architectures and sizes, especially given the rapid development in the field. The current focus on two models limits the generalizability of the findings.
- Although GPT-4 is used to assist in the analysis, there may still be some uncertainty in the interpretation of the results. The "Interpreting Module" may not be completely accurate in all cases, and the reliance on a single LLM for interpretation introduces a potential bias. The lack of a more robust validation process for the interpretations is a concern.

### Questions
1.	How do the authors ensure that the selective fine-tuning approach does not lead to overfitting, particularly when focusing on specific components of the model?

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
3

### Summary
The paper investigates the commonsense reasoning processes within large language models (LLMs) by analyzing hidden states across layers and token positions using interpretability techniques such as Path Patching, Logit Lens, and Sparse Autoencoder. The authors propose a five-stage reasoning model within LLMs and identify specific failures in knowledge retrieval. To enhance reasoning performance, they introduce a selective supervised fine-tuning (SSFT) approach that targets specific layers of the model. Experiments demonstrate slight improvements over full-model fine-tuning, particularly in out-of-domain tasks, suggesting potential benefits of selective tuning for commonsense reasoning tasks.

### Strengths
•	Application of Interpretability Techniques: The use of Path Patching, Logit Lens, and Sparse Autoencoder offers a diverse set of tools to interpret commonsense reasoning within LLMs.

•	Focused Analysis on Model Components: The identification of key components, such as attention heads and MLP layers, that influence commonsense reasoning could inform future efforts to improve model architectures.

•	Resource-Efficient Fine-Tuning: Introducing SSFT presents a potentially more efficient alternative to full-model fine-tuning, showing moderate improvements in certain scenarios.

### Weaknesses
•	Limited Novelty: The proposed reasoning process and interpretability insights do not substantially differ from existing concepts, limiting the originality of the work. The identified stages of knowledge augmentation and retrieval are well-established in prior literature, and the addition of a re-ranking stage, while potentially relevant, lacks a clear demonstration of unique mechanistic insights. The interpretability techniques, while diverse, are applied in a fairly standard manner, without revealing novel aspects of the model's internal representations or processing.

•	Marginal Improvements from SSFT: The performance gains from selective fine-tuning are minimal, making it unclear whether the approach offers significant advantages over existing methods. The reported improvements are not substantial enough to justify the added complexity of the selective fine-tuning approach, especially given the potential for increased computational overhead compared to standard fine-tuning. The lack of a more rigorous comparison with other targeted fine-tuning methods further weakens the claims of efficiency.

•	Surface-Level Interpretability Analysis: The interpretability techniques are applied without providing deep insights into the specific reasons behind the model’s failures in commonsense reasoning tasks. While the authors identify the re-ranking stage as a source of errors, the analysis does not delve into the underlying mechanisms that cause the model to select incorrect attributes. The analysis lacks a detailed examination of the specific attention patterns or neuron activations that lead to these errors, which limits the practical utility of the findings.

•	Narrow Experimental Scope: The experiments focus on a limited set of datasets, lacking diversity that could provide a more comprehensive evaluation of the model’s reasoning abilities across different contexts. The reliance on a single dataset for the primary analysis limits the generalizability of the findings. The lack of experiments on datasets with different reasoning requirements or knowledge domains makes it difficult to assess the robustness of the proposed approach.

### Questions
1. Have the authors tested the SSFT approach on larger models or more complex tasks to assess its broader applicability?

2. How does this work differentiate itself from prior studies on retrieval-augmented generation and knowledge editing, and what unique insights does it provide on commonsense reasoning?

3. Are there plans to extend the interpretability analysis to explore deeper relationships between reasoning components, such as hierarchical or causal connections?

### Soundness
3

### Presentation
2

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
The paper employs techniques such as Path Patching, Logit Lens, and Sparse AutoEncoders (SAE) to interpret the internal mechanisms of large language models (LLMs) in commonsense reasoning. Specifically, the authors find that: (1) certain positions in the LLM's internal states augment attribute information; (2) later tokens also encode significant attribute information across multiple layers; (3) deeper MLP layers are responsible for retrieving and reranking relevant knowledge; and (4) the final answer is largely a result of transferring and consolidating this accumulated previous information.  
Building on these, they analyze the error distribution and discover that most errors stem from the model’s failure to retrieve relevant knowledge. As a result, they selectively fine-tune specific attention heads and MLP layers to enhance the model's ability to retrieve and rerank knowledge. Through experiments they show that the proposed SSFT (Selective Supervised Fine-Tuning) technique outperforms standard SFT while using less than 10% of the model’s parameters.

### Strengths
1)	The paper provides a detailed analysis of how the internal states of LLMs function during commonsense reasoning, making the mechanisms of LLMs more transparent. The reviewer believes this will interest a broad audience within the community and serve as a foundation for future research.

2)	The paper introduces a novel fine-tuning technique (SSFT) that selectively fine-tunes the most critical attention heads and MLP layers, achieving improved performance with significantly reduced computational resources.

### Weaknesses
1.	The methodology section could benefit from additional details, particularly in Section 3.2, which covers the interpreting module. Providing more explanation on how each of the modules works would be helpful for readers who are not familiar with these techniques, as currently, they may need to consult other papers. The reviewer suggests that adding these details would enhance the coherence and readability of the paper. Specifically, the paper should elaborate on how Path Patching identifies critical attention heads, how Logit Lens attributes token importance across different layers (MLP, attention, residual), and how Sparse Autoencoders (SAE) are used to decode the information encoded in specific MLP layers. Furthermore, the paper should explain how attention head pattern analysis is used to understand the information flow between tokens.
2.	The writing in the Experiment Results section could be further refined, especially in sections 4.2, 4.3, and 4.4. There are two issues that the reviewer may think to consider for improvement:   
   a.	When introducing specific terms like “concept” and “attributes”, it would be useful to refer back to the Preliminary section or include footnotes to avoid confusion. Readers might be unclear about which specific concepts or attributes you are referring to, given that multiple are mentioned in the preliminary section. Similarly, the distinction between “general attribute” and “predicted attribute”, which appears frequently in these sections, could be clarified to avoid ambiguity. For example, when discussing the 'Ganesha' concept, it is unclear if 'Hindu' is the predicted attribute, and what other general attributes are considered. A clear definition of these terms with examples is needed.
        b.	Another improvement would be to more explicitly connect each section. Upon first reading, it can be difficult to understand how sections like 4.3 build on 4.2, and I had to spend some time figuring out the relationships. Explaining how each section progresses and relates to the previous one would help guide the reader through the flow of the results. For instance, it is not immediately clear how the findings on attribute information in section 4.2 directly motivate the analysis of attribute evolution across layers in section 4.3, or how these two sections lead to the knowledge retrieval analysis in 4.4. A more explicit narrative is needed to connect these sections.

3.	More explanation could be added to the figures to assist with interpretation. While the figures look visually informative, they take some time to understand. For example, Figure 6a lacks guidance on how it should be interpreted, and adding this clarification would make it easier for readers to grasp the key points. Specifically, the paper should explain what the node size represents in Figure 6a, and how the attention heads are selected for visualization. The paper should also clarify how the figure demonstrates the transfer of semantic information.
4.	The logic error example in Section 4.6 is a bit confusing. In the correct answer, it states that Sony sold more units than Sega but concludes that “Sony did not win the war”, which seems contradictory. Given that Sony outsold Sega, shouldn’t the conclusion be “Sony win the war”? This contradiction between the conclusion and the green-underlined statements needs further clarification to resolve the confusion. The example should be revised to ensure the conclusion logically follows from the provided statements.
5.	There are way too many citation format problems: e.g., line 080, “Wang et al. (2023a)” -> “(Wang et al. 2023a)”. The reviewer hopes that the authors thoroughly check all related issues and fully polish the paper presentation.
6.	In the main experimental results presented in Table 2, the authors only compare the results using the Llama2 as the backbone LLM. Yet they do not analyze the performance across other important relevant LLMs, both open-sourced and proprietary. This omission likely limits the generalizability of the conclusions drawn from the proposed method. The reviewer thus suggests adding more MLLMs for experimental comparison. Specifically, the paper should include results from models such as Qwen, or other models of similar scale, to validate the robustness of the findings. The paper should also discuss the challenges of applying the method to closed-source models.
7.	More importantly, the reviewer may have identified a problem with the baselines used for comparison by the authors. For instance, they have ignored the performance comparison with all successful RAG-related methods, which should have been included in Table 2. Thus, the reviewer is a little bit skeptical about the consistency of the conclusions. Please provide further detailed explanations. The paper should include a comparison with RAG methods, and discuss why the proposed method is superior, or when it is more appropriate to use the proposed method over RAG.

### Questions
1.	Are the probing experiments conducted based on the average results across both datasets, StrategyQA and CommonsenseQA? Have you observed any differences in model behavior between these two datasets?
2.	Could you clarify the distinction between “General Attribute” and “Predicted Attribute”?
3.	What are the exact values for k and l in the SSFT experiment setup? Just to confirm, do these parameters refer to the attention heads and MLP layers you found in section 4.4 as responsible for retrieving and reranking knowledge in the LLM?
4.	Do the authors plan to release the code? the reviewer could not find any provided code or metadata that would allow for a technical review of the details.

### Soundness
3

### Presentation
2

### Contribution
3
