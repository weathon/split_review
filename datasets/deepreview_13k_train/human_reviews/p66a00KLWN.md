# NEXT-MOL: 3D Diffusion Meets 1D Language Modeling for 3D Molecule Generation

- Decision: Accept
- Scores: 3, 8, 3, 8

## Abstract
3D molecule generation is crucial for drug discovery and material design. While prior efforts focus on 3D diffusion models for their benefits in modeling continuous 3D conformers, they overlook the advantages of 1D SELFIES-based Language Models (LMs), which can generate 100% valid molecules and leverage the billion-scale 1D molecule datasets. To combine these advantages for 3D molecule generation, we propose a foundation model -- NEXT-Mol: 3D Diffusion Meets 1D Language Modeling for 3D Molecule Generation. NEXT-Mol uses an extensively pretrained molecule LM for 1D molecule generation, and subsequently predicts the generated molecule's 3D conformers with a 3D diffusion model. We enhance NEXT-Mol's performance by scaling up the LM's model size, refining the diffusion neural architecture, and applying 1D to 3D transfer learning. Notably, our 1D molecule LM significantly outperforms baselines in distributional similarity while ensuring validity, and our 3D diffusion model achieves leading performances in conformer prediction. Given these improvements in 1D and 3D modeling, NEXT-Mol achieves a 26\% relative improvement in 3D FCD for de novo 3D generation on GEOM-DRUGS, and a 13% average relative gain for conditional 3D generation on QM9-2014. Our codes and pretrained checkpoints are available at https://anonymous.4open.science/r/NEXT-Mol.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces the NEXT-Mol method, which first generates 1D molecular character representations using the Mol-LLAMA model and then generates the 3D structures of the molecules. The pre-trained molecular generation model’s atomic representations improve the performance of 3D structure generation.

### Strengths
1. This strategy has advantages in terms of the stability and effectiveness of molecule generation because it completely ignores the influence of 3D structures during the generation process.
2. The pre-trained molecular representations and the improved structural diffusion model achieve a new state-of-the-art (SOTA) in small molecule conformation generation, although the improvement is very slight.

### Weaknesses
1. The comparison results of 3D molecular generation in the paper are unfair because the authors completely ignore the influence of 3D structures on molecular representation during the generation process. The results of molecular generation should be compared with generation models based on 1D molecular representations. Specifically, the method's reliance on a 1D representation for initial molecule generation, while potentially simplifying the process, inherently limits its ability to capture complex 3D structural dependencies that are crucial for accurate molecular modeling. This approach neglects the rich information encoded in 3D conformations, which could lead to suboptimal results when compared to methods that directly incorporate 3D information during the generation phase.
2. The improvement in molecular conformation generation results mentioned in the paper is actually very small. In Table 3(A), DMT-B on GEOM-Drugs only improves by 1.4% compared to MCF-B, COV-R. Compared to Par. Guid, COV-P decreases by 3.7%, but the model parameters increase by 30 times. The significance of this method is limited. The reported 1.4% improvement in COV-R for DMT-B over MCF-B is marginal, especially considering the substantial increase in model complexity and computational cost. Furthermore, the decrease in COV-P compared to particle-guided methods, coupled with a 30-fold parameter increase, raises serious concerns about the practical utility and efficiency of the proposed approach. The trade-off between a slight increase in one metric and a significant decrease in another, alongside a massive increase in parameters, suggests that the method may not be a practical solution for real-world applications.

### Questions
I think the authors should provide new evidence of the advantages of this method as a 3D model for molecular generation.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper "NEXT-Mol: 3D Diffusion Meets 1D Language Modeling for 3D Molecule Generation" introduces a foundational model for 3D molecule generation that combines the 3D diffusion model with a 1D language model trained on SELFIES representations. By integrating the advantages of both approaches, NEXT-Mol aims to address challenges in chemical validity, scalability, and data scarcity. The model comprises three components: (1) MoLlama, a large language model for generating 1D molecules, (2) DMT, a diffusion model for 3D conformer prediction, and (3) a transfer learning technique that utilizes MoLlama’s 1D representations to improve DMT’s 3D predictions. The experiments show that NEXT-Mol performs well on several datasets and tasks, including 3D molecule generation and conditional molecule generation with specific quantum chemical properties.

