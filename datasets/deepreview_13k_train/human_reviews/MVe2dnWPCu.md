# A Probabilistic Framework for Modular Continual Learning

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
Modular approaches that 
use a different composition of modules for each problem 
are a promising direction in continual learning (CL). However, searching through the large, discrete space of  module compositions is challenging, especially because evaluating a composition's performance requires a round of neural network training. We address this challenge through a modular CL framework, \PICLE, that 
uses a probabilistic model to cheaply compute the fitness of each composition, allowing \PICLE\ to achieve both perceptual, few-shot and latent transfer. The model combines prior knowledge about good module compositions with dataset-specific information.
We evaluate \PICLE using two benchmark suites designed to assess different desiderata of CL techniques. 
Comparing to a wide range of approaches, we show that \PICLE is the first modular CL algorithm to achieve perceptual, few-shot and latent transfer while scaling well to large search spaces, 
outperforming previous state-of-the-art modular CL approaches on long problem sequences.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the modular continual learning setting.  They introduce a probabilistic model to determine a distribution over paths for perceptual transfer.  This can be interpreted as selecting modules based on how similar the current features at that layer are to the modules' input distribution.  For latent transfer, they have a probabalistic model based on the idea that suffixes similar in L2 distance should have similar performance.  This modeling allows predicting the validation performance of a path without training.  Due to the modeling, they only need to evaluate a number of paths which grows linearly with the depth L.  Their method outperforms the other methods marginally on average, while in some cases demonstrating significant boosts, e.g. few-shot transfer.

### Strengths
* The probabalistic models introduced are simple and make sense.  Using such modeling to avoid the expensive counterfactual of evaluating a path is a logical approach.
* The paper is well written and I found the appendix helpful.
* The evaluations seem consistent with prior works

### Weaknesses
 * The quantitative advantage over MNTDP-D in accuracy is marginal on average ~1-3%
* The method requires slightly more FLOPs than MNTDP-D (Figure 3 (a))

### Questions
**Table 1:** Why are the numbers for MNTDP-D and PICL forward transfer so similar?

Typo: “The CL algorithm should be able to ”remember” previous problems“ (backwards quotation) 

**Algorithm 3:** Bold lambda on right side of line 5

“This search results in the most relevant previous solution $\pi'$. Finally, in lines 11-14, we evaluate NT paths created by transferring a different number of the last $\ell \in \\{\ell_{min} + 1, ..., L − 1\\}$ layers of $\pi'$, to see if re-using more layers leads to further improvement”. (do you mean $\ell \in \\{2, \ldots L - 1\\}$?  That's what the code appears to be searching over

### Soundness
3 good

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
This paper introduces PICLE, a scalable modular continual learning algorithm that addresses key challenges in the field. PICLE is task-aware and optimizes for different types of transfer learning, such as perceptual, few-shot, and latent transfer. Utilizing a probabilistic search method, it efficiently approximates the fitness of different module compositions, significantly reducing training requirements. The algorithm outperforms existing state-of-the-art solutions, demonstrating its efficacy on the popular CTrL benchmark suite and a new extension called BELL.

### Strengths
1. Modularity in continual learning is highly promising, offering a good balance between scalability and the ability to transfer knowledge across tasks without undue interference.
  
2. The key challenge in modular approaches is the exponentially increasing search space for module combinations, particularly as the number of layers grows. PICLE addresses this scalability issue effectively, allowing for both perceptual and latent transfer, which makes it a standout in the field.
  
3. The paper's empirical study is both comprehensive and well-executed, adding robustness to its claims.

### Weaknesses
Minor weaknesses, if addressed during the rebuttal, I will keep my score at an 8:

1. The table in the paper lacks uncertainty metrics such as standard deviation. This omission should be addressed to enhance the study's reliability. Additionally, for readability purposes, it would be better to show the percentages only up to three digits instead of four (e.g., XX.XX% should be changed to XX.X%).

2. The paper should clearly state that the PICLE method is task-aware, which is an important limitation. Ideally, there would be a column in Table 4 that discusses task-agnosticism, a feature that another algorithm, LMC, is capable of.

3. The concept of using a generative model to approximate latent activations and assume local independence from one layer to the next, as introduced in Section 4, was initially proposed in the LMC paper. The authors should give credit to this paper and clarify how their methods differ from those originally proposed in the LMC paper.

### Questions
None

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The work proposes a probabilistic modeling approach to efficiently search for the best-fit module composition out of the large discrete space of possible compositions of the modules in continual learning. Depending upon the similarity of the input distributions with that of a previous problem, two variants of the probabilistic model have been proposed: one for perceptual transfer where the prior uses the original accuracy of pre-trained modules to order these, and the other for latent transfer where the prior specifies that pre-trained modules in a path have been used together to solve a previous problem.

### Strengths
- Good motivation, presentation, and writing. The equations have been explained well.
- The idea of using the validation accuracy for a path as the proxy for its fitness is simple and elegant.
- The limitations of the proposed method have been elaborated well.
- The reported evaluation metrics are rigorous.

### Weaknesses
 - On page 3, the authors mention their strategy is based on a generative model of the input x. How is the generative quality of the proposed method quantitatively? Some further evaluation of the proposed method using metrics like ECE can thus be more insightful.

- While I am not very familiar with the up-to-date modular continual learning literature, the baselines in Tables 1-2 look classic to me. Can the authors comment on comparing with more recent works?

- Can the authors compare the computational overhead of their method against the baselines?

### Questions
- On page 3, the authors mention their strategy is based on a generative model of the input x. How is the generative quality of the proposed method quantitatively? Some further evaluation of the proposed method using metrics like ECE can thus be more insightful.

- While I am not very familiar with the up-to-date modular continual learning literature, the baselines in Tables 1-2 look classic to me. Can the authors comment on comparing with more recent works?

- Can the authors compare the computational overhead of their method against the baselines?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose PICLE a probabilistic approach to spawn, compose and train a series of neural modules for solving continual and transfer learning tasks with compositionality. The proposed method considers two separate scenarios:  perceptual transfer, where the input space is the same for all tasks and the output function has to be adapted; and latent transfer, where the output functions have to be reused on new input spaces. For the first scenario, the authors approximate the input distribution of each module with the combination of a low-rank gaussian distribution and the accuracy as the prior. The final path is found by greedy search. For the second scenario, the authors use Bayesian optimization and a Gaussian process to approximate the accuracy of unseen module combinations. One of the main advantages of the proposed approach is that it scales with respect to the number of tasks sinc it evaluates a constant number of compositions and trains a network with a fixed size for each task. The proposed approach achieves state of the art perfomance on CTrL as well as on a new compositional version of CTrL named BELL by the authors.

### Strengths
Originality
=======
* The probabilistic modular framework proposed in this work is novel to the best of my knowledge.
* The authors introduce BELL, a new compositional version of CTrL along with this work.

Quality
=====
* The proposed approach is sound.
* The low-rank approximation of the input as a proxy for the likelihood is simple yet effective.
* The appendix contains details to ensure reproducibility and the authors promise to release the code.
* The authors provide Algorithms.
* The authors discuss the limitations of their approach.
* Ablations can be found in the Appendix.

Clarity
=====
* The text is well-written.
* I found Figure 3 and Table 4 very useful in order to understand the difference between PICLE and other algorithms.
* The authors provide details about hyperparameters in the Appendix.

Significance
=========
* Continual learning is a challenging problem and I believe this work is an interesting step towards a modular solution
* PICLE achieves a slight improvement on CTrL and greater improvement on some of the BELL tasks.
* BELL complements CTrL with few-shot and compositional tasks.

### Weaknesses
Originality
=======
* LMC also introduced a benchmark for compositional generalization based on colored-mnist that is not mentioned when introducing BELL.
* Moreover the authors claim not to be able to obtain acceptable results with LMC on BELL despite their best efforts, while this is possible, they could have tried to run PICLE on compositional color MNIST task introduced in LMC. This would provide a direct comparison to a relevant existing method and further contextualize the performance of PICLE.

Clarity
=====
* This work introduces a method and a benchmark, however most information about the benchmark is left in the appendix. I suggest providing simpler versions of the Algorithms in the main text, and to use the space to make the paper more self-contained (less dependent on the Appendix). Specifically, the core logic of Algorithm 1, which involves the low-rank Gaussian approximation and greedy search, could be better explained in the main text. The current presentation makes it difficult to grasp the practical implications of these steps without referring to the appendix.

Significance
=========
* There exists a vast number of continual learning benchmarks. Although they enrich the field, they also dilute the efforts of the research community. Thus I suggest the authors to include some more motivation on why BELL is needed and why researchers should use it rather than other benchmarks or tasks. The current justification for BELL is not sufficiently compelling given the existing landscape of continual learning benchmarks. A more detailed explanation of the specific limitations of existing benchmarks that BELL addresses is needed.

Minor
====
* Page 4: Accordignly
* Appendix I: pre-traiend

### Questions
* Would it be possible to run PICLE on compositional color MNIST to be able to compare with LMC (see LMC paper)? (It is ok if you do not have enough time / compute resources to do it). 
* Could you include some more motivation on why BELL is needed and why researchers should use it rather than other benchmarks or tasks.
* Why $\{\pi}^*$ is not used in Algorithm 2?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
