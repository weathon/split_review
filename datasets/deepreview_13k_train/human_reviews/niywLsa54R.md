# ViTally Consistent: Scaling Biological Representation Learning for Cell Microscopy

- Decision: Reject
- Scores: 3, 5, 8, 5

## Abstract
Large-scale cell microscopy screens are used in drug discovery and molecular biology research to study the effects of millions of chemical and genetic perturbations on cells. 
To use these images in downstream analysis, we need models that can map each image into a feature space that represents diverse biological phenotypes \emph{consistently}, in the sense that perturbations with similar biological effects have similar representations.
In this work, we present the largest foundation model for cell microscopy data to date, a new 1.9 billion-parameter ViT-G/8 MAE trained on over 8 billion microscopy image crops.
Compared to a previous published 
ViT\nobreakdash-L/8 MAE, our new model achieves a 60\% improvement in linear separability of genetic perturbations and obtains the best overall performance on whole-genome biological relationship recall and replicate consistency benchmarks.
Beyond scaling, we developed two key methods that improve performance: (1) training on a curated and diverse dataset; and, (2) using biologically motivated linear probing tasks to search across each transformer block for the best candidate representation of whole-genome screens.
We find that many self-supervised vision transformers, pretrained on either natural or microscopy images, yield significantly more biologically meaningful representations of microscopy images in their intermediate blocks than in their typically used final blocks. More broadly, our approach and results provide insights toward a general strategy for successfully building foundation models for large-scale biological data.\footnote{Correspondence: \url{kian.kd@recursion.com}, \url{info@rxrx.ai}}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors presented a new 1.9 billion-parameter ViT-G/8 MAE model, trained on over 8 billion microscopy image crops. The authors demonstrated performance boost over a smaller ViT-L/8 model in various downstream tasks.

### Strengths
- Cell microscopy analysis is an important problem and has a large impact on the future of computational pathology and bioinformatics research.
- The authors curated a dataset to only include relevant data using biological informed methods, which may be a worthwhile contribution.
- The authors performed careful tuning of model architectural and training details.

### Weaknesses
 - The methodological contribution is limited. The authors applies MAE, and evaluated on various downstream tasks. It is also known that newer algorithms such as iBOT or DINOv2 that are more effective in learning visual representations. The authors should benchmark these methods as well.
- The author’s model performance boost over a much smaller MAE-L/8 trained on RPI-93M model is very marginal, and the benchmarks do not have error bars.

### Questions
- Please address the weakness mentioned above, especially regarding the model evaluation and model training algorithm.
- Are the data, model, and training code going to be publicly available?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In this work, the authors present a large 1.9B parameter masked auto-encoder model (MAE-G/8) trained on over 8 billion microscopy image crops. In addition to scaling dataset and model size, they also explore data curation strategies and evaluation on proxy tasks for searching for the optimal representation for biologically relevant tasks from the transformer architecture. They introduce a data curation strategy that filters perturbations that do not have a statistically significant consistent morphological change in cells compared to negative controls on smaller pre-trained networks (WSL and MAE-L/8). 

Through their experiments, they demonstrate that intermediate layer representations capture 60% more linearly separable latent space which is also more biologically informative (improvements in both recall and replicate consistency) across all models pre-trained on ImageNet and models trained on microscopy datasets. The paper also presents a manually curated 40-class dataset named Anax and compare performance of their proposed methods against baselines across Anax, RxRx1 and whole genome dataset.

### Strengths
* This paper explores the following important aspects of training and scaling large foundational representation models for microscopy images such as 
  - dataset curation, 
  - proxy linear probing tasks for reasonable evaluation of models during training that generalizes to downstream performance and 
  - selection of optimal intermediate layer representation for specific downstream tasks
* The paper shares details of a manually curated dataset of 40 functionally-diverse gene groups containing 348 genes which provide a useful dataset for linear probing proxy tasks and evaluation of the models

### Weaknesses
1. While the paper shows performance improvements with model scale on microscopy images, the overall contribution is incremental and lacks sufficient ablation studies. Specifically, the paper does not explore the impact of different masking ratios during pre-training of the MAE model, or the effect of varying the patch size on the learned representations. Furthermore, the improvements observed with the larger MAE-G/8 model could be due to increased capacity rather than the proposed data curation or block selection strategies, and this is not adequately addressed with ablation studies.
2. While the authors hypothesize why their dataset curation might be better compared to other dataset curation strategies, there is no experimental comparison of different data curation strategies on microscopy datasets. For example, the authors could compare their statistical significance-based filtering approach with a simpler approach of filtering based on the magnitude of morphological change, or with a completely unfiltered dataset, to quantify the benefits of their proposed method. The lack of direct comparison makes it difficult to assess the true value of the proposed curation strategy.
3. There is very little novel contribution in the selection of optimal block for specific downstream task based on balanced accuracy on linear classification task. This is a standard practice in the field, and the paper does not introduce any new methodology or insights regarding this process. The authors could have explored more sophisticated methods for block selection, such as using a learned attention mechanism to weigh different blocks, or by using a multi-objective optimization approach that considers both linear separability and downstream task performance.
4. The gains in biological recall metric (across all 4 gene network databases) for the larger MAE-G/8 seem very modest compared to the MAE-L/8 baselines (Table 2). The reported improvements are not substantial enough to justify the increased computational cost of training and using the larger model. A more detailed analysis of the specific gene sets where the larger model performs better would be necessary to understand the practical implications of these gains.
5. The biological recall metrics for trimmed vs untrimmed versions of the MAE models trained on microscopy images are mostly the same which is counterintuitive to the argument that intermediate block representations are more useful. This suggests that the trimming strategy might not be as effective as claimed, or that the evaluation metric is not sensitive enough to capture the differences between trimmed and untrimmed models. It would be beneficial to explore other evaluation metrics that can better capture the impact of the trimming strategy.
6. The paper describes a data curation and a methodology for trimming blocks of ViT, it specifically explores the two options for training MAE models. While DINO-ViTs trained on ImageNet are a useful reference, additional experiments with DINO-ViT trained on microscopy images would be required to demonstrate the general applicability of the proposed data curation and ViT trimming strategies. The authors should have included experiments with DINO-ViT models trained on microscopy data to validate the generality of their findings.
7. The paper does not explicitly state that the dataset and model weights will be available to the public. Metrics shared on private datasets (manually curated datasets) are insufficient to use for evaluation of scientific contribution. The lack of public availability of the dataset and model weights limits the reproducibility and impact of the work.
8. While CA MAE was used as a baseline, the results and lower performance of CA-MAE compared to other baselines is not discussed. The authors should provide an explanation for why CA-MAE performs worse than other baselines, and discuss the potential limitations of this approach in the context of microscopy image analysis.

### Questions
* Dataset Availability: Will the 384-gene manually curated Anax dataset and curated Phenoprints-16M datasets be released as part of this submission?
* Model Availability: Will the ViT-G/8 model weights be released as part of this submission?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors:

Curate a large dataset (Phenoprint-16M) using a unique combination of previously introduced curation methods.
Introduce a ViT-G/8 MAE foundation model for cell microscopy imaging which outperforms the previous STOA model.
Show, using linear-probing, that mid-level representations from their model can outperform the representations from deeper layers enabling cheaper inference and improved performance.
Show that scaling to a 1.9 billion parameter MAE model continues to improve the performance for cell microscopy imaging / HCS.

### Strengths
The paper is very well written and provides clear explanations of the experiments and dataset curation. I believe that this will help future researchers better curate their own datasets.
Their foundation model outperforms the previous SOTA and would be valuable to the scientific community if made publicly available.
The required effort to produce the curated dataset and training of the large-scale model was substantial.
Although it has been shown in other domains, the evidence that mid-level representations can be of higher quality than deeper layers is valuable for this field as it reduces the cost of inference and potential fine-tuning.

### Weaknesses
It’s already well-established that scaling up models + dataset curation helps performance, these findings are not novel.
Only one method to evaluate the quality of the representations is used (linear-probing). It would be more convincing if other measures were given as well (kNN, fine-tuning). Fine-tuning evaluations on down-stream tasks using a varying number of blocks would have been useful as well. I understand that this may have been too expensive for all layers, but could have been done for a select number of layers.
No comparison is made between DINO-V2 pretrained on microscopy images versus MAE pretrained on microscopy images. Are the MAE results better because of the training method or just the training data? There’s nothing in this paper that convinces me that an MAE is more suitable than any other SSL techniques.
Why is Figure 5 comparing the ViT-G/8 MAE model against the DINO-V2 G/14 pretrained on natural images? The results in Table 2 already show that pretraining on microscopy images is critical. It feels like an unnecessary comparison. I believe a more fair comparison would be against MAE-L/8 , RPI-93M, the previous STOA.
The bolding in table 2 is inconsistent.

### Questions
Will the ViT-G/8 MAE foundation model be made publicly available? I see no mention of this.
The bolding in table 2 is inconsistent.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The study presents a novel dataset specifically designed to train foundational models for the Cell Painting assay, a high-content imaging technique used for profiling cellular phenotypes. By curating this dataset, the authors aim to address the unique challenges associated with cellular imaging, such as variations in cellular morphology and staining patterns, which require specialized data to train robust and generalizable models.

In addition to introducing the dataset, the study evaluates the effectiveness of several ImageNet-pretrained models in encoding cellular images from the Cell Painting assay. By leveraging pretrained models originally trained on ImageNet, the authors explore how well these architectures can transfer to the domain of cellular imaging.

### Strengths
This paper provides an analysis of the critical role dataset curation plays in achieving high-quality representations in microscopy imaging, including the effects of aggressive curation strategies. The work demonstrates how curatorial decisions impact the fidelity and accuracy of data representation.

The authors have presented their findings in a well-organized and accessible manner, with each section building logically on the last. The clarity of the language and structure ensures that concepts are conveyed effectively.

One of the strengths of this paper lies in its visual aids. The figures and images are thoughtfully designed to illustrate core concepts and provide visual clarity, enhancing the reader's understanding of the methodology and outcomes. 

The experimental results are convincing to some extent.

### Weaknesses
Firstly, I have some reservations regarding the model's evaluation protocol. I recommend that the authors consider using a phenotypic screening benchmark [1]. Specifically, for chemical perturbations, the validation splits should ideally be based on the scaffold, ensuring that drugs with similar structures do not appear in both the training and testing sets. Furthermore, an independent dataset is used to validate the method, which would help clearly assess the influence of batch effects. As an independent dataset I would propose to similar approach as in [1], namely, I would use the trained model and do the linear probing for mode of action prediction. 

In terms of contributions, the authors emphasize the importance of data quality. This includes aspects like the overall integrity of the data [2] as well as challenges related to imbalance and undersampling [3]. While these are critical considerations in vision or general datasets, they also apply to microscopy, so the contribution may not be particularly impactful for the research community. I do not see that those issues are specific for microscopy only, they are general for computer vision and transferable to microscopy. The microscopy-related issue is batch effects, and there is not much of their influence on the work. That is why I believe this work's novelty is extremely limited. 

Additionally, it appears that the authors have not made the pretrained model or dataset publicly available. While sharing these resources is not a requirement, their absence limits reproducibility, especially given the lack of detailed descriptions in the paper. Without these, reproducing the model’s training process—such as the steps required to train MAE on this dataset—is challenging and limits the model's utility as a foundational resource for the scientific community. I would envision seeing all the details about the quality control step. The descriptions of Appendix A are too general and to make it reproducible, they should be much more detailed. Probably a few times longer description than it is right now. 

There are also inconsistencies in the comparison of models. The models were trained with different hyperparameters, which raises questions about the validity of direct comparisons. Lastly, the results in Table 2 lack confidence intervals, making it difficult to assess whether the reported differences are statistically significant. Please add confidence intervals in the results. Additionally, would be great to see if the model trained with the same hyperparameters performs differently.

### Questions
I do not have questions about the paper per se. I do not see novel and reproducible enough to be published.

### Soundness
1

### Presentation
4

### Contribution
1
