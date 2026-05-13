# A General Single-Cell Analysis Framework via Conditional Diffusion Generative Models

- Decision: Reject
- Scores: 8, 6, 6, 6

## Abstract
The fast-growing single-cell analysis community extends the horizon of quantitative analysis to numerous computational tasks. While the tasks hold vastly different targets from each other, existing works typically design specific model frameworks according to the downstream objectives. In this work, we propose a general single-cell analysis framework by unifying common computational tasks as posterior estimation problems. In light of conditional diffusion generative models, we introduce scDiff through the proposed framework and study different conditioning strategies. With data-specific conditions, scDiff achieves competitive performance against state-of-the-art in various benchmarking tasks. In addition, we illustrate the flexibility of scDiff by incorporating prior information through large language models and graph neural networks. Additional few-shot and zero-shot experiments prove the effectiveness of the prior conditioner on scDiff.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors present scDiff, a diffusion model for single cell sequencing tasks.
They start off by phrasing a variety of tasks within the single cell sequencing world as probabilistic modeling tasks, which may involve a shared generative model of single cells and a generic mechanism for conditioning.
Once they establish that -correct- link, they proceed to utilize diffusion models to build such a generic "prior" over single cells, and pair it with a conditioning mechanism per layer in order to be able to inject specific conditions or knowledge into the model.
Once they establish that modeling framework, which closely follows the diffusion modeling best practices, the authors proceed to test their model in a variety of tasks by utilizing conditioning in various was.

In their tasks ranging from conditioning on prior knowledge, cell type inference, and imputation, they show that the model is broadly applicable and performs well.

### Strengths
I want to praise this paper, it does a lot of things well that I've been hoping to see in the field.

Casting single cell sequencing modeling as a generative model is not a novelty per se, various VAE frameworks have blazed that trail, but utilizing a diffusion model sheds a particular light on this that is both useful and performant.

This paper stands well as a baseline introduction into what can be done with diffusion models as they currently are and executes neatly on the idea of using the conditioning model per layer to map to a variety of tasks.
It is also important that the paper insists on the unified model ov er all these tasks and realizes that conditioning is the one mechanism to express different tasks, but unifies the model which can modularly be decomposed from the conditioning aspect.

The paper is also overall well written and attributes ideas well, and the application domain will benefit from its existence.

### Weaknesses
I have three nitpicks to note in the paper.

First, the application here is straightforward, no core ML innovation was necessary to execute this project.
However, I think that realizing how diffusion models map to this important modeling domain and executing the basics well once absolutely justifies this well-executed paper, but I wanted to note that it is not innovating dramatically.

Second, the authors keep using the term "casting single cell tasks as posterior inference" throughout the paper, but do not really perform much inference in truth beyond the classical training scenario of diffusion models. 
I would prefer if they used language like "we cast these tasks as probabilistic modeling using a shared model", since inference is not the heart of the story here and in fact is relatively generically solved since we do not really inspect posterior distributions per layer over specific conditions and so on.  This is a minor point, but since I anticipate this paper to be read a lot it would be good to use that language carefully.

If I can add a third nitpick, the imputation task is not entirely correct in how it is phrased as a conditioning setting. 
If the authors inspect their predictive distribution, it probably contains outputs beyond the ones that are visible.
I understand the conditioning mechanism injected per layer will increase affinity towards imputing the right thing, but it's not exactly p(x|m*x) that the authors are modeling, but rather a p(x*|m*x) where x* is sampled from "some" distribution conditioned on embeddings of x*m.
I want to point out that I find this to be a fine approximation to the task and not a reason to reject the paper, but I would prefer the authors to call it out as such and leave space for future improvements.

### Questions
I would be curious to see the scaling behavior of the systems the authors study given different dataset sizes.

Diffusion models tend to be data and compute hungry, how do they behave here? Can we apply them on one screen?
Do we have to pre-retrain them broadly?

I am sold on the modeling framework and think this paper will stand on its own, but the field would get more value out of it if we inspected these questions of data efficiency.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
- This work applies a conditional diffusion model to scRNA-seq datasets.
 - The proposed model incorporates previously described innovations (e.g. the simplified, unweighted objective, injecting the diffusion time step into embeddings, reverse mixing etc.)  
  - Architecture choices are not directly validated/ explored for scRNA-seq datasets.
  - Authors showcase the performance of this model on a range of tasks that fit into the form of estimating $P(X|C)$ where $X$ is expression data, and $C$ is some generic conditioning information.

### Strengths
- S1. Authors apply diffusion models to scRNA-seq datasets, and tackle a wide range of tasks. 
- S2. At face value the results are quite impressive.

### Weaknesses
 - W1. The model description is more of a sketch (e.g. even Fig 1) than a self-contained and unambiguous description. More detail about how and what conditioning information is used for each task is lacking. For instance, it's unclear how the various conditioning inputs (cell type, batch, perturbation status, etc.) are encoded and integrated into the diffusion process. The manuscript lacks a precise definition of the conditioner's architecture and its interaction with the diffusion model's latent space. This makes it difficult to understand the exact mechanism by which the model learns to generate data conditioned on these inputs.

 - W2. Given that this is an application to a new domain, rather than evaluating it on a suite of tasks with the same mode., it might make sense to characterize the model and the validity of those choices for scRNA-seq datasets. For example, the choice of a 6-layer encoder and 1-layer decoder is not justified for this specific data modality. An analysis of how different architectural choices (e.g., number of layers, activation functions, attention mechanisms) impact performance on scRNA-seq data would be valuable. Furthermore, the impact of the diffusion process itself on the learned representations is not explored. It is unclear if the diffusion process is actually beneficial for the downstream tasks, or if a simpler model would suffice.

 - W3. The authors tune their own model, and report performance with default values for competing methods. I appreciate the transparency in communication, but it makes it harder to interpret results. Perhaps using benchmarks where train/test splits are fixed, and other methods are reported with tuned performance would be more informative. [Openproblems](https://openproblems.bio/) curates such benchmarks on a wide variety of such tasks for many easy-to-access datasets. Performing some evaluations with those datasets and comparing the pre-defined metrics on those tasks against the leaderboard there would certainly boost my confidence in results.

 - W4. While there is an impressive number of tests performed with scDiff coming out on top on all fronts, it is unclear why there is a marked improvement. In particular details about the training and testing procedure are missing at a granular-enough level to reproduce results. For example, the Jurkat dataset consists of ~3,000 cells and ~12,000 genes. Was the network trained from scratch on this? Was any preprocessing / feature selection used to report results on that dataset? The lack of detail regarding the training procedure, such as batch size, learning rate, and optimization algorithm, makes it difficult to assess the robustness of the results. Furthermore, the specific method for generating samples during inference for each task is not clearly defined, making it challenging to reproduce the reported performance.

### Questions
- Q1. Some of the datasets have a very small number of cells (~3000 for Jurkat). Can the authors clarity in which cases was the model trained from scratch (i.e. with randomly initialized weights)?

 - Q2. Eq. 1 uniform prior assumption seems to be a strong over-simplification. Would this hurt on unbalanced datasets (e.g. when considering cell type classification as in appendix C)?

 - Q3. What is $L$ here? Is it simply the number of distinct conditions?
    > The goal of each conditioner is to extract a set of L numerical representations of an input condition c. 
 
 - Q4. In the same section about the conditioner, can you provide examples for:
    > The mapping here can be designed to suit the specific needs of different input types.

 - Q5. If there are only ~30 cell types in the dataset (e.g. Liver in Fig. 5), how is any high (e.g. 64 or 128 dim) dimensional embedding from LLM's helpful for the model for one-shot classification?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a novel single-cell analysis framework, scDiff, which approaches various computational tasks through posterior approximation. scDiff comprises three key components: a conditional diffusion model for posterior approximation, a series of encoders that enocod cell conditions into numerical vectors, and a cross-attention unit that combines these condition embeddings. scDiff also has an adaptable structure, allowing the incorporation of text as prior knowledge. 

To evaluate the model's performance, the authors conducted experiments covering a range of benchmarking tasks. These tasks included cell annotation, prediction of missing values, identification of novel cell types, and annotating cells using just one or a few samples. The results demonstrated that scDiff achieves competitive performance when compared to state-of-the-art models across multiple datasets and task categories.

### Strengths
The authors tackle a range impactful problems in the field of single-cell analysis, including tasks such as cell type annotation, imputation, novel type identification, and perturbation prediction for scRNA-seq data. Typically, each of these tasks would demand a separate model.

Despite the existence of extensive literature on each of these individual problems, the authors suggested a unifying framework that encompasses multiple benchmark tasks within a single, cohesive framework.

### Weaknesses
 **Major:**

- *Novelty:* It is not clear what the novel aspect of scDiff model is from a machine learning perspective. Although the authors introduced posterior inference as a novel unified framework for several single-cell tasks, posterior inference through variational or generative processes is a well-explored area, even within the field of single-cell analysis.

- *Contributions:* The reported results in the experimental sections do not convincingly demonstrate that scDiff significantly outperforms relevant models for the specific tasks at hand. Furthermore, the authors have not quantified the computational cost associated with having a unified model that covers multiple tasks, particularly in relation to the observed improvements. While the enhanced performance might not necessarily stem from the model's extension, it could be attributed to factors like the use of the diffusion process, attention units, or different implementations.


**Minor:**

- Some of the experimental settings descriptions, such as those outlined in section 4.2.1, are not clearly explained and can be rather confusing. Additional clarification is needed in this regard.

- In Table 1, it would be valuable to include the number of clusters and chance level for each dataset to provide a more comprehensive understanding of the results.

### Questions
- In the context of the missing value imputation task, the assumption that all zero-expressed genes are missing and no actual zero-expressed genes exist may not be entirely accurate. It might be more biologically relevant for the model to learn the mask matrix, $M$, instead of assuming that $x_g > 0$. In biology, we know that non or less-expressed genes can still play a marker role in some cell types.

- Can you provide further elaboration on Equation 10? It is not entirely clear why the single-cell data are encoded using the suggested *"TimeEmbed"* function.

- Why does scDiff utilize a linear encoder / decoder?

- It would be insightful to understand the computational efficiency of using a model like scDiff compared to an equivalent model designed solely for solving one or a few downstream tasks.

- In Table 2a, for the missing value imputation task, the authors reported correlation values. However, is not the primary goal to approximate the value of gene expression rather than capturing the overall expression pattern (correlation at the gene population level)? It might be more informative if the authors report the average (normalized) error.

- In Table 2, it would be beneficial to include the number of genes used for each task per dataset.

- For the study in Table 2a, is there any consideration for zero-expressed genes?

- What is the chance level in Figure 2? Is not the number of cell types limited in this context?

- In Figure 3, why the top and bottom subfigures do not reveal the same relative performance pattern? Could you provide further elaboration on how they are related to each other?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper tries to form three common single-cell analysis, cell labeling, expression completion and knowledge transfer, into a unified posterior estimation problem by leveraging the ability of learning data distribution of diffusion model. The idea is general reasonable and proved effective compared with baselines, but the paper still needs to be further clarified and improved.

### Strengths
(1) The problem that the paper tries to address is significant in the field of analyzing single-cell data.
(2) The idea of forming three major tasks of analyzing single cell data into posterior distribution is doable.
(3) The paper illustrate the method clear in its Figure 1.
(4) The datasets employed to evaluate the method is comprehensive.

### Weaknesses
 (1) The paper mentions using LLMs as the prior, but why not compare the proposed method with LLMs-based ones, such as those in [1]? It's unclear if the 'LLMs' mentioned refer to natural language models or large-scale pre-trained models on single-cell data. A comparison with relevant single-cell pre-trained models is necessary to contextualize the performance of the proposed approach.
(2) From the part of the paper under Section 2.2 to equation (9), the author used a large amount of words to introduce basics of the diffusion model. I would suggest the author to move this part to appendix as this is not the contribution of this paper. The lengthy introduction of diffusion models distracts from the core contributions and should be placed in a supplementary section.
(3) For the conditioner part, how does the cross-attention exactly used? Will it be able to automatically detect which task the model is focusing on? The mechanism of cross-attention and its ability to discern different tasks requires further clarification. It's not clear how the model utilizes the condition embeddings to focus on specific tasks.
(4) There are quite a few confusing part in the paper. For instance, the paper claims that it forms the task into a posterior estimation, but how the prior is used in the model? I don't think the paper explicitly explains this. Also, for cell labeling and knowledge transfer, I don't thinks it's a generation task so that generative model is a good practice in this case. Intuitively cell lebeling and knowledge transfer is more like a prediction task to me. The formulation of cell labeling and knowledge transfer as posterior estimation needs more justification, as these tasks are typically approached as prediction problems rather than generative ones. The role of the prior in the model is also not clearly defined.
(5) I don't feel the strong motivation of using a attention mechanism to help the model learn specific tasks. To me it's more like the proposed method assembles three tasks very hard to let the model to learn. Therefore, the proposed method lacks novelty as each individual task can still be solved in the same framework. The motivation for using cross-attention for task-specific learning is weak. It appears that the method is forcing three separate tasks into a single framework, which may not be the most effective approach. The novelty of the proposed method is questionable, as each task could be solved individually with similar frameworks.
(6) I'm also confused about the current formation of the x_\theta(x_0, \epsilon, c, t). Why not just follow the standard way as in CV that just uses U-Net? I strongly suggest the author to clarify the motivation of their model structure. The choice of model architecture, particularly the deviation from a standard U-Net, is not well-justified. A clear explanation of why a U-Net was not used and the motivation behind the current architecture is needed.

### Questions
Please refer to my comments in "Weakness".

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
