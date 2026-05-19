### Summary

This paper proposes a novel method to solve the Schrödinger Bridge problem (SBP) in the unpaired image-to-image translation task. The authors first identify the main reason for the failure of previous SB methods as the curse of dimensionality. Based on this, they propose the Unpaired Neural Schrödinger Bridge (UNSB) algorithm, which formulates the SB problem as a sequence of transport cost minimization problems under the constraint on the KL divergence between the true target distribution and the model distribution. The authors demonstrate the effectiveness of UNSB on various image-to-image translation tasks and show that it outperforms existing methods in terms of both quantitative and qualitative results.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and clearly explains the proposed method and its theoretical foundations.
2. The authors provide a comprehensive experimental evaluation of their method on various image-to-image translation tasks, demonstrating its effectiveness and superiority over existing methods.
3. The proposed method is novel and addresses an important problem in image-to-image translation, which has many applications in computer vision and machine learning.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed method and potential directions for future research.
2. The authors could provide more insights into the computational cost and scalability of their method, as well as potential ways to improve its efficiency.
3. The paper could include a more thorough analysis of the impact of different hyperparameters on the performance of the proposed method.

### Suggestions

The paper would be strengthened by a more thorough discussion of the limitations of the proposed Unpaired Neural Schrödinger Bridge (UNSB) method. While the authors demonstrate strong performance on several image-to-image translation tasks, it is important to acknowledge scenarios where the method might struggle or fail. For example, how does the method perform when the source and target domains have significantly different underlying structures or when the data distribution is highly multimodal? A discussion of these limitations would provide a more balanced view of the method's capabilities and help guide future research. Furthermore, it would be beneficial to explore the sensitivity of the method to the choice of the regularization term and the impact of different choices on the quality of the generated images. This could involve a more detailed analysis of the trade-off between the transport cost and the KL divergence constraint.

To improve the practical applicability of the proposed method, the authors should provide a more detailed analysis of its computational cost and scalability. The current discussion is limited, and it is unclear how the method would perform on very large datasets or high-resolution images. A breakdown of the computational complexity of each step in the algorithm, including the adversarial training and the Schrödinger bridge solving process, would be valuable. Additionally, the authors should explore potential strategies for improving the efficiency of the method, such as using more efficient network architectures or optimization techniques. This could involve investigating the use of techniques like knowledge distillation or model compression to reduce the computational overhead. A discussion of the memory requirements of the method, particularly when dealing with high-resolution images, would also be beneficial.

Finally, a more thorough analysis of the impact of different hyperparameters on the performance of the UNSB method is needed. While the authors mention some hyperparameters, a more systematic study is required to understand their influence on the quality of the generated images. For example, how does the choice of the discriminator architecture affect the stability and convergence of the training process? How does the regularization term impact the diversity and fidelity of the generated samples? The authors should consider conducting ablation studies to isolate the effect of each hyperparameter and provide clear guidelines for selecting appropriate values. This analysis should also include a discussion of the sensitivity of the method to the initialization of the neural networks and the random seeds used during training. A more thorough hyperparameter analysis would make the method more accessible and reproducible.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
