# Connected Hidden Neurons (CHNNet): An Artificial Neural Network for Rapid Convergence

- Decision: Reject
- Avg Score: 3.75
- Scores: 6, 3, 3, 3

## Abstract
Despite artificial neural networks being inspired by the functionalities of biological neural networks, unlike biological neural networks, conventional artificial neural networks are often structured hierarchically, which can impede the flow of information between neurons as the neurons in the same layer have no connections between them. Hence, we propose a more robust model of artificial neural networks where the hidden neurons, residing in the same hidden layer, are interconnected that leads to rapid convergence. With the experimental study of our proposed model in deep networks, we demonstrate that the model results in a noticeable increase in convergence rate compared to the conventional feed-forward neural network.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel FFNN architecture where neurons in hidden layers are "connected to themselves" (albeit without a non-linearity), as well as being connected to previous and future layers. The authors demonstrate that this architecture leads to faster convergence and better final performance on a set of MNIST tasks. They also acknowledged the potential comparison issue that self-connections result in more parameters, and performed another raft of experiments which normalized for parameter count between traditional and CHHNet architectures, and showed continued increased convergence for CHHNets even in that setting.

### Strengths
- The paper was straightforward in its proposal and the evidence for it, and was thus easy to engage with as an isolated idea 
- I appreciated the authors pre-empting the concern about parameter-count-parity; I think I would indeed have found these results less compelling in the absence of that experiment 
- I appreciated the ways the authors drew comparisons with and also distinctions from other self-loop architectures like RNNs

### Weaknesses
 - The limited number of datasets tested on strikes me as the primary experimental weakness of this paper: given the similarities between all of the MNIST and MNIST-adjacent datasets, it's a little hard to tell to what extent these results suggest a more general conclusion, vs just a property of training FFNNs on MNIST and similarly-structured datasets.
- I think the convergence speed proof could have done with a little more explanation to make the intuitions of the steps in the chain more clear

### Questions
- This is more a question than a suggestion, but given the central role MLPs are currently playing in modern transformer architectures, it would be interesting to see whether this approach leads to better performance/faster convergence in that setting (i.e. as a way to modify the parameterization of internal MLPs)

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a neural architecture that interconnects hidden neurons on the same hidden layer.
It also presents the learning laws for updating the weights using backpropagation.  
The central of this work is that the new architecture promotes rapid convergence.
It also presents a rapid convergence proof and some experimental results to support the claim.

### Strengths
The paper is well-organized

### Weaknesses
(1). It appears that the mathematical model for this new model reduces to the conventional feedforward network without intra-hidden layer connections.

 Equations (1) and (2) seem to suggest that  $H^{[l]}$ is a linear transformation of input $A{[l-1]}$. If you compose linear transformations, you get a linear transformation. Specifically, if you put equation (2) in equation(1), you will get a new linear transformation that is similar to using no intra-hidden layer connection.  The core issue is that the proposed intra-layer connections, when analyzed mathematically, do not introduce non-linearity or a fundamentally different transformation than a standard feedforward network. This raises concerns about the actual novelty and effectiveness of the proposed architecture.


(2). I think the experiments are insufficient:

The number of training epochs before convergence does not give the full picture. The claim of rapid convergence fails to account for the overhead per epoch due to the extra intra-layer computations. Also, I think the authors should compare this work with the use of skip connections. The experiments need to include a comparison of the computational cost per epoch, measured in time, to properly evaluate the claim of rapid convergence. Furthermore, the absence of a comparison with skip connections, which are known to improve training, makes it difficult to assess the true contribution of the proposed method.

### Questions
(1). Please can you provide more information on how this model architecture differs from the conventional feedforward network with an intra-connection layer?   Especially with the simplification of plugging equation (2) into equation (1)

(2). Can you provide more information about the compute time per epoch?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes what is claimed to be a more robust model of artificial neural networks where the hidden neurons, residing in the same hidden layer, are inter-connected thus leading to an increase in convergence, when compared to feed-forward neural networks.

This is an interesting idea, inspired by the lateral connections omnipresent in the neural systems of primates, and in fact responsible for the center-surround motif in the retina. However, the mathematical formulation of the recurrence thus occurring in the networks seems incorrect, and equivalent to a feed-forward neural network. In more detail, the proposed formulation for a layer l is as follows:

    A(l) = f(Z(l))  where  
        Z(l) =  W1(l) A(l-1) + W2(l) H(l) + B(l)   
        H(l) = W1(l) A(l-1) + B(l)

where A(l) is the output of layer l, f is the activation function, and H(l) are the horizontal connections (Equations 1-3, on Page 3). However, by replacing H(l) with its definition one obtains:

    Z(l) =  (W1(l) + W2(l) W1(l)) A(l-1) + W2(l) B(l) + B(l) 
          = W3(l) A(l-1) + B3(l)

Hence, the result is a classic feed forward computation unit of the form:

        A(l) = f(Z(l))  where 
            Z(l) = W3(l) A(l-1) + B3(l)

Hence, by trying to avoid the recursion inherent in the lateral inhibition network, by taking the "hidden output" to be what the unit would generate as output in the absence of horizontal connections, leads to a network that is in all respects equivalent to a feed-forward network.

It might be the case that this partitioning of the computation leads in some cases to a faster convergence, but in this case the authors have to make a better case for the way in which the mathematically correct recurrent formulation is replaced with a feed-forward variant.

### Strengths
This paper introduces an interesting idea, inspired by the lateral connections omnipresent in the neural systems of primates, and in fact responsible for the center-surround motif in the retina.

### Weaknesses
This paper proposes what is claimed to be a more robust model of artificial neural networks where the hidden neurons, residing in the same hidden layer, are inter-connected thus leading to an increase in convergence, when compared to feed-forward neural networks.

This is an interesting idea, inspired by the lateral connections omnipresent in the neural systems of primates, and in fact responsible for the center-surround motif in the retina. However, the mathematical formulation of the recurrence thus occurring in the networks seems incorrect, and equivalent to a feed-forward neural network. In more detail, the proposed formulation for a layer l is as follows:

    A(l) = f(Z(l))  where  
        Z(l) =  W1(l) A(l-1) + W2(l) H(l) + B(l)   
        H(l) = W1(l) A(l-1) + B(l)

where A(l) is the output of layer l, f is the activation function, and H(l) are the horizontal connections (Equations 1-3, on Page 3). However, by replacing H(l) with its definition one obtains:

    Z(l) =  (W1(l) + W2(l) W1(l)) A(l-1) + W2(l) B(l) + B(l) 
          = W3(l) A(l-1) + B3(l)

Hence, the result is a classic feed forward computation unit of the form:

        A(l) = f(Z(l))  where 
            Z(l) = W3(l) A(l-1) + B3(l)

Hence, by trying to avoid the recursion inherent in the lateral inhibition network, by taking the "hidden output" to be what the unit would generate as output in the absence of horizontal connections, leads to a network that is in all respects equivalent to a feed-forward network.

It might be the case that this partitioning of the computation leads in some cases to a faster convergence, but in this case the authors have to make a better case for the way in which the mathematically correct recurrent formulation is replaced with a feed-forward variant.

### Questions
Why have you avoided a recurrent formulation?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a novel MLP architecture where individual hidden neurons in a layer are densely interconnected. The authors derive the back propagation algorithm for the proposed architecture (in broad strokes), and show (theoretically) that the proposed model is expected to have steeper gradients, which the authors associate with faster convergence. Experiments are conducted on MNIST dataset variations, where the proposed model has a favourable training profile.

### Strengths
**Originality:** The paper proposes an MLP architecture with self- and neighbourhood-connections within a layer. According to the literature review done by the authors, this is the first instance of such an architecture being proposed. Authors do compare their model to classic RNNs, and I would have appreciated a deeper discussion on the parallels. Either way, I am convinced that the idea is novel.

**Quality:** The authors give some theoretical backing to the rapid convergence claims, which is appreciated.

**Clarity:** The paper is clearly written and very easy to follow.

**Significance:** I believe a broader benchmarking experiment is needed to determine the significance. However, it is nice to see a simple and elegant idea proposed.

### Weaknesses
 **Benchmarking experiments:** The authors have chosen MNIST and its variations for benchmarking. The choice seems very unobvious: these are image datasets, with lots of “redundant” inputs (e.g. pixels that are white for all digits). A fully-connected architecture should rather be applied to a selection of classification and regression tasks where at least some of the input variables are mutually independent. Why not take a random pick from: https://github.com/EpistasisLab/pmlb

**Hyperparameters:** It seems that the same learning rate was used for both the proposed architecture and the standard MLP. This seems inappropriate: log-likelihood (cross-entropy) loss yields higher gradients than the mean squared loss, as such one usually picks smaller learning rate value for cross-entropy. The comparison between architectures will only be fair if the hyperparameters are optimised separately for each, the proposed model and the MLP. Furthermore, the authors should explore a wider range of learning rates, and not just a single value, for both models to ensure a fair comparison across the entire hyperparameter space. The lack of individual hyperparameter tuning for each architecture casts doubt on the validity of the comparison.

 **Formatting:** The authors do not always adhere to correct formatting standards. A few grammatical mistakes are present in the paper. Please see below for the suggested list of corrections:

“disconnected from biological reality. (Akomolafe, 2013).” - please remove the full stop prior to the reference.

“model depicted a noticeable increase” - model exhibited

“While Hopfield use” - While Hopfield used

“UNet++(Zhou et al., 2018), “ - add a space in front of the bracket

“Though the forward propagation mechanism of the proposed model echoes the forward propagation mechanism of conventional RNNs, in conventional RNNs, the activations of the hidden neurons, obtained from the prior time step, are used to calculate the output of the hidden layer, whereas in CHNNet, the current pre-activations of the hidden neurons are used to calculate the output of the hidden layer.” - this sentence is too long, please break it up into three separate sentences.

“equation 3 and equation 4” - Equation (3) and Equation (4)

I suggest that the contributions are listed in present tense.

### Questions
*“the difference between the cost of CHNNet, generated at two sequential time steps, is greater than that of the conventional FNN; that is, CHNNet converges faster than the conventional FNN.”* — is this really a valid statement? From the loss landscape perspective, a higher difference in loss values implies “steeper” gradients. Whether or not that would lead to faster convergence is not easily answered, in my opinion. With very steep gradients one might experience higher oscillations and stronger sensitivity to the learning rate value. I think the authors should only state what they know for certain: that the proposed approach provably yields higher gradients (which may lead to faster convergence).

The p-values show that the difference in performance is not statistically significant for the proposed model and the MLP. What about convergence speed? Can that be quantified and statistically evaluated for significance? Also, what about runtime efficiency—in absolute terms, when the number of parameters is comparable, which architecture is quicker to train? Please evaluate/comment on this.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair
