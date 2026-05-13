# Few-Class Arena: A Benchmark for Efficient Selection of Vision Models and Dataset Difficulty Measurement

- Decision: Accept
- Scores: 5, 5, 6, 6

## Abstract
We propose \fca~ (\FCA~), as a unified benchmark with focus on testing efficient image classification models for few classes. A wide variety of benchmark datasets with many classes (80-1000) have been created to assist Computer Vision architectural evolution. An increasing number of vision models are evaluated with these many-class datasets. However, real-world applications often involve substantially fewer classes of interest (2-10). This gap between many and few classes makes it difficult to predict performance of the few-class applications using models trained on the available many-class datasets. To date, little has been offered to evaluate models in this \fcr~. We conduct a systematic evaluation of the ResNet family trained on ImageNet subsets from 2 to 1000 classes, and test a wide spectrum of Convolutional Neural Networks and Transformer architectures over ten datasets by using our newly proposed \FCA~ tool. Furthermore, to aid an up-front assessment of dataset difficulty and a more efficient selection of models, we incorporate a difficulty measure as a function of class similarity. \FCA~ offers a new tool for efficient machine learning in the \fcr~, with goals ranging from a new efficient class similarity proposal, to lightweight model architecture design, to a new scaling law. \FCA~ is user-friendly and can be easily extended to new models and datasets, facilitating future research work.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper tackles the problem of choosing image classifiers for tasks with only a small number of categories ("Few-Class"). To do so, they introduce a new benchmark, termed "Few Class Arena" (FCA) on which they train and evaluate a range of models on subsets of various full datasets (e.g wit so-called sub-models trained on between 2 and all 1k ImageNet categories). The FCA benchmark is open-sourced with code available on GitHub. The paper provides detailed discussion of how the open-source package can be used for model selection in the few-class setting.

Overall, the authors show that models trained on specific sub-classes (sub-models) are better than models trained on the full dataset and evaluated on the same sub-classes, across model sizes. They further show that there is no single best model architecture for a given dataset, and that training models on different datasets result in different rankings of architecture. The authors also propose a "dataset difficulty" metric which can be computed without training a model, and correlates well with the few-class performance of a model on a dataset.

### Strengths
- Tab 1 / Fig 2b shows the results when training different base architectures on different classification datasets from scratch. Interestingly, not all results are correlated with the trend on ImageNet-1K, indicating the optimal architecture choice depends on the dataset.
- The code is open sourced and well documented. It seems that it would be simple for a researcher to reproduce the authors claim with limited effort (though I have not run the code myself).
- It is interesting that sub-models consistently outperform full models on ImageNet. The fact that full models have seen more training datapoints in total may have compensated for fewer classes, which makes the result not totally intuitive.

### Weaknesses
My main issue with this paper is in overall utility. The high level goal of the paper is to provide a tool with which practitioners can select a model (dominantly through the lens of model *architecture*) for a few-class classification task. The tool basically allows authors to train a model (with most results presented from scratch) on subsets of a given dataset. However, this does not align with the practical problem to me, where practitioners might take a model pretrained on a large amount of *data* (e.g DINOv2 or CLIP) is finetuned for a given task (note that lightweight variants of these models are also open-source).

Given that this paper is predominantly an empirical examination which proposes a practical open-source library, I feel that the lack of experiments with pretrained models prevents acceptance.

Other issues:

- The citation format makes the main text quite difficult to parse
- L52: Main text does not seem to describe Figure 1 accurately?
- There is no discussion of few-shot literature, which is at least tangentially related to this problem

### Questions
* I may have missed something, but I cannot understand exactly how the proposed difficulty metric is intended to be used?
* The proposed difficulty metric seems expensive to compute, with pairwise similarity scores required for large subsets of the data. How does this compare to the cost of conducting a single model training run?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a benchmark tool called Few-Class Arena to benchmark models on different datasets with smaller number of classes (e.g. < 10) and propose a similarity metric called SimSS to measure dataset difficulty measure. They show that ResNet family models trained on full ImageNet 1K classes show reduced performance when tested only for few ImageNet classes (< 10 classes). On the other hand, the same models when trained on smaller number of ImageNet classes from scratch show higher performance on these classes when compared to models trained on all classes of ImageNet 1k. They show that the proposed SimSS metric can serve as a proxy to estimate the upper bound accuracy of model performance on few-class datasets.

### Strengths
•	Addressed an important problem by proposing the benchmarking tool.

•	The tool is designed to be user friendly and allows to run wide range of experiments by setting few hyper-parameters. The tool allows to benchmark on custom models and datasets.

•	Provided a behavioral understanding between models trained on large number of classes vs smaller number of classes in the few-class regime.

•	The proposed similarity metric shown to be linearly corelated with the model performance on small number of classes. Such proxy helps to save computation cost and time of conducting various experiments.

### Weaknesses
Despite focusing on an interesting problem setting, the analysis shown in the paper has limited scope. Authors shown experiments on models evaluated or trained on smaller number of classes, however there are no details discussed on how these few classes have been selected and how semantically close these few classes to each other? Would the analysis presented differ by choosing the those few classes differently?

The aspect of transfer learning has not been discussed. It is a common practice to finetune ImageNet pretrained models like ResNet50 or ViT, or recent foundation models like CLIP and DINOv2 to different downstream tasks that include adapting or finetuning them on few classes. The analysis presented in the paper is missing this exploration. Is it better to train the models from scratch on the few classes or finetuning these models work better for few classes? Does SimSS score also align on the finetuned models?

To compute SimSS, a score called Nearest Inter-Class Similarity requires a nearest class (C_hat) to the target class (C), it is not clear how this C_hat is acquired.

Overall, I appreciate the motive and tool for benchmarking few-class regime, however the analysis presented in the paper is incomplete, and I suggest authors to extend their analysis.

### Questions
1. For FC-Full, when N_{CL} decreases, how to make sure that model predicts only few classes? Are the logits of those few classes are selected to get the prediction and discard logits of all other classes?

2. If a user has a custom dataset with few classes and want to find a model that works better on this custom dataset, it would be helpful to have an explanation on how this benchmark can assist the user in this case.

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
3

### Summary
This paper presents a new benchmark for the “few-class” problem, which  is a classification problem with very few classes. Most of the scientific literature focuses on datasets with many classes while practitioners often encounter the few-class scenario. The benchmark consist of several selected datasets and several settings, such as training on large set of classes and evaluating on a smaller set, and popular vision models are evaluated and compared. Finally, an analysis of what happens in few-class regimes is proposed.

### Strengths
- The benchmark is well executed and will be useful for “few-class” adaptation research. There are many models evaluated with many datasets and the analysis is thorough. In particular, the author study in depth the evolution of the performance of models trained on large set of classes compared to specialized models, as a function of the number of classes, and show the importance, and therefore propose a metric for evaluating this adaptation.

- The similarity benchmark is a nice addition. It correlates well with the performance while being easy to evaluate and with a modest cost.

- The presentation and writing are very clear. The figures are very informative.

### Weaknesses
 - The motivation behind few-class evaluations is not fully convincing. In practice, one will take a large model and fine-tune it (without the classification layer) to a target set of classes, hence obtaining a specialized model. Evaluating the capabilities of a full model on few-class is only interesting when there are too many subsets to consider ? When does that happen in practice, and could you just not use small adaptation layers on top of frozen backbone for each of the subsets ?

 - One thing that is missing from the paper is a recommendation for practitioners on which vision model to use for someone interested in the few-class problem. Basically discussing in more details the results from Table 1 and providing comparison between models in Section 4.2 and 4.3. One interesting question is, do models that perform really well on the many classes setup are the same that also perform well on the few-class setup ?

 - Some of the findings in the paper are fully expected. The fact that a model specifically trained on the target subset of classes perform better that a larger model trained on a superset is not very surprising or novel.

### Questions
- What original research do you expect will use this benchmark and what do you hope it will achieve or unlock ?

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
3

### Summary
The paper introduces a benchmark designed to evaluate and select efficient image classification models in scenarios with a limited number of classes. This setting, common in real-world applications (e.g., 2-10 classes), contrasts with widely used benchmarks like ImageNet and COCO, which involve hundreds or thousands of classes. The paper presents FCA as a tool to help researchers and practitioners efficiently select models for few-class tasks. The paper coins the term ``few-class regime'' and presents some interesting non-intuitive insights regarding the performance of models that are pre-trained with many class datasets and then applied in few-class settings.
In addition, they introduce a dataset difficulty metric by inverting image similarity measured via CLIP and DINOv2 features.

### Strengths
1. The necessity of a few-class benchmark is well-motivated by a strong finding that models pre-trained on many-class datasets perform worse than expected on few-class datasets which is an issue not addressed in literature thus far.
2. The paper presents some interesting insights that contradict expected model behavior based on intuition.
3. The authors provide a ready to use code base integrated with other frameworks and libraries ensuring usability.

### Weaknesses
1. The scope of the study only covers image classification, while it is in principle also applicable to dense prediction tasks where object classes are present (e.g., object detection, semantic segmentation). It would be insightful if the same findings hold for these tasks. The authors could add a discussion or experiments (if available) for other vision tasks.
2. The experiments cover classification tasks based on supervised (pre-)training. However, there is an increasing trend that classification models are fine-tuning based on self-supervised pre-trained models. This paradigm is not covered in this study, and therefore, the findings are limited to the more traditional fully supervised paradigm. The authors could discuss these aspects or add experimentation with self-supervised pre-trained models (if available).

### Questions
1. (Related to W2) The finding that the scaling law w.r.t. model size is violated for submodes is interesting. I would be curious if this only applies to supervised training or also to self-supervised pre-training combined with minimal fine-tuning or linear probing. Did you conduct any experiments into this direction or do you have an intuition on that?
2. You mention that you conducted experiments on different architectures such as ResNet’s and ViT’s. However, the results are presented in an aggregated way. Did you find any significant differences between model architectures? Do the findings of Fig 1 equally apply for both architectures?
3. I agree with your description and ad-hoc interpretation of Fig. 5. However, I am missing a discussion on why we see the low correlation for DCN-Full. Do you have any interpretation of this?


**Minor comments:**

- The correct use of author-year citations would improve readability. I.e.: Author (2024) for in-text citations and (Author, 2024) elsewise.

### Soundness
3

### Presentation
3

### Contribution
3
