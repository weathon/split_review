# Learning from Demonstration with Implicit Nonlinear Dynamics Models

- Decision: Reject
- Scores: 3, 5, 6, 3

## Abstract
Learning from Demonstration (LfD) is a useful paradigm for training policies that solve tasks involving complex motions, such as those encountered in robotic manipulation. In practice, the successful application of LfD requires overcoming error accumulation during policy execution, i.e. the problem of drift due to errors compounding over time and the consequent out-of-distribution behaviours. Existing works seek to address this problem through scaling data collection, correcting policy errors with a human-in-the-loop, temporally ensembling policy predictions or through learning a dynamical system model with convergence guarantees. In this work, we propose and validate an alternative approach to overcoming this issue. Inspired by reservoir computing, we develop a recurrent neural network layer that includes a fixed nonlinear dynamical system with tunable dynamical properties for modelling temporal dynamics. We validate the efficacy of our neural network layer on the task of reproducing human handwriting motions using the LASA Human Handwriting Dataset. Through empirical experiments we demonstrate that incorporating our layer into existing neural network architectures addresses the issue of compounding errors in LfD. Furthermore, we perform a comparative evaluation against existing approaches including a temporal ensemble of policy predictions and an Echo State Network (ESN) implementation. We find that our approach yields greater policy precision and robustness on the handwriting task while also generalising to multiple dynamics regimes and maintaining competitive latency scores.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a method for incorporating non-linear dynamic systems in a policy representation for learning from demonstration (LfD). The approach extends the echo state networks architecture to include learned components to embed the inputs of the policy (pen state + image to be drawn). These input embeddings are then integrated into the architecture in a way that influences the dynamics of the layer. The work is evaluated on the LASA human handwriting dataset. The baselines are: feedforward networks, echo state machine, and temporal ensembling. The results show that the proposed method improves precision and generalization without strongly compromising the jerkiness of the movements and the latency of the inference.

### Strengths
- the paper is well-written and enjoyable to read.
- the paper is self-contained and includes most of the needed background knowledge for an author to follow.
- the proposed method is quite interesting. It makes a lot of sense to model temporal dynamics with non-linear dynamical systems for learning from demonstration.
- the experiments study multiple metrics that are relevant to the LASA dataset.
- the results are very promising and nicely demonstrate the benefits of the method, namely improving precision and generalization without strongly compromising latency.

### Weaknesses
My main concern with this work is in its evaluations:
- the experiments do not include multiple baselines that account for context or memory such as transformer, SSMs, LSTMs...
- the experiments are limited to a single small-scale dataset. It would be interesting to understand how the proposed method would perform on various LfD tasks. Ideally, it would be nice to include tasks that require the policy to be reactive, for instance, tasks involving interaction with an object like pushing, or sticking to your example, drawing the drawings from different starting positions.
- the paper lacks ablations of some components and hyperparameters it includes (ResNet, $\alpha$...).

**Minor issues:**

- punctuation of equations is missing for most equations.
- line 341 --> represented using/by a neural network.

### Questions
- why does the proposed approach lead to a higher jerk than the temporal ensembling baseline (figure 3f)? 
- why the latency of the ESN is worse than their method in Table 1 but better in Table 2?
- can you elaborate further on how the proposed method ensures the preservation of the echo state property?
- how would the proposed method perform on more reactive and complex tasks, for instance, tasks involving interaction with an object like pushing, or sticking to your example, drawing the drawings from different starting positions?
- how does the method compare to transformer, SSM, and LSTM-based architectures?
- there are multiple ways of implementing temporal ensembling, can you elaborate on your temporal ensembling approach?

For all questions, please provide possible explanations or hypotheses where suited.

### Soundness
3

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
2

### Summary
This paper proposes a combination of neural networks and nonlinear dynamics models to model sequential data. In comparison to traditional reservoir computing, the additional neural components in the dynamic model allow for better generalization. The authors demonstrate that the new proposed layer reduces the compounding error in LfD on the Human Handwriting Dataset.

