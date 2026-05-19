### Summary

The paper studies the behavior of LLMs in two simple games: a beauty contest and a second price auction. In both games, there is a unique Nash equilibrium and it is easy to verify whether a bid is NE or not. The authors use this to evaluate how close the LLM's bid is to the NE. They also evaluate how the LLM's bid changes when the game configuration changes (e.g., the range from which the numbers are picked in the beauty contest) or when the other players change. Finally, they evaluate how the LLM's bid changes when given the history of the game. They also evaluate how often the LLM breaks the rules of the game.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The experiments are well-designed and the results are interesting. The authors also propose some interesting metrics to evaluate the LLM's behavior.

### Weaknesses

#### Some Related Works


#### comment

The paper has a few weaknesses. First, the games studied are very simple and may not capture the full range of LLM's capabilities. Second, the paper does not provide much insight into why the LLMs behave the way they do. Third, the paper does not compare the LLM's behavior to that of humans.

### Suggestions

The paper would benefit from a more thorough investigation into the limitations of using simple games to evaluate LLM behavior. While the beauty contest and second-price auction provide clear metrics for assessing rationality, they may not fully capture the complexities of strategic reasoning that LLMs are capable of. For example, the paper could explore games with more complex payoff structures, or games that require more sophisticated forms of reasoning, such as those involving deception or cooperation. This would provide a more comprehensive understanding of the LLM's strategic capabilities and limitations. Furthermore, the paper should consider the impact of the specific prompt design on the LLM's behavior. It is possible that the way the game is presented to the LLM could influence its bidding strategy. A more systematic analysis of how different prompt variations affect the LLM's behavior would be valuable.

To address the lack of insight into why LLMs behave the way they do, the authors could explore techniques for interpreting the LLM's internal representations. For example, they could analyze the activation patterns of different layers in the LLM to understand which features are most relevant for making bidding decisions. This could provide a more fine-grained understanding of the LLM's reasoning process. Additionally, the paper could investigate the impact of different training data on the LLM's behavior. It is possible that the LLM's bidding strategy is influenced by the type of data it was trained on. A more detailed analysis of the LLM's training data and its relationship to the observed behavior would be beneficial. The paper could also explore the use of techniques such as adversarial attacks to test the robustness of the LLM's bidding strategy.

Finally, the paper should include a more detailed comparison of the LLM's behavior to that of humans. While the authors mention that some LLMs achieve higher payoffs than humans, they do not provide a detailed analysis of the differences in behavior. A more systematic comparison of the LLM's bidding strategy to that of human players would be valuable. This could involve analyzing the distribution of bids, the convergence to equilibrium, and the sensitivity to changes in game parameters. The paper could also explore the use of behavioral models to characterize the LLM's behavior. This would provide a more rigorous framework for comparing the LLM's behavior to that of humans and could help to identify any systematic biases or deviations from rationality.

### Questions

1. How do you ensure that the LLM understands the game and the rules?
2. How do you measure the LLM's rationality?
3. How do you compare the LLM's behavior to that of humans?
4. How do you interpret the results of your experiments?
5. What are the limitations of your approach?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
