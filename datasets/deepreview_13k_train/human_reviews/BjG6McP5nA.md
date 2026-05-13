# Improving Gradient-guided Nested Sampling for Posterior Inference

- Decision: Reject
- Scores: 8, 5, 5, 6, 8, 6

## Abstract
We present a performant, general-purpose gradient-guided nested sampling algorithm, \algoname, combining the state of the art in differentiable programming, Hamiltonian slice sampling, clustering, mode separation, dynamic nested sampling, and parallelization. This unique combination allows \algoname to scale well with dimensionality and perform competitively on a variety of synthetic and real-world problems.
    We also show the potential of combining nested sampling with generative flow networks to obtain large amounts of high-quality samples from the posterior distribution. This combination leads to faster mode discovery and more accurate estimates of the partition function.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a new nested sampling algorithm which
through a pruning method and adaptive step size results in
asymptotically fewer likelihood evaluations compared to the
current state of the art. Experiments show that the method
in addition to being more computational efficient yields
higher quality samples as compared to popular libraries
doing the same thing

### Strengths
This is highly original work that makes a significant contribution
to the literature on nested sampling. The method has compelling experiments
to support it, and the underlying techniques are reasonably well-explained.

### Weaknesses
As the paper includes many contributions, it would have been nice to see
an ablation study showing how each of the contributions work to improve
the nested sampler. Additionally, some contributions like Mode Collapse
Mitigation only have supporting evidence in the appendix. It would be nice
if some of those figures could be in the main paper.

An additional concern I have relates to the main claim that the sampler
only need O(1) bounces. I saw no proofs or even intuition for why this is
the case. For something so core to the paper, it would greatly improve the
paper if even some intuition was provided for why that might be the case.

Minor Issues:

There are a few typoes and misspellings that should be fixed.

### Questions
What suggests only O(1) bounces are needed?
Would it be possible to do an ablation study?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a general-purpose gradient-guided nested sampling algorithm, GGNS, combining the state of the art in differentiable programming, Hamiltonian slice sampling, clustering, mode separation, dynamic nested sampling, and parallelization.  The authors show that the combination leads to faster mode discovery and more accurate estimates of the partition function.

### Strengths
The authors present a comprehensive review of related works.

### Weaknesses
1. The main contribution of the paper is a combination of different existing methods. The paper lacks originality and significance.

3. The reviewer cannot find the proposed GGNS  algorithm. The authors need to give a concrete GGNS  algorithm.

2. There is no theoretical analysis regarding the GGNS. There is no theoretical guarantee for the advantages of the GGNS algorithm.

4. Since the method is a combination of different strategies, the authors need to conduct an abolition study on the strategies to validate their effectiveness.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a way to effectively combine Hamiltonian slice sampling with nested sampling.

### Strengths
* Nested sampling is a widely used algorithm for model comparison in physics. Therefore, improving the scalability of nested sampling to higher dimensions is an important problem.
* The paper provides a guideline on how to implement Hamiltonian slice sampling with nested sampling. It is well known that MCMC algorithms are very sensitive to such implementation detail. Therefore, this paper tackles a worthwhile issue.

### Weaknesses
While the paper discussed how to implementat nested sampling, the exact details of the implementations are not self-contained within the paper. Therefore, it is difficult to actually grasp *how* the paper is proposing to implement these parts. I expect a paper of this type to be self-contained in terms of details. While the authors do provide code, (note that the reviewers are not expected to look at the supplementary material) the paper should explain the algorithmic details, provide insight, and contrast with previous implementations. The paper mostly relies on textual explanation, which lacks the required technical preciseness. Below are some specific examples:

* Section 3 "Adaptive Time Step Control": "This time step is adjusted dynamically ... increase or decrease ..." How is it adjusted exactly?
* Section 3 "Trajectory Preservation": What is exactly a "trajectory" here? It is the states of the Markov chain after multiple Markov chain transitions? Or the intermediate states of a Hamiltonian trajectory as in recycled MCMC methods [1]?
* Section 3 "Trajectory preservation": "select a new live point at random from the stored trajectories" how random? Uniformly at random? Or weighted resampling as in typical Hamiltonian Monte Carlo implementations [2,3]?
* Section 3 "Pruning Mechanism": "This mechanism significantly improves the computational efficiency" How/why does it improve the computational efficiency exactly?
* Section 3 "Differentiable Programming": How is differentiable programming used here? Why does it help?

Furthermore, for quantatitive/theoretical claims, quantatitive/theoretical evidence (rigorous if possible) is necessary. There are multiple claims that were not entirely obvious to me:

* Section 3 second paragraph: "the fact that gradients guide the path means one no longer requires $n_{\text{live}} \sim O(d)$": I'm not sure if this is obvious. Is there a proof for this statement?
* Section 3 "Mode Collapse Mitigation": "... preventing them from converging prematurely to a single model": Is there theoretical/empirical evidence for this? 
* Section 3 "Robust Termination Criterion": "terminate ... has decreased by a predetermined fraction from its maximum value": What is the theoretical principle behind this termination criterion?
* Section 6: "gradient-guided nested sampling ... makes use of the power of ... parallelization for significant speed improvements": I couldn't find any empirical evidence on much this method takes advantage of parallelization. Did the authors measure the strong scaling of this method? Until how many cores does this scale? What is the efficiency? 

Lastly, I found the experiments inconclusive both in terms of experimental design and the choice of baselines.
* The paper claims that "the ingredients in GGNS ... to significantly improve its performance in high-dimensional settings ..." but none of the experiments are necessarily high-dimensional in todays standard. For instance the synthetic experiments in Section 4.1 Figure 1 only go as high as 128. See [4] Section 4.5 where the dimensionality goes as high as tens of thousands. While the method could be said to be scalable among nested sampling algorithms only, one could then question the significance of making nested sampling more scalable where more scalable alternatives exist.
* The exact contribution of each design choices in Section 3 are not evaluated independently. Therefore, it is unclear how much each of the components are contributing to any performance improvement. Given that no theoretical evidence is provided, I would expect a thorough empirical analysis and motivations for the design decisions. A great example of this is the no-u-turn sampler paper [5], which provided two innovations: tuning the trajectory length and the stepsize. They provide separate evaluation for each: Figure 3,4 for tuning the stepsize and Figure 5 for the trajectory length.
* Furthermore, some of the baselines are unclear. In Section 4.2, the paper states that HMC was used as a baseline. But HMC alone does not produce an estimate for the log-evidence unless special tricks are used like the harmonic mean estimator or Chib's method. How was HMC used to produce a log-evidence exactly? Similarly, the paper cites Halton (1962) for sequential Monte Carlo, but this paper seems unrelated to the sequential Monte Carlo used for estimating log-evidences as in [6]. Was this the intended citation? People usually attribute the genesis of sequential Monte Carlo to the bootstrap particle sampler [7] or the later seminal works [8,9]. 
* Moreover, the baselines are insufficient to really judge the performance of the method. At least in statistics, log-evidence estimation is popularly done using thermodynamic integration or bridge sampling [10]. Also, if the authors did intend to compare against sequential Monte Carlo as in [6], more implementation details are needed to really judge its validity, since SMC is notable for being sensitive to implementation details.
* It is also curious why the authors did not use the same set of baselines for all problems. For instance, comparable nested sampling methods are only used in Section 4.1.

### Questions
* Figure 3 why are the error bars decreasing as the dimensionality increases? I would assume higher dimensions are more challenging and therefore more variance. Is it not the case? In fact, in Figure 1, which I presume is the same type of plot, the results do seem intuitive.
* Section 1 second paragraph: "From the perspective of differentiable programming, less attention has been paid in recent years" I did not quite understand the intention of this sentence. In what context does differentiable programming have something to do with sampling here?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces Gradient-Guided Nested Sampling (GGNS), a novel nested sampling algorithm that utilizes Hamiltonian Slice Sampling and gradient information for improved scalability and efficiency, especially in high-dimensional settings. By leveraging differentiable programming frameworks and parallelization, GGNS achieves significant speed advancements, overcoming the dimensionality dependence that hampers previous methods. The paper also demonstrates GGNS's ability to integrate with generative flow networks for effective sampling from complex posterior distributions.

### Strengths
The paper is well structured and presents comprehensive experiments that highlight the merits of the proposed method. Notably, the method exhibits linear scaling with dimensionality, a feature not evident in prior techniques. Moreover, it outperforms existing approaches on several benchmark posterior sampling datasets. Furthermore, the authors present the idea clearly with the help of good visualizations.

### Weaknesses
My primary concern with the paper is the lack of clarity regarding the proposed method. While the contributions section seems to align with the methods, it primarily outlines algorithmic tweaks to existing methods. These minor modifications collectively seem to yield an impact. However, the paper does not showcase the final algorithm that encapsulates these changes; I only found references to current algorithms in the appendix. This absence of a clear differentiation in algorithmic terms hinders my ability to give a higher score, even though the experiments are commendable. Additionally, I found section 5 ambiguous, especially concerning the objectives of the experiments outlined there. Specifically, it is unclear how the proposed method improves the training of the drift in the context of generative flow networks. The paper does not provide a baseline comparison to demonstrate the advantage gained by using the proposed method for this specific application. Furthermore, the explanation of GPU interoperability is not sufficiently detailed. It is not clear what specific aspects of GPU functionality are being leveraged beyond standard parallelization. Finally, the observation that error bars reduce with increasing dimensionality in Figure 3 is counterintuitive and lacks a clear explanation in the main text.

### Questions
-	I didn’t understand what was the advantage of the method for section 5, it seems a nice application that you can apply to generative flow networks, but what have we gained in training of the drift with your method, is there a baseline we can compare your method against?
-	Page 5 at the top there is some overlapping text below Figure 1. 
-	I don’t really understand how you took advantage of ‘GPU interoperability’?  
-	I don’t quite understand why there error bars reduce with the number of dimensions in Figure 3.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper the authors propose a new nested sampling algorithm based on Hamiltonian slice sampling. Their sampling method removes the linear dependence of the number of live points on dimensionality. They show that their algorithm runs significantly faster using parallelization in state-of-the-art programming frameworks. Empirically they show that their algorithm can scale up to higher dimensional problems compared to prior work. In addition, they show potential integration into the generative flow networks.

### Strengths
I think it is an interesting and novel idea that they combine the learning-based samplers with nested sampling algorithms. In this sense this paper is well motivated. The paper is also clearly written and the math derivations are sound, to my best knowledge. They also provide comprehensive evaluations on various tasks and show that their sampling algorithm can scale to higher-dimensional problems.

### Weaknesses
1. In the introduction section, the authors list 4 differences from prior work. Conceptually I am bit confused about how each of these 4 parts work with each other. I would hope that the authors can elaborate a bit.

2. A minor formatting issue: the caption of Figure 1 got cluttered and needs to be fixed later.

### Questions
Please see my questions in the previous section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes GGNS, a performant, general-purpose gradient-guided nested sampling algorithm that scales well with dimensionality and demonstrates competitively on a range of synthetic and real-world problems. In particular, the gradients calculated with differentiable programming are combined with HSS to propose new points, dynamic nested sampling is used for parallelization, a new termination criterion and cluster identification are also proposed. Furthermore, the authors show the potential of combining nested sampling with generative flow networks, leading to faster mode discovery and convergence of evidence estimates compared with GFlowNets.

### Strengths
GGNS enables the use of gradient information through the differentiable programming frameworks. 
Empirically, GGNS shows the best linear scaling and performs evidence estimation accurately even as the dimensionality approaches the number of live points. 
The proposed method adds practical value in the nested sampling community. 
The combination of GGNS with GFlowNets opens the door to a number of interesting future research.

### Weaknesses
Novelty is limited to a combination of existing methods. 
The proposal of using gradients in guiding the choice of new live points can be elaborated more in the Contribution section. Specifically, the mechanism by which gradients are used to propose new points is not fully clear, and the potential limitations of this approach, such as getting stuck in local optima, are not discussed. It would be beneficial to see a more detailed explanation of how the gradient information is incorporated into the sampling process and how this addresses the challenges of high-dimensional sampling. 
Experiments are almost all synthetic, and some results do not seem to be better than GFlowNets. The lack of real-world experiments limits the assessment of the practical applicability of the proposed method. Furthermore, the comparison with GFlowNets in the 'Many Wells' experiment does not clearly demonstrate a significant advantage for GGNS, and it would be helpful to see a more thorough analysis of the performance differences.

### Questions
In Figure 1, instead of plotting the error in the estimate of log Z versus the number of dimensions, how does the error grow versus the number of likelihood evaluations? 

In Figure 1, the error bar (i.e., standard deviation across 10 runs) are much bigger for GGNS compared with the baselines, does it mean it is trading off variance for bias? 

Table 1, all methods except GGNS are under-biased for the Gaussian mixture example, is it just by chance? 

In the 'Many Wells' experiment (Figure 4), are you comparing against FAB or FAB with buffer (which should give better results than FAB)? 

Minor:
Formatting under Figure 1 needs to be modified. 
page 7, "due to the high its high dimensionality" -> "due to its high dimensionality"

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
