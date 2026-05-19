### Summary

This paper proposes to model interacting dynamical systems by combining ODE and GNNs. The paper proposes to extract disentangled contexts including object-level and system-level, which are then integrated into a graph ODE framework. The paper conducts experiments on physics dynamics simulations and molecular dynamics simulations, and the proposed method achieves good performance.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is in general well-written and easy to follow.
2. The proposed method is technically sound.
3. The experiments show good performance of the proposed method.

### Weaknesses

#### Some Related Works

[1] Neural interacting dynamical systems.
[2] Graph interacting dynamical systems.
[3] HOPE: Higher-order Graph ODE for Modeling Interacting Dynamics.

#### comment

1. The idea of combining ODE and GNNs for modeling interacting dynamical systems is not new, which has been explored by many existing works [1, 2, 3]. This paper does not explain the limitations of these existing works and explain what the main difference and advantages of the proposed method.
2. The paper claims that the proposed method can alleviate the issue of OOD, but it is not convincing. First, it is not clear how the designed disentanglement module can help with OOD. In particular, the paper asks to minimize the mutual information between g and u_i, but this is just done for disentanglement, how can it help with OOD? Second, the paper does not conduct sufficient experiments for OOD. For example, it would be good to see the performance of the proposed method under the scenario of varying system size.

### Suggestions

The paper needs to more clearly articulate the novelty of its approach compared to existing methods that also combine ODEs and GNNs for modeling interacting dynamical systems. Specifically, the authors should provide a detailed analysis of the limitations of methods like [1, 2, 3], highlighting the specific scenarios where their approach offers a significant advantage. For instance, if existing methods struggle with long-term predictions due to error accumulation, or if they fail to capture complex interaction patterns, these points should be explicitly stated and supported with evidence. Furthermore, the paper should clarify how the proposed prototype decomposition and contextual discovery mechanisms address these limitations, providing a more concrete explanation of their benefits beyond just stating that they do. A more thorough comparison, both theoretically and empirically, is needed to establish the unique contribution of this work.

To strengthen the claim regarding out-of-distribution (OOD) generalization, the paper needs to provide a more convincing explanation of how the disentanglement module achieves this. While disentanglement can be a useful tool, the paper needs to explicitly link the minimization of mutual information between the global context 'g' and the object-level contexts 'u_i' to the model's ability to generalize to unseen system parameters. It is not sufficient to simply state that disentanglement helps; the authors need to explain the underlying mechanism. For example, does disentanglement allow the model to learn system-invariant object representations, and how does this lead to better OOD performance? Furthermore, the experimental evaluation of OOD generalization should be expanded to include more challenging scenarios, such as varying system sizes, to provide a more comprehensive assessment of the model's robustness.

Finally, the paper should include more ablation studies to justify the design choices of the proposed method. For example, the authors should investigate the impact of different levels of disentanglement on the model's performance, both in-distribution and out-of-distribution. This could involve varying the weight of the disentanglement loss and analyzing its effect on the model's ability to generalize. Additionally, it would be beneficial to explore the sensitivity of the model to different choices of prototypes and contextual information. Such analysis would provide a deeper understanding of the model's behavior and help to identify the key factors that contribute to its performance. Without these additional experiments, it is difficult to fully assess the effectiveness and robustness of the proposed method.

### Questions

1. How are the system parameters \xi defined for different datasets? Are they all known during training and testing?
2. Can the proposed method achieve good performance for long-term prediction? Some existing methods [2, 3] can achieve very good performance for long-term prediction (e.g., 500 steps), and it is interesting to see the performance of the proposed method for long-term prediction.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
