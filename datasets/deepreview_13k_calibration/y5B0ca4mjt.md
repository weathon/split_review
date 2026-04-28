# PIG: Physics-Informed Gaussians as Adaptive Parametric Mesh Representations

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
The approximation of Partial Differential Equations (PDEs) using neural networks has seen significant advancements through Physics-Informed Neural Networks (PINNs). Despite their straightforward optimization framework and flexibility in implementing various PDEs, PINNs often suffer from limited accuracy due to the spectral bias of Multi-Layer Perceptrons (MLPs), which struggle to effectively learn high-frequency and non-linear components. Recently, parametric mesh representations in combination with neural networks have been investigated as a promising approach to eliminate the inductive biases of neural networks.
However, they usually require very high-resolution grids and a large number of collocation points to achieve high accuracy while avoiding overfitting issues.
In addition,  the fixed positions of the mesh parameters restrict their flexibility, making it challenging to accurately approximate complex PDEs.
To overcome these limitations, we propose Physics-Informed Gaussians (PIGs), which combine feature embeddings using Gaussian functions with a lightweight neural network. Our approach uses trainable parameters for the mean and variance of each Gaussian, allowing for dynamic adjustment of their positions and shapes during training. This adaptability enables our model to optimally approximate PDE solutions, unlike models with fixed parameter positions. Furthermore, the proposed approach maintains the same optimization framework used in PINNs, allowing us to benefit from their excellent properties. Experimental results show the competitive performance of our model across various PDEs, demonstrating its potential as a robust tool for solving complex PDEs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors use deep Gaussian mixture models as parametric mesh representations to replace MLP in PINN, so that it performs better for high-frequency and non-linear components. Experiments for PDEs such as Allen-Cahn, Helmholtz, Nonlinear diffusion, etc., are conducted compared with several previous PINN derivatives, showing that the proposed method achieves sota solution accuracy.

### Strengths
- A theoretical proof of the universal approximation capability for the proposed method is provided.
- The experiments are diverse, the baselines are sufficient, and the ablation study is detailed.
- The writing is overall clear and detailed.

### Weaknesses
 - Though diverse and rich, the experimental settings are all relatively simple, and lack comparisons to traditional methods.
- Correct me if I am wrong, but I think only the solution accuracy is provided, without the computation time?

### Questions
- With the work SIREN in mind, I wonder if the Gaussian basis is the best choice?
- The idea is quite similar to 3D Gaussian splatting in rendering. However, there are differences. One easy way to explain is that, we can think of the volume rendering equation as a specific type of governing physics equation. Then the success of applying parametric mixed Gaussian in one specific type of equations doesn't mean it is the best idea for others. For example, there can be long-range interactions for certain PDEs, while Gaussian functions are local and lack such representation capability. I would like to have the authors' opinions on such comments.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose the Physics-Informed Gaussian (PIG) that learns feature embeddings of input coordinates, using a mixture of Gaussian functions. Compared to PINN, this paper applies Gaussians to input coordinates and makes the mean and covariance matrix learnable. The locality of Gaussians encourages the model to capture high-frequency details by effectively alleviating spectral bias.

### Strengths
The paper is well-written and easy to follow. The code and experiments are of good quality. It provides a more concise and more parameter efficient feature embedding method compared to previous parametric grid representations method.

### Weaknesses
 - The primary concern lies in the originality of this method. Though it’s considered as a feature embedding, mathematically, it is in the same spirit of a KAN layer with RBF. Also, it is not uncommon to consider Gaussian embedding in ML.

- The paper states that the approach "dynamically adjusts the positions and shapes of the Gaussians during training" with parameters "iteratively updated throughout the training process." The claims in the paper give an impression of adaptive sampling method based on the training. However, the approach does not actually take into account the residual or the loss function landscape. It would be better to provide a more rigid description on this. Also, in the experiments, the method is compared with different PINN approaches for each PDE, and the authors report the results without conducting experiments by themselves again. Though “the sensitivity of PINN variants to hyperparameters complicates fair comparisons”, it’s still necessary to conduct experiments with same setup and number of parameters to ensure a fair comparison. The average error of PIG is generally higher, but the authors only highlight the best of PIG. PIG is claimed to “enable more accurate and efficient approximations”, but the efficiency is not clear. Hence, it seems a lot of conclusions in this paper are overstated.

