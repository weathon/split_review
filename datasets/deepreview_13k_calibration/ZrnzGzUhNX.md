# Closed-Form Interpretation of Neural Network Latent Spaces with Symbolic Gradients

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
\small

It has been demonstrated in many scientific fields that artificial neural networks, like autoencoders or Siamese networks, encode meaningful concepts in their latent spaces.
However, there does not exist a comprehensive framework for retrieving this information in a human-readable form without prior knowledge.
In order to extract these concepts, we introduce a framework for finding closed-form interpretations of neurons in latent spaces of artificial neural networks.
The interpretation framework is based on embedding trained neural networks into an equivalence class of functions that encode the same concept. We interpret these neural networks by finding an intersection between the equivalence class and human-readable equations defined by a symbolic search space. 
The approach is demonstrated by retrieving invariants of matrices and conserved quantities of dynamical systems from latent spaces of Siamese neural networks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors proposed a framework to find mathematical interpretations of what a neuron does in mathematical equations readable to humans.  It relied on searching for an equivalence class of functions that encodes the same concept as the target neuron, and a symbolic search process guided by minimizing the difference in gradients. Experiments were conducted to show the proposed method can indeed identify the invariant mathematical operations among various inputs.

### Strengths
To identify what a neuron does in a trained network and, therefore, open the "black box" of neural networks is of significant importance. Specifically, The ability to express the internal operation of networks by standard mathematical formulas in general cases is highly desirable.     The method proposed is relatively straightforward to understand, and represents a notable attempt to address this issue.

### Weaknesses
1. The tests were to identify relatively straightforward invariance and express it with mathematical symbols. However, it is not clear if real tasks completed by neural networks, e.g., recognition of a complex object or making a decision in dynamic environments, can be understood in that way. It is not clearly explained how the proposed method can be used in more complex tasks. Specifically, the method's reliance on gradient alignment might become problematic in high-dimensional, non-convex loss landscapes typical of complex tasks, where gradients can be noisy or misleading. The paper lacks a discussion on how the method would handle such scenarios, including potential failure modes and limitations.

2. Only one specific network structure was tested experimentally, without showing that it could work for other networks. This raises concerns about the generalizability of the approach. The method's effectiveness might be highly dependent on the specific architecture and activation functions used. The paper does not provide any theoretical justification for why the proposed method should be architecture-agnostic, nor does it explore the impact of different architectural choices on the quality of the identified symbolic expressions.

3. In the experiments, a single neuron that carries out the complete network output was analyzed, which did not demonstrate effectiveness in more complex situations.  For example, if we want to understand what a hidden layer containing multiple neurons does, how could this be done with the proposed method? More generally, it is more important to understand what is the operation carried out by a population of neurons, rather than by a single neuron. The paper does not address how the method could be extended to analyze distributed representations across multiple neurons, which is a common characteristic of deep neural networks. The current approach seems fundamentally limited to scalar outputs, and it is unclear how it could be adapted to handle vector-valued or higher-order tensor outputs.

### Questions
I would appreciate if the authors could address the questions I raised in the Weaknesses section, at least by adding explanation and clarification, but preferably by further experiments.

### Soundness
3

### Presentation
2

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
The paper proposes a novel method for finding closed-form interpretation for closed-form expression interpretation of neurons in the artificial neural networks. The authors demonstrate the method’s efficiency on retrieving matrix invariants  and conserved quantities of dynamic systems within the latent spaces.

### Strengths
- Significance: The symbolic interpretation is an important aspect of interpreting  opaque neural network representations.

### Weaknesses
 - Motivation: the authors should clearly state what the proposed interpretation aims for and how, by whom and for what scenarios it could be used.
 - reproducibility and clarity: see the questions below, in summary, the authors need to significantly change the text to reach the necessary standard of clarity
- correctness: see the questions below
- novelty: it is important to highlight how the proposed solution contrasts with the other symbolic interpretation methods such as 	Cranmer et al., 2020; Mengel et al., 2023, and why these methods cannot achieve such interpretation

### questions:
 Questions on correctness: 

