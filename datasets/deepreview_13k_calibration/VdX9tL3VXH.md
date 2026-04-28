# A long range foundation model for zero-shot predictions in single-cell and spatial transcriptomics data

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 3, 6, 3

## Abstract
Large transformers pre-trained with language model objectives have demonstrated success in multiple fields, and have tremendous potential for modeling single-cell RNA-seq and spatial transcriptomics data. However, these approaches are yet to overcome various challenges, including inductive biases that hinder generalization, artifacts and quality of the underlying data, as well as downstream evaluation pipelines that do not reflect the biological challenges in the field. In this work, we propose a new framework, sCellTransformer (sCT), that relies on a first principles formulation of the problem as well as a validation pipeline designed to evaluate models generalization through zero-shot predictions. sCT leverages a long-range convolutional-transformer architecture that is trained from unprocessed single-cell and spatial transcriptomics data. In contrast to previous works, sCT represents cells with up to 20,000 protein-coding genes, processes sets of multiple cells, and predicts about a million discretized gene expression tokens. We show that representing gene expression as discrete levels allows us to mitigate the high sparsity present in single-cell data both during training and evaluation. We present state-of-the-art empirical results on several zero-shot gene expression imputation, cell-typing, and clustering tasks in both single-cell as well as spatial domains, outperforming current foundation models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors of the paper develop sCellTransformer, a new foundation model for single-cell and spatial transcriptomics data. The sCT model overcomes existing issues in single-cell transformers, namely the limit to processing one cell at a time due to memory constraints and the lack of a principled method to model properties in single cells such as discreteness and overdispersion. To tackle said problems, sCT utilises a convolutional architecture to process multiple cell representations for better contextual information. The model also discretises the predicted gene expression to better represent the true data domain via masked language modelling. Finally, sCT introduces spatial positional encodings to infuse spatial awareness into the sequence tokens. The authors showcase the model on multiple tasks such as whole cell imputation, which is crucial to infer gene expression from neighbourhoods when array-based spatial assays fail to capture single-cell profiles in the spatial slide. The paper also tackles single-cell RNA-seq reconstruction and clustering using the model’s embeddings.

### Strengths
Overall, I find the ideas covered in the paper interesting. What I particularly liked is a certain attention to biological properties of single-cell data, such as discreteness and variability, which, in my opinion, have been severely overlooked in other models. I also liked the reasoning towards contextual modelling by introducing an architecture able to handle multiple cells at the same time. Finally, I appreciate the use of positional encodings for modelling the spatial identities of cells. The performance seems pretty promising.

### Weaknesses
* In lines 59-60, I find that the connection between modelling continuity and the lack of accounting for over-dispersion is not very clearly motivated. I think this is a very important point when modelling single-cell RNAseq and I am happy the authors brought it up. In general, though, it could be stated clearly why modelling continuous raw counts is a problem when trying to recover the over-dispersion in scRNA-seq. Specifically, the manuscript should elaborate on how the continuous nature of predicted values, often optimized with mean squared error, fails to capture the discrete and highly variable nature of gene expression counts, which are better represented by distributions like the negative binomial. This is crucial because over-dispersion is a key characteristic of scRNA-seq data, and a model that does not explicitly address it may not accurately reflect the underlying biology.
* From a terminology perspective, I would not define individual cell expression vectors as “gene expressions”. I would replace the term with something like “expression values” or so. 
* I find myself disagreeing with the sentence “Unlike scRNA-seq, spatial transcriptomics is a relatively new technology and publicly available data is still scarce.” Nowadays there are a lot of public spatial transcriptomics datasets out there and technologies to produce them, which makes the field so exciting. I would probably tune the claim down a bit. 
* The architecture in 3.2 is understandable and clear. However, I feel it is a bit confusing for a less expert audience what a sequence here actually is (i.e. a stack of cells), especially because this is what makes sCT different from foundation models processing one cell at a time. You describe this in Learning intercellular dependencies but I believe it would make the flow better if you define this formalisation from before.
* I think the structure of the paper could be improved. Especially, Table 1 is referenced multiple times in the methods section, but it contains a metric (MCC) that goes undefined till much later in the paper as a representation of optimality. Probably I would either refer to Table 1 only in the results or give some elements of understanding before. 
* I would not discuss results in the Table caption (e.g. in Table 2) but only in the text. 
* I appreciated the experiment in Table 3. But I think it would add value to it to add how the two models perform on gene predictions in the three sparsity levels separately. Also, Table 3’s caption does not describe the depicted evaluation metric. Furthermore, it would be beneficial to specify how the sparsity levels are defined, e.g., are they based on the percentage of zero counts for each gene across cells or some other criteria? This would allow for a better understanding of the results.
* I believe the presentation of results in Figure 3 is suboptimal. I would add titles to the single plots and definitely include a UMAP plot from the real cell gene expression to show how the embedding compares with the gene expression space. As of now, saying that sCT “corrects gene expression” sounds unsupported, as correction implies visualising and comparing with the data when the batch effect is still present. I also think that clustering requires some simpler baseline (like scVI or even the plain PCA embedding of the data). The current presentation lacks a clear comparison to the actual data distribution, making it difficult to assess the quality of the correction.

### Questions
* I also think that Table 1 is overall unclear. I think I would add more detail in the legend on how to read it. For example, are the “-“ in the first columns bullet points or “minuses” with a specific meaning? Does removing layer normalisation make the results better (0.39—>0.40)?  From this result, I would not claim it is a very useful add-on. I recommend improving the Table presentation and description since it is very important to add value to the story. 
* I personally do not find the reasons for using discretised expression convincing in section 3.3. Isn’t binning based on the raw data? How does this buffer out the problem with raw count heterogeneity among studies? 
* Could you please elaborate more on this sentence “In order to ensure a fair comparison with models like scGPT and CellPLM, which output continuous values, we bin the output predictions with the bin-edges that we calculate during preprocessing.” How are lower vs higher bin edges chosen here to assign a continuous expression value?
* “We also evaluate the effect of using multiple cells as input, by training and testing variants of sCT with one and ten cells in Fig. 9.”. Here you miss the fact that you tested with 50 as well (which eventually you use as the default value). 
* How many neighbours were selected for the KNN approach for predicting whole cell expression tokens?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces sCellTransformer (sCT), a novel framework for modeling single-cell RNA-seq and spatial transcriptomics data using a convolutional-transformer architecture. Unlike previous approaches, sCT is designed to address key challenges such as inductive biases, data quality issues, and biologically relevant downstream evaluation pipelines. It employs a first-principles approach and aims for better generalization through zero-shot predictions. sCT processes sets of multiple cells, representing them with up to 20,000 protein-coding genes and predicting approximately one million discretized gene expression tokens. By discretizing gene expression levels, the model effectively tackles the sparsity problem in single-cell data during both training and evaluation. The framework demonstrates superior performance in zero-shot gene expression imputation, cell-typing, and clustering tasks across single-cell and spatial datasets, surpassing existing foundational models.

### Strengths
1. Study the foundation models on single-cell and spatial transcriptomics data.
2. Employ convolution layers for efficiency.

### Weaknesses
1. The proposed improvements in the paper are rather straightforward. Learned Gene Normalization refers to the layer normalization, Positional Embeddings refer to standard sinusoidal position embeddings. The authors stack 50 cells into a single sequence, which from my perspective, creates sudo bulks and lowers the granularity instead of modeling intercellular dependencies. It would be great if the authors could elaborate more on how the proposed strategy can help with modeling intercellular dependencies.
2. Some statements in the manuscript are not put correctly. For example, in line 231, the authors state that CellPLM and scGPT are built on MLM objective and predict raw gene expression values. In fact, CellPLM conducts library size normalization and log1p on the counts, and scGPT utilizes next token prediction with data binning. Note that the binning strategy has already been employed in scGPT. The authors should explicitly acknowledge where their approach uses similar techniques (like binning) to prior work.
3. The authors mention that *downstream evaluation pipelines that do not reflect the biological challenges in the field* in the abstract. However, in the experiments, the authors only include gene imputation and cell clustering tasks, which is quite limited. Please consider tasks like gene perturbation prediction, gene regulatory network inference, cell-cell communication, etc.

### Questions
See weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
In this study, the authors pretrained a convolutional-transformer combined model on both single cell and spatial transcriptomics data. Quantitative comparison with previous models on the imputation and clustering tasks showed the advance of the current model. Several ablation experiments motivate specific choices in the model.

### Strengths
The authors proposed several architecture-level improvements including convolutional layer and learned gene normalization. The ablation experiments on certain aspects are well-designed and provide insights into the model design. The author also extended the imputation task to the whole cell level.

### Weaknesses
First of all, current downstream tasks can not support the claim of a foundation model; it is more like an imputation model. A foundation model should deal with various tasks. Also, some concepts like "a first principles formulation of the problem" are not clearly explained.

