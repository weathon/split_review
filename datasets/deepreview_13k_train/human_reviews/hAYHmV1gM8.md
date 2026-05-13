# FedWon: Triumphing Multi-domain Federated Learning Without Normalization

- Decision: Accept
- Scores: 8, 5, 6, 5

## Abstract
Federated learning (FL) enhances data privacy with collaborative in-situ training on decentralized clients. Nevertheless, FL encounters challenges due to non-independent and identically distributed (non-i.i.d) data, leading to potential performance degradation and hindered convergence. While prior studies predominantly addressed the issue of skewed label distribution, our research addresses a crucial yet frequently overlooked problem known as multi-domain FL. In this scenario, clients' data originate from diverse domains with distinct feature distributions, instead of label distributions. To address the multi-domain problem in FL, we propose a novel method called \textbf{Fed}erated learning \textbf{W}ith\textbf{o}ut \textbf{n}ormalizations (FedWon). 
   FedWon draws inspiration from the observation that batch normalization (BN) faces challenges in effectively modeling the statistics of multiple domains, while existing normalization techniques possess their own limitations. In order to address these issues, FedWon eliminates the normalization layers in FL and reparameterizes convolution layers with scaled weight standardization. 
   Through extensive experimentation on five datasets and five models, our comprehensive experimental results demonstrate that FedWon surpasses both FedAvg and the current state-of-the-art method (FedBN) across all experimental setups, achieving notable accuracy improvements of more than 10\% in certain domains. Furthermore, FedWon is versatile for both cross-silo and cross-device FL, exhibiting robust domain generalization capability, showcasing strong performance even with a batch size as small as 1, thereby catering to resource-constrained devices. Additionally, FedWon can also effectively tackle the challenge of skewed label distribution.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a scaled weight standardization method (FedWon) for federated learning. The proposed method eliminates the normalization layers in FL and reparameterizes convolution layers with scaled weight standardization to counter the drawbacks of common normalization layers in the FL model. Extensive experiments on real-world datasets validate the effectiveness of FedWon and demonstrate its robust generalization capability for both cross-silo and cross-device FL.

### Strengths
This paper studied the multi-domain FL problem and proposed a novel FL method FedWon which employs the Scaled Weight Standardization technique as an alternative to the batch-normalization module. 

1. The FedWon can achieve competitive performance to the SOTA methods without additional computation cost during inference.

2. Experiments on multi-domain datasets show the FedWon overperforms the conventional FL methods even if the batch size of the training process is small (1 or 2), and the visualization of feature maps demonstrates that the FedWon can effectively mitigate domain shifts across different domains.

3. The paper is well-written and organized. Extensive experiments demonstrate the effectiveness of the proposed method.

### Weaknesses
1. The paper brought the Scaled Weight Standardization (SWS) technique to handle the multi-domain FL problem. However, there is less analysis about the SWS’s impacts to the FL process, e.g., will it lead to a better convergence bound? Specifically, while the empirical results are promising, the paper lacks a theoretical understanding of why SWS is effective in the FL setting. It would be beneficial to analyze how SWS affects the optimization landscape and the convergence properties of the federated learning algorithm, especially compared to traditional normalization methods.

2. Many methods are compared in the paper, some of them have BN, some of them are suitable for cross-silo FL only, and some of them are suitable for cross-device FL, it would be clearer to have a structured summarization to help understand the scenarios where these methods are suitable for. A table summarizing the methods, their applicability to cross-silo vs. cross-device settings, and their reliance on batch normalization would greatly improve clarity. This would allow readers to quickly understand the context of each comparison and the specific advantages of FedWon in different scenarios.

3. Only one dataset is evaluated for the skewed label distribution problem. This limits the generalizability of the findings regarding the method's robustness to skewed label distributions. Evaluating on multiple datasets with varying degrees of skew would provide a more comprehensive understanding of the method's performance in such challenging scenarios.

### Questions
1. Please refer to weakness.

2. Sec.4 claims that the FedWon will achieve competitive results even at a batch size of 1 while [https://arxiv.org/abs/1602.05629] shows the FedAvg will degenerate to the FedSGD and be less effective. It is an interesting topic, and do you mind to report more details about the learning curves (communication round v.s accuracy) at different batch sizes or on different datasets?

3. What is the impact of local epochs on the proposed method?

### Soundness
3 good

### Presentation
4 excellent

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
This paper considers the problem of multi-domain federated learning. This paper proposes to remove batch normalization and reparameterize the convolution layer weights for another kind of normalization. Finally, experiments show that this simple technique yield considerable improvement for the performance of multi-domain FL over many baselines, e.g., FedAVG and FedBN.

### Strengths
The proposed method is easy to implement, and can be potentially plug into many existing methods. The experiments are extensive and the paper is well-writing in general.

### Weaknesses
 * I have many questions that I wish could be solved. Some of them are from questionable arguments from the paper, some of them are from the abnormal experimental results, and some of them are from the my curiosity in why the proposed method would work. Please see the Questions section for details. 
* The novelty is quite limited, where the proposed method is to use an existing reparametrization trick (Brock et al. (2021a)) in the FL setting.


### Questions
* Why the proposed method is only applied to the convolution layer? From Eq. 1, it seems that it can be applied to any kinds of layers represented by a weight matrix $W$. 
* In Eq. 1, how is $\gamma$ chosen? In particular, how robust is the training result to the choice of $\gamma$?
* Since the proposed method does not depend of batch statistics, I'm curious why FedWon B=1 better than B=2 (e.g., Figure 4)?  
* Also, in figure 4, I'm curious to see how would FedAvg (B=1) perform.
* It is claimed in this paper that FedBN can't do cross-device FL. However, there is not enough evidence, as far I can tell, from the paper that supporting this argument. Can the authors elaborate more on why FedBN can't do cross-device FL?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to address the challenge of multi-domain federated learning (FL) where clients have data from diverse domains with distinct feature distributions. The proposed method, Federated Learning Without Normalizations (FedWon), eliminates normalization layers and reparameterizes convolution layers. Extensive experiments on various datasets and models demonstrate that FedWon outperforms existing methods.

### Strengths
- The paper is easy to read, and the comparison figure (Figure 2) effectively illustrate the differences with previous methods.
- The ablation experiments for cross-silo federated learning cover various factors affecting model performance, such as batch size and client sampling rate.

### Weaknesses
 - The proposed method lacks innovation; it essentially directly applies the weight standardization and gradient clipping from the NF-Net series [1, 2] to the federated learning setting. It does not offer targeted improvements to address the unique challenges of the federated learning setting. The core idea of removing normalization layers and applying weight standardization is directly borrowed from prior work, and the paper does not sufficiently explore the nuances of adapting these techniques to the federated learning context, such as the impact of heterogeneous data distributions on the convergence of the proposed method.
- The experiments for cross-device FL in the paper are not sufficient for the proposed method's effectiveness. The cross-device FL experiments only include a single dataset and 100 clients. This limited scope makes it difficult to generalize the findings to more realistic cross-device scenarios with diverse data distributions and a larger number of clients. The paper needs to demonstrate the robustness of the proposed method across more diverse and challenging cross-device FL settings.


### Questions
- In the upper image in Figure 1b, it seems that the green points representing the server are entirely invisible, while in the lower image, it appears that there is no information at all.
- The presentation of feature maps in Figure 5 doesn't seem very informative. What information can we extract from the feature maps, and how are they related to the model's performance? Additionally, it appears that there is not much difference between the feature maps of FedAvg and FedBN.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel method called Federated learning Without normalizations (FedWon) to address the problem of multi-domain federated learning (FL). FedWon eliminates normalization layers and reparameterizes convolution layers with scaled weight standardization to effectively model the statistics of multiple domains. Experimental results on five datasets demonstrate that FedWon outperforms the current state-of-the-art methods. FedWon is versatile for both cross-silo and cross-device FL, exhibits robust domain generalization capability, and performs well even with a small batch size of 1, making it suitable for resource-constrained devices.

### Strengths
Originality:
The FedWon method is a new approach to reparameterizes convolution layers with scaled weight standardization to effectively model the statistics of multiple domains. This is a creative combination of existing ideas that addresses the limitations of traditional batch normalization federated methods. 

Quality:
This work provides a thorough experimental results that demonstrate the effectiveness of FedWon compared to other customized approaches on batch normalization. The experiments are well-designed, and the results are statistically significant.

Clarity:
The paper is well-written and easy to understand. The authors provide clear explanations of the FedWon method and its implementation. The experimental results are presented in a clear and concise manner.

Significance:
The research direction is crucial as federated multi-domain learning is essential in real-world applications where data may originate from multiple sources with distinct characteristics.

### Weaknesses
1. Lack of Technical Novelty: The paper's technical innovation is limited to reparameterizing the convolution layers using the Scaled Weight Standardization technique. While this approach may have some benefits, it lacks novelty as the Scaled Weight Standardization technique has been proposed and utilized in previous studies. The application of this technique in the context of federated learning, while potentially useful, does not represent a significant conceptual leap. The core idea of removing normalization layers and replacing them with a standardized weight approach is not fundamentally new, and the paper does not sufficiently demonstrate a novel adaptation or insight beyond the existing use of scaled weight standardization.

2. Insufficient Theoretical Analysis: The paper lacks a theoretical analysis of the effectiveness of the proposed Scaled Weight convolution (WSConv) layer. The authors should provide a more rigorous theoretical foundation to explain why the WSConv layer is suitable for addressing the challenges in federated multi-domain learning. Specifically, the paper does not offer any theoretical justification for why removing normalization and using weight standardization would be more robust to domain shifts in federated settings. A theoretical analysis should address the convergence properties, generalization bounds, and the impact of weight standardization on the optimization landscape in the context of heterogeneous data distributions.

3. Limited Comparative Analysis: The paper does not sufficiently compare with other federated multi-domain methods, such as PartialFed and FMTDA. The experimental section needs to include a more comprehensive comparison with these methods to understand the relative strengths and weaknesses of FedWon. The absence of a direct comparison makes it difficult to assess the true contribution of the proposed method against existing state-of-the-art techniques in federated multi-domain learning.

4. Limited Applicability to Convolutional Neural Network (CNN) Models: The proposed method is limited to CNN-based deep learning models, which restricts its applicability to a specific class of models, such as recurrent neural networks (RNNs), graph neural networks (GNNs) or transformer. The paper does not discuss the challenges or potential adaptations required to extend the proposed method to other architectures. This limitation significantly reduces the practical applicability of the method in various real-world scenarios where non-CNN models are often preferred.

### Questions
This paper mainly discusses the challenges of normalization in federated multi-domain learning and proposes to eliminate normalization. However, other directions exist to solve the federated multi-domain problem, such as PartialFed and FMTDA, which do not follow the normalization idea. What are the advantages and characteristics of FedWon compared with these methods?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
