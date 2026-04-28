# Stable-Transformer: Towards a Stable Transformer Training

- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
The scale of parameters in Transformers has expanded dramatically—from hundreds of millions to several trillion. A key challenge when scaling the model to trillions is the training instability. Although many practical tricks, such as learning rate warmup, query-key normalization and better weight initialization, have been introduced to mitigate the training instability, a rigorous mathematical understanding of why such instabilities happen and why the above-mentioned tricks work well is still unclear. In this paper, we give a theoretical analysis of the initialization, normalization and attention mechanism in Transformers, and present a set of stabilized designs of the initialization, normalization and attention mechanism, which are thus termed as StableInit, StableNorm and StableAtten, individually. In experiments, we demonstrate that each of our stabilized designs, i.e., StableInit, StableNorm and StableAtten, exhibits better stability. Furthermore, by putting the stabilized designs together, we propose a stabilized Transformer, termed Stable-Transformer, and show in experiments on large model (1B parameters) and deep model (200 layers) that our proposed Stable-Transformer
achieves a more stable training process.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes theoretical and experimental approaches to improve the training stability of Transformer models. To address the instability issues arising from the expansion of parameters in large-scale Transformers, the authors introduce new initialization (StableInit), normalization (StableNorm), and attention mechanisms (StableAtten). These three techniques are combined to form a "Stable-Transformer," which the authors demonstrate experimentally to improve training stability and performance.

### Strengths
Theoretical Contribution: The paper provides a theoretical analysis of the training instability in Transformers and proposes improvements to initialization, normalization, and attention mechanisms to address this instability. This is a significant contribution to the understanding and enhancement of Transformer model training.

Novel Stabilization Techniques: The authors propose StableInit, StableNorm, and StableAtten to stabilize the initialization, normalization, and attention mechanisms, respectively. By combining these, the authors offer a comprehensive solution to stabilize the entire Transformer architecture.

### Weaknesses
Lack of Scalability Validation for Large Models: While the paper provides a theoretical foundation and experimental validation of the stabilization techniques, it lacks empirical testing for scalability to larger models, such as massive language models. Specifically, the experiments do not demonstrate the effectiveness of the proposed methods on models with billions of parameters, which is a crucial aspect for practical applications in large-scale machine learning.
Implementation Complexity of StableNorm and StableAtten: The proposed techniques, StableNorm and StableAtten, require additional hyperparameter tuning, which may increase implementation complexity. The paper does not provide sufficient guidance on how to choose these hyperparameters, making it difficult to apply these methods in practice. The need for additional tuning could limit the practical applicability of these methods in real-world scenarios, especially given the computational cost of hyperparameter search.
Limited Experimental Scope: The experiments are limited to GPT and ViT, with no validation across a broader range of Transformer architectures or real-world applications. This raises questions about the generalizability of the proposed stabilization techniques. The absence of experiments on other Transformer variants, such as BERT or T5, and on diverse datasets, makes it difficult to assess the robustness of the proposed methods.

### Questions
see weakness

### Soundness
2

### Presentation
2

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
The paper introduces several techniques to stabilize transformer training: StableInit, StableNorm, and StableAtten, which replace Xavier initialization, LayerNorm, and Attention, respectively. For each component, the authors first identify limitations in previous methods and key factors contributing to stability, then propose the solutions. They provide theoretical analyses and experimental validation of each technique on GPT2-S and ViT backbones, demonstrating improved training stability over baselines. Additionally, the supplementary materials show that these stabilization techniques enable training with larger learning rates.

### Strengths
1. The authors identify instability issues in each vanilla module when training large models and propose insights to address them.

2. Experiments on GPT and ViT verify that the proposed approaches enhance training stability, with each experiment and theoretical analysis supporting the stability claims.

3. The authors demonstrate that these methods enable the network to tolerate larger learning rates.

4. The paper is well-written, with a clear structure that makes it easy to follow.

### Weaknesses
1. While each method contributes to improved stability, the gains from each proposed module are incremental. It would strengthen the argument to demonstrate that alternative methods, such as enforcing Lipschitz continuity in normalization [1], cannot replace each proposed module (e.g., showing that StableNorm outperforms other normalization techniques). Comparing the proposed methods with alternative stability techniques, rather than just naive baselines, would be more compelling. How does StableNorm compare to other recent normalization techniques like DeepNorm? And how does StableAtten compare to L2 Self-Attention [2]? Specifically, the comparison should include a detailed analysis of the computational overhead and the convergence rate of the proposed StableNorm versus DeepNorm, as well as a comparison of the performance of StableAtten with L2 Self-Attention when the query and key projection matrices are distinct, which is a common scenario in practice.

2. Although these methods make training more stable and tolerant of larger learning rates, the authors do not present other potential benefits of stable training. Emphasizing the importance of stability improvements would strengthen the argument. Does improved stability benefit generalization, lead to faster convergence, or improve performance on out-of-distribution data? It would be beneficial to see experiments that explicitly measure the generalization gap, training time, and performance on datasets with distribution shifts, such as CIFAR-10-C and CIFAR-100-C, to quantify the benefits of the proposed stabilization techniques beyond just training stability and tolerance to larger learning rates.

3. It would be valuable to test stability across an increasing number of layers and demonstrate whether improved stability benefits downstream tasks or enhances robustness to sample or label noise. Can the proposed techniques enable training with more layers, such as 200 or 1000 layers? Does improved stability benefit fine-tuning ViT for image classification on smaller datasets like CIFAR-10/100, or make it more robust to distribution shifts, such as on CIFAR-10-C and CIFAR-100-C? Furthermore, it would be important to evaluate the performance of the proposed methods on a wider range of downstream tasks, including those beyond image classification and language modeling, to assess their general applicability.

### Questions
Please see the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper is motivated by the observation that a rigorous mathematical understanding of why training instabilities occur in transformers—and why current stabilization techniques work—is still lacking. To address this, the authors provide a theoretical analysis of transformer initialization, normalization, and attention mechanisms, proposing a set of stabilization methods for each. Experimental results show that these individual stabilizations enhance training stability. Furthermore, by combining these approaches, the authors introduce a new model, the Stable-Transformer, which demonstrates a more stable training process in experiments.

### Strengths
1.  The paper is well-organized and clearly articulated. The problem statement, proposed solution, and experimental results are presented in a logical and accessible way. The figures and diagrams effectively illustrate the key concepts and findings. 
2.  The paper holds significant value as it thoroughly analyzes the instability issues associated with training transformers. It also introduces a stabilized model, the Stable-Transformer, and demonstrates through experiments that this model achieves a more stable training process.
3. The proposed method is firmly based on robust theoretical analysis. The mathematical formulation and proofs are clearly articulated and well-supported.

### Weaknesses
Overall, I'm satisfied with this paper and its core contributions. Other minor concerns/suggestions are listed as follows:

Have the authors considered assessing Stable-Transformer on large multi-modal models such as CLIP or Flamingo? Evaluating these models could showcase the wider applicability of the proposed stabilization techniques beyond just language and vision transformers.

### Questions
Considering the encouraging outcomes with GPT and ViT models, what do the authors identify as the key next steps for validating and enhancing Stable-Transformer? Are there specific challenges you foresee in implementing these techniques on larger models or different modalities?

### Soundness
4

### Presentation
4

### Contribution
4
