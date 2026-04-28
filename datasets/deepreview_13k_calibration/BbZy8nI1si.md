# Learning Molecular Representation in a Cell

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 8, 6, 3

## Abstract
Predicting drug efficacy and safety \textit{in vivo} requires information on biological responses (e.g., cell morphology and gene expression) to small molecule perturbations. However, current molecular representation learning methods do not provide a comprehensive view of cell states under these perturbations and struggle to remove noise, hindering model generalization.
We introduce the \textbf{Info}rmation \textbf{Align}ment (InfoAlign) approach to learn molecular representations through the information bottleneck method in cells. We integrate molecules and cellular response data as nodes into a context graph, connecting them with weighted edges based on chemical, biological, and computational criteria.
For each molecule in a training batch, InfoAlign optimizes the encoder's latent representation with a minimality objective to discard redundant structural information. 
A sufficiency objective decodes the representation to align with different feature spaces from the molecule's neighborhood in the context graph.
We demonstrate that the proposed sufficiency objective for alignment is tighter than existing encoder-based contrastive methods. 
Empirically, we validate representations from InfoAlign in two downstream applications: molecular property prediction against up to 27 baseline methods across four datasets, plus zero-shot molecule-morphology matching.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a novel approach called Information Alignment (InfoAlign) for learning molecular representations by integrating molecular structure, cell morphology, and gene expression data. The method leverages the information bottleneck principle to optimize a molecular graph encoder and multiple MLP decoders, aiming to achieve minimal yet sufficient molecular representations.

The authors demonstrate the effectiveness of InfoAlign through extensive experiments on molecular property prediction and zero-shot molecule-morphology matching, showing superior performance compared to 27 baseline methods across four datasets.

I find the paper of good quality in general. Besides, the problem it is tackling is meaningful but less explored. I suggest an acceptance to advocate this direction.

### Strengths
- The approach is well-motivated. Applying information bottleneck to this problem for learning minimal yet sufficient molecular representations seems a valid match of theory and real-world problem.
- The approach is comprehensively evaluated by comparisons across different methods and even paradigms. InfoAlign demonstrates improved accuracy over up to 27 baseline models across four datasets.
- The paper is well-organized and clearly presented.
- In addition to empirical evidence, the paper provides theoretical proofs to support the advantages of the proposed method.
- The provided supplementary material contains code, dataset and checkpoints. This suggests good reproducibility of the results in the paper.

### Weaknesses
 - As I mentioned in the summary, the problem is meaningful yet less tackled in the AI community. To my eyes, it is mostly due to the missing prerequisites of biological knowledge. The paper provides some explanation of the problem in the introduction, but it would be much more helpful if more context could be provided (maybe in the appendix).
- Line 215: The motivation for computing edge weights on random walk paths is unclear, and no empirical evidence is provided to support it. Since the context graph incorporates data from three modalities, the edges likely exhibit strong heterogeneity. Is there evidence suggesting that a cumulative product of edge weights effectively captures dependency or similarity between nodes? The use of a cumulative product, specifically, needs more justification given that edges represent different types of relationships (e.g., structural similarity, gene expression correlation, morphological similarity) which may not be well-modeled by multiplication.
- Line 303: The approach for avoiding noisy edges in computations lacks motivation and an ablation study. Providing more detail here would offer valuable insights for researchers interested in extending InfoAlign to new contexts. The specific threshold used for edge removal is not justified, and it is unclear how sensitive the method is to this parameter. Furthermore, it's not clear how this threshold interacts with the edge weights computed earlier.

### Questions
- What are the minimum data requirements for cell morphology and gene expression to effectively apply InfoAlign? How does the method perform when these data are sparse or incomplete?
- Given the promising performance of structure-based pretrained GNNs, have the authors considered using representations from these pretrained models instead of Morgan fingerprints as molecular features? This might leverage the strengths of both approaches.
- How does the computational complexity of InfoAlign compare to existing methods, and what are the practical limitations in terms of dataset size and computational resources?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a method called InfoAlign for predicting molecular properties by integrating three different modalities: molecular structures, gene expression, and phenomics embeddings. To learn useful representations, they construct a weighted connected graph over cell morphology profiles, related molecules, and gene expression values. They train an encoder-decoder architecture where, for a molecule of interest, they encode its representation and decode both itself and all other nodes encountered during a random walk on a pre-specified graph. This approach results in mutual information maximization between the compound of interest $x_i$ and related entities discovered through the random walk on the pre-encoded graph. The authors test their method on a variety of chemical property prediction datasets, demonstrating that they outperform various baselines, including pre-trained Graph Neural Networks (GNNs), chemical language models, uni-modal models such as cell morphology or gene expression, and some multi-modal alignment models.

### Strengths
- The authors perform a comprehensive evaluation against baseline models across a variety of datasets.
- They convincingly demonstrate that including additional modalities improves performance, as evidenced by thorough evaluations and ablation studies.
- The incorporation of a graph is an interesting way to introduce prior knowledge into the learning representations for a particular molecule.

### Weaknesses
 - The validity and robustness of the pre-specified graph are not thoroughly explored. It would be informative to assess how sensitive the method is to the quality of the graph. For example, one experiment could involve removing 50% of valid connections and replacing them with random pairs of nodes; another could involve using a completely random graph. It is unclear if the graph edges are weighted, and if so, how these weights are determined, which could significantly impact the random walk and subsequent representation learning.
- The second gap identified by the authors is slightly misformulated: "They treat molecules as the sole connectors between gene expression and cell morphology, ignoring the potential for genetic perturbations."
    - Essentially, the authors are arguing that incorporating genetic perturbation data can further improve predictive capacity. However, there is no ablation study where this information is omitted to directly validate its impact on empirical performance. It is not clear if the genetic perturbation data is used as a node in the graph or if it is used to create edges between existing nodes. The specific mechanism of how genetic perturbation data is incorporated into the model is not well-defined.
- Regarding the ToxCast dataset, the authors report a performance of 0.72 ROC AUC using GROVER. Did the authors use a different partitioning of the dataset than previous works? It is crucial to specify the exact data splitting procedure to ensure reproducibility and allow for fair comparisons with other methods. The discrepancy in reported performance raises concerns about the comparability of the results.
- The ablation loss is only regarding removal of the losses as far as I understand the data itself is still input into the training. Can the authors perform an ablation where a full data modality is not added as part of training? It is unclear if the model is robust to the absence of a full modality, and the current ablation study does not address this concern. The model's reliance on each modality should be evaluated by removing the modality entirely from the input.

### Questions
- Are the authors surprised by the relatively minor drop in ROC AUC values when omitting individual modalities?
- Some additional relevant literature that could enhance the discussion includes:
    [0] Cross-Modal Graph Contrastive Learning with Cellular Images
    [1] How Molecules Impact Cells: Unlocking Contrastive PhenoMolecular Retrieval (a work evaluating zero-shot classification)
    [2] Approximating Mutual Information of High-Dimensional Variables Using Learned Representations (proposes a scalable approach for approximating mutual information of high-dimensional objects)
- One of the conclusions from the work is emphasizing the importance of molecular features. Dot he authors have an explanation for why the absence of molecular features in the ablation results in a ToxCast AUC that overlaps the non-ablated model performance? Without seeing the results I would expect the performance in the absence of an ablated molecular feature reconstruction loss to be a lot worse.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Thank you for a really interesting read, I agree that the most important next step in molecular representation is combining different modalities and current methods leave much to be desired, and I really liked the novel way shown here to combine data in a constricted way. It is well mathematically motivated and the work done clearly extensive. 

Summary:
* The authors present a new multi-domain method to learn the representation between drugs, genes and cells. In contrast to typical contrastive training setups the InfoAlign method removes the redundant information through a bottleneck using a well formulated mutual information method. 
* They show a method to create walks over the cellular context  graph representing the interactions between the modalities, and use this to populate the compute graph for their representation learning. 
* This representation framework uses Morgan fingerprints as molecular node features, CellProfiler features for the cell node features, and L1000 features for the gene node features, and the connections are based on chemical perturbations and cosine similarities. 
* The authors show results across a range of benchmarks, demonstrating good performance, achieving top ranking scores in all but 2 / 15 of the key datasets/criteria evaluated in Tables 1 and 2.

### Strengths
* The novel construction of the problem mitigates a significant issue with current implementations using a standard contrastive learning approach, by combining the modalities into a single method there is no decoupling between the different representations, and the MI approach to filter the data seems an effective way to reduce the data required to train over, potentially increasing data quality and improving time to train. 
* The visual presentation is good, with tables are figures clearly designed to convey meaning. 
* The breadth of models evaluated against gives a really clear status against both several standard approaches one might take, and also against SOTA prior work. This comparison is really nice to see.

### Weaknesses
 * Model clarity - I found it hard reading this paper to extract exactly how the model was constructed to run these experiments. The method is clearly novel, and an interesting approach to the multi-domain problem, but after being strongly theoretically motivated the method / implementation details, or even a description of model size was lacking. If these details could be expanded on it would help place the model / method in the appropriate context. 
* Impact of the MI bottleneck - The mutual information bottleneck is well theoretically motivated, however I didn’t feel the power of the bottleneck was evaluated in the paper? A different approach would be just using all the data and relying on data size / model size to outweigh data quality. I like the idea with MI, but would have liked to see an ablation with this feature included / not as that would help me evaluate the importance of the bottleneck vs the joined training setup?
* Impact of context graph - Similarly the impact of the context graph and different ways of including the context felt under-explored. Fig 4(b) I think shows that the random walk length had little impact, but how this is impacted by composition of the random walk path (are the walks just reconstructing the most likely combinations that would form a triplet anyway?) and what happens if instead of walking the relevant combinations are just grouped together. This feels like an important baseline. 
* The presentation of the research questions felt more like a report than a paper, I would have liked to see some more motivation / explanation of each rather than assuming knowledge on the readers part.

### Questions
Questions / suggestions:
* I would ask for some more clarity on the results presented in table 1, specifically for the Broad6k results. Many columns have a +/- 0 error on a reoccurring 3.1 result. I suspect this means that there are a few tasks that are always identified with a high AUC, but given the lack of discussion of these results it’s hard to interpret. It might be worth using a different set of thresholds for the Broad6K to get more resolution? 
* It would also help in section 6 for each of the research questions to have a couple of sentences explaining what each question is and why we are asking them, otherwise the results feel disjointed to the uninitiated reader and hard to connect. 
* I found the explanation of the exact model architecture / parameters used to be lacking, and while pointed in the main text to the appendix I did not find enough information there on the size of/ structure of the MLPs / training regime to feel like the result could be replicated. This is of particular importance in Table 1 where comparing to other methods I can only guess at things like parameter efficiency etc. 

* In general I feel like the weighting of the paper is very theoretical, no bad thing I really like the inclusion of the mutual information, but I wonder if more details could be moved to the appendix to free up more space for the experimental method, the model construction, and discussion of the results. In the current format of the paper I find a really interesting set of ideas, that I find very hard to understand how to weight the importance of / a method that I could follow to replicate certain components. 


Specific formatting suggestions:
* Fig. 3. I don’t really understand what this graph is conveying? The top bar shows the proportion of single representation tasks, but the bottom splits along the model types? I either need more detailed explanation, or maybe consider a better type of graph to convert this information?
* Table 3. (right) (This should be a separate figure - I understand it might make formatting harder but it is hard to reference) I personally don’t like these KDE type plots as they imply smooth functions from what is usually limited data, and make it almost impossible to draw quantified conclusions from, I would be much happier with a histogram if this is important information to convey. Additionally x-axis labels. 
* Fig 4 (a) - this plot is almost unreadable with the overlapping lines / y-scale, and the meaning I think is being conveyed with the LR spans such a number of magnitudes in range that I would rather see both more granularity and perhaps these results presented in a table? 
* Fig 4 (b) - I can guess what the plot means but without a key / description detailing elements like the error band (? 1 std dev I assume, based on what variation is unclear though), the points are connected, but given the discrete data this is misleading, and the huge discrepancy at length 8 suggests to me either the error band is under-estimating the variance, or there are properties of a random walk length 8 that are not discussed. Again this is a really interesting result as it's looking at the way that different parts of the compute graph contribute to the final result, but I'm left asking more questions with this figure than it answers. 
    * While I thin this statement on line 521 is correct, “we observe in Figure 4b that downstream performance on ChEMBL2K is relatively robust across a wide range of walk lengths.” The inclusion of this plot raises questions that are not answered.  
* On a similar point to Fig 4b, I would be very interested to see a description / plot of what the typical construction of the random walk graphs contain. 



Thank you again for a really interesting read, I like the approach with InfoAlign, and appreciate the large quantity of effort put into this work. 
I'd request a slight look again at the weighting of different sections in this paper, as I found it slightly unbalanced, and think as a reader I would find benefit from more detail in the method so I could reproduce if I wanted, and more detail in the discussion of the results to understand how to place the results in better context. i.e. which parts of the method are the most important.

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
4

