# PharmaVQA: A Retrieval-Augmented Visual Question Answering Framework for Molecular Representation via Pharmacophore Guided Prompts

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 6, 5

## Abstract
In drug discovery, molecular representation learning is vital for understanding and generating new drug-like molecules. The accurate representation of molecules facilitates drug candidate screening and the optimization of lead compounds. The vastness of chemical space challenges traditional drug design and relies on complex computations. The Pharmacophore is a functional group contained within a drug molecule, which binds to receptors or biological macromolecules to produce biological effects and reduce computations. Pharmacophore-guided representation of molecules, however, remains a significant challenge. To address this issue, we propose an improved deep learning-based model called PharmaVQA for retrieving pharmacophore-related information directly from molecule databases, allowing for a more targeted understanding of drug-like molecules. Through the use of Visual Question Answering (VQA) framework, PharmaVQA captures pharmacophore data, generates knowledge prompts, and enriches molecular representations. On 46 benchmark datasets, PharmaVQA has demonstrated superior performance in both molecular property prediction and drug-target interaction prediction. Additionally, the applicability of PharmaVQA in drug discovery has been validated on an FDA-approved molecule dataset, where the Top-20 predictions were analyzed in real-world studies, with the majority of them experimentally validated as potential ligands previously reported in the literature. Our assessment of PharmaVQA is that it is a powerful and useful tool for accelerating the development of AI-assisted drug discovery across a wide range of areas.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces PharmaVQA, an innovative deep learning model designed to enhance molecular representation learning in drug discovery by leveraging pharmacophore information. By integrating a Visual Question Answering (VQA) framework, PharmaVQA effectively retrieves and processes pharmacophore-related data from molecule databases, generating enriched molecular representations that facilitate more accurate drug candidate screening and lead compound optimization. Demonstrated through extensive testing on 46 benchmark datasets and validated on an FDA-approved molecule dataset, PharmaVQA shows superior performance in predicting molecular properties and drug-target interactions, with many of its top predictions confirmed as potential ligands in real-world studies. This model represents a significant advancement in AI-assisted drug discovery, offering a powerful tool to accelerate the development of new drugs across various therapeutic areas.

### Strengths
The paper is easy to follow and well-organized, and the idea is quite straightforward. The paper presents PharmaVQA, a novel deep learning model aimed at improving molecular representation learning in drug discovery by utilizing pharmacophore information. By incorporating a Visual Question Answering (VQA) framework, PharmaVQA efficiently extracts and analyzes pharmacophore data from molecular databases, enhancing the representation of drug-like molecules. 

The experimental studies are intensive and thorough. Extensive testing on 46 benchmark datasets and validation using an FDA-approved molecule dataset show that PharmaVQA excels in predicting molecular properties and drug-target interactions. Many of its top predictions have been experimentally verified as potential ligands in real-world studies. This model marks a significant step forward in AI-assisted drug discovery, providing a robust tool to speed up the development of new drugs across multiple therapeutic areas.

### Weaknesses
The paper does not evaluate the performance on out-of-distribution data. The retrieval-based method requires the test and training data follows the same distribution. However, in drug discovery scenario, the drug molecular distribution varies greatly.

The performance improvement looks marginal.

The test setup for drug-target binding is not fair. We should evaluate the test set where both drug and protein are unseen in training set.

### Questions
Please see the weakness part.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents PharmaVQA, a framework designed for molecular representation learning, specifically incorporating pharmacophore information to enhance molecular embeddings. The proposed model fuses SciBERT embeddings derived from pharmacophore-related questions with molecular graph embeddings, aiming to improve downstream performance on tasks such as property prediction and binding affinity prediction. PharmaVQA is evaluated on standard molecular property prediction datasets (from MoleculeNet) and drug-target interaction (DTI) prediction datasets.

### Strengths
The paper is well-organized and technically clear, making it easy to follow the proposed methodology and experimental setup.

### Weaknesses
 - The authors call the framework "retrieval-augmented" yet provide limited details on the retrieval mechanism involved. Specifically, the retrieval process here seems limited to constructing pharmacophore-based prompts rather than an actual retrieval mechanism traditionally seen in RAG frameworks.
- Despite labeling the framework as a "Question-Answering" model, the primary focus of the paper appears to be molecular property prediction rather than true question answering. The tasks covered are standard property and binding affinity predictions, which do not necessarily involve question-answering paradigms as presented. (in contrast to MolInstructions or 3DMolLM)
- Given the architecture's resemblance to BLIP-based models, a direct comparison with 3DMolLM could help delineate PharmaVQA's contributions more clearly. If the main contribution is representation learning, there should comparisons with SOTA models such as GIMLET. Models such as MoleculeSTM are primarily used in the context of Molecule structure-text alignment, and not the most suitable head on head comparison method.
- It is unclear why the question-based framework is beneficial for the limited set of pharmacophore-based features provided. Since these features are often easily extractable with tools like RDKit, adding question-based prompts might introduce unnecessary complexity.
- The architecture largely reuses existing components, such as the Bilinear Attention Network and SciBERT embeddings, with minimal novel methodological contributions specific to molecular representation.
- Tables 3 and 4 lack error bars, which are essential given the close values in performance metrics across models. Error bars or confidence intervals would substantiate the claims of improved performance. In Tables 12 and 13, the ablation studies show high standard deviations, with overlapping values between the base and ablated models. This overlap weakens the evidence that the queries add meaningful improvement.

