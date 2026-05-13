# PREDICTING THE BEHAVIOR OF AI AGENTS USING TRANSFER OPERATORS

- Decision: Reject
- Scores: 8, 5, 5

## Abstract
Predicting the behavior of AI-driven agents is particularly challenging without a preexisting model. In our paper, we address this by treating AI agents as stochastic nonlinear dynamical systems and adopting a probabilistic perspective to predict their statistical behavior using the Fokker-Planck equation. We formulate the approximation of the density transfer operator as an entropy minimization problem, which can be solved by leveraging the Markovian property and decomposing its spectrum. Our data-driven methodology simultaneously approximates the Markov operator to perform prediction of the evolution of the agents and also predicts the terminal probability density of AI agents, such as robotic systems and generative models. We demonstrate the effectiveness of our prediction model through extensive experiments on practical systems driven by AI algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper addresses the challenge of predicting AI agents' behavior, treating these agents as stochastic nonlinear dynamical systems. Using a probabilistic approach, the authors propose a framework based on the Fokker-Planck equation to predict statistical behaviors via an entropy minimization strategy. Their primary contribution is the PISA algorithm, which enables accurate predictions of agents' behavioral density evolution, particularly over long horizons. PISA leverages the spectral decomposition theorem to simultaneously approximate the Markov operator from agent trajectory data and predict asymptotic behavior. The authors demonstrate PISA's effectiveness in diverse applications, including robot trajectory prediction, generative model behavior, and pedestrian movement forecasting.

### Strengths
- The paper introduces a unique probabilistic perspective on AI agent behavior, combining concepts from stochastic processes with the Fokker-Planck equation. The originality stems from adapting a statistical density-based approach for complex, high-dimensional AI-driven environments. The spectral decomposition-based formulation for behavioral density evolution is novel in predicting long-term agent alignment.
- The mathematical rigor is evident, with clear derivations of the density evolution framework and detailed algorithmic steps. The PISA algorithm’s grounding in spectral decomposition provides robust theoretical backing. Although, it might be possible that I have not completely understood some parts of the proof.
- I feel that this research tries to address the need to understand and predict the behavior of complex AI agents, which has critical implications for fields requiring safety and reliability in autonomous systems. Applications like reinforcement learning, generative modeling, and pedestrian prediction show the method's versatility.

### Weaknesses
Because the paper does not situate the proposed method in a broader context (neither by discussing other work on the problem of predicting AI systems' behavior, nor by discussing how the results compare to alternative approaches), I hard a hard time judging the contribution of this paper.

1. The introduction section contains basically no citations. Has nobody else worked on the problem of predicting the behavior of AI systems? There are several places where the text hints at relevant work, but does not cite any. Here are some examples (although this is not an exhaustive list):
    - "The integration of artificial intelligence (AI) models within autonomous agents has transformed many fields" (l. 26 - 27)
    - "there has been a notable increase in modeling these behaviors as nonlinear dynamical systems" (l. 46 - 47)
    - "techniques such as Dynamic Mode Decomposition (DMD) and its generalizations have demonstrated significant capability in revealing the underlying evolutionary laws of AI agents" (l. 47 - 48)
    - "Although the application of probabilistic models to learn and predict the statistical behavior of complex AI agents has increasingly attracted interest in areas such as autonomous driving, motion planning, and human-robot interaction" (l. 53 - 54)
2. The paper does very little to be accessible to a broader audience that might be in interested in predicting behavior but is not well-versed in statistical mechanics. In particular, a section providing a bit more mathematical background and intuition about the Perron-Frobenius operator (transfer operator / Markov operator) would be useful. For instance, explaining how the eigenvalues and eigenfunctions of this operator relate to the long-term behavior of the system would greatly benefit the reader. A discussion of the limitations of using a finite number of samples to approximate the operator would also be helpful.
3. The part where the reasoning behind the model and loss function is explained (Section 4) would be more useful in the methods section instead of after the results. The current structure makes it difficult to understand the motivation behind the specific choices made in the method.
4. The description of the methods is not very detailed, so that reproducing the results would be difficult just from the paper. For example, there is no indication of how the hyperparameters of the training were set, and little detail is provided on the neural network architectures and the training procedure. For example, what is the specific architecture of the neural networks used to represent the functions G and A? What optimization algorithm is used? What are the learning rates and batch sizes? I understand that there are page limits, but there is also no code provided and no supplementary material.
5. No code is provided as supplementary material, which might have been helpful to address the shortcoming mentioned in the previous point and to get an intuitive understanding about how the abstract mathematical concepts are represented in concrete code. This lack of code also makes it difficult to verify the claims made in the paper.
6. As someone who was not familiar with this kind of modeling of the evolution of non-parametrically estimated densities, it was hard for me to judge how the approach compares to alternative appraoches, such as directly modeling the stochastic dynamics of the state (e.g. using a parametric model). This narrowness might be fine if the paper wants to provide a specific technical contribution in the context of these approaches. But the way the introduction is set up with the quite general goal of predicting the behavior of AI systems, I expected at least some comparison to alternative approaches. This applies to several sections of the paper
    a. The literature review is quite narrowly focused on methods for estimating the transfer operator. What about other approaches to reachability analysis, trajectory prediction etc.? For example, methods based on Hamilton-Jacobi reachability analysis or sampling-based methods for trajectory prediction are not discussed.
    b. The results only includes a comparison with two other methods. Are these the only applicable baseline methods? Please justify. It is unclear why these specific baselines were chosen and whether they represent the state-of-the-art in predicting the behavior of AI systems.
    c. The discussion section also does not set the method in a broader context. It hints at the limitations resulting from using KDE to approximate the densities. How does this compare to possible alternative approaches? For example, how does the performance of the method compare to methods that directly model the stochastic dynamics using a parametric model, especially in high-dimensional spaces?
7. Formatting errors
    - Section 2.1 still contains parts of the instructions for using ICLR's Latex template (l. 180 - 181)
    - The citation style often makes no distinction between in-text citations and citations that should be in parentheses (e.g. l.60, l. 105 - 106, l. 153)

### Questions
1. Could the authors elaborate on the feasibility of adapting PISA for real-time, high-dimensional AI systems? Additionally, has the choice of Gaussian kernel in KDE been optimized for different applications? Would adaptive kernel techniques enhance density estimation accuracy?
2. The authors mention the computational resources used for experiments but do not discuss performance time or computational trade-offs explicitly. Can the authors quantify PISA's computational efficiency compared to DPDD and Meng et al., especially in scenarios requiring frequent density updates?
3. How robust is PISA if the Markov assumption for AI agent dynamics is slightly violated? Could incorporating non-Markovian extensions or memory-enhanced operators enhance prediction accuracy for more complex behaviors?
4. The paper evaluates PISA primarily through KL divergence. Have other evaluation metrics been considered (e.g., likelihood estimation or out-of-sample testing)? It would be insightful to understand the robustness of PISA across various performance metrics.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a method for producing the statistical behavior (terminal distribution) of agents using the  Fokker-Planck equation.

### Strengths
The paper is well-written and well-motivated.  
The statistical analysis appears to be sound.
To the best of this reviewer's knowledge, this exact method for agent modeling has not been previously defined.

### Weaknesses
The paper seems to suggest that the idea of agent modeling originated in the 2020s.  All related work is from that time or later.
There is a survey entitled "Autonomous Agents Modelling Other Agents" that was published in 2017 and covers research from at least the two decades prior to that.  To properly assess the novelty of this approach, the authors should relate to the prior research and identify the closest methods for direct comparison.

Finding the "terminal distribution" of the agent behavior appears to amount to finding the stationary distribution of a Markov process.  Is that the case?  If so, there have been prior methods for doing so that ought to be compared.

If I understand correctly, the approach is designed for a purely single agent context, without any strategic interactions among agents.  Nonetheless, it is assessed in a pedestrian domain, which is an inherently multiagent setting.  Methods such as replicator dynamics (e.g. see the work of Karl Tulys et al.) could be brought to bear for finding the terminal distribution.

### Questions
Please see the weaknesses section.

### Soundness
3

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
2

### Summary
The paper aims to predict the behavior of AI systems using density estimation and models of the stochastic dynamics of the systems. It introduces a method based on learning the evolution of probability densities from trajectory data. The probability densities at each time step are first non-parametrically approximated using kernel density estimates. A transfer operator on the densities is then learned assuming a particular proposed functional form involving neural networks. The method is evaluated on three examples: a reinforcement learning agent in a continuous control domain, a score-based generative model, and a dataset of pedestrian walking. In comparison with two baseline methods, the predicted densities are closer to the true densities in terms of the KL divergence.

### Strengths
In general, the paper tackles an interesting problem and the results are clearly presented. The key strength of the method seems to be the ability to directly predict the stationary distribution (eq. 9), which would not be straightforward to obtain for many other approaches.

### Weaknesses
Because the paper does not situate the proposed method in a broader context (neither by discussing other work on the problem of predicting AI systems' behavior, nor by discussing how the results compare to alternative approaches), I hard a hard time judging the contribution of this paper.

1. The introduction section contains basically no citations. Has nobody else worked on the problem of predicting the behavior of AI systems? There are several places where the text hints at relevant work, but does not cite any. Here are some examples (although this is not an exhaustive list):
    - "The integration of artificial intelligence (AI) models within autonomous agents has transformed many fields" (l. 26 - 27)
    - "there has been a notable increase in modeling these behaviors as nonlinear dynamical systems" (l. 46 - 47)
    - "techniques such as Dynamic Mode Decomposition (DMD) and its generalizations have demonstrated significant capability in revealing the underlying evolutionary laws of AI agents" (l. 47 - 48)
    - "Although the application of probabilistic models to learn and predict the statistical behavior of complex AI agents has increasingly attracted interest in areas such as autonomous driving, motion planning, and human-robot interaction" (l. 53 - 54)
2. The paper does very little to be accessible to a broader audience that might be in interested in predicting behavior but is not well-versed in statistical mechanics. In particular, a section providing a bit more mathematical background and intuition about the Perron-Frobenius operator (transfer operator / Markov operator) would be useful.
3. The part where the reasoning behind the model and loss function is explained (Section 4) would be more useful in the methods section instead of after the results.
4. The description of the methods is not very detailed, so that reproducing the results would be difficult just from the paper. For example, there is no indication of how the hyperparameters of the training were set, and little detail is provided on the neural network architectures and the training procedure. I understand that there are page limits, but there is also no code provided and no supplementary material.
5. No code is provided as supplementary material, which might have been helpful to address the shortcoming mentioned in the previous point and to get an intuitive understanding about how the abstract mathematical concepts are represented in concrete code.
6. As someone who was not familiar with this kind of modeling of the evolution of non-parametrically estimated densities, it was hard for me to judge how the approach compares to alternative appraoches, such as directly modeling the stochastic dynamics of the state (e.g. using a parametric model). This narrowness might be fine if the paper wants to provide a specific technical contribution in the context of these approaches. But the way the introduction is set up with the quite general goal of predicting the behavior of AI systems, I expected at least some comparison to alternative approaches. This applies to several sections of the paper
    a. The literature review is quite narrowly focused on methods for estimating the transfer operator. What about other approaches to reachability analysis, trajectory prediction etc.?
    b. The results only includes a comparison with two other methods. Are these the only applicable baseline methods? Please justify.
    c. The discussion section also does not set the method in a broader context. It hints at the limitations resulting from using KDE to approximate the densities. How does this compare to possible alternative approaches?
7. Formatting errors
    - Section 2.1 still contains parts of the instructions for using ICLR's Latex template (l. 180 - 181)
    - The citation style often makes no distinction between in-text citations and citations that should be in parentheses (e.g. l.60, l. 105 - 106, l. 153)

### Questions
- Is the method specific to the use case of predicting the behavior of AI systems or is it applicable in general to stochastic dynamical systems? The introduction suggests the former, but the rest of the paper the latter.
- What is the role of the two hyperparameters of the loss function ($\lambda$ and $\mu$)? How were they set? How does changing these hyperparameters affect the performance of the method?
- Algorithm 1: how are the constraints on the functions $G_\gamma^i$ and $A_\theta^i$ enforced? Which optimization algorithm is used to train the neural networks?
- Non-parametric density estimation techniques are known to be particularly prone to the curse of dimensionality. How does the method scale to higher-dimensional spaces?

### Soundness
2

### Presentation
2

### Contribution
2
