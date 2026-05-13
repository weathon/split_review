# Variational Bayesian Pseudo-Coreset

- Decision: Accept
- Scores: 8, 6, 8, 5

## Abstract
The success of deep learning requires large datasets and extensive training, which can create significant computational challenges. To address these challenges, pseudo-coresets, small learnable datasets that mimic the entire data, have been proposed. Bayesian Neural Networks, which offer predictive uncertainty and probabilistic interpretation for deep neural networks, also face issues with large-scale datasets due to their high-dimensional parameter space. Prior works on Bayesian Pseudo-Coresets (BPC) attempt to reduce the computational load for computing weight posterior distribution by a small number of pseudo-coresets but suffer from memory inefficiency during BPC training and sub-optimal results. To overcome these limitations, we propose Variational Bayesian Pseudo-Coreset (VBPC), a novel approach that utilizes variational inference to efficiently approximate the posterior distribution, reducing memory usage and computational costs while improving performance across benchmark datasets.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper presents the Variational Bayesian Pseudo-Coreset (VBPC) method, aimed at efficiently approximating the posterior distribution in Bayesian Neural Networks (BNNs). Given that BNNs face substantial computational challenges when dealing with large datasets due to their high-dimensional parameter spaces, VBPC provides a promising method. Traditional Bayesian Pseudo-Coreset (BPC) techniques have been proposed to alleviate these issues, yet they often struggle with memory inefficiencies. VBPC addresses this by leveraging variational inference (VI) to approximate the posterior distribution. This method achieves a memory-efficient approximation of the predictive distribution using only a single forward pass, which makes it appealing for computationally intensive applications.

### Strengths
The paper effectively utilizes variational inference to derive a closed-form posterior distribution for the weights of the last layer, thereby addressing some of the performance limitations observed in prior BPC approaches.
VBPC’s capability to approximate the predictive distribution in a single forward pass enhances both computational and memory efficiency, positioning it as a potentially valuable method for large-scale applications.

### Weaknesses
The experimental validation on practical application is limited.

While VBPC demonstrates improvement over some BPC baselines, its classification accuracy on benchmark datasets like CIFAR-10, CIFAR-100, and Tiny-ImageNet remains notably lower than that of state-of-the-art classifiers. This raises concerns about the practical competitiveness of VBPC in real-world applications, particularly in image classification tasks where accuracy is crucial. Could additional optimizations or refinements to the VBPC approach improve performance?

### Questions
- While VBPC demonstrates improvement over some BPC baselines, its classification accuracy on benchmark datasets like CIFAR-10, CIFAR-100, and Tiny-ImageNet remains notably lower than that of state-of-the-art classifiers. This raises concerns about the practical competitiveness of VBPC in real-world applications, particularly in image classification tasks where accuracy is crucial. Could additional optimizations or refinements to the VBPC approach improve performance?
- The current experiments may not adequately showcase the strengths of VBPC in relevant scenarios. To enhance the paper’s impact and applicability, I suggest conducting additional experiments in settings where VBPC’s efficiency gains could be more convincingly demonstrated.

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
3

### Summary
This paper proposes Variational Bayesian Pseudo-Coreset (VBPC), a novel approach to efficiently approximate posterior distribution in Bayesian Neural Networks (BNNs). Bayesian Neural Networks often face issues with largescale datasets due to their high-dimensional parameter space. To reduce the computational load, many Bayesian Pseudo-Coreset (BPC) methods have been proposed, but they suffer from memory inefficiencies. VBPC addresses these limitations by using variational inference (VI) to approximate the posterior distribution. Moreover, this paper provides a memory-efficient method to approximate the predictive distribution with only a single forward pass instead of multiple forwards, making the approach computationally and memory-efficient.

### Strengths
- This paper leverages the variational formulation to obtain the closed-form posterior distribution of the last layer weights, which resolves the issue of suboptimal performance seen in previous approaches.
- And, the method approximates the predictive distribution with only a single forward pass instead of multiple forwards, making the approach computationally and memory-efficient.

### Weaknesses
 - The experiment is not enough to illustrate the function of the algorithm.

 - The accuracy of these algorithms on cifar10, cifar100 and Tiny-Imagenet is too low. VBPC is effective relative to several existing BPC baselines, but the performance is significantly lower compared to existing state-of-the-art classifiers.
- In the field of image classification, at least the scenes you choose for classification, these experiments do not seem to show the advantages of your method convincingly. 
- Please try to provide some new experiments, in more convincing scenarios, to illustrate the practical application value of your method.

### Questions
- The accuracy of these algorithms on cifar10, cifar100 and Tiny-Imagenet is too low. VBPC is effective relative to several existing BPC baselines, but the performance is significantly lower compared to existing state-of-the-art classifiers.
- In the field of image classification, at least the scenes you choose for classification, these experiments do not seem to show the advantages of your method convincingly. 
- Please try to provide some new experiments, in more convincing scenarios, to illustrate the practical application value of your method.

### Soundness
3

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
3

