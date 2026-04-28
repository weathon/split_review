# Improving Molecule-Language Alignment with Hierarchical Graph Tokenization

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 3, 6, 3

## Abstract
Recently there has been a surge of interest in extending the success of large language models (LLMs) to graph modality, such as molecules. As LLMs are predominantly trained with 1D text data, most existing approaches adopt a graph neural network to represent a molecule as a series of node tokens and feed these tokens to LLMs for molecule-language alignment. Despite achieving some successes, existing approaches have overlooked the hierarchical structures that are inherent in molecules. Specifically, in molecular graphs, the high-order structural information contains rich semantics of molecular functional groups, which encode crucial biochemical functionalities of the molecules. We establish a simple benchmark showing that neglecting the hierarchical information in graph tokenization will lead to subpar molecule-language alignment and severe hallucination in generated outputs. To address this problem, we propose a novel strategy called HIerarchical GrapH Tokenization (HIGHT). HIGHT employs a hierarchical graph tokenizer that extracts and encodes the hierarchy of node, motif, and graph levels of informative tokens to improve the graph perception of LLMs. HIGHT also adopts an augmented molecule-language supervised fine-tuning dataset, enriched with the hierarchical graph information, to further enhance the molecule-language alignment. Extensive experiments on **14** molecule-centric benchmarks confirm the effectiveness of HIGHT in reducing hallucination by **40%**, as well as significant improvements in various molecule-language downstream tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a new approach to aligning molecular graph representations with language using a method called Hierarchical Graph Tokenization (HIGHT). Traditional graph-language alignment models primarily focus on node-level information, often neglecting the inherent hierarchical structure of molecules, which leads to alignment issues and hallucination in large language models (LLMs).

The authors introduce HIGHT, which utilizes a hierarchical graph tokenizer to capture information at the node, motif, and entire molecule levels. This tokenizer incorporates both atom-level and motif-level tokens, which are then used to improve alignment with language models. To address the alignment of hierarchical molecular data with textual descriptions, the authors also develop an enhanced molecular instruction tuning dataset called HiPubChem, which provides detailed motif information.

### Strengths
1. The Hierarchical Graph Tokenization (HIGHT) technique is a major advancement. By incorporating hierarchical structure at multiple levels (node, motif, and graph), the paper addresses a crucial gap in previous molecule-language alignment methods, which typically rely only on node-level information. This hierarchical approach captures the functional groups and structural motifs inherent in molecules, improving the model’s ability to represent complex biochemical properties accurately.

2. The introduction of HiPubChem, an augmented molecular instruction tuning dataset enriched with motif and functional group information, enhances model training by aligning molecular structural details with language descriptions. This contribution is valuable for future work in molecular and biochemical language model alignment.

3. The effectiveness of each of the two methods was verified through simple ablation studies.

### Weaknesses
1. The introduction of the hierarchical graph tokenizer seems to make the tokenizer larger compared with the ordinary node-level tokenizer. It should be discussed that whether the performance gain comes from the larger tokenizer. Specifically, the paper lacks a detailed analysis of the parameter count for both the node-level and hierarchical tokenizers, and how this difference in size might affect the results, especially given that larger models often exhibit better performance simply due to increased capacity. A comparison of the number of parameters in the GNN encoder and the projection layers for both tokenizers is needed to understand the source of the performance gains.

2. There should be more detail descriptions and discussions about the evaluation tasks. The paper does not provide sufficient detail regarding the specific inputs and outputs for each evaluation task. For example, in molecular property prediction, it is unclear whether the task is classification or regression, and what the exact input format is (e.g., SMILES strings, graph representations). Similarly, for chemical reaction prediction, the paper should specify the input (reactants, reagents) and output (products) formats, and whether the task involves single-step or multi-step reactions. Without these details, it is difficult to assess the validity and generalizability of the results.

### Questions
1. How many parameters do those two tokenizers have respectively?
2. What are the ablation study results on other tasks such as property prediction and chemical reaction prediction? 
3. What are the input and output of the molecular property prediction task and other tasks? The performance gain mainly comes from hierarchical graph tokenization, and it has nothing to do with the new tuning dataset, right?

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
3

### Summary
The authors study Large Graph Language Models (LGLM). Drawing inspiration from Multimodal LLMs, authors focus on the task of incorporating graph data as a separate modality with a GNN encoder and an adapter. Authors conclude that node-centric tokenization of molecules leads to LLM hallucinations when asked about the presence of specific fragments. To overcome this issue, the authors propose to enrich the molecule's description by adding the tokens corresponding to BRICKS-fragments that are present in the molecule. The experimental results demonstrate that such a tokenization scheme reduces the amount of motif-related hallucinations and improves performance on other tasks.

### Strengths
An improved tokenization of molecular graphs that enriches molecule's description with motif tokens.

### Weaknesses
Specifically, most existing LGLMs directly take the node tokens from GNNs as inputs to LLMs (Cao et al., 2023):
The paper cites InstructMol as a previous approach that utilizes node-centric tokenization. However, if I understand correctly, InstructMol takes the embedding of the whole graph along with the SMILES representations of the molecule. Moreover, it is not clear which previous models use the node-centric tokenization and whether there are such models at all.

Section 4.3 describes the fine-tuning approach that involves two stages, where the second stage is the finetuning on MoleculeNet, CheBI-20 and Mol-instructions specialized datasets. In my opinion, this implies that the resulting model is specialized. Please, provide better explanation for specialist and generalist models.				

