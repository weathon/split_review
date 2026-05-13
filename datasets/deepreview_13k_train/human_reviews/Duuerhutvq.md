# Controlled LLM Decoding via Discrete Auto-regressive Biasing

- Decision: Accept
- Scores: 6, 6, 3, 8

## Abstract
Controlled text generation allows for enforcing user-defined constraints on large language model outputs, an increasingly important field as LLMs become more prevalent in everyday life. One common approach uses energy-based decoding, which defines a target distribution through an energy function that combines multiple constraints into a weighted average. However, these methods often struggle to balance fluency with constraint satisfaction, even with extensive tuning of the energy function's coefficients. In this paper, we identify that this suboptimal balance arises from sampling in continuous space rather than the natural discrete space of text tokens. To address this, we propose \emph{Discrete Auto-regressive Biasing}, a controlled decoding algorithm that leverages gradients while operating entirely in the discrete text domain.
Specifically, we introduce a new formulation for controlled text generation by defining a joint distribution over the generated sequence and an auxiliary bias sequence. To efficiently sample from this joint distribution, we propose a Langevin-within-Gibbs sampling algorithm using gradient-based discrete MCMC. Our method significantly improves constraint satisfaction while maintaining comparable or better fluency, all with lower computational costs. We demonstrate the advantages of our controlled decoding method on sentiment control, language detoxification, and keyword-guided generation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces DAB (Discrete Auto-regressive Biasing), an algorithm for controlled text generation with large language models (LLMs).  Previous methods often use energy-based decoding in continuous space, which struggles to balance fluency and constraint satisfaction. DAB addresses this by operating entirely in the discrete space of text tokens.

DAB samples from the joint distribution of generated sequence Y and an auxiliary bias sequence B and alternate between biased auto-regressive generation and discrete gradient-based sampling. Specifically, given a generated text Y, the gradient-based discrete sampling is used to maximise constraint satisfaction. Then B is fixed, and biased auto-regressive generation is used to sample Y. A penalization is applied based on sampled tokens' distance from B in embedding space.

Experiments show DAB outperforms baselines such as BOLT and LM-Steer on sentiment-controlled generation, language detoxification, and keyword-guided generation.

### Strengths
* The paper identifies previous work's deficiency in balancing fluency and constraint satisfaction and proposed a method that maximises both (according to several benchmark numbers).

* DAB seems to be more stable and robust than other continuous methods.

### Weaknesses
Nothing major as I can see.

### Questions
N/A

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes an approach to controlled text generation --- DAB (Discrete Auto-regressive Biasing) --- that exploits the DLP (Discrete Langevin Proposal) technique from (Zhang et al. 2022) for efficiently sampling inside a discrete space while still being able to exploit gradients of an energy function over this space. The DLP technique is not used directly over the output sequence, but over an auxiliary "bias sequence" that is coordinated with the output sequence through a Gibbs-Sampling-like alternation. The experiments show competitive results with a few baselines in terms of efficiency as well as balance between constraints and fluency of the obtained results.

### Strengths
The main strength of the paper lies in its innovative application of the DLB technique to the general problem of controlled text generation (Zhang et al. did touch on text generation but only in a very limited way).

The paper is also creative in the way it uses an auxiliary bias sequence to steer the generation of the actual output sequence.

The experiments demonstrate certain advantages in terms of control (i.e. constraint satisfaction) and fluency over a number of baselines, in particular some based on gradient techniques over continuous relaxations of EBMs over discrete spaces.

### Weaknesses
The main weaknesses of the paper lie on two dimensions: (A) omission of significant related work, (B) lack of discussion/clarity about certain key aspects and modelling decisions in the paper.

(A) The Related Work section 2.1 devoted to Language Models as EBMs, totally ignores a substantial line of work specifically devoted to *discrete* sampling from EBMs, either (i) with focus on training autoregressive approximations to these EBMs (exemplified by [1] and a number of more recent publications at ML conferences (see references in [3])), or (ii) with focus on decoding-time techniques [2]. This line of work, like the present paper, is concerned with discrete (as opposed to continuous) sampling, and is not limited to encoder-based architectures.

[1] Khalifa et al. A distributional approach to controlled text generation. ICLR 2021.

[2] Eikema et al. An approximate sampler for energy-based models with divergence diagnostics. TMLR 2022.

[3] Kruszewski et al. disco: a toolkit for Distributional Control of Generative Models. ACL 2023.


(B.1) Concerning the core Equation (5). First, in the expression $P^{LM}(Y|X,B)$, what you seem to mean is that you concatenate the input $X$ with the bias sequence $B$ and then apply the LM on this new input, but it would be worth discussing this assumption. Second, and more importantly, while it is not clear at this point in the paper, it seems that in Algorithm 1 you actually need to compute $f(Y)$, and not only $f(B)$. Then a pretty obvious question for the reader is, why not simply define $P(Y|X) \propto P^{LM}(Y|X) \exp(f(Y))$ ? That would be much more direct than what the paper does, would directly define $P(Y|X)$ as an EBM, and then presumably the DLB technique could be directly applied to this EBM. It is not clear to me why the authors do not consider and discuss this possibility. 
(Of course, several other techniques for sampling from this EBM would be possible, including those mentioned in (A) and techniques related to RLHF/PPO where $f(Y)$ might be seen as a reward.)

(B.2) There are several other points in the paper that are kept implicit and would need more discussion. To give a few examples: 
- The fact that the length $n$ of the response $Y$ needs to be specified in advance, which appears to be a limitation of the approach, is kept implicit.
- The important DLB-based equation (7) should be described in a more self-contained way (perhaps using the Appendix), in particular the way the gradient is actually computed.
- The fact that step 6 in Algorithm 1 is actually deterministic should be mentioned, as this detracts from standard Gibbs-sampling practice.

### Questions
Questions/suggestions (in addition to those implicit in the previous section):

- Lines 238-243 seem problematic, as they introduce a notation $P(Y|B)$ that is not conditioned by $X$. Are they correct and/or needed later?

- In Lines 494-496, you mention that a good metrics for the keyword-guided generation should consider the meaning similarity of the produced sentence to the constraining keywords, not the actual presence of the keywords. I was not fully convinced by this remark, and was wondering whether considering the actual presence of the keywords should be seen as a more important metrics. More generally, I wondered whether it would be worth reporting, among the metrics, the value $f(Y)$ itself as this seems to be the main driver of the approach.

### Soundness
2

### Presentation
2

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
This paper proposes a new controlled text generation approach called DAB. DAB happens at decoding time, and it consists of two alternating steps: updating the bias term based on the gradient, and updating the response sequence conditioned on the bias term. This approach is designed to address the trade-off between fluency and control satisfaction. They experiment on sentiment, toxicity, and lexical control benchmarks.

### Strengths
- good summary of prior work, it nicely summarizes the field of controllable text generation from AR to NAR, with or without gradient guidance, etc. 
- the method makes intuitive sense, but the details of the methods seem very unclear.

### Weaknesses
 - Controllable text generation is important, but the benchmarks this paper tested have been mostly saturated by prior approaches, so further testing on these benchmarks can no longer demonstrate the goodness of the newly proposed approach. Furthermore, prompting could solve these problems, so can this approach solve even harder problems, like model jailbreaking via such MCMC type of approach? 

- I think the math is not very solid in the paper. equation 6 seems wrong. It's a circular definition. The equation (not numbered) immediately after 6 is also strange, should it be P(B | Y, X)? There are also unclear notations in the method section. 

- The method section is very badly written. I don't understand many technical details in the method section. Why eqn 7 has the (1-bij) term? Why is eqn 10 argmax for a sampling distribution? If B is the bias term, intuitively initializing B at 0 seems more reasonable than initializing B at Y?

### Questions
see the weakness section.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents an algorithm for constrained autoregressive decoding where the constraint is defined by a distribution function. This is a common approach using energy-based models.

Even though BOLT does propose similar algorithm, the main difference in this paper is that instead of sampling the bias in the continuous domain, the bias token sampling in this paper happens in discrete space. Author claim, and substantiate with experiments, that this produces sequences that not only follow the constraint better, but also the LLM policy model leading to more fluent outputs.

### Strengths
The authors propose DAB - Discrete Autoregressive Biasing, a modification of BOLT where both output sequence Y and the biasing B are always sampled in discrete space. This allows the model to always remain in the discrete space leading to not just lower computational cost compared to other energy based decoding methods, but also improve the generation with respect to fluency and constrain.

As part of DAB:
1. A joint distribution over the output Y and Bias tokens B is proposed.
2. Similar to Gibbs sampling, the proposed sampling algorithm (Langevin within Gibbs) alternates between sampling better Y and B while at the same time using Langevin for prediction the distribution to sample the tokens from.
3. Uses MCMC to sample the bias tokens, and then add bias from those while sampling the response token.

Albations are performed on both hard and soft constrains to show the effectiveness of the model.

### Weaknesses
 - Even though the method is fast compared to other energy based models, the method is still slow because of the autoregresive sampling happening inside the step for loop as shows in Algorithm 1, line 3-7.
- Results on Sentiment are mixed with decreased Fluency compared to BOLT.

### Questions
In equation 8, the bias value b_{i,j} corresponding to any bias token b_{i} is calculated as the L2 distance between their corresponding embeddings. LLM loss functions use inner product between the embeddings as the distance metric while calculating logits. Any reason to use L2, and were other options tried?

### Soundness
4

### Presentation
4

### Contribution
4
