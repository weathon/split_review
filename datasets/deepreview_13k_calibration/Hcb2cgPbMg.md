# Learning Continually by Spectral Regularization

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 8, 6

## Abstract
\freefootnote{Correspondence to: Alex Lewandowski <lewandowski@ualberta.ca>.}
  \vspace{-3mm}
Loss of plasticity is a phenomenon where neural networks can become more difficult to train over the course of learning.
Continual learning algorithms seek to mitigate this effect by sustaining good performance while maintaining network trainability.
We develop a new technique for improving continual learning inspired by the observation that the singular values of the neural network parameters at initialization are an important factor for trainability during early phases of learning.
From this perspective, we derive a new \emph{spectral regularizer} for continual learning that better sustains these beneficial initialization properties throughout training.
In particular, the regularizer keeps the maximum singular value of each layer close to one.
Spectral regularization directly ensures that \emph{gradient diversity} is maintained throughout training, which promotes continual trainability, while minimally interfering with performance in a single task.
We present an experimental analysis that shows how the proposed spectral regularizer can sustain trainability and performance across a range of model architectures in continual supervised and reinforcement learning settings. 
Spectral regularization is less sensitive to hyperparameters while demonstrating better training in individual tasks, sustaining trainability as new tasks arrive, and achieving better generalization performance.
\looseness=-1

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors derive a new spectral regularizer for continual learning inspired by the observation that the singular values of the neural network parameters at initialization are an important factor for trainability during early phases of learning. Under such regularization they keep the maximum singular value of each layer close to one. 

Under such spectral regularization they claim that they can directly ensure gradient diversity throughout training, which promotes continual trainability, while minimally interfering with performance in a single task. 

To validate the utility of the proposed regularization and the claims they present empirical evaluation. The experimental results shows how the proposed spectral regularizer can sustain trainability and performance across a range of model architectures in continual supervised and reinforcement learning settings. They try to demonstrate better training in individual tasks, trainability as new tasks arrive, and better generalization performance.

### Strengths
- The continual learning topic is important area and loss of plasticity is fundamental challenge.
 - The approach is interesting and the idea to regularize the maximum singular value of each layer close to one seems novel.
 - The presentation of the work is nice, while the motivation is appropriate.
 - The authors present results for several experiments, evaluating different properties.

### Weaknesses
 - It appears like a marginal improvement and novelty with respect to L2 regularization.
- It seems that there is a connection to L2 regularization, or L2 regularization towards initialization of parameters which is a sort of spectral regularization.
- Deeper understanding/analysis of the proposed and the one above seems important and might be beneficial, but I was not able to find it in the paper L2 norm vs spectral norm in this context.  
- In the experimental section, looking at the graph and the results it seems that the improvements are marginal, or not highlighted significantly.
- In the same experimental section, I was able to see only graphs and plots, was not able to see actual table or values, to be able to apricate the achieved results more.

### Questions
How different the propose approach is from L2 regularization on the same set of parameters?

### Soundness
3

### Presentation
3

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
The paper considers the continual learning problem. In order to keep the stability of problem, the spectral regularizer is added to the objective function. Experimental results demonstrate the effective of the approach method.

### Strengths
This paper provide the spectral regularize to the objective function for improving the stability of the problem.

### Weaknesses
However, the added spectral regularize would bring in the cost of computation for the continual learning if facing large model and large data.

Furthermore, the connection between the initialization, singular values of the Jacobian, condition numbers, and their influence on the selection of new parameters (e.g., rank) is not clearly established. The paper does not provide a detailed analysis of how these factors interact to affect the training dynamics and the final performance. The performance of the spectral regularization is not consistently superior to that of vision transformers and ResNets across all experimental settings, and the paper lacks a comprehensive comparison with state-of-the-art continual learning methods. The datasets used in the experiments may not be sufficiently diverse or challenging to fully demonstrate the robustness of the proposed approach. Finally, the sudden decrease observed in Figure 5 on the y-axis requires a more thorough explanation, including the potential causes and implications for the method's stability.

### Questions
1 through the initialization is the key to the trainability, singular values of Jacobian and the condition numbers would induce the new selected parameters, e.g., rank
2 how to effectively deal with computation of the spectral norm, i.e. spectral regularization,
3 the performance of the spectral is not always better than that of vision transformer and resents
4 what’s more, the datasets are not enough, please refer to the latest approach,
5 for the figure 5, what’s the phenomenon of suddenly decrease for the y-axis.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper addresses plasticity loss in continual learning by proposing a spectral regularization technique. The proposed regularization technique regularizes the network’s weights at each layer towards a spectral norm of 1. This method is motivated by a spectral analysis of (continual) learning and the observation that standard neural network weight initializations exhibit good trainability and generalization. The paper’s proposed method is validated on a series of continual learning benchmark problems where it is shown to be performant and robust to the choice of regularization strength.

### Strengths
- Section 1 Introduction and Section 2 Problem Setting are well written with clarity and detail, effectively introducing the problem, the spectral regularization algorithm, and some intuition behind its formulation.
- The spectral analysis of continual learning well motivates the algorithm. 
- The experiments consider a wide swathe of existing continual learning algorithms, both ResNet-18 and Vision Transformer architectures, and a variety of datasets and non-stationarities. Over this set of experiments, spectral regularization attains competitive performance and is robust to its choice of hyperparameter.

### Weaknesses
 - Although spectral regularization is well motivated and the paper includes positive empirical results, one way to improve the paper would be to derive some theory illustrating the benefit of spectral regularization, and drawbacks of other regularization schemes, in continual learning.



### Questions
- Is there any particular reason why Continual Backprop was not evaluated in the experiments?

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
The paper introduces a new regularization to encourage neural networks to combat loss of plasticity phenomenon in a continual learning setting. The new approach is based on the observation that the maximum singular value of neural network layers grow over the course of training and avoiding this growth can help improve trainability of models in a continual learning setting. The proposed regularizer attempts to steer the maximum singular value of a layer to 1 (and 0 for the bias terms). The paper uses accepted datasets and tasks in continual learning literature to study the effectiveness of the proposed method over several baselines.

### Strengths
- The paper solves the problem of loss of plasticity in continual learning by addressing trainability. 

- Section 3 and Section 4 in the paper are nicely written and is valuable to a general audience. Also, the paper provides at least two illustrative examples as well as some analysis to make the observation that the top singular value growth may cause training issues.

- The development of proposed solution via spectral regularization  is intuitive

### Weaknesses
 * The proposed method to keep top singular value small bears some similarities to the following paper:
  - https://arxiv.org/abs/2303.06296

* The experimental setup used in the paper is incomplete and not very convincing in order to judge the empirical results:
  - The models used are on the smaller side (ResNet-18 and ViT)
  - ViT model size is not specified in the paper 
  - The dataset used in Tiny-Imagenet which is not fully described. I believe the inputs are 64x64 based on my search but this detail is missing in the paper
While I am not an expert in continual learning area, there are recent papers that suggest that larger datasets (resolution and size) are available and used in continual learning studies

* The presentation of the experimental results and discussion section could be improved:
  - Figure 1 has legend only on the top left figure which makes it hard for the reader to follow how each method works across different continual learning scenarios
  - Figure 2 has a similar issue with legend
  - he paper does not define all the quantities plotted in Figure 3.
  - Since the paper focuses on trainability, additional graphs that show how trainability improves in CL setting might be useful in the presentation. Figure 3 provides a hint but in this case the shrink and perturb baseline shows better trainability as defined by singular value.

I'm unable to support acceptance at this point due questions on setup used in empirical analysis. The paper could benefit from an update that includes missing information that can give the reader an idea on exact metrics tracked, setup used, dataset details and other information.

### Questions
In addition to the points noted in weakness section, I wonder if the following statement is too strong
```
Note that these datasets and architectures encompass all continual supervised learning experimental settings considered in the loss of plasticity literature.
```

### Soundness
2

### Presentation
2

### Contribution
2
