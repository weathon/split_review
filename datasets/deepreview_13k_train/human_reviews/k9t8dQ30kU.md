# Task structure and nonlinearity jointly determine learned representational geometry

- Decision: Accept
- Scores: 8, 8, 6, 5

## Abstract
The utility of a learned neural representation depends on how well its geometry supports performance in downstream tasks. This geometry depends on the structure of the inputs, the structure of the target outputs, and the architecture of the network.  By studying the learning dynamics of networks with one hidden layer, we discovered that the network's activation function has an unexpectedly strong impact on the representational geometry: Tanh networks tend to learn representations that reflect the structure of the target outputs, while ReLU networks retain more information about the structure of the raw inputs. This difference is consistently observed across a broad class of parameterized tasks in which we modulated the degree of alignment between the geometry of the task inputs and that of the task labels. We analyzed the learning dynamics in weight space and show how the differences between the networks with Tanh and ReLU nonlinearities arise from the asymmetric asymptotic behavior of ReLU, which leads feature neurons to specialize for different regions of input space. By contrast, feature neurons in Tanh networks tend to inherit the task label structure. Consequently, when the target outputs are low dimensional, Tanh networks generate neural representations that are more disentangled than those obtained with a ReLU nonlinearity. Our findings shed light on the interplay between input-output geometry, nonlinearity, and learned representations in neural networks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The manuscript analyzes how the geometry of the latent representation of a one layer neural network is influenced by the choice of the activation function, in particular ReLU and Tanh activation functions.

Using different metrics from the literature, namely kernel alignment of the latent represent, linear decodability, CCPD and sd, it is shown that the latent representation of ReLUnetworks tend to retain more information about the input, while Tanh networks align more with the output(label) representation.

Experiments are performed on multiple synthetic tasks and on Cifar 10.

### Strengths
*Originality*

The analysis on how the activation function can enforce a different latent representation geometry is to the best of my knowledge, novel and interesting direction to investigate.

*Clarity*

The paper is overall clear.

*Quality*

There are multiple experiments on the synthetic setting which  support quite well the claims of the paper. However, the real experiment is not strongly supported( see weaknesses section).

*Significance*

While the result on synthetic data are promising, there still some missing buts in order that make somewhat difficult to evaluate the impact of the paper ( see weaknesses section).

### Weaknesses
 - While the analysis is interesting and it it wasn't clear to me how much it can impact can the paper have, its current form: (i) it is not clear  how much the analysis extends to real tasks: the experiments of Cifar are somewhat limited (just the alignment metric is reported and it is not clear if this behavior holds for deeper networks: i.e. some ablations on the network depth should be incorporated in the experiment in my opinion)  and the assumptions done on the synthetic tasks are unlikely to hold on larger networks (ii) there is no theory or additional experimental evidence that support why tanh and ReLU behave differently (see question section); 


- The paper should report a better contextualization in the literature and comparison with similar works (it misses a related work section). I reported some works that should be discussed:

- Hayou, S., Doucet, A.; Rousseau, J.. On the Impact of the Activation function on Deep Neural Networks Training. Proceedings of the 36th International Conference on Machine Learning

- Ramachandran, Prajit, Barret Zoph, and Quoc V. Le. "Searching for activation functions." arXiv preprint arXiv:1710.05941 (2017).

- Ding, Bin, Huimin Qian, and Jun Zhou. "Activation functions and their characteristics in deep neural networks." 2018 Chinese control and decision conference (CCDC). IEEE, 2018.

- Papyan, Vardan, X. Y. Han, and David L. Donoho. "Prevalence of neural collapse during the terminal phase of deep learning training." Proceedings of the National Academy of Sciences 117, no. 40 (2020): 24652-24663.

- Zhu, Zhihui, Tianyu Ding, Jinxin Zhou, Xiao Li, Chong You, Jeremias Sulam, and Qing Qu. "A geometric analysis of neural collapse with unconstrained features." Advances in Neural Information Processing Systems 34 (2021): 29820-29834.



