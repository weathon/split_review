# RootTracker: A Lightweight Framework to Trace Original Models of Fine-tuned LLMs in Black-Box Conditions

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5

## Abstract
Large Language Models (LLMs) demonstrate remarkable performance in various applications, yet their training demands extensive resources and time. Consequently, fine-tuning pre-trained LLMs has become a prevalent strategy for adapting these models to diverse downstream tasks, thereby reducing costs. Despite their benefits, LLMs have vulnerabilities, such as susceptibility to adversarial attacks, potential for jailbreaking, fairness issues, backdoor vulnerabilities, and the risk of generating inappropriate or harmful content. Since fine-tuned models inherit some characteristics from their original models, they may also inherit these issues and vulnerabilities. In this work, we propose a lightweight framework, RootTracker, specifically designed to trace the original models of fine-tuned LLMs. The core idea is to identify a set of prompts that can assess which pre-trained LLM a fine-tuned model most closely resembles. This process is conducted in a ''knockout tournament" style, where the model is repeatedly tested against pairs of LLMs until the original pre-trained model is identified. To evaluate the effectiveness of our framework, we created 200 distinct fine-tuned models, derived from original models including GPT-Neo, GPT-2, TinyLlama, and Pythia. The results demonstrate that our framework accurately identified the original models for 85.7\% of the fine-tuned versions. Therefore, we advocate for timely updates to model versions or deliberate obfuscation of model types when deploying large models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
RootTracker is a framework designed to trace the original models of fine-tuned Large Language Models (LLMs) under black-box conditions. It employs a "knockout tournament" style of comparison to identify the original pre-trained model of a fine-tuned LLM. While the experimental results show a certain level of accuracy, the framework's performance is limited by the predefined pool of candidate models and the high computational cost due to multiple rounds of comparison.

### Strengths
Innovative Comparison Method: The "knockout tournament" approach to model comparison is relatively novel in the field of LLM tracing.

### Weaknesses
Limitation of Candidate Model Pool: If the base model of a fine-tuned model is not in the candidate pool, RootTracker may not accurately identify it, potentially leading to misleading results.

Computational Overhead: The mechanism of multiple comparison rounds leads to significant computational costs, especially when there is a large number of candidate models.

Diversity of data sets and scenarios: Insufficient discussion of the diversity of data sets and test scenarios used in the paper may affect the universality of the results.

Comparison Efficiency: Multiple comparison rounds may lead to inefficiency, especially when dealing with a large number of candidate models.

Reliability of Results: If the candidate model pool is not comprehensive, the results from RootTracker may be unreliable, limiting its practical application.

### Questions
Comprehensiveness of the Candidate Model Pool: How do the authors ensure the comprehensiveness of the candidate model pool, and how do they handle models not in the pool?
Optimization of Computational Efficiency: Have the authors considered optimizing the algorithm to reduce the number of comparison rounds, thereby lowering computational costs?
Improvement of Comparison Method: Is it possible to reduce the necessary number of comparison rounds through other methods, such as machine learning or statistical analysis?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces "RootTracker," a framework aimed at tracing the original models of fine-tuned LLMs under black-box conditions. This approach is lightweight and claims efficiency in identifying the base model from a set of prompts using a "knockout tournament" structure. The framework is modular, involving model preparation, database construction, classification, and iterative knockout rounds, enabling the identification of pre-trained model origins without model access. Experimental results report an 85.7% accuracy in identifying the origin models of fine-tuned variants.

### Strengths
1.The modular design allows for scalability and future extensions.

2.RootTracker offers a lightweight solution for tracking model origins, potentially requiring fewer computational resources than parameter-tuning methods.

3.The use of a knockout tournament mechanism, inspired by elimination sports, is creative and aims to streamline the comparison process between multiple models.

4.Initial experiments show a high accuracy rate, suggesting the framework’s viability in identifying the base models of fine-tuned variants.

### Weaknesses
1.Limited Baseline Comparisons: The framework is compared only to a single prior study, limiting the understanding of its performance relative to other potential attribution methods.

2.Scalability Constraints: The paper reports using models of limited size (up to 1.4B parameters), which might limit RootTracker’s effectiveness when handling models with larger parameter counts, especially in real-world scenarios involving newer, more complex LLMs. The experiments do not explore the impact of increasing model size on the performance of RootTracker, which is a critical factor for real-world applicability.

3.Reliance on Predefined Model Pool: The framework's reliance on a predefined set of original models restricts its generalization. If the model under test is not derived from one of these, RootTracker may fail, limiting its practical applications. The method does not account for the possibility of models being derived from a combination of base models or from models outside the predefined pool, which is a significant limitation.

