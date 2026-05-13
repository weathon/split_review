# Training Robust Ensembles Requires Rethinking Lipschitz Continuity

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
Transferability of adversarial examples is a well-known property that endangers all classification models, even those that are only accessible through black-box queries. Prior work has shown that an ensemble of models is more resilient to transferability: the probability that an adversarial example is effective against most models of the ensemble is low. Thus, most ongoing research focuses on improving ensemble diversity. Another line of prior work has shown that Lipschitz continuity of the models can make models more robust since it limits how a model's output changes with small input perturbations. {\em In this paper, we study the effect of Lipschitz continuity on transferability rates.} We show that although a lower Lipschitz constant increases the robustness of a single model, it is not as beneficial in training robust ensembles as it increases the transferability rate of adversarial examples across models in the ensemble. Therefore, we introduce LOTOS, a new training paradigm for ensembles, which counteracts this adverse effect. It does so by promoting orthogonality among the top-$k$ sub-spaces of the transformations of the corresponding affine layers of any pair of models in the ensemble. We theoretically show that $k$ does not need to be large for convolutional layers, which makes the computational overhead negligible. Through various experiments, we show LOTOS increases the robust accuracy of ensembles of ResNet-18 models by $6$ percentage points (p.p) against black-box attacks on CIFAR-10. It is also capable of combining with the robustness of prior state-of-the-art methods for training robust ensembles to enhance their robust accuracy by $10.7$ p.p.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper makes 3 contributions to the field of robust ensemble training: 

1. It identifies a trade-off in neural network ensembles: while decreasing the Lipschitz constant of individual models improves their robustness, it unfortunately also increases the transferability of adversarial examples between models in the ensemble, potentially undermining the ensemble's overall robustness. 

2. It introduces LOTOS (Layer-wise Orthogonalization for Training rObust enSembles), a new training method that promotes orthogonality between corresponding layers of different models in an ensemble. LOTOS is computationally efficient and pretty architecturally agnostic. 

3. Through experiments on CIFAR-10 and CIFAR-100, the authors demonstrate that LOTOS improves ensemble robustness against black-box attacks by 6 percentage points, and when combined with existing robust ensemble methods, enhances their performance by up to 10.7 percentage points.

### Strengths
Overall I'm a fan of establishing (through published literature) empirical observations of interesting deep learning phenomena. This is an example of such a thing. The fact that we can both a) make an individual model more robust via Lipschitz constant changes, but at the same time b) make an ensemble of such models more similar in a way that reduces the overall robustness of the ensemble, is a very curious piece of empirical evidence.

I think the evaluation is pretty strong and despite some obvious additions (that I mention later) I think it is sufficient to establish this as a phenomenon that might be real and that should be investigated further.

### Weaknesses
There are a few weakness that I believe could be relatively easily addressed.

### Limitation 1: Testing only against a single type of adversarial attack
As far as I understand it, the authors only test the robustness against one type of an adversarial attack -- the PGD-50 = Projected Gradient Descent with 50 iterations. I think it is important to 1) add more types of attacks (including black box ones), and 2) possibly look at some standard attack suites such as RobustBench (https://github.com/RobustBench/robustbench)

### Limitation 2: Adversarial robustness vs other kinds of robustness
What about other kinds of robustness such as robustness to noise, sheer, etc. Do you see similar phenomena to what you describe under adversarial attacks?

### Limitation 3: Attack strength norms and their effect on the phenomenon and LOTOS
I would be very curious what the effect of the attack norm (L_infty vs L_2 etc) and attack size (8/255, ...) is on the observed phenomenon and the efficacy of LOTOS. I can imagine that different attack size norms might lead to different qualitative tradeoffs. Could you please be more specific with what exactly you do and how does this relate to your theory & experiments?

### Limitation 4: Weak models?
The results and improvements you present are (I think) pretty non-robust to begin with. Am I wrong about this? How do robust model perform under the same attack? If the model you are using does not have a high robustness to begin with, I believe this might lead to misleading results on what helps and what doesn't. This is because many things tend to help when we're not close to the maximum robustness, but might not generalize. **Addressing this is crucial for me to raise your score.**

### Questions
I addressed the questions in the Weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper finds that while Lipschitz continuity improves individual model robustness, it unexpectedly raises adversarial transferability in model ensembles. To counter this, the authors introduce LOTOS to boost ensemble robustness by promoting orthogonality between models.

### Strengths
This paper links decreasing Lipschitz continuity with increasing transferrability. This is an interesting point of exploration.

### Weaknesses
 - What are the white-box attacks that you used in this paper? Some attacks may not be reliable in assessing ensemble robustness.
- The method appears to be an improvement upon TRS. However, TRS was shown to have an overestimated robustness [a], and it is not well-explained why the LOTOS loss is an improvement.
- It is not clear to me why DVERGE was not considered in the baseline comparisons, as it is known to be an effective robust baseline for ensemble defenses.
- Section 4 is poorly written. I am having trouble understanding your method. For eq. (3):
  - Where is $w_i$ introduced?
  - Why does this equation measure similarity? Specifically, how does the sum of norms relate to similarity in the transformation space?
  - What are $A$ and $B$ matrices, are they model parameters? It is unclear if these are weight matrices or some other form of representation.
  - Also given that $A$ and $B$ are trainable, do you backprop through the SVD of them? If so, how is this done efficiently, given the computational cost of SVD?
- For eq. (4): There is no $k$ in the LHS. It is unclear how the hyperparameter k affects the overall loss function.
- Theorem 4.1:
  - "In Theorem 4.1, we prove even k = 1 can be effective in orthogonalization with respect to the remaining singular vectors for convolutional layers." It is not clear to me how it is proven for $k = 1$. The connection between minimizing the norm of the top singular vector and the orthogonality of the remaining singular vectors is not clear.
  - Why circular padding? The practical relevance of circular padding is not clear, especially if the models are not trained with it.
  - It is not clear to me how this theorem links with eq. (4). The connection between the theoretical result and the practical loss function is not well-established.

### Questions
- Could you compare your methods with other ensemble defenses, especially with DVERGE?
- Could you consider stronger attacks such as AutoAttack [b] and MORA [a] which specifically target ensemble models?

[a]: Yu et al., MORA: Improving Ensemble Robustness Evaluation with Model-Reweighing Attack. NeurIPS 2022. https://arxiv.org/abs/2211.08008
[b]: Croce et al., Reliable evaluation of adversarial robustness with an ensemble of diverse parameter-free attacks. ICML 2020. https://arxiv.org/abs/2003.01690

### Soundness
2

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
The paper analyzes the relationship between model Lipschitzness and the transferability of adversarial examples. Under the setting of TRS model ensemble, decreasing the model's Lipschitz constant improves standalone robustness but also increases transferability, which hurts ensemble robustness. To this end, the authors propose "LOTOS", which promotes the orthogonality of the singular vectors corresponding to the largest singular values of the transformation matrices of the layers of the ensemble candidate models. LOTOS can decrease transferability while only having a slight effect on individual robustness, thereby improving the ensemble robustness. Furthermore, LOTOS can work with heterogeneous model architectures in conjunction with adversarial training.

### Strengths
The paper analyzes an interesting problem, and uses the conclusions to propose a method that seems to work.

### Weaknesses
First of all, I would like to disclose that I am not an expert on black-box attacks or diversity-promoting robust ensembles. I am more familiar with the literature about the white-box scenario.

- The proposed method seems promising in the black-box setting, but how about the white-box case? I think this question is important because it will disentangle robustness from attack difficulty.
- What would happen if the "source model" in the black-box transfer attack is a LOTOS model itself (trained separately from the target model)?
- All definitions in this paper seem to build on the $\ell_2$ norm. Is the analyses and the proposed method only applicable to $\ell_2$ attacks? How about other attack budgets?
- Just to clarify, are all models in the ensemble trained simultaneously, or can they be trained sequentially? Asking for clarification here because the proposed loss function for each model depends on the weights of all other models.
- Line 285 says "for the orthogonalization to be effective in Equation (4), it is necessary to increase the value of $k$ (dimension of orthogonal sub-spaces)". Then, Line 294 says "$k = 1$ can be effective in orthogonalization with respect to the remaining singular vectors for convolutional layers." Are these not contradictory?
- In Theorem 4, the right-hand-side of Equation 5 has two terms under the square root. Which one is dominant? $\epsilon^2$ or the other terms?
- Line 333: typo "ensebmels".

### Questions
- The experiments in the paper focuses on ResNet and DLA. Do you think the method will extend to other popular architectures such as vision transformer, which operates differently and can be shallower?
- Line 215 (using the difference in the population loss of the two models on these adversarial examples as a proxy) -- How good is this approximation? If we use some alternative loss functions other than cross-entropy, is there any chance for this approximation become exact?
- In Equation (3), how would we determine $w_i$? Why do we need this weight, because intuitively we could perhaps just use the singular values here?
- Line 260 ($\\| \sum_{i=1}^d \sigma_i u_i v_i^\top v_i' \\|_2 = 0$). Here we only try to make the singular vectors orthogonal for each $i$, but the singular vectors for different $i$'s are not accounted. Would it possible to have the case where, for example, the first singular vector of $f^{(j)}$ is orthogonal to the first singular vector of $g^{(j)}$, but highly similar to the second singular vector of $g^{(j)}$? In this case, is the transferability between $f$ and $g$ still low?

### Soundness
3

### Presentation
3

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
The paper studies how Lipschitz continuity affects the transferability of adversarial examples in model ensembles. It finds that while lower Lipschitz constants improve individual model robustness, they increase transferability in ensembles. To address this, the authors propose LOTOS, a training method that promotes subspace orthogonality between models, enhancing ensemble robustness. Experiments show that LOTOS improves the robust accuracy of ResNet-18 ensembles and boosts the performance of existing robust ensemble methods.

### Strengths
- It's interesting to observe the trade-off between the robustness of individual models and the transferability of adversarial examples when changing Lipschitz constant. It highlights the importance of addressing the trade-off, an issue that has been overlooked in prior research.
- The proposed LOTOS method is presented as a solution that uniquely focuses on orthogonalizing affine layers, setting it apart from existing methods that target different aspects of model diversity. To my best knowledge, such contribution is also novel.
- The empirical results are shown clearly and shed light on so much understanding of the proposed solution.

### Weaknesses
 - **The soundness of the claim in this paper**: The authors suggest that "although a lower Lipschitz constant increases the robustness of a single model, it is not as beneficial in training robust ensembles as it increases the transferability rate of adversarial examples across models in the ensemble." While I believe that the first part is sound, I want to challenge the statement "a lower Lipschitz constant is not as beneficial in training robust ensembles as it increases the transferability rate of adversarial examples across models in the ensemble". There are too many aspects that may influence the result, for instance, the generalization of the models (because a lower Lipschitz constant may make the models more difficult to train). In other words, on a broad view, it's not just a trade-off between two aspects mentioned in this paper. I encourage the authors to incorporate deeper understanding of this issue (see below).
- **Missing related work and discussion**: As far as I know, there may be some papers that is relevant to yours. For example, some theoretical works [1,2,3] discuss the smoothness & Lipschitz constant in transferability of adversarial examples (see the bounds therein), which may be somehow relevant to Lipschitz continuity emphasized in this paper. Some of them may not discuss the model ensemble issue. However, these insights on individual models is theoretically connected with the analysis in this paper. Furthermore, the vulnerability-diversity decomposition [4] also sheds light on the relationship among transferability, single model robustness and diversity, which may be in line with your claim "We observe that while decreasing the Lipschitz constant makes each model of the ensemble individually more robust, it makes them less diverse and consequently increases the transferability rate among them which in turn hinders the overall ensemble robustness". In addition, the model ensemble literature [5] also suggests the trade-off between diversity and individual model performance. Therefore, maybe you could give a brief discussion of them to help us better understand your theoretical insights. You are also encouraged to choose to discuss other work that I haven't mentioned but is relevant to your paper.
- **Experiments**: Based on the above, I encourage the authors to incoporate more experiments. Since the model generalization / optimization process may also change the trade-off mentioned in this paper, you may add more experiments regarding more algorithms to show the soundness and consistency of your claim. However, in the current version, the experimental parts only consider their own method as well as TRS [1].

### Questions
- What is the definition of $\Re$ in the appendix (page 14)?
- Typos: line 333: "ensebmels"
- Do you think the method in this paper requires significant work on hyperparameter tuning?

### Soundness
3

### Presentation
2

### Contribution
2
