# Gradient descent with generalized Newton’s method

- Decision: Accept
- Scores: 5, 8, 6, 6

## Abstract
We propose the generalized Newton's method (GeN) --- a Hessian-informed approach that applies to any optimizer such as SGD and Adam, and covers the Newton-Raphson method as a sub-case. Our method automatically and dynamically selects the learning rate that accelerates the convergence, without the intensive tuning of the learning rate scheduler. In practice, out method is easily implementable, since it only requires additional forward passes with almost zero computational overhead (in terms of training time and memory cost), if the overhead is amortized over many iterations. We present extensive experiments on language and vision tasks (e.g. GPT and ResNet) to showcase that GeN optimizers match the state-of-the-art performance, which was achieved with carefully tuned learning rate schedulers.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes a robust optimizer for training deep neural networks on a diverse range of tasks, covering image classification, segmentation and detection, natural language generation, and natural language understanding. The proposed optimizer, Generalized Newton (GeN), is derived by taking a second order Taylor expansion of the loss function for a given search direction and analytically deriving the optimal learning rate given the quadratic approximation along this search direction. It generalizes the Newton method by allowing the search direction to be produced by any stochastic first-order optimization method (e.g., SGD or Adam). The derived learning rate requires the computation of Hessian-vector products and gradient-vector products. The proposed GeN implementation estimates these Hessian-vector products and gradient-vector products by using two additional forward passes, fitting a quadratic to the three points in the graph of the loss function, and then computing the learning rate analytically.

### Strengths
1. Clarity: The proposed method is conceptually simple.
2. Clarity: The paper is relatively clear and well written.
3. Quality: Diverse range of experiments on relatively larger neural networks (e.g., RN-152 and ViT-L)
4. Significance: Promising numerical results on the considered task suggest that the method may be of practical use.
5. Significance: Good discussion of limitations and the added computational complexity, as well as strategies for mitigating these (e.g., infrequent computation of the learning rate, and tracking an exponential moving average of the computed values).

### Weaknesses
There are some weaknesses to be addressed in the experiments and the related work.

Experiments:
1. Why are the vision models on image classification tasks only trained for 5 or 10 epochs? It is common to use much longer training schedules for CIFAR10/100/iNat/ etc. The choice of such short training runs makes it difficult to assess the true potential of the proposed optimizer, especially when compared to standard optimizers that are often run for hundreds of epochs. The reported results may not reflect the asymptotic performance of the method.
2. The loss in Figure for the RN18 trained with GeN-SGD exhibits a step-wise learning rate decay, which is strange since the proposed method cannot produce step-wise decay due to the strong EMA smoothing of the learning-rate in Alg.1. This needs to be clarified or corrected. The observed behavior suggests a potential implementation issue or an unaccounted-for mechanism influencing the learning rate, which requires further investigation.
3. The segmentation/detection experiments are not clear. Are you training on Penn-Fudan or COCO? What are you evaluating on? Are there pretrained components to your model or the neck/head? What are the 5 losses you're using? The lack of clarity regarding the dataset, evaluation protocol, and model architecture makes it difficult to reproduce the results and to properly assess the method's performance on these tasks. The specific losses used should be clearly defined, and the training procedure should be described in detail.

Related work is relegated to a small discussion in the appendix and is lacking much many obvious references, including stochastic newton and other stochastic second-order or sketching methods. The comparison with D-Adaptation is also lacking in the main text and the experiments (except Figure 8, but here all models are only trained for 5 or 10 epochs as well). The absence of a thorough discussion of related work, particularly stochastic second-order methods, limits the understanding of the novelty and contribution of the proposed method. The comparison with D-Adaptation is insufficient, and more comprehensive experiments are needed to establish the relative performance of GeN.

### Questions
Please see above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work proposes a new method of step size selection algorithm that is computationally efficient and can be combined with the descent direction provided by any off the shelf optimizer. The authors find a good step size by using gradient and Hessian information to find and fit a quaratic function of the step size that can be approximatly minimized analytiacally. They use a computationally efficient approach that does not require additional backward passes or Hessian vector products, as opposed to typical attempts that require relativly expensive power iteration or trace estimation. The authors then benchmark this method on several different tasks  ranging from large  language  models to convex functions. While the method is slightly more expensive than vanilla step size  schedules, it outperforms other methods on most benchmarks.

