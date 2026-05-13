# Deep Models modelled after human brain boost performance in action classification

- Decision: Reject
- Scores: 3, 1, 1

## Abstract
Recognizing actions from visual input is a fundamental cognitive ability. Perceiving what others are doing is a gateway to inferring their goals, emotions, beliefs and traits. Action recognition is also key for applications ranging from robotics to healthcare monitoring. Action information can be extracted from the body pose and movements, as well as from the background scene. However, the extent to which deep neural networks make use of information about the body and information about the background remains unclear. In particular, since these two sources of information may be correlated within a training dataset, deep networks might learn to rely predominantly on one of them, without taking full advantage of the other. Unlike deep networks, humans have domain-specific brain regions selective for perceiving bodies, and regions selective for perceiving scenes. The present work tests whether humans are thus more effective at extracting information from both body and background, and whether building brain-inspired deep network architectures with separate domain-specific streams for body and scene perception endows them with more human-like performance. We first demonstrate that deep networks trained using the Human Atomic Actions 500 dataset perform almost as accurately on versions of the stimuli that show both body and background and on versions of the stimuli from which the body was removed, but are at chance-level for versions of the stimuli from which the background was removed.  Conversely, human participants (N=28) can recognize the same set of actions accurately with all three versions of the stimuli, and perform significantly better on stimuli that show only the body than on stimuli that show only the background. Finally, we implement and test a novel deep network architecture patterned after domain specificity in the brain, that utilizes separate streams to process body and background information. We show that 1) this architecture improves action recognition performance, and 2) its accuracy across different versions of the stimuli follows a pattern that matches more closely the pattern of accuracy observed in human participants.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper takes insights from neuroscience and builds a model that processes body and background in images separately, aiming to improve the performance of action recognition.

### Strengths
This paper propose novel ideas of incorporating inductive bias from neuroscience in building artificial neural networks and shows that it does improve the performance of action recognition when compared with a baseline network. The paper is well-written and very clear. The human dataset collected in this paper is also valuable and should be perhaps incorporated into action recognition benchmarks.

### Weaknesses
This paper is a rudimentary effort in showing incorporating certain inductive bias from neuroscience could potentially help with artificial networks in certain tasks. However for the scope of the conference, I think the lack of comparison to state-of-art models as well as insights on how to even combine this inductive bias with state-of-art models makes this paper not suitable for application and making real impact on the task of action recognition. It is also not entirely true to assume that state-of-art model, which is much more complicated than a ResNet50 network does not implicitly extract information from the background and body when recognizing action. Furthermore, the paper does not provide a clear ablation study to show how much each stream (body vs. background) contributes to the overall performance, making it difficult to assess the true benefit of their proposed architecture. The experiments are limited to a single dataset and a relatively simple action recognition task, which raises concerns about the generalizability of the findings to more complex scenarios and datasets.

### Questions
Discussion of how to incorporate this into state-of-art models is recommended.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work begins by examining the similarities and differences between humans and deep neural networks in terms of action recognition. It demonstrates that a deep neural network trained with cross entropy on the entire video cannot perform action recognition when background information is omitted from the training data. In contrast to this, human subjects are capable of identifying activities solely from the body information. This highlights that DNN trained for action recognition incorrectly balances the body and background information present in the video data. In order for the deep neural network to exclusively distinguish actions coming from the body, the authors suggested using two different backbones, one for the body and one for the background. In addition to this, they implemented a loss function that was more complex and yet nevertheless compatible with their category-selective design. As a consequence of this, they demonstrated that a body-background separated backbone may produce an action recognition pattern that is comparable to the pattern seen in human participants, albeit with a significantly lower level of accuracy.

### Strengths
The authors try to optimize deep neural works towards reproducing action recognition patterns observed in human subjects.

### Weaknesses
As the authors already included in the related works, having separate streams for different information in video is not new. For example, an early work on dynamic texture processing used two separate backbones for “appearance” (the scene) and “dynamic” (the optic flow). Their loss function also combines the matching of both appearance and dynamic features. It is possible that the L_{combined} here is new. However, the authors do not include any details on how they define L_{body}, L_{background} or L_{combined}. If the only difference this work has with other work is its usage of L_{combined} (I guess this is the cross entropy between predicted frames vs. the true frames), the novelty is very limited.



Tesfaldet et al 2017 Two-Stream Convolutional Networks for Dynamic Texture Synthesis



This work needs a much more developed result section to fit as an ICLR manuscript. Its current format has one result. This result is not surprising given previous literature. I would encourage the authors to include a more detailed investigation of the proper loss functions, what predictive features are being used in humans to perform action recognition, etc. These extensions may strengthen this paper.

### Questions
Does the background contain any information about the actions in the video? If not, I hope the authors illustrate better why the background information should be used at all for action recognition. Would it be desirable that a neural architecture should focus on the “action” component of the video to perform action recognition? 

Which component of the loss function contributes the most when body-only information is being used? Or when background-only information is being used?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors investigate how neural networks label action-recognition video frames and compare the neural network against human behavioral performance. They manipulate the stimuli to separate bodies and background and show that both neural networks and humans perform very well with full stimuli, body only or background only. Humans perform better with the body only compared to background only conditions. The authors propose an architecture that is loosely based on notions of modularity in the brain and this new architecture improves performance and matching to human behavioral data.

### Strengths
Building networks to recognize actions is of high importance to practical applications 

Comparing how well networks perform to human performance is also of interest in terms of aligning machine and human visual capabilities.

### Weaknesses
The bottom line is that highly uncontrolled and bad datasets lead to spurious and uninterpretable results. This is the main challenge throughout. 

In Fig. 1 bottom left, the authors claim that baseline models perform similarly well when tested with ORIG, body or BG. This is NOT what the results show. The results do not have error bars, let alone any minimally rigorous statistical analysis. From eyeballing the figure, it seems that ORIG>>BG>>Body. 

The fact that humans can identify actions purely from the background frames with over 0.7 accuracy shows that
(1) The dataset is way too easy
(2) Background is a major confounding factor
(3) Time is not needed in such an easy task 

As far as I understand, the proposed architecture is trained very differently from the baseline architectures. The proposed architecture is trained with Body-only stimuli and does better on Body-only stimuli, and it is trained on BG-only stimuli and does not perform better on BG-only stimuli (again, no error bars, no statistics, this is all from eyeballing). Training yields better performance in general. 

It would be great to present actual results on how well Yolo v8 separates body and background.

The manuscript only has one main figure and minimal additional information that does not satisfy basic standards in the field. There are no error bars, there are no comparisons across multiple different models, no comparisons with different datasets, no ablations, no description of the effects of key variables like size, etc.

### Questions
A key aspect of action recognition is likely to be dynamics and time, which is not studied here.

Within the study of action recognition from frames, it would be useful to use rigorous datasets. If the authors are interested in the effect body and background, it would be important to rigorously control for basic variables like contrast, size, and multiple other confounds.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor
