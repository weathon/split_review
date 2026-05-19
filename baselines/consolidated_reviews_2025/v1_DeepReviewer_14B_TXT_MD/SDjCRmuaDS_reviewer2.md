### Summary

This paper proposes a novel autoregressive model for molecular generation. The authors introduce a fragment-based approach that constructs molecules through interpretable steps, ensuring chemical validity and accommodating variable molecular sizes. The model is demonstrated on a multi-target inverse design task for electroactive organic compounds, showing its ability to generate molecules that meet specific solubility, redox potential, and synthetic accessibility criteria.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

* The paper introduces an autoregressive model that decomposes molecular generation into a sequence of discrete steps using molecular fragments as units, which enhances the interpretability of the generation process.
* The model enforces chemical rules throughout the generation process, ensuring the chemical validity of the generated molecules.
* The approach supports variable molecule sizes, which is crucial for handling the diversity of molecular structures in materials design.

### Weaknesses

#### Some Related Works


#### comment

 * The model's performance is demonstrated on a specific dataset (RedDB) and task (multi-target inverse design), and its generalizability to other types of molecules or materials is not extensively explored. The evaluation lacks diversity in molecular structures and properties, making it difficult to assess the model's robustness across different chemical spaces. For example, the RedDB dataset primarily focuses on quinone-based molecules, which may not be representative of the broader range of organic compounds.
* The model's reliance on a specific set of chemical rules may limit its ability to generate novel molecules that do not adhere to these rules. This could be a limitation when exploring new chemical spaces or materials with unusual bonding patterns. The paper does not specify the exact rules used, making it difficult to assess the scope and limitations of this approach. It is unclear how the model handles edge cases or molecules with non-standard bonding.
* The model's performance is evaluated primarily on its ability to generate molecules that meet specific property criteria, but other important aspects, such as the diversity of the generated molecules and the computational efficiency of the model, are not thoroughly discussed. The paper lacks a quantitative analysis of the diversity of the generated molecules, which is crucial for ensuring that the model does not simply reproduce known structures. Furthermore, the computational cost of the model, including training and inference time, is not reported, making it difficult to assess its practical applicability.

### Suggestions

To address the limitations in generalizability, the authors should evaluate the model on a more diverse set of datasets, including those with different types of molecules and chemical properties. This could include datasets with varying sizes, functional groups, and structural motifs. For example, the authors could test the model on datasets of natural products, drug-like molecules, or materials with different bonding characteristics. Furthermore, the evaluation should include a quantitative analysis of the model's performance across these different datasets, such as the success rate in generating molecules that meet the target properties and the diversity of the generated molecules. This would provide a more comprehensive assessment of the model's generalizability and robustness. The authors should also consider using metrics such as the Fréchet ChemNet Distance (FCD) to quantify the diversity of the generated molecules.

To address the limitations of the rule-based approach, the authors should provide a detailed description of the chemical rules used in the model. This should include the specific bonding rules, valency constraints, and any other chemical constraints that are enforced during the generation process. The authors should also discuss the limitations of these rules and how they might affect the model's ability to generate novel molecules. Furthermore, the authors could explore methods for incorporating more flexible rules or learning rules from data, which could allow the model to generate a wider range of molecules. This could involve using a graph neural network to learn bonding patterns or incorporating a mechanism for handling exceptions to the rules. The authors should also consider how the model handles edge cases or molecules with non-standard bonding.

To address the lack of discussion on computational efficiency, the authors should provide a detailed analysis of the model's computational cost, including the training time, inference time, and memory usage. This analysis should include a breakdown of the computational cost of different parts of the model, such as the fragment selection and docking steps. The authors should also compare the computational cost of their model to other generative models for molecular design. Furthermore, the authors should discuss potential strategies for improving the computational efficiency of the model, such as using more efficient algorithms or parallelizing the computation. This would make the model more practical for real-world applications. The authors should also consider the scalability of the model to larger datasets and more complex molecules.

### Questions

* How does the model handle the generation of very large molecules, and does the performance degrade with increasing molecular size? Specifically, what is the relationship between molecular size and the number of steps required for generation, and how does this affect the computational cost?
* Could the model be extended to incorporate 3D information more explicitly, and how would this affect the generation process and the properties of the generated molecules? For example, how would the model handle steric clashes or other 3D constraints during the generation process?
* How does the model ensure the diversity of the generated molecules, and is there a mechanism to avoid generating similar molecules repeatedly? What metrics are used to quantify the diversity of the generated molecules, and how do these metrics compare to other generative models?
* What are the limitations of the chemical rules used in the model, and how might these rules be expanded or modified to allow for the generation of a wider range of molecules? Are there specific types of molecules or bonding patterns that the model cannot generate due to these rules?

### Rating

3

### Confidence

4

**********
