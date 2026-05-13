# Learning Successor Representations with Distributed Hebbian Temporal Memory

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
This paper presents a novel approach to address the challenge of online temporal memory learning for decision-making under uncertainty in non-stationary, partially observable environments. The proposed algorithm, Distributed Hebbian Temporal Memory (DHTM), is based on factor graph formalism and a multicomponent neuron model. DHTM aims to capture sequential data relationships and make cumulative predictions about future observations, forming Successor Features (SF). Inspired by neurophysiological models of the neocortex, the algorithm utilizes distributed representations, sparse transition matrices, and local Hebbian-like learning rules to overcome the instability and slow learning process of traditional temporal memory algorithms like RNN and HMM. Experimental results demonstrate that DHTM outperforms LSTM and a biologically inspired HMM-like algorithm, CSCG, in the case of non-stationary datasets. Our findings suggest that DHTM is a promising approach for addressing the challenges of online sequence learning and planning in dynamic environments.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this work, the authors proposed a novel approach to learn successor representations inspired by neuroscience. In particular, the model uses an underlying graphical model and applies message passing algorithms. The messages from the latent representations of previous timesteps contribute to the factors which are then used to compute the expected value function of the latent representation and the resulting policy. The authors tested their hypothesis in a 2D pinball environment against LSTM, a transformer based recurrent neural network model (Receptance Weighted Key Value) and a recurrent neural network that has been extended with a linear recurrent unit to handle long sequence modeling tasks (LRU). Considering a metric based on pseudo-surprise, the authors claimed that their model is able to approximate the successor representations better. They also simulated a changing task by comparing successor representations learned using 5-step vs 1-step temporal difference (TD) learning. Unsurprisingly, perhaps due to better reward error propagation, the model that uses the 5-step TD learning algorithm is able to adapt to the second task faster.

### Strengths
Overall, the writing and presentation are straightforward. The authors kept the writing simple which made it easier for me to digest the paper. The motivation of pursuing the research idea is clear.

### Weaknesses
The figures and the structure of the paper can be greatly improved. Please see the questions below.

The authors only consider one simple environment. It will be interesting to study their approach in 2D maze environments, such as the Minigrid environment, which are commonly used to study successor representations. This environment will also allow more analysis and make better and more accurate comparisons with ground truth successor representations. Specifically, the authors could compare their learned representations to the true discounted future occupancy to provide a more quantitative evaluation of the model's ability to learn accurate successor features. The current pinball environment, while useful for initial testing, does not provide the same level of interpretability and may limit the generalizability of the findings.

At the moment, it is hard to understand why their proposed model is performing better than the baseline. The baseline models seem to have more complex architectures but no learning curves were presented to verify that the complexity reduces the learning efficiency of these models. Without learning curves, it is difficult to determine if the baselines were given sufficient time to converge or if they were hyperparameter-optimized to the same degree as the proposed model. This makes it challenging to draw firm conclusions about the relative performance of the models.

### Questions
1.  Writing: Please spell out the full term at its first mention, indicate its abbreviation in parenthesis and use the abbreviation from then on. Example: Receptance Weighted Key Value (RMKV), Hidden Markov Model (HMM) etc. It makes it much easier to read and follow, especially for those who might not be familiar with all these models. 
2. There are some grammar errors: 
   a. … which can be formalized as agent?? Reinforcement Learning for a Partially Observable Markov Decision Process (POMDP) (Poupart, 2005).
3. Avoid using M for both successor representations and Messages. I understand that it is common to use M for SRs. Perhaps you can use “m” for messages. 
4. The caption for Figure 1 is lacking in detail and doesn't provide enough context to fully grasp its significance. It's understandable that you wouldn't want to repeat the main text, but some additional details in the caption would enhance clarity. The authors might also want to consider adding equations or indicating the link to the equations in the figure.
  a .1. What is i here? 
  b. Figure B is unclear. What do the variables E represent? Likewise, are the w_u and w_u'_l? 4. What is E?
  c.What does the red circle represent in Figure C? Is Figure C the overall graphical model? 

