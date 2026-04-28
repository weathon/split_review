# Transformers can optimally learn regression mixture models

- Decision: Accept
- Avg Score: 6.80
- Scores: 8, 6, 6, 8, 6

## Abstract
Mixture models arise in many regression problems, but most methods have 
seen limited adoption partly due to these algorithms' highly-tailored and model-specific nature. 
On the other hand, transformers are flexible, neural sequence models 
that present the intriguing possibility of providing general-purpose 
prediction methods, even in this mixture setting. 
In this work, we investigate the hypothesis that transformers can learn an optimal predictor for mixtures of regressions. 
We construct a generative process for a mixture of linear regressions 
for which the decision-theoretic optimal procedure is given by data-driven exponential 
weights on a finite set of parameters. 
We observe that transformers achieve low 
mean-squared error on data generated via this process.
By probing the transformer's output at inference time, we also show that transformers typically make predictions that are close to the optimal predictor. 
Our experiments also demonstrate that transformers can learn mixtures of regressions in a sample-efficient fashion and are somewhat robust to distribution shifts. 
We complement our experimental observations by proving constructively that the decision-theoretic optimal procedure is indeed implementable by a transformer.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper shows that transformer architectures can implement a mixture of linear regressions. Namely, it can implement the optimal solution that uses the true underline model parameters. The authors showcase their claim via a sequence of experiments.

### Strengths
* The idea of the paper is original and novel.
* The paper is written well. The illustration of the proof adds to the clarity of it and gives a good intuition.
* In general, the experiment section is good (although I think it misses some things; but more on that in the next section).
* Code was provided and the results seem to be reproducible.

### Weaknesses
 * I am not convinced about the significance of this work. To clarify that, I would like the authors to address the following questions, how and when can one use the observation in the paper? In the introduction, federated learning is mentioned as a possible application. But, federated learning systems do not use linear models and if they do the number of components is known in advance (which is arguably the biggest advantage of the proposed viewpoint in the paper). I acknowledge though that this work can be a stepping stone towards a mixture of non-linear models, which potentially can have more impact.
* I do not have experience with mixture models. But, to me, it seems that a clear advantage of using mixture models is the access to the underline model and the mixture components. This is somewhat lost here. Having an approximation for the posterior mean only is nice, but I assume that in many cases one wants to evaluate each mixture separately in order to make a choice.
* Unless I didn't understand something, a potential issue for taking the viewpoint of this paper is that training transformers can be demanding in computation and data. I would expect that in most cases one would like to use these types of models in exactly the opposite cases, i.e., small training sets with limited computation. 
* In section 3.1, under the noisy case, it is not surprising that the OLS model does not work as well since it doesn't model the noise. In my opinion, a more appropriate comparison would be an OLS model with a hyper-parameter for the noise variable which is chosen based on a validation set. Especially in light of the fact that a grid search was done for the dropout rate of the proposed approach. Conversely, and perhaps even more appropriate, is to compare to a Bayesian model and either optimize the noise via the marginal likelihood (or ELBO) or give it a full Bayesian treatment.
* To complement the question of "What is the transformer actually learning?" in section 3.3., I believe that some form of evaluation on out-of-distribution data be done. I suspect that the transformer learns an approximation for the posterior mean only in regions of in-distribution, but outside of it, it will behave in an arbitrary fashion. On the other hand, we know exactly how the posterior mean solution will behave in every region. Perhaps the authors can verify that using a similar experiment to the one in section 3.3 or on a simple 2D problem. If that is indeed the case, then how can you guarantee that indeed the solution found by the transformer matches that of the posterior mean?

### Questions
.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors argue that transformers provide a simple mechanism to efficiently and accurately learn mixtures of linear regression models.  They prove that the optimal solution is representable by such transformers and then experimentally verify that sample complexity/accuracy is on par with existing methods for this task.

### Strengths
It is a simply presented, well-articulated problem and solution.  The presentation is clear and more or less self-contained.

### Weaknesses
I'm not sure that the new work really address limitations in the existing literature.  The main motivation is that existing methods are potentially brittle and that their theoretical guarantees do not extend to the model misspecification setting.  It isn't clear that this work really demonstrates much of an improvement in that regard.  As a result, it isn't clear to me what this approach really offers (other than perhaps simplicity?).  It too does not come with any guarantees more generally -- or maybe I have misunderstood?

Also, it also feels like this result is a bit preliminary and could potentially encompass a wider range of mixture models and statistical settings.

### Questions
Questions are in the weakness section above. 

Minor typos/suggestions:
- "gradient descent would naturally extends"
- "definitions in display (4)." -> "definitions in (4)."
- "better predictor to adapted to the mixtures of linear regressions setting"

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the performance of transformers on in-context learning problems consisting of mixtures of linear regression models, where the prompt consists of input-output pairs coming from a linear model with one of $m$ different target weight vectors.
The authors show that the posterior mean in this problem may be implemented with a well-chosen transformer, and that empirically the predictions behave similarly to this algorithm, in particular outperforming OLS and EM approaches.

### Strengths
The paper makes an interesting contribution in the recently popular literature on using transformers for in-context learning regression models.

The posterior mean in eq.(4) is particularly interesting as a desired goal, as it requires a more complex transformer architecture than related papers, which combines both in-context algorithmic operations, and some "knowledge" from the data distribution, in the form of the $w_i^*$ vectors.

The experiments seem to give promising evidence that this target model may indeed resemble the one learned by transformers.

### Weaknesses
Two points would significantly strengthen the paper:

* while empirical results suggest the transformer might be related to the posterior mean, it would be good to have some interpretability results to assess whether this is true in practice, and if your construction in Theorem 1 is practically relevant: is there any evidence that the blocks shown in Figure 1 are actually being learned by the pre-trained transformer? Where are the $w_i^*$ being stored in the weights? Is it necessary to have at least 5 layers in practice, as in your construction? Is it sufficient?

* a more extensive empirical analysis would be useful, particularly on how the results vary when changing problem parameters. For instance, how does the performance change as $m$ varies? In particular, it seems difficult to find all the hidden directions $w_j^*$ once $m$ is too large -- does it start resembling OLS at some point? Does increasing the width, number of heads, number of layers change this?

* related work: is your setting covered by the general setting in [this paper](https://arxiv.org/abs/2306.04637)?

### Questions
see weaknesses

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors explore whether transformer architectures can be trained to learn mixtures of linear models from batched data. They find that Transformers are surprisingly effective at this empirically, and they support their empirical results with a constructive proof that the optimal solution is representable in a transformer architecture.

### Strengths
I should note that this paper is out of area for me, and while I followed all the details, I may have missed some of the broader context.

I thought this a was well executed paper:
 - They give a nice constructive argument that shows that transformers can implement mixtures of linear regressions. 
 - The experiments are very interesting in that they not only show that mixtures of linear regressions can be learned (this is perhaps not surprising given Garg et al's recent results showing this for linear regression), but that they are also competitive in terms of sample complexity with state of the art algorithms for this problem. I would have expected that you pay a larger cost for generality.

### Weaknesses
When I got to the end of the experimental section, I felt that there was a missed opportunity to look at whether Transformers allow one to easily go beyond the linear mixtures setting. While it is very interesting that Transformers are competitive with recent specialist algorithms for the linear mixture setting, I think the key advantage of a black-box method like a transformer is the ability to directly apply it to settings whether the linear mixture assumptions fail. Investigating how performance degrades (if at all) would have been interesting and would have potentially allowed you to show where Transformers outperform existing approaches.

This is brought up in the future work section of the discussion, but I think it would have been better to include it in this paper.

### Questions
I am most curious about whether you have experimented with any of the questions raised in your next steps. For example,

> in practice, the regression function within each component could potentially be nonlinear. To what extent do transformers perform well in these settings? 

> In general, the decision-theoretic optimal method could be more complicated to compute, as implementing the posterior mean would require computing a high-dimensional integral. Nonetheless, is it possible to approximate the optimal method with a trained transformer? 

I would be very happy to increase my score if you could show some experiments that show whether Transformers easily generalize beyond the linear Gaussian case (or not - a negative result could also be interesting if it is explained).

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the ability of transformer models to perform mixture of linear regressions. Specifically, the authors train transformer models in the task of mixture of linear regressions, in which $k$ possible weight vectors are sampled with equal probability. They show that  there exists a decoder-based transformer that can implement the Bayes optimal for this task. Furthermore, they compare the performance of the transformer models with previously proposed algorithms.

### Strengths
This paper performs extensive experimental comparisons on the transformers' performance with other algorithms. They also extend the setting of previous work from linear regression to mixture of linear regressions.

### Weaknesses
It is unclear why this setting is of interest. I understand that transformers match the performance of proposed algorithms and that they could be used as an alternative for mixture of linear regressions. However, we should think of the cost training transformers and the time consumed, compared to performing any of the other algorithms.  The current models are used to perform language tasks and we are unaware on how optimization/numerical tasks could be merged with language tasks. 

Furthermore, I think that more details should be provided for the experimental set-up.
Looking at the appendix of the paper, it is unclear to me how this proof is implemented. I think that the results of [1] require the design of specific encodings and entail some error, which was also not analyzed in [1], but the authors should at least show how it is controlled. I find in general the proof to be very high level and I had trouble verifying that it is correct.

### Questions
1. Did the authors perform experiments in which the weight vectors $w_i^*$ are not sampled with equal probability?
2. What models exactly the authors used? GPT2? 
3. How many samples did they use to train the models and how many to test them? Which is also the sequence length for in-context learning? Is the sequence length during training the same as the one during inference? 
4. How in the proof of lemma 2, the authors simply select $W_K H:,i = I_{2x2}$ since this matrix is required to have the second dimension equal to the sequence length.
5. Do the authors propose the use of transformers for this task ? 
6. In the discussion section it is mentioned that "The fact that transformers... quite useful for practical problems". Could the authors mention some of those problems in which transformers would be useful ?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
