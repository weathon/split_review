### Summary

This paper studies bandit learning in matching markets with indifference. The authors propose an arm-guided adaptive exploration algorithm and show that it achieves polynomial stable regret. The results are further supported by experiments.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The problem is well-defined and the algorithm is technically sound.
- The paper is overall well-written.

### Weaknesses

#### Some Related Works


#### comment

 - The lower bounds in (Liu et al., 2020) and (Sankararaman et al., 2021) are established for matching markets with strict preferences. It is unclear whether these lower bounds still hold when preferences include indifference. Deriving new lower bounds for the setting with indifference would provide a more accurate assessment of the proposed algorithm's performance.
- The literature on matching with indifference is extensive, yet the paper lacks a review of these works. A discussion on how the stable regret in this paper relates to the notion of stability in the matching with indifference literature would be beneficial. In (Erdil & Ergin, 2008), for instance, Erdil and Ergin introduce various stability concepts, such as stability with indifferences, stability with respect to a strict preference relation, and strict stability, highlighting that these are not equivalent. It is unclear which concept of stability the stable regret in this paper aligns with.
- The assumption that arms know their own preference rankings seems impractical. In many real-world scenarios, arms may also have uncertain preferences that need to be learned.

### Suggestions

The paper should more thoroughly address the relationship between its notion of stable regret and the existing literature on matching with indifference. Specifically, the authors should clarify which concept of stability their work aligns with, given the various definitions proposed by Erdil and Ergin (2008). For instance, if the algorithm aims for stability with indifferences, it should be explicitly stated and justified. Furthermore, a discussion on how the algorithm handles situations where multiple stable matchings exist due to indifference would be valuable. This would involve analyzing the algorithm's behavior in cases where ties in preference rankings lead to multiple possible stable outcomes. The authors should also consider providing examples to illustrate how their algorithm achieves stability in such scenarios, and how the stable regret is affected by the presence of indifferences.

To strengthen the paper's contribution, the authors should derive new lower bounds that are specific to the setting with indifferent preferences. This would provide a more accurate assessment of the proposed algorithm's performance and its optimality. The current comparison to lower bounds derived for strict preference settings is insufficient, as the inclusion of indifferences significantly alters the problem's complexity. The authors should explore the challenges in adapting existing lower bound techniques to the indifference setting or develop new techniques that are tailored to this specific problem. This would involve a deeper analysis of the information-theoretic limits of learning in matching markets with indifference. Additionally, the authors should discuss the implications of their lower bound results for the design of more efficient algorithms.

Finally, the assumption that arms have perfect knowledge of their preference rankings is a significant limitation that should be addressed. In many real-world applications, arms may also have uncertain preferences that need to be learned through interaction. The authors should discuss the implications of this assumption for the applicability of their algorithm. They could consider extending their model to incorporate learning of arm preferences, which would make the work more realistic and impactful. This would likely require a significant modification of the proposed algorithm and analysis, but it would also greatly enhance the paper's contribution. The authors could also discuss the challenges of learning in a decentralized setting where both players and arms have uncertain preferences, and how their approach could be extended to address these challenges.

### Questions

- The lower bounds in (Liu et al., 2020) and (Sankararaman et al., 2021) are established for matching markets with strict preferences. It is unclear whether these lower bounds still hold when preferences include indifference. Deriving new lower bounds for the setting with indifference would provide a more accurate assessment of the proposed algorithm's performance.
- The literature on matching with indifference is extensive, yet the paper lacks a review of these works. A discussion on how the stable regret in this paper relates to the notion of stability in the matching with indifference literature would be beneficial. In (Erdil & Ergin, 2008), for instance, Erdil and Ergin introduce various stability concepts, such as stability with indifferences, stability with respect to a strict preference relation, and strict stability, highlighting that these are not equivalent. It is unclear which concept of stability the stable regret in this paper aligns with.
- The assumption that arms know their own preference rankings seems impractical. In many real-world scenarios, arms may also have uncertain preferences that need to be learned.

### Rating

3

### Confidence

3

**********
