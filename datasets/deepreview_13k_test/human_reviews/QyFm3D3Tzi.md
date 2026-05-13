# Spatio-Temporal Few-Shot Learning via Diffusive Neural Network Generation

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Spatio-temporal modeling is foundational for smart city applications, yet it is often hindered by data scarcity in many cities and regions. To bridge this gap, we propose a novel generative pre-training framework, GPD, for spatio-temporal few-shot learning with urban knowledge transfer.
Unlike conventional approaches that heavily rely on common feature extraction or intricate few-shot learning designs, our solution takes a novel approach by performing generative pre-training on a collection of neural network parameters optimized with data from source cities. 
We recast spatio-temporal few-shot learning as pre-training a generative diffusion model, which generates tailored neural networks guided by prompts, allowing for adaptability to diverse data distributions and city-specific characteristics.
GPD employs a Transformer-based denoising diffusion model, which is model-agnostic to integrate with powerful spatio-temporal neural networks. 
By addressing challenges arising from data gaps and the complexity of generalizing knowledge across cities,
our framework consistently outperforms state-of-the-art baselines on multiple real-world datasets for tasks such as traffic speed prediction and crowd flow prediction.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The proposed GPDiff framework in this paper aims to tackle the challenging transfer learning problem in spatio-temporal graph (STG) predictions. At first, it basically trains a transformer-based diffusion model on collected data in source cities, to capture the mapping function from a set of region-specific features to a set of model parameters. Then GPDiff can directly generate corresponding model parameters for unseen regions in new cities, based on the spatio-temporal features of these regions. The first stage is described as the pretraining and the second stage is the prompt-based finetuning. Experiments on several datasets illustrate that GPDiff empirically performs well on different prediction tasks, compared with a series of state-of-the-art methods.

### Strengths
1.	Generally, the proposed method is sound and reasonable.
2.	The proposed framework seems flexible, as it can adapt to different model structures and support training on data collected from any number of source cities.
3.	The results show a large improvement. Ablation studies and case studies seem sufficient.
4.	I have checked the released code and found that it is well organized. The reproducibility should be good.

### Weaknesses
1. While the proposed method is sound, it is not clear what is the theoretical foundation behind GPDiff.
2. How do we guarantee that model parameters of regions among different cities are within the same parameter space?
3. Why choose diffusion for parameter generation? How much time does it consume in the denoising process?
4. The experimental setup is not clear, which confused me why only DiDi-Chengdu is used for speed experiments. Besides, the caption of table 1 is not correct if didi-cheng is for speed evaluation. 
5. It seems that the method uses a newly proposed network. It is unclear whether the performance gain comes from the Diffusion or the network. Could the framework generalized to other networks?

### Questions
please check the weakness

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper provides a generative pretraining framework for spatio-temporal graph (STG) transfer learning tasks in smart city applications. Unlike traditional transfer learning approaches in this field, authors leverage the power of pretraining and design a novel approach that first pretrains a diffusion-based hypernetwork and then, based on the spatio-temporal prompt, directly generates model parameters for each region in a target city. Experiments on 7 real-world datasets covering two typical STG prediction tasks, i.e., crowd flow prediction and traffic speed prediction, demonstrate the superiority of the proposed GPDiff framework over SOTAs, with an improvement of 9.8%.

### Strengths
S1.	This paper provides a promising solution for an important research problem. Specifically, it is a pioneering practice in handling urban data-scarce scenarios that explores the paradigm of pretraining and prompt-based finetuning.
S2.	The novelty of the proposed GPDiff framework is sound. Unlike existing works, it tackles the STG transfer learning problem from a new angle, i.e., pretraining a generative hypernetwork that captures the region-conditional distribution of optimized model parameters. This design overcomes the difficulties in applying pretraining in STG learning.
S3.	Building spatial prompts with easy-to-accessible data like POIs and region attributes is reasonable and practical. Building temporal prompts with a self-supervised representation learning technique is also technically sound.
S4.	By leveraging the generation power of transformer-based diffusion models, GPDiff achieves sota performance on two typical STG prediction tasks, covering 7 real-world datasets.

### Weaknesses
W1.	The presentation of experimental results can be improved. For example, in Figure 4, why only show the temporal variations? What about spatial information? Visualization of model parameters needs to be more apparent.
W2.	I find that the presented results on the traffic speed prediction task seem much less than those of the crowd flow prediction task.

### Questions
Please refer to the weaknesses part.

### Soundness
3 good

### Presentation
3 good

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
This paper addresses the problem of transfer learning on spatio-temporal graphs between cities. Inspired by recent advances in NLP, the paper proposes a new pre-training approach to generate different models for various regions based on a DDPM. The major insight here is to fit different data distributions across regions and cities. The proposed framework has been evaluated on two real-world spatio-temporal applications.

### Strengths
1. The paper addresses an interesting real-world problem.
2. The paper is easy to follow.
3. I appreciate the design of prompts in this paper, i.e., from both spatial and temporal domains.
4. The source code has been provided.

