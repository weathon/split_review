# General-purpose Pre-trained Model Towards Cross-domain Molecule Learning

- Decision: Reject
- Scores: 3, 5, 8, 5

## Abstract
Self-supervised pre-training on biomolecules has achieved remarkable success in various biochemical applications, such as drug discovery and protein design. However, in most approaches, the learning model is primarily constructed based on the characteristics of either small molecules or proteins, without exploring their potential binding interactions -- an essential cross-domain relationship crucial for driving numerous biological processes. In this paper, inspired by the success of multimodal learning, we fill this gap by proposing a general-purpose foundation model named **BIT** (an abbreviation for **B**iomolecular **I**nteraction **T**ransformer), which is capable of encoding a range of biochemical entities, including small molecules, proteins, and protein-ligand complexes, as well as various data formats, encompassing both 2D and 3D structures, all within a shared Transformer backbone, via multiple unified self-supervised atom-level *denoising* tasks. We introduce *Mixture-of-Domain-Experts* (MoDE) to handle the biomolecules from diverse chemical domains and incorporate separate structural channels to capture positional dependencies in the molecular structures. The proposed MoDE allows BIT to enable both deep fusion and domain-specific encoding and learn cross-domain relationships on protein-ligand complexes with 3D cocrystal structures. Experimental results demonstrate that BIT achieves exceptional performance in both protein-ligand binding and molecular learning downstream tasks, including binding affinity prediction, virtual screening, and molecular property prediction.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a multitask Transformer architecture for molecular interaction learning called Biomolecular Interaction Transformer (BIT)  and a self-supervised learning objective of coordinate denoising and masked token denoising. This approach allows the model to learn representations of biomolecules of both 2D and 3D structures. Moreover, the paper introduces the Mixture-of-Domain-Experts (MoDE) module, which enables the model to learn from biomolecules belonging to different chemical domains (proteins and ligands).

### Strengths
+ The paper is well motivated and the writing is clear.
+ The proposed approach focuses on protein-ligand interactions, which is of paramount importance for drug discovery and can potentially lead to more efficient and effective therapeutic solutions.

### Weaknesses
 - The pretraining process appears to be confined to proteins and small molecules. This limited scope raises questions about the model's applicability to a broader range of biomolecules and interactions.
- The proposed Transformer backbone is invariant to geometric transformations, which may limit its expressive power compared to SE(3) or E(3) equivariant architectures.
- The model only considers the binding pocket segment of proteins—while computationally efficient, may not be practically feasible without costly simulations to identify these segments. This reliance on prior knowledge or expensive computations could limit the accessibility and scalability in practical applications.
- The strategy of pre-training the model on both equilibrium structures of molecules and higher-energy protein-ligand complexes may be conceptually problematic. These two types of data represent vastly different energy states, and it is unclear what meaningful semantic learning can be achieved by pretraining them together. This may lead to a model that does not adequately distinguish between the distinct energetic landscapes of the two systems.  Also, the scales of the two training sources are not balanced, where PCQM4Mv2 is significantly larger than Q-BioLiP, but the model performance on molecular property prediction is not very significant compared to the baselines, which warrants a further examination.
- There is a lack of a detailed explanation for how positional encodings of 2D and 3D structures are integrated into the model, which leaves a gap in understanding the full architecture and mechanics of the model.

### Questions
Please see the above weaknesses section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this study, a new pre-trained transformer, BIT, is introduced for processing small molecules, proteins, and ligand-protein complexes. The architecture is based on Transformer-M, which is a transformer architecture that enables the processing of 2D and 3D structures. The main architectural innovation introduced in this work is the use of Mixture-of-Domain-Experts (MoDE) that replaces feed-forward layers, allowing for different processing of small molecules and macromolecules. Two pre-training methods, masking and coordinate denoising, are used to improve the performance of this model. BIT can be utilized for various molecular tasks, including molecular property prediction, structure-based virtual screening, and binding affinity prediction. The experimental section shows that BIT outperforms similar approaches in all three tasks.

### Strengths
- The proposition to use Mixture-of-Domain-Experts in order to process both small molecules and proteins and protein-ligand complexes is interesting. This way, the transformer can be (pre)trained using more data with high diversity.
- Two pre-training methods are implemented, and the strong performance of the pre-trained transformer is demonstrated in the experiments.
- The motivation of the paper is clear, and the methodology and experiments are easy to follow.
- This work has some significant applications in the molecular modeling domain, especially in structure-based drug design. Because BIT can process both small molecules and proteins, the application domain is very broad. The significance of the study is corroborated by the strong performance in the molecular property prediction, binding affinity prediction, and structure-based virtual screening tasks.

### Weaknesses
 - The main novelty of the paper is the introduction of MoDE in order to process data from diverse molecular domains. In my opinion, the paper lacks a proper evaluation of what these experts learn. For example, do molecule and pocket experts learn similar weights, or are there significant differences? What is the performance of this model when only one type of feed-forward layer is used (like in Transformer-M), but the same pretraining procedure is applied?
- The Authors propose to use two pre-training objectives. It would be interesting to see what is the impact of each of them. Why did the Authors decide to use a different pre-training procedure than used in Transformer-M? The experimental tables are missing the results achieved for the non-pretrained model.
- The choice of the models used in the experiments seems arbitrary. For example, why are different models used for binding affinity prediction and molecular property prediction? GROVER could be used in both scenarios. Why are some of these models not pre-trained, while the original works provide pre-training procedures (and sometimes also the pre-trained weights), e.g. GROVER and MAT?
- Finally, another benchmark for structure-based virtual screening would be helpful in assessing the performance of the proposed method. It has been shown, that decoys contain hidden biases that can impact the performance of deep learning methods [1].

