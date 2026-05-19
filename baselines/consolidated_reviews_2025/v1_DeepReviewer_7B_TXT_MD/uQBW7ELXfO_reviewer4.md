### Summary

This paper proposes a new method for solving the Schrödinger Bridge problem, which is a generalization of the Optimal Transport problem. The authors propose to solve the SB problem by iteratively solving a sequence of conditional generation problems. The authors provide a theoretical analysis of the proposed method and demonstrate its effectiveness on several image-to-image translation tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors provide a clear motivation for the proposed method and a thorough theoretical analysis. The experimental results are promising and demonstrate the effectiveness of the proposed method on several image-to-image translation tasks.

### Weaknesses

#### Some Related Works


#### comment

The paper does not provide a detailed analysis of the computational cost of the proposed method. It would be beneficial to understand how the computational cost scales with the size of the input data and the complexity of the model. Specifically, the paper lacks a breakdown of the time and memory requirements for each step of the iterative conditional generation process. This makes it difficult to assess the practical applicability of the method, especially for large-scale datasets or high-resolution images. Furthermore, the paper does not discuss the sensitivity of the method to hyperparameter choices, which is crucial for reproducibility and practical use. It would be helpful to see an analysis of how different hyperparameters affect the convergence and performance of the algorithm.

### Suggestions

The authors should provide a more detailed analysis of the computational cost of their proposed method. This should include a breakdown of the time and memory requirements for each step of the iterative conditional generation process. For example, they could provide a table showing the training time per epoch, memory usage during training, and inference time for different image resolutions and dataset sizes. This would allow readers to better understand the practical limitations of the method and its scalability. Furthermore, the authors should investigate the sensitivity of their method to hyperparameter choices. This could involve conducting a parameter study to show how different hyperparameters affect the convergence and performance of the algorithm. For example, they could show how the number of iterations, learning rate, and batch size affect the final image quality. This would help readers to better understand the robustness of the method and how to tune it for different tasks.

In addition to the computational and hyperparameter analysis, the authors should also consider providing more details about the implementation of their method. This could include a discussion of the specific neural network architectures used for the conditional generation steps, as well as the optimization algorithms and loss functions used for training. This would help other researchers to reproduce their results and build upon their work. Furthermore, the authors could consider releasing their code and pre-trained models to the public, which would further enhance the impact of their work. This would allow other researchers to easily use their method and compare it to other approaches. Finally, the authors should also consider providing a more detailed comparison of their method to existing approaches for solving the Schrödinger Bridge problem. This would help readers to understand the advantages and disadvantages of their method compared to other state-of-the-art techniques.

Finally, the authors should also consider including more qualitative results in their paper. While the quantitative results are promising, it would be helpful to see more visual examples of the generated images to better understand the behavior of the method. This could include showing examples of the generated images for different input images and different hyperparameter settings. This would help readers to better understand the strengths and weaknesses of the method and how it compares to other approaches. The authors could also consider including a discussion of the limitations of their method and potential directions for future research. This would help to put their work in context and highlight the areas where further work is needed.

### Questions

Please see the weakness.

### Rating

8: accept, good paper

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
