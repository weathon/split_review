# Unlocking SVD-Space for Feedback Aligned Local Training

- Decision: Reject
- Avg Score: 4.40
- Scores: 5, 3, 8, 3, 3

## Abstract
Deep Neural Networks (DNNs) are typically trained using backpropagation, which, despite its effectiveness, requires substantial memory and computing resources. To address these limitations, we propose a novel local training framework that enables efficient and scalable neural network training without relying on global backpropagation. Our framework harnesses the alignment of Singular Value Decomposed (SVD) weight space with feedback matrices, guided by custom layerwise loss functions, to enable efficient and scalable neural network training. We decompose weight matrices into their SVD components before training, and perform local updates on the SVD components themselves, driven by a tailored objective that integrates feedback error, alignment regularization, orthogonality constraints, and sparsity. Our approach leverages Direct Feedback Alignment (DFA) to eliminate the need for global backpropagation and further optimizes model complexity by dynamically reducing the rank of the SVD components during training. The result is a compute- and memory-efficient model with classification accuracy on par with traditional backpropagation while achieving a 50-75% reduction in memory usage and computational cost during training. With strong theoretical convergence guarantees, we demonstrate that training in the SVD space with DFA not only accelerates computation but also offers a powerful, energy-efficient solution for scalable deep learning in resource-constrained environments. Code is available.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Motivated by reducing the memory and computational cost of training deep neural networks, the authors propose a local training methodology based on Direct Feedback Alignment (DFA). DFA is limited in its application due to poor scaling to deep models and complex tasks. The authors propose to improve upon DFA by decomposing the model's weight matrices into orthogonal components using SVD, perform local updates on the orthogonal components, and to decrease the rank of this representation over the course of training. The authors provide convergence proofs in the appendix, and evaluate their method in training VGG-13, ResNet-32, and a custom small 3-layer CNN on CIFAR-10, CIFAR-100 and ImageNet.

### Strengths
* The methodology of the proposed extension of DFA proposed is intuitive, and interesting, specifically having a decreasing rank schedule over training and decomposition of the weight matrices.
* The method is well-motivated with compute and memory complexity being a challenging in contemporary applications and research with deep neural networks.
* The related-work does mention many other local training methods, although it might be a bit too dismissive of many as baselines.
* The authors provide a small ablation over the five different loss components, although this could have been more detailed.
* Please note I did not evaluate the convergence proofs in the appendix, as they were not in the main paper. Given the 5 different loss components in the methodology proposed however, I do believe they are necessary.
* Both top-1 and top-5 are evaluated for Imagenet (unlike so much contemporary work)

### Weaknesses
 * Despite the main motivation of methodology/paper, only real-world compute/memory complexity results in paper (including appendix) are VGG-13/Figure 2. This is very far from sufficient, and VGG itself is not an architecture that should be used when claiming efficiency results to begin with. The authors have accuracy results from more reasonable architectures (e.g. ResNet-32) with their method, so there is no reason not to include the compute/memory savings also. Notably the authors are themselves aware that lightweight architectures (e.g. MobileNet in 6.1) would be much better motivated, so I'm not seeing good reasons for the focus on only VGG.
* No variance/stddev in results. The results are lacking any mention of having been evaluated over multiple random inits, etc, and no variance or other measure of significance of the results is available. For small datasets/models, and with the claims behind the method being computationally efficient, there is no reason not to evaluate over multiple training runs and provide mean/variance over these runs to better evaluate the generalization results.
* Although hard to evaluate due to the above, with the results as presented, there is not clear evidence that the results are significant. In many of the results AugLocal or SVD-BP appear to be very close or better than the results of SSA.
* The work is not repeatable as presented, with a lack of experimental details, although there are some in appendix:
    * Experimental details are pronounced generally, e.g. "learning rates ranging from 1e-4 to 5e-4", rather than listed for specific experiments.
    * The five loss coefficient hyper-parameters ($\alpha, \beta, \gamma,\delta,\epsilon$), are very important. In the appendix the values for these hyper-parameters are listed to be used "ideally", and I'm not sure what this means, does it means they vary or not? Unfortunately there is both very little explanation as to how those are found (except "cross-validation"), the exact values of these hyper parameters used for each of the experimental results themselves (unless they are all the same).
     * Another example of the methodology I would consider a hyper parameter, the choice of which is poorly explained, is the rank reduction schedule.
     * Missing experimental details for CIFAR-100.
     * Missing experimental details for ImageNet.
