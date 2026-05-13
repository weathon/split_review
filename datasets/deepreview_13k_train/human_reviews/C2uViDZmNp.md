# Information Subtraction: Learning Representations for Conditional Entropy

- Decision: Reject
- Scores: 3, 3, 5, 3

## Abstract
The representations of conditional entropy and conditional mutual information are significant in explaining the unique effects among variables. The previous works based on conditional contrastive sampling have successfully eliminated information about discrete sensitive variables, but have not yet addressed continuous cases. This paper introduces a framework of Information Subtraction capable of representing arbitrary information components between continuous variables. We implement a generative-based architecture that outputs such representations by simultaneously maximizing an information term and minimizing another. The results highlight the representations' ability to provide semantic features of conditional entropy. By subtracting sensitive and domain-specific information, our framework effectively enhances fair learning and domain generalization.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors introduce a framework for learning representations, aimed at applications in fair learning and domain generalization. 
The authors use powerful MINE-based estimators to learn representations that share minimal MI with given conditional variables.
Previous methods focused on discrete sensitive variables, while here the authors extend these approaches to continuous cases.

### Strengths
* The choice of MINE-based MI estimator to maximize/minimize MI terms is an excellent choice which allows the proposed method to scale to high-dimensional data.
* Extending previous work to include continuous variables is an important contribution.
* The proposed method might have potential for broad application due to the above points, and the fact that it is independent of the choice of architecture.

### Weaknesses
 * Line 168: “Based on our previous work (?)” - this is a strong hint to the identity of the authors which breaks the double-blind regime of the reviewing process.
* The novelty might be very limited here. Specifically, the use of MINE-based methods might be the major novelty here.
* There is no discussion about the failing points of the proposed method. What happened when the condition variable X and the target Y are entangled in more complex ways? How will the learned representation Z be affected? 
* The formulation and the presented Algorithm are not clear.

### Questions
* Did you try adding a hyper-parameter to one of the terms in the loss? Could that allow for finer control by the user on the learned representation?
* Did you have issues in training stability?
* Did you test the effectiveness of the proposed method on high dimensional data? How did the computational cost scale?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a framework called "Information Subtraction" for learning representation Z that maximizes conditional entropy H(Y|X) or, put in another way, maximizes the conditional mutual information (CMI) I(Z;Y|X). The method applies for continuous variables, which is harder than discrete variables. The proposed framework utilizes an approach similar to generative adversarial training where discriminators are used to maximize or minimize information terms. The authors evaluate the framework's performance on synthetic and real-world datasets, demonstrating its effectiveness in fair learning and domain generalization tasks.

### Strengths
The framework tackles a relatively under-explored and challenging problem of selectively maximizing and minimizing specific information components during representation learning. Previous works in the topic of CMI are more focusing on getting a good estimation, while this work is interested in leveraging CMI for representation learning.

### Weaknesses
 **Lack of background of CMI estimators**: Previous works on estimating (conditional) mutual information are not discussed. In particular, [1] proposes similar framework where discriminators are used for the estimation. It's also unclear to me how the proposed method differs from the existing approaches for estimating conditional mutual information, e.g. MI-Diff+f-MINE in [1]. Are there any significant technical difficulties for turning an estimator into a representation learner? Would the classifier-based approach advocated by [1] results in better representation?

**Lack of baselines and ablation studies**: the experiments, synthetic or real, don't compare to any other methods. It's, therefore, not obvious how the experimental result should be interpreted. The experimental section would also benefit from ablation studies to analyze the contribution of different components of the architecture and the impact of hyperparameter choices.

### Questions
1. Are there any difficulties or details that need to pay attention to make the training scheme work? MINE has been proved to be difficult to tune.
2. In the paper, the generator takes Y as the input, could X also be given in the input? Would that change the result?
3. Line 168, reference missing. Why is it called an expanded architecture?
4. For the synthetic experiments, does the proposed method learns a better representation than the baselines such as contrastive-based approach?
5. Does the proposed method perform better in the downstream task than other approaches for the fairness and domain invariant learning setting?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors introduce a framework for representing arbitrary information components between continuous variables using Information Subtraction. Essentially a generator network is trained to generate a latent representation $Z$ which captures the mutual entropy of target viable $Y$ and conditional variable $X$, without carrying information about $X$ itself. 
To achieve this, they use two discriminator networks $A$ and $B$. While $A$ estimates $I(Z,X;Y)$, $B$ estimates $I(Z;X)$. The Objective $I(Z,X;Y) - I(Z;X)$ is back propagated to the generator network.

The authors test their method on two synthetic scenarios and on fair learning and domain generalisation.

### Strengths
The paper is well written in general. The challenge being tackled is of interest for part of ICLR's audience. While maybe not novel – I am not an expert on the related work – the approach of using two discriminator networks to estimate $I(Z,X;Y)$ and $I(Z;X)$ seems reasonable to me.

### Weaknesses
 **Related Work Section**:

The authors write: "While we share similar architectures with these works, their structures are not designed for conditional representations." It is unclear to me how large the contribution of this paper is. Is the proposed architecture only a slight modification of existing work? Or would a slight modification of existing work suffice to reach the same goal as the authors propose? If so, why is there no comparison to those in the experimental section?

**Experimental Section**:

The section lacks comparability to prior work. As I understand it, it stands very much isolated and it's hard for me to estimate the significance of  the contribution the authors have made. If existing models cannot be applied for comparison, I'd still expect the authors to come up with other, simpler, baseline architectures against which to compare.

It is unclear to me whether the reported values come from train, validation or test splits. The lack of standard deviation (suggesting no cross validation was used) makes it hard to estimate the significance of the results. Additionally, the chosen "real-world" datasets seem very simple to me.

Overall, unfortunately, the experimental section does not convince me.

### Questions
The *Weaknesses* section outlines the questions and concerns I have.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces the Information Subtraction framework, which addresses conditional representation learning for continuous variables. It employs a generative architecture with a generator neural network and two discriminators to stabilize information term estimations. The generator's objective is to maximize information from one discriminator while minimizing it from the other, effectively capturing semantic features of conditional entropy and enhancing fair learning by removing sensitive information.
The authors highlight the significance of conditional representation learning and demonstrate the framework's capacity to decompose signals and produce unbiased representations. Experimental results show that the proposed approach improves fairness in both synthetic and real-world contexts and enhances domain generalization by combining domain-specific factors with universal representations.

### Strengths
The paper effectively outlines the problem from a methodological standpoint, framing it as a well-defined optimization issue that is clear from a mathematical perspective. It provides a comprehensive overview of related work and their limitations, emphasizing the necessity for a representation learning method that can eliminate information pertaining to continuous sensitive variables. The primary objective is to elucidate the unique effects among variables. Additionally, the inclusion of real-world experiments highlights the paper's contributions to the current research landscape in fair learning and domain generalization applications.

### Weaknesses
The article presents challenges in terms of readability, as the mathematical loss functions being minimized in practice are not adequately described. The discussion of the quantities to be optimized tends to remain at a high level. Specifically, the paper lacks a clear, step-by-step derivation of the loss functions, making it difficult to understand how the information subtraction framework is implemented. For example, while the paper mentions maximizing information from one discriminator and minimizing it from the other, the precise mathematical formulations for these objectives, including the specific forms of the discriminator losses and how they interact with the generator's loss, are not sufficiently detailed.

Additionally, the architecture description is introduced late in the paper and lacks detail; a more concrete schematic representation with specific input types (e.g., images, tabular data) and detailed analytical loss expressions would be beneficial. The current description does not provide sufficient clarity on how the generator and discriminators are structured, what their inputs and outputs are, and how they are connected. A more detailed explanation of the network architecture, including the number of layers, activation functions, and the specific loss functions used for each component, is needed to fully understand the proposed method. Furthermore, the paper does not specify how the architecture would adapt to different data modalities, such as images versus tabular data, which is a critical aspect for practical applications.

Moreover, the existing literature on debiasing appears to be quite extensive regarding the elimination of sensitive information from continuous variables [A], [B]. I found it difficult to discern how this work connects to those prior studies. The paper does not adequately discuss how the proposed method differs from or improves upon existing techniques for removing sensitive information from continuous variables. A more thorough comparison with methods like those in [A] and [B], including a discussion of their limitations and how the proposed framework addresses these limitations, is necessary to contextualize the contribution of this work. The lack of a clear comparison makes it difficult to assess the novelty and significance of the proposed method.

Finally, the experimental section seems relatively weak in terms of the number of experiments and datasets utilized. Including a straightforward debiasing or fair learning experiment in a real-world context, such as healthcare applications or scenarios involving ethnic biases, along with qualitative visual explanations, would enhance the overall quality of the article. The current experiments do not sufficiently demonstrate the practical utility of the proposed method in real-world scenarios. The inclusion of more diverse datasets and a more thorough evaluation, including qualitative analysis of the learned representations, would be beneficial.

### Questions
Is it necessary to assume that your inputs or latent representations follow a specific distribution (e.g., Gaussian, von Mises-Fisher) to derive your loss functions?

Additionally, the authors mention "Based on our previous work (?)" at one point. It is important to note that ICLR requires authors to cite their own work as they would cite others'. In this case, the authors should state: "Based on the previous work [x]." This would allow readers to locate and review the referenced paper.

### Soundness
2

### Presentation
1

### Contribution
2
