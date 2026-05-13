# Learning High-Degree Parities: The Crucial Role of the Initialization

- Decision: Accept
- Scores: 5, 6, 6, 6, 8, 8

## Abstract
Parities have become a standard benchmark for evaluating learning algorithms. Recent works show that regular neural networks trained by gradient descent can efficiently learn degree $k$ parities on uniform inputs for constant $k$, but fail to do so when $k$ and $d-k$ grow with $d$ (here $d$ is the ambient dimension). However, the case where $k=d-O_d(1)$ (\textit{almost-full parities}), including the degree $d$ parity (the \textit{full parity}), has remained unsettled. This paper shows that for gradient descent on regular neural networks, learnability depends on the initial weight distribution. On one hand, the discrete Rademacher initialization enables efficient learning of almost-full parities, while on the other hand, its Gaussian perturbation with large enough constant standard deviation $\sigma$ prevents it. The positive result for almost-full parities is shown to hold up to $\sigma=O(d^{-1})$, pointing to questions about a sharper threshold phenomenon. Unlike statistical query (SQ) learning, where a singleton function class like the full parity is  trivially learnable, our negative result applies to a fixed function and relies on an \emph{initial gradient alignment} measure of potential broader relevance to neural networks learning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper considers the learning of full parity and nearly full parity when the input is sampled from the $d$-dimensional hypercube. It shows that when a two-layer ReLU network is initialized with the first layer weights following the Rademacher initialization (uniformly distributed $\pm 1$ values), and the noise level $\sigma$ is sufficiently small, the network can learn the full parity problem with polynomial sample complexity when trained with GD/SGD of the second layer of the network. On the other hand, if the distribution of the weights at initialization deviates significantly from the uniform distribution on the hypercube (e.g., using a Gaussian distribution), the network is unable to learn the full or nearly full parity.

### Strengths
**Novelty** : 
While sparse parity problems ($k=O_d(1)$) are well studied in the context of representation learning with two-layer neural networks, I did not know that full parity can be learned with polynomial complexity. Thinking analogously to the sparse parity problems, we would need to train the first layer matrix but the gradient would vanish as the order of the parity gets larger. However, for the full parity, if the Rademacher initialization used, the gradient of the second layer is exactly computed and does not vanish, and furthermore, changing the weight of the second layer suffices to solve the problem. The proof largely depends on the Rademacher initialization, but even so, the analysis seems novel and interesting. 

**Interesting phase transition**: 
This paper shows that by adding small noise to the initialization then learning full and nearly full parities becomes significantly difficult. In addition to the Gaussian initialization, this paper extend this negative result to the midpoint between the Rademacher initialization and Gaussian initialization by introducing the quantity that characterizes the initial alignment of the gradient.

### Weaknesses
 **Motivation**:
Although this paper trains the two-layer neural networks, the mechanism of learning is significantly different from sparse parity. In the sparse parity problems, people mainly discusses how the first layer weights align with the meaningful subspace. On the other hand, every direction is equivalent in this full parity setting, thus I am not sure whether this paper is motivated as a feature learning paper. Thus the paper should explain why solving full parity how neural network is motivated, especially connections to real-world phenomena. The current justification that full parity is a challenging target seems insufficient, as many other problems are also challenging. The paper needs to articulate why this specific problem is important for understanding neural network learning beyond its difficulty.

**Generality of the result**:
As the lower bound suggests, this result is specific to the Rademacher initialization. The fact that the gradient does not vanish and such a transformation of equations is possible is quite interesting. However, if the results no longer hold after adding a small perturbation to the initial weights, then I wonder if those results lose their general significance. It's unclear how robust the observed phenomenon is to minor deviations from the precise Rademacher initialization. The paper should discuss the implications of this sensitivity for practical applications. The analysis, while interesting, might be limited by its fragility to initialization perturbations.

### Questions
**Extension to $(d-k)$-parity**
In the lower bound, we are able to handle the $(d-k)$-parity. On the other hand, the upper bound is stated only for full parity. Given the complexity theory and feature learning literature, I would like to see the corresponding between $k$-parity and $(d-k)$-parity. Can you derive something like $d^{\Theta(k)}$ complexity? Or $k$-parity and $(d-k)$-parity are essentially different for $k\geq 0$?

**Connection to real-world problems**
I would like to know if there are any real-world domains where learning high-degree or full parities is relevant,

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper provides a theoretical analysis of learning full parities (all bits parities) $k=d$ with SGD from (small perturbed) Rademacher initialization. To my knowledge, there was no analysis known. The case where it was observed that SGD succeeds with this initialization.
The authors further make some important observations on the role of initialization as to when we succeed in doing so, and it turns out that the initialization is curicial. To complement, the authors provide also hardness results for learning *almost full parities* with correlation loss and the initialization that has poor initial alignment, proposed by some metric that they define. For example, as a corollary, they can show that Gaussian initialization is poor. 

1. **positive**: For the perturbed Radamacher initialization with noise level $\sigma=O(d^{-1})$, a 2-layer ReLU trained with SGD (Definition 3) with either correlation or hinge loss, succeeds in strongly learning the **full (all bits) parity** function within poly(d) samples/iterations. 
2. **negative**: A general result that applies to a broader class of functions (including **almost full parities**) in terms of initial gradient alignment (GAL0 "signal at initialization"), where they show noisy SGD (Definition 3) has an edge over $1/2$ (null error) that is bounded by some function of poly(GAL0) and some other relevant hyperparameters, so if this GAL0 is exponentially decaying, we fail to weakly learn even with this initialization in poly$(d)$ samples. One example is Gaussian initialization.

### Strengths
See summary. The paper has a nice negative result for correlation loss SGD trained network with poor alignment initialization.

### Weaknesses
My main criticism of this paper is two-fold.
1. The paper, throughout the beginning (including the abstract), gives the impression that they show the success of SGD for even almost full parity $k=d-O(1)$, but the positive result is only shown for the full parity case $k=d$. For example, the abstract lines (14-17). Later also in Lines (65-77). I found this very confusing when I got to the main formal results. (See also my Question 1)
2.  To me the real contribution is the negative result. Particularly, showing that with Gaussian initialization, we fail with SGD on correlation loss. As far as I knew, this was open (see [Abbe & Boix-Adsera] discussion). However, the fact that this only holds for correlation loss works against its generality. Also, the presentation of the paper should be in a way that it highlights this as a primary contribution in a clear way. 

Overall, both in terms of contributions and presentation, this paper requires more for me to recommend acceptance. Therefore, I am leaning toward a weak rejection.

### Questions
1. How big is this poly($d$) for positive results for sample complexity? This is my other minor quibble. The phenomenon was already known that it is possible to learn, so the value in positive results is in doing a careful analysis. Or at least empirically observe and report what is the complexity of learning full parity.
2. What are the main techniques used in upper bounding the success probability in terms of initial gradient alignment? Also, an intuitive way of thinking why initial alignment is poor for Gaussian initialization but good for Rademacher or its "mildly" perturbed variant? To me, this is the main interesting contribution, but I did not find a clear description of the key ideas in the main text.

**Suggestion / Typos**
1. Perhaps it is worth expanding on the technique you used as I suggested above. And also for future work on deeper networks and other losses, there could be a much closer discussion on what are the difficulties. 
2. In Line 237, the full parity function has missing $x_i$ in the product. Also, for positive result, it would be much more helpful to just explicitly define $f$ (full parity) in the Theorem statements only. Or at least clearly refer to it in an equation as the result only applies to just that function.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper considers learning full parity functions over hypercube with neural networks. Their main results are twofold: : 1) Neural networks initialized near the Rademacher distribution can successfully learn full parity functions. 2) Conversely, neural networks with low gradient alignment at initialization, when trained using noisy gradient descent (GD) or stochastic gradient descent (SGD), fail to learn the task. Notably, Gaussian initialization results in poor gradient alignment, which significantly hinders network performance in this context.

### Strengths
The manuscript is reasonably well-written. The primary contribution—demonstrating the gap between Rademacher and Gaussian initialization—is an interesting result, particularly in the context of how initialization impacts neural network learning.

### Weaknesses
* I would be careful when claiming negative results as they depend on additional noise injected to SGD, i.e., Z^t terms in Eq (3), which seems unnatural compared to other theoretical results related to ReLU networks. Is there a hope to extend to the negative results to SGD without additional noise injection? Specifically, how does the magnitude of this noise compare to the inherent noise in standard SGD, and what theoretical guarantees are lost or modified when this additional noise is removed? It would be helpful to see a more detailed analysis of the impact of different noise levels on the convergence properties.

*  The positive result in the paper notably involves training only the output layer, meaning there is no feature learning. However, it is unclear whether the authors consider training input layer weights for their negative results, which introduces ambiguity in the interpretation of these results. Could the authors clarify this aspect in the rebuttal? Furthermore, if the negative results hold when training both layers, how does this affect the claim that the network fails to learn the task? Does it imply a failure in representation learning or optimization, or both? Providing a clearer distinction between these cases would strengthen the conclusions.

* Since the positive results only require training the output layer weights, it is uncertain if the sample complexity of their SGD is tight. Could the authors discuss whether their sample complexity is indeed tight, and/or whether it might improve if the initial layer were trained as well? Additionally, what aspects of their analysis limit extending training to the input layer? A more thorough discussion on the tightness of the sample complexity, potentially with a comparison to lower bounds for similar problems, would be valuable.

* The authors introduce a new measure, termed "initial gradient alignment," for analyzing their negative results. However, in the paragraph following Definition 2, they note that this measure aligns with the previously studied "Label-Gradient Alignment." Could the authors elaborate on how their analysis diverges from or builds upon these earlier works? Specifically, what are the limitations of using Label-Gradient Alignment in this context, and how does the proposed initial gradient alignment overcome these limitations? A more detailed comparison, highlighting the novel aspects of the proposed measure, would be beneficial.

### Questions
See the Weaknesses part.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the role of initialization for learning dense parities with neural networks.
It is shown that the learnability by gradient descent heavily depends on the initialization through a notion of gradient alignment: if the initial gradient alignment is small, then it is hard for noisy gradient descent to learn the target.
In particular, for dense parities, initialization with Gaussian perturbations has small gradient alignment and thus prevents learning, while random Rademacher initialization is a special case that allows learning.
The results are supported by theoretical analysis and numerical experiments.

### Strengths
1. The paper is well written and easy to follow. The organization is very clear.
2. The paper provides an interesting perspective on the role of initialization for learning dense parities, and the observed phenomenon seems very different from the that in the case of sparse parities.
3. The negative result holds beyond the case of dense parities, and potentially leads to a better understanding of the role of initialization for broader settings.

### Weaknesses
1. The negative result seems to hold only for noisy (stochastic) gradient descent. How about deterministic gradient descent? There is a gap regarding this, and it would be helpful if the authors could discuss this. The theoretical framework presented in the paper focuses on the dynamics of noisy gradient descent, particularly in the context of how the gradient alignment evolves over time. While this is a common and relevant setting, especially in the context of deep learning, it leaves open the question of whether similar phenomena occur when using deterministic gradient descent. Exploring this aspect would provide a more complete picture of the role of initialization in learning dense parities.

2. It seems that the poly(d) width is crucial. It is mentioned in Section 4 that this ensures the linear separability of the full parity function. It would be helpful if the authors could discuss more about this design choice, and also what happens for narrower networks. Specifically, how does the minimum width requirement scale with the input dimension 'd'? Is there a theoretical lower bound on the width that still allows for successful learning, or does the network's ability to learn dense parities degrade gracefully as the width decreases? Understanding the relationship between network width and learnability is crucial for practical applications.

3. It is unclear how the choice of the loss function affects the results. It would be helpful if the authors could discuss this. The paper primarily focuses on the correlation loss, but the broader applicability of the findings to other common loss functions, such as cross-entropy or hinge loss, remains unclear. Different loss functions can induce different optimization landscapes and gradient dynamics. Therefore, it is important to investigate whether the observed effects of initialization on gradient alignment and learnability are specific to the correlation loss or generalize to other loss functions.

