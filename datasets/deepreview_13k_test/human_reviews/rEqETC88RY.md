# LLM Bandit: Cost-Efficient LLM Generation via Preference-Conditioned Dynamic Routing

- Decision: Reject
- Scores: 6, 6, 6, 3

## Abstract
The rapid advancement in large language models (LLMs) has brought forth a diverse range of models with varying capabilities that excel in different tasks and domains. However, selecting the optimal LLM for user queries often involves a challenging trade-off between accuracy and cost, a problem exacerbated by the diverse demands of individual queries. In this work, we present a novel framework that formulates the LLM selection process as a multi-armed bandit problem, enabling dynamic and intelligent routing of queries to the most appropriate model. Our approach incorporates a preference-conditioned dynamic routing mechanism, allowing users to specify their preferences at inference time, thereby offering a customizable balance between performance and cost. Additionally, our selection policy is designed to generalize to unseen LLMs, ensuring adaptability to new models as they emerge. Experimental results demonstrate that our method achieves significant improvements in both accuracy and cost-effectiveness across various LLM platforms, showcasing the potential of our framework to adaptively optimize LLM selection in real-world scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This study introduces a novel framework for optimizing the selection of large language models (LLMs) based on user preferences, effectively balancing accuracy and cost. The research addresses the challenges associated with selecting appropriate LLMs, given their diverse capabilities and associated costs. By employing a multi-armed bandit approach with preference conditioning, the authors provide a flexible and efficient solution for optimizing LLM selection tailored to individual user needs. The results indicate significant improvements in both performance and cost management, positioning this framework as a promising avenue for future research in LLM utilization.

### Strengths
1. The proposed methods effectively address the issue of routing among multiple models (more than two), allowing for scalability beyond the RouteLLM baselines.
2. The authors present a pipeline consisting of model quizzing and preference-conditioned routing. For each component, they conduct optimization analysis and develop corresponding solution methods.
3. The comprehensive results across multiple tasks and domains demonstrate that the routing mechanism provides superior performance.

### Weaknesses
1. The experimental results presented solely in figures are difficult to interpret. The authors could enhance clarity by including results in tables along with relevant metrics.
2. The integration of a multi-armed bandit framework with dynamic routing based on user preferences introduces complexity to the overall system. This complexity may present challenges in terms of implementation, maintenance, and scalability, particularly for organizations with limited technical resources.
3. There is a lack of detailed exploration of the complex components of the routing policy, such as the specific parameter selection for model quizzing and comparison methods.

### Questions
1. The predictor baseline shows strong results when dealing with a family of LLMs in the experimental results. How should we interpret the differences between baselines in the "Family of LLMs" setting?
2. The additional computational requirements for dynamically generating and processing user preferences may lead to increased latency and resource consumption. Could the authors provide an efficiency analysis regarding this?
3. Data sensitivity is a critical issue. The effectiveness of dynamic routing heavily relies on accurately capturing user preferences. If users are unable to clearly articulate their needs or if their preferences change frequently, the system's performance may suffer due to misalignment between model selection and actual user requirements. How should datasets be prepared to address this?
4. RouteLLM provides MT-Bench results to demonstrate its effectiveness. According to the results in this study, RouteLLM appears to perform poorly on selected benchmarks. Could the authors provide a comparison on MT-Bench for both the baselines and the proposed methods?

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
The paper introduces a cost-efficient routing framework for selecting Large Language Models (LLMs) by framing the selection process as a multi-armed bandit problem. This dynamic routing mechanism leverages user preferences to balance between cost and performance, adjusting selections based on individual needs and allowing for generalization to new, unseen models. The method uses a model identity vector to represent each LLM’s strengths across various tasks, and an efficient quizzing mechanism for integrating new models with minimal evaluation. Experimental results show the effectiveness of this approach in achieving optimal trade-offs in real-world applications​.

### Strengths
- This paper formulates a novel multi-objective routing mechanism that balances performance and cost through dynamic, preference-conditioned routing, capturing the Pareto front for user-specific trade-offs.
  
- This paper develops a flexible, action-space-aware routing policy that generalizes effectively across various LLM models, leveraging extensive evaluation data to handle diverse user queries and model configurations.

- This paper introduces an efficient quizzing method to rapidly integrate new models by assessing a small subset of prompts, demonstrating the routing mechanism’s superior adaptability and performance across tasks and domains.

### Weaknesses
- This paper proposes a sophisticated method for training the routing policy. While it is detailed, the complexity makes it challenging to track which data (prompts, embeddings, preference labels, target values, prediction scores, costs) is used for pretraining and training each component and how they are acquired. Although careful reading of different sections and the appendix clarifies these elements, it requires significant effort.

