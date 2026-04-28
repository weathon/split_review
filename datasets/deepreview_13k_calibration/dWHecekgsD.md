# Towards Fine-grained Molecular Graph-Text Pre-training

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 3, 5

## Abstract
Understanding molecular structure and related knowledge is crucial for scientific research. Recent studies integrate molecular graphs with their textual descriptions to enhance molecular representation learning. % enhancing the ability to generalize to unseen molecules and texts. 
However, they focus on the whole molecular graph and neglect frequently occurring subgraphs, known as motifs,% which encompass important submolecular knowledge common across molecules.
which are essential for determining molecular properties. 
Without such fine-grained knowledge, these models struggle to generalize to unseen molecules and tasks that require motif-level insights. 
To bridge this gap, we propose FineMolTex, a novel \textbf{Fine}-grained \textbf{Mol}ecular graph-\textbf{Tex}t pre-training framework to jointly learn coarse-grained molecule-level knowledge and fine-grained motif-level knowledge. 
Specifically, FineMolTex consists of two pre-training tasks: a contrastive alignment task for coarse-grained matching and a masked multi-modal modeling task for fine-grained matching. 
In particular, the latter predicts the labels of masked motifs and words, leveraging insights from each other,  thereby enabling FineMolTex to understand the fine-grained matching between motifs and words.
Finally, we conduct extensive experiments across three downstream tasks, 
achieving up to 230\% improvement in the text-based molecule editing task. Additionally, our case studies reveal that FineMolTex successfully captures fine-grained knowledge, potentially offering valuable insights for drug discovery and catalyst design.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces FineMolTex, a multi-modal learning framework for molecule-text modeling. FineMolTex is a multi-modal language model that jointly models molecules and texts. For molecules, it decomposes them into motifs, and utilize a GNN to obtain motif embedding; for text, it utilizes a pretrained BERT encoder to obtain text embeddings. Then, the motif embeddings and text embeddings are fed into separate transformers for cross-modal learning. Specifically, FineMolText utilizes two pretraining tasks: 1) contrastive alignment and 2) masked multi-modal modeling. For contrastive alignment, a classifical contrastive learning loss is applied on the final embedding of motifs and texts, obtained from separate transformers. For masked multi-modal modeling, motifs and texts are randomly masked, and the transformers are trained to recover the masked tokens using Cross-Entropy loss. Notably, for this task, the two transformers for texts and motifs are connected through the internal cross-attention layers.

The proposed method are further applied for downstream tasks of graph-text retrieval (Table 1, Table 2), molecular property prediction (Table 3), and molecule editing (Figure 3, Figure 4).

### Strengths
1. The proposed method is overall sound, and the studied problem is relevant to the ICLR conference.
2. The proposed method achieves top performances for graph-text retrieval for the DrugBank-Pharmacodanamics, and molecule-ATC datasets.

### Weaknesses
1. The overall methodology is not surprising. Most components, like the multi-modal masked modeling and contrastive learning, are already seen in previous works. The new part is to represent molecules as decomposed motifs and use GNN encoder for motif representation.
2. Considering PubChem is used as as the training dataset, you need to test your model on PubChem's test set to really demonstrate the performance of your model. This is standard in your baselines, like MoleculeSTM, MoMu, and MolCA.
3. The authors have tested their model for property prediction on the MoleculeNet datasets. However, as I understand, the value of this evaluation is insignificant. The main reason is the limited performances for the proposed method and all the baselines. As shown in [1], combining proper feature engineering and simple algos, like SVM, usually achieve much better performances than deep learning models. Therefore, the authors should explain the value of this evaluation.

### Questions
1. The motivation of this work is to study fine-grained molecule representation (motifs). Have the authors considered combining a global representation, like a global GNN embedding and a complete SMILES, with fine-grained representations for improved performance?
2. Does using fine-grained representation of motifs improve the explanability of your method?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes FineMolTex, a framework designed for fine-grained molecular graph-text pre-training, focusing on motif-level knowledge to bridge molecular graphs and textual descriptions. The paper claims novelty in learning fine-grained motif knowledge alongside coarse molecule-level knowledge. FineMolTex employs two key tasks: contrastive alignment for molecule-text matching and masked multi-modal modeling for motif-level alignment.

### Strengths
- FineMolTex emphasizes motif-level knowledge. This attention to motifs could improve understanding of molecular properties crucial for zero-shot tasks.
- The use of contrastive alignment and masked multi-modal modeling helps integrate fine-grained motif and molecule-level knowledge.
- FineMolTex demonstrates improved performance on tasks like graph-text retrieval and molecule editing.

### Weaknesses
 - The paper claims, “We are the first to reveal that learning fine-grained motif-level knowledge provides key insight for bridging molecular graphs and text descriptions.” However, prior work, such as HIGHT [1], has already established the importance of motif-level knowledge for improving alignment and preventing hallucination. HIGHT also introduces a hierarchical graph tokenizer that captures information at the node, motif, and graph levels. The motivation and core idea behind your paper and HIGHT are essentially the same.
