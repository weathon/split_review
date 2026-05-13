# Lie Group-Induced Dynamics in Score-Based Generative Modeling

- Decision: Reject
- Scores: 8, 3, 8, 3, 5

## Abstract
We extend score-based generative modeling by incorporating Lie group actions on the data manifold into the denoising diffusion process. Our approach yields a Langevin dynamics whose infinitesimal transformations decompose as a direct sum of Lie algebra representations, enabling generative processes that align with the underlying symmetry properties of the data. Unlike equivariant models, which restrict the space of learnable functions by quotienting out group orbits, our method incorporates both global and local symmetries and can model any target distribution. Standard score-matching, which minimizes the Fisher divergence, emerges as a special case of our framework when the Lie group is the translation group in Euclidean space. We prove that our generalized generative processes arise as solutions to a new class of reverse-time stochastic differential equations (SDEs), introduced here for the first time. We validate our approach through experiments on diverse data types, demonstrating its effectiveness in real-world applications such as SO(3)-guided molecular conformer generation and modeling ligand-specific global SE(3) transformations for molecular docking. We show that an appropriate choice of Lie group enhances learning efficiency by reducing the effective dimensionality of the trajectory space and enables the modeling of transitions between complex data distributions, lifting the requirement of a Gaussian prior. Additionally, we demonstrate the universality of our approach by deriving how it extends to flow matching techniques.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the authors present a general framework for construction diffusion processes on spaces $X$ that are acted on by Lie groups $G$.
Specifically, they show that the Lie algebra infinitesimal actions on that space induce a fundamental vector field $\Pi$ and its associated differential operator $\mathcal{L} = \Pi \cdot \nabla$.
They then define a noising processes on $X$ (Eq 5) via $\Pi$ whose solution can be easily computed, and whose time-reversal is given in Eq 6 and also involves $\Pi$ as well as the generalised score $\mathcal{L} \log p_t$.
They show that generalised score can be learned by minimising the generalised Fisher divergence (Eq 4) akin to standard score matching.
Setting $X=\mathbb{R}^n$ and $G=\mathrm{T}(n)$, one recovers the standard score matching framework.

### Strengths
The manuscript is generally well written and organised. I liked that $(X=\mathbb{R}^2, G=\mathrm{SO}(2))$ was used through the manuscript as a running example.

The framework presented is fairly general and elegant.

Although I did not check the proof, the assumptions and results presented seem sound.

The framework is applied to several tasks, including in molecular conformation modelling and docking.

### Weaknesses
Not sure whether this is a 'weakness' per se, but this framework feels pretty similar to building a generative model on the group $G$ (_flow coordinates_) itself using the reparameterisation $x(\tau)$ via the flow map (e.g. Cartesian to polar coordinates).
Why not directly construct a generative model on this space by first mapping sample into the Lie algebra? Is the difference that such a map would need to be _global_ whist the flow map here is _local_ (i.e. depends on an $x_0$)?

Could still construct such a generative model without relying on a global diffeomorphism (e.g. Corso et al. (2022), De Bortoli et al. (2022)). These formalisms actually feel very similar to the one presented here.
For the Rotated MNIST experimentation of Section 5.2 it feels pretty natural, and similarly for the docking task of Section 5.4.
What is the advantage in not doing so?

- Theorem 3.1: The $\Pi$ term is akin to covariance operator term right? (as in e.g. 'Score-based generative modeling through stochastic differential equations' Song et al 2021).
- 273: 'specific order is irrelevant since the Lie algebra generators commute.' -> how restrictive is this? Is this equivalent to assuming commutativity of the Lie group? E.g. does $\mathrm{SO}(3)$ satisfy this?
- 281: Does this mean that one needs to go back and forth the flow coordinates $\tau$ and the original $x$ at sampling time? Or only at the last iteration?
- 291: How efficiently can one compute the flow map? I assume that the action itself is cheaper than computing the exponential map in general?
- Section 5.3: Is the difference in energy differences significative here? What is the reasoning behind this group being beneficial? I would suggest evaluating the samples via PoseCheck/PoseBuster, which would be quite more indicative and robust than just looking at the Rdkit energy.

### Questions
- Theorem 3.1: The $\Pi$ term is akin to covariance operator term right? (as in e.g. 'Score-based generative modeling through stochastic differential equations' Song et al 2021).
- 273: 'specific order is irrelevant since the Lie algebra generators commute.' -> how restrictive is this? Is this equivalent to assuming commutativity of the Lie group? E.g. does $\mathrm{SO}(3)$ satisfy this?
- 281: Does this mean that one needs to go back and forth the flow coordinates $\tau$ and the original $x$ at sampling time? Or only at the last iteration?
- 291: How efficiently can one compute the flow map? I assume that the action itself is cheaper than computing the exponential map in general?
- Section 5.3: Is the difference in energy differences significative here? What is the reasoning behind this group being beneficial? I would suggest evaluating the samples via PoseCheck/PoseBuster, which would be quite more indicative and robust than just looking at the Rdkit energy.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a new class of diffusion generative models, where the forward process is defined through infinitetismal action of Lie algebra, to better model the underlying symmetry of data distribution. This also generalize the standard denoising score matching. Experiments are performed on rotated MNIST images, molecular conformer generation and molecular docking to demonstrate the effectiveness of the approach.

### Strengths
* The authors use nice and informative figures (Fig 1 - Fig 3) to demonstrate the complicated geometric object related to Lie groups and have provided some level of intuition with them.
* This paper has technically sound mathematical formulation and proof. The introduction of new SDEs based on Lie algbera is novel.
* This paper provides numerical experiments on molecular conformer generation and molecular docking, which are important tasks related to structural biology.

### Weaknesses
 * The paper does not provide a clear motivation on why and in what cases we should use this new class of SDE instead of standard Euclidean Diffusion models. Is it when the data distribution is invariant under some Lie group action? Is it when the data distribution is defined on Lie groups? This part is not clearly explained, which further makes it confusing under what scenarios using Lie-induced generalized score matching are more beneficial. The paper misses a detailed discussion on this part, which I believe is very important.

* The paper does not discuss how restrictive the technical assumptions are. In section 2.2, three conditions are presented as sufficient conditions to use generalized score matching. However, the general feasibility of these conditions is not well discussed. Furthermore, while the general setting assumes the data state space $X$ to be general manifolds, all the examples and calculations in the paper seem to be done in cases where $X$ is essentially Euclidean. This makes me wonder about the applicability of this approach to more general settings.

* The paper does not discuss the tractability of different score matching objectives in the general setting. In lines 293-304, seemingly only settings of Euclidean data are presented, where the generalized conditional score has an analytic closed-form expression. It's unclear how things are if the data space is not Euclidean. 

* The numerical experiments, while are important real-world applications, are not performed enough and comparison with benchmarks in the literature are missing. Molecular conformer generation and molecular docking respectively have a rich literature and many of them are based on generative modeling methods. Without comparison, it's hard to see the utility and advantage of the proposed approach.

* Paper writing clarity can be improved. Multiple typos and citations in inappropriate form could decrease paper readability. Missing some figure captions (e.g., Figure 5)

### Questions
* Can you elaborate more on in what scenarios, the proposed Lie algbera based SDE and Lie-induced generalized score matching are more beneficial than other approaches, e.g. vanilla Euclidean diffusion (with or without equivariance/invariance enforced), manifold diffusion models, etc?
* Can you provide more examples where the proposed framework is feasbile and the data space $X$ is not Euclidean?
* How to choose the drift function $f(x)$ in eq. (6), (7), and how does the choice relate to the associated Lie group $G$ in the problem set-up?
* Can you elaborate more on Line 400-404, specifically on how RSGM is a special case of the proposed framework?
* What's the connection between this work and diffusion models on general Lie groups, for example [1]?
* Given a data distribution, how do we know what Lie group $G$ to choose for using the proposed approach? And if the data distribution is invariant under the group action in $G$, does the proposed approach also guarantee to preserve such invariance?
* Would the proposed approach be applicable if the associated Lie group is high dimensional, say $G = SO(n)$ for $n > 3$?

