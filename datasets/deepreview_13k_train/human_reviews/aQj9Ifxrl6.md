# Mitigating Spurious Correlations via Group-robust Sample Reweighting

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Machine learning models often have uneven performance among subpopulations (a.k.a., groups) in the data distributions. This poses a significant challenge for the models to generalize when the proportions of the groups shift during deployment.
To improve robustness to such subpopulation shifts, existing approaches have developed strategies that train models or perform hyperparameter tuning using the group-labeled data to minimize the worst-case loss over groups.
However, a non-trivial amount of high-quality labels is often required to obtain noticeable improvements.
Given the costliness of the labels, we propose to adopt a different paradigm to enhance group label efficiency:
utilizing the group-labeled data as a target set to optimize the weights of other group-unlabeled data.
We introduce a two-stage approach called Group-robust Sample Reweighting (GSR) that first learns the representations from group-unlabeled data, and then tinkers the model by iteratively retraining its last layer on the reweighted data.
Our GSR is theoretically sound, practically lightweight, and effective in improving the robustness to subpopulation shifts. In particular, GSR outperforms the previous state-of-the-art results on standard benchmarks when using the same amount of group labels. Notably, GSR even outperforms approaches that require significantly more group labels.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper considers the case when samples can be grouped (not all training samples are necessarily grouped, but all validation samples and target samples must be grouped), and we consider training the prediction model to minimize the maximum groupwise risk (loss) among all groups, namely the "worst-group risk". To train the model under the situation above, the paper considers re-weighting samples during updating the model. Different from an existing method MAPLE, the proposed method considers using the Hessian of the risk when re-weighting. Also, the proposed method introduces the "last-layer retraining" to mitigate spurious correlations and improve group robustness and also to reduce the computational cost.

### Strengths
The combination of the sample reweighting and the last-layer retraining to tackle with subpopulation shifts and (consequent) spurious correlations. As far as the reviewer's understanding, (i) a baseline method MAPLE (Zhou et al.; 2022) updates sample weights $w$ for group robustness, but it uses not the Hessian $H_{\hat{\theta}^*,w}$ but only the last-step gradient. (ii) The use of the Hessian raises the computational cost, however, the proposed method focuses on the fact that the last-layer retraining is both costless even we employ the Hessian, and effective for group robustness.

### Weaknesses
-   Technical novelty looks not well emphasized. Although the advantage above ("Strengths" section) seems to be effective, the reviewer could find it by carefully reading the paper. This fact is good to be emphasized in a early part of the paper, e.g., in Section 1.
-   The experiments are desired to be more extended. One is to increase the number of datasets (perhaps are there not so many appropriate datasets?), and the other is to qualitative discussions. (How the results are well written, but the discussion on the reasons of the results is desired more.)
-   The proposed method employs the last-layer retraining, but is it known what types of datasets are not sufficiently learned by the last-layer retraining? If so, comparing performances between methods for such datasets may be interesting.
-   Section 1: It may be better to present an example of spuriously correlated datasets due to groups, e.g., using the "Waterbirds" dataset.
-   Section 3.1: Assumption 3.1 states that, we assume that $\hat{R}({\cal D}^\mathrm{tr}; w,\theta)$ is strongly convex. However, with respect to what variable(s) should we assume it is strongly convex? All of $(w,\theta)$? Please specify.
-   Section 4.1: It states that "Secondly, calculating the Hessian inverse in Equation 6 is no longer overly expensive, because the only free model parameters are in the last layer instead of the entire deep neural network", but how the Hessian inverse can be updated in accordance with the update of $\psi$? It looks a key point of the method, so it is good to be explicitly presented.
-   Section 5.1: The method GSR-HF (Hessian-free) is examined as an ablation study, but how about the ablation study of using the Hessian but not LLR? To compare with MAPLE, this ablation study is also desired. (Perhaps is it too costly?)

### Questions
-   The proposed method employs the last-layer retraining, but is it known what types of datasets are not sufficiently learned by the last-layer retraining? If so, comparing performances between methods for such datasets may be interesting.
-   Section 1: It may be better to present an example of spuriously correlated datasets due to groups, e.g., using the "Waterbirds" dataset.
-   Section 3.1: Assumption 3.1 states that, we assume that $\hat{R}({\cal D}^\mathrm{tr}; w,\theta)$ is strongly convex. However, with respect to what variable(s) should we assume it is strongly convex? All of $(w,\theta)$? Please specify.
-   Section 4.1: It states that "Secondly, calculating the Hessian inverse in Equation 6 is no longer overly expensive, because the only free model parameters are in the last layer instead of the entire deep neural network", but how the Hessian inverse can be updated in accordance with the update of $\psi$? It looks a key point of the method, so it is good to be explicitly presented.
-   Section 5.1: The method GSR-HF (Hessian-free) is examined as an ablation study, but how about the ablation study of using the Hessian but not LLR? To compare with MAPLE, this ablation study is also desired. (Perhaps is it too costly?)

### Soundness
4

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
3

### Summary
This paper studies the challenge of improving machine learning model robustness to subpopulation shifts, where models may perform inconsistently across different subgroups within data distributions. Traditional methods typically rely on group-labeled data to tune models and minimize worst-case loss across groups, but these approaches are limited by the high cost of obtaining substantial, high-quality labels. The authors propose an alternative framework, Group-robust Sample Reweighting (GSR), which enhances group label efficiency by utilizing group-labeled data as a target to optimize weights for group-unlabeled data. The two-stage GSR approach first learns representations from group-unlabeled data and then fine-tunes the model’s last layer by iteratively retraining on reweighted data. GSR demonstrates superior performance on benchmark datasets.

### Strengths
1. The paper highlights that previous methods estimate weight gradients through approximations, but they neither account for the curvature of the loss landscape with respect to the current model nor fully capture the training dynamics. The authors’ proposed method addresses these issues under the assumptions that the inner objective is unconstrained, strongly convex, and twice continuously differentiable.

2. The experiments in this paper are thorough, and the results are promising. Across multiple datasets, the proposed approach outperforms various baseline methods, achieving state-of-the-art performance.

### Weaknesses
1. One limitation of this paper is that the proposed method relies on the inner objective being unconstrained, strongly convex, and twice continuously differentiable—assumptions whose strength is not fully clarified. The authors address these requirements by fixing the feature layers during training and only updating the linear classifier layer. However, further explanation is needed to clarify why training only the classifier layer meets these assumptions. Specifically, while fixing the feature layers simplifies the optimization landscape, it's not immediately clear that the resulting loss function with respect to the classifier weights will always satisfy strong convexity, especially given the non-linear nature of the feature representations. The authors should provide a more rigorous justification, possibly with a proof sketch, demonstrating that the Hessian of the loss function with respect to the classifier weights is indeed positive definite under the stated conditions. Additionally, the practical implications of this constraint on the model's capacity to learn complex decision boundaries should be discussed.

2. The authors' second motivation is somewhat confusing. The statement that "regularization techniques must be applied such that training with weighted objectives leads to meaningfully different solutions than using ERM" may require further clarification. It would be helpful for the authors to elaborate on how this principle is specifically reflected in the design of their method. The concern is that without a clear explanation of how the chosen regularization method interacts with the reweighting scheme, it is difficult to assess whether the observed performance gains are truly attributable to the reweighting or simply a consequence of the regularization itself. A more detailed explanation of the interplay between the reweighting and regularization is needed to strengthen the motivation.

3. The authors should conduct additional experiments to examine, without computational constraints, how much performance is lost when training the model with frozen feature layers compared to full-parameter training. This would help determine whether the performance reduction is within an acceptable range. It is crucial to quantify the trade-off between the computational benefits of freezing feature layers and the potential loss in model accuracy. The current experiments do not fully address this concern, and additional experiments are needed to establish the practical limitations of the proposed approach in terms of model performance.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel approach called Group-robust Sample Reweighting (GSR) aimed at mitigating the issue of spurious correlations, particularly under subpopulation shifts. The paper proposes a two-stage strategy that utilizes group-labeled data more efficiently by leveraging it to reweight group-unlabeled data. The key contribution of the GSR method is its use of last-layer retraining (LLR), which simplifies the bilevel optimization problem by focusing only on the last layer of the model. Through iterative reweighting of the group-unlabeled data based on influence functions and adaptive aggregation of sample gradients, GSR aims to improve the worst-group accuracy.

### Strengths
1. The proposed method is built on a solid theoretical foundation, particularly leveraging bilevel optimization and influence functions, which enhances its robustness and credibility.

2. By focusing on the last layer, the method simplifies the optimization process, making it computationally efficient.

3. The paper provides extensive experimental results across a variety of benchmarks and other understanding experiments.

