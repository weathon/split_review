# Residual Deep Gaussian Processes on Manifolds

- Decision: Accept
- Avg Score: 7.60
- Scores: 8, 8, 6, 8, 8

## Abstract
We propose practical deep Gaussian process models on Riemannian manifolds, similar in spirit to residual neural networks.
With manifold-to-manifold hidden layers and an arbitrary last layer, they can model manifold- and scalar-valued functions, as well as vector fields.
We target data inherently supported on manifolds, which is too complex for shallow Gaussian processes thereon.
For example, while the latter perform well on high-altitude wind data, they struggle with the more intricate, nonstationary patterns at low altitudes.
Our models significantly improve performance in these settings, enhancing prediction quality and uncertainty calibration, and remain robust to overfitting, reverting to shallow models when additional complexity is unneeded.
We further showcase our models on Bayesian optimisation problems on manifolds, using stylised examples motivated by robotics, and obtain substantial improvements in later stages of the optimisation process.
Finally, we show our models to have potential for speeding up inference for non-manifold data, when, and if, it can be mapped to a proxy manifold well enough.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose a technique for manifold->manifold GP regression, which they propose to use as a component for deep GP regression on manifolds. They illustrate their procedure via a battery of numerical experiments on real and synthetic problems, including regression and Bayesian optimization.

### Strengths
--- 

Excellent presentation

Between the excellent illustrative figures such as figs 1/2 and the compelling narrative flow, this paper is a pleasure to read, which is especially outstanding given the proclivity of some authors to lean into the formalism when discussing ML on manifolds.

--- 

Clear and consequential applications

The authors make a good case that Deep GPs can be superior to single-layer GPs, and that manifold data are important, such that getting deep GPs for manifolds is an important problem to solve.

### Weaknesses
Since this paper uses numerical experiments rather than theory to introduce its methodology, the experiments are crucial to get right. I have some comments on them below.

---

Need clearer comparison to prior manifold->manifold GPs.

It would be help clarify the novelty and contribution of this article to make a more direct comparison to prior work with GPs on manifolds. Probably it is obvious to the authors, but it would be helpful to say exactly what the shortcomings of Mallasto and Feragen's 2018 work, say, which this work addresses. It would also be interesting to compare this methodology to theirs, or to explain why this is not feasible. See Questions for more.

---

Regarding BO on Ackley.
"This outcome aligns with our expectations, as the region around the minimum of the Ackley function is smooth and can be effectively modelled by a shallow GP."
But the model is modeling the entire function, not just a region around the optimum, right? And the ackley function exhibits significant nonstationarity, so we would expect a deep GP to do a better job modeling it. How do the two methods compare in terms of out-of-sample MSE on this function? Does the deepGP do a better job modeling it, but just not optimizing it?

---

 Section 4.4 

I'd like to first commend the authors for sharing a negative result; the failure to investigate limitations of methods is doubtless a serious drag on machine learning research.
However, I have methodological concerns about this study, such that I fail to be convinced that a negative result is indeed appropriate. 
i) The per-iteration complexity is interesting, but it's not the ultimate issue of concern, which is wall-time to a given accuracy (as iterations required may differ between methods).
ii) The use of different optimization methods makes the comparison difficult; I understand the idea may have been to make a comparison to the existing baseline rather than a different one, but it's crucial to identify where any advantage or lake thereof lies by using the Euclidean GP with Adam as well. 
iii) It would be great if you could clarify on where the memory requirements for L-BFGS are coming from; a priori, one would expect that, since Adam keeps track of two vectors of the same size as the parameter vector, using L-BFGS with a history of size 2 would have similar memory requirements, and it seems like it would be possible to use a slightly larger one, like size 10.

### Questions
1) Can you please make more clear for readers without expertise in differential geometry how your approach to defining a manifold-valued stochastic process differs from that of Mallasto and Feragen, who also use an exponential map on the tangent space at a given point? Please emphasize the practical implications of the differences.
Also, is it the case that that method could not support a deep GP, or that there would be considerable work required to make a deep GP out of it? 

2) Does your work have implications for spaces that have much more structure than a manifold, like vector or function-valued mappings? Or do we recover already-used methods when deploying it in such context.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper proposes a manifold-to-manifold deep GP inspired by residual neural networks. It only requires modifying the last layer with a Gaussian vector field that represents the residual from the identity map. The input to that layer is then translated by the residual using an exponential map. The authors demonstrate that this model is effective on a wide range of synthetic and real-world experiments.

