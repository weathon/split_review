# An Online Learning Approach to Prompt-based Selection of Generative Models

- Decision: Reject
- Avg Score: 5.33
- Scores: 6, 5, 5

## Abstract
Selecting a sample generation scheme from multiple text-based generative models is typically addressed by choosing the model that maximizes an averaged evaluation score. However, this score-based selection overlooks the possibility that different models achieve the best generation performance for different types of text prompts. An online identification of the best generation model for various input prompts can reduce the costs associated with querying sub-optimal models. In this work, we explore the possibility of varying rankings of text-based generative models for different text prompts and propose an online learning framework to predict the best data generation model for a given input prompt. The proposed framework adapts the kernelized contextual bandit (CB) methodology to a CB setting with shared context variables across arms, utilizing the generated data to update a kernel-based function that predicts which model will achieve the highest score for unseen text prompts. Additionally, we apply random Fourier features (RFF) to the kernelized CB algorithm to accelerate the online learning process and establish a $\widetilde{\mathcal{O}}(\sqrt{T})$ regret bound for the proposed RFF-based CB algorithm over T iterations. Our numerical experiments on real and simulated text-to-image and image-to-text generative models show RFF-UCB performs successfully in identifying the best generation model across different sample types.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes to study a novel problem: generative model selection based on the given prompt and proposes a contextual-bandits-based algorithm to achieve sub-linear regret. Empirical results show that this method is effective in choosing the best model for each prompt.

### Strengths
1. The formulation of generative model selection based on a given prompt using contextual bandits is clear to me. The choose of bandits algorithm is well motivated.

 2. The presentation is clear to me.

### Weaknesses
1. This paper did not include enough discussion on the existing works that use bandits algorithm to solve the selection of prompts/models. Two examples are [1,2]. More discussion on this is needed to position this work.

2. The experimental results seem to be weak since the author only compare with the method proposed in this paper not use any other existing methods. An intuitive approach will be random selection (i.e., selecting the models randomly in the proposed algorithm, instead of using UCB).

3. The theoretical results seem to be standard. The regret of kenerlized bandits/contextual bandits has already shown in many bandits works and the use of RFF to approximate the kernel regression process is also standard since it is heavily used in previous work. My recommendation is that if there are novelty in the proof, please specify. If not, I think the theories in main paper seem to be redundant and can be removed to focus more on empirical insights.

### Questions
see weakness

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, the authors work on selecting the optimal generative model for various text prompts, as different models may perform better on different types of prompts. They propose an online learning framework that utilizes a kernelized contextual bandit (CB) approach to dynamically predict the best generative model for each prompt. The proposed method, Shared-Context Kernel-UCB (SCK-UCB), updates a kernel-based function using observed prompt-model performance data to iteratively refine the model selection based on expected scores. To reduce computational demands, the authors introduce a variant with random Fourier features (RFF-UCB), which approximates SCK-UCB’s performance while lowering the computational complexity per iteration from cubic to linear time. The proposed framework is tested on tasks such as text-to-image generation and image captioning.

### Strengths
By adapting the kernelized contextual bandit framework for prompt-based selection, the authors introduce a method that dynamically identifies the best generative model according to prompt type, partially addressing the challenge of variable model performance across prompts. Further, the integration of random Fourier features (RFF) into the SCK-UCB algorithm significantly reduces computational complexity from cubic to linear time, enhancing the framework’s feasibility for real-world applications with constrained resources, all while maintaining high performance.

### Weaknesses
1. Although the RFF-UCB variant improves computational efficiency, the scalability of the proposed framework may still be limited in settings with a large number of prompts and models. The performance of SCK-UCB and RFF-UCB should be further explored under such conditions to determine their practical scalability in applications with larger datasets. Specifically, the linear time complexity achieved by RFF-UCB is with respect to the number of random features, which itself can grow with the complexity of the input space, potentially negating the efficiency gains if a large number of random features are required to accurately approximate the kernel. Furthermore, the memory requirements for storing the kernel matrix, even in its approximated form, could become a bottleneck when dealing with a very large number of prompts and models, which is a common scenario in real-world applications.

2. The manuscript briefly mentions selecting hyperparameters involved in the proposed method, such as the exploration parameter and kernel function. However, the authors might consider including a more detailed ablation study on hyperparameter sensitivity, which would provide insights. For instance, if the performance does not significantly depend on the hyperparameter, the robustness of the proposed method is then empirically supported. On the other hand, if the performance is sensitive to the hyperparameter, a detailed implementation of the hyperparameter selection would be beneficial. This is particularly important for the kernel parameters, such as the bandwidth in the RBF kernel or the degree in the polynomial kernel, as these parameters can significantly influence the model's ability to capture the underlying relationships between prompts and model performance. A lack of robustness to these parameters could limit the practical applicability of the proposed method.

