### Summary

This paper introduces SPaR, a self-play framework that enhances the instruction-following capabilities of large language models (LLMs) through tree-search self-refinement. The authors argue that existing methods for creating preference pairs often introduce irrelevant variations, which can interfere with the model's ability to learn how to follow instructions accurately. SPaR addresses this issue by using a tree-search strategy to refine previous responses, minimizing unnecessary variations and creating valid comparison counterparts for model training. The authors demonstrate that a LLaMA3-8B model trained with SPaR surpasses GPT-4-Turbo on the IFEval benchmark without losing general capabilities and shows promising scalability with larger models like LLaMA3-70B.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel self-play framework, SPaR, that combines tree-search refinement with preference learning to improve instruction-following in LLMs. This approach is innovative in its use of self-play and tree-search to create more focused and relevant preference pairs for training.
2. The experimental results are compelling, showing that SPaR-trained models outperform existing methods, including surpassing GPT-4-Turbo on the IFEval benchmark. The scalability of SPaR to larger models like LLaMA3-70B further demonstrates its potential.
3. The paper is well-structured and clearly explains the methodology, experiments, and results. The authors provide a thorough analysis of the approach and its effectiveness in enhancing instruction-following capabilities.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational resources required for training with SPaR, which could be a concern for practical applications. Specifically, the paper lacks information on the number of GPUs, training time, and memory usage for each iteration, making it difficult to assess the feasibility of the approach for researchers with limited resources. Furthermore, the paper does not discuss the energy consumption of the training process, which is an increasingly important consideration for large-scale experiments.
2. The paper's comparison with existing methods could be more comprehensive. While it compares SPaR with several baselines, a more detailed comparison with other state-of-the-art methods in preference learning and self-improvement could strengthen the paper's claims. For instance, a comparison with methods that use reinforcement learning from human feedback (RLHF) or other forms of self-improvement would provide a more complete picture of SPaR's relative performance. The current comparison is limited to a few baselines, and it is unclear how SPaR performs against a broader range of techniques.
3. The paper could benefit from a more in-depth discussion of the limitations of the SPaR framework. For example, the paper does not address the potential for the model to overfit to the IFEval benchmark or the generalization capabilities of the model to unseen instructions. Additionally, the paper does not discuss the potential for the tree-search algorithm to get stuck in local optima, which could limit the effectiveness of the refinement process. A more thorough discussion of these limitations would provide a more balanced view of the approach.

### Suggestions

To address the lack of detail regarding computational resources, the authors should include a comprehensive breakdown of the hardware used, including the specific GPU models, number of GPUs, training time per iteration, and memory usage. They should also provide an estimate of the energy consumption of the training process. This information is crucial for researchers to assess the feasibility of using SPaR in their own work. Furthermore, the authors should discuss the scalability of the approach in terms of computational resources, and whether the approach is suitable for researchers with limited resources. This could include exploring techniques to reduce the computational cost of the tree-search algorithm, such as using more efficient search strategies or reducing the number of refinement steps.

To strengthen the comparison with existing methods, the authors should include a more comprehensive evaluation against a wider range of state-of-the-art techniques in preference learning and self-improvement. This should include methods that use reinforcement learning from human feedback (RLHF) and other forms of self-improvement. The comparison should not only focus on the final performance on the IFEval benchmark but also consider other metrics such as training time, sample efficiency, and robustness to different types of instructions. A more detailed analysis of the strengths and weaknesses of SPaR compared to these methods would provide a more complete picture of its relative performance. This could also include a discussion of the trade-offs between different approaches, such as the computational cost of RLHF versus the potential benefits of SPaR's self-play approach.

Finally, the authors should provide a more in-depth discussion of the limitations of the SPaR framework. This should include a discussion of the potential for the model to overfit to the IFEval benchmark and the generalization capabilities of the model to unseen instructions. The authors should also discuss the potential for the tree-search algorithm to get stuck in local optima and how this could limit the effectiveness of the refinement process. They should also consider the potential for the model to generate responses that are correct but not human-like or creative. A more thorough discussion of these limitations would provide a more balanced view of the approach and help guide future research in this area. This could also include a discussion of potential mitigation strategies for these limitations, such as using data augmentation techniques or incorporating human feedback into the training process.

### Questions

1. Could the authors elaborate on the potential for SPaR to be applied to other types of tasks beyond instruction-following, and what modifications might be necessary?
2. How does the performance of SPaR-trained models generalize to different domains or types of instructions not seen during training?
3. What are the potential ethical implications of using SPaR to improve the capabilities of LLMs, particularly in terms of bias and fairness?

### Rating

6

### Confidence

4

**********