- The policy training does not explicitly address uncertainty in reward prediction, raising concerns that diverse prompts and a large sample space may be necessary to avoid suboptimal routing decisions.

### Questions
* Can the model identity vector be trained end-to-end with the preference-conditioned routing policy? The objectives of score prediction and model identity vector seem to overlap.

* The routing policy design might be innovative, but the remaining components feel traditional. Is there additional novelty in the proposed training algorithm or the data used for the routing policy?

* Can you elaborate more on how the policy can balance exploration and exploitation without explicitly modeling the uncertainty in the value functions?

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduce a novel routing policy that optimizes the selection of LLMs based on user-specific preferences. The authors frame the model selection problem as a multi-objective optimization task, balancing performance and cost. They propose a preference-conditioned routing mechanism that dynamically adapts to individual user preferences during inference.

The proposed method generalizes across various LLMs and user preferences, demonstrating significant improvements in both performance and cost-efficiency. For example, the method showed generalization to unseen model from HuggingFace OpenLLM
v2 benchmark.

### Strengths
1. Generalization Across Diverse Models and Tasks: One of the key strengths of the proposed routing mechanism is its ability to generalize effectively across a wide range of LLMs and various user queries. The authors leverage the model identity vector, which allows the routing policy to adapt to new and unseen LLMs seamlessly.

2. Model Identity Vector: The introduction of the model identity vector is another significant strength of the paper. This vector encapsulates the strengths and weaknesses of each LLM based on its performance across a diverse set of evaluation prompts. Which could be helpful in other tasks

### Weaknesses
While the reinforcement learning component lends credibility to the results, the generalization—particularly to unseen models—appears to be on the use of a model identity vector. This is a very interesting concept, as proposed in [1] as "model embedding". The authors could have strengthened their approach by comparing it to [1]. In that work, a systematic method is proposed for generate the identity vector, closely resembling the approach in this paper, which employs KL penalties alongside predictions for pairwise comparisons and binary evaluation outcomes.

[1] EmbedLLM: Learning Compact Representations of Large Language Models

### Questions
Is it possible to marry the identity vector with the method proposed in [1] to further improve the routing performance?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a method to choose a suitable large language model given a prompt. The proposed method frames the problem as a bandit and then trains a representation for prompts and models. Then a utility function is trained to estimate the reward by calling a specific LLM on a specific prompt. Based on the score and users' preference a LLM is selected. Experiments show that the proposed method is effective and efficient.

### Strengths
The strengthens of this paper are listed as follows

1. The studied problem is crucial. Framing the model selection task as a bandit is also interesting

2. The experiment, which includes a wide range of models and datasets, is comprehensive

3. The proposed algorithm is simple yet effective as shown by the experiment

### Weaknesses
I have several concerns regarding the clarity, structure, and conceptual alignment of the paper, which are outlined as follows.

1. Clarity of Writing in Section 2: Section 2, particularly Section 2.3, was challenging to follow. There are several points where the explanation is incomplete or ambiguous:

- In Equation (2), it is unclear which parameter is being trained—whether it is $I_k$ or $f$. 

- The distribution $p$ and $q$ in equation (4) is not defined, and it is unclear why $I_k$ should be sampled from some dstribution

- In Equation (5), the definition of $I_k^T$ is missing.

Furthermore, Algorithm 1 describes the method in two stages: pretraining and training. However, these terms are not clearly defined in the main text, leaving their motivation unclear. It would be helpful if the author elaborated on the specifics of these stages and how they relate to the overall algorithm.

2. Bandit Problem Formulation: The choice to frame the problem as a bandit problem seems misaligned with the algorithm itself. When I encounter the term "bandit," I expect the use of specific online bandit algorithms or techniques. However, Algorithm 1 appears more akin to a supervised-learning approach, as it seems to use prompt-reward pairs to train the IRT model ($f$) and the model identity vector ($I_k$). So what is the motivation for framing this task as a bandit problem? It would be helpful if the author could more explicitly justify the bandit analogy.

3. Contribution elaboration: Some of the claimed contributions are not well-articulated or explained in the paper. For instance:

- In the second contribution, the author says they proposed a preference-conditioned mechanism. However there is no clear definition or explanation of what preference-conditioned means in the context of the paper. 

- Similarly, the term "action-space aware" in the third contribution is introduced but not sufficiently explained. This lack of clarity hinders understanding and prevents a full appreciation of the contribution. A more thorough explanation of these terms and their relevance to the method would be beneficial.

4. In Contribution 4, the author claims that the method generalizes across prompts by "leveraging a wide range of data." However, generalization typically refers to a model's ability to perform well on unseen data—not merely data it has been trained on. Therefore the usage of "generalization" here might not be proper.

### Questions
See weakness above

### Soundness
3

### Presentation
1

### Contribution
2
