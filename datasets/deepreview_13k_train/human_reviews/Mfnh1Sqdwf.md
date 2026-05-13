# Learning to Discover Regulatory Elements for Gene Expression Prediction

- Decision: Accept
- Scores: 8, 8, 8, 6

## Abstract
We consider the problem of predicting gene expressions from DNA sequences. A key challenge of this task is to find the regulatory elements that control gene expressions. Here, we introduce Seq2Exp, a Sequence to Expression network explicitly designed to discover and extract regulatory elements that drive target gene expression, enhancing the accuracy of the gene expression prediction. Our approach captures the causal relationship between epigenomic signals, DNA sequences and their associated regulatory elements. Specifically, we propose to decompose the epigenomic signals and the DNA sequence conditioned on the causal active regulatory elements, and apply an information bottleneck with the Beta distribution to combine their effects while filtering out non-causal components. Our experiments demonstrate that Seq2Exp outperforms existing baselines in gene expression prediction tasks and discovers influential regions compared to commonly used statistical methods for peak detection such as MACS3.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper the authors have highlighted the importance of gene expression as the fundamental process in biology, and have introduced a framework for predicting gene expressions by leveraging causal relationships between DNA sequences, epigenomic signals and regulatory elements or motifs. They have provided viability of this approach over two cell types and also state that adding the "extra info" in form of epigenomic signals is not always useful and may act as noise in some prediction tasks. To agree on generalization of this approach it has to be tested on more cell types and diverse epigenomic data.

### Strengths
When I compare this paper with other benchmarks (except EPInformer) in the field and for the same problem definition - I would rate this paper as high in terms of originality & significance. Yes, this work shows that gene expression prediction is not a siloed process, and that there are causal relationships between DNA sequences, epigenomic data, regulatory elements, and surrounding causal / non-causal parts of the input data. Also, deep learning algorithms can learn from these relationships and perform better gene expression predictions.

### Weaknesses
This follows from my comments on the strengths of the paper. After reading the EPInformer paper (released in early 2024), my rating reduces. Was this idea a new approach? I respectfully decline. EPInformer highlights the same intent, experimental approach and even comes very close in performance benchmarks & standard metrics. Not sure if this paper has added anything new for the ICLR community? To me as a reader, it has only reinforced the claims of EPInformer. I would have been happier if they can show viability of this approach over multiple cell types. But, data availability may be a limitation here.

Table 1 shows good comparison with previously available benchmark models and datasets. However, looking at EPInformer row, my question is did the authors run the EPInformer code or model over the CAGE prediction data? Because I only saw Pearson metric in the EPInformer paper. How were they able to get MSE, MAE, R2 numbers for comparison?

In the same table, GM12878 CAGE prediction numbers between EPInformer and Seq2Exp are exactly the same at two decimal places (not a significant improvement). This also indicates that the approach presented in the two papers is very similar. Neither one is better than the other. Originality in terms of problem definition and solution is also similar.

Also, some numbers do not match between the EPInformer row in this paper and the original EPInformer paper. For example, in the original EPInformer paper, figure 2C, Pearson coefficient for K-562 on CAGE-seq hold out test set is 0.848. But, the same info in Seq2Exp paper, table 1, says is 0.8517. How come?

### Questions
Table 1 shows good comparison with previously available benchmark models and datasets. However, looking at EPInformer row, my question is did the authors run the EPInformer code or model over the CAGE prediction data? Because I only saw Pearson metric in the EPInformer paper. How were they able to get MSE, MAE, R2 numbers for comparison?

In the same table, GM12878 CAGE prediction numbers between EPInformer and Seq2Exp are exactly the same at two decimal places (not a significant improvement). This also indicates that the approach presented in the two papers is very similar. Neither one is better than the other. Originality in terms of problem definition and solution is also similar.

Also, some numbers do not match between the EPInformer row in this paper and the original EPInformer paper. For example, in the original EPInformer paper, figure 2C, Pearson coefficient for K-562 on CAGE-seq hold out test set is 0.848. But, the same info in Seq2Exp paper, table 1, says is 0.8517. How come?

Update: Questions / Concerns were settled by reply from the authors. Thanks!

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
The paper is aimed at predicting gene expression from DNA sequence. In addition to the sequence itself, it also incorporates epigenetic information at each based. The model consists of two MAMBA-based Caduceus networks: the first network is trained to estimate a sparse mask over the bases to select regulatory regions, and the second one uses the selected DNA regions to predict the expression of the gene.

### Strengths
The paper showcases a successful application of the recently-proposed Selective State Space models (specifically, MAMBA-based Caduceus) on relatively long sequences (200k). 

The model goes beyond most current approaches by combining sequence with epigenetic signaling in a single, jointly optimized architecture. The architecture is sound, and uses information bottleneck principle to promote sparsity of the mask for selecting sequence regions, and then a straight-through estimator to allow differentiability through the hard mask being produced by the first network.

Experimental evaluation shows that the proposed architecture leads to improved prediction, in comparison with Transformer- and State-space-based models.

### Weaknesses
While the manuscript is mostly well written, it could use a more detailed explanation in several places, specifically related to:
- gene expression Y: it is often just described as "target variable Y", or "$Y \in R$". From 5.1.4 we read that ultimately the model is applied to a 200kbp region around a specific target gene, and one can understand that Y is the expression of that gene; it would be helpful to provide this information clearly earlier in the paper. It is also unclear if this is a single value representing the expression of the gene, or if it is a vector of expression values, for example, across different cell types or experimental conditions. This ambiguity needs to be addressed for clarity.
- model architecture: it also deferred to 5.1.4, and only described in one sentence (Caduceus-Ph). One would expect it to be in 4.1. entitled "Model architecture". Also, key details are missing: what are the specific hyperparameters (#layers, hidden dimension, etc.)? Is this a network trained de-novo for the expression task, or pre-trained (Caduceus has pretrained models of up to 131kbp, this one is 200kbp, if it was pre-trained by the authors, more details should be provided). Furthermore, the description of the Caduceus architecture is too high-level. It would be beneficial to include a more detailed explanation of how the bi-directional and RC-equivariance are implemented within the model, as this is a key aspect of the architecture.

### Questions
Details about the network training (and pre-training, if used), including architectural hyperparameters, as well as training procedure details (# steps, etc).

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper describes a model, Seq2Exp, that predicts gene expression values from two inputs: DNA sequence and a corresponding matrix of epigenomic measurements.   A key component of the model is a binary masking strategy that aims to automatically identify relevant regulatory elements in the DNA sequence.  The model uses an information bottleneck approach to try to ensure accurate extraction of relevant sequence signals.  The method is compared to a variety of state-of-the-art methods and yields better performance according to a variety of measures.

### Strengths
The main idea is well articulated and sensible.

The paper is very clearly written.

The related work section does a reasonable job of covering the recent, relevant literature.

The model is well formulated and modeling choices are well motivated in the text.

The empirical results are strong.

### Weaknesses
I think the sentence "Gene expression prediction is one of the fundamental tasks in bioinformatics." should be supported with a citation or two from some of the seminal works in this area, e.g., Nir Friedman's 2000 paper on predicting gene expression from promoter sequences.

The task description should be expanded.  It's not clear, from the description, how the inputs are registered to the output value Y.  Is the idea that the length-L input window is centered on the TSS?  To my mind, it would be clearer to represent Y as a vector over genes, and then include some formalism to represent the indexing of genes relative to X_{seq} and X_{sig}.

Line 420 ("Furthermore, we incorporate additional features such as mRNA half-life and promoter activity ...") is problematic because it sounds like this is an incomplete list.  For reproducibility, all inputs should be precisely described.  These features are not mentioned at all in Appendix A.3.

I don't see any point in using both R and R^2 as two distinct performance measures.  One is just the square of the other.

Minor point, but I think you should mention in the description of the baseline methods the size of the field of view of each one.

### Questions
A priori, I would expect the true binary mask to be "lumpy," i.e., groups of nearby base pairs should tend to be either relevant or irrelevant, reflecting the fact that, e.g., TFs tend to bind to regions rather than single base pairs.  How does your model handle this?

Section 5.1.2 does not make clear whether the competing methods were trained using your cross-chromosome train/test splits.  Is that the case?  I think you should clarify this point in the paper and also discuss how it may impact your results.  If you trained from more or a different type of data than your competitors, the comparison might be unfair.  OTOH,  if your competitors trained on data from your test chromosomes, then it might be unfair in the other direction.

I like the idea of Section 5.3, but I had trouble understanding exactly what was done here. MACS3 is a peak caller, so what is the model that predicts expression in this setting?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper deals with integrating genomic and epigenomic data to extract relevant regulatory DNA regions to predict gene expression, through the learning of a mask on DNA base pairs. The mask is then applied on the data, base-pair-position wise, and the masked data is used to train the predictor for gene expression. The paper describes the corresponding model in detail, and tests it alongside several baselines on genomic and epigenomic data.

### Strengths
- Quality: The submission seems technically correct and experimentally rigorous (however, I did not check the appendix in detail). The experimental results are convincing and appropriately compared to the numerous baselines.
- Clarity: It is well-grounded in the literature. The paper is well written and the contribution is clear. 
- Originality: The paper proposes a novel decomposition of regulatory regions into three groups, that have different causal relationships to genomic and epigenomic data.

### Weaknesses
 - Quality: The submission is not reproducible, as no code is provided (nor is the availability of the code discussed in the main paper nor in Appendix). There is no mention of hyperparameter tuning or value selection, especially for $\alpha_3$ and $\beta_3$, which parametrize the distribution of the soft mask on the regulatory regions. Performance is important for these methods, but I think runtimes across baselines and Seq2Exp should also be reported for practical purposes.
- Clarity: Some parts are not clear, for instance, the inclusion of additional data in the experiments, or the use of Hi-C data (see questions). 
- Significance: The assumption of independence of selection of regulatory regions across base pair positions at fixed (epi)genomic data (assumption written at the bottom of page 4) might be a bit too strong for the real-life data (for instance, for CpG islands -although, no methylation peaks are considered in these papers). I understand that it simplifies the computations and allows for a tractable model training, but perhaps it should be discussed further in the paper. 

The non-reproducibility and the unclear parts are the main reasons why I rate this paper 6 instead of 7-8.

### Questions
- What values were used for $\alpha_3$, $\beta_3$ in the experiments?
- Hi-C data usually gives access to a contact matrix between regions of length at least 5,000 base pairs. The appendix mentions that the paper “calculat[es] the frequency of contacts between a specific region (TSS) and all other regions, generating a Hi-C frequency distribution across the genome.” (page 15) What is exactly concatenated to the remainder of epi/genomic data? A matrix of size #base pairs x #regions that contains the frequency of contacts between the region to which a base pair belongs and all other regions? Doesn’t the number of regions change across chromosomes? Or is it a fixed number in your implementation?
- At page 8, “we incorporate additional features such as mRNA half-life and promoter activity from previous studies”. Where are those features added? To train the gene expression predictor $g_\phi$? Are they also added to all other baselines, and if so, at which point in their model of gene expression? 
- Why don’t you use a neural network for also learning the parameters of the beta distribution for epigenomics ($\alpha_2$, $\beta_2$)?

### Soundness
3

### Presentation
2

### Contribution
3
