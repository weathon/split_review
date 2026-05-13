# Make Haste Slowly: A Theory of Emergent Structured Mixed Selectivity in Feature Learning ReLU Networks

- Decision: Accept
- Scores: 8, 3, 5, 8

## Abstract
In spite of finite dimension ReLU neural networks being a consistent factor behind recent deep learning successes, a theory of feature learning in these models remains elusive. Currently, insightful theories still rely on assumptions including the linearity of the network computations, unstructured input data and architectural constraints such as infinite width or a single hidden layer. To begin to address this gap we establish an equivalence between ReLU networks and Gated Deep Linear Networks, and use their greater tractability to derive dynamics of learning. We then consider multiple variants of a core task reminiscent of multi-task learning or contextual control which requires both feature learning and nonlinearity. We make explicit that, for these tasks, the ReLU networks possess an inductive bias towards latent representations which are *not* strictly modular or disentangled but are still highly structured and reusable between contexts. This effect is amplified with the addition of more contexts and hidden layers. Thus, we take a step towards a theory of feature learning in finite ReLU networks and shed light on how structured mixed-selective latent representations can emerge due to a bias for node-reuse and learning speed.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work builds provides a step towards theory of feature learning in finite ReLU neural networks by building on an equivalence between ReLU networks and Gated Deep Linear Networks (GDLNs). The authors introduce "Rectified Linear Networks" (ReLNs), which are GDLNs specifically designed to imitate ReLU networks, allowing them to derive exact learning dynamics.
The key contributions are:

The introduction of ReLNs as a theoretical framework to analyze ReLU networks, providing tractable dynamics for finite-width networks during feature learning. A demonstration that ReLU networks exhibit an implicit bias towards structured mixed selectivity - where neural units are active across multiple contexts but in structured, reusable ways. 
Evidence that this bias towards mixed selectivity and node reuse is amplified when: 1) more contexts are added to the task
and 2) additional hidden layers are included in the network

The authors support their theoretical findings with analytical solutions and empirical demonstrations on several tasks, including an adapted XOR problem and multi-context classification tasks. They show that while ReLU networks aren't biased towards strictly modular or disentangled representations, they do learn structured features that can be somewhat reused across contexts.
The work takes a step towards understanding how and why structured representations emerge in ReLU networks during learning, bridging a gap in theoretical understanding between linear networks and modern deep learning architectures.

### Strengths
Disclaimer: I did not study the proofs of the paper, as I was very late reviewing this paper. I will try to find more time in the coming weeks. 

I find the paper clearly writtin and well presented, the authors make an effort presenting the dense results in a clear manner. The authors, to the best of my understanding, extend the theory around GDLNs and allow for a more in-depth study of the training dynamics of ReLU networks. I find the exposition of quite toyish tasks enlightning and make the paper more easy to follow.

### Weaknesses
I can not judge fairly the novely of the paper, especially its relation to Saxe et a., 2022. For me, it would have been helpful to highlight the novelty a bit more.

1) Can you comment a bit more on Assumption 2.1 - I know that the mutally diagonalizable structure is quite restrictive, in particular, can you comment on why the tasks you chose follow these assumption(s). Which tasks can you not study, give these assumptions?

2) Can you give a bit more experimental results, especially when training your networks. Maybe a hyperparameter table in the appendix is nice. Can you give more details how you derived hyperparameters when training networks, you for example mention some in Figure 2. I missed if these hps are analytically derived.

3) I find the discussion wrt to compositionality and modularity, you mention "strictly modular" in the abstract, a bit unclear. Can you clarify, or even define in the work, what you mean with this - and then contrast this to your findings. I guess the same applies for an up-front (maybe even in the intro) definition of what you mean with this. I would find it easier to follow the paper, having these things more clearly explained.

### Questions
1) Can you comment a bit more on Assumption 2.1 - I know that the mutally diagonalizable structure is quite restrictive, in particular, can you comment on why the tasks you chose follow these assumption(s). Which tasks can you not study, give these assumptions? 

2) Can you give a bit more experimental results, especially when training your networks. Maybe a hyperparameter table in the appendix is nice. Can you give more details how you derived hyperparameters when training networks, you for example mention some in Figure 2. I missed if these hps are analytically derived. 

3) I find the discussion wrt to compositionality and modularity, you mention "strictly modular" in the abstract, a bit unclear. Can you clarify, or even define in the work, what you mean with this - and then contrast this to your findings. I guess the same applies for an up-front (maybe even in the intro) definition of what you mean with this. I would find it easier to follow the paper, having these things more clearly explained.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces Rectified Linear Networks (ReLNs), a subset of Gated Deep Linear Networks (GDLNs) designed to capture the training dynamics of finite-dimensional ReLU networks. By drawing an equivalence between ReLU and ReLN, the authors aim to provide theoretical insights into feature learning and structured mixed selectivity in ReLU networks, especially in tasks involving multi-contextual inputs.

### Strengths
1. The introduction of ReLN as a GDLN variant to study ReLU dynamics is innovative and offers a new angle on understanding feature learning in finite ReLU networks.
2. The paper provides theoretical insights into inductive biases in ReLU networks, particularly regarding structured mixed selectivity and node reuse.

### Weaknesses
1. It remains unclear why ReLU’s training dynamics and mixed selectivity properties cannot be derived directly from ReLU networks, as they’re already nonlinear. Specifically, the paper does not adequately explain why the proposed ReLN framework is necessary, given that ReLU networks exhibit nonlinear behavior and feature learning capabilities. The authors should clarify why existing analytical tools for nonlinear networks are insufficient for studying the observed phenomena.
2. The approach is demonstrated on relatively simple tasks, raising concerns about scalability. For instance, applying ReLNs to realistic datasets like MNIST remains unaddressed. The paper lacks a clear discussion on the computational complexity of the ReLN approach and how it might scale with increasing data dimensionality and network size. The current experiments do not provide sufficient evidence that the proposed framework can be generalized to more complex scenarios.
3. Terms like "feature learning" and "pathway doing feature learning" (line 302) lack precise definitions. More clarity is needed to distinguish “feature learning” in this theoretical context. The paper needs to provide a rigorous definition of feature learning, specifying how it is measured and quantified within the ReLN framework. The current description is too vague and does not allow for a clear understanding of the claims made.

### Questions
1. Could the main findings (e.g., mixed selectivity) be directly observed in the ReLU network without using ReLNs?
2. Does the method extend efficiently to larger datasets (e.g., ReLU networks trained on MNIST), and can a ReLN adequately explain such networks?
3. Could the authors clarify their definition of "feature learning" and what they mean by a pathway "doing feature learning" (line 302)?

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
3

### Summary
The paper introduced "Rectified Linear Network" (ReLNs) as a subset of Gated Deep Linear Networks (GDLN), and showed that for single-hidden layer network, for a ReLU network, it's possible to find a ReLN that have same loss and outputs at all time-steps (provided that the assumption 2.1 at L159 are satisfied) in a simple synthetic dataset. Using the ReLN as the equivalence of ReLU, the authors provided an analytical solution for the training dynamic for the finite single-hidden layer network with synthetic dataset, and also demonstrated that the predicted loss of ReLN matches with the empirical loss of ReLU networks. In this specific synthetic dataset (which includes hierarchical structure (animals, plants, fish, birds), and multiple contexts), the papers show that the equivalent ReLN network employs an implicit bias for structured mixed selectivity (e.g, one gating pathway can encode multiple context).

### Strengths
**Originality**
1. The paper presents a novel framework Rectified Linear Network to analytically investigate the dynamic of finite-width single-hidden layer neural networks via an extension of Gated Deep Linear Network.

**Quality**
1. The paper provides theoretical proof for the equivalence between ReLN and ReLU for the case of finite-width single-hidden layer network and verified that the predicted loss matches with the empirical loss in a synthetic dataset.

**Clarity**
1. The paper clearly present the background relevant work, including the formulation of Gated Deep Linear Network, decomposition of eigenmodes, and derived of learning dynamic based on these eigenmodes.
2. The theoretical proofs are presented clearly with both informal and formal versions, along with a proof sketch in the main paper, and a detailed proof in the appendix, facilitating the reader's understanding
3. The empirical results (including the dataset and figures) are clearly presented with clear figure and caption, along with descriptions in the main text.

**Significance**
1. The paper showed that there's an equivalent ReLN for ReLU for a single-hidden layer network, and it's possible to identify the gating structure of this equivalent ReLN via a clustering algorithm.
2. By investigating the gating structure of the equivalent ReLN network, the paper shows that there's an implicit bias for structured mixed selectivity (e.g, one gating pathway can encode multiple context).

### Weaknesses
While the paper proposed a novel framework ReLN to study learning dynamic and feature learning in finite-width neural network, a significant topic in the machine learning community, the paper has several limitations in both theoretical and empirical results, which I would clarify below:

1. Theoretical results: The main theoretical results of the paper requires very strong assumptions (L159, *Assumption 2.1*) in both (1) input dataset (*The dataset correlation matrices are mutually diagonalizable*) and (2) model training trajectory (*The neural network weights align to the singular vectors of the dataset correlation matrices.*). These are very strong assumptions, and the authors did not offer any analysis on specific scenario in which these assumption holds or not hold. For instance, the mutual diagonalizability of correlation matrices implies a very specific structure in the data, where different features are uncorrelated after a linear transformation. This is unlikely to hold in real-world datasets where features often exhibit complex, non-linear dependencies. Furthermore, the assumption that weights align with singular vectors is a significant constraint on the training dynamics, potentially excluding many realistic training scenarios where weights might explore a more complex trajectory. As we see in section 6, assumption (2) is violated in the case of 2-layer hidden network. As the paper only uses a very simple synthetic dataset (one-hot vector input and sparse binary-vector output), it's difficult to tell whether assumption (1) can hold for realistic dataset with complicated distribution, even in the 1-layer hidden network case.

2. Empirical evaluations: The empirical experiments that supports the claim and theoretical results only includes single-layer hidden network on a simple synthetic dataset (the paper did include 2-layer hidden network but this experiment did not align with the theoretical results, due to violation of the theoretical assumption). While it's reasonable to use this simple synthetic dataset as a proof of concept to verify the theoretical results and illustrate the mixed-selectivity phenomenon, it would be helpful and more convincing if the authors can demonstrate that the proposed approach work in a realistic image dataset (MNIST, CIFAR, etc.) with a more realistic and variety of model architectures (multiple layer perceptron, convolutional neural nets, etc.). The inclusion of real dataset and variety of architecture is even more important since the theoretical results require such strong assumptions. The lack of experiments on more complex datasets and architectures makes it difficult to assess the practical relevance and generalizability of the proposed framework.

3. Identification of gating structure: The gating structure identification is a central bottleneck of this framework, since gating *g* is treated as inputs, and needed to be identified before training. Identifying a fixed gating structure, or varying gating structure through training, would be one of the major difficulty of the framework. The paper did propose a clustering algorithm to identify the gating structure of ReLN from the representation of ReLU models. However, since the paper only operates with very small synthetic dataset and models, it's unclear whether this clustering algorithms can scale with realistic dataset and larger models. Furthermore, the clustering approach itself is not detailed, leaving uncertainty about its robustness and sensitivity to hyperparameter choices. Therefore, this is another reason that it is critical to evaluate this proposed framework on more realistic dataset, instead of only on the simple synthetic dataset.

### Questions
**Questions**
1. [L159] Would be helpful to comments on cases for each of the mentioned assumptions in `Assumption 2.1` since these seem to be not very general assumptions and can be easily violated.
2. [L183] What is the network architecture for the XoR dataset? Is it a 2-layer network? How would the gating structure look like? It would be helpful to explicitly write down the equation or numerical examples instead of vague description of “2 pathways” and “4 pathways”.
3. [L257] How do these pathways get identified? Are they identified manually based on the prior knowledge about the task? Since identifying gates would be a major bottleneck for the applications of ReLN, it would be helpful to provide more information on how to identify the pathways.

**Suggestions**
1. In the Contribution section, clearly state the models and dataset in which the theoretical and empirical results are obtained (single-layer network for theoretical results, and simple synthetic dataset with hierarchy and context (maybe would be helpful to give this dataset a name for easy reference?) to provide a clear expectation for the readers.
2. Spending more space in the main text to explain how to identify the gating structure and pathways from ReLU to ReLN.

### Soundness
2

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
3

### Summary
This paper shows that, under strong alignment assumptions of the data and network weights, finite feature learning ReLU networks learn modules that can be represented by Gated Deep Linear Networks (GDLNs), for which the exact learning dynamics are analytically tractable. For a synthetic task with hierarchical structure, the training dynamics of 2-layer ReLU nets are shown to exactly match those of a GDLN constructed for the task. Through this equivalence, it is shown that ReLU networks learn mixed-selective representations due to a bias for optimal learning speed.

### Strengths
The approach of identifying the linear submodules learned by ReLU networks and using this for tractability of the analysis is interesting. At least on toy datasets, natural modules to learn the structure in the data are exactly recovered by ReLU networks together with the learning speed. This provides mechanistic understanding how the bias toward learning speed explains why 2-layer ReLU networks learn common and context-specific but entangled representations.

### Weaknesses
I cannot strongly recommend acceptance as some key questions remain unaddressed. While this is a nice and tractable toy model for the learning dynamics of 2-layer ReLU networks, generalizability of the findings is questionable. The results only hold for the synthetic and very specific structure considered. The relevance on real data sets or practical architectures remains elusive, as it is not evaluated. The authors show and acknowledge that the silent alignment Assumption 2 already does not hold for 2-hidden-layer ReLU nets. In Figure 6, against the authors’ claim of ‘sharing the same characteristics’, ReLU networks appear to make larger, sharper steps in the loss. What happens in more practical architectures and real datasets, and whether an appropriate and interpretable GDLN can still be identified remains completely unclear. Experiments that show that this approach works on real data would greatly alleviate these concerns. See other critical questions below.

**Typos in lines:** 30, 392, many in 462-463, 473, 476, 477, 503, 527

### Questions
**Critical questions (order: most important to least important):**

1. Your analysis looks very particular to the structure of your synthetic task. Do you think it will be feasible to find unique or representative GDLNs for more complex datasets and architectures?

    a. Are the assumptions more generally broken, even for 2-layer ReLU nets beyond this toy task of hierarchical structure without noise? Atanasov et al. (2021) show that non-whitened data can weaken the silent alignment effect.

    b. ‘Once the common pathway has finished learning there is no correlation between the context features and labels’. But in practice, likely learning is not perfectly separated. Which impact does this have on the generalizability of your results?

2. You claim that the learning dynamics of the ReLN exactly describe those of the ReLU network. Why are the curves in Figure 4 then not exactly matching?
3. How do your results depend on the number of neurons? You never explicitly mention this.
4. Your proposed clustering algorithm in Appendix B evaluates the model at different stages of training. Is this not dangerous in cases where the learned function evolves in a more complex way than in your toy task and systematically changes? Then the algorithm tries to cluster outputs from intermediate functions that are rather unrelated to the final learned function. I would like to see whether clear gating mechanisms can be identified when applied to real data.

**Questions out of curiosity:**

1. In Figures 4 and 5, why is not the largest SV learned first?
2. Where does the bias towards node reuse come from? Can you see this in the learning dynamics equations?
3. Can your analysis be extended to SGD? Would you expect fundamentally different dynamics?
4. Can this theory also inform how to maybe slow down learning to learn disentangled representations?

**References:**

Atanasov, Alexander, Blake Bordelon, and Cengiz Pehlevan. "Neural networks as kernel learners: The silent alignment effect." *arXiv:2111.00034* (2021).

### Soundness
3

### Presentation
3

### Contribution
2
