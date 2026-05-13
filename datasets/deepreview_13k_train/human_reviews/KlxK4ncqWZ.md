# Shallow diffusion networks provably learn hidden low-dimensional structure

- Decision: Accept
- Scores: 6, 6, 5, 8

## Abstract
Diffusion-based generative models provide a powerful framework for learning to sample from a complex target distribution. 
The remarkable empirical success of these models applied to high-dimensional signals, including images and video, stands in stark contrast to classical results highlighting the curse of dimensionality for distribution recovery.
In this work, we take a step towards understanding this gap through a careful analysis of learning diffusion models over the Barron space of single layer neural networks.
In particular, we show that these shallow models provably adapt to simple forms of low dimensional structure, thereby avoiding the curse of dimensionality.
We combine our results with recent analyses of sampling with diffusion models to provide an end-to-end sample complexity bound for learning to sample from structured distributions. 
Importantly, our results do not require specialized architectures tailored to particular latent structures, and instead rely on the low-index structure of the Barron space to adapt to the underlying distribution.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates why diffusion models, specifically those utilizing shallow neural networks within Barron spaces, can effectively learn and sample from high-dimensional data distributions that possess hidden low-dimensional structures. By focusing on Barron spaces—the function space of single-layer neural networks—the authors demonstrate that diffusion models can adapt to simple forms of low-dimensional structure without the need for specialized architectures. They provide theoretical results showing that the sample complexity for learning these models depends polynomially on the intrinsic latent dimensionality rather than exponentially on the ambient dimension. The analysis includes end-to-end sample complexity bounds for learning to sample from structured distributions, highlighting how shallow diffusion networks can circumvent the classical curse of dimensionality by leveraging the low-index structure of Barron classes.

### Strengths
- The paper provides a rigorous theoretical framework that explains how diffusion models can overcome the curse of dimensionality by adapting to low-dimensional latent structures within high-dimensional data.
- By leveraging Barron spaces to model shallow neural networks, the authors bridge the gap between theoretical tractability and practical relevance, as these spaces capture essential features of networks used in practice.
- The work offers comprehensive sample complexity bounds that depend on the intrinsic latent dimensionality, providing valuable insights into the efficiency of learning diffusion models for structured distributions.
- The results do not rely on specialized network architectures tailored to specific latent structures, emphasizing the general applicability of shallow diffusion networks in learning hidden low-dimensional structures.

### Weaknesses
 - The analysis is restricted to shallow (single-layer) neural networks, which may not capture the complexities and representational power of deep neural networks commonly employed in state-of-the-art diffusion models. Specifically, the single-layer architecture may limit the model's ability to learn hierarchical features and complex dependencies present in real-world data. This is a significant limitation, as many successful diffusion models rely on deep architectures to achieve state-of-the-art performance.
- The theoretical results are derived under idealized conditions, such as target distributions concentrated on low-dimensional linear manifolds or composed of independent components, which may not fully reflect real-world data complexities. Real-world data often exhibits non-linear structures and complex dependencies, which the current theoretical framework does not fully address. This raises concerns about the generalizability of the results to more realistic scenarios.
- Optimizing over Barron spaces can be computationally challenging due to the infinite-dimensional nature of these function spaces, raising questions about the practicality of implementing the proposed methods. While the paper provides theoretical guarantees, the practical implementation and optimization of these models in Barron spaces may present significant hurdles, particularly when scaling to high-dimensional data. The paper does not provide sufficient details on how to address these computational challenges.
- Minor typo: Line 315 (difference -> different?)

### Questions
- To what extent can the assumptions of Lipschitz continuity and sub-Gaussianity be relaxed? Are there alternative conditions under which similar results could be obtained, possibly broadening the applicability of the theory?
- Can the authors elaborate on the practical aspects of optimizing over Barron spaces?
- In practical scenarios, data often contain noise and may deviate from idealized models. How robust is the proposed approach to such imperfections, and what modifications, if any, are needed to handle real-world datasets?
- Given that non-linear manifolds are noted as future work, could you share any preliminary insights on how extending to non-linear latent structures might impact sample complexity or theoretical guarantees?"

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
1

### Summary
The paper explores the effectiveness of shallow diffusion networks in learning distributions with low-dimensional structure, challenging the traditional belief that high-dimensional data inherently suffers from the curse of dimensionality. The study provides sample complexity bounds for these models, showing that they depend more on intrinsic latent dimensions rather than the ambient space, thus offering insights into the strengths of diffusion models for structured data generation.

### Strengths
The research presents a theoretically grounded approach to understanding the success of shallow diffusion networks, especially for low-dimensional structures in data.

