# Perturb and Learn: Energy-Based Modelling in Discrete Spaces without MCMC

- Decision: Reject
- Avg Score: 5.40
- Scores: 5, 6, 3, 5, 8

## Abstract
Energy-based models (EBMs) offer a flexible framework for probabilistic modelling across various data domains. However, training EBMs on discrete data poses significant challenges, primarily due to the intricacies of sampling in such spaces. In this work, we propose to train discrete EBMs with Energy Discrepancy which only requires the evaluation of the energy function at data points and their perturbed counterparts, thus eliminating the need for demanding sampling techniques like Markov chain Monte Carlo. Energy discrepancy offers theoretical guarantees applicable to a broad class of perturbation processes, of which we investigate three types: perturbations based on Bernoulli noise, deterministic transforms, and neighbourhood structures. We estimate the energy discrepancy loss effectively using importance sampling with two types of proposal distributions: uninformed and gradient-informed. Empirically, we demonstrate the efficacy of the proposed approaches in a wide range of applications, including Ising models training, discrete density estimation, graph generation, and discrete image modelling.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This research suggests a modification to the training process of Energy-Based Models (EBMs) by using the energy discrepancy loss. The main idea is to replace EBMs' conventional negative samples with perturbed versions of the observed samples, generared by a conditional distribution $q(y∣x)$. The energy discrepancy, which has previously been used in the modeling of continuous distributions, is here extended to address discrete distributions. The paper offers several designs for the perturbation mechanism $q$, including the application of Bernoulli noise, deterministic transformations, and neighborhood structures.

### Strengths
1. The paper presents its findings in a clear and structured manner, offering clear explanations of the energy discrepancy loss and provide useful insights on its connection to prior loss functions.

2. The paper focuses on the modeling of discrete distributions using Energy-Based Models (EBMs), an area that has not been extensively explored in previous research.

### Weaknesses
While the authors assert that their proposed model can provide flexibility and theoretical guarantees in the construction of negative samples without the need of MCMC sampling. After reading the paper, I still hold some doubts on whether this methods is powerful and flexible enough in modeling complex distributions. My concerns and questions are as follows:

1. Influence of the gap between KL Divergence and KL-Contraction Divergence on estimation

Equation (6) in the paper suggests that minimizing energy discrepancy loss is equivalent to minimizing KL-contraction divergence. Nevertheless, the KL-contraction divergence serves merely as a lower bound of the KL divergence, where the divergence between two transformed distributions, indicated by $q(y∣x)$, defines this bound. If we consider an extreme scenario where $q(y∣x)$ becomes (or is very close to) a deterministic identity function, then the transformed distributions may closely resemble the original distributions. Consequently, the KL-contraction could approach zero, irrespective of a potentially significant disparity between the actual data distribution and the fitted model. This raises my concern that the proposed loss term might offer a bound too lax to guide the optimization effectively toward the equivalence of $p_1$ and $p_2$.

2. Whether there can be a dilemma in selecting $q(y|x)$?

Building on my initial point, securing a tighter lower bound might necessitate a $q(y∣x)$ that significantly alters x by losing enough information. At another extreme, selecting $q(y∣x)$ that maps all samples to a normal distribution, irrespective of x (akin to infusing substantial noise as in diffusion processes), would mean the KL-contraction mirrors the original KL divergence closely. However, an excessive deviation of y from x (transforming it to what resembles random noise) could render negative samples trivially distinguishable from positive ones, potentially destabilizing the training. This seems to create a dilemma. Although in the experiments shown in the paper, the proposed simple perturbations seem to work. Given that the distributions shown in the paper are not very complex, I'm concerned about this problem in modeling more complex distributions.


3.  The Feasibility of Abandoning MCMC Sampling for Complex Distributions:

The discussion in Section 4.1 of the paper introduces an importance sampling strategy that utilizes gradient information (as shown in equation 12) to stabilize training. This approach seems to parallel a single-step gradient-based MCMC sample that 'denoises' the perturbed data (so that the negative samples become closer to true samples). I question whether such a simplified rule is viable for more convoluted distributions, or if multiple updates might be necessary to yield valid samples, essentially reverting to the conventional MCMC technique.

4. Sufficiency of Experimental Results to Substantiate the Algorithm's Effectiveness:

Reflecting upon the earlier points, the experiments demonstrated in this paper seem to be a bit easy to me. While models like the Ising Model and 2D examples can serve as sanity check examples, they might not pose a significant challenge with the current state of research. Similarly, the Ego-small dataset might lack complexity in its graph structure . Moreover, reference [1] seems to set a more robust benchmark. The MNIST dataset, used for image distribution analysis, is also relatively simplistic, and it appears the proposed model falls short of matching the performance of GWG. These factors collectively cast doubt on the proposed algorithm's performance and scalability when dealing with more sophisticated distributions.

[1] Score-based Generative Modeling of Graphs via the System of Stochastic Differential Equations.

5. More comprehensive review for EBM works: 

