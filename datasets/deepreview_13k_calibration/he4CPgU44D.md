# Active Continual Learning: On Balancing Knowledge Retention and Learnability

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 3, 6

## Abstract
Acquiring new knowledge without forgetting what has been learned in a sequence of tasks is the central focus of continual learning (CL). 
While tasks arrive sequentially, the training data are often prepared and annotated independently, leading to the CL of incoming supervised learning tasks. 
This paper considers the under-explored problem of active continual learning (ACL) for a sequence of active learning (AL) tasks, where each incoming task includes a pool of unlabelled data and an annotation budget.  
{
We investigate the effectiveness and interplay between several  AL and CL algorithms in the domain, class and task-incremental scenarios.
Our experiments reveal the trade-off between two contrasting goals of not forgetting the old knowledge and the ability to quickly learn new knowledge in CL and AL, respectively. While conditioning the AL query strategy on the annotations collected for the previous tasks leads to improved task performance on the domain and task incremental learning, our proposed forgetting-learning profile suggests a gap in balancing the effect of AL and CL for the class-incremental scenario.
}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors address the task of active continual learning, in which a sequence of tasks consisting of unlabeled data and an annotation budget are presented to the model. This is challenging because of the need of balancing the ability to not forgetting and quickly learning within the annotation budget. They propose a forgetting-learning profile to better understand the behavior of active continual learners and guidelines to choose active learning and continual learning algorithms. Specifically, they show that uncertainty-based active learning is better suited for domain incremental learning, whereas diversity-based active learning is better for task incremental learning.

### Strengths
There is a need for a systematic evaluation of continual active learning models given the variety of options for each of the main components of the system, namely, active learning and continual learning.

The authors took the time and effort to answer to the criticism raised by the reviewer in the weaknesses and question sections below, which increased the score relative to the initial value.

### Weaknesses
Presenting ACL results without error bars (consistently) has the potential of misrepresenting the capabilities of different approaches and a missed opportunity to also highlight the stability/consistency of different approaches.

The analysis of the results in Figure 3 (and Figure 4) is weak, for instance "ACL achieves comparable performance to CL in most scenarios", however, the statement seems to be purely qualitative. Why is it expected that experience replay methods achieve high accuracy than FT and EWC. Also, the Figure is difficult to read. Alternatively, showing accuracy relative to full will make for a better scaling and visualization of the differences between AL approaches.

Figures 8 and 9 are very difficult to read with so many dots with similar colors and similar to 3 and 4, the analysis is somewhat shallow given the amount of data in the Figures and what is not shown (due to error bars).

For a purely experimental contribution (with no methodological novelty) the design of the experiment lacks a systematic evaluation of the factors affecting the performance of CL and Al methods. For instance, number of tasks, backbone, model size, annotation budget (especially the annotation budget), computational budget, etc. Moreover, the analysis of the results is mostly qualitative instead of a quantitative evaluation of the significance of the improvements of different methods.

### Questions
How was Figure 1(b) obtained?

Why not showing Figures 5 and 6 like in Figure 1(b) to better show the trade-off between forgetting rate and LCA?

Figures 5, 6 and 7 have error bars, however, (in the paper proper) it is not described how they were obtained.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper has full study for active continual learning problem that explores the tradeoff between a quick learner and not to forget the learned knowledge.

### Strengths
The AL + CL have broad interest. There are many evaluations of current AL and CL approaches in paper.

### Weaknesses
The paper has the following concerns that I am afraid it cannot meet the ICLR threshold.

1) The paper does not seem to have a high novel approach, but mostly evaluate the current AL and CL approach.

2) The evaluation seems only on P-MNIST, S-MNIST, CIFAR-10, maybe small sets.

### Questions
What do you think would be the good application of ACL?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an experimental analysis exploring the potential of active learning for annotation of examples for continual learning. The paper considers a variety of continual learning settings, including domain-incremental, class-incremental and task-incremental learning, and examines aspects such as the balance between forgetting and learning in CL aided by active learning. The authors conduct experiments in six benchmark datasets + tasks, including P-MNIST, MNIST and CIFAR-10, and over a range of state-of-the-art continual learning methods for regularization and example replay. In the experiments, the authors examine the performance of these methods integrated with the ACL proposed approach, and compare this to joint learning and multitask learning with respect to overall accuracy, forgetting, and learning-forgetting profile.

### Strengths
- The paper examines a reasonable avenue for continual learning, which is selecting annotated examples by means of active learning. The paper aims at answering three important research questions in this setting. This demonstrates the originality of the paper. 
- The paper is in general well organized and the concepts are presented clearly and to sufficient depth.

### Weaknesses
 - The choice of some visualizations in the paper is very odd. For example, in Figures 3 and 4, a dashed red line is selected to represent the performance on the "full labelled dataset". But, why is a line used to connect in between methods (x axis)? What is the meaning of this? Similarly, all the dots representing different strategies make it very difficult to grasp what is the actual performance of each of the selected methods with each of those strategies. I would strongly suggest to find a much better representation. 
- Although the selected datasets are CL benchmarks, these are also the easiest ones. I would have expected to see experimental results on more challenging datasets such as CIFAR-100, some version of ImageNet (tiny-ImageNet, mini-ImageNet), etc. Furthermore, from Figure 3 and 4, it seems that for the slightly more challenging datasets and tasks (P-MNIST, CIFAR-10 CIL, TIL), all the ACL methods perform substantially badly, therefore raising questions on the actual effectiveness of CL combined with active learning, and the significance of the proposed approach.
- A final remarkable weakness that I see in this paper is the limited number of tasks in the experiments. While the authors consider multiple datasets, the number of tasks within each dataset is quite low (e.g., 5 for MNIST and CIFAR-10). I would expect that active selection of examples would be significantly more difficult as the number of tasks increases, and therefore would have expected to see results along these lines. The analysis should include scenarios with a larger number of tasks to properly evaluate the scalability and robustness of the proposed active learning approach.

### Questions
- Please refer to questions in the "weaknesses" section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper explores the domain of active continual learning, a novel problem that, to the best of my knowledge, has not been previously investigated. It doesn't aim to introduce a new model; instead, it serves as an analytical study, delving into the interplay between active learning and continual learning.

### Strengths
1. The problem is novel and interesting
2. The analysis experiments are extensive and should be valuable to the community

### Weaknesses
At first glance, this paper encompasses both text and image datasets, along with three CL settings. However, upon closer examination of the baseline, it appears that the baselines are largely drawn from Class-Incremental Learning (CIL), such as DER++, iCaRL, and GDumb. Consequently, the paper doesn't utilize any state-of-the-art methods for specific settings and data types. For example, in the Text-Incremental Learning (TIL) for text data, [1,2] represent more likely SoTa approaches (further details available in the survey [3]). This lack of a fair comparison with state-of-the-art methods is the major drawback for this analysis paper.

### Questions
See above

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
