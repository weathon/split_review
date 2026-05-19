### Summary

This paper proposes to use competitive games as an evaluation for the rationality and strategic reasoning ability of LLMs. The authors find that most of LLMs are rational in the sense of playing strategies that can increase their payoffs, but not the most rational strategies, i.e. Nash Equilibria (NEs). Moreover, when game history are available, certain types of LLMs, such as GPT-4, can converge faster to the NE strategies, which shows a higher level of rationality compared to other models. In the meantime, certain types of LLMs can win more often when game history are available, and the authors argue that the winning rate reflects the reasoning ability with respect to the strategies of other players. The authors also observe that the ability to strictly follow the game rules described by natural languages also vary among the LLMs they tested. Finally, the authors provide an economics arena for the LLMs research community as a dynamic benchmark to test the above mentioned abilities of LLMs, i.e. rationality, strategic reasoning ability, and instruction-following capability.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. 
2. The paper proposes a new evaluation for the rationality and strategic reasoning ability of LLMs, which is interesting and novel. 
3. The paper provides an economics arena for the LLMs research community as a dynamic benchmark to test the above mentioned abilities of LLMs, i.e. rationality, strategic reasoning ability, and instruction-following capability.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not propose a new method for improving the strategic reasoning abilities of LLMs; rather, it focuses on evaluation. While this is valuable, it limits the paper's contribution to providing a benchmark without offering solutions for improvement.
2. The paper only considers games with unique pure Nash Equilibria, which may not fully capture the range of strategic interactions that LLMs might encounter in real-world scenarios, including mixed-strategy equilibria and more complex dynamics.
3. While the paper varies game configurations and opponent types, the scope of these variations may not be sufficient to fully assess the adaptability of LLMs to truly dynamic and unpredictable environments.
4. The paper does not deeply explore the reasons behind the observed behaviors of LLMs in these games, such as why certain models perform better than others or why some models break rules more frequently.
5. The paper does not compare the performance of LLMs to other types of AI agents or to human behavior in the same games, which could provide a more comprehensive understanding of the capabilities and limitations of LLMs.

### Suggestions

The paper's focus on evaluation is a valuable contribution, but it could be strengthened by exploring the underlying mechanisms driving LLM behavior in these economic games. For instance, the authors could investigate the impact of different prompt engineering techniques on the strategic reasoning abilities of LLMs. Specifically, they could explore whether providing explicit instructions about Nash equilibrium or offering examples of rational play influences the convergence to equilibrium strategies. Furthermore, analyzing the internal representations of LLMs during gameplay could shed light on how they process information and make decisions. This could involve examining the activation patterns of different layers in the network or using probing techniques to understand the information encoded in the model's state. Such analyses could help identify the specific limitations of current LLM architectures in strategic reasoning and suggest avenues for improvement.

To address the limitation of focusing solely on pure Nash equilibria, the authors should consider incorporating games with mixed-strategy equilibria and more complex strategic dynamics. For example, they could include games like the matching pennies game, which has a unique mixed-strategy equilibrium, or games with multiple equilibria to assess the ability of LLMs to select among them. Furthermore, they could explore games with sequential moves and imperfect information to evaluate the ability of LLMs to reason about beliefs and counterfactuals. This would provide a more comprehensive assessment of the strategic reasoning capabilities of LLMs and their ability to handle a wider range of real-world scenarios. The analysis should also include a discussion of the convergence rates to equilibrium under different game conditions and with different opponent types, which could reveal the limitations of LLMs in adapting to dynamic environments.

Finally, the paper would benefit from a more thorough comparison of LLM performance to other AI agents and human behavior. The authors could compare the performance of LLMs to reinforcement learning agents trained specifically for these games, which would provide a baseline for evaluating the strategic reasoning abilities of LLMs. Additionally, they could conduct experiments with human subjects to compare their behavior to that of LLMs. This would help to determine whether LLMs exhibit human-like biases or whether they are able to achieve higher levels of rationality. The comparison should also include an analysis of the learning curves of LLMs and humans, which could reveal the speed and efficiency of learning in these different agents. Such comparisons would provide a more comprehensive understanding of the capabilities and limitations of LLMs in strategic reasoning.

### Questions

1. How do you ensure that the LLMs understand the economic games and follow the instructions accurately?
2. What are the specific criteria used to measure the rationality and strategic reasoning abilities of LLMs in these games?
3. How do you control for the variability in LLM responses due to factors like prompt engineering or randomness in the models' outputs?
4. Can the proposed framework be extended to more complex games with multiple equilibria or incomplete information?
5. How do the findings of this paper contribute to the broader understanding of the capabilities and limitations of LLMs in real-world applications?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
