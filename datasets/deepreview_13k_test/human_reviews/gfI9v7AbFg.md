# Strategist: Self-improvement of LLM Decision Making via Bi-Level Tree Search

- Decision: Accept
- Scores: 3, 6, 6, 6, 6

## Abstract
Traditional reinforcement learning (RL) typically requires vast amounts of training
data to develop effective policies. In contrast, large language models (LLMs)
exhibit strong generalization and zero-shot capabilities, but struggle with plan-
ning and understanding complex action policies. In this work, we introduce
STRATEGIST, a novel approach that integrates the strengths of both methods. Our
approach leverages LLMs to learn high-level strategic abstractions, which are
then refined and executed by a low-level mechanism, such as Monte Carlo Tree
Search (MCTS). STRATEGIST is a generalizable framework that can be trained
through population-based self-play simulations and self-improvement, without the
need for prior training data. We demonstrate the effectiveness of STRATEGIST in
learning optimal policies for competitive, multi-turn games with partial informa-
tion, including Game of Pure Strategy (GOPS) and multi-agent, hidden-identity
discussion games like The Resistance: Avalon. Our results show that agents trained
with STRATEGIST outperform those trained with traditional RL methods, other
LLM-based skill acquisition techniques, and pre-existing LLM agents across both
game environments.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents STRATEGIST which combines LLM-generated high-level strategies with Monte Carlo Tree Search (MCTS) for refined action execution. STRATEGIST uses population-based self-play to optimize strategies. The paper presents experimental results in two game environments: GOPS and The Resistance: Avalon. The results indicate that STRATEGIST outperforms traditional RL agents and pure LLM-based methods.

### Strengths
1. The idea of using LLM to generate high-level strategy and use MCTS to get low-level strategy is interesting.

2. The proposed method is evaluated in two game environments, one simple and one complex, which is good.

### Weaknesses
1. Lack of Competitive Baselines: The paper compares with methods that do not use LLM at all (like DeepRole) and methods that only uses LLM but no RL. However, the comparisons exclude more recent RL-LLM hybrid methods that would provide a fairer benchmark for STRATEGIST's effectiveness. In fact, in the past two years, there are a number of papers that combines RL with LLM to play complex strategic multi-agent games that involve natural-language based communication. For example, the paper mentioned the Cicero paper by FAIR, but there is no comparison with the method used in the Cicero paper. There are a lot more papers following up the Cicero paper, and can potentially be used for games like Avalon. Here are a few example papers: 1). Exploring large language models for communication games: An empirical study on werewolf. 2). Language agents with reinforcement learning for strategic play in the werewolf game; 3). Enhance reasoning for large language models in the game werewolf; 4). Agent-pro: Learning to evolve via policy-level reflection and optimization. 

2. Limited Analysis on Strategic Randomization: Strategic randomization is essential in hidden-role games like Avalon. However, the experiment section does not show how well STRATEGIST presents deceptive behavior in a properly randomized fashion. 

3. Absence of Human Evaluation: Despite STRATEGIST's applicability to discussion-based games, there is no reported evaluation of the model's interactions with human players, which would provide insights into its performance in realistic scenarios.

4. Comparison of Bi-Level Structure: Cicero also uses a bi-level structure, although in a different way as this paper proposes: In Cicero, it uses iterative learning methods to choose the intent at the high-level, and uses LLM to generate low-level actions. Cicero's bi-level structures ensures strategic randomization at the high level. In this paper, it is not well explained why this paper's bi-level structure is more effective than Cicero's.

5 (minor). Ambiguity in RL Positioning: The abstract and methodology sections position MCTS as an RL method. However, MCTS is typically classified as a heuristic search within the RL framework and lacks key RL characteristics, such as learning policy updates from experience. So I would suggest the authors carefully choose the wording to avoid confusing the readers.

### Questions
1. How does the proposed method compare to other RL-LLM approaches? Both conceptually and experimentally?

2. Is STRATEGIST properly randomizing its actions in the actual play of Avalon?

