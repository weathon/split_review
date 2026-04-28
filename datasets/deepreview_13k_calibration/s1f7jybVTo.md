# A Visual Case Study of the Training Dynamics in Neural Networks

- Decision: Reject
- Avg Score: 4.00
- Scores: 6, 3, 3

## Abstract
This paper introduces a visual sandbox designed to explore the training dynamics of a small-scale transformer model, with the embedding dimension constrained to $d=2$.
This restriction allows for a comprehensive two-dimensional visualization of each layer's dynamics. 
Through this approach, we gain insights into training dynamics, circuit transferability, and the causes of loss spikes, including those induced by the high curvature of normalization layers. 
We propose strategies to mitigate these spikes, demonstrating how good visualization facilitates the design of innovative ideas of practical interest.
Additionally, we believe our sandbox could assist theoreticians in assessing essential training dynamics mechanisms and integrating them into future theories.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel visual sandbox designed to explore the training dynamics of a small-scale transformer model with a restricted embedding dimension of $d=2$. This setup allows for two-dimensional visualization, providing a detailed look into the model’s internal mechanisms. The sandbox helps uncover hierarchical learning processes, circuit transferability, and causes of loss spikes, particularly those due to high curvature in normalization layers. The authors propose methods to mitigate these spikes, highlighting how visualization can lead to more effective training strategies. They suggest that this tool could assist in developing theories and improving training processes for more complex neural networks.

### Strengths
- The paper introduces a novel tool for visualizing the training dynamics of transformers. The visualization offers both practical and theoretical insights, making complex mechanisms more accessible.

- The authors identify a hierarchical learning process inside a pretrained transformer via their visualization tool, showing how low-level features are established before higher-level refinement. This is valuable for understanding model behavior and training stages.

- The tool also helps to recognize loss spikes caused by high curvature in the model's normalization layers. Based on this, the authors suggest practical mitigation strategies, potentially making training more stable and efficient.

### Weaknesses
 - My first concern is that, while the visualization tool is insightful, its restriction to small-scale transformers with $d=2$ limits its applicability to larger and more complex models commonly used in practice. It remains unclear whether insights from this sandbox will generalize to high-dimensional transformers. Further discussions on the higher dimensional embedding should be provided.

- There is no comparison between a pretrained model and a fine-tuned model based on insights derived from the sandbox. Consequently, it remains unclear whether the recommendations informed by the sandbox visualizations effectively contribute to improved model performance on practical tasks.

### Questions
- Could the authors discuss the scalability of their sandbox tool to higher-dimensional transformer models, for example, when $d=3$? How does the computational complexity of this sandbox grow in terms of $d$?

- Are there quantitative metrics for evaluating the effectiveness of the proposed loss spike mitigation strategies?

- What types of theoretical developments/problems in training dynamics can be recognized or conjectured from the visualization results of this sandbox?

### Soundness
3

### Presentation
3

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
In this work, the authors presented a case report that using 2D visualization to demonstrate the training dynamics of a neural network trained to solve the sparse modular addition problem. Various aspects of the training dynamics, including the two stages of learning, the influence of initialization, process of network adaptation in sequential learning, trajectory of the loss function including its anomaly (the spikes) are visualized and analyzed qualitatively.

### Strengths
By choosing a well-structured task and proper visualization, the authors have demonstrated a number of interesting and potentially important phenomena regarding network training dynamics. The framework presented may be extended to study other networks and tasks, leading to better understanding of networks’ learning process.

### Weaknesses
It is unclear what part of the current work can generalize. Is it the methodology of 2D embedding and visualization? If so, what is the difficulty of doing it and what is the innovative way to overcome them in the present work? And how the proposed method can generalize to other tasks and networks? These needs to be explained and clarified in a clearer way. Or, is the conclusion of the training dynamics generalizable? But here it seems unlikely, because the current observations were based on a particular network structure trained with a specific task. Even for the current network and task, the authors need to show how robust of the observations, e.g., the two stages of training, with one for embedding and one for classification. Without either the method or the conclusions generalizable to more situations, the impact of the work might be limited.

### Questions
I suggest the authors re-organize the paper to better explain and clarify what is the problem solved by this case report, and how it can help readers working in training networks in general.

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
This paper examines the training dynamics of neural networks by conducting a detailed study on a small-scale transformer model, employing a novel visual sandbox. This tool facilitates the observation and analysis of the model's internal mechanisms, offering insights into more efficient training strategies.

### Strengths
- The experimental motivation and setup are clearly articulated.

### Weaknesses
 - The presentation of the experimental results is suboptimal. In Figure 4, many values overlap, resulting in readability issues.
- There is a lack of theoretical support for the proposed method. The paper claims, "This tool allows us to observe and analyze the model’s internal mechanisms vividly, providing both theoretical and practical insights that could lead to more efficient training strategies." However, the theoretical insights remain unclear.
- The experiments are limited. The paper lacks experiments across varied datasets, tasks, and neural network architectures.

### Questions
- Could you present the experimental results more clearly?
- Could you provide theoretical support for the proposed method?
- Could you conduct additional experiments across various datasets, tasks, and neural network architectures?

### Soundness
2

### Presentation
1

### Contribution
2