While the paper primarily concentrates on modeling discrete distributions, it would be beneficial to provide a more comprehensive review of the field of Energy-Based Model (EBM) training, with particular emphasis on those studies that explore sampling methods for negative samples. For example, [1] pioneering work using cnn as energy function, [2] [3] [6] are works that use different armortized methods to reduce MCMC steps, [4] uses a replay buffer and [5] moves to the latent space to facilitate sampling.

[1] "A theory of generative convnet." International Conference on Machine Learning. PMLR, 2016.

[2]  "Cooperative training of descriptor and generator networks." IEEE transactions on pattern analysis and machine intelligence 2018 

[3]  "No MCMC for me: Amortized sampling for fast and stable training of energy-based models." ICLR 2021

[4] "Improved contrastive divergence training of energy-based models." ICML 2021

[5] . "VAEBM: A Symbiosis between Variational Autoencoders and Energy-based Models" ICLR 2021

[6] "A tale of two flows: Cooperative learning of langevin flow and normalizing flow toward energy-based model." ICLR 2022

### Questions
Please check the weakness part.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper generalizes the energy discrepancy training algorithm from continuous space to discrete space for training energy based models. In particular, the paper introduces three types of perturbations to construct the energy discrepancy in discrete space. Also, the paper developed gradient-based proposals in discrete space to efficiently estimate the energy discrepancy. The paper conducts experiments on Ising model, synthetic discrete patterns, graph generation, and discrete images. The results shows the proposed method is a competitive algorithm compared to existing energy based models training algorithms in discrete space.

### Strengths
* The paper, in the first time, introduces energy discrepancy objective in training discrete energy based models. The idea is simple but smart, and looks promising especially for training deep energy models where a disturbed data is supposed to be a good negative sample. 
* The paper conducts intensive experiments with different perturbations and gradient-based proposal methods to justify the effectiveness of the proposed method. Also mentioned some basic philosophy to choose perturbation and proposal, for example, in section 6.4, the paper conjectures the combination of gradient-based proposal with grid neighborhood transformation tends to get trapped in local modes as it only
flips one bit for each negative sample.
* The paper is well written with appropriate explanation and examples.

### Weaknesses
 * The energy discrepancy was used to train continuous energy based models. The paper does not provide enough evidence about the limitation of continuous perturbation with continuous relaxation to train discrete energy based models. This makes the paper less motivated. An explanation about why continuous perturbation does not work or some empirical comparisons would be helpful.
* Although the paper provides comparisons between different perturbation and proposals, a principled criteria to choose them is missing. This is no doubt a hard question and a bit more discussion would be helpful. Specifically, the paper lacks a clear explanation of how the choice of perturbation affects the exploration of the energy landscape and how the proposal method impacts the variance of the gradient estimates. A more detailed analysis of the trade-offs between different perturbation and proposal combinations is needed.
* In experiments, the proposed training algorithm is not significantly better than existing methods. I guess the main reasons are the tasks are simple and the existing algorithms already get very good results. As mentioned in the last paragraph of the paper, the evaluations on more structured data like molecules or text would be helpful.

Minor:
Clarification in page 2, theorem 1. $\text{Var}(x|y)$ is a bit confusing. $\text{Var} (z), z \sim p(\cdot|y)$ would be easier to understand for me.
Typo in page 3, first sentence: $p(x|y) \Rightarrow p_\text{ebm}(x|y)$

### Questions
* Will using an energy based model with continuous relaxation with continuous energy discrepancy training work? How does it perform compared to current discrete framework?
* Can we train a variational distribution for informed proposal? How would that compare to a gradient-based proposal?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper discusses the concept of energy discrepancy application in training energy-based models on discrete data by evaluating the energy function at data points and perturbed counterparts. It is claimed that the paper introduces a novel approach with theoretical guarantees to achieve this goal. Some experiments are provided to support their claim.

### Strengths
- This is a very interesting problem to investigate. 
- The applicability of this method to perturbed processes makes it versatile for various data domains. 
- It is easy to read the paper and the presentation is clear.

### Weaknesses
 - The novelty of this paper is moderate at best. It seems like this paper is a combination of a few papers for instance: 

     * Gradient_Guaided importance sampling for learning binary energy-based models by Meng Liu, Haoran Liu, Shuiwang Ji
     *  Energy Discrepancies: A Score-Independent Loss for Energy-Based Models by Tobias Schröder 2023

- Seems like the theorems are not novel and are borrowed from other papers; they should have been as a proposition with reference to the original paper. Even the proofs are very similar and all could have been omitted. 

- This paper seems to be an extension of a poster However, not much is added to the paper compared to the poster. More detailed experimental results are much needed. A lack of comparison between this method and other state-of-the-art on diverse datasets.


### Questions
A few questions regarding the algorithm: 

1- Seems like sampling a large number of negative samples for each data point in every iteration can be computationally intensive, especially for high-dimensional discrete data which can lead to slowing down the training process. Also, there are many hyperparameters involved in this algorithm such as the number of negative samples, and stabilization parameters. Could the author please elaborate on these concerns? How does the tuning work and how sensitive it is to suboptimal choices?  

2-The algorithm's exploration of the energy landscape might be constrained, particularly when the perturbation distribution (q) does not encompass diverse regions of the data space. This limited exploration could lead to models capturing only specific facets of the data distribution, potentially resulting in biased or incomplete representations. Could the authors please elaborate on that? In addition, the choice of perturbation distribution (q) seems to heavily rely on the characteristics of the training data. How can one design an effective perturbation strategy that is adaptive to different types of discrete?

3- Could the authors please discuss the scalability of the proposed methods with increasing dataset sizes? Moreover, can you provide insights into the interpretability of the learned models?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper builds on top of Energy Discrepancy, a recently proposed approach for training energy-based models (EBMs), and demonstrates how to leverage Energy Discrepancy to train discrete EBMs. It presents three different types of perturbations, investigates two different types of proposal distributions for efficiently estimating the energy discrepancy loss using importance sampling, and empirically demonstrates the effectiveness of the proposed approach for multiple applications.

### Strengths
* The paper studies an important problem: how to efficiently learn discrete EBMs.
* The paper is clearly written, and easy to follow. The method and the experimental results seem sound.
* The paper demonstrates improved performance for a variety of different discrete EBMs.

### Weaknesses
All of the proposed perturbation methods and all of the experiments are only dealing with EBMs with binary variables. As a result, presenting the proposed method as an approach to learn discrete EBMs seems to be overclaiming. Moreover, it seems to me the study of this approach when applied to EBMs with discrete variables having more than two states should be within scope of this paper, as this is a very natural and straightforward extension but there might be new issues arising when applied to discrete EBMs with non-binary variables (e.g. the mean-pooling perturbation depends on the parametrizations of the variable states and this can impact the performance of such perturbations). The lack of experiments on non-binary discrete variables significantly limits the impact and generalizability of the proposed method.

Related to the above point, I also find the contributions of this paper to be underwhelming. This paper is a straightforward application of Energy Discrepancy, the proposed perturbations are only applicable to binary EBMs, and estimation of Energy Discrepancy is also largely simple adaptations of existing methods. The experimental results also seem to be overclaiming (in table 1, EB-GFN performs best on circles, and in many cases the performance difference seems neglible, elg. on pinwheel; in table 2 the authors claim the proposed methods consistently outperforms baselines which does not seem to be the case; in table 3, the authors claim the performance is comparable but both GWG and DULA seem to be significantly better than the proposed methods on static and dynamic MNIST). The performance gains are not substantial enough to justify the introduction of a new method, especially considering the limited scope of the experiments.

Due to the above weaknesses, I am leaning towards rejecting the paper as is.

### Questions
* The paper seems to be taking a lot of the proofs from the original Energy Discrepancy paper more or less verbatim (e.g. appendix A and B). Why is this needed? Why can't these be replaced by a simple pointer to the original paper?
* Page 3 first line, p(x|y) should be p_ebm(x|y)
* The notation p_ebm in equation (6) seems a bit confusing to me
* How is the mean pooling calculated exactly? Take the mean in float and then round to either 0 or 1? It seems to be this would cause issues when extended to non-binary variables as the mean in float for non-binary variables is not particularly meaningful/informative in many cases.
* Mean pooling seems to be applicable only to image data? Presenting it as one of 3 perturbations seems a bit odd as it is more specialized and not very generally applicable.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes training discrete EBMs using Energy Discrepancy (ED) instead of Contrastive Divergence (CD). Training with ED does not require sampling, instead it only requires evaluating the energy function at data points and their perturbations.

The paper claims that existing approaches suffer from a tradeoff between obtaining more accurate samples during training, and increasing the time-cost of training, and obtaining less accurate samples, increasing the bias of the gradients used during training. 

To apply this technique, one must choose a suitable distribution to sample data perturbations, and an efficient method to estimate the contrastive potential induced by this distribution on data perturbations. 

The authors propose several data perturbation distributions, and propose estimating the contrastive potential using importance sampling. For the proposal distribution, the authors investigate using uninformed proposals, and gradient-informed proposals. Uninformed proposals do not exploit any information about the learned energy function U. 

Gradient-informed proposals used a Taylor expansion similar to that shown in Gibbs-with-Gradients (GwG). The authors draw a connection between their approach and GwG.

Finally, the authors train a lower bound on this loss to improve training stability. The authors present several configurations of their approach and compare to baselines. 

The authors present results on small toy problems for visualisation, as well as on graph generation and image generation. 

The authors present thorough ablations and experimental details in the appendix.

### Strengths
Very thorough ablations are presented in the appendix, investigating the effects of a number of parameters to configure their method.

### Weaknesses
The results on discrete image modelling are not very strong, either in terms of sample quality or in terms of estimated NLL.


### Questions
I’m curious about the wall-clock speed of training. Your approach admits better parallelisation than existing techniques since it relies on importance sampling rather than MCMC. Do you have any wall-clock timing experiments investigating this? For example, how does the wall-clock time compare of your approach vs. CD-10? 

Must the GwG sampler be tuned differently when training with ED vs. GwG? i.e. do you find that sampling is less efficient at test-time when a model is trained with ED?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
