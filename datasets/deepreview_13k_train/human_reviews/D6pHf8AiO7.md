# Pruning neural networks using FishLeg estimation

- Decision: Reject
- Scores: 6, 5, 3, 3

## Abstract
In many domains, the most successful AI models tend to be the largest, indeed often too large to be handled by AI players with limited computational resources. To mitigate this, a number of compression methods have been developed, including methods that prune the network down to high sparsity whilst retaining performance. The best-performing pruning techniques are often those that use second-order curvature information (such as an estimate of the Fisher information matrix) to score the importance of each weight and to predict the optimal compensation for weight deletion. However, these methods are difficult to scale to high-dimensional parameter spaces without making heavy approximations. Here, we propose the FishLeg surgeon (FLS), a new second-order pruning method based on the Fisher-Legendre (FishLeg) optimizer. At the heart of FishLeg is a meta-learning approach to amortising the action of the \emph{inverse} FIM, which brings a number of advantages. Firstly, the parameterisation enables the use of flexible tensor factorisation techniques to improve computational and memory efficiency without sacrificing much accuracy, alleviating challenges associated with scalability of most second-order pruning methods. Secondly, directly estimating the inverse FIM leads to less sensitivity to the amplification of stochasticity during inversion, thereby resulting in more precise estimates. Thirdly, our approach also allows for progressive assimilation of the curvature into the parameterization. In the gradual pruning regime, this results in a more efficient estimate refinement as opposed to re-estimation. We revisit the autoencoder optimisation benchmark of the original FishLeg paper and show that FLS yields highly effective one-shot and gradual pruning, better than previous methods. We further extend FishLeg by developing new structured approximations of the inverse Fisher for convolutional layers. We find that FishLeg greatly improves one-shot pruning accuracy over previous second-order methods on ResNet50 (e.g. 62\% accuracy at 75\% sparsity, v.s. 41\% for M-FAC).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a novel pruning mechanism that uses the FishLeg optimizer, which is based on the the inverse fisher information matrix. This work proposes a number of improvements to the fishleg optimizer to make it more amenable for unstructured pruning, such as  modeling the full FIM, as opposed to its action of a parameter subspace, as well as a preconditioner for the auxiliary loss. When applied to pruning, the authors show that there are improvements on various benchmarks, outperforming other second-order methods, and shows potential for network quantization applications.

### Strengths
* Interesting application of fishleg optimizer
* Fishleg extended to model the full inverse FIM with preconditioning
* Efficient and flexible parameterization of inverse FIM
* Good experimental results on benchmarks (figures 2,3)  compared to approaches like oBERT and M-FAC

### Weaknesses
 * Efficiency is mentioned as an important component of the method, but no timing analysis was performed, There is some mention of memory consumption, but this is not made concrete.  It would be beneficial to see a breakdown of the computational cost, specifically the time spent on computing the inverse Fisher Information Matrix (FIM) and the subsequent pruning steps, compared to the baseline methods. The memory consumption should also be quantified, detailing the memory footprint of storing the full FIM or its approximation, as this could be a limiting factor for larger models.
* The introduction claims that the largest models are inaccessible to those without compute resources. How does this method help this situation when only ResNet-50 (that anyone can run) is examined. The paper should include experiments on larger models or at least provide a clear explanation of how the proposed method scales to such models. The current experiments on ResNet-50, while useful, do not fully address the claim about accessibility to large models.
* Results only show small dense autoencoder and resnet-50, would be nice to see more architectures and tasks. The evaluation should be extended to other architectures, such as transformer networks, and tasks, such as object detection or natural language processing. This would provide a more comprehensive assessment of the method's generalizability and robustness. The current results are limited in scope and do not fully demonstrate the potential of the method.
* Results are quite marginal for imagenet (table 1), but I acknowledge that competing approaches saw smaller gains over each other.

### Questions
1. What is the computation burden of all methods? ResNet-50 may take up < 3Gb of VRAM, so 17GB is quite a lot more.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors proposed a Optimal Brain Surgery pruning technique where importance is based on the Fisher information matrix.  Following the FishLeg optimization due to Garcia et al., they proposed a specific parameterization of the inverse Fisher information matrix, as well as optimization procedures.  They further demonstrated with experiments on unstructured network pruning.

### Strengths
A potentially better yet practically tractable importance measure for OBS is of value to network compression practice in general.  The hypothesis that an approximated Fisher information inverse by FishLeg meta-optimization can play such a role is a novel idea.

### Weaknesses
 - The parameterization of the inverse of Fisher information matrix (Eq. 9) is not unique even under the practicality constraint.  There might exist a practical tradeoff between the capacity and form of the parameterization and the quality of the resulting importance metric for pruning.   Specifically, the choice of parameterizing the inverse Fisher with a low-rank plus diagonal structure, while computationally convenient, may limit the expressiveness of the approximation, potentially leading to suboptimal pruning decisions. The authors should explore the sensitivity of the pruning performance to different parameterization choices, and provide a more thorough justification for their specific choice. For instance, they could investigate the impact of varying the rank of the low-rank component or using different forms of the diagonal matrix.
