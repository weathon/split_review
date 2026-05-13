# Informing Reinforcement Learning Agents by Grounding Language to Markov Decision Processes

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
While significant efforts have been made to leverage natural language to accelerate reinforcement learning, utilizing diverse forms of language efficiently remains unsolved. Existing methods focus on mapping natural language to individual elements of MDPs such as reward functions or policies, but such approaches limit the scope of language they consider to make such mappings possible. We present an approach for leveraging general language advice by translating sentences to a grounded formal language for expressing information about *every* element of an MDP and its solution including policies, plans, reward functions, and transition functions. We also introduce a new model-based reinforcement learning algorithm, RLang-Dyna-Q, capable of leveraging all such advice, and demonstrate in two sets of experiments that grounding language to every element of an MDP leads to significant performance gains.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a framework to leverage natural language-based advice to accelerate RL learning process. The RLang-Dyna-Q algorithm extends the original RLang framework and combines it with the traditional Dyna-Q. Empirical results over two sets of experiments help verify the effectiveness of propose algorithms.

### Strengths
1. The writing is overall good and easy to follow.
2. The idea of translating natural language advice to RLang and using RLang to generate synthetic transitions makes sense.
3. The writing flow in the experiment is great – sec 4.1 and 4.2 present two effective cases with assumptions on semantically-meaningful labels, while sec 4.3 also presents efforts to try to address this assumption. Also, user study has been completed in Table 2.

### Weaknesses
1. Only Q-learning-based RL is tested in the experiment. More advanced and modern RL algorithms are needed to show the generality, e.g. PPO. The current experiments do not demonstrate the applicability of the proposed framework to more complex RL algorithms that utilize function approximation, which is a significant limitation.
2. More LLM + RL baselines are needed. There are a few simple alternatives to directly leverage LLM to process natural language advice to help RL training. For example, what if we don’t use any RLang-based program, and only treat LLM’s as the generator for actions and transitions? The paper lacks a comparison against a more direct approach where the LLM directly outputs actions or transitions, which could serve as a strong baseline.
3. Another important assumption (and limitation) in the paper is that each environment will be provided with human-annotated natural language advice. This is a strong prior compared with all RL baselines. The author needs to discuss more about this assumption and whether we can use any other ways to bypass the need for human labels. For example, could LLMs directly generate advice for any given environment? The reliance on human-annotated advice is a significant practical hurdle and limits the scalability of the approach. The paper needs to explore methods to reduce or eliminate this reliance.
4. More qualitative results are needed for section 4.3 (a demo is not enough). The symbol grounding demonstration, while interesting, lacks a quantitative evaluation. The paper should include metrics such as grounding accuracy and the impact of the grounded symbols on the RL agent's performance.

### Questions
1. Any idea why the DynaQ baseline doesn’t work in Figure 6’s experiment?
2. Typo in line 164.
3. If we are going to extend the algorithm to high-dimensional continuous RL problem, what could be the biggest challenges?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This pager introduces RLang-Dyna-Q, an extension of prior work, RLang, that transforms natural language into a formally specified language for solving tasks. Rather than focusing on policy-centric translations, as in much prior work, the authors observe that much of the advice or coaching offered by human experts will come in the form of statements that describe a transition function (e.g., "If you miss, you will fall down"), a reward function (e.g., "You get 10 points when you touch the key"), or a plan (e.g. "Go to X, then pick up Y, then return to Z"). RLang-Dyna-Q is a combination of Dyna-Q and RLang that uses the learned world model/transition functions of RLang to further refine the Q function learned in Dyna-Q. 

The proposed RLang-Dyna-Q algorithm is compared to Dyna-Q and to a random policy in a handful of tabular RL domains, showing that it significantly outperforms Dyna-Q. The authors also perform an ablation study in which they test only subsets of RLang-Dyna-Q (only policy advice, only transition advice, or only plan advice).  Finally, the authors conduct a small user study in which 10 undergraduate students provide advice to warm start an RLang-Dyna-Q, with each student contributing one piece of advice, and 5/10 pieces of advice leading to policy improvements over the baseline, un-advised policy.


After reviewing the rebuttal, the authors have clarified the scope of the paper and their intended contributions and research area. Given the research direction and goals are more in line with language grounding and leveraging language for tasks, rather than improving task-learning performance or RL/IL efficiency, I will raise my contribution score to 2 and my overall score to 5.

### Strengths
* The paper is well written and provides a clear overview of the motivation, problem setting, and proposed solution.
* The paper proposes a blend of conventional planning literature and formal specification with the advancement of LLMs, leading to a significant improvement over conventional tabular RL solutions.
* The authors conduct a small scale user study, which solicits and leverages advice from untrained human coaches for a planning task.

