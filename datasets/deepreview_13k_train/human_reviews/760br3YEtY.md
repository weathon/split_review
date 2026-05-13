# ($\texttt{PEEP}$) $\textbf{P}$redicting $\textbf{E}$nzym$\textbf{e}$ $\textbf{P}$romiscuity with its Molecule Mate – an Attentive Metric Learning Solution

- Decision: Reject
- Scores: 6, 6, 5, 6, 5

## Abstract
Annotating the functions of proteins (e.g., enzymes) is a fundamental challenge, due to their diverse functionalities and rapidly increased number of protein sequences in databases. Traditional approaches have limited capability and suffer from false positive predictions. Recent machine learning (ML) methods reach satisfactory prediction accuracy but still fail to generalize, especially for less-studied proteins and those with previously uncharacterized functions or promiscuity. To address these pain points, we propose a novel ML algorithm, PEEP, to predict enzyme promiscuity, which integrates biology priors of protein functionality to regularize the model learning. To be specific, at the input level, PEEP fuses the corresponding molecule into protein embeddings to gain their reaction information; at the model level, a tailored self-attention is leveraged to capture importance residues which we found are aligned with the active site in protein pocket structure; at the objective level, we embed functionality label hierarchy into metric learning objectives by imposing larger distance margin between proteins that have less functionality in common. PEEP is extensively validated on three public benchmarks, achieving up to 4.6%,3.1%,3.7% improvements on F-1 scores compared to existing methods. Moreover, it demonstrates impressive generalization to unseen protein sequences with unseen functionalities. Codes are included in the supplement.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes PEEP, a metric learning framework for protein functionality. The framework uses established techniques, such as ESM2 embeddings and Momentum Contrast as the backbone of the model. On top of these, the paper applies three types of algorithmic insights: using the ligands as additional information, leveraging a self-attentive mechanism to identify key residues, and a modified objective focused on the hierarchy of EC labels. PEEP outperforms relevant baselines on Price-149, New-392 and CATH and ablation studies show the relevance of the proposed changes.

### Strengths
The paper is well written and motivated. The final architecture is backed by good empirical performance, and ablation studies are thorough, providing necessary insight into the importance of the proposed modifications.

### Weaknesses
I encourage the authors to revise the writing in "To meet the goal, we customize a self-attention mechanism (Figure 1, c) to model the residue importance within protein sequences” as it currently reads as though the self-attention mechanism is newly-proposed, while it seems to be a standard setup.

While the paper is well-motivated, it seems that a significant part of it studies how some well-known techniques fit together in the context of the chosen task. The lack of novelty hinders from a higher rating at the moment unfortunately.

### Questions
In the paper, it is stated that "PEEP randomly samples one from the ligands’ SMILE embedding and integrates it with the protein’s sequence representation”. It would be useful to provide additional information on the distribution of ligands per protein and the sensitivity of the random choice with respect to the results.

Moreover, in 3.3, two methods are described for doing the fusion — how does the performance compare/which one is used?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors focus on the problem of predicting an enzyme's function given it's amino acid sequence, with a focus on situations where the sequence is quite remote from any enzyme with known function or where we seek to make predictions for a novel enzyme function that had not previously appeared in the training data. They use a number of techniques for improving models, such as triple-loss-based contrastive learning, using pre-trained protein and small molecule embeddings, a loss function that accounts for the label hierarchy, and an attention-based pooling technique.

### Strengths
The intro/background is accessible, comprehensive, and well written.

The problem that the paper approaches is important for the life science community and the paper achieves reasonable performance improvements.

The authors are careful to construct train-test splits that probe a model's ability to do meaningful extrapolation, both in terms of protein sequence and protein function.

The paper provides a significant number of ablations probing the impact of various design choices.

### Weaknesses
Despite the paper's title, it doesn't really model enzyme promiscuity, just enzyme function. Promiscuity is the tendency of an enzyme to accept many substrates. There is no evaluation setup that focuses on enzymes with annotated activity on multiple substrates. In part this is because Swissprot, the training data, only contains annotations for enzymes' natural function, while there are many other reactions that these enzymes could catalyze in the lab.

The paper boasts about incorporating 'biology priors', but the actual solutions aren't particularly novel or biology-specific. For example, the authors use a learned attention head to pool per-residue embeddings into a per-sequence embedding. The motivation about attention as focusing on active site residues is tenuous and post-hoc. Attention-based pooling is common these days. Similarly, another 'biology' detail is that the labels are hierarchical in nature, and the loss function is adjusted such that the similarity of 2 proteins' embeddings reflects the degree of their similarity in terms of the hierarchy of function. There's nothing biology-specific about training models with hierarchical labels.

It's unclear if the benchmarking setup is fair to baseline models. See below.

I'm confused by the comparison to baseline models. When you compare to proteinfer, for example, do you retrain it on the same train-test split as your model? If not, how is the comparison fair?

I'm confused by the motivation for changing the clustering threshold for de-duplicating the training data. To me, the key quantity when assessing the difficulty of an extrapolation task is the distance between evaluation examples and training examples. How does this distance change as you vary the training threshold?

Can you elaborate on the concept of 'promiscuity'? In what sense are you tackling the promiscuity problem?

I was confused by the statement in the intro that 'only 570K (∼ 0.3%) sequences have been manually annotated with computational methods that bridge the sequence-annotation gap.' Surely there are far more sequences in uniprot with computationally-derived functional annotations. Do you mean that there are 570K sequences with human-curated annotations (i.e., Swissprot)?

I found fig 4 unsatisfactory, since the distributions seem to overlap so much. Is there a way to quantitatively evaluate this separation, such as a precision/recall/f1 for classifying residues as occurring in the active site?

### Questions
I'm confused by the comparison to baseline models. When you compare to proteinfer, for example, do you retrain it on the same train-test split as your model? If not, how is the comparison fair?

I'm confused by the motivation for changing the clustering threshold for de-duplicating the training data. To me, the key quantity when assessing the difficulty of an extrapolation task is the distance between evaluation examples and training examples. How does this distance change as you vary the training threshold? 

Can you elaborate on the concept of 'promiscuity'? In what sense are you tackling the promiscuity problem?

I was confused by the statement in the intro that 'only 570K (∼ 0.3%) sequences have been manually annotated with computational methods that bridge the sequence-annotation gap.' Surely there are far more sequences in uniprot with computationally-derived functional annotations. Do you mean that there are 570K sequences with human-curated annotations (i.e., Swissprot)? 

I found fig 4 unsatisfactory, since the distributions seem to overlap so much. Is there a way to quantitatively evaluate this separation, such as a precision/recall/f1 for classifying residues as occurring in the active site?

==Update after authors' response==
Thank you for clarifying so many of my questions. Many of my concerns regarding technical soundness have been addressed. However, I continue to feel that the methodological novelty of the paper is lower than many ICLR papers. Of course, there are accepted papers that have low novelty, but they typically introduce new tasks, datasets, or provide interesting extensions of methods.  I have raised my score to 'weak accept', but acknowledge that the paper is truly borderline and unfortunately may not get accepted due to the space constraints at ICLR.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a ML algorithm, PEEP, to predict the function of enzymes.  The method integrates three different aspects into its pipeline: 1) It utilizes the EC number hierarchy to define different levels of similarity. 2) It uses self-attention to capture residues at the active pockets in binding to ligands. 3) It fuses the information of a protein’s ligands (their SMILES representation) with its own sequence representation by traversing the substrates and the products involved in different reactions. The method is validated on three public benchmarks and shows performance improvements in F-1 scores. It also generalizes to unseen protein sequences with unseen functionalities.

### Strengths
The authors demonstrate deep domain knowledge to find three different aspects in protein structure prediction that can be added to improve performance.

Detailed experimental studies have been carried out with all different kinds of optimizations, attention mechanisms, and regularizations.

Ablation studies demonstrate that all three factors are needed to improve prediction. However, it is interesting that the performance becomes worse by adding EC metric netween the 4th and 5th rows of Table 2.

### Weaknesses
The ideas do not seem to be that novel. The methods make use of the available data in interesting ways but there is limited ML innovation. 

It is difficult to understand the significance of the performance improvement, especially when all the values are so low (e.g., on the CATH dataset).

### Questions
Please refer to the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on a specific bioinformatic problem, named function annotation of proteins. Previous studies like CLEAN have achieved good performance, yet they also suffer from generation ability. To achieve this problem, this paper proposes a novel metric learning method. First, at the input level, SMILE representation is used to preserve the prior of proteins. At the objective, they propose a
metric learning objective that captures the hierarchical nature of EC numbers to appropriately weight
dissimilarity at each EC level. Three datasets and extensive experiments have varified the effectiveness of the proposed method.

### Strengths
1. The proposed metric-based method seems simple but effective, the fusion of prior information in function annotation is an interesting idea.

2. The strong performance when given a few training data and strong generalization ability.

3. The detailed ablation experiments verified the modules on the Price dataset.

### Weaknesses
1. The paper might lack key explanations, such as references to EC in the second paragraph.

2. The differences between the CLEAN method and the proposed method need further discussion. I did not see a concrete motivation for CLEAN.

### Questions
How to use the transformer layer to achieve "facilitate learning functional residues associated with an enzyme function"?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel ML algorithm, PEEP, to predict enzyme promiscuity, which integrates biology priors of protein functionality to regularize the model learning.

### Strengths
1) This work introduces PEEP, a metric learning method, designed to identify promiscuous enzymes that can be utilized in subsequent protein engineering processes.

2)  OThe PEEP framework integrates biology-aware designs to enhance the learning of protein functionality. (1) the integration of cognate ligands' embeddings ; (2) the incorporation of an attentive module to identify crucial residues for protein functionality; and (3) the introduction of an EC-aware training objective to bolster the metric learning capability.

3) code and dataset are available.

### Weaknesses
1. The technique contribution of this work is not very high since it mainly use MoCo in the protein domain.It also mixes up some biological efforts to improve performance.

2. In the experiments, the dataset may be very small. e.g., very small number of proteins.

### Questions
1. The technique contribution of this work is not very high since it mainly use MoCo in the protein domain.It also mixes up some biological efforts to improve performance.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
