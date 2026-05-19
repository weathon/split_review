# Improved Sampling Algorithms for Lévy-Itô Diffusion Models

- Decision: Accept
- Scores: 8, 8, 6, 5

## Abstract
Lévy-Itô denoising diffusion models relying on isotropic α-stable noise instead of Gaussian distribution have recently been shown to improve performance of conventional diffusion models in image generation on imbalanced datasets while performing comparably in the standard settings. However, the stochastic algorithm of sampling from such models consists in solving the stochastic differential equation describing only an approximate inverse of the process of adding α-stable noise to data which may lead to suboptimal performance. In this paper, we derive a parametric family of stochastic differential equations whose solutions have the same marginal densities as those of the forward diffusion and show that the appropriate choice of the parameter values can improve quality of the generated images when the number of reverse diffusion steps is small. Also, we demonstrate that Lévy-Itô diffusion models are applicable to diverse domains and show that a well-trained text-to-speech Lévy-Itô model may have advantages over standard diffusion models on highly imbalanced datasets.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a paremetric family of SDEs allowing different sampling scheme from a single pretrained Levy Ito diffusion model. It brings the toolbox for Levy Ito diffusion models (LIM) closer to that of standard "Gaussian" diffusion models (DM). Empirically, the authors find that the new paremetric family of SDEs has benefit in term of generated samples quality and diversity at low number of functional evaluations, which lowers the computational cost of sampling from Levy Ito diffusion models. Finally, they train a text-to-speech diffusion model on an imbalanced dataset and evalutate the benefits of LIMs compared to DM.

### Strengths
* The parametric family of SDEs derived by the author is new and offer more flexibility for LIM sampling.
* The authors give a rigorous derivation of the proposed SDEs
* The paper clearly tries to show how their theoretical results compare with existing litterature on LIMs. It explains clearly what is the limitation of Yoon et al (approximation of the reverse process).
* Promising results for text to speech models
* The paper is well written overall

### Weaknesses
* The experiments about text to speech models are interesting and promising but they are not tied to the main results of the paper (theoretical and empirical contributions to LIM sampling). The baseline DM against which authors compare is also new and has the modifications outlined in lines 809 to 825 in the Appendix.
* The simple toy example explains well why processes with zero mean and finite variations cannot be omitted completely in low NFE schemes. However, in my opinion, the paper does not explain clearly what steps/changes in the parametric family of SDEs prevents any such (intractable) process to come into play. I understand from line 286 that the reverse time SDE is no longer a model of the forward time SDE and that trajectories are different. Is that what allows you to have "better" SDEs?
* (Not a real weakness per se) The new paremetric family of SDEs does not improve the capabilities of LIM in term of imbalance "correction". As examplified by table 4.

### Questions
* Please explain weakness 2.
* For the text to speech model, even on the main mode (female speakers), LIMs outerperform Gaussian DMs. Why is that? Wouldn't we expect Gaussians DM to perform better on the main mode of the distribution? Does fixing the "bias" in the text encoder (line 809 to 825) unfairly disadvantage Gaussians DM even on the main mode? What would the results have been with a standard encoder (or alternatively do you have other baselines for text to speech imbalanced modeling that would shed light on the benefits of LIM on both the main mode and the tail mode)? You are also using an ODE sampler, which, in your image generation experiment, favors the less frequent class. 
* It seems that the common accepted reason for which LIMs are better for imbalanced datasets is that Lévy Ito processes, with their heavy tails and jump possibilities, better cover less probable isolated modes of the data distribution. In your opinion, why does this phenomenon subsist when using ODE sampling? In your imbalanced CIFAR experiment, classes 8 and 9 seem favored by the ODE.

### Soundness
3

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
3

### Summary
Levy diffusion models perform better (especially on rare classes) when it’s trained on imbalanced datasets. However, the previous reverse Levy process doesn’t have same marginal probabilities at each noise level due to the omitted intractable term, resulting in non-exact sampling. 
The authors propose a novel parametric family of SDE whose solutions have the same marginal densities as the forward levy diffusion process, leading to exact solutions. 
Empirical experiments demonstrate that the proposed reverse process has superior sample quality with small number of sampling steps, and also performs good in terms of sample diversity.

