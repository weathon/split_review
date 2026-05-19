### Summary

This paper proposes a generalization of the submodular Bregman divergence, called the difference-of-submodular Bregman divergence (DBD). The key idea is to generalize the submodular function to the difference-of-submodular (DS) function, which can be any set function. The authors show that the DBD is non-negative and zero if and only if the two sets are equal. The authors also show that the DBD is strictly more expressive than the submodular Bregman divergence. Finally, the authors propose a learnable form of the DBD using permutation-invariant neural networks, and show that it outperforms existing methods on clustering and set retrieval tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The theoretical results are solid and well-supported by proofs.
- The proposed method is novel and well-motivated.
- The experimental results demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

 - The paper could benefit from more detailed explanations of the submodular-Bregman divergence and the difference-of-submodular Bregman divergence, including more examples and illustrations.
- The paper could benefit from more experiments to demonstrate the effectiveness of the proposed method, including comparisons with other state-of-the-art methods and ablation studies to analyze the impact of different components of the proposed method.

### Suggestions

The paper would be significantly strengthened by providing more concrete examples and illustrations of both the submodular-Bregman divergence and the proposed difference-of-submodular Bregman divergence (DBD). For instance, when discussing the submodular-Bregman divergence, it would be helpful to show how specific choices of submodular functions (e.g., facility location, graph cut) lead to different divergence measures and how these measures behave in practice. Similarly, for the DBD, the paper should include examples that clearly demonstrate how the difference of submodular functions is constructed and how it affects the resulting divergence. A visual illustration, perhaps using simple sets and intuitive submodular functions, would greatly enhance the reader's understanding of the proposed divergence and its properties. Furthermore, the paper should include a discussion of the computational complexity of calculating the DBD, especially in comparison to the standard submodular-Bregman divergence, as this is a crucial aspect for practical applications.

To further validate the effectiveness of the proposed method, the experimental section needs to be expanded. The current experiments, while demonstrating the potential of the approach, lack a thorough comparison with state-of-the-art methods. Specifically, the paper should include comparisons with other relevant clustering and set retrieval algorithms, not just the submodular Bregman divergence. This would provide a clearer picture of the advantages and limitations of the proposed DBD. Additionally, the experimental section should include ablation studies to analyze the impact of different components of the proposed method. For example, the paper should investigate the effect of different choices of submodular functions on the performance of the DBD. It would also be beneficial to analyze the sensitivity of the method to the choice of hyperparameters, such as the learning rate and the architecture of the permutation-invariant neural networks. Such analysis would provide valuable insights into the robustness and generalizability of the proposed method.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. While the authors mention that the DBD is more expressive than the submodular Bregman divergence, they do not discuss the potential drawbacks of this increased expressiveness. For example, does the increased expressiveness lead to overfitting or increased computational cost? The paper should also discuss the potential challenges in optimizing the DBD, especially when the submodular functions are complex. A thorough discussion of these limitations would provide a more balanced view of the proposed method and guide future research in this area.

### Questions

- Can you provide more examples and illustrations of the submodular-Bregman divergence and the difference-of-submodular Bregman divergence?
- Can you provide more experimental results to demonstrate the effectiveness of the proposed method, including comparisons with other state-of-the-art methods and ablation studies to analyze the impact of different components of the proposed method?

### Rating

6

### Confidence

3

**********
