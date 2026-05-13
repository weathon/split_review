# Generator Matching: Generative modeling with arbitrary Markov processes

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
We introduce \emph{Generator Matching}, a modality-agnostic framework for generative modeling using arbitrary Markov processes. Generators characterize the infinitesimal evolution of a Markov process, which we leverage for generative modeling in a similar vein to flow matching: we construct conditional generators which generate single data points, then learn to approximate the marginal generator which generates the full data distribution. We show that Generator Matching unifies various generative modeling methods, including diffusion models, flow matching and discrete diffusion models. Furthermore, it provides the foundation to expand the design space to new and unexplored Markov processes such as jump processes. Finally, Generator Matching enables the construction of superpositions of Markov generative processes and enables the construction of multimodal models in a rigorous manner. We empirically validate our method on protein and image structure generation, showing that superposition with a jump process improves image generation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a framework for creating generative models using arbitrary Feller processes. The framework is based on the concept of a generator that describes the infinitesimal change of distribution of a Feller process and on a possibility to learn that generator through minimizing a training objective. Existence of such a framework allows to design novel generative approaches and perform model combinations for building multimodal generative models.

### Strengths
**Significance and originality.** The main result of the paper lies in developing a generalization of the existing generative models into one theoretical framework. For example, the universal characterization of generators (provided by Theorem 1) appears for the first time in machine learning literature. Moreover, the result is stated for time-inhomogeneous Markov processes while the vast majority of mathematical literature focuses on studying properties of time-homogeneous ones. The paper also demonstrates immediate benefits of having such a theoretical framework by designing two new generative models based on jump and diffusion processes. 

**Clarity and quality.** Overall, the paper is well-executed and well-written. It provides necessary background into Feller processes. The authors usually provide a motivation and an intuition behind introduced mathematical concepts. The paper gives guidance principles to build new generative models in a concise manner. The proposed generator matching framework is both mathematically sound and computationally feasible. The authors provided the empirical results on protein and image generation to demonstrate validity of the approach.

### Weaknesses
The main weakness of the paper is that the authors ignore previous results that have been done for jump processes [1, 2]. For example, [1] introduces a theoretical framework for constructing Diffusion Models in discrete-state spaces for an arbitrary Markov process, which can be either discrete time or continuous-time in nature. [1] uses generators and adjoint generators together with Chapman–Kolmogorov equations. Moreover, [1] constructs a generative model using the pure-death process, which, in its turn, is the example of jump processes. [2] focuses on the Levy process.  I believe the authors should provide a very detailed comparison with these papers in section 8 (Related Work).

I believe that the exposition of the framework can be improved. It still remains unclear from the paper why the generator $L_t$ can be used in forward and reverse processes. It remains unclear why using generators and adjoint KFE leads to “correct” generated samples.

 The authors skip a discussion of Anderson’s result [3], which was an important brick in developing generative diffusion models. Why is it not needed in the general framework? Why does focusing on matching of probability paths remove the need for Anderson's result for generators and adjoint generators?

Why does regularity assumption 2 (finite number of discontinuities) is needed? I see that the authors discard one of the terms in the proof of theorem 1. What does this term break in the framework if we do not discard it?

The authors state several times through the main part of the paper that generator matching works with arbitrary Markov processes while in reality they restrict the family of Markov processes to Feller processes. Do the authors expect that restricting to Feller processes may not be needed and the whole framework can be applied to any process with just Markovian property?  

In proposition 1, the object “conditional generator” appears without any definition. I also believe that $X^z_t$ appears for the first time. Could the authors provide a definition of these objects and notation before using it in the proposition? 

Could the authors provide a motivation behind introducing three regularity assumptions on Markov process under consideration? 

*Minor:*

Page 3, line 120. “Starting with the right initial distribution $X_0 \sim p_0$.” What is the meaning (or definition) of “right” in the sentence?

Page 3. Line 096-099. The meaning of $\delta_z(dx)$ is neither defined before nor in the formula. 

What does the authors mean under the words “an informal” in lines 129-130? 

Page 17, lines 762-763. “... the following two regularity … ” -> “... the following three regularity…”

### Questions
1. The authors skip a discussion of Anderson’s result [3], which was an important brick in developing generative diffusion models. Why is it not needed in the general framework? Why does focusing on matching of probability paths remove the need for Anderson's result for generators and adjoint generators? 
2. Why does regularity assumption 2 (finite number of discontinuities) is needed? I see that the authors discard one of the terms in the proof of theorem 1. What does this term break in the framework if we do not discard it?
3. The authors state several times through the main part of the paper that generator matching works with arbitrary Markov processes while in reality they restrict the family of Markov processes to Feller processes. Do the authors expect that restricting to Feller processes may not be needed and the whole framework can be applied to any process with just Markovian property?  
4. In proposition 1, the object “conditional generator” appears without any definition. I also believe that $X^z_t$ appears for the first time. Could the authors provide a definition of these objects and notation before using it in the proposition? 
5. Could the authors provide a motivation behind introducing three regularity assumptions on Markov process under consideration? 

*Minor:*
 
6. Page 3, line 120. “Starting with the right initial distribution $X_0 \sim p_0$.” What is the meaning (or definition) of “right” in the sentence?
7. Page 3. Line 096-099. The meaning of $\delta_z(dx)$ is neither defined before nor in the formula. 
8. What does the authors mean under the words “an informal” in lines 129-130? 
9. Page 17, lines 762-763. “... the following two regularity … ” -> “... the following three regularity…”

[3] Anderson, B. D. Reverse-time diffusion equation models. Stochastic Processes and their Applications, 12(3):313–326, 1982. ISSN 0304-4149.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces the generator-matching (GM) framework for modeling arbitrary Markov processes in both continuous (i.e., $\mathbb{R}^d$) and discrete (i.e., $\\{1,...,N\\}^D$) domains. GM generalizes the (continuous and discrete) flow-matching (FM) approach, extending its concept of transforming the complex task of learning *marginal* distributions/scores/flows/generators to a simpler task of specifying *data-conditional* distributions/scores/flows/generators, and approximating the marginal ones through a loss based on conditional expectations. The framework not only unifies a variety of existing methods across continuous and discrete generative modeling, but also holds promise for multimodal applications, where the state space comprises the product of multiple different state spaces.

### Strengths
As discussed above, The GM framework extends the FM approach, building on the well-established relationships between marginal distributions/scores/flows and their data-conditional counterparts. From my persepective, this framework presents several notable innovations:

1. The introduction of jump, a type of stochastic process in the continuous domain with non-continuous trajectories, which largely unexplored within the generative AI community. Particularly compelling is the result showing that the widely-used conditional path $p_ {t|1}(x|z)={\cal N}(x|tz,(1-t)^2)$ can also be achieved through jumps, highlighting its potential utility for generative tasks.

2. An elegant theorem establishing that the generators of interest in $\mathbb{R}^d$ for applications can be decomposed to three basic types: flow (ODE), diffusion (scaled Brownian motion), and jump. This decomposition underscores the advantages of using the generator perspective in modeling.

The paper also introduces methodologies for: (a) combining models that use different generators, and (b) modeling multimodal data distributions. While not entirely novel, these contributions effectively systematize existing techniques through the GM perspective. Prior works have addressed these topics, for example: the equivalence of backward SDE and backward probability-flow ODE, the detailed balance condition for CTMC (Campbell et al., 2024), and the predictor-corrector for CTMC (Gat et al., 2024) are all examples of model combination; similarly, multimodal flows introduced in Campbell et al. (2024) and earlier models such as FrameFlow and FrameDiff have laid groundwork in multimodal data modeling, potentially inspiring aspects of this work.

Finally, the paper is well-written, featuring clear notations, a strong motivation, and a rigorous mathematical foundation.

