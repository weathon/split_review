# Does CLIP’s generalization performance mainly stem from high train-test similarity?

- Decision: Accept
- Scores: 6, 6, 6, 5

## Abstract
Foundation models like CLIP are trained on hundreds of millions of samples and effortlessly generalize to new tasks and inputs. Out of the box, CLIP shows stellar zero-shot and few-shot capabilities on a wide range of out-of-distribution (OOD) benchmarks, which prior works attribute mainly to today's large and comprehensive training dataset (like LAION). However, it is questionable how meaningful CLIP's high zero-shot performance is as it seems likely that web-scale datasets like LAION simply contain many samples that are similar to common OOD benchmarks originally designed for ImageNet. To test this hypothesis, we retrain CLIP on pruned LAION splits that replicate ImageNet’s train-test similarity with respect to common OOD benchmarks. While we observe a performance drop on some benchmarks, surprisingly, CLIP’s overall performance remains high. This shows that high train-test similarity is insufficient to explain CLIP’s performance, and other properties of the training data must drive CLIP to learn good representations. Additionally, by pruning data points that are dissimilar to the OOD benchmarks, we uncover a 100M split of LAION (¼ of its original size) on which CLIP can be trained to match its original performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper tries to uncover the reason for the good generalization of foundation models like CLIP. Specifically, we see that CLIP has a good zero-shot accuracy on OOD datasets, which is much higher compared to the models that are first trained on the labeled dataset (ID), such as ImageNet, and then tested on OOD datasets, such as ImageNet-Sketch.

As the pre-training data is large, it is highly likely to contain similar images to the OOD dataset. If that is the case, we might not call the test OOD dataset to be truly out-of-distribution, which might be the reason for the good performance of CLIP. 

Authors try to find an answer to the above problem through various experiments. 

They define the perceptual similarity of two images using the CLIP ViT-B/16 embedding of a pre-trained CLIP model. They find that the general OOD datasets like ImageNet Sketch have more common images with the LAION dataset than the ImageNet dataset.

In the first experiment, the authors removed images similar to the OOD dataset from the LAION dataset iteratively and measured the performance of models trained on a pruned dataset. As expected, they found a general trend of performance decrease, indicating that similar images in the training dataset had more importance.

The second experiment compared the models trained on small datasets such as ImageNet vs those trained on LAION. The authors define a metric called generalization gap, which is the set of minimum distance of each image in the test set with every image in the training set. They then remove the data points from the larger dataset (here, LAION) to have the same generalization gap as that of the ImageNet with the OOD dataset. They then trained a CLIP model on the pruned dataset. 
They discovered some performance drops, but the performance was still high compared to the case where the model was just trained on the ImageNet training set. This led to them concluding that the high performance of the CLIP is mostly due to more training data rather than test train similarity.

### Strengths
The paper is very well written. The experiments are clearly defined, and the motivation for each experiment is mentioned.

### Weaknesses
Even though authors perform many experiments, the experiments are performed on a single type of dataset, which are the variations of the ImageNet.
It would have been to include experiments with other OOD datasets such as iWILDCam or FMoW. Without these experiments it is not sure if these analysis is limited to one type of dataset.



### Questions
1. Are there experiments on other datasets unrelated to ImageNet? Having these experiments would be better to make a strong case.
2. Why do we use only CLIP ViT-B/16 embeddings to filter? Won't larger CLIP models have a better embedding to filter out the data points?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The goal of this work is to understand whether the superior OOD performance of foundation models like CLIP is a result of the training dataset containing images that are very similar to the OOD test set. Towards this, the authors systematically create several splits of the base LAION dataset that was used for training OpenCLIP. Firstly, they find that pruning samples that are very similar to the OOD test sets results in a considerable drop in the OOD performance. However, by matching the train-test similarity with that of ImageNet for a fair comparison, the authors find that CLIP still shows significant gains when compared to an ImageNet pretrained model. Thus, although LAION contains images that are very similar to ImageNet-OOD test sets, this is not the key reason for better OOD generalization of CLIP. Understanding the reasons for better generalization of CLIP still remains an open question.

### Strengths
- The key finding that despite reducing the similarity between the training data and the test sets, there is an improvement in test set performance, is helpful. 
- Several insightful experimental results are presented, which is helpful for the community, especially given that these experiments are very computationally intensive. 
- The pruned datasets whose code is released, can help with further investigation on why CLIP models have better OOD performance.

### Weaknesses
 - Although the results are interesting, my main concern is that the analysis is not sufficient to enable fair **OOD** testing. If the paper was about **ID** performance alone, removing train set samples that are similar to each test sample would have been sufficient, as reported in the paper. However, **OOD** implies that the **distribution** of images is unknown. So, to actually conclude that OOD evaluation is fair, all images from the test **domain** should have been removed, not only the images that are similar to every test set image. Therefore, as mentioned in the abstract, the term "out-of-distribution generalization" is still not meaningful even by training on the pruned datasets considered in the paper.
- To elaborate, if there are 5 sketches of the class "airplane" in the dataset, all images that are close to these sketches are removed. But there may be other airplane sketches, which are farther away than the closest image in ImageNet-test set, which are not removed. Thus, it is not guaranteed that all images of the given classes and test **domain** are removed from the train set.
- Further, there may be other objects, such as "space shuttle"  which are not included in ImageNet, thus sketches of space shuttles can be present in the training data, in addition to natural images of the same. Thus the domain "sketch" is not unseen by CLIP, and hence the evaluation is not truly OOD. 

Minor feedback: 
- Clarity of the abstract and contributions list needs improvement. It would be better to make a shorter summary of the key contributions.
- It would be better to give a different name to "generalization gap" as this term is used in a different context.

Typo:

"We provide anecdotal evidence in Fig. 1 where we choose samples from ImageNet-Sketch and ImageNet-R and examine their nearest perceptual neighbors in LAION-400M and **ImageNet**"

### Questions
Several additional experiments are required to be done, in order to emulate a true **OOD** setting, as discussed in the weaknesses section.
For example, one should remove all "sketch" style images as well, from L-200M+IN-Train (sketch-pruned) in order to test on the ImageNet-sketch test set for a true OOD evaluation. Otherwise, other sketch images that are present in the dataset can help bridge the domain gap between sketches and natural images, leading to an unfair OOD evaluation.

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the generalization behaviour of CLIP from the perspective of the training set. CLIP, as a pioneering foundation model, is well known for its exceptional generalization capability. However, it remains unclear whether such a good generalization capability stems from the web-scale training set, as it may well enclose samples similar to those on the test sets. This paper tackles this question by filtering out similar samples according to CLIP-embedding-based nearest neighbors. By creating a LAION subset that comes with as large a generalization gap as the ImageNet-1K training set, this work concludes that it is other factors, rather than the model has already seen samples with similar distribution, that leads to the outstanding ood generalization of CLIP models.

### Strengths
1. This paper first studies the ood generalization behaviour of CLIP from the interesting perspective of train-test distribution similarity, and has drawn some intriguing conclusions, like a subset of 100M of LAION-400M is able to train a good-performing model on ood benchmarks.
2. The experiments are well motivated and designed, resulting in compelling results that even without nearest neighbor samples, CLIP is still to maintain good performance on ood benchmarks.

### Weaknesses
1. This paper only works on common classification ood benchmarks, but neglecting a whole bunch of other CLIP application domains. In the very least, retrieval is the most foundamental test ground to probe how good a CLIP model is. The authors could use MSCOCO as the in-domain dataset for sample filtering, and use Flickr-30k as the out-of-domain dataset. Also, experiments on more diverse benchmarks, like VTAB (check datacomp paper for current best practices), are encouraged. The lack of exploration into retrieval tasks, which are a core application of CLIP, significantly limits the scope of the conclusions. Specifically, the paper does not address whether the observed generalization behavior in classification extends to retrieval, where the interplay between image and text embeddings is crucial. This is a major oversight, as a model might exhibit strong classification performance while still struggling with retrieval tasks, which are more sensitive to the quality of the joint embedding space. Furthermore, the paper should consider more diverse benchmarks beyond the ImageNet-based OOD datasets, such as the VTAB benchmark suite, to ensure the findings are robust across different types of distribution shifts. This would provide a more comprehensive understanding of CLIP's generalization capabilities.
2. Some crucial experimental details seem to be missing. For instance, how the nearest neighbor sets in section 4.1 are constructed are not mentioned at all (or mentioned in the appendix). How many samples are chosen in this set, and what is the threshold of CLIP score used here? The absence of these details makes it difficult to reproduce the experiments and evaluate the validity of the results. The paper should explicitly state the number of nearest neighbors considered for each query sample and the criteria used to determine the similarity threshold. Without this information, the conclusions drawn from the nearest neighbor analysis are less convincing.
3. The authors should compare the similarity of nearest neighbors to test sets between the whole LAION datset (after filtering in section 5/6) and ImageNet-Train. Otherwise, one could argue that, even though the closest sample in LAION and ImageNet training set is about the same far away to the test set, LAION has a lot more samples close to the closest sample than ImageNet (but not as close to the test set as the closest sample), and thus still has a unfair advantage on those ood benchmarks, compromising the validity of the conclusion. This comparison is crucial to understand the true impact of the filtering process. It is not sufficient to only analyze the single nearest neighbor; the distribution of similarities for all training samples relative to the test set is also important. The paper needs to demonstrate that the filtered LAION dataset does not retain an advantage due to a higher density of near-similar samples, even if those samples are not the absolute closest.

### Questions
What is the potential application of the finding in this paper? I know this is a pure analytical work, and believe its merit is above the aceeptance threshold of ICLR. But I am still intrigued to learn what is the broader impact of this work, like how this would enlighten future research or engineer endeavours.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies the hypothesis “Does CLIP’s accuracy on test sets mainly stem from highly similar images in its train set?”. Their approach is to take a CLIP training dataset, LAION, and remove samples similar to OOD benchmarks, then retrain and evaluate the performance drop. In Section 4.1, they show that for some OOD datasets e.g., ImageNet-Sketch and ImageNet-R, there are more similar images to the OOD dataset in LAION than there are in the ImageNet-train set. These images are both semantically and stylistically more similar. They also observe a positive correlation between accuracy and having similar neighbors in the training set for each OOD benchmark. In the remainder of the paper, they prune the dataset by removing similar samples to OOD datasets and evaluate the performance of models trained on pruned datasets.

### Strengths
- Figure 1 clearly shows that the LAION-400M dataset contains semantically and stylistically similar images to OOD benchmarks while the ImageNet training set does not.
- Figure 3 quantitatively shows the nearest neighbors of OOD datasets in LAION-400M are on average more similar than the nearest neighbors from ImageNet-train set except for the Imagenet-Val set itself. Fig 3.right also clearly shows that CLIP model performs better on samples that it has seen similar images of it in the training set.
- Figure 4 shows that pruning LAION for similar samples to ImageNet-Sketch and ImageNet-Val results in substantial accuracy drop compared with pruning random samples. Hence showing that these similar samples are crucial for the effective robustness of CLIP models.

### Weaknesses
 - Even though the results in Figure 4 show the near-pruned samples are crucial for OOD generalization of CLIP, they are not conclusive. In particular, the following two experiments would be useful:
i) Does a model *only* lose OOD generalization on one benchmark or are these near-pruned samples crucial for all sorts of image-classification performance on any benchmark? This requires plotting the accuracy on two datasets, e.g., ImageNet-Val and ImageNet-Sketch, and showing that after pruning samples similar to ImageNet-Sketch, we only lose performance on ImageNet-Sketch. The current results in Figure 7 show a performance drop across all datasets, which raises the concern that the removed “similar images” might be generally the most informative samples, or the highest quality samples, for the model. To verify this, the authors should evaluate the performance of models in Figure 7 on tasks unrelated to ImageNet, such as retrieval or other zero-shot classification tasks that are farther from ImageNet (e.g., tasks in the open-clip/Datacomp eval suite). This would help determine if the removed samples are crucial for general performance or just for ImageNet-related tasks. This point is also related to the validity of the metric used to define “similar images”. The distinction between “similar” and “highly similar” is not well-analyzed. For example, what are some examples that appear in both? What are some examples that appear in either one? It is unclear if “similar” images are important for training and “highly similar” images are not.
ii) Do CLIP models lose OOD generalization more quickly than classification models trained on ImageNet? For this, one would prune ImageNet with a similar procedure for X% of samples and compare whether the accuracy drop in ImageNet models is slower than CLIP models. If not, then we would know that any OOD generalization we have been seeing could be due to seeing similar samples in the training set.

- This paper is a good place to have a broader discussion on “What is zero-shot?” and “What is out-of-distribution robustness?” and I think the paper should expand on that. In particular, after showing that pruning loses OOD generalization, it is not clear what the community should do with these datasets and evaluation benchmarks. Should we say CLIP models have cheated and they are not zero-shot? Related to that, the objective of Sections 5 and 6 that “Correct for highly similar images” is not clear. Why would we want to prune our training datasets to get worse on some test benchmarks if those exact test samples do not appear in the training set? Why would we want models in Table 1 trained on pruned datasets that perform worse?

### Questions
- Figure 4: What if we perform a similar process for training on the ImageNet dataset? Do we observe a similar accuracy drop?
- Figure 7 shows that removing samples similar to ImageNet-Sketch and ImageNet-Val result in lower performance in all other ImageNet OOD datasets as well. Could this mean that these samples are important for a general understanding of the ImageNet distribution?
- Section 5: Would this method and any model trained on this dataset be considered as transductive learning? Because the test datasets would have been seen directly or indirectly by the model. Would this be against the license of datasets such as ObjectNet that say “ObjectNet may never be used to tune the parameters of any model.”?

Typos:
- Page 7: Let us for consider -> Let us consider

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
