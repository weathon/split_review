# Eye Fairness: A Large-Scale 3D Imaging Dataset for Equitable Eye Diseases Screening and Fair Identity Scaling

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
Fairness or equity in machine learning is profoundly important for societal well-being, but limited public datasets hinder its progress, especially in the area of medicine. It is undeniable that fairness in medicine is one of the most important areas for fairness learning's applications. Currently, no large-scale public medical datasets with 3D imaging data for fairness learning are available, while 3D imaging data in modern clinics are standard tests for disease diagnosis. In addition, existing medical fairness datasets are actually repurposed datasets, and therefore they typically have limited demographic identity attributes with at most three identity attributes of age, gender and race for fairness modeling. To address this gap, we introduce our Eye Fairness dataset with 30,000 subjects (EyeFairness-30k) covering three major eye diseases including age-related macular degeneration, diabetic retinopathy and glaucoma affecting 380 million patients globally. Our EyeFairness dataset include both 2D fundus photos and 3D optical coherence tomography scans with six demographic identity attributes including age, gender, race, ethnicity, preferred language, and marital status. We also propose a fair identity scaling (FIS) approach combining group and individual scaling together to improve model fairness. Our FIS approach is compared with various the-state-of-the-art fairness learning methods with superior performance in the racial, gender, and ethnicity fairness tasks with 2D and 3D imaging data, which demonstrate the utilities of our EyeFairness dataset for fairness learning. To facilitate fairness comparisons between different models, we propose performance-scaled disparity measures, which can be to compare model fairness account for overall performance levels. The dataset and code are publicly accessible via https://github.com/anonymous4science/EyeFairness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a publicly available large-scale (30,000 subjects) 3D eye imaging dataset (OCT/Fundus) for disease screening and fair identity scaling. The authors also propose a fair identity scaling metric to evaluate model performance.

### Strengths
1. Addressing the fairness issue is an important topic and organizing such a large-scale dataset including three types of measurements: 1) retinal imaging 2) demographic group information 3) disease diagnosis requires a large amount of effort.

2. The authors ran several baselines (EfficientNet, 3D CNN) and evaluated the classification with some fairness metrics (e.g. PSD, DPD).

### Weaknesses
1. The abstract and introduction section is quite lengthy. The core contributions and the highlights can be combined.

2. Some of the writing needs to be improved (e.g. "model performance across different models").

3. The trend of hyperparameter $c$ in Figure 2 is not quite clear since it kind of alternates for both AUC and mean PSD. The authors might need to further discuss the choice of $c$, which still seems rather empirical given the current visualization.

4. The experimental results section is currently flooded with numbers and quite hard to follow.

### Questions
1. The trend of hyperparameter $c$ in Figure 2 is not quite clear since it kind of alternates for both AUC and mean PSD. The authors might need to further discuss the choice of $c$, which still seems rather empirical given the current visualization.

2. The experimental results section is currently flooded with numbers and quite hard to follow.

### Soundness
3 good

### Presentation
2 fair

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces the EyeFairness dataset that includes both 2D fundus photos and 3D optical coherence tomography (OCT) scans, together with six demographic features (age, gender, race, ethnicity, preferred language, marital status), and proposes a fair identity scaling (FIS) approach to combine group and individual scaling to improve model fairness. FIS was demonstrated to improve performance in eye disease screening according to fairness metrics, when implemented together with EfficientNet-B1, against other fairness methods. Fairness methods are especially appropriate in the eye screening domain due to known differing burdens of eye diseases amongst ethnicities.

### Strengths
-	FIS exploits both group and individual scaling to manage within-group sample variation
-	Detailed comparison of proposed FIS against other fairness methods (Adv, FSCL) on various demographic features

### Weaknesses
-	Minimal ablation analysis temperature scaling parameter, FIS group/individual scaling trade-offs actually not very consistent (Figure 2)
-	Side-effects of fairness on adjacent demographic features not considered

### Questions
1. The main contribution of a Fair Identity Scaling (FIS) model with learnable group weights and past individual loss data, might have been analyzed in greater details as to the temperature scaling parameter (alongside fusion weight).
2. Conceptually, the distinction between improvements in “general (AUC) performance” and “fairness” might have been further considered. In particular, from the results in Tables 2 to 7, FIS appears often capable of not only improving “fairness” (i.e. minimizing performance-scaled disparity), but instead often improves performance in all groups (and overall). As such, a natural question might be whether FIS might be used with arbitrary groupings of data, to improve classifier performance.
3. Returning to fairness as a focus, the presented analysis does not appear to be concerned with the impact on fairness amongst other demographic features, when FIS is applied to a particular feature. For example, when FIS is applied on race (as in Tables 2 & 3), what is the effect on results stratified with other features such as gender, ethnicity, age etc.? This appears particularly relevant since the other demographics may be no less significant for the consideration of fairness/equity purposes.
4. The costs of considering fairness might be discussed in greater detail, in particular the possibility that optimizing the proposed PSD metric possibly reduces overall classification performance (and thus medical care). This is because PSD (and other fairness metrics) emphasize between-group equality, which may come at the cost of reduced aggregate performance (although this is largely not the case in this study).

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a new large-scale dataset for eye disease diagnostic comprising of 30’000 2D fundus as well as 3D OCT images for AMD retinopathy and glaucoma diagnostics. In addition to some baseline comparison on fairness metics it also proposes a new fair identity scaling.

### Strengths
The proposed dataset is very valuable as it is very large in size (30’000 patients with 2D and 3D imaging) covering three relevant eye diseases. The analysis is strong and the explored fair identity scaling is a reasonable approach to address inequality in datasets in general. Providing (to my understanding) paired 2D fundus and 3D OCT imaging could also pave the way for new hybrid diagnostic tools.

### Weaknesses
Overall, despite its value, the proposed dataset is somewhat limited in that it seems to be acquired from a single centre in the US. A pooling with previous public datasets would likely increase its value and reduce the “unfairness” by design (rather than re-weighting). 
The statement “effective image augmentation strategies for 3D imaging data are largely unclear” is wrong in my opinion and there is no citation that backs it up. Many 3D medical image analysis methods make good use of image augmentation strategies. 
The chosen baselines are rather simple and no true SOTA results are presented. The presentation of the results is mainly focussed on numerical comparison and I would be missing a more in-depth analysis or discussion why certain races perform better or worse. E.g. since Hispanics are under-represented in the dataset it is not intuitive that this group achieves the highest AUC without and not with FIS. 
It remains unclear whether the data is always “paired”, ie. the same patient is measured with 2D and 3D imaging.

### Questions
Clarify the 2D/3D data split wrt. patients. Discuss a pooling of other public datasets from centres with different scanners / from different countries. Expand the baselines and correct the statement of non-existing 3D augmentation strategies.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces the EyeFairness dataset, aimed to promote the fairness study for medical imaging. The dataset comprises 30,000 subjects with both 2D and 3D imaging data, capturing various demographic attributes. Additionally, the authors propose a fair identity scaling (FIS) approach to enhance model fairness for this dataset.

### Strengths
- This paper studies an important topic of fairness for medical imaging. The authors introduce a relatively large-scale dataset for 2D fundus photos and 3D OCT scans. It covers major eye diseases and captures a few different demographic attributes, which can be a useful resource for the community.
- The authors propose Fair Identity Scaling (FIS) to improve the fairness of the model.

### Weaknesses
 - The authors didn't tune the hyper-parameters of the baseline methods but only used the default HPs, which leads to unfair comparisons. The baseline methods are not designed for medical imaging, so if applied to a different setting, the hyperparameters should be carefully tuned to get the best performance. Especially there're adversarial training method and self-supervised pretraining method that are very sensitive to the HPs.
- The definition of performance-scaled disparity (PSD) is not clear. It says in the paper: "PSD metrics are calculated as the standard deviation of group performance or absolute maximum group performance difference divided by overall performance." Which one did the authors use? And what does Mean PSD and Max PSD mean?
- Also, regarding the metrics, authors can provide the worst-case AUC and the AUC gap between best-performing and worst-performing groups besides the current overall AUC and group-wise AUC. It would be clearer to directly look at the AUC gap to validate the effectiveness of the proposed methods. Additionally, what are the advantages of using PSD instead of the AUC gap? Consider an extreme case: for model 1, two groups have an AUC of 25% and 51% while for model 2, two groups have an AUC of 50% and 100%. According to the authors' definition, $PSD_1 = (51-25)/51=0.51 < PSD_2 = (100-50)/100=0.5$, but can you say model 2 is fairer than model 1 as it's the smaller the better? I know the AUC usually is higher than 50% but this is just an example and I think there are many similar cases in regular scenarios.
- I think Table 1 in this paper is taken from Table 1 in [1] without reference as (1) the number of images of each dataset is not the original number but the number after preprocessing by [1] and (2) the so-called ADNI 1.5T is a subset of the large ADNI dataset [2] extracted by [1].
- At the time I wrote this review, the GitHub repo authors provided was empty.
- Minor: the current citation style makes reading difficult. The author should use (Deng et al. (2009)) instead of Deng et al. (2009), i.e. \citep instead of \cite.

### Questions
- Can the authors also provide further breakdown statistics of the intersectional groups, e.g. black females?
- The dataset also contains some other attributes such as preferred language. I'm not very sure how this is related to eye diseases and fairness, e.g. do non-English speaking patients get lower AUC? But how does the eye imaging model perceive the speaking? Also, the authors did not evaluate the performance of different subgroups of preferred language and marital status.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
