# CellPLM: Pre-training of Cell Language Model Beyond Single Cells

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
The current state-of-the-art single-cell pre-trained models are greatly inspired by the success of large language models. They trained transformers by treating genes as tokens and cells as sentences. However, three fundamental differences between single-cell data and natural language data are overlooked: (1) scRNA-seq data are presented as bag-of-genes instead of sequences of RNAs; (2) Cell-cell relations are more intricate and important than inter-sentence relations; and (3) The quantity of single-cell data is considerably inferior to text data, and they are very noisy. In light of these characteristics, we propose a new pre-trained model, $\textit{CellPLM}$, which takes cells as tokens and tissues as sentences. In addition, we leverage spatially-resolved transcriptomic data in pre-training to facilitate learning cell-cell relationships and introduce a Gaussian prior distribution as an additional inductive bias to overcome data limitations. $\textit{CellPLM}$ is the first single-cell pre-trained transformer that encodes cell-cell relations and it consistently outperforms existing pre-trained and non-pre-trained models in diverse downstream tasks, with 100 times higher inference speed on generating cell embeddings than previous pre-trained models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a language model that learns from single-cell RNA sequencing (scRNA-seq) data. Their model takes as input a series of genes and their expression values, aggregates them, and then feeds them through an embedding matrix to create cell-level embeddings. These embeddings are then fed to a transformer along with other cell embeddings. The model is trained using the variational autoencoder (VAE) objective with a Gaussian prior, which includes a reconstruction term, a conditional prior term, and a cluster prior term. Unlike previous models, the authors leverage spatial data and show that their model outperforms previous models on several tasks.

Further, they claim that their method is faster than previous methods -- the reason for this is because of collapsing the model input down to cell level representations as opposed to feeding individual gene level tokens

### Strengths
Overall, the paper is clear and easy to follow, but several important details must be included in the text, such as the prior estimation for $z_i$ and $y_i$, and the dataset details and experimental setup. It is also important to note how the comparisons were standardized.

Other strengths of the paper include:

* It explores spatial + gene expression data using LLMs.
* It models the task at a cell level as opposed to a gene level (questions in weakness).
* It explores a smooth latent space for this task.

### Weaknesses
The source of the pre-training gains is unclear, given the current presentation. The authors restrict the gene set to a subset of 13,500 genes, but it is not specified which genes are included or whether they are protein-coding or non-protein-coding. The dataset section should be expanded to include details on how the data was preprocessed.

* **Cell masking:** The authors aggregate cell genes using their embeddings and pass these tokens to the LLM. What does it mean to mask a cell? In the diagram, the cells are masked, but in the equations, the genes are masked. Assuming the masking is at the gene level and samples are taken from the same batch, wouldn't other cell genes have the necessary information to impute the cell? In essence, is the model cheating?
* **Single-cell operation:** How would the model operate if you only have a single-cell sample? Would you feed a single cell token to the LLM and use the latent representation?
* **Sequence length:** I'm curious how the model performance would change if you vary the "sequence length". For example, in your batch, do you have the same number of genes for each cell?
* **Spatial information:** How is the spatial information leveraged here? Is it through the positional encoding? What would happen if this positional encoding is removed?
* **Positional Encoding:** It is not clear if this had a significant improvement in the quality of representation learnt.
* **Comparison with previous models:** Although the authors compare with previous single-cell models, these models only operated on gene expression data and fed a single cell at a time (i.e., the sequence dimension is the genes within the cell as opposed to other cells, as done in this work).
* **Benefit of pre-training:** The benefit of which part of the pre-training is the result of the improvements shown in the result section is not clear from the current presentation. Also, the authors don't compare with scVI (although they do cite the method) or even a simpler baseline like HVG.
* **Gene interactions:** Does the model learn gene level interactions? By feeding cell-level representations, how can this be assessed?
* **Batch Token:** How would you transfer the model to a dataset which has a new batch token are these fine-tuned as well?

### Questions
See weakness section

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors propose a CellPLM to address certain issues identified in previous work. Specifically, the proposed CellPLM considers cells as tokens and tissues as sentences, whereas previous work treated genes as tokens and cells as sentences. The CellPLM is designed to learn the relationship between cells. Additionally, they adopt a Gaussian mixture prior distribution to overcome the out-of-distribution problem. Experimental results show CellPLM consistently  outperforms previous work.

### Strengths
1. The proposed method effectively addresses the issues contained in previous work.

2. Experimental results demonstrate that CellPLM consistently surpasses the performance of previous methods.

### Weaknesses
1. The experiments in this paper are not sufficient. For instance, ablation studies are needed to verify the effectiveness of each module. Specifically, the contribution of the Gaussian mixture prior and the transformer encoder architecture needs to be isolated and quantified through targeted ablation experiments. It is unclear how much each component contributes to the overall performance gain.

