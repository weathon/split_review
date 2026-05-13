# L(M)V-IQL: Multiple Intention Inverse Reinforcement Learning for Animal Behavior Characterization

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
In the pursuit of comprehending decision-making, behavioral neuroscience has made significant progress, aided by mathematical models in recent years. Among various approaches, Inverse Reinforcement Learning (IRL) stands out as a promising technique, distinguishing itself from other paradigms through its ability to circumvent the necessity for a reward function in characterizing observed behavior. Nevertheless, the widespread adoption of IRL within the field of neuroscience remains limited. This constraint may be attributed, in part, to the prevailing assumption in many existing IRL frameworks that animals exhibit a singular intention throughout a given task, wherein their behavior is optimized based on a single static reward function. In an effort to overcome this limitation, we propose the class of Latent (Markov) Variable Inverse Q-learning (L(M)V-IQL) algorithms, a novel IRL framework designed to accommodate multiple discrete intrinsic rewards. We formulate an Expectation-Maximization approach to cluster observed trajectories into multiple intentions, and subsequently solve the IRL problem independently for each intention. We illustrate the application of L(M)V-IQL through simulated experiments, followed by its utilization on a dataset of mice engaged in a two-armed bandit task. Our methods exhibit exceptional proficiency in discerning animal intentions and yield interpretable reward functions corresponding to each identified intention. We anticipate that this progress will open up new possibilities in neuroscience and psychology, serving as an important advancement in elucidating the intricacies of animal decision-making and uncovering underlying brain mechanisms.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This method, LMV-IQL, seeks to extend a class of IRL algorithms to the case of multiple intrinsic rewards, applied to behavioral modeling in neuroscience. They first identify each intention / reward and then solve for each. They demonstrate their method on both simulated and experimental datasets.

### Strengths
The text is well written, particularly when defining theorems and the algorithmic steps. It would be a definite strength to extend IRL approaches to the regime of multiple unknown (intrinsic) reward functions or internal motivation states.

### Weaknesses
Some of the figures need additional details/components. E.g., Figure 1, 2 need color scalebars, Figure 3 would benefit from some explanation of the legend (where are the red and blue squares?), the colors on the state labels in Figure 4C are unnecessary and uncorrelated with the colors in the legend, ... 

Definitions of the comparison methods were weak. For example, 'IAVI was further extended to the sampling-based model-free Inverse Q-learning (IQL) algorithm' with no citation or explanation of how the authors of this paper implemented those algorithms, is insufficient. It is unclear what specific modifications or implementation choices were made to adapt IAVI to a model-free setting, and how this compares to existing model-free IRL methods.

Similarly, the primary metric, EVD, is cited but not defined. The lack of a clear definition makes it difficult to assess the significance of the reported results and compare them with other studies that may use different metrics. The reader is left to guess what the specific calculation of EVD entails.

The authors only show an improvement over IAVI and IQL, and do not compare these other methods (including LV-IQL, which performed the same on the simulated dataset) in the experimental dataset. The absence of comparisons with other state-of-the-art methods on the experimental data limits the impact of the study. The fact that LV-IQL performed the same as LMV-IQL in simulation suggests that the additional complexity of LMV-IQL is not justified without a more thorough comparison on experimental data.

### Questions
The authors motivate their method as extending beyond a single reward function, but then apply it only to the case of 2-3 rewards/intentions/states. Can this be extended easily to more than a small number?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an expectation-maximization approach for multi-goal IRL based on the inverse Q-learning IRL method. The approach involves clustering trajectories into multiple intentions and independently solving the IRL problem for each intention. The authors evaluate their algorithm using both simulated experiments and real-world mice data.

### Strengths
The problem of multi-goal IRL is highly relevant and its applications to cognitive science have been sparse in the past. I therefore particularly appreciate the application to the cognitive science domain to interpret real mice data.

The introduction of a multi-goal approach based on the inverse Q-learning algorithm seems novel and holds the promise of potentially outperforming previous multi-goal IRL methods.

The paper is well-structured and easy to follow, contributing to its readability and comprehensibility.

The algorithm's application to real mice behavioral data demonstrates its practical applicability in real-world scenarios.

### Weaknesses
The most significant weakness of the paper is the lack of discussion regarding related work on multi-goal IRL. Despite the existence of numerous prior works in this field (e.g., [1-6]), the paper does not reference or discuss any of them. The absence of a comparison with existing methods raises questions about the true novelty and contribution of the proposed approach. The paper should explicitly highlight what sets its method apart and how it compares to the existing literature. Especially works [4-6] previously approached the multi-goal IRL problem with an expectation-maximization approach, even though inverse Q-learning was not used as backbone algorithm.

### Questions
How does your approach compare to previous multi-goal IRL methods, especially those mentioned in the references [1-6]? It is crucial to provide a detailed comparison to establish the uniqueness and advantages of your proposed method in light of the existing literature.


-----
I appreciate the additional discussion of past work provided by the authors. For me, the main problem is still that this work is conceptually very close to past multi-objective IRL approaches. Finally, they have added a discussion of related work, but they still claim their model with latent intention states and EM as their new contribution. It seems to me that their approach is basically the same as older work (after careful rereading, the closest is probably [7]), but the original IRL approach was swapped out for IAVI or IQL to support non-linear reward functions and have a model-free variant. I do not think there's anything wrong with that, and I think work showing that this combination works could still make a good paper and be useful to the community. However, I would have liked to discuss these close connections to other approaches with the authors to assess the actual novelty and ensure that the work is not overstated. I know that there is limited time in the rebuttal phase to make improvements, and they used that time well to add a schematic overview of previous algorithms. However, I do not like that they initially did not address past methods at all and provided this discussion on the last day of the rebuttal phase, which made a real discussion and improvement of the paper impossible. Therefore, I would suggest the authors make their paper clearer in terms of its true novelty and resubmit it so that a discussion with the reviewers can take place. I will still increase my rating to a 5.

[7] Nguyen, Q. P., Low, B. K. H., & Jaillet, P. (2015). Inverse reinforcement learning with locally consistent reward functions. In Advances in neural information processing systems, 28.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work considers an inverse reinforcement learning model (IRL) with latent discrete intention variables. Using an inverse Q-learning and EM-based approach, they perform inference on these latent variables at each time based on either generalized Bernoulli or Markovian dynamics, learning both the transition dynamics between intentions (in the Markov case) and their corresponding reward functions. Experiments involve recovery on simulated data and from behavior in mice performing a two-alternative forced choice task with randomly changing reward structure.

### Strengths
- Intriguing generalization of inverse RL methods to neuroscience.
- Well-motivated incorporation of latent drives.

### Weaknesses
 - The fitted model is somewhat simplistic. Latent states are assumed to be multinomial or Markov, but the most plausible biological assumption would be that transitions between drives also interact with reward/satiety/recent history.
- There are only two experiments: one on simulated data (where it is) compared to IAVI and IQL but not the Ashwood et al. or other similar models that might be applicable. Similarly, the mouse behavior is quite limited in terms of the need for RL. Again, the Ashwood Nature Neuro paper or the Ebitz, Albarran, and Moore (2018) provide fairly flexible models that are likely to capture the data as well. Given the synthetic data, one would have expected a more challenging task here as a target for IRL.

### Questions
- Is it possible to incorporate some recent reward history into the transition structure? Since the inference algorithm is EM, will any EM-compatible latent variable model work, in principle?
- Where are the bottlenecks for the method in terms of inferential complexity? Is the limiting factor the IAVI regression (i.e., the size of the tabular problem) or the EM complexity?

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this work, the Authors propose a novel algorithm for discerning and characterizing multiple intents underlying natural behaviors. To this end, they combine the inverse Q-learning (a version of IRL) with the expectation-maximization algorithm used to delineate the intents. The Authors consider two types of dynamics in their framework: the Bernoulli process and the Markov process; they provide theoretical derivations and describe implementations for both. They then test their framework on a simulated task (a gridworld with 2 underlying intentions) where they show the framework’s ability to recover the ground truth, and on an existing mouse dataset (a bandit reversal learning task) where they reconstruct and describe mouse intents.

### Strengths
A definite strength of this work is that it has been anticipated in the field. As a continuous-time model for multiple intent reconstruction has been developed by Ashwood et al (NeurIPS 2022; referenced in current manuscript), a question that has been repeatedly raised was about the discrete version of the framework. This question has become especially relevant after another work by Ashwood et al (Nat Neurosci 2022; also referenced in current manuscript) that used large-scale IBL data to propose that natural behaviors can be represented via an MDP featuring rapid progression of discrete states. This ICLR submission delivers on that expectation.

The model in the paper is well-founded; it features reasonable choices of the constituting algorithms (e.g., the Baum-Welch algorithm for discerning the intents).

Having the analysis for both simulated and animal data is a plus.

### Weaknesses
Along the same line with the strengths, I see the main weakness here in high similarity to Ashwood et al (NeurIPS 2022) work. The Authors mention in the Appendix that the aforementioned approach “is limited to capturing continuous intra-episode variation of reward functions during navigation behavior, and difficult to adopt to other environments” but, should that be true, that requires further substantiation. The data analyses offered in this paper seem to mainly serve as a proof of principle for the proposed model.

Overall, the work is nicely done and well-timed; my only concern is that the high similarity to prior literature determines the work’s novelty which may be insufficient for ICLR. With that said, I’m open to comments by the Authors, other Reviewers, and the Area Chair in that regard.

-Introduction: wouldn’t it make more sense to introduce your work via Ashwood et al, 2022a and 2022b papers? I feel like this way the reason for the development of your model and the comparison to the existing state-of-the-art would be more transparent.

-Page 5 under Equation 10: what does Delta Z mean? Is it supposed to reflect the available transitions?

-Page 6 under Figure 3: why is it necessary to punish the types of reward irrelevant to the intentions? A more natural way seemingly would be to set them equal to zero. I assume this natural way hasn’t worked out for some reason?

-Figure 4A: why does the LL in the training curve drop? That is unlikely to be explained by overfitting as suggested in the text.

-Page 7 bottom line: “Although model performance continued to improve slightly with more latent states, we will focus […] on […] 3 states”. Wouldn’t it be easier to make this argument by using the Bayesian Information Criterion instead of the pure NLL to choose K? This way one can arrive at a principled number of intents that very well may turn out to be equal to 2.

-Figure 5C. Following up on my previous point, this figure leaves me with the impression that the third intent is just spurious (not stable; immediately reverses to the first intent). Could you please comment on why you consider it important?

Minor comments:

-Figure 3: the overlap of the crosses (x) and dots ( . ) is hard to follow. Could you please use an alternative way to represent this data?

I’d also suggest tuning down a couple of literature-related claims:

-Page 2: “[IRL’s] adoption as mathematical behavior models in neuroscience research has been relatively limited”. I had another impression – it seems to be an up-and-coming tool, as exemplified by some awesome works from Jon Pillow’s and Xaq Pitkow’s groups.

-Page 2: “[our method presents a […] framework for characterizing the delicate balance between exploration and exploitation […] which constitutes a […] comparatively understudied aspect within the realm of neuroscience.” I’d say that, first, there’s a huge spillover from the machine learning field of intrinsic motivation (a.k.a. an internal reward for exploration); many of these works claim biological plausibility. There are some other nice works, e.g. Pisupati et al (eLife 2021) and references therein that directly address the issue. There’s also lots of work on Bayesian optimality that study the deviations from optimal exploitation to account for the environmental dynamics, e.g. Yu and Cohen (NeurIPS 2008).

-Page 4: “In behavioral neuroscience, it is commonly considered that animals alternate between multiple intentions under the Markov property”. The entire reason why the Ashwood et al (Nat Neurosci 2022) paper cited there emerged is because that’s _not_ how people used to characterize natural behaviors. This is reflected literally in the first sentence of the said paper. While this new work has gotten substantial traction in the field, I wouldn’t say that that new way to model data has completely wiped out the conventional approach.

### Questions
-Introduction: wouldn’t it make more sense to introduce your work via Ashwood et al, 2022a and 2022b papers? I feel like this way the reason for the development of your model and the comparison to the existing state-of-the-art would be more transparent.

-Page 5 under Equation 10: what does Delta Z mean? Is it supposed to reflect the available transitions?

-Page 6 under Figure 3: why is it necessary to punish the types of reward irrelevant to the intentions? A more natural way seemingly would be to set them equal to zero. I assume this natural way hasn’t worked out for some reason?

-Figure 4A: why does the LL in the training curve drop? That is unlikely to be explained by overfitting as suggested in the text.

-Page 7 bottom line: “Although model performance continued to improve slightly with more latent states, we will focus […] on […] 3 states”. Wouldn’t it be easier to make this argument by using the Bayesian Information Criterion instead of the pure NLL to choose K? This way one can arrive at a principled number of intents that very well may turn out to be equal to 2.

-Figure 5C. Following up on my previous point, this figure leaves me with the impression that the third intent is just spurious (not stable; immediately reverses to the first intent). Could you please comment on why you consider it important?

Minor comments:

-Figure 3: the overlap of the crosses (x) and dots ( . ) is hard to follow. Could you please use an alternative way to represent this data?

I’d also suggest tuning down a couple of literature-related claims:

-Page 2: “[IRL’s] adoption as mathematical behavior models in neuroscience research has been relatively limited”. I had another impression – it seems to be an up-and-coming tool, as exemplified by some awesome works from Jon Pillow’s and Xaq Pitkow’s groups.

-Page 2: “[our method presents a […] framework for characterizing the delicate balance between exploration and exploitation […] which constitutes a […] comparatively understudied aspect within the realm of neuroscience.” I’d say that, first, there’s a huge spillover from the machine learning field of intrinsic motivation (a.k.a. an internal reward for exploration); many of these works claim biological plausibility. There are some other nice works, e.g. Pisupati et al (eLife 2021) and references therein that directly address the issue. There’s also lots of work on Bayesian optimality that study the deviations from optimal exploitation to account for the environmental dynamics, e.g. Yu and Cohen (NeurIPS 2008).

-Page 4: “In behavioral neuroscience, it is commonly considered that animals alternate between multiple intentions under the Markov property”. The entire reason why the Ashwood et al (Nat Neurosci 2022) paper cited there emerged is because that’s _not_ how people used to characterize natural behaviors. This is reflected literally in the first sentence of the said paper. While this new work has gotten substantial traction in the field, I wouldn’t say that that new way to model data has completely wiped out the conventional approach.

________________________________________________________________________________
post-rebuttal:

I would like to thank the Authors for their clarifications. I appreciated the fast, detailed responses.
Posting my final response here as, at this time, I cannot otherwise make it visible to the Authors.

I believe that the updated manuscript is a more solid, transparent, and substantiated work.
The most interesting finding to me is that new priors here allowing for abrupt changes of goal maps, enabled by the novel problem formulation, optimization objective, and solver, were more consistent with the mouse decision-making data in the maze experiment than DIRL (the previous SOTA), rendering the proposed model important. I would also like to thank the Authors for the clarification that the choice of different smoothness prior in DIRL would not necessarily be able to recover the same dynamics, necessitating the formulation of the problem in the way proposed here.

Despite the similarity to prior work, this is an important and interesting result. I increased my score to reflect it.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
