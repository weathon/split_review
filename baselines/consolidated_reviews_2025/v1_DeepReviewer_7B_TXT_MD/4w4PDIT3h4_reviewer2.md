### Summary

This paper proposes two novel data augmentation methods for visual reinforcement learning, aiming to improve generalization to unseen environments. The first method, Diverse Data Augmentation (DDA), uses a pre-trained encoder-decoder model to segment primary pixels (e.g., agent, object) from the background and applies diverse data augmentations to the background while keeping the primary pixels intact. The second method, Differential Diverse Data Augmentation (D3A), builds upon DDA by further differentiating data augmentation based on the semantic-invariant state transformation. The authors evaluate their methods on the DeepMind Control Generalization Benchmark (DMC-GB) and demonstrate improved sample efficiency and generalization performance compared to state-of-the-art methods.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed methods are simple yet effective, achieving state-of-the-art performance on the DMC-GB benchmark.
- The authors provide a detailed analysis of the proposed methods, including ablation studies and visualizations of the learned representations.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed methods are not novel, as they are based on existing techniques such as random data augmentation and masking. The paper does not provide a clear explanation of why these techniques are effective for improving generalization in visual RL.
- The evaluation is limited to the DeepMind Control Generalization Benchmark (DMC-GB), which may not be representative of all visual RL tasks. The paper does not evaluate the proposed methods on other benchmarks, such as the DeepMind Control Suite or the Atari Learning Environment.
- The paper does not provide a detailed analysis of the computational cost of the proposed methods. It is unclear whether the performance gains are worth the additional computational overhead.

### Suggestions

The paper would benefit from a more thorough discussion of the novelty of the proposed approach. While the individual components, such as masking and random data augmentation, are not novel, the specific way they are combined and applied to the problem of visual RL generalization could be highlighted more effectively. The authors should clearly articulate the unique aspects of their method and how it differs from existing approaches. For example, a more detailed explanation of how the pre-trained encoder-decoder model is used to segment primary pixels and why this is crucial for effective data augmentation would be beneficial. Furthermore, the paper should provide a more in-depth analysis of the semantic-invariant state transformation in D3A and how it leads to improved generalization compared to DDA. A more rigorous justification for the design choices would strengthen the paper's contribution.

To address the limited evaluation, the authors should consider expanding their experiments to include a wider range of visual RL benchmarks. While DMC-GB is a good starting point, it is important to demonstrate the generalizability of the proposed methods on other tasks with different characteristics. For example, evaluating the methods on the DeepMind Control Suite, which includes a variety of tasks with different levels of difficulty and complexity, would provide a more comprehensive assessment of their performance. Additionally, the authors could consider evaluating their methods on the Atari Learning Environment, which includes a large number of games with different visual characteristics. This would help to demonstrate the robustness of the proposed methods across different types of visual inputs and environments. The paper should also include a more detailed analysis of the performance of the proposed methods on different tasks and environments, highlighting any strengths or weaknesses.

Finally, the paper should include a more detailed analysis of the computational cost of the proposed methods. The authors should provide a breakdown of the computational overhead associated with each step of the algorithm, including the data augmentation, masking, and training of the RL agent. This would help to understand the trade-off between performance gains and computational cost. It would also be beneficial to compare the computational cost of the proposed methods with other data augmentation techniques. The authors should also discuss potential strategies for reducing the computational cost of the proposed methods, such as using more efficient data augmentation techniques or optimizing the implementation of the algorithm. This would help to make the proposed methods more practical and accessible for a wider range of applications.

### Questions

- How does the proposed method compare to other data augmentation techniques in terms of computational cost and performance?
- How does the proposed method generalize to other visual RL benchmarks, such as the DeepMind Control Suite or the Atari Learning Environment?
- What is the impact of different augmentation parameters on the performance of the proposed methods?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
