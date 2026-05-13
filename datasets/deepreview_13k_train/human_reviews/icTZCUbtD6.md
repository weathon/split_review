# Dissecting Sample Hardness: A Fine-Grained Analysis of Hardness Characterization Methods for Data-Centric AI

- Decision: Accept
- Scores: 8, 1, 8, 6, 8

## Abstract
\vspace{-2mm}
Characterizing samples that are difficult to learn from is crucial to developing highly performant ML models. This has led to numerous Hardness Characterization Methods (HCMs) that aim to identify ``hard'' samples. However, there is a lack of consensus regarding the definition and evaluation of ``hardness''. Unfortunately, current HCMs have only been evaluated on specific types of hardness and often only qualitatively or with respect to downstream performance, overlooking the fundamental quantitative identification task. We address this gap by presenting a fine-grained taxonomy of hardness types. Additionally, we propose the Hardness Characterization Analysis Toolkit (H-CAT), which supports comprehensive and quantitative benchmarking of HCMs across the hardness taxonomy and can easily be extended to new HCMs, hardness types, and datasets.
We use H-CAT to evaluate 13 different HCMs across 8 hardness types. This comprehensive evaluation encompassing over \emph{14K setups} uncovers strengths and weaknesses of different HCMs, leading to practical tips to guide HCM selection and future development. Our findings highlight the need for more comprehensive HCM evaluation, while we hope our hardness taxonomy and toolkit will advance the principled evaluation and uptake of data-centric AI methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a benchmark for evaluating methods that make supervised learning models robust to hard data examples. The paper introduces a taxonomy of hard cases and defines each category in terms of where the corruption happens and how the data distributions differ. The authors developed a toolkit to automatically evaluate models and include 13 algorithms in their study. The paper summarizes the results and presents the main highlights, together with an extensive supplementary material with more details.

### Strengths
* The organization of the taxonomy is sound and formalizes observations from prior literature.
* The systematic experimental design is strong and the evaluations are exhaustive.
* The toolkit for evaluating and comparing performance across HCM seems well designed.

### Weaknesses
 * The conclusions of the study seem limited. Despite the extensive experimental work, it is unclear how the hardness characterization field can make progress. While the paper claims to have practical tips, there is the underlying assumption that the hardness type is known and coming from only one type. This is not realistic in practice and undermines the value of the recommendations for practitioners.
* The paper insists that studying data hardness is critical for advancing data-centric AI, but it is unclear what data-centric AI is, and why HCMs are the key to advance it. A more fundamental question is, do we really need HCMs at all or we only need to create high quality datasets that eliminate corrupted examples?
* Following the need for HCMs, a baseline of training models without HCMs is missing. There are two scenarios that should be considered as baselines: 1) training a model without HCM with the same level of corruption introduced as the other models. 2) Training a model without HCM and with only the easy examples, i.e. removing the portion of corrupted samples. This would be informative to evaluate what cases in the taxonomy really need to be investigated further with HCMs and which ones can be addressed by simply cleaning the dataset.
* The taxonomy is manually defined based on the interpretation of previous literature, and the datasets used in the study are intentionally clean (MNIST and CIFAR) to simulate hard samples. Perhaps data hardness should be evaluated in a data-driven way, i.e., using a real world dataset and using data science, statistics, and machine learning to find out the nature of hard samples on the dataset. This reviewer finds the approach of defining the hardness of data artificial, and perhaps not reflecting the challenges of current problems and datasets.
* The paper points to the use of indirect measures, such as improvement in downstream performance, as an issue (Sec. 2.2). However, it seems like the metric that they use to evaluate methods and create the benchmark is downstream performance in the corresponding classification task. It was not clear what the proposed solution to this issue is in the benchmark.
* The writing style and paper formatting is too flashy and very distracting. Instead of having a natural flow, the paper has sentences in bold, boxes in colors, and other decorations that ask for too much attention, giving the impression that there is something more important to read than the argument the reader is focusing on. I found this style very hard to follow. In addition, the paper reads as if it was trying hard to sell a toolkit rather than presenting a study with solid conclusions.

### Questions
Unfortunately, I don't find this study very compelling as a full research article. As it is currently, the paper seems to be more appropriate for a Datasets & Benchmarks track at NeurIPS, for instance, rather than bringing in novel insights to advance hardness characterization methodology. Maybe I'm missing what the most important conclusion is, which is what I'd like the authors to clarify.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper did the following:
- A taxonomy of hardness -- mislabel, OOD, atypical
- Provide a library of modules for dataloading, hardness measurements across different types of hardness, unified interface and evaluator
- Propose that hardness is ill-defined, indeed
- Propose that hardness is usually being measured by downstream, which should not be
- Give a list of takeaways at the end
- Experimentd ran on cifar and mnist

### Strengths
The paper dedicated a significant portion to describing why hardness is not well-defined anywhere. It also provides a taxonomy of hardness that are split into mislabeling, OOD and atypical. It also provides a unified interface for evaluation.

### Weaknesses
The authors stated that hardness should not depend on downstream improvement. I find that to be very controversial. One model's hardness may be another model's easy. Maybe I have not understood this completely and would like clarification. Moreover, in the end you run classification on cifar and mnist to obtain a list of takeaways iiuc -- did the authors not just use downstream tasks (cifar and mnist classifications) to inform us of their takeaways? If I understood incorrectly, please provide clarification. Also the categorization of hardness into mislabel, ood and atypical is quite unsatisfying. Why mislabel? Also in this era of self-supervision, LLM autoregressive, etc., I find this paper a little not keeping up with time. What is hardness in this new day and age?

Experiments on cifar and mnist only --- authors claimed that they did not select imagenet because imagenet has less than 5% mislabel. Can you not artificially mislabel yourself then?

A large part of the paper reads like an engineering document. I appreciate that, but I think scientific insights are more important while the engineering information can be delegated to appendix.

While I do appreciate the whole framework, but I am asking is it really useful in the fundamental sense which your paper is kind of claiming iiuc?

RE: "not keeping up with time" -- let me put it this way, from your paper, I don't know how to characterize hardness for LLM, LMM. What is OOD in LMM/LLM?

On ImageNet: sorry, I misread. However, I am still concerned that the datasets used are very toy, very small. I would like to see some real world datasets.

Also, you did not answer my question (or at least I did not see it) on why categorize hardness into mislabel, ood and atypical. Do these three cover all the hardness in the world of data?

You also only show for images. For claiming being a fundamental hardness framework, what about other modalities? I am not trying to split hair, but my point is that it comes down to these three categories on images, and you create samples of them on mnist and cifar and run experiments on them, and finally make those takeaways. That's what it is. All the modules are engineering models (and I am not disputing their usefulness), but everything comes down to what I described. What is so fundamental about it?

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new framework called H-CAT for evaluating HCM methods that measure how difficult it is for a classification model to learn from certain examples. The paper provides three possible reasons for an example to be 'hard':
- The example is mislabeled
- It is OOD or outlier
- The example is valid but is atypical

Now the methods that are used to estimate the any of hardness types above are called HCMs:
- Learning dynamics-based
- Gradient-based
- Distance-based

The paper presents a codebase which allows to evaluate the hardness types as well as the HCMs. The main takeaways are:
- Many HCMs disagree with each other.
- Some types of hardness are characterize to measure than others.
- Learning dynamics-based methods are generally more effective.
- The best HCM to use depends on the specific problem.

### Strengths
- The paper introduces a novel codebase for the systematic analysis of HCMs. The categorization done in section 2.1 is nice to read. It is great to define hardness more formally and identify different underlying reasons for the difficulty a classification model in learning from certain examples.

- The paper have sufficient experiments. The authors evaluated 13 HCMs, providing a robust validation of their findings.

- The takeaways are generally valuable. The authors offer practical advice on how to choose HCMs based on the type of data hardness, and they highlight the advantages of learning dynamics-based methods.

- Overall, the paper is well-written. However, reorganizing the content and moving some parts to the appendix and placing back some key figures and explanations to the main text could improve its readability.

### Weaknesses
 - The paper could be structured better. Introducing and clearly defining "hardness types" and "HCMs" earlier would help readers understand the paper better. Some important explanations and figures that support the main concepts are in the appendix, which makes it difficult for readers to access them quickly and easily

- The paper would be more technically rigorous if it included detailed equations and unified notation for the various HCMs in the appendix. Providing a more detailed explanation of methods, AUM for example, in the main text would also make the paper more instructive.

- While the authors acknowledge certain limitations, two are particularly significant in my opinion:

1. Before evaluating HCMs, you need to know what type of hardness is present in the data. This may not always be possible in real-world scenarios.
2. The paper does not address the fact that hardness can change during the training process. A hard example at epoch 1 might not be hard at epoch 10.

### Questions
I would like to know authors opinion regarding the limitations mentioned above, particularly 1) not knowing the type of hardness and 2) evolving hardness.

Two recommendations:
- I would suggest to reorganize the content to ensure a logical flow of information, placing Figure 7, for example, and some details to the main body can help grasping key concepts.

- Add detailed equations in a unified notation for the HCMs explored in section A.2.*. This would make your paper a go-to paper whenever someone wants to learn about hardness literature.

--------------------
Post rebuttal note:
Thank you very much for your response and applying the changes I suggested. I respectfully disagree with Reviewer 5UHg- the fact that the community's focus is now on LLMs doesn't make this type of works worthless. I believe that this paper has significant potential to advance our understanding of hardness in machine learning and hence I vote towards acceptance.

### Soundness
4 excellent

### Presentation
2 fair

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
The paper proposes a new taxonomy for quantifying hardness of samples and then creates a framework on top of it (H-CAT) which uses existing hardness evaluation techniques to predict hardness categorized into different hardness types from their taxonomy. The paper then goes on to conduct hardness evaluation experiments on 2 image and 2 tabular datasets and highlights several key takeaways and recommendations for practitioners using their toolkit.

### Strengths
1. The taxonomy proposed by the paper is simple, clearly explicated, and practically useful. Relating it in detail to previous methods and frameworks and what's missing in existing HCMs based on this taxonomy helps readers create a good mental model of the space.
2. The comprehensive benchmarking of more than 13 HCMs across multiple datasets, on robust evaluation criteria is useful for the community.
3. Some takeaways like the efficacy of learning dynamics-based HCMs, lack of efficacy of computational-efficiency motivated methods, importance of significance testing and the variation in stability of the HCMs across seeds, backbones and parameterizations, all provide relevant, empirical information to practitioners using these methods.

### Weaknesses
1. Sticking to just MNIST and CIFAR10 limits the usefulness of the takeways. The dataset sizes and complexity we currently operate with are very different from MNIST/CIFAR10 and I'm afraid these learnings might not generalize to larger, more complex datasets. Specifically, the low resolution of MNIST and CIFAR10 images might not expose the same kinds of hardness that would be present in higher-resolution images with more complex textures and object arrangements. The limited number of classes in these datasets also fails to capture the nuances of multi-class classification problems encountered in real-world applications.
2. The Near OOD, far OOD, and the atypical perturbations used in the experiments are oversimplified in my opinion. In the real world, defining near/far OOD and atypical have a complicated notion of support of the sample distribution, but the use of Gaussian noise, texture changes for near OOD and exchanging MNIST with CIFAR (which are drastically different) for far OOD, and using simple invariant functions like shift and zoom for atypical does not do justice to these concepts. For instance, near OOD could involve subtle changes in lighting or viewpoint, while far OOD could be a completely different domain, not just a different dataset. Atypical examples could include adversarial examples or samples with rare combinations of features, which are not captured by simple shifts and zooms.
3. [Minor] The bulk of paper is focussed on creating a taxonomy for hardness evaluation and then building a software toolkit to evaluate existing methods for its quantification. Some initial discussions during the taxonomy creation and some of the non-obvious takeaways are instructive for the researchers in this field, but most of this work is geared towards practitioners. This isn't necessarily a negative thing, but limits the research novelty/impact of the work.

### Questions
1. As the severity of perturbations increases, do the methods used in HCMs also show an increase in the hardness score? Does this vary for learning-integrated methods vs others?
2. What is the effect of using augmentations during training for these models? I'm guessing the hardness predictions will change for some methods but not others.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The author claims that existing works on Hardness Characterization Methods (HCMs) fail to address comprehensive and quantitative evaluation of HCMs. Also, the author points out the absence of an integrated and practical software tool that can simulate and evaluate various types of HCMs. In this context, the author proposes a fine-grained taxonomy for categorizing multiple hardness types and introduces the Hardness Characterization Analysis Toolkit (H-CAT), which supports over 14K setups with 13 different HCMs across 8 hardness types. The author reports the performance of each HCM in various settings using H-CAT and provides invaluable takeaways and practical tips that were not seen in previous works.

### Strengths
1) This paper diligently considered all the recently proposed HCM algorithms within the past 3-4 years and developed H-CAT, reporting experimental results using it.
2) Through graphical illustration (Figure 1) and table analysis (Table 1), the need for a systemic evaluation framework for HCMs was effectively underscored.
3) Figures 3, 4, 5, and 6 analyzed the behavior of popular HCMs under various hardness settings from different perspectives. Additionally, the experiments conducted using the toolkit developed by the authors hold greater significance.
4) The author provided detailed instructions for use of H-CAT and additional experimental results through a voluminous appendix.

### Weaknesses
Hardness characterization is an important concept in various fields such as computer vision works like object detection and segmentation, as well as natural language processing and reinforcement learning. However, the proposed HCM evaluation framework in this paper can only handle image classification.

### Questions
1) In the Introduction, it is stated that "These 'hard' samples or data points can significantly hamper the performance of ML models." However, from an active learning perspective, can't we consider hard samples to be more informative and better samples with higher annotation efficiency?
2) On page 3, in the section "Data characterization," it is mentioned that difficult or easy samples are classified into separate easy or hard subsets. However, instead of categorizing sample difficulty into two binary sets, wouldn't it be better to dynamically control the learning process by assigning weights or using other methods based on continuous difficulty values? Additionally, excluding OOD/outlier and atypical samples from model training could potentially enhance the model's generalization capability. So, couldn't excluding them altogether from training be a suboptimal choice?
3) The author mentioned that existing works have a disadvantage of conducting indirect evaluation in downstream tasks. In that case, how does the proposed framework perform direct evaluation?
4) In Figure 6, Spearman rank correlation scores for HCMs are reported. As far as I know, Spearman rank correlation calculates the correlation between two variables. How was the correlation computed from multiple runs in this case?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
