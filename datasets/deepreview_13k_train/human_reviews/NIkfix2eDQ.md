# Plastic Learning with Deep Fourier Features

- Decision: Accept
- Scores: 6, 8, 5, 6, 6

## Abstract
\freefootnote{Correspondence to: Alex Lewandowski <lewandowski@ualberta.ca>.}
  Deep neural networks can struggle to learn continually in the face of non-stationarity.
  This phenomenon is known as loss of plasticity.
  In this paper, we identify underlying principles that lead to plastic algorithms.
  In particular, we provide theoretical results showing that linear function approximation, as well as a special case of deep linear networks, do not suffer from loss of plasticity.
  We then propose \emph{deep Fourier features}, which are the concatenation of a sine and cosine in every layer, and we show that this combination provides a dynamic balance between the trainability obtained through linearity and the effectiveness obtained through the nonlinearity of neural networks.
  Deep networks composed entirely of deep Fourier features are highly trainable and sustain their trainability over the course of learning.
  Our empirical results show that continual learning performance can be drastically improved by replacing \texttt{ReLU} activations with deep Fourier features.
  These results hold for different continual learning scenarios (e.g., label noise, class incremental learning, pixel permutations)
  on all major supervised learning datasets used for continual learning research, such as CIFAR10, CIFAR100, and tiny-ImageNet.
  \looseness=-1

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Continuous learning involves a model learning from changing, non-stationary distributions. The model should avoid forgetting previously learned information while adapting to new incoming data. The paper first demonstrates that linear networks adapt more easily to new data than non-linear models. However, non-linearity is crucial for capturing features and achieving good performance in supervised settings. To balance linearity and non-linearity, the paper proposes using an activation function that combines cosine and sine functions, which is called deep fourier features.

### Strengths
The proposed activation funtion may replace the ReLU and serve as the comman practice when building continuous learning model.

### Weaknesses
1. While the authors establish that linear networks can more readily adapt to new data (Sec 3.1), they do not examine whether these networks are resistant to catastrophic forgetting. Without measuring anti-forgetting properties, it’s unclear if the proposed approach truly meets both requirements of continuous learning (adaptability and retention). Specifically, the theoretical analysis in Section 3.1 focuses on adaptability to new data distributions but lacks a corresponding analysis of how the proposed deep Fourier features activation function would mitigate interference with previously learned knowledge. A more rigorous evaluation of the anti-forgetting capabilities of deep Fourier features would involve experiments on established benchmarks for catastrophic forgetting, such as permuted MNIST or split CIFAR.

2. The proposed activation function, $Fourier(z)=[sin(z),cos(z)]$, lacks clear implementation details, which may hinder practical use and replication. For instance, it’s ambiguous how the function applies to each unit in a layer and whether each pre-activation value is mapped to both sine and cosine or alternates between the two. If each pre-activation value $z_i$ in a layer is mapped to both $sin(z_i)$ and $cos(z_i)$, this would effectively double the width of the layer, which has implications for computational cost and parameter count. Conversely, if there's an alternating mechanism, the specific rule for selecting between sine and cosine needs to be defined. Furthermore, the interaction between this activation function and standard network components like batch normalization or dropout is not discussed.

3. While using sine and cosine for the activation function is interesting, the rationale behind this choice is not fully explained. Periodic linear functions might also be a candidate for balancing linearity and non-linearity, so further justification or comparative analysis would strengthen the argument for cosine and sine. The authors should elaborate on why properties like smoothness and closure under differentiation make sine and cosine preferable to other periodic or piecewise linear functions. For example, a comparative analysis of training stability and convergence speed between deep Fourier features and other periodic activation functions would provide stronger evidence for the chosen design.

### Questions
1. The theory in Section 3.1 suggests that linear networks can adapt to new data, but does not address resistance to forgetting. Could the authors provide empirical results to assess the anti-forgetting capability of their approach? This would help clarify whether the method supports both critical aspects of continuous learning.

