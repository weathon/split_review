# Optimizing Layerwise Polynomial Approximation for Efficient Private Inference on Fully Homomorphically Encryption: A Dynamic Programming Approach

- Decision: Reject
- Scores: 5, 3, 5, 5

## Abstract
Recent research has explored the implementation of privacy-preserving deep neural networks solely using fully homomorphic encryption. However, its practicality has been limited because of prolonged inference times. When using a pre-trained model without retraining, a major factor contributing to these prolonged inference times is the high-degree polynomial approximation of activation functions such as the ReLU function. The high-degree approximation consumes a substantial amount of homomorphic computational resources, resulting in slower inference. Unlike the previous works approximating activation functions uniformly and conservatively, this paper presents a \emph{layerwise} degree optimization of activation functions to aggressively reduce the inference time while maintaining classification accuracy by taking into account the characteristics of each layer. Instead of the minimax approximation commonly used in state-of-the-art private inference models, we employ the weighted least squares approximation method with the input distributions of activation functions. Then we obtain the layerwise optimized degrees for activation functions through the \emph{dynamic programming} algorithm considering how each layer's approximation error affects the classification accuracy of the deep neural network. Furthermore, we propose modulating the ciphertext moduli-chain layerwise to reduce the inference time. By these proposed layerwise optimization, we can reduce inference times for the ResNet-20 model and the ResNet-32 model by 3.44 times and 3.16 times, respectively, in comparison to the prior implementations employing uniform degree polynomials and a consistent ciphertext modulus.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper makes two main contributions to reduce the inference latency of deep convolutional neural networks (CNNs such as ResNet-20/32) when the input data is encrypted using a fully homomorphic encryption (FHE) scheme (RNS-CKKS).

1) Assuming that the input distribution to the ReLU activation function is a normal distribution, it has been claimed that optimizing the mean squared error (MSE) of the polynomial approximation is better than the conventional minimax approach (which assumes uniform distribution). This has been achieved by tying it to minimizing the variance of the loss function.

2) A dynamic-programming based method has been proposed to determine "optimal" polynomial degree in each layer of a neural network. Based on this optimization approach, it have been shown that the inference latency can be reduced 3-4x compared to the baseline.

### Strengths
The paper address an important problem in the field of private inference and the proposed solution appears to be based on solid principles, provided that the stated assumptions are true.

### Weaknesses
1) Two key claims in the paper have been stated without any strong validation.

a) Firstly, what is the guarantee that the input to the ReLU activation layer will always follow a normal distribution? Is this true for every layer of the neural network? What happens if this assumption does not hold? The paper needs to provide empirical evidence or theoretical justification for this claim, especially considering that the distribution of activations can change significantly across different layers and network architectures. It's not sufficient to simply assume normality without demonstrating its validity in the specific context of the experiments.

b) More importantly, why is the "variance of the loss" a good surrogate for the classification accuracy? The challenge in encrypted domain inference is not sensitivity to small approximation errors. Contrarily, even a single large (unbounded) approximation error can screw up the entire inference process (as observed in the bit-flip attack on machine learning models). This is reason we need some bound on the approximation error (leading to the minimax formulation). The paper needs to rigorously justify why minimizing the variance of the loss is a suitable objective, especially given the sensitivity of FHE-based inference to large errors. The connection to classification accuracy needs to be made explicit, not just implied.

2) It is well-established in the literature on MPC-based private inference that not all ReLUs are equally important in the inference process. For example, see Peng et al., "AutoReP: Automatic ReLU Replacement for Fast Private Network Inference", ICCV 2023 and the references therin. In fact, the literature on MPC-based private inference does not stop layer-wise and tries to find exactly which particular neuron requires more accurate approximation. 

a) It is important to acknowledge the progress made on ReLU reduction in the field of MPC-based private inference because it is directly relevant to the problem considered in this work. The paper should discuss how their approach compares to existing methods that selectively approximate ReLUs, rather than treating all ReLUs uniformly within a layer.
 
b) Can the proposed dynamic programming approach be scaled one step further to find the optimal polynomial degree for each specific neuron? The current approach optimizes polynomial degree per layer, but it's unclear if further gains could be achieved by optimizing at the neuron level.

3) The results indicate that there is orders of magnitude decrease in the max. polynomial degree (see Table 3), which is surprising not reflected in the max. depth as well as the overall inference time. There should be a more in-depth analysis of how the max. polynomial degree impacts the inference time because that forms the core motivation for this work. The paper should provide a detailed breakdown of the computational cost associated with different polynomial degrees and depths, and explain why the observed reduction in polynomial degree does not translate to a proportional reduction in inference time. A more granular analysis of the impact of polynomial degree on the overall inference latency is needed.

### Questions
Please see weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a novel approach to enable private inference by using only Homomorphic Encryption (HE), without the need for retraining or model redesign.  The authors achieve this by replacing ReLUs with polynomial functions. They employ dynamic programming techniques and leverage layer-specific characteristics to adaptively select polynomial degrees for different layers in a pre-trained model.

### Strengths
1.  Authors exploited the layer-specific characteristics to significantly reduce the degree of polynomials for HE-only PI. 

2. The proposed approach does not require any redesigning or fine-tuning of the model, which often helps recover the accuracy. 


3. Methods are very well presented in the paper.

### Weaknesses
$ullet$ **Complexity and scalability of the proposed approach:** An essential concern regarding the presented solution lies in its complexity, an aspect left unexplored in the paper. Given that the method determines the appropriate polynomial degree for each layer, its computational complexity varies depending on the network's depth. This adaptability makes it increasingly impractical for deeper networks, such as ResNet101 and ResNet152. In contrast, the complexity of PI-specific manual ReLU pruning depends solely on the number of stages within the networks and remains independent of the total number of layers.

Additionally, the authors must have included a comparative analysis of their approach's complexity with previous methods that involve retraining, with a focus on absolute time, to demonstrate the advantages of their method, which eliminates the need for retraining.

$ullet$ **Lack of comprehensive empirical evaluation:**  The experimental evaluation in the paper is limited to CIFAR-10 using ResNet20 and ResNet32 networks. As per the standard practice in PI [1, 2, 3], an evaluation on CIFAR-100 and TinyImageNet datasets with networks such as ResNet18 should have been included to validate the effectiveness of the proposed solution on complex datasets. 


$ullet$ **Comparison with prior work:** To demonstrate the superiority of the HE-only solution over a hybrid approach (HE + MPC) [1, 2, 3],  a comparative analysis of the end-to-end PI runtime is required. Also, a discussion on low-degree polynomial substitution should have been included, which has been shown to be effective even on complex datasets such as [4]. 


**In conclusion,** I question the practicality of using higher-degree polynomials, especially considering their need for extensive bootstrapping when compared to the hybrid approach (HE/VOLE for linear layers and GC/OT for ReLUs). Additionally, this paper doesn't offer any new insights to enhance the feasibility of PI.

### Questions
Given that Table 1 indicates the need for a high-degree polynomial in the initial layer, is it possible to solely utilize the identity connection in these layers? Previous research on PI-specific ReLU optimization has shown that the initial ReLUs are not critical and can be eliminated without significant performance degradation. Is this applicable here?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
1. The paper proposes a layerwise degree optimization method for activation functions in fully homomorphic encryption (FHE) to reduce inference time while maintaining classification accuracy. 
2. The previous approaches approximated activation functions uniformly, but this work takes into account the unique characteristics of each layer. 
3. The simulations were performed using the Lattigo library on a high-performance computing system.

### Strengths
1. The author target the polynomial approximation problem for private Inference acceleration, which is a necessary and essential part for FHE-based private inference.
2. The authors employ the weighted least squares approximation method and optimize the degrees of activation functions using a dynamic programming algorithm. 
3. They also propose modulating the ciphertext moduli-chain layerwise to further reduce inference time. 
4.Experimental results on the CIFAR-10 dataset using the ResNet model show that the proposed method significantly reduces inference times compared to previous approaches.

### Weaknesses
 1. I just have one major concern. There exist some work use 2-degree polynomial approximation [1,2] with ignorable accuracy loss. How does the proposed method compared to other advanced low-degree polynomial approximation techniques? As a low-degree polynomial approximation would outperforms the results in this work.



### Questions
See Weakness part.

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a layer-wise approximation of activations to reduce the FHE-based secure inference time. By considering the characteristics of each layer, the proposed layer-wise approximation does not require re-training while maintaining the model performance (e.g., accuracy). In terms of polynomials approximations, this paper employs the weighted least squares approximation method with the input distribution to approximate the activation function and utilizes a dynamic programming algorithm to reduce the approximation polynomials’ degrees. In terms of the FHE ciphertext evaluation, the authors propose modulating the ciphertext moduli-chain layer-wise to reduce the inference time. Compared to prior works, this paper reduces the secure inference time by over 3 times on ResNet-20/ResNet-32 on dataset CIFAR-10 with negligible accuracy loss.

### Strengths
1. This paper studies the input distribution of the activation, uses the weighted least squares approximation method, and presents a dynamic programming algorithm designed to determine the optimal degree set for each layer. This algorithm efficiently obtains the optimal polynomial degrees, minimizing the overall negative impact on classification accuracy. The authors give a detailed mathematical analysis of the polynomial approximation method and dynamic programming design.
2. The authors propose a moduli-chain management method to achieve additional reductions in inference runtime. This method focuses on removing unused moduli. Instead of using a single moduli chain, the authors propose to use multiple moduli chains for each depth of the activation approximation polynomial function. In this way, this paper can reduce the number of bootstrapping operations.

### Weaknesses
1. The authors only evaluate the proposed method on ReLU. However, other activation functions, e.g., Swish, Sigmoid, GeLU, are not evaluated.

2. Some visualization of (1) the ReLU function, (2) the proposed approximation, and (3) other baselines will be helpful to understand the effect of the proposed approximation.

3. The authors need to show the improvement introduced by each technique, including the weighted MSE over minimax, layerwise over uniform, dynamic programming over simple greedy, etc. Right now, when compared with Lee et al., 2022a, it seems most of the benefits come from minimizing the weighted MSE, which drastically reduces the polynomial order.

4. Only a simple dataset, i.e., Cifar-10, is demonstrated. Larger datasets are important as they may impact the distribution of the activation functions as well as the required approximation accuracy.

### Questions
Please refer to the weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
