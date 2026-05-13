# Grokking as a First Order Phase Transition in Two Layer Networks

- Decision: Accept
- Scores: 3, 6, 8, 6, 6

## Abstract
A key property of deep neural networks (DNNs) is their ability to learn new features during training. This intriguing aspect of deep learning stands out most clearly in recently reported Grokking phenomena. While mainly reflected as a sudden increase in test accuracy, Grokking is also believed to be a beyond lazy-learning/Gaussian Process (GP) phenomenon involving feature learning. Here we apply a recent development in the theory of feature learning, the adaptive kernel approach, to two teacher-student models with cubic-polynomial and modular addition teachers. We provide analytical predictions on feature learning and Grokking properties of these models and demonstrate a mapping between Grokking and the theory of phase transitions. We show that after Grokking, the state of the DNN is analogous to the mixed phase following a first-order phase transition. In this mixed phase, the DNN generates useful internal representations of the teacher that are sharply distinct from those before the transition.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper makes attempts to explain the grokking phenomenon in deep learning via an adaptive kernel approach (Seroussi et al., 2023). Two settings are studied: a student erf-network learning a single index teacher; and a two-layer net with quadratic activation learning modular addition.

This paper doesn't introduce the background knowledge and related work at all, making it a very hard task to understand what they are exactly doing.

### Strengths
* This paper seems to have made some efforts to explain grokking, though I cannot fully understand them.

### Weaknesses
This paper makes attempts to explain the grokking phenomenon in deep learning via an adaptive kernel approach (Seroussi et al., 2023). Two settings are studied: a student erf-network learning a single index teacher; and a two-layer net with quadratic activation learning modular addition.

This paper doesn't introduce the background knowledge and related work at all, making it a very hard task to understand what they are exactly doing.

### soundness:
 2 fair

### presentation:
 1 poor

### contribution:
 2 fair

### strengths:
 * This paper seems to have made some efforts to explain grokking, though I cannot fully understand them.

### weaknesses:
 * This paper is poorly written. It claims that it is using an "adaptive kernel approach" to explain grokking, but they never explains what this method is. I tried to read the previous works, but they are not easy to read for ML audience, either. I urge the authors to introduce the background better: What is the "adaptive kernel"? Why is it important to study "action"? Why does the approximation in the paragraph beginning with "Next," in Page 4 make sense? What is the theory of phase transition in physics? How are phase transitions connected to bifurcation and saddle point equations? The current version of the paper contains too many unexplained jargons. Even if I could have spent hours reading previous works to understand the background better, I don't believe the current version of the paper is ready for ML audience to read.
* If this paper focuses on theory, then it is better to organize the claims into theorems and lemmas. In the current version, there are no theorems and lemmas at all. Everything seems to be stated in a very informal way, making it very hard to check the correctness.
* In my current understanding, the whole "adaptive kernel approach" builds on top of the Langevin dynamics, where isotropic noise is injected into the weights. If there is no noise or the noise is not isotropic, then the theory in this paper may not hold anymore. However, in the paper that proposes grokking (Power et al., 2022), the noise should be from the random sampling of batches and thus can hardly be isotropic, but the grokking phenomenon can still be observed. The adaptive kernel theory in this paper cannot cover this case at all.

### Questions
I would like to ask the authors to give more introduction of the technical tools they are using and rephrase their results in terms of theorems and lemmas.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies Grokking by building on prior work on adaptive kernel approaches for feature learning and claims that Grokking can be understood as a phase transition between different internal representations of the network. The authors explore feature learning in the two models studied (cubic teacher and modular addition) through this mapping to phase transitions.

### Strengths
- The formal treatment of Grokking using the approach proposed appears to be novel and compelling.
- Understanding the phenomenon through the lens of feature vs. lazy learning and casting it in the language of phase transitions is a direction of research that many prior works speculated about. This paper presents much interesting work in this direction.