2. Although the improvement in experimental results is very significant, further analysis is needed to determine whether it is due to the relationships between cells. The paper claims that the model learns relationships between cells, but there is no direct evidence to support this claim. The performance gain could be due to other factors, such as the increased model capacity or the specific parameter tuning, rather than the explicit modeling of cell-cell relationships. More analysis is needed to isolate the effect of cell-cell relationships.

3. I'm not sure if the Gaussian distribution can achieve the expected effect in this method, this point also needs to be validated through experiments. The choice of a Gaussian mixture prior is not sufficiently justified. While it is mentioned that it addresses the out-of-distribution problem, it is not clear why a Gaussian mixture is the optimal choice. The paper needs to provide a more detailed analysis of the prior distribution's impact on the learned representations and downstream performance. It is also unclear how the number of mixture components is chosen and whether this choice is robust.

### Questions
see Weaknesses

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a pre-trained language model CellPLM, the first single-cell pretrained language model that utilizes cell-cell relations.

### Strengths
- This paper is well written. Provide enough introductions for people without much background in this field.
- The proposed method is sound. Taking cell-cell relationships into the modeling is a well-motivated idea.

### Weaknesses
I integrate the questions and weaknesses in this section since I have very little bio background and all the weaknesses I identified are based on my own understanding of this area, which could be incorrect.

- Where do the huge speed improvements of CellPLM come from? It is because CellPLM aggregates the genes within each cell directly in the embedding layer, so it only needs to process dramatically shorter input sequences. So basically, CellPLM works at the cell level, while baselines work at the gene level. If this is true, the Claim "with 500x times higher inference speed compared to existing pre-trained models." is unfair since you are compared to a task that your model is specifically designed for. At least it should be reduced to "with 500x times higher inference speed when generating cell embeddings".

- Why does the CellPLM model from scratch outperform most of the pre-trained baselines? This seems to be really unrealistic to me. Is it because your model is much larger than the baselines or cell-level LM is more suitable for the tasks? If the randomly initialized model already outperforms most of the baselines, then we need to re-evaluate the claims in the paper, since the performance boost may mainly result from the Transformer architecture instead of the specific model designs you mentioned.

- There is a lack of ablation study to show the effectiveness of each proposed component.

### Questions
Please see the Weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
A novel pretrained single-cell transcriptomic model CellPLM is proposed. It takes cells as tokens and tissues as sentences as opposed to existing counterparts which usually takes genes as tokens and cells as sentences. By leveraging spatially-resolved transcriptomic data in pre-training, cell-cell relationships can be learned. Empirical studies demonstrate CellPLM outperforms prior arts in diverse downstream tasks and has higher efficiency in inference.

### Strengths
++ The study adapts the large language model pretraining techniques to the single-cell transcriptomic data, but uses a novel analogy to better capture the cell-cell relationships. 

++ The paper is well organized and easy to understand. Technical details are given clearly.

++ The work provides a new direction for training single-cell foundation models and demonstrates its advantages against existing works. It will make a significant contribution to the community.

### Weaknesses
-- The motivation and benefit of using a VAE-like architecture is not clear. Specifically, the paper does not adequately justify why a variational approach is necessary when the primary goal is representation learning rather than generative modeling. The added complexity of the VAE, including the Gaussian mixture prior, should be more thoroughly motivated, especially given the potential for simpler architectures to achieve similar representation quality.

-- Two paradigms of modeling single-cell data should both have their pros and cons but the authors do not discuss them thoroughly. The paper presents a novel approach of using cells as tokens and tissues as sentences, but it lacks a detailed comparison with existing methods that use genes as tokens. A more in-depth discussion of the trade-offs between these two approaches, including their respective strengths and weaknesses in different downstream tasks, is needed.

-- The benefit of using Gaussian mixture distribution as the prior of latent embedding is not validated. While the authors propose a Gaussian mixture prior, they do not provide sufficient empirical evidence to demonstrate its advantage over simpler prior distributions, such as a standard Gaussian. The paper should include ablation studies to isolate the effect of the Gaussian mixture prior on downstream performance. Furthermore, the specific parameters of the mixture model and how they are optimized should be clarified.

-- It is not clear which parts (e.g., the combination of two types of single-cell data, the VAE-like architecture or the novel paradigm of single-cell data modeling) contribute the most to the performance gains against other existing foundation models (e.g., scGPT, scBert, etc.). The paper does not provide a detailed ablation study to disentangle the contributions of the different components of the proposed model. It is unclear whether the performance gains are primarily due to the novel tokenization strategy, the VAE architecture, the use of spatial data, or a combination of these factors. A more thorough analysis is needed to understand the relative importance of each component.

### Questions
1. Based on different modeling paradigms of scRNA-seq data, the proposed CellPLM may have its pros and cons compared with existing foundation models (e.g., scBert, scGPT, etc.) using genes as tokens. In which downstream tasks CellPLM may be/not be a better choice?
2. Is the batch embedding learnable? If not, how are they defined?
3. What's the motivation and benefit of using the VAE-like architecture for CellPLM when the goal is not to learn a generative model? Is there a problem if a typical transformer architecture plus a head (without Gaussian prior latent embedding) is employed?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
