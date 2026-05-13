# Privacy-Preserving Logistic Regression Training with A Faster Gradient Variant

- Decision: Reject
- Scores: 3, 3, 3, 3, 5

## Abstract
Training logistic regression over encrypted data has been a compelling approach in addressing security concerns for several years. In this paper, we introduce an efficient gradient variant, called $quadratic$ $gradient$, for privacy-preserving logistic regression training. We enhance Nesterov's Accelerated Gradient (NAG), Adaptive Gradient Algorithm (Adagrad) and Adam algorithms by incorporating their quadratic gradients and evaluate these improved algorithms on various datasets. Experimental results demonstrate that the enhanced algorithms achieve significantly improved convergence speed compared to traditional first-order gradient methods. Moreover, we applied the enhanced NAG method to implement homomorphic logistic regression training, achieving comparable results within just 4 iterations.
There is a good chance that the quadratic gradient approach could integrate first-order gradient descent/ascent algorithms with the second-order Newton-Raphson methods, and that it could be applied to a wide range of numerical optimization problems.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors propose a privacy-preserving approach to training logistic regression based on homomorphic encryption. Their approach utilises second-order information through quadratic gradients to implement various optimisers such as NAG/Adagrad and claim this helps achieve improved convergence speeds compared to first-order methods.

### Strengths
- The paper tackles an important and useful problem, focusing on improving the convergence speed of privacy-preserving logistic regression.
- The paper is clearly written and well-structured.

### Weaknesses
 - The evaluation in the privacy-preserving setting is limited. Most of the experiments focus on the non-private setting and the private experiments compare only to a single baseline method.
- The empirical results are often unconvincing. It is not clear that the proposed quadratic gradient approach gives any clear benefit on some of the benchmark datasets in terms of convergence speed or accuracy/AUC. Specifically, the enhanced NAG method often performs worse than the baseline in terms of accuracy and AUC, despite the claim of faster convergence. This raises concerns about the practical utility of the proposed method.
- There is not enough of a comparison with prior privacy-preserving logistic regression methods to enable a clear understanding of why this method should be used compared to prior work. The lack of comparison to methods like the Simplified Fixed Hessian (SFH) approach makes it difficult to assess the novelty and advantages of the proposed method.


### Questions
1. In Tables 1 and 2, the proposed enhanced NAG method generally performs worse than the baseline method for accuracy and AUC. It is also mentioned then when compared to the Kim et al. baseline, the enhanced NAG requires one additional ciphertext multiplication and so you run it for less iterations.  Is the only advantage of the enhanced NAG computation time?
2. In addition to the point above, there could be a more thorough set of experiments for the privacy-preserving setting. Restricting the comparison to 4 iterations vs. 7 does not do enough to highlight when the enhanced NAG method should be used. There is a likely trade-off in terms of convergence and compute that is not being fully explored in the experiments.
3. As far as I can tell, the proposed quadratic gradient method is a straightforward extension to the work of Bonte and Vercauteren (2018). Why do you not compare to their method in Section 5? I feel the privacy-preserving experiments are lacking further baselines.
4. In Line 185, is the gradient meant to have a subscript i here? Is is meant to be referring to $\nabla_\beta$?
5. Minor point: There are a few typos that could be corrected — L477: pulbic → public, L248: practicable -> practical, L269: setted → set

### Soundness
2

### Presentation
3

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
The paper proposes a new optimization technique for privacy-preserving logistic regression training called quadratic gradient. This method combines elements from first order gradient algorithms and the second-order Newton-Raphson method. The variant constructs a diagonal Hessian approximation that allows for the computation of an optimized gradient update without recalculating the computationally expensive Hessian matrix. As a result, the quadratic gradient facilitates faster convergence by leveraging curvature information while retaining the simplicity of first-order methods.
The authors show that quadratic-gradient versions of Nesterov Accelerated Gradient (NAG), Adagrad, and Adam optimizers converge, and, in most cases, demonstrate strong performance in terms of convergence speed, by empirical evaluation on multiple datasets. The authors apply the quadratic gradient-enhanced NAG to homomorphic encryption-based logistic regression training, showing comparable model accuracy within only a few iterations.

### Strengths
The quadratic gradient approach provides a new combination of first-order gradient and second-order Newton-Raphson methods. Multiple experiments were considered to demonstrate the improvements in convergence speed achieved by the enhanced NAG, Adagrad, and Adam algorithms. The paper aims to address a practical challenge in encrypted logistic regression training, where efficient computation is crucial.
The quadratic gradient concept builds on several ideas from the literature, which are well reported in the paper.

