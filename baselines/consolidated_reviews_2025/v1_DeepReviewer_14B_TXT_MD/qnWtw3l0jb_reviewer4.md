### Summary

This paper proposes to use the forward-backward (FB) framework as a behavior foundation model (BFM) for imitation learning (IL). The FB model is trained using unsupervised data, and then used for IL. The paper shows that with the right choices of reward function, the FB model can be used for BC, reward-based IL, distribution matching, feature matching, and goal-based IL. The proposed methods are tested on the DeepMind control suite, and outperforms other baselines with significantly less computation time.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper does a great job of providing background information and references to the literature. The proposed method is clear, and the theoretical justification is well explained. The experimental results are state-of-the-art, and the method is efficient.

### Weaknesses

#### Some Related Works


#### comment

The paper claims that the proposed method can use few demonstrations to imitate any behavior, but the experiments only include continuous control benchmark tasks. It is not clear if the proposed method can work for more complex tasks like manipulation that may require a discrete set of skills, or for image-based observations. The paper could also include an experiment that tests how the performance changes with more demonstrations to fully validate the few-shot claim.

### Suggestions

The paper would benefit from a more thorough investigation into the limitations of the forward-backward (FB) framework when applied to complex, hierarchical tasks. While the current experiments on the DeepMind Control Suite are promising, they do not fully capture the challenges associated with tasks that require a discrete set of skills or long-term planning. For example, manipulation tasks often involve distinct phases, such as grasping, moving, and placing, each of which might benefit from a specialized policy. The current FB approach, which learns a single set of successor features, may struggle to capture these distinct modes of behavior. It would be valuable to see experiments on benchmarks that explicitly test these capabilities, such as those involving tool use or multi-stage problem solving. Furthermore, the paper should discuss how the FB framework could be extended to handle such hierarchical structures, perhaps by incorporating options or skills into the learning process.

Another area that requires further exploration is the robustness of the proposed method to changes in the environment or task parameters. The current experiments are conducted in relatively static environments, but real-world scenarios often involve dynamic conditions and variations in task requirements. For instance, the dynamics of a robot arm might change due to wear and tear, or the goal of a manipulation task might be slightly different each time. It would be important to evaluate how well the FB-based imitation learning method adapts to these changes. This could involve experiments where the environment dynamics are perturbed or where the task goal is varied. The paper should also discuss potential strategies for improving the robustness of the method, such as domain randomization or adaptive learning techniques. This would help to establish the practical applicability of the proposed approach.

Finally, while the paper touches on the use of variational autoencoders (VAEs) for state embeddings, it would be beneficial to provide more details on the specific architecture and training procedure used. The quality of the state embedding is crucial for the performance of the FB framework, and different VAE architectures can produce embeddings with varying levels of semantic information. It would be helpful to see a comparison of different VAE architectures and to analyze the properties of the resulting embeddings. Furthermore, the paper should discuss how the choice of VAE architecture affects the overall performance of the imitation learning method. This would provide valuable insights into the practical considerations of using the FB framework for imitation learning.

### Questions

Can the proposed method work for tasks that require both continuous and discrete actions? 

Can the proposed method work for image-based observations? 

Can the proposed method work for tasks with long horizon and where a discrete set of skills is needed? For example, a robot arm that needs to assemble an object. 

Can the proposed method work if the dynamics of the environment changes?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
