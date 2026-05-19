### Summary

The paper proposes a method for inferring the coefficients of a PDE from a single observation of the solution. The method is based on a combination of an autoencoder and a neural network. The autoencoder is trained to compress the data into a latent representation, and the neural network is trained to predict the coefficients of the PDE from the latent representation. The method is evaluated on several PDEs, including the Burgers' equation, the FitzHugh-Nagumo equations, and the Navier-Stokes equations. The results show that the proposed method outperforms several baselines, including neural ODEs, Fourier neural operators, and U-Nets.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The problem is well-motivated, and the proposed method is clearly explained. The experiments are well-designed and provide strong evidence for the effectiveness of the proposed method. The paper also includes a thorough comparison with several baselines, which helps to demonstrate the advantages of the proposed method.

### Weaknesses

#### Some Related Works

[1] Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations
[2] Learning in the Fourier Domain for Solving Time-Dependent Inverse Problems
[3] Learning in the Fourier Domain for Solving Time-Dependent Inverse Problems
[4] Learning in the Fourier Domain for Solving Time-Dependent Inverse Problems

#### comment

The paper does not provide a clear motivation for the proposed method. It is not clear why the proposed method is better than existing approaches. The authors should provide a more detailed explanation of the limitations of existing methods and how the proposed method addresses these limitations.

The paper does not provide a detailed analysis of the computational complexity of the proposed method. It is not clear how the computational cost of the proposed method scales with the size of the input data and the complexity of the PDE. The authors should provide a detailed analysis of the computational complexity of the proposed method and compare it to existing methods.

The paper does not provide a detailed analysis of the robustness of the proposed method to noise and uncertainty in the data. It is not clear how the proposed method performs in the presence of noisy or incomplete data. The authors should provide a detailed analysis of the robustness of the proposed method to noise and uncertainty in the data and compare it to existing methods.

The paper does not provide a detailed analysis of the generalization performance of the proposed method. It is not clear how well the proposed method generalizes to new PDEs or new data distributions. The authors should provide a detailed analysis of the generalization performance of the proposed method and compare it to existing methods.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of existing methods for inferring PDE coefficients. Specifically, the authors should elaborate on why methods like neural ODEs, Fourier neural operators, and U-Nets are not directly applicable or are less effective in the context of the problem they are addressing. For example, while neural ODEs can learn dynamics, they typically require a time-series of data or a known time evolution, which is not the case here. Similarly, Fourier neural operators are designed for learning mappings between function spaces, and while they can be used for PDE solving, they are not inherently designed for coefficient inference from a single snapshot. A more detailed explanation of these limitations would help to justify the need for the proposed method and highlight its unique contributions. Furthermore, the authors should discuss the specific challenges of inferring PDE coefficients from a single observation, such as the ill-posed nature of the inverse problem and the potential for multiple solutions. This would provide a stronger motivation for the proposed approach.

To address the lack of computational complexity analysis, the authors should provide a detailed breakdown of the computational cost of each step in their method, including the autoencoder training, the neural network training, and the inference process. This analysis should include a discussion of how the computational cost scales with the size of the input data, the complexity of the PDE, and the number of parameters in the neural networks. A comparison of the computational complexity with existing methods would also be beneficial. For example, the authors could compare their method to a standard finite difference method for solving the PDE, or to a method that uses a different approach for coefficient inference. This would help to put the computational cost of the proposed method into perspective and allow readers to assess its practical feasibility. The authors should also discuss the memory requirements of their method, which can be a limiting factor for large-scale problems.

Finally, the paper needs a more comprehensive analysis of the robustness and generalization capabilities of the proposed method. The authors should provide a detailed analysis of how the method performs under different levels of noise and uncertainty in the data. This could include experiments with synthetic data corrupted by different types of noise, or with real-world data that contains measurement errors. The authors should also investigate how the method generalizes to new PDEs or new data distributions. For example, they could test the method on PDEs with different boundary conditions or different types of non-linearities. This would help to assess the limitations of the proposed method and identify areas for future research. The authors should also discuss the sensitivity of the method to the choice of hyperparameters and provide guidelines for selecting appropriate values.

### Questions

How does the proposed method compare to existing methods for PDE parameter inference, such as PINNs and neural operators?

How does the proposed method handle noisy or incomplete data?

How does the proposed method generalize to new PDEs or new data distributions?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
