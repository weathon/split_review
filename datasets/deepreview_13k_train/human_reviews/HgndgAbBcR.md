# CNNGEN: A GENERATOR AND BENCHMARK FOR SUSTAINABLE CONVOLUTIONAL NEURAL NETWORK SEARCH

- Decision: Reject
- Scores: 5, 3, 3

## Abstract
Neural Architecture Search (NAS) emerged as a promising approach to search for
optimal neural network architectures in a limited, predefined architecture space.
One popular method to form such a space is to derive a known architecture in
which we insert cells where NAS algorithms can automatically combine network
functions and connections. Cell-based methods yielded hundreds of thousands
of trained architectures whose specifications and performance are available to de-
sign performance prediction models. Cell-based approaches come with three main
limitations: i) generated networks have limited diversity resulting in very sim-
ilar performances, in turn hampering the generalization of trained performance
models, ii) networks’ implementations are missing hampering performance un-
derstanding, and iii) they solely focus on performance metrics (e.g., accuracy)
ignoring the growing sustainability concern. We propose CNNGen, an approach
that addresses: i) by leveraging a domain-specific language (DSL) to automat-
ically generate convolutional neural networks (CNNs) without predefined cells
or base skeleton. It allows the exploration of diverse and potentially unknown
topologies; ii) CNNGen’s comprehensive pipeline stores the network description
(textual and image representation) and the fully executable generated Python code
(integrated with popular deep-learning frameworks) for analysis or retraining, and
iii) in addition to training and performance metrics, CNNGen also computes en-
ergy consumption and carbon impact for green machine learning endeavors. We
demonstrate the possibilities of CNNGen by designing two performance predic-
tors and comparing them to the state of the art.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a new approach to Neural Architecture Search (NAS) that uses a domain-specific language (DSL) to generate convolutional neural networks without predefined cells or base skeletons named CNNGen.
This approach offers a more diverse and sustainable solution to NAS, addressing the limitations of cell-based methods.
The paper outlines the comprehensive pipeline used by CNNGen to store network descriptions and fully trained models, and discusses the growing concern for sustainability in neural network design and implementation. Overall, CNNGen is an innovative and promising tool for generating and benchmarking sustainable convolutional neural networks.

### Strengths
- The paper introduces a new approach to use a domain-specific (natural) language (DSL) to generate convolutional neural networks, that allows the exploration of diverse and potentially unknown topologies.
- The paper discusses the growing concern for sustainability in neural network design, also computes energy consumption and carbon impact for green machine learning endeavors.

### Weaknesses
 - The extracted five key concepts used to describe architectures (architecture, featureExtraction, featureDescription, classification) are still limited, not sure why this would lead to better diversity in neural architectures.

 - I feel the method is just trying to use natural language to replace the tradtional symbolic respresentation in NAS search spaces. I'm sceptical of why the proposed method could generate more diverse architectures.

### Questions
- It's unclear how the author choose the five key concepts used to describe architecture.
- I feel the method is just trying to use natural language to replace the tradtional symbolic respresentation in NAS search spaces. I'm sceptical of why the proposed method could generate more diverse architectures.

### Soundness
3 good

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
This paper presents a new way to generate a NAS search space. The authors dubbed their method CNNGen. This new methods relies on domain-specific language (DSL) to capture neural architectures using a dedicated grammar. The authors claim this methods results in more diverse architectures to search. The authors also present a method to compare their work against other search spaces and claim their method outperforms state-of-the-art. The authors also propose adding a carbon footprint metric to the models.

### Strengths
I highlight the following strengths:
- The idea of adding DSL to generate network candidates is interesting. Using grammar to represent networks is a good idea and it has the potential to represent more diversity of solutions as the authors point out in their results
- Representing an a network candidate as an image is also interesting and it allows for metrics that are more aligned with computer vision tools. The authors demonstrate the use of these metrics in the paper

### Weaknesses
I see 2 critical flaws with this work:
- The benchmark's are insufficient. The authors only compare the data with the one presented in [1]. This comparison is limited to CIFAR data only. Even in [1] the authors present a comparison using ImageNet data. Additionally, the authors present a benchmark but don't really benchmark any NAS methods. To show good power of the benchmark the authors need to present results showing that NAS methods can benefit from this benchmark and find architectures with better accuracy and even better carbon footprint (since the authors present this as a metric). As it stands I don't see sufficient evidence of novelty or impact for this work. The authors should run a real benchmark of methods and present more extensive results.
- The authors completely ignore the advancements in differentiable NAS [2,3,4,5]. In these works there is no need to use a search space and one can optimize an architecture using gradient decent. In fact, some works like [3] and [5] show how to do this and also add constraints for latency and power consumption. Given the existence of these methods, I don't see the value of creating a new search space benchmark. I ask the authors to clarify the lack of mention and comparison here and clarify any misunderstanding from my side.

### Questions
See weaknesses.

### Soundness
1 poor

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work presents a new benchmark consisting of various performed architectures automatically generated from domain-specific language (DSL) and the performance, training code, and energy consumption information of each architecture.

### Strengths
This work presents a new benchmark and an image-based performance predictor.

### Weaknesses
 1. Why the performance of networks should be diverse? Note the goal of NAS is to find architecture better than human crafted ones, while human designed architecture perform quite well in nearly all cases. The importance of NAS to distinguish models with similar high performance. For instance, NAS is designed to distinguish ConvNeXt and ResNeXt, rather than ConvNeXt and LeNet. The previous benchmark that has most architectures with very close and high accuracy actually make more sense than the proposed ones. The paper does not adequately justify why a benchmark with diverse performance is more valuable for NAS research than one focused on high-performing architectures.

 2. DSL has limitation in the expressivity of the architecture. The proposed DSL seems only supports sequential architecture without branches ( Fig 3 and Fig. 8). The lack of support for branching architectures significantly limits the scope of the benchmark and its relevance to modern neural network design. The DSL's inability to represent common architectural patterns, such as skip connections or parallel processing paths, is a major drawback.

 3. Intuition of predictor. Why do you think a CNN can know the network's performance by looking at the image of its architecture? What is the intuition behind it? For me, it just overfits a small dataset. The paper fails to provide a clear explanation for why a CNN should be able to predict network performance from an image representation of the architecture. The lack of a theoretical basis for this approach raises concerns about its validity and generalizability.

### Questions
1. Why do we need an accurate number of energy consumption? Why not just model parameters and FLOPs? Energy consumption is very sensitive to the setup of machines and can be easily outdated. A model that consumes many energy might be very energe-saving in the next year due to the new software support and hardware update.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor
