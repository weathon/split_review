# Can we get the best of both Binary Neural Networks and Spiking Neural Networks for Efficient Computer Vision?

- Decision: Accept
- Scores: 6, 6, 5

## Abstract
Binary Neural networks (BNN) have emerged as an attractive computing paradigm for a wide range of low-power vision tasks. However, state-of-the-art (SOTA) BNNs do not yield any sparsity, and induce a significant number of non-binary operations. On the other hand, activation sparsity can be provided by spiking neural networks (SNN), that too have gained significant traction in recent times. Thanks to this sparsity, SNNs when implemented on neuromorphic hardware, have the potential to be significantly more power-efficient compared to traditional artifical neural networks (ANN). However, SNNs incur multiple time steps to achieve close to SOTA accuracy. Ironically, this increases latency and energy---costs that SNNs were proposed to reduce---and presents itself as a major hurdle in realizing SNNs’ theoretical gains in practice. This raises an intriguing question: *Can we obtain SNN-like sparsity and BNN-like accuracy and enjoy the energy-efficiency benefits of both?* To answer this question, in this paper, we present a training framework for sparse binary activation neural networks (BANN) using a novel variant of the Hoyer regularizer. We estimate the threshold of each BANN layer as the Hoyer extremum of a clipped version of its activation map, where the clipping value is trained using gradient descent with our Hoyer regularizer. 
This approach shifts the activation values away from the threshold, thereby mitigating the effect of noise that can otherwise degrade the BANN accuracy. Our approach outperforms existing BNNs, SNNs, and adder neural networks (that also avoid energy-expensive multiplication operations similar to BNNs and SNNs) in terms of the accuracy-FLOPs trade-off for complex image recognition tasks. Downstream experiments on object detection further demonstrate the efficacy of our approach. Lastly, we demonstrate the portability of our approach to SNNs with multiple time steps. Codes are publicly available [here](https://github.com/godatta/Ultra-Low-Latency-SNN).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a new training method for binary activation neural networks. This method employs the Hoyer regularizer to each BANN layer to shift the activation values away from the threshold. As a result, the proposed BANN model can achieve better accuracy than other methods.

### Strengths
* The proposed method can improve the accuracy of both BANN and SNN models
* Experiments show the energy efficiency comparisons to demonstrate the effectiveness of this method

### Weaknesses
 * The proposed method is not closely related to SNN, and it mainly focuses on the BANN. This method can be used in SNNs for better model accuracy, but it can not bridge the gap between BNN and SNN as the title said. It would be preferable to discuss more about the relationship between BNN, SNN, and the proposed method to illustrate how this method bridges BNN and SNN.
* The energy evaluation method in the experiments is inaccurate. Usually, memory accesses take a large proportion of energy consumption. However, in the experiments, it only estimates the computed energy. It is better to consider the energy of memory access as well.



### Questions
* In section 2.2, “Note that this model is similar to leaky-integrate-and-fire (LIF) model”. This is not very direct. Why they are similar? In this model, there is no membrane potential, which is important in LIF.
* Typo: in section 4, Accuracy Comparison with SNNs, “Table 7” should be “Table 2”

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The presented method trains binary neural networks with the goal of sparse activations. The is achieved by borrowing concept from SNN training that use a threshold function in the neuron model to generate output spikes. In this method, the threshold value is determined for each layer using the Hoyer extremum. The method was tested on CIFAR-10 and ImageNet datasets and achieved superior accuracy and energy efficiency.

### Strengths
BNNs can certainly benefit from sparsity, just as SNNs do. Hence, the approach to transfer the SNN thresholding concept to BNNs with binary activations 0 and 1 is promising. With the right hardware, operations can be saved. The effect of sparsity becomes clear when compared with BNNs that use binary weights. The proposed method seems more energy efficient despite using floating-point weights.
The activations achieve a high sparsity. And by using the Hoyer regularisation during training, activations are resistant to noise and achieve higher accuracy than most SNNs, especially ones with only 1 time step.

### Weaknesses
The experiments executed in this paper are generally insightful. It is especially interesting to compare with both BNNs and SNNs. However, some evaluations are lacking detail. The energy consumption is estimated using power numbers of a paper from 2014 at an outdated technology node. Real values obtained from logic synthesis will be significantly different. Additionally, sparse operation induces overhead, such as checking if an activation is actually zero. Those factors are not accounted for in the estimations. Since there was an FPGA simulation done to evaluate the effect of quantisation, I would like to see a power estimation using this FPGA simulator. Alternatively, a GPU evaluation of the actual power consumption is interesting, since it is stated that the BNN operations are compatible with “existing hardware (standard GPUs)”.

For comparison of the energy consumption between SNNs and the proposed method, sparsity is used as a proxy. However, it is not clear how the sparsity numbers in Figure 3 were obtained except that they “represent existing low-latency SNN works”. Were those numbers given by the references or was it a replicated implementation by the authors?

More emphasis could be placed on the comparison with BNNs. It is stated that SOTA BNNs use network modifications that increase FLOPS but also expressivity. To which extend does calculating the Hoyer extremum during inference incur additional FLOPS? The power estimation in Equation 9 only accounts for one additional comparison.

Important parameters such as λ are not provided. At the same time, it was not indicated that training code and trained models will be provided. That means it is currently difficult to validate the results of this paper and derive further research. I would see open sourcing as a requirement of acceptance.

The formatting of the references in the text makes the paper very hard and slow to read. Figure 2 was prominently placed in the manuscript but never mentioned or further explained in the text.

### Questions
During inference, the Hoyer extremum is used to do the binarisation of the activations. How does is affect the number of FLOPS in Equation 9? How can the Hoyer extremum be reduced to a simple comparison to make the inference match the equation?

Could you take some actual energy measurements using your already existing FPGA simulator? It would also be interesting to see SNN’s energy consumption on hardware. This way, we do not need to rely on outdated energy numbers from 2014 and also account for the overhead induced by the sparsity.

Why is the ImageNet energy lower than that for CIFAR-10 in Table 4? Could you elaborate how you arrived at those numbers?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a spiking neural network-based training scheme that eliminates the iterative time step down to 1 while keeping the uni-polar activation scheme (0 and 1). The proposed algorithm is mainly constructed based on a layer-wise learnable threshold trained by the Hoyer regularization. The proposed method achieves comparable accuracy as the prior BNN work on both the CIFAR and ImageNet datasets.

### Strengths
The major contribution of the proposed method is reducing the multi-step, iterative spiking process down to one. I agree with the argument that increasing the number of 1s in the output spike can improve the activity of the training process (weight update) and convergence.

Regarding the performance of the proposed method, reporting the accuracy of the classification and object detection datasets is acceptable.

It is helpful that the author can provide some theoretical insights and proofs.

### Weaknesses
 **W1:** Most of the binary neural network research binarizes the weights weights as well. However, this paper does not report the weight precision and compares the precision scheme with BNN in a comprehensive manner.

**W2:** The performance comparison against SNN is not comprehensive enough. E.g., The recent TET [R1], DSpike [R2], and DSR [R3] are excluded from Table 2.

**W3:** The proposed method shows worse performance on ResNet-50 than VGG-16, which is controversial with the full-precision model performance, why is that?

**W4:** The proposed method incorporates the learnable potential threshold, I think it is important to report the evolvement of the threshold value during the training process, especially the training stability of the threshold value.

**W5:** Although the static image-based classification datasets (e.g., ImageNet) are good indicators of model performance, it is also important to evaluate the performance of SNN with DVS datasets due to the property of spatial-temporal events (e.g., DVS-CIFAR10, N-CalTech101, IBM-Gesture).

### Questions
Please refer to Weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