### Weaknesses
 - The claim that the enhanced algorithms achieve significantly improved convergence speed compared to traditional first-order gradient
methods is not very well supported, as the performance of the algorithms varies across different datasets. The enhanced Adagrad and Adam methods do not achieve faster convergence on the iDASH, and while they do perform better on other datasets, it is hard to assess the overall extent and consistency of the improvement. Namely, the authors mention: _"Although the enhanced Adagrad and Adam methods do not achieve faster convergence than their original counterparts on the iDASH genomic dataset, they demonstrate clear advantages in all other cases. The reason for this discrepancy is beyond the scope of this paper and will be addressed as part of future work."_. It is worth providing additional analysis in this work on why certain datasets showed less improvement, as it would help identify conditions under which the method is most effective (i.e., how do the methods behave under different number of dimensions, dataset size, etc.). Providing bounds on convergence speed or computational efficiency would also strengthen the contribution.
- The paper's writing makes its focus somewhat unclear. The quadratic gradient method is proposed specifically as a technique for privacy-preserving logistic regression, but a significant portion of the paper is dedicated to showing that quadratic gradient can perform better than first-order gradient methods in the general (non-private) setting. The private setting is proposed as an application.

### Questions
- Further insights (through experiments and/or theory) should be provided on the performance of the quadratic gradient approach (see weaknesses).

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a secure training algorithm for logistic regression models. Specifically, the proposed training algorithm uses a gradient estimator called quadratic gradient which preconditions the gradient using the estimated second-order information. To reduce the computational burden, the second-order information (i.e., Hessian) is approximated as a diagonal matrix. The training algorithm is implemented with a homomorphic encryption framework.

### Strengths
- The proposed algorithm employs the fixed diagonal approximation of Hessian which reduces computational cost for calculating the Hessian during the training and can be approximated in the encrypted form.
- The proposed quadratic gradient is applied to three optimization algorithms: Nesterov’s Accelerated Gradient (NAG), AdaGrad, and Adam, and their performance is compared across various datasets.

### Weaknesses
 - The proposed quadratic gradient seems to be similar to the preconditioned gradient, which has long been utilized in the optimization community, and there exists a substantial body of literature on this topic. The proposed work seems to make an incremental contribution, as the quadratic gradient appears to be a rebranding of the existing preconditioned gradient. In addition, the idea of approximating the parameter-dependent Hessian matrix with a parameter-independent input covariance matrix was introduced in the literature. For example,
  1. Ida, Yasutoshi, Yasuhiro Fujiwara, and Sotetsu Iwamura. “Adaptive Learning Rate via Covariance Matrix Based Preconditioning for Deep Neural Networks.” In Proceedings of the Twenty-Sixth International Joint Conference on Artificial Intelligence, IJCAI-17
  2. Mehta, Harsh, Walid Krichene, Abhradeep Guha Thakurta, Alexey Kurakin, and Ashok Cutkosky. “Differentially Private Image Classificafrom Features.” Transactions on Machine Learning Research, November 29, 2022.

- The proposed algorithm is implemented using the existing homomorphic encryption framework. It is unclear what the significance of the use of quadratic gradient in the context of homomorphic encryption. The paper does not adequately explain why this specific gradient approximation is advantageous or necessary within the constraints of homomorphic encryption, especially given that the diagonal approximation of the Hessian is already computationally efficient. The work needs to clarify the specific benefits of the proposed method in this setting.
- The empirical results are not well explained. The performance comparison with the existing algorithm by Kim et al. shows that the proposed algorithm achieves lower accuracy than the baseline method on some datasets (for example, Edin and pcs datasets). The paper lacks a detailed analysis of why the proposed method underperforms in these cases. Furthermore, the paper does not provide sufficient insight into the convergence behavior of the proposed method compared to the baseline, especially given that the proposed method introduces a preconditioning step.
- The presentation of the paper can be improved.

### Questions
- The empirical results presented in Section 5 require further explanation. The proposed method uses twice as much memory as the baseline, which is understandable given that it needs to store diagonal entries of the preconditioning matrix. However, it seems to be faster than the baseline in terms of the learn time. What exactly does the learn time measure and why is it the case? Given that the proposed algorithm includes an addition step compared to the baseline, it is not clear why the proposed algorithm is faster.
- What is the motivation for approximating the diagonal entries of Hessian with the row-wise sum of $\bar{H}$?
- I am not sure how the formulation presented in line 176 - 181 help better explain the idea of proposed work.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a preconditioning scheme for accelerating gradient-descent style algorithms. The paper explains how to incorporate this scheme into the logistic regression fitting with homomorphic encryption framework introduced in prior work (Kim et al.  2018a).

Experiments on a variety of datasets in very tiny plots show that the proposed preconditioner improves the training convergence and/or training loss for nesterov accelerated gradient, adagrad, and adam. However, comparisons in the homomorphic encryption framework to Kim et al. are inconclusive as often the Kim et al. version can improve accuracy at a cost of a few more minutes of training.

### Strengths
This paper proposes a preconditioner that improves the training loss or training convergence of 3 different styles of gradient descent on 8 datasets.

### Weaknesses
Before discussing  weaknesses, it is important to add some context to the paper. Multiplying the gradient by a positive (or negative) definite matrix during gradient descent/ascent is known as preconditioning.  This is perhaps the connection the paper was looking for on Line 178. Thus this paper is mostly about finding a satisfactory preconditioner. With this context, one can observe the following weaknesses.

1) The literature on preconditioning is huge and classical texts such as Numerical Optimization by Nocedal and Wright discuss it in depth. When the main contribution is a preconditioner, not only does the author need to start with the classical practical preconditioners mentioned there, but also conduct a literature search to identify what's new and check if this specific preconditioner has already been proposed. On top of that, since so many preconditioners and variations are available, it is always possible to find something that works well for any handful of datasets and a theoretical analysis of when it is superior is needed.

2) The proposed preconditioner is a small variation of Kim et al. As far as I can tell, it adds absolute values and an additive epsilon term that is a fairly common techniques for making matrices more positive definite (or negative definite, depending on the sign).

3) The paper does not propose anything new on the privacy side. The framework of Kim et al. is re-used.

4) The paper offloads some computation on the client, specifically the computation of the preconditioner. It raises the question of what is reasonable to offload on the client and what is not.
- One possibility is to offload nothing onto the client -- the client simply uploads the dataset to the cloud for long term storage and the cloud servers can provide various analytics functionality in the future. However, for this setting the paper needs a privacy preserving preconditioner computation.
- On the other hand, if the client is already computing the preconditioner, why wouldn't the client run gradient descent (or sdg for large datasets) to train the logistic regression themselves? There are many software packages that do this and it is a very fast computation.

5) Most of the experiments in the paper suspiciously only focus on the training loss and the paper explicitly refuses to examine other metrics, such as training classification error, testing loss, and testing classification error. Since loss and classification error are not perfectly correlated, and can exhibit strange behaviors when an optimizer is changed, it raises red flags that the paper should avoid (by running these more complete experiments).

### Questions
I do not have any questions.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper introduces an enhanced NAG (Nesterov Accelerated Gradient) method for efficient training of logistic regression, specifically designed for secure training under homomorphic encryption. The empirical study shows that the proposed method achieves comparable results in just four iterations.

### Strengths
- S1: The proposed enhanced NAG method is well-analyzed theoretically.
- S2: The advantages of the enhanced NAG method are demonstrated empirically in both plaintext and ciphertext settings. Under homomorphic encryption, it achieves comparable accuracy to baselines with improved efficiency in learning time and iteration count.
- S3: The paper is well-organized and easy to follow.

### Weaknesses
 - W1: The related work section lacks sufficient detail. In particular, the relationship to other learning algorithms under FHE, beyond just NAG, should be more clearly described. Specifically, the paper should discuss how the proposed method compares to other gradient-based optimization techniques adapted for FHE, such as those using stochastic gradient descent or Adam, and whether these methods have been explored with similar acceleration techniques.
- W2: The experimental baseline is limited to a single method. Given the existence of various homomorphic computation methods, comparisons with these alternatives are necessary to establish the novelty of the proposed approach. The paper should include comparisons with other FHE-compatible machine learning algorithms, even if they are not directly based on NAG, to demonstrate the specific advantages of the proposed method. This could include methods that use different approximation techniques for non-linear functions or alternative optimization strategies.
- W3: Although the paper shows that the proposed method accelerates learning computation in FHE, the improvement in performance is modest, and there is a slight drop in accuracy. The paper should also discuss potential applications where these specific efficiency gains are essential. The paper should provide a more detailed analysis of the trade-off between the reduced iteration count and the slight decrease in accuracy, and discuss scenarios where this trade-off is beneficial, such as real-time processing or resource-constrained environments.

### Questions
Address W1, W2, and W3

### Soundness
3

### Presentation
3

### Contribution
3
