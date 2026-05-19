# Efficient ConvBN Blocks for Transfer Learning and Beyond

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
Convolution-BatchNorm (ConvBN) blocks are integral components in various computer vision tasks and other domains. A ConvBN block can operate in three modes: Train, Eval, and Deploy. While the Train mode is indispensable for training models from scratch, the Eval mode is suitable for transfer learning and beyond, and the Deploy mode is designed for the deployment of models. This paper focuses on the trade-off between stability and efficiency in ConvBN blocks: Deploy mode is efficient but suffers from training instability; Eval mode is widely used in transfer learning but lacks efficiency. To solve the dilemma, we theoretically reveal the reason behind the diminished training stability observed in the Deploy mode. Subsequently, we propose a novel Tune mode to bridge the gap between Eval mode and Deploy mode. The proposed Tune mode is as stable as Eval mode for transfer learning, and its computational efficiency closely matches that of the Deploy mode. Through extensive experiments in object detection, classification, and adversarial example generation across $5$ datasets and $12$ model architectures, we demonstrate that the proposed Tune mode retains the performance while significantly reducing GPU memory footprint and training time, thereby contributing efficient ConvBN blocks for transfer learning and beyond. Our method has been integrated into both PyTorch (general machine learning framework) and MMCV/MMEngine (computer vision framework). Practitioners just need one line of code to enjoy our efficient ConvBN blocks thanks to PyTorch's builtin machine learning compilers.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper primarily investigates the forward computation and backpropagation process in model training or testing of three modes (i.e., Train, Eval, Deploy) of the ConvBN module (Convolution layer plus BN layer), with a focus on the instability of the Deploy mode during transfer learning. Thus, a new mode called Tune mode is proposed, which boasts the advantages of training stability and low computational time and space costs. 

To verify the effectiveness of Tune mode, the authors selected 5 datasets and 12 models, and conducted extensive experiments in classification and detection tasks. The experiments show that using Tune mode for transfer learning results in a slight improvement in model performance, and a significant reduction in time and space costs. Furthermore, the authors tested the effectiveness of Tune mode in the generation of adversarial samples, thereby demonstrating the general applicability of Tune mode as a replacement for Eval mode in tasks that originally used Eval mode.

### Strengths
1. The article is clearly articulated, with detailed experimental settings, and the proposed Tune mode is simple to implement and easy to reproduce.
2. The theoretical analysis and experimental verification of the instability in Deploy mode training presented in the article seem plausible.
3. The author conducted a large number of experiments to validate the advantages of Tune mode in terms of training stability and low time-space cost, with the latter being significantly beneficial.

### Weaknesses
1. The method proposed in this article is only applicable to methods that originally used Eval mode, its application scenarios are not very broad, and the impact is relatively small.
2. This article only provides experimental verification for the time and space cost advantages of Tune mode. Is it possible to make theoretical estimates and give a result similar to O(N)?

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a novel calculation strategy for ConvBN by changing the order of calculation. The proposed Tune mode have exact same forward/back propagation expression with the eval mode yet are faster and has lesser memory footprint, demonstrated both theoretically and empirically. This makes it a useful component in transfer learning. The authors also attributed the instability of the training using deploy mode to the scaled weight and gradient, leading to the necessity of saving part of the parameters.

### Strengths
1. The writing is pretty clear with solid proof and extensive result.
2. The proposed method can be used widely in computer vision tasks.

### Weaknesses
Not much.

### Questions
Is it possible to merge $b$ and $\beta$?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors introduce the Tune mode of ConvBN blocks, which can save memory and time costs during transfer learning. Experiments show that when transferring the backbone with ConvBN to downstream tasks, Tune mode can save 20%-40% of memory costs without loss of accuracy.

### Strengths
1. The writing and presentation of the paper are clear and easy to understand. 
2. The method (Tune mode for ConvBN blocks) is reasonable and novel.
3. The experiments on five datasets and 12 model architectures show the method's effectiveness: Tune mode can save 20%-40% of memory costs without losing accuracy.

### Weaknesses
1. Although the method to reduce the cost of Eval mode is very clever, the contribution of the paper to academic research is limited. This paper is more like introducing a useful technical trick to reduce the overhead of ConvBN's eval mode in transfer learning. There are no foreseeable follow-up research directions here. This method technically belongs to Gradient Checkpointing (Bulo et al. (2018)), but the authors cleverly use the affine transformation of BN to escape the time cost. On the other hand, this trick can only apply to BN with eval mode.

### Questions
1. The conclusion that "Eval mode gets significantly better mAP than Train mode" is too strong for me. From my personal experience, I sometimes get better accuracy using BN's training mode than using eval mode for transfer learning. Therefore, the authors should provide more experiments than the two selected models to verify this strong conclusion.
2. As SyncBN's eval mode has similar behavior to BN, I am not sure whether the Tune mode can be directly applied to the backbone trained with SyncBN. The author can explain this in the response.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper explored the trade-off between stability and efficiency in Convolution-BatchNorm blocks which are popular convolution neural networks：Deploy mode is efficient but suffers from training instability; Eval mode is widely used in transfer learning but lacks efficiency. 
Based on detailed analysis, the paper proposed a Tune mode, which is stable and efficient, to bridge the gap between Eval mode and Deploy mode. Numerous experiments conducted in various tasks have verified the effectiveness of the proposed Tune mode.

### Strengths
1. The paper provided detailed  analysis of proposed Tune mode from both theoretical and experimental perspectives.
2. The author's writing is very good, and the entire paper is relatively easy to understand.
3. Simple algorithm, easy to follow. (codes are available for the public according to the abstract: "Our method has been integrated into both PyTorch (general machine learning framework) and MMCV/MMEngine (computer vision framework).")
4. The experimental results are reliable and sufficient to verify the effectiveness of this method.

### Weaknesses
1. the proposed Tune mode looks like an engineering technique. (this method might be more suitable for patent applications) 
2. The novelty of this method is somewhat weak for top-tie conferences focused on theoretical research.

### Questions
see weaknesses above

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent
