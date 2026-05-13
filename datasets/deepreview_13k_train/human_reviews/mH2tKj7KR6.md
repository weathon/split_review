# The Discretization Complexity Analysis of Consistency Models under Variance Exploding Forward Process

- Decision: Reject
- Scores: 3, 6, 3, 5

## Abstract
Consistency models, a new class of one-step generative models, have shown state-of-the-art performance in one-step generation and achieve competitive performance compared to multi-step diffusion models. The most challenging part of consistency models is the training process, which discretizes the diffusion process and trains a consistency function to map any point at any discretized timepoint of the diffusion process to the data distribution. Despite the empirical success, only a few works focus on the discretization complexity of consistency models. However, the setting of those works is far away from the empirical consistency models with good performance, suffers from large discretization complexity, and fails to explain the empirical success of consistency models. To bridge the gap between theory and application, we analyze consistency models with two key properties: (1) variance exploding forward process and (2) gradually decay discretization stepsize, which are both widely used in empirical consistency models. Under the above realistic setting, we make the first step to explain the empirical success of consistency models and achieve the state-of-the-art discretization complexity for consistency models, which is competitive with the results of diffusion models. After obtaining the results of the one-step sampling method of consistency models, we further analyze a multi-step consistency sampling algorithm proposed by \citet{song2023consistency} and show that this algorithm improves the discretization complexity compared with one-step generation, which matches the empirical observation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the theoretical aspect of consistency models with VESDE forward process and EDM discretization scheme. The discretization complexity to achieve a small error in Wasserstein distance is studied. Multi-step sampling is proven to improve the discretization complexity.

### Strengths
1. This paper studies the consistency model with variance exploding forward process and decaying stepsize, which are both widely used empirically;
2. Multistep sampling as an iterative sampling procedure to reduce error is studied.

### Weaknesses
1. The main result heavily depends on $L$, the Lipschitz constant of the exact consistency function $f^{ex}$. According to the equation in line 689 and 701, the reverse beginning error (first term in Line 669) is bounded by $L\cdot R$, where $R$ is the radius of the support of the target distribution. As a result, when $L = \Omega(1)$ the result becomes meaningless since $R$ is the largest error possible. There are some discussions in line 342-348 regarding the $L$, but I'm not sure if I understand them correctly. In particular, 
  - could you please provide a detailed derivation to obtain the equation in line 342 using eq 3 of Karras et al.? Why does the exact consistency function minimize the $L2$ error in eq 2?
  - I think the equation in line 345 implies $|\nabla f|| \le 1 + R^2/\sigma^2$. The constant $1$ will make Theorem 1 meaningless. The reverse beginning error is then bounded by $(1 + R^2/\sigma^2) R$ following the steps in line 689 and 701. Since a trivial mapping as simple as $f(x,t) = 0, \forall x,t$ already achieves $W_2 \le R$, the main result becomes meaningless.
  - could you please provide an example on how the current result apply to multimodal distributions, like Bernoulli distribution or Gaussian mixture? A phase transition in the consistency function is anticipated, i.e. a threshold to map the noise to different modes. Will the consistency function have a large Lipschitz constant around such a threshold?

2. Why the analysis was limited to 2 steps? Are there specific technical challenges in extending to more steps? is there a further improvement when sampling with 3 steps?

### Questions
Could you provide a step-by-step derivation on the application of Gronwall's inequality in line 874 - 882?

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
1

### Summary
This paper differentiates itself by bridging the gap between theory and practice in consistency models, which hasn’t been fully addressed in previous research. While earlier works often relied on a variance-preserving forward process (VPSDE) and uniform step sizes for noise injection, these setups don’t align with the high-performing configurations used in practice. Real-world consistency models instead use a variance-exploding forward process (VESDE) and an EDM (exponential decay model) discretization scheme, where the step size starts large and gradually decreases, making sampling more efficient and accurate. By focusing on these practical settings, this paper provides a theoretical foundation that explains the empirical success of consistency models, shedding light on why these design choices lead to strong results in real applications.

### Strengths
The paper provides a well-written background on consistency models, highlighting what differentiates them from diffusion models and clearly explaining the motivation for this study—namely, that previous theoretical work does not align with practical design choices that lead to optimal performance. The supplementary materials offer essential background information, enhancing the paper’s completeness.

