# RetroBridge: Modeling Retrosynthesis with Markov Bridges

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8

## Abstract
Retrosynthesis planning is a fundamental challenge in chemistry which aims at designing multi-step reaction pathways from commercially available starting materials to a target molecule.
Each step in multi-step retrosynthesis planning requires accurate prediction of possible precursor molecules given the target molecule and confidence estimates to guide heuristic search algorithms.
We model single-step retrosynthesis as a distribution learning problem in a discrete state space.
First, we introduce the Markov Bridge Model, a generative framework aimed to approximate the dependency between two intractable discrete distributions accessible via a finite sample of coupled data points.
Our framework is based on the concept of a Markov bridge, a Markov process pinned at its endpoints. Unlike diffusion-based methods, our Markov Bridge Model does not need a tractable noise distribution as a sampling proxy and directly operates on the input product molecules as samples from the intractable prior distribution.
We then address the retrosynthesis planning problem with our novel framework and introduce RetroBridge, a template-free retrosynthesis modeling approach that achieves state-of-the-art results on standard evaluation benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a novel single-step retrosynthesis method called RetroBridge, utilizing the Markov Bridge Model. RetroBridge formulates the reactants and products in single-step retrosynthesis as two discrete distributions and learns the dependencies between them. By performing conditional sampling, the generated reactions demonstrate high accuracy.

### Strengths
1. To the best of my knowledge, this paper is the first to introduce the concept of the single-step retrosynthesis problem by framing it as a distribution fitting task, akin to a diffusion model.
2. The proposed model achieves the SOTA Top k accuracy (k > 3) on USPTO-50K.
3. The comparison with diffusion model makes a perfect sense.

### Weaknesses
1. The top 1 accuracy achieved on the USPTO-50K dataset is relatively low, and a similar trend is observed in the forward prediction task. It would be helpful if the authors could provide an explanation for these results.
2. Some baseline methods are missing, which may perform much better than RetroBridge, like DualTF, RSMILES, PMSR, etc.
3. In comparison to other TF methods, RetroBridge requires atom-to-atom mappings, which could potentially pose limitations on its feasibility. This constraint could become a hindrance when applying RetroBridge to larger datasets such as USPTO-Full.

### Questions
This paper provides a fresh perspective on AI for retrosynthesis; however, it could benefit from further elaboration on the chemical aspects involved. Some previous works, like GraphRetro and MEGAN somehow, mimic the process of chemical reactions. So, how Markov bridge formulates chemical reactions? I would consider raising my rating if the authors addressed my concerns.

### Soundness
3 good

### Presentation
2 fair

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
The authors introduce a novel approach to retrosynthesis planning by modeling it as a distribution learning problem in a discrete state space. The core of this approach is the Markov Bridge Model, which is a generative framework designed to approximate the relationship between two discrete distributions that are intractable. By optimizing a variational lower bound, similar to that in diffusion models, the method learns a Markov process that transitions between the product and reactant distributions. Empirical results suggest that the proposed method surpasses existing ones, achieving state-of-the-art results on standard benchmarks.

### Strengths
- The paper offers a novel perspective on retrosynthesis planning, framing it as a distribution learning problem on a discrete distribution instead of a discriminative learning problem. The introduction of the Markov Bridge Model in this context and its comparison with the diffusion model is novel and interesting.
- The presentation of the methodology is clearly written and easy to follow.
- The derivation of the variational objective, which involves maximizing a lower bound of log-likelihood, is theoretically sound.
- The empirical result is competitive against existing one-step retrosynthesis models.
- The proposed method is general and can potentially be extended to other application domains involving the learning of transitions between discrete distributions.

### Weaknesses
 - The paper does not discuss the time required during training and inference stage of the proposed method, including the time step T, the number of samples needed to converge on the top-k prediction, etc.
- From the atom/bond level parametrization in Section 3.2, it seems that the required T could be quite large. An ablation study to report the top-k performance vs. different Ts could be very useful.

### Questions
- How much more time is needed during the training and inference phase compared with the baselines?
- What's the choice of T in the experiments, and how many samples are needed to obtain the results?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a retrosynthesis model where the reactant is diffused to product, inducing a Markov Bridge. The method is simple and gets state-of-the-art performance.

### Strengths
- The presentation of the paper is clean, and the paper is easy to read and understand.
- The method is principled and simple, and seems to work well. The idea of flowing product to reactant is very sensible.

### Weaknesses
 - The method is incremental: the diffusion is directly from Austin, and I think the loss function is also only a variant of diffusion losses. The network is directly from literature. There is no chemical inductive biases that I can identify.
- The performance is opened up somewhat, but not sufficiently. I like the ablations that show the context and VLB help, but these are generally known from diffusion literature already. It would have been good to try to expose why the performance is better than MEGAN. For instance, how much of the results are from network tuning or training tricks?
- There are many missing competing methods, such as RetroFormer and Graph2Smiles.

### Questions
- The paper misses quite a lot of related works. Retroformer, Graph2Smiles, GTA, Tied transformer all seem to be missing. The paper needs to cite methods from 2022 and 2023, and include USPTO benchmark comparisons.
- If you pin the outcome to y in eq 2, why does fig1 show that we start from x, and diverge into a bunch of y’s? Shouldn’t fig1 show starting from single x, fanning out, and reducing all mask down to single y?
- What does t ~ U(0,…,T-1) mean in eq 7? Seems very odd… Why doesn’t it go to the end T? Why do we have multiple values?
- What happens to the last timestep in eq 7? This seems to be a Dirac, which probably poses problems. Currently it seems that the final prediction is never evaluated, and we only predict until z_{T-1} instead of matching the final z_T to y. How do you evaluate the final prediction z_T?
- What is p(z|x,y)?
- What is p(z_t+1 | z_0, z_T)? Where does this go? Why do we talk about this? Does this have something do with p(zt | z0, y)?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses single-step retrosynthesis.
The single-step retrosynthesis is formalized as the mapping problem from product molecule graphs to reactant molecule graphs.
The authors propose the Markov Bridge Model, which learns the dependency between two discrete variables, and the model is applied to the graph mapping problem.
The proposed method outperforms state-of-the-art template-free methods on the USPTO-50K benchmark.

### Strengths
* The Markov Bridge Model is a novel and interesting approach for discrete variables and can be applied to other fields.
* The evaluation results using top-k round-trip coverage and accuracy support the potential of the proposed method.
* The future work described in Section 5 clearly describes the limitations of this work.

### Weaknesses
 * The reason for selecting graph-based representation needs to be explained.  It is not clear to me why molecules are represented as a graph instead of the 3D coordinates of atoms since 3D coordinates are frequently used in the unconditional generation of molecules  (Hoogeboom et al., 2022).


### Questions
No question.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
