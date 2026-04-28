# Quadratic models for understanding catapult dynamics of neural networks

- Decision: Accept
- Avg Score: 6.40
- Scores: 6, 8, 5, 8, 5

## Abstract
While neural networks can be approximated by linear models as their width increases,  certain properties of wide neural networks cannot be captured by linear models.  In this work we show that recently proposed Neural Quadratic Models can exhibit the ``catapult phase'' \citep{lewkowycz2020large} that arises when training such models with large learning rates. We then empirically show that the behaviour of neural quadratic models parallels that of neural networks in generalization, especially in the catapult phase regime. Our analysis further demonstrates that quadratic models can be an effective tool for analysis of neural networks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper studies a quadratic approximation of two-layer neural networks to understand optimization behaviours that cannot be captured by linear models. More precisely they theoretically evidence the so-called catapult dynamics for respectively one and multiple training points, ie they show the existence of two critical values for the learning rate which delimits respectively exponential convergence to the minimum, catapult dynamics (ie first increase of the loss then convergence to low loss) and finally divergence. Finally they provides experiments evidencing catapult dynamics as well as the fact that the quadratic approximation of a neural networks shows similar behaviours that the neural network above the critical learning rate.

### Strengths
This paper is well-written with clear figures and a good explanation of the setting and the results. This paper studies a very interesting phenomenon about the optimization of neural networks and has to deal with non-linear phenomena which are usually not well understood. They are able to evidence theoretically the catapult dynamics and the existence of two critical learning rates when dealing with neural quadratic models.

Empirical results shed light on the similarity of behaviours in terms of generalization between the NQM and the neural network function, evidencing the coherence of the quadratic model.

### Weaknesses
I find the proofs a bit hard to understand because of the use in the proofs of O,o, $\Omega$ notations. Hiding constants behind such notations makes the proofs a bit cloudy to me. 

1)Especially I have some concerns about the proof of lemma 1 in appendix D: you use a proof by induction, and still use O,o notations. But summing $O$ terms remains $O$ only when the number of iterations is controlled. To still have $O$ in the end of the summation with respect to m, it should be checked that the summation index T is itself $O(1)$. However I am not sure such a result is proved (correct me if I'm wrong).
Especially it seems to me that it might not be the case by considering the fact that T must satisfy a relation of the form $(1+\delta)^T\sim \log(m)$ with $\delta \sim \frac{\log(m)}{\sqrt{m}}$. Indeed $u(t)$ goes from $O(1/m)$ to $O(\log(m)/m)$. In that case, $T\sim \frac{\log(\log(m))\sqrt{m}}{\log(m)}$ which is not $O(1)$. The core issue is that the inductive argument relies on bounding the change in $\kappa(t)$ across iterations, but the accumulation of $O$ terms within the inductive step is not properly controlled, especially when the number of iterations, $T$, is not $O(1)$. This makes the inductive argument unsound.

2) Another ambiguity about the $O$ notation is for example when it is stated: $\kappa(0)>(1+\delta-O(1/m))^2>(1+\delta-O(\delta^2/\log(m)))^2$ in appendix D. In full generality it seems wrong for general sequences as it depends on the constants in the $O$ itself and their sign. For example $(1+\delta))^2<(1+\delta-(-3\delta^2/\log(m)))^2$. I think this statement in its current form would perhaps need an additional study of the constants, their sign or if they are zero. The issue is that the $O$ notation hides the sign and magnitude of the constant, making it impossible to ensure the inequality holds without further analysis of these constants.

3) The non-linearity that is used in this paper is a ReLU: it allows to compute easily the second derivative of the neural network function (it deletes the diagonal terms of the hessian of the neural network function). My only concern is regarding the generalization to non-linearities that are not piecewise linear and hence which make another term appear in the Hessian of the neural network function, which corresponds to the second derivative of the non-linearity (correct me if I'm wrong). Could the author comment about how to handle this and if they expect the analysis to be the same and the results to still hold?

### Questions
1) I am curious if you could clarify the links, if they exist, between catapult dynamics and recent works on edge of stability analysis of neural networks (cf the paper "Second-order regression models exhibit progressive sharpening to the edge of stability" that is not cited but seems to me very related to your setting). It seems interesting because both studies explore the influence of a non-linear quadratic term on the coupled dynamics of the sharpness and the learning rate.

2) It is written in the text that the results hold with high probability over initialization but I'm not sure if this is written in the statement of the theorems. Perhaps it could be added in the theorems themselves.

3) I find the results interesting and they provide good contribution. I would increase my score if the authors address my concerns about the clarity of $O,o,\Omega$ notations in the proof, especially the proof by induction.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
The paper studies the "catapult phase" during training models with large learning rates.
Importantly, it proposes Neural Quadratic Models (NQMs) as a tool to study it and proves that when large learning rates are used they exhibit a similar catapult phase as modern neural networks, which is not the case of other tools such as linear models, a popular theoretical tool to analysis the learning of neural networks.
The paper presents these findings with proofs and suggests that NQMs can be useful tools to analyze neural networks in the future.

