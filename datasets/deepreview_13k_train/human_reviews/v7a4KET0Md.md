# Inverse Reinforcement Learning with Switching Rewards and History Dependency for Characterizing Animal Behaviors

- Decision: Reject
- Scores: 6, 3, 3

## Abstract
Traditional approaches to studying decision-making in neuroscience focus on simplified behavioral tasks where animals perform repetitive, stereotyped actions to receive explicit rewards. While informative, these methods constrain our understanding of decision-making to short timescale behaviors driven by explicit goals. In natural environments, animals exhibit more complex, long-term behaviors driven by intrinsic motivations that are often unobservable. Recent works in time-varying inverse reinforcement learning (IRL) aim to capture shifting motivations in long-term, freely moving behaviors. However, a crucial challenge remains: animals make decisions based on their history, not just their current state. To address this, we introduce SWIRL (SWitching IRL), a novel framework that extends traditional IRL by incorporating time-varying, history-dependent reward functions. SWIRL models long behavioral sequences as transitions between short-term decision-making processes, each governed by a unique reward function. SWIRL incorporates biologically plausible history dependency to capture how past decisions and environmental contexts shape behavior, offering a more accurate description of animal decision-making. We apply SWIRL to simulated and real-world animal behavior datasets and show that it outperforms models lacking history dependency, both quantitatively and qualitatively. This work presents the first IRL model to incorporate history-dependent policies and rewards to advance our understanding of complex, naturalistic decision-making in animals.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces SWIRL (SWItching IRL), a novel framework that extends inverse reinforcement learning (IRL) by incorporating time-varying, history-dependent reward functions to model complex animal behaviour. Traditional IRL methods often assume a static reward function, limiting their ability to capture the shifting motivations and history-dependent decision-making observed in animals. SWIRL addresses this limitation by modelling long behavioural sequences as transitions between short-term decision-making processes, each governed by a unique reward function. It incorporates biologically plausible history dependency at both the decision level (transitions between decision-making processes depend on previous decisions and environmental context) and the action level (actions depend on the history of states within a decision-making process). The authors apply SWIRL to simulated data and two real-world animal behaviour datasets, demonstrating that it outperforms existing models lacking history dependency, both quantitatively and qualitatively. They also highlight connections between SWIRL and traditional autoregressive dynamics models, arguing that SWIRL offers a more generalized and principled approach to characterizing animal behaviour.

I think this is a very interesting and well-written paper. I gave a score of 6 but I am willing to reconsider this score if the authors can adequately address my concerns, particularly regarding the methodological details, hyperparameter selection, and theoretical analysis.

### Strengths
- **Originality/innovation**: The paper presents a novel extension to IRL by incorporating history-dependent reward functions, addressing a significant gap in modelling complex, naturalistic animal behaviours. This is the first IRL model to integrate both decision-level and action-level history dependency.
- **Quality/empirical validation**: The authors provide a thorough mathematical formulation of SWIRL, including detailed explanations of how history dependency is incorporated at different levels, and a clear demonstration of improvements over baseline methods. The choice of the authors to use both simulated and real-world datasets strengthens the validation of their approach.
- **Clarity**: The paper is generally well-written, with clear explanations of the concepts and methods. The connection drawn between SWIRL and traditional autoregressive dynamics models helps to contextualize the work within existing literature.
- **Significance**: The SWIRL framework offers a more accurate model of animal decision-making. Hence, I believe it has the potential to advance our understanding in neuroscience and behavioural science, opening up new ways for analysing long-term, complex behaviours driven by intrinsic motivations. Finally, the presented experiments are (in theory) reproducible with public datasets and publicly available code.

### Weaknesses
 - **Methodology**: Some aspects of the implementation, such as hyperparameter selection and the specifics of the inference algorithm, are not fully detailed. Providing more information on these would enhance reproducibility and allow for better assessment of the method. There is limited analysis on hyperparameter sensitivity or discussion of how to choose the history length L in practice. In addition, the impact of number of hidden modes is not thoroughly explored. Finally, there is a lack of a theoretical analysis that would strengthen the paper, such as providing convergence guarantees, a discussion on optimality conditions.
- **Scalability**: The computational complexity of SWIRL, especially with history dependency and the EM algorithm, may pose challenges for large datasets. The paper would benefit from a discussion on scalability to larger state/action spaces and potential optimization strategies. Could also benefit from runtime comparisons with baseline methods.
- **Biological plausibility**: While the model is said to incorporate biologically plausible history dependency, the paper could provide more evidence or discussion on the biological validity of the specific mechanisms used.

