# ZeroFlow: Scalable Scene Flow via Distillation

- Decision: Accept
- Scores: 8, 5, 5

## Abstract
Scene flow estimation is the task of describing the 3D motion field between temporally successive point clouds. State-of-the-art methods use strong priors and test-time optimization techniques, but require on the order of tens of seconds to process full-size point clouds, making them unusable as computer vision primitives for real-time applications such as open world object detection. Feedforward methods are considerably faster, running on the order of tens to hundreds of milliseconds for full-size point clouds, but require expensive human supervision. To address both limitations, we propose \emph{\ourpipelinefull{}}, a simple, scalable distillation framework that uses a label-free optimization method to produce pseudo-labels to supervise a feedforward model. Our instantiation of this framework, \emph{\ourmethod{}}, achieves \textbf{state-of-the-art} performance on the \emph{Argoverse~2 Self-Supervised Scene Flow Challenge} while using zero human labels by simply training on large-scale, diverse unlabeled data. At test-time, \ourmethod{} is over 1000$\times$ faster than label-free state-of-the-art optimization-based methods on full-size point clouds (34 FPS vs 0.028 FPS) and over 1000$\times$ cheaper to train on unlabeled data compared to the cost of human annotation (\$394 vs $\sim$\$750,000). To facilitate further research, we release our code, trained model weights, and high quality pseudo-labels for the Argoverse~2 and Waymo Open datasets at \url{https://vedder.io/zeroflow}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a scalable point-cloud-based scene flow approach via distillation. Given unlabeled raw point cloud data, the paper first calculates pseudo-GT scene flow using a test-time optimization-based method (Neural Scene Flow Prior), which tends to demonstrate much better accuracy than feed-forward approaches. Then given the pseudo GT, the method trains a feed-forward model in a supervised manner. With this distillation pipeline, their method archives comparable/sometimes even better accuracy than the optimization-based method and of course much better than other feed-forward methods, while maintaining real-time performance. This pipeline is scalable as what it needs is just unlabeled point cloud data.

### Strengths
+ Good performance (Table 1)

   The method achieves better accuracy over previous work while maintaining real-time performance. This source of gain requires the cost and time of generating pseudo-GT using the existing optimization-based approach. However, this can be done offline in a parallel way, so it's not a critical concern.

+ Simple, effective idea

   This distillation idea is very simple, but previous work on point-cloud-based scene flow methods hasn't tried the idea yet. The paper demonstrates that this simple idea is working and demonstrates that it's scalable by using large-scale diverse unlabeled data. It would be great if the computed pseudo-GT would be released to the community.

+ In-depth analysis

  Not only the main experiments, the paper provides in-depth analysis, such as accuracy versus dataset size (Fig. 4), endpoint residual maps (Fig. 5), and variance study (Table 7 and 8). This clearly helps a better understanding of the paper. The paper is pretty much self-contained.

### Weaknesses
There seem to be not many weaknesses in the paper but some minor questions related to the accuracy.

- In Table 1, how can ZeroFlow XL 3X (Ours) outperform the NSFP w/ Motion Comp baseline as ZeroFlow's accuracy can be bounded by the accuracy of pseudo GT (i.e., NSFP)? Would it be also possible to include the accuracy of pseudo GT in Table 1?

- In Fig. 4, why is FastFlow3D better than 'Ours' when the dataset size is less than 100%? I thought ZeroFlow's backbone was based on FastFlow3D, but what change made it underperform FastFlow3D?

### Questions
(just a remark) By the way, there is a recent paper [a] that significantly improves the runtime performance of NSFP by 10 or 30 times (varying different datasets). The proposed approach can reduce the compute cost for pseudo GT generation by using this faster method. 

[a] Fast Neural Scene Flow, ICCV 2023

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new method called ZeroFlow that combines the strengths of optimization-based and feed-forward methods to achieve efficient and label-free scene flow estimation.
It introduces an optimization-based teacher method, which generates pseudo labels, and uses these labels to supervise a feed-forward student model. 
It conducts extensive quantitative evaluations and achieves comparable performance to NSFP and FastFlow3D.

### Strengths
- The overall writing of the paper is good, with a clear description of the motivation and implementation of the proposed approach.
- As can be seen from Table 1, the proposed method achieves a good balance between performance and efficiency.
- The paper verifies the proposed ideas through a series of experiments.

### Weaknesses
- The innovation and contribution of the paper mainly lie in the new application of the distillation strategy, and I suggest the authors provide further analysis or insights into the scene flow estimation task.
I think the achieved performance of the proposed approach is highly dependent on the quality and effectiveness of the existing works.
The authors combine two previously published works, using NSFP to generate pseudo labels and training the FastFlow3D model using these labels.

- In Sections 3.2 and 3.3, the author provides a detailed description to help understand the proposed method, but it is difficult for me to detect the author's new in-depth thinking about this work from these descriptions.
At the same time, Section 3 contains many statements on existing work, such as 3.1. This section might benefit from providing a more in-depth analysis of combining the strengths of optimization-based and feed-forward methods.

- The quantitative results in Table 2 on Waymo Open are less competitive, making the method's performance on this dataset not very convincing.

- The overall style of the article is more like a technical report than a research paper, and I feel that it contains more engineering skills.

### Questions
Please refer to the Weaknesses

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on tackling the practical challenge of real-world scale scene flow. The method employed in this study can be summarized as follows: 1) a slow teacher NSFP is identified; 2) a fast student FastFlow3D is recognized; 3) the teacher is adopted to create auto-labels for supervising the student.

### Strengths
This paper carries out a thorough series of experiments to validate the efficacy of the straightforward autolabel concepts and raises several intriguing questions. Furthermore, the paper includes experiments designed to address these questions, potentially offering valuable insights to the autonomous vehicle industry.

### Weaknesses
The idea lacks novelty, particularly for consideration at ICLR. In my opinion, this paper would be better suited for ICRA or WACV, as they tend to focus on more application and system-oriented research.

### Questions
1. For the full point cloud setting, what is the exact number of points in average? Have we applied ground point removal so the number of points has been significantly reduced. I know there is a discussion in 3.1, but I want to confirm the actual number of points and settings in the later experiments.
2. Algorithm 1 can be removed; it does not provide any useful information.
3. (This is not important) I feel we should not call this scene flow foundation model; scene flow is only a single problem in Computer Vision/Perception.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor
