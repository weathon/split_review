# Powering Neural Architecture Search with Robust Masked Autoencoders

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 3, 5

## Abstract
Neural Architecture Search (NAS) relies heavily on labeled data, which is labor-intensive and time-consuming to obtain. In this paper, we propose a novel NAS method based on an unsupervised paradigm, specifically Masked Autoencoders (MAE), thereby eliminating the need for labeled data during the searching process. By replacing the supervised learning objective with an image reconstruction task, our approach enables the robust discovery of network architectures without compromising performance and generalization ability. Additionally, we address the problem of performance collapse encountered in the widely-used Differentiable Architecture Search (DARTS) in the unsupervised setting by designing a hierarchical decoder. Through extensive experiments conducted across various search spaces and datasets, we demonstrate the effectiveness and robustness of our method, offering empirical evidence of its superiority over baseline approaches.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a new DARTS based architecture search method with MAE as the objective. This enables effective NAS without supervised vision data. The results improve over existing supervised NAS methods and Unsupervised previous works.

### Strengths
1. The proposed method looks straight forward given the possibility of UnNAS and the effectiveness of MAE.
2. Experiments were carried out comprehensively in traditional NAS settings for convolutional neural networks.
3. Interesting phenomenon has been observed, such as the correlation between task difficulty and performance collapse, thus leading to the proposal of hierarchical decoder, etc.

### Weaknesses
1. Given the successful search for various pretext tasks in UnNAS, as well as the successful application of MAE as a self-supervised learning method, it is expected that MAE-NAS is possible and will generate reasonably good results. It is true that this paper shows a successful implementation of the idea, but the novelty or contribution to the field may not be sufficient for ICLR. The core idea of applying MAE as a proxy task for NAS, while intuitive, lacks significant novelty given the existing body of work in unsupervised NAS and the established effectiveness of MAE. The paper does not sufficiently demonstrate a substantial leap in methodology or conceptual understanding beyond the straightforward application of these existing techniques.
2. As shown in UnNAS paper, the performance difference in the architectures searched with different objectives are quite small. This conclusion also transfers to this paper where the performance gain on top of existing methods has been quite limited as shown in Table 1, 2, 3. The reported gains over existing methods, while present, are not substantial enough to justify the introduction of a new NAS method. The improvements are incremental and do not represent a significant advancement in the field. The performance differences are within a range that could be attributed to minor variations in training or hyperparameter tuning, rather than a fundamental advantage of the proposed method.
3. MAE was proposed for transformers and enabled efficient pre-training of transformers without labels. However, MAE-NAS works for convolutional search space only and has not shown promise in searching in more interesting spaces such as transformers. Similarly, the adoption of the convolutional space defeats the purpose of MAE paradigm of pre-training efficiency — the resulting convolutional architecture has to be trained without MAE. The limitation to convolutional search spaces is a significant drawback, as it fails to leverage the primary strength of MAE, which is its applicability to transformer architectures. The method does not address the potential of using MAE for searching architectures in more complex and relevant spaces, thus limiting its impact. The fact that the resulting convolutional architecture cannot be pre-trained with MAE further undermines the motivation of using MAE as a proxy task.
4. minor: Presentation. Section 3 includes 1 subsection 3.1 only.

### Questions
1. Is it possible to design a new search space on top of MAE training so that masked patches can still be dropped during pre-training?
2. Does the method apply to other domains such as 3D networks or medical imaging where the best architectures have been less exploited and where data may be more limited than 2D images? This may help demonstrate the strength of the paper.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the challenge of Neural Architecture Search (NAS) dependency on supervised signals, which can be costly due to the need for labeled data. To overcome this, the authors propose a novel NAS approach that integrates DARTS with a masked autoencoder (MAE) paradigm, adapting it for unsupervised learning. A key challenge is the collapse of DARTS in unsupervised settings, which is mitigated by increasing the mask ratio and introducing a hierarchical decoder for enhanced performance. The method achieves comparable results to both supervised and unsupervised NAS counterparts, validated through experiments on seven datasets.

### Strengths
Originality and Quality: This paper explores a novel integration of MAE with DARTs, proposing that reconstruction targets can also serve as effective guidance for neural architecture search. The paper is of acceptable quality, with experiments conducted across several common benchmarks and supported by multi-run results, providing a reasonable foundation for the claims made.

Clarity: The paper is presented with straightforward figures and tables and the writing is easy to follow.

Significance: While the paper offers a fresh perspective, its significance is a primary concern, as discussed in the weaknesses section

### Weaknesses
Firstly, while I acknowledge that directly combining MAE and DARTS is not entirely novel, this paper falls short of fully realizing the impact of such a combination. In terms of results, as noted by the authors in Line 323, performance on large-scale datasets like IN-1K and standard benchmarks like CIFAR appears saturated. Without a clear performance or efficiency advantage, the approach lacks significance. Specifically, MAE’s strengths lie in efficiency (training speed) and scalability (e.g., training ViT-Huge on IN-1K alone), which other unsupervised methods lack. If applied effectively to NAS, I would expect MAE to offer fresh insights, such as addressing overfitting in NAS or demonstrating scalability. Unfortunately, the current work does not meet these expectations.


Secondly, several claims in the paper are ambiguous and require further clarification. For instance, the authors emphasize that directly applying MAEs with DARTS leads to training collapse, which can be mitigated by adjusting the mask ratio. However, Table 7 does not substantiate this claim, nor can I find any supporting experiments elsewhere in the paper to confirm training collapse. Additionally, while the authors propose HD to address this issue, the ablation studies indicate that HD has minimal impact on performance.


Minor: The format of the citation should be revised.

### Questions
1.  Why MAE+DARTS? The motivation is fundamental for this paper to improve its overall quality, given the technical novtiy is not significant and improvements are marginal. I expect to see more insight into the motivation.

2.  What is the design logic behind the proposed HD? I cannot see a clear improvement using this block.

3. What is the baseline in the paper? I cannot find a comparable method that can justify the proposed method's novelty and significance.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a novel NAS method called MAE-NAS leveraging masked autoencoders to achieve unsupervised searching. Specifically, the proposed MAE-NAS method is designed based on the optimization objectives of DARTS, along with the encoder designed based on the supernet of DARTS and the hierarchical decoder. Moreover, the proposed MAE-NAS method also has the ability to escape from performance collapse via changing the mask ratio. The proposed MAE-NAS method is evaluated on various search spaces and datasets, and the experimental results demonstrate the effectiveness of the proposed method.

### Strengths
1) The idea of proposed MAE-NAS method is simple and easy to understand. 
2) The framework and core components of the proposed MAE-NAS method is clearly presented in the paper. 
3) The performance collapse is an important problem in differentiable NAS methods, and this problem is not well explored in an unsupervised manner.

### Weaknesses
1) The motivation for adopting masked autoencoders to achieve unsupervised NAS is relatively unclear. In particular, the authors stated that the motivation for using masked autoencoders is that no studies have explored this direction. However, the necessity and the advantage for using masked autoencoders are still unclear. Besides, the proposed method seems a direct combination of the masked autoencoder and DARTS. I suggest the authors provide more discussions for adopting the masked autoencoders for unsupervised NAS.
2) The proposed MAE-NAS method is combined with DARTS, PDARTS, and PCDARTS to show its effectiveness in the plug-and-play manner. However, these differentiable NAS methods are relatively old. Why not integrate the proposed method into the recent differentiable NAS method to achieve the state-of-the-art performance?
3) Lack of in-depth analysis in terms of the performance collapse. Specifically, the authors states that the collapse phenomenon still exists in the unsupervised manner. However, they failed to explain why this phenomenon appears. Please provide more analysis and evidences in terms of the reason why this phenomenon can appear in the unsupervised manner.
4) Some claims are not well supported in terms of the performance collapse. For example, it is not well supported that the encoder can learns a more powerful architecture when the mask ratio becomes larger. Besides, why the unsupervised proxy can be viewed as the regularization? More empirical or theoretical evidences are needed for the points mentioned above.
5) The experimental results need further explanations. For example, the experimental results in Table 7 seem strange. When the mask ratio is set to 0.1 and 0.3, the Top-1 Errors are 2.79 and 2.77. However, when the mask ratio is set to 0.7, the Top-1 Error changes to 2.80. This phenomenon is conflict to the claim “when the mask ratio is less than 0.5, the probability of collapse is significantly high” in Section 3.1.1. Besides, it seems that when the mask ratio is small, the derived architecture does not suffer from serious performance degradation as shown in Table 8.
6) The writing needs improvements. For example, the format of the references in the main article seems incorrect. It is suggest to use “\citep{}” instead of “\cite{}”. Besides, the words “(i.e. DARTS)” should be “(i.e., DARTS)” in line 197.

### Questions
Please see weaknesses. Because there are a lot of ambiguous claims and weird experimental results in this version, and the motivation and novelty are not properly presented, I tend to recommend rejection temporarily.

### Soundness
2

### Presentation
2

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
This paper presents a new neural architecture search method based on unsupervised mask autoencoder. The author specifically designed their method to address performance collapse issues with adjustments of the mask ratio and a curated hierarchical decoder. They further validated their proposed approaches on cifar10, imagenet and nas bench 201 etc..

### Strengths
This presents a clear and straightforward way of leveraging unsupervised mae for neural architecture search, and it's interesting to understand how they synergize in the NAS framework.

### Weaknesses
1. While the idea of leveraging MAE for neural architecture search is straightforward, there is a lack of discussion and understanding of how they synergize together (more can be added in Sec 3). For example, it's vague whether there are any characteristics making MAE suitable for this task and a better choice over other unsupervised NAS methods. It's hard to tell the advantage from unsupervised NAS comparisons in Sec 4.

2. Regarding the hierarchical decoder, the authors have compared against the use of a regular decoder in Sec 4.8, still some doubts why this particular decoder design works the best. Also, as part of the novelty is from this hierarchical decoder (while combining mae and nas is more straightforward), I'd expect improvements from this to be more evident. However, the effectiveness of the proposed decoder is limited with high mask ratio, which is eventually what the authors adopt to use.

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