### Weaknesses
 - The connection to Grokking, as observed in prior work across various tasks and modalities, seems almost secondary in this paper. This work focuses on some toy models, solves them, and refers very little to the general phenomenon of delayed generalization. The analysis is limited to two specific toy models (cubic teacher and modular addition), and the paper does not sufficiently explore the broader implications for more complex or real-world scenarios. The link between the observed phase transitions in these models and the Grokking phenomenon in more general settings remains unclear. The paper would benefit from a more thorough discussion of the limitations of the chosen models and how the results might generalize to other architectures and tasks.

The general feeling I have from this paper is that the approach somewhat obscures the contributions and implications. The formalism developed here and in the referenced work seems compelling, yet the paper does not go beyond two simple toy models. It’s not immediately clear which aspects can be generalized to other problems and what insights a reader can take away to their particular settings. It would have been great had the paper explored some of the directions suggested in the discussion section. For instance, providing a measure for Grokking on problems in the wild or studying whether using this formalism for pruning/regularization could be a fruitful application. Without these directions, I find it difficult to recommend a strong acceptance. But overall, I like the approach and would want to see more work in this direction, so I give a score of 6 (weak accept).

### Questions
- “We set the gradient noise level … under the equilibrium ensemble of fully-trained networks.” Feels ambiguous. Could you clarify?
- Could you clarify Figure 2? Specifically, the caption implies a qualitative change at the phase transition point, but I’m not sure what I’m supposed to be looking for. Also, how is it that increasing the strength (in abs terms) seemingly improves the linear component?
- Why is there a -1/P term in the definition of the target labels in the modular addition case?
- Is there a reason why the modular addition task is referred to as a student-teacher setting? It doesn’t feel like a teacher is involved here; the targets are simply the modular addition labels.

**Nits:**
- Typo: In section 3.1.2, “effecting amount of data” should be “effective amount of data”
- Better flow if Figures 1 and 2 were moved closer to the text explaining them. Otherwise, the reader might have to keep moving between pages.
- I think the paper could have a broader reach if improved intuition is provided (e.g., explaining how the terms in the action stem from the loss, regularization, and added noise more explicitly).

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies phase transitions in a model of deep neural networks. The authors focus on two distinct tasks: polynomial regression and modular arithmetic. Using an approach to study large width neural networks trained to equilibrium with Langevin dynamics, they derive an action that defines the Bayesian posterior distribution of read-in weight vectors given the training data. The authors show a competition of the Gaussian weight prior proportional to $\log p(w) \propto - \frac{1}{2} |w|^2$ and a data dependent likelihood term which arises from integration of the readout layer. Because of the competition of these terms, the action can transition from having one saddle point at $w=0$ (giving the lazy NNGP kernel + small feature learning corrections) to having multiple saddle points which all contribute to the final predictor. Beyond a certain point, the outlier overlap values dominate the action and the $w=0$ saddle point no longer contributes. These define the 3 phases of what the authors refer to as Grokking transitions and the three phases are Gaussian Feature Learning (GFL), then Gaussian Mixture Feature Learning GMFL-I and GMFL-II.  For tasks with a target function that is controlled by a single direction $w^*$ , they show that the overlap $w \cdot w^*$ has a distribution which becomes multimodal and that this can be made dramatic by scaling up the likelihood term. The authors argue that this phenomenon can lead to sudden changes in the learned representations and generalization error in neural networks as a function of $\sigma^2$ , dataset size $n$ or model width $N$ since all three of these quantities appear in the likelihood term, in analogy to first order phase transitions.

### Strengths
This paper extends a promising approach to neural network theory, known as the adaptive kernel approach, which studies how the kernels of deep networks adapt to data after feature learning. This paper provides two interesting case studies (polynomial regression and modular arithmetic) where they make progress on deriving an effective action which depends only on overlaps with the teacher direction $w^*$ or $v$. They show that the derived theory is accurate in simulations of networks on these learning tasks.

### Weaknesses
While the phenomena described and the resulting theoretical picture of 3 phases is quite impressive, I am not sure that this transition constitutes grokking as it is usually understood where training loss decreases much earlier than test loss during gradient based learning dynamics.  I do not see this as a fundamental limitation of the paper (which I quite appreciate) but mainly as an issue of framing. In my opinion this work is a more fundamental phenomenon than grokking since it pertains to fundamental questions in deep learning such as how width, data and parameterization affect feature learning. The paper is not completely rigorous and relies on various approximations, but I think that is completely fine since it supports its claims with experiments and computations at a physics level of rigor. It also relies on some prior work from Seroussi et al 2022 and a short summary of this approach in the Appendix could be helpful. Lastly, some of the exposition is a bit challenging to follow (see questions below).

That said, if these issues/questions are addressed I would be happy to raise my score.

### Questions
1. I am a bit confused about the scaling limits. What is the exact order of limits taken? Is width $N$ and data $n$ scaled together in some way? Is the kernel $Q$ always full rank? What about the scaling of $\sigma^2$ with various quantities? In the Appendix, this is discussed in a high level ($n$ large first, then $d$), but the resulting action still contains factors of $N, d, \sigma^2$ , etc rather than $O(1)$ quantities, which makes it a bit difficult to interpret. Is it thought that the $n$, $d$ limit commute? I suspect not, as the authors discuss various joint scalings like $n \sim d^3$ or $n \sim d^{1.5}$ etc in Appendix. Which (if any) of these are actually adopted when deriving the action? 
2. In the Appendix A.1 the authors describe how they adopt a mean field parameterization, yet the resulting action’s likelihood term vanishes as $N \to \infty$. Is it clear why finite width networks would have less feature learning in the mean field parameterization? I was under the impression that this should be constant with $N$. 
2. Could one study mean squared error so that the likelihood term was intensive in dataset size corresponding to a loss $\mathcal L = \frac{1}{n} \sum_{\mu=1}^n \ell(x_\mu, y_\mu)$ and parameter distirbution $p(\theta) \propto \exp\left(  - \beta \mathcal L - \frac{1}{2} |\theta|^2 \right)$? If this choice was made does the dataset size still control the phase transition? The reason I ask is because this would correspond to Langevin dynamics on a reasonably scaled and regularized cost function $\mathcal L + \frac{1}{2\beta} |\theta|^2$ with added Brownian motion with variance $\frac{2}{\beta}$, which at large $\beta$ is closer to how networks are trained in practice ( mean loss, rather than extensive sum over data points). I am wondering if many of the factors of $n$ which appear in the computation are in fact artifacts of the comparison of the raw scale of the likelihood to the prior.
4. I understand that the density of $w$ undergoes transitions as the number of critical points in the action changes, requiring use of multiple saddle points when computing observable averages. Why must a saddle point approximation over the density of weights $w$ be taken? One could also imagine computing observable averages by sampling this non-Gaussian density as in works on mean field neural networks like Mei et al 2019 or Bordelon & Pehlevan 2022? Is there something lost by approximating each ``well” around a minimum of the action $S(w)$ with a quadratic? Is this the approach taken by the authors when they predict macroscopic quantities like scale of cubic component in the predictor? Could the authors comment on these different approaches?
5. Could there be a connection between the phase transition reported here and the transition in https://arxiv.org/abs/2210.02157 Figure 5c where as the feature learning strength $\gamma_0$ increases, the training dynamics transition from having a convergent perturbation series in $\gamma_0^2$ to a non-perturbative regime where the power series diverges?

### Soundness
3 good

### Presentation
2 fair

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors provide a heuristic analysis of two settings (a teacher-student model and a modular arithmetic model), which they show exhibit the grokking phenomenon. They relate this phenomenon to a first order phase transition, and provide a characterization of the effective action, with grokking corresponding to the transition from one minimum to the apparition of local minima.

### Strengths
The question addressed (grokking, and on a higher level feature learning) is an important one, and the authors provide an insightful and intriguing viewpoint  into how it arises. I also acknowledge the fact that the settings the authors set out to analyze are theoretically very challenging, making the provided insights valuable.

### Weaknesses
Overall, I find the presentation and clarity to be rather poor, making it hard to identify the claims and judge their soundness, and am in favour of rejection. If the authors clarify some points and promise to greatly overhaul the presentation I am happy to increase my score.

