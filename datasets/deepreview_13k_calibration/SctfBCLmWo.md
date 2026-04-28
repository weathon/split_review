# A Decade's Battle on Dataset Bias: Are We There Yet?

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8

## Abstract
We revisit the ``dataset classification'' experiment suggested by Torralba and Efros a decade ago \cite{Torralba2011}, in the new era with large-scale, diverse, and hopefully less biased datasets as well as more capable neural network architectures. Surprisingly, we observe that modern neural networks can achieve excellent accuracy in classifying which dataset an image is from: \eg, we report 84.7\% accuracy on held-out validation data for the three-way classification problem consisting of the YFCC, CC, and DataComp datasets. Our further experiments show that such a dataset classifier could learn semantic features that are generalizable and transferable, which cannot be simply explained by memorization. We hope our discovery will inspire the community to rethink the issue involving dataset bias and model capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a modern version of the dataset classification experiment proposed by [Torralba & Efros (2011)](https://people.csail.mit.edu/torralba/publications/datasets_cvpr11.pdf): training a neural network to assign images to the right dataset it comes from. SVM reached reasonable accuracies by then on image classification datasets -- indicating dataset bias exist.

This paper experiments with modern backbones (eg, ConvNeXt and ViT) on modern large-scale datasets (eg, WIT, LAION), finding that dataset classification becomes even easier -- dataset bias is easier to spot by models despite the datasets being diverse and large-scale. The authors tried to explain this phenomenon, but it turns out the bias is not attributed to low-level clues and models do not simply memorize the data -- they learn high-level signals. The authors also show that self-supervised representations -- which tend to be good in semantics -- also work well on dataset classification, indicating that the dataset bias can be attributed to some high-level pattern.

### Strengths
- This paper presents a timely revisiting of an old question: how biased are ML datasets in the view of ML models? While it is widely accepted that some modern datasets are substantially diverse and large-scale, they can still be easily discriminated by modern models. This is a fresh conclusion and could trigger meaningful rethinking about the bias of large-scale datasets and models trained upon.

- The study is comprehensive and well-presented. It covers most modern backbones and pertaining datasets, and studies various factors that affect dataset classification performance. It is also accompanied by a thorough analysis that considers what kind of clue networks are used to discriminate these datasets, what kind of representation is beneficial, and how well models generalize across datasets, etc.

### Weaknesses
The way this paper is presented might be over-focused on the dataset classification task itself, and it might require readers to read [Torralba & Efros (2011)](https://people.csail.mit.edu/torralba/publications/datasets_cvpr11.pdf) first to gain a full picture. In the context of that paper, the task was proposed to show that image classification datasets by then are biased and cannot make a complete representation of the visual world. They discussed possible sources of such bias (eg, in data selection), but more importantly it also led to discussions on how to measure the value of a dataset (cross-dataset generalization), how such biases shape representations (eg, different negative sets make models capture different aspects of representations), and how to overcome such biases (eg, random cropping augmentation). If without considerable discussions on the latter, it might be unclear for readers to understand the significance of studying the dataset classification task.

### Questions
- To me there might never be a simple answer to the question of what kind of signal models learn when they succeed in discriminating the dataset one image comes from. Modern neural networks are so good at overfitting and any subtle patterns in dataset curation -- no matter low-level or high level, could be captured by them and processed to a strong black-box representation. If we accept that there is bias between CC, WIT, and LAION, and the bias remains as these datasets grow in scale, then what kind of harm would there be? If the representations learned from them generalize well, is the bias no longer a concern?

- When we only consider datasets at a very large scale (eg, >100M), will it still be easy for models to tell the difference?

- Dataset classification may not be a universal indicator of the bias between datasets, as it only sees one sample each time. Other aspects like concept frequency distribution (motivation of MetaCLIP) are also an important aspect of dataset bias and is highly related to the quality of representations learned upon. Do we need some new surrogate task/indicator for measuring bias in modern datasets in the next decade?

### Soundness
4

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
The paper studies the phenomenon of dataset bias through the lens of dataset classification. In this work, the authors expand upon the "Name the dataset" experiment from Torralba and Efros (2011) to modern neural networks. They then observe that modern NNs are relatively successful at the task of dataset classification, that is, predicting the source dataset of an image, under a variety of settings. The claim is that dataset bias still exists as NNs can exploit minor differences between large-scale image datasets to successfully solve the problem. The authors further test upon their hypothesis by designing and evaluating ConvNext, ViTs, and other models under a variety of confounding factors.

### Strengths
1. The paper is very well written, and clearly conveys the experiments as well as the intuition behind each one. 

2. The experiments are well-designed and clearly support the conclusions. While the underlying idea of `dataset classification' is not new, the authors have extended the experiments to clearly account for a variety of confounding factors.

3. It is also interesting to observe that the dataset bias task is also learning semantically useful features similar to pretraining, and self-supervised learning objectives. This is of independent interest as it can be used as a quick, cheaper method to initialize networks. While performance lags behind other approaches, this opens up some interesting ideas towards using dataset bias as an exploiting factor for self-supervision in future work.

4. The model generalization vs memorization experiments show a significant vulnerability in deep networks exploiting dataset-specific features, with methods like augmentation failing to correct for the same.

### Weaknesses
Overall, I found the paper to be well-written and clear. However, I am listing some points for improvement,

1.  It might be a useful exercise to use unbalanced mixes of the datasets as well, to observe effects of bias when a model encounters sources with varying numbers of images.

2. I also suggest adding confusion matrices for the experiments in Table 2 to help understand correlations between datasets.

3. The paper also does not address any directions on how to specifically tackle dataset bias. Given that standard approaches like data augmentation do not work, I am curious to know the authors' thoughts on methods like synthetic data generation, or domain generalization approaches as possible solutions to the problem.

### Questions
Please see weaknesses above.

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
4

### Summary
The paper revisits the "dataset classification" experiment from Torralba and Efros 2011 and applies it to modern neural networks and web-scale datasets. The authors find out that modern deep networks are very capable of solving such an artificial task, with a recognition accuracy of up to ~90%.

### Strengths
1) The paper's main finding, i.e., that the accuracy for the dataset classification task can be as high as 90% is surprising considering the size and diversity of the experimented web-scale datasets.

2) The authors perform a comprehensive set of experiments to cover multiple settings and ensure the validity of their findings, including 20 dataset combinations, several model sizes, architecture types, data augmentation strengths, and the number of available data points.

3) In Section 5, the paper provides additional analyses that rule out the possibility of achieving such high accuracy due to low-level signatures. Through a pseudo-dataset experiment and self-supervised learning, the authors also demonstrate that the networks are indeed learning dataset-related "semantic" features, further supporting their findings.

4) Overall, I found the paper well-written, clear, and easy to follow.

### Weaknesses
1) The paper is repeating an experiment that was introduced roughly 10 years ago but at a larger scale. Hence, despite the surprising practical result, the paper does not introduce a novel concept in absolute terms, and it does not propose a method to mitigate/decrease dataset bias (only observations and not practical solutions).

2) The paper lacks (even controlled) experiments to offer a qualitative evaluation of potential biases present in large-scale modern datasets. Looking at Table 2 (top panel), the classification performance significantly varies up to 30 percentage points. This variance is not sufficiently explored, leaving the reader to speculate about the underlying causes of such large differences in performance across dataset combinations.

3) Although the authors repeatedly assert, with empirical backing, that the networks can learn "semantic" features for dataset classification, they do not characterize these features in practice, even qualitatively. This absence of practical insight leaves a gap in understanding how the networks perform these tasks. The paper would benefit from a more detailed exploration of what these semantic features are, and how they differ across datasets.

### Questions
- Can a qualitative analysis be provided to explain why specific dataset classification tasks are significantly more challenging than others?
For instance, the ConvNeXt-T model on YFCC-CC-ImageNet scores 92.7%, whereas on CC-DataComp-LAION, it only reaches 62.8% (Table 2, top panel). Is this large discrepancy solely due to differences in distribution overlap? How could this phenomenon be visualized or understood more intuitively?

- It would also be interesting to visualize the difference in features learned by the network via, e.g., intra-class visualizations in latent space [1] or CAM approaches, compared to features learned when performing an actual classification task.

[1] Donglai Wei, Bolei Zhou, Antonio Torrabla, and William Freeman; Understanding Intra-Class Knowledge Inside CNN

Overall, the paper's strengths, including the finding of high dataset classification accuracy at large scales and the extensive, well-executed experiments, outweigh its weaknesses.
The findings interest the community, and the work is clear and well-presented. While addressing the identified weaknesses, such as providing more qualitative insights into the learned features and biases, which would strengthen the contribution, I am leaning towards acceptance. I would be inclined to raise the score if these aspects are improved.

---POST REBUTTAL---

The authors provided an extensive rebuttal covering my main concerns. For this reason, I am updating the score. I encourage to include the additional analyses performed in the final manuscript to strengthen the contribution.

### Soundness
3

### Presentation
4

### Contribution
3