### Questions
1. Intuitively speaking, what is the role of the gradient alignment at initialization? How does it affect the learning process?
2. In other common settings, such as regression with single- or multi-index models, what is the typical value of the gradient alignment at initialization?
3. In the sparse parity case, what's the role of gradient alignment at initialization?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies the problem of learning Boolean parities using gradient descent. This is a problem which in recent years has come to serve as a useful way of understanding the effectiveness and dynamics of training neural networks using gradient descent when the labels arise from a concrete, classical functional class. The set of all parities (or indeed any superpolynomial-size subset) is well-known to be SQ-hard to learn efficiently. This paper instead focuses on the the singleton function class consisting of the full parity, or the polynomial-size function class consisting of "almost-full" parities (of size $d - O(1)$). The main question tackled is the following: what is the effect of the precise neural network initialization on whether GD succeeds at learning such parities?

The main results are as follows:
- In general, for any fixed target function, whether or not GD/SGD with a particular initialization scheme succeeds is largely determined by a quantity dubbed the "gradient alignment" at initialization. Importantly, the gradient alignment is both target-specific and input distribution-specific. (Caveats: this characterization holds assuming certain types of Gaussian-smoothed, symmetric initialization schemes, neural networks with linear outer layers, and certain natural losses.)
- As an instantiation of this result, it turns out that Gaussian initializations as well as Gaussian-perturbed Rademacher initializations (with a sufficiently large perturbation) do _not_ have high gradient alignment and do not succeed at learning dense parities. (Subject to the same caveats above.)
  - In particular, this holds for poly-sized two-layer ReLU networks with pure Gaussian initializations.
- By contrast, the pure Rademacher initialization (or Gaussian-perturbed Rademacher with sufficiently small perturbation) is unusual and does succeed at efficiently learning dense parities.

### Strengths
The paper makes a useful contribution to our understanding of what neural networks can learn using gradient descent. In particular, the role of the initialization is clearly important in practice, and this paper considers a natural toy theoretical setting in which to study it formally.  The main results (both positive and negative) and proof techniques are interesting, and the separation between Gaussian and Rademacher is arguably a little surprising a priori. The most general negative result for arbitrary target functions (Theorem 7) seems particularly interesting and potentially useful even in practice. The technical contribution here in general is solid, although it very much builds on a large body of prior work with similar techniques. The paper is clearly written.

### Weaknesses
I am a little unsure about the novelty and significance of the paper. The problem of learning parities started as a natural toy theoretical setting for understanding what neural networks can learn, and there have recently been several papers that have studied this problem in increasing detail. The picture that is emerging for parities looks roughly as follows:
- In general they are trivially PAC-learnable by Gaussian elimination
- But they are SQ-hard (and also GD-hard) unless our prior information restricts the target to a small subset
- For parities of size $k$, GD and SGD on natural architectures do succeed in time $n^k$ [3,5]
- For a single fixed parity, it is learnable by GD under certain initialization schemes (inner weights all 1, as in [2], or Rademacher, as in [4])
- Again for a single fixed parity, it is not learnable by GD under other initialization schemes (such as the Gaussian, by the results of this paper, eg Theorem 3 --- under certain assumptions)

It would be nice if the authors could clarify how we should view this picture as a whole, especially keeping in mind the original motivation where the parities were just examples of complex functions. In general for learning a potentially complex function using deep learning, is there concrete guidance on what architectures, initializations etc do and do not work? For example, should we prefer Rademacher over Gaussian initializations in general? Should we always try to estimate the GAL before actually training? Does the GAL view subsume all prior results? My concern is that the parities are a very special case that allow various arguably superficial algebraic manipulations, and so lessons here may not be widely applicable.

The general negative result for general target functions is more interesting. I would view this as the main technical result of the paper. The techniques here borrow from prior work [4,6], and the GAL quantity and the arguments here also seems related to quantities like the "variance" considered in [6] and follow-up works. It seems that the main difference is that these prior works did not focus on the role of the initialization per se. Can the authors comment in more detail on the differences in proof techniques?

It would be nice to have the authors clarify their case for novelty and significance in light of these remarks and questions. On balance I am leaning positively but would like to hear their case first and hence am rating this a 6 for now.

### Questions
1. Repeating from above: it would be nice to get the authors' thoughts on the emerging picture around parities and complex function learning, and what the broader takeaways are.
2. Similarly regarding differences in proof techniques from prior works, esp Abbe and Boix-Adsera 2022 and Abbe et al 2022 (the INAL paper).
3. I am curious how Theorem 7 might be used in practice. It seems that the gradient alignment at initialization is something we can estimate purely using some labeled examples, without knowing the target. Does this mean that the following is a practical procedure when fitting any neural network by GD: first measure the GAL at initialization using some labeled examples, if it is small essentially abandon hope (for most reasonable architectures and initializations), otherwise proceed? Basically what power do we gain from the fact that we can estimate the GAL? Considering this is a target-specific, distribution-specific measure, this would be the dream result (namely a target-specific characterization of "practical" learnability) and seems like a very powerful operational interpretation --- if valid.
I wonder if there is an important distinction between the GAL being merely polynomially small and superpolynomially small. If it is only polynomially small, it might still be learnable in polynomial time. And to check if it is truly superpolynomially small, we would need superpolynomial sample complexity. So perhaps it is infeasible to measure it accurately enough for it to be useful?
4. Separately, a more minor technical point: it seems unfortunate that the main negative result (Thm 7) involves an additional Gaussian smoothing on top of an already smoothed initialization. I realize Corollary 1 tries to fix this but in any case it seems like an odd technical artifact. I am curious if things would be simplified if the initial Gaussian perturbation was itself defined as purely additive (i.e. $A + H_\sigma$ instead of $A + \\sqrt{Var(A)} H_\sigma$).

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proves that the full parity is learnable with SGD on 2-layer rademacher-initialized neural networks, with the hinge and correlation loss. The paper presents a notion of gradient alignment, which measures the distance between the gradients on the true distribution and those of a randomly-labeled distribution. The authors then use this measure to upper bound the accuracy any NN with a linear output layer can achieve with noisy GD and the correlation loss, providing a general negative result for learning. They follow up with application of that result to show that almost-full parities are not learnable when initialized differently enough from the rademacher init., all in all providing a separation result for learning full parities, depending on the initialization.

### Strengths
The authors advance an active and open area of research, providing answers on the learnability of full parities and almost-full parities.
The authors introduce a new measure that might be used to derive negative learning results in future research.

### Weaknesses
The phrasing in the abstract and introduction can be a bit misleading, in a way that suggests that your positive results include almost-full parities.

While the term "full parity" is mentioned in the abstract, no place indicates that the positive results refer to that case, and not the more general one of almost full parities. This omission is then continued in the introduction (lines 59-78), where you mention Abbe & Boix-Adsera who considered learning almost-full parities, then stating "First, we show that SGD on a two-layer fully connected
ReLU network with Rademacher initialization can achieve perfect accuracy, thus going beyond weak learning". Which could imply again that you have showed learnability of almost-full parities, as the last case you referred to is that of almost-full parities.

Personally I was confused, and have searched around the paper for the more general case for a while. (the only place where the result is carefully stated is the conclusion). I suggest changing the phrasing to avoid this confusion. It could be as simple as changing the above sentence to "...can achieve perfect accuracy on full parities, thus going beyond weak learning". Similarly, changing the abstract to "enables efficient learning of full parities".

Theorem 4 is long. I suggest breaking it down claims / corollaries / etc, according to the items in the theorem.

I suggest using a consistent format throughout all related theorems, containing all relevant information. e.g. for the positive results the reader is referred to the text to find the definition of the target function (full parity), while the target function for the negative results is stated in the theorem.

### Questions
What is the obstacle in applying the technique of the positive results to almost-full parities?

### Soundness
3

### Presentation
2

### Contribution
3