### Weaknesses
Although the paper is theoretical in nature, it includes several empirical claims—such as the assertion that previous work does not operate in a realistic setting, or that the results are superior to those of other generative models and theoretical approaches. These claims should ideally be supported within the paper by empirical evidence to strengthen their validity. Specifically, the paper mentions that previous theoretical work does not align with practical design choices, but it does not provide concrete examples of these discrepancies. For instance, the paper should detail how the variance-preserving forward process (VPSDE) and uniform step sizes used in prior theoretical analyses differ quantitatively from the variance-exploding forward process (VESDE) and EDM discretization scheme used in practice. Furthermore, the claim of superior results needs to be substantiated with specific metrics and comparisons to existing state-of-the-art generative models. Without this empirical backing, the theoretical contributions, while potentially significant, lack the necessary validation to fully support the paper's claims.

### Questions
What is defined as great performance? that term is repreated multiple times.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces a theoretical framework to analyze the discretization complexity of consistency models using a variance-exploding forward process (VESDE) and the EDM discretization scheme, both common in empirical models. Under these settings, the discretization complexity of consistency models can be significantly reduced, achieving results competitive with state-of-the-art diffusion models. Additionally, it examines a multi-step sampling approach to further improve the complexity, effectively reducing training requirements. The authors argue that their approach bridges the gap between theoretical analysis and practical performance, providing insights into why consistency models perform well empirically.

### Strengths
(1) The paper is to provide a theoretical analysis of consistency models under realistic conditions, specifically using the variance-exploding forward process (VESDE) and EDM discretization scheme. This aligns with empirical practice and closes the gap between theory and real-world applications.

(2) By analyzing the time-dependent Lipschitz constant and leveraging the EDM step size, the authors achieve a state-of-the-art discretization complexity that rivals diffusion models. This advancement reduces the computational cost of training and sampling in consistency models, making them more efficient for practical applications.

(3) The paper extends its contributions by analyzing multi-step sampling, showing that it can further reduce discretization complexity compared to one-step sampling. This added flexibility makes the method more adaptable to different use cases and aligns well with empirical observations.

(4) The paper provides a thorough comparison of discretization complexity across multiple methods, including diffusion and consistency models with various discretization schemes. This context helps to illustrate the unique benefits and performance of the proposed approach in relation to existing methods.

### Weaknesses
(1) Although the paper makes substantial theoretical contributions, it lacks empirical experiments to validate the practical impact of the proposed theoretical improvements. Real-world experiments are needed to demonstrate the actual effectiveness and robustness of the discretization complexity reductions across various datasets and tasks, such as image generation, where the benefits of reduced complexity should be clearly measurable in terms of training time and sample quality.

(2) The paper assumes an accurate enough approximated score function and consistency function without examining the practical challenges in achieving these accuracies. Since these assumptions are critical to achieving the proposed complexity bounds, this omission may limit the method’s applicability, especially in settings where training perfect consistency functions is difficult. The analysis does not address how sensitive the results are to deviations from these ideal conditions, which is a critical aspect for real-world deployment.

(3) While the method improves complexity theoretically, its actual scalability to very high-dimensional or large-scale datasets remains untested. For real-world applications like 3D reconstruction or high-resolution video generation, the computational gains may not fully offset the high resource demands, making scalability uncertain. The paper needs to address the practical limitations of applying this method to very large datasets, which may require distributed training or other specialized techniques.

(4) The paper’s reliance on parameters such as the EDM step size and Lipschitz constant suggests potential sensitivity to hyperparameter tuning. However, it does not offer extensive guidance on optimizing these parameters in practice, which could hinder reproducibility and performance consistency across different scenarios. The paper should include a sensitivity analysis of these parameters and provide practical recommendations for their selection.

(5) The paper’s assumptions, including time-dependent Lipschitz constants and bounded support, while theoretically sound, may not always hold in diverse, real-world data distributions. Such limitations could restrict the generalizability of the method, especially in multimodal distributions where these assumptions might break down. The analysis needs to discuss the implications of these assumptions and how they might affect the performance in more complex scenarios.

(6) The paper focuses on the consistency distillation paradigm, which requires pre-trained score functions. This reliance on pre-trained models may limit the standalone applicability of the approach, as obtaining high-quality score functions is often computationally intensive and may not be feasible for all applications. The paper needs to address the practical limitations of relying on pre-trained models and discuss alternative approaches for scenarios where such models are not readily available.