- As the authors demonstrated, the procedure of meta-optimization of $\lambda$ has hyperparameters that are tricky to tune.  This leads to practical complexity.  The meta-optimization process introduces additional hyperparameters, such as the learning rate and the number of iterations for the meta-optimization, which can significantly impact the quality of the learned inverse Fisher approximation. The authors should provide a more detailed analysis of the sensitivity of the method to these hyperparameters and offer practical guidelines for their selection. Furthermore, the computational cost associated with the meta-optimization process should be explicitly quantified and compared to the cost of other pruning methods.
- Lack of demonstration with large models in comparison against competing techniques.  The experimental evaluation is limited to relatively small models and datasets. The authors need to demonstrate the scalability of their method by evaluating it on larger models, such as those used in state-of-the-art computer vision or natural language processing tasks. This is crucial to assess the practical applicability of the proposed method in real-world scenarios. Furthermore, a more comprehensive comparison against competing pruning techniques, including both first-order and second-order methods, is needed to establish the superiority of the proposed approach.
- Even with the small-model examples presented, the superiority of the proposed method has not been convincingly demonstrated.  For example, if the proposed importance metric (Eq. 4) is indeed superior than that from a competing method, e.g. OBC, then it is necessary to show the disagreement between them with a concrete example, e.g. a specific layer in Resnet50, where the optimal solutions in one is suboptimal in the other, but the current solution leads to lower loss change. The authors should provide a more detailed analysis of the differences in the importance scores computed by their method and other second-order methods, and demonstrate that their method leads to better pruning decisions by showing that the weights pruned by their method are indeed less important than those pruned by competing methods.

### Questions
See above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes FishLeg Surgeon (FLS), a pruning technique that uses the FishLeg under the hood (an already existing approach to estimate Fisher Information Matrix (FIM) in neural networks, initially used for optimization) in the Optimal Brain Surgeon (OBS) framework to perform unstructured pruning, more precisely one-shot and gradual pruning. The experiments are performed on an autoencoder for MNIST and ResNet-50 on ImageNet.

### Strengths
1. the paper is easy to follow
2. the results on the AutoEncoder and ResNet-50 show improvements over other approaches, such as M-FAC and oBERT at 70%, 80% and 90% sparsity

### Weaknesses
I believe that paper contribution is not good enough for ICLR standards. Since the authors adapted the FishLeg implementation for pruning, I would have expected a broader evaluation process. The AutoEncoder benchmark on MNIST (which is also used in the FishLeg paper) and ImageNet on ResNet-50 are not that relevant for pruning.

The M-FAC and oBERT baselines are not state of the art for ImageNet/ResNet-50 benchmark. For example, in the Figure 8 from the CAP approach [1] also show around 70% accuracy for M-FAC for the same benchmark (ImageNet/ResNet-50 @ 75% sparsity), but the CAP approach is much better than M-FAC, reaching about 75% accuracy for 75% sparsity.

The paper does not have any experiments on LLMs pruning. Since this paper addresses the one-shot pruning too, some good results can be obtained using SparseGPT [2] technique, which showed good results on one-shot pruning on large models.

### Questions
Given the presented weaknesses, I would like to add the following questions and I would appreciate if you could answer them one by one.

1. did you run M-FAC and oBERT from scratch during your evaluation process?
2. how does FLS behave for other tasks, such as:
- LLMs pruning, such as BERT on GLUE/SQuAD
    - for example, against gradual pruning on oBERT
    - one-shot pruning on large models against SparseGPT
- ViT or DeiT on ImageNet against CAP

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a novel method of deep neural network unstructured pruning (sparsity). They claim that the best-performing pruning techniques use second-order methods for importance estimation. However, due to the size of modern neural networks, these methods are computationally too expensive. To address this limitation, the authors introduce FishLeg surgeon (FLS). The core idea is to leverage an accumulation of the gradients instead of storing them individually. This is achieved through tensor decomposition for an effective approximation. The authors mainly evaluate the proposed method on ResNet 50 trained on ImageNet.

### Strengths
Deep neural network compression is of paramount importance for future deployment. The authors proposed a novel method which brings marginal improvements over previous state-of-the-art methods.

### Weaknesses
I see three major concerns with this work
1. the empirical validation is not sufficient for a conference like ICLR. Research on pruning should at least involve a transformer architecture in its benchmarks. This has been the case for a few years in quantization.
2. The current results on ResNet 50 suggest that the benefits of the proposed method in terms of accuracy v.s. compression trade-offs are marginal and do not include many other works such as [1,2] which all achieve more impressive results (without using second order importance estimation)
3. The authors list many advantages of FishLeg which translate in marginal improvements on ImageNet

### Questions
I have listed a few concerns above. I will wait for the authors' response regarding 2 and 3. With respect to 1, i would like to open a discussion with other reviewers.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor
