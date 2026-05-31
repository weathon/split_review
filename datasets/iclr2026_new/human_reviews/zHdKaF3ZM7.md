## Human Reviewer 1

### Summary
The authors seek to incorporate domain priors and in-context reasoning into linear RNNs.
They show that (i) linear RNNs can act as effective hypernetworks, (ii) these RNNs can engage in in-context learning or physics-informed modeling, and (iii) these hypernetworks exhibit significant improvements over baseline models.
Models are evaluated on forecasting / reconstruction, classification, and in-context linear regression tasks.
Baseline models include gated RNNs, linear SSMs (S4), and transformers.

### Strengths
- Fantastically written, very clear.
- Related work and appendix are thorough.
- Experiments show clear improvements of the proposed WARP RNN over baseline models, both in accuracy and compute.
- Authors are clear about limitations, especially the important limitation that the hidden state transition matrix is dense.

### Weaknesses
- The introduction does not (although the related work does) mention selective SSMs (e.g., Mamba), which have re-introduced nonlinearities into linear RNNs.
- CelebA reconstruction seems a bit contrived as a task: the annotated S4 article referenced does indeed reconstruct MNIST and similar image data, but then proceeds to spoken digit data, which the authors did not try reconstructing.
Moreover, CelebA face reconstructions are substantially corrupted.
While I do not deny WARP's improvement in image reconstruction over baseline, I am unsure about the salience of image reconstruction as a metric for evaluating RNNs.
I think there are more relevant tasks to measure long-range dependencies, such as Long-Range Arena benchmarks.
- There are no experiments on text prediction or classification, which are some of the most relevant tasks for evaluating new RNN architectures - does WARP have limitations or inductive biases that prevent it from expressively processing text?
If so, the authors should state it, as this is an important limitation, especially to claims of in-context learning.
If not, then the authors should evaluate their model with text to support the expressivity of WARP.
- WARP's connections to biology are not sufficiently explained in the main text, although the authors do discuss it further in the appendix.

### Questions
I suggest the following:
- Traditional long-range dependency experiments like Long-Range Arena benchmarks.
- Text prediction and classification experiments to support claims of expressivity.
- Connections to biology, especially in the main text, should be clarified.
- As stated by the authors, future work should explore ways to reduce the density of hidden-state transition matrices used in WARP. 
Complex diagonal recurrences may be fruitful in this regard.

### Soundness
3

### Presentation
4

### Contribution
4

### Rating
8

### Confidence
3

---

## Human Reviewer 2

### Summary
This paper proposes WARP, a novel class of recurrent neural networks (RNNs) that perform sequence modeling directly in weight-space, blending linear recurrence with non-linear decoding. Unlike standard RNNs, which maintain a hidden state that is a result of propagating the sequence through the network, the proposed model’s hidden state is instead equal to the parameter vector of a so called auxiliary (“root”) MLP and is updated over time via a linear recurrence. Each update is driven by consecutive input differences, and the auxiliary MLP provides nonlinear decoding using an input that encodes the canonical ordering of the sequence.  This formulation enables gradient-free adaptation and in-context learning during inference, as well as the injection of physics priors through explicit parameter constraints.
Extensive experiments are conducted across time-series analysis, dynamical system reconstruction, and multivariate time-series classification. WARP shows consistent or superior performance to state-of-the-art baselines on most tasks. A physics-informed variant, WARP-Phys, achieves significant improvements on physical dynamics reconstruction tasks.

