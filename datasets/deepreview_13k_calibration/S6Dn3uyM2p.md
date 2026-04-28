# Differentially Private One Permutation Hashing

- Decision: Reject
- Avg Score: 4.60
- Scores: 5, 5, 3, 5, 5

## Abstract
Minwise hashing (MinHash) is a standard algorithm for large-scale search and learning with the binary Jaccard similarity. One permutation hashing (OPH) is an effective and efficient alternative of MinHash which splits the data into K bins and generates hash values within each bin. In this paper, we combine differential privacy (DP) with OPH, and propose DP-OPH framework with three variants: DP-OPH-fix, DP-OPH-re and DP-OPH-rand, depending on the densification strategy to deal with empty bins in OPH. A detailed roadmap to the algorithm design is presented along with the privacy analysis. Analytical comparison of our DP-OPH methods with the DP minwise hashing (DP-MH) alternative is provided to justify the advantage of DP-OPH. Experiments on similarity search confirms the merits of our proposed DP-OPH algorithms, and provide guidance on the choice of proper variant in different practical scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers making a version of min-wise hashing algorithm differentially private. 

Minwise-hashing is a well know algorithm for estimating Jaccard Similarity between large sets. Jaccard similarity is a widely used similarity measure in many situations including document similarity. In the standard scheme, to improve quality, multiple random permutations need to be used to get multiple hash values. One Permutation Hashing (OPH) is a variant that uses just one random permutation to generate multiple hash values and hence reduces complexity. 

The main contribution of this paper is making OPH differentially private (in the Dwork et al DP framework).   They give DP OPH for three versions of OPH what the authors call OPH with fixed densification and OPH with re-randomized densification (densification is a technique to deal with "empty bin" problem that arise in OPH), and OPH with Random bits. The authors also experimentlaly evaluate their   algorithms.

### Strengths
The main strength is that the paper considers DP version of a very practical algorithm and hence could be of use where privacy is important. The paper also experimentally evaluate their algorithm.

### Weaknesses
 The methods seem to be straight forward and hence scientific content appears not that substantial.

### Questions
I do not have any questions at this point.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This manuscript proposes DP-One Permutation Hashing, which (the hashing itself) is an improved approach of the minwise hashing that is used for Jaccard similarity estimation. The DP-OPH framework has three variants based on different densification approaches. And the main technique is the randomized response tailored to the hash values. The analysis is given for the approximate-DP guarantee. To establish a comparison, DP-Minwise Hashing is also discussed, however experimental results show that DP-OPH outperforms DP-MH very frequently.

### Strengths
1. In general, the paper is well-written with clarity. The related work is carefully discussed.
2. Recently there are more increasing interest in studying DP for hashing, sketching, etc. This work contributes to the developing topic.
3. Algorithms for three densification approaches are discussed, and this work further fixed a small error of previous work. The correctness should be OK. -- I checked 60% of the proof and skip the rest due to the timeline. But I am happy to come back to it should there be any concern.

### Weaknesses
1. My major concern is the missing analysis of the utility. From what I read, the DP guarantee is shown but the utility is justified by experiments.  It is somewhat an incomplete work if no upper/lower bound on the utility is discussed, and further weaken the some of the experimental results. For example: Though the proposed DP-Minhash and DP-OPH are similar at a schematic level, it is unfair if the DP-MH is not the optimal algorithm however DP-OPH is. I will say more in the questions section.

2. The technique seems to be randomized response mechanism -- it is quite naive.

3. There should be discussion on pure-DP.

### Questions
1. What is $J$ in the equation after equation 2 on page 3?
2. In the section of __Privacy statement and applications__, it is mentioned the privacy model is "attribute-level". Are there other privacy models for this type of problem? (Such as node/edge level privacy for graphs)
3. Corresponding to the major concern. I briefly checked two previous papers on this topic and really appreciate it if the authors help me understand why the analysis of utility is not available in this work. In [2], it is claimed that One Permutation Hashing outperforms Minwise Hashing, and the theoretical analysis includes two lemma on page 5: Lemma 1 says the expected number of 'jointly empty bins' has an upper bound; Lemma 2 says the estimator of the resemblance is unbiased. Would you please explain intuitively how these two analysis show the better utility?
4. To continue, in [1], where there is a small error of probability distribution fixed in this paper, the authors gave utility analysis. Looking at lemma 5 and theorem 2 on page 6 (arxiv version), the upper bound of additive error seems to be $O(\frac{1}{\sqrt{n\varepsilon}})$ by taking $\alpha =1, \tau = n$ if I did not misunderstand. Why cannot we do a similar analysis on the algorithms proposed here?

Minor: Maybe explicitly state the randomized response mechanism in the preliminary.

[1] Differentially Private Sketches for Jaccard Similarity Estimation.
[2] One Permutation Hashing

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The Jaccard similarity is a measure that allows to compute the amount of items that two parties have in common. It is widely used to compute the similarities of two entities or individuals (e.g. preferences, genomes). Since its exact computation is expensive, it is commonly estimated via sketches such as Min-Hash (MH) and One Permutation Hash (OPH). An interesting problem is to provide privacy preserving estimations in order to hide sensitive information when the data of individuals is involved. 

The proposed work addresses the privacy preserving computation of Jaccard estimations. It proposes privacy preserving versions of different variations of OPH and MH, proves their differentially private guarantees and compares their accuracy under different parameters.

### Strengths
I think that obtaining privacy preserving Jaccard distance estimations is an interesting problem. 

The paper has properly addressed its claims by providing proofs of privacy and extensively evaluating their results. 

Key aspects of the contribution have been in general well presented.

### Weaknesses
However, I found several problems that I list below. 

1- Impact of the results: all algorithms are proven private, but their privacy-accuracy tradeoffs do not seem widely applicable in practice. The evaluation of Section 4 shows that estimations are accurate for only very large values of $\epsilon$ (i.e. between 10 and 50) and therefore a large privacy loss. A partial exception is DP-OPH-rand, which shows fairly better accuracy already when $\epsilon$ reaches 5. However, I its behavior is not clear since plots focus on a larger scale and we cannot see in detail what is happening in the range [0.1, 10].  The practical utility of the proposed methods is questionable, as the accuracy at lower privacy budgets (e.g., $\epsilon < 5$) is not sufficiently high for many real-world applications. For instance, in scenarios where Jaccard similarity is used for tasks like near-duplicate detection or recommendation systems, the high error rates at low $\epsilon$ values would render the results unusable. The paper should include a more detailed analysis of the error rates at lower $\epsilon$ values, perhaps with a zoomed-in view of the plots, and discuss the practical implications of these error rates for different use cases.

2- Novelty: I do not find substantial novelty in the work. The application of randomized response to MH sketches is already present in Aumüller et al. (2020). It is true that the authors found a mistake on the proof of this related work and corrected it, but as said in the paper, this mistake is minor. It seems that the application of these ideas to the proposed OPH variations do not have substantial changes. If the authors could clearly explain the novelty in the content of their proofs with respect to Aumüller et al. (2020), I will take this point back and re-asses my score. The core idea of applying randomized response to the hash outputs, while effective for achieving differential privacy, is not a novel contribution in itself. The extension to OPH variations, while requiring some adaptation of the proofs, does not introduce a fundamentally new approach. The paper should more clearly articulate the specific technical challenges overcome in the proofs for OPH, and how these differ from the existing work on Min-Hash. A more detailed comparison of the proof techniques, highlighting the novel aspects, would be beneficial.

3- Clarity: Even if I think the paper is overall well presented, it still requires more clarity in the technical sections. 

3a- The degree of "locality" of the DP guarantee could be more clearly explained. In the contribution, there is no need to trust a central party to take two vectors and output a noisy estimation of its Jaccard distance as it would be needed in central DP. Clarifying this aspect would also help to better motivate the scope of application of the result. The paper should explicitly state that the proposed methods provide local differential privacy, where the randomization is applied directly to the individual hash outputs, rather than requiring a trusted aggregator. This distinction is crucial for understanding the privacy model and its applicability in decentralized settings. The paper should also discuss the implications of this local privacy model, such as its robustness against collusion and its limitations compared to central DP.

3b- The results presented in Section 3.2 of the paper are not always self contained and could be better presented.

### Questions
Please comment on points 1 and 2 raised in as weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes differentially private versions of Min-wise Hashing One Permutation Hashing. By restricting the hash values to b-bit integers, the proposed algorithms achieve differential privacy by applying the randomized response technique over the finite space of output values. The numerical performance of proposed algorithms is validated on real data sets.

### Strengths
* The proposed algorithms are intuitive and easy to understand/implement.
* The author(s) took care to define their notion of neighboring data sets and the implied privacy guarantees ("attribute-level").
* There is an extensive set of numerical experiments on real data sets.
* The concise introduction to Min-wise Hashing and One Permutation Hashing allow readers who are unfamiliar with the field to quickly pick up the necessary background and understand the problems studied by this paper.

### Weaknesses
 * Lack of utility analysis. As motivated in the introduction, hashing is frequently for the purpose of approximately calculating the similarity between two high-dimensional binary vectors. The paper also mentions the bias and variance of non-private estimators of the Jaccard similarity. However, except in Section A of the Appendix, there is not much mention of how the estimation accuracy, using the proposed hashing methods, depends on the privacy parameters, dimension of data, number of bins, etc. The discussion in Section A is also limited in two ways: (1) the variance analysis is only empirical; (2) it only considers replacing the non-private hash values in a specific estimator defined in equation (2) by private hash values, while there is no clear justification given for why this particular estimator is still the best candidate for private estimation of Jaccard similarity. Some utility analysis can be very useful for assessing the proposed algorithms in their own right, or relative to existing methods. For example, one advantage of this paper's set up, as suggested at the end of Section 1.2, is that it makes no assumptions about whether hash functions are kept private. However, without understanding the cost of this generality, potential users may still have difficulty in choosing between competing methods of DP hashing.

* Some gap in motivating One Permutation Hashing and b-bit coding. The paper mainly studies One Permutation Hashing with hash values restricted to b-bit integers, but the justifications for these choices appear somewhat ambiguous, especially to readers without much background in this topic. For example, it would be helpful if the last sentence of the first paragraph in Section 3.1 can include some more details (why unstable? violating the triangle inequality with respect to which metric?). For another example, restricting hash values to b-bit integers appears to be crucial to the DP algorithms (otherwise, the randomized response mechanism may not apply), however the paragraph on b-bit coding on page 3 feels rushed and leaves out some important details (without considering privacy yet, is there any accuracy loss by restricting to b-bits? How is b usually chosen? Is b-bit coding convenient, or rather, necessary for DP hashing?)

### Questions
In addition to the questions mentioned in "weaknesses":

* On the usefulness of "attribute-level" privacy, is there any application of hashing/Jaccard similarity where it is more natural to consider the entire D-dimensional vector, as opposed to one coordinate of the vector, as the data of "one individual"?

* In the DP literature, it is customary to set $\delta$ to be smaller than 1 divided by the data set's size ($1/D$ in the case of this paper). What value of $\delta$ do you recommend in general, and what is its relationship to $1/D$?

* Does your approach require that the dimension $D$ is fixed and/or public information? Strictly speaking, the notion of DP also allows adding/deleting one record from the data set, as opposed to merely replacing one record and keeping the data size unchanged.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies differentially private minwise hashing (MinHash) algorithms as variants of the one permutation hashing (OPH) algorithm. Three DP variants are introduced in the paper, DP-OPH-fix, DP-OPH-re and DP-OPH-rand. The authors show that these variants can provide attribute-level DP guarantee with in-depth examination and utilization of the nature of OPH. Some experiments show that the proposed three variants can outperform the straw-man algorithm (DP-MH), and DP-OPH-rand and DP-OPH-re have advantages in different privacy strengths.

### Strengths
1. The paper designs three different variants of differentially private minwise hashing (MinHash) algorithms.
2. The proof for deciding how the privacy budget should be split demonstrates an in-depth analysis of the nature of OPH, and it can be inspiring for the study of DP on other sketches.
3. The paper provides theoretical analysis and some empirical evidence to support the superiority of the proposed algorithm.

### Weaknesses
1. The attributed-level DP seems to relatively weak in terms of privacy protection. For example, when one attribute in MNIST data used in the experiment is just whether a pixel value is zero, ensuring such attribute level indistinguishability may provide only limited privacy protection.  Specifically, the paper's attribute-level DP definition, which considers neighboring datasets differing by a single attribute, might not sufficiently protect against inferences based on combinations of attributes or more complex data manipulations. The example of a single pixel being zero or not in MNIST is a good illustration of this, as an adversary could easily combine multiple pixel attributes to reconstruct a significant portion of the original data. This raises concerns about the practical privacy guarantees offered by the proposed approach.
2. While there is no theoretical utility guarantee shown, it is also hard to evaluate the empirical effectiveness of the proposed algorithm because (a) the non-private baseline is missing (b) it is not clear what it means to downstream machine learning tasks given such precision.  Without a non-private baseline, it's difficult to quantify the utility loss incurred by the DP mechanisms. The paper needs to show how much the accuracy of a downstream task is degraded due to the privacy constraints. Furthermore, the paper does not clearly specify what downstream tasks would benefit from the proposed method and how the precision of the Jaccard similarity approximation translates to the performance of such downstream tasks. The lack of clarity on the practical implications of the proposed method makes it hard to assess its real-world value.
3. While attribute-level DP is already a weaker privacy notion, the empirical results show that it requires $\epsilon>5$ to achieve some acceptable precision. Also, any $\epsilon > 20$ can provide extremely limited privacy protection and usually will not be considered in privacy literature. The high $\epsilon$ values required to achieve reasonable utility suggest that the privacy-utility trade-off is not very favorable. The privacy guarantees offered by the proposed methods are quite weak, especially when $\epsilon$ exceeds 20, which is often considered insufficient in the privacy community. The paper should discuss the implications of such high $\epsilon$ values and whether the proposed methods can be improved to provide better privacy-utility trade-offs.
4. The writing of the paper can be improved. For example, $\tilde{f}$ in equation (3) and $N_{emp}$ are never introduced in the main text, which harm the integrity of  the main text. The lack of clarity in the definitions of $\tilde{f}$ and $N_{emp}$ makes it difficult to follow the technical arguments in the paper. These terms are crucial to understanding the proposed method, and their absence in the main text is a significant oversight. The paper should ensure that all key terms and notations are properly defined in the main text to enhance clarity and readability.

### Questions
1. What is the non-private OPH performance on the same datasets?
2. How useful are the retrieved samples to the downstream tasks with the shown precision?
3. Is it possible to strengthen the protocol to be sample-level DP? What may be the key challenge?
4. Is there any theoretical performance guarantee for the DP OPH algorithms? 
5. How tight is the proposed privacy splitting compared to the existing sequential composition techniques (e.g., Renyi DP)?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
