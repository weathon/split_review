# Topological Expressive Power of ReLU Neural Networks

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 8, 3

## Abstract
We study the expressivity of ReLU neural networks in the setting of a binary classification problem from a topological perspective. Recently, empirical studies showed that neural networks operate by changing topology, transforming a topologically complicated data set into a topologically simpler one as it passes through the layers. This topological simplification has been measured by Betti numbers, which are algebraic invariants of a topological space. We use the same measure to establish lower and upper bounds on the topological simplification a ReLU neural network can achieve with a given architecture. We therefore contribute to a better understanding of the expressivity of ReLU neural networks in the context of binary classification problems by shedding light on their ability to capture the underlying topological structure of the data. In particular the results show that deep ReLU neural networks are exponentially more powerful than shallow ones in terms of topological simplification. This provides a mathematically rigorous explanation why deeper networks are better equipped to handle complex and topologically rich datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
The paper studies the expressivity of ReLU neural networks in the setting of a binary classification from a topological perspective. 
The authors prove new lower and upper bounds for topological expressivity of ReLU networks. Here, the topological expressivity is the sum of Betti numbers of input subspaces, which network separates. Such expressivity grows polynomially with the width (for fixed depth) and exponentially with the depth (for fixed width). Most of the paper is dedicated to obtaining the lower bound by explicitly constructing weights of a network.

### Strengths
Research on the intersection of topology and deep learning is active right now.
Regarding the expressivity analysis and proving UAT-like theorems, I am not an expert in this area and I can't evaluate originality and impact of the manuscript.
I haven't thoroughly checked math, but I don't see evident errors. 
Overall, the paper is well written and language is fine.

### Weaknesses
1. I don't understand the notation $\beta_0(F) \in \Omega(M^d \cdot n_L)$. Is it the same as $\beta_0(F) = \Omega(M^d \cdot n_L)$ ? (that is, $C_1 M^d \cdot n_L \le \beta_0(F) \le C_2 M^d \cdot n_L$)
2. The most of the paper is dedicated to the proof of the **existence** of a network with a given topological expressivity.
But in deep learning we are interested in a practical algorithm for finding such a network. The manuscript will benefit from computational experiments. You can use simple synthetic datasets with known Betti numbers (like in Naitzat et al. (2020)) and estimate depth/width of a network which is able to classify it with accuracy > 0.95, for example. 
3. The manuscript is very long (30 pages), the Appendix is dedicated to proofs. Maybe some journal will be a better destination for such a manuscript.

### Questions
1. You explicitly construct a network with a given topological expressivity, but are this network's weights reachable by gradient optimization?

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
The paper studies ReLU networks from the perspective of their topological expressivity. The measure used here is that of Betti numbers that is a suitable measure for characterizing how complicated the topological properties of a network are.

The main contribution of the paper is to derive several upper and lower bounds for the Betti numbers depending on the depth and width of the ReLU network, by using clever constructions of functions.

The main takeaway is that Betti numbers depend on the depth, and can significantly grow with the depth. If the depth is unbounded, Betti numbers increase exponentially with the size of the network. In contrast, if the networks is shallow then its Betti numbers do not grow as fast. This is interesting as it showcases that a possible bottleneck for effective data representation is the depth.

The constructions in the paper are heavily inspired by previous ideas used in Montufar et al. where the goal was to characterize another measure of ReLU neural network complexity, that of linear regions. We know that the number of linear regions can exponentially grow with the depth, but not the width. The paper under review essentially sets out to formally establish the connection and proposes clever constructions to transfer the results to the complexity measure of Betti numbers.

### Strengths
+well-motivated theoretical question about the expressivity

+the question has been empirically observed and the paper develops interesting theory to address this in a simple binary classification setting

+in my opinion, the paper proves a very elegant characterization for expressivity and interesting dependence on Betti numbers for the depth and width

+potential interesting connections to dynamical systems (see comments below)

### Weaknesses
Overall, the paper is strong and there are not major weaknesses in my opinion. One thing I believe should pointed out though has to do with the novelty of the final conclusion of the paper.

- The key takeaway of the paper is that depth is more important than width. The paper has an elegant way of proving this via the Betti numbers. However, the reviewer just wants to point out that similar depth-width tradeoffs were known, albeit using different techniques and different connections. So in some sense we already knew that depth is exponentially better than width. For example:

The authors cite Telgarsky's works who used a basic triangle construction and as a measure of complexity he used the number of linear regions. Similarly, Montufar et al. had the number of linear regions as a way to show that depth is much more important. 

There is also a generalization of the works of Telgarsky that use connections to dynamical systems (Li-Yorke chaos, periodic orbits) and the notion of *topological* entropy [3]. See [1], [2], [3]. Papers [1] and [2] give lower bound constructions using more general functions that than Telgarsky's triangle and [3] provides characterization using topological entropy.

[1] Depth-WidthTrade-offs for ReLU Networks via Sharkovsky’s Theorem
[2] Better depth-width trade-offs for neural networks through the lens of dynamical systems
[3] Expressivity of Neural Networks via Chaotic Itineraries beyond Sharkovsky’sTheorem

It would be interesting to see if the characterization of the Betti numbers for the depth/width tradeoffs can actually follow in certain cases because of the connection to Li-Yorke chaos and periodic points.

### Questions
Q: Related to the weakness comments above, do the authors see any connection between their construction and the notion of periodic points/topological entropy in dynamical systemts? At least their examples in Fig. 3,4,5,6 for the binary classification problem resembles both Telgarsky's triangle characterization, and also the more general result proved in [1] Depth-WidthTrade-offs for ReLU Networks via Sharkovsky’s Theorem.

Q: For 1-dimensional neural networks (i.e. input is just a real number) similar to the ones that Telgarsky used, do your results imply the exact separation that Telgarsky proved? Is there a sense why your results are stronger in this special case? I believe this is the simplest case where we can understand whether or not the connection to dynamical systems is valid.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This article is about topology of certain sublevel sets of functions defined by fully connected ReLU neural networks.  Asymptotic bounds for Betti numbers of the sublevel sets of such functions are established.

### Strengths
Paper is situated within the framework  trying to approach expressivity of neural networks via topology. A set of interesting mathematical results concerning bounds for Betti numbers is proven

### Weaknesses
Weaknesses:

1)In deep learning  both the positive and negative data points typically lie near very low dimensional surfaces, so in general, there is no relation between Betti numbers of the sublevel set of the function defining a decision boundary and the Betti numbers of the support of the distributions from which the data points are sampled. The Betti numbers of the support of distribution can be arbitrary big, while at the same time the zeroth Betti number of the sublevel set of the function defining a decision boundary can be  equal to one. Therefore the practical meaning of the paper's results is limited.


2)Lower bound is obtained only for some specific weights of neural network. However, given a neural network architecture there are always weights that produce constant function and thus have strictly zero Betti numbers, so the meaning of  paper's "lower bound" term is not quite clear. Furthermore, the specific weights that achieve the lower bound appear to be highly contrived and unlikely to arise from standard training procedures, making the practical relevance of this lower bound even more questionable.

3)Also it is not clear whether the constructed network weights can be  found via regular optimization algorithms, 

4)The calculation of Betti numbers is difficult so it  also undermines practical implications of the work.

5)The claim of the exponential gap is somewhat unclear in the paper. It is not clear what exactly is being compared to establish this gap. Is it a comparison of the number of parameters, or the number of layers, or some other measure of complexity? The lack of clarity makes it difficult to assess the significance of this result.

6)The upper bound proof lacks some details, only about half a page is devoted to upper bounds, the paper mostly concerned with lower bounds. The sketch provided is insufficient to fully understand the proof, and the missing details are not obvious or easily inferred from standard topological arguments.

7)The lower bounds found by the authors are similar to previous ones that have appeared in the literature, e.g. in  Bianchini and Scarselli (2014). For example the principal zeroth Betti number result is an extension of the loc.cit to  ReLU activations. The extension to ReLU activation, while relevant, does not seem to introduce a significant conceptual advance over existing results. The paper does not adequately address the novelty of this extension.

Minor remarks:

Grammar errors: section 1.2.1 : ares -> are

Notations are somewhat confusing M_a and M_b are topological spaces, but M is an integer in section 2, lemma 4  etc. 

Why does this graph, consisting of two points, represents the functions that folds the interval on Figure 1, there seems to be a problem with this figure, are some lines missing ?

### Questions
Can authors provide an example from real world data when their bounds have practical implications ? 

The paper really needs to show concrete real world examples  with practical meaning of the paper's results.

Reply to post-rebuttal remarks:  
I thank the authors for further clarification. I encourage the authors to spell out the precise meaning of their notion "lower bound of" in concrete mathematical terms. It seems that this is the lower bound of the maximum of certain quantity taken over some set, but what exactly is the set over which the maximum is taken? Does this maximum depends on the architecture only, or also on the dataset $X$? If it depends on the dataset $X$ what is the meaning/effectiveness of this depending on $X$ notion?  
Also concerning another issue, I really encourage the authors to try to find a practical real-world case in which their results bring a novel perspective.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