- Concerning clarity a better description of the metrics employed (especially SD an CCPD) would be needed, also in terms of mathematical/formal statements,if helpful.



*Minor*

I spotted a typo:

- section 5 eiegenvalues -> eigenvalues

### Questions
- Can the authors elaborate on the intuition of why Tanh and ReLU behave in this way? And it would be possible to derive theoretical results on this?

- The target alignment  phenomenon of Tanh relates to neural collapse [a] phenomenon : i.e. when training is kept under zero error the representation in the last layer tend to collapse in equidistance clusters aligned to the targets.
However, to the best of my knowledge this phenomenon should be agnostic of the activation function. Can the authors elaborate on this perspective?

[a] Papyan, Vardan, X. Y. Han, and David L. Donoho. "Prevalence of neural collapse during the terminal phase of deep learning training." Proceedings of the National Academy of Sciences 117, no. 40 (2020): 24652-24663.

[b] Zhu, Zhihui, Tianyu Ding, Jinxin Zhou, Xiao Li, Chong You, Jeremias Sulam, and Qing Qu. "A geometric analysis of neural collapse with unconstrained features." Advances in Neural Information Processing Systems 34 (2021): 29820-29834.


- How much the assumptions of fixing weights of the second layer is limiting in terms of measuring the four metrics employed (alignment, decodability, ccpd, sd). Is it needed just in order to approximate the dynamics?


- What is the mathematical formulation of the nonlinearity analyzed in section 7 ?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The current paper discussed how ReLu and Tanh activation functions impacted the representation geometry of a single layer feedforward neural network. The authors found that Tanh nonlinearity tend to generate target aligned representation, while RuLe nonlinearity favors input aligned representation. It seems the symmetric saturation of the nonlinearity is the key for target-aligned representation of the Tanh function.

### Strengths
The paper has thoroughly studies the representation geometry using various geometry matrix, which allowed authors to generate insights on whether a network generate input- or target- aligned representation in the hidden layer of a single layer feedforward network. It shows how the representation geometry evolves over the course of learning. In particular the trajectories of input weights to hidden layer neurons for inter-class and intra-class labels is interesting.

### Weaknesses
In general, the results generated by the current study that Tanh nonlinearity helps generate target aligned representation is limited to simple networks and simple input-output mapping. The representation geometry in these simple networks probably are not sufficient for many real-world problems that require capturing intricate patterns. Furthermore, the study does not explore the effect of network depth on the observed representation geometry. It is unclear if the observed input or target aligned representations would persist in deeper networks, where the hidden layers are further removed from the input and output layers. The study also does not consider the impact of different initialization schemes, which could potentially influence the observed alignment. The non-monotonic effect of noise on ReLU networks is not fully explained. While the authors suggest smoothing gradients, the evidence for this is not fully convincing. The study also does not fully explore the impact of different noise distributions. It's possible that the observed non-monotonic effect is specific to the type of noise used in the experiments. The paper also does not fully explore the effect of different optimization algorithms. It is possible that the observed alignment is dependent on the specific optimization algorithm used.

### Questions
1.	Why the decoding accuracy is worse in training data with high separability of trained dichotomy for Tanh network (figure 3 upper left)? The separability has non-monotonic effects on input alignment in the Tanh network, why is that?
2.	Why the noise level has non-monotonic effects on the Relu network, consistently observed in all geometric matrix and for all tested separability of trained dichotomy? Author suggested smoothing gradients. What’s the evidence supporting such conclusion?
3.	Are the results robust to the input data range, eg. Input data ranges between 0 to 1, vs. input data ranges between -1 to 1.  
4.	When training data becomes more complicated, as suggested by the noise input analysis and the XOR task, the difference between tanh and ReLu vanish. This suggested that Tanh helps generate a target-aligned representation when the input data is readily separated for clustering. Or in a multi-layer network, using tanh at the final layer seems to be beneficial. This is not a novel conclusion. What’s the new insights learnt from the current study. Provide a discussion on how the results learnt in the current study would have a general impact.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors systematically conducted a series of gradually more intricate experiment to investigate how nonlinearity, label separability, and input data geometry affects the learned representation in the hidden layer of 2 layer MLP, with potential generalization to CNNs. They quantified representation geometry with many statistics, including the CKA with input data, output label; parallelism index; CCGP; classifying ability for unseen label. They found a central unexpected theme that Tanh network seems to keep more geometry about the target label; while relu network seems to align the representation with the input data, and keep more target-unrelated information about the input. Finally, they dissect the source of differences between the nonlinearities ReLU and Tanh, and found that the double sided symmetric saturation of Tanh function probably explain their difference.

### Strengths
- Clear results. Though the general theme is expected, the relevance of activation function still has a little bit surprise.
- The experiments are systematic and well-designed, which formed an investigation with clear logic. The statistics for quantifying the representation geometry are quite comprehensive and laudable.
- The way of visualizing the training dynamics in weight space along intra-class vs inter-class axes is illuminating, further this analysis of toy model indeed provides intuition for the phenomena regarding different gradient learning dynamics for different activation functions (at lease in 2-layer networks).
- Nice controlled experiments to parse out factors explaining difference between relu and tanh, in Sec. 7, showing that the rough two-sided saturation shape is the key. in another perspective, the banded gradient structure of activation function is key.
- The claim, (if it’s general) will definitely impact how we understand the representation similarity between two systems, e.g. the brain vs CNNs. Namely, if neurons in the visual brain are using a different activation function from the CNNs, even the underlying linear function is the same, the similarity matrix won’t match.

### Weaknesses
 - Most of the experiment focused on toy scale examples of binary classification with 2-layer network, even experiments with CNN has only 2 conv-layer networks. I feel it’s within the scope of this paper to show empirical evidence that the observations may generalize to larger scale CNN and larger dataset. (e.g. resnet and ImageNet) Will it be feasible to swap the activation function and show some similar effects?
- Notation in Eq. (in Sec. 3.1.1), or the method description in Sec. 3.1.1 is a bit confusing. Is it using multi-output setup so $W_O$ is also a vector?
- There seems to be super interesting intuition going on in Figure 1C, but the text in Sec. 3.1.1 didn’t seem to walk through the logic, leaving the reader to parse the schematics themselves. —— though after working through the math of an example it starts making sense.

### Questions
- The assumptions for making the weight learning animation seems a bit strong, can we alleviate those assumptions? (fixed output weights and discretized output weights)?
- How to generalize the learning dynamic visualization to non-two-layer deeper networks?
- Is there a typo of formula in Sec 3.1.1 “*the covariance between input and output: xxx*" should it be $y_i$?

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the learning dynamics of 1-hidden-layer neural networks, and focuses on how representation properties are affected by the nonlinearity of the network. Specifically, the paper compares Tanh and ReLU nonlinearity, and show that Tanh networks tend to reflect structure of target outputs while ReLU networks tend to retain more information about the inputs.

### Strengths
The paper presents an interesting empirical study on how nonlinear activation functions affect the learned representation in the network, specifically how they align with the target output and the input. The results are evaluated using several previously established metrics, starting from simple toy model dataset, the authors carefully analyzed the effect of input geometry on learned representations, and later extended their results to more complicated tasks.

### Weaknesses
The paper largely focuses on ReLU and Tanh nonlinearity, which are two very specific type of activation functions. It would be nice if the authors can identify what exactly is the property of the nonlinear function that causes the difference in representation, and evaluate further (as they show in Fig. 5 but with more extensive results). 
The paper also presents mostly empirical evaluations and analysis without theoretical insights.

### Questions
In most of the work the result focuses on 1-hidden-layer neural networks but in the convolution part there are two FC hidden layers. I'm wondering how depth affect your current observations.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