### Strengths
**originality** The finding of the paper seems to be novel and the proposal of using NQMs can be new as well.

**quality** The finding and theory from the paper seems to be sound.

**clarity** The paper is overall well-written but can be hard to follow for people who are not very familiar with the field.

**significance** The contribution of the paper seems to be significant and can enable many future work on analysis with NQMs, which could lead to more useful findings than the catapult phase.

### Weaknesses
The proposed term Neural Quadratic Models seems to be unnecessary as for linear models we don't call them Neural Linear Models.

While the paper demonstrates the catapult phase with NQMs, it does not fully explore the limitations of this model. For example, how does the NQM approximation change as the neural network moves further away from its initial parameters? This is important since the catapult phase is a highly non-linear phenomenon, and the validity of the quadratic approximation might degrade significantly during this phase. Also, the paper lacks a discussion on the potential impact of the Hessian's condition number on the NQM's ability to capture the catapult phase. A poorly conditioned Hessian could lead to unstable or inaccurate approximations, especially with large learning rates.

### Questions
Some recent findings such as the deep double descent are high-dependent on the size of the neural networks and other hyper-parameters.
Is the "catapult phase" here sensitive to other hyper-parameters apart from learning rates?
I don't see many conditions for the theorem presented in the paper.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes using neural quadratic models -- second order taylor expansion of any function f around initial parameters $w_0$ -- as a way to study neural network dynamics. The authors start by explaining that linear dynamics perspective of neural networks falls short in explaining some of the behaviors in neural network dynamics; specifically, catapult phase of learning rate. They approximate a two layer neural network using its second order expansion. They first show that for a single training example, where tangent kernel reduces to a scalar, monotonic convergence, catapult phase, and divergence are separated based on learning rate and inverse of kernel value at random initialization. They further extend their analysis to uni-dimensional multiple example setting where the analysis is driven by the eigenvectors of the kernel matrix. Finally, the authors empirically show that for wide neural networks, catapults happen in the top eigenspace of the kernel -- similar to the multiple example setting. Experimental results suggest that catapult phase results in lower test error compared to error with sub-critical learning rate for the quadratic model, mimicing the dynamics of neural networks more closely.

### Strengths
The paper is written well and in general easy to follow. Empirical results on top eigenspace of tangent kernel for analyzing general wide neural networks is convincing.

### Weaknesses
Several assumptions about underlying the theory are not clear and different from the practice.

1. The neural network in Eq (9) is initialized as $u_i \sim \mathcal{N}(0, I_d)$ and $v_i \sim Unif(-1, 1)$. Can you explain why $v_i$ is initialized different from $u_i$, also different from the typical inverse fanin/fanout initialization in practice? Specifically, it's unclear why a uniform distribution is chosen for $v_i$ instead of a more common Gaussian initialization, and what impact this choice has on the subsequent analysis. The justification for this choice needs to be more clearly stated and its implications explored.

2. The assumption that width (m) is larger than data size (n) which is assumed to be a small constant is unrealistic. While in the limit where width goes to $\inf$, this would be the case but for any finite width network, this does not hold in practice. Is this assumption crucial, can you still assume that $n/m$ does not necessarily go to zero? The paper needs to discuss the limitations of this assumption and how the results might change if $n/m$ is not negligible. The practical relevance of the theoretical results under this assumption should be more clearly explained.

3. $p_1(t)$ is the top eigenvector of $K(t)$. Given that $p_1(t)$ is not necessarily equal to $p_1(t+1)$, it is not clear how you derived $\lambda_1(t+1)=\lambda_1(t)-p_1(t)^TR_K(t)p_1(t)$. Could you please explain in more detail? The derivation seems to assume that the top eigenvector remains constant across iterations, which is not generally true. A more rigorous justification is needed for this step, possibly involving perturbation analysis or other techniques.

4. In Eq(12), $R_\lambda(t)$ is defined without the minus sign. In the following paragraph, you mention that "$R_\lambda(t)$ stays positive and results in monotonic decrease of kernel" which makes sense since $\lambda(t)=\lambda(t-1)-R_\lambda(t)$. But in the next paragraph, you write down $\lambda(t)=\lambda(0)+\sum_{\tau=0}^{t} R_\lambda(\tau)$ which suggests that $R_\lambda(t)$ should include the minus sign. Please clarify. The inconsistency in the sign of $R_\lambda(t)$ needs to be resolved, and the correct definition should be used consistently throughout the paper.

5. Related to above, I think it should be $\lambda(t+1)=\lambda(0)+\sum_{\tau=0}^{t} R_\lambda(\tau)$ or $\lambda(t)=\lambda(0)+\sum_{\tau=0}^{t-1} R_\lambda(\tau)$

