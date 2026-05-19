### Summary

The paper studies the problem of learning in matching markets with indistinguishable preferences. The authors provide an algorithm with polynomial regret bound. The paper also provides a lower bound for the problem.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper is well-written and addresses an interesting problem. The proposed algorithm is simple and intuitive, and the analysis is sound. The paper also provides a lower bound for the problem, which is helpful for understanding the problem.

### Weaknesses

#### Some Related Works


#### comment

The paper has several weaknesses, which are detailed in the following sections.

1. The paper does not provide a detailed discussion of the limitations of the proposed algorithm. For example, it is not clear how the algorithm would perform in settings with more complex preference structures or in the presence of strategic behavior by participants. Specifically, the algorithm's reliance on a single exploration phase may not be robust to scenarios where preferences evolve over time or where there are multiple stable matchings, potentially leading to suboptimal outcomes. The analysis does not address the potential for the algorithm to get stuck in local optima, especially if the exploration phase is not carefully tuned to the specific problem instance.

2. The paper does not provide a detailed discussion of the practical implications of the algorithm. For example, it is not clear how the algorithm would perform in real-world settings with noisy or incomplete preference data. The paper lacks a discussion on the computational complexity of the algorithm in practice, and how it scales with the size of the market. Furthermore, the paper does not address the practical challenges of implementing the algorithm in a dynamic environment where new participants may join or leave the market, or where preferences may change over time. The assumption of a single exploration phase may not be practical in real-world scenarios where continuous learning and adaptation are necessary.

3. The paper does not provide a detailed discussion of the potential for the algorithm to be used in real-world applications. For example, it is not clear how the algorithm could be adapted to different types of matching markets or how it could be integrated with existing matching mechanisms. The paper does not discuss the potential ethical implications of using the algorithm, such as the possibility of bias in the matching process or the potential for manipulation by participants. The paper also does not address the limitations of the algorithm in terms of its ability to handle large-scale markets or its robustness to adversarial behavior.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of the proposed algorithm. Specifically, the authors should analyze the algorithm's performance under more complex preference structures, such as those involving cyclic preferences or preferences with varying degrees of similarity. The paper should also explore the algorithm's robustness to strategic behavior by participants, such as manipulation of the preference elicitation process. Furthermore, the authors should investigate the potential for the algorithm to get stuck in local optima and propose mechanisms to mitigate this issue. A more detailed analysis of the algorithm's computational complexity and scalability is also needed, especially in the context of large-scale markets. The authors should also discuss the practical challenges of implementing the algorithm in real-world settings, such as dealing with noisy or incomplete preference data, and the need for continuous learning and adaptation in dynamic environments.

To enhance the practical relevance of the paper, the authors should provide a more detailed discussion of how the algorithm could be adapted to different types of matching markets. For example, the paper could explore the applicability of the algorithm to labor markets, school choice, or organ transplantation. The authors should also discuss the potential ethical implications of using the algorithm, such as the possibility of bias in the matching process or the potential for manipulation by participants. A thorough analysis of these ethical considerations is crucial for ensuring the responsible use of the algorithm. The paper should also address the limitations of the algorithm in terms of its ability to handle large-scale markets, and its robustness to adversarial behavior. For example, the authors could investigate the algorithm's performance under different levels of noise in the preference data, or in the presence of malicious participants who try to manipulate the matching process.

Finally, the paper should provide more concrete guidance on how to choose the exploration parameter in practice. The authors should discuss how the exploration parameter should be set in different market settings, and how it should be adjusted in response to changes in the market conditions. The paper should also provide a more detailed analysis of the trade-off between exploration and exploitation, and how this trade-off affects the performance of the algorithm. The authors should also discuss the potential for using adaptive exploration strategies that adjust the exploration parameter based on the observed performance of the algorithm. A more detailed discussion of these practical considerations would greatly enhance the value of the paper.

### Questions

1. How would the algorithm perform in settings with more complex preference structures or in the presence of strategic behavior by participants?

2. How would the algorithm perform in real-world settings with noisy or incomplete preference data?

3. How could the algorithm be adapted to different types of matching markets or integrated with existing matching mechanisms?

4. What are the potential ethical implications of using the algorithm?

5. How should the exploration parameter be chosen in practice?

### Rating

5

### Confidence

3

**********