2. Can the authors explain how the Fourier activation function, defined as $Fourier(z)=[sin(z),cos(z)]$, is applied in practice? For instance, if a pre-activation vector is given as $[z_1, z_2, ..., z_n]$, how would each unit in the layer be processed? Should each pre-activation value use both sine and cosine, or is there a selection mechanism between the two? Pseudo-code or a mathematical expression would be highly helpful.

3. Why did the authors choose cosine and sine for the activation function over other periodic functions or piecewise linear functions within defined intervals (e.g., periodic $y = x$ replacing $ y = sin(x)$, periodic $y = 1-|x|$ replacing $ y = cos(x)$)? A justification of this choice would provide greater insight into the effectiveness of these functions for balancing linearity and non-linearity in continuous learning.

Addressing these questions could strengthen the paper’s contribution and may support a higher rating score.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper studies the problem of plasticity loss in deep neural network under continual learning. The authors suggest that the loss of plasticity or trainability is caused by the nonlinearity in activation functions.  The authors prove that linear layer and a diagonal linear network dont suffer from a loss of plasticity, showing empirically that deep linear network also dont suffer from that   The authors then suggest that a perfect mix of linearity and nonlinearity  is a potential solution to the plasticity loss while maintain the expressiveness of deep neural network. 
The authors then suggest deep Fourier features where sin and cosine activation functions are combined. The authors showed in the experiments that such activation function maintain trainability but needs regularization to prevent overfitting.

### Strengths
The paper is well written. 

A discussion and analysis of an important problem. 

Showing that linear network don't suffer plasticity loss and a mix between linear and non linear can retrain trainability. 

Theoretical evidence and empirical evidence support the paper contribution.

### Weaknesses
While I enjoyed reading the paper and its flow, the presentation can still be improved substantially especially in the figures and equations. 
For example, equations are not numbered which makes it hard to refer back to specific equation. Figures are not well explained, and colours are really hard to distinguish among different baselines. 

While a new activation function is introduced, a proper analysis of its behaviour and the performance of the network should be demonstrate here we only see results on continual learning and later figure out that the results were with a regularization.

It is not clear which metrics are reported, e.g., test accuracy measured by what? performance on the latest task or all tasks?
Forgetting is never discussed. 

Only one network is studied, what about other architectures?



### Questions
Why loss of trainability is used, does it differ from the loss of plasticity defined in https://www.nature.com/articles/s41586-024-07711-7 and if not why using different terms?

What is the performance compared to ReLU or LeakyReLU activations on offline setting (training on full dataset with no continual learning)?


Ln 076-079 are not quite clear

Could you define unit sign entropy earlier, or make it clear when using it in the intro.

ln 107 is unclear.

What is the suboptimality gap in line 144

In ln 305, what if \alpha was trainable parameter?

Could you add continual backpropagation as a baseline https://www.nature.com/articles/s41586-024-07711-7

Please add a section to describe the metrics used. 

It is unclear to me why the setup of diminishing noise is considered as the first experiment.

Does the trainability still persist on longer tasks, e.g., the ImageNet sequence of   https://www.nature.com/articles/s41586-024-07711-7

I am welling to increase my score upon addressing my questions, thanks!

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work investigates loss of plasticity in different continual learning scenarios, which hinders networks' ability to adapt to new knowledge over time. The authors introduce Deep Fourier Features as a new method to enhance plasticity, which integrate sine and cosine functions as activation components in each layer of the network. These features concatenate sine and cosine functions in each network layer, allowing for a balance between linearity (supporting plasticity) and nonlinearity (supporting representational power). Through theoretical and empirical results, the paper demonstrates that using Deep Fourier Features can significantly improve continual learning performance across different tasks and datasets, outperforming traditional ReLU-based networks.

### Strengths
+ The paper presents a novelty method by integrating Fourier Features into deep networks, offering a new view on balancing linearity and nonlinearity to sustain plasticity.
+ The authors provide a comprehensive theoretical basis for their Deep Fourier Feature, proving that linear function approximations and certain linear networks maintain plasticity.
+ The experiments were conducted on benchmark datasets under various continual learning scenarios.

### Weaknesses
 + Although they compare the proposed method with ReLU-based architectures, it could include comparisons with other advanced techniques in continual learning to validate the advantages further.
+ There is limited discussion on the computational and memory costs associated with the model compared to standard activation functions.
+ The authors claim that the proposed method focuses on the loss of plasticity, however, there seems to be something confusing about the experiments on label noise and pixel permutations (especially label noise).
+ The manuscript could benefit from more discussion of the overfitting problem.
+ The manuscript could benefit from more practical insights or guidelines for implementing deep Fourier features.
+ More continual learning methods related to plasticity should be included, like

[1] Architecture matters in continual learning 

[2] Revisiting Neural Networks for Continual Learning: An Architectural Perspective

### Questions
plz see Weaknesses.

### Soundness
4

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
4

### Summary
This manuscript targets continual learning and the phenomenon of loss of plasticity. The authors propose a theoretical analysis to solve this issue, thereby proposing deep Fourier features that employ sin and cos as activation functions.

### Strengths
I find that the manuscript is well-written, including motivation, problem statement, and theoretical analysis. The underlying theory is quite solid and sufficiently described with mathematical details in the appendix.

The use of sin and cos looks plausible to me. Indeed, sigmoid activation function is known to exibit vanishing gradient problem. However, when using sin and cos simultaneously, at least one of the two functions would exhibit an alive gradient. In consideration of this issue, the combination of sin and cos would provide much stable behavior compared with the use of a single one.

### Weaknesses
Nevertheless, the most critical issue for this manuscript is the small-scale experiments. Nowadays, experiments on MNIST/CIFAR/tiny-ImageNet with ResNet-18 are too weak to validate the proposed methods. They have only small scale sizes, which is quite deviated from the practical scenario. I believe that the ICLR paper should have a technical bar at least for ImageNet experiments. Note that experiments with ImageNet would require a large number of GPUs and training time (2~3 days per training). I found that you mentioned limited GPU sources, which may be inappropriate to conduct ImageNet experiments. Although my comment may be unfair for your experimental environment, conducting extensive validation with sufficient datasets is critical in our research field, so please understand my concern. Readers want credibility.

### Questions
See the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the loss of plasticity in commonly faced by deep neural networks in continual learning settings: As the training data continues to shift, eventually most deep networks start to lose their ability to adapt to the new distributions. The authors observe empirically and provide theoretical analysis showing that deep linear networks do not suffer this same problem. However, deep linear networks do not have the same representation power as nonlinear ones, so the authors instead propose imbuing nonlinear networks with more linear characteristics through deep Fourier features. The paper goes on to explain why alternative activation functions fail to embed a similarly linear network, and empirically demonstrate how deep Fourier features are able to preserve model trainability in two continual learning settings (Diminishing Label Noise, a variant of Class-Incremental Learning), for CIFAR-10, CIFAR-100, and tiny-ImageNet.

### Strengths
S1. A well-motivated, principled perspective: I’ve been reading (and reviewing) papers on continual learning for 7 years now, and most of the papers I’ve seen after the first papers that established the popular continual learning paradigms (e.g. replay, regularization, parameter isolation/expansion) have continued to fall into those buckets. Generally, many of the submissions I see are hacky and heuristics driven, consisting of various remixes of previously explored ideas. I thus found this paper to be a breath of fresh air, examining some of the problems of continual learning from a more theoretical perspective, building upon past works on plasticity, activations functions, Fourier features, and more to examine what exactly about nonlinear deep networks leads to lower plasticity for future tasks, as well as how to mitigate. I want to see more papers trying to solve continual learning from this kind of approach.

S2. Insights on plasticity: Continual learning papers tend to focus on the catastrophic forgetting problem, forgetting that being able to continually learn is also part of the problem. This paper doesn’t originate the observation of the loss of trainability in nonlinear deep networks (previous works cited), so it shouldn’t be attributed to the authors, but I would like to see more activity from the continual learning on this topic. I feel this paper could make a good contribution in this sense.

S3. Connections with other common activations: I appreciate the framing of other common activation types like ReLU and leaky ReLU from the perspective of this paper’s analysis (especially lines 361-369). These were helpful for understanding why these standard practices might lose trainability, and why the proposed Fourier feature approach might succeed.

S4. Writing: The paper is written very clearly and are organized well. The small empirical experiments in Figures 2 and 4 very compactly provides good empirical evidence of trainability over long task sequences for linear and non-linear models. Thanks for including.

### Weaknesses
W1. What about catastrophic forgetting?/Why not re-init?: A discussion about catastrophic forgetting--the most prominent challenge of continual learning--is largely absent from the paper. To be fair, trainability/plasticity is also often absent from papers focusing on catastrophic forgetting, and it’s good to have a deeper exploration on trainability given the lesser attention to it. However, I still feel a discussion and empirical investigation of deep Fourier features response catastrophic forgetting behavior is necessary; focusing on just trainability doesn’t make much sense to me, because if trainability is a major problem, then worst case a model can just be re-initialized and retrained from scratch. See Q4.  If the problem can be solved by just re-initialization, then the contribution here is interesting but not practical. This is currently my biggest concern.

W2. Strong Assumptions: While I understand that strong assumptions are commonplace in many theoretical treatments of deep learning, the restrictiveness of some of the assumptions here still are worth calling out. In particular, Theorem 2 assumes a deep diagonal linear network. Despite the cited precedents for such an assumption, this is pretty far from the reality of my deep networks in practice. How much do these insights shed here transfer to the more general deep linear network setting? 

W3. Double width vs half representation: The proposed method involves concatenating sin(z) and cos(z). This either involves double the width of the network (increases parameters and computation time) or halves the effective width (reduced model capacity). For a fixed size head-to-head comparison then, models parameterized this way may be at a sizable disadvantage. The experiments however are fair in this regard however, as they choose to incur the half effective penalty rather than unfairly double model width.

W4. Page Length: The page limit of ICLR now permits papers up to 10 pages, but 9 pages is highly encouraged; the recommendation for using the tenth page is more for including larger and more detailed figures. This paper extends past 9.5 pages, but I personally do not feel the visual content justifies going over the 9-page recommendation. I would recommend the authors try to get down to 9 pages (e.g. moving more content to the Appendix), or else for fairness reasons I believe this paper should be evaluated at a higher bar.

Miscellaneous:
- Figure 3: Having a graph inset in another like is non-standard and can be a little confusing. It seems like this may be better suited as two separate subplots.
- Linear 273: “function” => “functions”
- Line 419: Class incremental learning definition: This is not the traditional class incremental learning setup usually shown in most continual learning papers. Notably, it seems like addressing catastrophic forgetting is completely optional, as new tasks still contain the classes from the previous tasks. I would suggest naming this something else to distinguish it from the more common (and harder) setting.
- Line 465: extra space before footnote
- Figure 6 (right) caption: It doesn’t appear that deep Fourier features “substantially improve over most baselines”. In fact, they seem pretty middle of the pack?

### Questions
Q1: Line 117: “The problem setting that we consider is continual supervised learning without task boundaries.” The description that follows sounds like there are task boundaries every $T$ iterations? Is the “without” a typo?

Q2: Figure 4: Any reason not to also include plain ReLU in this figure? I presume it does badly.

Q3: Figure 5: Deep Fourier features have a very stark advantage over the other approaches for tiny-ImageNet, but the sizable gap disappears on less complex datasets like CIFAR 10 and 100. This happens in Figure 6 too. Why do you suspect this is?

Q4: In both the experimental settings, it doesn’t seem like any sort of remembering of past tasks is necessary. For diminishing noise, the label space remains the same, and the new data distributions just contain better information; for the class-incremental setting, the new data distributions contain all past distributions as a subset. What about just re-initializing the model and training from scratch? It would be good to have this naïve baseline also plotted in Figure 5 + 6.

### Soundness
3

### Presentation
4

### Contribution
3