### Strengths
1. Novel conceptual framing:  The idea of treating the recurrent hidden state of a linear state-space model as the weights of another neural network is both elegant and novel. It bridges ideas from fast weights, meta-learning, hypernetworks and structured state-space models while maintaining linear recurrence efficiency. Additionally, it offers a built-in support for gradient-free adaptation, in-context learning, and physics-informed modeling in a single architecture.
2. Computational Efficiency: Once the model has learned from the context, the final root network can be extracted and reused to process subsequent queries without reevaluating the entire sequence, yielding significant computational savings compared to other in-context learning models. Furthermore, the proposed architecture leverages a dual training mode that combines linear recurrence with a parallel scan operator – a well-established technique in the State Space Model (SSM) literature – to accelerate state propagation. Together, these design choices lead to notable computational efficiency improvements.
3. Strong empirical results: Competitive or superior performance on time-series analysis, especially Traffic Flow Forecasting (despite ignoring graph priors) and Image completion, as well as dynamical system reconstruction. The inclusion of a physics-informed variant further demonstrates the framework’s adaptability and potential for interpretability.
4. Clarity and completeness:  The paper is well-written, includes high-quality figures, ablations, detailed appendices, and clear pseudocode.

### Weaknesses
1. Scalability constraints:  The main bottleneck is the large transition matrix which scales quadratically with the number of root-network parameters. Experiments are thus limited to moderate model sizes, raising questions about feasibility for large-scale models.
2. Limited theoretical grounding:  While the empirical evidence is compelling, the theoretical analysis of representational capacity and stability (e.g., under linear recurrence updates) still remains to be established. 
3. Computational cost reporting:  Although the recurrence is linear, updating and decoding weight vectors remains costly. Memory and compute scaling with model size are not fully quantified and are only provided in the appendix, but entirely missing from the main body of the paper.
4. Limited setting for dynamical system reconstruction:  While the possibility of making the network physics-informed is compelling, the shown examples illustrate this for relatively simple systems with a small number of parameters. While the proposed method clearly allows for in-context learning, and hence does not need to retrain a network for each new dynamical system (from the same category), the setups are done for what appears to be noiseless input-output data, and a low number of parameters. One could, instead of learning the entire mapping of the system, learn only its phase or exponential mapping for any other sequence model that allows for ICL, in the same way as demonstrated in this work. This alternative formulation would serve as a fairer baseline for comparison.
5. Novelty relative to prior work:  There is conceptual overlap with other concepts briefly outlined in the related work (e.g., fast weight RNNs), though the authors’ framing is distinctive. A more explicit comparison to those baselines would help to better position WARP’s contribution.

### Questions
1. Have you evaluated WARP’s performance on noisy measurement scenarios for dynamical system reconstruction?
2. Could you discuss related sequence modeling approaches in weight space and explain why these were not included as baselines in any of the tasks?
3. For the Energy Prediction experiment: what are the current state-of-the-art results? In general, for all experiments, how were baselines tuned, and how much effort was spent on hyperparameter optimization? Also, performance of S4 is reported only on MNIST, and ConvCNP only on CelebA. Full performance tables in the appendix would improve transparency.
4. Have you considered benchmarking WARP on long-range dependency benchmarks, such as Long Range Arena (LRA)? This could contextualize WARP’s capabilities relative to other established long-sequence models that were evaluated on these tasks.

### Soundness
3

### Presentation
4

### Contribution
3

### Rating
8

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper offers a new weight-space learning technique that iterates weights of a feedforward neural network in a linear state space, enabling in-context learning. The authors evaluate WARP across diverse tasks including image completion, time series forecasting and classification, and dynamical system reconstruction, demonstrating competitive or superior performance compared to standard RNNs, state-space models (S4, Mamba), and Transformers. Notably, a physics-informed variant achieves order-of-magnitude improvements on physical system reconstruction benchmarks.

### Strengths
The core idea of parametrising RNN hidden states as weights of an auxiliary neural network is conceptually interesting and, to the best of my knowledge, novel. The authors test their method on a diverse set of domains and perform a large range of ablations to show the necessity of design choices. The writing is generally accessible, with good intuitive explanations, and goes far to place itself in the larger test-time adaptation literature.

### Weaknesses
Claims are sometimes overstated and/or imprecise. For example, phrases like "transformative paradigm for adaptive machine intelligence" (Abstract, Conclusion) and "redefine sequence modeling" (Abstract) are not well-supported. The empirical results show WARP is competitive but not uniformly superior. "Brain-inspired formulation" (Abstract, page 2) refers only to using input differences, with citation to synaptic plasticity [16], but the connection is somewhat superficial - there is a rich literature concerned with modelling realistic synaptic plasticity rules which this approach to weight-space trajectory modelling does not engage with. "Infinite-dimensional RNN hidden states" (page 9, footnote 6) is misleading—the hidden state is finite-dimensional, though it parametrizes a function.

### Questions
“Rather than relying on direct inputs, we draw inspiration from the human brain and compute signal differences to drive such recurrences.” - from where is the inspiration drawn? Did you try ablating this, i.e. just using x_t as the input to B? Similarily, did you try ablating the random noise applied to observations in AR mode? i.e. p_forcing = 0 (or 1, whatever means noise is never added)

What is the operational difference between gradient-free adaptation and in-context learning? The definitions provided seem to be nested on page 2 (i.e. in-context learning implies gradient-free adaptation).

"This strategic initialisation also imposes a critical constraint wherein the initial hidden state θ_0 must encode semantically rich information applicable to the entire sequence." Could you give some clarity here - how can the weights encode information about a sequence prior to observing it?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 4

### Summary
This paper analyzes recurrent neural networks (RNNs) through a weight-space linear recurrence formulation that unifies several modern architectures — including continuous-time linear RNNs, state-space models (SSMs), and residual recurrent networks — under a single linear operator perspective.

The authors derive closed-form expressions for training dynamics and generalization in the overparameterized limit, showing that convergence properties and implicit regularization can be understood via the spectral structure of the recurrent Jacobian. They provide:

A linearized weight-space recurrence model that approximates nonlinear dynamics by a low-rank operator with analytically tractable behavior.

A demonstration that generalization error scales with spectral conditioning, extending kernel-based intuition from linear networks to recurrent architectures.

Empirical validation on synthetic sequence modeling and dynamical-system reconstruction tasks (mass–spring–damper, Lotka–Volterra, PEMS08 traffic), showing alignment between predicted and observed convergence trends.

Overall, the paper contributes to a principled understanding of how weight-space geometry and recurrence interact to shape training efficiency and generalization.

### Strengths
The paper builds on well-established analyses of linear networks and extends them naturally to recurrent settings using a spectral-decomposition framework (Schur- and SVD-based). Derivations are internally consistent and clearly documented.

The proposed linear recurrence view elegantly bridges RNNs, residual-RNNs, and diagonal SSMs, helping clarify connections between recent model families.

Experiments across several dynamical-system tasks (MSD, LV, traffic flow forecasting) confirm the predicted dependence of training speed and generalization on spectral conditioning and effective recurrence length.

The inclusion of both synthetic physics systems and real-world time-series (PEMS08) demonstrates breadth and internal consistency.

Mathematical exposition is detailed; hyperparameters and architectures are listed (Appendix D.4–D.6). Code release and ablation details are promised.

### Weaknesses
1.  The analytic results rest on linear, Gaussian assumptions; nonlinear recurrence effects and gating dynamics are only discussed qualitatively. As such, predictive power for modern gated RNNs or structured SSMs is limited.

2. The analysis centers on the infinite-width, overparameterized limit; it does not quantify where the asymptotic predictions break down for finite models.

3. The authors reference Saxe et al. (2014) but omit more recent theoretical works on curriculum and transfer in RNNs (e.g., Rajan, Kepple & Engleken) and on gradient-flow analyses in recurrent kernels — literature directly related to their spectral-mode interpretation.

4. Although the experiments match qualitative trends, they serve mainly as demonstrations rather than quantitative tests (e.g., no variance or uncertainty estimates, small sample sizes).

