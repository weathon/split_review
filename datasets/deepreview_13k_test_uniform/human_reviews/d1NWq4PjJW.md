# Gyrogroup Batch Normalization

- Decision: Accept
- Scores: 6, 6, 8, 8

## Abstract
Several Riemannian manifolds in machine learning, such as Symmetric Positive Definite (SPD), Grassmann, spherical, and hyperbolic manifolds, have been proven to admit gyro structures, thus enabling a principled and effective extension of Euclidean Deep Neural Networks (DNNs) to manifolds. Inspired by this, this study introduces a general Riemannian Batch Normalization (RBN) framework on gyrogroups, termed GyroBN. We identify the least requirements to guarantee GyroBN with theoretical control over sample statistics, referred to as pseudo-reduction and gyroisometric gyrations, which are satisfied by all the existing gyrogroups in machine learning. Besides, our GyroBN incorporates several existing normalization methods, including the one on general Lie groups and different types of RBN on the non-group SPD geometry. Lastly, we instantiate our GyroBN on the Grassmannian and hyperbolic spaces. Experiments on the Grassmannian and hyperbolic networks demonstrate the effectiveness of our GyroBN.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a new batch normalization method on Riemannian manifolds named GyroBN. GryoBN is a new batch algorithm on a class of algebras geometries named “pseudo-reductive gyrogroups”, which relaxes the left reduction law of a gryogroup as defined by [Ungar 2009]. The work generalizes prior work on batch normalization on Lie groups, such as LieBN [Chen et al., 2024b], and the SPD batch norm proposed by Brooks et al., 2019.

### Strengths
To me, the main contribution of the work is how it theoretically generalizes several prior work on batch norm for manifolds. The work generalizes LieBN [Chen et al., 2024b] and the SPD Batch norm proposed in [Brooks et al., 2019] to a wider class of geometries. While there have been some work such as [Lou et al., 2020] which propose general batch norm algorithms, it does not give control over sample statistics. Although the originality of extending prior work on gyrononreductive gyrogroups (as done by [Nguyen, 2022] to the proposed pseudo-reductive gryogroups) seems limited, it still appears to be an important extension.

### Weaknesses
While the paper provides experiments on Grasmannian and hyperbolic manifolds, it is not clear from the paper why empirically GryroBN outperforms prior work. Is there a theoretical reason why using gryodistance may outperform prior work that use geodesic distance for batch norm? I wish the paper would do a deeper analysis into this difference, and how it affects what the networks are learning. Here are some possible experiments that could strengthen the paper's analysis:
- The original reason behind batch norm for Euclidean neural networks is covariate shift. Can you show empirically that the baselines suffer from covariate shift, and that GryoBN reduces covariate shift? Even a result showing the opposite would be an interesting contribution to the geo DL community. 
- Another experiment is to analyze the condition numbers of network's layers. Is is true that GryoBN makes the outputs of the neural networks better conditioned?



Another weakness is that the paper does not analyze how efficient the proposed batch norm algorithm is compared to prior work. Prior work based on Karcher flow are known to be slow. It would strengthen the paper to include this analysis for the experiments on Grassmannian and hyperbolic spaces. I see that there is a table showing training efficiency in Appendix F.1.4, but it only a comparison to prior work without batch normalization, not other work that do use batch norm.

### Questions
- Is there a reason why the notations for the identity and left inverse different in Eq. 12 than the ones used in Section 2? Is Eq 12 equivalent to saying that $gry[ \ominus b, b] = e$?
- How efficient is the mean and variance calculation? Prior work based on Karcher flow are known to be slow. How does GyroBN’s speed compare to prior work?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper addresses the problem of extending batch normalization, which has accelerated deep learning in many areas, to non-Euclidean geometries, where the data lies on a Riemannian manifold. While computing mean and variance are trivial in Euclidean spaces, they become non-trivial in general Riemannian manifolds, because there is no analogue of addition that is associative, and would allow for an easy computation of the mean. The main goal is to extend the algebra for Riemannian manifolds, where mean and variance in the BN operator should be replaced by  Fréchet mean and Fréchet variance over the manifold. The main theoretical contribution of the work is unifying the analysis of some previous works that cover special cases of Riemannian manifolds, and extending them to some new types of Riemannian manifolds, so that batch normalization can be defined and computed. They go on to show the empirical value of their proposed method by testing newly developed Grassmannian network, GyroGr, with different types of batch normalization, and their proposed normalization improves the test accuracies. 

The paper builds on previous works that has addressed these problems for specific forms of Riemannian manifolds (Table 1). However, authors argue that a more general approach can combine these as special cases, thereby unifying the analysis. Furthermore, they introduce a more relaxed notion than earlier works, termed "pseudo-reductive gyrogroup" that encompasses previous works, but can admit new Riemannian structures due to its relaxed condition, such as Grassmannian manifolds. More specifically, they introduce the relaxed condition, pseudo-reductive, which replaces left reduction (G4) condition that is more stringent, which covers Grassmannian manifolds.

