# Neural Networks and Solomonoff Induction

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3

## Abstract
Solomonoff Induction (SI) is the most powerful universal predictor given unlimited computational resources. Naive SI approximations are challenging and require running vast amount of programs for extremely long. Here we explore an alternative path to SI 
  consisting in meta-training neural networks on universal data sources.
  We generate the training data by feeding random programs to Universal Turing Machines (UTMs) and guarantee convergence in the limit to various SI variants (under simplifying assumptions). We provide novel results on how a non-uniform distribution over programs still maintain the universality property. Experimentally, we investigate the effect neural network architectures (i.e. LSTMs, Transformers, etc.) and sizes on their performance on algorithmic data, crucial for SI. First, we consider variable-order Markov sources where the Bayes-optimal predictor is the well-known Context Tree Weighting (CTW) algorithm.
  Second, we evaluate on challenging algorithmic tasks on Chomsky hierarchy that require different memory structures. Finally, we test on the UTM domain following our theoretical results.  We show that scaling network size always improves performance on all tasks, Transformers outperforming all others, even achieving optimality on par with CTW. Promisingly, large Transformers and LSTMs trained on UTM data exhibit transfer to the other domains.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors explore approximate versions of Solmonoff induction via meta-learning and neural networks.  Their experimental setup compares the performance of a variety of deep neural network architectures within their framework on several algorithmically generated data sets.

### Strengths
The paper is clearly written and motivates the general problem.

The discussion, although it is primarily focused on Turing machines, is relevant broadly to themes in modern ML, e.g., large language models and other increasing large DNNs trained on massive data sets.  As a result, this work might help make connections between more classical AI and modern ML.

### Weaknesses
While the discussion is clear in many places, it also assumes quite a bit a background without references, e.g., "Kolmogorov's probability axioms".  As this is a submission to an ML conference, I suggest that the authors provide the necessary context to aid unfamiliar readers.  In the same vein, not many participants at ICLR are likely to be familiar with Solmonoff induction. So, the fit might be better at a more traditional AI venue -- the advances here are more from about using existing NN tools rather than pushing the state-of-the-art in deep NNs.

The experimental setup is missing some details, e.g., how many training examples are there?

### Questions
- I don't really have good intuition about how varied the prediction tasks are.  Can you provide a bit more intuition here?

- Like large language models, I expected that you would need a significant amount of data for training in this case.  Can you talk a bit more about data sizes, and why the results are or are not expected?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this work, authors theoretically investigate how universal approximators using a dataset converge to SP in some limit and show that universality is maintained even when underlined distribution shifts. They experiment with Transformers and LSTM NNs to show model complexity increases with increase in parameters, such that convergences can be seen on challenging dataset.

### Strengths
1. The paper is well written
2. Good set of experiments

### Weaknesses
1. Novelty is limited
2. Several key papers are not cited

It is true only for first-order RNNs that they are Turing complete with infinite precision and time, however, tensor RNNs with and without memory are shown to be equivalent to TM with finite precision [5,6] and also UTM

Lemma 10, Corollary 11, Lemma 12-14 [ 1-2] – Theorem 9 in paper shares some similarities, slightly different ways to prove the same property. 

Theorem 3 Linear separation [4] – the paper could benefit by showing how various layers in transformers cause linear separation using hard attention and would lie in Banach space dual. Again, with some assumption, it is trivial to show how their approach is also universal. 

Generalized Solomononff semimeasures definition and Theorem 9 in the paper also share similarity with [3]; second majority of suggestions and claims are given in [3]. Furthermore they have shown some experiments and multiple hypothesis generation can be seen as a case of meta-learning. There are several lemmas on recursive functions, that can be extended with modern RNNs such as LSTM and even for Transformers (assuming within a finite length, they approximate RNN).

Authors should cite these line of work. Thus it seems the current manuscript is more incremental aligned with the experimental setup in the meta-learning space using modern NNs.

Finally, it is hard for me to see what values the current method provides to the community; I will briefly discuss why I feel this,

* theorem 11 in [7] proves that equivalence between two RNN is undecidable, Theorem 6 shows that consistency problem in RNN is also undecidable, Theorem 7 shows 2 layer RNN using BPTT on a finite corpus is necessary not consistent, furthermore Theorem 11 and 8 points out best string problem is NP-hard and in some cases undecidable. Given we know above properties for RNN, that is also true for transformers with some conditions, thus I am not sure Solomonoff induction would help in getting universal capability of the modern day NNs

* Second RNN and transformers are turing complete comes from a unrealistic assumptions where entire tape is encoded into a tape. Based on bignum arithmetic we can see there is infinitely many hierarchies across various natural numbers, and works in infinite space. Therefore, what practical benefits it offers is still a open question.

* Third when we move to UTM space and show RNN is equivalent to UTM will also work in infinite space and time

* Fourth Solomonoff induction also requires infinite samples, given everything or in simple words all components are working in infinite space, how can one show practical universality? Nor can it be claimed that the model trained on the dataset is universal. So, I would advise authors to lower down the claim as it is highly misleading.

### Questions
It is true only for first-order RNNs that they are Turing complete with infinite precision and time, however, tensor RNNs with and without memory are shown to be equivalent to TM with finite precision [5,6] and also UTM

Lemma 10, Corollary 11, Lemma 12-14 [ 1-2] – Theorem 9 in paper shares some similarities, slightly different ways to prove the same property. 

Theorem 3 Linear separation [4] – the paper could benefit by showing how various layers in transformers cause linear separation using hard attention and would lie in Banach space dual. Again, with some assumption, it is trivial to show how their approach is also universal. 

Generalized Solomononff semimeasures definition and Theorem 9 in the paper also share similarity with [3]; second majority of suggestions and claims are given in [3]. Furthermore they have shown some experiments and multiple hypothesis generation can be seen as a case of meta-learning. There are several lemmas on recursive functions, that can be extended with modern RNNs such as LSTM and even for Transformers (assuming within a finite length, they approximate RNN).

Authors should cite these line of work. Thus it seems the current manuscript is more incremental aligned with the experimental setup in the meta-learning space using modern NNs.

Finally, it is hard for me to see what values the current method provides to the community; I will briefly discuss why I feel this,

* theorem 11 in [7] proves that equivalence between two RNN is undecidable, Theorem 6 shows that consistency problem in RNN is also undecidable, Theorem 7 shows 2 layer RNN using BPTT on a finite corpus is necessary not consistent, furthermore Theorem 11 and 8 points out best string problem is NP-hard and in some cases undecidable. Given we know above properties for RNN, that is also true for transformers with some conditions, thus I am not sure Solomonoff induction would help in getting universal capability of the modern day NNs

* Second RNN and transformers are turing complete comes from a unrealistic assumptions where entire tape is encoded into a tape. Based on bignum arithmetic we can see there is infinitely many hierarchies across various natural numbers, and works in infinite space. Therefore, what practical benefits it offers is still a open question.

* Third when we move to UTM space and show RNN is equivalent to UTM will also work in infinite space and time

* Fourth Solomonoff induction also requires infinite samples, given everything or in simple words all components are working in infinite space, how can one show practical universality? Nor can it be claimed that the model trained on the dataset is universal. So, I would advise authors to lower down the claim as it is highly misleading.


It would benefit if authors can provide insight how transformers and RNNs LM can benefit. For instance, by showing how they work when state space is small vs large, symbols are increased, model is trained on short strings and tested on longer. How do attention weights attend in such scenarios, how does LSTM memory adapt to these changes? Do you observe any tape-like or even stack-like behaviour etc. showing these analyses would further benefit the paper and will help understand how using SI can help LLMs reason about the world in some finite space. 



1.	Sterkenburg, T.F., 2017. A generalized characterization of algorithmic probability. Theory of Computing Systems, 61, pp.1337-1352.

2.	Wood, I., Sunehag, P. and Hutter, M., 2013. (Non-) equivalence of universal priors. In Algorithmic Probability and Friends. Bayesian Prediction and Artificial Intelligence: Papers from the Ray Solomonoff 85th Memorial Conference, Melbourne, VIC, Australia, November 30–December 2, 2011 (pp. 417-425). Springer Berlin Heidelberg.

3.	Li, M. and Vitanyi, P.M., 1992. Inductive reasoning and Kolmogorov complexity. Journal of Computer and System Sciences, 44(2), pp.343-384.

4.	Sunehag, P. and Hutter, M., 2013. Principles of Solomonoff induction and AIXI. In Algorithmic Probability and Friends. Bayesian Prediction and Artificial Intelligence: Papers from the Ray Solomonoff 85th Memorial Conference, Melbourne, VIC, Australia, November 30–December 2, 2011 (pp. 386-398). Springer Berlin Heidelberg.

5.	Stogin, J., Mali, A. and Giles, C.L., 2020. A provably stable neural network Turing Machine. arXiv preprint arXiv:2006.03651.

6.	Mali, A., Ororbia, A., Kifer, D. and Giles, L., 2023. On the Computational Complexity and Formal Hierarchy of Second Order Recurrent Neural Networks. arXiv preprint arXiv:2309.14691.

