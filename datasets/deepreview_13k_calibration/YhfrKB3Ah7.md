# PABBO: Preferential Amortized Black-Box Optimization

- Decision: Accept
- Avg Score: 7.40
- Scores: 8, 8, 8, 8, 5

## Abstract
Preferential Bayesian Optimization (PBO) is a sample-efficient method to learn latent user utilities from preferential feedback over a pair of designs. It relies on a statistical surrogate model for the latent function, usually a Gaussian process, and an acquisition strategy to select the next candidate pair to get user feedback on. Due to the non-conjugacy of the associated likelihood, every PBO step requires a significant amount of computations with various approximate inference techniques. This computational overhead is incompatible with the way humans interact with computers, hindering the use of PBO in real-world cases. Building on the recent advances of amortized BO, we propose to circumvent this issue by fully amortizing PBO, meta-learning both the surrogate and the acquisition function. Our method comprises a novel transformer neural process architecture, trained using reinforcement learning and tailored auxiliary losses.
On a benchmark composed of synthetic and real-world datasets, our method is several orders of magnitude faster than the usual Gaussian process-based strategies and often outperforms them in accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work introduces a novel approach to Preferential Bayesian Optimization (PBO) by fully amortizing the optimization process. Traditional PBO methods rely on GPs for modeling user preferences between design pairs, requiring extensive computational resources due to approximate inference for non-conjugate likelihoods. PABBO addresses this challenge by employing a transformer-based neural architecture and reinforcement learning to learn both the surrogate model and acquisition function end-to-end, significantly accelerating the optimization process. By pre-training on synthetic and real-world datasets, PABBO achieves several orders of magnitude in speed improvement while often surpassing GP-based methods in optimization quality.

### Strengths
- The paper is well written and easy to understand for the most part.
- The proposed method is a novel and interesting application of amortized learning/BO for PBO setting. The empirical results seem superior than traditional PBO methods and acquisition functions.
- Nice set of experimental evaluation and ablation studies — though I’d love to see a more comprehensive experimentation section (see weaknesses below) for methods that are hard to provide theoretical guarantees.

### Weaknesses
 - Evaluation on harder problems are very limited. Most test functions are of very small dimensions and may not resemble real-world optimization tasks. The only experiments with moderate dimensionalities are 6 and 9-dims respectively and are all from the HPO-B. This leaves the scalability of the proposed methods in question.
- No ablation studies on meta-learning training set. It is plausible that amortized learning methods are highly sensitive to the selection of pre-training data. There’s no justification or ablation on the choice of pre-training data for PABBO and it’s unclear how robust the method is to a different set of pre-training data.
- The performance advantage vs baseline methods are not significant in many cases.
- While it is true that estimating the true posterior of a preference model’s posterior might be expensive, variational inference or Laplace approximation with some clever implementation can go quite far and allows for gradient-based optimization for acqf value. On the other hand, for larger models like PABBO1024, the inference time advantage of amortized learning might be diminishing when compared to GP-based model according Figure 3 and 5.

### Questions
- S in query set is from a Sobol sample. How big is sufficient? How would this affect the optimization quality as even the largest experimented S=1024 might not be sufficiently for moderately high-dimensional spaces, limiting the scalability of this PABBO.
- How does PABBO work for higher dimensional problems? All experiments presented are of very small dimensions and may not resemble real-world optimization tasks.
- Algorithm 1 seems to only describe the meta-learning/pre-training part of PABBO as we are still updating the PABBO model at the end of the loop. What’d be the algorithm for applying PABBO on new, unseen dataset? I’d assume that’d be the same as the inner loop of the algo, but it’d be nice to have some clarification from the author.

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
4

### Summary
This paper explores preferential black-box optimization with an amortized inner-loop solver. In other words, RLHF but from the lens of Bayesian optimization instead of NLP.

### Strengths
This work is well motivated. Aligning training objectives with downstream use makes sense (i.e. the explicit acquisition head) and amortization also makes sense if you expect to solve the same (or nearly the same) optimization problem many many times.

The paper is clear and well-written

The experiments hit pretty much all the key points I would expect

### Weaknesses
This paper seems to treat simple and cumulative regret as interchangeable, although I am sure the authors know the difference. If the policy is optimized to minimize cumulative regret, why is cumulative regret not reported? On the other hand if simple regret is really what you care about, why are none of the baselines aimed at best-arm identification? For example, Thompson sampling is optimal w.r.t. cumulative regret, not simple regret. Top-two thompson sampling is optimal in the discrete case [1], although translating to the continuous case requires some thought (what epsilon is sufficiently large to constitute a different arm?).

I also feel that the experimental design could be more directed at identifying under what conditions this solution makes sense. What is the breakpoint when amortization starts paying off compared to direct search at test time? How far can you push this before it breaks, especially in terms of the initial data package?

It also seems very odd that preference tuning for language models is not mentioned even once, even though it is obviously the same problem and basically the same solution (ignoring low-level implementation choices). I can't tell if this is a deliberate choice that reflects the legal sensitivity around LLMs right now or a genuine oversight, however I see no reason not to draw the connection to preference tuning work.

I generally try to avoid policing language, but sentences like "... amortization ... has emerged as an almost magical bullet solution" clearly crosses the line from excitement to needless hype. Amortization is not anything close to a magic bullet. You know that and I know that. It is just moving compute around from test time to train time. Of course science involves some marketing, but language and framing like this hurts our credibility with more staid scientific disciplines, people that you presumably would like to take you seriously. Write like a scientist, not a salesman. It's ok to be excited, just don't get carried away!

### Questions
Can you add a reasonable interpretation of top-two thompson sampling in the continuous case to your experiments by the end of the rebuttal period? 

Are you warm-starting the amortized solver training as the data changes? Do you lose performance because of that choice? How expensive does the test-time search have to be to warrant amortization? How carefully have you thought about the FLOPS involved here?

How much can you push this? I don't just want to see rosy results, I want to know when this breaks.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents PABBO a preference based Bayesian optimization approach using transformer architectures and deep sets approaches to amortize the inference time. The paper extend ideas of amortization from past works to preference based optimization and presents an end-to-end trainable approach.

The main idea behind the approach is to use a transformer and attention mechanisms on historical observed data and use them to make query predictions. Another prediction head from the same transformer produces the policy function which is used to suggest the future queries. Experimental results indicate that the proposed approach is faster compared to previous approach and achieves a smaller regret.

### Strengths
Strengths:
- The paper presents a new approach to preference based BO using transformers which as several advantages - it can incorporate preferences, has amortized inference cost and can be trained end-to-end.
- The proposed approach is intuitive and a reasonable way to model preferences in BO, with the potential to scale to very large problems. The method uses neural networks instead of Gaussian processes which helps it scale to a large number of data points.
- Extensive experimentation shows that PABBO has a smaller inference cost while achieving a smaller regret compared to prior approaches.

### Weaknesses
Weaknesses:
- While the proposed approach is faster than BO, the scale at which the experiments are performed (100 observations max), the gains are not fully realized since BO methods can perform quite comfortable at such small scales. The paper does not sufficiently demonstrate the advantage of the amortized approach over traditional BO methods, especially when considering the overhead of pre-training.
- The full potential of the algorithm is only realized in large experiment with thousands of observations. Such large scale experiments have not been presented in the paper. The lack of experiments with a large number of observations makes it difficult to assess the scalability and practical relevance of the proposed approach. The paper should include experiments with a significantly higher number of observations to demonstrate the benefits of the amortized approach.
- Preference based optimization is most useful when modeling users with varying preferences. The paper can benefit from the interesting extension of learning to model individual user preferences. The current approach assumes a single, consistent preference model, which limits its applicability in real-world scenarios where user preferences may vary significantly. The paper should explore methods to adapt the model to different user preferences or to learn personalized preference models.

### Questions
General questions
- How does preference based optimization work when users have varying preferences? Is it possible to incorporate personal user-preferences in this framework.

