### Summary

The paper introduces Memoria, a memory network based on Hebbian theory, designed to enhance the processing of long-term dependencies in neural networks. The architecture stores and retrieves information, referred to as engrams, across three memory levels: working memory, short-term memory, and long-term memory. Experiments with Transformer-based models, such as BERT and GPT, demonstrate that Memoria significantly improves the models' ability to handle long-term dependencies in tasks like sorting, language modeling, and long text classification.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The concept of integrating Hebbian theory into deep learning is interesting.

### Weaknesses

#### Some Related Works


#### comment

1. The paper has poor writing and is difficult to follow.
2. The paper lacks a clear research question, making it difficult to understand the study's purpose and objectives.
3. The paper fails to adequately compare Memoria with other memory-augmented neural networks, such as NTM and DNC, which are relevant to the study's focus.
4. The experimental setup is not well-explained, particularly regarding the choice of datasets and the rationale behind the selected tasks.
5. The results presented in Table 3 lack statistical significance testing, making it difficult to assess the validity of the claims.

### Suggestions

The paper needs significant improvements in clarity and experimental design. First, the authors should clearly define the research question they are trying to answer. Is the goal to improve long-range dependency modeling, or is it to create a biologically plausible memory system? Currently, the paper seems to be trying to achieve both, which leads to a lack of focus. The introduction should be rewritten to clearly state the problem, the proposed solution, and the specific contributions of the work. The paper should also clearly explain the motivation behind the design choices, especially the use of Hebbian learning. While the concept is interesting, the paper does not adequately explain why Hebbian learning is the right choice for this particular problem, and how it compares to other memory mechanisms.

Second, the experimental setup needs to be significantly improved. The authors should provide a clear rationale for the choice of datasets and tasks. For example, why is the sorting task used, and what does it demonstrate? The paper should also include a detailed description of the experimental setup, including the hyperparameters used, the training procedure, and the evaluation metrics. Furthermore, the paper should include a thorough comparison with existing memory-augmented neural networks, such as NTM and DNC. While these models may not be directly applicable to the transformer architecture, a comparison is still necessary to understand the relative strengths and weaknesses of Memoria. The authors should also consider comparing their model with other transformer variants that address long-range dependencies, such as those using sparse attention or recurrent architectures. The current comparison with vanilla transformer, transformer-XL, and compressive transformer is insufficient.

Finally, the paper needs to include statistical significance testing for all results. The current results in Table 3 are not convincing without statistical analysis. The authors should also provide a more detailed analysis of the results, including error analysis and ablation studies. For example, how does the performance of Memoria vary with different memory sizes? How does the performance vary with different Hebbian learning parameters? The paper should also include a discussion of the limitations of the proposed approach and potential directions for future research. The current discussion is too brief and does not adequately address the limitations of the work.

### Questions

1. Why do you need Hebbian learning? What is the motivation behind it?
2. What is the research question of the paper?
3. Why do you need the sorting task? What is the rationale behind the experimental setup?
4. How does your model perform compared to NTM and DNC?
5. Table 3 lacks the significance test, which needs to be filled.

### Rating

3

### Confidence

4

**********
