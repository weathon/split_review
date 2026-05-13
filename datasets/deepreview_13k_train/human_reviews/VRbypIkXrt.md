# MetaOptimize: A Framework for Optimizing Step Sizes and Other Meta-parameters

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
We address the challenge of optimizing meta-parameters (i.e., hyperparameters) in machine learning algorithms, a critical factor influencing training efficiency and model performance. Moving away from the computationally expensive traditional meta-parameter search methods, we introduce MetaOptimize framework that dynamically adjusts meta-parameters, particularly step sizes (also known as learning rates), during training. More specifically, MetaOptimize can wrap around any first-order optimization algorithm, tuning step sizes on the fly to minimize a specific form of regret that accounts for long-term effect of step sizes on training, through a discounted sum of future losses.  We also introduce low complexity variants of MetaOptimize that, in  conjunction with its adaptability to multiple optimization algorithms, demonstrate performance competitive to those of best hand-crafted learning rate schedules across various machine learning applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper provides a framework to dynamically update hyperparameters such as learning rate during training.

### Strengths
The proposed framework contains some existing algorithms as specials cases.

Their explanations are clear and facilitates easy understanding.

### Weaknesses
While the explanations provided are clear and easy to understand, some aspects are not thoroughly covered, e.g. Equation (5) would benefit from additional intuition or theoretical support. Specifically, the connection between the backward view update and the forward view update is not rigorously established, and the conditions under which the approximation is valid are not clearly defined. The paper lacks a discussion on the potential impact of the approximation error on the overall performance of the proposed method. 

There are established lines of work on gradient-based hyperparameter optimization using bilevel optimization. Discussing the connection between the proposed method and these existing approaches would strengthen the paper. The current discussion does not adequately address the similarities and differences, particularly in terms of computational complexity, convergence properties, and applicability to different problem settings. A more detailed comparison is needed to position the proposed method within the broader landscape of hyperparameter optimization techniques.

### Questions
Please discuss Equation (5) and the connection between the proposed method to bilevel optimization.

### Soundness
2

### Presentation
2

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
The submission aims to adapt the learning rate while model training. By minimising the regret of the historical model training, the learning rate is updated by the meta gradient computed by a proposed MetaOptimise framework wrapped with the proposed approximation method to reduce the computational cost, especially that caused by the Hessian matrix. The method is empirically texted on both image and language datasets with learning curve and computational cost shown as demonstration for efficiency.

### Strengths
1. The motivation that learning learning rate is clear and practical. 
2. The operation details are discussed and given in the appendix for readers to have a broad insight.

### Weaknesses
1. The paper is not presented clearly. 
2. The experiment results do not cover the generalisation performance of the trained models by different optimisations. For example, there is no direct comparison of the accuracy of the test set. The top 5 accuracy applied in the paper can reflect the performance of the optimisers but usually top 1 accuracy is more important. 
3. As learning rate learning is usually a special case of optimiser learning, some previous works are missing for comparison [1,2,3]. 
4. The proposed backward-view update is similar to the forward mode differentiation (FMD) in [1] and the follow-up study on learning rate learning paper [2]. In addition, Equation 1 only contains the training information, the motivation for optimising the learning rate against this objective function is not clear and a follow-up question can be what benefits are achieved by optimising this. 
5. I believe approximate Hessian with either diagonal matrix or block diagonal matrix is common in the precondition optimisation field, L-approximation is another special ly format which is parallel with the others. Stating it as containing existing algorithms as special cases may be overclaiming. Also, it could be interesting to know that with diagonal matrix approximation, the Meta-optimize works and it will definitely reduce computational cost. 
6. Suggestions: The reference format is a little mass, which does not affect my score for this paper.  For example, DoG is published in ICML 2023 while in the reference it is the arXiv version.

### Questions
1. In terms of time-space complexity comparison, MetaOptimize does not show a significant advantage on ImageNet but on TinyStoires. Can the authorise explain why? 

Also, see the weaknesses section.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes a MetaOptimize framework that dynamically adjusts hyperparameters (like step size) of base algorithms (like SGD and Adam), to minimize a discounted sum of future losses. Specifically, this work adopts an idea similar to eligibility traces in reinforcement learning to construct the future loss, uses base algorithm to minimize this future loss to output the weight vectors, leverages the weight vectors to compute the Jacobian matrix, and finally takes the Jacobian matrix as input of a meta algorithm to update the hyperparameters across different tasks/times. Complexity-reduced variants of MetaOptimize (include approximation version and Hessian-free version) are also proposed. Experiments on classification and language tasks are further conducted to validate the effectiveness of the proposed MetaOptimize framework. I did not check the proof line by line, because all the proofs in the appendix are about derivative computation, and such computation is basic.