### Questions
- What specific retrieval process is involved in PharmaVQA that qualifies it as a Retrieval-Augmented model? Traditional retrieval augmented or RAG frameworks involve retrieval steps that seem missing here.
- Why is this called a "Question-Answering" framework if it primarily performs property prediction tasks? How does this differ from existing molecular representation models focused on property and affinity predictions?
- Could the pharmacophore features simply be appended to the input without the need for question-based prompts? This would streamline the model without losing relevant information, given the simplicity of the question set and the ready availability of pharmacophore features from RDKit.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a novel model, PharmaVQA, based on the Visual Question Answering (VQA) framework, which is designed to retrieve pharmacophore-related information directly from molecular datasets. It conducts experiments on multiple benchmark datasets, including tasks such as molecular property prediction and drug-target affinity and interaction prediction, which demonstrates superior results.  Furthermore, it also presents experiment that demonstrate biological meaningful significance.

### Strengths
1. This method applies VQA technology to the field of drug discovery, extracting pharmacophore knowledge through a question-and-answer approach, and providing a new perspective and approach for molecular representation.
2. In the context of the 11 downstream tasks related to predicting molecular properties as outlined by Li, pharmaVQA demonstrates superior performance across 9 datasets. The 30 downstream tasks from MoleculeACE, pharmaVQA achieves the highest performance on 24 datasets when evaluated with RMSE and on 23 datasets in terms of  R2. Additionally, pharmaVQA surpasses other methods when applied to datasets concerning drug-target affinity and interactions.
3. The method integrates deep learning techniques,  the bilinear attention network to achieve precise question-answer tasks for multiple pharmacophores. With the pharmacophore fusion  module, enhancing the richness of molecular representations.
4. The PharmaVQA model is capable of being used for downstream tasks such as molecular property prediction and drug-target affinity and interaction prediction. It can also be used for discovering potential ligands. This multifunctionality enables PharmaVQA with broad application prospects in the field of drug discovery.

### Weaknesses
Some technical details should be explained, please refer to Question part.

### Questions
1. PharmaVQA appears to introduce several novel aspects compared to existing state-of-the-art molecular representation learning models. Could you explain how the pharmacophore-guided prompts are obtained? Is it possible for users to design custom prompts themselves? Could you provide some examples of pharmacologically guided prompts and explain the rationale behind their design? Could you provide some limitations or challenges in designing effective prompts?
2. Could you clarify the relationship between the visual question-answering (VQA) component and the retrieval mechanism in PharmaVQA?
3. The selection of HPK1, FGFR1, and VIM-1 as validation datasets appears to be well-considered. How do they reflect real-world challenges in drug discovery, and what does PharmaVQA's performance on these datasets suggest about its broader applicability?
4. Figure 3 effectively shows how PharmaVQA identifies donor atoms in response to the question. The combination of highlighted molecular structures and relevant query terms provides a clear view of the model's interpretability. How are the top-5 query characters selected? Are they ranked solely by attention weights, or are other factors considered?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a framework to extract pharmacophore information from molecules with text question answering. The learned embeddings are then connected with embeddings from another molecular encoder for downstream tasks. This framework achieves good results on several downstream tasks.

### Strengths
1. The integration of text-based question-answering to enhance molecular representations is an interesting and original idea. By directly querying pharmacophore-related information, the model captures key molecular features that may be overlooked by conventional molecule-text alignment models like MoleculeSTM.

2. PharmaVQA achieves SOTA results on multiple downstream tasks.

### Weaknesses
1. Paper writing can be improved.  The paper’s focus on detailed architectural descriptions detracts from its main contributions. Readers might find greater value in a thorough explanation of how the pharmacophore-related questions were designed and in ablation studies that demonstrate the effectiveness of the QA component. Important insights into the QA framework’s impact on downstream tasks are relegated to the appendix, whereas they should be central to the main text. 

2. The provided visualizations show that important textual information related to donor pharmacophores ranks highly among tokens, which is expected in molecule-text multimodal models. However, the paper lacks a deeper analysis of how this textual information and pharmacophore knowledge extraction enhance downstream task performance. For example, it would be insightful to explore whether the prompt embeddings generated by specific pharmacophore related questions contribute more to some specific property prediction tasks.

### Questions
1. The term “Retrieval-Augmented” in the title seems to refer to the extraction of knowledge from the molecule itself, rather than retrieving external data. Could the authors clarify this usage? If external data retrieval is not involved, the term might be somewhat misleading.

2. For each downstream task, what specific model is used as the downstream encoder ? It would strengthen the paper to include performance comparisons between models using only this encoder without the QA prompt embeddings and those that include them. Such ablation studies are crucial to demonstrate the distinct contribution of the QA component to the overall performance.

3. The current approach trains the feature extraction module and the downstream tasks simultaneously. Is it feasible to train these components separately? Exploring this possibility could provide insights into the modularity of the framework and its applicability to different tasks without retraining the entire model.

### Soundness
3

### Presentation
2

### Contribution
3
