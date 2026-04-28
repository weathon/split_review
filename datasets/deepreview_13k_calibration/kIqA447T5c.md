# Bellman Diffusion: Generative Modeling as Learning a Linear Operator in the Distribution Space

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 6, 5, 5

## Abstract
Deep Generative Models (DGMs), including Energy-Based Models (EBMs) and Score-based Generative Models (SGMs), have advanced high-fidelity data generation and complex continuous distribution approximation. However, their application in Markov Decision Processes (MDPs), particularly in distributional Reinforcement Learning (RL), remains underexplored, with the classical histogram-based methods dominating the field. This paper rigorously highlights that this application gap is caused by the nonlinearity of modern DGMs, which conflicts with the linearity required by the Bellman equation in MDPs. For instance, EBMs involve nonlinear operations such as exponentiating energy functions and normalizing constants. To address this problem, we introduce \emph{Bellman Diffusion}, a novel DGM framework that maintains linearity in MDPs through gradient and scalar field modeling. With divergence-based training techniques to optimize neural network proxies and a new type of  stochastic differential equation (SDE) for sampling, Bellman Diffusion is guaranteed to converge to the target distribution. Our empirical results show that Bellman Diffusion achieves accurate field estimations and is a capable image generator, converging $1.5 \times$ faster than the traditional histogram-based baseline in distributional RL tasks. This work enables the effective integration of DGMs into MDP applications, unlocking new avenues for advanced decision-making frameworks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors propose a new genarative model, Bellman diffusion, that only depends on the density and its derivative. This choice enables learning return distributions in distributional RL as it's consistent with the linearity requirement of an MDP.

### Strengths
* The author propose a sampling technique that combines both the target density and its derivative and show that it theory it leads to convergence to the target.

### Weaknesses
* Structure and clarity: The paper can be restructured in a better way.  For instance, the motivation would be clearer if it would have integrated some material from Sec. 21 can help convey in the intro. Also, in the intro, the authors refer to equations (83) from the approach section. This assumes that the paper has to be read twice?

* Notation issues:
** x is undefined in Eq1
** The prime is Eq2, line 2, right most term, should be applied to z
** Extra dot in line 185

* Formulation lacks preciseness: 
** Eq 1 in linear in p but not linear in x. The fact that the linearity is related to the operator can only be understood in Sec 2.2
** The explanation of eq2 can be clearer is it would have explicitly mentioned that the energy formulation transforms the equality in eq2 into an inequality. 

* Approach:
** What's the use of the isotropic Gaussan in Eq 199? There are no references to how this proxy is derived. It's similar to score matching with a new Gaussian term?
** The score matching loss is not scalable (even the sliced version is not). It's established that score matching is not equivalent to fisher divergence because the derivation requires integration by parts which assumes access to an infinite number of samples. This is not the case in practice.
** A sub-section or a figure/algorithm showcasing how this generative model can be used in distributional RL is missing.

### Questions
* Please, check weakness section.
* Instead of Eq12, why not use SVGD sampler and the derived distribution following:
Messaoud S, Mokeddem B, Xue Z, Pang L, An B, Chen H, Chawla S. S $^ 2$ AC: Energy-Based Reinforcement Learning with Stein Soft Actor Critic. ICLR., 2024 ?
The sampler doesn’t depend on the score of the updated particle itself, which makes it have the desired property of linearity.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a new generative framework, Bellman Diffusion, tailored for applications in Markov Decision Processes (MDPs) and distributional reinforcement learning. Because of the inherent non-linearity in the modeling operator, traditional generative models such as energy-based models (EBMs) and score-based generative models (SGMs) cannot be applied to RL contexts; they cannot preserve the linearity of the Bellman update. The proposed new model addresses this challenge by modeling both gradient and scalar fields directly in the distribution space, thereby maintaining linearity and enabling effective generative modeling in MDPs.

The paper introduces divergence-based training methods to optimize neural networks to approximate both fields and defines a specialized SDE for sampling. On the theoretical side, the paper proves that the proposed model will converge to a target distribution (in terms of both KL divergence and Wasserstein distance) regardless of the initial distribution. Experimentally, Bellman Diffusion demonstrates superior performance in estimating and generating target distributions. Also, the proposed model performs well on two OpenAI Gym environments and converges faster than the baseline model.

### Strengths
1. The proposed model addresses a key gap in using deep generative models for Markov decision processes. It is well motivated by maintaining the linearity of the Bellman equation.
2. Following the motivation, the authors build a solid theoretical framework around the proposed model. Some important theorems are stated and proved, including the steady-state convergence theorem (Theorem 4.1) and error bounds for neural network approximation (Theorem 4.2). Note that I do not fully follow the proof in the appendix, and cannot guarantee its correctness.
3. The experiments performed are in a variety of domains, including synthetic point distributions, images, and RL enviroments. I especially like the experiments on OpenAI Gym, which demonstrates the fast and stable convergence of the proposed model over the conventional baseline.

### Weaknesses
While this paper is primarily focused on methodology and theoretical contributions, I believe there is room for improvement on the experimental side:

1. The abstract claims that the proposed model is a "capable image generator." However, the only image generation results provided are on MNIST (Figure 7, Appendix), and these are purely qualitative. This claim would be better supported with quantitative experiments on real-world image datasets. The lack of quantitative metrics makes it difficult to assess the true performance of the model in image generation tasks. For example, reporting metrics like FID or IS scores on a standard dataset would be necessary to validate the claim.

2. Are there specific reasons preventing the application of Bellman Diffusion to larger or more complex RL environments? Currently, only two simple examples are shown. Additionally, if possible at all, it would be valuable to compare the performance of Bellman Diffusion with that of denoising diffusion models on these RL tasks, to observe how the non-linearity of traditional diffusion models impacts their performance in this context. The current experiments do not fully explore the limitations of the proposed approach in more challenging RL scenarios, and a comparison with diffusion models would provide valuable insights into the trade-offs of the proposed approach.

### Questions
1. How strong are the assumptions (Assumptions C.1 and C.2) required for proving Theorems 4.1 and 4.2, compared with those typically used in related theoretical analysis? It would be helpful to see more justification regarding their validity. For example, could you provide examples of other works in the field that rely on similar assumptions?

### Soundness
4

### Presentation
3

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
This paper introduces Bellman Diffusion, a novel generative model designed to approximate both the gradient and scalar field of the data’s probability distribution. Bellman Diffusion is distinguished by its linear modeling property, meaning that if we aim to model a combined distribution f+g, we can simply sum the fields of f and g. This property is particularly advantageous for distributional reinforcement learning (RL). By first modeling the distribution of returns in terminal states, we can subsequently perform Bellman-like updates on the approximated fields, ultimately deriving the distribution for all states in the Markov Decision Process (MDP). In essence, Bellman Diffusion’s linearity makes it well-suited for distribution modeling tasks where data exhibits a linear structure. The authors validate Bellman Diffusion’s effectiveness through evaluations on low-dimensional toy tasks, high-dimensional benchmarks, and applications in distributional RL.

### Strengths
The motivation behind this paper is both clear and compelling. In reinforcement learning, many distributions exhibit inherent structures that can be effectively described through Bellman iteration. Beyond the return or value distribution, other examples include the successor state distribution, which describes the probability of transitioning to a state s' at any time after taking an action a in a state s. Learning these distributions—even with powerful generative models—can be challenging if the data’s inherent structure isn’t properly respected. In this regard, Bellman Diffusion offers a practical solution, enabling the modeling of such structured distributions in a way that aligns with their underlying characteristics.

