# STAR: Stability-Inducing Weight Perturbation for Continual Learning

- Decision: Accept
- Scores: 8, 5, 6, 5

## Abstract
Humans can naturally learn new and varying tasks in a sequential manner. 
  Continual learning is a class of learning algorithms that updates its learned model as it sees new data (on potentially new tasks) in a sequence.
  A key challenge in continual learning is that as the model is updated to learn new tasks, it becomes susceptible to \textit{catastrophic forgetting}, where knowledge of previously learned tasks is lost. A popular approach to mitigate forgetting during continual learning is to maintain a small buffer of previously-seen samples, and to replay them during training. However, this approach is limited by the small buffer size and, while forgetting is reduced, it is still present.  In this paper, we propose
a novel loss function STAR that exploits the worst-case parameter perturbation that reduces the KL-divergence of model predictions with that of its local parameter neighborhood to promote stability and alleviate forgetting. STAR can be combined with almost any existing rehearsal-based methods as a plug-and-play component. We empirically show that STAR consistently improves performance of existing methods by up to $\sim15\%$ across varying baselines, and achieves superior or competitive accuracy to that of state-of-the-art methods aimed at improving rehearsal-based continual learning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces STAR, a plug-and-play loss component designed to enhance rehearsal baselines by addressing potential forgetting from future parameter updates. Since future parameters are unknown, STAR estimates forgetting through a surrogate measure: i.e., capturing the worst-case perturbation of current parameters within their local neighborhood. Substantially, the authors argue that making the model resilient to perturbations (with a dedicated loss components) helps in reducing the future forgetting. Ideally, STAR is evaluated across three datasets, comparing rehearsal baselines i) with and without its application, and ii) against other state-of-the-art plug-and-play components.

### Strengths
1) Tackling the problem of future forgetting by acting on the current task is novel and interesting;
2) the ablations and exploratory experiments are concise yet to the point;
3) leveraging straight weight perturbation as a regularizer when training in continual learning is compelling, although similar in spirit to [1].

[1] Lorenzo Bonicelli, Matteo Boschini, Angelo Porrello, Concetto Spampinato, and Simone Calderara. On the effectiveness of lipschitz-driven rehearsal in continual learning. Advances in Neural Information Processing Systems, 35:31886–31901, 2022.

### Weaknesses
1) While an improvement over existing rehearsal baselines is interesting, its appeal is limited as these baselines have largely been surpassed by prompting approaches. Indeed, some of these techniques [1, 2] now represent the state of the art in Continual Learning; 
2) while the improvements on Split-CIFAR10 are solid, those on Split-CIFAR100 and Split-miniImageNet (Table 2) are far less noticeable and sometimes absent; 
3) the results in Table 1 for Split-CIFAR100 seems to be different for X-DER [3] to what reported in the original paper. This hinders a good evaluation, as the original results (reported in [3]) surpass those of X-DER equipped with the proposed methodology.

Generally, I feel this work is incremental w.r.t. LiDER [4] in its idea. Also, the improvement w.r.t. other plug-and-play techniques appears not significant enough.

Some minor issues that did **not** affect my evaluation:
 - In the related works section, regularization-based methods are listed twice.
 - In the line preceding Eq. 4, “f” should be “f(x).”
 - For the gradient ascent step, eta seems to be used in place of gamma (as in Figure 2).
 - In the explanation of the gradient ascent, the equivalence of eta within the i.e. parentheses appears incorrect.
 - In Algorithm 1, “f” is used instead of “q” in the STAR gradient.

### Questions
None

### Soundness
3

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
5

### Summary
In this paper, the authors mainly focused on maintaining the output distribution of previous models to prevent the catastrophic forgetting in rehearsal-based CL. To maintain the output distribution, the proposed method adopts not only the regularization between the future output and the output of the current model, but also minimizing the worst case version of this regularization. By doing so, the models can be updated toward the region in which the model outputs are well preserved. In the experiment, the authors show that the proposed method can strengthen the baselines, and also extensively conducted the ablation analysis.

### Strengths
Strengths

1. The viewpoint that the model should preserve the output distribution may be similar to the methods using the knowledge distillation in CL, the approach minimizing the worst case version of the regularization is novel. I think the critical difference between STAR and previous methods lies on the optimization scheme.

### Weaknesses
Weaknesses

1. I think the proposed method highly focuses on the stability of the model. If the number of incoming tasks is quite large (e.g. 50 tasks in split Omniglot), I wonder the proposed approach can still strengthen the baselines in the settings containing large number of tasks.

2. The authors said that this method does not assume any information on the task boundary. However, in the experiment, is it possible to consider the notion of epoch without the assumption on the task boundary? I know there is no terms on the task identifier in the formula, but I think the experiment setting is not consistent to the authors' argument. If the proposed method can cover any scenario in CL, does this methods also can work in single epoch setting?

3. The computational cost on optimizing the min-max loss is not negligible. I think it would be better to show the running time of this algorithm.

4. There is no experiments on large-scale dataset. Since the optimization procedure is much complex than previous methods, I wonder the proposed approach can be applied to much larger networks with large datasets

5. In terms of computing the gradient of Eq.8, the authors said that they assume the Hessian is identity matrix. However, I wonder using this gradient can find the minimum of the worst case loss function. In the all procedure, there are too many approximations to optimize the loss function.

### Questions
Already mentioned in the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper focuses on improving rehearsal-based continual learning by stabilizing future predictions across the local neighborhood of the parameters. Specifically, it proposes a plug-and-play loss function, STAR, which applies parameter perturbation and reduces the KL-divergence between the model's predictions and those of its local parameters neighborhood. For each forward pass during training, a local neighbor of the current parameters is sampled, and this neighbor is perturbed by a single step of normalized gradient ascent to maximize the KL-divergence between the predictions of the model and the neighbor. Then, by combining the gradient of the KL-divergence between predictions with respect to the perturbed neighbor and the gradients of the rehearsal method's log-likelihood, the model parameters are updated cumulatively. This approach allows the models to learn a flat loss landscape, making the learned local parameter space less sensitive to future updates.

### Strengths
1. The paper is easy to follow and provides extensive experiments to show its plug-and-play effectiveness across different replay-based methods on small to large-scale datasets.

2. The authors have thorough experiments including ablation study, choice of buffer or current data for STAR loss and demonstration of distribution shift for seen tasks.

### Weaknesses
1. The paper lacks theoretical justification for why the method works, which could have further strenghtened the proposed method.

1. Minor Inconsistencies in Algorithm 1: (i) does not use epochs, (ii) two different hyper-parameters $\gamma$ and $\eta$ in equation (11) for perturbation coefficient (iii) $f$ used instead of $q$ in 345.

### Questions
1. Why is the perturbation ratio defined as the ratio of two norms in line 316 even though it is called and actually used as a hyper-parameter, as shown in table 7.

2. What is the essence for scaling gradients by the norm of weights in equation 11?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a new method ‘STAR’ to prevent catastrophic forgetting in continual learning, by minimizing the KL divergence between the output of the current parameters and the worst case parameters in a neighborhood of the current ones. The hypothesis is that if the parameters in the neighborhood of the current solution don’t change the output much for past tasks, then it will be easier to find a solution within that region that also performs well on new tasks. Since the exact computation of this method is intractable, a practical approximation is proposed by first taking a gradient ascent step to find the worst case parameters and then it is assumed that the gradient at the worst case parameters is approximately equal to the gradient of the actual current parameters. The approach is tested by combining this idea with several state of the art rehearsal methods. STAR consistently improves other rehearsal baselines across different datasets and memory sizes.

### Strengths
* The paper is well written and clearly explains the followed methodology
* The hypothesis and solution are plausible
* The results are well tested with regard to improvement of typical CL baselines and adequately compared to other similar approaches.
* Section 3 is especially clear, which makes the remainder of the paper a lot easier to understand.

### Weaknesses
 * The main hypothesis of this paper is that it is important to reduce the difference in output with the worst case parameters in the neighborhood of the current solution. A loss function is proposed to avoid the worst case parameters, but I am not convinced that is sufficiently shown that this works as intended. Figure 3 does show that the final KL divergence between the current model and the final model are reduced, but that doesn’t imply anything about the worst case situation, only that one specific instance in the neighborhood is closer. To test this, an experiment could be done were a gradient ascent step is taken as in Equation 10 for both the proposed solution and one of the other replay benchmarks to directly compare the worst case parameters. An alternative explanation for the current results may be that the additional loss function acts as a good regularizer to prevent overfitting on the memory samples.

* The drawing in Figure 1 and 2 are solely hypothetical. There is no evidence that the actual loss landscape looks like this nor that the proposed method actually follows the path that is indicated in these figures. Without evidence that this is the problem, it is hard to accept a solution as long as the problem is not clearly identified.

* The mathematical derivation in lines 288:321 is confusing. First a gradient ascent step is taken to maximize the KL divergence (Eq. 10). Then at those parameters a new gradient is calculated to minimize the same KL divergence (line 323), which should be equal to the negative gradient of Eq. 10, if linearity is assumed (which is done in line 323). Applying this gradient at parameters $\theta$ is then simply a gradient descent step at the initial parameters. So either this derivation could be simplified, or it could be shown that because of the non-linearity of the loss surface, these extra steps actually make a difference (but then the assumption in line 323 is no longer accurate). Figure 2 shows this differently, but only because non-linearity is assumed there.

* Line 051: in a class incremental setting stability is sometimes not sufficient; if new classes are similar to representation of old classes may need to change too. (E.g. if a model had only learned a color representation of a past object and later a new yellow object is added an old yellow object cannot be represented as only being yellow).

 * Line 109: repeated sentence from earlier.

### Questions
* Is it possible that the results are explained by a different hypothesis, e.g. reduced overfitting on the memory?
* Is there any empirical evidence for the loss landscapes in Figures 1 and 2?
* Can the mathematical derivation in 4.3 be simplified, or the importance of non-linearities be highlighted?
* Is local stability always sufficient in a class incremental settings, as is claimed in line 051?

### Soundness
2

### Presentation
3

### Contribution
2
