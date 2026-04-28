# Characteristic Function-Based Regularization for Probability Function Informed Neural Networks

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 5, 1, 3

## Abstract
Regularization is essential in neural network training to prevent overfitting and improve generalization. In this paper, we propose a novel regularization technique that leverages decomposable distribution and central limit theory assumptions by exploiting the properties of characteristic functions. We first define Probability Function Informed Neural Networks as a class of universal function approximators capable of embedding the knowledge of some probabilistic rules constructed over a given dataset into the learning process (a similar concept to Physics-informed neural networks (PINNs), if the reader is familiar with those). We then enforce a regularization framework over this network, aiming to impose structural constraints on the network’s weights to promote greater generalizability in the given probabilistic setting. Rather than replacing traditional regularization methods such as L2 or dropout, our approach is intended to supplement this and other similar classes of neural network architectures by providing instead a contextual delta of generalization. We demonstrate that integrating this method into such architectures helps improve performance on benchmark supervised classification datasets, by preserving essential distributional properties to mitigate the risk of overfitting. This characteristic function-based regularization offers a new perspective for enhancing distribution-aware learning in machine learning models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a characteristic function-based regularization method for contextual regularization. They compute the characteristic function for a linear combination of Bernoulli random variables and discretize it for use as a regularization term. They empirically evaluate the proposed regularization approach compared to existing baselines across 5 different classification datasets. Their results demonstrate that integrating this method improves performance on the considered benchmark supervised classification tasks.

### Strengths
This paper investigates a novel regularization technique based on characteristic functions of datapoints, getting motivation from physics-informed neural networks.

### Weaknesses
 - Some contents of the paper is unnecessary, which greatly diminishes the quality of the paper (e.g., extensive description of MNIST, and classification problem (Sections 2.1-2.2), informal proof sketches of Proposition 2-5 which are not proposed by the paper but already well-known)
- Gains achieved by the method are weak. The authors state "It is generally observed that the mean for the regularization we proposed, throughout 4 out of 5 datasets, achieve the highest mean". However, as shown in Table 1, for those 4 out of 5 datasets, the performance of their method often times just match or is only slightly better (~0.0001) compared to no regularization at all (None column). The reported gains are not practically significant, and the method's performance is inconsistent across datasets. The marginal improvements do not justify the added complexity of the proposed regularization technique.

### Questions
NA

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
3

### Summary
The authors propose a novel form of regularization which regularizes the model output probabilities towards that of a characteristic function defined over a sum of Bernoulli random variables.

### Strengths
- The idea is novel and provides a new route of regularization which has not been considered before. 
- The presentation and derivation is clear, and well done.

### Weaknesses
 - The overall motivation of using characteristic function regularization is not clear. Specifically, while the authors propose regularizing towards a characteristic function of a sum of Bernoulli random variables, the connection to improved generalization is not established. It's unclear why this specific target characteristic function is chosen over others, or how it relates to the underlying data distribution or model architecture. The paper lacks a clear explanation of the theoretical benefits of this approach.
- The abstract states “improves performance … by preserving essential distributional properties…” -> How does the preservation of such properties aid in generalization? The link between preserving distributional properties via characteristic function regularization and improved generalization is not clearly articulated. It's not evident how constraining the output distribution to resemble that of a sum of Bernoulli random variables leads to better performance on unseen data. A more detailed explanation of the theoretical underpinnings is needed.
- The abstract states that the method is meant to be used in conjunction with existing regularization methods. Were the results presented results utilizing multiple forms of regularization (such as $L_2 + \psi_2$) or were the only singular forms of regularization? The paper does not clearly specify whether the reported results are based on the proposed regularization method in isolation or in combination with other regularization techniques like L2 regularization. This makes it difficult to assess the true contribution of the proposed method and its interaction with other common regularization strategies.
- In the conclusion, the author state the follwoing: “integrating these techniques can offer a probability theory based perspective on model architecture construction which allows assembling relevant regularization mechanisms.” —> I do not see how this can be done after reading the work. can you give a concrete example of how the results presented in this work may give any insight into model architecture construction? The conclusion suggests a link between the proposed regularization and model architecture design, but this connection is not substantiated by the presented results or discussion. The paper does not provide any concrete examples or guidance on how the characteristic function regularization can inform the design of neural network architectures.

### Questions
Questions are covered above in the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper proposes to incorporate probability rules into the neural network architectures, more specifically the central limit theorem. They use a linear model on MNIST as an example and propose to regularize the distance between the characteristic function of the data distribution and the normal distribution.

### Strengths
Incorporating probability rules into the neural network architectures is a good idea. The classification task in machine learning is essentially learning a prediction rule $\mathbb{P}(Y|X)$. Incorporating probability rules into the model may facilitate the learning of this prediction rule.

### Weaknesses
- The described model in Sec 2 looks like just neural networks used in common practice. I don't see any novel architecture here.
- The authors assume the data follows a linear combination of Bernoulli distributions. This does not make sense for practical data. For example, the MNIST data, which is given as an example in Sec 2, is continuous data in $[0, 1]$ and is not Bernoulli. Or does the authors mean to assume the output of the model is Bernoulli?
- In line 315, the authors claim "for a general class of PFINNs, one only needs to adjust the modeling of the random variable presented in Definition 3 to reformulate the equation in Proposition 1 accordingly." However, for data in practice, it is hard to compute its characteristic function as we do not know its true distribution and the distribution is what the model is trying to learn in some sense. This makes the proposed regularization method invalid. Even if we can compute the characteristic function of data distribution, the regularization is not a function of weight parameters. How do you update the parameters through the regularization?
- The writing is not professional. The paper spends a lot of space introducing the setup of the model and MNIST dataset. The dataset and network architecture are quite common and can be introduced briefly. For example, the dataset can be represented generally as $\{x_i, y_i \}_{i=1}^N$. Some sentences are not professional in scientific writing, such as, "To explore the existence of PFINNs as (neuro)symbolic AI and as hybrid systems would require significantly more than 9 pages in a manuscript. (line 052)" and "Maybe other potential questions may merit consideration? (line 171)". I would suggest the authors read some high-quality papers and learn their writing styles.

### Questions
- What data distribution assumption is used in the experiment to implement the proposed regularization?
- Where is the assumption 1 used in the paper?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes regularization via the characteristic function of datapoints to train networks, similar to physics-informed neural networks. 

They derive the characteristic function for a linear combination of Bernoulli random variables, and discretize this function to use as regularization.

The perform experiments on a flattened version of MNIST with a linear model with a softmax activation.

### Strengths
Proposes a new approach to perform regularization via a discretized version of the characteristic function

### Weaknesses
I believe that a large amount of the content in this paper is unnecessary background. For instance, much of section 2 focuses on introducing the dataset of MNIST and the setting of a classification problem – all of which are standard and used in the field. 

For section 5, the informal proof sketches are describing results that are not all that relevant to the paper and some of which are already known facts. For instance, it is already known that the set of reals are complete. Most of these propositions are not new and follow the content in (https://www.lix.polytechnique.fr/~bournez/load/MPRI/Cours-2024-MPRI-partie-I-goodMPRI.pdf)

In the experiments, the authors fix $\lambda$ to 0.01 for all methods, while I believe that this should be tuned for each method individually on held-out validation data. 

Furthermore, I have some reservations about the authors' empirical results. There seems to be almost no difference between regularizing with $\psi_{\inf}$ and standard training without any regularization. While the authors claim the best mean performance across 4 of the 5 tasks, this roughly equivalent performance with standard training without any regularization makes up 3 of those best-performing tasks. Thus, it’s unclear if this regularization is beneficial in general and just is essentially not performing any regularization.

### Questions
How is the characteristic function related to the motivations in section 3 (specifically with regards to the infinite series of inquiries about the input image)?

### Soundness
2

### Presentation
2

### Contribution
2