While new convolutional architecture is interesting, the authors did not verify its effectiveness by comparing it with simple MLP, and also did not clearly explain the reason behind the design. The authors also did not fully compare the different gene expression discretization methods, making it hard to show its novelty. At least the authors should refer to the previous works on the discretization methods (https://openreview.net/pdf?id=gdwcoBCMVi). Also for the imputation task, some important baseline methods are missing, such as gimVI (https://arxiv.org/abs/1905.02269), scFoundation (https://www.nature.com/articles/s41592-024-02305-7), which are the foundation and also domain specific models claimed to deal with the missing data.

Some critical details are missing for the spatial imputation experiment design. For example, how did the author use other compared methods, did these models fine-tuned the same training data? Also, the authors did not provide detailed information on held-out data in HEST, as some of the fovs are actually replicates of the training data, which may lead to the risk of data leakage.

### Questions
1. Could the author further explain the concept of "a first principles formulation of the problem"? or it is better to remove this claim in the abstract.

2. What is the rationale behind the design of the new convolutional architecture? As gene expression data is nonsequential, how can the author define the "local" and "global" patterns in the data? Also, could you compare it with simple MLP to show its effectiveness?

3. Could the author further explain the difference between learned gene normalization and the original layer normalization? What is the meaning of "subsequence"? How does the learned gene normalization help the model?

4. Could the author justify the choice of the discretization method? How did you decide the bing edges? How does it compare with the previous works on discretization methods?

5. Since the expression distribution is quite different between the two data types, how can the author justify the contribution of single cell data to the spatial imputation tasks? I would like to see the performance of sCT pretrained on the spatial data only.

6. For the imputation benchmark, could the author compare with the gimVI and scFoundation, which are models that can deal with the missing data?

7. Still in the imputation tasks, did the author fine-tune the compared models on the same training data? It should be clarified in the paper.

8. Could the author provide the details of the held-out data in HEST? I suggest the author leave out FOV from new studies to avoid the risk of data leakage.

9. Since the cell type information is not used in the training process, how can the author assign cell types based on the training-free cell embeddings? 

10. Some incomplete sentences in the paper, such as "with a decay rate of ...." could be revised.

### Soundness
2

### Presentation
2

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
Here the authors present sCellTransformer (sCT), a transformer model for analyzing single-cell RNA-seq and spatial transcriptomics data. sCT is distinguished from previously proposed "single-cell foundation models" through its use of a convolutional transformer architecture that scales to handle all ~20,000 protein coding genes per cell. The authors apply their model to a set of imputation/clustering tasks.

### Strengths
* **Architectural choices**: The authors incorporate new architectural ideas (e.g. from Linder et al. 2023) to enable the use of all ~20,000 protein coding genes with single-cell transformer methods.
* **Incorporation of spatial information**: To my knowledge, sCT is the first single-cell transformer that specifically attempts to incorporate spatial information via spatial positioning tokens.

### Weaknesses
After reading the paper I have numerous major concerns that prevent me from recommending acceptance. In short, the presented results suffer from a number of common issues in recent "single-cell foundation model" papers (e.g. lack of rigorous benchmarking against current best practice methods), and it's not clear to me that sCT represent a major advance for the analysis of single-cell data. Details below:

* **Missing comparisons with non-"foundation model" baselines**: A number of recent benchmarking studies (e,g, [1, 2, 3] among others) have found that recently published transformer-based single-cell foundation models perform no better than significantly simpler (e.g. linear) baseline models at a variety of downstream tasks. However, the authors' manuscript only compares against other transformer models, thus making it impossible to assess whether the authors' method indeed represents a meaningful advancement. For for the batch effect/cell type classification tasks, how do simpler baselines (e.g. logistic regression, scANVI, etc.) compare? Specifically, the lack of comparison against methods like scVI, which explicitly model batch effects, makes it difficult to assess the true contribution of sCT in this domain. Furthermore, for cell type classification, a comparison against a basic k-nearest neighbors classifier on the raw data would provide a crucial baseline.
* **Unclear real-world utility**: Based on the provided experimental results, it's not clear to me that the authors' method provides additional utility beyond current standard scRNA-seq analysis workflows. For example, given that (as mentioned by the authors) <6% of protein-coding genes are expressed in an individual cell on average, I'm not sure why the results presented in Table 2 are meaningful, as most of the time all the masked values will have zero measured expression. It is unclear how masking a gene that is already zero provides any information about the model's ability to impute missing values. Similarly, I'm not clear on what real-world need the authors are trying to address in the "whole-cell imputation task". The authors mention that measurements from some individual cells can be missed due to misalignment with spot boundaries, but it's not clear to me why this phenomenon would lead to an entire spot dropping out. The bottom line is: what **new** analyses are enabled by the authors' approach? As-is I'm sure what sCT brings to the table compared to previous approaches, beyond (maybe) better imputation performance. The manuscript needs to clearly articulate the specific biological questions that sCT can address that are not already addressed by existing tools.
* **Preprocessing/evaluation details**: For preprocessing the authors mention only applying a log transform to raw expression values and then tokenizing via a uniform binning strategy. How do the authors handle differences in sequencing depth/library size between cells? From the description provided in the manuscript I don't see which preprocessing steps (if any) handle this issue, which could confound the authors' tokenization scheme. Specifically, library size differences can lead to vastly different distributions of gene expression values, which would be problematic for a uniform binning strategy. On a related note, the performance of some baseline methods is bad enough that I'm concerned the reported results may be an artifact of the authors tokenization/evaluation setup. For example the results for scGPT in Table 2 show mean absolute error values of 260, which seems suspicious to me given that the data has been log-transformed/binned. Are the scGPT-outputted values on a significantly different scale than the bin values calculated for sCT during preprocessing? Or as another sanity check, what do the corresponding errors look like for simple baseline of prediction zero expression or the mean expression for that gene? This is important to establish whether the reported MAE values are meaningful or simply an artifact of the evaluation setup.

### Questions
See "Weaknesses".

### Soundness
1

### Presentation
2

### Contribution
1