6.  You mention in the decreasing phase section in page 6 that decrease in $v(t)$ would cause a decrease in $\kappa(t)$. But in Eq (13), reducing $v(t)$ would increase inside of square which should lead to an increase in $\kappa(t)$; unless, $u(t)+w(t)<0$ which is not clear if it holds. Please clarify. The relationship between $v(t)$ and $\kappa(t)$ needs a more detailed explanation, and the conditions under which $\kappa(t)$ decreases should be clearly stated.

7. In Eq (10), $1/\sqrt(d)$ is missing from $\sigma(u_{0,i}^Tx)$. It is present in Appendix A.

8. Page 27 in the Appendix, it should be $\Pi_1 \mathcal{L}(t)=K_1(t)\Pi_1 \mathcal{L}(t-1)$

### Questions
Please see above for related questions as they are more meaningful within their respective contexts.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
I was asked to review this paper at the last minute, so although I did not get the chance to work carefully through the proofs, I can comment on the broad content and contributions

The paper analyzes optimization and generalization properties of neural networks using quadratic models. It shows theoretically and empirically that quadratic models exhibit the "catapult phase" with large learning rates, explaining a property of neural networks not captured by linear models. The quadratic model and its (changing) tangent kernel is studied analytically for the case of a single training example and multiple uni-dimensional training samples. Three regimes are identified. When catapault effects occur, better generalization is observed in quadratic models. Experiments demonstrate quadratic models parallel neural networks better than linear models in generalization with large learning rates.

### Strengths
The paper rigorously analyzes the catapult phase in NQMs theoretically. Prior works have attempted similar analyses, but the presentation here is particularly readable. The experiments validating theory and demonstrating applicability are thorough. They successfully demonstrate that NQMs better capture neural network behavior than linear models. The experiments in the appendix in particular provides good additional support. The mathematical analysis appears solid.

### Weaknesses
The architectures and datasets used are still relatively limited. While the authors explore a range of datasets, the model architectures are not as diverse as they could be. It would be beneficial to see experiments with more complex architectures, such as a ResNet or a more modern transformer architecture, to demonstrate the broader applicability of the findings. It would also be good to highlight what the incremental value of this paper is over prior work on quadratic models. The current discussion does not sufficiently delineate the specific novel contributions of this work compared to existing literature on quadratic models. A more thorough comparison is needed to clarify the unique aspects of this analysis. A CNN and transformer experiment would be particularly welcome.

From a cursory literature review, I have found this paper which has relatively substantial overlap in topic, and I believe should at least be cited (Meltzer and Liu https://arxiv.org/abs/2301.07737). A more thorough set of references on recent work around the catapult effect and edge of stability would also benefit the paper. The current literature review is not comprehensive enough, and a more thorough discussion of related work, particularly on the edge of stability and catapult effects, is needed to contextualize the contributions of this paper. This would help to position the work more clearly within the existing body of research.

From empirical work, I've also seen that quadratic model's validation curve only tracks the NN's curve in the early stages of training, but then diverges from it. It would be nice to give an example of the limitations of the quadratic model for understanding generalization. Being clear about potential limitations of quadratic models to fully model neural networks would be welcome. The paper should explicitly address the limitations of using quadratic models to approximate neural network behavior, particularly in the later stages of training where the approximation may not hold as well. This would provide a more balanced perspective on the applicability of the model.

### Questions
Have you analyzed how the Hessian evolves during catapult phase? This could shed some light onto the phase transition.

It may be interesting to consider explicitly varying the feature learning parameter (e.g. $\alpha$ in Chizat et al) and see how the quadratic model differs from the linear one. This would be related to going into $\mu$ parameterization as in Yang. 

Can you relate observed properties of trained NQMs to improvements in generalization, perhaps through the lens of something like kernel-target alignment for the after-kernel of the quadratic model?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work shows that quadratic models exhibit the catapult phase of neural networks.

### Strengths
The strength of the work lies in the soundness of the theory and that the topics covered by the paper are all pertinent problems to the contemporary deep learning theory.

### Weaknesses
There are quite a few fatal weaknesses in my opinion.

1. The paper covered too many topics that it feels that it does not achieve any point satisfactorily. For example, the paper feels mistitled. The main focus of the paper is the catapult mechanism -- which does appear in deep learning but cannot represent all types of "neural network dynamics." In my opinion, the catapult mechanism is a rather special / specific type of dynamics and the title is an overclaim. If the authors change the title to a more proper one, the paper could be much easier to evaluate.

2. Lack of discussion of a highly relevant problem. Essentially, within the framework of quadratic models, it appears to me that the catapult mechanism is nothing but what the academia traditionally calls "chaos." For example, consider a width-1 quadratic model, and compare the dynamics of GD to that of a logistic map -- the dynamics is essentially identitical -- the loss of local stability leads to chaos in the logistic map, and the same here in the quadratic model. The authors need to discuss this point in my opinion.

### Questions
See weakness


------
I feel more positive about the paper with the new title. However, I still feel that the paper needs to clarify why or why not chaos is present in the model and clarify its connection to the studies in this line.

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor
