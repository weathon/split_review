# Neural Network-Based Score Estimation in Diffusion Models: Optimization and Generalization

- Decision: Accept
- Scores: 6, 8, 5, 6

## Abstract
Diffusion models have emerged as a powerful tool rivaling GANs in generating high-quality samples with improved fidelity, flexibility, and robustness. A key component of these models is to learn the score function through score matching. Despite empirical success on various tasks,  it remains unclear whether gradient-based algorithms can learn the score function with a provable accuracy. As a first step toward answering this question, this paper establishes a mathematical framework for analyzing score estimation using neural networks trained by gradient descent. Our analysis covers both the optimization and the generalization aspects of the learning procedure. In particular, we propose a parametric form to formulate the denoising score-matching problem as a regression with noisy labels. Compared to the standard supervised learning setup, the score-matching problem introduces distinct challenges, including unbounded input, vector-valued output, and an additional time variable, preventing existing techniques from being applied directly. In this paper, we show that with proper designs, the evolution of neural networks during training can be accurately modeled by a series of kernel regression tasks.
Furthermore, by applying an early-stopping rule for gradient descent and leveraging {recent developments in neural tangent kernels}, we establish the first generalization error (sample complexity) bounds for learning the score function with neural networks, despite the presence of noise in the observations. Our analysis is grounded in a novel parametric form of the neural network and an innovative connection between score matching and regression analysis, facilitating the application of advanced statistical and optimization techniques.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies score estimation using neural networks trained by gradient descent. In particular, they train a two-layer fully connected neural network through gradent descent to learn the score function. To establish a theoretical result, they introduce a parametric form for the score function and connect neural network learning with learning a kernel regression task. They separately upper bound the loss caused by (1) RKHS approximation to the score function, (2) difference between kernel regression and training a neural network. (3) label mismatch.

### Strengths
This paper proposes a framework that gives an end-to-end result for sampling with diffusion model, starting from using GD to learn neural network to score estimation. Their technical idea is highly-nontrivial: They connect GD training of a two-layer NN with kernel regression, and bound each component separately.

### Weaknesses
The paper's presentation is a bit dense and can be improved. Clarifying the dependency of constants and explaining why the assumptions are reasonable would be helpful. In addition, the upper bounds presented in the paper seem far from tight. It is not clear whether these bounds are useful for getting guarantee in specific contexts. Finally, the parametric form this paper proposes does not seem to be novel. Specifically, the decision to fix $a$ and only update $W$ during training deviates from the random feature model where $a$ is trained and $W$ is randomly generated. This choice needs further justification, especially in comparison to the NTK regime where $W$ is assumed to remain relatively stable, effectively reducing the problem to fitting a linear model with $a$ as coefficients. The uniform sampling of time also warrants further explanation, particularly since non-uniform weight functions are often employed in practice. It would be beneficial to understand how the choice of this weight function impacts the results. The notation and assumptions also need clarification. For instance, the notation $\beta_x$ is confusing, as it should not depend on $x$. Assumption 3.5 seems to be a fact rather than an assumption when the target is bounded, especially when $g$ is a positive constant. Theorem 3.6's upper bound appears quite large, potentially exceeding $O(d)$, which is the scale of the noisy label. A clearer explanation of why this bound is interesting and relevant would be valuable. The relationship between the two delta functions in Assumptions 3.7 and 3.8, and the large second term in Theorem 3.9's upper bound, also require further clarification. Lastly, the statement that "Assumption 3.11 can be satisfied by an extension of classical early stopping rules for scalar-valued kernel regression" needs elaboration and perhaps a concrete example.

### Questions
1. Could the authors elaborate a little bit more on why is it reasonable to fix $a$ throught training and only update $W$? In a random feature model $a$ is trained while $W$ is generated randomly. In the NTK regime it is also assumed that $W$ does not change too much during training, hence the problem reduces to fitting a linear model with $a$ representing the coefficients. 
2. Why the authors propose to uniformly sample the time? In practice usually a non-uniform weight function is employed. How does the choice of weight function affect the result. 
3. I feel the most general form of Lemma 3.1 has already been established in many past works. See for example, section 5.1 of https://arxiv.org/pdf/2306.09251.pdf and the intro section of https://arxiv.org/pdf/2309.11420.pdf. I think the authors should at least cite these papers and discuss the relation. 
4. How is $\gamma$ initialized? 
5. The notation $\beta_x$ is a bit confusiong. I assume it should not depend on $x$. Maybe the authors can state what does it depend on? 
6. I think Assumption 3.5 is a fact instead of an assumption when the target is bounded, at least when $g$ is a positive constant. This is because taking the gradient of the conditional expectation gives the conditional covaraince, which has bounded operator norm when data is bounded.  
7. In Theorem 3.6, should I interpret $c_1$ as a universal constant? If not, what does it depend on?
8. I might have missed something, but I feel the upper bound given in Theorem 3.6 is pretty large. Like it could be much larger than $O(d)$, the scale of the noisy label. Why is it an interesting bound?
9. In Assumption 3.6 you mean $1 - \delta (\Delta, R)$? 
10. There are two delta functions in Assumption 3.7 and 3.8, what are their relation? 
11. I feel the second term in Theorem 3.9 upper bound is huge. If it is not, maybe the authors can comment on it a little bit. 
12. Could the authors elaborate more on why "Assump- tion 3.11 can be satisfied by an extension of classical early stopping rules for scalar-valued kernel regression." Maybe giving an example in which this assumption is satisfied would be helpful for readers to digest.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In the paper, the authors analyze the generalization of diffusion models through the lens of Neural Tangent Kernels and their RKHS. Authors derive generalization bounds, universal approximation, and convergence of gradient descent and implications for early-stopping.

