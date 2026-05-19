### Summary

This paper proposes a new method for adapting vision-language models to downstream tasks. The method is based on the idea of learning multiple prompts for each class, which are referred to as class prototypes. The authors propose an adaptive attention mechanism to weigh the importance of different prototypes and a prototype decorrelation loss to reduce the probability of co-occurrence of multiple prototypes. The method is evaluated on several tasks, including generalization to unseen classes, new target datasets, and domain generalization. The results show that the proposed method outperforms existing methods on several benchmarks.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective. The idea of learning multiple prompts for each class is novel and interesting. The adaptive attention mechanism and prototype decorrelation loss are also well-designed.
3. The method is evaluated on several tasks and benchmarks, and the results show that it outperforms existing methods.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is not very novel. The idea of learning multiple prompts for each class has been explored in previous works, such as MaPLe and CoCoOp. The adaptive attention mechanism is also not very novel, as it is similar to the attention mechanism used in CoCoOp. The prototype decorrelation loss is also not very novel, as it is similar to the decorrelation loss used in MaPLe.
2. The paper does not provide a detailed analysis of the proposed method. For example, the authors do not analyze the effect of the number of prototypes on the performance of the method. The authors also do not analyze the effect of the attention mechanism on the performance of the method. The authors also do not analyze the effect of the prototype decorrelation loss on the performance of the method.
3. The paper does not provide a comparison with some important baselines, such as CoCoOp and MaPLe. The authors should compare their method with these baselines on all benchmarks.

### Suggestions

The paper would benefit from a more thorough analysis of the proposed method. Specifically, the authors should conduct ablation studies to evaluate the impact of each component of the method, including the number of prototypes, the adaptive attention mechanism, and the prototype decorrelation loss. For example, the authors could vary the number of prototypes and report the performance of the method on different benchmarks. They could also remove the adaptive attention mechanism and report the performance of the method. They could also remove the prototype decorrelation loss and report the performance of the method. These ablation studies would help to understand the contribution of each component of the method and to identify the most important components of the method. Furthermore, the authors should analyze the effect of the attention mechanism on the performance of the method. For example, they could visualize the attention weights to understand which prototypes are most important for different classes. They could also report the performance of the method when the attention mechanism is not used. They could also analyze the effect of the prototype decorrelation loss on the performance of the method. For example, they could report the performance of the method when the prototype decorrelation loss is not used. These analyses would help to understand the contribution of each component of the method and to identify the most important components of the method.

In addition, the paper should provide a more detailed comparison with existing methods, such as CoCoOp and MaPLe. The authors should compare their method with these baselines on all benchmarks. For example, they should compare their method with CoCoOp on the few-shot learning benchmarks, the generalization to new classes benchmarks, and the domain generalization benchmarks. They should also compare their method with MaPLe on the same benchmarks. These comparisons would help to understand the advantages and disadvantages of the proposed method compared to existing methods. The authors should also discuss the differences between their method and CoCoOp and MaPLe. For example, they should discuss the differences in the number of prototypes, the attention mechanism, and the prototype decorrelation loss. They should also discuss the advantages and disadvantages of their method compared to CoCoOp and MaPLe. These discussions would help to understand the novelty and contribution of the proposed method.

Finally, the paper should provide a more detailed analysis of the results. For example, the authors should analyze the performance of the method on different classes. They could report the performance of the method on classes with high intra-class variance and classes with low intra-class variance. They could also report the performance of the method on classes with different number of prototypes. These analyses would help to understand the strengths and weaknesses of the proposed method. The authors should also analyze the effect of the hyperparameters on the performance of the method. For example, they could vary the number of prototypes, the attention mechanism, and the prototype decorrelation loss and report the performance of the method. These analyses would help to understand the sensitivity of the method to the hyperparameters.

### Questions

1. What is the effect of the number of prototypes on the performance of the method?
2. What is the effect of the attention mechanism on the performance of the method?
3. What is the effect of the prototype decorrelation loss on the performance of the method?
4. How does the proposed method compare with CoCoOp and MaPLe on all benchmarks?

### Rating

5: marginally below the acceptance threshold

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********
