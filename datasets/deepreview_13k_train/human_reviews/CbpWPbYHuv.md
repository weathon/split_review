# Polynomial Composition Activations: Unleashing the Dynamics of Large Language Models

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
Transformers have found extensive applications across various domains due to the powerful fitting capabilities. This success can be partially attributed to their inherent nonlinearity. Thus, in addition to the ReLU function employed in the original transformer architecture, researchers have explored alternative modules such as GeLU and SwishGLU to enhance nonlinearity and thereby augment representational capacity. In this paper, we propose a novel category of polynomial composition activations (PolyCom), designed to optimize the dynamics of transformers. Theoretically, we provide a comprehensive mathematical analysis of PolyCom, highlighting its enhanced expressivity and efficacy relative to other activation functions. Notably, we demonstrate that networks incorporating PolyCom achieve the \textbf{\textit{optimal approximation rate}}, indicating that PolyCom networks require minimal parameters to approximate general smooth functions in Sobolev spaces. We conduct empirical experiments on the pre-training configurations of large language models (LLMs), including both dense and sparse architectures. By substituting conventional activation functions with PolyCom, we enable LLMs to capture higher-order interactions within the data, thus improving performance metrics in terms of accuracy and convergence rates.  Extensive experimental results demonstrate the effectiveness of our method, showing substantial improvements over other activation functions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work presents a method to extend activation functions using polynomials.
Two examples of these extended activation functions are introduced: PolyReLU and PolyNorm.
PolyReLU is shown to achieve an optimal approximation rate in Sobolev spaces.
Language modelling experiments indicate that the proposed activation functions accelerate training.

### Strengths
- (clarity) Overall, the paper is clearly written and easy to follow.
 - (originality) The proposed activation functions are novel (to the best of my knowledge).

### Weaknesses
 - (quality) The proof of lemma 2 (and therefore also lemma 2) seems to be incorrect.
   It seems like the rank (and number of polynomials) from lemma 3.4 in (Telgarsky, 2017) have been ignored.
   Furthermore, it is unclear why the minimum has disappeared because even $\ln(1/x)^2 < \ln(1/x)$ does **not** hold for $x \in (0, 1)$.
   Also, there is no argument for why the addition of the ReLU function in the proof does not change the size of the overall network.
 - (quality/significance) The lower bound in theorem 2 does not make sense.
   If the PolyReLU network happens to have PolyReLU parameters $a_1 = 1$ and $\forall i \neq 1 : a_i = 0$,
   it should be possible to model it exactly with a ReLU network of the same size.
   Similarly, I do not see how the upper bound in theorem 2 would make sense.
   It should always be possible to make the network arbitrarily large by adding neurons for which all incoming and outgoing weights are zero.
 - (clarity/quality) The polynomial activation functions seem to introduce additional learnable parameters.
   However, the paper never explicitly states this anywhere.
   Futhermore, there is no discussion on whether/how the number of parameters of the different models was controlled.
   This possibly introduces a capacity advantage for the models with PolyCom functions compared to the baselines,
   leading to an unfair comparison.
 - (clarity/quality) There is no discussion on how the hyper-parameters were found.
   Furthermore, it seems like the same hyper-parameters were used for every model.
   If these hyper-parameters were tuned on the proposed models, this would be an unfair comparison.
 - (quality) The authors claim that the activation functions are able to capture higher-order interactions.
   However, based on the training curves (e.g. figure 3), none of the models were trained to convergence.
   As a result, it is not possible to conclude anything concerning the complexity of the interactions that can be learned.
   After all, it might be that the same interactions are captured for both models when converged, but one captures them "faster".
   As a result, these experiments do not confirm the stated claims.
 - (quality/significance) There is no discussion on the runtime overhead of the introduced functions.
   If the PolyCom functions introduce too much overhead, they might not be practically useful.
   Also, it would be useful to include a comparison performance for a given compute budget.
 - (clarity) It is not clear why the proposed activation functions should be especially suited for language modelling.
   I suspect that this should also work for models that do not require that much compute and allow for more extensive experiments.

###### Minor Comments
 - There seem to be some type-setting issues with equation (7) (Thereom 1).
 - Could it be that there is a superscript $d$ missing for the space of $\boldsymbol{m}$ on line 869-870?

