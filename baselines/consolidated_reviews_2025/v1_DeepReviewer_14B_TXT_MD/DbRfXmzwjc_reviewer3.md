### Summary

The paper introduces a novel approach for generating molecules using graph-based models. The authors identify the limitations of existing models that rely on substructures (motifs) and propose a new model, MAGNet, which generates abstract shapes before allocating atom and bond types. This approach aims to overcome the limitations of motif-based methods and improve the representation of substructures. The paper demonstrates that MAGNet outperforms other graph-based approaches on standard benchmarks and shows improved expressivity, leading to molecules with more topologically distinct structures and diverse atom and bond assignments.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel factorization of molecules' data distribution that accounts for the molecules' global context, which is a significant advancement in the field of molecule generation.

2. The proposed MAGNet model demonstrates superior performance compared to other graph-based approaches on standard benchmarks, indicating its effectiveness in generating molecules with topologically distinct structures.

3. The paper provides a thorough analysis of the proposed method, including comparisons with existing approaches and evaluations on standard benchmarks, which strengthens the credibility of the findings.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion on the computational complexity and scalability of the proposed MAGNet model. Understanding the computational requirements and limitations of the model is crucial for its practical application in real-world scenarios.

2. While the paper demonstrates the effectiveness of MAGNet on standard benchmarks, it would be valuable to see its performance on a wider range of datasets and real-world applications. This would provide a more comprehensive evaluation of the model's generalizability and robustness.

### Suggestions

The paper should include a more rigorous analysis of the computational complexity of the MAGNet model. Specifically, the authors should provide a breakdown of the time and space complexity for each stage of the model, including the shape generation, atom type assignment, and bond type assignment. This analysis should consider the number of nodes, edges, and shapes involved in the process. Furthermore, it would be beneficial to discuss how the computational cost scales with the size and complexity of the molecules being generated. For instance, how does the runtime change when generating molecules with a larger number of rings or more complex branching patterns? Providing empirical runtime measurements on molecules of varying sizes would also strengthen the analysis. This detailed analysis is crucial for assessing the practical applicability of the model, especially when dealing with large datasets or complex molecules.

To further validate the generalizability of the MAGNet model, the authors should evaluate its performance on a more diverse set of datasets. While the current benchmarks are useful, they may not fully capture the range of molecular structures encountered in real-world applications. It would be beneficial to include datasets that contain molecules with different types of chemical structures, such as those with a high degree of branching, large rings, or unusual functional groups. Additionally, the authors should consider evaluating the model's performance on datasets that are specifically designed for downstream tasks, such as drug discovery or materials science. This would provide a more comprehensive assessment of the model's ability to generate molecules that are not only structurally diverse but also relevant for practical applications. The inclusion of such datasets would significantly enhance the paper's impact and demonstrate the model's broader applicability.

Finally, the paper should include a more detailed discussion on the limitations of the proposed approach. For example, what types of molecules are difficult for MAGNet to generate? Are there specific structural features or chemical properties that the model struggles with? Understanding these limitations is crucial for guiding future research and development in this area. Furthermore, the authors should discuss potential avenues for improving the model's performance, such as incorporating additional constraints or using more sophisticated shape representations. Addressing these limitations and suggesting future research directions would strengthen the paper and provide a more balanced perspective on the proposed approach.

### Questions

See weakness.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