Taking into consideration that the difference between specialist and generalist models is not clear, the resulting model does not demonstrate performance superior to baselines in most of the experiments.

There is no comparison with [1] in Table 4. The results in [1] are superior to all the models from Table 4.

In Table 5, the Mol-instruction has the highest MACCS FTS for the retrosynthesis task. However, a smaller number is balded.

The comparison on MotifHallu is not complete. Please provide comparison with SMILES-based approaches. Moreover, the improvement on the MotifHally benchmark is expected, as the proposed approach was explicitly designed to better solve this task.

### Questions
Listed in Cons.

### Soundness
2

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
4

### Summary
This paper proposes HIerarchical GrapH Tokenization (HIGHT), which tries to improve how LLMs understand and process molecular data. The key idea of HIGHT is to introduce a hierarchical graph tokenizer that extracts and encodes information at multiple levels: atoms, motifs, and the overall molecule. The paper demonstrates that HIGHT can reduce hallucination and improve performance across various molecular tasks, including property prediction, molecular description generation, and chemical reaction prediction.

### Strengths
1.  This paper proposes to incorporate hierarchical graph information into LGLMs, and the authors achieve this with new architecture and instruction tuning dataset HiPubChem.
2. To address hallucination issue, the paper creates MotifHallu, the first hallucination benchmark based on the existence of common functional groups.
3. The paper includes extensive experiments with 14 real-world molecular and reaction comprehension benchmarks. The results show that HIGHT significantly reduces the hallucination on MotifHallu and demonstrates significant improvement on a number of tasks.

### Weaknesses
1. The hierarchical graph tokenization process, which involves the use of multiple adapters, is likely to be more computationally expensive than traditional node-centric tokenization. The paper does not discuss the computational complexity. Also, LLM is tuned using LORA, and the number of parameters tuned should be discussed.
2. One motivation of applying LLMs for graph data is to utillize the generalization capability of LLMs. However, this paper do not provide experimental results on zero-shot or few-shot scenarios of the proposed model. I think it will greatly strength the paper if HIGHT has good performance under such cases.
3. The performance of HIGHT will largely depend on the backbone LLMs, and only vicuna-v-1.3-7B is evaulated.

### Questions
1. At line 273, the authors said "attach positional encodings $p$ to all of the tokens", How are position encodings of motifs obtained?
2. If the input graphs use the positional encodings, then, should the original positional encodings in the LLMs be diabled? e.g, the widely used ROPE for the graph input part? 
3. What is the papameter count to be tuned?
4. Besides the vicuna-v-1.3-7B, can the authors provide experimental resutls for other LLM backbones? Since different backbones may have  a big impact on the performance.
5. How is the proposed model performance for zero-shot or few-shot scenarios?
6. In table 2, llama 13b has wrose performance than llama 7b on most of datasets. Also, Galactica-120B has a sharp performance drop on BACE. Any explanations on these results?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a framework named HIGHT to align molecular data with LLMs. It identifies a shortcoming of LLM on learning functional groups, and proposes to extend the graph tokenization to motif level. Specifically, its input to the LLM includes node/atom embeddings as well as motif embeddings. The model is fine-tuned with motif prediction tasks on a dataset constructed using RDKit. The model shows good performance on molecule properties prediction compared to language models.

### Strengths
The overall presentation is clear and the paper is easy to follow. The work proposes a complete pipeline to build a model with stronger motif/functional group querying ability. Using motif tokens is a straight-forward solution to enhance such ability. Various experiments are conducted to validate the model.

### Weaknesses
 - From the novelty and contribution perspective, taking motif representations/tokens is not new. By simply searching on Google, I found several papers that extract motifs for graph modeling [1, 2] (as the author also mentioned in the paper). This work is a simple extension of these techniques to align the motifs to the LLM. The core idea of using structural motifs to enhance molecular representation is well-established, and the paper doesn't sufficiently demonstrate a novel application of this concept within the context of large language models.

- If I understand correctly, the motif tokenization algorithm, BRICS, will break the molecule in a very chemistry-aligned way. For example, a "OH" functional group will be tokenized into a motif. The downstream task of identifying the functional group will be very easy (simply aligning a single motif token with the text description of the function group, and the task is like asking "does a -OH motif have -OH functional group"). The author should justify how this is a helpful task besides simply telling the LLM that "there is such a functional group." For example, the author should show that the method has better downstream performance than simply telling the LLM the existence of functional groups. The current evaluation does not adequately demonstrate that the model learns beyond a simple lookup of pre-defined motifs.

- The distinction between specialist model and generalist model is arbitrary to me. Methods like MolFM and Text+Chem T5-augm-base have the same functionality as the proposal, yet they achieved better performance than HIGHT. I think the HIGHT is more specialized, as it requires explicit and specialized atom and motif tokenization. Can you be more specific about the distinction, and what's the advantage of a generalist model? The paper needs to clarify what specific architectural or training differences make a model 'generalist' versus 'specialist' in this context. The current explanation is insufficient to justify the categorization.

- Even without the motif tokens, many models achieved stronger performance. Can you explain why a better motif prediction ability does not lead to better downstream performance? Link back to weakness 1, does this also mean that the proposed task is too easy for the motif tokenization, preventing the model from learning meaningful/molecule-property-related from the pretraining process?

### Questions
- In tables 3, 4, 5, are all baselines also fine-tuned with the same dataset as HIGHT?

### Soundness
2

### Presentation
3

### Contribution
2
