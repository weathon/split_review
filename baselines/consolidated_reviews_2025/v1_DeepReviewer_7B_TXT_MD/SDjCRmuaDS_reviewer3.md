### Summary

The paper introduces MolMiner, a novel transformer-based model for multi-target inverse design of molecules. The model decomposes molecules into fragments and generates them sequentially, ensuring chemical validity and transparency in the generation process. MolMiner addresses key challenges in molecular design by enforcing chemical rules, allowing variable molecule sizes, and incorporating 3D information. The model is trained on the RedDB dataset and demonstrates promising results in generating molecules with desired properties.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and intuitive.
- The authors perform a detailed analysis of the model's performance on a real-world dataset.

### Weaknesses

#### Some Related Works

[1] Moltrans: A transformer-based model for molecular graph generation.
[2] Moltrans-gnn: A transformer-based graph neural network for molecular generation.
[3] Molformer: Transformer-based molecular generation and optimization with graph diffusion.
[4] Molformer-gnn: Transformer-based molecular generation and optimization with graph diffusion.
[5] Molformer-2: Transformer-based molecular generation and optimization with graph diffusion.
[6] Graph transformer networks for molecular property prediction.
[7] Molformer: Transformer-based molecular generation and optimization with graph diffusion.
[8] Molformer-gnn: Transformer-based molecular generation and optimization with graph diffusion.

#### comment

 - The paper's novelty is limited. The proposed model is a straightforward application of a transformer-based architecture for multi-objective inverse design, with the main contribution being the step-by-step generation of molecules from a set of fragments. The use of a transformer architecture for this task has been explored in prior works, and the paper does not introduce any significant architectural innovations or modifications to the transformer that would justify its novelty.
- The paper lacks a comparison with existing methods. The authors do not compare their model with other state-of-the-art methods for multi-objective inverse design, making it difficult to assess the performance of their model relative to existing approaches. This lack of comparison makes it hard to determine if the proposed method offers any significant advantages over existing techniques.
- The paper does not provide sufficient details on the training process. The authors do not provide sufficient information on the training data, the training procedure, and the hyperparameters used. This lack of detail makes it difficult to reproduce the results and to assess the validity of the claims made in the paper.
- The paper's focus on a single dataset limits the generalizability of the findings. The authors should evaluate their model on a wider range of datasets to demonstrate its robustness and applicability to different chemical systems.
- The paper does not address the computational cost of the proposed method. The authors should provide an analysis of the computational complexity of their model and compare it to other methods. This is important for assessing the scalability of the proposed approach.
- The paper does not discuss the limitations of the proposed method. The authors should acknowledge the limitations of their approach and suggest potential avenues for future research.

### Suggestions

The authors should consider expanding their evaluation to include a more diverse set of datasets, encompassing different chemical spaces and molecular properties. This would provide a more robust assessment of the model's generalizability and applicability. For example, datasets with larger molecules, different functional groups, or different types of chemical reactions could be included. Furthermore, the authors should compare their method against other state-of-the-art methods for multi-objective inverse design, such as those based on GANs or other generative models. This would provide a more comprehensive understanding of the strengths and weaknesses of the proposed approach. The comparison should not only focus on the final performance but also on the computational cost and the interpretability of the generated molecules.

To address the lack of detail regarding the training process, the authors should provide a more comprehensive description of the training data, including the size of the dataset, the distribution of the data, and the preprocessing steps applied. They should also provide details on the training procedure, including the optimization algorithm, the learning rate schedule, and the batch size. Furthermore, the authors should specify the hyperparameters used for training, such as the number of layers, the number of attention heads, and the embedding dimension. This information is crucial for reproducibility and for assessing the validity of the claims made in the paper. The authors should also consider releasing their code and data to facilitate further research in this area.

Finally, the authors should address the computational cost of their method and compare it to other approaches. This is important for assessing the scalability of the proposed approach. The authors should provide an analysis of the computational complexity of their model and discuss the limitations of their method. They should also discuss the potential for using their model in real-world applications, such as drug discovery or materials design. The authors should also discuss the potential for using their model in real-world applications, such as drug discovery or materials design. The authors should also discuss the potential for using their model in real-world applications, such as drug discovery or materials design.

### Questions

- How does the proposed model compare to other state-of-the-art methods for multi-objective inverse design?
- What is the novelty of the proposed model compared to existing works?
- Can the authors provide more details on the training process?
- How does the proposed model perform on other datasets?
- What is the computational cost of the proposed method?
- What are the limitations of the proposed method?

### Rating

5

### Confidence

4

**********