* Tables are really all over the place, often with a single odd line of text randomly interspersed between them, making it hard to read both the paper and the tables - must have been forced with [H]. Recommend authors use [tbp] float placement for all their tables to fix this.
* In 6.2 (limitations) to their credit, the authors explain that the method is very sensitive in particular to the five loss coefficient hyper-parameters ($\alpha, \beta, \gamma,\delta,\epsilon$), as might be expected. Anyone who has attempted to work with a loss with even a few coefficients can recognize how unstable/hard such a methodology might be in practice. It's hard from the paper (as-is) to judge if using SSA requires these needed to be changed for each experiment or were kept constant for different models/datasets. If it's the former, it would be hard to justify the method as reducing training times in practice.


### Questions
* What are the real-world compute/memory results for the other models in your work?
* How exactly did you find your hyper parameters, and what are the hyper-parameters (and all other experimental details required to repeat the experiments)?
* How much do the five loss coefficients themselves have to be tuned to get good performance, i.e. how different are they for your different models/results? This is important as if they have to be found for each different experimental setup by sweeping training, it's hard to justify the method as speeding up training.
* Why did you choose to demonstrate improvements in training compute/memory usage not on a lightweight architecture, but instead VGG which is not used anymore in research/applications and widely recognized to be highly inefficient compared to e.g. ResNets, MobileNet, EfficientNet, etc.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a new learning framework dubbed SSA that combines DFA with SVD. A local loss function with five components and a dynamic rank reduction strategy are adopted to train accurate and efficient DNNs. Comprehensive experimental results demonstrate that SSA can reach comparable accuracy performance as BP while reducing memory and computational cost by a large margin.

### Strengths
1. The idea of combining DFA with SVD is novel.
2. The designed loss function takes care of many different aspects of training.

### Weaknesses
1. The paper focuses on reducing memory and computational cost during training. However, to deploy models in resource-constrained environments, efficiency during post-training inferences is more important. The paper does not adequately address the inference-time overhead of maintaining and utilizing the SVD decomposition, which could negate the training-time benefits if not carefully managed. Specifically, the cost of matrix multiplications with the decomposed matrices U, S, and V^T during inference needs to be thoroughly analyzed and compared against standard dense matrix operations.
2. It's better to provide comparison between the proposed method and model compression techiques like quantization-aware training (QAT). The paper lacks a detailed comparison with existing model compression techniques, particularly QAT, which is a widely used method for reducing model size and computational cost. A direct comparison, including metrics like model size, inference speed, and accuracy, would provide a clearer understanding of the advantages and disadvantages of the proposed method relative to established techniques. The absence of such a comparison makes it difficult to assess the practical utility of the proposed approach.
3. The proposed method has many limitations such as hyperparameter sensitivity and inability to scale to larger models. Also, no evidence is provided to show the effectiveness of SSA on transformer-based models. The paper does not provide sufficient evidence to demonstrate the robustness of the method across different hyperparameter settings. The lack of scalability to larger models is a significant limitation, as many real-world applications require large-scale models. Furthermore, the absence of experiments on transformer-based models, which are increasingly prevalent in various domains, limits the generalizability of the findings.

### Questions
Please see the weakness part.

### Soundness
2

### Presentation
2

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
This paper proposes a backpropagation-free training framework called SVD-Space Alignment (SSA). SSA decomposes weight matrices by Singular Value Decomposition (SVD) and then updates the SVD components by direct feedback alignment (DFA) under the guidance of customized layerwise loss fuctions. The experimental results demonstrate that SSA achieves classification accuracy close to that of backpropagation however with significantly reduced memory usage, computational cost, and energy consumption. A theoretical proof for SSA convergence guarantees is also presented. This novel local training framework provides a promising energy and computation-efficient solution for deep learning in resource-constrained situations.

### Strengths
The paper creatively combines SVD and DFA for neural network training. The authors introduce a tailored layerwise loss function that incorporates several different constraints so that the local layerwise updates during training are both convergent and efficient.

As network sizes grow, training becomes increasingly unaffordable for organizations and individuals with limited resources. This research presents a compelling alternative to conventional backpropagation for training deep neural network models.

This paper is well organized and clearly written.

### Weaknesses
The effectiveness of SSA for training deep convolutional neural networks has been validated in this work. Given that transformers currently dominate in domains such as Natural Language Processing (NLP), it would be beneficial for future research to explore the extension of SSA to other architectures.

It remains unclear how the dynamic rank reduction strategy is implemented and guaranteed, especially given that updates to SVD components are not inherently directed towards reducing rank. The paper mentions a progressive reduction, but lacks specific details on the mechanism. The use of a Hoyer regularizer is mentioned, but the connection to rank reduction is not clearly explained. Furthermore, the threshold-based checks are vaguely described, making it difficult to assess their effectiveness in preventing loss of representational capacity.

