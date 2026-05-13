# Evaluating Representation Learning on the Protein Structure Universe

- Decision: Accept
- Scores: 6, 5, 6, 8

## Abstract
We introduce \emph{ProteinWorkshop}, a comprehensive benchmark suite for representation learning on protein structures with Geometric Graph Neural Networks. We consider large-scale pre-training and downstream tasks on both experimental and predicted structures to enable the systematic evaluation of the quality of the learned structural representation and their usefulness in capturing functional relationships for downstream tasks. We find that: (1) large-scale pretraining on AlphaFold structures and auxiliary tasks consistently improve the performance of both rotation-invariant and equivariant GNNs, and (2) more expressive equivariant GNNs benefit from pretraining to a greater extent compared to invariant models. We aim to establish a common ground for the machine learning and computational biology communities to rigorously compare and advance protein structure representation learning. Our open-source codebase reduces the barrier to entry for working with large protein structure datasets by providing: (1) storage-efficient dataloaders for large-scale structural databases including AlphaFoldDB and ESM Atlas, as well as (2) utilities for constructing new tasks from the entire PDB.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work presents an open benchmark for evaluating protein structure representation-learning methods. The benchmark includes a diverse set of pre-training methods, downstream tasks, and corpora and includes experimental and predicted protein structures. The structure-based pre-training and fine-tuning datasets and tasks emphasize tasks that enable structural annotation.

### Strengths
1. Modular benchmark enabling rapid evaluation of protein representation learning methods across various tasks, models, representations, and pre-training setups.

2. Analysis of model performance across these different representations and architectures.

3. Using auxiliary tasks to improve the performance of both invariant and equivariant models.

4. Providing tools and procedures for training and evaluating models.

### Weaknesses
1. The work is missing an explanation of the limitations of the featurization schemes and pre-training tasks.

2. Would be beneficial to include a discussion about the generalizability of the benchmark results 
to the overall protein structure space, and how this translates to proteins not included in the current dataset.

3. Missing a discussion about how geometric models may be improved to surpass sequence-based models.

4. Missing information about the ease of use of the tools, and details about the computational resources required for using the benchmark.

5. Missing (i) aggregation of methods for improving model performance; and (ii) computation of uncertainties in evaluations.

### Questions
Can the work be adapted for other biological macromolecules beyond protein structures?
See, for example, the recent reference:
Performance and structural coverage of the latest, in-development AlphaFold model, 2023.
Predicting structure of proteins, nucleic acids, small molecules, ions, and modified residues. Providing a quantitative benchmark, and improving accuracy of protein-ligand structure prediction, protein-DNA and protein-RNA interface structure prediction, and protein-protein interfaces.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper focuses on the task of protein structure representation learning and aims to provide a robust and standardized benchmark for this task. 

In this paper, the authors provide different pretraining datasets, downstream datasets, pretraining tasks, auxiliary tasks, featurisation schemes, and model architectures. They cover most of the widely used training strategies, datasets, and model architectures. 

In addition, the authors run experiments using the provided code base and provide some observations and insights.

### Strengths
This paper is well-written and easy to follow.

The provided datasets, GNN models, and training strategies are comprehensive.

### Weaknesses
1. In addition to datasets etc, I think a good benchmark should also provide experimental results with well-searched hyperparameters. In such case, future researchers can directly take results for a fair comparison.
 - However, in the current version, the authors didn’t provide results on all downstream tasks.
 - In addition, I am not sure whether the hyperparameters are well-searched, since the best results reported here are still worse than some existing methods. For example, the best results on Fold (considering both with and without auxiliary tasks) are still worse than ProNet [1] and CDConv [2] which don’t use any auxiliary tasks.

2. Do ESM results in the table use pre-trained ESM weights?

3. Some other pretraining strategies are used in Geom3D [3] and ESM-GearNet [4].

### Questions
See weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors have introduced a novel framework aimed at curating datasets sourced from public repositories like PDB. Their objective is to construct benchmark datasets that facilitate the evaluation of protein structure representation. This framework takes into account various settings, including different backbone models such as various GNN-based models and diverse feature representations, to enhance our understanding of protein structure presentation. Additionally, the authors explore a wide range of pretraining tasks, including sequence/structure denoising and inverse folding, before subjecting these models to a battery of diverse downstream tasks, operating at the Alpha carbon, residue, or overall protein levels.

