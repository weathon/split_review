# An Analytical Solution to Gauss-Newton Loss for Direct Image Alignment

- Decision: Accept
- Scores: 8, 6, 8

## Abstract
Direct image alignment is a widely used technique for relative 6DoF pose estimation between two images, but its accuracy strongly depends on pose initialization.
Therefore, recent end-to-end frameworks increase the convergence basin of the learned feature descriptors with special training objectives, such as the Gauss-Newton loss.
However, the training data may exhibit bias toward a specific type of motion and pose initialization,
thus limiting the generalization of these methods.
In this work, we derive a closed-form solution to the expected optimum of the Gauss-Newton loss. 
The solution is agnostic to the underlying feature representation and allows us to dynamically adjust the basin of convergence according to our assumptions about the uncertainty in the current estimates. These properties allow for effective control over the convergence in the alignment process.
Despite using self-supervised feature embeddings, our solution achieves compelling accuracy w.r.t. the state-of-the-art direct image alignment methods trained end-to-end with pose supervision, and demonstrates improved robustness to pose initialization.
Our analytical solution exposes some inherent limitations of end-to-end learning with the Gauss-Newton loss, and establishes an intriguing connection between direct image alignment and feature-matching approaches.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the task of Direct Image Alignment, which is used to estimate the relative 6DoF pose between two images. The task is strongly affected by pose initialization, which has been addressed by prior art by switching to optimization methods that increase the convergence basin, such as the Gauss-Newton loss. The authors claim that these prior methods induce bias towards the training data which limits their generalization. 
The papers main contribution addresses this problem. The authors introduce an analytical close from solution to the Gauss-Newton loss. This solution is independent of the feature representation and enables adjustment of the convergence basin based on the uncertainty in current estimates, giving control over the algorithm’s convergence properties. This property is used during the experimental evaluation, where optimization is first performed on a uniform distribution with a wider range, but then is switched out to a Gaussian with an increasingly narrowing distribution. 
Their secondary contributions are insights that the analytical solution provides. Specifically, they show that under their simplified conditions, the Gauss-Newton step is determined by the neighboring points of interest. The author conclude that this is inherently limiting in comparison to other optimization methods. 
Experimental results demonstrate superior performance in almost all results over supervised state-of-the-art methods using self-supervised descriptors. 
The appendix provides further insights on the derivations, as well as more interesting experimental results.

### Strengths
1) Well-written paper. It was a joy to read. It explains the context of the problem well, as well as establishing the necessary preliminary knowledge before delving into its actual contribution. There is a minor exception to this for the derivations (see Weaknesses)
2) Under the simplifying assumption that eps follows an isotropic Gaussian, the authors derive a close-form solution to the minimizer of the Gauss-Netwon loss in expectation. Under the assumption that the authors claim about poor generalization due to training-data-biased feature maps holds (see Weaknesses), the proposed solutions has the main advantage that it provides unbiased feature map. In addition, it provides the ability to control the basin of convergence, which in turn makes the proposed method more robust to bad initialization (cf. Fig 3). Lastly, the assumed simplification which was necessary to derive the closed-form solution has been shown to lead to negligible differences (cf. Fig 5)
3) Using self-supervised features, the proposed method is capable of outperforming supervised related work on almost all metrics. This is a strong statement, as the method can be used in conjunction with large and powerful foundation models, enabling bigger generalization due to the superior dataset sizes of such models. Therefore it is complimentary to these works.
4) The authors provide an interesting insight when using Gauss-Newton as feature matching and indicate that it may be inherently limited. This is important for informing future work in optimization-based methods. Further analysis also shows that joint training of both losses for L_GN may lead to numerical instability and may shed light on reported training divergence of prior work.