Disclaimer: While I have expertise in GPs, I don’t know much about non-Euclidean spaces or manifolds except for a high level understanding. Therefore, I might underestimate or overestimate the technical contributions of this paper. This is reflected in my low confidence score.

### Strengths
1. This paper proposes a simple and effective way to construct manifold-to-manifold deep GPs by modeling the residuals, which is both novel and interesting.

2. The paper is well-written with a good logic flow. It provides a clear introduction of the relevant technical background and a discussion of related works, which makes it easy for readers to understand the context of this work. The description and derivation of the model is also clear and easy to follow. The beautiful figures are a nice addition to the excellent content of the paper.

3. The proposed model is thoroughly evaluated on a wide range of synthetic and real-world experiments, including a careful ablation study of different choices of Gaussian vector fields and variational families. Empirical results show that the model consistently provides improved predictive accuracy and robust uncertainty estimation compared to shallow manifold GP baselines, which demonstrates its usefulness and wide applicability.

### Weaknesses
It seems that the deep GPs saturate quite quickly as depth increases in practice as shown in Figures 3 and 6, especially when the number of data points is small (which is the setting where GPs are typically employed). More generally, deep GPs can be difficult to train and not very scalable in practice, due to, e.g., mode collapse in variational inference. I guess residual deep GPs also share these limitations or perhaps even worse due to the additional components for handling manifolds. In the conclusion section, could the authors comment more on the limitations of residual deep GP (e.g., balance between dataset size, effective depth, scalability, accuracy, uncertainty quality, robustness, approximation, etc) and provide some suggestions as to when residual deep GPs should be preferred over, say, manifold-to-manifold neural networks (and potentially their ensembles if uncertainty estimation is required)?

### Questions
See weaknesses.

### Soundness
4

### Presentation
4

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
This paper outlines the idea of using compositions of Gaussian process priors on manifold structures. The basic idea is to take a normal Gaussian process with identity mean function, here referred to as a residual GP, and at each layer use the exponential map to constrain this to the tangent space of the manifold at x. This Riemanninan formulation has quite a nice connection to the identity mean function as the map itself is now defined by the location as in Eq 10. The paper then continues to fit the proposed modelling approach in how it fits into the literature of the doubly stochastic inference mechanism typically used for composite GPs and with interdomain inducing points to formulate the variational bound.

The paper concludes with a set of experiments, both synthetic experiments and a real experiment on a manifold.

### Strengths
This is a very well written paper, there are quite a few concepts to explain to get the background and the authors do this in a splendid manner. A lot of these topics are quite involved and it would have been easy to stray of the necessary path but the authors do an excellent job of not doing this. Very concrete and to the point, well done!

The derivation of the model is well done keeping a good balance between details and intuition of the approach.

### Weaknesses
A substantive assessment of the weaknesses of the paper. Focus on constructive and actionable insights on how the work could improve towards its stated goals. Be specific, avoid generic remarks. For example, if you believe the contribution lacks novelty, provide references and an explanation as evidence; if you believe experiments are insufficient, explain why and exactly what is missing, etc.

If I should play devils advocate with this paper the authors do not do enough to highlight the novelty of their approach neither highlight the benefits except for experimentally. We know that composite GPs are horrific to train, while the doubly stochastic bound often allows us to train the model it often leads to very questionable uncertainties. The authors do not do enough to highlight how, or if, this approach addresses these issues. These might come as very generic comments as it more relates to composite GPs in general but this is also how the authors mainly "sell" the paper, that it is a benefit in general to have a manifold structure even if I do not know the manifold of the actual data. It would be great to hear the authors address this.

I also find the Bayes Opt experiment a little bit disappointing, the idea of switching model after a specific set of iterations makes sense but how do I know where to switch, is this the optimal choice that is shown and if so what happens in other locations, both earlier and later? It would be good to see a more in-depth comparison here, what is the result if I use the composite GP from iteration 1? What happens if I swap to another shallow model at the same time? How are the hyper-parameters dealt with, do you marginalize them at each iteration? What is also worrying is the variance in the composite GP doe seem to go up quite substantially even while having 175 points to start from. It would be great to see a few different functions not just Ackley to see if the behavior is consistent across experiments.