### Questions
- **History length**: How does the choice of history length L in the action-level dependency affect the performance of SWIRL? Did you experiment with values beyond 1 and 2, and if so, what were the findings? What trade-offs did you observe between increased history length and computational complexity? What guidelines would you suggest for choosing L in practice?
- **Computational complexity**: Can you provide more details on the computational complexity of SWIRL compared to baseline models? How does it scale with the size of the dataset and the length of the history dependency? Could you provide specific runtime comparisons on the datasets used in the paper? Additionally, can you provide insights into the convergence properties of the EM algorithm?
- **Hyperparameter selection**: How were hyperparameters, such as the temperature parameter α in the soft-Q iteration, selected? Was any hyperparameter tuning performed, and if so, what criteria were used? Did you employ any cross-validation procedures to ensure the robustness of the results? How sensitive is the model to the choice of initial parameters?
- **Limitations**: Could you elaborate on any limitations of SWIRL in modelling certain types of animal behaviours? Are there situations where history dependency might not adequately capture the decision-making processes? How might SWIRL perform on behaviours with very long-term dependencies that extend beyond the history length L? Also, does this framework work in both discrete and continuous state/action spaces?
- **Robustness to noisy data**: How does this framework handle noisy or incomplete data, which are common in real-world animal behaviour datasets? Did you assess the robustness of the model under such conditions?
- **Minor:** line 83: In the experiment "section?" - or "In the Results section,"
- **Discussion suggestion:** Could this framework be used to provide evidence whether models of intrinsic reward (e.g. expected free energy or empowerment) are indeed able to capture animal behaviour?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper addresses the problem of inverse RL in a hidden-mode MDP, i.e. an MDP with an additional hidden-mode parameter that affects the reward. The authors propose an EM-style algorithm that learns both the reward function/policy and hidden mode in the given expert trajectories.
The authors then validate their approach on a synthetic gridworld task and go on to use it to model animal behavior in a rat maze, where the hidden mode represents the rat's current objective (i.e. get water, explore, go home).

### Strengths
* The method seems to work well and produces nicely interpretable result on the real world dataset.
 * The paper is well written and reads quite nicely.

### Weaknesses
 * The literature review is limited. For example, a different interpretation for this problem setting would be a POMDP, for which previous IRL literature exists, e.g. [1]. Yet another interpretation of the mouse experiments would be a hierarchical RL setting, for example an Option setting in which options might be "get water" "explore" "go home". For this setting previous IRL method exist as well, e.g. [2]. I'm not sure if they are directly applicable to this paper's problem setting, but I think they might be applicable?
 * The method seems to be limited to relatively small discrete state and action sets, limiting it's general applicability.

**Experiments**
 * The most competitive baseline was labeled as "I-1" in plots, while the poorly performing baselines are labeled with their names. This might lead to it being confused as the author's contribution and is thus highly misleading and should definitelyl be corrected.
 * It is not clear how often each experiment was run, or how the box plots were created. How were outliers selected? Figure 3E eliminates the best result for baseline I-1.
 * It is also not clear what shaded areas in Figure 4B represent.
 * The MaxEnt baseline is missing in Figure 4? Why?

Minor points
 * L453 refers to an appendix which seems to be missing?
 * L202 $\xi$ is never defined in the paper?

### Questions
* Why is the problem modelled as a hidden-mode MDP rather than a POMDP or Hierarchical RL setting?

Overall I think this paper has potential, and if the issues with the experimental validation and related work discussed above are corrected I would be happy to increase my score.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a framework called SWIRL that extends traditional IRL to capture the complex, long-term decision-making processes of animals in natural environments. SWIRL incorporates biologically plausible history dependency at both the decision-level and action-level, allowing it to better account for how past decisions and environmental contexts shape current behavior. The algorithm is evaluated on both synthetic and real-world datasets.

### Strengths
This work is well motivated by recent advances in applying IRL methods for characterizing animal complex behavior. By incorporating history-dependent policies and rewards, SWIRL outperformed the state-of-the-art in understanding animal decision-making processes.

### Weaknesses
•	Novelty: Insufficient comparison with Nguyen et al.'s 2015 work, which leaves SWIRL's unique contributions unclear.

The difference between SWIRL and the previous work by `Nguyen, Quoc Phong, Bryan Kian Hsiang Low, and Patrick Jaillet. "Inverse reinforcement learning with locally consistent reward functions." Advances in neural information processing systems, 28 (2015)` needs further discussion to clarify the novelty of this work.

