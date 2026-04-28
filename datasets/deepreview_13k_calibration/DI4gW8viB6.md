# Competing Large Language Models in Multi-Agent Gaming Environments

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Decision-making is a complex process requiring diverse abilities, making it an excellent framework for evaluating Large Language Models (LLMs). Researchers have examined LLMs' decision-making through the lens of Game Theory. However, existing evaluation mainly focus on two-player scenarios where an LLM competes against another. Additionally, previous benchmarks suffer from test set leakage due to their static design. We introduce GAMA($\gamma$)-Bench, a new framework for evaluating LLMs' Gaming Ability in Multi-Agent environments. It includes eight classical game theory scenarios and a dynamic scoring scheme specially designed to quantitatively assess LLMs' performance. $\gamma$-Bench allows flexible game settings and adapts the scoring system to different game parameters, enabling comprehensive evaluation of robustness, generalizability, and strategies for improvement. Our results indicate that GPT-3.5 demonstrates strong robustness but limited generalizability, which can be enhanced using methods like Chain-of-Thought. We also evaluate 13 LLMs from 6 model families, including GPT-3.5, GPT-4, Gemini, LLaMA-3.1, Mixtral, and Qwen-2. Gemini-1.5-Pro outperforms others, scoring of $69.8$ out of $100$, followed by LLaMA-3.1-70B ($65.9$) and Mixtral-8x22B ($62.4$). All code and experimental results are available in the supplementary materials and will be made publicly available upon publication.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the capabilities of LLMs in the multi-agent gaming setting. To this end, the authors propose a new benchmark including eight classical game theory problems and a dynamic scoring rule. They evaluated twelve LLMs. In terms of the scoring rule, the Gemini-1.5-Pro has the best performance among closed-source LLMs and the LLaMA-3.1-70B has the best performance among open-source LLMs. Besides, their results show that GPT3.5 is robust to multiple runs and different temperatures but is poor in the generalization of various game settings.

### Strengths
1. This paper proposes an interesting benchmark that allows LLMs as agents to compete with each other. The authors systematically conducted experiments under multiple runs, different temperatures, and various game parameters, which made their conclusions more convincing.

2. This paper is well-written and easy to read. Especially the quick links of game descriptions, prompt templates, and experimental results are very helpful in understanding this paper.

### Weaknesses
1. My main concern is that, from a conceptual/technical point of view, the contribution and novelty of this work are somewhat limited. The authors discussed related literature limited to two players or actions and motivated their focus on the multi-player setting. However, the study of multiple LLM agents in gaming is not novel. I think a more detailed and thorough comparison with previous related benchmarks is needed.

2. The single metric that measures how far the LLM agent's behavior is from the Nash equilibrium cannot fully evaluate the performance of LLM agents in decision-making. 

3. Some of the insights are not very surprising in light of the prior literature (such as it is possible to improve the performance of GPT3.5 through CoT).

### Questions
Have you tried to test the robustness and generalizability of models other than GPT3.5, especially the open-source model and the close-source model that have the best performance?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors measure LLMs competing ability in various multi-agent game theoretic based scenarios. They put together a collection of 8 games and test across 12 different LLMs with dynamic parameter changes to the games to test for robustness. They contribute a literature review of studies focusing on game theory based LLM studies, the GAMA-bench (available after paper publication), and the results of benchmarking the LLMs they test.

### Strengths
Overall the paper is great.

- Robust testing, using "multiple runs, temperature parameter alterations, and prompt template variations" as well as testing across 12 different LLMs.
- Approach to Generalizability (RQ3) is useful, unique, and future-proofs the benchmark to a degree.
- Excellent presentation with logical structure and intuitive navigation, all information is presented clearly. (Section 3.1 links to all game prompts, key findings and answers to research questions nicely emphasized.)

### Weaknesses
 - The case could be made stronger for "LLMs being good at Game Theory" == "LLMs useful for decision making". The intro "jumps" from "decision-making poses a significant challenge for intelligent agents" to Game Theory. It's slightly strengthened by noting that your "framework evaluates LLMs’ ability to make optimal decisions". In the conclusion you mention "Our findings reveal that GPT-3.5 (0125) demonstrates a limited decision-making ability on γ-Bench", which is great. Overall, I think your paper points in the direction and does well, but this introduction is a bit jarring.

 - "We leveraging GPT-4 to rewrite our default prompt" -> 'We leverage'
 - "The game has a PSNE where all players", "a PSNE but presents an MSNE, "  -> PSNE and MSNE is defined in the appendix but acronyms are used in the main body.
 - "The model produces average numbers of 34.59, 34.59" -> intentionally the same numbers?
 - "We first focus on open-source models, including OpenAI’s GPT-3.5 (0613, 1106, and 0125), GPT-4 (0125), and Google’s Gemini Pro (1.0, 1.5)." -> closed source
 - RW: "Other than papers listed in Table 3 on evaluating..." -> this should present the table better. "We present a comparison of studies using LLMS..." It currently feels like a passing note, but is stronger than that. Also, link this in your statement contributions in the introduction.

 - RQ4: Qwen-2 seems to do great in all but Diner and SBA which seem very out of place and there's no mention of this result or why it could've happened. What happened here?

### Questions
- RQ4: Qwen-2 seems to do great in all but Diner and SBA which seem very out of place and there's no mention of this result or why it could've happened. What happened here?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors introduce GAMA-Bench, a benchmark with 8 well-designed game scenarios. They performed evaluation on GAMA-bench for multiple mainstream LLMs and in addition evaluate robustness, reasoning, and generalizability of these models.

### Strengths
1. The benchmark questions are designed carefully, drawing inspiration from classic game theory scenarios. The objective of the three categories of games are clear. 
2. On top of measuring performance, extensive experiments are conducted to understand the effect of prompting and sampling, CoT, and sensitivity to same game with different parameters.

### Weaknesses
1. The author mentioned that most previous benchmarks incorporates classic settings that LLM has seen during training. Yet most games proposed in GAMA-Bench seem to also be taken from classical work. For instance, I prompted the game definition of all 3 cooperative games to GPT-4o and it is able to recognize which famous game it is. The authors could improve on this by proposing variants and provide concrete evidence on no test set leakage by comparing LLM performance on variants vs. original games. 
2. Language model are not designed to solve games, nor provide concrete mathematical calculation which is required to compute NEs. If the goal of this work is to understand LLM's ability to adapt in dynamic, multi-agent systems, I would encourage the authors to design additional experimental settings where partial actions by other agents are revealed. For instance, it would be more informative to see how models will adjust in "Guess 2/3 of the Average" game knowing there is a weak/malicious model that is likely to output a large number, compared to simply letting the model work its way to the NE. An example could be a series of rounds where the LLM is given information about other players' previous moves or tendencies, and then measure how quickly it adapts its strategy.

### Questions
I don't have any particular clarifying questions and most of my concerns are mentioned in "Weaknesses" section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces GAMA-Bench, a novel benchmark designed to evaluate the gaming and decision-making abilities of LLMs in multi-agent environments. The benchmark comprises eight classical game theory scenarios, where LLMs are evaluated on how closely their decisions align with the Nash equilibrium, a theoretical standard for rational decision-making. Twelve different types of LLMs, including GPT-4, Gemini, and LLaMA, are tested. Additionally, the paper explores the impact of hyperparameters, prompt design, reasoning strategies, and persona on the robustness of LLM performance.

### Strengths
1. The paper is well-organized, making it comprehensible to a broad audience, including those unfamiliar with game theory. The authors provide clear explanations of complex game-theoretic concepts and how they apply to LLMs. 
2. This work fills a gap in the literature by focusing on multi-agent scenarios, which are more complex and less explored compared to simpler single-agent or two-agent interactions. 
3. The authors go beyond simply testing the LLMs and investigate the role of different factors such as temperature settings, prompt design, and reasoning strategies (e.g., CoT). By examining how these parameters influence LLM behavior and outcomes, the paper adds a layer of rigor, ensuring that the benchmark is not merely static but adaptable and robust under various conditions.

### Weaknesses
1. The paper does not sufficiently clarify which specific cognitive or decision-making abilities of LLMs are being measured through this benchmark. While the Nash equilibrium is a logical choice for evaluating decision rationality, the paper does not articulate whether the benchmark truly reflects the LLMs’ capacities in areas such as long-term planning, adaptability, or ethical decision-making. The discussion of which kind of ability can be measured through this benchmark.
2. The paper misses an opportunity to delve into the reasons behind the LLMs’ decisions. Different models may exhibit distinct decision-making tendencies based on their training data and architectures. For instance, GPT-4’s tendency toward cooperative behavior, as seen in the Public Goods Game, may stem from its RLHF process, which favors kindness and prosocial actions. Understanding these motivations could offer valuable insights into model alignment and performance tuning. One section of analyzing the reasoning behind the decision is the need for a better explanation of the various performances of LLMs.

### Questions
1. Could you explain why some LLMs, which are typically considered more advanced, do not perform well on this benchmark? For example, models like GPT-4 generally excel in many NLP tasks but underperform in certain games. Could this be due to the influence of ethical considerations embedded in their training (such as RLHF) that conflict with the purely rational strategies required to achieve Nash equilibrium?
2. Is Nash equilibrium the most appropriate evaluation target for LLMs, given that humans often make decisions based on ethical, emotional, or social factors rather than strict rationality? For example, GPT-4 tends to exhibit prosocial behavior, which may prevent it from reaching the Nash equilibrium in certain scenarios like the Diner’s Dilemma. Could the benchmark be expanded to account for human-aligned behavior, considering that LLMs are often used in contexts where replicating human-like decisions is more relevant than adhering to game-theoretic models?

### Soundness
2

### Presentation
3

### Contribution
2
