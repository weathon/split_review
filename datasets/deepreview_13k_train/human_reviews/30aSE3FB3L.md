# Matrix Manifold Neural Networks++

- Decision: Accept
- Scores: 3, 8, 6

## Abstract
Deep neural networks (DNNs) on Riemannian manifolds have garnered increasing interest in various applied areas. 
For instance, DNNs on spherical and hyperbolic manifolds have been designed to solve a wide range of 
computer vision and nature language processing tasks.  
One of the key factors that contribute to the success of these networks is that spherical and hyperbolic manifolds 
have the rich algebraic structures of gyrogroups and gyrovector spaces. 
This enables principled and effective generalizations of the most successful DNNs to these manifolds.   
Recently, some works have shown that many concepts in the theory of gyrogroups and gyrovector spaces can also be generalized to matrix manifolds such as Symmetric Positive Definite (SPD) and Grassmann manifolds. 
As a result, some building blocks for SPD and Grassmann neural networks, e.g., 
isometric models and multinomial logistic regression (MLR) can be derived 
in a way that is fully analogous to their spherical and hyperbolic counterparts.  
Building upon these works, %in this paper, %we improve MLR on SPD manifolds, 
we design fully-connected (FC) and convolutional layers for SPD neural networks. 
We also %improve MLR on SPD manifolds, 
develop MLR on Symmetric Positive Semi-definite (SPSD) manifolds, 
and propose a method for performing backpropagation with the Grassmann logarithmic map 
in the projector perspective. 
We demonstrate the effectiveness of the proposed approach in the human action recognition and node classification tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposed a gyro space and gyro-vector based DNN on Grassmannian and SPD. The authors proposed formulation of building blocks like Convolution, Fully connected based on formulation derived in Nguyen, 2022a;b. The authors showed improved performance on human action recognition and node classification tasks formulated as on SPD and Grassmannian.

### Strengths
1. The paper is nicely motivated in the context of gyro vector representation.
2. The formulation of convolution and fully connected layers are nicely derived and formulated from Nguyen, 2022a;b.

### Weaknesses
1. The paper mostly based on formulation by Nguyen, 2022a;b. I don't want to treat this as a weakness, but a lack of strength.
2. The experiment results are rather naive, in recent years there is increasing literature in manifold DNNs so one wants to see thorough experimentations both in terms of different setting. Also some comparisons are missing including that with Chakraborty et al. (2020).



### Questions
The authors should elaborate what are the limitations in Chakraborty et al (2020) as they stated “Their proposed layers have nice theoretical prop- erties. A common limitation of the above works is that they do not provide necessary mathematical tools for constructing many essential building blocks of DNNs on SPD manifolds” without mentioning what mathematical building blocks are missing. A quick search reveals that same authors proposed other building blocks such as normalization using similar tools, please see “https://arxiv.org/pdf/2003.13869.pdf"
In 3.1, it is quite confusing why authors choose different notation to denote Grassmannian using different representations.
The authors should explain the abbreviation of the metrics on SPD like ai, le, lc used in section 3.1. For a general reader it will be easier to understand.
As FC layer can be treated as special case of convolution (with full kernel size), the authors should restructure the paper by defining convolution first, then the authors can just address FC trivially. 
It is not clear why authors suddenly defining MLR in section 3.3 on positive semi-definite matrices. The MLR for SPD (and trivially can be extended to SPSD ) by using formulation in  Nguyen (2022a)
What is the motivation behind using different metrics: “We use Affine-Invariant metrics for the convolutional layer and Log-Euclidean metrics for the MLR layer”?
What is rationale behind better performance using structure space representation as mentioned in “These results show that MLR is effective when being designed in structure spaces from a gyrovector space perspective.”? They should essentially represent same space, why the difference in achieving different optima?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes novel formulations of fully-connected and convolutional layers, as well as MLR, on the SPD manifold based on gyrovector calculus.

### Strengths
The paper is well written, easy to follow, and the mathematics appear sound. The theoretical contributions are extensive and significant, with the potential of impacting research on matrix manifold neural networks in different areas.

Showing how to compute the Grassman logarithmic map in a differentiable way is another contribution.

The experimental evaluation for action recognition includes existing SPD deep learning methods and shows improvements.

### Weaknesses
The formulation of convolutional layers is more like a sketch of the proof than an actual definition. The description lacks sufficient detail to understand the precise operations performed, particularly how the concat_spd operation is applied and how the resulting tensors are used in the gyrovector calculus. For example, it's unclear how the spatial arrangement of the input SPD matrices is handled during the convolution. Is there a sliding window approach, and if so, how is the gyrovector calculus applied within each window? This needs to be explicitly defined.

The experimental evaluation for node classification as shown in the main text is fairly weak: the authors did not include any baseline, at least a few Euclidean-featured GNNs should have been included, as well as hyperbolic graph neural networks (Chami et al., and newer architectures). The absence of these comparisons makes it difficult to assess the true performance of the proposed method relative to established approaches. The lack of a standard Euclidean baseline makes it hard to ascertain if the performance gains are due to the manifold structure or simply the architecture. The comparison to hyperbolic methods is crucial to understand if the proposed method is competitive with other non-Euclidean approaches.

There is actually no definition of what GyroSpd++ in the paper beyond a description of the matrix dimensions. Likewise, Gr-GCN is not properly defined in the experimental evaluation. Overall, this makes it difficult to understand the full network design and what is being evaluated. The lack of precise definitions for these architectures makes it impossible to reproduce the results or to compare them with other methods. The description should include the specific layers, their parameters, and the flow of data through the network.

### Questions
What non linearities were used? Is it a classical ReLU applied on the manifold, in the tangent space, or a specifically adapted rectifier such as those typically used with SPD deep nets, e.g., to inflate the small eigenvalues?

Can the authors restructure the text to improve the flow of the exposition and the introduction of the networks for the experimental evaluation?

As it stands, a lot of the content is in the supplementary.

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- This paper discusses the design of deep neural networks (DNNs) on matrix manifolds, specifically Symmetric Positive Definite (SPD) and Grassmann manifolds.
- This paper mathematically proposes a way to compute the Fully Connected layers and Convolutional layers for SPD matrices. 
- The paper also presents a method for performing back-propagation with the Grassmann logarithmic map in the projector perspective for Grassmann manifolds.
- Experiments are designed in human action recognition and node classification tasks, while both are very small datasets.
- The paper tries to address limitations of existing works and provides necessary mathematical tools for building DNNs on SPD and Grassmann manifolds.

----
I've read the rebuttal and would like to slightly increase the rating.
Thanks.

### Strengths
- The paper builds upon the theory of gyrovector spaces and extends it to matrix manifolds such as SPD and Grassmann manifolds.
- This paper defines a new way to build the basic blocks of neural networks - fully-connected and convolutional layers, for SPD matrices, and most specially for Grassmann, which is rarely discovered in the field.
- The authors demonstrate the mathematical rigor and effectiveness of their approach.
- The authors provide an ablation study and comparison against state-of-the-art methods, further validating the effectiveness of their approach.

### Weaknesses
 - The experimental evaluation is based on some small and not generally used dataset, (not as big as ImageNet or equivalent). This limits the overall generalizability of the proposed approach.
- The network structures are limited with FC and CNN in most cases, while other network structures are missing, such as attention/ activation/ etc.
- It would be helpful if the author can clearly highlight the novel contributions and how they differ from or improve upon the existing theories discussed in other papers, for example [1,2,3,4]. Most of these existing papers discussed the building blocks of SPD network/ Grassmann network/ etc. Some other paper discussed other manifold such as Hyperbolic [5,6].



### Questions
- What is the main difference between this paper and other existing manifold network?
- The author mentioned "our convolution operation can be used for dimensionality reduction", can you explain this more? From my understanding, if the input is NxN SPD matrix, the output has to lie within this NxN space. So I'm a little confusing about the reduction.
- Some tiny comments, the author defined exp(P) and log(P) but seems not use this annotation at all.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
