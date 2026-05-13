# Novelty Unlocking with Multiobjective Generative Models: Batch Diversity of Human Motions

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
Current generative models have shown potential performance in many tasks, which typically focus on generating samples that closely adhere to a given distribution, often overlooking the requirement to produce optimal diverse solutions in a batch diversity.
Recognizing that maintaining ``diversity" has been a longstanding challenge in multiobjective optimization, we were inspired to introduce a multiobjective optimization approach to enhance diversity in a single pass.
This paper utilizes the in-betweening human motion generation task as an example and introduces the multiobjective generative models to demonstrate the effectiveness of the proposed method in producing diverse and smooth human motion sequences. The resulting method, termed the \textit{Multiobjective Generation Framework with In-Betweening Motion Model} (MGF-IMM), frames the human motion in-betweening task as a bi-objective optimization problem. The designed in-betweening motion model is then integrated into a nondominated sorting-based optimization framework to address this bi-objective optimization problem.
Through comprehensive qualitative and quantitative experiments, MGF-IMM has demonstrated state-of-the-art performance, surpassing the latest methods and validating its superiority in generating diverse in-betweening human motions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
Authors propose a multi-objective framework for the human motion in-betweening task. More specifically, they introduce a bi-objective optimization problem; optimizing the diversity and smoothness of transitions between keyframes and generated motions. The proposed optimization framework is applied on top of a pretrained generative model to produce the final diverse completed motions.

### Strengths
* The problem of diversity in human motion generation/completion is an important problem. One of the major limitations of most generative models developed for the in-betweening task, is the lack of diversity due to overfitting.
* Paper is well-structured and easy to read.
* The experiment section contains most of the important in-betweening baselines.

### Weaknesses
 * My main concern with this work is the substance of the paper. To me, it primarily appears that the proposed framework suggests iteratively sampling from a pretrained generative model, rejecting samples that lack sufficient smoothness while ensuring diversity among the generated samples. The only substantial contribution seems to be the definition of a bi-objective function to balance both diversity and smoothness. However, I am not entirely convinced that this specific framing is necessary; simply rejecting samples based on smoothness and applying a diversity metric across the entire sample set might have been equally effective.

* While I appreciate the authors' thorough investigation of related work and relevant baselines, some recent in-betweening studies are missing from the discussion and experiments sections. For example, CondMDI (Cohan et al., 2024) and OmniControl (Xie et al., 2023) are notable recent works that should be considered.

* The effectiveness of the proposed method relies heavily on the performance of the underlying generative model. If the backbone generative model has limited diversity, the iterative framework is unlikely to significantly enhance diversity.

### Questions
1. I am having trouble understanding the diversity component as defined in Equation 2. Isn't $C(Y)$ a single value between $0$ and $D-1$ and $P_c(Y)$ the probability of Y belonging to class $c$? Can you elaborate on how this definition ensures diversity?

2. Can you explain how your model differs from simple rejection sampling, where $N$ motion sequences are iteratively generated and the $M<N$ sequences with the highest diversity (using any heuristic or method, such as pairwise distance maximization) are retained? Then, samples below a certain smoothness threshold are rejected, and this cycle repeats until $N$ samples are obtained.

3. I believe it would be beneficial to compare the proposed method with straightforward rejection-based sampling approaches to highlight the unique advantages of your method.

4. I highly recommend that the authors include recent relevant diffusion works of CondMDI (Cohan et al., 2024) and OmniControl (Xie et al., 2023) in the related work section (Section 2.2).

5. As with any iterative or rejection-based method, inference time is a key consideration. What is the inference time with this method? How does it compare with SOTA methods?

6. What is the data representation used here? Is it global joint positions? How are the keyframes defined?

7. I am curious to know the details of the backbone generative models used in this work. Particularly, how they condition on keyframes. I think these details need to be added to the supplementary material.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
A method is presented for generating batches of diverse examples for motion in-between problems, via generative modeling,
i.e., a VAE, GAN, or DDPM model.  Thus given two motion sequences A and B, the goal is to be able to generate diverse sequences 
(possibly of varying length) that connect the end of A to the start of B. This is formulated as a multiobjective optimization problem,
whereby a population of samples is repeatedly adapted to capture the pareto front of this optimization.
Key to the method is a classifier C(Y) that can categorize the motion-type of a motion Y into one of D distinct categories.
The multiobjective optimization is defined in a 2D space defined by two functions, F1(Y) = alpha1(Y) + Beta(Y) 
and F2(Y) = (1-alpha1(Y)) + Beta(Y).
Alpha1(Y) maps the most-likely class evenly along the interval [0,1], (plus an epsilon that is related to the likelihood of that class).
Beta(Y) defines a smoothness loss.  Points along the pareto front thus seek to maximize class diversity, as well as being as
smooth as possible.  Diverse samples are generated by iteratively calling the generative network, each time conditioning
the network on the motions to be connected, e.g., A and B as above, and the already-generated samples, Y_i.
A memory-augmented Transformer-based architecture is used as the encoder for a conditional VAE, to generate new samples.
The results also present GAN and DDPM generative results.

The method is trained and tested on 4 different motion datasets (BABEL, HAct12, NTU, GRAB) and evaluated
based on FID and a diversity metric (APD), and two others (ACC, ADE).
The method produced the best results for FID and diversity, particularly for the DDPM version.
In addition to the quantitative results, qualitative results are provided using a visualization of the pareto front,
and a figure that illustrates 4 diverse samples generated for 2 example problems.
No video is included.

### Strengths
- an interesting problem, i.e., maximizing diversity within a batch of samples coming from a generative motion model.
  The specific problem being tackled here, i.e., generating diverse ways to produce a bridging motion that connects 
two existing motion sequences is interesting, although it is quite a specific problem domain.
- Reasonablly extensive quantitative evaluations
- Potentially an interesting and novel method for achieving the diversity, although I still do not understand it all
- the applicability of this as a method to different classes of generative models is a real plus, i.e.,
  GANs, VAEs, and diffusion models.

### Weaknesses
Weaknesses:
- It is difficult to understand the given multiobjective framework. 
  As best I understand it, is described by a 2D pareto optimal front, as described in the summary I've given above.
  In particular, the intuition of equation should be described. Figures and diagrams would really help the exposition.
  The specific motivation and geometric intuition for alpha1(Y) could be explained, and how it encourages diversity.
  This reader spent was stuck on equation (2) for a long amount of time.
- The multi-class classifier C(Y) is key to the method, but is not described in detail in the results and experiments,
  unless I missed it. This leaves the reader confused about the intent of this classifier, and its importance.
- There are no video results, unless I missed it as supplemental material (I did check OpenReview twice for this).
  This makes it really difficult to judge the quality and diversity of the output in practice.
- A variety of things about the method that were difficult for this reader to understand -- see questions below.

Minor comments:
- The structure of the paper was challenging for this reader.  Leading with Figure 3, then Figure 2, and then Figure 1
  is an alternate order that makes more sense to this reader.
- L047: "batch diversity" is ambiguous, i.e., it could mean intra-batch or inter-batch diversity.
- the notation of "decision variables" comes as a surprise.  Perhaps it is standard in multiobjective optimization,
  but it is worthwhile motivating in the current context.  Is it simpler to be thinking in terms of "samples"
  and "sample space"?
- the Pareto Dominance math is more intuitive when helped by a related figure
- related works on animation and pareto-frontiers:
   "Sampling of Pareto-Optimal Trajectories using Progressive Objective Evaluation in Multi-Objective Motion Planning"
   "Diverse motion variations for physics-based character animation"
- "in-betweenning" should probably be "in-betweening"
- eqn (4):  the addition of beta(Y) here seems like a bit of a hack.  
  It would also be nice to more generally understand why the smoothness component is needed, i.e., why can't the
  conditional generative model capture this?  Also, Beta(Y) in eqn (3) appears to be a vector, whereas in eqn(4) it is scalar.
  Which is it?
- "the generative model is prompted":  in the age of LLMs, this is an overloaded (and therefore ambiguous) phrasing,
  as there are no LLMs involved.
- L378: "Action Accuracy (ACC), Action Accuracy (ACC)" (sic)
- Figure 4: labeling the default locations of the D classification categories would help interpret the pareto-front figure
- Figure 5: It is difficult to interpret whether to read the figure on the left, from left-to-right or right-to-left

### Questions
Questions:
- Q1: What is a "Hamilton" distance?  Do you mean Hamiltonian distance or Hamming distance?
  A web search produced no results for this concept.
- Q2: Wondering why the "+P_C(Y)" term is really needed, i.e., does it add value? 
  The addition to the classification category number is quite strange, given that they represent different things.
- Q3: how do FID_tr and FID_te differ?
- Q4: It is still unclear how the variable-length motions are encoded and sampled.
- Q5: It is not clear how the generative model is conditioned on the previously-generated samples.
  Does this happen implicitly via the memory/GRU? If so, how is the GRU update trained so as to be incentivized
  to make the next sample highly-diverse with respect to previous samples?  This reader is very confused on this point.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the problem of generating diverse in-between motions by formulating it as a multi-objective optimization problem. The proposed Multiobjective Generation Framework with In-Betweening Motion Model introduces an evolutionary algorithm at the inference stage to enhance motion diversity while maintaining motion quality.

### Strengths
The authors' formulation of the diverse motion generation problem as a multi-objective optimization problem is novel. The derived general generative framework effectively guides the sampling process towards diverse motions, successfully balancing diversity and quality in generated in-betweening human motion sequences.

### Weaknesses
Conditional diffusion models, such as those presented in [1] seem to solve the same problem using generative models with conditional diffusion. By changing the conditions, they can also generate diverse motions. It would be helpful if the authors could compare their approach to these methods or explain why the multiobjective formulation is necessary, and whether it can be further combined with conditional motion generators. Moreover, a discussion over the difference and advantage in terms of formulation compared with [1] would enhance the quality of the paper. 

Specifically, the paper lacks a detailed analysis of how the proposed evolutionary algorithm (EA) compares with simpler sampling strategies, such as ancestral sampling or rejection sampling, which are commonly used with diffusion models. The authors should provide a more thorough justification for the use of an EA, given its computational cost, and demonstrate its superiority over these baseline sampling methods in terms of both diversity and quality of the generated motions. The current analysis does not sufficiently address the trade-offs between computational cost and the benefits of using the EA.

### Questions
1. **Computational Overhead of the Evolutionary Algorithm:** EA will introduce extra computational cost during inference time, especially when using expensive diffusion models. Could the authors elaborate on what the computational overhead is compared with a stand-alone generative model?
    

2. **Comparison with Conditional Generative Models:** Given the classifier that the authors trained, one might imagine training a conditional generative model based on the classifier. Could the authors explain why using an EA would be better than training a motion-class-conditioned generative model?

### Soundness
3

### Presentation
3

### Contribution
3
