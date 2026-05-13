# Q-Adapter: Customizing Pre-trained LLMs to New Preferences with Forgetting Mitigation

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Large Language Models (LLMs), trained on a large amount of corpus, have demonstrated remarkable abilities. However, it may not be sufficient to directly apply open-source LLMs like Llama to certain real-world scenarios, since most of them are trained for \emph{general} purposes. Thus, the demands for customizing publicly available LLMs emerge, but are currently under-studied. In this work, we consider customizing pre-trained LLMs with new human preferences. Specifically, the LLM should not only meet the new preference but also preserve its original capabilities after customization. Drawing inspiration from the observation that human preference can be expressed as a reward model, we propose to cast LLM customization as optimizing the sum of two reward functions, one of which (denoted as $r_1$) was used to pre-train the LLM while the other (denoted as $r_2$) characterizes the new human preference. The obstacle here is that both reward functions are unknown, making the application of modern reinforcement learning methods infeasible. Thanks to the residual Q-learning framework, we can restore the customized LLM with the pre-trained LLM and the \emph{residual Q-function} without the reward function $r_1$. Moreover, we find that for a fixed pre-trained LLM, the reward function $r_2$ can be derived from the residual Q-function, enabling us to directly learn the residual Q-function from the new human preference data upon the Bradley-Terry model. We name our method \abbr as it introduces an adapter module to approximate the residual Q-function for customizing the pre-trained LLM towards the new preference. Experiments based on the Llama-3.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors of this paper aim to discuss the customization process of LLMs, focusing on adding new preferences to open-source LLMs without losing original knowledge to meet specific application needs. The authors propose a novel approach called Q-Adapter. Q-Adapter redefines LLM customization as a reward maximization problem and utilizes a residual Q-learning framework with a new loss function to implement a customization process that aligns with new preferences. This framework enables direct learning on preference data, thereby avoiding the problem of forgetting the original model.

### Strengths
1. The idea of applying the reinforcement learning method to LLM customization is novel. Many existing works focus on adapting models to new contexts through fine-tuning. This can alter the model's original knowledge structure and decrease performance on other tasks. The method proposed by the authors enables alignment with new preferences without the need to change the original structure of the LLM. 

2. Q-Adapter can learn directly from preference data without accessing or modifying the original reward functions used during the initial model training. This direct learning approach reduces the complexities of retraining or fine-tuning models on new datasets, making it easier to transfer and deploy the method to new tasks.

3. The authors provide sufficient mathematical derivations and experimental parameters in the paper and its appendices, which aids in replicating the experiments described in the paper.

### Weaknesses
1. According to Section 4, the effectiveness of this framework highly depends on the quality and relevance of the training preference data. The author may further discuss the impact of noise and the limitation of the model's ability to align with user preferences accurately within more datasets. Specifically, the paper should explore how varying levels of noise in the preference data affect the convergence and stability of the Q-learning process. Furthermore, it would be beneficial to analyze the model's sensitivity to different types of noise (e.g., label flipping, irrelevant preferences) and discuss potential mitigation strategies. The current discussion lacks a detailed analysis of these crucial aspects.

2. In Section 5, the authors only compare the Q-Adapter with two Policy Regularization baselines, DPO and PPO. The authors should include more up-to-date baselines in their experiments to better validate the effectiveness of their method. The choice of baselines is limited, and the paper would benefit from comparisons with more recent methods that also aim to preserve original model knowledge while adapting to new preferences. This would provide a more comprehensive evaluation of the proposed approach's strengths and weaknesses.

### Questions
1. According to Section 5.1, the evaluation metrics may need further clarification. It seems that in all tasks, including MMLU, MMLU Pro, GSM8K, BBH, and IFEval, the Base Model shows the highest score compared to other methods. 

2. In section 5.2, the authors evaluate the model's capabilities in learning new preferences only by demonstrating the evaluation of OpenAI GPT-4o. This evaluation is insufficient; the author may further discuss the evaluation results from other LLMs and human labelers.

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
3

### Summary
This paper proposes a Q-learning-based customization approach for adapting LLMs to new user preferences. The authors introduce Q-Adapter, which employs residual Q-learning to incorporate specific preferences while retaining the LLM's original knowledge base. Experimental results show that Q-Adapter effectively mitigates forgetting, allowing customized models to perform well on both general and preference-specific tasks​.

### Strengths
1. The methods are described systematically and in detail. In the methodology section, the authors clearly explain each step in the Q-learning-based customization process. 

2. The design choices, such as selecting embedding models, are well justified within the context of LLMs adaptation. The model compatibility and customization needs are clearly discussed, and the chosen embedding models align with the goals. This method effectively balances retaining general knowledge with integrating user-specific preferences.

3. Their clear discussion of each step of their methodology and the discussion of their variants prepare the reader for their experiments with the techniques.

### Weaknesses
1. In Section Judgments from LLMs, the evaluation with GPT-4o is not convincing. The LLM-as-a-judge is intended to provide an objective and robust assessment of model outputs across different dimensions. However, simply using GPT-4o for evaluation actually introduces potential biases and lacks the transparency needed for reliable performance validation. Specifically, the lack of inter-annotator agreement metrics for the LLM judgments raises concerns about the consistency and reliability of the evaluation. Without knowing the variance in GPT-4o's judgments, it's difficult to ascertain the statistical significance of the reported results. Furthermore, the prompt engineering used to elicit these judgments is not detailed, making it hard to assess whether the LLM's evaluation is truly objective or influenced by subtle prompt variations.

2. For the experimental result, the authors may add more analysis as the performance of this Q-Adapter does not significantly outperform baseline methods. For example, there is minimal improvement in the BBH dataset (Table 1), and without error analysis, it is challenging to demonstrate the method's effectiveness. The lack of statistical significance testing on the reported improvements further weakens the claims. It is unclear whether the observed differences are due to the proposed method or simply random variation. A more granular analysis, such as examining performance on specific sub-tasks within the datasets, would be beneficial to understand the method's strengths and weaknesses. Additionally, a comparison of the computational cost and efficiency of Q-Adapter against baseline methods is missing, making it difficult to assess its practical applicability.

3. Also the paper lacks a thorough discussion on the computational overhead or practical considerations associated with deploying Q-Adapter. The paper does not discuss the memory footprint of the Q-Adapter, which is crucial for deployment on resource-constrained devices. The inference time overhead of using both the base model and the adapter is also not clearly addressed. Without these details, it is difficult to assess the practical feasibility of the proposed method.

### Questions
1. The result in Table 1 is confusing, as the base model seems to have the best performance. Could any training harm the model's performance?

2. The paper employs the DSP and HH-RLHF datasets but does not explain the criteria for selecting these datasets over other domain-specific or preference-aligned datasets (Section 5.1, Experimental Setup). What are the key attributes of these datasets that make them particularly suitable for evaluating Q-Adapter’s capabilities in preserving and adapting model preferences?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a Q-learning-based customization approach for adapting pre-trained LLMs to new human preferences. The authors develop a method called Q-Adapter, which uses a residual Q-function to learn new preferences while preserving the LLM's original knowledge. They conduct a series of experiments to validate the effectiveness of Q-Adapter compared with baseline methods.

### Strengths
The idea of using a Q-learning-based customization approach to adapt LLMs to new human preferences without overwriting existing knowledge is innovative. Most existing work focuses on fine-tuning or prompt-based adaptation, but these approaches cannot effectively preserve the model’s original knowledge, often leading to catastrophic forgetting and limiting the adaptability of LLMs in learning new preferences while retaining prior abilities. This Q-Adapter method employs a residual Q-function to incrementally learn user-specific preferences, as well as successfully mitigate forgetting issues associated with traditional fine-tuning.

The mathematical derivations are thorough and presented. And the workflow is reasonable, as it integrates Q-learning with residual functions to balance learning new preferences while maintaining existing knowledge systematically. This approach improves model adaptability and further enhances stability in customization tasks across various user-specific requirements.

### Weaknesses
In the experiment, the authors do not compare their method with some SOTA methods other than PPO and DPO (See Questions). Also they only use GPT-4o as a judge (Judgments from LLMs part). Although it is common to use LLM-as-a-judge for similar tasks, the authors may consider using more models, especially those with more explainability or reasoning ability for their ranking and evaluation.

### Questions
Authors may consider referring to and comparing with:
https://arxiv.org/abs/2404.14723 
https://arxiv.org/abs/2402.01306
https://arxiv.org/abs/2405.00675
https://proceedings.mlr.press/v238/gheshlaghi-azar24a.html

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
Large Language Models (LLMs), trained on a large amount of corpus, have demonstrated remarkable abilities. However, it may not be sufficient to directly apply open-source LLMs like Llama to certain real-world scenarios, since most of them are trained for general purposes. Thus, the demands for customizing publicly available LLMs emerge. This paper introduces Q-Adapter, a method that directly learns the residual Q-function from new human preference data, bypassing the need to learn a reward function. With the residual Q-function and the pretrained LLM, Q-Adapter are able to generate responses that not only meet the preference in the dataset, but also inherit knowledge of the pre-trained LLM. The experimental results show that Q-Adapter on both retaining existing knowledge and learning new preferences.

### Strengths
1. The writing is generally clear and fluent. 
2. The idea is well-motivated and easy-to-follow.
3. Based on the results provided in the paper, the Q-Adapter demonstrates good performance.

### Weaknesses
1. In Table 1, under the Category: Business, the PR (PPO) method shows a significantly lower performance compared to the other baselines (this is not as evident in other categories).
2. The study could include full parameter fine-tuning and additional baselines for comparison, such as other forgetting mitigation techniques or model fine-tuning strategies (e.g., NEFTune), to provide a more comprehensive evaluation of Q-Adapter's performance.

### Questions
Please refer to “Weakness”

### Soundness
3

### Presentation
3

### Contribution
2