Specific questions
- Line 237, Is the same MLP applied to x_i,1, x_i,2 and l_i individuall? Why should l_i be encoded into the same embedding space as x_i,1 and x_i,2? Or does the statement mean to encode the concatenation of the triple using an MLP?
- Line 267, It seems that to train $\pi_\theta$ the reward used is given in line 305 defined as the maximum of the observations so far. This part is unclear to me.
  - How is this reward helping in learning a good policy?
  - It seems that the loss function is static given a history H_t, so it is not a RL setup but simply a supervised learning setup. Is any RL specific learning procedure being used here? Are the reward values r_t fixed observations or are they learnable and also backpropagated through to the prediction values y and consequently through the prediction head?
  - This step looks very similar to offline BO where a offline data set is used to learn an acquisition function or a function approximation. What is the relationship of this method to offline BO?
- Line 303, How is the query set constructed when computing $\pi_\theta$? Is it a random subset of all query pairs? Or is any specialized strategy used to locate the most promising queries?
- How is PABBO able to avoid sub-optimal solutions caused due to not exploring the whole optimization space?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a new approach to preferential Bayesian Optimization, using large-scale pretraining to enhance inference speed and optimization performance. PABBO employs two distinct transformer heads: a Prediction Head that captures the underlying function determining preferences, and an Acquisition Head that selects the next query pair. Experimental results show that PABBO outperforms existing methods in accuracy and computational efficiency.

### Strengths
1. The idea of utilizing meta-learning for Amortized Optimization in preferential Bayesian Optimization is new and reduces the cost of inference.

2. Experiment results show that PABBO outperforms other methods in the datasets selected in this paper.

### Weaknesses
1. The pretraining in this method requires a large amount of data, which could be costly for certain tasks.

2. PABBO is currently limited to tasks with a fixed input dimensionality.

3. PABBO only supports pairwise preference queries, limiting its ability to handle queries with multiple options, which could reduce the efficiency of information gathering. While existing works like [1] could handle queries with multiple options.

4. Including more datasets in the experiments would provide a more comprehensive evaluation. For example, incorporating all acquisition functions and tasks from [1] and other related works could strengthen the comparison.

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces the Preferential Amortized Black-Box Optimization (PABBO) approach, which learns acquisition function values for candidate pairs based on preferential feedback between pairs of designs. The method utilizes a transformer-based architecture and a reinforcement learning-based pretraining scheme.

### Strengths
The PABBO architecture achieves end-to-end training for preference feedback and employs an application of amortization within a preferential Bayesian optimization (PBO) setting. The algorithm’s contributions are demonstrated through experiments against Gaussian process-based benchmarks.

### Weaknesses
This paper seems to fall below the standard expected at ICLR for the following reasons:

1. A critical issue is that the paper lacks a theoretical foundation or even a mathematical intuition for its approach, focusing primarily on reporting numerical results without a deeper analytical context.

2. In terms of experiments, the explanation of the architecture design and the choice of hyperparameters requires more clarity and justification. I will outline these concerns in further detail in the questions below.

3. Finally, the paper would benefit from additional polishing. For instance, in line 189, y_{i,1} and y_{i,2} appear without prior explanation. In line 219, the term “P” in “the rest of P queries” may be confusing for readers. In line 718, For in "M=50 For" should be for.

### Questions
About the architecture:
1. Why did you choose the Gaussian distribution in equation (4)? What's the role of the Gaussian distribution in the algorithm's success for the out-of-distribution case in synthetic experiments of section 5.1 and human preferences in section 5.3? Are there any mathematical intuitions?
2. What's the influence of D^{ctxpred} in your training procedure? How do you determine the percentage of D^{ctxpred} and D^{tarpred}?

About the hyperparameters:
1. Why do you fix lambda=1 in all experiments? What's the influence of lambda?
2. In line 500, why do you choose gamma=0.5, 0.9, 0.98, 1.00? These choices seem unusual and may have been selected deliberately, potentially compromising the generality of the results.
3. What's the influence of query budget T?
4. What would high dimensions influence the algorithm? For example, what would happen if you chose the D to be very large in line 719? 

I would be willing to increase the score if the above questions could be well clarified.

### Soundness
3

### Presentation
3

### Contribution
2
