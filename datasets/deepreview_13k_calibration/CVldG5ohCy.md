# Adam through a Second-Order Lens

- Decision: Reject
- Avg Score: 4.00
- Scores: 6, 3, 6, 1

## Abstract
Research into optimisation for deep learning is characterised by a tension between the computational efficiency of first-order, gradient-based methods (such as SGD and Adam) and the theoretical efficiency of second-order, curvature-based methods (such as quasi-Newton methods and K-FAC). We seek to combine the benefits of both approaches into a single computationally-efficient algorithm. Noting that second-order methods often depend on stabilising heuristics (such as Levenberg-Marquardt damping), we propose AdamQLR: an optimiser combining damping and learning rate selection techniques from K-FAC (Martens and Grosse, 2015) with the update directions proposed by Adam, inspired by considering Adam through a second-order lens. We evaluate AdamQLR on a range of regression and classification tasks at various scales, achieving competitive generalisation performance vs runtime.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper tried to combine the first-order method (such as Adam) with the second-order methods, such as K-FAC. More specifically, the authors propose a novel optimizer AdamQLR: combining damping and learning rate selection techniques of K-FAC. The experimental results illustrate that the proposed method AdamQLR can achieve competitive generalisation performance and training efficiency.

### Strengths
1. The idea of combining first-order and second-order methods is very interesting. In addition, the research direction is also very important. 
2. The proposed method is very easy to understand. I think we should pay more attention to second-order method and improve its efficiency.

### Weaknesses
1. I think the main results are from the figure 2. But the figure is not very clear for me, maybe you can list the training loss, test loss, convergence steps, and generalization gap ( |training_loss - test_loss| ) in a table. From this figure. I'm not very clear whether the proposed method can solve the overfitting issue and improve the generalization. So I think you can analyze the generalization gap. 

2. The experimental results are not very strong for me. Although the proposed method can achieve fast convergence and lower test loss, their performance is still too close. In addition, you try to analyze training loss and test loss in figure 2. But loss value is not a great metric for classification tasks and I think you should show the accuracy. 

3. The training task is too simple and the results on complex tasks (such as ImageNet) is not very strong.

### Questions
1. Loss value in figure 2 is not great enough to compare the performance of different methods and maybe you should provide the accuracy value.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper authors propose some symbiosis of two optimization methods: Adam and K-FAC. They combine damping and learning rate selection techniques from K-FAC and use it inside Adam algorithm. The resulting algorithm, called AdamQLR, is then evaluated on different regression and classification tasks.

### Strengths
1. Lots of numerical experiments.
2. Clear description of algorithm modification.
3. Good description of the motivation of the heuristics, adopted from K-FAC.
4. Description of the experimental setup and hyperparameter search space.