### Strengths
I think this is an interesting approach that attempts to bridge older ideas in optimization (subspace optimization, quadratic interpolation) with the modern challenges of deep learning. The method is well motivated from an optimization  perspective and converges under the typical assumptions (smoothness, convexity). One of the key advantages  of this method is that it is more computationally efficient than other second order information type methods, which is paramount for adoption by those training big models (which is most people these days).  The authors are honest about what extra compute is required when and how the additional costs can be  minimized.

The presentation of this method has a few difficulties (addressed below) but overall is fairly clear, I particularly think Figure 2 summarizes the idea well. The resulting algorithm is also fairly simple and  would not be a challenge to implement or modify. I additionally like the experiments showing that the method is able to correct for poor initial guesses at a step size. To test the algorithm the authors use a very wide  array of tasks and models which is  helpful. I particularly like the choice of using test functions which offer more insights into the dynamics of various algorithms and step sizes prior to training large models, it’s a cheap experiment that can offer  more insight despite being less useful in practice than deep models. 

Overall I think this is an interesting idea that is mostly presented well and has a diverse set of experiments showing strong performance.

### Weaknesses
While minor I do feel some of the notation is confusion, for example using bold capitals for both vectors and matricies such as the gradient $\mathbf{G}_t$ and Hessian $\mathbf{H}_t$ in equation 2.2. Another example is in equation 3.2, which like the ratio of two quadratic forms when really its an inner product scaling the gradient in the numerator and a quadratic form in the denominator. It may be better to stick to typical notation for the gradeint like  $\nabla L$ or at the very least use a lower case letter.

My concern regarding the algorithm itself is that I do not see a step to actually verify that the learning rate chosen in combination with the diretion ends up with a descent direction. This would be a simple thing to fix, but would require some (small) extra computation. More classical methods like Armijo line searches are guranteed to decrese the loss, where it appears here that the algorithm is very reliant on the loss being locally quadratic enough such that the loss between the samples points used to form the quadratic does not increase drastically then go back down. Given the empiracle performance of the algorithm it’s unlikely this actually happens, but I don’t see why it couldn’t. 

The algorithm appears to perform well frequently, but is not always optimal. While I don’t think its reasonable to expect a new algorithm to  be universally best, it would be nice  to see some thoughts on why it underformed in the instances it did.

Typos:

On line 208 should it be “we apply gradient descent” rather than “we apply the gradient descent”?

line  842, the grid has $C10^{-k}$ followed by $k=-5,\ldots,0$. I’ll assume this is a typo rather than having learning rates around $10^5$

### Questions
- When you find the step size by minimizing the quadratic, do you ensure that the step  is actually a good one? Given the highly nonconvex and nonsmooth nature deep learning loss surfaces I would be concerned that you could get unlucky and the minimizing step size would actually significantly increase the loss (i.e. the interpolating points happen to have low loss values but any point on a convex combination between them has a high loss).
- Given that the solution to the quadratic $\eta^*$ should be optimal, what is the motivation for instead taking an exponential moving average of learning  rates? While  it is mentioned that it   helps in C.3, is the instability prohibitive  if you just use $\eta^*$? If so is there a reason why?
- Could the authors be more clear on the connections between minimizing a quadratic defined by $\ge3$ points  and the finite differencing schemes discussed in appendix  A.1 and A.3?  It seems to me  that A.1 and A.3 are not actually  referenced in the  main text aside from a  justification for minimizing  error  in the step size chosen. The connections between these methods could be clarified, especially for an ML audience that is typically very averse  to anything involving  finite differences. It was  additionally  unclear  to me why the  scheme involving $L_-,L_0,L_+$ is equivalent  to minimizing equation 2.4 until reading A.3, so perhaps mentioning this earlier would be beneficial.
- Is there any way to  measure  the estimation of   error that the proof in A.4 addresses? Central limit theorem  arguments can be very  loose at times  especially in situations without a large batch size (perhaps this is why some experiments required a larger than usual batch). Is it possible to show the error on models that are  small enough to actually compute $\eta^*$? 
- Could the authors clarify how many  points they sample to form the quadratic? In Algorithm 1, three points are used, in appendix C.2 5 is reccomended, and in Figure 2 there  appear to be 11 and 10 for the ResNet and GPT2 respectivly. Given this is one of the more important and expensive hyperparaemters, I would be interested to know the sensitivity and if results would differ significantly for fewer/more  points. 
- When comparing to other algorithms, such as in Figure 8, are the hyperparemters for those algorithms/schedules tuned or taken from other  works using these configurations?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes an adaptive learning-rate scheme based on a local quadratic approximation of the loss function during optimization. By approximating the loss as a locally quadratic function of the learning rate along some descent direction, the optimal learning rate can be easily computed. The authors show that this scheme is successful for a wide range of descent directions derived from other optimization algorithms.

### Strengths
To my knowledge, all derivations are correct for the proposed method.

Including a discussion and short theoretical analysis of the approximation error is valuable too. This provides useful insight on when the method is most likely to be successful (at larger batch sizes).

The paper includes a diverse set of experiments using modern deep-learning architectures. The performance of the proposed method remains competitive with tuned learning rate schedules across all tasks. There is improved performance in settings where AdamW has likely been less aggressively tuned, but other methods do outperform the proposed techniques in some tasks --- I think this is quite reasonable given the ease of implementation and lack of tuning required for GeN.

### Weaknesses
The major weakness of this paper is that the proposed method is not novel. This technique has been used before within the optimization literature and has even been applied to deep-learning optimization problems. The clearest direct reference is [1], which uses this technique exactly. These techniques are also closely related to quadratic interpolation which has been studied within the optimization literature [2]. QLAB [3] is another method that applies the two-point quadratic interpolation approach (instead of the 3-point zeroth-order method).

Another missing related work is [4], which proposes a computationally efficient solution to Equation 2.3 directly using Hessian-vector products.   The authors should compare with this work to determine the relative change in wall-clock time to achieve a threshold loss.

Overall, this constitutes a significant oversight in the placement of this work among the rest of the literature. Several claims made in the paper, e.g., "To our best knowledge, GeN is the first automatic optimizer that is applicable to the general optimizers" are overly strong even without the related work that I have introduced here --- adaptive learning rate methods are a well-studied area.

As a secondary point, I found it highly confusing to refer to this method as "Generalized Newton's Method" when there is no second-order computation. The proposed method applies a local quadratic approximation to choose a learning rate adaptively. It can be combined with a second-order preconditioner, but as it stands this technique is not related to Newton's method.

The paper can be difficult to follow at times. The derivation of the optimal learning rate should be laid out more clearly (as it is in the original works). For example, you could write down how the quadratic equations are combined to compute the coefficients. And then the form of the optimal learning rate in terms of these coefficients, before the final derivation shown in Eq. 3.3.

I felt that the DCGAN experiments in the appendix added little to the paper. The final generation quality is quite poor, and it isn't clear that a quadratic approximation to the loss is suitable for this bilevel optimization problem. That said, it is interesting that it works somewhat.

### Questions
I cannot recommend that the paper be accepted in its current form. The proposed method is presented as a novel contribution despite it existing in the literature for at least four years --- and related methods have been used in adjacent fields for longer. The new experiments provide an updated evaluation of this technique that might spur the community to consider using it. However, the paper would require a significant rewrite to reposition itself.

It would be interesting to see how the approximation error compares to other approaches like QLAB [1] or ADLER [2] that utilize a first-order and second-order solution to the local quadratic approximation. Intuitively, these techniques should achieve a lower approximation error.


[1]: "QLABGrad: a Hyperparameter-Free and Convergence-Guaranteed Scheme for Deep Learning", Fu & Wu. 2023

[2]: "ADLER - An efficient Hessian-based strategy for adaptive learning rate", Balboni & Bacciu. 2023


-----

**Post-rebuttal** 

The authors addressed my concerns regarding novelty and have provided a revised version that gives credit to the related work --- most prominently the LQA method of Zhu et al. that implements the same Algorithm 1 with SGD updates. The authors also provide greater emphasis on the curve-fitting approach they introduced that allows greater than 3 loss evaluations to be used in estimating the optimal learning rate.

