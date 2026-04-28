# Leveraging Discrete Structural Information for Molecule-Text Modeling

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
The integration of molecular and natural language representations has emerged as a focal point in molecular science, with recent advancements in Language Models (LMs) demonstrating significant potential for comprehensive modeling of both domains. However, existing approaches face notable limitations, particularly in their neglect of three-dimensional (3D) information, which is crucial for understanding molecular structures and functions. While some efforts have been made to incorporate 3D molecular information into LMs using external structure encoding modules, significant difficulties remain, such as insufficient interaction across modalities in pre-training and challenges in modality alignment. To address the limitations, we propose \textbf{3D-MolT5}, a unified framework designed to model molecule in both sequence and 3D structure spaces. The key innovation of our approach lies in mapping fine-grained 3D substructure representations into a specialized 3D token vocabulary. This methodology facilitates the seamless integration of sequence and structure representations in a tokenized format, enabling 3D-MolT5 to encode molecular sequences, molecular structures, and text sequences within a unified architecture. Leveraging this tokenized input strategy, we build a foundation model that unifies the sequence and structure data formats. We then conduct joint pre-training with multi-task objectives to enhance the model's comprehension of these diverse modalities within a shared representation space. Thus, our approach significantly improves cross-modal interaction and alignment, addressing key challenges in previous work. Further instruction tuning demonstrated that our 3D-MolT5 has strong generalization ability and surpasses existing methods with superior performance in multiple downstream tasks, such as nearly 70\% improvement on molecular property prediction task compared to state-of-the-art methods. Our code is available at \url{https://anonymous.4open.science/r/3D-MolT5-ICLR2025}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces 3D-MolT5, a novel framework for integrating molecular sequence and 3D structural information within a unified language model. While recent language models have advanced molecular science applications, most neglect critical 3D structural data essential for accurately understanding molecular properties. To address this, 3D-MolT5 uses a unique 3D token vocabulary that captures detailed 3D substructure information, enabling it to encode molecular sequences, spatial structures, and natural language together in a cohesive architecture. Through multi-task pre-training, 3D-MolT5 develops robust cross-modal comprehension. Experimental results show strong generalization, with the model achieving nearly a 70% improvement in molecular property prediction compared to current methods.

### Strengths
This work shows strength in its comprehensive comparison with various existing models, showcasing 3D-MolT5’s effectiveness across different approaches and highlighting its strong performance in molecular structure understanding. By integrating both molecular sequence and 3D structural information, the study addresses a crucial aspect of molecular modeling that is often underexplored, underscoring its relevance in capturing complex molecular properties.

### Weaknesses
While the work presents a solid approach, the concept of multimodal integration itself is not entirely new. Including a comparison with fine-tuned large language models (LLMs) that incorporate multimodal data[1] would further strengthen the evaluation, providing a clearer benchmark comparing to a boarder types of multimodal molecular representation models and other LLM as well e.g. Galactica[2]. The novelty of the approach is somewhat limited by the fact that it builds upon existing multimodal techniques, and the performance gains, while present, are not dramatically higher than existing methods. The core idea of integrating 3D structural information is valuable, but the specific implementation details and the extent to which this integration truly surpasses existing methods needs further clarification. The evaluation could also benefit from a more in-depth analysis of the model's performance on complex molecules and edge cases, rather than focusing solely on average performance metrics.

### Questions
Given that multimodal approaches are increasingly common, how does 3D-MolT5 specifically leverage 3D structural data differently or more effectively than existing fine-tuned LLMs that incorporate multimodal information?
In the model’s tokenized format for 3D structures, what considerations were made for maintaining structural fidelity across different molecule sizes and complexities? How does the approach handle conformational flexibility within molecular ensembles?
Could the model’s performance be further validated on additional downstream tasks, such as reaction prediction or drug-target interaction, to assess its versatility across a broader range of applications in molecular science?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors introduce a novel approach that integrates spatial molecular data by calculating a set of E3FP-based discrete tokens for each atom, then combining these tokens with corresponding SELFIES embeddings. Additionally, they propose a new pretraining scheme designed to improve the alignment and interaction between structural (1D) and spatial (3D) tokens. Finally, the authors present a thorough evaluation of the 3DMol-T5 model, which incorporates these novel methods into an encoder-decoder architecture, across various molecular tasks.

### Strengths
The paper is well-written and easy to follow, with supplementary materials providing all necessary details to reproduce the method. The concept of integrating spatial molecular fingerprints alongside molecular sequence representations is a novel contribution in the field of language models. Experimental results demonstrate a notable improvement in model performance compared to baseline models.

### Weaknesses
Despite the comprehensive benchmarking of the model across various molecular tasks, the limited ablation studies make it difficult to assess the individual contributions of each component of the proposed approach to overall model performance. Specifically, the necessity of the five pretraining subtasks is not sufficiently justified, and it remains unclear whether all are essential or if a subset would suffice. Additionally, a minor drawback is the absence of non-language model baselines in the Molecular Property Prediction tasks section. Further details on these points are provided in the Questions section.

### Questions
As noted in the Weaknesses section, although the proposed method achieves significant performance improvements over baseline models, it appears overly complex and includes numerous subcomponents. The necessity of each part is not sufficiently justified.
* The authors introduce a novel pretraining scheme comprising five subtasks. Are all these subtasks equally essential for optimal model performance, or could the model show similar performance using only one or two? Intuitively, the “3D molecule to text translation” task might be sufficient, as it encompasses all three modalities—text, 1D molecular structure, and 3D molecular structure. It would be valuable to explore this question further by showing the performance of 3DMol-T5 after pretraining on each individual task while excluding the remaining four.
* Several recent works [a, b] have demonstrated that language models can process spatial molecular data directly as text containing atom coordinates. Compared to the proposed E3FP-based discrete tokens, this direct coordinate representation is considerably simpler, more transparent, and requires no model modifications. Furthermore, it can serve as both input and output (for example, in spatial molecular generation tasks). Providing a comparison with this approach is important to justify the use of the E3FP-based discrete token scheme.
* The proposed alignment scheme for combining 1D and 3D molecular information involves summing their embeddings as $E=\frac{1}{2}E_{1D} + \frac{1}{2}E_{3D}$ which necessitates modifications to the language model's source code—requiring time and substantial programming knowledge to adapt it for other models. However, is this modification truly necessary? Could the E3FP tokens be interpreted as textual tokens and used directly within the text without altering the model? Intuitively, a sequence such as “$s_0, d_{01}, d_{02}, d_{03}, s_1, d_{11}, d_{12}, d_{13} \cdots$” might accomplish this. It would be useful to elaborate on this question.

Minor suggestions:
* While the QM9 dataset is suitable for demonstrating the model's capability in using 3D molecular information to predict quantum properties, I recommend that the authors consider the QMUGS dataset [c] due to the greater diversity in molecular structures and quantum properties. Notably, QMUGS includes atom-wise properties, which could provide a more comprehensive evaluation. Testing model performance on this dataset could enhance the significance of the experimental section.

a. Language models can generate molecules, materials, and protein binding sites directly in three dimensions as XYZ, CIF, and PDB files, 2023

b. BindGPT: A Scalable Framework for 3D Molecular Design via Language Modeling and Reinforcement Learning, 2024

c. QMugs, quantum mechanical properties of drug-like molecules, 2022

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a unique framework, 3D-MolT5, that integrates 3D structural data and molecular sequences into a unified language model. 3D-MolT5 embeds molecular geometry directly into the language model using discrete 3D tokens generated from the E3FP algorithm. The model is pre-trained with multi-task objectives, including both denoising and translation tasks. The model achieves state-of-the-art results in tasks like molecular property prediction, molecule captioning, and text-based molecule generation.

### Strengths
- The introduction of 3D tokens for representing molecular substructures at atomic level removes the dependency on structure encoders.
- The combination of 1D and 3D embeddings enables alignment of molecular sequence and structural data at atomic level.
- The novel pre-training denoising and translation tasks enhance cross-modal training and alignment.
- The model demonstrates performance gains over existing baselines across different benchmarks, including 3D-dependent tasks.

### Weaknesses
 - The term “tokenization” may not be accurate here, as 3D-MolT5 does not achieve unified molecule-text modeling in token space as UniMoT [1] does. UniMoT can generate molecule tokens as text, but 3D-MolT5 lacks the ability to generate 3D tokens. The token generation ability is the major difference between discrete and continuous structures, with 3D-MolT5 limited to encoding rather than generating 3D data.

  - The 3D “tokenization” in this paper functions more like a 3D molecular encoder, encoding each atom into a 3D embedding rather than generating 3D structures.
  - 3D-MolT5 lacks 3D generation abilities because it cannot map 3D embeddings back to specific atoms or structures.
  - The motivation section resembles that of UniMoT. A more detailed comparison between the two would be helpful.

- The E3FP algorithm introduces additional space and time complexity than using a well-pretrained encoder.

- The reasoning for further encoding $d_i$ with $E_{3D}(d_i)$ instead of using $d_i$ directly is unclear.

- It’s not explained why the authors chose the E3FP algorithm over a 3D molecular encoder like Uni-Mol. And the paper does not provide an ablation comparison to illustrate any advantages of E3FP.

- In Algorithm 1, it appears that $\cup$ is used to indicate concatenation; this should be stated for clarity.

### Questions
- Why do the authors focus solely on T5 instead of exploring other LLM architectures? Could the 3D "tokenization" approach work effectively with models like Llama or Mistral?

- What advantages does the E3FP algorithm have over a 3D molecular encoder?

- How many embeddings are used for encoding SELFIES tokens and 3D tokens?

- Since the SELFIES sequence length differs from the number of atoms, how do you manage the additional SELFIES tokens?

- What are the time and memory costs for running the E3FP algorithm?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose 3D-MolT5, a unified framework designed to model molecule in both sequence and 3D structure spaces. The key innovation of our approach lies in mapping fine-grained 3D substructure representations into a specialized 3D token vocabulary. This methodology facilitates the integration of sequence and structure representations in a tokenized format, enabling 3D-MolT5 to encode molecular sequences, molecular structures, and text sequences within a unified architecture. Leveraging this tokenized input strategy, we build a foundation model that unifies the sequence and structure data formats. We then conduct joint pre-training with multi-task objectives to enhance the model’s comprehension of these diverse modalities within a shared representation space. Authors also provide source code for reproducibility.

### Strengths
The authors describe developments for LLMs to capture textual information in molecules, as well as graph representation models to capture 3D structure topology of molecules. Limitations of the existing work is also well described. 

There are a variety of tasks evaluated both on text generation as well as structure learning, which is informative and comprehensive.

### Weaknesses
The paper seems to be missing the important citation from the IJCAI survey paper on Graph-based molecular representation learning:

[IJCAI 2023] Zhichun Guo, Kehan Guo, Bozhao Nan, Yijun Tian, Roshni G. Iyer, Yihong Ma, Olaf Wiest, Xiangliang Zhang, Wei Wang, Chuxu Zhang, and Nitesh V. Chawla. 2023. Graph-based molecular representation learning. In Proceedings of the Thirty-Second International Joint Conference on Artificial Intelligence (IJCAI '23). Article 744, 6638–6646. https://doi.org/10.24963/ijcai.2023/744

While experiment results achieve competitive results, there seem to be only 2 benchmark datasets being considered. There are more diverse and difficult datasets such as USPTO. Can the authors evaluate on more datasets to make the results more conclusive?

### Questions
See above section for details.

### Soundness
3

### Presentation
2

### Contribution
3
