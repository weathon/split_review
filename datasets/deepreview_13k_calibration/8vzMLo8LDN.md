# Neural Context Flows for Meta-Learning of Dynamical Systems

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 5, 6

## Abstract
Neural Ordinary Differential Equations (NODEs) often struggle to adapt to new dynamic behaviours caused by parameter changes in the underlying system, even when these dynamics are similar to previously observed behaviours. This problem becomes more challenging when the changing parameters are unobserved, meaning their value or influence cannot be directly measured when collecting data. To address this issue, we introduce Neural Context Flow (NCF), a robust and interpretable Meta-Learning framework that includes uncertainty estimation. NCF uses higher-order Taylor expansion to enable contextual self-modulation, allowing context vectors to influence dynamics from other domains while also modulating themselves. After establishing convergence guarantees, we empirically test NCF and compare it to related adaptation methods. Our results show that NCF achieves state-of-the-art Out-of-Distribution performance on 5 out of 6 linear and non-linear benchmark problems. Through extensive experiments, we explore the flexible model architecture of NCF and the encoded representations within the learned context vectors. Our findings highlight the potential implications of NCF for foundational models in the physical sciences, offering a promising approach to improving the adaptability and generalization of NODEs in various scientific applications.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces Neural Context Flows, a method for meta learning. The main contributions of the work are focusing on how to combine context vectors in a way that allows OoD generalization and interpretability.

### Strengths
- Writing is very clear and the methodology is well explained. This allows readers to understand the differences between this method and previous ones.
- Interesting use of context vectors through the 3-network model. Ablation studies in supplementary material show the need for such an architecture. 
- The combination via context through the Taylor expansion seems to be an interesting and novel application, which I can see being used in other fields outside of ODE and PDE simulations.
- The estimation of uncertainty via different context vectors is very simple yet very clear and useful.

### Weaknesses
Manuscript makes reference to sample efficiency of using such adaptive models for new context. However the manuscript does not include any experiments to support such a statement.

With respect to the 3-network model, it is unclear how crucial the state-network is. The manuscript does not provide sufficient evidence to justify the necessity of the state network in addition to the context network. Specifically, the paper lacks experiments that isolate the effect of removing the state network while retaining the context network. This makes it difficult to assess whether the performance gains are due to the specific three-network architecture or simply the increased model capacity.

### Questions
Question:

- With respect to the 3-network model, can you remove the state-network but keep the context network? Does it make any difference compared to the one-network model which performs similar to CAVIA?


Suggestions:

- Include sample efficiency experiments for some example ODEs and PDEs. For example MSE for a model trained from scratch vs one finetunes via a new context vector.
- Include uncertainty as a function of forecast. One would assume that uncertainty increases as the forecast becomes longer. Could you provide such an estimate?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes a new meta-learning strategy for learning dynamical systems governed by PDEs. It introduces a new multi-environment framework, where environments are defined by specific PDE coefficients, each describing a specific behavior. To do so, the paper proposes a Taylor expansion of a forecaster network at a context vector $\xi^e$ around other context vectors $\xi^j$. It thus collects information from other environments via a context pool of P indices, modulating the forecaster network and allowing also contexts themselves to be self-modulated. The method has other properties: parallelization, interpretability, uncertainty estimation, ... The method is evaluated both for in-domain and out-domain environments agianst two baselines (CAVIA & CODA) on multiple datasets and show competitive or sota performance.

### Strengths
The targeted problem is important. Building neural-ode like solvers able to generalize to changes in the PDE coefficients is important, often referred to solving parametric PDEs.

The method seems novel for learning dynamical systems with changes in pde coefficients. The use of taylor expansion is intuitive and natural. I particularly liked the intuition given line 202-205. Existing context-based methods do not try to leverage information from each context vectors, each describing the environment information. NCF fills this gap.

The method is evaluated on a wide range of PDE problems and is SOTA or competitive when considering a second order talyor expansion.

### Weaknesses
Regarding the writing style of the paper:
- I think there is room for improvement. In the introduction, I think the problem of solving parametric PDEs / learning dynamical systems with varying PDE coefficients should be stated more clearly and explains what is an environment in your specific setting. The introduction should 1) clearly defines the problem of building generalizable neural PDE solvers, 2) what are the different directions taken to do so [1, 2, 3] and 3) explain how your work fits into these different directions and advances the field.
- There are especially 2 paragraphs, where neural ODEs and physics-based (hybrid) approaches are introduced, that are not necessary or too much detailed in my opinion.

The authors state that the method can be interpretable, provides uncertainty quantification and is parallelizable. These are important properties that lack for instance for CoDA, as you mentioned. I think that the paper should have exploit these properties in more depth, provide more ablation studies to show that NCF can exploit these properties such as:
- a detailed analysis showing how the learned context vectors relate to physical parameters, demonstrating interpretability
- benchmarks showing how parallelization impacts training time as the number of environments increases