5. Generalization is assessed by mean-squared error only; tasks with stochastic noise or long-term dependency tests (copy, addition, character-level modeling) would strengthen claims about recurrence depth and spectral bias.

### Questions
1. How sensitive are your analytical predictions to non-normal dynamics (upper-triangular Hₕ) versus the diagonal “normal” case you ultimately focus on?

2. Could your framework accommodate nonlinear activation perturbations (e.g., ReLU linearization) to estimate when linear approximation fails?

3. Have you compared your spectral regularization predictions to empirical spectral shrinkage observed during training (e.g., spectrum compression in Wh)?

4. Could you clarify how your results relate to implicit bias analyses in linear transformers or SSMs (e.g., Merrill & Sabharwal; Orvieto et al.)?

5. Are there regimes where the recurrence’s spectral radius predicts too-rapid forgetting or instability, contradicting observed dynamics?

### Soundness
3

### Presentation
4

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 5

### Summary
The paper proposes **WARP**, a framework that performs *linear recurrence in weight space* rather than in hidden-state space. At each step, the parameters of a small decoder network evolve linearly:

$$\omega_t = A \omega_{t-1} + B(x_t - x_{t-1}), \qquad y_t = \text{MLP}_{\omega_t}(\varepsilon)$$

where \(A, B\) are learned transition matrices and $\varepsilon$ encodes position or context.  

Conceptually, this shifts recurrence from feature dynamics to parameter dynamics. It blends (i) the efficiency of linear RNNs/SSMs (e.g., S4, Mamba), (ii) the expressivity of nonlinear decoders, and (iii) in-context or gradient-free adaptation through weight evolution. The model is tested across image completion, time-series forecasting, dynamical-system reconstruction, and classification.

### Strengths
S1. Original framing. The move to perform recurrence directly in parameter space is novel
and quite elegant. It reads as a middle ground between hypernetworks and fast-weight
RNNs, but with the analytical simplicity of a linear transition.

S2. Range of results. The experiments span diverse domains - MNIST/CelebA completion,
ETT and PEMS forecasting, DSR, and UEA time-series classification. The UEA section
is particularly strong: comparisons include modern SSMs like S5, Mamba, S6, NRDE,
and NCDE, with WARP performing competitively across most tasks.

S3. Interpretability and analogy. The weight updates via input differences evoke synaptic-
plasticity rules, which gives the method a neat biological parallel and some explanatory
appeal.

S4. Presentation. The paper is clear, visually well-organized, and balances theory with
intuition. Figures showing progressive reconstruction genuinely help convey how the recurrence behaves.

### Weaknesses
W1. Benchmark depth. While broad, the benchmark is missing some of the newer SSMs
that define the current frontier. In particular, LinOSS (Rusch & Rus, 2024)—an oscilla-
tory, long-sequence SSM—is cited but not compared. Given that LinOSS, FACTS, and
Griffin all outperform S4 and Mamba on long forecasting tasks, excluding them makes
the SoTA claim weaker.

W2. Scalability. The transition matrix $A \in \mathbb{R}^{D_\omega \times D_\omega}$ scales quadratically with the size of the decoder, which will quickly become impractical. No structured or low-rank variants are
explored.

W3. Theory gap. The paper is mostly empirical. There’s no discussion of spectral properties,
stability, or representational capacity of the linear map in weight space.

W4. Domain imbalance. Some domains (especially physics and image experiments) use
small or older baselines (ConvCNP, GRU, Transformer). More recent adaptive or physics-
informed baselines like Neural Context Flows (ICLR 2025) or ZEBRA (2024) would
strengthen those sections.

### Questions
• Include direct comparisons to LinOSS, FACTS, and Griffin.

• Explore structured or low-rank A, B for scale.

• Add runtime and memory tables.

• Include a brief stability/spectral analysis.

• Clarify what fundamentally distinguishes this from hypernetworks and fast-weight RNNs.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
4