### Summary
The paper studies the problem of core set extraction using Bayesian inference. The proposed solution builds on a two-stage variational inference scheme where the first stage is responsible for inferring the optimal core set while the second is to fit this core set to the full-scale data set at hand. The developed solution overarches the whole family of the distributions that belong to the exponential family.

### Strengths
- The paper is particularly well-written with a clearly defined problem scope and a solid solution methodology that follows a well-justified sequence of development steps,
- The proposed bilevel variational inference formulation is neat and sensible.
- The computational complexity analysis is indeed helpful to see the merit of the devised solution.
- The reported results are strong on the chosen group of data sets.

### Weaknesses
 - The paper motivates the core set extraction problem with use cases such as processing big data and addressing continual learning setups. However, the presented results are on data sets that can be considered in the present technological landscape as toy problems. I do symphathize the idea of prototyping. But given the strong applied component of the present work, I am still unconvinced about the generalizability of the observed scores to a case where coreset extraction is an actual necessity. The issue may be addressed during the rebuttal by showing results on a large enough data set used as a standard coreset extraction benchmark or a continual learning application.
- The need to use the Gaussian likelihood to avoid the need for an approximation stage is only partially convincing. It is an artiffact of choosing variational Bayes as the inference scheme, which is exogeneous to the problem anyway. Maybe this issue, linked to my first question below, will be clarified during the rebuttal.

### Questions
- Would Laplace approximation on the softmax likelihood be a better option than first choosing a variational inference scheme and then using a Gaussian likelihood? Laplace proves to be a powerful approach in Gaussian process classification.
- Is the claim of Manousakas et al. 2020 contrary to the main message of the paper? If correct, would this not undermine the significance of the proposed solution? If incorrect, why?
- Do we really lack an analytical solution or at least an EM-like algorithm where the E-step has an analytical solution when only the last layer of a neural net is probabilistic?
- What is the take-home message of Figure 1? I am missing to see a particular pattern there that helps motivate the proposed solution.

My initial score is a borderline as the paper has both certain merits and clear question marks. I am happy to consider significant score updates based on a convincing rebuttal discussion.

---
POST-REBUTTAL: The authors gave convincing answers to the above questions and they published additional results that demonstrate the advantages of the proposed method more clearly than the experiments reported in the original submission. I update my score to an accept.

### Soundness
3

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
4

### Summary
The paper titled “Variational Bayesian Pseudo-Coreset” introduces a novel method aimed at reducing the computational and memory challenges associated with large datasets in deep learning, particularly within the context of Bayesian Neural Networks (BNNs). The authors address limitations in prior methods of Bayesian Pseudo-Coresets (BPCs), which often face inefficiencies in memory usage and suboptimal results during training. They propose a new approach called Variational Bayesian Pseudo-Coreset (VBPC), which leverages variational inference to approximate the posterior distribution of model weights. The key innovation of VBPC is the use of a closed-form solution to compute the posterior for the last layer of BNNs, eliminating the need for complex gradient-stopping techniques used in previous BPC methods. This significantly reduces memory usage and computational load. Additionally, VBPC allows for more efficient training and inference by using a single forward pass for predictive distribution computation. Empirical evaluations demonstrate that VBPC outperforms existing BPC methods on benchmark datasets, showing improvements in both accuracy and negative log-likelihood metrics across various datasets, such as MNIST, CIFAR10, and CIFAR100. The paper contributes to the field by enhancing the efficiency and scalability of BNNs, particularly in environments that require handling large-scale data while maintaining the benefits of Bayesian inference.

### Strengths
The paper introduces a novel approach to improving the efficiency of Bayesian Neural Networks (BNNs) by combining variational inference with pseudo-coresets. This innovation is notable because it addresses the longstanding challenges in the field related to computational and memory inefficiencies when scaling BNNs to large datasets. The proposal of a closed-form solution for last-layer variational inference is a significant departure from prior methods that relied on more memory-intensive sampling-based approaches. By focusing on variational inference and pseudo-coresets, the authors provide an original contribution that builds on existing methods but removes key limitations such as memory usage and the reliance on gradient stopping.
The technical rigor of the paper is high, with well-founded theoretical development and comprehensive empirical evaluations. The authors derive closed-form solutions for coreset variational inference, addressing a critical computational bottleneck in Bayesian model averaging. Their empirical results, demonstrated across multiple datasets (e.g., MNIST, CIFAR10, CIFAR100), show significant improvements over existing BPC methods in terms of both accuracy and negative log-likelihood, which strengthens the quality of their proposed method. The paper also includes a variety of comparisons with competitive baselines, reinforcing the robustness and effectiveness of their approach.
The paper is clearly structured and provides sufficient background for readers to understand both the motivation and the details of the proposed method. The explanation of the problem, the limitations of prior work, and the step-by-step presentation of the VBPC approach are clear and easy to follow. The use of mathematical derivations is well-supported by intuitive explanations, making the complex variational inference approach more accessible. The inclusion of visual results and performance tables also contributes to clarity, helping readers visualize the practical benefits of VBPC.
The significance of the work lies in its potential to influence how BNNs are applied to large-scale data problems. By significantly reducing the memory and computational burdens of Bayesian model averaging, the proposed VBPC method makes BNNs more feasible for real-world applications, such as those in healthcare and climate analysis, where uncertainty estimation is critical. The method could have broad implications for other fields requiring scalable, probabilistic neural networks. Additionally, the ability to perform Bayesian inference with less computational overhead enhances the practicality of deploying BNNs in production environments.

