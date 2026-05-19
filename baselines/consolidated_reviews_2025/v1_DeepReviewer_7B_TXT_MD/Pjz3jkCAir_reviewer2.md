### Summary

The paper proposes a new method for inferring the parameters of a PDE from a data sample. The method is based on a combination of an autoencoder and a neural network. The autoencoder is used to encode the data sample into a compact representation, while the neural network is used to infer the parameters of the PDE from the encoded representation. The method is tested on several PDEs and compared to other methods.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The paper addresses an important problem of inferring the parameters of a PDE from a data sample. This is a challenging problem, and the proposed method is a novel approach to solving it.
- The paper is well-written and easy to follow. The authors provide a clear explanation of the proposed method and its advantages over existing approaches.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a clear motivation for the proposed method. It is not clear why the proposed method is better than existing approaches. The authors should provide a more detailed explanation of the limitations of existing methods and how the proposed method addresses these limitations.
- The paper does not provide a detailed analysis of the computational complexity of the proposed method. It is not clear how the computational cost of the proposed method scales with the size of the input data and the complexity of the PDE. The authors should provide a detailed analysis of the computational complexity of the proposed method and compare it to existing methods.
- The paper does not provide a detailed analysis of the robustness of the proposed method to noise and uncertainty in the data. It is not clear how the proposed method performs in the presence of noisy or incomplete data. The authors should provide a detailed analysis of the robustness of the proposed method to noise and uncertainty in the data and compare it to existing methods.
- The paper does not provide a detailed analysis of the generalization performance of the proposed method. It is not clear how well the proposed method generalizes to new PDEs or new data distributions. The authors should provide a detailed analysis of the generalization performance of the proposed method and compare it to existing methods.

### Suggestions

The paper would benefit significantly from a more thorough comparison with existing methods, particularly those that also leverage neural networks for PDE parameter inference. The authors should clearly articulate the specific scenarios where their approach offers a clear advantage over methods like PINNs or neural operators. For instance, if the proposed method is designed to handle specific types of PDEs or boundary conditions, this should be explicitly stated and supported by experimental evidence. Furthermore, a more detailed discussion of the limitations of existing methods, such as their sensitivity to hyperparameter tuning or their inability to generalize to unseen PDEs, would help to justify the need for the proposed approach. The authors should also consider including a comparison with methods that use different neural network architectures or training strategies to ensure a comprehensive evaluation.

To address the lack of clarity regarding the method's advantages, the authors should provide a more detailed explanation of the specific mechanisms that enable their method to outperform existing approaches. For example, if the autoencoder is used to extract features that are more relevant to the PDE parameters, this should be explained in detail. The authors should also discuss the specific properties of the autoencoder architecture and training process that contribute to the method's performance. Furthermore, a more detailed analysis of the computational complexity of the proposed method is needed. The authors should provide a breakdown of the computational cost of each step in the method, including the autoencoder training, the neural network training, and the inference process. This analysis should include a discussion of how the computational cost scales with the size of the input data, the complexity of the PDE, and the number of parameters in the neural networks. A comparison of the computational complexity with existing methods would also be beneficial.

Finally, the paper needs a more comprehensive analysis of the method's robustness to noise and uncertainty in the data. The authors should provide a detailed analysis of how the method performs under different levels of noise and uncertainty, including both Gaussian and non-Gaussian noise. This analysis should include a discussion of the method's sensitivity to the choice of hyperparameters and the impact of these hyperparameters on the method's performance. Furthermore, the authors should provide a more detailed analysis of the method's generalization performance. This analysis should include experiments on new PDEs or new data distributions, as well as a discussion of the method's limitations in terms of generalization. The authors should also consider including a discussion of the method's limitations in terms of the types of PDEs that it can handle and the types of data that it can be applied to.

### Questions

- How does the proposed method compare to existing methods for PDE parameter inference, such as PINNs and neural operators?
- How does the proposed method handle noisy or incomplete data?
- How does the proposed method generalize to new PDEs or new data distributions?

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