### Weaknesses
Although this paper has the above merits, I would like to point out the following concerns.

W1. Insufficient related work and baselines:

The examination of related works in the paper appears to be extremely insufficient, with a noticeable lack of comparison to existing studies. From my understanding, numerous studies [1,2,3,4, 5] have delved into the application of meta-learning or hypernetworks to tailor prediction models for each node or region, especially [1] and [2] with high impacts in the field of traffic forecasting. It seems that implementing these directly could address the issue of varying data distributions across regions or cities. Therefore, I find it necessary for this paper to provide a compelling justification for the utilization of the framework proposed in this manuscript. What's more, they should be considered as baselines for empirical comparison.

W2. Limited technical novelty:

Compared to existing meta-learning-based methods, this paper has no significant novelty and technical contributions. The primary difference lies in the utilization of a DDPM (along with some prompts) to generate model parameters for each region, without theoretical contributions from the model side. This approach doesn't seem to surpass the acceptance threshold set by ICLR. The originality and technical value of this study could benefit from further enhancement.

W3. Weak evaluation:

Firstly, while the paper asserts that the proposed framework is model-agnostic, this claim is substantiated solely with evaluations on two outdated baselines, published before 2019, while recent methodologies have been overlooked, e.g., [6, 7, 8], see more in [9]. Secondly, the affirmations made in Section 4.4 lack persuasiveness. Figure 4 doesn't offer any insightful revelations, except reporting their differences. For instance, is there any proximity amongst various regions based on their respective POI information? These elements need to be elaborated on for a comprehensive understanding. Thirdly, the paper lacks a discussion on the model's efficiency. Customizing models for each region always brings considerable computational overhead. By the way, the efficiency of the proposed method should be benchmarked against the existing approaches as mentioned in W1. 

W4. Some SOTA baselines are missing, such as CrossTReS, MetaST, etc.


Reference:

[1] Urban traffic prediction from spatio-temporal data using deep meta learning, KDD 2019.

[2] Adaptive graph convolutional recurrent network for traffic forecasting, NeurIPS 2020.

[3] Spatio-temporal meta learning for urban traffic prediction, TKDE 2020.

[4] Region Profile Enhanced Urban Spatio-Temporal Prediction via Adaptive Meta-Learning, CIKM 2023.

[5] Hyperst-net: Hypernetworks for spatio-temporal forecasting, arXiv.

[6] Pre-training enhanced spatial-temporal graph neural network for multivariate time series forecasting, KDD 2022.

[7] Graph Neural Controlled Differential Equations for Traffic Forecasting, AAAI 2022.

[8] Spatial-temporal identity: A simple yet effective baseline for multivariate time series forecasting, CIKM 2022

[9] Spatio-temporal graph neural networks for predictive learning in urban computing: A survey, arXiv.

### Questions
Please reply to W1 to W3.

Additional questions:
- Should region prompts also include information about the entire city? Merely focusing on regional features might not provide comprehensive information.
- Some alternative methods may consider transferring at different levels or scales, whereas this model appears to only consider regional features. Is there a way to adaptively incorporate large-scale features as well?
- The authors mentioned the issue of negative transfer between cities as the second limitation in the introduction. However, it is not clear how the proposed model explicitly addresses this problem. Can the authors provide more discussion and experimental evidence?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a generative pre-training framework based on diffusion models, GPDiff, to generatively pre-train a set of model parameters and generate tailored model parameters using data from the source city guided by prompts. The proposed solution addresses the challenges of inter-city transfer caused by data gaps across cities.

### Strengths
- The authors design a novel generative pretraining framework for STG transfer problems, especially the unique angle of generating fine-grained model parameters that can serve as a good initial point for model optimizations on small-scale datasets.
- Utilizing diffusion modeling for generative pretraining is technically sound. The designed model structure based on transformers is also appropriate and flexible for supporting the model-agnostic requirement.
- The conducted experiments are sufficient to demonstrate the superiority of the proposed GPDiff framework in terms of not only prediction performance but also compatibility with different STG prediction models.
- The paper presentation and writing are good.

### Weaknesses
- The time consumption of this framework needs to be provided.
- Some details require further clarification. For example, how exactly is the improvement value of 9.8% calculated? As in the last part of the Introduction part, i.e., “an improvement of 9.8%”. Similar cases are in the description text of Table 2.
- I think the rationality behind the excellent performance of GPDiff is easy to understand. But I still expect some further explanations by designing some more pertinent experiments. For example, which kind of regions in target cities would be much easier to benefit from knowledge transfer in this pretraining framework?

### Questions
- Case Study only wrote for different regions to generate a different distribution of parameters, indicating that the parameters can be generated for different data, but can explain the parameters are effective?

- ABLATION STUDY content is too coupled, it can be split into CONTRAST STUDY, or directly changed to Study of GPDiff.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
