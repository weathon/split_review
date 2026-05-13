# Suspicion-Agent: Playing Imperfect Information Games with Theory of Mind Aware GPT-4

- Decision: Reject
- Scores: 3, 3, 6, 5

## Abstract
\vspace{-0.6em}
Unlike perfect information games, where all elements are known to every player, imperfect information games emulate the real-world complexities of decision-making under uncertain or incomplete information. 
GPT-4, the recent breakthrough in large language models (LLMs) trained on massive passive data, is notable for its knowledge retrieval and reasoning abilities. This paper delves into the applicability of GPT-4's learned knowledge for imperfect information games. 
To achieve this, we introduce \textbf{\agentname{}}, an innovative agent that leverages GPT-4's capabilities for imperfect information games. With proper prompt engineering to achieve different functions, \agentname{} based on GPT-4 demonstrates remarkable adaptability across a range of imperfect information card games. Importantly, GPT-4 displays a strong high-order theory of mind (ToM) capacity, meaning it can understand others and intentionally impact others' behavior. Leveraging this, we design a planning strategy that enables GPT-4 to competently play against different opponents, adapting its gameplay style as needed, while requiring only the game rules and descriptions of observations as input.
In the experiments, we qualitatively showcase the capabilities of \agentname{}  across three different imperfect information games and then quantitatively evaluate it in Leduc Hold'em. {As an exploration study, we show that \agentname{} can potentially outperform traditional algorithms without any specialized training or examples, but still cannot beat Nash-Equilibrium algorithms}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the applicability of LLM on imperfect information games. The authors show superior performance of their agent w.r.t. traditional algorithms (such as CFR).

### Strengths
The study of LLM in decision making problem is currently one of the most important topic of research. This paper studies the applicability of LLM in imperfect information games and uses theory of main planning to infer private information based on the observed history. Moreover the topics of the paper are in line with the interests of the ICLR community.

### Weaknesses
In the reviewer's opinion the evaluation of the method is conceptually flawed. First, Nash equilibrium is never mentioned in the paper, which is the correct way of assessing the performance of algorithms in games. Second, the opponents considered are not optimal choices, new algorithms such as CFR+ or its optimistic variants (e.g. [1,2]) are now the state of the art in solving such games. DQN, DMC and NFSP are deep learning approaches that are not well motivated in such small games. 
The main objective is the fallowing, any good algorithm in such games reaches ~0 exploitability (meaning that it finds optimal strategies, in terms of NE) and, be definition, no strategy can win against such strategies  when considering enough games. Thus either the CFR implementation is wrong (or far from convergence) or the evaluation methodology is flawed in other ways.

Moreover ToM s a valid approach only against exploitable agents, as the correct strategy against an agent with ~0 exploitability is itself a strategy with ~0 exploitability.

### Questions
1) Do you consider only two players games?
2) Way do you make a distinction between 0 and 1 position?
3) How is it possibile to consistently win against a strategy that computes NE?
4) Way are the evaluation made in terms of win/loss instead of exploitability as common in GT?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studied the applicability of GPT-4's learned knowledge for imperfect information games. They introduced a suspicion agent that leverages GPT-4's capabilities for performing in imperfect information games. With proper prompt engineering to achieve different functions, the suspicion agent based on GPT-4 demonstrates remarkable adaptability across a range of imperfect information card games.

### Strengths
This paper introduced a prompting system designed to enable large language models to engage in imperfect information games using only the game rules and observations for interpretation. By incorporating first-order ToM and second-order ToM capabilities, They showed that a GPT-4-based agent can outperform traditional algorithms, even without specialized training or examples.

### Weaknesses
The main contribution of this paper is designing the experiments based on LLMs to solve games, but I have some concerns about the experiments:

-The game on Leduc Hold’em is too specific. It is possible that the winning strategy of playing Leduc Hold’em was discussed online and then used to train LLMs. Then, the assumption that LLMs are trained without specialized training or examples for playing this game is not held anymore.

-CFR used in experiments is too old, and new versions should be considered, e.g., CFR+, Discounted CFR, predictive CFR.

Tammelin, O., 2014. Solving large imperfect information games using CFR+. arXiv preprint arXiv:1407.5042.

Brown, N. and Sandholm, T., 2019, July. Solving imperfect-information games via discounted regret minimization. In Proceedings of the AAAI Conference on Artificial Intelligence (Vol. 33, No. 01, pp. 1829-1836).

Farina, G., Kroer, C. and Sandholm, T., 2021, May. Faster game solving via predictive blackwell approachability: Connecting regret matching and mirror descent. In Proceedings of the AAAI Conference on Artificial Intelligence (Vol. 35, No. 6, pp. 5363-5371).

-The CFR strategy used in experiments may not trained well to be a Nash equilibrium strategy. In two-player zero-sum games, a Nash equilibrium strategy is not exploitable. However, in the proposed experiments, CFR strategies are exploited: “CFR may occasionally raise even with a mid-level hand to exert pressure on Suspicion-Agent. In these instances, Suspicion-Agent’s tendency to fold can lead to losses……………..when CFR chooses to check—often indicating a weak hand—or when DMC checks—suggesting its hand doesn’t align with the public cards—Suspicion-Agent will raise as a bluff to induce folds from the opponents” 
Another possible reason is that the CFR (mixed) strategy is not presented well in experiments.

-The current experiment setting is not fair because LLMs used the online information when playing the game, but CFR cannot use this information. That is, LLMs exploit more information while playing the game.

-The comparison results among different algorithms for Game Coup and Texas Hold’em Limit should be presented.

### Questions
No

### Soundness
2 fair

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
This paper proposed an agent (the Suspicion-Agent) constructed upon GPT-4, bearing up to second order Theory of Mind capability, for playing imperfect information games. 

The agent is made up of several modules:
- Rule introduction (Fixed): introduce game rules, winning conditions, observations, actions and hidden states. 
- Observation interpreter (Coded): Interpret the environmental states into natural languages in certain format.
- Reflexion (LLM): Self-learning module, finding which action is useful in examples and game history.
- Planning (LLMs): Generating several plans for current situation
    - Vanilla: suppose the opponent takes any valid action uniformly
    - First order ToM: Analyse the opponent's behavior and guess opponent's hand while assuming opponent plays honestly.
    - Second order ToM: guessing the reasonable belief of the opponent about the hand of self, and play accordingly.
- Evaluator (LLM): Calculate the expected reward, then choose a plan and execute.

The agent is tested in the multiple card games, Coup, Leduc Hold'em, and Texas Hold'em limit. The Suspicion-Agent outperforms other models like DQN, CFR, DMC, NFSP. 

The experiment shows that the GPT-4 with second order ToM construction behaves the best among all other models tested in the paper, including 1st-order and 0th-order ToM, GPT-4 and GPT-3.5 agents, and other tensor models.

### Strengths
- The paper shows the construction of Suspicion Agent constructed with 2nd-order ToM on GPT-4 masters the three card games.

- The paper provides evidences that the models can follow particular instructions of second order ToM template to construct ToM analysis up to order 2, but cannot do it without the template.

- The paper builds and tests a particular cognitive architecture purely via LLMs to solve decision problems. Response templates are given, but as far as I see, it is not a typical few-shot prompt.

- The statistical data of game-play indicates some similarity and differences among the 0th-,1st- and 2nd-order ToM results.

### Weaknesses
 - The game of Texas and Ludec is still fairly simple: which means the rounds per game is not large and the context window may be able to handle several full games without compressing or discarding any history. (I am not very sure about each module's context structure in the construction among rounds / games, frankly.) And the situation does not change much in large scale.

- Most of the templates are given, so the GPT-4 is thinking in the given logic. Only those games with very clear given logic can be played by second-order ToM version of Suspicion-Agent.

- The decision pipeline is fixed and the only learnable part is the **Reflexion module**.

### Questions
1. Is there a study on the intermediate responses from GPT-3.5 and GPT-4, about **correctness in calculations**, on the distribution of opponent's hand, the probability of winning rate, expected rewards, etc.? I think the agent did not specifically develop a numerical model for calculating them and insert them into prompts.

2. If the above calculation values of GPT-3.5 is usually incorrect, then would checking and correcting them be effective in leveraging its behavior?

3. Is there a necessity in constructing or thinking with 3rd-order (or even higher) ToM, while playing the game?

4. Has anyone (human player) played with Suspicion Agent? How does it behave? Is there any bluffing tricks to win it?

5. In Algorithm 1. Typos: "My Pettern" (My Pattern, I guess), and "Reflection" (Reflexion).

### Soundness
3 good

### Presentation
3 good

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
This paper proposes an interesting agent called Suspicion-Agent that leverages GPT-4's knowledge and reasoning capabilities for imperfect information games. The key idea is to decompose the gameplay into modules like observation interpreter, planning, etc. and craft prompts to enable GPT-4 to understand the game states and make informed decisions. An interesting contribution is incorporating theory of mind (ToM) into the planning module to predict and influence the opponent's actions. The method is evaluated on games like Coup, Texas Hold'em, and Leduc Hold'em. Qualitative examples demonstrate generalization ability across different games with no specialized training. Quantitative experiments on Leduc Hold'em show Suspicion-Agent can outperform algorithms like CFR and NFSP. Ablation studies provide insights into the agent's adaptive strategies.

### Strengths
1)	An interesting application of harnessing GPT-4 for imperfect information games through prompting and ToM.
2)	Promising generalization capability shown qualitatively across games.
3)	Sharing code/data enables reproducibility.