### Weaknesses
1. The writing style in some part of the paper, especially section 6, feels overly general and abstract. While the GM framework is indeed comprehensive, it primarily applies to only 4 specific examples: flow, diffusion, jump in $\mathbb{R}^d$, and CTMC in finite state spaces. Although the theoretical concepts like target-affine (TA) loss and Bregman divergences are elegant, they lack practical utility in these contexts. This abstraction, without sufficient illustrative examples, limits the reader's ability to grasp the practical impact of the framework. I suggest exploring these theoretical constructs further to enrich the paper. For instance, theoretically or numerically comparing the performance of the TA-loss and discussing generator choice in more general state spaces would provide valuable insights. Additionally, a discussion on how TA-loss may facilitate the development of better training losses for generative tasks would be appreciated.

2. The literature review for jump-based models is insufficient. Jump is related to piecewise deterministic process (flow + jump) and piecewise diffusion process (flow + diffusion + jump) in the stochastic process literature (see, e.g., Del Moral & Penev, 2014), and there have been several works leveraging such process for generative modeling, e.g., Campbell et al. (2023) and Bertazzi et al. (2024), which the author(s) have not mentioned. Including these citations would better position GM within the broader literature and highlight its contributions.

3. The experiments are not convincing enough and lack the design details necessary for fair comparisons.

- For $\mathbb{R}^d$, the paper introduces two constructions of the conditional probability path (mixtures and geometric averages), each with realizations based on flow, diffusion, jump, or a mixture of these (Markov superposition). The toy example in figure 2 is worth further explorations: (1) Which conditional probability path is recommended for better empirical performance? Comparing the performance on more complex target distributions, such as $6\times6$ checkerboard patterns (Lou et al., 2023), would be informative. (2) Although these processes all generate the same marginal probability distribution in theory, practical implementations face approximation and discretization errors. Which realization provides the best sampling quality? (3) One potential advantage of jump over flow and diffusion is the ability of exploring complicated landscape of target distribution due to its non-continuous nature, but this benefit isn’t evident in the experiments. Therefore, it remains unclear whether the new algorithms offer practical advantages over existing methods, such as FM.

- The details of image generation experiment are lacking, such as the model size, neural network structure, and sampling schedule. The baselines (DDPM, VPSDE, and EDM) are outdated, and the datasets (CIFAR10 and ImageNet32) are less challenging than those commonly used today, such as ImageNet256.

- Despite emphasizing the GM framework’s potential for multimodal data, there are no numerical results on joint multimodal generation. For example, instead of considering protein backbone generation or pure image generation (which are unimodal tasks where existing algorithms already achieved amazing performance), evaluating GM on protein structure-sequence co-generation or image-text joint generation (which has been mentioned in section 7.2) would better showcase its advantage in multimodal settings.

- For the protein experiments, critical experimental details are absent, such as sampling NFE, training time, and model size. The target task is restricted to protein with length less than $128$, a relatively unchallenging setting. Designability, as an important metric for evaluating protein backbone, is not presented. Additionally, more up-to-date work like FoldFlow (Bose et al., 2023) and FoldFlow-2 (Huguet et al., 2024) are missing from the benchmarks. The performance gain achieved by the proposed approach seems to be minimal at the cost of training a separate network with more computational resources. Thus, its efficacy for protein generation remains unclear, especially in comparison to existing methods. It would certainly be more compelling to apply GM to multimodal tasks in protein design by incorporating additional sequence information.

### Questions
1. In appendix D.1, line 1319 suggests that the solution $\lambda_ t(x)$ is not unique. The derivation selects the form that achieves equality on line 1319 (see line 1334). Are there alternative choices of $\lambda_ t(x)$ that also satisfy the constraint? If so, are all choices of $\lambda_ t(x)$ equivalent in some sense, or do they have different characteristics in practical uses (given that they all correspond to the same conditional path $p_ {t|1}(x|z)$)?

