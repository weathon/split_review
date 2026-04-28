# Compelling ReLU Networks to Exhibit Exponentially Many Linear Regions at Initialization and During Training

- Decision: Reject
- Avg Score: 6.00
- Scores: 3, 8, 8, 5

## Abstract
A neural network with ReLU activations may be viewed as a composition of
piecewise linear functions. For such networks, the number of distinct linear regions
expressed over the input domain has the potential to scale exponentially with depth,
but it is not expected to do so when the initial parameters are chosen randomly.
Therefore, randomly initialized models are often unnecessarily large, even when approximating simple functions. To address this issue, we introduce a novel training strategy:
we first reparameterize the network weights in a manner that forces the network
to exhibit a number of linear regions exponential in depth. Training first on
our derived parameters provides an initial solution that can later be refined by
directly updating the underlying model weights. This approach allows us to learn
approximations of convex, one-dimensional functions that are several orders of
magnitude more accurate than their randomly initialized counterparts. We further demonstrate how to extend our approach to multidimensional and non-convex functions, with similar benefits observed.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper designs a novel training strategy: (1) reparameterise the network weights in to make it exhibit a number of linear regions exponential in depth; (2) train on the derived parameters for an initial solution; (3) refine the parameter by directly updating the underlying model weights. Experiments are given to support the method.

### Strengths
-	The paper presents detailed introduction and explanation of the proposed method, including how to construct the initialisation and how to calculate the gradient. The paper is compressive, well-structed, and easy to follow. 
-	The paper present experiments for cases of one dimension and high-dimension non-convex problems.
-	I find the paper makes conceptual contributions of proposing a new initialisation strategy.

### Weaknesses
-	The experiments are not sufficient. The current experiments only cover quite shallow (three layers) ReLU neural networks on very simple tasks. It is unclear whether the results apply to complex scenarios, like deeper neural networks, transformer on fitting images, mining on text data, etc. Thus, the paper actually cannot help understand the success of deep learning.
-	No comparison is given with other initialisation methods.
-	The explanation of why this method works is not sufficient. This makes the method not convincing.
-	No theoretical results are provided. This is particularly severe given the experiments are insufficient.

### Questions
Please address the Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper focuses on the expressivity of ReLU networks and argues that the standard neural network training approaches lead to models that cannot utilize all of the linear regions that a ReLU network has the potential to exhibit. The paper contains an approach to overcome this issue.

### Strengths
Please see the Questions section.

### Weaknesses
I think this paper brings up important issues with standard neural network training practices (such as using relu for activation or gradient descent, etc).

- One thing that I think is potentially missing is the verification of the findings on a somewhat more realistic scenario. Could we expect the proposed method to outperform a standard neural network approach (e.g. a similar size relu network trained by SGD) when, say, predicting airline delays? Or, other more standard methods such as linear regression or decision tree?

- To make the results potentially more broad, I wonder if the proposed strategy could be somehow applied to classification (perhaps can test it on a simple dataset such as "two spirals" dataset). If that's not straightforward, I think it'd still help me understand the contributions better if the authors can comment on the challenges.

- Which of the findings of this paper could we expect to carry over to other non-linear activation functions such as sigmoid?

### Questions
My review is as follows:

- I think this paper brings up important issues with standard neural network training practices (such as using relu for activation or gradient descent, etc).

- One thing that I think is potentially missing is the verification of the findings on a somewhat more realistic scenario. Could we expect the proposed method to outperform a standard neural network approach (e.g. a similar size relu network trained by SGD) when, say, predicting airline delays? Or, other more standard methods such as linear regression or decision tree?

- To make the results potentially more broad, I wonder if the proposed strategy could be somehow applied to classification (perhaps can test it on a simple dataset such as "two spirals" dataset). If that's not straightforward, I think it'd still help me understand the contributions better if the authors can comment on the challenges.

- Which of the findings of this paper could we expect to carry over to other non-linear activation functions such as sigmoid?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes to reparameterize ReLU networks by parameterizing the peaks of the triangle wave basis functions generated by ReLU activations. This ensures that the number of linear regions grows exponentially with the depth of the network, which reduces the waste of representation capacities in randomly initialized ReLU networks. A learning algorithm is proposed to train the reparameterized ReLU network by first updating the derived parameters and then updating the actual weights underlying the model. The proposed method is empirically evaluated on 1D convex and 2D nonconvex target functions, which demonstrate its improved accuracy compared to randomly initialized networks.

### Strengths
1. The proposed reparameterization of ReLU networks is novel and interesting. Based on the observation that ReLU networks can generate symmetric triangle waves, the proposed approach introduces an approach to directly reprent the ReLU neurons (rather than weights) as asymmetric triangle wave basis function with learnable locations of the peaks within [0, 1].
2. The proposed learning algorithm is simple and seems to be effective in training the reparameterized network for simple target functions as shown in the experiments.
3. The 1D demonstrations and experiments are nice, which illustrate how the proposed method learns useful patterns for fitting the target function.

### Weaknesses
1. Theorem 3 seems to be an “only if” statement, and therefore setting $s_{i+1}$ according to Eq 4 is a necessary but not sufficient condition to guarantee differentiability of the reparameterized network. Specifically, while the condition ensures the possibility of a differentiable limit, it doesn't prevent scenarios where the peak locations are chosen such that the linear regions collapse, for instance if the peak locations are at the boundaries (0 or 1), or if they form a sequence that converges too slowly, such as 1/2, 2/3, 3/4, etc. This could lead to a piecewise linear sum instead of a smooth, differentiable function. 

2. It is unclear how useful the proposed method is in practice, since it is mostly evaluated on simple 1D convex target functions. The experiments do not demonstrate the method's effectiveness on more complex, real-world datasets. As this is not solely a theory paper, the proposed method should be evaluated on some common benchmark datasets, such as those from UCI, to assess its practical applicability and limitations. The current experiments do not provide sufficient evidence for the method's general utility.

3. Writing needs to be improved. The logic flow is a bit confusing. Also, several important concepts and building blocks are not well explained in the paper. For example, important definitions like definitions of linear regions, activation patterns, and activation regions should be stated in the paper or appendix. The lack of clear definitions makes it difficult to fully grasp the proposed method and its implications.

4. The following closely related works which analyze compositions and/or reparameterization of ReLU activations are not discussed in the paper.

[1] K Eckle, J Schmidt-Hieber. A comparison of deep networks with relu activation function and linear spline-type methods.

[2] DM Elbrächter, J Berner, P Grohs. How degenerate is the parametrization of neural networks with the ReLU activation function?

[3] W Chen, H Ge. Neural characteristic activation analysis and geometric parameterization for ReLU networks.

[4] B Hanin, D Rolnick. Complexity of linear regions in deep networks.

[5] M Raghu, B Poole, J Kleinberg, S Ganguli, J Sohl-Dickstein. On the expressive power of deep neural networks.

[6] D Rolnick, K Kording. Reverse-engineering deep ReLU networks.

### Questions
1. How are ReLU activations guaranteed to generate symmetric triangle waves? There are many possible compositions of ReLU activations, but only a subset of them are symmetric triangle waves. If the network is reparameterized using only the triangle wave basis functions as proposed in the paper, will it lose some flexibility and expressivity as it is not possible for the reparameterized network to create other shapes or patterns within each layer? 

2. Could you provide some intuitions and/or theory regarding why pretraining helps maintain the triangle generating structure and avoid eliminating activation regions as the network gets deeper?

3. Does the proposed method improve convergence rate? Could you demonstrate it with some experiments and/or theory?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a novel strategy to improve the efficiency of ReLU neural networks. It focuses on overcoming the limitations of randomly initialized networks, which tend to be unnecessarily large and inefficient in approximating simple functions. The authors introduce a reparameterization of network weights that ensures an exponential number of activation patterns, thus maximizing the linear regions in the input space. Their approach includes a pretraining stage using derived parameters that enhances the expressivity of the network before standard gradient descent is applied. This method shows significant improvement in approximating both convex and non-convex functions, with better accuracy and efficiency compared to traditional networks. The paper's findings demonstrate that networks initialized with exponential linear regions can capture nonlinearity more effectively, leading to more accurate function approximations. It concludes with potential extensions to multidimensional and non-convex functions, positioning this strategy as a promising tool for more efficient deep learning models.

### Strengths
* The paper introduces a novel approach to reparameterize ReLU network weights, which forces the network to exhibit an exponential number of activation regions. This significantly enhances the expressivity of the network and addresses the inefficiencies of randomly initialized models, providing a more accurate and efficient approximation of nonlinear functions.

* The proposed pretraining strategy allows the network to initialize with exponentially more linear regions, thus reducing the reliance on gradient descent to discover new activation patterns. This results in faster convergence and much more accurate function approximations, as demonstrated through numerical experiments, showing orders of magnitude lower errors compared to standard initialization methods.

### Weaknesses
While the paper demonstrates improvements in one-dimensional convex functions, the results for higher-dimensional functions and complex non-convex problems are not as thoroughly explored. The proposed method may face scalability challenges when extending to high-dimensional inputs, where the complexity of real-world tasks lies. Specifically, the paper lacks a rigorous analysis of how the reparameterization affects the optimization landscape in higher dimensions. The claim of exponential activation regions, while theoretically sound in 1D, needs empirical validation in higher dimensions, where the curse of dimensionality could significantly impact the practical benefits. Furthermore, the paper does not provide a detailed analysis of the computational cost associated with the pretraining step, particularly as the dimensionality of the input increases. This is a crucial factor for practical applicability, and without such analysis, it's difficult to assess the overall efficiency gains. 

The introduction of a pretraining step with specific reparameterization adds complexity to the network training pipeline. This may make the approach more difficult to implement or integrate into standard deep learning workflows, especially for practitioners looking for more straightforward techniques. The paper does not adequately address the potential for increased hyperparameter tuning required by the pretraining stage. The reparameterization introduces new parameters that need to be carefully tuned, which could potentially offset the benefits of improved initialization. Additionally, the paper does not discuss the sensitivity of the method to the choice of these new hyperparameters, which is critical for practical use. A detailed analysis of how these parameters affect the final performance is needed to make the method more accessible to practitioners. 

The effectiveness of the method heavily relies on carefully derived theoretical constructs, such as triangle functions and their parameterization. While this works well in controlled scenarios, its practical robustness in more diverse and noisy real-world datasets is not fully tested or demonstrated. The paper's reliance on idealized triangle functions raises concerns about its applicability to real-world data, which is often noisy and does not conform to such simple structures. The lack of experiments on datasets with varying levels of noise makes it difficult to assess the method's robustness. Furthermore, the paper does not address how the method would handle data with outliers or missing values, which are common in real-world scenarios. A more thorough evaluation on diverse datasets is needed to establish the practical utility of the proposed approach.

### Questions
* How does the proposed reparameterization strategy perform in complex, high-dimensional tasks, and what are the challenges in scaling this method effectively to more realistic datasets?

* Have you considered testing this method on real-world datasets with more variability and noise? How robust is the technique in such scenarios, and are there any performance trade-offs when dealing with non-synthetic data?

### Soundness
3

### Presentation
2

### Contribution
2
