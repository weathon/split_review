### Summary

This paper proposes a novel prompting framework, Problem Representation Enhanced CoT (PreCoT), which enhances the solution process of LLMs with problem representation. PreCoT extracts the ingredients of the initial and goal state of the problem, which constitute the problem representation together. Then, it initiates an enhanced solution process based on the generated problem representation. In extensive evaluation on benchmarks from a wide range of domains, including arithmetic, commonsense, and symbolic reasoning, PreCoT outperforms CoT on most tasks in both few-shot and zero-shot manners.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The idea of PreCoT is simple and effective. It is inspired by the human problem-solving process, which is interesting.

2. The authors evaluate PreCoT on 15 benchmarks across three reasoning categories, demonstrating its effectiveness.

3. The authors provide code for reproducibility.

### Weaknesses

#### Some Related Works


#### comment

1. The authors should compare PreCoT with other prompting methods, such as self-consistency.

2. The authors should discuss the limitations of PreCoT.

### Suggestions

The paper introduces an interesting approach by incorporating problem representation into the prompting of large language models. However, the evaluation could be strengthened by comparing against a wider range of prompting techniques. Specifically, self-consistency, which involves generating multiple responses and selecting the most consistent one, is a powerful method that should be included in the comparison. This would provide a more comprehensive understanding of the relative performance of PreCoT. Furthermore, it would be beneficial to analyze the computational cost of PreCoT compared to other methods, as the extraction of problem representation might introduce additional overhead. A detailed analysis of the time and resources required for PreCoT would be valuable for practical applications.

In addition to comparing against other prompting methods, a more thorough discussion of the limitations of PreCoT is needed. While the paper demonstrates the effectiveness of PreCoT on a variety of tasks, it is important to acknowledge potential failure cases. For example, it would be useful to explore scenarios where the problem representation is not easily extracted or where the extracted representation is misleading. Understanding these limitations would help to identify areas for future improvement and provide a more balanced perspective on the applicability of PreCoT. The authors should also consider the sensitivity of PreCoT to the quality of the extracted problem representation. How does the performance of PreCoT vary with different levels of noise or inaccuracies in the extracted representation? Addressing these questions would provide a more complete picture of the robustness of the proposed method.

Finally, the paper could benefit from a more detailed analysis of the types of problems where PreCoT excels and where it struggles. Are there specific characteristics of problems that make them more amenable to the problem representation approach? For instance, does PreCoT perform better on problems with a clear initial state and goal state, or does it also work well on problems with more ambiguous or complex problem spaces? A deeper analysis of the problem characteristics would help to identify the niche where PreCoT is most effective and provide guidance for future research. Furthermore, it would be beneficial to explore the potential for combining PreCoT with other prompting techniques to further improve performance. For example, could PreCoT be used in conjunction with self-consistency to achieve even better results? Investigating these possibilities would be a valuable direction for future work.

### Questions

N/A

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
