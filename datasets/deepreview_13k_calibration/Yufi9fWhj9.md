# Chain-of-thoughts for molecular understanding

- Decision: Reject
- Avg Score: 5.20
- Scores: 6, 6, 5, 3, 6

## Abstract
The adaptation of large language models (LLMs) to chemistry has shown promising performance in molecular understanding tasks, such as generating a text description from a molecule. However, proper reasoning based on molecular structural information remains a significant challenge, e.g., even advanced LLMs such as GPT-4o struggle to identify functional groups which are crucial for inferring the molecular property of interest. To address this limitation, we propose \Algname, a structure-aware chain-of-thought (CoT) that enhances LLMs’ understanding of molecular structures by explicitly injecting the key structural features of molecules. Moreover, we introduce two fine-tuning frameworks for adapting the existing LLMs to use our \Algname. Our experiments demonstrate that incorporating \Algname with our fine-tuning frameworks leads to consistent improvements in both molecular understanding tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes a framework to enhance molecule captioning and generation by integrating structure-related textual information. In the molecule-to-text task, structural information is extracted using RDKit and then provided along with the SMILES representation as input to fine-tune models for caption generation. For the text-to-molecule task, an additional model is trained to generate this structural information from captions, which is subsequently passed to a target model to generate molecules. This approach demonstrates improved performance in molecule captioning and generation with models such as MolT5 and ChemT5.

### Strengths
- The proposed method of adding structural information is well-motivated and systematically applied, with distinct steps for molecule-to-text and text-to-molecule tasks. The overall setup is clearly presented.
- The method demonstrates encouraging results, particularly in the text-to-molecule task, where structural prompts improve fidelity to the exact SMILES representation. This suggests that the structural prompts positively impact molecule generation accuracy.
- The paper is generally clearly written and well-organized.

### Weaknesses
1.  **Limited Dataset and Baselines**: The evaluation could benefit from using a larger and more diverse training set, such as PubChemSTM[1], which would add robustness to the results. Additionally, several recent models (such as the ones in MolInstructions[2]) are not benchmarked, limiting the scope of the evaluation. The lack of comparison with models trained on the MolInstructions dataset, which includes a large-scale biomolecular instruction dataset, is a significant oversight. This dataset could provide a more comprehensive evaluation of the model's ability to handle diverse molecular descriptions. Furthermore, the absence of comparisons with models specifically designed for molecule captioning and generation tasks on this dataset makes it difficult to assess the true advancement of the proposed method.
2.  **Comparisons with ChemCrow and BioT5**: The comparison with ChemCrow is not entirely appropriate, as ChemCrow was not specifically designed for molecule captioning. Additionally, the method underperforms compared to BioT5 in certain metrics. An augmented BioT5 would serve as a stronger baseline, potentially offering more relevant comparisons. The underperformance against BioT5, particularly in metrics where BioT5 excels, suggests that the proposed method may not be leveraging cross-modal information as effectively. A direct comparison with an augmented BioT5, incorporating similar structural information, would provide a more rigorous benchmark and clarify the specific advantages of the proposed approach.
3.  **Handling of Missing Structural Information in Text2Mol**: There is no mechanism for handling cases where structural details may be absent in the caption during text-to-molecule generation. This could lead to "hallucination" of inaccurate details, affecting the reliability of generated molecules. The method's reliance on explicit structural information raises concerns about its robustness when dealing with less descriptive captions. The lack of a mechanism to infer or handle missing structural details could lead to the generation of molecules that do not accurately reflect the intended structure, especially when captions focus on other aspects like activity or properties.
4.  **Limited Technical Contribution**: The technical novelty of the paper is modest, as the approach primarily focuses on input augmentation rather than introducing a new model architecture or algorithm. The core contribution is primarily an input augmentation technique, and the method does not introduce any novel architectural components or learning algorithms. This limits the technical impact of the work, as it does not advance the state-of-the-art in model design or learning methodologies.
5.  **Narrow Scope of Structural Information**: The structural information used is restricted to basic elements like functional groups and ring systems. Given the diversity of molecular captions, expanding beyond these elements could increase the effectiveness of the method. The limited scope of structural information, focusing on basic elements, may not capture the full complexity of molecular descriptions. Expanding the structural features to include more advanced concepts like stereochemistry, bond types, or 3D conformations could potentially enhance the method's ability to generate more accurate and detailed molecular representations.
- Minor: The term “Chain of Thought” (CoT) is misleading in this context, as it traditionally refers to intermediate reasoning generated by the model. Here, “StructCoT” is provided as input rather than produced by the LLM. This choice of terminology may mislead readers, as the structural information is not generated by the model itself.
- Minor:  Phrasing like "We propose to" in the contributions section could imply a suggestion rather than a concrete result. It might be more effective to use definitive statements, such as “We demonstrate…”.

### Questions
- While the method positively impacts captions with structural information, it is not clear whether it aids captions that focus on other descriptors (e.g., molecular activity or properties). Are there any results on how the structural prompt affects captions beyond structural descriptions?
- BioT5 is noted to outperform the proposed approach in some tasks. Would incorporating the same structural augmentation improve BioT5’s performance further, potentially establishing a new baseline?
- Although the method improves molecule captioning performance, the real-world applications of these gains are unclear. Are there specific downstream tasks that would benefit directly from enhanced captioning? This is a question regarding the general line of research, and not specifically pointed at this paper.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This study introduces STRUCTCOT, a structure-aware chain-of-thought (CoT) approach designed to enhance large language models (LLMs) for molecular structure understanding tasks. By embedding key structural features into LLMs, STRUCTCOT aims to improve the models' performance in chemistry-specific applications. The results show that incorporating STRUCTCOT consistently enhances molecular understanding tasks, highlighting its potential to address a notable gap in LLM-based molecular reasoning.

### Strengths
The study presents an innovative approach by focusing on structural feature embedding, a novel strategy for leveraging LLMs in chemistry. The method demonstrates notable improvements in molecular understanding tasks, suggesting that STRUCTCOT could effectively bridge limitations of traditional LLMs in molecular reasoning. The work’s originality and the clear effort involved in developing STRUCTCOT make it a valuable contribution to the field of ai for chemistry.

### Weaknesses
One potential limitation is the choice to use an LLM-based approach for molecular structure tasks, where specialized models like Chemprop[1] are typically more efficient and effective. Additionally, existing tools like RDKit can generate much of the necessary structural information directly, often without the interpretative challenges LLMs face with SMILES strings. These aspects raise questions about whether LLMs are the most suitable tool for these tasks, considering their current limitations. Furthermore, the study does not sufficiently address the inherent challenges of using SMILES strings as input for LLMs, such as the lack of explicit spatial information and the potential for multiple valid SMILES representations for the same molecule, which can lead to inconsistencies in model interpretation. The reliance on a limited set of structural features also raises concerns about the generalizability of the approach to more complex molecules with intricate stereochemistry or unique bonding patterns.

### Questions
What is the primary motivation for adapting LLMs to structure-based molecular tasks, given the availability of specialized models (e.g., Chemprop) and tools (e.g., RDKit) that handle structural information efficiently?
How were the specific structural features selected for inclusion in STRUCTCOT? For example, complex configurations like chirality and E/Z isomerism might be critical in some molecular contexts, but it’s unclear whether and how these were considered in the study’s framework.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper addresses the limitations of large language models (LLMs) like GPT-4 in accurately interpreting and reasoning about molecular structures. The authors introduce StructCoT, a structure-aware chain-of-thought framework designed to enhance LLMs' performance on molecular understanding tasks. StructCoT explicitly incorporates key molecular structural features into the reasoning process, aiming to improve tasks such as molecule captioning (Mol2Text) and text-based molecule generation (Text2Mol). The authors also propose fine-tuning frameworks to adapt existing LLMs to effectively utilize StructCoT, demonstrating consistent performance improvements over baseline models.

### Strengths
The paper tackles the novel challenge of integrating detailed molecular structural information into the reasoning process of LLMs. The paper is well-organized and clearly articulates the motivation behind StructCoT. The methodology is systematically presented, with clear definitions of the six key structural elements incorporated into StructCoT. The experimental setup is thorough, and the results show that incorporating StructCoT leads to performance improvements in the evaluated tasks.

### Weaknesses
- Limited Evaluation Scope: The paper evaluates StructCoT primarily on tasks involving the generation and interpretation of molecular descriptions (Mol2Text and Text2Mol). These tasks, while relevant, may not fully capture the complexity of molecular understanding. Evaluating the model on more challenging tasks, such as molecular property prediction, reaction prediction, or synthesis planning, would provide a more comprehensive assessment of its capabilities.

- Methodology too Simple: The methodology relies heavily on augmenting input data with explicit structural information extracted using existing tools like RDKit. While this approach is practical, it raises questions about the novelty of the contribution. The performance improvements might stem more from the inclusion of precise structural data rather than the proposed StructCoT framework itself.

- Underutilization of Advanced Tools: Given that RDKit and similar tools can compute complex molecular properties and descriptors, the paper's focus on basic structural features seems limiting. Incorporating more advanced concepts, such as molecular fingerprints, electronic properties, or 3D conformations, could enhance the model's understanding and enable it to tackle more sophisticated tasks.

### Questions
1. Have the authors considered testing StructCoT on more complex molecular understanding tasks, such as molecular property prediction or reaction outcome prediction? How does StructCoT perform in these contexts compared to existing methods?

2. Since RDKit can compute a wide range of molecular descriptors and properties, why did the authors limit the structural information to the six basic elements? Would incorporating more complex concepts, as suggested in AutoMolCo [1], lead to better performance or broader applicability?

[1] Zhang, Shichang, et al. "Automated Molecular Concept Generation and Labeling with Large Language Models." arXiv preprint arXiv:2406.09612 (2024).

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors propose StructCoT, a structure-aware chain-of-thought (CoT), to improve the LLMs' understanding of molecular structures by directly pointing out the crucial features in their structures. At the same time, two fine-tuing frameworks are also incorporated for StructCoT. Experimental results show that STructCoT can improve the performance in molecular understanding tasks such as molecule captioning.
Soundness:

### Strengths
1. Structural information, epecially the substurture information, is important for accurate molecule understanding.
2. StructCoT does contribute to the performance improvement according to the experimental results.

### Weaknesses
1. The novelty is not enough. Chain-of-thought (CoT) is widely used in prompting LLMs for complex tasks. I don't see enough technical contributions in the proposed method.
2. The presentation of this paper is poor. Firstly, the authors claim that StructCoT could improve the molecule understanding tasks, but in the experiments, they include the text-based molecule generation task, which does not belong to the molecule understanding task. Meanwhile, how could you obtain accurate molecule structural information if LLMs are not reliable as you claim previously in Figure 1? Secondly, after reading through this paper, I still could not figure out clearly what "two fine-tuning frameworks" mean, especailly in Figure 2. Does the authors mean two tasks? Thirdly, in the molecule captioning task, It seems that no CoT is applied, and the structral information is generated by external tools like Rdkit. Forthly, the xlabel of Figure 6 is missing.
3. The performance of GPT-4o in molecule captioning task is way too low. According to MolReGPT, the 10-shot performance of GPT-4 is comparable to MolT5-large. As GPT-4o is even more advanced, I remain doubtful on the experiment results. Did the authors follow the prompt template used in MolReGPT?
4. Although BioT5 is much better in their original performance, the authors still choose the ChemT5. I wonder what is the exact reason.
5. The baselines selected are not strong enough, please include more up-to-date methods for comparison.

### Questions
Please address the weaknesses mentioned above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Summary:

The paper proposed StructCoT - a structure-aware chain-of-thought method including six predefined structure information elements as part of the input to LLMs. The paper also proposed a matching ratio-based rejection sampling method to help sample structure valid molecules.

### Strengths
Strengths:

1. Introducing structure information in LLM-based molecule understanding is crucial.
2. The paper is well-written and easy to understand.

### Weaknesses
Weaknesses:

1. The matching ratio-based rejection sampling requires further clarification and expansion. For instance, it is unclear whether different structural elements are weighted differently when calculating the matching ratio. In the experiments, the authors exclude molecular formula, molecular weight, and IUPAC names due to their low reasoning accuracies. It is also necessary to explore how the parameter k influences the sampling performance; while k=5 is used in the ablation study, the impact of varying k remains unexamined. Furthermore, the influence of the sampling module on efficiency should be addressed. Discussing the efficiency and running time associated with this sampling method would be beneficial for understanding its practical implications.
2. Further ablation studies about how different structural information impacts performance are necessary to conduct. As a main contribution of the paper, six structural elements are incorporated within the methodology. However, the paper currently lacks a detailed analysis of how each individual element influences performance. It is beneficial to include these studies in the experimental section.

### Questions
Please refer to weaknesses

### Soundness
2

### Presentation
3

### Contribution
3