### Questions
- While the work is theoretically sound I would love to see more analysis of why it works well. My conclusions from the paper are two, the first, if my data lies on a manifold then of course I should constrain my prior to reflect this. However, it does also seem to be the case that this approach performs better in general. I would love to try and get an intuition into this. We know after 10 years of working with composite GPs that simply they do not work, there are too many symmetries in the structure and together with the lax approximations this makes them very hard to use. What of this does this approach address? I would love to get some insights into this from the authors.
- In general it would be great to have more explanation of the model set-up for the different experiment, what are the thoughts behind specific model choices etc. As far as I understand from the experiment you perform modelling on the hyper-sphere, why is this a motivated choice?
- I would love to see an experiment where you actually have known manifold structures that are combined in a composition. What would be interesting to see is if you can correctly factorise the uncertainty across the different layers in the composition.
- It would be great if the authors could make more comments related to paper [1] which is at the moment only referenced as a footnote comment. 
- Would be great if you could expand the caption to Figure 2 to include explanations to both a and b. Right now there is a lot of jumping between pages to get that caption.
  
[1] Mallasto, A., & Feragen, A. (2018). Wrapped gaussian process regression on riemannian manifolds. In , 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 5580–5588). : .

### Soundness
3

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
This work generalizes Deep Gaussian Processes to Manifolds. They address the key challenge of modeling each hidden layer being a manifold to manifold map by interpreting the output of each hidden layer as a Gaussian Vector Field combined with an exponential map, allowing each layer to learn a residual displacement on the manifold. From pre-existing works, they outline three different ways for constructing Gaussian vector fields (GVFs) on manifolds: Projected GVFs, Coordinate-frame-based GVFs and Hodge GVFs. They perform inference with this model by optimizing a variational objective.

### Strengths
1. I think this work is quite a natural and well-motivated extension of recent works on GPs on Manifolds. I find the perspective of defining hidden layer outputs as a residual(deviation from identity maps) to be quite ingenious since it leads to natural generalization to manifolds. As far as I know, this is a novel contribution.

2. I think the paper is quite well-written and very clear in its presentation.

### Weaknesses
My main concern is that I found the experimental results to be a bit mixed, some of the choices to be a bit confusing and the main claim of the paper(in 015 "Our models significantly improve performance in these settings ...")  to be not fully validated:
1. The choice of GVF across the experiments seems a bit ad-hoc. It's understandable that the Hodge GVF can only be used when the eigenfunctions of the Laplacian are known but 4.2 uses coordinate-based GVF and 4.4 uses projected gvf. This choice seems arbitrary and it would have been nice to see both the gvfs across all experiments. It is unclear why a specific GVF is chosen for a particular experiment, and the lack of a systematic comparison makes it difficult to assess the relative strengths and weaknesses of each GVF in different contexts. For instance, the coordinate-based GVF might be more suitable for certain manifold structures, while the projected GVF might be better for others, but without a direct comparison, it's hard to draw any conclusions.

2. Euclidean GPs are not considered as baselines in experiments 4.2 and 4.3. Additionally, in experiment 4.1 I am a bit concerned about the fairness of the comparison. It is stated that "we match the number of optimized parameters between models as closely as possible". I am not sure what this means and it would have been nice to make this concrete by having plots of wall-clock times for optimization of the different GPs or something similar. In experiment 4.4 euclidean GPs outperform the manifold variants by a margin. Additionally in experiment 4.1 while Figure 3 paints a flattering picture of the method proposed by the authors, figure 8 seems to paint quite a different picture. The baseline either matches (or outperforms?, It is hard to tell just from the image) the Hodge GVF in terms of MSE. Also, the trend looks like with additional layers deep Euclidean GPs would outperform all the manifold GP variants. As it stands I am not convinced that Residual Deep Gaussian Processes consistently outperform Euclidean Deep Gaussian Processes.

### Questions
See weaknesses

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors proposed practical deep Gaussian process models on Riemannian manifolds by leveraging Gaussian vector fields and manifold-specific operations. Specifically, the proposed interdomain variables-based residual deep Gaussian processes show considerable improvement over the baseline for manifold data. Additionally, this approach can significantly accelerate inference (~2x) for Euclidean data while maintaining comparable performance. The claims made by the authors are well-supported by both rigorous theoretical development and extensive experimental validation.

### Strengths
* The paper is well-written and easy to follow

* The theoretical development is novel and solid

* The experiments are well-designed and thorough, starting from synthetic manifold data, progressing to real-world climate examples, with additional analyses of Euclidean data

* The appendix provides informative supplementary experiments that enhance understanding of the details

### Weaknesses
 * The paper is technically dense and may be challenging for readers unfamiliar with Riemannian geometry. It would be helpful if the authors could provide a more detailed background on Gaussian processes in Riemannian geometry in the appendix. For practical use, I also encourage the authors to consider releasing the code for public use in the future

### Questions
See the weakness

### Soundness
4

### Presentation
3

### Contribution
4