### Questions
This paper investigated consistency models with variance exploding forward process and gradually decay discretization step size, explaining the empirical success of consistency models and achieve the state-of-the-art discretization complexity for consistency models. After obtaining the results of the one-step sampling method of consistency models, they further analyze an existing multi-step consistency sampling algorithm and show that this algorithm improves the discretization complexity compared with one-step generation. The achieved discretization complexity consistency models have obtained competitive with the results of diffusion models. The detailed questions are listed below:
-	Could you provide experimental results or empirical evidence demonstrating the practical impact of your theoretical improvements on discretization complexity? Specifically, how do these theoretical gains translate to performance improvements in high-dimensional, real-world applications like image and video generation?
-	Given the critical role of an "accurate enough" score and consistency function in achieving the complexity bounds, how realistic are these assumptions in practice? What techniques or guidelines do you recommend ensuring that these accuracy conditions are met in real-world applications?
-	Can you discuss the scalability of the proposed framework when applied to very large or high-dimensional datasets? Have you tested the framework on computationally intensive tasks like 3D reconstruction, and if so, what performance gains or limitations did you observe?
-	Your method depends on parameters like the EDM step size and the time-dependent Lipschitz constant. How sensitive is the performance of the model to these hyperparameters, and what recommendations can you provide for optimizing them? Would adaptive methods for step size selection be viable here?
-	While EDM is effective in reducing complexity, did you consider alternative discretization schemes? Are there scenarios where EDM may not be the most optimal choice, and could other schemes, such as non-uniform steps with different decay patterns, offer additional benefits?
-	Your analysis relies on assumptions like bounded support and time-dependent Lipschitz constants. How robust is your approach if these assumptions do not strictly hold in a real-world context, particularly in multimodal or noisy datasets? Could your method be adapted to handle more flexible data assumptions?
-	The framework depends on consistency distillation, which requires a pre-trained score function. In applications where pre-trained score functions are unavailable or costly to obtain, is there a way to apply your framework effectively without a pre-trained model, or could you suggest an alternative training strategy?
-	Have you conducted any error analysis to identify cases where the model may misestimate the required discretization complexity or sampling steps? Understanding the types of samples or data conditions that lead to higher error rates could provide valuable insights into the robustness of your approach.
-	Given the theoretical nature of this work, what practical recommendations or guidelines can you provide to facilitate the deployment of your framework in production settings? Specifically, how can practitioners balance the theoretical complexity improvements with computational feasibility in time-sensitive applications?
-	What are the differences and connections between diffusion models and consistency models? In what ways, we need to consider consistency models instead of diffusion models and vice versa, such as generating samples in a single forward pass, which leads to much faster inference times compared to diffusion models?
-	What are the theoretical insights from Theorem 1? How does the generation error upper bound in Theorem 1 change when considering the introduced noise? All detailed proofs need to be moved in appendix and replaced by technical insights summarization.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This work studies the discretization complexity of consistency models trained from pre-trained score function, used in practice to reduce the computational burden of diffusion models that require many steps to generate samples.

### Strengths
* This work provides the first analysis of consistency distillation, under VESDE.
* Their complexity bound seems reasonable, compared with similar analysis conducted under difference assumption (on the reverse SDE).

### Weaknesses
 * I think that the manuscript could benefit from organization of the technical terms, for example by introducing an entire section with all the terms and definitions used in this analysis. Currently, many parts of the paper introduce their notation, which makes it hard to follow. Specifically, the definitions of key terms such as $q_0$, $s_\phi$, $\hat{Y}^{\phi}_{t_{k}}$, and $\boldsymbol{f}_{\theta}$ are not provided in the notation section, forcing the reader to search through the text. This lack of a comprehensive notation section significantly hinders the readability and understanding of the paper, especially given its technical nature.
* Minor: Table 1 is hard to read, and I believe captions should be above and not below the table.
* I would suggest that the authors would justify their assumptions and explain why these are reasonable assumption. In the current manuscript, the authors simply state other papers in which these assumptions were made (assumptions 3 and 4).
* The authors should refrain from evaluating their own work (remark 2: "our great results")
* the authors claim that they "why consistency models have competitive performance compared to diffusion models in application". I don't quite follow why this is the case? The complexity bound hold under certain assumptions that may not hold in practice. Can the authors please clarify this point?

### Questions
* the authors claim that they "why consistency models have competitive performance compared to diffusion models in application". I don't quite follow why this is the case? The complexity bound hold under certain assumptions that may not hold in practice. Can the authors please clarify this point?

### Soundness
2

### Presentation
1

### Contribution
3