### Questions
You introduce different context pool strategy (RA, NF, SF). What are the differences in terms of performance for your method? Some ablations should have been done to compare the different methods, e.g.:
- Comparing the performance (e.g. MSE, adaptation time) of RA, NF, and SF for different datasets.
- Analyzing how the choice of strategy impacts the learned context representations.
Then, propose guidelines for choosing the appropriate strategy.

You mentioned LEADS, a multi-task learning problem. It would have been nice to add this baseline to the different generalization experiments, especially for the new datasets that are not present in [3].

Can you provide training time details for the different meta-learning frameworks?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a new method for meta-learning of dynamical systems by enforcing context vector to be smooth and close to each other using a training method based on Taylor expansion of the vector field.

### Strengths
The paper introduces a method that seems reasonable, with several interesting analysis of the behavior of the learned vector field. The related works section does present the most popular baselines and methods for this problem. The datasets used to evaluate the method are in par with what is currently used in the litterature.

### Weaknesses
I have several major concerns on this paper that I will try to rank from higher to lower importance.
1) **Overfit**: I am very confused by the OoD adaption protocol used in the paper. From what I understood, Algorithm 2 is used on the validation set to tune the value of $\xi$ using gradient descent. Then, the prediction error is computed **on the same trajectories as the one used to pick $\xi$**. Given the size of $\xi$, it is most certainly overfitting to the (small) set of trajectories used to tune the context vector. I suspect that the value of $\xi$ is specifically tuned to match a small set of trajectories during validation, hence the results are not representative of the true performance of the model. A quick look at the code seems to confirm that, although it is hardly readable (many commented functions, no comments, empty README, residual files from project development). Moreover, the model performs almost systematically better in OoD setup than in In-domain, (table 1 and 2), which is unexpected, and very unusual.
2) **Unsupported claims**: 
	- "we introduce a *robust*  ..." ? The word "robust" is never used in the experimental section.
	- line 248 : "*The $L^1$ regularization term is particularly vital in promoting sparsity in possibly high dimensional context vector*". Sparsity is indeed used a lot for equation retrieval, such as SinDy-like methods, but I don't see why this is crucial here. Yet it probably is, but I don't see which experiment in the paper justify this.
	- "*straightforward method for uncertainty quantification*": seems like an overstatement according to my understanding of the experiment. Quantifying the uncertainty means that the model can provides an interval to which the true trajectory must belong (up to some probability score). From what I understand from your experiment, you consider that the predictions from your model obtained with different contexts (including unrelated to the current environment) gives an uncertainty on the prediction.
3) **Motivation of the method**: the use of Taylor development is motivated (section 3, l.200 to 206) by the fact that it forces context vector to remain close. It is not clear to me why closeness is important for the task, and more importantly why simpler regularization to force $\xi_i$ to remain close from each other would not perform well.
4) **Complexity of the method**: training NCF requires to compute the second order derivative of a neural network, and then back-propagate through the entire computation graph, including the use of a Neural ODE. The method seems utterly complex and computationally demanding. Moreover, some design choices are unclear to me (see questions). Many hyper-parameters have to be set, and the paper provides no clear indication on how to set them (mostly, size of the context vector and context pool mode (RA, NF or SF)). However, I did appreciated the experiments on the size of the context pool. 

	Finally, Figure 7 and 16 shows training curves of the model exhibiting high spikes, including one (figure 7) from which the model never recover. This seems to indicate a highly unstable and difficult training, which is not a good sign for extrapolation to more complex dynamics.
	
5) **Experimental section**: It seems that the order 1 NCF model is trained with a different algorithm than the order 2 (l.264-268). I am not sure to see why, and more importantly, if the gap between the two models in table 1 is due to the supplementary order of the Taylor expansion, or the different training algorithm.

**Minor** (no effect on rating)
- in the introduction: "*Its dynamics are heavily depending on its parameter*" looks like an overstatement. The dependance of a dynamical system on its parameter can vary significantly from a system to another.
-  In section 2, you mentioned that CoDA involves two networks instead of one, hence requiring more computational resources to train. Your approach uses three networks. You might clarify this statement to explicitly mentioned hyper-networks as the bottleneck, and not the use of two networks ?
- in the beginning of section 3 (l.168), $\mathcal{D}_{ad}$ is mentioned before being introduced.
- L. 171, you refer to the smoothness assumption as an inductive bias. It's closer to a constraint than a real inductive bias (or at least, it is an inductive bias on the type of dataset you will test your model on, but not an inductive bias of general physical systems).

**Motivation for my grade**
My grade is mostly driven by my suspicion of overfitting. However, I am also concerned by the (in my opinion) poorly motivated design choices (use of Taylor expansion to promote closeness of context vector, supplementary encoder for context vector, back-propagating through the Hessian) and my difficulty to understand several claims and experiments.