7.	Chen, Y., Gilroy, S., Maletti, A., May, J. and Knight, K., 2017. Recurrent neural networks as weighted language recognizers. arXiv preprint arXiv:1711.05408.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
- This paper investigates "amortizing Solomonoff Prediction into a neural network". 
- They then "introduce a generalized Solomonoff prior". 
- Lastly, they conduct experiments to show predictive performance on sequence prediction tasks, where they use meta learning with log-loss on a heterogeneous set of string related tasks.

### Strengths
The paper draws connections between Solomonoff Prediction and meta learning.

The paper seems to have a formal grasp on some concepts in computational complexity that are useful formalism for describing tasks in machine learning, for example ranking them according to the Chomsky hierarchy (does the task require a stack to solve? or a more complicated data structure)

### Weaknesses
Overall, the paper is hard for me to follow. In summary the issues are:

- Many definitions given up front (up to beginning of page 4) are fairly non-standard, given the general body of work that shows up at ICLR. At the same time, the presentation features little discussion of definitions after they are given, with most details relegated to appendix.


- Theorem statements in main text contain uncommon terms "probability gap" without definition. The notion of a 'probability gap' is not a standard term in probability theory or machine learning, and its usage without a clear definition makes the theorem statements difficult to interpret. It is unclear how this gap relates to more established concepts like KL divergence or total variation distance, which would provide a more familiar frame of reference.

- Definitions that are given contain other undefined terms within definition, e.g.:
  - An algorithmic data generating source µ is simply a computable data source by" A "data source" was not defined. The term 'data source' is used without specifying whether it refers to a stochastic process, a function, or some other mathematical object. This lack of clarity makes it difficult to understand the scope and limitations of the proposed framework.
  - SI: Inductive inference aims to find a universally valid approximation to µ. What's "universally valid"? The term 'universally valid' is vague and requires a more precise definition. Does it mean that the approximation holds for all possible inputs, or for all possible data sources? Without a clear definition, it is difficult to assess the theoretical claims of the paper.

- Propositions (e.g. prop 4, prop 8) are given and followed immediately  by a next section with no concluding sentence on what the takeaway should be or what the theorem means in words. The lack of interpretation makes it difficult to understand the significance of the propositions and how they contribute to the overall argument of the paper. It is crucial to provide a clear explanation of the implications of these results.

- Many data details (e.g."Variable-order Markov Source", one of the 3 experiments) are not defined in main text and details are relegated to appendix, and, as mentioned, are generally not particularly well known within the ICLR community. The Variable-order Markov source is a specific type of stochastic process, and its definition is crucial for understanding the experimental results. The fact that it is not defined in the main text makes it difficult for the reader to assess the validity of the experiments.

- Many baselines / models not defined in main text: Stack-RNNs, Tape-RNNs,  Context Tree Weighting, where the last one is used as the main baseline. These models are not standard and require a brief explanation in the main text. The reader should not have to refer to external sources to understand the experimental setup.

- Important experimental details that are glossed over, e.g. there is a test distribution described as "out-of-distribution" in passing in the analysis of results without a formal experimental setup given for precisely what the shift between in- and out-distribution is. The lack of a formal definition of the in- and out-of-distribution setting makes it difficult to interpret the experimental results. It is crucial to provide a precise description of how the test data is generated and how it differs from the training data.

### Questions
- It is stated that $\pi_\theta$  approximates the predictive distribution for each task $p(x_{t+1}|x_{\leq t}, \tau)$ for each task $\tau$ . However $\pi_\theta(x_{\leq t})$ is not notated to be a function of $\tau$. If $\pi_\theta$ is optimized with log loss it will learn a mixture of the predictive distribution across tasks rather than each task, unless extra assumptions are stated, such as that the support of $x_{\leq t}$ is disjoint across tasks for each $t$. Could the authors clarify  whether $\pi_\theta$ is also a function of $\tau$, and if not, what are the assumptions on the data that make this statement true?


- "Out-of-distribution" appears twice in the main text, including in the qualification of a test distribution. However, no particular definition of what is in versus out, or what the distribution shift is precisely, was given. A few sentences later, length-generalization is mentioned in passing, so I had to infer what in versus out meant. Usually it's really important to mention training versus test distribution details up front rather than in passing in the results. Could you please explain the precise experimental setup including data generation in more detail, in the main text?


- Finally, experimentally, it's not clear that the experiments run were anything different than running log likelihood optimization on a mixture of datasets. What's the practical/algorithmic difference or significance in what was run, and what should the takeaways be? If there is no difference, is the significance in the connection to the theoretical results? If so, what is that connection?

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair
