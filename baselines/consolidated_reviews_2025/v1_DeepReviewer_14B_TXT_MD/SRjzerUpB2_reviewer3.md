### Summary

This paper introduces a novel offline policy optimization algorithm called Fat-to-Thin Policy Optimization (FtTPO) that addresses the challenge of learning sparse continuous policies from logged datasets. The key idea is to maintain a fat (heavy-tailed) proposal policy that learns from the dataset and injects knowledge into a thin (sparse) policy responsible for interacting with the environment. The authors instantiate FtTPO with the general q-Gaussian family and demonstrate its effectiveness in a safety-critical treatment simulation and the MuJoCo suite.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper proposes the first offline policy optimization algorithm specifically designed for sparse continuous policies, addressing a significant gap in the literature.
- The fat-to-thin approach is novel and provides an elegant solution to the out-of-support action issue that plagues sparse policies in offline RL.
- The use of q-Gaussian distributions allows for a unified framework encompassing both heavy-tailed and sparse policies.
- The empirical evaluation is thorough, including ablation studies and comparisons with popular offline RL algorithms.
- The visualization of policy evolution provides valuable insights into the learning process.
- The paper is well-written and clearly explains the motivation, methodology, and results.

### Weaknesses

#### Some Related Works


#### comment

 - The choice of q=0 for the thin policy and q=2 for the fat policy seems somewhat arbitrary. A more detailed justification or sensitivity analysis of these choices would be beneficial. Specifically, the paper lacks a discussion on how these specific q values relate to the desired properties of the fat and thin policies, such as the degree of heaviness in the tails or the level of sparsity. It is unclear why these particular values were chosen over others, and how they might affect the overall performance and stability of the algorithm.
- The paper primarily focuses on the case where safety is explicitly coded into the reward function. It would be interesting to explore how the proposed method could be extended to scenarios where reward and safety need to be considered separately. The current approach does not address situations where safety constraints are not directly reflected in the reward signal, which is a common scenario in real-world applications. The paper should discuss how the method would handle such cases, and whether it would require modifications to the reward function or the learning algorithm itself.
- The performance of FtTPO is sometimes comparable to the best baselines, but it doesn't consistently outperform them across all environments. Further investigation into the limitations of the proposed method would be valuable. While the method shows promise, it is not clear under which conditions it excels or fails compared to existing methods. A more detailed analysis of the environments where FtTPO does not perform as well is needed to understand the limitations of the approach and identify potential areas for improvement.

### Suggestions

The paper should include a more thorough analysis of the impact of the q parameter on the performance of the FtTPO algorithm. Specifically, a sensitivity analysis should be conducted to explore how different values of q for both the fat and thin policies affect the learning process and the final policy performance. This analysis should not only focus on the final performance metrics but also on the properties of the learned policies, such as the sparsity and the heaviness of the tails. The authors should provide a clear explanation of how the choice of q values influences these properties and how they relate to the overall performance of the algorithm. This would provide a more solid foundation for the choice of q=0 and q=2 and help readers understand the trade-offs involved in selecting different q values. Furthermore, the authors should investigate the potential for adaptive selection of q during training, which could lead to more robust and efficient learning.

To address the limitation of relying on safety-coded reward functions, the authors should explore methods for incorporating safety constraints directly into the learning process. This could involve techniques such as constrained optimization or the use of safety critics to guide the learning process. The paper should discuss how these methods could be integrated with the FtTPO framework and how they would affect the performance and safety of the learned policies. Additionally, the authors should consider evaluating the proposed method in environments where safety is not explicitly encoded in the reward function, such as those with safety constraints or penalties. This would provide a more comprehensive evaluation of the method's ability to handle safety in a broader range of scenarios. The authors should also discuss the limitations of the current approach and suggest potential directions for future research in this area.

Finally, the paper should provide a more detailed analysis of the environments where FtTPO does not perform as well as the baselines. This analysis should include a discussion of the characteristics of these environments and how they might affect the performance of the proposed method. The authors should investigate the potential reasons for the performance differences, such as the complexity of the environment, the quality of the offline dataset, or the specific properties of the fat and thin policies. This analysis should also include a discussion of the limitations of the proposed method and suggest potential areas for improvement. Furthermore, the authors should consider comparing the performance of FtTPO with other sparse policy methods, if available, to better understand the strengths and weaknesses of the proposed approach.

### Questions

- How sensitive is the performance of FtTPO to the choice of q values for the fat and thin policies? Is there a principled way to select these values?
- How does the proposed method perform in environments where reward and safety are not explicitly linked?
- What are the limitations of the proposed method, and under which conditions does it fail to outperform existing approaches?

### Rating

6

### Confidence

3

**********
