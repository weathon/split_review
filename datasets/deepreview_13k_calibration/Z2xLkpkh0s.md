# FARSE-CNN: Fully Asynchronous, Recurrent and Sparse Event-Based CNN

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Event cameras are neuromorphic image sensors that respond to per-pixel brightness changes, producing a stream of asynchronous and spatially sparse events. Currently, the most successful algorithms for event cameras convert batches of events into dense image-like representations that are synchronously processed by deep learning models of frame-based computer vision. These methods discard the inherent properties of events, leading to high latency and computational costs. Following a recent line of works, we propose a model for efficient asynchronous event processing that exploits sparsity. We design the Fully Asynchronous, Recurrent and Sparse Event-Based CNN (FARSE-CNN), a novel multi-layered architecture which combines the mechanisms of recurrent and convolutional neural networks. To build efficient deep networks, we propose compression modules that allow to learn hierarchical features both in space and time. We theoretically derive the complexity of all components in our architecture, and experimentally validate our method on tasks for object recognition, object detection and gesture recognition. FARSE-CNN achieves similar or better performance than state-of-the-art asynchronous methods, with low computational complexity and without relying on a fixed-length history of events.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper intorduces an RNN architecture that is tailored to event-based processing in asynchronous manner. The architecture is evaluated against several other methods on 3 event-based datasets.

### Strengths
The paper is written clearly, and the illustrations support the text well. I believe the problem that is being addressed in the paper is important, as the authors mentioned, many modern event-based camera methods rely on image-like representations and thus are suboptiomal for event data processing.

### Weaknesses
1) Abstract: It would be better to clarify or paraphrase, as these two sentences seem to contradict each other: "most successful algorithms for event cameras convert batches of events into dense image-like representations" and "achieves similar or better performance than state-of-the-art
asynchronous methods". What was the goal of the paper - to beat the best methods or do develop a sota asynchronous pipeline? I assume the latter, but this needs to be stated more clearly in the abstract.

2) It would help if the evaluation was expanded, since there are not so many event-based datasets available. E.g. CIFAR10-DVS and SL-Animals could be added. A more complex EV-IMO (https://better-flow.github.io/evimo/download_evimo_2.html) could strengthen the paper further.

3) It would be also great to see the performance of the method measured (train / inference separately) on a modern computer or embedded platform. Theoretical computations are valuable, but in practice there are many factors besides flops that can affect the performance. A side-by-side comparison of a few methods would make it more clear to the reader what the implications of the architecture are.

4) From table 1, it seems that the accuracy is not the best (or significantly better compared to competition). The compute cost seems not the lowest as well. I believe a better explanation should be provided to explain the results.

### Questions
1) The authors mention, in the introduction, 3D convolutional networks. What is the main difference / advantage of the presented asynchronous scheme compared to 3D cnns, given that both leverage temporal information and, in theory, could be ran event-by-event? An example paper that explores this: https://openaccess.thecvf.com/content_CVPR_2020/papers/Mitrokhin_Learning_Visual_Motion_Segmentation_Using_Event_Surfaces_CVPR_2020_paper.pdf - it would be beneficial to add it to the review section as well.

2) Are there plans to release the source code as a (e.g. Pytorch) package? I believe this would add to the overall contribution of this work.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
A new deep learning architecture - RNN for processing event data.

### Strengths
The authors show similar or better performance at higher computation efficiency than other approaches that uses asynchronous methods.

### Weaknesses
 - How does the complexity of the architecture affect the implementation? Does this architecture of asynchrony give actual speedup?
- Are the datasets shown here sufficient? I am aware of a few other event vision work that looks at some other event data-streams. Can the authors do more SOTA comparisons ?
- Temporal dropout while interesting seems to be an already existing technique? [1] uses some dynamic temporal exit. Further, there are some temporal coding works [2] that use some interesting forms of temporal representation. Can the authors comment on how dropout is different from these?

### Questions
See above weakness

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper investigates the asynchronous processing of individual event data without converting them into image-like inputs, thereby significantly reducing the overall model energy consumption. The paper designs and implements modules such as FARSE-CNN, SUB-FARSE-CNN, Sparse Pooling, Temporal Dropout, and validates the model's effectiveness in tasks like recognition and detection.

### Strengths
1. Based on LSTM design, the paper has implemented a FARSE-CNN for event data, with Sub-FARSE-CNN specifically producing outputs for the central pixel of each cell and updating the state of each cell, addressing the issue of a sharp increase in the number of events after passing through the module.

2. Sparse Pooling compresses event data in the spatial dimension, while Temporal Dropout considers discarding some data in the temporal dimension to encourage the model to learn long-term features, fully utilizing the spatiotemporal characteristics of events.

3. In the tasks of object recognition and object detection, the paper validates the role of the proposed modules in the network, showing their ability to balance computational complexity and accuracy, achieving performance comparable to or better than previous methods. It also achieves performance similar to synchronous methods in gesture recognition tasks.

### Weaknesses
1. Although the asynchronous method proposed in the paper handles event data, it does not demonstrate the real-time performance and execution speed of this method. Is there any data available regarding this aspect?

2. For the Temporal Dropout discussed in Contribution 2 and the "l" parameter mentioned in Section 3.5, the experimental section does not provide relevant configurations or discussions. Specifically, the paper lacks details on how the dropout rate is chosen, how it impacts the model's learning of long-term dependencies, and whether different values of 'l' were explored and their impact on performance.

3. While the paper mentions both FARSE-CNN and SUB-FARSE-CNN, with the latter being an optimized improvement of the former, there is no experimental data to prove the effectiveness of this optimization. For example, there is no performance or computational complexity comparison. The paper should include a direct comparison, showing metrics like inference time, memory usage, and accuracy for both FARSE-CNN and SUB-FARSE-CNN to justify the optimization.

### Questions
see Weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a model for efficient asynchronous event processing that exploits sparsity. They design the Fully Asynchronous, Recurrent and Sparse Event-Based CNN (FARSE-CNN), a novel multi-layered architecture which combines the mechanisms of recurrent and convolutional neural networks. To build efficient deep networks, they propose compression modules that allow to learn hierarchical features both in space and time.

### Strengths
S1: The authors try to present an inherently spiking/event domain based approach for processing asynchronous data from event-like sensors. Often in the related literature you see efforts at converting the data to frame like representations in order to process it using traditional algorithms developed for the synchronous domain. This approach tries to deal with the problem of processing the raw data directly without performing this limiting transformation which could hinder latency. As a result this is the main strength of the paper in my opinion

S2: overall the paper is well written and the algorithm seems interesting, so i think it will be of interest to a subset of the community interested in on the edge based processing approaches

### Weaknesses
W1: it is not clear to me if source code will be provided. Please clarify

W2: I would have liked to see a more thorough discussion on the number of events produced internally by this architecture. To run something like this on neuromorphic hardware efficiently, you need to ensure that a sparse number of events are created internally. A discussion on this in the paper, would improve it. Specifically, it would be beneficial to analyze how the number of internal events scales with the input event rate and the network depth. Furthermore, a comparison of the internal event rate with other event-based architectures would provide valuable context.

### Questions
See comments above

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