### Summary
This article proposes a pre-training method where the authors utilize genes, cells, and molecular information as nodes, and construct a context graph using the interactive or similar relationships between different components as edges. The authors then extract paths on the graph using random walks to construct training data, design training objectives from the perspective of mutual information, and integrate cellular and genetic information into molecular representations. After pre-training, the authors fine-tune the model on downstream tasks across four datasets to validate its performance.

### Strengths
- This article pioneeringly incorporates cellular modality information in molecular representation learning, which enables the learned molecular representations to achieve better results in biochemistry-related tasks.
- The article conducts sufficient experiments to validate the effectiveness of the model.
- The paper is well-motivated; adding cellular modality data to enhance the model's performance in biochemical aspects is very reasonable.

### Weaknesses
 - The writing requires improvement; the methodology is difficult to follow, and many variables are not clearly defined. See Questions for details.
- The description of the dataset and downstream tasks is not sufficiently detailed, with some parts being confusing. See Questions for details.

- The paper focuses on molecular representations, but if such a representation cannot outperform the features obtained from full fine-tuning, then what is the significance of such a kind of representation? If you have collected so much multimodal data and constructed complex pre-training tasks, but they still cannot surpass the work of others that use single-modality pretraining plus full fine-tuning, then why go through all this trouble to collect this data? I only need to use single-modality pre-training plus full fine-tuning, which is more in line with Occam's Razor.
- Moreover, single-molecule data is easier to collect and more abundant than biological data, making it easier for people to scale up their models. So, if your method cannot defeat an approach that only uses molecular pre-training plus full fine-tuning, why would anyone choose to use your method, which lacks both scalability and performance?

- The supplementary experimental results in the authors' rebuttal have demonstrated that **full-finetuning can significantly enhance the performance of the baselines**. However, the paper **does not present the performance of fully finetuned baselines**. The presented performance of pretrained-GNNs is **substantially underestimated**. This means the paper lacks sufficient evidence to show that the proposed methods, which require more complex multi-modal data construction, demonstrate a clear advantage over simple single-molecule pretraining.
- Additionally, the supplementary experimental results indicate that after full finetuning, the proposed method only provides a **marginal performance improvement** on 3/4 of the datasets used in the paper compared to Uni-Mol, not to mention that Uni-Mol is not the most outstanding among all pretrained-GNNs. According to Occam's razor, which is agreed upon by both reviewers and authors, it is difficult to justify the necessity of the proposed complex multi-modal pretraining, especially when the collection of biological experimental data is much more challenging than that of single-molecule data.
- Even if the authors were to update the performance of all pretrained-GNNs, **nearly half of the experimental results would need to be modified**, and consequently, the experiment analysis would also require extensive revision. If the authors were to undertake such a large-scale rewrite of the paper, the review provided by the reviewer would no longer be applicable to this article, necessitating new reviewers and a new round of peer review, which would violate the ICLR submission process.

### Questions
- **Methodology**
  - How is the neighboring node of $x$ defined in line 250? Is it the neighbor of $x$ on the context graph or all the $v_i$ on the sampled path?
  - As shown in Fig. 2, different decoders are used to reconstruct the features of different types of nodes. However, if there are multiple neighbors $v_1, v_2, \ldots, v_n$ of a certain molecule $x$ sharing the same type, how can the decoder decode various $y_{v_i}$ from the same encoded latent  $z$ of $x$ without any additional information about $v_i$ being provided?

- **Experiments**
  - The ChEMBL dataset provides information on whether a certain molecule exhibits activity against a specific target. In this manuscript, a task is defined as predicting whether a molecule can interact with a given target. However, it is unclear why the molecule would be characterized by **Cell Morphology** and **Gene Expression**. Such information should be related to the task (target) itself rather than the input molecule. Could the authors explain how **Gene Expression** and **Cell Morphology** data are generated for molecules?
  - To substantiate the claim that the proposed multimodal alignment method more effectively models molecular properties within a cellular context, the authors must include a baseline comparison using a simple concatenation approach for alignment. Specifically, the authors should employ a pretrained GNN, such as Uni-Mol[1], to extract molecular features and concatenate them with Cell Morphology and Gene Expression representations as inputs for prediction tasks on the ChEMBL2k and Broad6k datasets.
  - During the fine-tuning for downstream tasks, is the encoder frozen or is a full-fine-tune performed with the encoder also being trained?

**If the authors can address all my major concerns, I would be pleased to raise the score.**

[1] Zhou G, Gao Z, Ding Q, et al. Uni-mol: A universal 3d molecular representation learning framework[J]. 2023.

### Soundness
3

### Presentation
2

### Contribution
3