The decomposition of a convolutional layer while retaining its hierarchical information is described in Appendix A.3, however it may be challenging for readers to grasp. Including a schematic diagram would enhance understanding by providing a visual aid. The current description lacks sufficient detail to fully comprehend the process, especially how the SVD is applied to preserve spatial relationships within the convolutional filters.

### Questions
1. Beyond theoretical analysis, it would be beneficial to present empirical results that demonstrate the convergence rate and training stability of SSA in comparison to BP.

2. A dynamic rank reduction strategy is used to reduce the rank of weight matrix progressively. How is it implemented and guranteed, especially considering that updates to SVD components are not inherently directed towards reducing rank.

3. The decomposition of a convolutional layer while retaining its hierarchical information is described in Appendix A.3, however it may be challenging for readers to grasp. Including a schematic diagram would enhance understanding by providing a visual aid.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes SVD-Space Alignment (SSA), a local layerwise training method combining Direct Feedback Alignment (DFA) and Singular Value Decomposition (SVD) to layer weights.
The authors propose to decompose the weights and feedback matrices using SVD and to use heavily regularized local losses to ensure alignment, sparsity and orthogonality.

Experiments on three networks of different depths are conducted, presenting competitive results with back-propagation on image classification tasks with a significant reduction of memory usage and computational cost during training.

### Strengths
1. Using low rank factorization together with DFA is an interesting and natural idea.

2. The presented results seem competitive with back-propagation (BP), while heavily reducing memory usage and computational cost during training.

3. An interesting ablation study over each component of the composite loss is provided.

### Weaknesses
1. A major issue of the paper is the lack of coherence of the writing and somewhat evident mistakes.

Equation 6 for example states that the cross entropy loss is: $L_{CE}=y_{predict}-y_{label}$, while this is instead supposed to be its derivative with respect to the predictions.

In standard DFA this derivative is denoted $e$ and is then projected onto every layer $l$ thanks to fixed feedback matrices $B_l$, with a weight update reading: $W_l^{t+1}=W_l^t - \eta B_l e \odot f'(a_l)h_{l-1}^T$, with $a_l$ and $h_l$ being respectively the pre-activation and activation of the layer.
The choice of the loss to optimize in DFA (and thus of its derivative $e$) is thus left to the user, which is clearly not the case in the paper.

2. The notations should be revised in order to be coherent.

3. The composite loss comprises some terms that are not well motivated nor explained. While the provided ablation study is interesting, it clearly lacks details as for example one could ask if the cosine similarity loss indeed improves the cosine similarity. The behavior of each individual objective with respect to the others could also be interesting to study.

4. Some sentences sound like claims and are not motivated: eg l.254: what are the "stable and smooth updates" ensured by DFA? Is there a study of the "stability of the training process" (l.262)?

5. The empirical results are somehow strange in many ways:
- one would expect a more extensive comparison with DFA to be conducted, as SSA is basically a low-rank approximation of DFA
- As DFA has been successfully extended to ResNet-56 by (Sanfiz and Akrout, 2021) with open-sourced code and even to Transformers by (Launay et al., 2020), excluding DFA evaluation from Table 2 where shallower networks (VGG-13 and ResNet-32) are tested claiming it is unable to scale to larger networks is false.
- The reported results with PEPITA on a 3 convolutional layers networks (Table 1) are very surprising as the original paper by (Dellaferrera and Kreiman, 2022) only reported results for one convolution and no other more recent paper has successfully trained a deeper convolutional network to the best of my knowledge. I would be very interested to know more about how those results were obtained as it has been observed by (Srinivasan et al., 2024) that PEPITA gets progressively worse results as the network grows deeper (for MLPs). I would expect that this observation would stay true for convolutional networks but the results seem to be the exact same as for the architecture used in the original paper by (Dellaferrera and Kreiman, 2022)
- I find the reported results on ImageNet very strange as the Top-5 Accuracy is lower than the Top-1 Accuracy (Table 2). Are the two column titles inverted?

6. The theoretical analysis provided in the appendix is unfortunately false as the composite loss function is not Lipschitz smooth as the cosine similarity component is not Lipschitz smooth. Linee 830-834 are false if $x$ is very small.

7. The paper would greatly benefit from a thorough proofread.

8. Table 1 seems very weird:
>DFA was not originated by (Akrout et al., 2019). Furthermore this specific paper focused on learning the feedback connections in FA setting and not DFA. Lastly the results they got was on par with BP for ResNet 18 and ResNet 50 when trained on ImageNet.

> The PEPITA results you mention come from a recent preprint paper. This preprint reports false results on PEPITA, claiming training on a SmallConv network but reporting **the exact same results** as the original PEPITA paper on a single convolutional network. The code attached in this preprint futher does not include the PEPITA baseline.

I would like to outline that the authors should not base themselves on preprints to copy/paste some results and propagate false information. The baselines should be sourced from published papers or (in the ideal case) re-runned to verify coherence.
The given results should also be attributed to the correct paper as (Akrout et al.) did not report results for DFA.
These errors make the whole experimental section unreliable.

9. There is no hyper-parameter search for the composite loss reported. A 5 (!) component loss is presented with fixed hyper-parameters set across the experiments. Though a discussion is now in appendix, the choice of these hyper-parameters still seems coming out of pure luck.

### Questions
8. What are your interpretation of the ranges of the different hyperparameters of the composite loss, given that some components are bounded and some are not?

9. How would different scheme of initializing the feedback matrices could impact the results you give as two components of the composite loss are dependent on those matrices? 

10. How do you perform SVD on convolutional layers?

11. How do you update specific operations in ResNets such as downsampling convolutions, batch-normalization, etc?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors improve the Direct Feedback Alignment (DFA) algorithm to make it more efficient through low-rank decomposition. The weight and feedback matrices are decomposed using SVD, and local losses are used to encourage alignment and sparsity, and preserve orthogonality of the U and V matrices.

The algorithm is competitive with backpropagation on different models and image classification tasks, while providing attractive gains in terms of time and memory.

### Strengths
- Combining DFA with low rank factorization is a good idea.
- The proposed algorithm is relatively simple and intuitive.
- The results are competitive with backpropagation, with encouraging time and memory gains.
- The authors compare their method with an extensive spectrum of other alternatives to backpropagation.
- The ablation study is very relevant and clearly shows the impact of each loss on accuracy and computation time

### Weaknesses
1. As SSA is essentially a low-rank approximation of DFA, I would expect a more extensive comparison with DFA, as the proposed method is built upon it. As far as I know, DFA has successfully been applied to larger models as used in the paper (see Sanfiz et al. (2021), https://arxiv.org/pdf/2108.13446). I am unsure what “omitted from the next Table 2 due to their inability to scale to larger networks” means.
    
    Also, it would be expected that SSA at best matches DFA. On table 1 however it outperforms it by 13%. This is likely due to the alignment losses in SSA, and I believe that applying the same losses to DFA could provide a fairer baseline. It would also allow us to quantify the loss in accuracy caused by the low-rank factorization.
    
2. I could be beneficial to include models different than CNNs, and tasks different than image classification. For instance, a simple MLP.
3. The method introduces 4 to 5 new hyperparameters, which currently have to be tuned. It would be interesting to measure the impact of these on the final accuracy.
4. Presentation and formatting: The citations are not correctly inserted in the text, the parentheses are missing. Use the \citep command instead if using natbib. Less important, but I believe the tables and figure 1 could benefit from a cleaner layout / style to improve readability and visibility of the results.
    
    Eq. 6 is unclear to me. This quantity is the error (i.e. the gradient of the loss w.r.t the last hidden states), not the crossentropy loss. I find the notations very confusing. In addition, the layers do not receive the gradients of the cross-entropy loss but instead use DFA to approximate it, which is not reflected in equations 5 and 6.
    
5. The theoretical analysis in the Appendix is wrong in many ways.
    - At the beginning, on line 613, it is stated that the composite loss is Lipschitz smooth, which is clearly not the case given that the cosine similarity is not.
    - The loss functions are also dependent on the output of the previous layer and on the error, which is not taken into account here. This means that the local loss is not always decreasing, as updating layer 1 can impact the loss of layer 2 for example.
    - In A.1.6, the claimed “Lipschitz constant” of $\nabla_U L_\text{ortho}(U)$ depends on U, which is forbidden.
    
    I would strongly advise the authors to revise this part. It would also be best to make it more concise, for instance A.2.1 is trivial, and there is no need to take so much space proving a function is smooth, especially when it is not (see the part about cosine similarity).
    
    However this analysis does not impact the contributions of the paper, and the algorithm does not rely on it.

### Questions
1. I do not understand how convolution are handled by SSA. How do you perform SVD decomposition on the convolution layers?
2. What is the motivation behind the cosine similarity loss? I do not get why aligning the output of the layer with its estimated gradient could lead to better learning (although I do see that this is the case from the ablation study).

### Soundness
2

### Presentation
2

### Contribution
3
