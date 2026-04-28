# KW-Design: Pushing the Limit of Protein Design via Knowledge Refinement

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Recent studies have shown competitive performance in protein inverse folding, while most of them disregard the importance of predictive confidence, fail to cover the vast protein space, and do not incorporate common protein knowledge. Given the great success of pretrained models on diverse protein-related tasks and the fact that recovery is highly correlated with confidence, we wonder whether this knowledge can push the limits of protein design further. As a solution, we propose a knowledge-aware module that refines low-quality residues. We also introduce a memory-retrieval mechanism to save more than 50\% of the training time. We extensively evaluate our proposed method on the CATH, TS50, TS500, and PDB datasets and our results show that our KW-Design method outperforms the previous PiFold method by approximately 9\% on the CATH dataset. KW-Design is the first method that achieves 60+\% recovery on all these benchmarks. We also provide additional analysis to demonstrate the effectiveness of our proposed method. The code is publicly available via \href{https://github.com/A4Bio/ProteinInvBench}{GitHub}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a refining method, called KW-design, to refine the generated protein sequences from previous methods, such as PiFold. In specific, KW-design is an iterative process that uses pretrained sequence and structure models to extract multi-modal features and a confidence-aware gated layer to fuse these features. It also applies a memory retrieval mechanism to save the training time.

### Strengths
- The idea of iteratively refining generated sequences from protein structures based on a confidence-aware gated fusion layer that fuses features from multi-modal feature extractors looks novel to me. 
- Experiments across multiple datasets show the effectiveness of the proposed method. 
- Ablation studies are well conducted to show the impact of main components.

### Weaknesses
My main concern is on the clarification of the paper. I feel like a large revision is needed to make the presentation more clear to the readers. 
- The method section is not very clear. In particular, Section 3.2 and 3.3 have a large portion of redundancy. For instance, the explanation of the "Knowledge extractor & Confidence predictor" in Section 3.3 seems to largely repeat the content presented in "Virtual MSA" in Section 3.2. I suggest that the “Fuse layer” could be merged into “Virtual MSA” to improve the conciseness of the presentation. Furthermore, the relationship between Eq (13) and Eqs (8) and (9) is unclear. While they all seem to describe the process of updating embeddings, it is not evident how “PiGNN” processes $e^{(l)}$ to ensure that Eq. (13) is consistent with Eqs (8) and (9). A more detailed explanation of the data flow and the role of PiGNN in transforming $e^{(l)}$ to $h^{(l+1)}$ is needed.
- In “Confidence-aware updating”, the rationale behind using two separate MLPs to process the same input, albeit with opposite signs, for the gate calculations is not adequately justified. A more thorough explanation of the necessity and functionality of these MLPs is required. Additionally, providing a justification for the specific formulation of Eq. (11) would be beneficial.
- In Algorithm 1, the process for determining the optimal $\phi^{(l)}$ and the application of the “patience of 5” are not clearly defined. A more detailed explanation of how the optimal parameters are identified and how the patience mechanism is implemented during the training process would enhance the clarity of the algorithm. Also, in line 12 (Algorithm 1), the meaning of $n$ in $h_n^{(l+1)}$ is unclear.
- I wonder why not split Table 1 into two subtables: one for CATH 4.2 and another for CATH 4.3? This would improve readability and allow for a more direct comparison of results within each dataset.
- In Table 2, the meaning of the “Worst” metric is not defined. Additionally, it is concerning that the proposed method performs worse than all other methods on this metric. A clear definition of this metric and a discussion of the potential reasons for the observed underperformance are necessary.
- Minor typo issue. “settings Specifically” -> “settings. Specifically” on page 6. “3d CNN” -> “3D CNN” on page 3.

### Questions
See my comments in the above.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces KW-Design, a novel method for protein design that iteratively refines low-confidence residues using knowledge extracted from pretrained models. The approach incorporates a multimodal fusion module, virtual MSA, recycling technologies, and a memory-retrieval mechanism to enhance performance and efficiency. The method demonstrates substantial improvements across various benchmarks, achieving over 60% recovery on datasets such as CATH4.2, CATH4.3, TS50, TS500, and PDB.

### Strengths
1. The paper is well written and exhibits a clear and logical structure.
2. The proposed method effectively leverages the knowledge from pretrained protein sequence/structure models, resulting in notable benefits for protein sequence design.
3. The paper includes a thorough ablation study, examining different components of the models such as recycling, virtual MSA numbers, and the pretrained model. This is crucial for gaining a deep understanding of the proposed methodology.

### Weaknesses
1. The code associated with the paper is currently unavailable.
2. Given that the model relies on pretrained models, some of which have been trained on the test set utilized, there is a potential risk of data leakage. This is a significant concern, as it could artificially inflate the reported performance metrics. The authors should provide a more detailed analysis of the training data used for the pretrained models and how they overlap with the test datasets used in this study. A rigorous evaluation of the impact of this overlap on the results is necessary.
3. The paper predominantly employs perplexity and recovery as metrics for evaluating the designed sequences. However, there is a chance that the designed proteins may not be soluble or may not fold correctly to the given backbone. It would be beneficial for the authors to incorporate additional metrics (e.g., scTM score, solubility) in their evaluation. The lack of experimental validation also limits the practical impact of the findings.

### Questions
1. Is there any fine-tuning done on the pretrained language model used in your approach?
2. In Section 4.3, Table 3 claims that “the predictive confidence score, an unsupervised metric, exhibits a strong correlation with recovery.” Could the authors provide a more detailed analysis, perhaps including the Spearman correlation between these two values?
3. Regarding the virtual MSA, does the sequence order affect the resulting residue embedding? If not, what criteria are used to determine the sequence order?
4. In Section 3.3, the initial node and edge features are extracted using PiFold. Is PiFold fine-tuned or kept fixed during this process?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper addresses the 'inverse protein folding'  problem of designing a protein sequence that folds into a particular shape. They achieve strong results on standard benchmarks.  It draws on a number of interesting ideas, from graph neural networks to leveraging embeddings of pretraining language models, to a 'recycling' approach that updates predictions based on the current uncertainty over those predictions.

### Strengths
The paper achieves really strong empirical results on a panel of common benchmarking setups. The results will definitely be of interest to the community.

### Weaknesses
The paper's explanation of the model is extremely difficult to understand because it is not using standard terms for deep neural networks. For example, 'knowledge' is used in a vague way, I guess, to mean leveraging pretraining? If I understand correctly, the composition of functions in section 3.1 is just describing a multi-layer neural network, but uses very verbose and non-standard notation. Further, why are the layers trained in a stagewise fashion in section 3.4 instead of standard back-propagation? It was confusing to me why you chose this, since it is much more complex to implement. Does it provide better performance?

The paper's experiments are quite careful about train-test splits, using a number of clustering-based splits that are well-established in the literature. I'm concerned about data leakage, however, from the pretrained language models used to help guide predictions for low-confidence residues in the 'knowledge' module. There models were trained across vast numbers of proteins and likely do not follow the same train-test splits as for the structure -> sequence benchmarks. As a result. The exact target sequence for structure -> sequence design may have appeared in the LM pretraining data. This may explain why the paper's method is able to increase the per-residue recovery rate so dramatically. The paper also mentions that the ESM-IF train-test split is not compatible with some of the other benchmarking setups, yet ESM-IF embeddings are used here.

### Questions
Can you please clarify my questions regarding train-test splits and data leakage from the 'knowledge' module?

Can you please explain why you use such a non-standard training procedure?

I have raised my score to weak accept. We had an extensive back and forth regarding train-test splits and I appreciate the attention that the authors have devoted to this important topic.


==Comments after author's response==
My principal concerns about the paper were (1) data leakage and (2) the unconventional presentation of a multi-layer neural network architecture and stagewise training procedure.

Regarding (1), the overall challenge with this research field is that the primary application of inverse folding models is to find sequences that fold into de-novo designed protein structures. However, to validate models on offline natural data, the sequence-structure pairs in the test set aren't de-novo, particularly if they were seen in pretraining. The authors created a new test set at my request, which is small, but establishes good community standards for how to think about  these issues in the future.

Regarding (2), please update the paper to use more standard terminology for a multi-layer model. When describing the stagewise training procedure, please make it clear in updated versions of the manuscript that this was done for computational reasons, and the superiority of it in terms of achieving a better model is not evaluated empirically.

Finally, note that in future work an alternative to your stagewise training approach would be to use gradient checkpointing, which reduces memory overhead (at the expense of additional forward passes).

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
