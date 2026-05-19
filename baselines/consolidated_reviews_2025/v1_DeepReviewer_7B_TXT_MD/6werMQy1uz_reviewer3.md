### Summary

The paper introduces an open-source simulated digital marketplace where agents (LLMs) can act as both buyers and sellers of information. The central mechanism of this marketplace is the ability of agents to preview and purchase information before it is fully disclosed. This mechanism is designed to address the "buyer’s inspection paradox" in information markets, where buyers typically need access to information to evaluate its value before making a purchase. The authors conduct a series of experiments to investigate the impact of this preview mechanism on the quality of information purchased, the effects of different pricing strategies, and the rationality of LLM-based agents in decision-making. The findings indicate that allowing agents to inspect information before purchase significantly improves the quality of the information they acquire, and that agents can make rational decisions when inspection is permitted. The paper also explores the dynamics of the marketplace, including the impact of different credit budgets and the role of LLM-based agents in overall performance.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper addresses a significant gap in the literature by exploring the dynamics of information markets with LLM-based agents. The use of LLMs as both buyers and sellers is a novel approach that provides valuable insights into the behavior of these agents in a simulated environment.
- The concept of allowing agents to preview and purchase information before full disclosure is innovative and addresses a key challenge in information markets, where buyers often need access to information to evaluate its value. This mechanism has the potential to improve the efficiency and quality of information exchange in real-world scenarios.
- The paper presents a comprehensive set of experiments that explore various aspects of the information marketplace, including the impact of different pricing strategies, the role of LLM-based agents in decision-making, and the dynamics of the marketplace under different conditions. The experiments are well-designed and provide valuable insights into the behavior of the agents.
- The paper is well-written and clearly explains the methodology, experiments, and results. The use of figures and tables effectively communicates the key findings of the study.

### Weaknesses

#### Some Related Works


#### comment

 - While the paper introduces an open-source simulated digital marketplace, it lacks a detailed discussion of the limitations of the simulation environment and the potential impact of these limitations on the generalizability of the findings. For example, the paper does not address the potential for biases in the LLM-based agents or the limitations of the information model used in the simulation.
- The paper does not provide a thorough analysis of the economic principles underlying the design of the marketplace. While the paper introduces the concept of the "buyer’s inspection paradox," it does not delve into the broader economic theories that could inform the design of the marketplace. This lack of theoretical grounding may limit the paper's contribution to the field of information economics.
- The paper does not explore the potential for strategic behavior by the LLM-based agents. While the experiments demonstrate the behavior of the agents under different conditions, they do not investigate the potential for agents to manipulate the marketplace through strategic behavior, such as gaming the preview mechanism or engaging in collusion.
- The paper does not provide a detailed discussion of the ethical implications of using LLM-based agents in information markets. While the paper acknowledges the potential for bias in LLMs, it does not explore the broader ethical considerations of using these agents in real-world scenarios, such as the potential for manipulation or the impact on human users.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations inherent in the simulated environment. Specifically, the authors should address the potential for biases in the LLM-based agents, which could arise from the training data used to develop the models or from the specific prompts used to control their behavior. These biases could significantly impact the results of the experiments and limit the generalizability of the findings. Furthermore, the authors should discuss the limitations of the information model used in the simulation. The model may not capture the full complexity of real-world information environments, and the authors should acknowledge this limitation and discuss how it might affect the results. A more detailed analysis of these limitations would strengthen the paper and provide a more realistic assessment of the proposed approach.

To enhance the theoretical grounding of the paper, the authors should delve deeper into the economic principles that underlie the design of the marketplace. While the paper introduces the concept of the "buyer’s inspection paradox," it would be beneficial to explore the broader economic theories that could inform the design of the marketplace. For example, the authors could discuss the concept of information asymmetry and how it relates to the design of the preview mechanism. They could also explore the economic principles of market equilibrium and how they might be affected by the introduction of the preview mechanism. A more thorough theoretical analysis would provide a stronger foundation for the paper and enhance its contribution to the field of information economics. This would also help to contextualize the experimental results and provide a more nuanced understanding of the dynamics of the marketplace.

Finally, the paper should address the potential for strategic behavior by the LLM-based agents. The authors should investigate the potential for agents to manipulate the marketplace through strategic behavior, such as gaming the preview mechanism or engaging in collusion. For example, agents could try to game the system by providing false information or by colluding with other agents to manipulate the outcome of the marketplace. The authors should also discuss the ethical implications of using LLM-based agents in information markets. While the paper acknowledges the potential for bias in LLMs, it does not explore the broader ethical considerations of using these agents in real-world scenarios. The authors should discuss the potential for manipulation, the impact on human users, and the need for safeguards to prevent harm. A more thorough discussion of these issues would strengthen the paper and provide a more comprehensive assessment of the potential impact of the proposed approach.

### Questions

- How do you plan to address the limitations of the simulation environment in future work? Specifically, how do you plan to incorporate more realistic models of information and agent behavior?
- How do you plan to extend the theoretical framework to incorporate broader economic principles that could inform the design of the marketplace?
- How do you plan to address the potential for strategic behavior by the LLM-based agents in future work?
- How do you plan to address the ethical implications of using LLM-based agents in information markets in future work?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