### Questions
1. Does theorem 2 make sense?
2. What is happening in the proof of lemma 2?
3. Do the PolyCom functions introduce additional learnable parameters?
4. Do the different models in the comparison have the same number of parameters?
5. How were the hyperparameters tuned?
6. How do the models compare when trained to convergence?
7. What does the performance look like as a function of training budget?
8. Does this method work also provide benefits when used outside of language modelling?

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
4

### Summary
This paper introduces polynomial composition activations (PolyCom), which is shown to be theoretically more expressive relative to common activation functions like ReLU and has an optimal approximation rate for general smooth functions in Sobolev spaces. Experiments show PolyCom, especially PolyNorm, achieves significantly better performance per token for training 1B parameters dense language models and 7B total parameters MoE model compared to SwiGLU, GeLU, and other ReLU variants.

### Strengths
- PolyReLU and PolyNorm show nontrivial performance gains for training language models with >1B parameters, even compared to strong baselines such as SwiGLU and squared ReLU.
- The experiments are comprehensive, covering both pre-training and downstream evaluations.
- PolyReLU has strong theoretical guarantees, showing it's more expressive than ReLU and has an optimal approximation rate for general smooth functions in Sobolev spaces.
- The paper is well-presented.

### Weaknesses
 - The paper does not discuss potential overhead in using PolyCom. For example, naively, using PolyCom would increase the activation memory by a factor of $r$ (set to 3 in the experiments) compared to ReLU. 
- The analysis section is not completely convincing. Why is a higher effective rank better? Both GeLU and SwiGLU have lower effective ranks than ReLU, but they achieve better performance.
- It's not clear that PolyNorm MoE has lower layer-wise cosine similarity in Figure 7 compared to SwiGLU MoE.
- An important unaddressed question is how the benefit of PolyCom scales to larger models. For example, is it most significant for smaller models and vanishing for larger models? I suspect this is not the case, but showing some evidence would be important.

### Questions
- What is the memory and runtime overhead of switching from, e.g., squared ReLU to PolyCom?
- Can you show how PolyCom affects the scaling laws of loss v.s. model size or training computed by, for example, training additional smaller models?

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
- The authors propose PolyCom, a set of polynomial composition activations that are tailored especially to the needs of transformer models. Theoretical and empirical evaluations compare the expressivity and other capabilities for PolyCom to common pre-existing activations, including traditional ReLU and SwiGLU.
PolyCom applies a composition of a polynomial function and another function $\rho$. Two variants of - PolyCom are focused on. Type 1 PolyCom applies $\rho$ before the polynomial exponent, while Type 2 applies the polynomial exponent before $\rho$ (Equation 1 in the paper). The paper’s evaluations concentrate on one specific substantiation for each type:
  - For Type 1, the authors use PolyReLU. This activation sets $\rho$ to ReLU and applies $\rho$ before the polynomial. 
  - For Type 2, the authors use PolyNorm. This activation has the L2 normalization for $\rho$ and applies the polynomial before $\rho$.
- The theory results focus on PolyReLU and proceed in three steps:
  - In section 3.1, the authors show that the sets of all ReLU and ReLU^2 networks are subsets of the set of all PolyReLU networks, indicating that PolyReLU has stronger approximation abilities than ReLU or ReLU^2
  - The main result of Section 3.2 (Theorem 2) is that the size of any ReLU network that approximates a PolyReLU network with depth L and width K within tolerance $\epsilon$ must be at least $\Omega(KL \ln(\epsilon^{-1}))$. By this, authors conclude that PolyReLU networks are more efficient than ReLU networks in terms of representational capacity.
  - Theoretical results build to Section 3.3, which shows in Theorem 3 that PolyReLU networks achieve the optimal approximation rate: that is, there exists a PolyReLU network of size $O(\epsilon^{-d/n})$ that can approximate arbitrary function $f$ in a unit ball within a Sobolev space $F_{d,n}$.
- Empirical evaluations in section 4 apply PolyCom to one dense model with 1B parameters and one MoE model with 1B active and 7B total parameters. Comparison activations are ReLU, ReLU^2, GELU, and SwiGLU. Training datasets are RedPajama-1T for the dense and OLMoE Mix for the MoE model, and several other datasets are considered for downstream fine-tuning tasks. Authors state that lower training/validation loss and downstream task accuracy for PolyCom activations are indicative that PolyCom accelerates the convergence of LLMs and increases model expressivity, with PolyNorm performing generally better than PolyReLU as well. Ablations include the polynomial order of PolyCom and the choice of polynomial composition function $\rho$, and the rank of model weights and layer-wise similarity are also compared favorably towards PolyNorm.