### Weaknesses
 * The method is not entirely clear, particularly given the heavy reliance on prior work (RLang) in this paper. It is not clear how the Q table relates to the RLang vocabulary files or RLang declarations, and this information must be obtained by referring to and reading prior work (meaning that RLang-Dyna-Q does not entirely stand on its own, but feels more like the "second half" of the RLang work).
* The results for RLang-Dyna-Q are not very convincing, and the comparison to a method that is nearly three decades old is also not very convincing. Comparisons to more modern RL baselines would improve the work. In particular, comparing to an LLM that generates Python/programming solutions seems like a very important baseline (even if there is no RL refinement, it would be useful to simply see to what extent an advanced LLM can solve these tabular domains out-of-the-box).
* The advice required to make RLang-Dyna-Q actually improve over baselines seems very particular. For example, looking at the advice in Figures 3-6, there is a combination of plans, general advice, and state transition advice. There is not a discussion or written analysis on what types of advice work best, or why. Similarly, the success of different types of advice seems extremely finicky. Comparing advice from participants 5 and 10 in the user study, the written advice is nearly identical. However, the performance deltas are quite significant (from a 33% increase to just a 2% increase).

### Questions
* Why not compare to conventional RL methods (e.g., PPO with a small neural network), to RLang itself, or to LLMs that generate code for plans? 
* Why cut training off at 30-75 episodes, which is quite a small budget given that these are not expensive or safety-critical domains? It seems that one argument for RLang-Dyna-Q is that it could be is significantly more efficient than modern RL baselines by leveraging human advice, but if so then this should be shown by empirical comparisons (e.g., how many episodes does each method require to achieve maximum returns?).
* What differentiates good vs. bad advice for RLang-Dyna-Q? The user study provides great insight into the effects of different natural language prompts for the method. However, at times the prompts appear semantically identical, but they yield different results.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the problem of leveraging natural language advice for training effective/efficient RL agents. The authors hypothesize that some natural language advice is more suitable to be grounded in reward function while others are better captured in transition functions. They further suggest that leveraging natural language advice by grounding them in a formal language (RLang) that is capable of describing all aspects of the system, is better than advising a subset of the system. 

The authors adapt Dyna-Q to work with grounded advice in RLang. They evaluate this method in Minigrid and VirtualHome with mostly positive results to support their hypothesis.

### Strengths
1. I appreciate the range of experiments included, as well as a comparison with SayCan in the appendix.
2. I also enjoy reading the section on user studies, and section 4.3 on automated semantic labeling for disambiguation advice. In general, I agree that gradually removing the need for expert annotations is important, let it be dense natural language advice, crafted vocabulary, or RLang grounding files in this case.
3. This is an important research topic and the contribution is contextualized nicely.
4. Most of the paper is quite clear. A few improvements can be made - see weakness 3.

### Weaknesses
 1. Expert advice seems much more dense, verbose, and low-level (almost program-like) than non-expert advice. It is not completely surprising to me that LLMs can ground them to predefined symbols that are approximately defined on a similar level of abstraction.
2. It might help to have a paragraph discussing results and how advice on effect/policy/plan each contributes to the combined policy. Are they the same? Is it task-dependent? I think this can help better justify that an approach to encode "information about every element of an MDP" is necessary.

(The two concerns above are why I gave 2 for contribution and not higher. Would be happy to improve scores if they are addressed)

3. Stylistic nit-picking: could you please increase the font size in Figure 1, and reward curves in Figure 2-6? The text in Figure 7 looks much better. Perhaps capitalize "Perception" in the title in the left figure for consistency. Consistent legend colors and orders for different methods on page 8 would improve comparability across figures.
4. Broken reference on line 164.

### Questions
1. How was the expert advice (textboxes on page 8) collected for the main experiments (who are the experts, how are they trained, what's the protocol)?
2. Do you have ablation studies for HardMaze in Figure 4?
3. Why is RLang-Dyna-Q-combined worse than RLang-Dyna-Q-plan curve in Figure 6?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposed RLang-Dyna-Q, which can ground any language advice to all components in MDP, compared to grounding only to individual components before. The solution uses in-context learning to first select the grounding type, then translate the advice to RLang program. The enhancement outperforms prior approaches.

### Strengths
1. The algorithm automates language-to-MDP component translation, and streamlines the process of learning human decision-making for robots
2. The authors conducted extensive experiments and described the algorithm clearly

### Weaknesses
1. In-context learning limits the capability enhancement of the language model. It might be better if we could make the LM trainable and train the language model and the RL system end-to-end
2. Human language might not be expressive enough to be translated to RLang. In the experiment section, it stated that some advice cannot be converted to RLang. Could we have a more natural intermediate representation for the advice and agent?

### Questions
1. How to go beyond in-context learning?
2. How to handle the inexpressiveness of human language for RLang?

### Soundness
3

### Presentation
3

### Contribution
2
