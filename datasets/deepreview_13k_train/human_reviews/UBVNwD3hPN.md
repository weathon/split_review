# CivRealm: A Learning and Reasoning Odyssey in Civilization for Decision-Making Agents

- Decision: Accept
- Scores: 8, 8, 6

## Abstract
The generalization of decision-making agents encompasses two fundamental elements: learning from past experiences and reasoning in novel contexts. However, the predominant emphasis in most interactive environments is on learning, often at the expense of complexity in reasoning. In this paper, we introduce \civ, an environment inspired by the \textit{Civilization} game. \textit{Civilization}'s profound alignment with human history and society necessitates sophisticated learning, while its ever-changing situations demand strong reasoning to generalize. Particularly, \civ sets up an imperfect-information general-sum game with a changing number of players; it presents a plethora of complex features, challenging the agent to deal with open-ended stochastic environments that require diplomacy and negotiation skills.
Within \civ, we provide interfaces for two typical agent types: tensor-based agents that focus on learning, and language-based agents that emphasize reasoning. To catalyze further research, we present initial results for both paradigms. The canonical RL-based agents exhibit reasonable performance in mini-games, whereas both RL- and LLM-based agents struggle to make substantial progress in the full game. 
Overall, \civ stands as a unique learning and reasoning challenge for decision-making agents.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This is a dataset and benchmark paper that introduces the CivRealm environment. It supports a number of game features based on the Civilization game, including an agent-agnostic framework, a friendly interface, and a tensor-based agent interface, supporting a variety of custom tasks with custom goal definitions, etc. This is a very exhaustive benchmark for a long-horizon strategy-based game. The paper also discusses the performance of three methods (one tensor-based and one LLM-based).

### Strengths
1. This dataset and associated framework is very useful and will support a lot of research for multi-agent settings involving various kinds of agents. 
2. The whole framework is very novel.

### Weaknesses
I'm not sure how robust the client-server architecture used in the framework is. There are no comments on the robustness of this.

### Questions
1. How robust is the server-client architecture? Did you do any experiments to test it?
2. Is there support for designing custom games? I see Lua script being mentioned to specify the reward structure, new goals, etc. Is there also a support for new maps?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a novel testbed environment inspired by the Civilization game, called *CivRealm*, which is a multi-agent multi-goal long-horizon challenging environment. The authors also implement RL and LLM baseline agents and show that they struggle to make substantial progress in the full game.

### Strengths
1. The authors present a novel and challenging testbed for agent studies, which is a big contribution.
2. The experiments on the proposed agents also set up baselines that follow-up works can improve upon.
3. The environment also has mini-games that can benefit the (multi-agent) RL community.
4. The paper is clearly written and easy to follow.

### Weaknesses
1. Some details are not clear enough. As this is a multi-agent environment, what are the baseline RL and LLM agents play against? I didn't seem to find such details in the description. Specifically, are these other agents rule-based, or are they also learning agents? What are their capabilities and limitations? This is crucial for understanding the difficulty of the environment.
2. The proposed baselines are not working in the (full game) environment. Maybe it is better to also set different difficulty levels (e.g. by different task horizons) for the full game so that later research can more easily be evaluated on the benchmark. The current setup makes it difficult to assess incremental progress, and it would be helpful to have a clear path for future research to build upon. For example, could the authors provide a curriculum of increasing difficulty?
3.  Is Figure 2 the real situation that the LLM agents discover or the expected situation? If it is what the LLM agents discover, why does Tit still behave poorly? It's unclear what the LLM agent is actually perceiving and how that relates to its actions. It would be helpful to see the raw input to the LLM.
4. The text in Figure 4 is too small to view.

### Questions
1. Why the success rate of the RL agent in some mini-games (e.g., SettlerBuildCity) is higher for the hard setting than for the easier settings?
2. Can the authors comment on the reason for instability and the sudden drop in performance in Figure 9?
3. It would be great if the authors could provide videos of the experiments or visualization ways in the future code repo.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The primary contribution of this paper is the introduction of the CivRealm environment, which is built on Civilization VI, a complex and popular video game. This environment offers a platform to study long-term planning, multi-agent interactions, and intricate decision-making etc.

### Strengths
- The paper doesn't just introduce an environment but also provides benchmark tasks and baseline.
- The API provides a comprehensive log of game state and actions.
- It allows AI agents to interact at both high (strategic) and low (tactical) levels.
- It focus on long-term planning which is crucial to agents

### Weaknesses
As a work in the area of datasets and benchmarks, I think a lot of the details are in the code, and I don't have good confirmation of those details just by virtue of the text in the paper. This environment is based on an open-source game http://freeciv.org/. I don't know how different is the open-source game and the environment introduced by the authors. It would be excellent if authors could give reviewers an early release of code to review.

### Questions
This environment is based on an open-source game http://freeciv.org/. From the development aspects, what is the main modifications/effort has been done upon the open-source game?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