- I would like to see how the spectral bias can be alleviated, either through experimental evidence or analytical justification.

- For the 2D and 3D cases, what is the mathematical formulation for the Gaussian embedding? How is the parameter being initialized? Additionally, how are the boundary conditions (BC) being constrained?

- The paper mentions that "computational costs per iteration of our method are significantly lower than JAX-PI." A detailed report of these computational costs would be beneficial.

### Questions
- I would be interested to see how the authors address the weaknesses above. Could authors provide additional evidence or context to support the novelty? 
- Have the authors conducted any experiments to demonstrate how the method alleviates spectral bias?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Physics-Informed Gaussians (PIG) is proposed, an efficient and accurate PDE solver that utilizes
learnable Gaussian feature embeddings and a lightweight neural network, counteracting the problems inherent in previous static parametric grid approaches. PIG model achieves competitive accuracy and faster convergence with fewer parameters compared to state-of-the-art methods.

### Strengths
- The paper is well-written and easy to follow. I enjoyed reading it.

- Motivation is clear.

- Comparisons with previous works are well-discussed.

- The proposed model is supported by both theoretical and empirical evidence.

- Error bars are provided, enhancing the reliability of the experimental results.

- Code is provided for reproducibility.

### Weaknesses
 - (Minor) Figures should be vector images to avoid pixelization.

- While I found no significant weaknesses, there may be room to further expand the discussion on the novelty and its potential impact on future research.

- (Line 245-) "Similar to the previous parametric grid methods, which obtain feature embeddings by interpolating only neighboring vertices, this locality encourages the model to capture high-frequency details by effectively alleviating spectral bias": Is it possible to mathematically prove that "this locality encourages the model to capture high-frequency details by effectively alleviating spectral bias" in some sense? This is just a question out of curiosity.

- Is the title of Section 3.2.2 relevant?

- Why is tanh used in the architecture (it is fine if there is no specific reason)? What about sin or swish activations?

- Is there any issues about mode collapses ($\mu_i \rightarrow \mu_j$ for all $i$ and $j$ and/or $\sigma_i \rightarrow 0$ or $\infty$)?

- I think the update scales of $W$ and $\theta$ differ significantly from those of $\mu_i$ and $\sigma_i$. The optimal updates for $\mu_i$ and $\sigma_i$ likely depend on the scale of the simulation. Did the authors encounter any issues related to this?

- It may be off-topic, but is the proposed method applicable to high-dimensional PDEs, such as $d\gtrsim100$? How significant is the computational cost?

### Questions
- (Line 245-) "Similar to the previous parametric grid methods, which obtain feature embeddings by interpolating only neighboring vertices, this locality encourages the model to capture high-frequency details by effectively alleviating spectral bias": Is it possible to mathematically prove that "this locality encourages the model to capture high-frequency details by effectively alleviating spectral bias" in some sense? This is just a question out of curiosity.

- Is the title of Section 3.2.2 relevant?

- Why is tanh used in the architecture (it is fine if there is no specific reason)? What about sin or swish activations?

- Is there any issues about mode collapses ($\mu_i \rightarrow \mu_j$ for all $i$ and $j$ and/or $\sigma_i \rightarrow 0$ or $\infty$)?

- I think the update scales of $W$ and $\theta$ differ significantly from those of $\mu_i$ and $\sigma_i$. The optimal updates for $\mu_i$ and $\sigma_i$ likely depend on the scale of the simulation. Did the authors encounter any issues related to this?

- It may be off-topic, but is the proposed method applicable to high-dimensional PDEs, such as $d\gtrsim100$? How significant is the computational cost?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes Physics-Informed Gaussians (PIGs), which incorporates Gaussian embeddings in the PINNs framework, to eliminate the inductive biases of neural networks.

### Strengths
The strength of this paper is to overcomes the limitations of traditional PINNs.  The proposed method maintains the benefits of PINNs, improves performance in PDE approximation, and can be applied to various PDEs.

### Weaknesses
As mentioned in Discussion and Limitations, theoretical understanding of the convergence properties is lack, although the universality of PIG is discussed in Section 3.3.

### Questions
I may miss something but, is there any reason why choose Gaussian functions as feature embedding? Would other embedding functions fail in the proposed framework?

### Soundness
3

### Presentation
3

### Contribution
3