### Weaknesses
1) My biggest gripe with the paper is that their claim that motivates the approach is not empirically validated and there is no mention of such validation elsewhere. The authors claim both in the abstract as well as in the appendix that prior art use feature maps that may embed the inductive bias of the training data. While I can comprehend the underlying reasoning, such a claim needs to be empirically shown. 
For example, an experiment on out-of-distribution test sets demonstrating the superiority of the closed-form solution would back the authors claims and in turn strengthen the paper. Specifically, the authors should consider testing on datasets with significant domain shifts from the training data used for the feature extractors, such as changes in lighting, viewpoint, or object categories. This would provide concrete evidence for or against the claim that learned feature maps are biased towards their training data.
2) On the same topic of bias, I argue that the authors should explicitly state that their method still exhibits bias, but that the source of this is the underlying feature representation (result of this can be seen in Tbl. 1, Aachen Night dataset). Otherwise it may read that the authors claim their method is not biased. This is stated at the end of Section 3, but I think it should be stated clearly in either Abstract, Introduction and Conclusion section. This is a minor point however and only serves to improve clarity. It would be beneficial to explicitly state that the method's performance is still dependent on the quality and generalization capabilities of the chosen feature representation, and that the analytical solution only addresses the bias introduced by the optimization process itself, not the feature representation.
3) A little contradictory to my point in the Strengths section, I believe the math heavy section 4 and 5 could be made a little more clearer when derivations skip multiple steps. Otherwise the sections read as if one equation immediately follows from the other, which is not always the case. (e.g Eq 6. -> Eq. 7). This would enhance the readability of the paper. For instance, explicitly mentioning the mathematical operations or substitutions performed between equations would greatly improve clarity. The authors could also consider adding intermediate steps or a brief explanation of the mathematical reasoning behind each transition.
4) On the Aachen-Night dataset, the proposed method clearly suffers. The authors claim that this is due to the underlying feature representation used, which was not trained day-night correspondences. While I find the reasoning sound, it would help the authors claim to have used a feature representation that have used such correspondences during training. This in turn would again strengthen the papers contribution and indicate that it can work in different settings. It would be beneficial to see results using a feature representation trained on a dataset that includes both day and night images, or even better, specifically trained for cross-domain image matching. This would help isolate whether the performance drop is due to the feature representation or the proposed method itself.

### Questions
Questions:
- Eq. 23 leads to numerical instability. Is there a way to avoid this for stochastic optimization?
- Fig. 4) The median is stable for all tested errors. For what ranges does this hold? I.e How far can the initial error be?
- Fig. 4) Is there a similar plot for translation?

Comments:
- Sec 2, Image Alignment: Add the variable T to make the text more consistent with the rest -> "(...) estimate the relative 6DoF camera pose T."

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a closed-form solution to the Gauss-Newton loss in the field of direct image alignment. This method allows for dynamic control of the convergence basin to improve the robustness of the alignment to pose initialization. Moreover, the proposed method shows the intrinsic limitations of employing Gauss-Newton loss in deep learning, which offers an insight between direct image alignment and feature matching. The simulation experiments have shown its superior performance.

### Strengths
1.	The paper provides an analytical solution to the Gauss-Newton loss, which is a novel technology for generating a dense feature map.
2.	The paper shows the inherent limitations of feature learning with backpropagation via the Gauss-Netwon optimization.
3.	The paper is well-organized and shows the explicit introduction to notion of the Gauss-Newton.

### Weaknesses
1.	The paper is required to give more comparisons with state-of-the-art in terms of accuracy of SE3. Specifically, while the paper mentions recall with respect to translation and rotation thresholds, it lacks a direct comparison of the absolute trajectory error (ATE) and relative pose error (RPE) against established methods. These metrics are crucial for evaluating the practical applicability of the proposed method in real-world scenarios.
2.	Can the authors provide more training details of the proposed method, for example, the feature embedding network E, the learning rate, the batch size. The paper lacks specifics on the architecture of the feature embedding network E, which is critical for reproducibility. Details such as the number of layers, activation functions, and the dimensionality of the feature embeddings are missing. Furthermore, the optimization process is not clearly defined, including the learning rate schedule, batch size, and the optimizer used.

### Questions
See the weakness part

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper builds on the Gauss-Newton loss and establishes a closed-form solution for the expected optimum of this loss; it doesn't depend on the specific feature representation being used, and it enables the adjustment of the convergence basin based on assumptions about the uncertainty in the current estimates. This provides a means to effectively control the convergence properties of the algorithm. Notably, even when employing self-supervised feature embeddings, this approach attains impressive accuracy compared to the SOTA direct image alignment methods that are trained end-to-end with pose supervision. Furthermore, it demonstrates enhanced robustness in terms of pose initialization.

### Strengths
To the best of my knowledge, the closed-form derivative of the Gauss-Newton loss is innovative, and its effectiveness has been confirmed through empirical evaluation within the domain of direct image alignment, specifically with self-supervised feature descriptors - SuperPoint. What's particularly noteworthy is that this derivative can be applied to other areas to encompass methods employing backpropagation through Gauss-Newton or Levenberg-Marquardt optimization, among others.

### Weaknesses
No major weakness.
1. It would be interesting to see more discussions on the insight to the end-to-end learning framework's limitation, and a solution to that.
2. It would be interesting to see this approach handles outliers inherently.
3. It would be interesting to see this approach is applied to other areas.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
