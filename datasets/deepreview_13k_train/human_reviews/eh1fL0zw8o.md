# Large Language and Protein Assistant for Protein-Protein Interactions prediction

- Decision: Reject
- Scores: 5, 6, 5, 8

## Abstract
Predicting the types and affinities of protein-protein interactions (PPIs) is crucial for understanding biological processes and discovering macromolecular drugs. While encoding proteins themselves is essential, PPI networks can also provide rich prior knowledge for these predictive tasks. However, existing methods oversimplify the problem of PPI prediction in a semi-supervised manner when utilizing PPI networks, limiting their practical application. Furthermore, how to effectively use the rich prior knowledge of PPI networks for novel proteins not present in the network remains an unexplored issue. Additionally, due to inflexible architectures, existing methods cannot handle complexes containing an arbitrary number of proteins. To overcome these limitations, we introduce LLaPA (Large Language and Protein Assistant), a multimodal large language model that integrates proteins and PPI networks. LLaPA offers a more rational approach to utilizing PPI networks for PPI prediction and can fully exploit the information of PPI networks for unseen proteins. Through natural language instructions, LLaPA can accept any number of protein sequences and has the potential to perform various protein tasks. Experiments show that LLaPA achieves state-of-the-art performance in multi-label PPI type prediction and is capable of predicting the binding affinity between multiple interacting proteins based on sequence data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces LLaPA, a multimodal large language model that integrates PPI networks as external knowledge to predict protein-protein interactions and affinity.

### Strengths
1. **Writing**. The writing is mostly clear and easy to follow.
2. **Significance**. Predicting protein-protein interactions and affinity is an important problem in biology and medicine. Comparing models in a realistic setting is a good practice.

### Weaknesses
1. **Potential major error in chemistry facts**. The Multi-sequence Affinity Prediction is theoretically not a well-defined task. For antibody chains H+L and antigen chain A, the antibody-antigen binding affinity (the usually measured one) is defined by $K_\text{D} = \frac{[\text{HL}][\text{A}]}{[\text{HLA}]}$, i.e. between the entity HL (the antibody) and A (the antigen). Usually, for a set of chains, a single affinity value does not exist; rather, it is dependent on the choice of two binding partners. The paper does not clearly define which binding partners are used to define the affinity, leading to ambiguity in the task definition. For example, if there are three chains A, B, and C, the affinity between A and B might be different from the affinity between A and C, or the affinity between the complex AB and C. The paper needs to clarify this point.
2. **Unclear function of LLM**. The LLM in this paper acts as a vessel to integrate the PPI network and the protein embedding. Since the tasks you study are closed-domain (i.e. no open answer needed), you could theoretically replace it with a smaller network, e.g. Graph Transformer, that inputs the target proteins and their related PPI graph embeddings (the cosine similarity between the target protein and the related protein on the PPI graph can be incorporated into this graph embedding), and outputs the mPPI logits or logKd values. It is unclear how much benefit the LLM brings to the task. The current implementation does not provide a clear justification for using a large language model, especially given the computational overhead. A smaller, task-specific model might achieve comparable or even better performance with significantly less computational cost. The paper should provide a more detailed analysis of the LLM's contribution beyond simply acting as an information aggregator.
3. **Unfair comparison**. In the main text, the authors present results for the "/R" models where the test edges are removed. As these models are trained on the PPI graph, it is to be expected that the "/R" models will underperform significantly due to a significant gap in training and test settings. Outperforming these nerfed models is not a convincing achievement of LLaPA. The removal of test edges during training creates an unrealistic scenario where the model is not exposed to crucial interaction information, making the comparison with LLaPA less meaningful. This setup unfairly penalizes graph-based methods and does not accurately reflect their potential performance in a more realistic setting.

### Questions
1. Regarding weakness #2, could you provide more theoretical or emperical evidence to justify the benefit of LLM?
2. Regarding weakness #3, if removing test edges makes the graph structure useless, the authors should add one or more PPI-graph-free baselines for comparison, e.g. ESM2/3 or SaProt. The protein encoders can be directly trained on the train edges and tested on the test edges.

### Soundness
2

### Presentation
3

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
In this paper, the authors proposed a novel method LLaPA (Large Language and Protein Assistant), which integrate protein sequences and PPI networks to improve the protein-protein interaction prediction. The two-stage training strategy enables the model to project the sequence and network information within the LLM representation space. Moreover, the LLaPA can predict the interaction among flexible number of proteins. Extensive experimental results have verified the effectiveness of LLaPA.

### Strengths
1.	The authors offer a rational multimodal LLM for protein-protein interaction prediction. In addition, the method can accept more than two proteins to infer the potential relationship among them. It overcomes the evaluation issues present in previous work, demonstrating greater generalizability. 

2.	The authors propose a novel knowledge injection method by treating the PPI network as external knowledge and integrating it into the large language model. This approach effectively leverages information from the PPI network, showing promising performance, especially in the prediction of unknown proteins.

3.	It achieved the SOTA performance on the mPPI task and demonstrates significant accuracy in multi-sequence affinity prediction.

### Weaknesses
1.	A comparison with some large model-based methods is lacking.

2.	Although the SHS27k and SHS148k datasets are widely used, adding other real biological datasets, such as protein interaction data from different species, would make the experimental results more generalizable and convincing.

3.	The experiments on MA prediction lack persuasiveness and need to be tested on a larger dataset.

4.	The authors used cosine similarity of protein features, but did not consider sequence alignment scores and structural similarity.

5.	For the training step 1, the authors pretrained the model on UniprotQA. There is a potential for data leakage in this method.

6.	For MA prediction, the authors require the model to directly generate logKd scores. In this setup, the model is likely to mimic training data rather than output genuine scores. The poor performance of Group 6 may be due to its significant divergence from the training data distribution, and analysis shows that the model generated two instances of 7.52 for this group, which could be a high-frequency value in the training data. 

7.	The authors have constructed UPPIN by merging STRING, PDBBind, and SAbDab. As the authors state, the STRING contains different types of interactions between proteins, and the other two databases have edges of different types from it, how do the authors handle this here? Could this lead to an inconsistency in the information of the edges in UPPIN, causing the graph encoder to fail?

8.	There are over 59 million proteins in the latest release of STRING, so why were only 15,202 proteins considered? And the type of edges in STRING doesn't match with what is mentioned in the article, could the authors please explain it?

9.	In LLM loss (L_LLM), P(*|*;p) should be P(*|*;Q,p).

### Questions
1.	Please describe in detail why the training is divided into two phases, and why there is a need for the first phase. It is suggested that the authors could add an experiment to illustrate the need of the first training phase.

2.    In the prompt, the authors included text representations of the protein sequences and indexes. Please demonstrate the reason.

3.   For training, there are 2 L_LLM. Please demonstrate their difference.

4.   Why do the authors use SGC as graph encoder? What happens if you use gnn like GNN-PPI, e.g. GCN to encode networks? Compared to SGC, it seems like GCN just have one extra step of using a nonlinear activation function.

5.   For the similarity of proteins, the authors used the cosine similarity between protein features. Why not consider sequence alignment scores and structural similarity? Please conduct additional experiments as a supplement.

6.   For the training step 1, the authors pretrained the model on UniprotQA. Is there a possibility of data leakage in this method?

7.  For MA prediction, the authors require the model to directly generate logKd scores. In this setup, the model is likely to mimic training data rather than output genuine scores. The poor performance of Group 6 may be due to its significant divergence from the training data distribution, and analysis shows that the model generated two instances of 7.52 for this group, which could be a high-frequency value in the training data. 

8.  The authors have constructed UPPIN by merging STRING, PDBBind, and SAbDab. As the authors state, the STRING contains different types of interactions between proteins, and the other two databases have edges of different types from it, how do the authors handle this here? Could this lead to an inconsistency in the information of the edges in UPPIN, causing the graph encoder to fail?

9. There are over 59 million proteins in the latest release of STRING, so why were only 15,202 proteins considered? And the type of edges in STRING doesn't match with what is mentioned in the article, could the authors please explain it?

10.	In LLM loss (L_LLM), P(*|*;p) should be P(*|*;Q,p).

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
4

### Summary
This paper presents LLaPA (Large Language and Protein Assistant), a multimodal language model aimed at predicting protein-protein interactions (PPIs). Unlike prior graph-based and sequence-based models, which oversimplify PPI networks or struggle with unseen proteins and multi-protein complexes, LLaPA incorporates PPI networks as external knowledge, integrating protein and network data through Retrieval-Augmented Generation (RAG). LLaPA's flexible input allows it to handle varying protein numbers and conduct multiple protein tasks, showing good results in multi-label PPI type prediction and multi-sequence affinity prediction.

### Strengths
S1. **Multi-modality Input Handling**: The use of RAG integrates both graph, language, and protein information into the input. 

S2. **Good Results**: LLaPA outperforms the explored baselines in PPI type prediction, demonstrating robustness in complex PPI settings and validation tasks.

### Weaknesses
W1. **Lack of Comparative Discussion and Limited Contribution**: The most critical issue of the paper is that it ignores relevant protein LLM works which obviously can address the proposed challenges, i.e. relying on structural input and handling multiple protein input. To illustrate, ProtLLM should be discussed and compared. It models a joint space of protein and language, which directly addresses the proposed challenges. Also, there is another work ProLLaMA that does the similar thing. These two works are neither discussed in related work nor are they compared in the experiments.

W2. **Insufficient Benchmarking**: The experiments lack baselines based on protein language models. Specifically, as noted in the original ESM paper, embeddings for protein complexes can be obtained by concatenating the protein chains as input. Given that LLaPA uses ESM embeddings, fine-tuning ESM2 with concatenated inputs is an essential baseline. Additionally, comparisons with ProteinLLM baselines, such as those mentioned in W1, should also be included for a more comprehensive evaluation.

W3. **Redundant Challenges**: Challenges 1 and 2 overlap, both emphasizing issues in graph-based inference at test phase, reducing clarity in presenting the model’s motivation.

### Questions
NA

### Soundness
3

### Presentation
3

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
The authors propose LLaPA, a multimodal model for predicting protein-protein interactions (PPI) and the binding affinity of protein complexes with a variable number of proteins. Their main contributions are 1) characterization of the performance drop of existing methods using PPI network information when topological information on the test set is restricted, 2) handling PPI networks as external knowledge that can be provided to an LLM via retrieval augmented generation, 3) a large, general PPI network called UPPIN that combines the information from three smaller datasets, and 4) a multimodal approach which incorporates protein features, graph features, and natural language text-based instructions. The authors both compare LLaPA's ability to predict multi-label PPI types to existing methods and evaluate LLaPA's capability to predict multi-sequence binding affinity. LLaPA achieves strong performance, and the authors perform ablation experiments and use multiple baselines.

### Strengths
1. The paper is written very clearly and does a good job identifying limitations in existing approaches.
2. There is a strong focus on making LLaPa practical for plausible real-world scenarios, where, for example, a protein sequence that is not a member of an existing PPI network is seen or the goal is to predict the binding affinity on a complex with more than 2 proteins
3. The authors address a major issue of data leakage in protein ML benchmarks, where overlaps between training and test data can inflate performance metrics. To ensure robust evaluation, they completely remove any edges that overlap between the PPI network in the training set and the test set. This approach contrasts with prior evaluations, where such overlaps were not consistently removed, and the authors demonstrate how performances differ for existing methods under this stricter evaluation.
4. The authors clearly demonstrate the effect of using LLaPA to predict multi-sequence binding affinity against the baselines they implement (E(2), E(3), and E(4)), especially since no prior baseline for the 3 and 4 sequences cases existed.
5. The demonstrated performance increase for multi-label PPI class prediction (for DFS and BFS especially) is very strong
6. LLaPA performs pretty well and very stably for various numbers of unique proteins per complex, and the authors investigate the single case where there is unexpectedly high error, providing a plausible explanation for this behavior

### Weaknesses
I would appreciate additional details for RAG prompt preparation (addressed in more details in the Questions section), but my primary concern with the paper is that of data leakage for the evaluation:

The authors take steps to ensure that an "unseen protein" is actually unseen with respect to the PPI network (UPPIN), but this doesn't mean that the sequence is unseen with respect to the entire model. Ideally, a protein in the test set should not be seen by any component of the model until inference.
- I understand that this may be difficult and impractical to enforce with large pre-trained protein language models like ESM-2, but it is worth nothing that if ESM-2 has seen two closely related homologs X and Y during training, and LLaPA sees X with additional graph and annotation information (from UniProtQA), then if LLaPA sees sequence Y during inference, high performance can be achieved by simply copying the annotations/predictions for X.
- In the first step of training, the protein projector is trained using UniProtQA, which has function, name, family, and sub-cellular location information about ~600K proteins. I imagine that significant leakage could occur here if there is overlap between the test sets and UniProtQA, since these pieces of information can be very relevant to determining protein complex membership.

These issues of "leakage" may also impact the comparisons against existing methods, which depending on how they are trained, may not have access to all of this information. At the very least, I think it would be worth adding some information about the degree of overlap between UniProtQA and the test sets. It may also be worthwhile to evaluate on a subset of train that is separated from the sequences in UniProtQA by some percent identity threshold at the sequence level.

These may be difficult things to address and should probably be mentioned in the limitations at least.

### Questions
1. In Section 3.4 lines 258-260, it is mentioned that the cosine similarity between protein embedding are used to retrieve the most similar proteins in the PPI network. What are the retrieval criteria exactly? Is there a score-based threshold or maybe a limit on the number of similar proteins that can be retrieved? 
- There are several works that address predicting sequence similarity/homology at the sequence level using ESM-2 and cosine similarity. It may be worth checking out PLMSearch (Liu et al; 2024) as one example of this. 
- Additionally, it may be worth checking out other protein database sequence similarity search tools like HMMER (Accelerated profile HMM searches (Eddy; 2011)), since UPINN only contains ~30K unique sequences. This would be very fast (probably faster than doing comparing the unseen sequence to all nodes in the graph) and could be used to provide more fine-grained control over which sequences are returned (considering where within a sequence matching regions are identified or the domain architecture of a returned sequence).

2. For multi-sequence affinity prediction, why is the sequence number determined by the number of unique sequences? Is is something to do with the the way the prompt is formulated for the LLM? It would be interesting to call sequence number based on the total number of sequences rather than the number of unique sequences, and it may result in a performance boost for LLaPA.

### Soundness
3

### Presentation
3

### Contribution
3