- The core architecture of FineMolTex lacks novelty. The contrastive pretraining and cross-attention mechanisms for different modalities are derived from BLIP-2, while the masked modeling approach is taken from BERT and is commonly used in models like MAE. The methodology does not present any surprising innovations. The use of standard techniques, such as contrastive loss and masked modeling, without significant modifications or novel combinations, raises concerns about the overall contribution.
- The architecture of FineMolTex appears no more advanced than Q-Former in BLIP-2 and lacks key pretraining tasks such as Image-Text Matching and Image-Grounded Text Generation present in Q-Former. It is unclear why the authors propose an architecture seemingly weaker than Q-Former instead of directly leveraging Q-Former itself. The absence of these established pretraining tasks further weakens the justification for the proposed architecture.
- The experiments could be expanded to include more tasks, such as molecule captioning and generation. The current evaluation is limited in scope, and additional tasks would provide a more comprehensive assessment of the model's capabilities.
- The paper compares against older baselines and omits recent baselines like 3D-MoLM [2]. This casts doubt on the reported state-of-the-art performance. The lack of comparison with state-of-the-art models makes it difficult to assess the true impact of the proposed method.
- Key hyperparameter details are not provided.

### Questions
- Do you train the transformer and cross-attention layers from scratch? How many layers are used?
- Why did you choose to train the transformer layers rather than using a pretrained LLM and then finetuning?
- Given that FineMolTex does not use a pretrained LLM, how does its computational efficiency (in terms of training and inference time) and memory cost compare with models that utilize LLMs?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents FineMolTex, a pre-training framework designed to enhance molecular representation learning by integrating coarse-grained molecule-level knowledge with fine-grained motif-level insights. 
Recognizing the importance of motifs in tasks that require detailed molecular understanding, FineMolTex employs a two-branch architecture for motif embedding and textual representation learning, incorporating a cross-attention layer to facilitate information exchange between modalities. 
The framework utilizes two pre-training tasks: a contrastive alignment task for molecule-level matching and a masked multi-modal modeling task for motif-level matching. 
Experimental results indicate performance improvements in downstream tasks, particularly in text-based molecule editing.

### Strengths
1. The experimental results demonstrate a promising performance gain over existing baselines.
2. The paper is well-organized, featuring a logical flow and clear explanations that make it easy to follow.

### Weaknesses
1. The figures require refinement; in Figures 1 and 2, some highlighted areas extend beyond the dashed boxes, and the <mask> tokens overlap with the text and motifs (e.g., in Figure 2(b), did you input "carboxylic"?).
2. Retrieve tasks need more metrics like recall.
3. The experiments and datasets generally follow the MoleculeSTM framework but overlook more challenging and practical text-based molecule editing tasks, such as multiple-objective property-based editing, binding-affinity-based editing, and drug relevance editing. This omission significantly undermines the claim of "a notable improvement of up to 230% in the text-based molecule editing task."

### Questions
I fully acknowledge the significance of motif-level molecule-text alignment, which the authors assert as their primary contribution. 
However, I did not find any explicit supervision signal for such fine-grained alignment. 
I remain unconvinced that masked multi-modal modeling can effectively capture it. 
Furthermore, the experiments lack qualitative results that would demonstrate the effectiveness of this alignment, aside from the case studies. 
Given that this is the most critical claim made by the authors, I would reconsider my rating to accept if I am convinced that masked multi-modal modeling successfully achieves motif-level molecule-text alignment.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The main idea of this paper is to show that fine-grained motif-level knowledge is crucial for molecular representation learning. Basen on this, the author propose FineMolTex, which jointly learns both coarse and fine-grained knowledge through a contrastive alignment task and a masked multimodal learning task. Experimental results on three downstream tasks and two case studies demonstrate the effectiveness of FineMolTex.

### Strengths
1. Unlike previous models that primarily focus on molecule-level representations, the proposed FineMolTex incorporates motif-level knowledge, capturing the significance of frequently occurring subgraphs within molecular graphs. This allows the model to better generalize to unseen molecules, achieving better performance on zero-shot tasks.
2.  This paper is well-written, and each component is clearly presented. The author performed extensive experiment evaluations, and showed that FineMolTex achieved good performance.

### Weaknesses
1. As compared with existing studies, e.g., MoleculeSTM, the main difference in this paper is to consider motif-level knowledge. Then the similar framework from MoleculeSTM seems can be extended in a straightforward way. Also, motif info is widely used in existing studies (though not in the molecule-text moltimodal scenario). Therefore, the authors need to better explain the novelties of the proposed approach.
2. Modeling both molecule-level and motif-level knowledge may increase computational costs compared to models focusing solely on molecule-level representations, and the computational complexity should be discussed.
3.  The effectiveness of FineMolTex will rely on accurate and meaningful motif extraction from molecular graphs. Can BRICS algorithm used in this paper meet this requirement? or is there other motif extraction algorithms that will show a performance difference?

### Questions
Please see the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
