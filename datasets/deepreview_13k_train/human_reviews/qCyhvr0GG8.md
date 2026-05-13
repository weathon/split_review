# VONet: Unsupervised Video Object Learning With Parallel U-Net Attention and Object-wise Sequential VAE

- Decision: Accept
- Scores: 5, 6, 6, 5

## Abstract
Unsupervised video object learning seeks to decompose video scenes into structural object representations without any supervision from depth, optical flow, or segmentation.
We present \method{}, an innovative approach that is inspired by MONet.
While utilizing a U-Net architecture, \method{} employs an efficient and effective parallel attention inference process, generating attention masks for all slots simultaneously.
Additionally, to enhance the temporal consistency of each mask across consecutive video frames, \method{} develops an object-wise sequential VAE framework.
The integration of these innovative encoder-side techniques, in conjunction with an expressive transformer-based decoder, establishes \method{} as the leading unsupervised method for object learning across five MOVI datasets, encompassing videos of diverse complexities.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents VONet, an innovative approach to unsupervised video object learning inspired by Monet. Specifically, Monet implements an efficient and effective parallel attention inference process that simultaneously generates attention masks from U-Net for all slots. In addition, the temporal consistency necessary to track objects across video frames is achieved by integrating an object-wise sequential VAE framework. Experiments demonstrate that the approach achieves competitive performance on several challenging object-centric video prediction benchmarks.

### Strengths
1.The parallel attention inference process proposed in this paper greatly improves the slot generation efficiency of MoNet and creates conditions for its further application.

2.This paper proposes the KLD loss, which utilizes the principle that "only slot representations that exhibit temporal consistency can exhibit predictability" to cleverly achieve temporal consistency in unsupervised video object learning.

3.The paper is relatively easy to follow, with good mathematical formulations and diagrams.

### Weaknesses
1.VoNet is a work based on MoNet and is highly similar to ViMON, a comparison of results with MoNet and ViMON should be reported in the experimental phase to demonstrate the advantages of VoNet.

2.Can the method in this paper correctly handle objects appearing in the middle of the video or reappearing after being occluded and maintain temporal consistency? The MOVI dataset does not seem to be able to model this situation, consider adding experiments in natural scenes.

3.Existing video object-centric learning methods based on slot attention are developing rapidly, e.g.DINOSAUR(https://arxiv.org/abs/2209.14860), VideoSAUR(https://arxiv.org/pdf/2306.04829.pdf), and perform well on natural scene datasets such as YouTube-VIS, please explain the advantages of the method in this paper compared to methods based on slot attention.

### Questions
For writng, the introduction section is short. It is hard to understand the main idea of the whole work.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
VONet introduces two key innovations: 1) a parallel attention network that employs the same U-Net architecture simultaneously on K context inputs, and 2) an object-wise sequential VAE framework, aimed at improving the temporal consistency in unsupervised video object learning. Notably, VONet significantly outperforms the baseline by a substantial margin.

### Strengths
1. Within this paper, the "object-wise sequential VAE" is introduced, which is a novel and highly effective representation for exploring temporal dependencies in video frames. 
2. The experimental results in this paper are impressive, surpassing previous methods by a large margin.

### Weaknesses
1. In order to show the advantages of parallel processing, it would be beneficial that a comprehensive latency/accuracy comparison with MONet could be provided in the single-frame scenario.

2. It would be beneficial to have a comparative analysis between the object-wise sequential VAE and other temporal dependency networks, particularly the memory network mentioned in reference [1]. These methods excel in modeling temporal information and such a comparison would greatly enhance the paper's overall comprehensiveness.

### Questions
Please see Weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a framework for unsupervised video object learning, VONet. The uniqueness of VONet is primarily the parallel attention process that is capable of generating attention masks for all slots with the consideration of temporal consistency which utilizes context propagation across time and object-wise sequential VAE framework. Their results on 5 MOVI datasets show that the proposed method significantly outperforms previous methods as measured by two popular metrics namely FG-ARI and mIoU.

### Strengths
The proposed method addresses unsupervised video object learning which can be paralleled and temporally consistent given the slot numbers. Both temporal consistency and parallel segmentation instead of a sequential learning are crucial for learning objects in a video. This paper solves these very important first steps.

### Weaknesses
As already mentioned in the paper when the predefined slot numbers is larger than the actual number of objects, an unwanted side-effect if over-segmentation. Can the authors provide any insights on how to potentially combine multiple slots to prevent such overfitting?

### Questions
Can the authors provide any insights on how to potentially combine multiple slots to prevent such overfitting?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an unsupervised video object representation learning framework, namely VONet. Taking an image-based method as per-frame baseline, the proposed VONet builds temporal attention to learn correspondence in high-level space, resulting in significant improvement against previous video-based methods.

### Strengths
1. The results look good with large improvement against previous methods.

### Weaknesses
1. The current title is too broad, which makes the readers hard to understand the specific contributions of this paper.

2. The motivation of each contribution of the proposed method is not clearly clarified in Introduction, especially the difference or new insights w.r.t previous  methods.

3. It is hard to refer to the expression of the symbols in Figure 3.

### Questions
See weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
