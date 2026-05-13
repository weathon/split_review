# BAYESIAN EXPERIMENTAL DESIGN VIA CONTRASTIVE DIFFUSIONS

- Decision: Accept
- Scores: 8, 6, 8

## Abstract
Bayesian Optimal Experimental Design (BOED) is a powerful tool to reduce the cost of running a sequence of experiments.
When based on the Expected Information Gain (EIG), design optimization corresponds to the maximization of some intractable expected  {\it contrast} between prior and posterior distributions.
Scaling this maximization to high dimensional and complex settings has been an issue due to BOED inherent computational complexity.
In this work, we introduce an {\it expected posterior} distribution with cost-effective sampling properties and provide a tractable access to the EIG contrast maximization via a new EIG gradient expression. Diffusion-based samplers are used to compute the dynamics of the expected posterior and ideas from bi-level optimization are leveraged to derive an efficient joint sampling-optimization loop, without resorting to lower bound approximations of the EIG. The resulting efficiency gain allows to extend BOED to the well-tested generative capabilities of diffusion models.
By incorporating generative models into the BOED framework, we expand its scope and its use in scenarios that were previously impractical. Numerical experiments and comparison with state-of-the-art methods show the potential of the approach.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper presents a new expression for the gradient of the expected information gain (EIG)---a central quantity in Bayesian optimal experimental design (BOED). Their method, named CoDiff, combines the two steps of maximizing the EIG and then sampling from the posterior in BOED into a single joint step by leveraging the sampling-as-optimization setting of e.g. Marion et al. (2024). Doing so results in a more efficient BOED method, as demonstrated by numerical experiments.

### Strengths
The paper advances the field of BOED by making it more computationally efficient, whilst broadening the scope of problems that can be tackled by BOED by extending it to diffusion-based generative models. The idea of performing joint sampling and optimization using bi-level optimization seems novel to, although I am not very familiar with this literature. The experimental results are significant and demonstrate the efficacy of CoDiff compared to other baselines. The method is presented clearly along with discussions w.r.t. to the related works. Overall, this is a well-written and technically solid paper, and I am happy to recommend its acceptance.

### Weaknesses
Some minor points:
* It would be nice to see some uncertainty bars around the results in Figure 3.
* Parts of Section 4 and 5 were a bit difficult for me to follow, but that could just be because I am not familiar with the relevant literature. However, if possible, it might be a good exercise for the authors to think about making these parts a bit more accessible to the BOED community who are not familiar with the sampling-as-optimization literature.
* It would have been nice to empirically test the performance of CoDiff as e.g. the dimensions of $\theta$ or the hyperparameters (if any) vary.
* Please include some limitations of CoDiff in the conclusion section.

### Questions
See the "Weaknesses" section.

### Soundness
3

### Presentation
3

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
This paper is a little outside of my expertise and I apologize in advance for any misunderstanding I may have and look forward to any correction from the authors. I have set my confidence to low accordingly.

The authors consider the problem of experimental design, given a statistical model of the form $P(y | \xi, \theta)$, we can choose values of $\xi$ and observe a corresponding $y$, and the goal is to infer $\theta$. In the first example in the paper, $\xi$ are locations on a 2D plane, $y$ are the measurements at the $\xi$ locations, and $\theta$ represents the source locations of contamination in the plane.

