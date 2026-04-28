# The polytopal complex as a framework to analyze multilayer relu networks

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5

## Abstract
Neural networks have shown superior performance in many different domains.
However, a precise understanding of what even simple architectures actually are
doing is not yet achieved, hindering the application of such architectures in safety critical
embedded systems. To improve this understanding, we think of a network
as a continuous piecewise linear function. The network decomposes the input space
into cells in which the network is an affine function; the resulting cells form a
polytopal complex. In this paper we provide an algorithm to derive this complex.
Furthermore, we capture the local and global behavior of the network by computing
the maxima, minima, number of cells, local span, and curvature of the complex.
With the machinery presented in this paper we can extend the validity of a neural
network beyond the finite discrete test set to an open neighborhood of this test set,
potentially covering large parts of the input domain. To show the effectiveness of
the proposed method we run various experiments on the effects of width, depth,
regularisation, and initial seed on these measures. We empirically confirm that
the solution found by training is strongly influenced by weight initialization. We
further find that under regularization, less cells capture more of the volume, while
the total number of cells stays in the same range. At the same time the total number
of cells stays in the same range. Together, these findings provide novel insights
into the network and its training parameters.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper analyzes the ReLU-based MLP (piecewise linear activation functions) by viewing their layer representations as polytopes. Based on the analysis, an algorithm is proposed to decompose trained NN into polytope sets and then align them with the training/testing data to assess the performance, which seems to be a single-dimension regression error using MSE. The theoretical analysis specifically focuses on several properties of polytopes, aligning them with the behaviors of NNs. Four typical target functions with different structures and characteristics on polytope separations of input space are used for testing the proposed algorithm. This work is new to the best of the reviewer’s knowledge, but the reviewers have concerns regarding presentation quality and completeness.

### Strengths
•	The idea is new in that 1) using a set of polytopes to represent ReLU-based MLP for geometric understanding of layer compositions, and 2) using the polytopes to separate training or testing data points for final outputs.

•	The visualization to align trained NNs with polytope representation is well-understood.

•	The theoretical analysis is not limited to shallow alignment, but translating the properties of polytopes into behaviors of NN layers.

### Weaknesses
The reviewer has doubts about the motivation of this work considering the following:

•	What is the purpose of using polytope representation to analyze NNs? While piecewise linear functions are a characteristic of ReLU networks, the connection to properties like strong convexity is not clearly established. The paper needs to elaborate on why a polytopal view is superior to other analyses, such as examining the Hessian for convexity or directly analyzing the piecewise linear nature of the function. The current justification is insufficient to motivate the complexity of the proposed approach.

•	Is the theory only for ReLU-based MLP? While piecewise linear is mentioned, the paper should clarify the scope of the theory. It is not clear if the theory applies to other piecewise linear activations beyond ReLU and Leaky ReLU. The paper needs to discuss the limitations of the theory when applied to activations with more complex nonlinearities, like ELU, and whether approximations are needed, and if so, how these approximations affect the analysis.

Regarding clarity and completeness of the work:

•	At the beginning of the Introduction, while the example and Figure 1 catch the eye, the explanation is vague, e.g., what is the “symmetry of the data” and what is the difference between the right two plots so that you prefer the right one? The concept of 'symmetry' needs to be defined more rigorously in the context of the data and the network's representation. The preference for the right plot should be justified with more concrete arguments, rather than relying on visual intuition. The paper should explain how the polytope structure in the right plot is more desirable for the task.

•	“Assess the network” seems to be the target, but it’s unclear what metrics are used to quantify which commonly focused capability of NNs. The paper needs to specify what aspects of the network are being assessed and what metrics are used to quantify these aspects. For example, is the assessment focused on generalization, robustness, or some other property? The lack of clarity on the assessment criteria makes it difficult to evaluate the significance of the results.

•	The algorithm and theoretical analysis mainly discuss the properties of polytopes without sufficient transitions and demonstrations of the NN representation. The paper should provide more concrete examples and explanations of how the theoretical properties of polytopes translate into the behavior of the neural network. The connection between the polytope analysis and the actual neural network performance is not clearly established.

•	Four typical target functions are used for testing, each with two inputs. While these toy examples are useful for initial analysis, the paper needs to discuss the scalability of the approach to higher-dimensional inputs and more complex network architectures. The paper should also discuss the limitations of using only toy examples and how the results might generalize to real-world applications.

### Questions
Please refer to the bullet points in Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper proposes an algorithm that decomposes the input space of a ReLU MLP in convex polytopes. This algorithm allows for analyzing such neural networks beyond validation points, including properties such as curvature, hyperplanes, and stars.

### Strengths
Interesting research direction; Figure 8 looks awesome.

### Weaknesses
I am not familiar with this line of research, so I lack the expertise to judge the novelty of this paper, and I apologize for potential misunderstandings in advance.

1. Motivation:
- This paper presents some cool results, but it is still not clear to me why the community would benefit from the polytopal analyses. Furthermore, all analyses are on toy problems that fit closed-form functions. The paper does not adequately explain the practical utility of decomposing the input space into convex polytopes for ReLU MLPs. The current examples, while illustrative, do not demonstrate how this decomposition provides insights beyond what can be obtained through standard analysis techniques. The connection between the geometric properties revealed by the decomposition (such as curvature, hyperplanes, and stars) and their implications for real-world performance is missing. This makes it difficult to assess the significance of the proposed method.
- One good way to clear up this confusion would be to apply the proposed method on some real-world classifiers (such as ResNet for image classification, or some simple MLPs for various real-world smaller tasks), show that the polytopal analyses reveal properties of the learned neural network that could not be found with existing methods, and discuss how these properties affect real-world applications. The lack of experiments on real-world datasets and models is a major limitation. The paper needs to demonstrate that the proposed method can uncover non-trivial properties of neural networks trained on complex, high-dimensional data.

2. Comparison with existing works:
- Line 444 (Humayun et al. (2023) works only for two dimensional inputs) -- the experiments in this paper also considers two dimensions, and Line 134 says "we only investigate curvature only for the two-dimensional case." The comparison with Humayun et al. (2023) is not sufficiently detailed. While the authors mention that their method works for higher dimensions, the experiments primarily focus on two-dimensional cases, similar to the cited work. The paper needs to clarify the specific advantages of their approach over existing methods, especially in higher-dimensional settings where the computational complexity of polytopal analysis may become a limiting factor.

3. Other weaknesses:
- Although Figure 8 is nice, it lacks legend and axis labels. The lack of axis labels and a legend in Figure 8 makes it difficult to interpret the results. The figure is visually appealing but lacks the necessary information to understand the underlying data and its significance. This oversight hinders the reproducibility and understanding of the experimental results.
- Typo: Line 150 -- MLP->MPL.
- Typo: Line 234 -- the final "s" in the word "assess" is missing, making it borderline NSFW ;)
- Typo: Line 318 -- the the.

### Questions
- Line 235 (checking can further check if any derived vertex lies outside of the input cube) -- what does this mean?
- Why do we need the validity checks in Section 3.2? Does the proposed algorithm not guarantee the validity of its results? If the validity checks fail, what do we do?
- Line 429 (Balestriero & LeCun (2023) has some similarities to our algorithm but differs in scope) -- how is the scope different?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper is motivated by the fact that not all activation regions contain training data. The work can be divided into two parts. In the first part, the authors introduce a variation of Region Subdivision algorithm that allows them to use both H- and V-representations of the cells in the polyhedral complex produced by ReLU networks. In this part they also provide a thorough analysis of the algorithm, most notably, in regards to validity, and timing. In the second part, they leverage the obtained decomposition for various analyses, such as analyzing the cell volume, star volume and curvature. They also analyze the impact of width, depth, and regularization parameters on the computation time and number of cells.

### Strengths
1. The paper reads well. The flow between the sections and paragraphs is smooth. Some Figures need minor improvement for better clarity, but in overall they are well thought through. I particularly like the usage of level sets, as they make visualizing the three dimensional functions much clearer, and, as far as I know, it's not a very common approach in this field.
2. I really enjoyed Section 3.2. It is absolutely necessary to validate the polyhedral complex obtained by our algorithms, yet, as far as I know, this is the first work that actually mentions the steps taken to ensure validity. This is a good step towards more trustworthy methodologies.
3. Great analysis of the decomposition time in Figures 5 and 6. It is known that computing the polyhedral complex is tremendously computationally intensive, yet not many works provide detailed runtime analysis-only other work I know of that does something similar is the work of Serra et al. (2018), although their analysis is less detailed.
4. As far as I know, this is the first work to show the impact of regularization on the number of activation regions.
5. The motivation behind the paper is really interesting. I agree with the authors that there is a “need for methods which extend the validity of networks beyond the test data”. This also fits the data-driven principles perfectly, and might allow for more informed data augmentation/pruning strategies in the future if this method is extended to real world applications.

### Weaknesses
# Inconsistent story

In the *Motivation* paragraph of Section 1 the authors mention that this paper is motivated by a need for methods that extend the validity of networks beyond the test data. Despite that, this is not the main focus of the later sections. It appears to me that the motivation does not match the paper. Authors later state that “this paper extends the validity of a neural network beyond a discrete test data point to its neighbors”. I don’t believe that this paper actually meets that claim. After reading the *Introduction* I expected to see experiments showing me how we can perform testing beyond the test set, and how it changes the perceived generalization capabilities of a model.  However, there are no such experiments in this work. To me, the paper focuses more on investigating properties of linear regions, rather than extending testing beyond the test set. 

I expect the authors to rewrite the Introduction so that it fits the rest of the paper, and doesn’t make any false claims. To reiterate, in its current form, the paper only shows that it is theoretically possible to extend the testing beyond the test set, and that stars of a polyhedral complex could be used for that. However, there is no explicit algorithm proposing this extension, neither are there any experiments showcasing the validity of that extension, despite Section 1 hinting that it's the main focus of the paper,

# Poor literature review

The literature review of the field of linear/activation regions is practically nonexistent. The authors missed several essential works from the field of activation/linear regions. Below I list the most influential ones that I would expect to be referenced by any paper in this field. 

[1] Hanin, B., & Rolnick, D. (2019, May). Complexity of linear regions in deep networks. In International Conference on Machine Learning (pp. 2596-2604). PMLR.

[2] Wang, Y. (2022, July). Estimation and Comparison of Linear Regions for ReLU Networks. In IJCAI (pp. 3544-3550).

[3] Liu, Y., Cole, C. M., Peterson, C., & Kirby, M. (2023, September). ReLU neural networks, polyhedral decompositions, and persistent homology. In Topological, Algebraic and Geometric Learning Workshops 2023 (pp. 455-468). PMLR.

[4] Arora, R., Basu, A., Mianjy, P., & Mukherjee, A. (2018). Understanding deep neural networks with rectified linear units. ICLR.

[5] Serra, T., Tjandraatmadja, C., & Ramalingam, S. (2018, July). Bounding and counting linear regions of deep neural networks. In International conference on machine learning (pp. 4558-4566). PMLR.

[6] Raghu, M., Poole, B., Kleinberg, J., Ganguli, S., & Sohl-Dickstein, J. (2017, July). On the expressive power of deep neural networks. In international conference on machine learning (pp. 2847-2854). PML.

[7] Novak, R., Bahri, Y., Abolafia, D. A., Pennington, J., & Sohl-Dickstein, J. (2018). Sensitivity and generalization in neural networks: an empirical study. ICLR.

[8] Gamba, M., Chmielewski-Anders, A., Sullivan, J., Azizpour, H., & Bjorkman, M. (2022, May). Are all linear regions created equal?. In International Conference on Artificial Intelligence and Statistics (pp. 6573-6590). PMLR.

[9] Hanin, B., & Rolnick, D. (2019). Deep relu networks have surprisingly few activation patterns. Advances in neural information processing systems, 32

[10] Zhang, X., & Wu, D. (2020). Empirical studies on the properties of linear regions in deep neural networks. ICLR.

[11] Croce, F., Andriushchenko, M., & Hein, M. (2019, April). Provable robustness of relu networks via maximization of linear regions. In the 22nd International Conference on Artificial Intelligence and Statistics (pp. 2057-2066). PMLR.

[12] Xiong, H., Huang, L., Yu, M., Liu, L., Zhu, F., & Shao, L. (2020, November). On the number of linear regions of convolutional neural networks. In International Conference on Machine Learning (pp. 10514-10523). PMLR.

## Minor issues stemming from poor literature review

1. [3] already showed that adjacent activation regions differ in only one bit of their activation sequence, which the authors mention in L232, and so should be correctly cited. 

2. Until Section 3 it is unclear if the authors work on activation or linear regions. $C_k = \text{conv} (v_1, ..., v_p)$ requires convexity, which doesn’t hold for linear regions as mentioned by [9], so for clarities sake authors should clarify which regions they focus on early in their work.

# Novelty
Frankly, I am unsure whether the paper is novel enough to be accepted to a venue like ICLR. The algorithm in Section 3.1 is an incremental modification of the classical Region Subdivision algorithm. The validity and time checks are a pleasant addition to the paper (compared to relevant literature), but they do not provide significant novelty. Similarly, other contributions that I praise in *Strengths* are new but do not feel novel enough to me to deem acceptance to ICLR.  My opinion on novelty would significantly change if the authors performed experiments in which they “extend the discrete training data set to a neighborhood given by the union of the cells, and show experimental results”, rather than showing that it is theoretically possible. I believe that this would be a very strong and novel contribution. Especially, if the authors managed to generalize this outside of toy datasets (possibly by employing approximations or taking a scenario from embedded systems or virtual sensors mentioned in Section 6). I believe that without this, the work would not be of interest to the wider research community.

Consequently, a possible future direction that the authors can take is proposing and implementing an algorithm that extends testing beyond the test set. Analytically computing the polyhedral complex in large datasets (or even on MNIST) is absolutely unfeasible. However, I think that the authors could estimate the neighboring linear regions using linear search (monitoring changes in activations along a random vector from a data point). This would allow them to extend both the training and test sets. Both could be used for measuring robustness, while the latter could be used for achieving more thorough accuracy (it’s important to find if incorporating these new test point has any effect on the perceived accuracy and robustness though).

# Potential improvements in clarity (minor)
Here I propose few changes  that could be implemented to further improve clarity (please consider these as simply suggestions rather than requests for change):
 1. Not all readers will be acquainted with topology, and visualizing what a star is would allow for easier reading.
 2. There are typos in Lines 134, 150, 235-236, 265, 266
 3. In L150 authors do not mention which appendix to go to.
 4. Wouldn’t it be easier to visualize the Himmelblau and Griewank functions rather than explaining them?
 5. The Figures 4 and 5 don’t specify the unit for time. Figure 4b has the wrong ylabel. The digits in the yellow cells of Figure 6 are unreadable.
 6. What are $\rho$ and $\nu* from L128?
 7. It would be great to provide a few sketches that would simplify understanding of the algorithm from Sec. 3 for readers that are new to the field, especially for ($\alpha^3$) which is very confusingly written.

# Summary
I believe that in its current state the paper should be rejected. However, if the authors address my issues regarding *Inconsistent story* and *Poor literature review* I am happy to increase the rating of the paper. However, my rating is unlikely to change beyond boundary reject (5). In my opinion, for this paper to introduce a strong contribution to the research community the authors should expand it towards extending the testing beyond the test set with some experiments showing the applicability of this new technique (ideally beyond toy datasets).

### Questions
# Clarification
1. What did the authors mean in L369-370 (“Further, looking at … interpolating the data.”)?
2. What did the authors mean by “until the training collapses” in L414?
# Curiosity
1. The idea behind motivation made me think about robustness. I know that currently the setting is closer to regression than classification. Have the authors thought about generalizing to classification? I think it would be interesting to see the relation between the robustness of an activation region and the number of samples it contains (as I mentioned in the Weaknesses when proposing a possible future direction).

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper considers neural networks with linear layers and ReLU activation function. In this case, the network is a continuous piecewise linear function and the input space can be decomposed into cells in which the network is an affine function for each cell. The authors provided an algorithm to compute the polytopal complex formed by such cells of a neural network. By this decomposition, they can compute several statistics, such as the maxima, minima, number of cells, local span, and curvature of the network. They also provide several empirical results for some functions such as the Himmelblau function and the Griewank function.

### Strengths
1. This paper provides a novel algorithm to compute the polytopal complex of a neural network.
2. From the obtained polytopal complex the authors can analyze several properties, such as the maxima, minima, number of cells, local span, and curvature of the network.
3. The authors also analyze the effects of depth, width, and regularization on the complex.

### Weaknesses
1. The time complexity $O(|vertices|)$ of the algorithm in this paper is very high, since the number of vertices obtained in this algorithm should be some exponential functions of the number of neurons or the number of layers in the network, which makes the algorithm not very useful in practice, especially for deep networks. The paper does not provide a clear analysis of how the number of vertices scales with network parameters, such as the number of layers, the number of neurons per layer, and the input dimension. This lack of analysis makes it difficult to assess the practical applicability of the algorithm, especially considering that the number of vertices can grow exponentially with these parameters. A more detailed theoretical analysis of the vertex count is needed to understand the limitations of the proposed method.

2. The assumption that the network is a continuous piecewise linear function is also not very useful since the DNNs used in practice have much more complicated structures. While ReLU networks do produce piecewise linear functions, the practical relevance of analyzing the exact polytopal complex is questionable. Many practical networks incorporate other non-linearities, such as sigmoid or tanh activations, or use more complex architectures such as convolutional or recurrent layers, which are not covered by this analysis. The paper should discuss the limitations of this assumption and its impact on the generalizability of the results.

### Questions
1. It will be useful if the authors can provide more analysis on the bounds of the number of vertices obtained in their algorithm, thus providing more information on the complexity of their algorithm.
2. In Equation (1), it should mention that $\sum \lambda_i = 1$, otherwise it is not true.
3. More references on the bounds of the number of cells and vertices should be added to the paper.

### Soundness
3

### Presentation
3

### Contribution
2
