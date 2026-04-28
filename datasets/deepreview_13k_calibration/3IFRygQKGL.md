# OptionZero: Planning with Learned Options

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 6, 8

## Abstract
Planning with options -- a sequence of primitive actions -- has been shown effective in reinforcement learning within complex environments. Previous studies have focused on planning with predefined options or learned options through expert demonstration data. Inspired by MuZero, which learns superhuman heuristics without any human knowledge, we propose a novel approach, named OptionZero. OptionZero incorporates an option network into MuZero, providing autonomous discovery of options through self-play games. Furthermore, we modify the dynamics network in MuZero to provide environment transitions when using options, allowing searching deeper under the same simulation constraints. Empirical experiments conducted in 26 Atari games demonstrate that OptionZero outperforms MuZero, achieving a 131.58% improvement in mean human-normalized score. Our behavior analysis shows that OptionZero not only learns options but also acquires strategic skills tailored to different game characteristics. Our findings show promising directions for discovering and using options in planning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The work proposes a revamped approach to the well-known options framework, which allows agents to take temporally extended actions as well as myopic ones. By combining a network which learns options with MCTS MuZero (which models transition dynamics) the authors propose a method to utilise options alongside single actions in self-play games.

### Strengths
The need for efficiency in decision making in RL is clear, as single-step actions are slow and computationally expensive (even more so in slow simulators). Thus, the problem addressed by OptionZero is clear and its existence is well-motivated. Additionally, since much prior work in options appear to be in manually defined and demonstration-based settings, the generalisability of OptionZero is a strong selling point.

Within fixed computational constraints, the idea of decreasing the frequency of queries to the network is a strong idea for the current state of RL. Also important is the notion of learning subroutines which the options network will identify as useful in different scenarios and not have to re-learn temporal relationships.

The flexibility to play options or primitive actions results in tailored reactions to scenarios, as an agent may need the fine-grained approach taken by traditional RL. The main results in Table 1 indicate the validity of the method, as using options provides a performance benefit more often than not, with longer option limits sometimes outperforming shorter ones.

### Weaknesses
It is unclear why options are outperformed by primitive actions in certain environments. The authors suggest that in environments with high combinatorial complexity, learning of the dynamics model may be difficult and thus options may simply produce more overhead than actual benefit. A more detailed analysis of these environments would be beneficial, for e.g. investigate whether there is a correlation between the stochastic branching factor of the environment and the performance of options. Specifically, it would be useful to see a breakdown of the performance in environments with varying degrees of stochasticity and branching factors, as it is not clear if the dynamics model struggles with high branching or high stochasticity, or both. Further, the performance of the dynamics model itself should be analysed in these cases, to see if the model is indeed learning a useful representation of the environment.

Additionally, it seems that longer options may improve efficiency but not always increase performance when those options may be overextending in environments where more granular control is required. Have the authors considered implementing dynamic options lengths somehow? This may make the idea more viable, or at least a discussion on the complications of implementing that would be a good addition to the work. For example, it is not clear how the maximum option length is chosen, and whether this is a hyperparameter that needs to be tuned for each environment. A discussion of the sensitivity of the method to this hyperparameter would be beneficial, as well as a discussion of the trade-offs between longer and shorter options.

### Questions
Clerical: In section 5.2 the $l_{1}$ option setting is mentioned as a baseline, but Table 1 compared the options to something called $l_{0}$. Do $l_{0}$ and $l_{1}$ refer to the same baseline? If so, using consistent notation will help make the results section more readable.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents OptionZero, a novel approach that incorporates an option network into MuZero and allows the agent to learn temporary extended actions. The authors conducted empirical experiments and find OptionZero outperforms MuZero in teams of mean human-normalized scores on 26 Atari games.

### Strengths
The paper is well-written. The authors explain the use of options clearly with a toy example, demonstrating how options are used. The empirical results are also strong, achieving high mean normalized scores.

### Weaknesses
It's not clear the actual benefits options bring. In the intro, the paper claims options allow for "searching deeper", but the empirical analysis shows "deeper search is likely but not necessary for improving performance". While it's nice to have the option to do option, could the authors provide a more detailed analysis of options beyond a deeper search?

The paper could also benefit more from discussions of 
1) the trade-offs between increased complexity and performance gains
2) how much tuning did the authors perform to make OptionZero work; were there failure cases/ideas during the development and how did the authors overcome them?

### Questions
1. Why select these 26 Atari games instead of using the standard 57 Atari games?
1. What is the hardware resource for conducting the experiments?
1. How long does training a single Atari game with OptionZero take?
1. How long does training a single Atari game with MuZero take?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors introduce OptionZero, an advanced extension of the MuZero algorithm that autonomously identifies temporally extended actions, known as options, without the need for predefined options or expert-provided demonstrations. By incorporating an option network, OptionZero enhances planning efficiency by decreasing both decision-making frequency and the computational load required for complex environments. Evaluated on a suite of Atari games, OptionZero demonstrates notable improvements in human-normalized scores compared to MuZero, accompanied by a detailed analysis of how options are utilized across varying game states and scenarios