2. I don't fully understand the argument in appendix D.2, starting from line 1473. Specifically, can you have a detailed elaboratation on the reason why the prior has compact support poses a potential issue (i.e., lines 1473-1474)? What implications do the non-zero boundaries of $\tilde\sigma_ t^2(\cdot|z)$ have? Moreover, I hope that the author(s) could have a review of the reflected SDE (the process ${\rm d}L_ t$) so that the readers can better understand the intuition behind how this pure diffusion solution to mixture path works.

3. Minor comments:

- I personally don't quite appreciate the unconventional notation $p_ t\odot f$ and $p_ {t+h|t}\odot f$ in this paper. Typically, $p_ t\odot f$ would be denoted as $\mathbb{E}_ {p_ t}f$; in standard textbooks of Markov semigroup (e.g., Bakry et al., 2014), $p_ {t+h|t}\odot f$ in this paper would appear as $P_ {t,t+h}f$, where the semigroup $(P_ {t,s})_ {s\in[t,\infty)}$ is defined as $P_ {t,s}f=\mathbb{E}(f(X_ s)|X_ t=\cdot)$. However, I recognize these non-standard notations may be acceptable within the machine learning community.
- Line 274, *no* diffusion coefficient? Besides, the $x_ 1$ in equation (9) seems to be a typo.
- Line 667: $\mathbb{E}_ {x\sim\mu_ 1}[f(x)]=\mathbb{E}_ {x\sim\mu_ 2}[f(x)]$.
- Line 669: $(X_ t)_ {0\le t\le1}$.
- Line 725: $p_ {t+h|t}(A_ {t+h}|x)$.
- Line 755: the limit operation is missing.
- Line 863: should mention the definition of matrix inner product $A\cdot B=\operatorname{tr}(AB)$ for positive definite $A,B$.
- Lines 901 and 968-978: should be "with probability $...+o(h)$ when $h\to0$".
- Lines 917, 1001-1017, 1050, 1060, 1067, 1072: the parentheses are missing: should be $\int_ {y\ne x}(f(y)-f(x))Q_ t({\rm d}y;x)$. 
- Lines 1112-1125: $B(F_ t^\theta(x))$ is missing.
- Line 1155: the first generator is $\bar{\cal L}_ t$, not ${\cal L}'_ t$.
- Appendix C.6, proof for conditional generator: I suggest deriving the equation by directly applying derivative by parts to line 1178, which simplifies the proof and reduces its length.
- Line 1264, should mention that $\lambda_ t(x)$, $Q_ t(y;x)$ and $J_ t(y;x)$ may depend on $z$, and here this dependence is omitted for conciseness. Similarly, in line 1426, should mention that $a_ t,b_ t$ may depend on $z$ but are independent of $x$.
- Appendix D.1, time-derivative $\frac{\partial}{\partial t}p_ t$: I suggest rewriting the proof by directly calculating $\partial_ t\log{\cal N}(x|tz,(1-t)^2)$, which would simplify the presentation.
- Appendix D.2, I suggest replacing all $p_ {\rm simple}$ with $p_ 0$.
- Line 1421: the definitions of $G_ 0(x)$ and $G_ {z,\sigma_ {\min}}(x)$ have typos.
- Line 1476: "Let's *consider* a ..."

I will be happy to raise the score if the author(s) could address my concern.

**References**

- Bakry et al. Analysis and Geometry of Markov Diffusion Operators. Springer 2014.
- Bertazzi et al. Piecewise deterministic generative models. Arxiv 2407.19448, 2024.
- Bose et al. SE(3)-Stochastic Flow Matching for Protein Backbone Generation. ArXiv 2310.02391, 2023.
- Campbell et al. Trans-Dimensional Generative Modeling via Jump Diffusion Models. NeurIPS 2023.
- Campbell et al. Generative Flows on Discrete State-Spaces: Enabling Multimodal Flows with Applications to Protein Co-Design. ICML 2024.
- Del Moral & Penev. Stochastic Processes: From Applications to Theory. Chapman & Hall 2014.
- Gat et al. Discrete Flow Matching. NeurIPS 2024.
- Huguet et al. Sequence-Augmented SE (3)-Flow Matching For Conditional Protein Backbone Generation. ArXiv 2405.20313, 2024.
- Lou et al. Scaling Riemannian Diffusion Models. NeurIPS 2023.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
Generator matching is introduced as an ambitious unification of multiple generative modeling methods, both in continuous and discrete spaces. This unified design space encompasses jump processes and in general any Markov process. Experiments on protein modeling and generative image modeling.

### Strengths
1. This paper has the ambitious goal of presenting a unifying framework for many (currently popular) generative modeling paradigms. Even unifying continuous and discrete models, and jump processes. This can be very relevant for the community, and the theory seems adequate and well supported.

2. Experiments are performed on diverse applications: proteins and images

### Weaknesses
1. It is unclear to me, and difficult to gauge, in how far the GM framework has benefits over *simple, naive* combinations of different modeling paradigms. I.e. how will the GM framework help future researchers in practice to build better models, other than only providing a theoretical unificiation? The paper does not sufficiently demonstrate that the proposed framework leads to practical advantages beyond what could be achieved by combining existing models in an ad-hoc manner. The experimental results, while diverse, do not clearly show a significant performance boost or novel capabilities that are directly attributable to the GM framework itself, rather than the specific models used within it.

2. It is not clear what the limitations of the GM framework are. The paper mentions that the operators need to be 'simple', but does not define this clearly. The use of linear operators, while mathematically convenient, may restrict the complexity of the generative processes that can be modeled. It is unclear if this linearity imposes a practical limitation on the framework's ability to capture highly non-linear data distributions. The paper should provide a more thorough discussion of the trade-offs between mathematical tractability and modeling power.

3. Figure 2 lacks clarity and requires improvement. The abbreviation 'ME' in the legend is not defined and the figure's text is too small, making it difficult to read. The naming in the legends does not match the vertical naming of the rows, which adds to the confusion. The figure should be revised to ensure that it is easily understandable and that the results it presents are clearly communicated.



### Questions
1. What are the limitations of GM? Is the linearity of the operators a limiting factor in the modeling capacity?
2. Line 128. What exactly is meant with *"simple"*. If I understand correctly, it needs to be linear, why not use that word?
3. Figure 2. What is *ME* in the legend? This figure could benefit some extra attention. Larger text size, match the naming in the legends with the vertical namings of the rows.

## Minor remarks/typo's:

- The use of $dx$ is somewhat confusing to me. I guess it is not the product of $d$ and $x$, is it supposed to signify $\mathrm{d}x$?
- On line 124: (1) and (2) hyperlink to seemingly random equations in the appendix. The same on line 401.
- Line 429: is *the* probability kernel
- Line 447: the informal use of *just increase number of channels* can be distracting to readers. In general the Experiments section could benefit from some additional refining.
- Equation numbering is inconsistent. Absent for large parts of the appendix. Also in the main text numbering is sometimes absent (e.g. lines 223, 251)

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a generalized framework called *generator matching* to train diffusion-based models for continuous-time Markov processes, encompassing various well-known models as special cases. In particular, the proposed framework provides a consistent theory for training generative models of continuous-time Markov processes within the class of Feller processes. Feller processes include various types of continuous-time Markov processes, such as Ito diffusions, continuous-time Markov chains (CTMCs), jump processes, and continuous-time normalizing flows.

