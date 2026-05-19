### Summary

This paper proposes a transformer-based autoregressive model for fragment-based molecular generation. The model decomposes molecular generation into a sequence of discrete steps using molecular fragments as units, ensuring chemical validity and interpretability. The authors demonstrate the model's effectiveness in multi-target inverse design, focusing on properties like solubility, redox potential, and synthetic accessibility.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel approach to molecular generation by using a fragment-based autoregressive model, which addresses the challenge of generating chemically valid molecules.
2. The model's ability to incorporate spatial information and handle variable molecule sizes is a significant advancement in the field.
3. The authors demonstrate the model's effectiveness in multi-target inverse design, showing its potential for practical applications in materials science and drug discovery.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed comparison with existing molecular generation models, particularly those using fragment-based approaches. This makes it difficult to assess the novelty and advantages of the proposed method. Specifically, the paper should compare against models that also use a fragment-based approach, such as those employing recurrent neural networks or other sequence-based models, to highlight the specific advantages of the transformer architecture. A comparison should also be made against models that use different molecular representations, such as graph-based models, to understand the impact of the fragment-based approach.
2. The evaluation of the model is limited to a specific dataset and set of properties. It is unclear how the model would perform on other types of molecules or different target properties. The paper should include an analysis of the model's performance on a more diverse set of molecules, including those with different sizes and structural complexities. Furthermore, the evaluation should include a broader range of target properties, such as binding affinity or toxicity, to demonstrate the general applicability of the model.

### Suggestions

To address the lack of detailed comparison with existing models, the authors should include a comprehensive benchmark against several state-of-the-art molecular generation methods. This should include fragment-based models that use recurrent neural networks or other sequence-based architectures, as well as models that use different molecular representations, such as graph-based models. The comparison should not only focus on the final performance metrics but also on the computational cost, training time, and the interpretability of the generated molecules. For example, the authors could compare the number of parameters, the training time per epoch, and the inference time for generating a molecule of a given size. Furthermore, the authors should analyze the generated molecules to understand the differences in the structural properties and the chemical validity of the generated molecules. This would provide a more complete picture of the advantages and disadvantages of the proposed method compared to existing approaches.

To address the limited evaluation, the authors should expand the evaluation to include a more diverse set of molecules and target properties. This should include molecules with different sizes, structural complexities, and chemical functionalities. The authors should also consider using a benchmark dataset that includes a wide range of molecules and properties, such as the ZINC database or the MOSES benchmark. Furthermore, the evaluation should include a broader range of target properties, such as binding affinity, toxicity, or other relevant properties for materials science and drug discovery. The authors should also analyze the performance of the model on different types of molecules and properties to understand the limitations of the model and identify areas for future improvement. For example, the authors could analyze the performance of the model on small molecules versus large molecules, or on molecules with different functional groups.

Finally, the authors should provide a more detailed analysis of the model's ability to handle variable molecule sizes. While the paper mentions that the model can handle variable molecule sizes, it lacks a detailed analysis of how the model performs on molecules of different sizes. The authors should include an analysis of the model's performance on molecules of different sizes, including the computational cost, the training time, and the quality of the generated molecules. This analysis should also include a comparison of the model's performance on small molecules versus large molecules, and the authors should discuss the limitations of the model in handling very large molecules. This would provide a more complete understanding of the model's capabilities and limitations.

### Questions

1. How does the model handle the trade-off between exploration and exploitation during the generation process? Are there any mechanisms in place to encourage the generation of novel molecules while still ensuring chemical validity?
2. Can the model be extended to incorporate 3D information more explicitly, and how would this affect the generation process and the properties of the generated molecules?
3. What are the computational requirements for training and deploying the model, and how do they scale with the size of the molecule and the complexity of the target properties?

### Rating

6

### Confidence

3

**********
