# FedCVD: The First Real-World Federated Learning Benchmark on Cardiovascular Disease Data

- Decision: Reject
- Scores: 6, 5, 3, 5

## Abstract
Cardiovascular diseases (CVDs) are currently the leading cause of death worldwide, highlighting the critical need for early diagnosis and treatment. Machine learning (ML) methods can help diagnose CVDs early, but their performance relies on access to substantial data with high quality. However, the sensitive nature of healthcare data often restricts individual clinical institutions from sharing data to train sufficiently generalized and unbiased ML models. Federated Learning (FL) is an emerging approach, which offers a promising solution by enabling collaborative model training across multiple participants without compromising the privacy of the individual data owners. However, to the best of our knowledge, there has been limited prior research applying FL to the cardiovascular disease domain. Moreover, existing FL benchmarks and datasets are typically simulated and may fall short of replicating the complexity of natural heterogeneity found in realistic datasets that challenges current FL algorithms. To address these gaps, this paper presents the first real-world FL benchmark for cardiovascular disease detection, named FedCVD. This benchmark comprises two major tasks: electrocardiogram (ECG) classification and echocardiogram (ECHO) segmentation,  based on naturally scattered datasets constructed from the CVD data of seven institutions. Our extensive experiments on these datasets reveal that FL faces new challenges with real-world non-IID and long-tail data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors present a benchmark for federated learning applied to two cardiovascular disease related modalities: ECG and ECHO. The ECG dataset comprises 4 publicly available datasets, while the ECHO dataset comprises 3 publicly available datasets. The authors evaluate several existing SOTA approaches, including FedAvg, FedProx, Scaffold, FedInit, Ditto, FedSM, and FedALA, and investigate several settings: local vs global test set performance, long-tail challenge, non-IID challenge, and label incompleteness.

### Strengths
- The paper aggregates several publicly available datasets that are useful for advancing research in this area in future work. 
- The repository is well organized and easy to navigate.
- The analysis is thorough and spans three different challenges related to FL (long-tail distribution, label incompleteness, and non-IID data).
- The authors include several SOTA baselines and describe their hyperparameter tuning strategy. 
- They also consistently provide confidence intervals across all results tables. 
- The figures and tables are neat and easy to understand.

### Weaknesses
 - Can you clarify the key differences and potential impact of your benchmark compared to existing work like Goto et al. 2022. Can you also discuss how the focus on long-tailedness and incomplete labels advances the field beyond prior benchmarks?
- To improve the paper's accuracy, can you change the title so that it better reflects the scope, e.g. "FedCVD: A Federated Learning Benchmark for ECG Classification and Echocardiogram Segmentation"?
- The paper requires significant proofreading, i.e. inconsistencies with abbreviations / capitalization / spelling mistakes.
- The abstract should make it clear that the benchmark is using publicly available datasets, rather than presenting new datasets. 
- The API functions in Figure 1 are more like functions in their repository so I'm not sure if the term API is the best fit description. 
- The dataset sizes and characteristics should be summarized in the main text.
- To better interpret the results, could you discuss why certain FL methods performed better on the long-tail challenge or label incompleteness scenarios?

### Questions
Please see above

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This is a benchmark study aiming to evaluate the performance of the commonly used Federated Learning strategies for both the ECG-based arrhythmia classification task and also the echocardiogram video segmentation task. The study specifically focused to investigate the impact from non-IID in data from different sites, the long-tail distribution (where distributions among labels are very imbalanced) and the label incompleteness.

Four ECG datasets and three echo datasets were included for the benchmarking exercise. Seven federated learning algorithms were included, and their performances were compared with the one from a centralized scenario and the ones from individual sites.

### Strengths
1/ The manuscript was reasonably written. Most of the key concepts were explained clearly.

2/ Although there is some related work to evaluate the performance federated learning algorithms over multiple ECG datasets, this can be the first benchmarking exercise that have conducted  detailed and extensive experiments to evaluate seven FL algorithms over both the ECG-based arrhythmia classification task and also the ECHO video segmentation task.

3/ Major datasets for both tasks that are publicly available are included.

