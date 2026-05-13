# Weighted Diversified Sampling for Efficient Data-Driven Single-Cell Gene-Gene Interaction Discovery

- Decision: Reject
- Scores: 5, 3, 1

## Abstract
Gene-gene interactions play a crucial role in the manifestation of complex human diseases. Uncovering significant gene-gene interactions is a challenging task. Here, we present an innovative approach utilizing data-driven computational tools, leveraging an advanced Transformer model, to unearth noteworthy gene-gene interactions. Despite the efficacy of Transformer models, their parameter intensity presents a bottleneck in data ingestion, hindering data efficiency.  To mitigate this, we introduce a novel weighted diversified sampling algorithm. This algorithm computes the diversity score of each data sample in just two passes of the dataset, facilitating efficient subset generation for interaction discovery. Our extensive experimentation demonstrates that by sampling a mere 1\% of the single-cell dataset, we achieve performance comparable to that of utilizing the entire dataset.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel computational framework designed to discover gene-gene interactions linked to complex diseases through single-cell transcriptomic data. Utilizing a Transformer model named CelluFormer, the authors address the challenge of computational efficiency by implementing a weighted diversified sampling algorithm. This algorithm allows the selection of a representative data subset by calculating a diversity score based on the Min-Max density kernel.

### Strengths
- The proposed method significantly reduces computational requirements without sacrificing accuracy. This approach addresses a key challenge in handling large-scale single-cell transcriptomic data.
- By leveraging Transformer models (CelluFormer) for gene-gene interaction discovery, the paper effectively adapts state-of-the-art NLP techniques to bioinformatics.
- The extensive experimental validation across multiple datasets and comparison with various baselines (e.g., Pearson Correlation, Spearman’s Correlation) provides empirical support for the proposed method’s effectiveness and robustness in data efficiency.

### Weaknesses
 - The paper does not thoroughly discuss potential limitations or biases in using Transformer attention maps for gene-gene interaction discovery, such as how model-specific patterns may impact biological interpretability or generalizability.
- While the diversity score and sampling algorithm are well-motivated, the paper lacks detailed explanations regarding parameter sensitivity (e.g., choice of sample size) and the scalability of the method to even larger datasets or different cell types beyond the focus on Alzheimer’s Disease data.
- The paper could benefit from a more comprehensive comparison with existing gene interaction discovery techniques, especially non-Transformer-based methods that might offer complementary insights or efficiency advantages.
- For the scGPT model, there are cases where it performs better than the proposed method on specific datasets. Therefore, simply attributing the foundation model's lower performance to overfitting to pretrained knowledge or a mismatch between pretraining and fine-tuning data seems insufficient to support the claim that it underperforms compared to the proposed method.

### Questions
Please see the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper propose a method that is related to transformer architecture to do gene-gene interaction discovery in single cell data. The key idea of the method is a density-based sampling method to reduce the data size.

Edit: after the rebuttal, I still keep the scores.

### Strengths
N/A

### Weaknesses
The paper has major problems that prevent me from understanding the method itself and its relations to related methods such as transformer and previous work on the same problem.
- Problem setting is not clear: It is stated that data set X given, so what is a disease D is in the dataset? What need to be learnt? How many dimensions are there in X, |V| or m?
- Model is not clear: what is "f"? The proposed model is not described anywhere in the text. Where is the interaction map in the model? What does it mean by "f" can successfully predict a disease infection? What does it mean by a gene pair that contribute the most to "f"?
- I think the paper simply refers the model to transformer architecture but the data here vectors!?! 
- Conditions 2.1 on permutation invariant is totally misleading. "f" is defined for vectors, should we permute vector elements? 
- While the data is said to be sparse, there are up to ... 12000 expressed genes in a cell, most of them have 2000+ expressed genes?
- The definition of Min-Max density is clumsy since it can refer to its root: kernel density estimation.

### Questions
Refer to the weaknesses for the questions that need to be addressed. 
More general ones:
- What are the related methods for this problem?
- What is the model proposed here?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper aims to use transformer model trained from scRNA-seq data to identify gene-gene interactions.  The approach involves combining the attention matrices over all the layers of the transformer and then evaluating whether the resulting aggregated attention values give higher weights to known pairs of interacting genes.  To make the approach computationally feasible, the authors also develop a sketching procedure to select a representation subset of cells.

### Strengths
The problem of detecting gene-gene interactions directly from scRNA-seq data is important.

### Weaknesses
The main idea here -- that you can infer gene-gene interactions by looking at the attention map in the transformer -- is pretty obvious.

The proposed sketching procedure is not compared to any existing methods.

The proposed transformer model is insufficiently described, and the paper doesn't say how it differs from existing models.

One of the major contributions here is a method for finding representative subsets of cells from scRNA-seq data (Section 3).  Unfortunately, this problem is already fairly well studied, and the paper fails to cite any existing methods that tackle this problem (e.g., Hie et al., Cell Systems 2019; Yang et al., ACM-BCB 2020; Yi & Stanley, bioRxiv, 2023; Hao et al. Nat Biotech 2024).  These methods should be employed and compared against.

More generally, there are many existing methods for detecting gene-gene interactions from scRNA-seq data.  Prominent examples include SCENIC (Aibar Nature Methods 2017), GRNBoost2 (Moerman Bioinformatics 2019), PIDC (Chan Cell Systems 2017), SCODE (Matsumoto Bioinformatics 2017), SCRIBE (Moerman Nature Communications 2019).  This large literature is not cited, and none of the methods therein is compared against.

In line 161, you say that you train a Transformer model to classify whether a cell is an "Alzheimer's disease-infected cell or not."  First, Alzheimer's is not an infection.  But more importantly, there is no way to label individual cells as being affected by Alzheimer's or not.  I am guessing that this sentence should say that you are labeling cells based on whether they come from an individual with Alzheimer's disease.  How exactly this is done should be clarified.

The evaluation of the gene-gene interactions is problematic.  The approach amounts to filtering a large set of known gene-gene interactions to include only those interactions that are implicated in Alzheimer's disease.  This ignores the fact that many genes not involved in Alzheimer's disease continue to function and interaction with one another in the cell.  It's not actually clear to me whether the evaluation considers pairs of genes not involved in Alzheimer's.  It seems, from the description, like these pairs are treated as non-interacting.

### Questions
Why develop a new transformer model if the goal is just to identify gene-gene interactions? It seems like it would be easier to work with some existing model.

How does the proposed Transformer model differ from scGPT, GeneFormer, and scFoundation?  On line 124 we are told that they are similar to CelluFormer, but I don't see any indication of how they differ.

How do the "scatter addition operations" described in line 231 work?  This entire paragraph would benefit from a more formal treatment, since I found the textual description very hard to follow.

On the face of it, the fact that you can achieve the same performance from 1% of the data as from 100% can have two interpretations: you made fanastic use of the 1% to achieve performance comparable to 100%, or you made terrible use of the 100% and only achieved performance as good as using 1%.  How do we know which is the case here?

How are the cell type labels in Table 1 derived? More detail needs to be given to make this experiment reproducible.

### Soundness
2

### Presentation
2

### Contribution
1