### Strengths
* A simple idea that updates the ESN with newer deep learning-based components.
* The paper is well-written and presents its ideas clearly, making it accessible and easy to follow.
* Code release for simple integration of the proposed Echo State Layer

### Weaknesses
 * The method is only evaluated on a single dataset.
* It is challenging to assess its real-world relevance based on the presented experiments. For example, in robotic manipulation tasks, the practical benefits of this approach remain uncertain. The lack of evaluation on more complex datasets, particularly those with higher dimensionality or more intricate temporal dependencies, makes it difficult to ascertain the method's robustness and scalability. The current evaluation does not provide sufficient evidence to claim that the proposed Echo State Layer (ESL) offers a significant advantage over existing methods in more demanding scenarios. The absence of comparative analysis against other sequence modeling techniques, beyond basic reservoir computing, further limits the conclusions that can be drawn about the ESL's performance.

### Questions
* Would it be possible to show the layer's effectiveness on tasks closer to robotics, such as the MIME Dataset?
* Or on datasets with larger input/output dimensions?
* Is there a limit in the dimensionality where one baseline would start to get the upper hand? A simple experiment with the handwriting dataset would be to treat multiple characters together as a single character in a higher-dimensional space. E.g., two characters are then represented as one character with a 4D curve (u1, u2, u3, u4)
* How does the proposed architecture compare to deep learning methods that use Behavioral Cloning or Dagger-like approaches? Is there a way to use ideas from these algorithms to train the ESL?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper develops a recurrent neural network layer that includes a fixed nonlinear dynamical system with tunable dynamical properties for modeling temporal dynamics. And their method outperforms existing approaches including a temporal ensemble of policy predictions and an Echo State Network (ESN) implementation.

### Strengths
This paper is well-written, and has clear figures.

The method is introduced in a reasonable and theatrical way.

The results show that their method performs well practically.

### Weaknesses
N/A (I'm not an expert in this area, but I'd be happy to get input from other reviewers)

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes to use echo state network as layers to fit temporal trajectories in learning from demonstration tasks. The idea includes learning selected parameters of the dynamical system and also a conditional model for contextual input in fitting multi-mode demonstrations. The proposed method is validated in a handwriting dataset and a few metrics on trajectory reproduction precision are reported.

### Strengths
1. The paper is easy to understand.
2. The paper approached the problem from the dynamical system perspective, which is worth more attentions in the LfD domain.

### Weaknesses
1. The paper only reports results on a handwriting dataset with low-dimension states, lacking comparison to modern LfD approaches in more realistic scenarios, such as robotics. The current evaluation is insufficient to demonstrate the method's applicability to complex, high-dimensional control problems, which are common in robotics. Specifically, the 2D handwriting task does not capture the challenges of redundant degrees of freedom, complex contact dynamics, and noisy sensor data present in robotic manipulation tasks.
2. The novelty is unclear. The core technique appears to be completely borrowed from echo state network and the significance of adopting this design in the target context is not sufficiently addressed. The paper does not provide a clear justification for why an echo state network is superior to other recurrent architectures or more established dynamical system models for the specific problem of learning from demonstration. The benefits of the echo state property in this context are not clearly articulated or empirically validated.
3. The paper motivates with addressing compounding errors in deploying behaviour cloned policies. But this is not demonstrated in the methodology or the experiment sections. The current results and presentation are not coherent with the paper theme. The experiments do not explicitly evaluate the method's robustness to compounding errors during long-horizon execution or in the presence of perturbations. The reported results do not provide a clear link between the proposed method and its ability to mitigate error accumulation.

### Questions
1. What makes the proposed layer differ from a recurrent neural network layer? How is this less susceptible to compounding errors as the dynamical system is also time-discretised and explicitly integrated?
2. Will the approach scale up to more complicated motion/policy? How about high-dimension state space beyond 2D? How will it be compared to state-of-the-art methods such as diffusion policy?
3. Even focusing on the handwriting task, can the method be comparable/outperforming classic network approaches like Alex Graves' work?
 4. What is the advantage of the proposed approach considering all existing LfD and handwriting generation models, since none of them are involved in the comparative study?

### Soundness
1

### Presentation
2

### Contribution
2
