# Trivialized Momentum Facilitates Diffusion Generative Modeling on Lie Groups

- Decision: Accept
- Avg Score: 6.75
- Scores: 5, 8, 6, 8

## Abstract
The generative modeling of data on manifold is an important task, for which diffusion models in flat spaces typically need nontrivial adaptations. This article demonstrates how a technique called `trivialization' can transfer the effectiveness of diffusion models in Euclidean spaces to Lie groups. In particular, an auxiliary momentum variable was algorithmically introduced to help transport the position variable between data distribution and a fixed, easy-to-sample distribution. Normally, this would incur further difficulty for manifold data because momentum lives in a space that changes with the position. However, our trivialization technique creates to a new momentum variable that stays in a simple \textbf{fixed vector space}. This design, together with a manifold preserving integrator, simplifies implementation and avoids inaccuracies created by approximations such as projections to tangent space and manifold, which were typically used in prior work, hence facilitating generation with high-fidelity and efficiency. The resulting method achieves state-of-the-art performance on protein and RNA torsion angle generation and sophisticated torus datasets. We also, arguably for the first time, tackle the generation of data on high-dimensional Special Orthogonal and Unitary groups, the latter essential for quantum problems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors present a method for diffusion on Lie groups. The method is based on the recently published idea of trivialized momentum, that is, diffusion (i.e. noising) is performed on the Lie algebra of the group, and not on the Lie group itself. The advantage of this approach is that the Lie algebra is a vector space isomorphic to $\mathbb{R}^n$, and therefore it simplifies the problem since all the curvature terms pretty much drop out. This diffusion is brought back into the actual Lie Group G by using the map connecting two tangent spaces of G at different point, which is the tangent of the left multiplication map. 

The authors show that this noising dynamics has an inverse dynamics as well, in very familiar fashion as the usual diffusion dynamics, in which a score function appear, which it is possible to learn with neural networks. 

The authors further argue that it is possible to have a dynamics that is exaclty on the curved manifold at all steps without the need of a projection (I do not agree with this statement, please refer below in the "Questions" section). This is done by separating each step into two contributions, i.e., the update of the Lie algebra element $d\xi$ and the update of the lie group element $dg = g \xi$. Note that also this procedure is already known in the literature. 

They provide an explicit formula for the Abelian case, while they point out that for the general case, it is necessary to learn the score with implicit score matching, which unfortunately involves the divergence term.

### Strengths
The topic is very relevant, as diffusion-based models achieved quite successful results in many applications, but very little has been explored in terms how inductive bias can be incorporate into them, and diffusion on manifold is surely an important field. 

The notation is fairly consistent and the math is, to the extend that I checked, correct (I did not carefully checked the proofs in the appendix).

### Weaknesses
My two main concerns regard the originality of the work and its practical relevance:

- **Originality**: As far as I can see, the idea and the theory behind trivialized momentum has been developed in previous works, as well as the  splitting discretization technique to exactly integrate the SDEs. The authors prove a theorem for the inverse SDE of the system, but given that the non-trivial equation (about the variation of the Lie algebra) is essentially in flat space, it reduces pretty much to the flat-space formula.
- **Practical Relevance**: The main drawback is in the non-Abelian case, which is the most interesting since the Abelian case is essentially SO(2) (or copies of it). For non-Abelian groups, there's no conditional transition probability available, requiring implicit score matching. This involves computing the divergence with respect to the data space (more precisely, the Lie algebra space, but as dim data = dim $G$ = dim $\mathfrak{g}$ its computationally as expensive). This limitation significantly reduces the method's practicality and makes it unlikely to be widely adopted. 

I think the paper would be significantly more relevant if it provided an analogue of Theorem 2 for non-Abelian groups.

### Questions
- 280-283: The sentence “Since the Brownian motion…” does not seem to be grammatically correct.
- 292: “Unfortunately, note [that] even though”. Missing “that”.
- 382: $A_g^B$ used twice, probably copy-paste error.
- The authors make several times the claim that the formalism on which they based their work does not required projection on the manifold. I think this statement, as is, is false. Group equation is $dg = g_0 \xi$, which is an equation on the tangent space of the group. Its solution is (neglecting the variation of $\xi$), $g=\exp(g_0 \xi)$. But the exponential map is precisely the projection function on Lie groups, $\exp: TG —> G$. So to stay on the manifold the authors are performing a projection exactly as all other methods too.

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
3

### Summary
The paper introduces a new framework for constructing diffusion models on manifold-structured data in the particular case where the manifold is a Lie group. This is achieved through the use of a forward noising process defined by kinetic Langevin dynamics on the Lie group and its tangent space jointly. The authors demonstrate that the group structure of this class of manifolds allows for the corresponding reverse process to rely solely on a Euclidean score function, as well as allowing for the manifold-preserving and projection-free sampling of the forward and reverse processes, circumventing the complexities and multiple approximations required in previous work. The authors then apply this to various tasks presenting convincing results.

### Strengths
The authors present a novel and clever way to address the computational limitations of previous approaches to manifold-valued diffusion models, by exploiting the group structure of Lie groups through the use of Kinetic Langevin dynamics. This allows for learning a score function in a fixed Euclidean space which reduces the numerical errors associated with the approximations arising from scores defined directly on curved manifolds. This approach is well-fleshed out by the authors who provide a detailed methodology for the application of this for generative modelling, for example, by providing an integration scheme which is manifold-preserving and projection-free, and training objectives for both Abelian Lie groups and non-Abelian Lie groups. This framework is further validated by experiments demonstrating the novel scaling of manifold-valued diffusion models to SO(N), N>3.

### Weaknesses
The framework can only provide simulation-free training for the manifold SO(2) and its product space which is less flexible than Riemannian Flow Matching. However, this setting is still important for applications.

### Questions
Some possible typos in the text:
- line 155, missing brackets for g_t, \xi_t?
- line 325, should be "\sigma_t evaluated at"?
- line 1022, the A_\xi^\F should be A_\xi^\B?

### Soundness
4

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
3

### Summary
This paper provides a new framework for performing generative modelling on Lie groups which doesn’t require any geometry-specific projections or approximations, utilizing the notion of “trivialized momentum.” The authors provide the denoising score matching loss which can be used for SO(2)^n, as the conditional transition probabilities are tractable and an implicit score matching loss for other connected compact Lie groups. They also provide an integration scheme for the forward and backward dynamics.

### Strengths
- The paper is overall well-written and easy to follow. The problem the authors tackle is interesting and important.
- The proposed technique is interesting and avoids some of the problems mentioned with other existing approaches, such as projections, requiring specific architectures, etc.
- The mathematical details are explained cohesively and clearly. 
- The results on the torus datasets, as well as the toy tasks for the SO(n) and U(n) groups seem promising.

### Weaknesses
 - The main weakness of the paper is the lack of rigorous experiments to demonstrate the effectiveness of the model in comparison with existing approaches. 
- First, the authors didn’t clarify how the experimental setup and training procedures vary across the different benchmarks. The experimental results would be more convincing if details on the setup are clearly provided. 
- Secondly, it wasn’t clear me to what approximations one has to make when doing RFM in the torus settings, especially since going from the Lie algebra to the Lie group element is essentially trivial in that case. Could the authors clarify what approximations are required in RFM for SO(2)^n experiments?
- Lastly, although the results on the SO(n) and U(n) experiments are interesting and show promise, more rigorous experiments are required to show the scalability of the implicit score-matching loss (as it generally doesn’t perform as well). I think the paper could be strengthened if the authors clearly show better performance compared to RFM and RDM on the higher-dimensional SO(n) and U(n) tasks.
- It would be very helpful if the authors provided a more detailed discussion on the approximations made in RFM and RDM which the authors attribute to the worse performance of these models in the torus settings. 
- The paper also provides experiments for the SO(3) setting, however it doesn’t provide a comparison with SE(3) generative models that rely on IGSO(3) distribution. As mentioned in the paper, the special structure of SO(3) can be leveraged, which makes applying TDM in that setting less motivated.

### Questions
See above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
- The paper is concerned with tackling the challenge of incorporating diffusion models into a manifold setting
- Their key takeaway is that on Lie groups for both training and sampling diffusion can take place in the Lie algebra
- They show that their method performs well on various Lie groups of various dimensions that arise in different applications

### Strengths
- The authors provide a very nice motivation for the problem and highlight the key challenges that current manifold-valued models are dealing with.
- The mathematics is displayed in a very clear way and adequately addresses the challenge discussed in the motivation, i.e., how to set up manifold diffusion models on the Lie algebra. They also address different types of Lie groups well. In particular, it is nice that they highlight the special case of Abelian Lie groups learning, where training becomes easier than on non-Abelian ones
- The numerical experiments nicely display that the method performs well on high-dimensional Lie groups (which is where one would expect issues due to numerical inaccuracies from projections and manifold mappings), but also showcase that for low-dimensional Lie groups performance is superior to baselines.

### Weaknesses
 - I feel that for the introduction, there are some mistakes in terms of English grammar 
- Some parts could have been explained in more detail, but given the page limit restrictions it is natural that the authors aimed to be as concise as possible
- p.2 l.59: the authors bring up numerical integration errors. It would be helpful to the reader to specify this a bit more. I assume this is because mappings like the exponential mapping can be expensive. Is this only the case in high dimensions or even on low-dimensional Lie groups? 
    - a bit more nuance would improve the paper a lot as it would make the actual challenge even clearer, which would highlight your contributions even more
- p.2 l.78: the authors write ``while still encapsulating the curved geometry without any approximation.’’ There is an approximation error if there is curvature right? 
    - It would be great if the authors are a bit more nuanced here as well as it should be clear that this method might introduce new errors.
- Section 3: In the Lie algebra, the learned distribution wraps around. So ideally, the score should be periodic or should become zero if this cannot be enforced. Is there some mechanism that enforces this? 
    - If not, I would recommend adding this explicitly to let the reader know that there is possibility for error here.
- p.6 l.337: In the implicit score matching paragraph, it is not very clear to me how one would go about sampling here (does one have to do a forward simulation for this?). Would the authors clarify this?
- Section 5: 
    - It feels natural to also mention something about flow matching in the outlook. Do the authors have any ideas on this they would like to disclose in the conclusions?

Additional feedback
- Section 1: please do a grammar check. A couple of small things that I noticed:
    - p.1 l.43: change ''manifold’’ in … Neural ODE to manifold with maximum … to ''manifolds’’. This reads better
    - p.1 l.44: change ''algorithm’’ in Rozen; Ben-Hamu develop simulation free algorithm but… to ''algorithms for the same reason as above
    - p.1 l.94: add ''a'' right before ''trivialized’’ in …through learning trivialized score function…
- Section 2: It looks a bit odd that section 2 is just one line. Consider integrating this line in section 3 instead.
- Section 3:
    - p.3 l.133: replace ''sequal'' with ''following''. It sounds like this will be discussed in your next paper rather than further down in this one.
    - p.3 l.147: the authors consider the tangent map. I believe that this is the differential? For the reader who is used to other nomenclature and/or notation, I would suggest to also mention that this is often referred to as the differential.
    - In equation 8, shouldn’t there be a superscript i for the xi in the dt term?
    - p.7 l.373: the authors write ``do not admit a closed form.’’ A closed form what?

### Questions
Questions for clarification 
- p.2 l.59: the authors bring up numerical integration errors. It would be helpful to the reader to specify this a bit more. I assume this is because mappings like the exponential mapping can be expensive. Is this only the case in high dimensions or even on low-dimensional Lie groups?
    - a bit more nuance would improve the paper a lot as it would make the actual challenge even clearer, which would highlight your contributions even more
- p.2 l.78: the authors write ``while still encapsulating the curved geometry without any approximation.’’ There is an approximation error if there is curvature right? 
    - It would be great if the authors are a bit more nuanced here as well as it should be clear that this method might introduce new errors.
- Section 3: In the Lie algebra, the learned distribution wraps around. So ideally, the score should be periodic or should become zero if this cannot be enforced. Is there some mechanism that enforces this? 
    - If not, I would recommend adding this explicitly to let the reader know that there is possibility for error here.
- p.6 l.337: In the implicit score matching paragraph, it is not very clear to me how one would go about sampling here (does one have to do a forward simulation for this?). Would the authors clarify this?
- Section 5: 
    - It feels natural to also mention something about flow matching in the outlook. Do the authors have any ideas on this they would like to disclose in the conclusions?

Additional feedback
- Section 1: please do a grammar check. A couple of small things that I noticed:
    - p.1 l.43: change ''manifold’’ in … Neural ODE to manifold with maximum … to ''manifolds’’. This reads better
    - p.1 l.44: change ''algorithm’’ in Rozen; Ben-Hamu develop simulation free algorithm but… to ''algorithms for the same reason as above
    - p.1 l.94: add ''a'' right before ''trivialized’’ in …through learning trivialized score function…
- Section 2: It looks a bit odd that section 2 is just one line. Consider integrating this line in section 3 instead.
- Section 3:
    - p.3 l.133: replace ''sequal'' with ''following''. It sounds like this will be discussed in your next paper rather than further down in this one.
    - p.3 l.147: the authors consider the tangent map. I believe that this is the differential? For the reader who is used to other nomenclature and/or notation, I would suggest to also mention that this is often referred to as the differential.
    - In equation 8, shouldn’t there be a superscript i for the xi in the dt term?
    - p.7 l.373: the authors write ``do not admit a closed form.’’ A closed form what?

### Soundness
4

### Presentation
3

### Contribution
4