General remarks:
- The main presentation issue is to me the excessive focus on the technical details of the derivation,  from 2.4 to 3.1.2, at the expense of necessary details. For example, the discussion of the Langevin dynamics in 2.3 would strongly benefit from having the corresponding equation clearly written for definiteness, especially because several conventions exist, and also for the sake of readability.
- While I admit some technical details are essential in the understanding of the result and the flow of the paper,  this is not the case of all of them (e.g. the discussion at the beginning of 3.1.1 could be shortened). 
- As a consequence, the assumptions on the scaling of $d,n,N$ are also dispersed through the text, making it difficult to follow which assumptions are needed in the end for the results to hold.

- In 3.1, "$\sigma^2/n$ is kept fixed". Do you mean $\sigma^2 \sim n$ in scaling? Wouldn't the result of Cohen et al. rather hold for $\sigma^2=O(1)$?

- In 3.1.2, "thus the assumption that higher-order Hermite polynomials are irrelevant becomes inadequate." : I do not find which assumption this line points to. Does it refer to the ansatz (12)? Since the target only depends on $H_{1,3}$, I do not understand why the model would depend on higher order Hermites, nor why this would be a sign of feature learning. Could you elaborate?

- Am I right to understand the theory quantitatively predicts the experiments only in the GFL phase, and only holds qualitatively in terms of phenomenology to explain the transition to GMFL-I and II phases?

- (Minor) In Fig. 2, solid lines correspond to the theory? It should be explicitly stated for better readability.

- (Minor)  It would be more compelling to complement Fig. 3 with experimental simulations, similarly to Fig.1 middle and right.

### Questions
- In 3.1, "$\sigma^2/n$ is kept fixed". Do you mean $\sigma^2 \sim n$ in scaling? Wouldn't the result of Cohen et al. rather hold for $\sigma^2=O(1)$?

- In 3.1.2, "thus the assumption that higher-order Hermite polynomials are irrelevant becomes inadequate." : I do not find which assumption this line points to. Does it refer to the ansatz (12)? Since the target only depends on $H_{1,3}$, I do not understand why the model would depend on higher order Hermites, nor why this would be a sign of feature learning. Could you elaborate?

- Am I right to understand the theory quantitatively predicts the experiments only in the GFL phase, and only holds qualitatively in terms of phenomenology to explain the transition to GMFL-I and II phases?

- (Minor) In Fig. 2, solid lines correspond to the theory? It should be explicitly stated for better readability.

- (Minor)  It would be more compelling to complement Fig. 3 with experimental simulations, similarly to Fig.1 middle and right.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper attributes grokking to a phase transition described by a Laudau-like theory using techniques of Gaussian processes. In the grokking process, representations form more and more "droplets", until these droplets come together to form water, completing the phase transition. The physical intuition is clear and makes sense. However, I'm not sure whether this theory really explains grokking or something else, given that there is no empirical experiments that compare NN training results to theory.

### Strengths
This paper is well-motivated and well written.

### Weaknesses
 * The physical picture should be made clearer, to help non-physicist readers. For example, it would be nice to have a figure illustrating what you mean by "droplet" in terms of physics, and in terms of grokking. Specifically, how do these "droplets" relate to the learned features or representations within the neural network? Is a droplet a single feature, a collection of correlated features, or something else entirely? The analogy to phase transitions is compelling, but a more concrete connection to the neural network's internal state is needed.
* The link to NN training is unclear. How to translate the theory to NN training results? The paper mentions full-batch gradient descent with a vanishing learning rate and added noise, but it's not clear how these specific training conditions map to typical neural network training scenarios. For example, how does the theory account for the use of mini-batches, adaptive learning rates, or different optimization algorithms? Are there specific predictions that can be tested on real neural networks trained under more realistic conditions?
* The fact that the analysis only applies to two-layer networks is not satisfactory but understandable. While the kernel adaptation formalism might extend to deeper networks, the current analysis is limited. It is important to discuss the limitations of this approach and how the results might change for deeper architectures. For example, do the phase transition characteristics change with network depth, or are there other phenomena that might arise in deeper networks that are not captured by this theory?
* Missing some literature review on grokking, e.g., "Omnigrok: Grokking Beyond Algorithmic Data" and "Explaining grokking through circuit efficiency".

### Questions
See weaknesses above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
