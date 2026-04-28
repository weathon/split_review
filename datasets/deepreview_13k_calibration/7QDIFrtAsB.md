# Anomaly Detection by Estimating Gradients of the Tabular Data Distribution

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
Detecting anomalies in tabular data from various domains has become increasingly important in deep learning research. Simultaneously, the development of generative models has advanced, offering powerful mechanisms for detecting anomalies by modeling normal data. In this paper, we propose a novel method for anomaly detection in a one-class classification setting using a noise conditional score network (NCSN). NCSNs, which can learn the gradients of log probability density functions over many noise-perturbed data distributions, are known for their diverse sampling even in low-density regions of the training data. This effect can also be utilized, and thus, the NCSN can be used directly as an anomaly indicator with an anomaly score derived from a simplified loss function. This effect will be analyzed in detail. Our method is trained on normal behavior data, enabling it to differentiate between normal and anomalous behaviors in test scenarios. To evaluate our approach extensively, we created the world's largest benchmark for anomaly detection in tabular data with 49 baseline methods consisting of the ADBench benchmark and several more datasets from the literature. Overall, our approach shows state-of-the-art performance across the benchmark.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This manuscript proposes to utilise a well-established diffusion model, Noise Conditional Score Network (NCSN), to perform unsupervised anomaly detection (including the semi-supervised one-class anomaly detection setting) in tabular data, leading to an anomaly detection method called NCSNAD. During the training phase, NCSNAD learns a vector field which represents the underlying distribution of (normal) data; while during the inference phase, NCSNAD assigns an anomaly score by estimating the likelihood of staying within the learned vector  filed for each test data instance. Overall, NCSNAD follows the generic principles of one-class anomaly detection, where the novelty of NCSNAD lies in utilising diffusion model to learn the data distribution of normal instances. After establishing NCSNAD, they conduct very extensive experiments (on 57+15 datasets ) to show the effectiveness of NCSNAD and compare it with SOTA baselines (with more than 50 anomaly detectors). The results show that NCSNAD outperforms most baselines in terms of detection accuracy (measured with three different metrics).

### Strengths
1. Overall, this manuscript is well organised and easy to follow;
2. The authors conducted very extensive experiments, showing the effectiveness of their method and superiority compared to SOTA baselines;
3. Although there already exist some work that employ diffusion models to perform anomaly detection in tabular data, this research topic is definitely worthy of more research attention;

### Weaknesses
1. The novelty is limited: it seems that the authors simply employ the established model NCSN, with a simplified loss function to perform anomaly detection. It is a very straightforward idea. 
2. NCSNAD is not well motivated. For example, when comparing to the closest related work DTE (which is the only existing diffusion model based anomaly detection method in tabular data), the authors did not explain why they chose to use NCSN rather than DDPM; what are the corresponding pros and cons of each method, etc.?
3. I appreciate that the authors have conducted very extensive experiments (in the sense there are many datasets and baselines), but I have several major concerns regarding the experiments:
* 3.1. they only considered the semi-supervised one-class setting in this manuscript: namely they utilise 50% of normal data instances as training while the rest data instances as validation or test set. In other words, they did not consider the truly unsupervised setting, where the training set should contain both normal and abnormal data instances. As far as I know, one-class anomaly detection anomaly detection methods usually do not work well if the training data is contaminated (namely containing abnormal instances);
* 3.2. the results show that simpler models like LUNAR, KPCA, and especially GMM (which have less training and inference time) achieve comparable detection accuracy (in terms of the box plots of ROC-AUC, F1-Score, or ROC-PR). A natural question raises: why people in anomaly detection community will use NCSNAD? (which is more complicated and computationally more expensive)
* 3.3. the authors try to show that NCSNAD (or NCSNADVAL) is the best method by comparing the absolute performance metrics by providing the box-plots of ROC-AUC, F1-Score, or ROC-PR. My question is that: is this informative or fair to other methods? To mitigate this issue, I suggest the authors to include the results of relative rankings (namely the ranking of anomaly detectors on each dataset, and then aggregate the results in a similar manner), which I believe is more informative. 
* 3.4. I friendly point out that NCSNADVAL is unfair to other methods: if the authors utilise the validation set with labels to tune NCSNAD, this validation set should also be used to tune all other baselines. A more critical question is that: if I have a validation set with labels, why don’t we directly use it to train the models (by turning unsupervised into semi-supervised with the help of these labels)?

### Questions
Please see the weak points.

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
The authors propose a new method for semi-supervised anomaly detection using a noise conditional score network. They demonstrate the efficacy of their new method on a large benchmark of tabular datasets. They showcase the interpretability of their method on computer vision anomaly detection and provide extensive resources for reproducibility of the paper.

### Strengths
To the best of my knowledge, this paper showcases the first application of score networks to anomaly detection. The theoretical foundations are well substantiated. Similarly, I commend the authors for aiming to make the paper reproducible by providing a readme and all code used in the experiments. The authors have put considerable effort in constructing a large benchmark, including many methods and datasets from various different studies.

### Weaknesses
- The paper could be more clear with respect to its domain: i.e. **semi-supervised/one-class** anomaly detection. For example at line 55-57 it is stated that training is done unsupervised, in absence of labels. While I agree that the training is done without labels, it is done only on data that is labelled "normal", so some information of the labeling is provided to the models. To avoid confusion, at least the abstract should clearly state that the proposed method is semi-supervised in nature. The introduction then can elaborate that this means that the model is trained on only "normal" data, in contrast to semi-supervised classification, where access to all labels is more common. Similarly, at line 328 it is, in my opinion, incorrectly stated that this paper concerns the unsupervised setting.
- The network architecture study, detailed in Appendix A, leads me to believe that the network and method have been thoroughly optimized on the benchmark. While this is not necessarily bad, it leads to a heavily unfair comparison. All other methods in the comparison have not been optimized to a similar degree, and will in many cases perform subpar. It is therefore not strange that the proposed method is the best performing one, as it simply has the highest degree of optimization. This is especially concerning as the optimization is done on a subset of the benchmark, which can still lead to overfitting on the entire benchmark.
- Similar to the previous point: the authors show that allowing their method access to a validation set improves performance. Yet, no other methods are allowed the same benefit. This can lead to great discrepancies. GAN, and AE-based methods for example greatly improve with early stopping. Even beyond early stopping, the argument could be made that hyperparameter tuning should be done for many of these methods if a validation set is available. 
- In the experimental setup it is described how the various train/val/test sets are constructed. However, some datasets contain paired data which can't be split in the described manner without introducing cross-contamination. An example is the MI-F/MI-V data from the ex-AE study. The MI-F/MI-V datasets are derived from a collection of 18 experiments, and splitting these experiments across train/validation/test sets can lead to data leakage and an overestimation of performance. Standard cross-validation procedures are not appropriate for this type of data.
- Generally, Fbeta scores are hard to compare across datasets, as they are not readily interpretable like AUC scores. Specifically: some problems are inherently harder than others, leading to the great variability observed in Figure 2. The authors could and should consider using the average precision (now shown in appendix) or the adjusted measures proposed by Campos (G. O. Campos, A. Zimek, J. Sander, R. J. Campello, B. Micenkov´a, E. Schubert, I. Assent, and M. E. Houle. On the evaluation of unsupervised outlier detection: measures, datasets, and an empirical study. Data Mining and Knowledge Discovery, 30(4):891–927, 2016)
- Some of the methods used in the comparison are not properly implemented for tabular data, or are insufficiently optimized. I've not thoroughly studied all code provided by the authors, but some examples include the VAE, which uses a sigmoid activation at the last layer, which is not suitable for standardized real-valued tabular data, and DeepSVDD, of which the PyOD implementation does not use many of the needed optimizations/steps the original paper by Ruff et al. introduces. The VAE implementation should use a linear activation function on the last layer to match the distribution of the input data. The use of a sigmoid activation function is only appropriate when the data is scaled between 0 and 1. The current implementation is not statistically sound.
- Section 5 concerns interpretability. In contrast to the rest of the paper this only shows how the score map can be used for the intepretation of anomalies in the computer vision domain, but not on tabular data, which is the main focus of the paper. This seems disconnected, and I would urge the authors to either show how to interpret tabular anomaly detection using their method, or include this experiment only in a separate paper showcasing the method on computer vision anomaly detection.

Minor comments/typographical issues:
- line 254: benifit -> benefit
- Throughout the paper: spacing is too large near references: for example Appendix  C -> Appendix C and Algorithms  1 and   2 -> Algorithms 1 and 2.
- The y-axis labels in Figure 2 are too small to read.
- The x-axis and y-axis labels in figure 3 are not needed when displaying images

### Questions
- Many of the classically unsupervised methods used in this comparison can't readily be used in the typical fit/predict paradigm that corresponds to distinct training, validation, and test sets. This confuses me as to how they are included exactly in the comparison, are the methods applied as is typical in the unsupervised setting: they get access to both train+test data and make a single prediction on the entire collection? If methods from for example PyOD are applied in the fit/predict paradigm on external test data they will yield incorrect results.
- At lines 59 and 60 it is stated that the network **learns** to differentiate between normal and abnormal data during testing. From the rest of the paper it seems that no network updates are done during testing. This sentence may therefore be misleading, could the authors clarify?
- in the **main results** subsection the authors first state that they subsample datasets to 50.000 data points. Is this done for the test set, the training set, or is this the total dataset which is then further split according to the procedure described earlier? Are all anomalies still included in this subsample? If so: that make anomalies much less rare than they would originally be. If not: anomalies are generally assumed to be heterogenous, so subsampling might introduce a severe bias.
- In the **main results** subsection it is stated that five different random seeds are used. Is this the random seed for the methods, or for the dataset subsampling, or both?
- In the **Main results** subsection it is stated that the notable performance of LUNAR, KPCA, and GMM methods goes overlooked in similar comparison. Yet, the results of Bouman et al. (2024) have observed similar performance of LUNAR and GMM on the collection of Local anomaly datasets. As a different collection of datasets is used in this paper in contrast to their comparison, does this not perhaps indicate that a larger proportion of the datasets used in this research is likely to contain "local" anomalies rather than the generally studied "global" anomalies?

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes an improved unsupervised tabular anomaly detection method based on a diffusion model.

### Strengths
The experiments designed in this paper are extensive.

The method proposed in this paper is given adequate theoretical derivation and proof.

### Weaknesses
- The title’s phrase "Estimating Gradients" does not seem to be sufficiently reflected throughout the paper; it would be helpful to provide a reasonable explanation. The connection between the core methodology and the gradient estimation process, as implied by the title, is not explicitly clear. The paper should elaborate on how the diffusion model's reverse process directly leverages gradient information for anomaly detection, rather than just using it as a generative process. Specifically, the role of the score function (gradient of the log data density) in identifying anomalies needs further clarification.

- Although the paper includes numerous baselines (a commendable aspect), a small suggestion would be to mark the proposed method in all comparative result charts, using an identifier like "(ours)". This would greatly improve readability and allow for a quicker visual assessment of the proposed method's performance relative to the baselines.

- The paper claims that the introduced method requires no additional prior knowledge; however, it still seems to be a reconstruction-based framework, which typically involves basic prior assumptions. While the method may not require explicit thresholds or pre-defined distributions, the inherent assumption that normal data can be reconstructed accurately by the diffusion model is itself a form of prior knowledge. This assumption needs to be acknowledged and discussed, especially in the context of its limitations when dealing with complex or multimodal normal data distributions.

### Questions
What is the detailed structure of the MLP2048? Could it be clearly described through diagrams or text? For instance, the structure used in the experiments, including the number of layers and the parameters of each layer. If different datasets use different configurations, including this information in the appendix would help readers replicate this work.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces noise conditional score networks (NCSN) to tabular anomaly detection and propose a new method called NCSBADVAL. However, it just made minor adjustments on NCSN and combines some popular techniques, such as time-step embedding to adapt the standard NCSN to this area. The authors have made extensive experiments to verify that if we aggregate the performances across all the 57 datasets, the average F1 and AUC-ROC of NCSBADVAL are better than the baselines. Also, the authors provided a good example to exhibit the interpretability of it.

### Strengths
1. Extensive experiments and good visualization. The authors have made extensive experiments to prove that the proposed method can achieve an overall better performance across 57 datasets compared with tens of baselines. Besides, the authors have made a good visualization of such a mass experiment results and verify the effectiveness of NCSBADVAL.
2. Good interpretability.  The authors also provide a good example in figure 3 to exhibit the strong interpretability of NCSBADVAL.

### Weaknesses
Though I really admire the huge experiment workload of this paper, I have some concerns about it.

1. Limited novelty. Actually there are many works have introduced diffusion model into anomaly detection area, for example [1] [2] [3]. Though it may firstly introduce NCSN (a branch of diffusion model), it is not an original idea to introduce this kind of model into anomaly detection. Besides, this work only make little adjustment on NCSN when adapting it to anomaly detection area by combining some popular techniques such as time step embedding and finding a correspondence relationship between the anomaly score and score in diffusion model.
2. Consistently good performance but not best performance. Though NCSBADVAL can make overall better average performance when aggregating the performances across all the datasets, I found in Table 6- Table 13 that NCSBADVAL actually can not achieve the best performance on majority of the datasets (I have not counted it accurately due to the huge amount). Thus, could I understand it as that NCSBADVAL can only obtain a relatively good results on most datasets, but the best performance is achieved by different methods on different datasets?

### Questions
1. How many times that NCSBADVAL have achieved the best performance among 57 datasets?
2. Could you emphasize the adaptions you have made compared to the standard NCSN?

### Soundness
3

### Presentation
2

### Contribution
2