Assuming we have chosen the $\xi$ values, we can use the $p(y|\xi)$ to simulate $y_i$ values, one hallucinated rollout into the future, then infer the hallucinated posterior $p(\theta'|y_i, \xi)$ and measure the posterior distribution's entropy, $H(p(\theta'|y_i,\xi))$, typically requiring Monte-Carlo over the $\theta'$. We may repeat this process many many times for $i=1,...,N$, and compute the average posterior entropy, wrapping the inner Monte-Carlo over $\theta'$ in another outer Monte-Carlo over $y$. This average posterior entropy is the Mutual Information (MI) between $y$ and $\theta$ up to an additive constant (that is the prior entropy $H(p(\theta))$). This MI quantifies the benefit of sampling $y$ at $\xi$, we can therefore change $\xi$ in a way to maximise MI and this is a standard method for experimental design known as Expected Information Gain, or EIG.

However as evaluating EIG requires performing nested Monte-Carlo, and optimizing $\xi$ requires the gradient of EIG, much work has focused on various methods to construct efficient EIG gradient estimators. In past works and this works, the second inner integration over $\theta'$ is performed with MCMC or by Monte Carlo with importance sampling using a proposal $q(\theta'|y_i)$ that must be updated for every outer MC iteration $i$.

This work proposes to use a single proposal distribution across all outer MC iterations $i$ called the "expected posterior" which is a geometric mixture of all the hallucinated posteriors
$$
q(\theta') \propto \prod_i p(\theta|y_i, \xi)^{\nu_i}
$$

The paper proposes to Langevin dynamics to generate samples for the outer Monte Carlo $\\{y_i, \theta_i\\}$ from the joint distribution. As these samples are updated in a iterative manner, and the goal is to iteratively optimize $\xi$, these nested iterative procedures can be merged and updated together, if $\xi$ only incrementally moves, it is wasteful ti discard all the old samples $\\{y_i, \theta_i\\}$ but keep incrementing them so they're up-to-date.

Finally the proposed method is applied to two sequential design applications, the first is the source location example in which the $p(\theta)$, $p(y|\theta, \xi)$ have known analytical forms and the proposed method outperforms baselines. The second is where $p(\theta)$ cannot be evaluated but can be sampled, specifically a diffusion model trained on MNIST images, $\theta$ is a full image,  $\xi$ are pixel locations, and $y$ are the 7 X 7 patch of pixel values around $\xi$. The goal is to infer the full image by cherry-picking image patches.

### Strengths
- rigorously cites and discusses related ideas
- merging multiple nested loops into a single loop is intuitive idea and has been applied in multiple separate fields (training a VAE is effectively the EM algorithm was simplified into a single step, in Bayesian optimzation few-shot Knowledge Gradient)
- the writing is clear and each idea is easy enough to follow.

### Weaknesses
### Technical Comments
- __expected posterior__ the paper states that they aim to find one proposal distribution that covers all possible future posteriors and proposes a distribution that is a geometric mixing of hallucinated posteriors $q(\theta) \propto \prod_i p(\theta|y_i, \xi)^{\nu_i}$. The prior is the true expected posterior $p(\theta) = \mathbb{E}_Y[p(\theta|y)]$, exactly the average density of all possible posterior densities.  Why not use the prior $p(\theta)$ as the one global proposal distribution for integration over all the hallucinated posteriors? In the sequential case (introduced at the end of the paper)

### Writing Comments
- __Writing Density__ while the writing is thankfully clear, the paper cites and quickly introduces many ideas from prior works in quick succession making the paper very hard work to read for me, a lot of context switching making the paper very tiring. I would suggest reducing the details of referenced works, and providing higher level descriptions where possible and elaborating more on the novel parts of the proposed method.

### Questions
- Can the authors provide an intuition as to why the proposed expected posterior is preferable to the true expected posterior = prior? Is this purely for the sequential setting?
- how are the $\nu_i$ values determined in the expected posterior?
- what stop other methods from being used on the MNIST example? Is it just the computational cost from multiple nested loops and the sequential use case?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper makes an interesting connection between Bayesian optimal experimental design (BOED) and optimization by sampling using a diffusion model. While an interesting connection that may prove fruitful with some refinement, the authors seem to misunderstand the basis of BOED and maximization of a lower bound of mutual information using contrastive learning, as well as miss prior work that might better-inform this method. This disconnect, as well as confusing notation regrading how the diffusion model is used in multi-round BOED and lackluster empirical evaluation, makes me think this work is too early and could benefit from refinement in writing and additional experimental evaluations of the method.

### Strengths
- The authors make a great connection to optimization by sampling via diffusion models. 
- Thorough gradient analysis.
- The connection to inverse problems e.g. inpainting in MNIST images as a BOED problem is an interesting new task in the BOED setting and could see BOED objectives (really mutual information objectives) gain further adoption in generative modeling.

### Weaknesses
While the authors make a great connection to optimization by sampling, theoretical analysis of the convergence of the desired goal distribution is missing. This would e.g. especially be helpful in the multi-step BOED setting to show how to improve bounds of the mutual information. I list out my critiques and questions below:

- The authors miss that they are also optimizing a lower bound of the mutual information by the InfoNCE bound, thus their comments that their approximation is exact is incorrect.
- The definition of information in Equation 2 does not make sense. The KL divergence is written in a non-standard way - do you mean $E_{p(y|\xi)}KL(p(\theta|y, \xi) || p(\theta))$?
- The authors miss the connection to Fotster et al. 2019b of LF-ACE that uses a posterior estimate in the InfoNCE bound to refine samples. e.g. in equation 5. 
- The notation for the expected posterior in equation 9, it's not clear what is the proposal distribution $q(\theta)$ in the paper. Are you using likelihood evaluations? Also, how are you choosing the weighting of $\nu_i$?
- I would prefer to see the notation for iterative sampling operators similar to Marion et al. 2024, where the Y, and $\Theta$ are variables of the operator instead of in the superscript. I think that would make the optimization problem more clear. 
- After equation 15, are you using two generative models to define the observed distribution $y$ and the parameter distribution $\theta$?
- in terms of the location finding experiment, usually we would expect to see the designs and final posterior distribution. the way it's portrayed in the paper is confusing. I'm not sure which samples are shown, which design round the designs come from, and why the seeming optimal design isn't on the ground truth values. It looks like the chosen design is quite far from the true theta_0.
- While the EIG seems to improve over others in Figure 3, the upper bound is _much_ worse. Why is that? 
- The MNIST experiment is interesting but lacks quantitative evaluation. Maybe including a classifier and using the number of successfully classified images would help? Also, there seems to be opportunity to change the design size to see how that influences outcomes.

In summary, I think the notation is a little bloated. The authors tend to repeat themselves in the text and could be more concise. Concision would help make space for exposition of more salient points that would improve this paper. Additionally, it would help the authors to explicitly lay out what are the likelihood, posterior, and priors they use in experiments. Also, it would be nice to see calibration of the posterior that results of the final design round using e.g. the l-C2ST method or other simulation based calibration methods. Most applications of amortized posteriors using BOED will be interested in this, but it can be computationally expensive, which is why I think just on the final round is sufficient. This is an interesting method that I think needs cleaner exposition.

### Questions
My questions are contained in the Weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3