### Weaknesses
From theoretical point of view, the result seems insignificant. You took some heuristics, that improve the model, and moved it to another model. There is no evidence, that it should work better in theory. From practical point of view, as far as I understand, the number of hyperparameters increased: $\beta_1, \beta_2, \varepsilon$ for Adam vs $\beta_1, \beta_2, \varepsilon, \lambda$ for AdamQLR (or even $w_{dec}, w_{inc}$ instead of $\lambda$.

Rosenbrock function example seems unfair, because you use Hessian there, what do you think?

1. You say, that your main motivation is to show that untuned version of AdamQLR performs similarly to tuned Adam. However you do not provide the results for untuned Adam. Maybe it performs similarly.
2. Again, you do not provide the results for untuned K-FAC. Thus, we do not know, how it performs on these tasks.
3. FashionMNIST: you say, that K-FAC overfits much earlier, compared to other methods. But It achieves the best test accuracy faster, then any other method. So it is a wrong conclusion: if we stop all the methods earlier, and not when K-FAC starts overfitting, it will be the best. 
4. Actually, K-FAC performs the best in most of the experiments. And, if you say, that your main motivation is not to provide SOTA method, but to provide a method, which untuned version has comparable performance with tuned Adam or K-FAC, then again see points 1 and 2.
4. The section about batch size seems weird, since obviously the bigger batch size, the better convergence of the algorithm, since it narrows the area of convergence of stochastic gradient-based method, which can be seen from convergence rate of SGD [1].
4. You only provide performance results against time, which seems not enough, and it is better to provide also performance against epochs.
4. When we look at experiments on bigger models and datasets (ImageNet, Penn Treebank), we see, that proposed method is outperformed by all the others. Taking into account my points 1-4, it seems unfair to say, that untuned AdamQLR performs on the same level as tuned Adam on any task.

### Questions
Rosenbrock function example seems unfair, because you use Hessian there, what do you think?

### Soundness
1 poor

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work refers to Adam and proposes to adaptively adjust the learning rate. Specifically, the authors utilize $\rho$ to denote the ratio between the difference of true loss function $f()$ and the difference of second-order estimation $M()$. Then the authors refine the estimated Hessian matrix through $\lambda$ according to $\rho$. Finally, the learning rate is then computed by minimizing $M(\theta - \alpha d)$.

### Strengths
1.	The method makes sense.

2.	Extensive experiments show the effectiveness of the method.

### Weaknesses
1.	I wonder how to get the matrix $C$ in Eq. 1.

2.	What is the principle of setting $\omega_{dec}$ and $\omega_{inc}$, and why $\lambda$ is adjusted when $\rho$ larger than 3/4 or smaller than 1/4?

### Questions
Please see the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes AdamQLR, which is a modification of the Adam optimizer and tries to adapt some heuristics used in the K-FAC optimizer for Adam, such as Levenberg Marquardt damping (equation (2) in the paper) and learning rate selection (equation 3 in the paper), both based on a truncated second order Taylor expansion of the function computed by the neural network at the current parameters $\theta_t$ (equation 1 in the paper). The authors perform experiments on 6 tasks (Rosenbrock, UCI Energy/Protein, Fashion-MNIST, SVHN and CIFAR-10) and they compare two versions of their work (Adam QLR Tuned/Untuned) against a few popular optimizers in the literature (SGD Minimal/Full, Adam, K-FAC).

### Strengths
Below I enumerate the strengths of the paper:
1. clearly written and easy to understand
2. code is provided
3. optimal hyper-parameters are clearly stated in Table 2
4. ablation study for Levenberg-Marquardt heuristic

### Weaknesses
The paper lacks novelty and originality because it only combines Adam and K-FAC in a facile way and thus doesn't provide better results for most of the tasks mentioned, such as UCI Energi/Protein, Fashion-MNIST and CIFAR-10 (in these cases, K-FAC and/or original Adam are better than the proposed method because the generalization performance VS runtime is not competitive as stated in the abstract).

The evaluation was performed on small tasks and I believe that the usage of Rosenbrock function not adding any value to the paper since the tasks that involve Neural Networks are much more complicated. The paper does not have any tables that contains accuracies for classification tasks and it is extremely difficult to figure out what the final accuracies are only by looking at the plots. In the end, it is unfortunate to say that the paper does not meet the novelty and originality requirements for ICLR.

I am continuing by pointing out some inconsistencies between the abstract/introduction and the results in Figure 2, which I use to justify my score for the paper.

**AdamQLR VS other optimizers**
1. UCI Energy, Figure 2a:
- **train loss**: K-FAC < Adam < Tuned AdamQLR < Untuned AdamQLR < SGD (Minimal / Full)
- **test loss**: K-FAC has lowest (you could have zoomed in on the interval 0-50 seconds)
2. UCI Protein, Figure 2b:
- **train loss**: K-FAC << Tuned AdamQLR < Adam < Untuned AdamQLR < SGD (Minimal / Full)
- **test loss**: same relationship as for the train loss
3. Fashion-MNIST, Figure 2c:
- **train loss**: K-FAC is by far the best, while AdamQLR (Tuned and Untuned) and original Adam have similar trajectories
- **test loss**: K-FAC is the best in the first 5 seconds, then Tuned AdamQLR is better than Adam and Untuned AdamQLR
- ** test accuracy**: K-FAC is the best, while Tuned/Untuned AdamQLR and Adam are all similar
4. SVHN, Figure 2d:
- **train loss**: here, Untuned AdamQLR is better than all other optimizers in the first ~75s of the training. However, I do not know why there are so many large and frequent decreases in the training loss, compared to the other optimizers, can you please explain that? To me it seems like the learning rate decay is performed more often than for the other optimizers (or is it from the automatic learnign rate adjustment?)
- **test loss**: Untuned AdamQLR is the best in the first 50s of the training, while it is almost outperformed by SGD
- **test accuracy**: Untuned AdamQLR is similar to SGD
5. CIFAR-10, Figure 2e:
- **train loss**: K-FAC < Untuned AdamQLR < Tuned AdamQLR < SGD < Adam
- **test loss**: K-FAC decreases the test loss by a lot in the first 250s and is much better than Tuned and Untuned AdamQLR
- **test accuracy**: Tuned AdamQLR is better by the time point 1200s
6. ImageNet, Figure 6:
- **validation accuracy**: Untuned Adam is better than AdamQLR and SGD
- **test accuracy**: same as for the validation accuracy

I would like to give more justification for my rating, point by point with citation from your manuscript and I would appreciate your feedback on each of them.

**About computational efficiency of AdamQLR**. I believe that adapting the heuristics of K-FAC to Adam is not a natural approach since Adam is a popular optimizer especially for its simplicity: the covariance matrix of the gradient is used as a proxy for the Hessian matrix, which is supposed to be diagonal, making it easy to compute by squaring the gradient entries, providing a computationally efficient algorithm. I believe that estimating full Hessian information (via the vector products with an additional backward pass) just to compute the learning rate for Adam (that uses the assumption of diagonal Hessian, as described above) just doesn't make sense to me. Moreover, calling this approach computationally-efficient is fundamentally wrong since it incurs  that additional backward pass because, as you have also stated in the paper, Adam is already an adaptive learning rate optimizer.

> **We propose a variation of damping based on Adam’s internal curvature estimates which, when applied to Adam’s update proposals, outperforms classical damping from e.g. K-FAC**

This statement is unclear to me. How do you measure which damping scheme is better and from which point of view, what is the metric based on which you compare these?

> **We might ask if accepting first-order methods’ inaccurate curvature models and applying second-order stability techniques would blend the computational efficiency and optimisation accuracy of each**

From your paper I understand that you ran standard K-FAC and I would be interested in whether you tried K-FAC without these heuristics that you inputted to Adam. I believe this should have been a first step in the research flow.

**Momentum for K-FAC**. In your paper you skipped the momentum heuristic from K-FAC and state that Adam already has a momentum correction. Indeed, Adam uses momentum for the gradient (similar to how SGD applies it), but K-FAC uses momentum term in such a way that the quadratic approximation M is minimized, which is completely different. Can you please elaborate more on this particular topic, since it is also an heuristic of K-FAC.

**Learning rate clipping**. When you rescale the learning rate, you clip it to $\alpha_\text{max}$, which is another heuristic that you introduce. After a quick look at the K-FAC paper, learning rate clipping is not mentioned in the original paper. I believe that blending this heuristic with the ones from K-FAC leads to unfair comparison

**Other evaluation flaws**. I believe that it is not fair to compare different optimizers with different batch-sizes, since this parameter yields different number of optimization steps. This also requires manual scaling of initial learning rate to account for the gradient noise in the stochastic gradient.

**AdamQLR increases learning rate**. It is known that in the context of stochastic optimization the gradient is noisy, depending on the batch size. The learning rate schedules are designed to decay the learning rate over the course of optimization, converging to zero by the end of training. From SGD convergence analysis we know that by decaying the learning rate we alsodecay the term that depends on the gradient noise which contributes to increasing the upper bound for the convergence (at least in SGD analysis). The simple fact that AdamQLR increases the learning rate might be a problem for why this technique does not yield good results.

**Tuning**. It seems to me that your approach needs a lot of tuning in order to make it work, which is an indication that the method is not numerically stable.

**Manuscript inconsistencies**. There are some inconsistencies in the information from abstract and introduction which I do not agree with and they are related to all the points that I mentioned in this comment, backed by the observations in the next comment. This is what I meant when I first said that it doesn't meet the ICLR standards.

### Questions
1. how does AdamQLR behave on NLP tasks?
2. how do you compute the curvature matrix C that is used to update the learning rate $\alpha$ and the damping factor $\lambda$? In the manuscript you state that the overhead is only one additional forward pass, while we all know that computing Hessian-vector-products requires an additional backward pass (which, of course, implies a forward pass in the first place)

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
