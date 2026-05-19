### Summary

This paper studies the problem of learning in matching markets with indistinguishable preferences. The authors propose an algorithm with polynomial regret bound. The paper also provides a lower bound for the problem.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and addresses an interesting problem.
2. The proposed algorithm is simple and intuitive, and the analysis is sound.
3. The paper also provides a lower bound for the problem, which is helpful for understanding the problem.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed discussion of the limitations of the proposed algorithm. For example, it is not clear how the algorithm would perform in settings with more complex preference structures or in the presence of strategic behavior by participants. Specifically, the algorithm's reliance on a single exploration phase may not be robust to scenarios where preferences evolve over time or where there are multiple stable matchings, potentially leading to suboptimal outcomes. The analysis does not address the potential for the algorithm to get stuck in local optima, especially if the exploration phase is not carefully tuned to the specific problem instance.
2. The paper does not provide a detailed discussion of the practical implications of the algorithm. For example, it is not clear how the algorithm would perform in real-world settings with noisy or incomplete preference data. The paper lacks a discussion on the computational complexity of the algorithm in practice, and how it scales with the size of the market. Furthermore, the paper does not address the practical challenges of implementing the algorithm in a dynamic environment where new participants may join or leave the market, or where preferences may change over time. The assumption of a single exploration phase may not be practical in real-world scenarios where continuous learning and adaptation are necessary.
3. The paper does not provide a detailed discussion of the potential for the algorithm to be used in real-world applications. For example, it is not clear how the algorithm could be adapted to different types of matching markets or how it could be integrated with existing matching mechanisms. The paper does not discuss the potential ethical implications of using the algorithm, such as the possibility of bias in the matching process or the potential for manipulation by participants. The paper also does not address the limitations of the algorithm in terms of its ability to handle large-scale markets or its robustness to adversarial behavior.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of the proposed algorithm. Specifically, the authors should analyze the algorithm's performance under more complex preference structures, such as those involving cyclic preferences or preferences with varying degrees of similarity. The current analysis focuses on a relatively simple setting, and it is unclear how the algorithm would behave in more realistic scenarios. For example, the paper should investigate the algorithm's robustness to strategic behavior by participants, such as manipulation of the preference elicitation process. Furthermore, the authors should explore the potential for the algorithm to get stuck in local optima, especially if the exploration phase is not carefully tuned to the specific problem instance. A more detailed analysis of these limitations would provide a more complete understanding of the algorithm's applicability and limitations.

To enhance the practical relevance of the paper, the authors should provide a more detailed discussion of the algorithm's performance in real-world settings. This should include an analysis of how the algorithm would perform with noisy or incomplete preference data, which is common in real-world scenarios. The paper should also address the computational complexity of the algorithm and how it scales with the size of the market. Furthermore, the authors should discuss the practical challenges of implementing the algorithm in a dynamic environment where new participants may join or leave the market, or where preferences may change over time. The assumption of a single exploration phase may not be practical in real-world scenarios where continuous learning and adaptation are necessary. A more detailed discussion of these practical considerations would make the paper more relevant to practitioners.

Finally, the paper should provide a more detailed discussion of the potential for the algorithm to be used in real-world applications. This should include an analysis of how the algorithm could be adapted to different types of matching markets, such as labor markets, school choice, or organ transplantation. The authors should also discuss how the algorithm could be integrated with existing matching mechanisms. Furthermore, the paper should address the potential ethical implications of using the algorithm, such as the possibility of bias in the matching process or the potential for manipulation by participants. The paper should also address the limitations of the algorithm in terms of its ability to handle large-scale markets or its robustness to adversarial behavior. A more comprehensive discussion of these practical and ethical considerations would make the paper more impactful.

### Questions

1. How would the algorithm perform in settings with more complex preference structures or in the presence of strategic behavior by participants?
2. How would the algorithm perform in real-world settings with noisy or incomplete preference data?
3. How could the algorithm be adapted to different types of matching markets or how could it be integrated with existing matching mechanisms?
4. What are the potential ethical implications of using the algorithm?
5. How should the exploration parameter be chosen in practice?

### Rating

6

### Confidence

3

**********