5. It was stated in the abstract that the proposed model is inspired by “neurophysiological models of the neocortex, distributed representations, sparse transition matrices, and local Hebbian-like learning rules.” The introduction of binary cell activities, presynaptic cells as well as receptive fields could be greatly enhanced by including them in Figure 1. This would create a more cohesive and complete visual representation of the concepts.

6. It is a common practice to use mathbb{I} for indicator function. This will help to remove the confusion with the Identity matrix. 

7. In algorithm 1, link it with the equations being optimized during the learning process. At the moment, it is hard to tell how your proposed algorithm contributes to the standard reinforcement learning framework. 

8. “The next step after computing p(h_{t}^{k}) distribution parameters is to incorporate information about .."  How does this relate to algorithm 1? 

9. How are the weights w_u_l being learned? Is it through equation 18? If it is, eq 18 should be moved to the main paper.
 
10. Details for the agent’s architecture are missing. Please provide them in the appendix. Ideally, given that you proposed a novel method, a computational graph of your architecture should also be included so that the readers can relate it to figure 1 and algorithm 1. 

11. Figure 4 seems to have very high variance. How many seeds are being used to generate the results in this plot? Looks like more seeds are required. 

12. Also, in figure 4, there seems to be a stability issue for the 1 step model as the average reward did not stabilize for the first task and starts to diverge before the task switches.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces an novel approach for learning sequences in partially observable environments called Distributed Hebbian Temporal Memory (DHTM). DHTM is rooted in factorial HMMs and incorporates local Hebbian-like learning rules and transition matrix sparsification, both inspired by biologically plausible multi-compartment neural models. The authors illustrate DHTM's capability to learn successor representations and demonstrate its functionality in a simple pinball environment.

### Strengths
This paper tackles the significant challenge of online hidden representation learning for decision-making in non-stationary, partially observable environments. The proposed method, DHTM, amalgamates various intriguing concepts, such as factorial HMMs, successor representations, and multi-compartment neuron models. The biological plausibility of the method is a notable feature. I believe there is ample potential for further exploration and the establishment of very interesting results in this research direction.

### Weaknesses
This paper brings together a wide array of interesting concepts, including factorial HMMs, successor representations, multi-compartment neuron models, and sparse distributed representations, making it a dense and challenging read. It would definitely benefit from a longer format, such as a journal article. However, there remains three-quarters of a page that could be employed to break down and refine Section 3.1 on Distributed Hebbian Temporal Memory. Dividing this section into smaller subsections would aid in better organizing the material. For example, the description of the Hebbian learning rule could be more clearly delineated from the update of the transition matrix. Additionally, incorporating a notation glossary, either in the main paper or in an appendix, would be a valuable addition. It is difficult to keep track of the various symbols and their meanings, especially with the use of superscripts in the factor graph model, which are not immediately clear. 

Although the model itself is quite compelling, the experiments fall short of doing it justice. Only a single experimental result is provided, where the performance is marginally inferior to one of the baseline models, the fchmm. The results presented do not fully demonstrate the potential of the proposed method. There is potential for more comprehensive experiments that can showcase all the intriguing aspects of this model, such as the online learning capability and the emergence of sparse representations. The current experiment does not adequately highlight these advantages. Furthermore, the lack of a thorough hyperparameter search and sensitivity analysis makes it difficult to assess the robustness of the method. 

Minor issues include typos and grammatical errors scattered throughout the text.

### Questions
- In section 2.4, when you mention the "spatiotemporal property of cortical network activity," what specific aspect or characteristic are you referring to?
- In the factor graph model, what do the superscripts $i$ and $k$ correspond to?
- What parameter values were used for DHTM for the results in Figures 3 and 4? What about for the other methods?

### Soundness
2 fair

### Presentation
1 poor

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
This paper introduces Distributed Hebbian Temporal Memory (DHTM), a state-update function used to derive an approximate Markov state in partially observable environments. The DHTM is modeled as a factor graph of an HMM with additional modifications to consider the dependence of hidden states. The paper’s primary contribution is to introduce a graphical model that approximates the successor representation in finite horizon POMDPs.

### Strengths
- The problem that the authors address is an important one, i.e., developing models that can infer the underlying Markov state from partially observed sequential data.
- DHTM relies on local Hebian-like updates, avoiding some of the issues of gradient-based sequence models employing backpropagation like RNNs.

### Weaknesses
I think the current state of the paper isn’t in a form I would feel comfortable recommending for acceptance. The paper does present a novel architecture, but much of the paper relies on empirically demonstrating DHTM’s effectiveness, which I believe the authors haven't done convincingly. Furthermore, I feel the authors should discuss the limitations of their method and better discuss related work. Below, I’ll address specific concerns:

- The method as presented wouldn’t scale to infinite horizon or large POMDPs. At the very least, I’d like to see a discussion on the challenges presented when scaling DHTM. Specifically, the use of a factor graph with a fixed number of hidden variables and connections seems inherently limited in its ability to represent complex, long-range dependencies in the environment. The paper should address how the number of hidden variables and their connectivity would need to grow with the complexity of the POMDP and how this growth would impact computational cost and learning stability.
- The empirical methodology and agent architecture are poorly explained, which makes it hard to evaluate the method. More direct questions can be found below.
- The empirical results are of limited value; specifically, the authors use a single custom environment with non-standard metrics (see below for more questions about pseudo-surprise). The lack of comparison to standard RL benchmarks makes it difficult to assess the practical relevance of the proposed method. The use of a custom environment also raises concerns about the generalizability of the results. Furthermore, the pseudo-surprise metric is not a standard measure, and its interpretation and relevance to the task are unclear.
- The paper could be better positioned in the literature regarding successor representations in POMDPs. For example, I expected to see a discussion with [1], which seeks to model an SR in POMDPs. The current discussion lacks a thorough comparison with existing approaches, particularly those that address the challenges of partial observability and temporal abstraction in successor representation learning. The paper should clarify how DHTM compares to and differs from these methods, highlighting its unique contributions and limitations.

### Questions
- Section 2.1, shouldn't optimal policy be defined as $\text{argmax}_a$ not $\text{softmax}_a$?
- The SR in RL is defined with respect to a policy; in DHTM, the target policy is ignored. Is this on purpose? If so, could authors comment on this and the difficulties of adapting their estimate with a changing policy?
- Section 2.3, I’m quite confused about this section; although the SR could be used to model observations, you’ve discussed the SR up to this point as being a good representation of the hidden state. I’m not sure that the expected discounted observation occupancy, given a state, is the same object. It feels like successor features should be discussed here, as there’s an implicit assumption that the reward function lies in the span of the observation features. You might not be able to linearly predict the value function $V(h)$ given $M^\pi(\cdot | h) \in \mathbb{R}^{|\mathcal{O}|}$.
- Section 4, can you describe how the pseudo-surprise is computed? I’m not sure I fully understand what’s going on here.

### Agent Architecture

- Can you provide more details about the baseline methods and how they are employed in the architecture? e.g., what’s the input to the RNNs?
- What is an SR representation here? A tabular representation of the SR with respect to the HMM states?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The current work implements belief propagation in Hidden Markov Models using neural circuits.

### Strengths
The implementation of belief propagation in a neural circuit is innovative.

### Weaknesses
The article has three main shortcomings:

There is a lack of theoretical analysis for the proposed algorithm. Many parts of the article involve approximations or assumptions, but the author fails to discuss these aspects. For example, the author does not explain why the 'independent' variable can be represented in the form of Eq. (11), and the parameters such as w_ul, learned using Hebbian rules, lack clear explanations. The learning targets and the specific characteristics of the learning dynamics are also left unaddressed.

Secondly, the author fails to provide a clear description of the entire workflow of the algorithm. It is uncertain whether the sum–product message passing can converge within the given graphical structure. If it does converge, it needs time to do so. It is unclear how many iterations are required for message m_u to converge. If multiple iterations are needed for convergence, the transmission of information from time t+1 to t may be questionable. Actions also affect the transition matrix of HMM, but in Section 3.1, I did not see the author modeling actions.

The article does not clarify the specific biological correspondences of 'f' and 'm' within the context of sum–product message passing. 'f' appears to correspond to neural connections, but neural connections are typically one-to-one. If 'f' includes more than two nodes, its precise correspondence within a neural circuit is unspecified. Similarly, the biological interpretation of 'm' is not clearly defined, and the mechanism for nodes to transmit 'm' among each other remains unclear.

### Questions
See weakness

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair
