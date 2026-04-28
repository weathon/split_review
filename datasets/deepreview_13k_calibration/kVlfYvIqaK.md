# Node-Time Conditional Prompt Learning in Dynamic Graphs

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Dynamic graphs capture evolving interactions between entities, such as in social networks, online learning platforms, and crowdsourcing projects. For dynamic graph modeling, dynamic graph neural networks (DGNNs) have emerged as a mainstream technique. However, they are generally pre-trained on the link prediction task, leaving a significant gap from the objectives of downstream tasks such as node classification. To bridge the gap, prompt-based learning has gained traction on graphs, but most existing efforts focus on static graphs, neglecting the evolution of dynamic graphs. In this paper, we propose DyGPrompt, a novel pre-training and prompt learning framework for dynamic graph modeling. First, we design dual prompts to address the gap in both task objectives and temporal variations across pre-training and downstream tasks. Second, we recognize that node and time patterns often characterize each other, and propose dual condition-nets to model the evolving node-time patterns in downstream tasks. Finally, we thoroughly evaluate and analyze DyGPrompt through extensive experiments on four public datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the problem of adapting pre-trained dynamic GNNs. The authors propose DYGPROMPT, a dual prompt mechanism with node and time prompts, supported by dual condition-nets, to bridge the gaps between pre-training and downstream objectives as well as temporal inconsistencies, achieving improved adaptability and performance across dynamic graph tasks.

### Strengths
S1. I like the idea of using dual prompt mechanism to bridge task and temporal gaps.

S2. Experiments show DYGPROMPT is effective on small real-world graphs.

### Weaknesses
W1. The introduction of dual prompts and dual condition networks enhances adaptability but significantly increases model complexity. I would suggest the authors to add some analysis or experiments to demonstrate DYGPROMPT’s performance in terms of computational efficiency.

W2. I have concerns about the experimental setup. Using the first 80% of interactions for pre-training is uncommon in pre-trained frameworks. For example, TIGPROMPT uses only 20% of the data, yielding surprisingly strong results in comparison.

W3. The discussion of current dynamic graph prompt learning methods, such as TIGPROMPT, is brief and lacks an in-depth analysis of their limitations or how DYGPROMPT specifically addresses these issues. Additionally, Section 4 contains extensive information on previous works, making it difficult to discern the paper’s core contributions.

### Questions
Q1. In previous work, prompts are often implemented as vector concatenations. What are the author’s considerations for using dot-product instead?

Q2. Personally, I am curious whether a pre-trained time encoder can address questions such as “What is the time of the next interaction?”

Q3. How does DYGPROMPT perform on large-scale dynamic graphs?

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
The paper introduces DYGPROMPT, a novel pretraining and prompt learning framework designed for dynamic graph learning. It addresses the challenges of bridging the gap between pre-training objectives and downstream tasks. The authors propose dual prompts -- node prompts and time prompts -- to address the discrepancies in both task objectives and temporal variations between pre-training and downstream tasks. The authors introduce dual condition-nets to model the evolving node-time patterns in downstream tasks. This includes a time condition-net that generates time-conditioned node prompts and a node condition-net that generates node-conditioned time prompts. Experiments on four public datasets demonstrate its superior performance compared to state-of-the-art approaches in tasks such as temporal node classification and temporal link prediction.

### Strengths
- **Relevance to Real-World Applications:** The framework's focus on dynamic graphs makes it highly relevant to real-world applications such as social networks, online learning platforms, and crowdsourcing projects.

- **Parameter Efficiency:** DYGPROMPT's ability to perform well with minimal parameter updates is a significant strength, especially for applications where labeled data is scarce.

- **Open source:** It is commendable that the authors have made their code publicly available, enhancing the transparency and reproducibility of their work.

### Weaknesses
 - **Motivation:** The motivation for this work is insufficiently justified. After reading the paper, it remains unclear why temporal patterns would be influenced by node features. Time, as a continuous scale, is inherently objective and independent of specific events.

- **Novelty:** Based on the above, the novelty of this work appears limited. TIGPrompt has already proposed an effective strategy for dynamic graph learning by fusing prompts through the concatenation of node and time embeddings for prompt-based fine-tuning. This contrasts with the authors’ claim that TIGPrompt only considers temporal factors within node features. Thus, the main difference between this work and TIGPrompt seems to lie in the adoption of a more complex information fusion strategy rather than a simple concatenation.

- **Experiments:** The experimental setup and results raise some concerns. First, the reported results are noticeably lower than those of TIGPrompt. Given the relevance of TIGPrompt as a baseline, I recommend that the authors adopt identical experimental settings to ensure comparability. Additionally, the influence of model size on performance is unclear; I suggest that the authors report the number of parameters for both their model and TIGPrompt.

- **Writing:** The writing could be further polished to improve clarity and readability.

### Questions
See above.

### Soundness
2

### Presentation
2

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
To address the challenges of prompt-based learning on dynamic graphs, this paper develops a novel pretraining and prompt learning framework for dynamic graph modeling. The authors propose dual prompts and dual condition networks to model the evolving node-time patterns. Extensive experiments are conducted to evaluate the performance of the proposed node-time solution. Overall, the approach is sound and reasonable.

### Strengths
1.	This paper identifies the issue of pretrained Graph Neural Networks (GNNs)—specifically, the gap between pre-training and task objectives—and proposes novel prompt learning approaches for dynamic graphs. It also considers the evolving interplay patterns between nodes and time points.
2.	The framework addresses temporal variations across time and divergent task objectives by leveraging a node prompt and a time prompt to reduce the gap between the pre-training and downstream phases. The main novelty lies in the introduction of the time prompt, which narrows the inconsistencies that arise from varying priorities at different times. The proposed method is reasonable.
3.	Extensive experiments are conducted to evaluate the performance of various methods. The source codes are available anonymously, which adds to the credibility of the results.
4.	The manuscript is well written and easy to follow.

### Weaknesses
1.	The concept of temporal prompts for dynamic graphs has been previously investigated (e.g., TIGPrompt), but the differences between approaches are not clearly articulated. In the related work, it is stated that “it only considers the temporal factor in node features, overlooking that temporal patterns are also influences by node features.” More explanations are needed to highlight the technical novelty of this paper.
2.	The overall framework presented in Figure 2 could be improved; it is not clear how to compute the downstream loss (Eq. 11) and why it only links to the time branch.
3.	All evaluated datasets are relatively small, and the paper lacks an efficiency or complexity analysis for larger-scale datasets, which is important for practical applications.
4.	There are minor typos and errors, such as “are also influences by node.”

### Questions
The study considers only two tasks on dynamic graphs. Is it possible to apply this framework to other graph tasks?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces DYGPROMPT, a novel framework for dynamic graph modeling that aims to bridge the gap between pre-training and downstream tasks, such as node classification and link prediction, on dynamic graphs. The authors propose a two-stage approach involving pre-training and prompt learning. In the pre-training phase, a dynamic graph neural network is trained on the task of temporal link prediction. For the downstream tasks, the authors design dual prompts (node and time prompts) to address the differences in objectives and temporal variations between the pre-training and downstream phases. Additionally, they introduce dual condition nets to generate a series of time-conditioned node prompts and node-conditioned time prompts, capturing the evolving node-time patterns. The framework is evaluated on four public datasets, demonstrating superior performance compared to state-of-the-art methods.

### Strengths
S1. The paper presents a creative solution to the challenge of adapting pre-trained DGNNs to downstream tasks, which is a novel contribution to dynamic graph learning.

S2. The paper is well-written and easy to follow.

S3. Extensive experiments compared with DGNNs, SOTA pre-training models, and graph prompt learning models demonstrate the effectiveness of the proposed model.

### Weaknesses
W1.  While the paper mentions the computational complexity, a deeper analysis comparing the complexity of DYGPROMPT with other methods, especially in terms of training and inference time, is necessary for a prompt-based model.

W2. The used datasets are very small-scale. The largest dataset used only contains about 10K nodes. This makes it difficult to confirm whether the model can be successfully applied to large-scale data and the real world.

W3. The experimental datasets have extreme class numbers. Specifically, 3 of the datasets are binary classification and another one contains 474 classes. It would be better to experiment on other more datasets. Furthermore, the DGraph dataset is also a binary classification dataset on graph anomaly detection tasks (like 0: anomaly, 1: normal).

### Questions
Q1: Can the authors comment on the scalability of DYGPROMPT to large-scale dynamic graphs, both in terms of computational resources and performance?

Q2: How does DYGPROMPT adapt to long-term temporal changes in dynamic graphs, especially when the graph's structure and node behaviors evolve significantly over time?

### Soundness
3

### Presentation
3

### Contribution
3
