# Probabilistic Neural Pruning via Sparsity Evolutionary Fokker-Planck-Kolmogorov Equation

- Decision: Accept
- Scores: 8, 6, 8, 8

## Abstract
Neural pruning aims to compress and accelerate deep neural networks by identifying the optimal subnetwork within a specified sparsity budget. In this work, we study how to gradually sparsify the unpruned dense model to the target sparsity level with a minimal performance drop. Specifically, we analyze the evolution of the population of optimal subnetworks under continuous sparsity increments from a thermodynamics perspective. We first reformulate neural pruning as an expected loss minimization problem over the mask distributions. Then, we establish an effective approximation for the sparsity evolution of the optimal mask distribution, termed the **S**parsity Evolutionary **F**okker-**P**lanck-**K**olmogorov Equation (**SFPK**), which provides closed-form, mathematically tractable guidance on distributional transitions for minimizing the expected loss under an infinitesimal sparsity increment. On top of that, we propose SFPK-pruner, a particle simulation-based probabilistic pruning method, to sample performant masks with desired sparsity from the destination distribution of SFPK. In theory, we establish the convergence guarantee for the proposed SFPK-pruner. In practice, our SFPK-pruner exhibits competitive performance across various pruning scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work formulates the neural network pruning procedure as the evolution of sparse mask distributions in response to increasing levels of sparsity, employing the Fokker-Planck-Kolmogorov equation. Specifically, given a rational dense solution, it provides a theoretically well-founded definition of the distributional transition for the sparse mask, indicating which parameters should be pruned. Experimental results are provided for both one-shot and iterative schemes, as well as for structured and unstructured sparsity, covering convolutional and vision transformer architectures.

### Strengths
S1. In neural network pruning, a line of research focuses on iterative methods that start with a dense network with zero sparsity and gradually increase the sparsity level. A well-known example is the Iterative Magnitude Pruning (IMP) algorithm, which, while computationally expensive, is highly effective at producing high-performance sparse networks. This work shares a similar spirit (especially in the prune-and-retrain setup), deriving the sparse mask for each new sparsity level from the previous one, gradually updating the mask as sparsity increases. However, rather than treating the optimal mask at each level as a fixed point estimate, this work consider a distribution over masks, adding a compelling dimension to the method.

S2. As the authors noted, the most closely related work is the ODE framework proposed by Mo et al. (2023), which evolves sparse masks over time by treating the sparsity level as the timestep. This work explicitly acknowledges this connection in the main text and provides a clear discussion in the Introduction that highlights the contributions unique to them. It not only gives proper credit to prior work but also helps readers understand the progression of ideas.

S3. The proposed SFPK methodology is well-motivated, and the flow of Sections 1-4 effectively presents it. Overall, the experiments are well-executed, featuring a comprehensive comparison to various baselines. While there is room for improvement, as noted in the Weaknesses section, the core results are largely well presented.

### Weaknesses
Since I appreciate the underlying concepts of the proposed SPFK methodology, I will primarily concentrate on addressing the experimental concerns here.

W1. The tables do not include error bars, making it unclear how statistically significant the current results are. How many trials were conducted for the values presented? From the caption of Figure 2, is it three trials for all experiments? If space is a concern, the main text could provide only the averaged numbers, while a full table with standard deviations could be included in the appendix.

W2. In the _One-shot Pruning_ experiment in Section 5.2, it is quite intriguing that the SPFK method achieves such performance after one-shot pruning on a given pre-trained dense weight without requiring further training for recovery. However, it is important to note that all three methods—WF, PSO, and SFPK—incur significantly higher costs compared to Mag, SNIP, and SynFlow for obtaining valid results. Including a cost comparison for each method would be beneficial. At the very least, the costs associated with SFPK compared to WF and PSO should be presented (especially since Mag, SNIP, and SynFlow would not even be considered when targeting high sparsity). The computational cost should be detailed in terms of both theoretical complexity and actual runtime, highlighting the practical implications of the proposed method.

W3. In the _One-shot Pruning_ experiment in Section 5.2, Table 1a presents results for the convolutional architecture, while Table 2a displays results for the vision transformer architecture. However, Table 1a only includes results _without_ further training and _unstructured_ sparsity, whereas Table 2a only includes results _with_ further training and _structured_ sparsity. Is there a specific reason for this distinction? From the reader's perspective, it would be beneficial to see comprehensive results for both convolutional and vision transformer architectures for each method—{Mag, SNIP, SynFlow, WF, PSO, SFPK}, particularly for {WF, PSO, SFPK} as they are the main competitors—across all scenarios: with and without further training, and structured and unstructured sparsity. The lack of consistent experimental settings across different architectures makes it difficult to draw general conclusions about the method's effectiveness.

W4. The SFPK methodology fundamentally assumes "rational" pre-trained weights, denoted as $\theta^\ast$. I noticed that the paragraph _"Constraints of SPFK-pruner"_ in Appendix A.1 discusses this topic, stating, _"We recommend applying SFPK to sufficiently trained "rational" models (e.g., trained to convergence)."_ However, there is currently no experimental evidence supporting the practical significance of this recommendation. It is particularly important in the prune-and-retrain setup, as the extent of retraining to re-obtain the "rational" $\theta^\ast$ can consume a substantial portion of the total training budget. I initially expected the Appendix B to address this (after reading lines 448-449), but it still fixes the retraining budget for SFPK at 100 epochs. Currently, there is no discussion on how "rational" pre-trained weights need to be for SFPK to function effectively. Including empirical results on this matter would undoubtedly strengthen the paper. It is crucial to understand how the performance of SFPK degrades with less-than-optimal pre-trained weights, and whether the method is robust to variations in the quality of the initial weights.

W5. As of 2024, 90% sparsity for ResNet50 on ImageNet is not considered particularly high (especially when all parameters, including the final linear weights, are allowed to be pruned). To convincingly demonstrate the effectiveness of the proposed method, comparative results should be presented in a higher sparsity regime of 95% or more. Additionally, the comparisons primarily involve relatively old baseline methodologies, with the most recent baseline in Table 2c dating back to 2020; it raises the question of whether it is appropriate to claim that _"our SFPK-pruner demonstrates decent performance compared to SOTA baselines."_ For instance, the method called Spartan (Tai et al., NeurIPS 2022) reports an accuracy of 76.17% for 90% sparsity in a 100-epoch setup. Although the pruning community has shifted its focus away from the ResNet50 on the ImageNet setup, and I am not sure whether recent SOTA results are being reported, it remains important to include comparisons with the latest baselines available in this paper. The lack of comparison with recent state-of-the-art methods limits the impact of the experimental results.

P.S. As I continue writing, I recognize that providing such extensive experimental results could be burdensome, especially during the rebuttal period. I want to clarify that I do not expect all results to be presented within this limited timeframe (particularly, feel free to skip W3). Please share any results you can within your available time and resources, along with a brief explanation of how you plan to address the mentioned concerns in the future if they are not currently available.

### Questions
Q1. In Lines 428-430, it states that _"the SFPK-pruner with a batch size of $256$ for $n \times K = 1500$ steps is equivalent to that of only ONE epoch of retraining on ImageNet."_ While I understand that running $n = 10$ particles sequentially for $K = 150$ steps (without parallelization) results in a batch size of $256$ over $n \times K = 1500$ steps, it seems that $256 \times 1500 = 384000$ samples would correspond to approximately 0.3 epochs of ImageNet (given that the total number of training samples in ImageNet is 1.28 million), rather than one epoch. Could you clarify this point?

Q2. Regarding W4, can SPFK operate with randomly initialized weights? While this clearly disregards the "rational" constraint, it is noteworthy that single-shot approaches like SNIP, GraSP, and SynFlow originally claim to find effective sparse masks using only randomly initialized weights (i.e., pruning-at-initialization). I am curious whether SPFK can outperform these methods in identifying a better sparse mask in a pruning-at-initialization manner. Ideally, the relationship would be random mask < SNIP, GraSP, SynFlow < SPFK. Alternatively, demonstrating that SPFK does not outperform SNIP, GraSP, and SynFlow in the pruning-at-initialization setup could also help clarify the significance of the "rational" constraint.

Q3. The core of the SFPK pipeline, particularly when compared to Mo et al. (2023), revolves around simulating $n>1$ particles. The paragraph _"Ablation on the Mask Particle Simulation Scheme"_ in Section 5.3 illustrates that the proposed SFPK significantly relies on both $n$ and $K$. Notably, the difference between using $n=1$ and $n>1$ is considerable (in Figure 3), highlighting the importance of leveraging multiple particles for the effectiveness of the SFPK methodology. I'm interested in the diversity of the particles in this context. Intuitively, at low sparsity, there are likely many mask candidates that yield effective sparse solutions. However, at high sparsity, could the particles collapse? If that’s the case, it may be advantageous to reduce the number of simulated particles as sparsity increases, potentially enhancing computational efficiency.

Q4. Are all trainable parameters, including convolutional weights, batch normalization scales and biases, and dense weights and biases, subject to pruning? Some studies on pruning convolutional neural networks focus solely on convolutional weights, e.g., the SWAMP paper (Choi et al. 2024) notes, _"we exclusively perform weight pruning on the convolutional layer, leaving the batch normalization and fully-connected layers unpruned."_ This can lead to discrepancies in reported numbers across studies, particularly in the ResNet50 on ImageNet setting, where the final linear layer accounts for about 8% of the total 25,557,032 parameters (i.e., 2,048,000/25,557,032). Could you provide further details on this? It is important to note that allowing the pruning of the final linear weights often leads to significantly better performance at the same level of sparsity (when we compute the sparsity as the number of unpruned parameters divided by the number of all parameters, regardless of such constraints).

Specifically, the SWAMP results for ImageNet presented in Table 6 indicate 88.9% sparsity, with approximately 2.8 million unpruned parameters, of which 2.0 million are linear weights. When calculating sparsity based solely on prunable parameters  for SWAMP (i.e., convolutional weights), we arrive at approximately 96.9% sparsity. Recalculating SWAMP's sparsity as the number of pruned prunable parameters divided by the total number of prunable parameters yields the following adjustments (see the code block below for details): 80.0% becomes 87.2%, 86.0% becomes 93.7%, and 88.9% becomes 96.9%. While this value may not perfectly align with the sparsity of SFPK, it is noteworthy that SWAMP achieves 75.69% accuracy at 87.2% sparsity, whereas SFPK achieves 75.65% accuracy at 87.4% sparsity, indicating a close alignment in results. Therefore, it is important to assess whether fair comparisons have been adequately conducted for not only SWAMP but also other methods.

```
ResNet50 for ImageNet.
- 25557032 : the total number of parameters in ResNet50 for ImageNet.
- 23454912 : the number of convolutional parameters.
- 2102120 : the number of remaining parameters.

If there are 5111406 (= 3009286 + 2102120) unpruned parameters,
- 1 - 5111406 / 25557032 = 80.0% sparsity.
- 1 - 3009286 / 23454912 = 87.2% sparsity, if we consider only the prunable parameters.
```

Q99. It's just a very minor detail, but I'm curious—why is it referred to as SFPK instead of SEFPK?

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
This paper introduces a method to identify a sparse network by incrementally selecting the mask that results in the smallest performance reduction as sparsity increases. Deriving from  thermodynamics, the authors begin with a population of dense masks and progressively evolve a distribution of sparse masks using the Fokker-Planck-Kolmogorov equation. Their approach offers a way to transition to a higher sparsity mask distribution by increasing the sparsity by a small amount in every step. Additionally, the authors propose a pruning scheme based on this transition, which iteratively refines a population of sparse masks to achieve an effective sparse network.

### Strengths
1. The proposed algorithm optimizes a population of sparse mask in an evolutionary manner while increasing sparsity to find a performant sparse network. This is a novel which seems to dynamical learn mask structure similar to dynamic sparse training method albeit in an evolutionary manner.
2. The authors also experimentally validate the proposed pruning method.

### Weaknesses
1. The authors provide a comprehensive experimental evaluation of the proposed method. However, the performance across tasks is similar to dynamic sparse training methods like RiGL and only slightly outperforms it in some cases (as in Table 8). Given this, it would be important to know the computational comparisons of DST methods versus the SFPK pruner. On ImageNet the authors mention that the SFPK pruner adds an overhead equivalent to 3 training epochs, would this mean it is marginally more expensive than DST?.
2. In order to optimize the mask, the sparsity function chosen by the authors is the polarizer. Is there a reason for choosing this specific operator, how would it compare with other operators such as soft thresholding or even a sigmoid. 
3. Results in Table 1 could be a bit misleading since the pruning at initialization methods like Snip and Grasp are not designed to minimize the loss upon sparsification and hence cannot be compared without any retraining after pruning.

### Questions
See above.

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
5

### Summary
Summary

- In this paper, the authors reformulate pruning as an expected loss minimization problem within the mask distribution space and introduce the SFPK to represent distributional transitions. Leveraging the proposed SFPK, they develop the SFPK-pruner, a particle simulation-based probabilistic pruning method.

### Strengths
Strengths

- The paper is well-written and easy to follow.
- Using the probabilistic lifting and convexification technique from [1] to develop a probabilistic soft neural pruning approach is a fresh and intriguing method.
- The theoretical analysis and approximations supporting the SFPK-guided pruning proposal are reasonable and add an interesting perspective.
- Overall, I am satisfied with the experimental scale, results, and novelty of the method. Although the requirement to create $ n $ mask particles presents practical challenges for applying this method to large models, such as large language models, I still believe this is a good paper that falls within the acceptance boundary.