### Questions
How does the framework handle cases where new generative models or prompt types are introduced after initial deployment? It remains unclear whether the proposed algorithms can adapt to or efficiently incorporate new options without retraining from scratch, which could be critical in certain applications.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the contextual bandit problem of selecting the best image generation models given input prompts. The work is motivated by the fact that existing work aims to identify the model that maximizes the average evaluation score across data, while picking different models for each input text may improve the evaluation metrics as different image models can work well on different prompts. For methodology, the paper adopts kernelized contextual bandits (CB) with random Fourier features (RFF) from the existing literature on contextual bandits.

### Strengths
- **The problem of selecting models per prompt is well-motivated.**

The idea of selecting different models for each input text rather than using a single model for the entire data is explained well. The illustrative example in Figure 1, which shows that the superiority of two models can change with two types of images, also nicely highlights the existing issues. 

- **Experiments on real data.**

The experiments are conducted using two image generation models. It is good that the performance is verified on real data, not only the synthetic data with noises.

### Weaknesses
 - **Is linear bandits really infeasible in this setting (i.e., is kernel CB is needed)?**

The paper argues that the paper proposes kernel CB because "the relationship between the prompt vector and score is often highly non-linear and generator-dependent". However, when using the clip score, I could not agree with this statement because the clip score can be (nearly) explained with the linear model as $s = \max ( 0, 100 \cdot cos(v_x, c_y) ) = \max ( 0, 100 \cdot v_x^{\top} c_y )$ when using the normalized
embeddings of the text ($v_x$) and image ($c_y$). While we have the max operator, unless $v_x^{\top} c_y$ is negative for all models, we can choose the best arm by $s' = v_x^{\top} c_y$. Moreover, even when each model $a$ has stochastic generation process of the image $y$, we can estimate the average score of $s$ as $\mathbb{E}[s|a] = v_x^{\top} (\mathbb{E}[c_y|a])$, where $(\mathbb{E}[c_y|a])$ can be represented by a linear vector. I could not understand why general Lin-UCB does not work in this setting. The core issue is that while the CLIP score calculation involves a cosine similarity, the image embedding $c_y$ is itself a complex, non-linear function of the input text prompt $x$ and the specific generative model $a$. The paper does not adequately justify why a linear model would fail to capture the relationship between the prompt and the expected CLIP score for a given model, especially when considering the non-linear transformations within the image generation process itself. The argument that the relationship is non-linear is not sufficiently supported by the analysis of the CLIP score calculation.

- **Missing baselines in the experiments.**

The experiment section only compares the variants of the proposed algorithm, including kernel CB and random Fourier features (RFF). No other baselines, including Lin-UCB, is not compared, and it is not evident if the proposed method works better than the possible baselines. The lack of comparison to a standard Lin-UCB algorithm is a significant oversight. Without this comparison, it's impossible to determine whether the added complexity of kernel methods is actually necessary or if a simpler linear approach would suffice. Furthermore, the paper does not include a direct comparison to a simple greedy approach that always selects the model with the highest average CLIP score, which would serve as a basic performance benchmark. The absence of these essential baselines makes it difficult to assess the true value of the proposed method.

- **Quality of writing.**

I realized some key components are not explained in the main text, making it hard to understand the proposed idea deeply. For instance, what is the difference between SCK-UCB-lin and SCK-UCB-poly? Also, what are the findings from the experiment section? It seems that the superiority among the compared methods changes with the experiment setting, but what affects the experiment results, and which algorithm we should use in practice (i.e., the experiment sections only report the results and lack the discussion)? The paper needs to address these questions in the main text. Also, the following are several small issues in the text, and I highly recommend restructuring and proofreading the paper once again.

[nits]

- Section 3.2; I guess $s$ refers to the evaluation score, but this variable is not formally defined.
- Remark 1; the sentence is not complete (end with "the")
- outcome-the-best (O2B); I think the definition is a bit ambiguous. I guess the "best individual model" refers to using a single model across the whole data, but I initially thought this was the best model chosen for individual inputs, i.e., I thought this was referring the regret at first.

### Questions
- How does the proposed method perform compared to Lin-UCB?

- What are the findings from the set of experiments?

- How are SCK-UCB-lin and SCK-UCB-poly different to each other?

- Empirically, how does the computation time differ among the methods?

### Soundness
2

### Presentation
1

### Contribution
2