### Strengths
- The idea of activation functions with better expressivity, without adding more trainable parameters to the model, is significant, useful and interesting
- The construction/definition of PolyCom is very flexible and serves as a good base for future experimentation with other activation variants beyond the specific instantiations of PolyReLU and PolyNorm
- The combination of both theoretical and empirical results is stronger than including just either type of result alone
- Theoretical results are approachable and elegant
- Paper is well-structured and well-written: it’s easy to follow and there were no confusing typos or other writing issues
- Empirical evaluations are conducted on several different downstream datasets, adding strength to the authors’ claims

### Weaknesses
 - No discussion of the differences in computational needs between PolyCom and prior activations: does it slow down training time a lot, or do you need much more memory? On lines 416-417 where you’re comparing different orders of PolyCom, you mention higher orders leading to overhead and overflow; I would want to hear more about that. Specifically, a detailed analysis of the FLOPs introduced by PolyCom, compared to ReLU, GELU, and SwiGLU, would be beneficial. Furthermore, the memory overhead of storing intermediate values during the forward and backward passes should be quantified, especially in the context of large language model training where memory is a critical constraint. The overflow issue with higher-order polynomials, especially when using lower precision formats like BF16, needs a more thorough investigation, including the specific polynomial orders at which overflow becomes problematic and potential mitigation strategies.
- Empirical results do not seem to be averaged across runs; I don’t see it stated anywhere. Results tables and graphs contain no error bars. Especially because the empirical results are fairly small in many areas, such as in Table 1, I would appreciate more evidence that these patterns hold across training seeds/different random initializations at the start of training. The absence of error bars or confidence intervals makes it difficult to assess the statistical significance of the observed differences between PolyCom and other activation functions. Given the stochastic nature of neural network training, it's crucial to demonstrate that the reported improvements are not due to random chance or specific initialization conditions. The lack of averaging across multiple runs also raises concerns about the reproducibility of the results.
- Other types of polynomial activations, such as those cited in Section 5’s paragraph on polynomial activation functions, are not compared against in the empirical results. Seemingly, no explanation is given for leaving these functions out. The choice of PolyReLU and PolyNorm as the primary instantiations of PolyCom is not sufficiently justified, especially given the existence of other polynomial activation functions. A more comprehensive comparison, including a wider range of polynomial activations, would strengthen the empirical analysis and provide a more complete picture of the performance landscape. The specific reasons for excluding other polynomial activations should be clearly articulated.
- Small comment: more discussion of the optimal approximation rate or a formal statement of DeVore et al.’s theorem 4.2 (cited on line 275) inside of your paper (even the appendix) could be nice for readers

### Questions
- Would you mind including more results on the computational requirements required for PolyCom versus other activations, as I mention in the limitations section? It could also be interesting to include an experiment where PolyCom is compared to other activations, and model size/parameter count is somehow adjusted to ensure that models using PolyCom and models using other activations have comparable computational requirements 
- It’s stated that PolyReLU and PolyNorm have equivalent expressivity, e.g. on lines 164-165. Do you have a proof for this?
- Have you tried any PolyCom activation in a non-transformer model? What causes you to think that they’re so good for transformers in particular, as opposed to also for other (deep-learning) architectures?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces PolyCom, a polynomial composition activation for transformers. Through theoritical analysis, PolyCom is shown to enhance expressivity and effectiveness over other activations. Empirical experiments on large language models (LLMs), both dense and sparse, demonstrate that replacing standard activations with PolyCom enables LLMs to capture higher-order data interactions, improving accuracy and convergence rates.

### Strengths
1) The authors demonstrate the expressivity of the proposed activation function both theoretically and empirically, using effective rank analysis and layer-wise similarity metrics. These methods provide insights into how the activation enhances the model’s ability to represent complex patterns and distinctions between layers, showcasing its potential advantages over traditional activation functions.

2) Extensive experiments on downstream tasks, along with improved convergence rates in the learning curves with fixed parameter size model, highlight the potential of the proposed activation function.

3) Overall, the paper is clearly written, with the description of polynomial activation easy to follow, and the results presented concisely.

### Weaknesses
1) Computational complexity analysis is not provided. Can the authors provide some analysis on the inference time throughput of the proposed activations with others?

2) How do the authors address stability or manage potential exploding gradient issues with the polynomial activation?

Typos: Line 274: Dowmstream Evaluation -> Downstream Evaluation

### Questions
Check the weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3