* In the QM9 molecular conformer experiment, how would the proposed approach compare in terms of numerical performance with other methods, e.g. [2-4]?
* In the molecular docking experiment, how would the proposed approach compare in terms of numerical performance with other methods, e.g. [5]?

Reference:

[1] Zhu, Yuchen, et al. "Trivialized Momentum Facilitates Diffusion Generative Modeling on Lie Groups." arXiv preprint arXiv:2405.16381 (2024).

[2] Wang, Yuyang, et al. "Swallowing the Bitter Pill: Simplified Scalable Conformer Generation." Forty-first International Conference on Machine Learning.

[3] Xu, Minkai, et al. "Geodiff: A geometric diffusion model for molecular conformation generation." arXiv preprint arXiv:2203.02923 (2022).

[4] Jing, Bowen, et al. "Torsional diffusion for molecular conformer generation." Advances in Neural Information Processing Systems 35 (2022): 24240-24253

[5] Corso, Gabriele, et al. "Diffdock: Diffusion steps, twists, and turns for molecular docking." arXiv preprint arXiv:2210.01776 (2022).

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces score-based generative models whose solutions abide to some symmetries, known as Lie groups. To achieve this, the authors show that diffusions in a space $ X $, which follow these symmetries, can be expressed using a directional derivative aligned with the symmetry. In particular, they shows that the stochastic differential equations of such diffusions includes a directional derivative of the log-density rather than the standard log-density gradient. Consequently, they propose a method for training the directional scores.

A symmetry group is a set of (closed) transformations on a space $ X $ that maintains certain symmetries, such as translation, rotation, and reflection. Specifically, a Lie group is a symmetry group with continuous symmetries. Each element (transformation/mapping) in a Lie group is known as a (Lie) group action. Since Lie group actions are continuous, they are differentiable with respect to the symmetries, such as rotations or translations. The derivative of a Lie group action is called a Lie algebra action, which is commonly viewed as a linearized form of the group action (analogous to any other derivative).

The paper highlights that the directional derivative at $ x \in X $, along group actions, can be represented by what is called the fundamental vector field. The fundamental vector field at $ x \in X $ is the linear mapping at $ x $, representing the Lie algebra actions (the derivatives of the symmetries) with respect to a basis of $ X $, and it is expressed through exponential mappings of Lie algebra actions. As a result, the directional derivative on $ X $ along the symmetries is defined by the inner product of the fundamental vector field and the ordinary derivative.

With this derivative representation of using fundamental vector fields, the authors show that forward and reverse diffusions under Lie groups can be represented in terms of the directional derivative of log-density. Based on this, the paper proposes generalized score matching (including a denoising variant) that learns the directional derivative of log-density in a manner similar to standard (denoising) score matching. 

The authors argue that the proposed method offers an advantage by allowing the use of more general network architectures, without the need for designing network structures specifically invariant or equivariant to Lie groups. 

Finally, the paper demonstrates the effectiveness of this approach through various experiments.

----
I have updated the overall rating from 6 to 8 and the soundness from 3 to 4 after the authors' rebuttal.

### Strengths
While the paper may not be entirely novel, it is original, beneficial, and contributes positively to the community. It bears some resemblance to diffusion or flow matching on Riemannian manifolds because a Lie group is a type of Riemannian manifold. Therefore, one might suggest using the previously proposed Riemannian diffusion models. However, the paper does an excellent job of explaining how the new differential equation contains directional derivatives along Lie groups and why the directional derivatives to the group action have a Jacobian-like term, i.e., the fundamental vector field. Such discussions can be considered original because it differs from simply showing a special case as an example from a general method.

The paper is written in a way that is easy for others to understand. It is beneficial, interesting, and well-explained.

### Weaknesses
I find the paper original and significant overall. However, the presentation should be improved.

In particular, the explanations of essential concepts in the preliminary section are too similar to the definitions and phrases found on Wikipedia. For example, the sections on Lie groups and Lie algebras closely mirror Wikipedia's wording. Wikipedia, while useful for quick references, is not always reliable or sufficiently detailed for scholarly work. It may lack the rigorous explanations required to fully grasp complex mathematical ideas. By closely copying Wikipedia's definitions—including any inaccuracies or omissions—the paper may fail to convey the nuances of the concepts involved.

The presence of typos in the equations is another area for improvement. Accuracy in mathematical expressions is crucial, as even minor errors can lead to misunderstandings. Careful proofreading and attention to detail in the equations would improve the clarity and overall quality of the paper.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
A traditional generative model is a (stochastic) flow of a vector field in Euclidean space. This paper expands it to a new case: it considers a vector field on the manifold and the vector field comes from a Lie group acting on the manifold. The paper is well-written with well-illustrated numerical experiments provided. However, there are some important weaknesses, please see the weaknesses section. I will increase my score if the weakness is explained.

### Strengths
The interesting idea of using the infinitesimal generator of a group action to generate a vector field on the manifold is new to me. The author claims that this approach enables us to design diffusion models on manifolds. The author claims the algorithm handles the non-Abelian Lie groups as long as conditions in Sec. 2.2 is satisfied. (see more discussion about Sec 2.2 in weakness)

The numerical experiments are interesting since it seems the manifold structure is well-learned in some synthetic examples. Applications on real datasets are also provided (MNIST and QM9).

### Weaknesses
My main concern is: Can X be curved? Here are the details for this question:

First, notice that in all examples, X is Euclidean, even in the example in line 223-226 and Sec A.3 arguing the conditions are not that strong. Could you please explicitly address whether your theoretical framework and algorithm can be applied to the cases where X is a curved manifold? If so, could you demonstrate this by applying your example to a curved X?

Secondly, in Eq. 8 in the algorithm, the order of multiplication of $O(\tau(t))$'s does not matter, which means they exchange. This means your algorithm highly depends on Condition 3.

Finally, assume condition 3 is given, then we can see $[L_A, L_B]f=0$ ->$L_{[A, B]}f=0$ -> $[A, B]=0$ -> the Lie bracket vanishes on X (by condition 2) -> X is flat. This seems to be short proof showing that condition 2+3 infers that X is flat. Is this true? If not, could you provide a counterexample or explain how the framework can accommodate curved spaces while satisfying the conditions in Sec 2.2?

### Questions
If the weakness I stated is incorrect, could you please give me an example that X is non-flat with all conditions in Sec 2.2 is satisfied?

If the weakness I stated is true, I have the following question: 

1. If the proposed method is indeed limited to Euclidean spaces, could you elaborate on the specific advantages it offers over traditional algorithms in these cases? Are there particular types of problems or data structures where your approach would be more efficient or effective?

2. Given that Condition 2 assumes a homogeneous space, how does this impact the expressiveness of your model compared to traditional Euclidean methods? Could you clarify if there are scenarios where your approach provides benefits even within these constraints?

### Soundness
3

### Presentation
4

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper the authors propose a new diffusion model framework to disentangle symmetries in the data. Assuming that there is a group action (where the group action is given by a Lie group) associated with the space of interest, they build a diffusion model which leverages the action of the group on the data space. This class of diffusion model is valid under certain assumptions on the relationship between the group action and the data space. For instance, one must assume that the group action is complete. In that case, the forward diffusion is linked with an (explicit) forward diffusion on the Lie group. In order to learn the quantity appearing in the backward diffusion, they propose a generalized score loss function, which in practice corresponds to a preconditioning of the score function. The proposed diffusion model is then tested on rotated image data, small molecule dataset (QM9) and molecular docking.

### Strengths
* I appreciate the rigor of the paper (with some caveats, see the Weaknesses section). Most of the quantities used in the paper are correctly introduced and I found the paper mostly easy to follow. 

* I think the proposed forward diffusion is interesting and worth studying. 

* I found the dynamics identified in Theorem 3.1 to be interesting. This is a nice link between some latent diffusion work and Riemannian geometry. However, I have several concerns regarding the novelty and applicability of such dynamics.

### Weaknesses
There are several limitations to this work:

* Lack of baseline experiments: while there is merit in this work I find the lack of baseline experiments to be concerning. There are many existing works on diffusion on Riemannian manifolds and I think a comparison with such works is necessary to assess the applicability of the method. To be more specific, in the case of rotated MNIST, why not compare the performance with a classical diffusion model on MNIST augmented with rotation? Similarly for QM9, why not compare with a diffusion model on QM9 where the QM9 dataset is augmented with the symmetries of the $G = (\mathrm{SO}(3) \times \mathbb{R}_+)^N$ and $G = T(3)^N$. Regarding Section 5.4 on CrossDocked2020, I know that the authors are space limited but I would suggest cutting some other parts of the paper to better explain CrossDocked2020. Such examples are important because, to my understanding, this is the only example in the paper dealing with a dataspace $X$ which is actually different from the classical Euclidean space. In these settings, it would be good to compare to other Riemannian based diffusion models such as [1, 2, 3]

* Motivation and link with existing literature: Looking at Theorem 3.1 I find that this result is extremely related to existing results on latent diffusion, see Section 4.1. of [4]. Broadly speaking, it seems to me that the main result of the paper is to translate a diffusion on a dataspace X to a Lie group G, the same way a bijective function would (or any minimal assumption needed to get a change of variable). The case of a bijective transformation is exactly the one treated in [4]. It would be great to acknowledge that fact if it is indeed the case. I understand that the settings and motivations are different but such works on latent diffusion cannot be ignored. Regarding works on Lie groups, there is a line of work devoted to the implementation of diffusion models on Lie groups, see for instance [5, 6] and references therein. In particular [5] focuses on diffusion models on SE(3) which seems to be related to the application presented in Section 5.4.
Mathematical correctness: I think the paper would highly benefit from a clarification between the general setting of a data space X and the special case of a Euclidean space. Indeed, while I understand that a few conditions are enforced to apply Theorem 3.1 (completeness, homogeneity, commutativity), the central mapping $\Pi$ should transfer a vector field defined on the Lie algebra of G into a vector field which is a section of the tangent bundle of X. In Theorem 3.1, we have that $\Pi$ is defined on Euclidean spaces. While there is a local identification between the tangent space of $X$ at any point and a Euclidean space, I am not clear where this is explicit in the paper. A similar remark holds for all the quantities introduced in Theorem 3.1. In general, I found the key quantity $\Pi$ to be poorly defined. The definition of this quantity given in line 173 “the collection of fundamental fields $\Pi$” is not enough to understand how it is defined truly. 

*Limitation: I don’t think the limitations of the work are discussed in enough depth. For instance, a central and essential point for the procedure described in the paper to work is the access to the mapping $\Pi$, its inverse and the ability to compute its determinant (according to the sampling paragraph, “Generating samples through the reverse SDE”). When is that the case? The authors have presented a few cases when that is possible but one of the crucial assumption is basically that G and X have the same dimensionality (in order to compute the inverse mapping). See Section 5.1, Section 5.2 and Section 5.3 to verify that the examples of the authors match this assumptions. There are many cases where the Lie group acting on the dataspace $X$ is not of the same dimension. In that case it seems very hard, if not impossible, to construct the diffusion process on $G$.

### Questions
* I might be missing something but I think Vect is TX in (1)

* What is the difference between x and bolded x (for example in (1)). Both seem to denote vector data. 

* Please unify the notation (x,y) and (x_1, x_2) in the fleshed out example on the rotation on the plane

* What action does A represent in (5)? It is not defined in this section. I am guessing that it is associated to L but for some reason the dependency of L with respect to A is not highlighted.

* Proposition 2.1. Can we have > dim X? This is suggested by the phrasing of Proposition 2.1. If such an example exists please provide it. 

* Is homogeneity really important? “ensure that the Langevin dynamics (5) will behave appropriately,” > what does appropriately mean here. For instance I could think of densities supported on only O_+

* I would move line 173 after Equation (1) to introduce the linear operator right away.

* A more general (open) question is the relevance of constrained generative models. In the light of the new Alphafold paper for instance [1], it seems that constrained generative models do not fare well compared to simpler models fed with a lot of data (and augmentations). I think running such comparisons and explaining the author's stance on this point would be very valuable for the paper and the community. 

[1] Abramson et al. – Accurate structure prediction of biomolecular interactions with AlphaFold 3

### Soundness
3

### Presentation
2

### Contribution
2