### Questions
1) Did you used **different** trajectories to compute the metrics in the tables than the one used to perform the adaptation in OoD setup?
2) Could you please explain why your model performs better in OoD than InD ? This is an unexpected resuls : we would expect the model to perform always better on seen data.
3) Could you clarify what *robust* means in this context ? (robustness to OoD, to noise, to unseen initial condition ? ) and point to the corresponding experiment that support the claim ?
4) Could you elaborate on the motivation of using Taylor expansion for training the model ? If the main reason behind this is to force context to remain close, then a crucial ablation is missing where the Taylor expansion is replaced by a simple distance loss between context vector. 
5) The context vector is a learned embedding, so what is the point of learning a supplementary dedicated network to convert it into $\tilde \xi$, since you could directly learn $\tilde \xi$ ? In the paper, you explains that "this allows the framework to automatically balance the potentially non linear influence of the context with that of the state vector". What does this means ? Could you please elaborate on this ?
6) Could you please justify the claim line 248 that $L^1$ regularization is crucial ? Did I miss the ablation of this regularization in the paper ?
7) I am not sure to understand fig. 6. It seems that you collected the prediction of NCF for a same initial condition with different context vectors (including unrelated ones) and consider the max/min of these prediction as uncertainty measure. Hence my questions:
	- What is the probability of the true solution to lie within these bounds ?
	- It seems that all model gives fairly similar outputs, which is surprising since they are adapted to different dynamics. How do you explain that ?

**Minor**
 - I do appreciate code release. May I ask you to document and clean the code before publication ?
 - Could you please fix the url link to the associated github repo in the paper ?
 - Could clarify if Theorem 3.2 should be considered as a contribution ? It seems to be a straightforward application of Theorem 2 in Li et al, 2019. If not, it might be interesting to provide more details about what changed, and for which reason.

# Rebuttal update
The authors have provided a thorough reply to most of my concerns and have clearly demonstrated that my suspicion of overfitting was unfounded. This significantly impacts my evaluation, and I have raised my score from 1 to 5.

However, I still recommend rejecting this paper. While the proposed method is interesting and well-supported, it would benefit from further development, particularly in the analysis of its behavior. Although the authors made commendable efforts to improve their manuscript, the short timeframe allocated for rebuttals limited the depth of the supplementary results included. Specifically:

- The emergence of clusters of "similar" environments due to the context pool-filling method, coupled with the Taylor expansion constraint, is a compelling idea. However, it warrants deeper exploration, perhaps with more environments and a detailed analysis of the content of these clusters. These behavior is at the heart of the success of NCF and deserve a better, deeper exploration.
- Some design choices remain unclear, particularly the use of a projection network on the context embeddings.
- The authors have strengthened the "uncertainty"-related experiments, but this discussion should have been made clearer in the main paper. However, addressing this would require significant restructuring of the paper, which is impractical within the rebuttal timeline.

For these reasons, I have updated my evaluation to a borderline rejection. While the paper presents interesting results, I believe it is not yet ready for acceptance.

### Soundness
2

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
This paper proposes NCF to solve parametric ordinary differential equations. It is designed to improve the adaptability and generalization of learning dynamical systems across various environments. NCF introduces a meta-learning approach that employs a context-modulation mechanism, incorporating uncertainty estimation. Specificaly,  NCF uses k-th order Taylor expansion to enable contextual self-modulation. The authors demonstrate the performance of NCF on a variety of ODEs and PDEs problems and illustrate the effectiveness of the proposed methods.

### Strengths
(1) Introducing a meta-learning framework to study complex dynamical systems driven by ODEs and PDEs is a novel and interesting direction.
(2) This article includes both experimental validation and some theoretical analysis.

### Weaknesses
 (1) Currently, there are several methods for parameterizing equations, such as those for ordinary differential equations [1] and partial differential equations [2]. In the paper, the authors mainly compared their approach with meta-learning methods like CAVIA and CODA. So, does it have a competitive advantage over other non-meta-learning methods?
[1] Parameterized Neural Ordinary Differential Equations: Applications to Computational Physics Problems
[2] Identification of the flux function of nonlinear conservation laws with variable parameters

(2) The authors mentioned that their method is robust. One important aspect of proving robustness is how the model performs when the observed data contains noise. However, this was not demonstrated in the experiments.

(3) The authors converted three PDE problems into ODE problems for their study. They should provide a detailed description of how this conversion was done and how the errors were controlled during the process. PDE problems are quite sensitive to the choice of numerical schemes, and different discretization methods can significantly affect the accuracy of the solution. Converting them into ODEs and solving them using an ODE solver will inevitably introduce errors.

(4) The link to the code provided in the paper is inaccessible.

### Questions
Refer to weakness.

### Soundness
3

### Presentation
3

### Contribution
2
