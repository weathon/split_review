# ChronoGAM: An End-to-End One-Class Time Series Gaussian Mixture Model

- Decision: Reject
- Scores: 3, 5, 1, 6

## Abstract
Recently, several algorithms have been proposed for One Class Learning (OCL) with time series. However, several problems can be found in these methods, problems involving the collapse of hyperspheres, manual thresholds, numerical instabilities and even the use of unlabeled instances during training, which directly violates the concept of OCL. To avoid these problems and solve cases like the numerical instability of some methods this paper proposes an end-to-end method for time series one-class learning based on a Gaussian Mixture Model (GMM). The proposed method combines the unsupervised learning technique of an autoencoder adapted to extract temporal and structural features of a time series, combined with distribution learning, to provide better performance than other state-of-the-art methods for the classification of time series data. ChronoGAM is a novel method that is capable of improving the temporal importance of the representations learned by the autoencoding system. We propose a new objective function with modifications to penalize the small values on the covariance matrix without resulting in exploding gradient propagation, causing numerical instabilities, and adapting the energy calculus to avoid the use of exponential functions. The method is tested on over $85$ benchmark datasets, generating $652$ datasets. We gain in $369$ datasets, with an average ranking of $2.68$, being the top-ranked method.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper is focused on the problem of one-class learning with time series data. Existing methods face problems like hypersphere collapse and numerical instability, etc. The proposed method uses a Gaussian Mixture Model, combines an autoencoder for feature extraction, and improves temporal importance. It's tested on many datasets and shows outperformance in 369 of them.

### Strengths
This is an applied paper and has little technical contribution. 

The experiment is relatively comprehensive on 85 benchmark datasets and derived 652 datasets.

### Weaknesses
1. The author claims the gain of the proposed method in 369 datasets out of a total of 652. The issue with this massive test is the lack of insights into the reasons for the proposed method's effectiveness and ineffectiveness on these many datasets. The sheer number of datasets, while impressive, obscures the underlying mechanisms at play. It is unclear why the method succeeds in some cases and fails in others, hindering a deeper understanding of its applicability and limitations. A more focused analysis on a subset of datasets, perhaps categorized by specific characteristics, would be more informative.

2. The proposed method appears to have no significant technical novelty; thus, it is a question of where the outperformance stems from. The authors are expected to provide a conceptual or theoretical explanation of why the proposed method can outperform in addition to experimental results. The use of a Gaussian Mixture Model (GMM) with an autoencoder is not novel in itself, and the modifications to the loss function, while potentially impactful, require a more rigorous justification. The paper lacks a theoretical analysis of how the proposed loss function addresses the issues of hypersphere collapse and numerical instability, which are claimed to be the main problems with existing methods. Without this, the outperformance remains an empirical observation rather than a theoretically grounded result.

### Questions
See the weakness section above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an end-to-end one-class time series Gaussian mixture model to resolve the collapse of hyperspheres, manual thresholds, numerical instabilities, and even the use of unlabeled instances during training. 

The proposed ChronoGAM aims at improving the temporal importance of the representations learned by the autoencoding system. 

The techniques are to penalize the small values on the covariance matrix without resulting in exploding gradient propagation, causing numerical instabilities, and adapting the energy calculus to avoid the use of exponential functions. 

Experimental results show the effectiveness.

### Strengths
- Simple and efficient reminiscences of numerical challenges in One-Class-Learning.
- Extensive experimental results show the effectiveness of the proposed method.

### Weaknesses
 - Limited concrete evidence for how the numerical challenges in One-Class-Learning are released
- By using an autoencoder, the numerical problems are resolved but with limited theoretical justification - and no ablation study is presented.

### Questions
it is overall interesting to see that with an end-to-end design, the performance is enhanced. However, it can be improved via the ablation perspective of the experiments in such an unsupervised setting. 

The impact of adopting an autoencoder is welcomed but it requires concrete examples and evidence regarding: 
- what temporal and structural features are well captured.
- how it helped in resolving the numerical challenges and why an autoencoder is the solution in that situation.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper addresses one-class detection for time series. To this end, the authors use an auto-encoder similar to the one introduced by Zong et al. (2018), while including some variations to tackle the temporal features as proposed by Fawaz et al. (2019).

### Strengths
This paper tackles an interesting problem, which is one-class detection on time series with deep learning.

### Weaknesses
A major issue of this paper is the incremental contribution. The authors use roughly the same the auto-encoder proposed by Zong et al. (2018), which was introduced and investigated to address unsupervised anomaly detection using a Gaussian mixture model. The only difference seems to be the convolution layers as proposed by Fawaz et al. (2019), and the snake activation of Ziyin et al. (2020).

Another major issue is that the paper does not demonstrate clearly the relevance of these modifications. The authors should conduct an ablation study in order to show how the implemented modifications impact the obtained results, including convolution layers of Fawaz et al. (2019) and the snake activation of Ziyin et al. (2020).

Another major issue is experiments and comparative analysis. The authors compare the proposed method to 4 other detection methods: OCSVM, IsolationForest, DeepSVDD and DAGMM. All these methods are not relevant to address time series. Therefore, this is not enough as the authors did not provide any comparative analysis with related methods, namely methods from the deep leaning literature that address anomaly detection in time series. For a review, see
* Choi, Kukjin, Jihun Yi, Changhwa Park, and Sungroh Yoon. "Deep learning for anomaly detection in time-series data: review, analysis, and guidelines." IEEE Access 9 (2021): 120043-120065.
See also related methods
* Kim, Siwon, Kukjin Choi, Hyun-Soo Choi, Byunghan Lee, and Sungroh Yoon. "Towards a rigorous evaluation of time-series anomaly detection." In Proceedings of the AAAI Conference on Artificial Intelligence, vol. 36, no. 7, pp. 7194-7201. 2022.
* Xu, Jiehui, Haixu Wu, Jianmin Wang, and Mingsheng Long. "Anomaly transformer: Time series anomaly detection with association discrepancy." arXiv preprint arXiv:2110.02642 (2021).
* Zhang, Chuxu, Dongjin Song, Yuncong Chen, Xinyang Feng, Cristian Lumezanu, Wei Cheng, Jingchao Ni, Bo Zong, Haifeng Chen, and Nitesh V. Chawla. "A deep neural network for unsupervised anomaly detection and diagnosis in multivariate time series data." In Proceedings of the AAAI conference on artificial intelligence, vol. 33, no. 01, pp. 1409-1416. 2019.
* Garg, Astha, Wenyu Zhang, Jules Samaran, Ramasamy Savitha, and Chuan-Sheng Foo. "An evaluation of anomaly detection and diagnosis in multivariate time series." IEEE Transactions on Neural Networks and Learning Systems 33, no. 6 (2021): 2508-2517.
* Li, Dan, Dacheng Chen, Baihong Jin, Lei Shi, Jonathan Goh, and See-Kiong Ng. "MAD-GAN: Multivariate anomaly detection for time series data with generative adversarial networks." In International conference on artificial neural networks, pp. 703-716. Cham: Springer International Publishing, 2019.
* Zhang, Yuxin, Yiqiang Chen, Jindong Wang, and Zhiwen Pan. "Unsupervised deep anomaly detection for multi-sensor time-series signals." IEEE Transactions on Knowledge and Data Engineering (2021).
* Tuli, Shreshth, Giuliano Casale, and Nicholas R. Jennings. "Tranad: Deep transformer networks for anomaly detection in multivariate time series data." arXiv preprint arXiv:2201.07284 (2022).
* Carmona, Chris U., François-Xavier Aubet, Valentin Flunkert, and Jan Gasthaus. "Neural contextual anomaly detection for time series." arXiv preprint arXiv:2107.07702 (2021).

Finally, there are some spelling and grammatical errors, such as “autoncoder”, “cossine similarity function”, “recomendation”.

### Questions
Why didn't you compare to other deep anomaly methods for time series ?

Why there is no ablation study that allows to demonstrate the relevance of the proposed modifications ?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method specifically targeted at time series data in the one-class learning problem. The proposed method consists of an autoencoder type with a convolutional layer that can capture the basic features of time series and a Gaussian mixture model that can capture multiple cluster structures in the latent space.
The authors have embedded some innovations in the proposed method to solve some problems that related methods have had in practical use. Specifically,
- The proposed method is a data-driven method using data energy instead of manual thresholding, which is often required in one-class learning.
- Instead of the ${\rm exp}$ function, which causes instability in the calculation of data energy, the proposed method improves the stability of the calculation by proposing an ${\rm explu}$ function.

Furthermore, the paper demonstrates the practical usefulness of the proposed method with objective measures for a remarkably large number of experimental data.

### Strengths
This paper proposes a very solid way to solve in a reasonable way several problems that have been practically and empirically intractable in the latest developments in one-class learning research. In particular, the following points can be listed as notable strengths: 
- The paper is very well written, the arguments are coherent, and the organization is well thought out for a diverse audience. The authors' perspectives on the latest developments and current issues are well organized, especially in the context of one-class learning.
- The objective evaluation experiments that demonstrate the usefulness and effectiveness of the proposed method are notably large, comprehensive, and fair. It is suggested that the models assumed by the proposed method (time series representation by convolutional auto encoder and cluster structure in latent space by Gaussian mixture model) fit well on many real data.

### Weaknesses
My concern is that the discussion of the validity of the improvements from the Deep Autoencoding Gaussian Mixture Model (DAGMM) [Zong+2018], which is the inspiration for this study, may be somewhat lacking. The model used in this paper can be viewed as a legitimate successor to DAGMM from an overarching and conceptual perspective. Therefore, I was reading the manuscript with the expectation that the manuscript would carefully explain the validity of each improvement from it. Certainly, I agree that empirically and experimentally those improvements work well, as the authors have shown us in their evaluation experiments, but I am left with some points that are not clear to me why they work well from the perspective of scientific and technological development. My concerns can be summarized as follows.
- This paper introduces a convolutional approach to time series modeling with reference (maybe, as a standard method described in [Wang+2017]) to existing research on time series classification problems. It seems to me that the strengths of this approach (i.e., for what time series can well-fitted features be captured) and the weaknesses (what time series are difficult to represent) have not been adequately discussed. Specifically, the use of convolutional layers, while effective for capturing local patterns, might not be optimal for time series with long-range dependencies or complex temporal structures. The paper does not delve into the limitations of this approach, such as its potential inability to model non-local interactions or handle time series with varying temporal scales effectively. A more thorough discussion of these limitations would be beneficial.
- I am having difficulty understanding the validity of the explu function, one of the devices of the proposed method. explu function can be seen as an approximation/substitution for computational stability of what is originally an exp function, but I have not been able to find an explanation of what the sacrifice is. While the paper claims that the explu function improves stability, the trade-offs of using this function instead of the exponential function are not clearly articulated. For instance, the explu function introduces a linear region for positive values, which might limit the model's ability to penalize outliers with very high energy values as effectively as the exponential function. A more detailed analysis of the implications of this approximation, including potential drawbacks and limitations, is needed.

### Questions
I would like to ask the following questions to see if my understanding of the two concerns I raised in the weaknesses section above is incorrect.

(1) Regarding the convolution approach that this paper employs to represent time series.
- Is the adoption of the convolution approach the recommended setting by the authors? Or is it adopted because it is known as the most basic and standard in the field concerned? For example, if the user has prior knowledge of the time series of interest, is it easy to change the proposed method to a time series model specific to that interest (in this context, the design of the AE layer)?
- Is this a robust setting for local (near temporal) features of the time series of interest, as the standard convolution assumes? Or is it also possible to capture very distant temporal dependencies (in the extreme case, where the first frame determines the last frame) or periodic structures?

(2) Regarding ${\rm explu}$ function.
I believe that instability in the computation of covariance (the inverse of covariance) is a challenge often faced in statistical machine learning. For example, this problem often arises in Gaussian process regression (GPR) when the observed data are of high dimension. In GPR, this problem is usually addressed indirectly (the direct motivation is to reduce the computational complexity of the inverse of the covariance matrix) using, for example, variational methods or induced points [Titsias+2009]. While these methods require rather complicated handling, I feel that the explu function in this paper is a very simple and impressive potential new way to deal with this problem. So let me ask a question.
- What are the disadvantages that arise when replacing the exp function with the explu function?
- Can that disadvantage be ignored in practical application situations?

M. Titsias. Variational learning of inducing variables in sparse Gaussian processes. In Proceedings of the Twelth International Conference on Artificial Intelligence and Statistics, pages 567–574, 2009.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
