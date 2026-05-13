# Can Textual Gradient Work in Federated Learning?

- Decision: Accept
- Scores: 6, 6, 5, 6

## Abstract
Recent studies highlight the promise of LLM-based prompt optimization, especially with TextGrad, which automates ``differentiation'' via texts and backpropagates textual feedback provided by LLMs. This approach facilitates training in various real-world applications that do not support numerical gradient propagation or loss calculation.  It opens new avenues for optimization in decentralized, resource-constrained environments, suggesting that users of black-box LLMs (e.g., ChatGPT) could enhance components of LLM agentic systems (such as prompt optimization) through collaborative paradigms like federated learning (FL). In this paper, we systematically explore the potential and challenges of incorporating textual gradient into FL. Our contributions are fourfold.
**Firstly**, we introduce a novel FL paradigm, Federated Textual Gradient (FedTextGrad), that allows FL clients to upload their locally optimized prompts derived from textual gradients, while the FL server aggregates the received prompts through text summarization. Unlike traditional FL frameworks, which are designed for numerical aggregation, FedTextGrad is specifically tailored for handling textual data, expanding the applicability of FL to a broader range of problems that lack well-defined numerical loss functions. 
**Secondly**, building on this design, we conduct extensive experiments to explore the feasibility of federated textual gradients. Our findings highlight the importance of properly tuning key factors (e.g., local steps) in FL training to effectively integrate textual gradients. 
**Thirdly**, we highlight a major challenge in federated textual gradient aggregation: retaining essential information from distributed prompt updates. Concatenation often produces prompts that exceed the LLM API’s context window, while summarization can degrade performance by generating overly condensed or complex text that lacks key context. 
**Last but not least**, in response to this issue, we improve the vanilla variant of FedTextGrad by providing actionable guidance to the LLM when summarizing client prompts by leveraging the Uniform Information Density principle. Such a design reduces the complexity of the aggregated global prompt, thereby better incentivizing the LLM's reasoning ability. Through this principled study, we enable the adoption of textual gradients in FL for optimizing LLMs, identify important issues, and pinpoint future directions, thereby opening up a new research area that warrants further investigation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces FedTextGrad, a novel paradigm designed to extend the capabilities of federated learning (FL) by incorporating textual gradients rather than traditional numerical ones. Building on TextGrad, an approach for LLM-based prompt optimization through text-based feedback, this work explores how such textual gradients can function within FL frameworks. The motivation behind this approach is to enable FL applications where numerical loss functions or gradients are impractical or unavailable, such as when working with black-box LLM APIs. FedTextGrad allows clients to upload optimized prompts—derived from textual feedback during local training—to a central server, which then aggregates these prompts and redistributes a global prompt to clients. This method adapts FL for decentralized and privacy-sensitive environments, expanding potential applications.

The paper identifies unique challenges in aggregating textual gradients across clients, particularly in retaining essential context within the aggregated prompts. Traditional methods like concatenation often lead to prompts that exceed LLM token limits, while summarization can compromise performance by overly compressing information. To address this, the authors propose an enhancement based on the Uniform Information Density (UID) principle, which balances information distribution within aggregated prompts to maintain a coherent context without excessive length. This UID-informed summarization improved global prompt quality.

Experiments are conducted to evaluate FedTextGrad across various reasoning tasks, including object counting and arithmetic problems, using different LLM architectures such as LLaMA and GPT-4. The results demonstrate that key FL hyperparameters, like local steps, batch size, and the number of clients, greatly impact FedTextGrad’s performance. Increasing local steps can enhance local adaptation but risks misalignment with the global prompt, while adding clients initially improves performance by introducing data diversity but eventually leads to synchronization challenges. These findings underscore the importance of carefully tuning FL parameters to balance local and global model alignment in a textual gradient setting.

While the study offers promising insights into applying textual gradients in FL, it acknowledges several limitations, particularly in terms of privacy and security. Textual gradients inherently carry more contextual information than numerical gradients, posing privacy risks when shared among clients and servers. Though the paper suggests differential privacy and encryption as potential solutions, it lacks an experimental exploration of these methods, leaving privacy protection as a critical area for future research.

### Strengths
1) The introduction of FedTextGrad as a framework to incorporate textual gradients into FL represents a novel approach, particularly valuable in settings where numerical gradients are unavailable, such as black-box LLM applications. 
2) The paper addresses a core challenge in aggregating textual data—preserving essential context without exceeding token limits—by proposing a UID-based summarization approach. This innovative method helps maintain critical information balance across prompts, solving a major limitation in using textual gradients and improving FedTextGrad's scalability and robustness in handling prompt length constraints in federated settings.
3) The paper thoroughly investigates key FL hyperparameters, including local steps, batch size, and the number of clients, assessing their impact on performance. This systematic analysis provides practical insights into optimizing FedTextGrad for different settings, demonstrating the framework's adaptability and offering a foundation for further research and application in federated environments with textual gradients.

### Weaknesses
1) The paper identifies privacy risks with textual gradients but does not provide or test concrete methods to protect sensitive information, which is crucial for FL applications in privacy-sensitive domains.
2) The experiments are primarily conducted on a few large LLMs, restricting insights into how FedTextGrad performs across diverse architectures, particularly smaller models in resource-constrained settings.
3) The UID-based summarization method helps with prompt aggregation but has limitations in fully retaining information, especially with high client heterogeneity and complexity, potentially affecting scalability. The effectiveness of UID summarization under varying levels of client heterogeneity and task complexity is not thoroughly explored.

### Questions
1) Has dynamic switching between aggregation methods, based on task complexity, been considered?
2) How effectively does UID summarization capture essential information across tasks?

### Soundness
2

### Presentation
2

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
The authors present a novel approach to analyze the potential and pitfalls of integrating methods like TextGrad (Yuksekgonul et al., 2024) into a federated learning context. In this setup, each client initiates a prompt and refines it locally using its data and local LLM. The optimized local prompts are then uploaded to a server, which aggregates the prompts and redistributes them back to the clients. The main aggregation strategies considered are concatenation and summarization, with an additional focus on optimizing aggregation by prioritizing words with the highest information content.

The authors offer several insights:
- Accuracy vs. number of local steps performed before sending the final prompt to the server
- Accuracy vs. number of clients
- Accuracy vs. batch size
- Impact of using different LLMs, e.g., GPT-4 vs. LLaMA
- Cost implications of concatenation in terms of $
- Insights on summarization vs. concatenation

One potential area for improvement, although I understand is challenging due to the novelty of the topic, is a comparison with previous federated learning or prompt optimization solutions. For example:
- A comparison with traditional Federated Learning based on numerical gradients, such as Communication-Efficient Learning of Deep Networks from Decentralized Data (2023) or FedBiOT: LLM Local Fine-Tuning in Federated Learning without Full Model (2023). If these comparisons are not feasible, it would be helpful to clarify why.
- A direct comparison with the centralized version (TextGrad).

### Strengths
- Presentation of a novel framework for handling prompt-based learning in a federated learning context.
- Numerous insights on learning in a federated learning setting without numerical gradients.

### Weaknesses
 - lack of comparisons w.r.t. previous works on federated learning

### Questions
Although the topic is new, authors should try to do the following things if possible: 
- A comparison with traditional Federated Learning based on numerical gradients, such as Communication-Efficient Learning of Deep Networks from Decentralized Data (2023) or FedBiOT: LLM Local Fine-Tuning in Federated Learning without Full Model (2023). If these comparisons are not feasible, it would be helpful to clarify why.
- A direct comparison with the centralized version (TextGrad).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper investigates the integration of textual gradients into federated learning environments, focusing on improving the optimization of large language models with privacy preservation. The authors propose a novel approach, Federated Textual Gradient (FedTextGrad), which adapts the concept of textual gradients for federated settings.

### Strengths
This paper proposes a concept called FedTextGrad for optimizing large language models by integrating text gradients. This method utilizes text feedback for model optimization in a federated environment, extending the application of federated learning to areas where numerical gradients are impractical or infeasible. This paper identifies and addresses key challenges in joint text gradient aggregation, such as maintaining basic information in distributed updates and managing prompt sizes to accommodate LLM API constraints.

### Weaknesses
Although the experiments in the paper are comprehensive, they mainly focus on inference tasks, which may not fully demonstrate the broad applicability of FedTextGrad in various fields.
The discussion on the limitations of the FedTextGrad method is somewhat insufficient. Although this article briefly discusses challenges such as prompt length management and information retention, it does not delve into potential limitations or scalability issues that may arise when deployed in larger, more heterogeneous environments.
Some parts of the manuscript are dense and highly technical, which may make it difficult for readers to understand. Using complex descriptions may obscure key points and findings.

### Questions
1. The quality of text gradients generated across different clients may fluctuate. How can we ensure the consistency and effectiveness of these text gradients, especially in cases of uneven data distribution or varying data quality?
2. The paper tests the proposed method primarily on reasoning tasks. Can you discuss or provide insights on how FedTextGrad might perform across different domains, where data might be more sensitive or heterogeneous?
3. Consider providing more detailed descriptions for the implementation of FedTextGrad, especially how textual gradients are computed and aggregated.
4. Elaborate on the practical implications of FedTextGrad. How can this method be integrated into existing federated learning frameworks? What are the practical challenges of deploying FedTextGrad in operational environments, and how can they be overcome?

### Soundness
2

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
3

### Summary
The paper presents FedTextGrad, a novel federated learning approach that incorporates textual gradients, allowing for the optimization of Large Language Models in decentralized environments. It introduces a new aggregation method based on the Uniform Information Density principle to address the challenge of retaining essential information from distributed prompt updates, thereby enhancing the applicability of federated learning to text-based optimization.

### Strengths
(1) Originality: The originality of the paper lies in its pioneering effort to adapt TextGrad, a method for automatic differentiation via text, into the federated learning (FL) framework. By proposing FedTextGrad, the authors have expanded the scope of FL to leverage the capabilities of LLMs in a decentralized manner, without the need for explicit numerical loss functions.
(2) Quality: The paper provides a thorough analysis of the proposed method's feasibility and identifies key challenges associated with textual gradient aggregation in a federated setting.
(3) Clarity: The paper is clear and well-structured. 
(4) Significance: The significance of the paper lies in its integration of textual gradients into the federated learning framework.

### Weaknesses
 (1) two typographical errors was identified on lines 191 and 216 of the paper;
(2) The description of "Client" in the paper is unclear: Figure 2(b) shows "Client Num" exceeding three, but on line 312, the number of clients is stated to correspond to the number of datasets used in the paper, yet the paper only mentions three datasets;
(3) This paper introduces TextGrad into the federated learning framework, but experiments are only conducted on reasoning tasks, which is not sufficient in terms of experimental scenarios.

### Questions
(1) The paper, while thorough in its experimental section, could be further strengthened by incorporating a wider array of datasets and tasks, including but not limited to coding, problem-solving, medicine and chemistry, to enhance the generalizability of its findings.
(2) The paper could benefit from a more direct comparison with existing federated learning methods, especially those tailored for LLMs.
(3) Why was the Llama-3.1-8B model exclusively utilized for prompt optimization and ablation studies, and not a variety of models?

### Soundness
2

### Presentation
3

### Contribution
2