Specifically, this paper first introduces some general properties of the continuous-time Markov processes to motivate the proposed method. Many continuous-time Markov processes of interest exhibit two main characteristics. First, their transition probability follows the Markov property. Second, sample paths created by Markov transitions exhibit some form of continuity (right-continuous or left-continuous). These two characteristics allow the averaged behavior of the transition probability at an infinitesimal time scale to be expressed by a gradient operator on the state space $S$. This operator is known as the (infinitesimal) generator of a Markov process and is uniquely defined for each transition probability. Notably, this generator is not simply a gradient evaluated at a point in the state space $S$ but an operator that yields the gradient when applied to a function $f$ on the process. It is essential to remember that a Markov process is uniquely determined by its transition probability (and initial distribution). Therefore, this averaged gradient operator, or generator, along with the initial distribution, uniquely determines the Markov process. The paper proposes a training method for a model generator based on sample paths of a reference Markov process, in particular, ones to bridge or connect two distributions, as seen in bridge matching or flow matching.

While similar works on generative modeling for Feller processes exist [1], this paper proposes a novel parameterization that directly models the generator of Markov processes. This enables direct training of the generator, in contrast to other parameterizations such as score-based training in Euclidean spaces or probability ratio training in discrete state spaces. Recall that the (infinitesimal) generator of a continuous-time Markov process is a type of averaged gradient operator on the stochastic process. When this gradient operator is applied to a function $f$ on the state space, it typically comprises a combination of the gradient, Hessian, divergence, or difference of $f$ and the transition probability-related parameters. The specific form of the generator depends on the chosen Markov process. However, the paper emphasizes that the generator for most Markov processes of interest can be expressed as $\langle \mathcal{K}f, F \rangle$, where $\mathcal{K}$ is a linear operator independent of the Markov process’s transition probability, making it parameter-independent. Thus, $F_t$ uniquely determines the generator, and the paper proposes to train $F_t$ directly—a technique called *generator matching*. The paper specifically employs a Bregman divergence-based objective for this approach.

This theory applies to all Feller processes, including continuous-time Markov processes like Ito diffusions, continuous-time Markov chains, jump processes, and continuous-time normalizing flows. Moreover, since generators are linear operators, defining a Markov process with a transition probability that combines various types of transition probabilities becomes straightforward: the generator can simply be represented as the sum of the original generators. This approach enables an intuitive understanding of combined Markov processes by summing their respective generators.

Unfortunately, generator matching faces the same challenges as (explicit) score matching, particularly since the exact $F_t$ of the reference processes is generally unknown. To address this, the authors show that $F_t$ at time $t$ can be reformulated as the expected value of an initial value-conditioned $F_t$ (with the expectation taken with respect to the posterior distribution of $X_0$ given $X_t$). Using this insight, the paper proposes *conditional generator matching*, which serves a similar function to denoising score matching in Euclidean diffusion-based models.

Finally, the paper demonstrates the effectiveness of the proposed method through various experiments.

[1] Joe Benton, Yuyang Shi, Valentin De Bortoli, George Deligiannidis, and Arnaud Doucet. From denoising diffusions to denoising markov models. Journal of the Royal Statistical Society Series B: Statistical Methodology, 86(2):286–301, 2024.

----
I have updated the overall rating from 6 to 8 and the soundness & presentation from 3 to 4 after the authors' rebuttal.

### Strengths
In my understanding, the paper's contributions are clear, and I consider that the results are essential for several reasons.

First and foremost, the authors introduce a unified framework that combines a unified theory to explain how distinct Markov processes, defined across various state spaces, can be represented within a consistent language. While this framework may be not be novel itself, the paper exploits this framework to propose a novel method for training these processes in the context of generative modeling. Specifically, the paper’s new generator-based parameterization leverages this unified theory, offering a streamlined and theoretically grounded approach to model various Markov processes in a consistent fashion.

Second, beyond recovering existing diffusion-based models within the unified framework, the paper uses this framework to establish innovative classes of generative models. For example, one of new class straightforwardly combines different types of Markov processes, paving the way for flexible yet rigorous generative modeling approaches.

I believe this paper provides invaluable insights for comprehensively understanding various diffusion-based models (including flow matching, bridge matching, and others). It offers a cohesive view that can unify these models within a broader framework. This paper could very well become a must-read for those interested in this topic, given the clarity it brings to understanding and advancing diffusion-based generative models.

### Weaknesses
I find the paper original and significant overall. However, the presentation should be improved. In particular, there exists some significant notational issue over the paper.

First, the author suggests that $ p_t $ can be interpreted both as a measure function (a set function on a $ \sigma $-algebra of the state space $ S $) and as a function on $ S $. This dual interpretation creates confusion in the derivations and leads to inconsistency in the notation. Additionally, it introduces an unnecessary operator $ \odot $, which is intended as an inner product. For the proofs in this submission to be correct, several notational revisions are necessary. Specifically, $ p_t $ should be defined as a density function, represented as a Radon-Nikodym (RN) derivative with respect to a reference measure $ \mu $ in a general setting.

Here, $ \mu $ denotes a reference measure on the state space $ S $, such as the Lebesgue measure for $ \mathbb{R}^n $ or the counting measure for a countable set. Consequently, $ p_t(x) = \frac{d\mathbb{P}_t}{d\mu}(x) $ represents the RN-derivative with respect to $ \mu $, often referred to as a probability density function in the Euclidean setting or as a probability mass function in a discrete (particularly countable) state space.

As a result, all equations involving $ \odot $ can be rewritten in terms of an inner product. For example, Equation (2) can be expressed as
$$
\mathbb{E}[f(X_t)] = \int f(x) p_t(x) d\mu(x) = \langle p_t, f \rangle.
$$
Another example is Equation (6), which becomes
$$
\partial_t \langle p_t, f \rangle = \langle p_t, \mathcal{L}_t f \rangle.
$$

Second, the notational issue discussed above introduces further complications, which undermine the motivation for using the $ F $-parameterization rather than directly parameterizing the generator $ \mathcal{L} $. In my understanding, for the continuous-time Markov processes mentioned, the generator $ \mathcal{L}f $ can be represented as $ \langle \mathcal{K}f, F \rangle $, where $ \mathcal{K} $ is a linear operator independent of the transition probability of the Markov process (thus parameter-independent). This formulation, in my opinion, effectively motivates the $ F $-parameterization. For example, in the case of a continuous-time Markov chain (CTMC),
$$
\sum_{y} ( f(y) - f(x) ) Q(y; x) = \Delta f(x)^\top Q(x),
$$
where $ \Delta f(x) = (f(x_1) - f(x), f(x_2) - f(x), \dots) $ and $ Q(x) = (Q(x_1; x), Q(x_2; x), \dots) $. With this notation, transitioning from matching the generator to matching the $ F $-parameterization becomes straightforward. Moreover, it allows the use of well-known objective functions, such as mean-squared error minimization, alongside the Bregman divergence-based loss. This expands the flexibility and applicability of the model training approach.

As previously mentioned, I consider this paper to be an excellent work that provides valuable insights into unifying various diffusion-based models (including flow matching, bridge matching, etc.). For those interested in this topic, I believe that it could very well become essential reading. However, due to the significance of the notational issues, there is a risk of widespread misunderstanding if these inconsistencies persist. While I believe that reviewers should respect the authors’ narrative, including their notations, I also believe that it is essential to avoid reinventing standard notations with new one, especially when these are well-established in standard textbooks. This is particularly important since once published, changing the notation would be extremely challenging. Therefore, I am inclined to assign a lower score at this stage. I am, however, open to raising the score if the paper is revised to address these issues.

Despite my willingness to increase the score following revisions, I must express a concern based on recent experience: I have frequently reviewed papers with similar notational issues where authors promised corrections but ultimately did not make the necessary changes. As a result, this time, I will not consider adjusting the score unless these notational issues are thoroughly addressed.

### Questions
N/A

### Soundness
4

### Presentation
4

### Contribution
4
