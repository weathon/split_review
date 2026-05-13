# Preserving Deep Representations in One-Shot Pruning: A Hessian-Free Second-Order Optimization Framework

- Decision: Accept
- Scores: 8, 5, 8, 6, 6

## Abstract
We present SNOWS, a one-shot post-training pruning framework aimed at reducing the cost of vision network inference without retraining. Current leading one-shot pruning methods minimize layer-wise least squares reconstruction error which does not take into account deeper network representations. We propose to optimize a more global reconstruction objective. This objective accounts for nonlinear activations deep in the network to obtain a better proxy for the network loss. This nonlinear objective leads to a more challenging optimization problem---we demonstrate it can be solved efficiently using a specialized second-order optimization framework. A key innovation of our framework is the use of Hessian-free optimization to compute exact Newton descent steps without needing to compute or store the full Hessian matrix. A distinct advantage of SNOWS is that it can be readily applied on top of any sparse mask derived from prior methods, readjusting their weights to exploit nonlinearities in deep feature representations. SNOWS obtains state-of-the-art results on various one-shot pruning benchmarks including residual networks and Vision Transformers (ViT/B-16 and ViT/L-16, 86m and 304m parameters respectively).

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper argues it is important to consider the effect of pruning of the whole network instead of just layerwise when performing one-shot post-training pruning. They use a Hessian-free second-order method to optimize their formulation. The results show significant improvement in image-classification tasks on resnets and vits.

### Strengths
1. The formulation is neat, and the use of tools from optimization literature (Hessian-free conjugate gradients) is elegant.
2. The results show significant improvements over OBC and pruning using the layerwise objective.
3. Writing is clear and the main claims are supported by the experiments.

### Weaknesses
1. The emphasis on using true Hessian information is not supported in the experiments. This is not a crucial point but in most scenarios in deep learning, Fisher matrix-based approximation of Hessian [a] (or even Ada-grad [b] or Adam) works well. It would be worth providing that baseline to better support the proposed method.

- [a] Martens, James. "New insights and perspectives on the natural gradient method." Journal of Machine Learning Research 21.146 (2020): 1-76.
- [b] Duchi, John, Elad Hazan, and Yoram Singer. "Adaptive subgradient methods for online learning and stochastic optimization." Journal of machine learning research 12.7 (2011).

### Questions
1. There are a few cases where other pruning methods fail (very low accuracy, Fig. 3, Tab. 1), could you comment on the potential reasons?
2. Does retraining improves the performance further after pruning using the proposed method?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The following paper presents SNOWS, a one-shot post-training pruning technique that performs pruning at a layer-wise level while globally optimizing joint layers within a deep neural network to include nonlinear activation functions within. While it resulted in a more challenging optimization problem due to nonlinearities, it is possible to use the Hessian-free approach integrated with a customized Conjugate Gradient (CG) method that efficiently solves second-order approximation during gradient computation while simultaneously allowing reduced memory requirements. Experiments on various Computer Vision tasks under both CNN-based architecture and Vision transformer highlighted the effectiveness of SNOWS.

### Strengths
1. Besides achieving performance improvement compared to other one-shot pruning methods, the proposed method also improves the classification performance in image classification tasks when built on top of existing sparse mask selection algorithms for N:M pruning, denoting its practicability for accelerated training.
2. Highly appreciate the fact that the source code is available for inspection.

### Weaknesses
1. There are no conclusions and limitations section in the paper, and the writing in the methods section can be more concise in Section 4, which mainly focuses on explaining the SNOW method. This could leave more space to explain the experiment section in the main paper properly along with the results. Overall, the organization of this paper needs a lot of improvement and it feels like the paper is not ready for publication in the current form. 
2. Typos:
- "Like retraining approaches" -> "Like retraining, approaches" (Section 1)
- "network parammeters $\mathbf{W} = (\mathbf{W}^1, ..., \mathbf{W}^1)$ should have been $\mathbf{W} = (\mathbf{W}^1, ..., \mathbf{W}^L)$ (Section 3)

### Questions
See the weakness section.

===EDIT: Rating is raised from 3 to 5=====

### Soundness
3

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
4

### Summary
This paper proposes a novel pruning method called SNOWS (Stochastic Newton Optimal Weight Surgeon), which is an adaptation of pruning methods like the Optimal Brain Surgeon method, that uses the second-order information of the weights to do the pruning.
However, SNOWS does not calculate the full hessian but merely the hessian products, and those too are not all calculated (approximated) at once and the optimization is performed using stochastic newton descent.

### Strengths
The following are the strengths of the paper:
1. The idea contributed by this paper seems to be novel and is very interesting. 

2. The theoretical aspect of the paper seems sound.

3. The proposed method seems universally applicable to convolution and ViT-based models. 

4. The writing of the paper is quite clear.

### Weaknesses
The paper's introduction makes some glaring errors in defining concepts. For example, it describes one-shot pruning methods as pruning methods that do not require retraining after pruning. However, this is not accurate. Pruning can be done iteratively or one-shot; however, some finetuning might be required after one-shot pruning, as shown by [1], [2], and many other methods covered by [3].

With the above definition for one-shot in mind, [4] achieves unstructured pruning with more than 90% sparsity while not dropping any clean performance for multiple architectures. The proposed SNOWS method should also be evaluated against [4] for unstructured pruning performance.


Lastly, the major motivation of the proposed work is gain in speed when performing pruning (as the entire hessian need not be calculated), however these no exists latency comparison to other pruning methods.

