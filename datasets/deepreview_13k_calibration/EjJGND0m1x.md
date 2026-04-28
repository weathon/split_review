# MIND over Body: Adaptive Thinking using Dynamic Computation

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
While the human brain efficiently handles various computations with a limited number of neurons, traditional deep learning networks require a significant increase in parameters to improve performance.
  Yet, these parameters are used inefficiently as the networks employ the same amount of computation for inputs of the same size, regardless of the input's complexity.
  We address this inefficiency by introducing self-introspection capabilities to the network, enabling it to adjust the number of used parameters based on the internal representation of the task and adapt the computation time based on the task complexity.
  This enables the network to adaptively reuse parameters across tasks, dynamically adjusting the computational effort to match the complexity of the input.
  We demonstrate the effectiveness of this method on language modeling and computer vision tasks.
  Notably, our model surpasses much larger ResNet-50 and EfficientNet on ImageNet, achieving 96.62\% accuracy, and achieves a 95.8\% F1 score on the SQuAD dataset, all with just a three-layer network.
  These results showcase the potential for dynamic and reflective computation, contributing to the creation of intelligent systems that efficiently manage resources based on input data complexity.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
1) This paper introduces a new method to dynamically allocate network compute based on the difficulty of the inputs allowing early exits at inference time. The proposed method comprises of 2 networks - a) prediction network that outputs activations at each layer for a given input b) an introspection network that taken in the activations and decide which layers to pick for more intensive computation (using fixed point iterations) and which layers to leave as is.

2) Authors also describe a training procedure to jointly optimize the introspection and prediction networks. 

3) Experiments show that a much smaller model (in terms of param count) achieves better performance than considered baselines on language modeling and vision tasks.

### Strengths
The proposed method is generic and has been applied across modalities with sufficient ablations to prove that the proposed method work.

### Weaknesses
1) The paper doesn't contrast and compare to more recent early exit methods proposed  for language modeling tasks :
a) Confident Adaptive Language Modeling (https://arxiv.org/abs/2207.07061) 
b) LayerSkip: Enabling Early Exit Inference and Self-Speculative Decoding (https://arxiv.org/abs/2404.16710)


### Questions
1) Can you provide experiments comparing the proposed method to more recent early exit methods like CALM and LayerSkip ?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a Model INtrospection for a Dynamically adaptive model (MIND) which dynamically adjusts computation depending on the complexity of the input. It consists of two networks: the introspection network and the prediction network. The introspection network takes as input the activations from the different layers of the prediction network, and outputs a binary mask over the layers, determining the layers which require more computation through fixed point iterations. The authors demonstrate the effectiveness of the MIND model for vision tasks using a three layer CNN as the prediction network, outperforming much larger models like ResNet-50, and EfficientNet B7 on ImageNet and CIFAR-100 datasets. The authors also propose MIND-Transformer, with fixed point iterations in self attention and feedforward networks, demonstrating its superior performance on language modeling tasks, despite using fewer parameters than RoBERTa-base. The authors further demonstrate that MIND’s dynamic allocation of computational depth depending on the input complexity is more effective, both in terms of accuracy and efficiency (fewer parameters and FLOPs) over static compression techniques like pruning and quantization.

### Strengths
1. The authors propose a model, MIND which dynamically adjusts computation via fixed point iterations in its prediction network using an introspection network depending on the input complexity.
2. MIND model with a three layer CNN as the prediction network, outperforms much larger models like ResNet-50, and EfficientNet B7 on ImageNet and CIFAR-100 classification datasets.
3. The authors also demonstrate that MIND using LSTMs and Transformers in the prediction network achieves superior performance on language modelling tasks using fewer parameters. 
4. MIND’s dynamic allocation of computational depth results in higher accuracy using fewer parameters and FLOPs over static compression techniques like pruning and quantization.

### Weaknesses
1. It is not clear how the input complexity metric is incorporated into the introspection network's mechanism, and how this can be more generally quantifiable. Specifically, the paper does not detail how the three components of the input complexity metric (softmax confidence, entropy, and gradient norm) are combined and used to influence the introspection network's layer selection. The lack of clarity on the specific functional form and the weighting of these components makes it difficult to assess the robustness and generalizability of the approach.

2. The MIND model when used with prediction networks with many layers (as in the case of LLMs) will significantly increase the inference time as more layers with fixed point iterations are used. The paper does not adequately address the potential for increased computational overhead during inference, particularly when the introspection network selects multiple layers for fixed-point iterations. This could lead to a substantial increase in latency, especially for complex inputs that require multiple iterations across several layers, negating the benefits of dynamic computation in practical applications.

### Questions
1. What is m’ in line 147?
2. What is the rationale behind Equation 5 for MIND-Transformer?
3. How is $w_l$ in Equation 7 computed? Also, what is the need for a separate $m_{i,l}$ term in Eq 7?

4. Just to clarify in the toy random dot motion task the model needs to classify in one of the four possible directions and the direction of the shifted image denotes the ground truth?

5. Which dataset are the results for in Table 5?

6. What are the parameters of the introspection network, like how many layers are there in the MLP and what are the sizes of the hidden dimensions? 

7. From $p_{i,l}$ in Equation 8, how are the binary layer selection variables $m_{i,l}$ obtained?

8. Can the authors share more details about the different MIND variants, like how are fewer FPI layers decided, what is a simpler inspection network and how are the decisions of the introspection network fixed after training?

Minor - Line 127 typo, should be “prediction”

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces an approach targetted at computational efficiency in deep learning by adapting amount of computation to complexity of each input. Inspired by how human brain is considered to allocate resources dynamically. Two core components, (i) introspection network and (ii) prediction network.  Introspection network analyses intermediate activations from prediction network & figures out which layers require additional compute via fixed-point iterations )FPI) as well as what can proceed with standard forward pass.  Prediction net performs FPI until convergence or threshold of iterations reached. Leverages phantom gradients method for backprop through FPI; gradients approximated without unrolling / jabobian calc to limit compute-memory needs during training.

The paper is well written and easy to read + get the core idea across.

### Strengths
Computational efficiency; optimal use of resources allocating more for compelx inputs. Clever use of intermediate activations to assess input complexity. Should be able to work with existing architectures making engineering it for downstream real-world use cases simpler. Backprop with phantom gradients done in an interesting way. Mixed with use of statistical methods ~ should allow for generalisation. Considered overfitting issues within architectural design.

### Weaknesses
The idea is subtle and complex + introspection network needs more compute cost. Approach may not capture actual gradient landscape given the number of adjustments made & have to be considered. Strategy for arrving at thresholds / stopping criteria around convergence is not clear as such. Gradient flow calc is non-trivial given the overall architecture. The introspection network, while intended to improve efficiency, introduces additional computational overhead. The fixed-point iteration (FPI) process, while theoretically sound, may not always converge to a stable solution, especially with complex inputs. The reliance on phantom gradients for backpropagation, while computationally efficient, is an approximation and may not accurately reflect the true gradient landscape, potentially leading to suboptimal training. The lack of clarity around the convergence criteria and stopping thresholds for the FPI process raises concerns about the robustness and reliability of the approach. The interplay between the introspection network and the prediction network, particularly in terms of gradient flow, is complex and requires careful consideration to ensure effective training.

### Questions
Given the size of the appendix can you put in a full section to indicate the weaknesses (vs hinting at them in the future works/conclusion section)?
Is the trade-off in terms of gain for the complexity worth while?; how can this be known earlier before selecting this approach?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a framework for designing architectures that are able to adaptively control the number of computations they perform in order to produce an output given an input. Their proposal has two main components. First, separate the model into two parts: a prediction network and a control network. At each step, the latter decides which layers to use to refine it’s estimate of the output. To make computations even more granular, they use a Deep Equilibrium networks to implement each layer as a fixed-point iteration computation. Thus the control network can no only decide which layers to apply, but for how long. The authors proceed to show the effectiveness of their approach on several qualitatively different datasets.

### Strengths
1. The approach is well motivated and the problem of adapting the computations used by a model is an interesting one.
2. The authors lay out the approach in good detail, explaining how it diverges and improves from previous work.
3. They conduct extensive experiments to support their goal of improving upon previous approaches.

### Weaknesses
1. Some details on model architecture and metrics are missing.
2. Parts of the language used to describe the model are misleading and fall into unnecessary anthropomorphising.

3. It is not clear how the controller network determines the computation time of each layer. Specifically, are the parameters governing the number of fixed-point iterations learned, or are they fixed? If fixed, what is the criteria for choosing the number of iterations?
4. The complexity metric is described as “thorough” but it is not clear what makes it such. Or even what complexity means in this case. The description lacks a clear mathematical definition and justification.
5. CompCost is said to depend on the number of layers and iterations, but is this a sum or some other function? It is not clear how these two factors combine to produce the final cost. The text lacks a precise definition of the CompCost function.
6. I have an issue with the anthropomorphising the authors lean into.
    1.  There is no mention about any “body” in the text so the title is misleading. 
    2. The model doesn’t think, it processes. There is no “self-awareness”, at most it self-regulates. 
    3. And why call it “MIND”? It doesn’t even match the first letter of the name they themselves assign.
    4. The title could be “Adaptive Processing through Dynamic Computation Control” or something, which conveys a better feel about what the authors are doing.

### Questions
1. It is not clear from Figure 1 or maybe not detailed enough in the text how the controller network determines the computation time of each layer. In other words, how are the parameters determined? Or are they always fixed and it is just a choice between 1 pass or multiple (until covergence)?
2. The complexity metric is described as “thorough” but it is not clear what makes it such. Or even what complexity means in this case.
3. CompCost is said to depend on the number of layers and iterations, but is this a sum or some other function? Not clear from the text.
4. I have an issue with the anthropomorphising the authors lean into.
    1.  There is no mention about any “body” in the text so the title is misleading. 
    2. The model doesn’t think, it processes. There is no “self-awareness”, at most it self-regulates. 
    3. And why call it “MIND”? It doesn’t even match the first letter of the name they themselves assign.
    4. The title could be “Adaptive Processing through Dynamic Computation Control” or something, which conveys a better feel about what the authors are doing.

### Soundness
3

### Presentation
3

### Contribution
3
