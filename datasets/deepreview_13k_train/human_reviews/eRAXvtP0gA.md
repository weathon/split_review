# Unsupervised Cognition

- Decision: Reject
- Scores: 5, 3, 1, 1

## Abstract
Unsupervised learning methods have a soft inspiration in cognition models. To this day, the most successful unsupervised learning methods revolve around clustering samples in a mathematical space. In this paper we propose a primitive-based unsupervised learning approach inspired by novel cognition models. This representation-centric approach models the input space constructively as a distributed hierarchical structure in an input-agnostic way. We compared our approach with the current state-of-the-art in unsupervised learning: K-Means for tabular data and IIC for image data. We show how our proposal performs better in average than any of the alternatives. We also evaluate some cognition-like properties of our proposal that other algorithms lack, even supervised learning ones.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Unsupervised learning methods that focus on clustering samples in a mathematical space can have limitations when it comes to capturing cognitive relationships between data. In this paper, the authors propose a representation-centric unsupervised learning approach that generates constructive representations of the input space. The approach transforms inputs into Sparse Distributed Representations (SDRs) and models the input space by organizing these SDRs in a hierarchical structure. The authors compared their approach with K-Means and Invariant Information Clustering (IIC) algorithms and found that their proposal performs better on average. They also evaluated the cognition-like properties of their proposal and found that it outperformed other clustering algorithms, including K-NN. The authors conclude that their proposal is a disruptive unsupervised learning algorithm with promising properties.

### Strengths
- Proposal of a novel representation-centric unsupervised learning algorithm: The paper introduces a new approach that focuses on generating constructive representations of the input space. This algorithm transforms inputs into Sparse Distributed Representations (SDRs) and organizes them hierarchically.
- Evaluation on multiple datasets: The paper evaluates the proposed algorithm on three different datasets: Wisconsin Breast Cancer, Pima Indians Diabetes, and MNIST. This demonstrates the algorithm's versatility and its ability to handle both tabular and image data.
- Empirical evaluation and analysis: The authors conduct thorough experiments to evaluate the performance of their proposal. They analyze the effect of different parameters and compare the algorithm's behavior with other alternatives. The results provide insights into the strengths and limitations of the proposed algorithm.
- Transparency and explainability: The algorithm's internal hierarchical organization of SDRs allows for transparency and explainability. The decision-making process can be traced back to the seed cell and the activation of specific footprints, providing interpretability to the algorithm's predictions.
- Capability to say "I do not know": The algorithm has the ability to recognize inputs that do not match any existing footprints and respond with an "I do not know" answer. This feature ensures that the algorithm does not provide false or hallucinated predictions for unfamiliar patterns.
- The paper is organized and provides a clear structure. The abstract provides a concise summary of the paper's content

### Weaknesses
1. Explain more detail about translating grey image to SDR. I can't understand how normalized input values are separated to bins. For example, MNIST dataset has 1 and 0 value. So, I can't understand how you divide input into bins.
Also, this translation to SDR looks like manual and specified to specific dataset such as MNIST. It seems difficult to extend your algorithm to high-resolution and diverse dataset even about CIFAR-10. 
This leads to the question of what the performance of the proposed method will be in situations where it is difficult to create an SDR.

2. Not only about a huge number of SDRs, non optimized iterative algorithm seems to require too much time and cost.  Your experiment dataset was MNIST, so optimization may have seemed easy.

3. Rather than using your algorithm, DINO [1] uses classwise clustering, and CAUSE [2] does semantic segmentation with unsupervised. I don't know the advantage of your algorithm when compared.

4. You tested proposed method on cognition capability task. But, raising such a problem does not seem persuasive.  I don't think it's enough to make readers understand why the problem is important in the field of deep learning. I think it would be good to give some examples. 

### Questions
Please see weaknesses above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an unsupervised learning algorithm inspired by cognition models. The algorithm focuses on generating constructive representations of the input space using Sparse Distributed Representations (SDRs). The authors compare their approach with K-Means and Invariant Information Clustering (IIC) algorithms and demonstrate its superior performance in both tabular and image datasets. They also evaluate the algorithm's cognition-like properties, showing its advantage over other clustering algorithms.

### Strengths
This paper introduces a representation-centric unsupervised learning algorithm that generates constructive representations.

### Weaknesses
1.	Lack of comparison with other state-of-the-art algorithms.
This paper only compares with K-Means and IIC. I suggest the authors to include comparisons with other recent unsupervised learning algorithms [cite1-7].

[cite1] He K, Chen X, Xie S, et al. Masked autoencoders are scalable vision learners[C]//Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2022: 16000-16009.  
[cite2] Carl Doersch, Abhinav Gupta, and Alexei A Efros. Unsupervised visual representation learning by context prediction. In ICCV 2015.  
[cite3] Mehdi Noroozi and Paolo Favaro. Unsupervised learning of visual representations by solving jigsaw puzzles. In ECCV, 2016.  
[cite4] Richard Zhang, Phillip Isola, and Alexei A Efros. Colorful image colorization. In ECCV, 2016.  
[cite5] Zhirong Wu, Yuanjun Xiong, Stella Yu, and Dahua Lin. Unsupervised feature learning via non-parametric instance discrimination. In CVPR, 2018.  
[cite6] Aaron van den Oord, Yazhe Li, and Oriol Vinyals. Representation learning with contrastive predictive coding. arXiv:1807.03748, 2018.  
[cite7] Ting Chen, Simon Kornblith, Mohammad Norouzi, and Geoffrey Hinton. A simple framework for contrastive learning of visual representations. In ICML, 2020


2.	Limited experimental evaluation. The experiments are conducted on a small number of datasets, and the evaluation could be expanded to include more diverse and challenging datasets.

3.	Memory requirements. The high memory costs associated with the algorithm need to be mitigated.

4.	The presentation quality needs to be improved. For example, writing needs to be polished and figures need to be more clearly.

### Questions
Please see the Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper discusses unsupervised learning for building cognition models. The proposed method consists of an embodiment, a primitive and a spatial attention modulator. The method is evaluated on three datasets: Wisconsin Breast Cancer, Pima Indians Diabetes, and MNIST.

### Strengths
- Unfortunately, I do not see any value in this submission.

### Weaknesses
- The paper is mostly incomprehensible. It fails to convey the central parts of the paper. Necessary background information is missing. It needs a major rewrite before it can be considered for publication.
- The experimental evaluation is insufficient: only three datasets where MNIST is the most challenging one. 
- Overall, the paper is of low quality (especially the figures are not helpful).

### Questions
Unfortunately, I cannot ask any questions as I did not understand what the authors were doing in this paper.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces a novel unsupervised learning approach inspired by cognition models, which constructs a distributed hierarchical structure in the input space without relying on specific data types. The proposed method outperforms current state-of-the-art techniques like K-Means for tabular data and IIC for image data, demonstrating better average performance and exhibiting cognition-like properties that even supervised learning methods lack.

### Strengths
Main contribution: Proposed algorithm can say "I don't know" about novel input. It doesn't assign novel inputs to the existed cluster.

### Weaknesses
1. Explain more detail about translating grey image to SDR. I can't understand how normalized input values are separated to bins. For example, MNIST dataset has 1 and 0 value. So, I can't understand how you divide input into bins.
Also, this translation to SDR looks like manual and specified to specific dataset such as MNIST. It seems difficult to extend your algorithm to high-resolution and diverse dataset even about CIFAR-10. 
This leads to the question of what the performance of the proposed method will be in situations where it is difficult to create an SDR.

2. Not only about a huge number of SDRs, non optimized iterative algorithm seems to require too much time and cost.  Your experiment dataset was MNIST, so optimization may have seemed easy.

3. Rather than using your algorithm, DINO [1] uses classwise clustering, and CAUSE [2] does semantic segmentation with unsupervised. I don't know the advantage of your algorithm when compared.

4. You tested proposed method on cognition capability task. But, raising such a problem does not seem persuasive.  I don't think it's enough to make readers understand why the problem is important in the field of deep learning. I think it would be good to give some examples. 

---

Minor
1. In the Figure 3 graph, y-axis boundary setting should consider reader convenience.

---

References

[1] Caron, Mathilde, et al. "Emerging properties in self-supervised vision transformers." Proceedings of the IEEE/CVF international conference on computer vision. 2021.

[2] Kim, Junho, Byung-Kwan Lee, and Yong Man Ro. "Causal Unsupervised Semantic Segmentation." arXiv preprint arXiv:2310.07379 (2023).


---

**Post Rebuttal**

Although the authors performed rebuttal, the reviewer would like to strongly recommend this paper be modified due to the following reasons:

(1) Only possible to Grey Image. Cannot validate ImageNet with Color-version. Therefore, high-dimensional feature naturally cannot be performed.

(2) In revision, there is a description of XX.X%.

(3) The author of DINO paper equal to be that of DeepSpectral. In other words, recent clustering method has been growing to Self-Supervised Learning since long days ago. (Previous Clustering: K-Means, Spectral, Recent Clustering Method: Self-Supervised Model (DINO, MAE, iBOT))

From these reasons, the authors of this paper should change the way introducing and holding a problem. I think the proposed method only performs in grey image, then it may be possible to conduct a task of only dealing with grey image such as medical task.

### Questions
Refer to Weaknesses

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