### Weaknesses
The article's most significant weakness is the unreliability of the experimental results, and its tendency to excessively exaggerate performance, as outlined in the following question section.

While this article is interesting, I find the experimental results in the paper to be questionable, potentially leading readers to misunderstand the capabilities of the LLM in handling imperfect information games.

The author conducted experiments on two-player zero-sum imperfect information games (specifically, Leduc Hold’em), with one of the comparative methods being CFR. The author claimed that Suspicion-Agent's performance significantly surpassed that of CFR, a statement that appears to be entirely unreliable and incorrect. 

*In two-player zero-sum games, following a Nash equilibrium strategy ensures that you will never lose in expectation.* Considering the simplest two-player zero-sum game of rock-paper-scissors, adopting the Nash equilibrium strategy (equal probability of choosing rock, scissors, or paper) ensures a non-negative expected payoff against any strategy. CFR stands as one of the most widely used algorithms for calculating Nash equilibrium in two-player zero-sum imperfect-information games. Leduc Hold’em is a rather small game, and CFR effortlessly identifies the Nash equilibrium for this game. Therefore, in theory, no algorithm can beat CFR in expectation in this game. The author's claim that Suspicion-Agent can beat CFR on Leduc Hold’em is entirely incorrect from this theoretical perspective.

The author's experimental results can be explained in two possible ways: 1) The sample size of 100 games is relatively small. Poker games exhibit substantial randomness, and the outcomes from just 100 games possess a high degree of randomness, making them potentially unrepresentative of the AI's actual performance. A more extensive number of games would be necessary to accurately assess the AI's performance (though this might be cost-prohibitive, especially for Suspicion-Agent). 2) The CFR algorithm employed by the author might not have converged, resulting in strategies that significantly deviate from Nash equilibrium. In either scenario, it raises significant concerns regarding the current experimental results.

Hence, the author's claim that Suspicion-Agent can outperform traditional algorithms like CFR without specialized training or examples is regrettably incorrect. 
To attain a level suitable for publication, this article necessitates substantial revisions. Consequently, I cannot recommend accepting this article in its current state.

### Questions
While this article is interesting, I find the experimental results in the paper to be questionable, potentially leading readers to misunderstand the capabilities of the LLM in handling imperfect information games.

The author conducted experiments on two-player zero-sum imperfect information games (specifically, Leduc Hold’em), with one of the comparative methods being CFR. The author claimed that Suspicion-Agent's performance significantly surpassed that of CFR, a statement that appears to be entirely unreliable and incorrect. 

*In two-player zero-sum games, following a Nash equilibrium strategy ensures that you will never lose in expectation.* Considering the simplest two-player zero-sum game of rock-paper-scissors, adopting the Nash equilibrium strategy (equal probability of choosing rock, scissors, or paper) ensures a non-negative expected payoff against any strategy. CFR stands as one of the most widely used algorithms for calculating Nash equilibrium in two-player zero-sum imperfect-information games. Leduc Hold’em is a rather small game, and CFR effortlessly identifies the Nash equilibrium for this game. Therefore, in theory, no algorithm can beat CFR in expectation in this game. The author's claim that Suspicion-Agent can beat CFR on Leduc Hold’em is entirely incorrect from this theoretical perspective.


The author's experimental results can be explained in two possible ways: 1) The sample size of 100 games is relatively small. Poker games exhibit substantial randomness, and the outcomes from just 100 games possess a high degree of randomness, making them potentially unrepresentative of the AI's actual performance. A more extensive number of games would be necessary to accurately assess the AI's performance (though this might be cost-prohibitive, especially for Suspicion-Agent). 2) The CFR algorithm employed by the author might not have converged, resulting in strategies that significantly deviate from Nash equilibrium. In either scenario, it raises significant concerns regarding the current experimental results.

Hence, the author's claim that Suspicion-Agent can outperform traditional algorithms like CFR without specialized training or examples is regrettably incorrect. 
To attain a level suitable for publication, this article necessitates substantial revisions. Consequently, I cannot recommend accepting this article in its current state.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