3. Are there any human evaluation results?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces STRATEGIST, which is a framework to optimize the strategy induced by LLMs through population-based self-play simulations without the need for any training data. The effectiveness of STRATEGIST in learning optimal strategies is demonstrated against strong baselines on Game of Pure Strategy (GOPS) and the Resistance: Avalon.

### Strengths
- The paper is well written and well organised.
- The description of different components in STRATEGIST is clear.
- The experimental results are strong and comprehensive.

### Weaknesses
- The differences and advantages of the self-play mechanisms of STRATEGIST in improving the strategy against previous related work on self-play for LLMs is unclear.  It would be helpful to provide a clear comparison (e.g. a table) between the self-play mechanism in STRATEGIST and previous self-play methods for LLMs  (e.g. [1] [2] ...) .

[1] Yao Fu, Hao Peng, Tushar Khot, and Mirella Lapata. Improving language model negotiation with
self-play and in-context learning from ai feedback. arXiv preprint arXiv:2305.10142, 2023.


[2] Cheng, Pengyu, et al. "Self-playing Adversarial Language Game Enhances LLM Reasoning." arXiv preprint arXiv:2404.10642 (2024)

### Questions
- What makes the self-play method in STRATEGIST better than previous self-play methods for LLMs, in terms of improving the LLM-induced strategy? I would expect a clear comparison against previous self-play methods in LLMs both in terms of the methodology (as mentioned in the weakness) and experiment study (For instance, ablation studies comparing STRATEGIST to other LLM self-play methods).

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
The paper presents Strategist, a novel framework that leverages Large Language Models (LLMs) for strategic skill acquisition in multi-agent games through a bi-level tree search and self-improvement mechanism. The approach aims to enhance both high-level strategy formulation and low-level execution by utilizing self-play simulations and LLM-based reflections. The framework is evaluated on two games, Game of Pure Strategy (GOPS) and Resistance: Avalon, demonstrating improved performance over baseline methods.

### Strengths
1. Novel approach: the combination of LLMs with a bi-level tree search for strategy improvement is a novel method for enhancing performance in complex multi-agent games. Addressing both high-level strategic planning and low-level execution allows for improvements of agent capabilities.
2. Good empirical evaluation: The authors conduct various ablation studies and additional experiments comparing their method with established baselines like DeepRole and ReCon, providing a broader context for their contributions.

### Weaknesses
1. Reliability of population-based self-play simulation: the authors use round-robin games between top-ten strategies to evaluate the performance of high-level strategies. Since games like Avalon have high uncertainty and the variance of the simulation result is large, it would require many simulations (like hundreds) to get a reliable evaluation of these strategies. However, these simulations would take a long time for LLM inferences. In addition, LLM usually cannot take so many trajectories as input due to the limited context length. It would be better if the authors could provide results to justify the reliability of population-based self-play simulation results.
2. Modular improvement Assumptions: the assumption that improvement ideas are universally applicable across different strategies requires further justification. Improvement ideas may interact with specific strategies in unique ways, possibly leading to unintended consequences or limited effectiveness when applied broadly. While the authors argue that improvements are additive and generalizable, empirical evidence demonstrating this across a variety of strategies would strengthen the claim.
3. Statistical significance and result variability: the reported variances are very large and show significant overlap in many results like Table 1, 2, 3, etc., which implies that the proposed methods might not be delivering substantial enhancements in these test environments. For example, in Table 2, the result of Alpha-go is $-0.39\pm0.71$, and the result of Strategist is $0.33\pm1.21$. The variance is too large to determine whether the new method offers improvements over existing baselines.
4. Suggestions on some related works: the experiments on mainly conducted on the social deduction game named Avalon. A closely related game is Werewolf and there are some recent works like [1,2,3] on building LLM AI agents for these games and could be added to the related work section.

[1] Yuzhuang Xu, et al. "Exploring large language models for communication games: An empirical study on werewolf." arXiv preprint arXiv:2309.04658 (2023).

[2] Zelai Xu, et al. "Language agents with reinforcement learning for strategic play in the werewolf game." arXiv preprint arXiv:2310.18940 (2023).

[3] Bailis, Suma, Jane Friedhoff, and Feiyang Chen. "Werewolf arena: A case study in llm evaluation via social deduction." arXiv preprint arXiv:2407.13943 (2024).

### Questions
Please see Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents STRATEGIST, a framework that combines LLMs with MCTS for learning optimal strategies in competitive multi-agent games. The approach uses LLMs to generate and iteratively improve high-level strategies, which are then refined into executable policies using MCTS. The framework is evaluated on two games: GOPS and Avalon, showing superior performance compared to traditional RL methods and other LLM-based approaches.

### Strengths
- Integration of LLMs with MCTS in a bi-level framework that leverages their complementary strengths.
- Clear empirical validation through rigorous experiments.
- The paper is well written and easy to follow

### Weaknesses
See the questions below.

### Questions
- What happens when the LLM generates syntactically correct but semantically inconsistent or illogical strategies? How does the framework detect and handle such cases? 
- How does the method prevent the idea queue from becoming dominated by similar or redundant improvement suggestions? 
- What happens when there are multiple valid interpretations of a strategy? How is the most appropriate one selected? 
- Are the proposed method verified to learn general strategies instead of overfitting to specific feedback examples?
- Could the method combine successful elements from different strategies into new hybrid approaches?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a new complicated method named Strategist for using LLMs to generate strategies and ideas for multi-agent games.

In summary, there are two levels.

- Low-level self-play tree-search provides value for learning and updating skills.

- High-level skill learning module improves skills, both for text-based strategies (in text modality) and for value heuristic functions (in code modality).

### Strengths
- The idea to learn skills (strategies) not only for (1) text strategy guide, but also for (2) a value heuristic is inspiring. Utilizing LLMs for generating and improving value functions in code modality seems to be an innovative practice that utilizes their ability to reason and to write code. Moreover, the value functions generated could be used to search for good actions for non-speech phases of the game. To use these generated functions rather than to use LLMs could be cost-efficient and time-efficient.
- Improvement is shown. Moreover, performance scales with improvement of inference budget.
- Extensive experiments and details are provided to show the improvement of value functions and text strategies.

### Weaknesses
- Some results measured have no or confusing error analysis. For example, in Table 1, the median scores and IQR of quantities measured are reported, but the error range of the median scores is not reported. I recommend the authors also to report $median\pm error(median)$, in which the error is introduced because number of experiments is limited. Moreover, I wonder if enough duplicated experiments are carried out to prove that Strategist is better than BFS with Thought w.r.t. Avalon Value Heuristic. Also the presentation in Figure 4 is a bit chaotic.

- From section 2 it seems that the value functions are mainly for non-dialogue actions, and the text-based strategies are mainly for dialogue actions, and the action planner based on MCTS tree search described in Appendix F seems to be searching on the values generated by heuristic value functions. According to Appendix G it seems that the authors do not conduct similar search process on dialogue actions, and speeches are mainly provided through a rather traditional prompt-based approach. Of-course this does make sense given that speech is more related to text and is harder to assign scores, but these different approaches for non-dialogue and dialogue actions give a sense of fragmentation.

- There are typos. For example, in table 2 for GOPS the averaged 'winrate' of AlphaGo and DeepRole is negative (I assume it is a typo here: do the authors mean Heuristic Value or other scores?); in table 4 there are only results for winrate but no assassination rate is reported (though mentioned in table caption).

### Questions
Please refer to Weaknesses. Especially,
- Could you report the standard error of the median in addition to the IQR for all results in Table 1? Could you improve the clarity of Figure 4, perhaps by separating the data into multiple plots or using a different visualization method.
- Could you discuss potential limitations or biases introduced by using textual strategies only for dialogue actions? Have you considered any alternative methods to unify the approach of both types of actions, and if so, why they were not pursued?
- Could you clarify what metric is being reported in the 'Winrate' column for GOPS in Table 2, as negative values are unexpected for winrates? If this is an error, please provide the correct values.

### Soundness
2

### Presentation
2

### Contribution
3