### Strengths
- The paper is well-organized, and the technique derivations are solid. Also most of the arguments are well supported by experiments. 
- Instead of developing a reverse-time process of the forward Levy-Ito SDE, the authors propose parametric reverse-time SDEs that have the same marginal probability densities as the forward process, which gives exact sampling. 
- It seems like compare to the baseline SDE, the proposed one is good with multiple numerical solvers. For example, in Table 1 and 2, SDE(11) performs good with both solvers, while baseline SDE approximate(9) has a different performance with different solvers.

### Weaknesses
- Though the improvement of FID scores given small number of sampling steps (e.g. N=20) is huge, the improvement on imbalanced CIFAR10 is marginal. Also, it could be nice to provide some FID scores of samples from Gaussian diffusion models, which shows a clear improvement in imbalanced dataset. 
- In the speech synthesis experiment, the authors compare the proposed model only with the Gaussian-based diffusion model. However, it remains unclear whether this model is still SOTA when compared to the baseline Lévy-Itô diffusion model.

### Questions
- In table 3, I wonder how many times the authors run the experiments? It seems that for both FID and coverage metrics, the proposed SDE has very close performance to the baseline SDE. 
- In the speech synthesis experiment, could you provide a comparison to the baseline Lévy-Itô diffusion model?

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
The paper offers a novel method for sampling using a Lévy-Itô diffusion model based on a new formulation of its corresponding SDE. The authors identify an issue in existing methods for the reverse SDE caused by neglecting one of the terms, and offer a solution. The paper includes experiments which compare the generation results of the proposed solutions to alternatives, as well as a demonstration of its use in addressing skewed training datasets in the text-to-speech field.

### Strengths
- The paper analyzes Lévy processed and their use for diffusion models, a field which is under-explored.
- The proposition in the paper is straightforward and mathematically justified.
- The experiments in the paper provide evidence of the benefits of the new method.

### Weaknesses
- The presentation of the paper could be improved, both at the sentence and at the paragraph level.
- The figures and naming scheme makes it hard to follow the result and illustrations in the paper. (specifically in Fig. (4), Fig (1), Tab. (5))
- The takeaway from the experiment shown in Tab. (4) is unclear. While Tab. (3) shows a small advantage for the proposed method, the results in Tab. (4) do not reflect that.
- The evidence for an advantage in underrepresented data could be made stronger (using more examples, specifically in the image domain).

If some of my weaknesses are properly addressed I am inclined to raise my score.

### Questions
- I believe it would be easier to follow the comparisons by using a consistent naming scheme, instead of the current SDE(<number>)
- How do extremely small NFEs (5-15) effect the sampling quality of the proposed method?

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
2

### Summary
A family of inverse dynamics is derived for diffusion models that use isotropic (\alpha)-stable noise instead of Gaussian noise. Such models have been proposed recently with a deterministic inverse dynamics and a stochastic one. The deterministic dynamics is guaranteed to retrieve the exact marginal distributions. Unfortunately, the stochastic dynamics yields only approximate solutions.  This paper addresses this limitation. The algorithm is expected to be effective for data generation on imbalanced datasets. Its practical usefulness is experimentally examined in applications to image generation and text-to-speech tasks.

### Strengths
A parametric family of inverse dynamics is derived for diffusion models that use isotropic (\alpha)-stable noise instead of Gaussian noise. Unlike the previously proposed one, this family is guaranteed to exactly retrieve the target marginal distributions for any parameter setting in ideal cases.

### Weaknesses
Writing in section 3.3 is sloppy. Since "some intractable data-dependent process Z_t" is not explained sufficiently, it is difficult to grasp the relation between the previously proposed algorithm and the current one.

### Questions
The relation between the algorithm by Yoon et al (2023) and the current one is unclear. Please explain more details on how equations (4) and (11) are related.

### Soundness
3

### Presentation
2

### Contribution
3
