# Fiber Monte Carlo

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
Integrals with discontinuous integrands are ubiquitous, arising from discrete structure in applications like topology optimization, graphics, and computational geometry.
    These integrals are often part of a forward model in an inverse problem where it is necessary to reason backwards about the parameters, ideally using gradient-based optimization. 
    Monte Carlo methods are widely used to estimate the value of integrals, but this results in a non-differentiable approximation that is amenable to neither conventional automatic differentiation nor reparameterization-based gradient methods. 
    This significantly disrupts efforts to integrate machine learning methods in areas that exhibit these discontinuities: physical simulation and robotics, design, graphics, and computational geometry.  
    Although bespoke domain-specific techniques can handle special cases, a general methodology to wield automatic differentiation in these discrete contexts is wanting. 
    We introduce a differentiable variant of the simple Monte Carlo estimator which samples line segments rather than points from the domain. 
    We justify our estimator analytically as conditional Monte Carlo and demonstrate the diverse functionality of the method as applied to image stylization, topology optimization, and computational geometry.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a way to estimate derivatives of integrals of discontinuous functions with respect to parameters. Sampling line segments rather than points produces an empirical estimate that is continuous and (almost-everywhere) differentiable. Assuming the discontinuous integrand is parametrized by a superposition of indicator functions parametrized by implicit level sets, the derivatives of integrals over individual line segments can be calculated by differentiating the implicit functions. The method is demonstrated on several problems: 2D inverse rendering, topology optimization, and convex hull approximation.

### Strengths
I like the simplicity and elegance of the central idea: sample extended geometric objects (in this case line segments) rather than points, and use the geometry to get better estimates. The authors point out the long history of this idea in mathematics, dating back at least to the Crofton formula, Radon transform, and integral geometry. These are ideas that I think have yet to be fully exploited in neural rendering/neural fields/inverse graphics. One related work I would suggest citing is the following, which also involves the evaluation of neural fields along lines rather than points:

- V. Sitzmann, S. Rezchikov, B. Freeman, J. Tenenbaum, and F. Durand, “Light Field Networks: Neural Scene Representations with Single-Evaluation Rendering,” in Advances in Neural Information Processing Systems, Curran Associates, Inc., 2021, pp. 19313–19325.

### Weaknesses
The applications seem less than convincing to me. It seems clear that the image stylization is meant to stand in for inverse graphics more generally, but it is unclear to me what advantage the type of representation to which this method is wed (superposition of sublevel sets) would be advantageous over a continuous field representation, which would obviate the need for the fiber sampler.

The application to topology optimization is more compelling in that topology optimization generally seeks solutions in indicator functions. However, the choice to represent the indicator function on a grid seems puzzling when a great advantage of a sampling-based estimator coupled to automatic differentiation is the flexibility of the underlying representation.

The convex hull application seems the weakest to me. It looks like the generated approximate hulls are not even convex, nor do they contain all the points, so it is unclear how they would be useful in downstream applications such as collision detection. In any case, classical convex hull algorithms in low dimension are plenty fast and come with correctness and performance guarantees. Accordingly, any proposal to replace them with a learned "oracle" must clear a very high bar.

More generally, only a few results are shown, and the numerical comparisons in the topology optimization case only show a marginal improvement in objective function. It would be good to include at least a few more test cases and comparisons.

### Questions
- It seems like the method is limited to settings where the integrand is described by a superposition of indicator functions parametrized by implicit sublevel sets. But if one is going to use such a representation, why not just use a continuous implicit function directly. For example, rather than using a superposition of level sets of SIREN networks, one could just use SIREN directly. In what application domains do you see this sort of representation being uniquely advantageous?
- The authors repeatedly emphasize that the method is only applicable in low dimension. Why is this? What would it take to extend the method to general dimension? What about to spaces other than $\mathbb{R}^n$?
- What are the island artifacts in the topology-optimized solutions using fiber sampling? Why do they appear?
- What would it take to extend the method to more general geometry representations for topology optimization rather than just grid discretization?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper considers a novel differentiable integral estimator that operates by sampling lines instead of points. The method generalizes to a relatively broad swath of low-dimensional integrals with discontinuous integrands, allowing for quick prototyping and broad application to a variety of scenarios, as shown in the experiments.

### Strengths
I have reviewed this paper previously as a NeurIPS submission, and it has changed relatively little. That is to say, I was pretty positive on it back then, and my opinions remain unchanged. 

* The problem considered is an important and wide-ranging one. The method is implemented in a common library, so should allow for ease of use by a variety of practitioners in other application domains.
* I still think the presentation is quite clear. A previous reviewer challenged it as imprecise, but I do not share their opinion and felt they were nitpicking.
* I appreciated the validation across three relatively different scenarios.

### Weaknesses
 * The restriction to low-dimensional integrands may cut out some desired use cases. This is more of an inherent challenge perhaps that any Monte Carlo-based method would suffer. Specifically, the curse of dimensionality will likely cause the variance of the estimator to grow exponentially with the dimension of the integral, making it impractical for high-dimensional problems. This limitation should be clearly stated and discussed in the paper, perhaps with a theoretical analysis of the variance scaling with dimension, or at least a reference to existing literature on this topic.
* As before, I think it would be interesting to see the method compared to bespoke algorithms in those particular use cases. I expect, of course, that the given method will do worse, but if it is comparable that would be a win, given its much broader applicability. It would be useful to see a more detailed analysis of the trade-offs between the generality of the proposed method and the performance of specialized algorithms. For instance, in the rendering example, how does the performance compare to state-of-the-art path tracing algorithms? While the authors mention that their method is not intended to compete with these algorithms, a quantitative comparison would be useful to understand the performance gap and the scenarios where the proposed method is most beneficial.

### Questions
1. Can you delineate what has been changed from the NeurIPS submission?
2. In the previous NeurIPS discussion, you referenced a plot of variance as dimension increased. Can you include this again in supplementary? I think it's useful for noting this limitation.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Proposes a new formulation of Monte Carlo Integration/Estimation that samples line segments on the integration domain as opposed to points.  This is of particular relevance in gradient-based optimization for inverse problems, where discontinuities in gradients of the MC estimate with respect to input parameters are either non-differentiable, or lead to incorrect results.  By sampling line segments instead of points, the parametric gradients become well-defined and differentiable.

### Strengths
The paper is generally well-written, and addresses an established problem space that is relevant to a broad range of applications as enumerated by the authors.  The central idea itself (sampling "fibers" rather than points) is interesting, and claims to be a general formulation that avoids domain-specific solutions and can be applied within a generic auto-differentiation framework.  The theoretical correctness of their proposed sampling method is proved (i.e. that it remains an unbiased estimator).

### Weaknesses
While the broad application areas presented are impactful, the actual evaluation is very limited.  Specifically, the rendering application is evaluated using only qualitative (not quantitative) results, on a single scenario.  The topology optimization example is also evaluated on only a single example -- while it is understandable that the authors specifically acknowledge that in-depth evaluation of this task is lacking, stating that this is not the central focus of the paper, it brings into question the meaningfulness of this experimental result.  In the case of the convex hull example, no comparison to alternative methods is provided.  (I would personally find a slightly more in-depth investigation of fewer applications to be more enlightening, though I do not expect the authors to drastically alter their existing experiments).

There seem to be missing key references w/r/t the claimed applications, for example, in the case of differentiable rendering and simulation.  Are such references considered to be out of the scope of the paper?  As mere examples, in the case if differentiable rendering (by no means an exhaustive list):
- Merlin Nimier-David and Delio Vicini and Tizian Zeltner and Wenzel Jakob.  Mitsuba 2: A Retargetable Forward and Inverse Renderer.
- Tzu-Mao Li, Miika Aittala, Frédo Durand, Jaakko Lehtinen.  Differentiable Monte Carlo Ray Tracing through Edge Sampling.

### Questions
- In some applications (e.g. Monte Carlo Path Tracing Rendering), the integration domain must be sampled according a non-uniform probability distribution.  This is commonly achieved by inverse-transform sampling, whereby random variables are sampled from a uniform distribution, then mapped to the target distribution via its inverse-CDF.  Is Fiber Monte Carlo compatible with such sampling requirements?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
