# Find A Winning Sign: Sign Is All We Need to Win the Lottery

- Decision: Accept
- Scores: 6, 8, 5, 8

## Abstract
The lottery ticket hypothesis (LTH) posits the existence of a sparse network (a.k.a. winning ticket) that can generalize comparably to its dense counterpart after training from initialization. However, early works fail to generalize its observation and method to large-scale settings. While recent methods, such as weight rewinding or learning rate rewinding (LRR), may have found effective pruning methods, we note that they still struggle with identifying a winning ticket. In this paper, we take a step closer to finding a winning ticket by arguing that a signed mask, a binary mask with parameter sign information, can transfer the capability to achieve strong generalization after training (i.e., generalization potential) to a randomly initialized network. We first share our observation on the subnetwork trained by LRR: if the parameter signs are maintained, the LRR-driven subnetwork retains its generalization potential even when the parameter magnitudes are randomly initialized, excluding those of normalization layers. However, this fails when the magnitudes of normalization layer parameters are initialized together. To tackle the significant influence of normalization layer parameters, we propose AWS, a slight variation of LRR to find A Winning Sign. Specifically, we encourage low error barriers along the linear path connecting the subnetwork trained by AWS to its counterpart with initialized normalization layer parameters, maintaining the generalization potential even when all parameters are initialized. Interestingly, we observe that across various architectures and datasets, a signed mask of the AWS-driven subnetwork can allow a randomly initialized network to perform comparably to a dense network, taking a step closer to the goal of LTH.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper explores the lottery ticket hypothesis (LTH), which suggests that a sparse network, or "winning ticket," can generalize as well as a dense network when trained from initialization. Previous methods struggled to find such tickets, especially in large-scale settings. The authors propose using a "signed mask," a binary mask with parameter sign information, to transfer generalization potential to a randomly initialized network. They introduce AWS, a variation of learning rate rewinding (LRR) to find A Winning Sign, which addresses the influence of normalization layers and maintains low error barriers. This approach enables a randomly initialized network to perform comparably to a dense network across various architectures and datasets, advancing the search for a true winning ticket in LTH.

### Strengths
+ The proposed AWS method leverages a signed mask (a sparse mask with sign information) to transfer the generalization potential of a subnetwork to a randomly initialized network. This approach help addresses a critical challenge in LTH by maintaining the network's basin of attraction, even after initializing all parameters, thus taking a meaningful step towards identifying a true winning ticket.

+ AWS effectively eliminates the reliance on trained normalization layer parameters, which has been a major limitation in previous methods. By encouraging linear mode connectivity between the AWS subnetwork and its counterpart with initialized normalization parameters, the method ensures that the subnetwork remains within its basin of attraction, which avoids the need for parameter retaining.

+ The paper provides empirical evidence demonstrating that the signed mask can enable a randomly initialized network to generalize comparably to a dense network across various architectures and datasets. This shows the method's applicability and effectiveness in various settings.

### Weaknesses
 - The proposed method heavily relies on the effectiveness of signed mask in preserving the generalization potential of the subnetwork. It is not clear whther the proposed method can be generalized to more model architectures and tasks. If the signed mask does not perform well across different architectures, tasks or datasets, the method's applicability could be limited.

- The method requires careful handling of normalization layer parameters, which adds complexity. The need to interpolate normalization parameters during training may bring challenges when scaling up the proposed method. its scalability to large scale models/datasets is unclear as well.

### Questions
Please refer to details of above "Weaknesses" sections.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The Lottery Ticket Hypothesis (LTH) assumes that there exists a sparse subnetwork inside a dense one that can be trained from initialization to reach a comparable performance to the full model; the aim is to find such a subnetwork, called the winning ticket. 
This work focuses around LTH and introduces a novel approach based on a sparse mask with sign information, while considering  a variation of learning rate rewinding (LRR) that encourages linear mode connectivity to bypass issues tied to the initialization of normalization layers. The experimental results vouch for the efficacy of the proposed method; across various architectures and datasets, the proposed sign mask allows for a randomly initialized network to perform comparably to a dense network.

### Strengths
The paper is overall well-written and easy to follow. The authors clearly present the motivation of the paper while providing some insights into the proposed approach right from the start. 
The related work section is clear giving a good overview of the LTH field and its issues. The proposed LRR variant is simple, considering a random an simple interpolation of the normalization parameters.

The experimental evaluation includes a variety of datasets and architectures with the experimental details clearly stated and the experimental results vouch for the efficacy of the proposed approach.

### Weaknesses
I find that the main novelty of the proposed approach is the insights into the normalization issues and the introduced AWS variant. In this context, I do not consider the contribution to be of the highest novelty.



### Questions
Why did the authors choose only the MobileNetV2 and MLP-Mixer for the Imagenet setting? Were there any issues with the other architectures?

Can the authors provide a corresponding table (similar to Table 1) for the CIFAR-100 and Tiny-ImageNet experiments?

What are the sparsity levels for these experiments? Do these correspond to the remaining parameter ratio in Fig. 3?

What is the behavior of the proposed approach in different sparsity levels in the case of ImageNet? How does it compare to standard LRR?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper aims to find lottery ticket hypothesis for neural network models, especially from the perspective of parameter sign. It proposes to slightly change the LRR based on an interpolation method to make the sparse network with good trainability for generalization. Experiments are based on CIFAR and imagenet dataset across different model architectures.

### Strengths
1. Find the winning ticket is still an open question in the sparse network training area, such topic is a valuable one to explore.
2. Experimental results shown in the draft support the claimed statement from the paper.

### Weaknesses
1. Compared with originla LRR, the change is relatively trivial with not enough research novelty.
2. Used datasets and model architectures are not large-scale like mentioned goal in the abstract. Adding more larger datasets and models will be more supportive.
3. The training configurations for cifar and imagenet may not reach the fully convergence for model training, where 100 and 120 epochs are used for these two, respectively.
4. Overall, the paper is not very clear to read, such as the figures on the main results section. Which line represents the proposed method and which one is for baselines? how to indicate the proposed method outperforms others?
5. In addition, in table.1, more sparsity ratios for experiments will be helpful. And using more other and larger networks will further support the paper claim. More comprehensive empirical studies are needed to support the draft conclusion.

### Questions
Please check the weaknesses section above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper suggests that a signed mask (a binary sparsity mask with sign) is necessary to find the winning tickets in the field of the Lottery Ticket Hypothesis (LTH). Specifically, this paper founds that equipped with the signed mask as well as normalization layer parameters of a subnetwork trained with learning rate rewinding (LRR), a random initialized network can also achieve comparable performance with learning rate rewinding (LRR) trained networks. Extensive experiments on CIFAR-100, Tiny-ImageNet, and ImageNet with various networks demonstrate the effectiveness of signed mask.

### Strengths
1. This is a pioneering work that studies the importance of signed mask in the field of LTH. The LTH suggests that the weights initialization, either the original random initialization from the vanilla LTH or some early checkpoints from the weight rewinding, is necessary to win tickets, while this paper suggests that we can rely on the signed mask with random initialization to achieve comparable performance. 
From my personal perspective, finding the signed mask is easier in practice than finding the ad-hoc initialization.

### Weaknesses
1. This paper only evaluate some lightweight networks on ImageNet such as MobileNet and MLP-Mixer, with an accuracy below 70%. Thus, it's unclear whether the proposed method still generalize well on more powerful networks such as ResNet and Vision Transformers. At least, it would be better if this paper could follow the setting in LRR paper that applies Resnet-50 on ImageNet (see Table 1 of Renda et al., 2020).


2. This paper assumes that networks always include normalization layers and its parameters is necessary, which could limit its generalization. Although normalization is pretty common in modern networks, some early networks don't have normalization layers, such as LeNet and VGG16 without batch normalization [1]. Therefore, it would be better to examine the performance of the signed mask of the LRR subnetwork on these pioneering models to determine if the conclusions hold consistently across different architectures.


3. This paper claims that "an effective signed mask is ALL WE NEED to win the lottery". However, this work still requires the learning rate rewinding to obtains the signed mask with multiple ($T$) iterations. Ideally, the signed mask can be directly obtained from a pre-trained dense networks in the future work. 

4. Some mathematical notations seem inconsistent. For example, if I understand correctly, in Line 184, the LRR subnetwork should be $\mathcal{A}( \theta_T^{LRR} ,  m_T^{LRR})$ (same as Line 436), rather than $\theta_0^{LRR}$.  Besides, is $\theta_0$ (Line 172) same as $\theta_{init}$.

### Questions
Please address and discuss the weaknesses above in author response.

### Soundness
3

### Presentation
3

### Contribution
3