### Weaknesses
1. In Section 2, it would help to be more explicit about how the proposed approach differs from previous methods. Right now, it feels like Section 3 is mostly about improving an already established objective (MAPLE). Adding the inverse Hessian in the optimization might make things more complicated than before. It’s not clear from the paper whether this extra complexity is worth the performance gains. The paper should clarify the specific limitations of MAPLE that GSR addresses beyond just computational efficiency. For instance, does MAPLE's one-step approximation of the outer loop gradient lead to instability or suboptimal solutions in certain scenarios, and how does GSR's implicit differentiation with the Hessian overcome these issues?

2. It’s not obvious how much of the performance boost comes from last-layer retraining (LLR) versus the optimization changes over MAPLE. It would be useful to see a comparison where MAPLE is combined with LLR, so we can better understand where the gains are really coming from. The paper needs to isolate the impact of LLR by comparing it with a version of MAPLE that also uses LLR. This would help determine if the performance gains are primarily due to the reweighting strategy or the LLR technique. Without this comparison, it's difficult to assess the true contribution of the proposed optimization method.

3. The claim that “over-reliance on spurious correlations mainly occurs in the last layer” feels a bit questionable. Prior research indicates that neural networks can develop biases throughout the entire network, not just in the final layer, e.g, [1]. It would be helpful to either provide more evidence or explain this assumption more clearly. The paper should provide a more detailed justification for focusing solely on the last layer, given that biases can emerge in earlier layers. It would be beneficial to discuss the potential limitations of this approach, especially in cases where spurious correlations are deeply embedded in the feature representations learned by the earlier layers. The paper should also discuss if the method is still effective when the spurious correlations are not primarily in the last layer.

4. Table 1 is missing some crucial results, especially for MAPLE, which is an important baseline here. The paper mentions that it couldn’t get the results from the original paper, but why not try reproducing them? Was there a specific issue? It feels like an incomplete comparison without those numbers. The absence of MAPLE results in Table 1 makes it difficult to evaluate the proposed method's performance against a key baseline. The paper should explain the specific challenges encountered in reproducing MAPLE's results and provide a more thorough comparison, even if it requires reimplementing the method. Without these results, the evaluation is incomplete and the claims of improvement are not fully substantiated.

### Questions
Please see above

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a method to mitigate spurious correlations and improve group robustness. The task is formulated as a bilevel optimization problem, which the authors solve via implicit differentiation. They employ Last-Layer Retraining (LLR) to ensure that the optimization problem meets the conditions required for implicit differentiation. Experiments on several datasets demonstrate the effectiveness of the proposed method.

### Strengths
- This paper utilizes implicit differentiation to calculate the gradient with respect to the sample weights and applies last-layer retraining to ensure that the risk function satisfies the conditions of convexity and continuous differentiability.

- Overall, the paper is written and organized well.

- The authors not only conducted experiments on benchmark datasets but also evaluated the performance of the proposed method in the presence of label noise. The proposed method demonstrated effectiveness in identifying noisy data.

### Weaknesses
 - There appears to be an issue with the proof in Appendix A.2. By examining the first and third lines together, we derive $\nabla_{w_i} \theta_T \approx \nabla_{w_i} \left( \theta_T - \eta \nabla_\theta \hat{\mathcal{R}}(\mathcal{D}^{\text{tr}}; w, \theta_T) \right)$ which then leads to $0 \approx - \eta \nabla_\theta \hat{\mathcal{R}}(\mathcal{D}^{\text{tr}}; w, \theta_T)$, which seems unreasonable. Furthermore, in the transition from the third to the fourth line, it is unclear why $\nabla_{w_i} \theta_T$ was eliminated. Was it because $\nabla_{w_i} \theta_T = 0$? If that is the case, the proof in Appendix A.2 could directly conclude that $\nabla_{w_i} \hat{\theta}^* \approx \nabla_{w_i} \theta_T \approx 0$. It might be worthwhile for the authors to review this part of the proof carefully. I do not believe this issue impacts the main contributions of the paper, but the authors may need to consider revising the related explanations in the paper that are based on this proof.

- In Appendix A.3, it is assumed that when $\nabla_{\theta} \hat{\mathcal{R}}(\mathcal{D}^{tr}; w, \hat{\theta}^*) = 0$, it follows that $\frac{\mathrm{d} \nabla_{\theta} \hat{\mathcal{R}}(\mathcal{D}^{tr}; w, \hat{\theta}^*)}{\mathrm{d} w} = 0$. Could the authors elaborate on why the gradient with respect to $\theta$ being zero implies that its derivative with respect to $w$ is also zero in this context?

### Questions
see weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3