4.Computational Demands: Although described as lightweight, the knockout rounds and prompt optimizations still involve iterative comparisons that could become costly with larger model datasets. The paper does not provide a detailed analysis of the computational complexity of the knockout tournament, nor does it provide empirical data on the time and resources required for different numbers of candidate models.

### Questions
1.How does RootTracker handle cases where the fine-tuned model diverges significantly from any of the original models in the pool?

2.Given the scalability limitations mentioned, does RootTracker plan to accommodate larger models in future iterations?

### Soundness
2

### Presentation
2

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
This paper presents a scheme for tracing the original models of fine-tuned LLMs. For a given original model, the scheme trains a binary classifier in a sentence embedding space to identify the ground-truth pair of the original and fine-tuned models, among other pairs. The classification and identification are conducted over a set of top-$k$ high-quality prompts and outputs.

### Strengths
1. This paper is easy to follow.
2. The experiments include 200 distinct fine-tuned models.

### Weaknesses
1. The approach does not address the issues in the motivation. The authors highlighted that fine-tuned models inherit some characteristics from their original models, such as susceptibility to adversarial attacks, potential for jailbreaking, fairness issues, backdoor vulnerabilities, and the risk of generating inappropriate or harmful content. However, telling the original model of a fine-tuned model does not mitigate these harmful characteristics.

2. I do not see an application of the proposed scheme. Watermark approaches can be used if a foundation model team wants to identify fine-tuned LLMs based on their model. If a fine-tuning team or an end user wants to select a good model, directly running evaluation benchmarks can help them identify the optimal model.

3. The prompt selection part is unclear. The authors instruct the original models to generate multiple (50-1000) prompts and select the top $ k$ of them for subsequent sentence classification and model identification. Here, I neither know what the $k$ is (e.g., 10) nor the limitation of publicly available prompts (e.g., Anthropic-HH).



### Questions
1. Could the authors provide specific examples of how knowing the original model could help mitigate or analyze vulnerabilities like jailbreaking or fairness issues in fine-tuned models?
2. Could the authors provide a comparison or discussion highlighting the proposed approach's advantages over watermarking and direct evaluation methods in specific scenarios?
3. Could the authors provide the exact value or range of $k$ used in the experiments? Additionally, are there limitations on using publicly available prompts?
4. Suppose the original model is not included in the pairs of models (i.e., not GPT-Neo, GPT-2, TinyLlama, or Pythia as is listed in the experiments), does the scheme produce a false-positive result?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposed RootTracker, a framework designed to identify the original pre-trained model of a fine-tuned LLM through a black-box approach. RootTracker employs a series of prompts and a "knockout tournament" classification mechanism to track the source model of fine-tuned LLMs with an accuracy of 85.7% across several common models.

### Strengths
- The studied problem - model tracing - is important for the domain.
- The structure is easy to follow.

### Weaknesses
1. Scalability Issues: Current experiments are only conducted with 1.4B parameter models, how would RootTracker adapt or scale to larger models such as 10B or 70B parameters? Would prompt-based classification require modification to retain efficiency? The paper does not address the potential increase in the complexity of the prompt space as model size increases. It's unclear if the current prompt design would remain effective, or if a more sophisticated approach to prompt generation and selection would be needed to maintain performance with larger models. Furthermore, the computational cost associated with evaluating these larger models is not discussed, which is a critical factor for the practical application of the method.
2. Practical Considerations: Current popular LLMs are all proprietary, where prompt tuning is impossible. Then, will RootTrace be applied to the proprietary setting? The paper does not specify how the method would be applied in scenarios where access to the model's internals or the ability to perform prompt tuning is restricted. This is a significant limitation, as many state-of-the-art models are only available through APIs, which limits the applicability of the proposed approach.
3. Efficiency Issues: while the paper emphasize the efficiency of the method, could you provide any experimental results on the efficiency? The paper lacks concrete data on the computational resources required for the proposed method, such as the time taken for each round of comparison and the memory footprint of the stored inputs and outputs. Without these results, it's difficult to assess the practical efficiency of the method, especially when dealing with a large number of candidate models.
4. Missing Baseline: The paper misses baselines. Could you provide any experiments comparing your method with the baselines? The paper does not compare the proposed method with any existing model tracing techniques. Without a baseline comparison, it is difficult to evaluate the effectiveness and novelty of the proposed approach. It is essential to compare the performance of RootTracker with other methods to demonstrate its advantages.
5. I strongly recommend the authors to further revise the writing of the paper. My suggestions include (1) adding problem setup to clearly describe the problem addressed in the paper and (2) revising the vague sentences in Section 2, e.g., " For instance, if the test model is based on GPT and the classifier is designed to differentiate between GPT and Llama, the classifier’s output would lean toward GPT."

### Questions
See Weakness part.

### Soundness
2

### Presentation
2

### Contribution
2
