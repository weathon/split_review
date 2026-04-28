# RAG-SR: Retrieval-Augmented Generation for Neural Symbolic Regression

- Decision: Accept
- Avg Score: 7.33
- Scores: 6, 8, 8

## Abstract
Symbolic regression is a key task in machine learning, aiming to discover mathematical expressions that best describe a dataset. While deep learning has increased interest in using neural networks for symbolic regression, many existing approaches rely on pre-trained models. These models require significant computational resources and struggle with regression tasks involving unseen functions and variables. A pre-training-free paradigm is needed to better integrate with search-based symbolic regression algorithms. To address these limitations, we propose a novel framework for symbolic regression that integrates evolutionary feature construction with a neural network, without the need for pre-training. Our approach adaptively generates symbolic trees that align with the desired semantics in real-time using a language model trained via online supervised learning, providing effective building blocks for feature construction. To mitigate hallucinations from the language model, we design a retrieval-augmented generation mechanism that explicitly leverages searched symbolic expressions. Additionally, we introduce a scale-invariant data augmentation technique that further improves the robustness and generalization of the model. Experimental results demonstrate that our framework achieves state-of-the-art accuracy across 25 regression algorithms and 120 regression tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a novel approach to symbolic regression based on neural-network based Retrieval Augmented Generation (RAG) and semantic descent (SD). The main idea is to dynamically construct a semantic library associating trees with their corresponding semantics (numerical evaluations of the tree). Semantic Descent starts from a set of initial trees and calculates the residual, i.e. the numerical error obtained from removing a specific tree from the original tree set. The goal of this step is to understand the contribution of the missing tree and replacing it with a new tree, possibly improving the residual. The proposal of a new tree is based on querying the semantic library with the residual and (optionally) refining such a tree with the prediction of a neural network conditioned on both the proposed tree from the semantic library and an appropriate encoding of the residual. A simple MLP is responsible for obtaining the latter encoding. A transformer encoder processes the tree extracted from the library and produces another embedding. The embeddings from the MLP and the transformer encoder are then concatenated and fed into a transformer decoder which in turn outputs the final proposed tree. The whole model is trained with online supervised learning. The library is dynamically updated with first-in-first-out queue mechanism. A data augmentation strategy is also proposed to improve the robustness of the model. Experiments are divided into two parts: first the model is evaluated on synthetic data and the various components of the model are ablated to quantify their relative importance and their contribution to the final running time; second the model is tested on the PLMB benchmark, resulting in very good results both in terms of accuracy and complexity.

### Strengths
- SR-RAG represents, to best of the reviewer knowledge, a novel method for symbolic regression combining techniques from the genetic programming literature and recent advances in neural networks. This combination is interesting as the two components have the potential to nicely address each other's limitations. In particular, the ablation studies seem to show that neural generation performs better than simple retrieval, suggesting that the neural network is benefitting the whole approach.

- Results are encouraging: the model performs very well in terms of R^2 score and complexity.

### Weaknesses
 - **Clarity of presentation could be improved**: I believe that the way the approach is presented should be made clearer. In particular, Fig. 1 is a bit hard to interpret and does not aid the reader understanding. In addition, I feel more details should be given on how the semantic library is populated and how the retrieval is performed given a residual.

- **I feel the way the neural network is trained is not explained in sufficient detail**: While the way the different neural network components are described is well done, I feel important details on their training are missing. In particular, I do not understand how the cross-entropy loss is used as it is not clear to me what the ground truth labels are and where they are taken from. In addition, more details about the online supervised learning training routine should be reported. I feel this is very important to precisely understand how to model is trained and to have an intuition of the overall complexity of the approach. I would appreciate if the authors could clarify these points.

- **Question on runtime**: RAG-SR performs relatively well in terms of training time, even though it incorporates neural networks and models are trained on CPU. I am wondering why possibly less complex models, exclusively based on GP techniques, perform comparably or worse in terms of runtime, despite not incorporating any neural network.

- **Question on complexity**: RAG-SR seems to perform well in terms of complexity, achieving a good trade-off between accuracy and complexity. I am wondering where this property comes from. Why does the model has a preference toward simpler expression. At which point of the model is this constraint imposed?

### Questions
See weaknesses section.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes RAG-SR, a retrieval-augmented generation framework for symbolic regression (SR) that utilizes a neural semantic library, semantic descent, and scale-invariant data augmentation to generate symbolic models effectively without pre-training. Through various experiments, the paper demonstrates that RAG-SR outperforms existing SR models, especially those relying on pre-trained language models, by producing interpretable and accurate symbolic expressions.

### Strengths
1. **Innovative Retrieval-Augmented Generation (RAG)**: The RAG mechanism effectively addresses the common issue of model hallucinations in SR tasks by incorporating relevant expressions from the semantic library. This approach is well-justified and experimentally validated, showing a significant positive impact on both the quality and relevance of generated models.

2. **Effective Feature Construction through Semantic Descent**: The proposed semantic descent strategy is a notable contribution that improves model refinement through selective feature replacement rather than addition, which helps maintain a compact and interpretable feature set while boosting accuracy.

