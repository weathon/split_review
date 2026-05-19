### Summary

This paper proposes an object-centric world model for model-based reinforcement learning. The model leverages a pre-trained object segmentation model to extract object features and combine with visual features for dynamics prediction. The model is trained by a VAE-like objective and is used to train a policy by model-free RL. The method is tested on Atari 100k and a new game Hollow Knight. The results show that the method outperforms the baseline in 18/26 Atari games and improves the performance on 5/6 bosses in Hollow Knight.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The proposed method is intuitive and easy to understand.
2. The experiments show that the method can outperform the baseline in many tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is not well-motivated. It is unclear why the method can outperform the baseline. The authors claim that the method can focus on decision-relevant details, but this claim is not well-supported. The paper lacks a clear explanation of how the object-centric approach leads to improved performance compared to the baseline. Specifically, it is not clear how the object features are extracted, how they are combined with visual features, and why this combination is superior to the baseline's approach. The paper needs to provide a more detailed analysis of the feature representations and their impact on the final policy.
2. The experiments are not convincing. The method is only compared with one baseline. The paper should include comparisons with other state-of-the-art model-based reinforcement learning methods to demonstrate the effectiveness of the proposed approach. The current evaluation is limited and does not provide a comprehensive assessment of the method's capabilities. The lack of comparison with other methods makes it difficult to assess the true contribution of the proposed approach.
3. The paper is not well-written. The paper is not well-organized and some of the technical details are not clearly explained. The paper needs to be reorganized to improve the clarity and readability. The current presentation makes it difficult to understand the proposed method and its contributions. The lack of clear explanations of technical details makes it hard to reproduce the results and assess the validity of the approach.

### Suggestions

The paper needs to provide a more detailed explanation of the object-centric approach and its benefits. The authors should clearly articulate how the object features are extracted, how they are combined with visual features, and why this combination is superior to the baseline's approach. A more thorough analysis of the feature representations and their impact on the final policy is needed. For example, the authors could visualize the learned object features and demonstrate how they capture decision-relevant details. They could also provide a quantitative analysis of the feature representations to show that the object-centric approach leads to better feature learning. Furthermore, the authors should provide a more detailed explanation of the training process and the hyperparameters used. This would help to ensure the reproducibility of the results and allow other researchers to build upon their work.

The experimental evaluation needs to be significantly improved. The authors should compare their method with other state-of-the-art model-based reinforcement learning methods, such as DreamerV3 and other relevant baselines. This would provide a more comprehensive assessment of the method's capabilities and allow for a more meaningful comparison with existing approaches. The authors should also consider evaluating their method on a wider range of tasks, including more complex environments. This would help to demonstrate the generalizability of the method and its applicability to real-world problems. The current evaluation is limited and does not provide a comprehensive assessment of the method's capabilities. The authors should also provide a more detailed analysis of the results, including error analysis and ablation studies. This would help to identify the strengths and weaknesses of the method and provide insights into its behavior.

The paper needs to be reorganized to improve the clarity and readability. The authors should provide a clear and concise explanation of the proposed method, including the technical details. The paper should be well-organized, with a logical flow of ideas. The authors should also provide clear definitions of all the terms and concepts used in the paper. The paper should be written in a clear and concise style, avoiding jargon and technical language. The authors should also provide more visual aids, such as diagrams and figures, to help the reader understand the proposed method. The current presentation makes it difficult to understand the proposed method and its contributions. The lack of clear explanations of technical details makes it hard to reproduce the results and assess the validity of the approach.

### Questions

1. How does the method perform on other tasks, such as Procgen?
2. How does the method perform compared to other model-based RL methods?

### Rating

3

### Confidence

3

**********