Overall, I feel that the curve-fitting approach is an interesting add-on but not a prominent part of this submission --- the authors primarily use Algorithm 1 which uses only three points as in LQA. And, I maintain that the LQA algorithm introduces most of the key methodological ideas from this work (quadratic interpolation for adaptive learning rate selection). However, this work includes some novel algorithmic components, a thorough empirical evaluation against modern deep learning benchmarks, and some novel theoretical analysis to help justify the method.

On balance, I have increased my score to reflect the improvements to the submission and recommend acceptance.

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces the Generalized Newton’s Method (GeN), a second-order optimization technique designed to dynamically adjust the learning rate for optimizers like SGD and Adam without manually tuning hyperparameters. The proposed method integrates Hessian information to select an optimal learning rate for each iteration, improving convergence speed with minimal computational overhead. Extensive experiments demonstrate that GeN achieves performance comparable to SOTA optimizers with carefully tuned learning rate schedules.

### Strengths
1. **Approach:** The paper presents a novel way to integrate second-order information into optimizers like SGD and Adam which is a significant improvement over traditional first-order methods. The method is generalizable to different optimizers and models, making it versatile and easy to adopt.

2. **Computational efficiency:** GeN claims to achieve better convergence without more computational overhead, particularly useful for large-scale models. 

3. **Extensive experiments:** The empirical results on diverse datasets (ResNet, GPT, etc.) provide robust evidence that GeN performs well across various tasks. 

4. **Theoretical:** The paper gives a convergence analysis of GeN, including error analysis for optimal learning rate estimation and an in-depth explanation of the second-order Taylor expansion.

### Weaknesses
1. **No GitHub repository:** At this day, there is no open-source implementation provided. 

2. **Plots:** Several plots (such as Figures 1 and 8) could be improved. For example, in Figure 8, placing the legend below the figures would enhance clarity, especially since they share the same optimizer legend.

3. **Computational overhead:** While the paper claims minimal overhead, the two extra forward passes in the training loop may introduce non-trivial complexities in practical implementations, especially on large distributed systems. A more detailed discussion or experiments about this could strengthen the paper. For example, replace the number of iterations by the training time. The analysis of the forward/backward complexity, $B \approx cF$, lacks precision; the constant $c$ is often cited as approximately 5, but the paper does not discuss the implications of this value on the relative speed estimation. A more detailed discussion on this point would be valuable.

4. **Tuning hyperparameter:** It is unclear how authors chose hyperparameters for AdamW, SGD, etc… A grid search experiment or reference to the literature could strengthen the paper. Providing more details on the tuning process would enhance the reproducibility of the results.

While this paper presents a highly interesting and innovative approach with GeN, its main weakness lies in the experimental section. The experimental results are promising but lack rigor in the precise description of the setup, particularly regarding training parameters and whether the models were pre-trained or not. Additionally, the paper would benefit from a more comprehensive discussion of related work, especially in the context of parameter-free methods (for e.g Francesco Orabona and Tatiana Tommasi. Training deep networks without learning rates through coin betting. 2017. and others papers…) would strengthen the theoretical and practical positioning of GeN. Addressing these gaps in the experimental setup and related work would significantly enhance the impact of the method.

5. **Figure 2:** The concept of $g_t^{\text{optim}}$  in the illustration is unclear. It would be helpful to clarify which optimizer (SGD?) is used in this figure. Can you add a brief explanation of in the figure caption or main text, specifying which optimizer it refers to ?

6. **Figure 4:** We can see training instability with sudden changes in curvature. Surprisingly (for me), ResNet-152 has a worse train accuracy than ResNet18 for GeN-SGD but not for GeN-AdamW. It would be better to run the same experiments with basic SGD and AdamW for comparison. The test loss for ResNet-152 appears quite unstable at the beginning of the training process.

