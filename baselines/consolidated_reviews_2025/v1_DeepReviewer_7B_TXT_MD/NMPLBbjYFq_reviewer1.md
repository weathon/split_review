### Summary

This paper studies the rationality and strategic reasoning ability of LLMs in the context of economics games. The authors design a framework to evaluate the rationality and strategic reasoning ability of LLMs in the context of economics games. They conduct experiments on various LLMs and find that they are not as rational as humans in these games.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The experiments are comprehensive and cover a wide range of LLMs.

### Weaknesses

#### Some Related Works


#### comment

 - The paper lacks a clear definition of rationality and strategic reasoning ability. The authors do not provide a formal definition of these concepts, making it difficult to understand the scope and limitations of their framework. For example, in the context of the beauty contest game, what specific criteria are used to determine if an LLM's behavior is rational or not? Is it based on the number of iterations the LLM takes to converge to a solution, or is it based on some other metric? Similarly, what constitutes strategic reasoning ability? Does it involve the ability to adapt to changing game environments, or does it involve the ability to reason about the strategies of other players? The lack of a clear definition makes it hard to evaluate the validity of the experimental results.
- The paper does not provide a clear explanation of how the LLMs are evaluated in the context of the economics games. The authors do not specify the metrics used to measure the rationality and strategic reasoning ability of the LLMs. For example, in the beauty contest game, how is the rationality of an LLM's behavior measured? Is it based on the number of iterations the LLM takes to converge to a solution, or is it based on some other metric? Similarly, in the second-price auction, how is the strategic reasoning ability of an LLM measured? Is it based on the LLM's ability to bid the optimal price, or is it based on some other metric? The lack of a clear explanation of the evaluation metrics makes it difficult to interpret the experimental results.
- The paper does not provide a clear explanation of how the LLMs are prompted to play the economics games. The authors do not specify the format of the prompts used to elicit the LLMs' behavior. For example, in the beauty contest game, how are the prompts designed to elicit the LLMs' iterative reasoning process? Are the prompts designed to explicitly encourage the LLMs to reason about the strategies of other players? The lack of a clear explanation of the prompting strategy makes it difficult to understand how the LLMs are being evaluated.
- The paper does not provide a clear explanation of how the game environment is designed. The authors do not specify the rules of the game, the payoff structure, and the information available to the players. For example, in the beauty contest game, what is the range of numbers that the players can choose? What is the payoff structure for each player? The lack of a clear explanation of the game environment makes it difficult to understand the experimental setup.
- The paper does not provide a clear explanation of how the experiments are conducted. The authors do not specify the number of trials, the number of players, and the number of iterations. For example, in the beauty contest game, how many iterations are used to evaluate the LLMs' iterative reasoning process? How many players are used in each game? The lack of a clear explanation of the experimental setup makes it difficult to reproduce the results.

### Suggestions

The paper would benefit significantly from a more rigorous definition of rationality and strategic reasoning ability within the context of the economics games. The authors should provide a formal definition of these concepts, specifying the criteria used to evaluate them. For example, in the beauty contest game, rationality could be defined as the number of iterations required for the LLM to converge to a solution that is close to the Nash equilibrium, or as the accuracy of the LLM's prediction of other players' choices. Similarly, strategic reasoning ability could be defined as the LLM's ability to adapt to changing game environments, or its ability to reason about the strategies of other players. The authors should also provide a clear explanation of how these concepts are measured in the experiments. For example, in the beauty contest game, the authors could measure the rationality of an LLM's behavior by comparing its performance to the performance of human players, or by comparing its performance to the performance of a theoretical model. In the second-price auction, the authors could measure the strategic reasoning ability of an LLM by comparing its bidding strategy to the optimal bidding strategy.

Furthermore, the paper needs to provide more details about the experimental setup. The authors should specify the exact prompts used to elicit the LLMs' behavior, including the format and the content of the prompts. For example, in the beauty contest game, the authors should provide the exact text of the prompt that is used to elicit the LLMs' iterative reasoning process. The authors should also specify the rules of the game, the payoff structure, and the information available to the players. For example, in the beauty contest game, the authors should specify the range of numbers that the players can choose, and the payoff structure for each player. The authors should also specify the number of trials, the number of players, and the number of iterations used in each experiment. For example, in the beauty contest game, the authors should specify how many iterations are used to evaluate the LLMs' iterative reasoning process, and how many players are used in each game. The authors should also provide a clear explanation of how the game environment is designed, including the specific parameters and settings used in each experiment.

Finally, the paper should provide a more detailed analysis of the experimental results. The authors should discuss the implications of their findings for the understanding of LLMs' rationality and strategic reasoning ability. For example, the authors could discuss why some LLMs are more rational or strategic than others, and what factors contribute to these differences. The authors should also discuss the limitations of their framework, and suggest directions for future research. For example, the authors could discuss the limitations of using LLMs to play economics games, and suggest ways to improve the evaluation of LLMs' rationality and strategic reasoning ability. The authors should also discuss the potential applications of their framework, and suggest ways to use it to evaluate LLMs in other domains.

### Questions

- How do you define rationality and strategic reasoning ability in the context of the economics games?
- How do you evaluate the rationality and strategic reasoning ability of the LLMs in the experiments?
- How are the LLMs prompted to play the economics games?
- What is the game environment like in the experiments?
- How are the experiments conducted?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
