# PETRA: Parallel End-to-end Training with Reversible Architectures

- Decision: Accept
- Scores: 8, 6, 8, 8

## Abstract
Reversible architectures have been shown to be capable of performing on par with their non-reversible architectures, being applied in deep learning for memory savings and generative modeling. In this work, we show how reversible architectures can solve challenges in parallelizing deep model training. We introduce PETRA, a novel alternative to backpropagation for parallelizing gradient computations. PETRA facilitates effective model parallelism by enabling stages (i.e., a set of layers) to compute independently on different devices, while only needing to communicate activations and gradients between each other. By decoupling the forward and backward passes and keeping a single updated version of the parameters, the need for weight stashing is also removed. We develop a custom autograd-like training framework for PETRA, and we demonstrate its effectiveness on CIFAR-10, ImageNet32, and ImageNet, achieving competitive accuracies comparable to backpropagation using ResNet-18, ResNet-34, and ResNet-50 models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a new algorithm for training reversible models. Compared to backpropagation, it can be run on each layer in parallel and with a reduced memory cost. They show empirically the advantages of their algorithm on RevNet models for image classification.

### Strengths
- The paper is well written, clear, and has helpful illustrations.
- The algorithm seems simple, natural and intuitive.
- While the algorithm relies on reversible layers, it can still be mixed with standard non-reversible layers, for which a standard backpropagation is performed.
- The authors validate their algorithm with thorough experiments and analyses.

### Weaknesses
1. Invertible networks are currently not very used. This limits the direct applications of the algorithm. However I am aware that PETRA could motivate such the use of such architectures.
2. The experiments are only performed on RevNet models for image classification. As mentioned in the conclusion, it would be very nice to see experiments on more tasks and models. Indeed, as PETRA is applicable to only a subset of models (reversible models), it is frustrating to only see experiments on a single architecture.
3. Lines 509-510: I think you meant RevNet instead of ResNet.

### Questions
- How is the approximated gradient influenced by the depth of the model? I would expect the error to increase as the model gets deeper.

I find the paper very interesting and am ready to increase my grade should my remarks be addressed by the authors.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
PETRA is a model-parallel training method for reversible neural networks that decouples forward and backward passes, eliminating the need for activation or parameter buffers. This enables efficient parallel computation across devices with reduced memory overhead. PETRA matches backpropagation in accuracy on datasets like CIFAR-10 and ImageNet, while also achieving notable speed and memory savings, making it a potential alternative for large-model training.

### Strengths
The PETRA paper presents a new alternative for large-scale neural network training, offering efficient parallelization by decoupling forward and backward passes, which enables stages to compute independently across devices. Utilizing reversible architectures, PETRA removes the need for activation and parameter storage, achieving up to 54.3% memory savings, making it especially valuable for training large models. It demonstrates accuracy comparable with backpropagation on datasets like CIFAR-10 and ImageNet.

### Weaknesses
Dependency on Reversible Architectures: The approach is designed specifically for reversible architectures, which may limit its application to models that can be easily adapted to this structure. Non-reversible architectures, such as standard ResNets or some types of transformers, may not benefit as fully from PETRA’s memory and efficiency gains.
Increased Communication Overhead: While PETRA reduces memory usage, its reversible stages require additional communication overhead during the backward pass, which could affect scalability on very large, distributed systems. And the PETRA propose dividing a model into some
Scalability Constraints with Non-Reversible Layers: Although PETRA performs well on reversible architectures, any non-reversible stages still require stored activations, potentially increasing memory use and complicating scalability for models that include such layers.

### Questions
How PETRA perform on large model and more complex task, such as pretraining language model? The experiment in the paper is weak. The scalability of PETRA can not be verified by the current empirical results. Experiments on distributed pretraining for llm is necessary to validate the efficiency of PETRA, for example: experiments on Pile dataset with varying model size.

Is the reversible architecture necessary for PETRA? For models that integrate both reversible and non-reversible layers, how does PETRA manage memory savings and efficiency, and could these hybrid architectures affect its scalability benefits?

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
The paper proposes to perform model parallel training using reversible architectures. Compared to delayed gradient, the proposed method is more memory efficient since it does not need to stash weights. It is shown that on shallower architecture the performance is slightly better than regular backprop and on deeper architecture such as ResNet-50, there is a slight drop but not significant. Overall, the work is likely to have a big impact as a way to scale up model parallel training.

### Strengths
- The paper demonstrated that activation reconstruction can work well with out-of-sync backward weights, and the reconstructed activations can be used to update weights.
- The paper has shown real computation and memory savings.

### Weaknesses
- It would be nice to see at what scale the method starts to break down (say when there is more and more delay in reconstruction). And show a plot on reconstruction error and final performance as a function of the number of delay steps. The model depth can be another variable to explore, aside from the few standard model architectures, perhaps sweeping a wider range of depths.
- Algorithm 1 is a little hard to process.
- The method relies on gradient accumulation to fully match with the It is unclear to me how gradient accumulation would have any impact when a large batch / data parallel is employed. This may not be a concern for LLMs, but for ImageNet and SSL training, many use very large batch sizes.

### Questions
N/A

### Soundness
3

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
5

### Summary
This paper proposes to utilize the concept of reversible architectures to improve parallelization in DNN training. A model is split into multiple stages that are trained asynchronously; i.e. in a model parallel fashion. Leveraging reversibility, the training of the different stages is effectively decoupled. This scheme offers a linear speedup in the number of stages relative to end-to-end backprop, while reducing the memory footprint. The method is evaluated using ResNets/RevNets with three different image classification benchmarks.

### Strengths
The paper is well-written and easy to follow. The idea of utilizing reversibility for parallelization is a nice, simple, and novel idea! Consequently, I find myself sufficiently convinced that the method works --- albeit, that the empirical evaluation is somewhat limited. The novelty and applicability of the method mostly outweighs my concerns about the evaluation.

### Weaknesses
My only objection to this work is the limited number of experiments. They are limited to ResNet/Revnet 18/34/50 and CIFAR10, ImageNet-32, and ImageNet. It would definitely improve the paper to have at least a few more architectures included.

### Questions
How did you partition the architectures for your experiments? How many layers/blocks in each stage? Were they all the same size? And if so, would that not bring them out of sync during training such that top layers/stage were idle a lot of the time? The size of the feature maps is decreasing in the layer index, no? Thus, the lower layers/stages would consume more memory and compute than the top ones?

Perhaps you could add some information about this in the appendix :-)

### Soundness
3

### Presentation
4

### Contribution
3
