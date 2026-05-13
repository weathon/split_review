# Magnitude Invariant Parametrizations Improve Hypernetwork Learning

- Decision: Accept
- Scores: 6, 6, 8, 5

## Abstract
Hypernetworks, neural networks that predict the parameters of another neural network, are powerful models that have been successfully used in diverse applications from image generation to multi-task learning.
Unfortunately, existing hypernetworks are often challenging to train. Training typically converges far more slowly than for non-hypernetwork models, and the rate of convergence can be very sensitive to hyperparameter choices.
In this work, we identify a fundamental and previously unidentified problem that contributes to the challenge of training hypernetworks: a magnitude proportionality between the inputs and outputs of the hypernetwork.
We demonstrate both analytically and empirically that this can lead to unstable optimization, thereby slowing down convergence, and sometimes even preventing any learning.
We present a simple solution to this problem using a revised hypernetwork formulation that we call Magnitude Invariant Parametrizations (MIP).
We demonstrate the proposed solution on several hypernetwork tasks, where it consistently stabilizes training and achieves faster convergence.
Furthermore, we perform a comprehensive ablation study including choices of activation function, normalization strategies, input dimensionality, and hypernetwork architecture; and find that MIP improves training in all scenarios. 
We provide easy-to-use code that can turn existing networks into MIP-based hypernetworks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors study the problem of improving the stability and efficiency of training hypernetworks. They first observe a previously unidentified problem with hypernetwork training, namely that for certain hypernetwork architectures the scaling of the input to the hypernetwork leads to the proportional scaling of the outputs. This can lead to destabilization of the training procedure and slow training. The authors propose a a novel hypernetwork formulation that removes this proportionality property. Across several architectures, tasks and optimizers, their framework leads to improved training stability and convergence.

### Strengths
While normalizing inputs to neural network models is already well established best practice, to the best of my knowledge the specific application of this best practice for hypernetwork inputs has not been studied as much. I consider the fact that the input encoding approach of the authors is straightforward a plus. The experimental validation of the key claims of the papers is extensive.

### Weaknesses
I am not really sure if the output encoding part of the framework fits well with the problem that the authors claim to solve. It is not clear how output encoding relates to the input and output proportionality problem. It also makes interpreting the experimental results where both input and output encoding are used harder. Intuitively, output encoding allows the model to learn the task even if the hypernetwork does nothing so it is not clear if we improve hypernetwork training or just make the hypernetwork path less critical and rely on "classical" parameter learning which is typically more stable.

Another thing that is not clear to me is that it is not clear to me what is special about hypernetworks so that input normalization needs to work differently than "classical" networks. The scaling property would hold for a "classical" network as well for the appropriate activations. And yet Appendix C.5 claims that standard normalization techniques of "classical" networks would not work for hypernetworks. Appendix C5 seems to suggest that "classical" normalization techniques could make the output independent of the input. It is not clear to me why this is a problem only for hypernetworks and not for "classical" networks.

Also it would be useful to clarify why one could not just divide the hypernetwork input by its norm, at least for the case of a multi-dimensional hypernetwork inputs. In my mind, if the problem was just the scaling of the output, this should have worked. The suggested methods go beyond just fixing the scale of the input vector as a whole so it is not very clear if the problem is indeed the input output proportionality or some more general feature scaling issue.

### Questions
I have summarized above some points that were not very clear to me. I would be willing to increase my score if they were to be clarified.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a solution, Magnitude Invariant Parametrizations (MIP), to a previously unidentified optimization problem in hypernetwork training that causes large gradient variance and unstable training dynamics. MIP, by modifying the typical hypernetwork formulation, addresses this issue without adding training or inference costs. The authors extensively test MIP, demonstrating improved stability and faster convergence in hypernetwork training across various settings. They also release HyperLight, an open-source PyTorch library, to ease the implementation of MIP and promote hypernetwork adoption. Through rigorous analysis and experimentation, the paper showcases MIP's potential in substantially enhancing hypernetwork training, marking a significant advancement in this domain.

### Strengths
The strengths of this paper include the identification of a novel optimization problem in hypernetwork training, the proposal of a new formulation (MIP) that addresses this issue without extra computational costs, extensive testing and comparative analysis demonstrating MIP's effectiveness, and the provision of an open-source library, HyperLight, to facilitate the practical adoption of the proposed solution in hypernetwork models. Through rigorous analysis and extensive experimentation, the paper makes a significant contribution towards improving the stability and convergence speed in hypernetwork training, providing a promising direction for the community.

### Weaknesses
The paper mainly focuses on fully connected layers and common activation, initialization choices, and optimizers (SGD with momentum and Adam) in its experiments, which may not encompass a broader spectrum of hypernetwork architectures or other types of networks. Specifically, the experiments do not explore the behavior of MIP with convolutional layers, recurrent layers, or attention mechanisms, which are prevalent in many modern neural network architectures. There's also a mention of unexplored territories like the effect of MIP on transfer learning and other less common architectures and optimizers, indicating a scope for broader empirical validation. For instance, the paper does not investigate the performance of MIP when combined with adaptive optimizers beyond Adam, such as AdaGrad, RMSprop, or their variants. Furthermore, the impact of MIP on real-world applications or larger-scale problems is not thoroughly explored, which might be crucial for the adoption of this technique in practical settings. While the medical imaging application is a good start, more diverse real-world datasets and tasks should be considered to demonstrate the general applicability of MIP.

### Questions
Mentioned in the weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a novel parametrisation for hypernetworks that is magnitude invariant (MIP). The main motivation for MIP stems from the author’s observation that the hypernetwork output, when using piece-wise linear activations, has a magnitude proportional to the hypernetwork input. The authors argue that this proportionality is detrimental for the hypernetwork optimization as it affects the gradient variance. MIP is then introduced as a way to remove this dependence on the magnitude by parametrising the input to the hypernetwork in terms of Fourier features that have a constant norm throughout training. Then, in order to allow for hypernetwork outputs that are non-proportional to the hypernetwork inputs, the authors propose a residual parametrisation where an auxiliary weight matrix is trained directly and the hypernetwork output is used as an additive correction to that weight matrix. The authors then show that these two modifications to standard hypernetwork training, solve the proportionality problem and improve hypernetwork performance across the board.

### Strengths
- The authors identify a novel issue that seems to be important (based on the improvement delta from MIP) for hypernetwork training.
- The specific MIP parametrisation is novel and practically broadly useful for any task that involves hypernetworks. 
- The experiments are relatively extensive in terms of tasks and ablation / robustness studies.
- The paper is mostly well written and clear in the presentation of the main ideas and results.

### Weaknesses
 - While the authors do empirically show that MIP benefits training, it is not clear whether the increased variance could also be controlled with, e.g., appropriately chosen (i.e., lower) learning rates and (i.e., higher) momentum, in the original parametrisation (which could attain similar performance, albeit slower). It would be beneficial to see a more detailed analysis of the optimization landscape and how the magnitude proportionality affects the gradient flow. Specifically, are there any differences in the sharpness of the minima or the presence of plateaus that could explain the observed benefits of MIP? A more rigorous comparison, perhaps using techniques like loss surface visualization or gradient norm analysis, would strengthen the claims.
- This is something that the authors themselves identify, but given that hypernetworks are becoming popular for fast adaptation of pertained models, e.g., [1], it is important to see whether the magnitude proportionality effect is also detrimental there. It is crucial to investigate the impact of MIP on few-shot learning scenarios where hypernetworks are used to adapt pre-trained models, as the magnitude proportionality issue might be exacerbated in these settings. The authors should consider including experiments that evaluate the performance of MIP in such few-shot adaptation tasks.

### Questions
I find the overall paper to be well written, the arguments clear and the proposed solution convincing. Therefore, I am happy to recommend acceptance. My questions and suggestions are the following:
- It would be interesting to see whether the residual formulation of the hypernetwork closes meaningfully the gap between fully task specific parameters and the ones predicted by the hyper network, i.e., $\theta^0 + h(E_{L2}(\gamma); w)$. For example, what is the performance if on a new task $t$ one starts from $\theta^0$ and just optimises for a specific number of steps on that task to get $\theta_t^*$? Is $\theta_t^* - \theta_0$ related to $h(E_{L2}(\gamma); w)$? Is the performance of $\theta_t^*$ similar to the performance of $\theta^0 + h(E_{L2}(\gamma); w)$?
- Does the update given by the hypernetwork in this residual formulation need to be dense? Is the hypernetwork only adapting a few dimensions of $\theta^0$?
- It is not clear why for non-scalar inputs $\gamma$, i.e., $\gamma \in \mathbb{R}^D$ with $D \geq 2$  a simple unit normalisation transformation, i.e., $\hat{\gamma} = \frac{1}{\|\|\gamma\|\|_2}\gamma$ would not work for removing the dependence on the magnitude. It seems to me that in this case each $\hat{\gamma}$ would just correspond to a different point on the hypersphere and the output of the hypernetwork would not be independent of the input.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper identifies a problem that contributes to the challenge of training for hypernetworks: The magnitude proportionality between the inputs and outputs of the hypernetwork. The authors demonstrate how this proportionality can result in unstable optimization processes. To mitigate this issue, they introduce a magnitude-invariant parameterization method for hypernetworks, demonstrating its effectiveness in stabilizing the training process and accelerating convergence.

### Strengths
- The techniques proposed in this paper are indeed helpful in stabilizing the training of hypernetworks. Given that hypernetworks are widely used in machine learning. These techniques can be useful for practitioners.

### Weaknesses
- The discussion regarding why input/output proportionality results in unstable training is somewhat insufficient. It is a well-known fact that neural networks with piecewise linear activation functions, such as ReLU networks, exhibit this proportionality between inputs and outputs. However, if proportionality is the main reason, why ReLU networks are not well-known for having such problems for classical tasks such as regression/classification (not in hypernetworks)?  The paper would benefit from a more in-depth analysis of the specific conditions within hypernetworks that exacerbate the instability caused by this proportionality. For instance, a comparison of the gradient behavior in standard ReLU networks versus hypernetworks under similar input scaling conditions could provide valuable insights.
- The two strategies introduced in the paper, namely input encoding and additive output formulation, are a bit ad hoc from my perspective. While these methods undoubtedly offer practical benefits for hypernetworks, I am not sure if the contribution is significant enough. A more thorough exploration and explanation of the theoretical underpinnings that underscore the significance of these techniques would enhance the paper's contribution and provide a clearer justification for their adoption. Specifically, the paper could elaborate on why the proposed input encoding scheme is more effective than other encoding methods, and how the additive output formulation interacts with the magnitude-invariant property to stabilize training.

### Questions
- I might miss the related information. Apologies if that is the case. Are there any results of combining additive output with BatchNorm/LayerNorm in Figure 5? It is interesting to see such results because it verifies that MIP has something that normalization layers cannot offer. If proportionality is the main reason, what are the theoretical reasons that MIP can solve the problem but normalization cannot?
- If the problem is proportionality, how about we use other activation functions such as ELU or GELU? Does that solve the problem? If not, can we still say the problem is proportionality?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
