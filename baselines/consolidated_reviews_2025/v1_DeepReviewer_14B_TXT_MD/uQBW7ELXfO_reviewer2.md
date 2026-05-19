### Summary

This paper proposes a new method for unpaired image-to-image translation based on the Schrodinger Bridge problem. The key idea is to formulate the Schrodinger Bridge problem as a sequence of adversarial learning problems, which allows the use of advanced discriminators and regularization techniques to mitigate the curse of dimensionality. The authors demonstrate that their method, called Unpaired Neural Schrodinger Bridge (UNSB), successfully solves various unpaired image-to-image translation tasks and outperforms existing methods in terms of both quantitative and qualitative results.

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

The paper would be strengthened by a more detailed discussion of the limitations of the proposed Unpaired Neural Schrodinger Bridge (UNSB) method. Specifically, the authors should explore scenarios where the method might fail or underperform. For instance, how does the method handle significant domain shifts or complex transformations between the source and target domains? Are there specific types of image content or structures that pose challenges for UNSB? A discussion of these limitations would provide a more balanced view of the method's capabilities and help guide future research. Furthermore, the authors should consider discussing the sensitivity of the method to the quality of the input data. For example, how does the performance degrade with noisy or low-resolution images? Addressing these points would provide a more complete understanding of the method's robustness and applicability.

In addition to the limitations, a more thorough analysis of the computational cost and scalability of the UNSB method is needed. The authors should provide a detailed breakdown of the computational complexity of each step in their algorithm, including the adversarial training and the Schrodinger Bridge solving process. This analysis should consider the impact of different hyperparameters, such as the number of steps in the Markov chain and the size of the neural networks. Furthermore, the authors should discuss the memory requirements of their method, particularly when dealing with high-resolution images or large datasets. It would also be beneficial to explore potential strategies for improving the efficiency of the method, such as using more efficient network architectures or optimization techniques. A discussion of the trade-offs between computational cost and performance would be valuable for practitioners considering the use of this method.

Finally, the paper would benefit from a more in-depth analysis of the impact of different hyperparameters on the performance of the UNSB method. While the authors mention some hyperparameters, a more systematic study is needed to understand their influence on the quality of the generated images. For example, how does the choice of the discriminator architecture affect the stability and convergence of the training process? How does the regularization term impact the diversity and fidelity of the generated samples? The authors should consider conducting ablation studies to isolate the effect of each hyperparameter and provide clear guidelines for selecting appropriate values. This analysis should also include a discussion of the sensitivity of the method to the initialization of the neural networks and the random seeds used during training. A more thorough hyperparameter analysis would make the method more accessible and reproducible.

### Questions

1. Can the authors provide more insights into the computational cost and scalability of their method, as well as potential ways to improve its efficiency?
2. How does the proposed method compare to other state-of-the-art methods in terms of computational cost and scalability?
3. Can the authors provide more insights into the impact of different hyperparameters on the performance of their method?

### Rating

6: marginally above the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