### Weaknesses
The presentation of the paper is poor. Since the authors motivate their approach through its application in distributional reinforcement learning, it would be more effective to explain how Bellman Diffusion can be integrated into and facilitate distributional RL (currently in Appendix D) directly within the main method section.

The evaluation of the proposed method is quite limited in both comparisons with existing methods and also the explanations about the performance.
+ In Section 6.1, the authors primarily demonstrate that Bellman Diffusion can model synthetic data distributions (though there are apparent modeling inconsistencies). Including comparisons with established baseline methods, such as DDPM, would provide a clearer picture of the advantages Bellman Diffusion offers.
+ In Section 6.2, given that the tasks lack internal structures, it raises the question of why Bellman Diffusion outperforms DDPM in certain tasks. Further explanation here would clarify the observed performance benefits and also certain claims made in line 431. Regarding Section 6.3, the benchmark environments (FrozenLake and CartPole) are too simple to truly assess the method’s effectiveness. These environments have relatively small state and action spaces, leading to straightforward return distributions. In contrast, existing methods like C51 are validated on more complex tasks, such as those in Atari environments, which exhibit greater structural complexity. In light of this, I think it would be necessary to extend the evaluations to more complex environments to truly reflect the effectiveness of the proposed method.

### Questions
One concurrent work [1] also seems to optimize the diffusion model in a temporal difference manner, and they used existing diffusion models, rather than proposing a new SDE with linear operators as in Bellman Diffusion. Although I understand that [1] deals with the successor measure instead of value distribution, could the authors briefly discuss about the difference or relationship between [1] and Bellman Diffusion? 

[1] Liam Schramm and Abdeslam Boularias. Bellman Diffusion Models.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces Bellman Diffusion, a deep generative modeling framework designed to overcome limitations in applying existing generative models to Markov Decision Processes (MDPs), especially when the downstream task is distributional Reinforcement Learning (RL). The authors identify a key issue: the nonlinearity of modern deep generative models conflicts with the linearity required by the Bellman equation in MDPs. To address this, they propose modeling the gradient field and scalar field of the target distribution directly, which preserves linearity.

### Strengths
1.	The paper put forth an innovative solution to a well-defined and very interesting problem in applying generative models to MDPs.

2.	The authors provide a rigorous theoretical basis for their algorithmic innovations, including convergence guarantees and error bound analysis.

3.	The paper offers detailed algorithms for training and sampling, making the method easier to follow for implementation purposes.

4.	The authors demonstrate the effectiveness of Bellman Diffusion on both synthetic and real datasets, and also show improvements towards distributional RL tasks.

### Weaknesses
1. The method introduces additional complexity compared to traditional histogram-based approaches, which may limit its adoption in some practical scenarios.

2. While the paper shows improvements over histogram-based methods, comparisons with other advanced generative modeling techniques in RL contexts are not extensively explored.

3. The paper does not thoroughly address the scalability of the method to very high-dimensional problems or large-scale RL environments.

4. The authors must improve quality and readability of their figures and other visualizations. For instance, Figure 4 is especially hard to follow.

5. There are multiple typos/grammatical errors across the manuscript which should be fixed.

### Questions
In addition to the aforementioned weakness comments, I request the authors to provide clarifications for the following questions.

1.	Are there any limitations or failure cases where Bellman Diffusion does not perform well compared to other generative modeling approaches?

2.	How computationally expensive is the training process for Bellman Diffusion compared to other generative modeling approaches? Are there any tricks used to improve training efficiency?

3.	The paper shows experimental anecdotes on how Bellman Diffusion could effectively learn multi-modal distributions. How does it compare to other methods like normalizing flows or mixture density networks for multi-modal density estimation?

4.	The slice trick is used to improve sample efficiency. How sensitive is the method to the choice of slice vector distributions q(v) and q(w)? Are there guidelines for selecting these?

5.	Can the authors please share details of the implementation codebase that was used for the experimental evaluations ?

### Soundness
2

### Presentation
2

### Contribution
3