In conclusion, the paper introduces some new ideas (mixing of domains and a different pre-training procedure), but the presented results do not support these design choices. It is not clear which novelties contribute most to the strong performance of BIT.

### Questions
1. For binding affinity prediction, did you consider measuring non-linear correlation, e.g. using the Spearman correlation coefficient? This evaluation metric could be better at showing which methods can correctly prioritize compounds with strong affinity.
2. Do you plan to publish the code for better reproducibility of your method?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The “General purpose pre-trained model…” paper proposes a Biomolecular Interaction Transformer BIT, which is to have a multi-modal training on molecules, together with protein—ligand matching, with 2-D and 3-D structures. The model includes a pre-training.

In my opinion, this is a valuable paper, presenting a well-defined model, together with well-designed experiments. The BIT model might not be revolutionary, but is a piece of a very solid work, and well performing. I opt for accepting this paper for the conference.

### Strengths
1. An advanced model, encompassing 2-D and 3-D structures for molecules, proteins, and ligand—protein interaction modelling, with multi-modal training. The model can be tuned.
2. Well-defined multi-modal representation learning employing a Transformer model (a Transformer-M model of Luo et al.) with independent tuning of proposed BIT for different knowledge domains.
3. A very good graphical abstract is given on page 2, showing in detail the proposed architecture. Clear presentation. All this increase the paper readability greatly.

### Weaknesses
1. Some generalization of the model to other areas would be welcome.


### Questions
1. In the comparison tables, the models (usually proposed BIT) with the best mean have values given in boldface. Are all the models trained on the same data-sets? For some predicted features, the differences between BIT and some other models are large, even though some of them are Transformers too. Are the optimal values for BIT the result of the proposed BIT architecture, the fine-tuning on different modes (the multi-modality), different data sets, better pre-training, or something other? The discussion on the comparison to other approaches is needed in the conclusions/discussion section.
2. Please correct the spelling of some words. Just as well, please correct the editing of mathematical expressions. E.g. in equations (1) and (2) the equal signs = should be aligned ;-)
3. Your paper and model is strictly molecule learning oriented. Do you think that the general approach can be used in other sciences? E.g. in biological experiments on cancerous cells and the impact of some sort of certain treatments, which would imply modifications in the course of the operation?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a general protein pre-training model, i.e., Biomolecular Interaction Transformer (BIT) to process molecules and pocket-ligand complexes in a unified style. Specifically, the main block of BIT is based on Transformer-M, a previous pre-training model. To enhance the model’s ability of capturing multi- and inter-domain relationships, authors further incorporate Mixture-of-Domain-Experts (MoDE), i.e., separate feed-forward layers, for fusing molecule and pocket information better. Experiment results show that BIT achieves state-of-the-art performance in various downstream tasks, including binding affinity prediction, virtual screening, and molecular property prediction.

### Strengths
- BIT shows great performance in all downstream tasks listed in the paper.
- BIT can handle molecules and protein pockets in a unified way.
- BIT can work well with both 2D and 3D molecules.

### Weaknesses
 - Contribution is minor. BIT combines the architecture of Transformer-M and Mixture-of-Domain-Experts technique, which both are from existing methods [1, 2, 3]. In addition, the way of combining the two is also a simple adaption. Specifically, the integration of MoDE appears to be a straightforward application of separate feed-forward networks, lacking a novel mechanism for domain-specific information fusion. The core idea of using separate experts for different domains, while effective, does not introduce a significant conceptual leap beyond existing mixture-of-experts approaches. In summary, I appreciate that authors provide a strong method but I also believe that the contribution of this paper is not enough for acceptance.
- Experiments are not convincing enough:
1) Authors did not provide ablation studies to directly show the effectiveness of the main components, e.g., MoDE, of BIT. It is unclear whether the performance gains are solely attributable to the increased model capacity from the additional parameters introduced by MoDE, or if there is a true benefit from domain-specific experts. A controlled experiment comparing a vanilla Transformer-M with an equivalent parameter increase from a larger FFN in the same Transformer-M architecture would be necessary to isolate the impact of MoDE.
2) The comparison between BIT and the main baseline, i.e., Transformer-M, may not be fair enough. As BIT adopts MoDE technique, it has more trainable parameters than the vanilla Transformer-M. Moreover, BIT uses not only small molecule data but also protein-ligand complex data in the pre-training stage, while Transformer-M only uses small molecule data. This difference in pre-training data and model capacity makes it difficult to ascertain if the performance improvements are due to the model architecture or these other factors.
3) The results of Transformer-M are not included in virtual screening and molecular property prediction benchmarks. This omission makes it difficult to assess the relative performance of BIT in these tasks, and to understand the extent to which the proposed method improves upon the baseline.
- Some important details are missing, e.g.,
1) In section 3.1, authors mentioned domain type embedding but without further description. It is unclear how these embeddings are generated and how they interact with other input representations.
2) Also in section 3.1, authors introduce two special nodes, i.e., [M_VNode] and [P_VNodes]. It is unclear how to build up the input representation with these two nodes. Specifically, it is unclear how these virtual nodes are connected to the actual atom nodes in the graph representation and how they influence the overall representation of the molecule or complex.
3) What is the specific value of noise scale controlling hyperparameter $\sigma$?

### Questions
- In section 3.3, why only add noise to molecules when doing pre-training?
- In section 3.4.1, Why not use [P_VNode] or the combination of [M_VNode] and [P_VNode] as the representation of protein-ligand complexes?
- In table 3, why the PCBA dataset is not included in the table?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
