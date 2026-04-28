# Block Coordinate Descent for Neural Networks Provably Finds Global Minima

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3

## Abstract
In this paper, we consider a block coordinate descent (BCD) algorithm for training deep neural networks and provide a new global convergence guarantee under strictly monotonically increasing activation functions.  While existing works demonstrate convergence to stationary points for BCD in neural networks, our contribution is the first to prove convergence to global minima, ensuring arbitrarily small loss. We show that the loss with respect to the output layer decreases exponentially while the loss with respect to the hidden layers remains well-controlled. Additionally, we derive generalization bounds using the Rademacher complexity framework, demonstrating that BCD not only achieves strong optimization guarantees but also provides favorable generalization performance. Moreover, we propose a modified BCD algorithm with skip connections and non-negative projection, extending our convergence guarantees to ReLU activation, which are not strictly monotonic. Empirical experiments confirm our theoretical findings, showing that the BCD algorithm achieves a small loss for strictly monotonic and ReLU activations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a block coordinate descent (BCD) training algorithm for deep networks and analyzes its convergence with respect to their weight parameters, which are proved to lead to a global minimum. This is done under monotonic increasing activation functions and ReLU (the latter with skip connections on the network. i.e., as ResNet). The paper also studies generalization only under monotonic increasing activation functions. A small number of simulations are provided to show the training convergence using the BCD algorithm.

### Strengths
- The paper is generally well-written. The presentation flows well.
- Remarks are added when appropriate, explaining connections with the literature.
- Algorithms are clearly written and the theoretical results are not difficult to parse.

### Weaknesses
 -- Important issues:

- There is a circular argument in Theorem 4.1 and Theorem 5.3 which weakens the theoretical results. The assumption of the theorem states that $\lambda_{min}(V_jV_j^\top)$ is abounded across **all** the training by the constant $C_V$, but then this same constant $C_V$ is used to define the selection of the step-size $\eta_W^{(1)}$ for the training. In other words, the authors are making an assumption on how the future behavior of the training will be, and then use this same assumption to establish the same training whose future behavior they are trying to study. This is a circular argument that makes not much sense. How can this be fixed?
I know that in Remark 4.1 it is stated that $\lambda_{min}(V_jV_j^\top)$ can be bounded differently by other parameters, which I think will be a better idea since that seems to get rid of the circular argument. However, no derivation is found of this other bound, and I believe it should be included. If such a bound is used, how would this change the theoretical results in the theorems and the proof derivations? There is no reason to believe that this different bound will work as well for the rest of the proof: new derivations are needed.

- The author establishes generalization results using classic Rademacher bounds found in Barlett et al. (2017). The problem is that the bound found by the author depends exponentially on the depth of the network! This has serious consequences: to achieve good generalization, according to the equation in Theorem 4.3, one would need to choose $n$, the sample size, larger than an exponential number of the depth $L$. This in turn means that the input neurons would also need to be exponentially large for deep neural networks (which has large $L$), since $d_{in}\geq n$ for the optimization setting in the paper. In other words, the number of parameters and sample size required for a good generalization is exponentially large and impractical. This weakens the contribution of the paper, since such loose generalization bounds **already** exist on the literature. Given that such loose bounds exist in the literature for deep neural networks, why is it necessary to include it in the paper? I am not sure that the activation functions used in the paper are different from the ones existing in the generalization literature.

- Curiously, many of the works that are cited by the authors in lines 108-109 try to fix the exponential dependence on the depth. For example, it surprises me that the authors cite Golowich et al., 2018, which I believe is a work that introduces a new way to avoid such exponential dependence, and which can be used with Rademacher based analysis. Can the authors find a way to eliminate such exponential dependence drawing ideas from this work or related others?

- Another issue is that the paper does not propose any generalization bounds for the ReLU case with skip connections, i.e., for ResNets. Why is that? This makes the paper less complete. Can the authors derive such a generalization bound using similar techniques to the case of monotonic increasing activation functions? I don’t know whether or not generalization results exist for ResNets with ReLUs: if they don’t exist, the contribution by the authors would be strengthened.

- In line 235 it is claimed that the initialization done for the $V_{j,i}$ parameters leads to “faster convergence”. However, there is no theoretical result nor experimental result in the paper to support this claim. Why are the authors claiming this? This a strong claim.