### Strengths
Innovative Approach: The combination of a 1D language model with a 3D diffusion model is an original solution to ensuring chemical validity while efficiently generating 3D conformers. This cross-modal learning technique enhances the model’s adaptability.
Comprehensive Experiments: The authors provide extensive experimental results across different tasks and datasets, demonstrating NEXT-Mol’s versatility and effectiveness in molecular generation and conformer prediction.
Practical Application Potential: This approach is particularly relevant for pharmaceutical applications where 3D molecular structures are critical for drug discovery and chemical analysis. The model’s strong performance on chemical validity and stability metrics suggests its practicality.
Scalability and Adaptability: The design of NEXT-Mol allows for transfer learning, making it more resource-efficient and adaptable to different datasets or molecule sizes, which is useful in a field with diverse requirements.

### Weaknesses
Limited Theoretical Insight: The paper lacks a theoretical explanation of why combining 1D and 3D modeling via transfer learning improves performance. Further theoretical analysis could provide deeper insights into the effectiveness of this architecture and potential limitations.

Absence of Ablation Studies on Model Size and Hyperparameters: While the paper shows promising results with two model sizes, a more detailed examination of how model size or key hyperparameters (e.g., noise schedule, batch size) impact performance would provide more guidance on model tuning. Specifically, the effect of different noise schedules on the diffusion process and the impact of batch size on training convergence are not explored.

Limited Exploration of Alternative Architectures: The use of RMHA and the specific structure of DMT are well-motivated but not directly compared to alternative architectures. A comparative study could clarify if these design choices are optimal for all molecular generation tasks. For example, a comparison with other graph attention mechanisms or different diffusion model architectures could provide valuable insights.

Lack of Discussion on Model Limitations and Future Extensions: Although the model shows improvements, potential challenges such as memory overhead in larger molecules or limitations in certain chemical property predictions are not thoroughly discussed. The paper also lacks a discussion of the limitations of the current approach, such as potential biases in the training data or difficulties in generating molecules with specific complex structural features.

### Questions
Could you provide a theoretical justification for transfer learning between 1D molecular sequences and 3D conformers? An in-depth explanation could clarify why this cross-modal transfer is effective.
What are the potential computational trade-offs for using larger models (DMT-L) in terms of scalability and inference speed? Including a computational analysis of DMT-B versus DMT-L could highlight the scalability limits.
Are there specific molecular properties or types of molecules where NEXT-Mol struggles to perform as well? Identifying any limitations or edge cases where the model’s performance drops would clarify its practical scope.
Could you elaborate on why RMHA was chosen over other potential attention mechanisms? A comparison or justification of this design choice could strengthen the architectural motivation.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces NEXT-Mol, a model for 3D molecule generation that combines 1D Language Models with 3D diffusion models. NEXT-Mol first uses a pre-trained LM to generate 1D molecular sequences, ensuring chemical validity. It then predicts these molecules' 3D shapes with a refined diffusion model. Enhancements in model scaling, architecture, and transfer learning between 1D and 3D representations improve 3D predictions. NEXT-Mol is claimed to generate stable, accurate 3D conformers.

### Strengths
100% Validity: Ensures generated molecules are chemically valid by using a 1D SELFIES-based LM.
●  	Improved 3D Accuracy: Enhanced 3D conformer prediction through a refined diffusion model.
●  	Transfer Learning: Leverages 1D representations to boost 3D conformer prediction accuracy.
●  	Scalability: Scales well with large molecular datasets for robust molecule generation.
●  	Versatility: Performs well across tasks like de novo 3D generation, conformer prediction, and conditional molecule generation.

### Weaknesses
●  	Focus on Core Objective: In the title the paper is presented as a generative model for molecules. The model is benchmarked as a conformer generating model. Currently, benchmarks appear misaligned from the title; consider established benchmarks like CheckPose or DrugPose for 3D generation.
●  	1D-to-3D Transformation Claim: The claim that converting a 1D sequence to 3D adds value is questionable, as the graph already provides all necessary information.
●  	Not accurate statement on Rotation Augmentation: The statement, “Following AlphaFold3 (Abramson et al., 2024), we apply random rotation augmentation on 3D conformers to help DMT obtain equivariance to rotated inputs by learning. While (Wang et al., 2024) report decreased performance given random rotations, DMT benefits from it, potentially due to the improved neural architecture,” is unclear. The authors imply that rotation can be achieved without using equivariant networks (those maintaining symmetry under rotation). However, AlphaFold claimed that it is not necessary to have equivariant networks, so it is essential to clarify how DMT benefits from rotation augmentation and to distinguish it from learned equivariance.
●  	Limited ML Novelty: The model presents minimal innovation from an ML perspective, as it mainly combines existing components—LLaMA and diffusion models. This combination, particularly in transferring 1D information to 3D, offers limited novelty and benefit for the conformer generation part.

### Questions
●  	What is the rationale for combining 1D and 3D generation sequentially, and what benefits does this approach offer?
●  	Could you clarify how transferring a 1D representation contributes to the overall model performance?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces Next Mol, an innovative model for 3D molecule generation that combines the strengths of 1D molecule generation using SELFIES representations with subsequent conformer prediction. This approach is particularly timely given the scarcity of 3D annotated molecules in existing databases. While billions of molecules are cataloged in databases like ZINC or Enamine, researchers often rely on datasets such as GEOM DRUGS, which contain only about 400,000 unique molecules with approximately 40 million 3D structures.

Key Contributions:
- Novel Methodology: The integration of 1D molecule generation through SELFIES with conformer prediction addresses the limitations of current datasets and methods in 3D molecule generation.
- Performance Improvements: Next Mol demonstrates significant enhancements on benchmarks for both conformer generation and unconditional 3D molecule generation, outperforming existing models.
- Transfer Learning: The study shows that transfer learning between the stages of 1D molecule generation and conformer prediction positively impacts the results, suggesting a valuable strategy for future research.
- Advancing Beyond Equivariance Restrictions: The proposed DMT (Diffusion Molecular Transformer) model pushes the boundaries of 3D molecule generation by moving beyond the equivariant restrictions that have been prevalent in recent years, potentially opening new avenues in molecular modeling.

### Strengths
- State-of-the-Art Conformer Generation: The model achieves state-of-the-art performance in conformer generation, demonstrated through extensive comparisons with popular models like GeoDiff, Torsional Diffusion, and MCF, as well as widely used tools such as RDKit and OpenEye-Omega.
- High Topological Metrics: Utilizing 1D generative models significantly improves topological metrics—such as molecular stability, validity, and uniqueness—elevating them to nearly 100%.
- Scalable Transformer Architecture: The Diffusion Molecular Transformer is a scalable model that employs a simple transformer architecture with proven efficiency, making it an excellent base model for numerous other related tasks.

### Weaknesses
Weaknesses:

**Lack of Comparison with Other Molecular Language Models:** Although the paper introduces a 1D molecule generation component (MoLama), a 3D conformer generation model (DMT), and a transfer learning technique, it primarily showcases the performance of the conformer generation part and the advantages of transfer learning. However, it lacks a comparison with other molecular language models concerning the quality of the generated SELFIES representations. Specifically, the paper does not benchmark MoLama against other state-of-the-art molecular language models on tasks beyond 3D molecule generation, such as molecular property prediction or molecule classification, which would highlight its standalone value.

**Overemphasis on 100% Validity:** The paper focuses on achieving 100% validity, but in real-world applications, validity filtering is an extremely simple process due to how validity is defined. Consequently, there is no significant practical difference between achieving 90% validity and 100% validity. The paper should instead focus on demonstrating improvements in more meaningful metrics, such as the quality of the generated 3D structures or their chemical relevance.

**Mischaracterization of Computational Complexity:** The paper states that structures were obtained using computationally intensive geometry optimization with DFT. However, the GEOM dataset was designed using the CREST software for conformer sampling, followed by geometry optimization with GFN2-xTB—a semi-empirical tight-binding method, not DFT. Moreover, compared to some deep learning models, this approach is not computationally intensive; on a reasonable workstation, geometry optimization takes about 0.5 seconds per average GEOM-Drugs structure. The paper should correct this mischaracterization and provide a more accurate description of the computational resources used to generate the dataset.

**Missing Performance Metrics for Conformer Generation:** In conformer generation, computational performance is extremely important. OpenEye Omega remains one of the most popular software tools for this task because of its speed. The paper lacks performance metrics related to speed and efficiency, which are necessary for a fair comparison with existing tools. The paper should include a detailed analysis of the computational cost of their method, including the time required for conformer generation and any additional steps, and compare it with the performance of existing tools like OpenEye Omega.

**Use of Questionable Metrics:** The metric reported by JODO shows a 2.8% 3D molecule stability for the GEOM-Drugs dataset, rendering it practically meaningless. I strongly encourage avoiding the propagation of this metric in new papers. According to the code, the metric is based on a predefined bond length table, and a bond length is considered "good" if it is within 0.05 Å of the table value. However, the optimal distances between atoms are primarily defined by the energy landscape underlying the data—for GEOM-Drugs, it's GFN2-xTB—and depending on atom configurations, deviations in bond lengths can exceed 10%. While I'm uncertain about the validity of the 3D FCP metric, it's not entirely clear that it's completely off when compared with 3D molecule stability. Instead of attempting to report every possible metric to compare with other methods, focus on identifying the most important ones and emphasize the significance of the margins your model is achieving. The paper should provide a more thorough justification for the use of each metric and focus on the most relevant ones for evaluating the quality of generated molecules.

**Inconsistencies in Metric Definitions and Reporting:** Providing detailed descriptions of the metrics used in the supplementary material is crucial due to inconsistencies across different papers. For example, MiDi reported the Wasserstein distance for bond angles and bond length distributions for all bonds and angles, whereas this paper (and at least JODO) uses MMD for the most frequent bonds, angles, and torsions. Additionally, the way MiDi computes atom stability and molecule stability differs from the JODO code. Performing kekulization at the beginning can alter the valencies of atoms, leading to different results (e.g., if you manually define H:O:H, where ":" is an aromatic bond, kekulization converts it to the valid water molecule H-O-H). Some models measure atom and molecule stability for raw data, while others use RDKit preprocessing before measuring stability, which can inflate results. It is essential to be consistent in comparisons. While this may not significantly change your results, it could artificially boost JODO's stability results, skewing the comparison. Overall, ensure that the same versions of the metrics are used across all comparisons and that they are well-defined in the supplementary material. The paper needs to clarify the specific implementation details of each metric, including any preprocessing steps, and ensure consistency across all comparisons.

**Omission of EQGAT-Diffusion in Comparisons:** EQGAT-Diffusion is a recent model—published well before the ICLR deadline—that should be included in the comparisons for 3D unconditional molecule generation to provide a more comprehensive evaluation.

### Questions
Questions to the Authors:

**Comparison of MoLama with Other Models:** Could you provide a comparison between your 1D molecule generation model (MoLama) and other models like Equiformer on tasks beyond 3D molecule generation, such as molecule classification (or any suitable task where you can compare MoLama and let's say Equiformer)? Including such a comparison would highlight the standalone value of MoLama.

**Practical Advantages of 100% Validity:** Given that validity filtering is straightforward in practice, what are the practical advantages of achieving 100% validity over, for example, 90% validity in real-world applications?

**Inclusion of Performance Metrics:** Considering that computational performance is crucial in conformer generation tasks, could you include speed and efficiency metrics for your model, particularly in comparison with tools like OpenEye Omega? I would also add OpenEye Omega conformer generation + consequent xTB geometry optimization time. 

**Analysis of Metrics Used:** Could you analyze the metrics used in your study, especially focusing on 3D molecular stability and the FCP metric? Since the FCP metric relies on a neural network, is it capable of handling your data distribution, and is it up-to-date with recent developments?

**Consistency and Clarity of Metrics:** To ensure consistency, could you provide detailed descriptions of the metrics used in your study and confirm that the same versions are applied across all comparisons? Additionally, please clarify any preprocessing steps that might affect the results.

**Inclusion of EQGAT-Diffusion in Comparisons:** EQGAT-Diffusion is a recent model relevant to 3D unconditional molecule generation. Could you include it in your comparisons to provide a more comprehensive evaluation?

### Soundness
3

### Presentation
3

### Contribution
3
