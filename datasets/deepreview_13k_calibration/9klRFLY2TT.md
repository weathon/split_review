# DNABERT-S: Pioneering Species Differentiation with Species-Aware DNA Embeddings

- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
We introduce DNABERT-S, a tailored genome model that develops species-aware embeddings to naturally cluster and segregate DNA sequences of different species in the embedding space. 
Differentiating species from genomic sequences (i.e., DNA and RNA) is vital yet challenging, since many real-world species remain uncharacterized, lacking known genomes for reference. Embedding-based methods are therefore used to differentiate species in an unsupervised manner.
DNABERT-S builds upon a pre-trained genome foundation model named DNABERT-2.
To encourage effective embeddings to error-prone long-read DNA sequences, we introduce Manifold Instance Mixup (MI-Mix), a contrastive objective that mixes the hidden representations of DNA sequences at randomly selected layers and trains the model to recognize and differentiate these mixed proportions at the output layer. We further enhance it with the proposed Curriculum Contrastive Learning (C$^2$LR) strategy.
Empirical results on 23 diverse datasets show DNABERT-S's effectiveness, especially in realistic label-scarce scenarios. 
For example, it identifies twice more species from a mixture of unlabeled genomic sequences, doubles the Adjusted Rand Index (ARI) in species clustering, and outperforms the top baseline's performance in 10-shot species classification with just a 2-shot training.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces DNABERT-S, a genome model focused on species-aware DNA embeddings to differentiate and cluster DNA sequences by species effectively. Building upon DNABERT-2, it incorporates two key innovations: Manifold Instance Mixup (MI-Mix) and Curriculum Contrastive Learning (C2LR). MI-Mix mixes hidden representations at random layers to enhance embedding robustness, whereas C2LR gradually presents increasingly challenging training samples to improve model generalization. Experiments across 23 datasets demonstrate DNABERT-S’s effectiveness, especially in species clustering, metagenomics binning, and few-shot classification tasks, showing that it significantly outperforms baselines, including by doubling clustering performance in Adjusted Rand Index (ARI). The model provides a robust and scalable solution to biodiversity studies and microbiome research in label-scarce environments, addressing limitations of previous genome foundation models in species differentiation.

### Strengths
1.	Innovative enhancement of embedding representation for species differentiation: The paper improves the embedding representation of DNA sequences by introducing techniques such as DNA-Dropout and DNA-Double, which enable the model to better distinguish DNA sequences of different species. This improvement enhances the robustness of the embedding and the ability to capture the similarity of DNA structures, significantly improving the accuracy of species clustering and classification.
2.	Improving model generalization using contrastive learning: the paper’s Mixing of Streaming Instances (MI-Mix) and Course Contrastive Learning (C2LR) techniques gradually introduce training samples of increasing difficulty during fine-tuning, allowing the model to adapt more efficiently to species-rich macrogenomic data. This approach improves the model’s generalization ability in environments with scarce labels and high data diversity and is suitable for tasks such as macrogenomic binning and species classification.
3.	Practicality for macro-genomic data: The model is particularly suitable for macro-genomic data and biodiversity research. Through targeted fine-tuning and optimization, DNABERT-S significantly improves its performance on tasks such as species clustering and few-sample classification, providing a powerful tool for microbiomics and biodiversity research.

### Weaknesses
1.	Limited Novelty of Methodology: The paper employs Manifold Instance Mixup (MI-Mix) and Curriculum Contrastive Learning (C2LR), which are widely recognized in deep learning, limiting the originality of the methodology. The primary innovation lies in adapting these techniques specifically to metagenomic tasks rather than introducing novel technical advancements (see Sections 3.3 and 5.2). To strengthen this aspect, further evidence could clarify why these specific strategies are especially suited to metagenomics, particularly in addressing the shortcomings of traditional Mixup or contrastive learning for the specific challenges within this domain. For instance, the paper does not sufficiently explain why mixing hidden representations at random layers is superior to mixing input sequences directly, especially given that genomic sequences may share common segments across species. A more detailed analysis of how MI-Mix addresses this challenge is needed.
2.	Limited Scope of Comparative Experiments: The paper’s experimental validation is confined mainly to select metagenomic datasets, lacking a broader comparison with other current genomic models and widely used bioinformatics tools, such as database search techniques (refer to the experimental setup). Including these common baselines would provide a more comprehensive assessment of DNABERT-S’s effectiveness, highlighting the model’s practical applicability across diverse tasks and data types. For example, a comparison against methods like BLAST or MMseqs2 would provide a more complete picture of the model's performance relative to established tools.
3.	Insufficient Visual Detail in Figures: In Figure 1, the current marker size obscures certain details, making it difficult to interpret the clustering and classification patterns. Adjusting the marker size could improve visibility, enhancing the visualization of data distribution across different methods.
4.	Figure Layout Issues: Figure 4’s layout partially overlaps with the text, which detracts from the paper’s readability and professionalism. Adjusting the figure’s placement could ensure proper spacing and clear separation between text and visuals.
5.	Ablation Study Lacks Detailed Discussion: While the ablation study indicates a substantial improvement when combining W. SimCLR and MI-Mix, the analysis does not sufficiently explore the mechanisms behind this synergy (see Section 5.3). A more detailed discussion, possibly with illustrative examples, would elucidate why the combined approach enhances data representation, providing stronger support for the method’s efficacy. For example, the study could analyze the embedding space to show how the combination of SimCLR and MI-Mix leads to better separation of species clusters compared to using either method alone.
6.	Unclear Parameter Justification and Redundancy Reduction: The paper references data filtering criteria, such as selecting only species with at least 100 sequences for classification, but lacks a detailed rationale for these choices. Additionally, the redundancy reduction steps are not thoroughly explained, which could influence the results’ transparency and reliability. Supplementing the parameter selection with explicit reasoning in the data preprocessing steps would enhance the methodological rigor. For instance, the paper should explain why a threshold of 100 sequences was chosen and how this impacts the diversity of the dataset.
7.	Potential Data Leakage in Pre-Training: Given that GenBank serves as a substantial training source, there is a potential risk of overlap between the training and testing datasets. The study does not confirm whether this overlap was checked, which raises concerns about possible data leakage (see Section 5.1). Verifying this aspect and addressing any overlapping data would strengthen the reliability of the results. Specifically, the paper should detail the steps taken to ensure that sequences used for evaluation are not present in the pre-training dataset, or at least quantify the extent of any potential overlap.

### Questions
1.	The paper lacks detailed information on hyperparameter selection and the tuning process, particularly regarding how these choices impact overall performance. Could the authors provide further details to clarify the influence of these selections on model stability and performance?
2.	What are the specific advantages of DNABERT-S over existing DNA classification models? A more detailed explanation would help elucidate the model’s unique contributions to the field.
3.	Could this method be extended to other biological sequences (e.g., RNA or protein sequences)? If so, what adjustments would be necessary to adapt to these cases?
4.	It would be helpful if the authors could further explain the measures taken to ensure fair comparisons in their experiments, including steps to prevent data leakage and whether model scales were controlled. While the downstream tasks performed well compared to multiple baselines, training/validation/testing based on sequence identity was not conducted, which could pose a risk of data leakage in this setup.
5.	One of the paper’s focuses is on exploring different embedding methods for DNA sequence classification, using a variety of pre-trained models to enhance classification performance. However, a detailed comparison of time and memory consumption across different embedding methods is missing, especially regarding:
(a)	Time and Memory Consumption of Embedding Methods: Could the authors clarify the computational time and memory usage differences between embedding methods during the training and inference stages?
(b)	Resource Analysis of Different Pre-Trained Models: How do time and memory consumption vary across different pre-trained models, and which models are most advantageous for specific tasks? A more detailed analysis could aid in model selection and optimization.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper finetunes the DNABERT-2 model to generate species-aware embeddings from genomic sequences.
Current genome foundation models (such as DNABERT-2) are trained on language-modelling training tasks but do not develop discriminative embeddings.
The authors leverage genome species datasets and contrastive methods to learn embeddings that perform better on both unsupervised and supervised downstream tasks in species differentiation.

They develop a training scheme they name C^2LR for Curriculum Contrastive Learning.
In C^2LR the training of the model is in 2 phases:

Phase 1 : First, a weighted version of SimCLR is used to encourage embedding s from the same species to be near each other. Weighted SimCLR is SimCLR but with with higher weights for negative samples closer to the anchor.

Phase 2 :   Next, they introduce and use a contrastive loss called Manifold Instance Mixup. This is a more challenging task where they mix hidden states in a random layer and predict the proportion of the mix at the output.

They create and share an evaluation benchmark and perform extensive evaluations of the resulting embeddings.

### Strengths
This is a well written paper with a clear goal and solid choices in methods.

The main novel contribution is the Manifold Instance Mixup method(MI-Mix). They take previous work (i-Mix) which mix inputs in the batch such as images to create examples. They realize that there are no good ways to mix (blend) DNA sequence s at the input and instead apply the i-Mix methodology to the hidden states at a random layer of the network.

They perform extensive evaluations with baselines from VAE and transformer competitors and perform ablation studies.

The embeddings are clearly beneficial in downstream tasks and useful to the community.

They also create and share a benchmark dataset.

### Weaknesses
In table 2, it is clear that MI-Mix performs very well on it's own. The paper would be much simpler and just as convincing re. performance if it focused on MI-Mix and dropped the curriculum and weighted SimCLR. Of course, getting the best result for a foundation model is also important.

In Table 1 there should also be at least one baseline for a model that has also gone through some kind of species differentiation training or finetuning. As noted in the text, baseline models are unlearnable or trained on generic language modelling objectives. As far as I can tell only DNABERT-S has had the luxury of using species labels in its training.

There could be more discussion about the original Manifold Mixup method (that i-Mix this method was partly inspired by), and how it relates to the new Manifold Instance Method.

Typos::

line 435 text overlaps with fig 4

### Questions
Do any of the other baseline models see the same or similar labels to those used in the contrastive trianing?

How well does MI-Mix perform on other modalities - such as the original i-Mix task?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces DNABERT-S, a modified version of its precursor, DNABERT-2, that is applied to the task of differentiating DNA sequences between different species.

### Strengths
- The authors perform comprehensive testing across a variety of scenarios, as well as a thorough set of ablations. 
- While each of the separate components - Manifold Mixup, weighted SimCLR, curriculum learning -  have been introduced and utilized previously, this paper appears to be a new application of these methods to genome sequence data. 
- The model strongly outperforms baselines on metagenomics binning, species clustering, and species classification.

### Weaknesses
 - In general, there is a lack of meta-level detail regarding the models that are being compared. It would be helpful to include tables that compare the number of parameters, embedding dimensions, and computational costs (inference time and memory) for each model/technique used. This is particularly important for assessing the practical applicability of DNABERT-S compared to simpler methods.
- The use of Curriculum Contrastive Learning (C$^2$LR) strategy with the Manifold Instance Mixup (MI-Mix) loss could be an impactful contribution, however not enough work is done to show the utility of these approaches, and whether they are even helpful enough in light of computational tradeoffs. Indeed, removing C$^2$LR appears to change the performance by a small amount (only a -1.13 to -1.17 decrease). The paper should include a more thorough analysis of the individual contributions of C$^2$LR and MI-Mix, including a breakdown of their impact on model performance and training time, as well as a more detailed explanation of the motivation behind their combination.
- The paper is missing comparisons to similar models that employ contrastive learning for metagenomic binning tasks. Specifically, the authors should include comparisons to methods such as COMEBin, a SOTA binning method based on contrastive multi-view representational learning (Wang et. al, 2024) and CLMB (Zhang et. al, 2022).
- It is strange that the authors would not use the benchmarking set up in CAMI II to assess their model performance, given the built-in genome binning benchmark and comparison to SOTA tools.

### Questions
- While the authors claim to compare DNABERT-S to the strongest existing methods, there appear to be a number of comparable approaches that they overlook, especially in metagenomics binning. Some examples include COMEBin, a SOTA binning method based on contrastive multi-view representational learning (Wang et. al, 2024) and CLMB (Zhang et. al, 2022). How does DNABERT-S compare to these baselines?
- In the classification tasks, what is the performance of each baseline? While it is helpful to highlight the difference between DNABERT-S and the best-baseline, please include the full table of performance on each of the datasets for each of the models tested (in the appendix), as this information is still a helpful contribution.
- How does Manifold Instance Mixup differ from Manifold Mixup, introduced in Verma et a. (2019)? Please clarify this in the paper.
- Dataset complexity, meaning the number of genomes present, and the relative abundances of those genomes, can often influence the performance of a model in metagenomics binning. How does DNABERT-S perform at metagenomics binning when these two factors are changed? For example, what happens when the number of relative abundances of different species are highly imbalanced?
- Given the well established, recent CAMI II challenge for metagenomic binning (that the authors reference in the paper), how does DNABERT-2 compare to the tools benchmarked during this challenge (see Meyer et. al, 2022)? 


Meyer, F., Fritz, A., Deng, Z. L., Koslicki, D., Lesker, T. R., Gurevich, A., ... & McHardy, A. C. (2022). Critical assessment of metagenome interpretation: the second round of challenges. Nature methods, 19(4), 429-440.

Wang, Z., You, R., Han, H., Liu, W., Sun, F., & Zhu, S. (2024). Effective binning of metagenomic contigs using contrastive multi-view representation learning. Nature Communications, 15(1), 585.

Zhang, P., Jiang, Z., Wang, Y., & Li, Y. (2022). CLMB: Deep contrastive learning for robust metagenomic binning. In International Conference on Research in Computational Molecular Biology (pp. 326-348). Cham: Springer International Publishing.

### Soundness
3

### Presentation
3

### Contribution
3
