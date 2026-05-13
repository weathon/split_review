# UniMoT: Unified Molecule-Text Language Model with Discrete Token Representation

- Decision: Reject
- Scores: 5, 5, 6, 3

## Abstract
The remarkable success of Large Language Models (LLMs) across diverse tasks has driven the research community to extend their capabilities to molecular applications. However, most molecular LLMs employ adapter-based architectures that do not treat molecule and text modalities equally and lack a supervision signal for the molecule modality. To address these issues, we introduce \textbf{UniMoT}, a \textbf{Uni}fied \textbf{Mo}lecule-\textbf{T}ext LLM adopting a tokenizer-based architecture that expands the vocabulary of LLM with molecule tokens.
Specifically, we introduce a Vector Quantization-driven tokenizer that incorporates a Q-Former to bridge the modality gap between molecule and text. This tokenizer transforms molecules into sequences of molecule tokens with causal dependency, encapsulating high-level molecular and textual information. 
Equipped with this tokenizer, UniMoT can unify molecule and text modalities under a shared token representation and an autoregressive training paradigm, enabling it to interpret molecules as a foreign language and generate them as text.
Following a four-stage training scheme, UniMoT emerges as a multi-modal generalist capable of performing both molecule-to-text and text-to-molecule tasks. Extensive experiments demonstrate that UniMoT achieves state-of-the-art performance across a wide range of molecule comprehension and generation tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
A key limitation in current applications of large language models (LLMs) to molecule-text tasks is the imbalance in processing modalities: text is handled directly by the encoder, while molecules require separate adapters. To address this, the authors propose UniMoT, a model that employs a Vector Quantization (VQ) tokenizer to incorporate molecules into the LLM vocabulary as discrete tokens. This tokenizer works with a Q-Former, which transforms molecular features into causal sequences, allowing the model to train on interleaved molecular and textual data with a single next-word prediction objective. A four-stage training process is then introduced. Experimental results across tasks, including molecular property prediction, molecule captioning, molecule-text retrieval, and molecule generation, show that the proposed method can prompt the understanding of text and molecules, often better than established baselines.

### Strengths
1. The work is well-motivated and builds on a solid foundation, given existing multimodal studies in text-image tasks. The approach to integrating molecules and text in a unified framework is reasonable and leverages known multimodal strategies.
2. The experiments cover multiple task types, showing the effectiveness of the proposed method across various molecule-related tasks. In most cases, the proposed approach outperforms established baselines.
3. The paper is clearly presented and well-organized, with figures that illustrate key concepts, making the ideas easy to follow.

### Weaknesses
1. Technically speaking, the proposed method shares overlaps with existing studies, such as SEED-LLaMA. While UniMoT targets molecule-text modalities, the frameworks overlap in modules like the discrete tokenizer, causal Q-Former, next-token prediction, and reconstruction during inference. This overlap raises questions about novelty.
2. Considering the complexity of the four-stage training process, the performance improvements may not fully justify the added effort. In some tasks, for example, Table 2, its performance is no better than that of baseline methods and is sometimes worse.
3. While the focus is on molecule-text, the paper needs a more comprehensive discussion of and comparison with existing multimodal research, even if primarily in text-image or multi-modality settings, such as AnyGPT and MIO.

### Questions
The fourth stage includes prompting and instruction following. Is this stage essential, considering the complexities of prompt generation and response parsing? If so, how does prompt engineering influence the final performance?

### Soundness
3

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
The paper presents UniMoT, a unified molecule-text language model that leverages discrete token representations to integrate molecular and text. UniMoT uses a tokenizer-driven framework, where a VQ-based tokenizer, combined with a causal Q-Former, encodes molecules as discrete tokens. These discrete tokens are aligned with text tokens in a shared vocabulary, enabling UniMoT to operate in an autoregressive training paradigm across both modalities.

### Strengths
* The VQ-driven tokenizer for molecules enables the unified modeling of molecule and text in language model.
* UniMoT shows impressive state-of-the-art results across multiple understanding and generation tasks.

### Weaknesses
 * The core components, such as the Q-Former and VQ-based tokenizer, appear to be direct adaptations from CV, which may limit the paper’s originality within the molecular modeling domain.
* The discrete tokenization approach could lead to information loss, and the model’s effectiveness over directly training with combined molecule SMILES and text is not convincingly demonstrated. Specifically, the paper lacks a direct comparison to a model trained end-to-end on SMILES strings and text, making it difficult to assess the true benefit of the tokenization approach. The ablation study should include a baseline that replaces the VQ-based tokenizer with a direct SMILES encoder/decoder to isolate the impact of the tokenization.
* The multi-stage training process is complex. The paper does not provide sufficient justification for the specific sequence of pretraining steps, and it is unclear why the Causal Q-Former needs to be pretrained before the tokenizer. A more detailed analysis of the impact of each stage on the final performance would be beneficial.
* The evaluation on the Mol-Instructions benchmark lacks some important baselines, like DARK[1].

### Questions
* Could the causal dependency in learnable queries negatively impact molecular understanding compared to bidirectional or other full-information modeling approaches?
* Are the models for each downstream task trained separately or together? The authors should provide more detailed introduction.
* More details on the adapter and SMILES decoder would strengthen clarity, particularly regarding their roles in aligning molecular representations and decoding.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents UniMoT, a Unified Molecule-Text Large Language Model that addresses limitations in existing molecular LLMs by employing a tokenizer-based architecture that treats molecule and text modalities equally. By introducing a Vector Quantization-driven tokenizer, UniMoT effectively bridges the gap between these modalities, enabling it to interpret and generate molecules as text. Extensive experiments show that UniMoT achieves state-of-the-art performance in various molecular comprehension and generation tasks.

### Strengths
* The paper proposes a novel methodology for chemical Large Language Model (LLM) pretraining which addressed multiple problems related to cross-modal text and molecule pretraining, including long sequence lengths and the lack of left-to-right causal dependency in molecule features.
* Extensive evaluation on MoleculeNet highlights the effectiveness of the proposed pre-training technique on non-generative molecular property prediction tasks.
* The experimental results on molecular retrieval and generation tasks show that the proposed UniMoT models performs on par or better than the selected baselines.
* The methodological decisions are experimentally supported with a thorough ablation study.

### Weaknesses
 * From the paper, it it unclear if the improvement over baseline methods is statistically significant.
* On molecule generation task, UniMot is mostly compared against general-purpose LLMs which were not specifically designed for chemistry-related tasks. The comparison against more domain-specific methods, such as nach0, GIT-MOL, and Text+Chem T5 could strenghten the paper claims.
* Lack of comparison with chemical language models (nach0, GIT-MOL, and Text+Chem T5, MolT5 as well as encoder-only ChemBERTa and PubChemDeBERTa) on MoleculeNet benchmark and molecule-text retrieval task.
* Lack of ablation study for training objectives. For instance, Equation 2 has 3 terms, what would happen if you remove some of them? How much would the performance drop if the codebook is removed and the model is forced to generate SMILES directly?


### Questions
Suggestions:
* Additional MoleculeNet experiments with encoder-only chemical language models, such as ChemBERTa [1], PubChemDeBERTa [2], would  show whether LLMs are needed for simple regression/classification tasks in the chemical domain.
* Provide statistical significance tests' results to explore whether the performance gain over baseline models is statistically significant.
* Why are MolT5, MoMu, MolCA absent from Table 1? For me, it makes sense to compare UniMoT with them on MoleculeNet since they are also chemical language models.
* Add more experiments with other recent state-of-the-art chemical language models: GIT-MOL [3], nach0 [4], and Text+Chem T5 [5]. nach0 and GIT-MOL also report the MoleculeNet results as well as performance on molecule generation and molecule captioning  
* Why don't you adopt SELFIES and experiment with SMILES only?
* Line 046: for a reader not familiar with the domain, it would be good have a brief description of what is SMILES and provide some examples.
* As far as I know, MoleculeNet mostly covers small datasets. How stable are results across different runs?

Typos:
* Line 159: $F$ is not introduced earlier.


References:
[1] Chithrananda, Seyone, Gabriel Grand, and Bharath Ramsundar. "ChemBERTa: large-scale self-supervised pretraining for molecular property prediction." arXiv preprint arXiv:2010.09885 (2020).
[2] Schuh, Maximilian G., Davide Boldini, and Stephan A. Sieber. "TwinBooster: Synergising Large Language Models with Barlow Twins and Gradient Boosting for Enhanced Molecular Property Prediction." arXiv preprint arXiv:2401.04478 (2024).
[3] Liu, Pengfei, et al. "Git-mol: A multi-modal large language model for molecular science with graph, image, and text." Computers in biology and medicine 171 (2024): 108073.
[4] Livne, Micha, et al. "nach0: Multimodal natural and chemical languages foundation model." Chemical Science 15.22 (2024): 8380-8389.
[5] Christofidellis, Dimitrios, et al. "Unifying molecular and textual representations via multi-task language modelling." International Conference on Machine Learning. PMLR, 2023.

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
The authors introduce UniMoT, a Unified Molecule-Text LLM adopting a tokenizer-based architecture that expands the vocabulary of LLM with molecule tokens. Specifically, we introduce a Vector Quantization-driven tokenizer that incorporates a Q-Former to bridge the modality gap between molecule and text. This tokenizer transforms molecules into sequences of molecule tokens with causal dependency, encapsulating high-level molecular and textual information. Equipped with this tokenizer, UniMoT can unify molecule and text modalities under a shared token representation and an autoregressive training paradigm. It can interpret molecules as a foreign language and generate them as text. Following a four-stage training scheme, UniMoT emerges as a multimodal generalist capable of performing both molecule-to-text and text-to-molecule tasks.

### Strengths
The background and motivation for utilizing LLMs for the learning process is well described, with relevant references. 

There are different informative experiment tasks evaluated including molecular property prediction and molecule captioning. Ablation studies are also informative for the different generation tasks.

### Weaknesses
There is not much information about how the design choice of the author’s model is representing the natural graph molecular structure of the molecule itself (e.g., atom and bond structure). This is a recent survey paper that is missing in the cited work that the authors should include. The LLM itself is known to not as comprehensively capture graph structure.

[IJCAI 2023] Graph-based molecular representation learning. In Proceedings of the Thirty-Second International Joint Conference on Artificial Intelligence (IJCAI '23). Article 744, 6638–6646. https://doi.org/10.24963/ijcai.2023/744

The experiment benchmarks need to include more GNN based representation models, and experiment results of the model do not seem conclusive for the molecular property prediction task, perhaps indicating that there needs to be more explicit learning of graph topological structure.

### Questions
See above sections for details.

### Soundness
2

### Presentation
3

### Contribution
2