### Strengths
Well written with rigorous theoretical analysis, well stated assumotions, showing generalization/convergence of diffusion models, which is rather important area right now, and paper definitely worth attention for such theoretical analysis.

### Weaknesses
1. The curse of dimensionality not discussed. In particular, it is interesting to know for this problem exact dependency of all constants on dimension and discuss this in limitations of the work if exponential dependency is present.
2. As training procedure considered gradient descent, not stochastic, which limits applicability, as noise for this setup should introduce another dimension dependent factors. But that's minor (and not important as results of the work are interesting by itself)


### Questions
In Lemma 3.3 bound depends exponentially on dimension d, which makes me wonder -- do we have the curse of dimensionality in those bounds? I guess, R can be varied to improve this dependency but what is final dependency in bounds on dimension? If this is exponential, this will somewhat limit applicability of the results, at least, make them good for low dimension setting but for high-res diffusion models dimension is enormous and, hence, might not be something that explains performance of diffusion models.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors analyzed score estimation with neural network parameterization.

### Strengths
The paper proposes a novel design that is a network-based parametrization for score estimation. 
They tackled three difficulties in traditional supervised learning. 
Their work built a connection between score matching and regression analysis.

### Weaknesses
This work's primary limitation lies in its focus on theoretical analysis within a constrained setting. Specifically, the study is confined to a two-layer fully connected network (FCN) trained using gradient descent (GD). While this provides a starting point, it raises concerns about the generalizability of the findings to more complex and widely used architectures in score estimation. The analysis, while rigorous, might not fully capture the intricacies and challenges encountered when training deeper networks or employing different optimization algorithms commonly used in practice. Furthermore, the theoretical nature of the study, although valuable, could benefit from more empirical validation to strengthen the practical implications of the derived results.

### Questions
Can this analysis be extended to other architectures, let’s say, transformers?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper establishes a mathematical framework to analyze the accuracy of score estimation using neural networks trained by gradient descent. It introduces a parametric form for the denoising score-matching problem as a regression problem with noisy labels. The study demonstrates that, with a well-designed neural network, the score function can be accurately approximated, and it provides the first generalization error bounds for learning the score function in the presence of noise in observations.

### Strengths
This paper addresses a significant question: Can a neural network trained via gradient descent effectively learn the score function? This study has the potential to make a substantial impact on the deep learning community.

The paper introduces a framework for analyzing the convergence and generalization of neural networks trained using gradient descent for score-based generative models. In particular, the authors investigate the relationship between minimizing the score-matching problem (as defined in equation 5) and training neural networks (as defined in equation 8). The authors demonstrate that, under conditions of overparameterization, where the neural networks are sufficiently wide, minimizing the score-matching problem is equivalent to training the neural networks to directly learn input samples or images, as stated in Theorem 3.9 and Theorem 3.10.

### Weaknesses
1. The analysis strategy and framework presented in this paper do not entirely convince me. The primary contribution lies in establishing a connection between stochastic optimization (as defined in equation 5) and deterministic optimization (as defined in equation 8). Once this connection is made, the convergence and generation results appear as corollaries drawn from existing literature. Additionally, this connection is also not new, as it was proposed in [1].
2. Building upon the first point, the results concerning convergence and generalization in this paper can be considered incremental, as they rely on NTK-type analysis, which is identical to previous work in the literature and does not introduce novel insights. The application of NTK analysis, while technically sound, does not provide a fundamentally new understanding of the problem. The core argument hinges on the equivalence between the score-matching objective and a regression problem, which, once established, leads to standard NTK results.
3. However, if one were to directly analyze or train the stochastic optimization in equation 5, the results would likely differ significantly, even when employing NTK-type analysis. This is because, in this case, the NTK would encapsulate randomness arising from the Brownian motion. The current analysis bypasses the inherent stochasticity of the score-matching problem by focusing on a deterministic surrogate, which may not fully capture the dynamics of the original problem.
4. It's important to note that this work is purely theoretical and lacks empirical experimentation to validate its assumptions, such as Assumption 3.2, Assumption 3.4, Assumption 3.5, Assumption 3.7, Assumption 3.8, and Assumption 3.11. While these assumptions might seem reasonable, their practical implications and the degree to which they hold in real-world scenarios remain unclear without experimental verification. For example, the assumption of a bounded support (Assumption 3.2) is often violated in practice due to the presence of outliers or heavy-tailed distributions.
5. The authors categorize errors into four parts: coupling, label mismatch, early stopping, and approximation. Without conducting numerical experiments, it becomes challenging to determine which error contributes the most. As a result, this work does not provide substantial practical insights. The theoretical analysis provides bounds, but it does not offer any guidance on how to minimize these errors in practice or which error term is the most dominant in a specific setting.

### Questions
See weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
