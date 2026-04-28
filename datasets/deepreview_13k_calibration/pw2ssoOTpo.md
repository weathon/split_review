# CIFAR-10-Warehouse: Broad and More Realistic Testbeds in Model Generalization Analysis

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
Analyzing model performance in various unseen environments is a critical research problem in the machine learning community. %In particular, we study the tasks of domain generalization and accuracy prediction on out-of-distribution (OOD) test sets. 
To study this problem, it is important to construct a testbed with out-of-distribution test sets that have broad coverage of environmental discrepancies. %, it is important to incorporate out-of-distribution test sets that have broad coverage of distributions. 
However, existing testbeds typically either have a small number of domains or are synthesized by image corruptions, hindering algorithm design that demonstrates real-world effectiveness. In this paper, we introduce CIFAR-10-\textbf{W}arehouse, consisting of 180 datasets collected by prompting image search engines and diffusion models in various ways. Generally sized between 300 and 8,000 images, the datasets contain natural images, cartoons, certain colors, or objects that do not naturally appear. With CIFAR-10-W, we aim to enhance the evaluation and deepen the understanding of two generalization tasks: domain generalization and model accuracy prediction in various out-of-distribution environments. %(AutoEval) and  (DG). 
We conduct extensive benchmarking and comparison experiments and show that CIFAR-10-W offers new and interesting insights inherent to these tasks. We also discuss other fields that would benefit from CIFAR-10-W. Data and code are available at \url{https://sites.google.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper constructed a thorough dataset for OOD evaluation based on CIFAR-10. They also provide a benchmarking analysis for a thorough list of accuracy prediction and domain generalization methods, which reveals interesting findings including identifying difficult settings that current methods fails. They also pointed out other directions that this dataset might be useful including denoising, unsupervised domain adaptation and OOD detection.

### Strengths
The paper is cleanly written and easy to read. The contribution can be pretty beneficial to the field as a thorough and high-quality benchmark dataset is the foundation for methods improvements, not to mention that OOD is a crucial problem in the field. The dataset built in this paper is quite thorough and high quality in my opinion as it includes not only many more domains compared with previous efforts but also includes state-of-art generative methods as well as real-world data for the dataset build. The author also provides interesting experiments that point out the limit of current state-of-art accuracy prediction as well as domain adaptation methods, which can certainly inspire corresponding methods improvements to be developed in the future.

### Weaknesses
Only want to point out this one typo: you seem to have an unfinished sentence at the last line of page 6.

### Questions
I am curious whether a finer-grained dataset like CIFAR-100-warehouse can be built as well. I know that many current state-of-art can suffer at finer-grained classification tasks. It could be interesting future work.

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a dataset called CIFAR10-W. I detail the construction of the dataset as the creation of the testbed seems to follow standard practices in DG, but done over a wide model zoo of classifiers.

**Construction**
A subset consists of all 10 classes of CIFAR10 with one colour and from the same source (all images are 224x224 but resized to 32x32 in experiments)

It consists of the following 180 subsets by (a-d):

*a) Querying 4 search engines*: Google, Bing, Baidu, 360 with a total of 12 colours (Google and Bing differing on 1-2 colours) using the two queries:
1) category_name 
2) category_name cartoon 
This creates {2 queries} x {12 colours} x {4 engines} = 96 subsets

*b) Querying other search engines*: Sogou, with the same 12 colours as Baidu/360, Pexe with 20 colours and Flickr with 15 colours. No cartoons queried from here.
This creates 12+20+15 = 47 subsets.

This creates 143 subsets which contain real images in total. 95 of these search by keywords (CIFAR-10-W KW) and 48 belong to the additional cartoon domain (CIFAR-10-W KWC).

*c) Querying Stable Diffusion 2.1*: This is done the two prompts for the same 12 colours as Baidu/360/Sogou for synthetic versions of the real data:
1) high quality photo of {color}{class name}
2) high quality cartoon photo of {color}{class name}

This creates 12 x 2 = 24 subsets

*d) 13 subsets created by using special prompts with SD-2.1*: Prompts given in Table 4 -- with background, context where target objects do not naturally co-exist.

Additionally:
- Cleaned annotations and details on previously labeled incorrect labels.

**Comparison**: CIFAR10-Cs benchmarks refer to a collection of CIFAR10-C, 10.1 and 10.2.

**Testbed**: Testbed comprises of two tasks:
- Model Accuracy Prediction using Unlabeled Test Sets – I am unfamiliar with this task
- Domain Generalization, similar to DomainBed – I am vaguely familiar with this task

