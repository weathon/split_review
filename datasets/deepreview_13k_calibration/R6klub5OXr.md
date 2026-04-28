# An Extensive Analysis on the Underlying Premises Behind Deep Reinforcement Learning Algorithm Design

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
The progress in reinforcement learning algorithm development is at one of its highest points starting from the initial study that enabled sequential decision making from high-dimensional observations. Currently, deep reinforcement learning research has had quite recent breakthroughs from learning without the presence of rewards to learning functioning policies without even knowing the rules of the game. In our paper we focus on the underlying premises that are actively used in deep reinforcement learning algorithm development. We theoretically demonstrate that the performance profiles of the algorithms developed for the data-abundant regime do not transfer to the data-limited regime monotonically. We conduct large-scale experiments in the Arcade Learning Environment and our results demonstrate that the baseline algorithms perform significantly better in the data-limited regime compared to the set of algorithms that were initially designed and compared in the data-abundant regime.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper contributes with theoretical arguments for the non-monotonic performance profiles of different algorithms when constrained to various data regimes. The proofs are concerned either with linear value function approximation or with the general problem of learning the distribution of a random variable or its expected value. It then proceeds to illustrate the theoretical claims empirically, in the context of deep learning algorithms on the Atari 100k.

### Strengths
This contribution adds to the body of work that highlights the difficulties of evaluating RL agents and points to some implicit assumptions that could lead to unwarranted performance claims.

It provides a theoretical argument for why larger capacity models can underperform in a low-data regime (compared to low capacity models) which I found sound as much as I could follow it but which I also find limiting since it only concerns linear value function approximation and, in some respects, it's empirically rendered vacuous by recent work, such as Schwarzer 2023.

Similarly, it reiterates some concerns regarding the merits of distributional RL by employing a statistical argument regarding the difficulty of learning a distribution as opposed to a mean. It should be noted that these concerns appear multiple times in the literature (eg. Lyle 2019 and Bellemare 2023 and even the original Bellemare 2017 paper).

Schwarzer, 2023: https://arxiv.org/pdf/2305.19452.pdf
Lyle, 2019: https://arxiv.org/pdf/2305.19452.pdf
Bellemare, 2023: https://www.distributional-rl.org/

### Weaknesses
I found the theoretical work limiting as it's only concerned with the linear case and therefore it ignores the many optimisation challenges of Deep RL (see Lyle, 2023 for a good example of the difficulties of pinpointing what exact intervention in the algorithm correlates with performance) which could easily dominate the sample complexity for any given data regime.

Furthermore I don't find the empirical work much compelling:

1. The paper repeatedly depicts distributional RL as being inefficient in the low-data regime. While I completely applaud the call for simpler baselines (as the authors are doing) and better ablations, the paper does not include SPR, yet another Rainbow-based, distributional algorithm, that generally was found to outperform most other methods in Atari 100k (see Agarwal 2021 for a solid empirical study and Schwarzer 2023 for recent work that uses SPR as a starting point). Including SPR or any of its variations would invalidate the empirical observation claimed in this paper that in the low-data regime "the performance profile of the simple base algorithm dueling (sic) is significantly better than any other algorithm that learns the state-action value distribution" or, elsewhere, "the simple base algorithm dueling (sic) performs significantly better than any algorithm that focuses on learning the distribution". The strong claim that *any* distributional method is outperformed by dueling is not sufficiently supported by the experiments, especially given the existence of high-performing distributional algorithms on the same benchmark.

2. While I find the claim that algorithms developed in one data regime won't monotonically transfer to other data regimes is generally true, I don't think it is a novel or surprising observation. There are several papers on tuning Rainbow alone (van Hasselt 2019 with DER, Kielak 2019 with OTR, more recently Schmidt et al) that make this exact point, that various data constraints will require essentially different algorithms. The observation that hyperparameter tuning is needed across different data regimes is well-established, and the paper's claim of non-monotonic transfer seems to be a restatement of this fact, rather than a novel insight. The provided evidence does not sufficiently demonstrate that the performance profiles are non-monotonic in a way that is not already implied by the need for data-specific hyperparameter tuning.


### Questions
1. Any reasons for not including SPR in the empirical evaluation?
2. If the aim is to illustrate the large sample complexity of distributional RL in the low-data regime, why not pick the best performing distributional algorithm on Atari 100K, replace the objective with the expected version and fine tune both to see if there is a difference indeed.
3. I couldn't find details on how Figure 3 was generated. A short description of the experiment in the main body followed by detail in the annex would help.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper theoretically shows that:
-  for finite horizon Markov decision processes (MDP) with linear approximation, lower (resp. higher) capacity function approximation can lead to lower regret in low-data (resp. high-data) regime.
- distribution-based algorithms may have higher sample complexity.
In addition, it empirically demonstrates that:
- higher capacity models (e.g., distribution based or higher dimension) may perform well in high-data regime, but lower capacity models can perform better in low-data regime.
- dueling DQN performs best in low-data regime and better than distribution-based algorithms.

### Strengths
The authors propose a theoretical formalization showing that lower-capacity models can perform better than higher-capacity models in low-data regime, while the opposite holds in high-data regime.

The experimental results validate the theoretical results.

### Weaknesses
I feel that the result that larger-capacity models require more data to be trained properly is quite evident (although a theoretical proof in the finite horizon MDP setting is appreciated). For instance, I think the paper proposing DER (data-efficient rainbow), which the authors cite, also somewhat acknowledges this fact and consequently tries to improve the sample complexity of rainbow with various tricks to make it perform better in the low-data regime.

I believe the title is too broad and don't clearly reflect the content of the paper. I would strongly suggest the authors to consider changing the title to mention their focus on the low vs high data regime.

I find the presentation a bit confusing in my first read. For instance, Section 2 introduces the infinite horizon case, while Section 3 considers the finite horizon case with slight different assumptions and notations (e.g., stochastic policy vs deterministic policy, discounted vs undiscounted, stationary MDP vs non-stationary,…). See below for some specific examples of issues.
I would suggest the authors to start Section 3 by emphasizing the difference with Section 2 and mentioning that they follow the framework proposed by Zanette et al., 2020.

Presentation and formalization issues:
The formalization of an MDP is a bit strange and not rigorous:
\mathcal P is directly defined as a probability distribution over S x A x S.
\rho_0 is not defined.
\pi(s, a) is not a map from states to actions. Moreover, the notation doesn't fit the mapping \pi : S \to \Delta(A).
The expected cumulative discounted rewards R is not very well defined, since s_{t+1} is also a random variable that depends on a_t.

The notations in (2-5) should be recalled. The definition of Q_\beta should be checked.

In Section 3, why the probability kernel \mathcal P_t depends on t? Same question for \mathcal R_t. This point was not mentioned in the definition of a finite horizon MDP, just above.

Is the discount factor missing in (6)? If not, it may be worthwhile to clearly specify that in the finite horizon case, the total reward criterion is used to avoid any confusion for the reader.

Above (8): Notation \theta_t \in d_t is incorrect.

Regarding \mathcal Q_t(\theta_t)(s_t, a_t), why not write it as \mathcal Q_t(s_t, a_t; \theta_t) like in Section 2?

The definition of the intrinsic Bellman error should be recalled.

Top of page 4: Typo: dimesions

The last sentence before Section 4 is too broad in my opinion. If the algorithms are compared using models with similar capacity, I think the comparison is fair.

Page 7: I find the first paragraph quite hard to understand. First of all, the authors should cite the original reference when mentioning an algorithm for the first time. For instance, DRQ^{ICLR} does not have any reference.
Agarwal et al., 2021 write "for DrQ, we used the source-code obtained from the authors". Does DRQ^{NeurIPS} refers to their DrQ(\epsilon)?
Also, as far as I know DrQ does not use the dueling architecture.

Fig. 3 (right) seems not be commented in the text.

*Edit:* After reading all the reviews and the rebuttal, I believe that most of the weaknesses I raised still hold.

### Questions
The interpretation of Prop. 4.1 is not clear to me. I understand Prop. 4.1 as follows: Even a small total variance error may lead to incorrect order over actions. However, the last sentence after this proposition seems to say: if the total variance error is not small, then there may be an incorrect order over actions. Did I misunderstand something?

What is DRQ^{NeurIPS}?

Does DRQ^{ICLR} use the dueling architecture?

### Soundness
2 fair

### Presentation
2 fair

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
The authors question a common assumption in low-data RL research that suitable baselines are the best-performing RL algorithms in high-data RL research (with tuned hyperparameters). They derive a theorem in the linear function approximation setting that shows that lower capacity function approximators (with larger approximation error) can outperform larger capacity models (with smaller approximation error) in the low data regime. They then gather results with a range of standard DRL methods on the Atari 100k benchmark to show their findings extend empirically to current research on DRL.

### Strengths
The authors question a common preconception in the RL community, which is always good to check. After providing the requisite background on the general settings and specific algorithms, they go on to prove their claim in the (linear) function approximation setting. And finally, the authors show that this holds with DRL algorithms on the benchmark that researchers are currently using, with appropriate consideration of changes in hyperparameters for the reduced sample complexity regime.

### Weaknesses
The authors only focus on DQN variants, and in particular, the form of the value function learned. The more expressive the value function, the better it does asymptotically, but the worse it does in the low-data regime. This therefore calls into question how general their claims are.

### Questions
Could you provide more clarity regarding how far your theory and results apply only to the form of value function (scalar vs. various forms of distributional)? It would be useful to be clearer about what the scope of the paper is, because the title and abstract make very general claims about the "data-abundant regime" and the "data-limited regime", whilst the latter half of the paper is restricted to DQN variants.

**Edit:** I have read the other reviews, the authors' feedback, and the updated paper. I believe the authors were able to address some questions, but I feel there is a still mismatch between the generality of the claims and the experiments, which focus on scalar vs. distributional value functions. As such, I will retain my original rating.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper promises to provide an extensive analysis on underlying premises behind RL algorithm design. Specifically, it promises to use the low and high data regime as explanation. It provides a theoretical analysis, and it provides experiments with a small number of algorithms.

### Strengths
An analysis of the difference between large and small experiments would be quite useful, and could provide insight into whether small experiments can be used to predict large-regime outcomes.

### Weaknesses
It appears to fulfil this promise, although questions remain. It does not explain the reason behind lo/hi data regime performance of different classes of algorithms. The theoretical results are unconvincing, there is no reason given why proposition 4.2 explains the algorithmic behaviour. The experiments do not provide enough detail (hyperparameters, seeds) to see if the reported differences in performance are statistically significant. The writing style is full of hyperbole, and repetitive. No convincing insight is provided in this paper. 
The writing of the capital Q is non-standard and distracting.

### Questions
Anonymous Code is not available. 
Can you please provide this?

Can you explain the conclusions that you draw based on the theoretical analysis?

Can you please explain the choice of algorithms?

Can you please tone down the claims in the text, to make them more in line with a regular paper?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
