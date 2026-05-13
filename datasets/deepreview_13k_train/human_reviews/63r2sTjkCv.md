# KinDEL: DNA-Encoded Library Dataset for Kinase Inhibitors

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
DNA-Encoded Libraries (DEL) are combinatorial small molecule libraries that offer an efficient way to characterize diverse chemical spaces. Selection experiments using DELs are pivotal to drug discovery efforts, enabling high-throughput screens for hit finding. However, limited availability of public DEL datasets hinders the advancement of computational techniques designed to utilize such data. To bridge this gap, we present \textbf{KinDEL}, one of the first large, publicly available DEL datasets on two kinases: Mitogen-Activated Protein Kinase 14 (MAPK14) and Discoidin Domain Receptor Tyrosine Kinase 1 (DDR1). Interest in this data modality is growing due to its ability to generate extensive supervised chemical data that densely samples around select molecular structures. Demonstrating one such application of the data, we benchmark different machine learning techniques to develop predictive models for hit identification; in particular, we highlight recent structure-based probabilistic approaches. Finally, we provide biophysical assay data, both on- and off-DNA, to validate our models on a smaller subset of molecules.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors have released a new dataset, KinDEL, based on DNA-encoded library (DEL) testing, specifically targeting two kinases, MAPK14 and DDR1. They conducted experiments on this dataset to test model performance.

### Strengths
The authors provide a substantial amount of new data.
The structure of the article is clear and easy to follow.

### Weaknesses
1. The evaluation is limited to only two kinase targets, MAPK14 and DDR1. Given that both targets are kinases, this dataset may have limited generalizability as a benchmark for models applied to broader, non-kinase targets.
2. The data-splitting method may ensure that compounds with the same disynthon do not end up in the same split, but it doesn’t fully prevent similar compounds from being grouped together, as disynthons do not necessarily represent the core structure of small molecules. Other approaches, such as scaffold-based or overall molecular similarity-based splits, may yield a more robust assessment. Specifically, methods that consider the maximum common substructure or Tanimoto similarity based on ECFP fingerprints should be explored to ensure a more rigorous separation of training and test sets.
3. Presentation Improvements: The table headers are somewhat confusing, making it unclear what the numbers in the table represent without reading the text. In Figure 3, "SP³" should be corrected to "sp³" for accuracy.

### Questions
1. Why use AI to reduce data noise? If DEL diverges significantly from reality, it may indicate instability or unsuitability for the current task. AI-based discriminative models are inherently inaccurate to some extent, so how effective is it to use one inaccurate method to adjust for another?
2. More explanation is needed for why certain chemical properties in Figure 3 are considered "drug-like". For instance, the molecular weight peak exceeds the traditional threshold of 500, and the QED values are relatively low.
3. Why is on-DNA data significant here, when off-DNA structures are more relevant for practical applications like drug development? On-DNA structures are unlikely to be developed as drugs.
4. Why didn’t the authors test more end-to-end models? Also, why did they use Morgan fingerprints as input instead of molecular representations like SMILES strings (1D), molecular graphs (2D), or atomic coordinates (3D)?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This study introduces a dataset of DNA-Encoded Libraries (DEL) focused on two specific kinases: Mitogen-Activated Protein Kinase 14 (MAPK14) and Discoidin Domain Receptor Tyrosine Kinase 1 (DDR1). Although the DEL datasets have proven valuable in drug discovery, they are relatively scarce for public use. The introduced dataset, named KinDEL (Kinase Inhibitor DNA-Encoded Library), comprises 81 million small molecules tested against MAPK14 and DDR1 kinases. An experimental evaluation is provided, comparing the performance of the proposed method in both on-DNA and off-DNA scenarios.

### Strengths
+ The availability of a well-curated and publicly accessible dataset is a notable contribution on its own, making this work a valuable resource for the research community.

+ The authors have conducted a thorough review of the relevant literature, effectively establishing the originality and motivation of the study, and demonstrating a clear understanding of the current state of the field.

### Weaknesses
- Given that the primary contribution of this work is a dataset, it would be beneficial to evaluate state-of-the-art (SOTA) methods on it, both to assess their performance in a new context and to demonstrate the dataset's comprehensiveness. The methods tested seem mostly old ones.

- Referring to Section 5.1 Current Datasets, there have been, especially recent, efforts of providing DEL datasets even though they don't exactly match the features offered by the present study. However, it might possible that these existing datasets could be adapted to resemble KinDEL.Could you elaborate on whether KinDEL is novel in that sense, i.e., for instance, enhancing the dataset from [Iqbal et al. (2024)] by incorporating on-DNA synthesis can be challenging?

- Furthermore, how does KinDEL compare to the existing DEL datasets in terms of diversity, and how well does it reflect the performance of existing methods in predicting Poisson enrichment? Does KinDEL offer a more comprehensive or representative testbed for evaluating these methods?

### Questions
- Referring to Section 5.1 Current Datasets, there have been, especially recent, efforts of providing DEL datasets even though they don't exactly match the features offered by the present study. However, it might possible that these existing datasets could be adapted to resemble KinDEL.Could you elaborate on whether KinDEL is novel in that sense, i.e., for instance, enhancing the dataset from [Iqbal et al. (2024)] by incorporating on-DNA synthesis can be challenging?

Sumaiya Iqbal, Wei Jiang, Eric Hansen, Tonia Aristotelous, Shuang Liu, Andrew Reidenbach, Cerise Raffier, Alison Leed, Chengkuan Chen, Lawrence Chung, et al. DEL+ ML paradigm for actionable hit discovery–a cross DEL and cross ML model assessment. ChemRxiv
doi:10.26434/chemrxiv-2024-2xrx4, 2024.

- Furthermore, how does KinDEL compare to the existing DEL datasets in terms of diversity, and how well does it reflect the performance of existing methods in predicting Poisson enrichment? Does KinDEL offer a more comprehensive or representative testbed for evaluating these methods?"

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
The paper presents KinDEL, one of the first large publicly available DNA-Encoded Library (DEL) datasets focused on kinase inhibitors, specifically targeting MAPK14 and DDR1 kinases. The papers benchmarks different machine learning methods for binding prediction.

### Strengths
1. the paper is clearly written and contains the experimental details in the appendix.

2. The dataset includes off-DNA data. The benchmark used different data split strategies.

### Weaknesses
1. This paper is a valuable contribution to DEL-based drug discovery. It may serve as a good resource for computational drug discovery. But I am not sure about the importance of this paper for the ICLR community.

2. The dataset has only two targets and both are kinase. The biophysical assay validation set is relatively small.
3. The authors did not mention the library size or sequence depth of the DEL dataset. Does it have an effect on the dataset?
4. The authors show that DEL-Compose performs better for off-DNA data. It would be helpful to discuss the potential biases due to the DNA barcode.
5. Why does the RF method become worse for the disynthon split?

### Questions
See Weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper propose a new open-source dataset as well as related benchmark for the DEL community. The main motivation behind this paper are: 

1. DEL community lacks a large, publicly available DEL dataset to benchmarking tasks. 
2. Current DEL dataset contains large bias and noise, and the existing methods cannot greatly address this issue. 

So, the authors propose an open-source dataset and a related enhancement approach to address these challenges. In details, these improvements and contributions are: 

1. KinDEL: a library of 81 million small molecules tested against two kinase targets, MAPK14 and DDR1, which is novel and with large amount. 
2. A comprehensive benchmark tested on current computational methods with on both on-DNA and off-DNA settings.

The proposed dataset and benchmark have great potentials to stimulate the development of the community.

### Strengths
1. The dataset constuction process is reasonable, sound, and comprehensive. Also, the related process is explained clearly.
2. The corresponding evaluation to the proposed dataset is comprehensive, and the two types of splits "random" and "disynthon" enhance the perspective of the benchmark. 
3. The evaluation is clear and straightforward (Table1, Table2, and Figure6). 
4. The comparison to the current datasets is well-written and shows the valuable insights from authors and their advanced understanding to the DEL-related tasks.

### Weaknesses
1. While there are very interesting performance comparison in the shown Table (Table1 and Table2), the explaination of the experiment results are expected, such as "why RF method performs the best on on-DNA set (Line 335)", "why there are different performance rankings on on-DNA and off-DNA settings?" and "why DEL-Compose(M) and DEL-Compose(S) performs differently on on-DNA and off-DNA settings?". I believe the insight provided by the authors would make the benchmark more solid and comprehensive. 
2. The proposed experiments including general performance (Table1, and Table2), and the visualization of experimental replicates are somehow not comprehensive enough. Serving as a benchmark for the DEL-community, more views and new settings are required, such as case study of top-ranking candidates (which can be potential candidates for real-world application), subset-Spearman coefficient (which is proposed in the paper "DEL-Dock: Molecular Docking-Enabled Modeling of DNA-Encoded Libraries" [1]), and potential effect of chemical properties and data source selections (building blocks) to the method performances on the KinDEL dataset. Then, the multi-view perspective of the benchmark could lead to larger contribution to the community.

### Questions
1. According to Table1 and Table2, the SOTA performance w.r.t. Spearman coefficient can reach over 0.7, which is a very promising result,  but in paper "DEL-Dock: Molecular Docking-Enabled Modeling of DNA-Encoded Libraries" [1], there's an another proposed dataset containing Fingerprint and docking poses, where existing methods can only achieve relatively poor performance (around 0.30 w.r.t. negative Spearman coefficient) compared to KinDEL dataset. May the authors explain what is the inner differeneces between two datasets that leads to the obvious differences between two datasets? I also believe this comparison can make this work more solid as the contributing benchmark. 
2. Is it possible to provide an advanced version of KinDEL dataset with machine-aided of molecule docking poses. I understand it's very time-consuming and CPU-resource costly, but the DEL dataset with 1D and 3D modalities would lead to wider applications and evaluations to this community. Considering the potential cost, I believe it is also great to have dataset with only fingerprint (1D) information of the molecules. 

Reference:
1. Shmilovich K, Chen B, Karaletsos T, et al. DEL-Dock: Molecular Docking-Enabled Modeling of DNA-Encoded Libraries[J]. Journal of Chemical Information and Modeling, 2023, 63(9): 2719-2727.

### Soundness
4

### Presentation
3

### Contribution
3
