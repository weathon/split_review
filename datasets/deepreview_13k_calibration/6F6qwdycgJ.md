# Towards Hierarchical Rectified Flow

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8

## Abstract
We formulate a hierarchical rectified flow to model data distributions. It hierarchically couples multiple ordinary differential equations (ODEs) and defines a time-differentiable stochastic process that generates a data distribution from a known source distribution. Each ODE resembles the ODE that is solved in a classic rectified flow, but differs in its domain, i.e., location, velocity, acceleration, etc. Unlike the classic rectified flow formulation, which formulates a single ODE in the location domain and only captures the expected velocity field (sufficient to capture a multi-modal data distribution), the hierarchical rectified flow formulation models the multi-modal random velocity field, acceleration field, etc., in their entirety. This more faithful modeling of the random velocity field enables integration paths to intersect when the underlying ODE is solved during data generation. Intersecting paths in turn lead to integration trajectories that are more straight than those obtained in the classic rectified flow formulation, where integration paths cannot intersect. This leads to modeling of data distributions with fewer neural function evaluations. We empirically verify this on synthetic 1D and 2D data as well as MNIST and CIFAR10 data. We will release our code.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel framework, hierarchical rectified flow, to model data distributions. It addresses the limitations of conventional rectified flow (RF), which only captures mean velocity, by incorporating distributional information in the velocity space. The objective, equivalent to acceleration matching, derives target acceleration from the data and prior velocity distributions. The framework can be extended beyond acceleration, creating a hierarchical generation model. The proposed approach offers benefits such as easier path integration and improved results with fewer NFEs.

### Strengths
The strengths of the paper are listed below:
- Clear motivation with well-written, easy-to-follow presentation.  
- Experimental results that partially support the theoretical claims.

### Weaknesses
The weaknesses of the paper are listed below:
- While the paper's motivation is sound, my main concern lies in the practicality and application of the proposed approach. The generation framework demands significantly more model calls compared to the conventional RF framework, specifically NFEs multiplied by the number of discretizations in the velocity space. Although RF only targets mean velocity, it delivers strong empirical results with far greater efficiency than the proposed method. Additionally, RF can be rectified multiple times for better results. I recommend that the authors conduct a comprehensive comparison between the rectified RF and the proposed method. This inefficiency could lead to significantly limited applicability, especially for larger datasets like ImageNet. Could the authors include a comparison of generation performance and training/inference time between the rectified RF and the proposed method on the existing datasets, or ideally on ImageNet?

- The inefficiency becomes even more pronounced with increased depth; for example, a D-depth model requires a substantially larger architecture compared to a one-depth model.  Does the forgetting problem of the optimal trajectory occur with increased depth, necessitating an expanded architecture? Could the authors provide an ablation study on how model performance and computational requirements change as depth increases?

- The paper lacks a comprehensive comparison of efficiency, including training and inference time, against RF and rectified RF. The paper should include details of the neural network architecture to ensure reproducibility in toy settings. The paper should include more details of the neural network architecture and experimental settings to ensure reproducibility in toy scenarios.

- On the theoretical side, does increasing depth make it harder for the model to converge during training? It would be helpful to include empirical evidence of convergence rates for models with different depths or a discussion of any theoretical bounds on convergence that might exist when using larger depths.

- Minor typo on line 156: it should be \pi_0. Please review and correct all typos.

### Questions
Please see the Weaknesses section for my concerns and questions.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The work enriches the concept of rectified flow for generating data from known base distribution to data distribution. Compared to the base approach, hierarchical rectified flow formulation models the multi-modal random velocity field and acceleration field, which leads to generating more interesting trajectories. The authors evaluate their approach on some low-dimensional use cases and small image benchmark data.

### Strengths
***Clarity and Accessibility***: The paper is well-written and presented in a logical manner, making the concepts and methodology easy to follow. Complex ideas are explained in a way that is accessible to readers with varying levels of familiarity with flow-based generative models, facilitating broader understanding and engagement with the research.

***Clear and Impactful Motivation***: The authors provide a compelling motivation for developing hierarchical rectified flow models, addressing limitations in existing flow-based generative models. This work has the potential to significantly impact the field by introducing a more flexible and expressive approach, which could inspire further research and applications in generative modeling.

***Solid Theoretical Foundations***: The paper presents strong theoretical foundations that support the proposed hierarchical model. These well-motivated considerations provide a rigorous basis for understanding how the model improves upon previous approaches, making the proposed framework robust and trustworthy.

***Intuitive Experimental Demonstrations***: The inclusion of low-dimensional toy experiments adds an important educational aspect to the study, offering readers an intuitive way to grasp the dynamics of the approach. These experiments clarify how the model handles multi-modal distributions and complex trajectories, offering insights that make the approach more transparent and easier to analyze.

### Weaknesses
 ***Ambiguity in Extended Hierarchical Approach***: Although the acceleration-based approach and its motivation are clear and well-justified, the transition to the extended hierarchical flow model lacks clarity. Specifically, while the training objective for the acceleration-based approach is defined by Equation (8), the relationship to the hierarchical model’s training objective, outlined in Equation (10), is not thoroughly explained. The conceptual progression and the structural specifics of the higher-dimensional source distribution (D-dimensional) are left somewhat ambiguous. It is unclear how the multiple levels of the hierarchy interact and how the velocity and acceleration fields are composed across these levels. A more detailed explanation of how the source distribution is constructed, particularly how its dimensionality is determined and how it interfaces with the hierarchical model, is needed to clarify the extension. The paper would benefit from a more explicit description of how the gradients are computed and propagated through the hierarchical structure during training. 

***Scalability and Computational Complexity***: While the hierarchical rectified flow method is innovative, its computational demands are significant, particularly when scaling to high-dimensional data. Even when considering latent models, the approach appears to be resource-intensive and potentially impractical for high-dimensional images due to its complex sampling procedure. The iterative nature of the sampling process, which requires multiple evaluations of the learned vector fields, contributes to the computational burden. This aspect could hinder its use in real-world scenarios where efficient sampling and rapid training times are crucial. The authors should provide a more detailed analysis of the computational overhead, comparing training and sampling times with other flow-based generative models, including a breakdown of the time spent on different stages of the algorithm, to highlight both the benefits and trade-offs of their approach. A discussion of potential optimizations to reduce the computational cost would also be beneficial.

***Limited Scope of Experiments***: The experimental evaluation primarily uses small, low-dimensional image datasets, which limits the generalizability and relevance of the results. Given current advancements in generative modeling, such datasets do not fully showcase the potential of the hierarchical approach. The experiments lack a thorough investigation of the model's behavior on more complex data distributions and its ability to capture fine-grained details. Adding experiments on higher-dimensional or more complex data—perhaps by incorporating latent diffusion architectures—would better demonstrate the method’s scalability and practical value. More comprehensive experimentation, including a comparison with state-of-the-art generative models on standard benchmarks, would help readers assess how well the model performs in scenarios closer to those encountered in modern applications of generative models. The analysis should also include a discussion of the limitations of the current experimental setup and potential future directions.

### Questions
Please refer to the weakness section.

### Soundness
2

### Presentation
3

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
Flows $p_t$ transform one distribution $p_0$ into another $p_1$ via a corresponding vector field $f(x_t,t)$ that satisfies its continuity equation. The flow is typically defined via conditional flows, for example $p_t(x|x_0, x_1)\sim t(x_1)+(1-t)x_0+\sigma\epsilon$, where one can take the limit $\sigma\rightarrow 0$. The corresponding flow is simply $p_t(x)=\int p_t(x|x_0, x_1) \pi(x_0, x_1)dx_0 dx_1$. The conditional vector fields $v_t(x_t|x_0,x_1)$ that satisfy the continuity equation of such flows are $x_1-x_0$, while the unconditional vector field is $f(x_t,t)=\int v_t(x_t|x_0,x_1) p_t(x_0, x_1|x_t) dx_0 dx_1=\int v_t(x_t) \pi_t(v_t|x_t) dv_t$.

This paper studies the possibility of using a sample of $\pi_t(v_t|x_t)$ at each integration step during data generation, instead of using the mean $f(x_t,t)$ which is akin to using stochastic gradient descent instead of gradient descent. . The result is a stochastic sampling process, which by using a derivation of $\pi_t(v_t|x_t)$ is proven to have marginals that coincide with the flow $p_t$.

The distribution $\pi_t(v_t|x_t)$ is itself modeled using the methodology of rectified flow matching, and the methodology is applied to synthetic and high dimensional image data.

### Strengths
The paper is generally well written, even though a few parts could be improved.

Theorem 1 and 2 are interesting results, and provide insights about the conditional distribution of velocities at each current point $x_t$ and they enable using higher order stochastic sampling.

### Weaknesses
My **main** concerns are the following:

1. The proposed method requires taking the position and the current velocity as input in order to predict the acceleration. The authors mention expanding the Resnet for their framework and increasing the amount of data processed. Can authors provide a detailed table comparing HRF and RF models, including parameter counts, training time per iteration, and memory usage across all experiments?

2. It is not clear if the NFE includes the steps required to sample the velocities. The paper should report both L and J in each experiment. Also the compute time for each step should be reported and compared with RF.

3. The results for CIFAR-10 unfortunately are not encouraging. Considering the results on MNIST and CIFAR-10 it seems that the proposed model does not scale as well. This is why it is important to also test the model on Imagenet.

4. The resulting model is not a diffeomorphism and as such we lose the ability to perform density estimation.

In my opinion the main contributions of the work are theoretical, and applying the proposed methodology in practice is challenging.

### Questions
1. What are the parameter counts for both HRF and the baseline HF? Also what is the training time per iteration?

2. Is the reported $NFE=J\cdot L$? What is the time required per NFE in both HFR and RF?

3. The paper claims that the resulting paths are straight as the trajectories can intersect. However the trajectories are stochastic, and thus they are likely to increase overall length. I would appreciate a clarification from the authors regarding this matter.

### Soundness
3

### Presentation
3

### Contribution
2