### Weaknesses
The paper focuses heavily on benchmark datasets like MNIST, CIFAR10, and CIFAR100, which are common in academic research but may not fully represent the complexity of real-world problems. While these datasets help establish baseline performance, the paper would benefit from exploring more challenging, domain-specific datasets, particularly those that are more representative of practical applications in fields such as healthcare or finance. Expanding the evaluation to datasets that feature more variability and noise could demonstrate the method’s robustness in real-world settings, which is especially important given the paper’s goal of making Bayesian Neural Networks more feasible for large-scale applications.
Αlthough the paper demonstrates memory efficiency improvements, there is no extensive discussion of the scalability of the method when applied to very large datasets beyond those tested (e.g., ImageNet or even larger datasets in natural language processing). The paper could benefit from a more detailed analysis of the method’s behavior as the dataset size grows significantly. Additionally, the paper does not provide enough insight into the sensitivity of the method to hyperparameter choices such as the coreset size or the initialization of the model pool. It would be helpful to include an ablation study or sensitivity analysis that investigates how performance degrades with suboptimal hyperparameter choices and whether the method requires careful tuning to achieve competitive results.
While the paper emphasizes memory savings, it does not provide a thorough comparison of training times between VBPC and existing methods, particularly in scenarios with high-dimensional datasets. A more detailed analysis of wall-clock time or computational complexity across different hardware configurations (e.g., GPUs versus CPUs) would be useful. This would help practitioners better understand the trade-offs between memory savings and potential increases in computational time, especially when scaling to larger architectures and datasets.
The paper relies on the last-layer variational approximation to simplify the posterior calculation, but the limitations of this approach are not thoroughly discussed. While the paper suggests that this approximation performs comparably to more complex methods, it would be valuable to include a deeper investigation of when this approximation might fail, especially in models with deep architectures or tasks requiring fine-grained uncertainty estimation. A discussion on whether the approximation is sufficient in all use cases or only certain tasks (e.g., classification versus regression) would make the paper more transparent.
The paper demonstrates that VBPC can learn pseudo-coresets that effectively approximate the full dataset’s posterior, but it doesn’t provide much insight into the interpretability of these pseudo-coresets. For example, what are the learned coresets capturing in terms of dataset distribution or feature representation? A qualitative analysis, such as visualizing the pseudo-coresets or interpreting what aspects of the data they retain, would help reinforce the method’s effectiveness. Additionally, further explanation of how these pseudo-coresets evolve during training and contribute to Bayesian uncertainty could strengthen the narrative.
While the paper briefly touches on robustness to distributional shifts using CIFAR10-C, the evaluation of predictive uncertainty in real-world settings is somewhat lacking. It would be useful to see how VBPC handles more complex out-of-distribution (OOD) detection tasks or how well it captures uncertainty under adversarial conditions, which are critical aspects of Bayesian inference in high-stakes applications like healthcare. A more thorough evaluation in these contexts could elevate the practical relevance of the method.

### Questions
1. Scalability to Larger Datasets: How does VBPC perform when applied to much larger datasets, such as ImageNet or larger text datasets? Does the method scale well in terms of both computational efficiency and accuracy, or does it encounter bottlenecks?

2. Hyperparameter Sensitivity: How sensitive is VBPC to hyperparameters such as the number of pseudo-coresets, coreset size, and model initialization? Do suboptimal hyperparameter settings lead to significant performance degradation?

3. Computational Costs and Training Time: Can you provide a detailed comparison of training times and wall-clock time between VBPC and other methods, particularly Bayesian Pseudo-Coreset methods using SGMCMC? How does the computational time scale with increasing dataset size?

4. Limitations of the Last-Layer Approximation: Does the last-layer variational approximation hold up in deeper networks or more complex tasks such as regression? Have you observed any failure cases where this approximation does not capture enough uncertainty?

5. Interpretability of Pseudo-Coresets: What do the learned pseudo-coresets represent? Are they capturing key features of the original dataset, and if so, how do they evolve during training? Is there a way to interpret or visualize the coreset to provide better intuition about what is being distilled?

6. Generalization to Different Tasks: Can the VBPC method be applied effectively to tasks beyond classification, such as regression or other types of Bayesian inference? If so, how does the method adapt to these different problem types?

7. Robustness to Out-of-Distribution (OOD) Data and Adversarial Attacks: Does VBPC provide any robustness to adversarial attacks or strong distribution shifts beyond what is demonstrated with CIFAR10-C? How does the method perform in more severe OOD scenarios?

8. Memory-Efficient Loss Computation: How significant is the impact of memory-efficient loss computation during training in terms of accuracy or stability? Does it introduce any trade-offs in performance, particularly in very high-dimensional settings?

### Soundness
3

### Presentation
2

### Contribution
2
