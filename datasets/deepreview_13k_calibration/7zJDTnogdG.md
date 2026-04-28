# Electrocardiogram Foundation Model Using Temporally Augmented Patient Contrastive Learning

- Decision: Reject
- Avg Score: 3.33
- Scores: 6, 3, 3, 1, 6, 1

## Abstract
Electrocardiograms ($ECGs$) capture the electrical activity of the heart, offering rich diagnostic and prognostic insights. Traditionally, electrocardiograms are interpreted by human experts, but deep learning is now encroaching on this domain and combining human-like intelligence with machine precision for a deeper insight. Self-supervised pretraining is essential for maximising the potential of scarce medical data. Applied to $ECGs$, patient-contrastive learning has shown promising results, by utilising the natural variations in the cardiac signals. In this study, we introduce  **T**emporally **A**ugmented **P**atient **C**ontrastive **L**earning of **R**epresentations ($TA\text{-}PCLR$), a novel approach that incorporates temporal augmentations into a patient contrastive self-supervised foundation model. Trained on one of the largest diverse cohorts of more than six million unlabelled electrocardiograms from three continents, we demonstrate the efficacy of our approach and show its value as a feature extraction tool for small and medium-sized labeled datasets. We also validate the performance on an open-source external cohort, surpassing other pretraining approaches while outperforming an ensemble of fully supervised deep networks on some labels. Additionally, we conduct a detailed exploration of how the pretraining and labeled electrocardiogram dataset distributions impact supervised task performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors introduce a novel, ECG-specific self-supervised learning approach which incorporates temporal augmentations (random cropping) over patient contrastive methodology. This work is portrayed as a new foundation model for ECG interpretation, where experiments are run on a large, private pretraining dataset of six million unlabeled ECGs and involves a number of downstream tasks (age, sex, mortality, and diagnostic super-classes). They further examine how the pretraining dataset distribution impacts downstream performance by way of dataset-specific training and evaluation.

### Strengths
Their use of a multi-source pretraining dataset is certainly a strength. Their literature background gives a relatively strong, concise overview of existing pretraining approaches. Their methodology selection is, in large part, explained well and intuitively. Their data scaling was vital in demonstrating TA-PCLR's dominant performance over fully-supervised methods for smaller datasets. I have not personally seen the random cropping approach they introduced as their temporal augmentation, which speaks, in part, to its originality.

### Weaknesses
This paper is introducing a novel method more than it does a foundation model. Although they do pretrain on a large dataset, there is a lack of experimentation which only seems reasonable when releasing a foundation model. Namely, model scaling, considering how they adopt a relatively smaller architecture; They pride themselves on this point, however, this is unfounded due to a lack of confirmation that such a small deep neural network could actually make most effective use of the vast pretraining dataset. This would have been vital to confirm. The literature background refers to just a couple existing foundation models (and only in passing). There is no interpretability method. They also report just one metric per task, which greatly reduces study comparability. Considering these points, it seems lacking for a foundation model paper, even though it seems sufficient for simply introducing a novel pretraining method.

Considering this paper is introducing a new pretraining method, it may have benefited from an ablation study of its various pretraining components beyond a comparison to PCLR. Or, if the authors believe that this is all that's necessary as an ablation, then explaining this in more detail to better communicate their contribution.

Certain methodological matters are somewhat ambiguous. It was unclear whether hyperparameter tuning was performed. It is not made abundantly clear that the positive pairs are necessarily augmented instances of the same recording (and not from different recordings of the same patient). It is unclear whether there was any signal preprocessing (such as standardization), and if not, this may be worth stating.

Certain purported claims are left unsubstantiated, for example: "Human perception is limited by low visual accuracy, gaps in theoretical knowledge, and the complexity of the diverse, non-linear, interrelations."

Certain references may be misleading provided its context, for example, "Hybrid techniques combining contrastive learning and generative pretraining based on transformer architecture have been implemented to train foundation models for ECG feature extraction (Song et al., 2024; McKeen et al., 2024)" may imply that ECG-FM (McKeen et al., 2024) using generative pretraining, which is not true.

Certain definitions are questionable, for example, the statement that, "There are diverse contrastive learning approaches, differing in their definitions of the positive and negative instances and the loss computations" negates how certain contrastive methods do not apply here, such as using a triplet loss.  Or also "In the visual image domain, the positives are augmentations (transformations) of the same image while the negatives are augmentations from others", which is not necessarily true. This also occurs in the literature background. Simply making less specific claims or by allowing for the existence of other alternatives (e.g., stating "may" or "usually") could solve the issue. Another is "The feature-generating model is frozen while a single neuron is trained to predict each label", which is misleading since neurons are computational nodes, it is the linear layer parameters being trained.

Certain methods, such as Song et al., 2024 and 3KG, should likely be referenced in the literature background in greater detail. There is some methodology mixed into the results section (Song et al., 2024), which may or may not be necessary, but can hurt the flow.

There are typos ("same train/test splits..") and a random section link ("Unique patients1").

Calling the dataset-specific training and evaluation "the first investigation of its kind" is an ambitious statement, where the abstract had me expecting some kind of domain shift/adaptation methodology to be applied. The analysis seems good, does emphasize their multi-source dataset, and is important to understand how data distributions affect performance (e.g., healthy versus unhealthy subjects); However, the results of this analysis left me unsure as to what explicit value it added to this particular study.

More discussion is warranted as to why performance on the fully supervised benchmarks would become similar after a finetuning dataset of 100k is reached.

The paper could have benefited from additional non-tabular figures, such as a data scaling graph.

### Questions
Is it fitting for this paper to introduce a foundation model given the nature of the experimentation performed, as well as those related points raised under "Weaknesses"?

I started (and sort of left) the paper wondering: Is TA-PCLR a combination of individual existing methods which form a novel aggregate approach? Even by name, it is clear that TA-PCLR builds off the PCLR method, and yet how is never made totally clear - one would have to read the PCLR paper to learn this. Is it simply adding random temporal cropping to the PCLR method? Was the method/cropping approach inspired by other work in the ECG or timeseries space?

Considering, "The number of ECGs from each patient greatly differs and thus the training epoch is defined as one complete iteration for all unique patients with the positive views randomly sampled at training time. In this way, the training is not biased by patients having more ECGs while still exploiting the available data diversity." I agree that this maintains better overall population diversity, however I would be curious to know whether this would lead to biasing the model away from representing the conditions of those people with chronic health issues (i.e., the people who do have those higher ECG counts). What if it were those people whom were the most important to represent well?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces Temporally Augmented Patient Contrastive Learning of Representations (TA-PCLR), a novel approach that incorporates temporal augmentations into a patient contrastive self-supervised foundation model.

### Strengths
1. This method adds temporally augmented patient contrastive learning that incorporates augmentations along the temporal axis.
2. This method constructed a new multi-center dataset for training with over six million ECGs with four cohorts from three different continents.

### Weaknesses
1. The organization of this paper needs improvement. The color of Fig2 is too dark. There are some empty results in table 4 and table 5, which should add a line '-' and explain why.
2. In table2, the pertaining cohorts in PCLR and TA-PCLR are different. One is MGH, and another is BCSV. It can't get any conclusion on the effectiveness of TA-PCLR because of using different cohorts.
3. The novelty of this method is concerned. Basically, this method just adds a general contrastive learning strategy to learn EEGs between patients.

### Questions
When showing performance comparison between Resnet and TA-PCLR, are there any latest SOTA methods like attention or transformer-based models to compare?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The study aimed to develop a contrastive learning based foundation model for ECG data to predict patients Age, Sex, 5-year mortality and various cardio abnormalities. The authors claimed that they have proposed a novel approach by introducing temporal augmentation to the previously proposed contrastive learning algorithm PCLR. Experiments with the major ECG datasets that are publicly available were conducted to benchmark the performance of the proposed method to some of the existing methods.

### Strengths
Development of foundation models for medical data and signals is obviously an important topic worth studying. Additionally, it is also true that the cost for engaging physicians to provide high quality labels for medical data is indeed much higher than many other domains. I can see how this can motivate the use of contrastive learning on medical data analysis.

### Weaknesses
1/ Lack of originality and novelty

The proposed method is built upon the previously published contrastive learning backbone, PCLR (by Diamant, Nathaniel, et al in 2022). The only enhancement was the introduction of some temporal augmentation of the ECG signals. These temporal augmentations included zero-marking and random clipping. These augmentations were nothing new too. Also, none of these augmentations were specifically inspired by any in-depth understanding of the ECG signals and its unique characteristics. The temporal augmentations, such as zero-masking and random clipping, are generic time-series augmentations and do not leverage specific knowledge of ECG signal morphology or physiological relevance. For instance, the authors do not explore augmentations that preserve the isoelectric line or the specific intervals (PR, QRS, QT) which are crucial for clinical interpretation. A commonly used loss function was used as well.