**Update**
In light of the other discussions as well as the explanations and clarifications by the authors, I'm happy to increase my score from 5 (marginally below acceptance) to 6 (marginally above the acceptance)

### Strengths
Normalization layers and in particular batch normalization have been key to success in training many modern architectures. However, when physical or mathematical constraints imply non-Euclidean geometries where data is on a manifold, computing mean and variance for BN becomes a non-trivial task. While one could take an ad hoc or heuristic approach, a more principled approach is likely to further our understanding and improve the state of the art in this field. 

This paper addresses this problem by studying a  relaxed set of properties, that admit a sufficiently rich algebra for computing mean and variance, and thereby a BN operator. This principled approach is certainly a welcome development.  To the extent that I could understand which was admittedly limited, the theoretical statements and assertions seem to be sound. Finally, in section 7 they present experiments mostly on GyroGr which is a Grassmannian network as a backbone, and compare it without BN, or with other types of BN, and show their proposed BN achieves the best results. While the empirical setup is sound, I cannot assess the significance of these results, given that they mostly focus on one network and one particular type of Riemannian manifold.

### Weaknesses
While this work seems to be on solid theoretical grounds and is mathematically sound, my main concern is the overall structure and writing, which make the theoretical contributions of the paper rather hard to grasp. I've added a few concrete suggestions that I believe would improve the readability of this paper. 

- An expanded preliminary on various concepts non-Euclidean geometry. While authors can assume that their readers is limited to those with deep and expert knowledge of this topic, such an assumption would narrow  the audience of this paper quite a lot. For reference, I spent >5 hours to try educate myself on some of the basics that I did not know before reading the paper, but besides "parsing" the theoretical statements, I could not gain a deeper insight. With an expanded preliminary that illuminates these concepts, I could have understood the results on a much deeper level. 
- Adding high level ideas : For theoretical contributions, it is always valuable to the reader to get a high level view of the ideas, techniques, or proof insights. In this particular case of Riemannian geometries, which presents itself as highly abstract, these types of explanations are even more crucial. 
- Adding concrete examples for abstract concepts: there are numerous technical terms, some classical and some introduced in the paper, that are left without any high level explanations, eg. gyrations, left gyroassociative law, left reduction law, pseudo-reductive gyrogroups, are all concepts that are formally introduced, but no high level explanations are given. So the reader is forced to just parse and compile the formal statements, which is not easy, unless they are already an expert on this topic. Would it be possible for authors to give concrete examples for each concept as they go along with their formal definitions and statements? For example, can they use a working example of a Grassmannian, and explain the rough geometric intuition behind each notion?  While that might not be easy in all cases, it would tremendously improve the readability and value of the paper.

### Questions
No questions.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a geometric neural network batch normalization operation that is based off of a proposed gyrodistance frechet mean.

### Strengths
1. The paper's method seems principled, and the derivations seem right to me.
2. The empirical results are reasonably convincing, showing good improvement over prior methods.

### Weaknesses
Overall, there are no major concerns from me. I believe that the paper is technically sound and complete, but the scope is rather limited and the overall contribution may ultimately be incremental (over prior Riemannian batch norm papers). Beyond that, I have two minor nitpicks:

1. A natural issue is that not all manifolds are gyrogroups. This means that the proposed method is not general. This is probably okay since most manifold methods are not general (by dint of the fact that it is hard to work on manifolds), but might affect some use cases that were not covered.
2. The empirical results are not very convincing. In particular, while they are controlled against other RBN methods, the base architecture is often weak/basic. I would like to see comparisons with other architectures (e.g. HNN++, Riemannian ResNet [1]). This may also be important since the architectures used are built solely from gyro-operations, and using different architectures could control for this confounding factor (gyro operations helping gyro operations).

[1] https://arxiv.org/abs/2310.10013

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper proposes a new Riemannian Batch Normalization (RBN), named Gyrogroup Batch Normalization. This new RBN method provides controllable means and variances and includes several previous RBN methods. To include the case of Grassmannian, this work proposes the pseudo-reductive gyrogroups that lie between the gyrogroup and the nonreductive one. Theoretical analysis regarding this new approach is provided with numerical verifications across several experiments.

### Strengths
The paper is well-written and well-structured and the comparisons with previous RBN methods are comprehensive. In particular, the comparison of assumptions is presented clearly. The theories seem solid and the performance is improved compared to the existing methods.

### Weaknesses
I suggest the authors provide a comprehensive version of Algorithm 1 to specify the calculation of each quantity or elaborate in the appendix.

### Questions
1. What is the computational complexity of GyroBN, and how does it scale with the input dimension compared to previous methods?

2. How do you predetermine the running mean, running variance, biasing parameter, and scaling parameter in Algorithm 1?

3. Can you provide any discussion if the gyrations are not isometric?

### Soundness
3

### Presentation
4

### Contribution
3
