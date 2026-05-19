### Summary

The paper presents a transformer-based architecture for multi-objective inverse design of molecules. The proposed model generates molecules by growing them step-by-step from a set of fragments. The model takes in a set of target properties and outputs a probability distribution over the next fragment to be added to the molecule. The authors demonstrate the performance of their model on a dataset of organic molecules for predicting log-solubility, redox potential, and synthetic accessibility.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The proposed model is simple and intuitive.
- The authors perform a detailed analysis of the model's performance on a real-world dataset.

### Weaknesses

#### Some Related Works


#### comment

 - The paper's novelty is limited. The proposed model is a straightforward application of a transformer-based architecture for multi-objective inverse design, with the main contribution being the step-by-step generation of molecules from a set of fragments. The use of a transformer architecture for this task has been explored in prior works, and the paper does not introduce any significant architectural innovations or modifications to the transformer that would justify its novelty.
- The paper lacks a comparison with existing methods. The authors do not compare their model with other state-of-the-art methods for multi-objective inverse design, making it difficult to assess the performance of their model relative to existing approaches. This lack of comparison makes it hard to determine if the proposed method offers any significant advantages over existing techniques.
- The paper does not provide sufficient details on the training process. The authors do not provide sufficient information on the training data, the training procedure, and the hyperparameters used. This lack of detail makes it difficult to reproduce the results and to assess the validity of the claims made in the paper.

### Suggestions

The authors should consider comparing their model against a wider range of existing methods for multi-objective inverse design. This would provide a more comprehensive evaluation of the model's performance and allow for a better understanding of its strengths and weaknesses. Specifically, the authors should compare their model against methods that use different generative models, such as GANs or VAEs, and methods that use different approaches for multi-objective optimization. This would help to determine if the proposed method offers any significant advantages over existing techniques. Furthermore, the authors should provide a more detailed description of the training process, including the size of the training dataset, the training procedure, and the hyperparameters used. This would allow other researchers to reproduce the results and to assess the validity of the claims made in the paper. The authors should also consider releasing their code and data to further facilitate reproducibility.

To improve the novelty of the work, the authors could explore more sophisticated methods for fragment selection or generation. For example, they could investigate the use of reinforcement learning to learn a policy for selecting the next fragment to add to the molecule. This could potentially lead to the generation of more complex and novel molecules. Additionally, the authors could explore the use of attention mechanisms to focus on specific parts of the molecule during the generation process. This could potentially improve the quality of the generated molecules and allow for the generation of molecules with specific properties. The authors should also consider incorporating domain knowledge into the model, such as the use of chemical rules or constraints, to further improve the quality of the generated molecules.

Finally, the authors should provide a more detailed analysis of the generated molecules, including their properties and their chemical structures. This would allow for a better understanding of the model's behavior and to identify potential areas for improvement. The authors should also consider evaluating the model on a wider range of datasets, including datasets with different types of molecules and different target properties. This would help to assess the generalizability of the model and to identify potential limitations. The authors should also consider comparing their model against other methods for multi-objective optimization, such as evolutionary algorithms or particle swarm optimization, to determine if the proposed method offers any advantages over existing techniques.

### Questions

- How does the proposed model compare to other state-of-the-art methods for multi-objective inverse design?
- What is the novelty of the proposed model compared to existing works?
- Can the authors provide more details on the training process?

### Rating

3

### Confidence

4

**********