7. **Line 311:** For a more precise discussion about the forward/backward complexity  $B \approx cF$ , consider referring to the paper “On the Complexity of Nonsmooth Automatic Differentiation” by Bolte et al. (2023). You also have "Evaluating Derivatives: Principles and Techniques of Algorithmic Differentiation" by Griewank et al. (2008), or the Bauer-Strassen theorem. The constant  $c$  is approximately 5 (in my knowledge), which might improve the relative speed estimation. A more detailed discussion on this point would be valuable. Moreover, could you give more insights into the sentence “GeN optimizers are roughly 60% as fast as the base optimizers”? Please, can you :
- Incorporate the suggested references into their discussion of forward/backward complexity.
- Clarify how they arrived at the 60% speed estimate and how it might change with the more precise constant c ≈ 5.
- Provide a more detailed explanation or derivation of the relative speed calculation.

8. **Figure 6:** Perhaps use 1000 iterations for Plot 3 to improve comparability? The same suggestion applies to Figure 7. Additionally, what happens if a different initialization for  $x_0$  and  $y_0 $ is used? Is it robust? Please, can you :
- Update Figures 6 and 7 to use 1000 iterations for all plots for better comparability.
- Conduct and report results from experiments with different initializations to demonstrate the robustness of their method.

9. **Figure 8:** The number of iterations is unclear—10,000 iterations correspond to 5 epochs? From my experience, practitioners use 200 epochs to achieve over 95% test accuracy for Adam (or AdamW) with ResNet on CIFAR10. Did you use pre-trained models? In addition, was a learning rate of  $1e^{-4}$ used for AdamW on ResNet-CIFAR10? If so, I recommend a grid search for the learning rate, as the literature (e.g., Prodigy or D-Adaptation) often uses  $1e^{-3}$. It is also unclear whether Figure 8 shows training from scratch or fine-tuning. Finally, including results for ImageNet trained from scratch would be interesting.

### Questions
1. **Figure 2:** The concept of $g_t^{\text{optim}}$  in the illustration is unclear. It would be helpful to clarify which optimizer (SGD?) is used in this figure. Can you add a brief explanation of in the figure caption or main text, specifying which optimizer it refers to ?

2. **Figure 4:** We can see training instability with sudden changes in curvature. Surprisingly (for me), ResNet-152 has a worse train accuracy than ResNet18 for GeN-SGD but not for GeN-AdamW. It would be better to run the same experiments with basic SGD and AdamW for comparison. The test loss for ResNet-152 appears quite unstable at the beginning of the training process.

3. **Line 311:** For a more precise discussion about the forward/backward complexity  $B \approx cF$ , consider referring to the paper “On the Complexity of Nonsmooth Automatic Differentiation” by Bolte et al. (2023). You also have "Evaluating Derivatives: Principles and Techniques of Algorithmic Differentiation" by Griewank et al. (2008), or the Bauer-Strassen theorem. The constant  $c$  is approximately 5 (in my knowledge), which might improve the relative speed estimation. A more detailed discussion on this point would be valuable. Moreover, could you give more insights into the sentence “GeN optimizers are roughly 60% as fast as the base optimizers”? Please, can you : 
- Incorporate the suggested references into their discussion of forward/backward complexity.
- Clarify how they arrived at the 60% speed estimate and how it might change with the more precise constant c ≈ 5.
- Provide a more detailed explanation or derivation of the relative speed calculation.

4. **Figure 6:** Perhaps use 1000 iterations for Plot 3 to improve comparability? The same suggestion applies to Figure 7. Additionally, what happens if a different initialization for  $x_0$  and  $y_0 $ is used? Is it robust? Please, can you :

- Update Figures 6 and 7 to use 1000 iterations for all plots for better comparability.
- Conduct and report results from experiments with different initializations to demonstrate the robustness of their method.

5. **Figure 8:** The number of iterations is unclear—10,000 iterations correspond to 5 epochs? From my experience, practitioners use 200 epochs to achieve over 95% test accuracy for Adam (or AdamW) with ResNet on CIFAR10. Did you use pre-trained models? In addition, was a learning rate of  $1e^{-4}$ used for AdamW on ResNet-CIFAR10? If so, I recommend a grid search for the learning rate, as the literature (e.g., Prodigy or D-Adaptation) often uses  $1e^{-3}$. It is also unclear whether Figure 8 shows training from scratch or fine-tuning. Finally, including results for ImageNet trained from scratch would be interesting.

### Soundness
3

### Presentation
2

### Contribution
3
