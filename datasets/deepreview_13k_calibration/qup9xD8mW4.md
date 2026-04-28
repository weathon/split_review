# Behaviour Distillation

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8

## Abstract
Dataset distillation aims to condense large datasets into a small number of synthetic examples that can be used as drop-in replacements when training new models. It has applications to interpretability, neural architecture search, privacy, and continual learning. Despite strong successes in supervised domains, such methods have not yet been extended to reinforcement learning, where the lack of a fixed dataset renders most distillation methods unusable.
Filling the gap, we formalize \textit{behaviour distillation}, a setting that aims to discover and then condense the information required for training an expert policy into a synthetic dataset of state-action pairs, \textit{without access to expert data}. 
We then introduce Hallucinating Datasets with Evolution Strategies (HaDES), a method for behaviour distillation that can discover datasets of \textit{just four} state-action pairs which, under supervised learning, train agents to competitive performance levels in continuous control tasks.
We show that these datasets generalize out of distribution to training policies with a wide range of architectures and hyperparameters. We also demonstrate application to a downstream task, namely training multi-task agents in a zero-shot fashion.
Beyond behaviour distillation, HaDES provides significant improvements in neuroevolution for RL over previous approaches and achieves SoTA results on one standard supervised dataset distillation task. Finally, we show that visualizing the synthetic datasets can provide human-interpretable task insights.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new branch of dataset distillation - behaviour distillation. Behaviour distillation aims at distilling a set of synthetic RL dataset without having access to the expert data. The authors handles indifferentiability of the formulation using evolution strategy, and show good performance.

### Strengths
+ The introduction of behaviour distillation can enrich the literature and direction of Dataset Distillation. Different from standard DD, behaviour distillation does not require access to the expert datasets. This is quite close to a standard /basic RL setting and could be a good starting point.

+ The author's writing is easy to follow and pretty clear on the technical details

+ The experimental section show promising results using the proposed algorithm HADES.

### Weaknesses
 - Although it is interesting, the proposed behaviour distillation seems to not have a clear motivation on why it can be useful (what's the motivation for proposing this problem and it's potential application, besides DD hasn't been applied to RL), and why not directly formulating the problem on expert dataset. Distilling directly from scratch can make the problem a lot harder.
- It would be great if the authors can discuss the behaviour difference of a standard RL algorithm and a synthetic data-driven RL algorithm (HADES). What's the potential benefits?
- One missing citation on BPTT [2]. It would be nice to add some discussion on optimization algorithm in DD, for example BPTT (the original one[1] and momentum-based[2]).

### Questions
See above.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This manuscript proposed a behavior distillation algorithm of HaDES that aims to distill a few synthetic (state, action) pairs ($\mathcal{D}_\phi$) in the reinforcement learning (RL) setting, and the network can fastly learn a satisfied policy by training on the small distilled dataset. Concretely, the authors firstly formulate that behavior distillation problems as a bi-level optimization where the inner loop optimizes the policy network parameters by supervised learning on distilled data, while the outer loop maximizes the cumulative reward ($J$) w.r.t. the RL task.  Then, synthetic (state, action) pairs are optimized by gradient ascent where  the gradient is estimated by evolution strategies (ES). The authors verified that distilled dataset outperform vanilla ES algorithm on multiple RL datasets including Brax and MinAtar exvironments.

### Strengths
This paper first introduces the dataset distillation into the RL setting, and the core pros of this paper are presented as below:

1. Formulate the behaviour distillation by incorporating dataset distillation with an RL reward function;

2. Propose a novel behaviour distillation algorithm of HaDES that learns a few (state, action) pairs to fastly train a policy network with supervised learning;

3. Multiple empirical studies are conducted to verify the effectiveness and robustness of the synthetic behaviour dataset.

### Weaknesses
While the authors creatively incorporate dataset distillation into RL setting, there are some weaknesses mainly lie on the motivation and experiments, which hurt the contribution of this manuscript. 

**Q1:** Sec. 1 states that this work is "motivated by the challenge of behaviour distillation", while this (challenge) is not a clear motivation for developing the behaviour distillation. What is the advantages of using the distilled dataset in RL except for fast training? In my opinion, the networks in RL are often small and do not require long time training. It is unclear why the authors focus on training speed when RL networks are typically not the bottleneck.

**Q2:** While I am not an expert in RL, I note that the authors employ different networks to run HaDES and the vanilla ES baseline due to "memory constraints" so that HaDES outperforms vanilla ES, while synthetic datasets often largely underperform the real data in dataset distillation. It will be more reasonable to compare HaDES and vanilla ES under the same experimental settings. Moreover, it will make this work more convincing to add the results of other RL methods instead of only ES. The comparison is not fair due to the different network sizes, and the lack of comparison to other RL methods makes it difficult to assess the true value of this approach.

**Q3**: There lack of experiments investigating the influence of the distill budget (the size of the distlled dataset) on the final performance. Without this analysis, it is hard to know how the size of the distilled dataset affects performance, and what the tradeoff is between dataset size and performance.

**Q4**: It will make this work more comprehensive if there is an analysis of efficiency. In detail, the author can list the GPU time of behaviour distillation, training on distilled dataset, vanilla ES and other RL methods, which can further highlight the importance of behaviour distillation. The current lack of runtime analysis makes it difficult to evaluate the practical benefits of the approach, especially given that RL training is often computationally intensive.

Based on these observations, I think this manuscript is marginally below the acceptance, but I would like to increase my rating if the above questions are well addressed. Below are some minor questions and typos.

---

Minors and typos:
1. The term Behavior Distillation has already been used in [1], which is borrowed from the concept of knowledge distillation instead of dataset distillation. The authors should discuss this to avoid ambiguity.

2. The algorithm 1 should be placed in the main text for clear illustration.

2. Page 2: "scaling independently" -> "scaling independence"

3. Page 2: "policy, reducing" -> "policy, thereby reducing"

4. Page 3: "train a model faster" -> "train a model fastly"

5. Page 4: The formulation of dataset $\mathcal{D}$: "$\mathcal{D} = \{x_i, y_i\}$" -> "$\mathcal{D} = \{x_i, y_i\}_{i=1}^N$"

6. Page 5: this first line: ", i.e. " -> ", i.e., "

7. Page 5: there exists an extra right bracket in Eq. (3)

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors attempt to transfer the concept of dataset distillation to the realm of reinforcement learning. To that end, they introduce the concept of behaviour distillation, which is trying to condense a dataset of state-action pairs required for training a RL agent. After introducing this concept, they propose a new method named HADES, that implements this concept and is able to distill the initial state-actions pairs into a dataset of just four state-action pair that, when trained upon by an agent can make it reach competitive performance.

### Strengths
- Transfer the concept of dataset distillation to reinforcement learning
- The condensed dataset can result in a quite small one
- The results on supervised classification dataset distillation also seem good

### Weaknesses
 - 1) I think the neuroevolution part is quite distinct from the dataset distillation part. It should be explained clearly why you need to use a neuroevolution technique instead of a more classical technique
- 2) Maybe the naming is a bit confusing, if the method proposed is meant to distill the dataset only (and not train on it later), then it would be clearer to name the experiments as Method + HADES (whenever training a method on top of hallucinated dataset).
- 3) If I understood correctly, one advantage of HADES is that it can distill behaviour by looking at some subpart of the episode (like 1/10th), and condense the gathered state-action pairs into much smaller dataset. However, from the rest of the paper, it's not clear whether they are some computational advantages of training on top of these condensed dataset. They should be made clearer. Indeed, by looking at the RL plots, in most of the cases, it's not clear if the red curve trains way faster than the green curve (apart from a few environments like humanoid and breakout-miniAtari

### Questions
- 1) If I understand correctly, HADES first distills a dataset into a condensed state-action pair and then trains a classical policy on it (as in classical dataset distillation). What I don't understand is the link with the neuroevolution part. Is this part requires only for distillation or is it also required for training on top of the distilled dataset ? In the latter case, it would be interesting to see how other methods that do not use neuroevolution perform when trained on the condensed dataset.
- 2) In the results plot of reinforcement learning, does the number of generation directly correlates to the training time ? Or are some generations quicker to run for methods trained on condensed dataset (that implies the inner loop would be faster I guess) ? I think the computational advantage of training on top of condensed dataset (if any) should be made clearer

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
