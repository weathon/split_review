# MV-CLAM: Multi-View Molecular Interpretation with Cross-Modal Projection via Language Model

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 5, 3

## Abstract
Large language models (LLMs) have shown significant potential in the biomolecular domain, particularly by demonstrating that effective adaptation of molecular representations for LLMs can greatly improve the quality of molecular captions. Most previous works have focused on aligning unimodal molecular structures with text, overlooking the diversity of modalities. Naive approaches to aligning multi-modal molecular structures with text often lead to (1) separately aligned embeddings, (2) inconsistent textual representations, and (3) increased computational overhead. To address these challenges, we propose LLM framework MV-CLAM equipped with MQ-Former, a novel multi-querying transformer. This architecture introduces a cross-model projector facilitating the simultaneous alignment of 2D and 3D molecular representations to a unified text token. By employing a shared self-attention layer, MQ-Former preserves rich molecular embeddings across different dimensions while consolidating them into a universal molecular token. Our approach outperforms baseline models in both molecule-text retrieval and molecule captioning tasks. Additionally, our framework shows promising results for zero-shot molecule editing and molecule-related question answering. By effectively integrating multi-view molecular data into a format conducive to LLMs, our method serves as a valuable tool for enhancing the characterization and understanding of chemical structures, facilitating a more seamless transition from molecular data to textual descriptions. The source code of MV-CLAM is available in https://anonymous.4open.science/r/mv-clam-4827.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The work proposes a novel multimodal LLM framework MV-CLAM for organic chemistry and MQ-Former — multi-querying transformer model for simultaneous 1D, 2D, and 3D molecular representation learning. Authors show SOTA results in two tasks of molecule-text retrieval and molecule captioning. In addition, authors claim that their approach allows zero-shot molecule editing and molecule-related question answering.

### Strengths
New molecular multimodal LLM framework for simultaneous incorporation of 1d 2D and 3D representations.
New Transformer architecture MQ-Former.

### Weaknesses
The claim of the state-of-the-art performance for molecule captioning is not satisfied, see the results in [6].
There is no comparison with the other strong retrieval methods for the molecule retrieval task, i.e. RAG.
There are various problems with the Zero-shot editing part of the paper. The task is not formally defined. There are no metrics nor baselines for it.

The QA part is practically absent in the paper, while claimed in the abstract and results parts..
There are many works on molecular conformation generation [1-4], it seems that SMILES and/or 2D-graph representation is enough for neural networks to reconstruct RDKIT conformations almost perfectly. It means that 3D input possibly does not add any new information to the model. There is no comparison of the 1D+2D+3D MQ-Former vs 1D+2D models in the paper.

There is no comparison with other works on multi-modal representation learning for molecules, e.g.: [5].

### Questions
1. 3D structures (conformers)

As mentioned in sec. 5.1 you use MMFF for molecular conformation generation.

a. Is it ETKDG geometry generation with further MMFF optimization?
b. Since it is possible to generate several different conformers for a single molecular structure, did you assess the dependence of the model quality on the conformations? Is it necessary to optimize a generated with ETKDG conformer with MMFF?

2.  It would be reasonable to compare your approach for Zero-shot editing with conditional generation models for small molecules.

3. Please, add experiments on the CHEBI-20 benchmark for the captioning task.

### Soundness
1

### Presentation
1

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
The paper introduces a framework that leverages large language models (LLMs) to interpret and generate molecular captions. The work incorporates both 2D and 3D molecular structures to provide a more comprehensive understanding of molecules.

### Strengths
1. The paper integrates both 2D and 3D molecular structures to enhance the model's understanding of molecular data.
2. The paper includes detailed figures (Figure 1-3) that clearly explain the method's framework and training scheme. 
3. And the analysis of attention maps in Appendix A.4 provides valuable insights into the model's behavior.

### Weaknesses
1. Compared to recent related work, such as 3D-MoLM (Li et al., 2024), the innovation in MV-CLAM appears incremental. While the paper claims to incorporate both 2D and 3D molecular structures for a more comprehensive understanding, the approach seems to merely extend the 3D-MoLM framework by introducing 2D components through MAT. The proposed MQ-former architecture does not demonstrate significant structural innovations beyond existing methods. A clearer articulation of the novel contributions and architectural advantages over 3D-MoLM would be necessary to establish the work's originality.
2. The paper considers SMILES as an important molecular modality and notes that "1D SMILES provide compact represen tation of molecular structures", but does not mention SELFIES (Krenn et al., 2020) at all, which has been widely adopted in recent works due to its robust characteristics and tokenization-friendly nature. SELFIES offers inherent robustness and easier tokenization that aligns well with LLMs, making it a potentially more suitable choice for this application. 
3. Some images (e.g. the big image at page 18) are not vector graphics and lack titles or captions, which makes it confusing.

### Questions
See 'Weaknesses' section.
1. Could the authors provide a more detailed explanation of the novelty of MV-CLAM compared to recent related work?
2. Why was SELFIES not considered as a molecular modality in this work, given its advantages over SMILES in tokenization and alignment with LLMs?

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
3

### Summary
The paper introduces MV-CLAM, a framework utilizing a novel multi-querying transformer (MQ-Former) to enhance the alignment of multi-modal molecular representations with text. By employing a shared self-attention layer, this approach effectively consolidates 2D and 3D molecular data into query tokens, improving performance in molecule-text retrieval and captioning tasks. Additionally, it demonstrates potential for zero-shot molecule editing and molecule-related question answering, thereby facilitating better characterization of chemical structures.

### Strengths
* The description of the proposed methodology is easy to follow. The paper is well written in general.
* The paper introduces a promising multi-view for approach for the infusion of specialized chemical knowledge into general-purpose pre-trained LLMs.
* The proposed MV-CLAM achieves state-of-the-art on PubChem324K for molecule captioning and retrieval tasks.

### Weaknesses
 * The experimental evaluation of the proposed method is conducted on a single dataset for both task: molecule captioning and molecule-text retrieval.
* The list of baseline models on molecule captioning only includes a single T5 language model while there are more recent works, including: nach0 and Text+ChemT5. 
* Some implementation decisions are not justified well enough. This includes: (i) the choice of SciBERT as a language encoder for MQ-Former; (ii) the choice of 2D and 3D encoders; (iii) introduction of $K$ query tokens instead of a single query token for each view; (iv) the choice of LLaMA2 as an LLM. It is unclear how the experimental results would change if each of the mentioned models is replaced with another one.
* Incomplete ablation study. The necessity of (i) Molecule-text Contrasting and (ii) Molecule-text Matching losses is not proven experimentally. For (i), it is unclear whether two loss components required or the model will perform well with a single one. For (ii), the impact of negative sample is under-explored. 
* The effect of most hyper-parameters in the method's module on the resulting performance is understudied. For instance, query token count, negative sample count in MTM loss.
* The methodology for molecule-text retrieval is unclear from the paper.
* The applicability of the proposed methodology to broader list of datasets is questionable: it requires 2D/3D molecular data in addition to simple SMILES string representations.

### Questions
* Add experimental comparison against more chemical language models on molecule captioning, e.g., nach0 [1], Text+Chem T5 [2], SciFive [3], PRESTO [4], GitMol [5].
* For retrieval task (Table 1), is it possible to add chemical BERT-based encoders in addition to textual encoder SciBERT? (e.g., ChemBERTa)
* Conduct additional experiments on other molecule captioning datasets such as Mol-Instructions [6] and CheBI20 [7].
* For molecule-text retrieval, do you adopt a generative approach (e.g., GENRE [8]) or the task is formulated as a cross-modal embedding-based search by similarity (e.g., as in [9])?
* In Figure 3, where does the textual description come from during prediction on a test set? As far as I understand the molecule captioning task, you are only given a SMILES string.
* What is the LLaMA version you use? Add adopted HuggingFace checkpoints. 
* Even if you adopt a LLaMA with 7B parameters, MolT5 has less than 1B. Could not we just scale MolT5 to 3-5B parameters and obtain a better molecule captioning quality?
* Why is MolT5 absent from the Table 1?
* Add ablation study for SciBERT, 2D/3D molecule encoders, LLaMA2.
* Add ablation study for training losses. For Molecule-text Contrasting loss, prove it requires two components. For Molecule-text Matching loss, explore the effect of negative samples.
* Is it possible to generalize the methodology to unseen datasets and unseen SMILES? Given a SMILES, can I always obtain its 2D/3D representation and apply a pre-trained MV-CLAM model?




Typos:
* Line 102: transformer -> Transformer, Add reference.
* Line 194: **$A$** under-specified.
* Line 234: Missing citation for LoRA.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes MQ-Former, an extension of the Q-Former framework, which incorporates a multi-query mechanism for aligning both 2D and 3D molecular data with textual information for enhanced molecule-text retrieval and molecule captioning.

### Strengths
- The paper aims to enhance cross-modal alignment by integrating 2D and 3D molecular views.
- The model demonstrates improvements in molecule-text retrieval and captioning performance over baseline models.
- The paper includes case studies and examples of zero-shot molecule editing.

### Weaknesses
 - The model lacks significant innovation, as MQ-Former primarily adds an extra branch to the existing Q-Former with only minor variations in training objectives. Specifically, the multi-query mechanism, while potentially useful, does not fundamentally alter the underlying architecture or training process compared to existing methods that utilize separate 3D encoders. The core idea of aligning multiple molecular views with text is not novel, and the paper does not adequately justify why a new branch is superior to simply using a pre-existing 3D molecular encoder.
- Experiments are restricted to molecule-text retrieval and captioning on PubChem. The paper lacks essential molecular tasks like molecule generation and datasets like ChEBI-20. The absence of molecule generation tasks is a notable gap, as this is a crucial capability for many practical applications. Furthermore, limiting the evaluation to PubChem restricts the generalizability of the findings, as PubChem is a relatively homogeneous dataset compared to more diverse datasets like ChEBI-20, which includes a broader range of chemical structures and complexities.
- The motivation for adding a branch to Q-Former, rather than simply using a 3D molecular encoder like prior works (e.g., 3D-MoLM), is unclear. The paper does not provide a strong rationale for why the proposed multi-query approach offers a significant advantage over existing methods. A more detailed analysis of the benefits and drawbacks of each approach is needed to justify the architectural choice. The paper also lacks a thorough comparison with existing 3D molecular encoders, making it difficult to assess the true contribution of the proposed method.
- The paper’s presentation could be improved. Plots lack careful formatting, with text that is difficult to read due to small font sizes. This lack of attention to detail in the presentation detracts from the overall quality of the paper and makes it harder to understand the experimental results.

### Questions
- How does MQ-Former handle scenarios where 2D and 3D molecular information may not equally contribute to textual descriptions?
- Could the authors include more molecular tasks, such as molecule generation or property prediction, to provide a more comprehensive evaluation of MQ-Former?
- What impact does the weighting of the multi-objective training loss have on the model’s performance?

### Soundness
2

### Presentation
2

### Contribution
2