### Weaknesses
The reliance on Barron spaces, while insightful, could pose challenges for scalability and model tuning in larger, more complex network architectures, which are crucial to modern success of diffusion-based generative models. Specifically, the Barron space norm, which is used to bound the complexity of the learned score function, may not be easily minimized in practice using standard gradient-based optimization techniques, especially as the network depth and width increase. This could lead to suboptimal performance when applied to more complex, real-world datasets where deeper networks are often necessary to capture the underlying data distribution. Furthermore, the analysis does not explicitly address the impact of architectural choices, such as the type of activation functions or the specific connectivity patterns within the network, on the learned score function's Barron norm, which could be a significant factor in practice.

### Questions
- Can the analysis be adopted to flow models/matching, which instead regresses a network onto the vector field of probability ODE (rather than the score)? 
- Can the authors give comments on how the analysis can be extended to discrete state spaces, for applications such as discrete diffusion models for language modeling?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper shows that learning diffusion model in Barron spaces (spanned by single-layer neural networks) avoids curse of dimensionality by adapting to low dimensional subspace.

### Strengths
Solid paper with concrete mathematical analysis. The results in the paper could be of general mathematical interests for related fields.

The paper makes a meaningful step towards understanding the gap between curse of dimensionality in theory and no curse in reality.

The paper has nice connection with recent progress in diffusion sampling process.

### Weaknesses
I have problems with calling results on "single-layer neural networks" by "results on shallow networks". Neural networks with a few layers are also shallow and the authors don't prove for them here. I'm not going to start a lecture on logic, but a paper should always try avoiding unnecessary confusions, especially those that make people think more favorably than it actually deserves.

The setting of single-layer networks is way too simple. The industry of deep learning scales to using 100k H100s, yet theories still are struggling with analyzing single-layer networks.

The formula in the theorems are complicated. If a simple setting leads to such convoluted formula, what would the more general cases be like?  Usually simpler things are more useful. It would benefit the presentation if a neat bound could be given the main body and a more detailed bound given in the appendix.

Lack of analysis of the gradient descent training process of neural networks.

Lack of direct usable implications. What could practitioners benefit from the theories? Or what future development of the theories could lead to some algorithmic innovations that is beyond imagination of practitioners? Machine learning is rather noisy compared with things like Physics. It's the best if we can get something useful from theoretical understandings.

Lack of experiments. The authors have proposed a set of assumptions which they believe is meaningful and proved results under these assumptions. It would be extremely beneficial to prove that these assumptions are relevant for the real world tasks and experiments on either simulation or real world data support the claim of the theorem. In theories, one inevitably chooses many simplification to make things elegant, which is quite understandable. However, experiments are needed to show that these simplification doesn't make the theoretical results irrelevant.

### Questions
Included in weakness.

### Soundness
4

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
3

### Summary
This theoretical work shows that for a neural network which is infinitely wide, and where neuron parameters come from the hypersphere, 
and there is one of two hidden latent structures in the data, then there is a bound on the emprical risk minimizer which only
depends on the dimension of the latent structure and not the dimension of the ambient space. 

If we denote the ambient dimension as D, the two hidden structures considered are 1) a linear combination of lower dimensional 
vectors (of dimension d << D) and 2) a linear combination of independent components all of lower dimension than the ambient 
space, but but where the sum of the dimensions of the components sum to D.

### Strengths
S1: Diffusion models are videly used, so theoretical work on them is highly relevant. 

S2: Going from needing a specific architecture to "only" needing the network to be infinitely wide to get a bound, is a step forward. 

S3: Corollary 3.4 and 3.8 give bounds on the KL-divergence between the true data distribution and that of the diffusion model, 
given enough training samples (and the extra assumptions) which is interesting.

### Weaknesses
W1: I found this paper difficult to follow. I count this as a weakness, since I am a machine learning researcher who is interested in
the theory of machine learning, so I should be the target audience. See my questions and suggestions for places where clarification is
needed.

Q1: On line 42-44 you write: "these works leave open the difficulty of statistical estimation, and therefore raise
the possibility that the sampling problem’s true difficulty is hidden in the complexity of learning."
Can you explain what you mean by this?
Especially, "the difficulty of statistical estimation", do you mean how close the estimation can get to the true distribution?
And "the sampling problem’s true difficulty is hidden in the complexity of learning.", what do you mean by this?


Q2: Line 165: W.r.t. risk for score function being asymptotic to $n^{-2/(D+4)}$. Do you mean asymptotic as $n \to \infty$?
(If yes, this could also be written in words, then you could avoid introducing the extra notation.)


Q3: Line 175-179: Can you give some intuition of the F_1-norm? Is it right that F_1 is the functions for which the integral is bounded
for all their basis functions? And does that mean the F_1-norm is the smallest integral for the "largest" basis function?


Q4: In line 180, you say that you only consider neuron parameters from the hypersphere. Is there a reason why this
generalizes to neuron parameters chosen over the entire space? If there is, I would like that argument added.
If there is not, I think you should add this assumption in the part of the introduction where you state your contribution.


Q5: In line 231: In your shorthand notation, you define $\mu_{t,x} = \mu_0 \lor \sigma_t\sqrt{D}$. I am used to $\lor$ being
the logical "or", but that cannot be what you mean in this context. So what does it mean here?


Q6: In your remarks under theorem 3.3, you say that you leave showing a $n^{2/(d+4)}$ to future work, but in 3.3 you give an upper
bound, and $n^{2/(d+5)} < n^{2/(d+4)}$ for $n > 1$. So how is $n^{2/(d+4)}$ a better bound?


Q7: I don't recognize the denpendence on $\sigma_t$ which you mention in the remarks after theorem 3.3. Where do you have something
bounded by $\sigma_t^{-4/(d+5)}$?


Q8: In line 491 you mention your "truncation arguments", could you say what you mean by this? And maybe give a reference to where
you make these arguments?

### Questions
**Questions:**

Q1: On line 42-44 you write: "these works leave open the difficulty of statistical estimation, and therefore raise 
the possibility that the sampling problem’s true difficulty is hidden in the complexity of learning."
Can you explain what you mean by this? 
Especially, "the difficulty of statistical estimation", do you mean how close the estimation can get to the true distribution?
And "the sampling problem’s true difficulty is hidden in the complexity of learning.", what do you mean by this?


Q2: Line 165: W.r.t. risk for score function being asymptotic to $n^{-2/(D+4)}$. Do you mean asymptotic as $n \to \infty$? 
(If yes, this could also be written in words, then you could avoid introducing the extra notation.)


Q3: Line 175-179: Can you give some intuition of the F_1-norm? Is it right that F_1 is the functions for which the integral is bounded 
for all their basis functions? And does that mean the F_1-norm is the smallest integral for the "largest" basis function? 


Q4: In line 180, you say that you only consider neuron parameters from the hypersphere. Is there a reason why this 
generalizes to neuron parameters chosen over the entire space? If there is, I would like that argument added. 
If there is not, I think you should add this assumption in the part of the introduction where you state your contribution.  
 

Q5: In line 231: In your shorthand notation, you define $\mu_{t,x} = \mu_0 \lor \sigma_t\sqrt{D}$. I am used to $\lor$ being 
the logical "or", but that cannot be what you mean in this context. So what does it mean here? 


Q6: In your remarks under theorem 3.3, you say that you leave showing a $n^{2/(d+4)}$ to future work, but in 3.3 you give an upper 
bound, and $n^{2/(d+5)} < n^{2/(d+4)}$ for $n > 1$. So how is $n^{2/(d+4)}$ a better bound? 


Q7: I don't recognize the denpendence on $\sigma_t$ which you mention in the remarks after theorem 3.3. Where do you have something 
bounded by $\sigma_t^{-4/(d+5)}$? 


Q8: In line 491 you mention your "truncation arguments", could you say what you mean by this? And maybe give a reference to where 
you make these arguments? 


**Suggestions:**

U1: Please make sure to use the full name and not an abbriviation the first time you mention a concept.
	For example: DDPM in line 66, ERM in line 74, DNN in line 90 and GD in line 97. 


U2: Please make sure to explain all the notation you use before you use it. If you feel it would take up too much space 
in the main paper, you can make a list of used notation in the appendix. 
Specific notation, where I cannot find an explanation in the paper: 
$\mathcal{F}_t$ in equation 3.7 (I am guessing this is the space of score functions), $\asymp$ in line 165, 
g cts in line 176 in the definition of the Total-Variation norm, the $\lor$ in line 231 and equation 3.10 and
Law(.) in last line of corollary 3.4. 
  

U3: I feel the title over-promises. "SHALLOW DIFFUSION NETWORKS PROVABLY LEARN HIDDEN LOW-DIMENSIONAL STRUCTURE"
sounds like it is _all_ shallow networks and _all_ hidden low-dimensional structures. Of course I understand 
if you feel the title would get too long if you add all the assumptions, so I would suggest finding a new title 
which is as short or shorter, and which does not make the result sound more general than it is. 


U4: Typo in line 189: Should be $B_2(r, d)$

### Soundness
3

### Presentation
2

### Contribution
3
