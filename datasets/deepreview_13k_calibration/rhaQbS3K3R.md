# Does Progress On Object Recognition Benchmarks Improve Generalization on Crowdsourced, Global Data?

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 8, 6

## Abstract
For more than a decade, researchers have measured progress in object recognition on the ImageNet dataset along with its associated generalization benchmarks such as ImageNet-A, -C, and -R. Recent advances in foundation models, trained on orders of magnitude more data, have begun to saturate performance on these benchmarks. Despite this progress, even today’s best models are brittle in practice. As a step toward more holistic measurement of model reliability, we propose studying performance on crowdsourced, global datasets, which contain natural distribution shifts seen practically in deployment. We perform a comprehensive empirical study on two crowdsourced, globally representative datasets, evaluating nearly 100 vision models to uncover several concerning empirical trends: first, that progress on crowdsourced, global data has significantly lagged behind standard benchmarks, with advances on ImageNet occurring at $2.5x$ the rate of progress on crowdsourced, global data. Second, we find that progress on standard benchmarks has failed to improve or exacerbated geographic disparities: geographic disparities between the least performant models and today's best models have more than tripled. We showcase the promise of using more curated and/or representative training datasets for mitigating these trends, and emphasize curation of web-scale, geographically representative training datasets as a critical open problem for the research community.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this work, authors target an important aspect of model training: the data imbalance across region. Author used  two globally crowdsourced datasets (DollarStreet and GeoDE), as calibrated geographic disparity measurement, and shows that model train on conventional dataset, like imageNet, are highly dominant by the west. And model perform better on conventional dataset will enlarge this geographic disparity across regions. Lastly, author propose to solve this problem by last layer fine-tuning on geographic balanced dataset.

### Strengths
1. The problem author targeting, is of significance to the community, especially in the foundation model, for which data are more dominant than the model itself. 
2. Author had made significant empirically contribution by experiment on a large number of models. 
3. Author have identified data imbalance in standard benchmark, and shows that improvement over conventional evaluation will exacerbate geographic disparities. 
4. Author shows that applying conventional trick like data augmentation and scaling won’t solve this problem. 
5. Author also propose a simple fix of adopting last layer fine-tuning over geographic balanced dataset.

### Weaknesses
Although the concept of adopting geographic disparities is a neat measurement for data bias, author limit the measurement of such concept only on two specific dataset, which make the final ‘improvement’ less convincing. Also, the proposed solution to resolve this bias by last layer fine-tune, is a common approach in data debiasing and less novel, especially author tried to fine-tune on a geographic dataset. 

One potential significant improvement of this work, in my opinion, is to apply author’s insight onto standard dataset. For instance, in appendix F LAION CLUSTERING EXPERIMENTS, author use two geographic dataset only as cluster center to measure the ‘geographic disparities’ for LAION datasets. It would be much stronger an insight if authors shows that finetuning/retraining model with ‘balanced LAION’ dataset could reduce geographic disparities.

### Questions
Plase refer to weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
To study the reliability of foundation models, this paper proposes to evaluate these models on crowdsourced, global datasets with natural distribution shift. The paper provides evaluation of 100+ vision models on the benchmark datasets DollarStreet, GeoDE, and compare to the evaluation on standard benchmark datasets ImageNet. The findings show that existing evaluation on standard benchmark dataset is limited, and it is promising to use more curated and/or representative datasets for evaluating foundation models.

### Strengths
The studies problem of this paper is important to the community. In the era of foundation models trained on billion-scale dataset, it is important to re-consider the proper datasets and metrics for evaluation. 

The paper provides interesting findings that show the importance of geographic factors in model evaluation.

### Weaknesses
Although the paper studies an important problem, the technical contribution is limited, and the main findings are mostly empirical. 

The paper mainly consider the geographic factor in evaluation, but does not provide a more comprehensive review, discussion or comparison on the other factors. For instance, most existing CLIP, OpenCLIP models are evaluated on a diverse set of datasets for completeness. Would the dataset diversity be another important factor?

The paper does not provide a very clear and conclusive discussion to point out the potential direction/solutions for resolving the data challenges in evaluation. For instance, what factors should be considered in designing the proper benchmark datasets? What are the right evaluation metrics to consider for evaluating foundation models?

### Questions
Please provide more discussion on the following questions:

What are the most important factors to consider to design the proper benchmark datasets for evaluating foundation models?

What are the proper evaluation metrics to evaluate these factors? 

What are the solutions/directions to design the proper evaluation metrics and benchmarks?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper conducts an extensive empirical evaluation of many vision models with a focus on understanding their geographical robustness. They choose two crowdsourced, geographically distributed datasets GeoDE and DollarStreet to highlight that progress on standard robustness benchmarks curated from ImageNet need not necessarily indicate geographically equitable progress. Specifically, they highlight that improvements in backbones, architectures and data showcase gains in standard benchmarks but progress on crowdsourced datasets is much more sluggish. Secondly, they also highlight the discrepancy between gains in western-centric data (European) compared to Afro-Asian data. Finally, they allude to few possible future directions which could help alleviate this bias.

### Strengths
- This paper addresses a very pertinent problem of investigating the equity of progress through modern deep learning advances in computer vision. They make several important observations pertaining to poor geographical robustness of current model, which can spur several future directions.

- The authors cover several key advances in their study, including large data, larger architecture and different architectures and the observations hold for most cases.

- A brief analysis of possible future directions is also presented, although it is notable that real progress demands labeled data from under-represented geographies, so unlabeled generalization is still an open challenge.

### Weaknesses
 - The paper really does not answer the questions as to why there is a disparity between progress in disparate geographical groups. Is it due to the dataset bias in training data? Is it because of the domain shifts/ label shift between different geographies? Although the current observation that there is a accuracy gap is important, it would be more useful if an inisght into the possible causes is also presented.

- The authors note that they perform manual re-labeling of DollarStreet and GeoDA categories to ImageNet classes. Does this induce any kind of labeling noise which might explain the result? For example, images percieved by model to be `stove` are actually evaluated with `oven`. Since oven and stove designs change worldwide, could this be a possible reason for the accuracy drops? Adding to this, can you also choose only these classes from other robustness benchmarks as well? (Like select a subset of ImageNet-S with only those labels which were mapped to DollarStreet and then evaluate the accuracy). This somehow seems a more fair comparison.

- Adding to the above point, it would be useful to include another contemporary dataset GeoNet [1] into the evaluation since they seem to directly source their dataset based on labels from the ImageNet (thus avoiding relabeling).

- Several recent efforts to study the problem of geographical adaptation are not cited or compared [1,2,3]. GeoNet seems to be a relevant work which addresses similar issues with broadly similar observations. Specifically, the conclusion that scaling model sizes and datasets would not automatically yield geographical robustness seems related, but no discussion or comparison with this work is presented.

- The disparity difference is only computed against Europe and Africa. Does the observations also hold for, say, Europe and Asia?

- Sec 5.3: Could the authors hypothesize why rates of improvement across regions in GeoDE is much more uniform compared to DollarStreet?

### Questions
The major question to the authors is their opinion on why the noted differences are observed. I am eagerly waiting for the responses on this and several other clarifications requested above, and I would be happy to further raise my rating.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Evaluating ~100 ImageNet models across different architectures, scales and pretraining datasets, the authors show that progress on ImageNet and ImageNet-adjacent generalization benchmarks is faster than on geographically diverse data. The crowdsourced, global data they consider are the DollarStreet and GeoDE datasets (released in prior work). They demonstrate that the geographic disparity (difference between the accuracy on European and African objects) increases as the models get better on ImageNet. They show that different robustness interventions and scaling the models and the datasets offer limited improvements, while training and fine-tuning on more diverse and carefully curated balanced data offers a path forward.

### Strengths
* The paper is well-written and easy to understand.
* Studying the generalization ability and geographic/socioeconomic disparities of computer vision models is an important topic.
* This work conducts a large-scale evaluation (of ~100 models) on the 2 geographically diverse datasets exploring the trends of ImageNet models on them.
* There are 2 key findings which I find interesting:
    * Models progress faster on standardized benchmarks than on the geographic datasets. This makes sense given that the standardized benchmarks are better aligned to ImageNet -- the dataset on which the evaluated models were trained and/or fine-tuned.
    * Better ImageNet models increase the geographic disparities as measured on the evaluated datasets. This finding was intuitive and understandable, but worth emphasizing and pointing out to me.
* The authors promise that they will release their code in an easy to use manner ("with just 4 lines of code").
* I appreciate that the authors present a balanced view on the significance of geographic distribution shifts. In particular, they do not see it as an ultimately universal metric but propose it as an additional metric that should be tracked and evaluated.

### Weaknesses
While the findings of this work are interesting and worthwhile, I feel that the technical contributions are relatively limited. In particular, I believe that better attribution to concurrent/prior works and highlighting the consistencies with them might be helpful and fair, especially in the cases where the experimental design is inspired by them.

1. The experiment in Sec. 5.1. is consistent with prior/concurrent work: Rojas et al., DeVries et al. and Ramaswamy et al.
2. The experiment in Sec. 6.3. is also aligned with prior work. Rojas et al. find that training on DollarStreet "can improve the performance of classification tasks for items from lower-income homes", while Ramaswamy et al. "extract features using a ResNet50 model ... and retrain the final layer".

Meanwhile, I acknowledge that, in contrast to prior work, this paper performs a large scale study (with ~100 models) and examines the effectiveness of fine-tuning on one dataset (DollarStreet) and evaluating on another (GeoDE). However, the benefits of the later are also somewhat limited, as we can see in Table 8 - the results on GeoDE are similar regardless of the portion of DollarStreet training data (going from 10 to 100%).

Minor: sometimes the legends and axes on the figures, e.g., on figs. 2 and 4 and 5 in the appendix are a bit hard to read.

### Questions
Q1: I could not find any discussion on the differences between the DollarStreet and GeoDE datasets, while some of the results and the trends on them sometimes differ. Are there any fundamental differences between the two datasets?
* Why is GeoDE omitted from Table 2. Rate of change on it seems closer to ImageNet-V2 and ImageNet-Sketch for example, compared to rate of change on DollarStreet.
* Comparing Figs. 4 and 5 in App. B, the accuracies on GeoDE are significantly higher than those on Dollar Street and sometimes even higher than the ImageNet induced benchmarks. Why is that the case? Is GeoDE "easier" because there are fewer labels or is there another fundamental reason?
* Do you have a hypothesis why the geographic disparities are much more consistent (relatively constant with the model improvements on ImageNet) for GeoDE compared to Dollar Street (Figure 8)? Why are the datasets different in that matter?

Q2: I would like to better understand the driving source of the disparities on Dollar Street. Is it the geographic region or the family income? I expect that these two are correlated, but could you please provide any quantitative results about the disparity when also controlling for family income? I.e., instead of comparing the groups Europe and Africa, compare the groups (Europe, some income level) and (Africa, the same income level).

Q3: Is "Progress Gap" a fair or meaningful metrics? E.g. (following-up on Q1), geographic datasets may be easier/more difficult, with different labeling biases, etc. Could you please provide a brief discussion what might influence the progress rates / contribute to its differences across datasets and further motivate the usage of the progress gap metric?

Q4: Should we expect the models to have high accuracy on all regions? E.g., would fine-tuning w.r.t region deployment be a good idea in certain use cases? How do you envision the models should be deployed in practice? If we look at the problem from fairness perspective, it has been well-known that there exists a trade-off between fairness and accuracy in general, so it might make sense to have different models for the different regions.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