- Related to the previous point, in line (64), it is mentioned that the “loss with respect to the output layer will decrease exponentially to zero”. However, how is this exponential convergence observed in the results of Theorem 4.1 and Theorem 5.3? Can the authors clarify this?
 
- The paper proposes a type of BCD algorithms (Algorithms 1 - 3). How does it compare to other types of BCD algorithms proposed in the literature, like the ones cited in the third paragraph of the Introduction? Why do the authors think these other works could not achieve global convergence? Could it be because of the particular algorithms used by these other works or could it be because of the proof techniques used by these other works?

- Line 049 claims that BCD has “more accessible landscapes to optimize”. What’s the basis for this claim? All the parts of the BCD loss are coupled with each other (look at equation (2) for example), so that doesn’t mean the energy landscape would be “more accessible to optimize”. It is still a non-convex optimization problem. The authors should explain what is meant by this, since I don’t see the right intuition with such statement.

- How does using activation functions that are monotonically increasing play a role in the derivations of the theoretical results? This would be important to know, even if a qualitative response is given. What happens when such condition is removed?

- There is a conflict of claims in the paper. In line 098, the authors claim that their analysis “does not require any overparameterization to ensure global convergence”. However, in line 273, the authors state that they have been working “in the overparameterized setting”. This is because they are in the regime $d_{in}\geq n$, where the neurons in the input layer is equal or larger than the number of samples—which means that they are in the overparameterized regime. Can the authors clarify such conflict of statements and change the paper accordingly?
Do previous works on BCD also assume $d_{in}\geq n$?

- For ReLU’s, why are skip connections important to assume for the proof techniques to work? What is the intuition behind it? Skip connections are arbitrarily introduced without any reference to how such new architectural change benefits the theoretical derivations compared to when there were no skip connections. There must be some motivation for it.

- In Section 6, the weights of the last layer are fixed after their initialization. How is it possible to achieve a global minimum, when the last layer weights are not being trained? Is there any intuition as to why this is the case? This would mean that every time we randomly initialize the neural network, there would exist a *new* global minimum whose weights on the last layer is the same as the one in the initialization—the existence of such result is not immediately intuitive and deserves an explanation.

- Regarding Figure 1 left, the layer 1 is seemingly missing from the plot. Also, the paper states that the last layer, i.e., layer 4, decreases to zero exponentially, but it is hard to see from the plot whether the layer 4 curve will go to zero: is it possible to show more epochs? 

-- Other issues:
- Do people use BCD in practice? Contrary to works that study SGD, for example, or even perhaps GD, we know they are widely used in practice. What about BCD? The authors should add citations in Section 1 where BCD is used successfully in practical applications.
- Specify what kind of skip connections are implemented in the topology of the neural network in Section 5 (which is now a ResNet), since no description is explicitly found in the paper. Judging by the optimization equation, it seems that there is a connection from every neuron of the previous layer to the input of two layers ahead. Please, clarify. A mathematical equation description such as the one in line 136 would be helpful.
- The paper seems to suggest (see first paragraph of Introduction) that using the NTK is the only other existing method to formally provide optimization guarantees to neural networks. However, last year’s paper “Restricted Strong Convexity of Deep Learning Models with Smooth Activations” by Banerjee et al., published at ICLR 2023, proposes a new method for providing such guarantees without being on the NTK regime necessarily. This is a missing relevant citation.
- Typo in line 162: should be “field” instead of "filed”.
- What does it mean by a vector to have positive and negative “components” in Lemma 5.1? Do the authors mean “entries”?
- In Theorem 4.1 and Theorem 5.3, make explicit that $\mathbf{W}$ and $\mathbf{V}$ are the parameters obtained at the last iteration $k$ of their respective algorithms.

### Questions
Please, see all questions in the Weaknesses question.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the optimization of deep neural networks via a specific block coordinate descent (BCD) algorithm. Their algorithm introduces a set of auxiliary parameters $V_{l, i}$, defined to approximate the output of the $l$th layer on the $i$th data point, and considers a layerwise GD algorithm on both the $V_{l, i}$ and the original weights $W_l$. The main result, Theorem 4.1 is that their algorithm converges to a global min (i.e interpolating solution) when the activation functions are strictly monotonic; the authors also provide a generalization to the ReLU activation. Additionally, the paper proves a generalization bound for the output of the algorithm.