3. **Data Augmentation and Double Query Strategy**: These techniques address the inherent challenges in SR by ensuring scale-invariance and robustness, with the double query strategy, in particular, effectively capturing symmetrical relationships in symbolic expressions.

4. **Strong Empirical Validation**: The paper demonstrates that RAG-SR achieves state-of-the-art results across diverse benchmarks, reinforcing the proposed method's efficacy. The study includes a well-structured comparison with relevant baselines, supporting claims of improved performance and interpretability.

### Weaknesses
1. **Complexity and Training Time Trade-offs**: While RAG-SR improves SR accuracy, the computational overhead from maintaining and querying the semantic library is a significant concern. The paper lacks a detailed analysis of how the size of the semantic library and the frequency of its updates impact training and inference times. For instance, how does the time complexity of querying the KD-Tree scale with the dimensionality of the semantic space and the number of stored expressions? Moreover, the strategy of selecting the top 50 most challenging instances every 10 generations, while effective, should be analyzed in terms of its impact on overall training time, especially when dealing with datasets that exhibit a high degree of variability in loss across instances.

2. **Limited Generalization to Non-SR Domains**: The paper primarily focuses on symbolic regression, which limits the method's applicability to other machine learning tasks. It would be valuable to explore the adaptability of RAG-SR to different types of regression or generative tasks. For example, could the semantic descent strategy be applied to feature selection in non-symbolic regression models? Additionally, how might the double query strategy be adapted for tasks involving sequential data or graph structures, where the concept of symmetry might manifest differently?

3. **Dependence on Hyperparameter Tuning**: The effectiveness of RAG-SR, particularly in terms of balancing the retrieval and neural generation probabilities, appears sensitive to hyperparameter choices. The paper does not provide a comprehensive sensitivity analysis of key hyperparameters like \( P_{\text{neural}} \) and \( \lambda \). For instance, how does varying \( P_{\text{neural}} \) affect the trade-off between exploration (neural generation) and exploitation (retrieval)? Similarly, how does the choice of \( \lambda \) impact the model's ability to learn meaningful representations in the semantic space, especially in the presence of noisy or redundant data?

4. **Interpretability of Generated Models**: Although RAG-SR aims to produce interpretable symbolic models, the paper lacks a quantitative analysis of interpretability. While the number of nodes in the symbolic tree is mentioned as a measure of complexity, it does not fully capture the nuances of interpretability from a domain expert's perspective. How does the complexity of models generated by RAG-SR compare to those generated by other SR methods, particularly in terms of the number of unique operators, the depth of the expression tree, and the presence of physically meaningful sub-expressions?

### Questions
1. **Explain Hyperparameter Choices and Sensitivity**: Could the authors provide more insights into the choice of hyperparameters, such as the probability $\( P_{\text{neural}} \)$ for neural generation versus retrieval, and the value of $\( \lambda \)$ for the contrastive loss term? A sensitivity analysis on these hyperparameters would be valuable for practical deployment.

2. **Computational Cost Analysis**: The results indicate increased computational costs with RAG-SR. Could the authors discuss how the computational demands scale with larger datasets? Are there specific optimizations for the semantic library or model architecture that could reduce inference times?

3. **Ablation on Data Augmentation and Double Query**: Data augmentation and double querying are innovative and appear to significantly contribute to the model's effectiveness. However, would these techniques still benefit RAG-SR in less structured or non-SR tasks? Clarifying this point would highlight the broader applicability of the approach.

4. **Comparison with Pre-trained Language Models**: While RAG-SR surpasses pre-trained models in SR tasks, does the method show robustness against varied functional distributions, especially in cases with substantial function overlap? A breakdown of results based on function novelty (seen vs. unseen functions) would deepen the insights into RAG-SR’s advantages.

5. **Interpretable Complexity Metrics**: Interpretability is a key focus in SR, yet model complexity is only briefly addressed. How does RAG-SR ensure a balance between interpretability and accuracy, especially as model complexity scales? Including complexity metrics or visualizations would substantiate claims on interpretability.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a novel approach to neural-guided symbolic regression. While prior work has focused on training generative models to directly produce new expression trees, such models often suffer from hallucination and struggle when faced with out-of-distribution data. In contrast, the authors propose training the generative model to produce a single feature at a time, rather than generating an entire expression tree. This approach aims to improve the model's performance on out-of-distribution problems. Additionally, the authors incorporate a prompting mechanism, feeding the model with relevant expression trees to help reduce hallucination.

The authors evaluate their method (RAG-SR) on a custom synthetic dataset and the no-noise version of SRBench. They find that RAG-SR outperforms other baselines on these task in terms of accuracy, size of the final equation, and speed.

### Strengths
- The general strategy of using a set of discrete latent codes for robustness is sound and widely acknowledged as beneficial in practical applications (e.g., VQ-VAE, discrete World Models, etc.).
- The paper is well written with great figures.

### Weaknesses
 - **Clarity**: Many related ideas exist within the broader community, and while they may not necessarily be weaknesses, these papers should be discussed in the related work section:

  - VQ-VAE (https://arxiv.org/pdf/1711.00937): This paper from the representation learning community learns a discrete latent representation (a _codebook_). The authors might benefit from reviewing this work. I believe the manuscrpt is more closely tied to "learning a discrete representation for neural guided symbolic regression" rather than "retrieval augmented generation." Regardless, I highly recommend adopting the nomenclature in this paper to increase comprehensiveness. This technique has also been applied in synthesizing general-purpose programs (https://arxiv.org/pdf/2012.00377), a comparision with this work would be useful.

  -  Since this work is heavily influenced by work in retrieval augmented generation, it would be useful to include a discussion on how the authors think their work is connected/influenced by work in RAG (https://arxiv.org/pdf/2406.14497) and how it's different from current work that uses RAG for code generation (https://arxiv.org/pdf/2108.11601, https://arxiv.org/pdf/2407.19619).


Regardless, I believe the authors have adequately demonstrated that this is novel and performant algorithm for symbolic regression. As such, I am in favor of accepting this paper.

 - L71: "pretraining free supervised learning:" I'm a bit confused by this phrase. Isn't pretraining, as used colloquially in NLP, a self-supervised learning strategy? Under this definition, all supervised learning algorithms should always be "pretraining free." Consider replacing this phrase.
- L103: Considering this paper has "RAG" in the title, it might be useful to have a section which introduces RAG, how it's relevant to symbolic regression / program synthesis problems, and how it's relevant to this algorithm. I suggest making a general section on "Foundation Models for program induction." These papers (the RAG paper, RAG + code generation papers, and symbolic regression + foundation models) might be useful:
  - https://arxiv.org/pdf/2406.14497: RAG Paper
  - https://arxiv.org/pdf/2108.11601, https://arxiv.org/pdf/2407.19619 : RAG + Code generation
  - https://arxiv.org/abs/2404.18400, https://arxiv.org/abs/2409.09359 : RAG + Foundation Models
- L198: Is the depth and number of trees fixed? How does the algorithm scale when $m$ is increased/decreased? How is $m$ selected for the experiments (Synthetic benchmark and SRBench)?
- L195-L209: "SD focuses on replacing existing trees in the model with more informative ones..."  Is the residual a tensor of real numbers or a single real number? Also, how is the difference measured? Regardless, it seems that calculating the residual requires evaluating the performance of the equation without the subterm to be replaced. For many domains where SR is used, evaluating the performance of a program is very expensive (eg: computational weather models).
- L206: What is the definition of the semantics $\psi(X)$? Is it a vector (e.g., $\psi(X) \in \mathbb{R}^N$), and is it learned, or does it represent subtree performance on indices in $X$?
- L210: How is P_neural computed? This isn't mentioned in the algorithm or in the following section. Is it a hyper-parameter?
- L409: Please add error bars to the runtime evaluation experiments by averaging across different seeds.
- L1177: Many SRBench ground-truth equations have depths greater than five. What do the failure modes on this experiment look like? What do the discovered equations look like? How do they compare to the ground truth equations (edit distance)?

### Questions
- L71: "pretraining free supervised learning:" I'm a bit confused by this phrase. Isn't pretraining, as used colloquially in NLP, a self-supervised learning strategy? Under this definition, all supervised learning algorithms should always be "pretraining free." Consider replacing this phrase.
- L103: Considering this paper has "RAG" in the title, it might be useful to have a section which introduces RAG, how it's relevant to symbolic regression / program synthesis problems, and how it's relevant to this algorithm. I suggest making a general section on "Foundation Models for program induction." These papers (the RAG paper, RAG + code generation papers, and symbolic regression + foundation models) might be useful:
  - https://arxiv.org/pdf/2406.14497: RAG Paper
  - https://arxiv.org/pdf/2108.11601, https://arxiv.org/pdf/2407.19619 : RAG + Code generation
  - https://arxiv.org/abs/2404.18400, https://arxiv.org/abs/2409.09359 : RAG + Foundation Models
- L198: Is the depth and number of trees fixed? How does the algorithm scale when $m$ is increased/decreased? How is $m$ selected for the experiments (Synthetic benchmark and SRBench)?
- L195-L209: "SD focuses on replacing existing trees in the model with more informative ones..."  Is the residual a tensor of real numbers or a single real number? Also, how is the difference measured? Regardless, it seems that calculating the residual requires evaluating the performance of the equation without the subterm to be replaced. For many domains where SR is used, evaluating the performance of a program is very expensive (eg: computational weather models).
- L206: What is the definition of the semantics $\psi(X)$? Is it a vector (e.g., $\psi(X) \in \mathbb{R}^N$), and is it learned, or does it represent subtree performance on indices in $X$?
- L210: How is P_neural computed? This isn't mentioned in the algorithm or in the following section. Is it a hyper-parameter?
- L409: Please add error bars to the runtime evaluation experiments by averaging across different seeds.
- L1177: Many SRBench ground-truth equations have depths greater than five. What do the failure modes on this experiment look like? What do the discovered equations look like? How do they compare to the ground truth equations (edit distance)?

### Soundness
3

### Presentation
3

### Contribution
3
