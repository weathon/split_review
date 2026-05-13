# Structured-Initialization Learning

- Decision: Reject
- Scores: 6, 6, 8

## Abstract
The emergence of large language models (LLMs) has revolutionized natural language processing, but their development and deployment face significant challenges in computational resources and environmental sustainability.
Traditional self-supervised learning (SSL) paradigms requiring extensive computational infrastructure and exhibiting slow convergence rates, leading to increased energy consumption and longer training durations.
While existing model fine-tuning techniques such as Low-Rank Adaptation (LoRA) are resource-intensive and fail to facilitate swift knowledge updates when integrating a mount of new data in model version iteration.
To mitigate these challenges, we introduce Sail, a novel method for accelerating the training of neural network models by leveraging knowledge from (publicly available) pre-trained models.
Our approach comprises two key components: (1) a parameter transformation technique that adjusts the dimensions of pre-trained model parameters to match the target architecture, and (2) a proximal parameter integration and retraining strategy that efficiently combines transformed parameters to initialize new models.
We formalize the concept of Proximal Parameter and provide theoretical guarantees for its convergence advantages.
Our approach achieves substantial reductions in training time and computational resources while maintaining or improving model performance on downstream tasks.
These results indicate that Sail provides a promising direction for the more efficient and accessible development of the deep learning community.
Our code will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents SAIL, a method to accelerate training by leveraging knowledge from pre-trained models using a structured initialization approach. It introduces a parameter transformation technique to adapt pre-trained model dimensions to the target architecture, alongside a proximal parameter integration strategy. Theoretical guarantees show the benefits of using transformed pre-trained parameters for faster convergence compared to random initialization as well as the guidance on obtaining the optimal parameters in the integration strategy. Experimental results across NLP and computer vision tasks confirm that SAIL reduces training time while improving model performance, supporting the efficacy and broad applicability of structured initialization for efficient large model training.

### Strengths
1. This paper offers strong motivation for addressing the challenges of efficient model initialization by harnessing pre-trained models, making a compelling case for its approach.
2. Rigorous theoretical analysis and effective visualizations are used throughout, solidly supporting the paper’s claims and enhancing interpretability.
3. Extensive experiments demonstrate that SAIL significantly outperforms random initialization, highlighting its effectiveness in reducing training time and improving model performance.

### Weaknesses
1. A major concern is the limited comparison with related methods. This paper’s approach aligns closely with areas like model reuse/expansion and model merging, both mentioned in the related work. Model expansion combined with proximal parameter integration or parameter transformation with model merging could potentially address the problem posed here. A comparison with methods from these areas would provide a more comprehensive evaluation of SAIL’s efficiency.

2. The paper lacks discussion on the gap between its linear model theory and real-world application, which is crucial to understanding SAIL's limitations. For instance, it would be beneficial to clarify practical computation of $\gamma^*$ and address situations where the required data isn’t available—a common issue with open-source models that often lack access to original training data. Furthermore, the theoretical claims regarding faster convergence should be more carefully stated, acknowledging the probabilistic nature of the guarantees and the potential for the initial advantage to diminish over iterations. The current presentation implies a deterministic improvement, which is not fully supported by the theory.

### Questions
1. How do the authors justify the claim in lines 268-269 based on Theorem 2?

### Soundness
3

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
This paper proposes Structured-Initialization Learning (SAIL), a method to accelerate training for large models by reusing parameters from pre-trained models. The approach includes transforming parameters to fit the target model and integrating them to form a more optimal starting point for training, reducing the need for random initialization.

### Strengths
1. The paper provides a solid theoretical analysis, effectively demonstrating how the proposed Proximal Parameter initialization leads to faster convergence. The authors present well-structured convergence theorems, lending strong support to the efficacy of SAIL in reducing training time and improving efficiency.
2. The method is tested on both NLP and computer vision tasks, demonstrating applicability across different domains and model architectures.

### Weaknesses
1. **Limited Novelty in Leveraging Pre-trained Models for Initialization** The proposed method of reusing parameters from pre-trained models to accelerate the training of new models is similar to existing work [1-2]. While the paper introduces a parameter transformation, it's not clear how this differs fundamentally from existing methods that also adapt pre-trained weights for new architectures. The core idea of transferring knowledge through weight initialization is not novel, and the paper needs to better articulate its unique contribution beyond incremental improvements.
2. The motivation and system design of Figure 1 claims to use a pre-trained model such as LLM, however, the actual experiments are conducted by training the model from scratch on small-scale datasets in a controlled setup. This discrepancy between the stated motivation and the experimental setup undermines the practical relevance of the findings. It would be more convincing to demonstrate the method's effectiveness using actual pre-trained models and larger datasets, as this would better reflect real-world scenarios.
3. The explanation of how the parameter transformation is conducted is not clear enough, the authors mentioned the random projection and learnable methods, but a detailed investigation and experiments on which method is better are not included. The paper lacks a thorough analysis of the impact of different transformation techniques on the final performance. Without a clear understanding of the trade-offs between these methods, it's difficult to assess the robustness and generalizability of the proposed approach.

### Questions
1. Could the author provide the training curves of the NLP experiments as shown in the CV experiments, it helps to verify if the proved fast convergence is also applicable to transformer training.

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
This paper proposed a novel way to combine the weights of multiple pre-trained LLMs into a smaller model. The problem to be addressed is important, as it offers opportunity to train a smaller specialized model faster, rather than train from scratch. 

The paper proposed a set of theorems support it's claims, which offers theoretical guarantees.

### Strengths
- This paper supports its claims with both theoretical and empirical results. The proposed theorems are proved in the appendix, which looks correct (without in-depth review)

- This paper address an important problem of LLM reusing, which lacks efficient solutions before. The proposed method seems to be better than naive averaging weights.

- This paper marks different theorems and labels in color, which helps readers to quickly locate and navigate.

### Weaknesses
 - The field of knowledge distillation should be discussed in the related works section, which is highly related.

- The use of colored block seems to be too extensive, which is not common in research papers. Though not an outstanding weakness point.

### Questions
- Why is there a spike at $\gamma=0.5$? 

- Are you assuming all other network elements are the same, e.g. activation functions, vocabulary size?

- Better to add discussion about knowledge distillation.

### Soundness
3

### Presentation
3

### Contribution
3
