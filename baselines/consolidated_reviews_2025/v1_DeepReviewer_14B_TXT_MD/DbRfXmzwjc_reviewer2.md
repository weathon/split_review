### Summary

This paper proposes a novel motif-agnostic generation model of molecules from shapes (MAGNet), which generates abstract shapes before allocating atom and bond types. The factorisation of the molecules’ data distribution that accounts for the molecules’ global context and facilitates learning adequate assignments of atoms and bonds onto shapes is introduced. The experimental results show that MAGNet outperforms the selected baselines on standard benchmarks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The structure of the paper is clear and easy to follow.
2. The idea of generating molecules from shapes is interesting and novel.
3. The experimental results show the effectiveness of the proposed model.

### Weaknesses

#### Some Related Works


#### comment

1. The validity of SM-LSTM is 100% in Table 5, but the validity of MAGNet is less than 100%. The novelty and uniqueness of MAGNet are 100%, but those of SM-LSTM are also 100%. Why is SM-LSTM included in the comparison? The inclusion of SM-LSTM, given its perfect validity, uniqueness, and novelty, does not provide a meaningful comparison for the core generative capabilities of MAGNet. The paper should clarify the specific rationale for including this baseline, especially when the primary focus is on the structural and chemical validity of generated molecules, where SM-LSTM performs perfectly.
2. The results of the ablation study are not surprising. For example, it is obvious that MAGNet without any component is the worst. The ablation study, as presented, lacks depth and does not provide significant insights into the model's architecture. The removal of each component and the resulting performance drop is predictable, and the study fails to explore the nuanced interactions between different parts of the model. A more detailed ablation study should investigate the specific contributions of each component and their impact on the generated molecular structures, rather than just showing a general performance decline.

### Suggestions

The paper should provide a more detailed justification for the inclusion of SM-LSTM as a baseline. While it is understood that SM-LSTM is a popular method, the paper needs to articulate why comparing against a model with perfect validity, uniqueness, and novelty is valuable for evaluating the proposed MAGNet. The authors should clarify whether the comparison is intended to highlight different aspects of the models, such as computational efficiency or the ability to generate specific types of molecules. If the comparison is meant to demonstrate MAGNet's ability to generate valid molecules, then the paper should explicitly state this and explain why SM-LSTM is still a relevant benchmark despite its perfect scores in other metrics. Furthermore, the paper should consider including additional baselines that are more directly comparable to MAGNet in terms of their generative capabilities, especially those that focus on structural and chemical validity.

The ablation study needs to be significantly enhanced to provide more meaningful insights into the model's architecture. Instead of simply removing components and observing a performance drop, the authors should investigate the specific contributions of each component and their impact on the generated molecular structures. For example, the study could analyze how the removal of the shape representation module affects the diversity of generated molecules or how the atom and bond allocation module influences the chemical validity of the results. The authors could also explore the interactions between different components, such as how the shape generation module influences the atom allocation process. This would provide a more nuanced understanding of the model's inner workings and the importance of each component. The ablation study should also include a quantitative analysis of the generated molecules, such as the distribution of molecular weights, ring sizes, and bond types, to provide a more detailed picture of the impact of each component.

Finally, the paper should provide more details on the implementation of the model, including the specific hyperparameters used for training and the computational resources required. This would allow other researchers to reproduce the results and build upon the proposed work. The paper should also discuss the limitations of the proposed approach and suggest potential directions for future research. For example, the authors could discuss the challenges of generating molecules with specific properties or the limitations of the shape-based representation for certain types of molecules. Addressing these limitations would provide a more balanced view of the proposed method and highlight areas for further improvement.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