I failed to the see the technical originality and contributions here.

Can the authors highlight and justify their technical novelty and contributions in this work further?

2/ Possible inflating some information
The authors claimed they trained their foundation model over 6 Mil ECGs in the introduction. After reading into the details then I learned that the authors actually counted a 12-lead ECG measurements of a single patient 12 ECG signals. This is a bit unusual. Can't help but to guess whether the team might present the dataset size in an inflated manner?

3/ Poorly designed experiments

The experimental design was so fragmented and confusing. There lacked of a systematic framework and experimental design to fairly benchmark the proposed method over the SOA methods over various tasks and datasets.

In Table 2, the authors compared PCLR with the proposed TA-PCLR. But PCLR were only pre-trained over the MGH and BIDMC datasets but not the combined BCSV dataset. The BCSV combined dataset is the largest. Why didn't a head-to-head comparison was done for PCLR and TA-PCLR for the BCSV dataset?

In Table 3, the authors then compared the proposed TA-PCLR against ResNet. Why ResNet, quite an old model, was picked as a baseline model to be compared with here? Why didn't the performance of PCLR included here?

In Table Table 4, the authors then compared TA-PCLR with the ensemble model developed by Strodthoff et al. in 2021 and the model in Bickmann et al. (2024) for the classification for both the super classes and sub classes for abnormalities. However, many readings for the result table were missing. What happened?

In Table 5, similarly, many of the result readings were missing. What happened?

It felt like the team didn't manage to finish the study in time and yet just submit the manuscript before the deadline?

### Questions
Please refer to the above section for my questions.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper presents an ECG-based foundation model using a large-scale dataset of six million ECGs from different institutions. The authors propose to use zero masking and random cropping as augmentation strategies.

### Strengths
1. The main strength of the paper is the scale of the dataset that they have access to, which combines data from multiple cohorts. 
2. The aim of building an ECG foundation model is interesting and important. 
3. The authors evaluate their proposed framework for multiple downstream prediction tasks.

### Weaknesses
1. The proposed work lacks novelty. The framework does not possess originality expected by ICLR and is very similar to existing frameworks. In fact, it is unclear to me what the novelty is. The methods section presents the vanilla InfoNCE loss and then discusses the augmentations, preprocessing, architecture and training scheme.
2. Comparison to existing SOTA frameworks is very limited. The authors do mention relevant papers but only compare to a few in the results section. There are many notable works in this area that are worth comparing to.
3. Did the authors conduct hyperparameter tuning for their proposed framework and baselines? What was the approach? I appreciate that the final values are listed in the appendix however this is not sufficient.
4. The authors did not conduct any statistical significance testing nor did they provide confidence intervals to understand whether the performance improvements are actually worthwhile.
5. Numbers should be presented with three significant figures.
6. There are empty rows in Tables 4 and 6, why is that?

### Questions
Please see above.

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Summary
The study introduces TA-PCLR (Temporally Augmented Patient Contrastive Learning for ECG Representations), a self-supervised learning approach for ECG data. This method combines temporal augmentations and patient-based contrastive learning to improve representation learning in ECGs. Key highlights include:

1. Novelty of TA-PCLR: It introduces temporal augmentations, such as zero-masking and random cropping, to enrich representations while preserving clinical relevance.
2. Performance Improvements: TA-PCLR outperforms previous methods in tasks such as predicting age, sex, and five-year mortality from ECG data, especially on small and medium-sized datasets where labeled data is scarce.
3. Impact of Dataset Demographics: The study explores how population diversity in training datasets influences model performance, showing that a mixed, diseased cohort provides richer ECG feature diversity and enhances model performance.

In indipendent validation with the PTB-XL dataset, TA-PCLR surpasses other models in diagnostic tasks, establishing itself as a robust foundation model for ECG interpretation. Future directions include refining data augmentations and enhancing interpretability in ECG feature learning.

### Strengths
- Effective Representation Learning: TA-PCLR leverages temporal augmentations with patient-based contrastive learning to enhance feature extraction. This approach enables more nuanced and clinically relevant ECG representations, which are critical for downstream diagnostic tasks, even in data-scarce environments.
- Broad Applicability and Generalization: Training on a diverse dataset of over 6 million ECGs from multiple global cohorts makes TA-PCLR highly generalizable. This diversity allows the model to perform well across varied patient demographics and health conditions, ensuring its robustness across different healthcare settings.
- Superior Performance on Limited Data: The model’s ability to perform better than fully supervised methods on small to medium-sized labeled datasets makes it especially valuable in clinical contexts where labeled data is often scarce. This makes TA-PCLR a powerful tool for institutions with limited data resources.

### Weaknesses
The important contribution of this research is that it highlights the importance of geographical and racial diversity in training data when creating machine learning models for electrocardiograms, but on the other hand, the results of this research have only been verified using the PTB-XL dataset.
The scope of this study may be narrow than the general interest of ICLR main conference.

### Questions
Do the authors have any specific proposals for the above weaknesses? How can we build the necessary data sets to verify geographical and racial diversity?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper proposes a novel Electrocardiogram Foundation Model using Temporally Augmented Patient Contrastive Learning (TA-PCLR), focusing on building a large-scale FM using ECG data. The TA-PCLR model combines patient-based contrastive learning with temporal augmentations, and it demonstrates superior results over traditional fully-supervised models.

### Strengths
Compared to other ECG FM studies, a key strength of this paper is the utilization of large-scale data. By handling over six million ECGs, the model incorporates diverse demographic characteristics, creating favorable conditions for improved model generalization.

### Weaknesses
The paper appears to lack analytical depth. Adding an exploratory data analysis (EDA) would provide a more comprehensive understanding of data distribution and representation, which could, in turn, enhance the reliability of the results. Additionally, assessing the representation distribution across different data types could further substantiate the FM’s robustness. For example, first, using methods like PCA or t-SNE, visualize the embeddings generated by the model in 2D or 3D to examine whether different data types fall within similar distributions or are distinctly separated. This analysis helps assess if the model represents various data types consistently. Second, analyze whether different data types are well-mixed or independently clustered to understand if the model extracts consistent features across types or demonstrates bias toward certain types. Third, examine specific features the model prioritizes across data types (e.g., certain words in text, patterns in images, frequency ranges in signals) to determine if the model consistently learns representations across data types. Lastly, feature correlation analysis assesses the relationships between key features learned by the model, which is especially insightful for multimodal data to understand how the model connects specific features across types.

The model primarily relies on temporal transformations such as zero-masking and cropping, with limited exploration of other data augmentation techniques. Moreover, the training approach employs conventional contrastive learning without attempting novel methods. The choice to rely solely on masking lacks sufficient justification, making it challenging to fully accept this design decision. Given the reliance on a limited set of augmentation techniques (https://dl.acm.org/doi/10.1145/3511808.3557591, https://arxiv.org/abs/2204.04360), it is difficult to assess their true effectiveness. To strengthen the study and provide clearer evidence of the augmentation strategy’s impact, it would be beneficial to incorporate and compare additional methods discussed in previous research, as outlined in this paper and this paper. Such a comparative approach would provide deeper insights and enhance the robustness and reliability of the findings regarding the model’s performance.

### Questions
To substantiate the proposed approach, it is essential to compare and analyze its performance against various existing learning approaches. Currently, the model relies on contrastive learning; however, evaluating its performance relative to other frameworks, such as Masked Autoencoder (MAE), could provide valuable insights. Specifically, understanding how TA-PCLR performs in comparison to MAE or other non-contrastive self-supervised learning methods would offer a clearer picture of its strengths and limitations in feature extraction and representation learning.

From a technical perspective, additional experiments are proposed to further validate the approach. Comparing the model’s performance against currently available models, such as those discussed in (https://arxiv.org/abs/2408.05178), would provide a solid benchmark. Additionally, applying alternative contrastive learning techniques, such as MoCo, could reveal how different contrastive frameworks impact model performance. It would also be insightful to experiment with exclusively using MAE as a non-contrastive method to better understand the unique contributions of the contrastive approach in this context.

By conducting these comparative experiments with a range of learning frameworks, this study could offer a more comprehensive evaluation, showcasing both the effectiveness of TA-PCLR and the relative benefits of its contrastive learning strategy. Such an analysis would greatly enhance the reliability and depth of the findings regarding the model’s capabilities in feature extraction and representation learning.
A comparative analysis would allow us to assess whether TA-PCLR’s temporal augmentations and patient-based contrastive learning truly offer a competitive advantage over alternative methods. Such comparisons could reveal potential improvements in the model’s predictive accuracy, robustness, and generalization across different ECG data subsets.

### Soundness
2

### Presentation
3

### Contribution
2