Under the similar IRL framework with multiple locally consistent reward functions, Nguyen's algorithm proposed that the transition kernel of reward functions can be dominated by some external inputs. In this case, could SWIRL then be considered as a special case of Nguyen's algorithm with the external input defined as $(s_1, \ldots, s_L)$? Although the RL inner-loop in the two algorithms are slightly different, but I suppose it is not the major difference between SWIRL and Nguyen's work.

It would be helpful if the authors could provide a more detailed comparison between these two algorithms, as well as some additional experiments to compare the performance between them.

•	Unclear scalability of SWIRL, particularly in large environments or with high-dimensional tasks.

•	Lack of transparency in choosing the number of hidden modes across experiments.

•	The math writing of this paper is a bit difficult to follow (see below).


**Complexity and scalability of the algorithm**

One major issue with variants of MaxEnt IRL methods (even with fixed reward function) is that the computing complexity would be very high since within each loop one needs to solve a forward problem to obtain the policy under the current reward function estimation. This problem would be further scaled up when there are multiple reward functions that needed to be evaluated via solving a RL problem (e.g., in equation (6) of this paper). So my question would be:

1. Is SWIRL guaranteed to converge under some large environments? For example, if the size of the simulated gridworld environment in section 4.1 is not $5 \times 5$ but, say, $50 \times 50$?
2. Following the last question, what is the relationship between computing time of SWIRL and the cardinality of the state, action, and the hidden mode space? This would be helpful to understand what is the maximum capacity of this method, i.e., to which scale of the environment that SWIRL can still handle. To address these questions, it would be helpful if the authors can provide some empirical results on the computing time of SWIRL under different setups.
3. I believe this question would be more suitable for a future work, but just out of curiosity, would SWIRL be possible to integrate some function approximations (of e.g., the state, action, or hidden mode space, since it is now already using gradient method for optimization) so that it can still be applied in high-dimensional tasks?

**Experiments**

1. How did the author choose the number of hidden modes? In the three experiment discussed in this paper, the total number of hidden modes varies across experiment (2 for the first experiment, 3 for the second, and 5 for the last), so I would be curious to know what is the criterion of the authors' to select this hyperparameter. Or did I missed some part such that this number is learnt by the algorithm automatically?
2. The discussion about the reward maps in section 4.3 (lines 492--505) is very hard to follow, as well as the related figures (Figure 4A). In general, I may propose that the results shown in Figures 4A and 4C and corresponding text do not really help for supporting the major claim about SWIRL. This could be due to the lack of space so that lots of experiment details are omitted, and this part would be more suitable for a scientific journal but not a conference. I may recommend the author to change the way of presenting the results.

**Math writing**

Some modifications that would be helpful to increase the readability of the paper are:

1. Numbering of equations in the paper is sloppy, e.g., all equations in the paper are labeled, though some of them are neither referenced nor needed for further discussion. I would recommend labeling only those equations that are referenced later. For example, in lines 660--671, four lines of a single equation is labeled "(8)", but then in lines 685--698, all lines within the same expression are given a different label from "(10)" to "(15)". Or are there any special meanings that I missed?
2. Some display-mode equations are missing punctuation.
3. Line 136, "$R$ corresponds to the reward function $r \in \mathbb{R}$": What is the difference between "$R$" and "$r$" in this notation? According to the rest of the paper (where the notation "$R$" never occurrs again), I would assume they both represent the reward function, then why introducing two different symbol for the same meaning? Besides, the notation "$r \in \mathbb{R}$" defines the reward function "$r$" as a real number, but subsequent reference of "$r$" indicates that it is actually a function on the cartesian product of the state space and action space into the real line. I would recommend make sure the definition of "$r$" is consistent through the paper for a better clarification.

4. Line 170: The symbol "$\mathcal{S}^L$" is used without definition. Does that mean the cartesian product of $L$ state spaces?
5. Line 231, "$\forall s \in \mathcal{S}, z \in Z$": Did you mean "$z \in \mathcal{Z}$"?

6. In the appendix, I only see section A.1.1 but no further sections. Is there are missing section after that? If not, I would suggest remove the subsubsection label for this part.

7. In the derivations in the appendix, the range of some summation is not consistent and not clear. For example, in lines 661--671, the summation is given by "$\sum_{n}$", but in subsequent lines (e.g., line 677) the same summation (I assume) is given by "$\sum_{n = 1}^N$". Is "$\sum_{n}$" just a slang for "$\sum_{n = 1}^N$", or the range in the two sums are actually different?

8. Line 701--703: The notation "$Q(\theta, \theta^k)$" is used without definition. According to the context, I assume it is a typo and the authors would have really meant "$G(\theta, \theta^k)$".


**Minor**

In Figure 3, the color for mode "water" and "explore" is very hard to distinguish if the reader only has access to the printed paper (especially in Figure 3F). Similar issue exists in Figure 4, but not so severe. Consider revising.

--
Post-rebuttal:  I believe the paper can be strongly improved if the concerns about writing, experimental design and representation are addressed, but I will keep my score for now.

### Questions
**Complexity and scalability of the algorithm**

One major issue with variants of MaxEnt IRL methods (even with fixed reward function) is that the computing complexity would be very high since within each loop one needs to solve a forward problem to obtain the policy under the current reward function estimation. This problem would be further scaled up when there are multiple reward functions that needed to be evaluated via solving a RL problem (e.g., in equation (6) of this paper). So my question would be:

1. Is SWIRL guaranteed to converge under some large environments? For example, if the size of the simulated gridworld environment in section 4.1 is not $5 \times 5$ but, say, $50 \times 50$?
2. Following the last question, what is the relationship between computing time of SWIRL and the cardinality of the state, action, and the hidden mode space? This would be helpful to understand what is the maximum capacity of this method, i.e., to which scale of the environment that SWIRL can still handle. To address these questions, it would be helpful if the authors can provide some empirical results on the computing time of SWIRL under different setups.
3. I believe this question would be more suitable for a future work, but just out of curiosity, would SWIRL be possible to integrate some function approximations (of e.g., the state, action, or hidden mode space, since it is now already using gradient method for optimization) so that it can still be applied in high-dimensional tasks?

**Experiments**

1. How did the author choose the number of hidden modes? In the three experiment discussed in this paper, the total number of hidden modes varies across experiment (2 for the first experiment, 3 for the second, and 5 for the last), so I would be curious to know what is the criterion of the authors' to select this hyperparameter. Or did I missed some part such that this number is learnt by the algorithm automatically?
2. The discussion about the reward maps in section 4.3 (lines 492--505) is very hard to follow, as well as the related figures (Figure 4A). In general, I may propose that the results shown in Figures 4A and 4C and corresponding text do not really help for supporting the major claim about SWIRL. This could be due to the lack of space so that lots of experiment details are omitted, and this part would be more suitable for a scientific journal but not a conference. I may recommend the author to change the way of presenting the results.

**Math writing**

Some modifications that would be helpful to increase the readability of the paper are:

1. Numbering of equations in the paper is sloppy, e.g., all equations in the paper are labeled, though some of them are neither referenced nor needed for further discussion. I would recommend labeling only those equations that are referenced later. For example, in lines 660--671, four lines of a single equation is labeled "(8)", but then in lines 685--698, all lines within the same expression are given a different label from "(10)" to "(15)". Or are there any special meanings that I missed?
2. Some display-mode equations are missing punctuation.
3. Line 136, "$R$ corresponds to the reward function $r \in \mathbb{R}$": What is the difference between "$R$" and "$r$" in this notation? According to the rest of the paper (where the notation "$R$" never occurrs again), I would assume they both represent the reward function, then why introducing two different symbol for the same meaning? Besides, the notation "$r \in \mathbb{R}$" defines the reward function "$r$" as a real number, but subsequent reference of "$r$" indicates that it is actually a function on the cartesian product of the state space and action space into the real line. I would recommend make sure the definition of "$r$" is consistent through the paper for a better clarification.

4. Line 170: The symbol "$\mathcal{S}^L$" is used without definition. Does that mean the cartesian product of $L$ state spaces?
5. Line 231, "$\forall s \in \mathcal{S}, z \in Z$": Did you mean "$z \in \mathcal{Z}$"?

6. In the appendix, I only see section A.1.1 but no further sections. Is there are missing section after that? If not, I would suggest remove the subsubsection label for this part.

7. In the derivations in the appendix, the range of some summation is not consistent and not clear. For example, in lines 661--671, the summation is given by "$\sum_{n}$", but in subsequent lines (e.g., line 677) the same summation (I assume) is given by "$\sum_{n = 1}^N$". Is "$\sum_{n}$" just a slang for "$\sum_{n = 1}^N$", or the range in the two sums are actually different?

8. Line 701--703: The notation "$Q(\theta, \theta^k)$" is used without definition. According to the context, I assume it is a typo and the authors would have really meant "$G(\theta, \theta^k)$".


**Minor**

In Figure 3, the color for mode "water" and "explore" is very hard to distinguish if the reader only has access to the printed paper (especially in Figure 3F). Similar issue exists in Figure 4, but not so severe. Consider revising.

--
Post-rebuttal:  I believe the paper can be strongly improved if the concerns about writing, experimental design and representation are addressed, but I will keep my score for now.

### Soundness
2

### Presentation
2

### Contribution
1