### Questions
Q1- Since this method is able to achieve semi-structured sparsity, how does its latency compare to unstructured pruning methods? A comprehensive latency study would be very helpful.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
(+) The authors propose optimizing a more global reconstruction objective referred to as SNOW, which accounts for non-linear activations deep in the network to obtain a better proxy for the network loss.

(+) This nonlinear objective leads to a more challenging optimization problem - the authors demonstrate that it can be solved efficiently using Hessian-free optimization.

(+) SNOWS demonstrates its effectiveness with state-of-the-art results on various one-shot pruning benchmarks, including  CNNs and Vision Transformers (ViTs).

### Strengths
(+) SNOW can be seamlessly applied to any sparse mask from prior methods, refining weights to leverage the nonlinearities in the deep feature representations of CNNs and ViTs.

(+) The updated rule (Newton) and the illustrative examples in the Supplementary section are well articulated.

### Weaknesses
(-) The motivations for the improved layer-wise model (Eq. 3) need clarification. Why are the subsequent operations $f^{l:l+K}$ necessary-are they intended to minimize residuals? Please clarify the motivation behind SNOW by explaining the concept of Fig. 2 and including additional captions.

(-) While SNOW’s performance with increasing K iterations is well documented, computational comparisons with baselines are lacking. For consistent comparisons, all experimental results should explicitly include the number of K-iterations in captions of tables and figures. Moreover, I recommend the authors add an ablation study on the time complexity of K-iterations to the experimental result tables. The current analysis lacks a detailed breakdown of how the computational cost scales with K and the network size, making it difficult to assess the practical applicability of the method, especially for large-scale models. Furthermore, the memory requirements for different values of K should also be included in the analysis, as this is a critical factor in determining the feasibility of the approach on resource-constrained devices.

### Questions
Please see the above weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes SNOWS, a one-shot pruning framework aimed at reducing vision network inference costs without retraining. Unlike traditional approaches that prioritize layer-wise error minimization, SNOWS optimizes a global objective that captures deeper, nonlinear network representations. To efficiently solve the resulting complex optimization problem, SNOWS leverages a Hessian-free second-order method that computes Newton descent steps without needing the full Hessian matrix. SNOWS also enhances any pre-existing sparse mask by refining weights to better leverage nonlinearities in deep features. The framework demonstrates state-of-the-art results across multiple one-shot pruning benchmarks, including residual networks and Vision Transformers. Results are shown for CIFAR10/100 and Mini-Imagenet.

### Strengths
**===After rebuttal, I raised score from 5 to 6=====**
+ A method with a new pruning strategy at the level of global reconstruction shows promising results on common datasets CIFAR and Mini-Imagenet.
+ The proposed framework is reportedly efficient where it does not require storing the full Hessian matrix, allowing it to perform running with large neural networks.
+ Providing more details of pruning with ViT models gives some new insights.

### Weaknesses
 **Concerns**
+ The baselines seem to be out-of-date, it would be helpful to specify additional recent baselines from 2024. More baselines should be considered for example [1,2]. Specifically, the paper lacks comparison with other one-shot pruning methods that leverage similar global optimization strategies or those that use second-order information, which would provide a more comprehensive evaluation of the proposed method's novelty and effectiveness.

+ Considering specific aspects of the method that could be condensed or moved to an appendix, and particular experimental analyses or comparisons should be expanded:  Accuracy and latency speed-up with different network architectures: Res50, MobileNet, ViT. The paper should include a more detailed analysis of the trade-offs between accuracy and inference speed for different architectures and sparsity levels. This should include reporting the actual inference time speed-up achieved, not just FLOPs reduction, as the latter does not always translate directly to the former, especially with sparse operations.

+ Section 5, "Experimental setup" is written too long, it contains also the results and a description of results that is not "setup". It should be separated into a new paragraph or subsection. More breaks between paragraphs should be added for better readability. The current organization makes it difficult to distinguish between the experimental setup and the results, hindering the clarity of the paper.

+ Considering particular efficiency metrics the authors could report (e.g., runtime, memory usage) and specific methods (in Table 3) they should compare against to demonstrate their efficiency claims. The paper should provide a more detailed analysis of the computational cost of the proposed method, including the time and memory required for pruning, and compare these metrics with other one-shot pruning methods, especially those that also use second-order information.

**Other suggestions**
+ Mentioning that experiments on ImageNet-1k (lines 102, 444)  might be misleading since the fact that the authors only use the Mini-ImageNet with 10,000 samples compared to ImageNet-1k (1.2M samples). Replacing ImageNet-1k with MiniImagenet-1k is more appropriate.

+ There are two "Experimental setup" parts which are the same level as the network part (CNN running, Vision transformers, ...), which might cause confusion, suggesting making it a subsection for each type of network.

+ The so-called "Figure 3" (Line 472-484) should be a "Table 3". The text referred to that table should be revised accordingly.

+ For better readability, I suggest rather "minimize (7)" --> "minimize Eq. 7", Taylor expansion in (7) --> "Taylor expansion in Eq. 7", each call to (5) --> "each call to Eq. 5", etc.

+ Equations are written in a separate line with a center and should be enumerated, for example for line 214, line 382, and 384.

+ Although it is lookable, Figure 4 should make the text inside the figure larger for better readability.

### Questions
Suggest that the authors define the MP metric/method when it is first used and provide a citation if it refers to a specific published method.

### Soundness
3

### Presentation
2

### Contribution
2
