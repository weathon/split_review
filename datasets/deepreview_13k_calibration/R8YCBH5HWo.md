# Two-Stage Pretraining for Molecular Property Prediction in the Wild

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3

## Abstract
Accurate property prediction is crucial for accelerating the discovery of new molecules.
Although deep learning models have achieved remarkable success, their performance often relies on large amounts of labeled data that are expensive and time-consuming to obtain.
Thus, there is a growing need for models that can perform well with limited experimentally-validated data.
In this work, we introduce MoleVers, a versatile pretrained model designed for various types of molecular property prediction \textit{in the wild}, i.e., where experimentally-validated molecular property labels are scarce.
MoleVers adopts a two-stage pretraining strategy.
In the first stage, the model learns molecular representations from large unlabeled datasets via masked atom prediction and \textit{dynamic denoising}, a novel task enabled by a new branching encoder architecture.
In the second stage, MoleVers is further pretrained using auxiliary labels obtained with inexpensive computational methods, enabling supervised learning without the need for costly experimental data.
This two-stage framework allows MoleVers to learn representations that generalize effectively across various downstream datasets.
We evaluate MoleVers on a new benchmark comprising 22 molecular datasets with diverse types of properties, the majority of which contain 50 or fewer training labels reflecting real-world conditions.
MoleVers achieves state-of-the-art results on 20 out of the 22 datasets, and ranks second among the remaining two, highlighting its ability to bridge the gap between data-hungry models and real-world conditions where practically-useful labels are scarce.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper designs a two-stage pre-training framework for molecular property prediction in the wild. The authors claim that previous methods are not good at generalizing to the testing cases with few labeled samples provided. The first stage of the proposed method additionally equips denoising objectives as branching encoder learning compared to the previous method. The second stage is training the model via weakly supervised learning with coarse labels (also through computation tools). Experimental results on a new benchmark dataset demonstrate the proposed method's effectiveness.

### Strengths
(1) The presentation of this paper is quite clear. The major idea is quite straightforward. It can be expected that better denoising frameworks and weakly supervised learning can be effective for enhancing few-shot molecular property prediction performance. 

(2) Comprehensive experiments have been covered in this work. And new large-scale benchmark dataset has been introduced for evaluation in this work.

### Weaknesses
(1) The algorithmic contribution appears somewhat limited. Firstly, both the denoising pretraining strategy and masking strategy have been explored in previous works. Therefore, this study primarily concentrates on the interaction between these two modules during the pretraining stage, which lacks novelty. Specifically, the denoising process, while utilizing a branching encoder, still relies on established techniques like adding Gaussian noise to atomic coordinates. The masking strategy, similarly, employs standard atom masking. The core novelty, therefore, hinges on the specific combination and interaction of these existing techniques, which requires more substantial justification. In the second stage, the effectiveness of weakly supervised learning is not surprising, provided the computed coarse labels are essentially accurate. Overall, the efficacy of the proposed strategies has been largely validated by previous works, which somewhat diminishes the significance of this study.

(2) It appears that the research works related to few-shot molecular property prediction have been overlooked in the discussion of related works. Interestingly, the experiments conducted in this study primarily focused on the few-shot molecular property prediction task, yet this line of research has not been addressed in the related works section.

(3) Given that the benchmark dataset introduced in this work is novel, it is not entirely convincing that the proposed method consistently outperforms previous approaches. The number of baseline methods covered is relatively small compared to the total number of molecular pretraining methods. It seems that some molecular denoising pretraining frameworks, which are crucial for validating the effectiveness and novelty of the proposed method, have not been included in the comparison. For instance, methods that explore different noise distributions or adaptive noise scales during denoising could provide a more comprehensive comparison.

### Questions
(1) Could the authors elaborate more on the novelty of the first stage of pre-training? What are the key novel points that distinguish the proposed method from previous approaches?

(2) Could authors have more discussions over related works about the few-shot molecular property prediction? There is also a series of works working on this problem. Considering this work is actually tackling the same problem, it is appropriate to have a few more discussions and even experimental comparisons over the previous approaches.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces MoleVers, a two-stage pretrained model aimed at improving molecular property prediction in low-data scenarios. The model first undergoes self-supervised training through masked atom prediction (MAP) and dynamic denoising. In the second stage, MoleVers utilizes auxiliary labels generated by cost-effective computational methods to further refine molecular representations. The model is evaluated on a newly curated benchmark, which includes 22 datasets with 50 or fewer labeled samples each. Experimental results indicate that MoleVers achieves competitive performance on them, suggesting its robustness in both low-data settings.

### Strengths
- **Valuable Research Question**: The research question addressed in this paper focuses on an area in the field that has lacked sufficient attention and remains underexplored. The authors provide a feasible solution for effective property prediction in low-data scenarios.

- **Benchmark Contribution**: The MPPW benchmark is a valuable addition to the field, as it reflects real-world scenarios where labeled molecular data is often scarce.

- **Strong Empirical Results**: MoleVers achieves consistently high performance across various assays, demonstrating its generalizability and effectiveness in low-data regimes.

### Weaknesses
 **Weaknesses:**

- My primary concern with this paper is the lack of technical novelty. Although the authors propose a two-stage pretraining approach, each pretraining stage employs widely used methods, such as MAP and dynamic denoising. Thus, in terms of technical contribution, this work may lean more toward engineering improvements.

- Some experimental setups and procedures lack sufficient motivation and explanation:

   1. In Section 3.2, the authors mention selecting HOMO, LUMO, and Dipole Moment as auxiliary tasks. However, as quantum properties, these may be less beneficial for ADMET tasks, raising doubts about the validity of the assumption in line 226.
   
   2. In line 298, the authors use a subset of the stage 1 pretraining dataset for auxiliary task labeling and further pretraining in stage 2. This implementation detail lacks motivation—why was a subset of the stage 1 pretraining dataset chosen for stage 2?
   
   3. In Section 5.4, the authors point out that the benefit from stage 2 pretraining might depend on the nature of the downstream task, which heightens concerns over the choice of task properties in stage 2.

   4. In line 425 of Section 5.6, the authors explore the impact of pretraining dataset diversity by filtering molecules based on certain elements. However, do these filtered datasets differ in size? This could also contribute to performance differences, so it would be preferable if the authors controlled for dataset size in this analysis.

- The authors’ evaluation in high-data settings is insufficiently comprehensive. They selected only three datasets (QM7, QM8, QM9), which are closely related to the auxiliary tasks. I recommend a more diverse downstream task evaluation on MoleculeNet or TDC datasets.

### Questions
Please refer to the questions in Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In real-world scenarios where molecular property labels are scarce, there is a need to develop property prediction methods that can perform well with limited labeled data. To address this, the authors propose a two-stage pretraining approach, MoleVers. The first stage employs atom masking and dynamic denoising, where a branching encoder is used to mitigate interference between denoising pretraining with larger noise scales and the masking task. To evaluate MoleVers' fine-tuning performance on limited labeled data, the authors introduce the MPPW benchmark, comprising 22 biological and chemical property subsets, each containing between 38 and 123 molecules. MoleVers outperforms four baseline molecular pretraining methods and also shows superior performance on QM property prediction datasets with abundant data. The ablation studies demonstrate the effectiveness of both pretraining stages, as well as the impact of noise scale and pretraining data on performance.

### Strengths
1. The writing is clear and easy to understand.
2. Experimental settings are well-detailed, with fair comparisons based on a shared pretraining dataset, making the results convincing.
3. Addressing the challenge of limited labeled data for biological and chemical property prediction is crucial, and the two-stage approach provides an effective solution that could inspire further research in this area.

### Weaknesses
1. Given that each task in the proposed MPPW benchmark includes only 38–123 molecules, there is a risk that the results are not robust and variable. However, I did not see any mention of repeated experiments or the reporting of standard deviations. I suggest the authors perform multiple runs and report the mean and standard deviation to make the results in Table 1 more robust and convincing.

2. The authors propose a dynamic denoising pretraining strategy and a branching network design, but no ablations are provided to test the effectiveness of these design choices. Could the authors conduct experiments to compare dynamic and static denoising pretraining, as well as examine the impact of branching on the results? Specifically, how does the performance change when the noise scale is fixed during pretraining, and how does a single encoder perform compared to the branching encoder across different noise scales? These experiments would help clarify the benefits of the proposed dynamic denoising and branching architecture.

3. The model descriptions could be more thorough to aid reader comprehension. For example, what is the network structure of the Denoising and MAP heads? Are they simple feedforward networks, or do they have a more complex architecture? What is the "pooling with multihead attention" (PMA) module, and what does the pair representation entail? A detailed description of the encoder architecture would also be helpful, perhaps included in the main text or the appendix. Providing more details on the network architecture, such as the number of layers, hidden dimensions, and activation functions, would make the paper more reproducible.

### Questions
1. In Section 3.1, you mention that "the denoising tasks are equivalent to learning a molecular force field" and that this explanation is based on the assumption that the input data is at equilibrium. Do the RDKit-generated conformations used here meet this "equilibrium" assumption?
2. In Section 3.1.2, you mention that increasing the noise scale can cover more unseen molecules. This issue was also addressed in [1], where they argued that the noise scale of an isotropic Gaussian correlates with the accuracy of force fields, showing that excessively small or large noise scales negatively impact force field accuracy (extended data Fig. 3 [1]). In contrast, this paper suggests that larger noise scales are beneficial. How do you think of this discrepancy?
[1] Pre-training with fractional denoising to enhance molecular property prediction, Nature Machine Intelligence, 2024.
3. Additionally, in the dynamic denoising pretraining, which is compared to the denoising diffusion model, does the dynamic noise scale $$\sigma$$ serve as an input to the network as in diffusion models?
4. In Section 3.2, you selected HOMO, LUMO, and dipole moment prediction as the second-stage pretraining tasks. Why were these tasks chosen? Are they related to downstream properties in MPPW? Regarding your assumption that "representations useful for predicting one type of property could also help in predicting others," does this require that the second-stage properties are correlated with downstream properties? After all, property prediction tasks are different from general pre-training tasks and are already learning high-level features.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces MoleVers, a two-stage pre-training framework designed for molecular property prediction. The first stage of pre-training includes a masking atom prediction strategy alongside a dynamic denoising approach. The second stage involves supervised learning tasks, leveraging labels generated by DFT methods.

### Strengths
1. The paper is well-written and easy to follow.
2. The dynamic scaling of the denoising process is an innovative and interesting approach.

### Weaknesses
1. Overall, the proposed pre-training strategy lacks novelty. Both the masking and denoising strategies have been widely adopted in previous pre-training methods, such as Uni-Mol[1] and 3D-denoising. Additionally, the second stage of pre-training, which involves supervised task learning with DFT-generated properties, is also used by Transformer-M[2]. The motivation for splitting the pre-training into two distinct stages needs further clarification.

2. The DFT process is computationally expensive, especially for large molecules. Relying on DFT-generated labels for pre-training tasks in MRL may not be a feasible or efficient choice.

3. The rationale for decoupling the denoising and masking atom tasks is unclear, as these two distributions operate on different modalities—coordinates and atom types, respectively.

4. Results for each subtask on QM9 and MoleculeNet should be reported to demonstrate the model's superiority effectively.

### Questions
See weakness

### Soundness
2

### Presentation
2

### Contribution
1