### Strengths
(1)	This paper provides a novel MetaOptimize framework to meta-learn hyperparameters of base machine learning algorithms. In particular, the introduction of eligibility traces (from reinforcement learning) into the field of hyperparameter optimization is new.

(2)	The further proposed approximation version and Hessian-free version make great efforts to reduce the complexity of the MetaOptimize framework.

(3)	The proposed MetaOptimize framework in Algorithm 1 is general and really wraps around any first-order optimization algorithm.

(4)	Experiments on image classification and language modeling benchmarks are extensive, demonstrating the effectiveness of the proposed algorithm when compared with hand-crafted learning rate schedules.

### Weaknesses
 **Major**

(1) I admire that the introduction of eligibility traces into hyperparameter optimization is novel. However, when introducing an existing technique (from reinforcement learning) into your research problem (hyperparameter optimization), some theoretical or insightful analysis should be provided. For example, what is the insightful relationship between the objective in Eq.(5) and the future loss in Eq.(1)? Minimizing the objective in Eq.(5) can provably minimize the future loss in Eq.(1)? Such theoretical analysis is necessary, otherwise the current version in my opinion looks more like a direct application of eligibility traces (i.e. Eq.(5)) into hyperparameter optimization, hence resulting in limited insights. Specifically, the paper lacks a clear explanation of how the backward view update in Eq. (5), which approximates the forward view update in Eq. (4), truly optimizes the discounted sum of future losses defined in Eq. (1). The connection between minimizing the objective in Eq. (5) and achieving a provable reduction in the future loss of Eq. (1) is not established, making the theoretical foundation of the method unclear. The paper should include a more rigorous analysis of the approximation error introduced by using the backward view and its impact on the overall optimization process.

(2) The introduction of the Jacobian matrix $\mathcal{H} _{t}$ in line 222 is novel, but the bilevel-optimization (i.e. base-meta algorithm optimization) framework in Algorithm 1 is not new for me. Besides, it will be better to utilize existing theoretical analysis for bilevel programming (e.g. [1] and references therein) to derive specific theoretical results (e.g. the stability or generalization guarantees) for the proposed MetaOptimize framework in Algorithm 1. The paper does not adequately address the theoretical properties of the proposed bilevel optimization framework, particularly in terms of convergence and stability. While the Jacobian matrix $\mathcal{H}_t$ is a novel component, the overall framework still relies on bilevel optimization, and the paper should explore existing theoretical results from this area to provide a more solid theoretical foundation. The lack of such analysis makes it difficult to assess the robustness and reliability of the proposed method.


**Minor**

(3) There exists too many blank spaces in the paper. For example, between Eq.(10) and Eq.(11), I would suggest use $(\frac{\mathrm{d}y _{t+1}}{\mathrm{d} \beta _{\tau}}, \frac{\mathrm{d}x _{t+1}}{\mathrm{d} \beta _{\tau }}, \frac{\mathrm{d}h _{t+1}}{\mathrm{d} \beta _{\tau}})^{T} = G _{t}(\frac{\mathrm{d}y _{t}}{\mathrm{d} \beta _{\tau}}, \frac{\mathrm{d}x _{t}}{\mathrm{d} \beta _{\tau }}, \frac{\mathrm{d}h _{t}}{\mathrm{d} \beta _{\tau}})^{T}$ to save space, and give more theoretical explanations. Similar problem also exists in Eqs.(12)-(16).

(4) Line 075, sum of future loss -> sum of future losses

(5) Eq.(2) has a misleading typo: $x _{t} = Alg _{base} (x _{t}, \nabla f _{t}(w _{t}), \beta _{t})$?

(6) Throughout the whole paper, the differential operator is $\mathrm{d}$ (mathrm{d}), not $d$.

(7) Line 138, times $\tau > t$.) ->  times $\tau > t$).

(8) Line 206, two case

(9) Line 208, what does $|H _{t}|$ mean?

(10) Line 234, $d,x _{t+1}/d, h _{t}$.

(11) Line 318, zeroed out; -> zeroed out,

### Questions
(1)	Can you give more theoretical explanations for why gradient descent in Eq.(5) can minimize the future loss defined in Eq.(1) ? Or can you give more theoretical analysis for the benefits of introduction of eligibility traces into hyperparameter optimization?

### Soundness
3

### Presentation
2

### Contribution
2