It is important to note that they performed evaluation over a wide range of models.

### Strengths
**S1) Good benchmark [Critical]**: I like the proposed dataset, which is one of the core contributions as:
(1) It is a realistic domain shift in contrast to synthetic corruptions
(2) It is large-scale and has 224x224 images (albeit is a 10 class classification problem)
(3) It has a large number of domains (36-180 domains)
(4) It has cleaning annotations available!

**S2) Comprehensive evaluation [Critical]**: The paper seems to have tested methods across a lot of different models and across different subsets of the C10-W on two different tasks. Appendix sections were quite a delight to go through.

**S3) DG results quite cleverly done [Important]**: I liked the setup using alternative sources like Yandex, etc. These aspects seemed quite thoughtful to me

### Weaknesses
 **W1) [Critical] Why is MAE of prediction scores the main metric reported in the paper for comparing methods in Table 2?**

Why I ask this (my understanding, could be caused by misinterpretation): 
- MAE of prediction scores, rather than prediction scores seems like a bad measure as indicated by Figure 2 and elaborated in Fig 9 – no correlation to accuracy, while Figure 7 shows prediction scores have high spearman rank order correlation (a strong measure of correlation!). 
- Hence, I can discern very little about the predictiveness of the accuracy from the MAE score as they’re uncorrelated!

**W2) [Important] Conclusions made from Task 1 need improvement-- Similar but to a lesser degree for Task 2.**

Details for Task 1:

*(C1) This benchmark is a harder benchmark compared to CIFAR-10-Cs.*

- Corruptions can be made harder by increasing the magnitude easily, increased hardness as the primary feature of the testbed seems weird. I would be interested in rather highlighting whether networks don't capture certain aspects introduced here.
 
*(C2) Predictions are more consistent across classifiers here.*

- One can easily argue that predictions are consistent here because the shift is not varied– it simply changes colours rather than the diverse, varied corruptions studied in CIFAR-10-C  benchmarks. 
- Note that this does have a distribution shift across cartoons and SD classifier, but SD classifier results are varying across classifiers too!

**W3) [Important] Little analysis of the dataset itself, far more focus on task/models**

- While this weakness is vaguely stated, I have fleshed out some components in Q1 to concretely ask what analysis would be helpful from my view.
- However, I do not work in either of the fields so it is hard for me to accurately ask, but there seems to little analysis done which is concerning.

### Questions
**Q1) How many visually distinct domains exist within these 180 subsets? Specifically, how different are images sampled from different search engines?**

I found 36 distinct domains:
- The 12 colour palettes seem like distinct domains
- Cartoon, real-world images and SD images seem distinctly different

By visual inspection by me, images across different search engines look similar (ordering the images by the same colour would have made my job, and an interested readers’ easier in Figures in Appendix F). Note that popular datasets are also collected from different search engines but treated as one domain-- do different engines introduce a noticeable shift?

*Counterclaim to the point: Significant drop in performance in Baidu and 360.*
- Is it due to a lesser number of images or because of the domain gap? [Maybe separating the search engines in Figure 1 would be have been very informative for a reader, alongside more analysis of drift]
- I suspect those engines have fewer images which might be causing the accuracy drop.

The benchmark seems to pitch that there are 180 clearly distinct domains, would be concerning if rather there are only 36 visually distinct domains. 

**Q2) What all components would be released publicly?**

I presume the dataset, along with the cleaned annotations and licenses would be released.
- Would the scraping code be released?
- Would the code for classifiers tested be released?
- Will the trained models/features be released?

Could the authors address the weaknesses, these questions and check if I missed pointing out some strengths? That would help me make a more balanced evaluation. I like the benchmark itself but the experiments and conclusions drawn from it need improvement in my view. Note that I am not familiar at all with Task 1 and only vaguely familiar with Task 2, indicated in my confidence.

### Soundness
2 fair

### Presentation
4 excellent

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
This paper proposes a new benchmark dataset for domain generalizations. Compared to the previous datasets, CIFAR10-Warehouse contains a lot more number of domains with both real-world images and images synthesized by stable diffusion. Extensive benchmarking and comparisons are conducted on this new dataset in terms of two generalization tasks.

### Strengths
1. This paper provides a new dataset with a much larger number of domains compared to existing domain generalization dataset. The idea of multi-domain dataset gives the researcher a new perspective on how to evaluate the domain generalization methods. 
2. The experiments are quite extensive and gives some interesting insights on domain generalization.

### Weaknesses
1. Can the authors give more analysis and justification on why they divide different domains based on color and cartoon/no cartoon? since there are a lot of other ways to categorize different domains, such as other styles besides cartoon. 
2. Can the authors give more empirical analysis on the advantage and difference of the proposed dataset compared to existing datasets. For example, are the performance comparison on CIFAR-10-W and existing datasets aligned? Are there any contradicted conclusions or new observations based on the experiment results on CIFAR-10-W?

### Questions
Please refer to the weaknesses.

### Soundness
3 good

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
The paper introduces CIFAR-10-Warehouse, a substantial dataset comprising 180 diverse datasets with images from the original CIFAR-10 categories, sourced from various sources including real-world searches and stable diffusion. CIFAR-10-Warehouse serves as a valuable resource for advancing research in model generalization analysis, accuracy prediction, and domain generalization. CIFAR-10-Warehouse creates a challenging testbed, shedding light on the complexities of model performance in diverse, real-world scenarios. Additionally, the paper highlights potential applications in fields such as learning from noisy data and out-of-distribution detection. This paper advances the understanding and evaluation of model generalization in machine learning research.

### Strengths
(1) The paper introduces a novel and extensive CIFAR-10-Warehouse dataset with a diverse collection of 180 datasets. The authors' approach of curating datasets from real-world searches and stable diffusion represents a novel and creative way to construct a comprehensive testbed for model generalization analysis.

(2) The paper maintains a high quality in dataset creation and experimentation. The dataset creation process appears thorough, involving both real-world image searches and diffusion model generation, while ensuring privacy and adhering to licenses. The experiments conducted on CIFAR-10-Warehouse are extensive, employing various methods and classifiers with detailed analysis of the results. 

(3) The paper is generally well-written and organized, making it easy to follow. The methodology for dataset creation and evaluation tasks is clearly explained.

(4) CIFAR-10-Warehouse serves as a valuable resource for researchers, providing a unique dataset that covers a wide range of real-world scenarios and challenges the generalization abilities of machine learning models. The paper's exploration of potential applications in learning from noisy data, domain adaptation, and out-of-distribution detection highlights its significance in various domains.

### Weaknesses
 (1) While the paper provides details about the data collection process, it lacks a discussion on potential biases and limitations introduced during data collection from search engines. Biases in search engine results can affect the diversity and representativeness of the dataset, which should be acknowledged and addressed. Specifically, the paper does not discuss how the search queries were designed to ensure a balanced representation of each class within CIFAR-10 across different search engines. Furthermore, the potential for geographical or cultural biases inherent in search engine results is not addressed, which could skew the dataset towards certain perspectives and limit its generalizability. 

(2) The paper focuses on domain generalization within the context of CIFAR-10-Warehouse. However, CIFAR-10 is indeed a relatively small dataset with low-resolution images and a limited number of categories compared to larger-scale and more diverse datasets like ImageNet or the Wilds[1]. This work does not extensively discuss how the findings from this dataset can be applied to real-world scenarios or other domains. The limited image resolution and the small number of classes in CIFAR-10 may not fully capture the complexities of real-world image recognition tasks, making it difficult to extrapolate the domain generalization performance observed on CIFAR-10-Warehouse to more complex scenarios.

(3) This work could be strengthened by discussing potential real-world applications beyond the scope of image classification. Evaluating and extending the methods on datasets with different characteristics and applications would provide a more practical significance for real-world applications. The paper does not explore how the proposed dataset and the domain generalization methods could be applied to other tasks such as object detection, semantic segmentation, or video analysis, which would broaden the impact of this work. 

(4) While the paper introduces several domain generalization and accuracy prediction methods, it could benefit from including additional state-of-the-art baseline methods, e.g., GVRT[2], and VNE[3], for a more comprehensive comparison. This would help establish a clearer benchmark for the proposed methods. The absence of these comparisons makes it difficult to fully assess the relative performance of the methods presented in the paper against the current state-of-the-art.

### Questions
(1) Can you elaborate on the potential biases introduced during data collection from search engines or how did you ensure the collected data is diverse and representative?

(2) How might the findings from CIFAR-10-Warehouse generalize to other larger-scale datasets or tasks beyond image classification?

(3) Analyzing and discussing the failure modes of domain generalization would provide insights into scenarios where these methods might not work well. Can you discuss and provide examples of failure modes for the domain generalization and accuracy prediction methods on the CIFAR-10-Warehouse testbed?

(4)The paper mentions addressing limitations and publishing future versions of CIFAR-10-Warehouse but does not provide a concrete roadmap for future research. A discussion of potential future directions, and how the dataset can evolve would be insightful.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
