### Summary

This paper proposes a periodic Bayesian flow network for crystal generation. The proposed method is built on the Bayesian flow network (BFN) and tailored to the crystal generation task. The authors propose a periodic Bayesian flow on the hyper-torus to model the periodic physical symmetry of crystals. The proposed method is evaluated on several benchmarks and achieves state-of-the-art performance.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and interesting. The authors propose a periodic Bayesian flow on the hyper-torus to model the periodic physical symmetry of crystals. This is a novel idea that has not been explored before in the context of crystal generation.
3. The authors provide a theoretical analysis of the proposed method, which is helpful for understanding the underlying principles.
4. The proposed method achieves state-of-the-art performance on several benchmarks, demonstrating its effectiveness.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is based on the Bayesian flow network (BFN), which is not widely used in the field. The authors should provide more background information on BFN and its advantages over other methods.
2. The paper lacks a detailed analysis of the computational complexity of the proposed method. It would be helpful to compare the computational cost of the proposed method with other methods.
3. The paper does not provide a detailed analysis of the limitations of the proposed method. It would be helpful to discuss the potential failure cases and the limitations of the proposed method.

### Suggestions

The authors should provide a more thorough explanation of Bayesian Flow Networks (BFNs), particularly in the context of generative modeling. While the paper introduces BFNs, it would be beneficial to elaborate on their specific advantages and disadvantages compared to other generative models, such as GANs, VAEs, and normalizing flows. A detailed comparison should include a discussion of the underlying mathematical principles, the training procedures, and the types of data for which each method is best suited. For instance, the authors could discuss how BFNs handle the trade-off between sample quality and diversity, and how this compares to other methods. Furthermore, a more in-depth explanation of the specific architectural choices made in the BFN implementation would be valuable, including the rationale behind the selection of the sender and receiver distributions, and how these choices impact the overall performance of the model. This would help readers better understand the nuances of the proposed method and its potential limitations.

To address the lack of computational complexity analysis, the authors should provide a detailed breakdown of the computational cost of each step in their proposed method. This should include the time complexity of the forward and backward passes, as well as the memory requirements for storing the model parameters and intermediate results. A comparison with other crystal generation methods, such as DiffCSP, should be provided, including a discussion of the factors that contribute to the differences in computational cost. For example, the authors could analyze the impact of the number of flow steps, the size of the neural network, and the dimensionality of the data on the overall computational cost. Furthermore, the authors should discuss the potential for optimizing the computational efficiency of their method, such as through the use of more efficient neural network architectures or through the use of parallel computing techniques. This would help readers better understand the practical implications of using the proposed method.

Finally, the authors should provide a more detailed analysis of the limitations of their proposed method. This should include a discussion of the potential failure cases, such as when the model generates unrealistic crystal structures or when it fails to capture the underlying physical constraints. The authors should also discuss the limitations of the proposed method in terms of its ability to generalize to new datasets or to handle more complex crystal structures. For example, the authors could analyze the sensitivity of the model to the choice of hyperparameters, and how this impacts the quality of the generated crystals. Furthermore, the authors should discuss the potential for improving the robustness of their method, such as through the use of data augmentation techniques or through the use of more sophisticated regularization methods. This would help readers better understand the limitations of the proposed method and its potential for future development.

### Questions

Please refer to the weaknesses.

### Rating

6

### Confidence

4

**********