### Strengths
- Novel idea for autonomous and adaptable option discovery. The proposed method's ability to autonomously discover and tailor options to diverse game dynamics removes the need for predefined actions, making it highly adaptable across different environments.

- Convincing results for enhanced planning in RL.  By integrating an option network, OptionZero reduces decision frequency, enabling computational efficiency, particularly in visually complex tasks like Atari games.

- Strong Performance Gains: On Atari benchmarks, OptionZero achieves a 131.58% improvement over MuZero, a significant improvement compared to previous SOTA papers.

- Interesting ideas to adjust option lengths, balancing performance and training efficiency, particularly useful in tasks needing variable action sequences.

### Weaknesses
 - Inconsistent Option Use Across Games: OptionZero's reliance on options appears to vary widely across Atari games. While longer options bring substantial gains in some games, they contribute less in others. This inconsistency suggests that the model’s option-based planning may struggle to generalize well across diverse, complex environments. The paper should discuss this limitation. Specifically, the paper lacks a detailed analysis of why certain games benefit more from longer options than others. For instance, are there specific characteristics of game environments, such as the frequency of state transitions or the complexity of the optimal policy, that correlate with the effectiveness of longer options? The paper should include a more thorough investigation into these factors.

- Challenges in Complex Action Spaces: In games with intricate action spaces, such as Bank Heist (Atari), OptionZero’s dynamic network encounters difficulty as option lengths increase, particularly with multi-step dependencies. This issue may restrict OptionZero’s application in environments where actions are highly combinatorial, relying instead on settings with more straightforward or predictable actions. The paper does not adequately explore the limitations of the dynamics network in handling complex action sequences, especially when these sequences are not easily decomposable into shorter, independent options. The authors should investigate how the model’s performance degrades as the complexity of the action space increases, and provide a more detailed analysis of the types of action dependencies that pose the greatest challenge.

- Reduced Prediction Accuracy for Longer Options: The model’s prediction accuracy tends to decrease as options become longer, affecting planning quality where extended strategies are essential. I would recommend adding an experiment to study this effect and discuss potential limitations of the proposed method. The paper should include a quantitative analysis of how prediction error increases with option length, and how this error impacts the overall planning performance. It would be beneficial to see a breakdown of the prediction error by different components of the model (e.g., state prediction, reward prediction) to better understand the source of the degradation.


- Limited Application Beyond Games: Although the model shows promise in game environments, the paper does not investigate its potential beyond Atari-like settings. I would appreciate seeing results on other domains, maybe robotic such as Gymnasium-Robotics. Under the current evaluation, the method seems limited to game-based scenarios. The paper should address the potential challenges in applying OptionZero to environments with continuous action spaces or more complex state representations, such as those found in robotic tasks. The authors should discuss how the option discovery mechanism might need to be adapted for such environments and provide a roadmap for future research in this direction.

### Questions
- How does the dynamics network handle complex action spaces, especially in games with highly varied option paths?"

- What are the specific computational costs of incorporating the option network, both in training and during MCTS simulations? Could the author discuss the associated overhead with the proposed method?

- Can the model be applied to environments beyond games with less predictable state transitions, and how would option discovery be affected? I would suggest adding studies in robotic environments.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces the OptionZero framework, which incorporates options into MCTS and enables the automatic design of options through self-play, thereby avoiding cumbersome manual design. In Atari games, OptionZero achieves significant improvements compared to MuZero, achieving a 131.58% improvement in mean human-normalized score. It has shown promising directions for discovering and using options in planning.

### Strengths
1. This paper is well-written with a clear structure, making the research content easily comprehensible.

2. By introducing the OptionZero framework and leveraging self-play for automatic option design, this study paves the way for new approaches. The novelty is good.

3. The experimental results robustly support the effectiveness of the algorithm.

### Weaknesses
1. I am curious about whether the introduction of options has any impact on the theoretical optimality of MCTS. Specifically, how does the integration of options affect the exploration-exploitation balance governed by the PUCT formula, and does it maintain the asymptotic convergence properties of standard MCTS? A more rigorous analysis of this aspect would strengthen the theoretical foundation of the proposed framework.

2. Is it possible to demonstrate the advancement of the algorithm more directly by solely utilizing the learned option network for action selection, without relying on MCTS? For instance, how does the performance of OptionZero compare to a policy that directly selects actions based on the learned option values, without the tree search? This could provide insights into the specific contributions of the option framework versus the planning component.

3. What is the expected performance as the value of $l$ increases? While the paper mentions experiments with $l_3$ and $l_6$, it would be helpful to understand the trade-offs involved in increasing the maximum option length. Does the performance continue to improve, or does it plateau or even degrade due to the increased complexity of the option space? A more detailed analysis of the impact of $l$ on performance would be valuable.

4. What are the differences in the running wall-clock time required for OptionZero compared to MuZero? While the paper focuses on performance improvements, understanding the computational overhead associated with incorporating options is crucial for assessing the practicality of the approach. A comparison of the training and inference times for both methods would be beneficial.

### Questions
Please refer to the weakness part.

### Soundness
4

### Presentation
4

### Contribution
4