To support this work, the authors have generously shared an anonymous GitHub link containing scripts for data preprocessing, which enables the creation of datasets for both pretraining and benchmarking. This contribution is particularly noteworthy as it addresses a critical gap in the field of protein structure representation learning. Historically, the lack of systematically curated benchmarking datasets covering aspects such as featurization, pretraining, and downstream task evaluation has hindered progress. The absence of such a framework has made it exceedingly challenging to compare or reproduce research findings in this specialized domain.

However, there are some concerns regarding the paper's completeness. Notably, the authors have outlined a set of downstream tasks in Figure 1, yet a significant portion of these tasks remains unreported in the results section.

### Strengths
The unveiling of this framework, designed for assembling public datasets in order to generate pretraining and downstream benchmark datasets for the study of protein structure representation, is a noteworthy development.

The examination of how pretraining and featurization affect various downstream architectures and tasks proves to be engaging and insightful.

The timeliness and significance of this research topic cannot be understated, as it addresses the pressing need for a standardized framework that enables the comparison of various state-of-the-art methods using the same benchmark datasets.

### Weaknesses
Addressing the Issue of Potential Leakage:

Efforts to mitigate potential data leakage are crucial to ensuring the integrity of benchmarking results, as such leakage could introduce misleading elements into the research findings. Have you considered the removal of overlapping sequences between the pretraining datasets and the downstream testing datasets to further safeguard against such issues?

Expanding Featurization Methods:

In terms of featurization, the paper seems to primarily focus on simple feature extraction methods. It might be valuable if the authors explored the integration of the following additional featurization techniques:

    Incorporating 3D presentations, such as Uni-Mol (available at https://github.com/dptech-corp/Uni-Mol).
    Utilizing pretrained models trained on 2D data, like ESM-1b and ESM-2. Considering that Table 1 showcases results using ESM as a backbone model, which produced superior outcomes on the fold dataset, it could be beneficial to include the results for other ESM models in the table.

Diverse Downstream Tasks:

Table 1 predominantly presents results for two specific tasks. However, it appears that several other downstream tasks have not been included in this experiment. It is worth noting that many of these unreported downstream tasks are of substantial importance and are conspicuously absent from the paper. Is there a particular reason for not considering these tasks, and could they potentially be included to provide a more comprehensive view of the research findings?

### Questions
1. Could you please address the potential leakage as discussed in the weakness comments?

2. Could you please consider additional featurization as pointed out in the weakness comments?

3. Could you please complete the experiments and provide the results with the downstream tasks that are missing in the paper?

### Soundness
3 good

### Presentation
4 excellent

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
The authors introduce a large suite of benchmarks for evaluating learned embeddings of proteins. Included are node-level evaluations (at the level of individual residues, e.g. inverse folding, metal binding site prediction) and graph-level evaluations (at the level of the entire protein, e.g. fold classification). The authors also provide a number of software tools, including dataloaders for various pretraining tasks. Finally, they evaluate selected architectures on various pretraining task/benchmark combinations.

### Strengths
New benchmarks are always welcome, and there is also great value in consolidating existing benchmarks. This paper does that well, as the selection here is quite broad, with good coverage. I appreciate the inclusion of both node-level and graph-level evaluations. Within each category, each choice of benchmark is accompanied by a specific rationale, which is also a strength. The documentation of the codebase also seems clear and easy to follow.

### Weaknesses
It would have been nice to see baselines for all of the downstream tasks in the benchmark using the tools in this software suite (or, lacking that, even scores copied from their respective papers if needs be). Certain tasks like "reaction class prediction" are currently missing. Part of the value-add here is the ease of running experiments on all of these tasks, and that isn't currently demonstrated in the current version of the manuscript. Also, consolidated baseline scores are useful sanity checks for reproduction experiments down the line.

Miscellaneous stuff:

- Please provide details about the confidence intervals in Table 2.
> whereas pLDDT prediction and structure denoising benefit invariant models the most
- I don't really understand what the basis of this claim (^) is. All four models do approximately as well in the pLDDT column, e.g.

### Questions
In Table 3, inverse folding (a downstream node-level task) is listed alongside four other tasks explicitly identified as pretraining tasks above. Is this intentional? 

Are the experiments in Table 2 at all realistic? I don't think these tasks ever be attempted using models with no pretraining at all in practice. Also, the ESM model without any pretraining can hardly be called an ESM model at all.

Did you consider adding any restrictions on the interfaces between model embeddings and the downstream tasks? If the goal is to evaluate the embeddings themselves, it seems to me like there should be an attempt to standardize e.g. the size of the task-specific MLPs used.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