References

[1] Veit David Wild, Sahra Ghalebikesabi, Dino Sejdinovic, and Jeremias Knoblauch. A rigorous link between deep ensembles and (variational) bayesian methods. In Thirty-seventh Conference on Neural Information Processing Systems, 2023.

### Weaknesses
Weaknesses

- Additional analysis on the computational overhead as $ n $ and $ K $ increase would be beneficial. While these values can be adjusted, a larger $ n $ could lead to a linearly increased memory overhead, and a larger $ K $ could introduce extra computational burden compared to other methods. Specifically, the memory usage for storing $n$ mask particles, each the size of the model's parameter space, needs to be explicitly addressed, especially when considering large models. Furthermore, the computational cost of the inner-product calculation, which scales as $O(nKd)$, where $d$ is the dimensionality of the mask, should be analyzed in detail, as this could become a bottleneck for very large models or high values of $n$ and $K$.

- A comparison with similar methods, such as iterative magnitude pruning methods, which also gradually adjust sparsity, would provide useful context. It is important to understand how the proposed method compares against iterative magnitude pruning in terms of both performance and computational cost, especially since iterative magnitude pruning is a widely used and well-understood baseline. A more detailed comparison should include metrics such as the number of pruning iterations, the computational time per iteration, and the final model performance at various sparsity levels.

- It would be helpful to assess the performance of each of the $ n $ particles individually and check if they display functional diversity. Verifying whether the method adequately covers the posterior distribution of the mask or simply converges towards one or a few local minima with good performance would more clearly demonstrate the effectiveness of the proposed method. Specifically, analyzing the variance in the performance of the $n$ particles and their mask configurations would provide insight into the exploration capabilities of the method. If the particles tend to converge to similar masks, it would indicate a lack of diversity and potentially limit the effectiveness of the approach.

### Questions
See Weaknesses section. If the responses to my questions are satisfactory, I am open to increasing my rating.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors use probabilistic lifting to reformulate gradual pruning as the evolution of the mask distribution. The authors then assume locality and derive the equations governing the sparsity evolution, which the authors refer to as the SFPK equation. Finally, based on SFPK, they propose a new pruning algorithm, which they demonstrate through extensive experiments its SOTA performance on a range of pruning tasks.

### Strengths
The paper presents a strong combination of theory and experiments. The paper proposes a theoretically driven algorithm, which achieves the state-of-the-art performance on a range of pruning tasks. The theoretical analyses, especially the relation to the FPK equation, bring new insights for pruning. Overall, the paper has a significant impact to the field.

### Weaknesses
Major points:

1.	The authors does not emphasize the critical role of using mini batches in algorithm 1. Mini-batches and stochastic noises are crucial for algorithm 1. If using full batches, then T should be the same for all m_i from the begining, resulting a collapse of the distribution. The lack of discussion on the impact of batch size on the mask distribution evolution is a significant oversight. Specifically, the algorithm's reliance on stochastic gradients for exploration of the mask space is not clearly articulated, and the potential for the mask distribution to collapse when using full batch gradients is not addressed. This could lead to a misunderstanding of the algorithm's practical requirements.

2.	The performances of SNIP and SynFlow in table 1 seem unreasonably low. I suspect there may be some mistakes in the experiments. Specifically, both methods prune the network at initialization prior to training. I wonder if the authors mistakenly apply those pruning algorithms at the end of training. This could explain the discrepancies in performance, and I recommend the authors review the experimental setup for these pruning algorithms to ensure correctness. The reported results for SNIP and SynFlow are significantly below expected performance levels, raising concerns about the experimental methodology. These methods are designed for pruning at initialization, and their poor performance in the reported post-training one-shot pruning scenario suggests a potential misapplication of the algorithms. It is crucial to verify whether these methods were correctly implemented and evaluated under their intended settings.


Minor points:

1.	It may be good to define the distributional transition T when it is first introduced at the end of section 3.

2.	I don’t find a definition of the mask polarizer $P_\epsilon$ in the main text. It should be defined.

3.	The authors claim their algorithm is robust against different $\lambda$, but this should be expected as $\lambda$ is introduced for a technical reason to convexify the optimization problem. From an algorithm perspective, it may not be necessary to have $\lambda$ at all. It would also be useful to include results in Fig. 3 with $\lambda=0$.

### Questions
Please refer to the weakness.

### Soundness
3

### Presentation
4

### Contribution
4