I’ve checked the maths carefully, and it seems to me that the model assumptions are conflated with the model properties. 
If we closely follow section 3.2, Eq.1 states that the model more likely learns the function as a composition of an uninterpretable transformation function $\phi$ and a closed form concept function $g$. The authors do not support that it actually the case. Then imagine that the function $g$ which maps inputs $x$, $x’$ into the same point, $g(x)  = g(x’)$. Then $\phi(g(x))=\phi(g(x’)$. But the end-to-end learnt counterpart of function $h$, with certain parameterisation, may learn to differentiate between the two. Therefore, it should be clearly stated that the authors assume that the function $h(x) = \phi(g(x))$, not that it’s likely the case.

Then the authors change the notation again, saying that actually one is dealing with a special type of  $h$, which is a neural network $f$. It looks confusing. Instead I understand that one can just define it in the very beginning that they assume that the neural network $f$ can be approximately decomposed into $f(x) \approx \phi(g(x))$ (this will be a kind of a concept bottleneck model, as per (Koh et al, 2020)). 

Then the authors say that they “ can show that the gradients of the two functions f and g point in the same direction”, but it is in no way obvious from the text that $\phi’ (g(x)$ would indeed be non-negative (or is it another assumption?). Furthermore, I am not sure what is $\phi’$? It is also unclear how the equivalence class from Eq. 5 folds into the rest of the narrative.

Questions on reproducibility and clarity:

The experimental section looks entirely unclear. I understand that the authors might assume that it would follow from the released code, but the paper needs to be self-sufficient in explanation and reproducibility and at least define the experimental setting and what should the readers refer to to reproduce the results. 

The authors state in line 233 that they are using genetic algorithm, but it is unclear where one can find a settings of such algorithm and what particular genetic algorithm they are referring to. There is no citation for the genetic algorithm either. There is no description of the neural network the authors use, nor there is any clarity about the dataset. The dataset should be described as well, with the links to the dataset and the procedure for reproducing the setting, also I cannot see in the text what are the input data the authors are using. Also, it does not relate to the claim that the authors are able to interpret the latent-space neurone as it is unclear while neurones are being interpreted.  

Also, is it possible to present any like-for-like comparison with other symbolic learning methods, perhaps Cranmer et al, 2020 or other related work aiming at symbolic interpretability?

### Questions
Questions on correctness: 

I’ve checked the maths carefully, and it seems to me that the model assumptions are conflated with the model properties. 
If we closely follow section 3.2, Eq.1 states that the model more likely learns the function as a composition of an uninterpretable transformation function $\phi$ and a closed form concept function $g$. The authors do not support that it actually the case. Then imagine that the function $g$ which maps inputs $x$, $x’$ into the same point, $g(x)  = g(x’)$. Then $\phi(g(x))=\phi(g(x’)$. But the end-to-end learnt counterpart of function $h$, with certain parameterisation, may learn to differentiate between the two. Therefore, it should be clearly stated that the authors assume that the function $h(x) = \phi(g(x))$, not that it’s likely the case.

Then the authors change the notation again, saying that actually one is dealing with a special type of  $h$, which is a neural network $f$. It looks confusing. Instead I understand that one can just define it in the very beginning that they assume that the neural network $f$ can be approximately decomposed into $f(x) \approx \phi(g(x))$ (this will be a kind of a concept bottleneck model, as per (Koh et al, 2020)). 

Then the authors say that they “ can show that the gradients of the two functions f and g point in the same direction”, but it is in no way obvious from the text that $\phi’ (g(x)$ would indeed be non-negative (or is it another assumption?). Furthermore, I am not sure what is $\phi’$? It is also unclear how the equivalence class from Eq. 5 folds into the rest of the narrative.

Questions on reproducibility and clarity:

The experimental section looks entirely unclear. I understand that the authors might assume that it would follow from the released code, but the paper needs to be self-sufficient in explanation and reproducibility and at least define the experimental setting and what should the readers refer to to reproduce the results. 

The authors state in line 233 that they are using genetic algorithm, but it is unclear where one can find a settings of such algorithm and what particular genetic algorithm they are referring to. There is no citation for the genetic algorithm either. There is no description of the neural network the authors use, nor there is any clarity about the dataset. The dataset should be described as well, with the links to the dataset and the procedure for reproducing the setting, also I cannot see in the text what are the input data the authors are using. Also, it does not relate to the claim that the authors are able to interpret the latent-space neurone as it is unclear while neurones are being interpreted.  

Also, is it possible to present any like-for-like comparison with other symbolic learning methods, perhaps Cranmer et al, 2020 or other related work aiming at symbolic interpretability?

Pang Wei Koh, Thao Nguyen, Yew Siang Tang, Stephen Mussmann, Emma Pierson, Been Kim, and Percy Liang, Concept Bottleneck Models, ICML 2020

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper presents a framework to interpret latent spaces of neural networks. The approach addresses the challenge of extracting human-readable concepts encoded in neurons within neural networks, particularly autoencoders and Siamese networks. The method constructs an equivalence class of functions that represent the same concept (under some assumptions) and retrieves interpretable mathematical expressions using symbolic search. It demonstrates its effectiveness in recovering invariants of matrices and conserved quantities under similarity and Lorentz transformations.

### Strengths
1. **Closed-form interpretation**. it is interesting that the proposed method produces closed-form interpretation for neurons. 

2. **Good performance on transformations**. the empirical results on similarity and Lorentz transformations are reasonable.

3. **Straightforward method**. The gradient-based method is easy to comprehend, despite some issues in the theory part.

### Weaknesses
1. **Interpretation limited to scalar outputs**. The proposed method assumes $f(\boldsymbol{x})$ and $g(\boldsymbol{x})$ to be in $C^{1}(\mathbb{R}^{n},\mathbb{R})$. This significantly restricts the method's applicability to high-dimensional latent spaces, where multi-dimensional vector-valued functions are the norm. While the method could be applied to each element of an output vector independently, this approach would (1) fail to capture inter-element relationships, and (2) be computationally inefficient. For instance, in a latent space representing object pose, the relationships between the x, y, and z coordinates are crucial, and interpreting each coordinate separately would lose the holistic understanding of the pose. Furthermore, the method does not address how to combine these individual interpretations into a coherent representation of the latent space.

2. **Issue with equivalence between $\tilde{H}_g$ and $H_g$**. The assumption that $g \in C^{1}(\mathbb{R},\mathbb{R})$ does not fully consider cases where $\phi'(g(x))$ is negative. In such instances, the gradient directions of $f$ and $g$ could be opposing, implying that functions in $\tilde{H}_g$ may not be present in $H_g$. This discrepancy undermines the theoretical foundation of the method, as it suggests that the gradient-based interpretation might not capture the full space of relevant functions.

3. **Class equivalence does not ensure correct interpretation**. Even if the issue with $\phi$ is resolved, the equality $\tilde{H}_g = H_g$ only establishes that the class of the ground truth function $\tilde{H}_g$ and the class of gradient-based interpretations $H_g$ are the same. It does not guarantee that the gradient-based method can recover the precise underlying $g(\boldsymbol{x})$. In practice, particularly in complex latent spaces such as those used in visual tasks, a single output could be explained by various combinations of input vectors. The proposed method might converge to an approximation or an equivalent function, but not necessarily the exact underlying concept. For example, a neuron might activate for both a specific object and a specific background, and the method might not be able to distinguish between these two concepts.

4. **Scalability of symbolic searching**. Genetic algorithms are known to scale poorly as the complexity of the search space increases. The paper does not provide empirical evidence demonstrating the method's effectiveness on complex latent spaces, such as those found in VAE-based image generation. The lack of such experiments raises concerns about the practical applicability of the method to real-world problems. The search space for symbolic expressions can grow exponentially with the number of input variables and the complexity of the mathematical operations, making it difficult to find the correct interpretation in a reasonable time.

5. (minor) **Assumption of $f$ and $g$ being continuously differentiable**. The assumption that $f$ and $g$ are continuously differentiable may not hold for all neural networks. For example, networks with ReLU activations are not continuously differentiable. The paper does not discuss how this non-differentiability affects the behavior of the proposed method. The gradient-based approach relies on the existence and smoothness of the gradients, and the presence of non-differentiable points could lead to unstable or incorrect interpretations.

### Questions
Please refer to the "weaknesses" section. 

Besides, it is clear that the proposed method is not applicable or scalable to all neural networks. Therefore, I would like the paper to explicitly discuss what types of neural networks and latent spaces it is able or unable to handle.

### Soundness
2

### Presentation
3

### Contribution
2