### Strengths
- It is an interesting question to prove that gradient based algorithms for neural networks can converge to global minima. The algorithm presented here is to the best of my knowledge novel, and this paper generalizes prior works which only proved stationary point convergence by proving global convergence.
- The paper is written quite clearly, and the proofs to the best of my knowledge appear sound.

### Weaknesses
 - The paper provides an algorithm which, for a dataset with $n \le d_{in}$ data points, outputs a neural network which interpolates the data points. Crucially, however, this algorithm is not a standard optimization algorithm such as vanilla gradient descent. We already know that networks in the NTK regime converge to global minima, yet the NTK is insufficient as it fails to accurately capture generalization. Similarly, while the algorithm presented here also converges to a global minimum, there is no (theoretical or empirical) justification for why we expect this algorithm to generalize well, what its inductive bias is compared to vanilla gradient descent, or whether it can perform feature learning. More concretely, there is no notion of why this algorithm is "better" than NTK-based approaches. Such omissions greatly limit the significance of the paper.
- For example, experiments on a toy dataset which compare the test error between neural networks trained with vanilla GD, nets in the NTK regime, and training with BCD could support this claim. Another idea would be a specific sample complexity guarantee with an improvement over the NTK for learning some class of target functions with BCD.
- The paper does claim that BCD "provides favorable generalization performance" (line 20, abstract). The only justification for this is the generalization bound Theorem 4.3. However, it has been observed in the literature that such spectral generalization bounds are vacuous and fail to explain the success of deep neural networks [1, 2]. It is unclear why the bound in Theorem 4.3 should be interpreted as achieving "good" generalization. 
- A more minor limitation is that the results only hold for $n \le d_{in}$, which is not satisfied in many standard deep learning settings.

### Questions
- More discussion on my above concerns re the significance of this work would be greatly appreciated.
- Theorem 4.1 assumes that $\lambda_{max}(V_jV_j^T)$ is bounded throughout training. This seems like a very strong assumption, and I don't see why one should expect this to hold (for example, it seems reasonable that this could scale with $d_{in}$ or $r$)). Can you comment on this point?
- A number of the algorithmic choices (use of different learning rates, different number of steps for different layers, etc.) seem a bit arbitrary, and so comments on these choices would also be helpful.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The contribution is theoretical: establishing the global convergence for a specific block coordinate descent used to optimize neural networks. Indeed, The specific block coordinate descent is a particular layerwise optimization method. While it is not explicit, the global convergence result is established for the overparameterized regime, where the number of parameters $>$ the size of the training set.

### Strengths
- Studying the convergence of BCD is well motivated in the intro using the related literature  
- Assumptions 1 and 2 are reasonable
- The theoretical settings is not far from the practical settings. 
- If the analysis and statements were correct, global convergence of any algorithms on deep neural networks is a valuable result.

### Weaknesses
I think there are mistakes in the proof. 

**Issue 1.** Check line 796 in the appendix. Recall notations $w'= w - \nabla $ where $\nabla = \eta X^\top D(\sigma(Xw)-Y)$. Line 796 proposes the following equation holds 

$$\|| \sigma(Xw') - Y\||^2 = \|| \sigma(Xw) - X \nabla -Y\||^2 $$

The above equation only holds for a linear $\sigma$. However, the equation does not hold for a general $\sigma$ obeying Assumption 2. This discrepancy is significant, as the equation underpins the derivations used to establish the main theorems.

**Issue 2.** 
In lines 802-803, it is claimed that $\||I- \eta \Xi X X^\top D \|_{op} \leq 1$ 
holds for a small positive $ \eta$. But why? If $A=\eta \Xi X X^\top D$ is not PSD, we can not ensure that the operator norm of  I - A  is less than one.

**Issue 3.** There is another issue in your derivation, please check derivation bellow and let me know if I am making a mistake here. 

$\|| I-A \||  =_{[line: 871]} \|| N (I - \eta  D^{1/2} \Xi^{1/2} M  D^{1/2} \Xi^{1/2} ) N^{-1}\||  \leq \|| N \|| \|| I - \eta  D^{1/2} \Xi^{1/2} M  D^{1/2} \Xi^{1/2} \|| \|| N^{-1}\|| \leq  \||N \|| \||N^{-1}\||$. Why does $ \||N \|| \||N^{-1}\||< 1$ hold for a small $\eta$?

### Questions
- Does the specific BCD considered in this paper connect to layerwise training of deep neural networks? If so, this literature can be used to motivate the topic from a practical view. 
- Is BCD cheaper than back propagation? Can you quantify the computational benefits of BCD? 
- You mentioned your analysis in section C.2 (where I pointed out the mistake) is similar to [Yehudai and Ohad (2020); Frei et al. (2020)]. Can you be more specific about the similarity?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper shows that under suitable assumptions and a specific design of the objective, block coordinate descent will always find parameters that have both arbitrarily small training loss and good generalization guarantee. The major assumptions this paper makes are that the dataset is full rank in the high-dimensional regime (where the input dimension >= number of data), and the activation is bijective. Optimality guarantee follows from the fact that the given objective is a sum of least squares, and optimizing least squares by gradient descent (or its variants) is possible. Generalization guarantee follows from the fact that they chose the hyperparameters appropriately to make the operator norm of the weights well-behaved, plus at the initialization they use singular value bounding. Finally, the paper extends the result to ReLU(which is not bijective) by adding skip connections, and show by numerical experiments that their claim holds.

### Strengths
1. The paper tackles an important problem and provides a new perspective that "block coordinate descent may be a better way to optimize".
2. The paper is easy to follow with sufficient insights and motivations so that the reader can understand the theorems and algorithms.

### Weaknesses
1. One critical issue that I did not understand is the following:

In this setting, do we "need" block coordinate descent? If so, why?

This question emerged because when the activation $\sigma$ is bijective (which is the case when Assumption 2 is satisfied), we could repeatedly solve a series of linear equations to find the optimal parameters $W_L, W_{L-1}, \cdots W_{1}$. Say $Y \in \mathbb{R}^{d_{out} \times n}, X \in \mathbb{R}^{d_{in} \times n}, W_L \in \mathbb{R}^{d_{out} \times r}, W_1 \in \mathbb{R}^{r \times d_{in}}, $and $W_i \in \mathbb{R}^{r \times r}$ for $i = 2, 3, \cdots L-1$. We could solve Y = W_LV to find the correct $V$, and then apply $\sigma^{-1}$, and then solve $\sigma^{-1}(V) = W_{L-1}V'$, and repeat this process until we find good parameters that fit $Y$ given $X$. Hence, without the complicated block coordinate descent algorithm, can't we train the network to global optimality?

2. Another weakness I find is the constant $C_V$. This paper assumes that the operator norm of $V_j$ is bounded by $C_V$, which is a convenient assumption to make many things simple (for example, it is used to prove that the weights $W_i$ behave well - which is used to prove generalization guarantees): Remark 4.2 says that $C_V$ can be expressed using $\eta_V$, $K$, and $K_V$, but I don't see a clear reason why. As $C_V$ is crucial in proving generalization bounds and well-behaving norms, clarifying this remark is I think needed.

3. The assumptions are somewhat restricted: $d_{in} \geq n$ seems restrictive, and $\sigma$ needing to be bijective is also quite restrictive. The network has a particular size (the weights are all square matrices in the intermediate layers). Also, it could be better if the authors could give an ablation study on singular value bounding: does this procedure help training, or is it a procedure that is of theoretical interest?

4. In numerical experiments, the trainning loss in Figure 1 does not seem to converge to 0 (it seems like it is decreasing, but it's hard to see that its a global optimum) - running this more to show that the algorithm actually finds a global minimum could be nice.

### Questions
1. In pg 21, there is a proof without any theorem. This could be a typo.

2. Addressing the weaknesses would be nice. If I see that block coordinate descent is beneficial, $C_V$ has a bound that only depends on the system parameters, I would definitely raise my score.

3. Assumption 2 should be made clearer. Subdifferential is only defined when $\sigma$ is convex. What if it is not convex? One suggestion is writing for any $u_1, u_2 \in \mathbb{R}$, $\sigma(u_2) - \sigma(u_1) \geq \alpha |u_2 - u_1|$. Another suggestion is assuming $\sigma$ is convex.

4. Is the intuition of adding skip connection for ReLU case trying to make ReLU into a bijective function?

### Soundness
2

### Presentation
3

### Contribution
1
