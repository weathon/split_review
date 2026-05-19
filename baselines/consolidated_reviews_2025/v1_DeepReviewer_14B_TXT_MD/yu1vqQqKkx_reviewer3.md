### Summary

This paper proposes a new method called LICO (Large Language Models for In-Context Optimization) for black-box optimization, with a particular application to the molecular domain. The authors equip a pretrained language model with separate embedding layers for molecules and their scores, and a prediction head to predict the score of unseen candidates. They train the model on a diverse set of intrinsic and synthetic functions, and then use it to optimize various molecular properties via in-context prompting. The authors evaluate LICO on the Practical Molecular Optimization (PMO) benchmark, and show that it achieves state-of-the-art performance on 21 optimization objectives.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The authors propose a novel method that leverages pretrained language models for black-box optimization in the molecular domain. The method is general and can be applied to various optimization tasks.
2. The authors train the model on a diverse set of intrinsic and synthetic functions, which enables the model to generalize to unseen molecular properties.
3. The authors evaluate LICO on the PMO benchmark, and show that it achieves state-of-the-art performance on 21 optimization objectives. The authors also perform ablation studies to understand the importance of different components and design choices in LICO.

### Weaknesses

#### Some Related Works


#### comment

1. The authors only evaluate LICO on the PMO benchmark, which may not be representative of all molecular optimization tasks. It would be useful to evaluate LICO on other benchmarks, such as the Guacamol benchmark, to assess its generalization ability.
2. The authors only use one pretrained language model (Llama-2-7b) to extend LICO. It is unclear how the performance of LICO would vary with different language models. It would be useful to investigate the impact of different language models on the performance of LICO.
3. The authors only use one type of synthetic functions (Gaussian Processes with Tanimoto kernel) to train LICO. It is unclear how the performance of LICO would vary with different types of synthetic functions. It would be useful to investigate the impact of different types of synthetic functions on the performance of LICO.

### Suggestions

The authors should consider expanding their evaluation to include the Guacamol benchmark, which offers a more diverse set of molecular optimization tasks, including those focused on generating novel molecules with specific properties, and those aimed at improving upon existing molecules. This would provide a more comprehensive assessment of LICO's generalization capabilities across different types of optimization problems. Specifically, the Guacamol benchmark includes tasks that are not directly covered by the PMO benchmark, such as those that require the model to generate molecules with specific substructures or functional groups, or those that involve multi-objective optimization. Evaluating LICO on these tasks would provide a more robust understanding of its strengths and limitations. Furthermore, the authors should analyze the performance of LICO on individual tasks within the Guacamol benchmark to identify any specific areas where the model excels or struggles, which could provide valuable insights for future improvements.

To address the concern regarding the choice of language model, the authors should conduct a more thorough investigation into the impact of different pretrained language models on LICO's performance. This could involve experimenting with models of varying sizes and architectures, such as smaller models like Phi-2 or larger models like Llama-3. This would help determine whether the performance of LICO is sensitive to the specific language model used, and whether there are any trade-offs between model size and optimization performance. Furthermore, the authors should analyze the computational cost associated with using different language models, as this could be a significant factor in practical applications. It would also be beneficial to explore the impact of different prompting strategies on the performance of LICO when using different language models, as this could reveal whether certain models are more amenable to in-context learning for molecular optimization.

Finally, the authors should explore the impact of different types of synthetic functions on the performance of LICO. While Gaussian Processes with a Tanimoto kernel are a reasonable choice, it is important to investigate whether other types of synthetic functions could lead to improved performance. For example, the authors could consider using randomly initialized neural networks or other types of kernel functions. This would help determine whether the choice of synthetic function is a critical factor in LICO's performance, and whether there are any specific types of synthetic functions that are particularly well-suited for molecular optimization. Furthermore, the authors should analyze the computational cost associated with training LICO with different types of synthetic functions, as this could be a significant factor in practical applications. It would also be beneficial to explore the impact of different hyperparameters of the synthetic functions on the performance of LICO, as this could reveal whether there are any optimal settings for these parameters.

### Questions

1. How does the performance of LICO vary with different pretrained language models?
2. How does the performance of LICO vary with different types of synthetic functions?
3. How does the performance of LICO vary with different hyperparameters of the synthetic functions?

### Rating

6

### Confidence

3

**********