### Weaknesses
1/ As the authors also mentioned, the reported study is closely related to the Goto et al 2022 (https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.121.058696) study. Although the author did mentioned about that study in the manuscript, think a more detailed explanations on how different and the new contributions of this work compared to the Goto study is still needed. Would suggest the authors to clearly compared the datasets included in both studies, the FL algorithms included, the different evaluation metrics measured, and this work's unique emphasis on non-IID in data, the long-tail distribution and the label incompleteness.

2/ For the ECG-based arrhythmia classification study, ResNet was chosen to be the base model. However, the authors did not explain the rational behind why model was chosen to be the only ONE base model for this study. Simply citing a previous paper won't justify that. Could explain what was the rational in choosing the current model?

More importantly, to report a more robust benchmarking study, suggest the author may investigate how different base models may or may not impact the performance of the included FL algorithms over the benchmarking datasets. It will useful to investigate why there may or may not be an impact?

Therefore, suggest the authors to include other base models too. Believe some customized LSTM and Transformers have been developed for ECG classification as well.  Would it be possible to include them as base models too?

3/ Similar to point 2, 2-D Unet was chosen to be the only base model in this study. Again, could explain the rationale behind picking the current base model?

Additionally, it will be also interesting to study how different segmentation base models may have different strengths in addressing the non-IID in data, the long-tail distribution and the label incompleteness challenges.

Therefore, suggest the authors to consider including one or two more base models?

Some of these possibilities could be:
Leclerc, Sarah, et al. "Deep learning for segmentation using an open large-scale dataset in 2D echocardiography." IEEE transactions on medical imaging 38.9 (2019): 2198-2210.

Wu, Huisi, et al. "Super-efficient echocardiography video segmentation via proxy-and kernel-based semi-supervised learning." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 37. No. 3. 2023.

Yang, Jiewen, et al. "GraphEcho: Graph-Driven Unsupervised Domain Adaptation for Echocardiogram Video Segmentation." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023.

and 3D models e.g.

Hatamizadeh, Ali, et al. "Unetr: Transformers for 3d medical image segmentation." Proceedings of the IEEE/CVF winter conference on applications of computer vision. 2022.

4/ For ECG datasets, would it make sense to include the Icentia11K dataset too? Although it was build mainly for self-supervised algorithms, part of the datasets do have labels? Additionally, it helps to expand the study's technical coverage if the team can expand their work to investigate how the FL learning mechanism can be combined with the newly proposed self-supervised learning models over CVD datasets.

Tan, Shawn, et al. "Icentia11k: An unsupervised representation learning dataset for arrhythmia subtype discovery." arXiv preprint arXiv:1910.09570 (2019).

### Questions
Please refer to the weakness section

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes FedCVD, the first real-world FL benchmark for CVD diagnosis. By utilizing FL, it aims to enhance the accuracy of CVD diagnosis while preserving data privacy, enabling collaborative model training across multiple institutions. Traditional FL research has largely relied on simulated data, often failing to capture the complexity of real-world data distributions. To address this limitation, FedCVD incorporates two primary tasks, ECG classification and ECHO segmentation, based on real ECG and ECHO data collected from seven institutions, reflecting the challenges of federated learning in a real-world healthcare setting.

### Strengths
The primary strength of this paper is its systematic approach to evaluating CVD-related tasks using federated learning. It effectively addresses the practical challenges of Non-IID and long-tail distributions in healthcare data, which are critical issues for achieving robust model performance. Non-IID data distribution, particularly when labels are collected independently from multiple institutions rather than through a consortium, introduces complexities in model evaluation. The paper adeptly tackles this challenge, offering a realistic evaluation approach that reflects the heterogeneous data across different institutions, thus enhancing the credibility of the proposed FL setting.

Moreover, the long-tail challenge is approached innovatively using a Top-K metric, which allows for detailed performance evaluation of model accuracy across classes with varying sample distributions. This approach provides valuable insights into the model’s handling of label imbalance in real CVD data. Additionally, FedCVD rigorously analyzes various FL methodologies, demonstrating how each method performs under the specific characteristics of CVD data. With open-source code available, it contributes a practical and reproducible resource for FL research in healthcare.

### Weaknesses
A limitation of this paper is that, in cases of label-non-IID, the increased label sparsity across institutions may pose challenges to quantitative evaluation. As the label distribution varies more widely across institutions, certain labels may not be adequately represented, potentially compromising evaluation reliability.

Another significant limitation is whether the domain of this study aligns with the conference scope. Despite the academic value of the proposed framework, it may not be fully aligned with the themes of the conference, potentially impacting its acceptance and reception.

### Questions
Could you please clarify what aspects make this benchmark-focused paper suitable for this conference, particularly in terms of its contributions to evaluating real-world healthcare data?

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work collates and harmonises 7 open-access cardiology datasets (4 ECG, 3 ECHO) to create a realistic benchmark for federated learning. The authors show that existing federated learning benchmarks may not adequately reflect real-world challenges in cardiovascular research: 1) natural partitions are needed to reflect inter-institution heterogeneity; 2) clinical outcomes of interest are often not binary but multi-class and long-tailed; 3) labelling may differ significantly between

### Strengths
Medical machine learning still lags behind many other domains, in part owing to the difficulties of collecting sufficiently large and diverse data. Federated learning is increasingly important to address this challenge and allow the training of larger models in secure and privacy-preserving manner. However, studies that evaluate the performance of different FL algorithms rely on artificially federated data that does not reflect conditions encountered in the wild. This work introduces two complex datasets that can help facilitate more realistic benchmarking of FL algorithms.

### Weaknesses
The paper tries to do many things at once, which makes it difficult to read at times. Here are some examples: 
- Scope: while the work presents itself as a benchmark for CVD, in terms of modalities it contains separate benchmarks for a time series (ECG) and 2D images/videos (ECHO). The benchmarks in Table 1 span additional modalities including tabular data (FedTD), time-to-event data (Flamby), graphs (FedDTI), NLP (FEDLEGAL), and multimodal data (FedMultimodal). It is unclear whether they are even comparable. 
- Related work: the related work section does not have a clear logical flow. As far as I can see, the main arguments are: 1) AI is important in cardiology and spans ECGs and images among other modalities (could be argued more concisely); 2) most existing applications are trained on single centre data but multicentre data is needed for reasons XYZ (currently not clear why multicentre data is needed); 3) federated learning provides a privacy-preserving way to share data between institutions but most studies to date only show proof-of-concept with artificially federated data; 4) realistic benchmarks for FL are needed (why?) and some work has been done in that direction, but they do not completely consider the challenges faced in FL for CVD. Section headings may help to guide the reader through this section. 
- The Proposed FedCVD: This section introduces the datasets, metrics, baseline models, and challenges. However, it does not actually introduce the framework. Here I would expect to see the flow of an experiment, how the framework/API supports adding new datasets or models, etc. The metrics and baseline models, on the other hand, belong into the experiment section and are indeed repeated there.
- Experiments: The current version is structured by dataset (Fed-ECG and Fed-ECHO). It might make it more readable if the authors group the results by challenges (non-IID, long-tail, incomplete) instead. The experiment section also mixes methods with results. For example, on page 8 F1-STD and Top-K are introduced right next to the discussion of the results. Consider explaining your metrics earlier in the experiment details section.

### Questions
Major suggestions: 
- Variability in the algorithms' performance estimates seemed quite substantial at times (e.g., Table 2 GLOBAL Mi-F1 FedAvg 67.9+/-3.8 compared to the leading Scaffold 70.1+/-0.8) , making it unclear whether the differences between algorithms are actually meaningful or just due to chance. I was unable to find information on how variability was calculated. Please include that information and consider adding formal tests for differences. 
- It is not immediately obvious to me how some algorithms like Ditto in Table 2 can have a much lower Mi-F1 in the GLOBAL set (68.1) than in any single local set (min 73.4). Do they authors have an intuitive explanation for this?
- I was unable to find any details on the semi-supervised algorithms for the ECHO data. Please add a clear description of what was done in those cases. 

Minor suggestions: 
- it might be worth replacing Client 1-4 with the actual dataset names to make sure which local performance is shown.

### Soundness
3

### Presentation
1

### Contribution
3
