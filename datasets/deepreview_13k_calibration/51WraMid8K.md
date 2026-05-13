# A Probabilistic Perspective on Unlearning and Alignment for Large Language Models

- Decision: Accept
- Avg Score: 8.00
- Scores: 10, 6, 10, 6

## Abstract
Comprehensive evaluation of Large Language Models (LLMs) is an open research problem. Existing evaluations rely on deterministic point estimates generated via greedy decoding. However, we find that deterministic evaluations fail to capture the whole output distribution of a model, yielding inaccurate estimations of model capabilities. This is particularly problematic in critical contexts such as unlearning and alignment, where precise model evaluations are crucial. To remedy this, we introduce the first formal probabilistic evaluation framework in LLMs. Namely, we derive novel metrics with high-probability guarantees concerning the output distribution of a model. Our metrics are application-independent and allow practitioners to make more reliable estimates about model capabilities before deployment. Through a case study focused on unlearning, we reveal that deterministic evaluations falsely indicate successful unlearning, whereas our probabilistic evaluations demonstrate that most if not all of the supposedly unlearned information remains accessible in these models. Additionally, we propose a novel unlearning loss based on entropy optimization and adaptive temperature scaling, which significantly improves unlearning in probabilistic settings on recent benchmarks. Our proposed shift from point estimates to probabilistic evaluations of output distributions represents an important step toward comprehensive evaluations of LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
3

### Summary
In this paper authors address the problem of reliable unlearning in LLMs. First they introduce a problem, that evaluations based on deterministic point estimates (sampled texts) fail to reliably catch the risks exposed in probablistic outputs. For the case of unlearning, authors state that existing methods rely on a single generated sequence to identify if the information leakage is present or not. Which might not be enough when assessed model might still eventually produce a text with leaked information (with some probability). Therefore authors propose a set of 4 metrics aiming accurately quantify information leakage in model output distribution. Then, authors propose a novel unlearning training objective, which aims to simultaneously minimize model's output distribution entropy on a set of "forget samples" while retaining diversity on "retain samples". The loss itself is a set of additional terms which can be applied to some existing unlearning objectives. Finally, authors conduct comprehensive evaluation of unlearning with different methods using the proposed metrics.

### Strengths
1) Authors provide 4 carefully defined metrics, along with necessary guarantee proofs. Overall, the paper is very well composed.
2) Those 4 proposed metrics allow to comprehensively evaluate model unlearning using entire output distribution (potentially, right now it is limited to MC sampling on certain examples). This appears to be a novel contribution and addresses the lack of probablistic evaluation in the field of unlearning.
3) This approach can be potentially extended to other tasks which require reliable evaluations.
4) The proposed entropy optimization objective is clearly defined and is formuated as additive terms which can be applied to existing unlearning losses, which makes it easy to implement. Addressing diversity on retain samples allows to ensure that models remains useful after unlearning.

### Weaknesses
1) While paper title reads as "A Probabilistic Perspective on Unlearning and **Alignment** for Large Language Models", authors effectively **do not touch** the alignment in their work, leaving it for further research. Indeed, alignment is only mentioned in Introduction, Limitations and Conclusion. This paper would benefit from having at least small discussion on how the proposed metrics can be extended to other evaluation tasks.

2) The term $\alpha$, which is used extensively in formulation of metrics and overall thorough the paper, is only loosely defined in appendix. While it may be the usual practice in math-heavy papers, it does substantially confuse readers who are not so proficient. It is quite pity to read a definition or proof and find terms that simply not defined anywhere above. Consider defining $\alpha$ in the main text of the paper.

3) How increased $\lambda_r$ impacts metrics other than diversity? Specifically, it is unclear if increasing the regularization strength might negatively impact the model's ability to unlearn, or if it introduces any bias in the output distribution even for the retain samples. The paper lacks a thorough analysis of this trade-off.

4) How does proposed EO objective impacts training efficiency (in terms of increased latency or increased VRAM requirements)? Does it limit it's applicability? The paper does not provide any information on the computational overhead of the proposed entropy optimization objective, which is a critical factor for practical applications, especially when dealing with large language models.

### Questions
1) The term $\alpha$, which is used extensively in formulation of metrics and overall thorough the paper, is only loosely defined in appendix. While it may be the usual practice in math-heavy papers, it does substantially confuse readers who are not so proficient. It is quite pity to read a definition or proof and find terms that simply not defined anywhere above. Consider defining $\alpha$ in the main text of the paper.
2) How increased $\lambda_r$ impacts metrics other than diversity?
3) How does proposed EO objective impacts training efficiency (in terms of increased latency or increased VRAM requirements)? Does it limit it's applicability?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed a set of metrics that bounds the risk of unlearning by estimating the bounds of probability of leaks, and the deviation of such random variables. Instead of computing the metric over deterministic point estimates drawn from greedy decoding of LLMs, it proposes the use of Monte Carlo methods, and then estimates these bounds by computation over the empirical distribution. Additionally, the authors proposed some mitigation methods to reduce the risk of leakage when fine-tuning a LLM, and show through experiments that such measures offer potential for reducing the risk and undesired biases in model outputs.

### Strengths
- The paper proposes metrics that is defined on the output distribution rather than the point estimate. I think this is a remarkable step and should be considered by various other scenarios.
 - The exposition on the estimation of probability of leakage and bounds of standard deviation are intuitive and sound. 
 - The set of experiments presented are convincing.

### Weaknesses
 - Notations can be improved in the exposition. For example, $M_1, \cdots, M_4$ actually stands for estimates of different variables, rather than 4 different ways of estimating the same variable. See questions below for more suggestions. 
 - Some derivation are not self-contained (e.g. in Metric 2, the $\epsilon = \sqrt{\frac{\log (1/\alpha)}{2n}}$ is not self-contained and is derived from prior work. 
 - Expositions tend to be a bit too formal, and lacking some intuitions and insights. See below.

### Questions
- L118: $V^\infty$: I believe that the more accepted notation for sequences of arbitrary sequences is $V^*$, where $*$ is the Kleene star. 
 - L150: "extend" -> "extent".
 - L177: "Binary case": This exposition feels a bit verbose. My understanding is that you are empirically fitting a Beta distribution based on whether data is leaked through your Monte-Carlo experiments, and outputting a quantile based on a desired safety level $\alpha$. Please correct me if my understanding is not correct.
 - L197: Make this part more self-contained: especially, what is the Dvoretzky-Kiefer-Wolfowitz inequality and how does it apply here?
 - L211: Proposition 3: This lower and upper bound is reminiscent of the Darboux integrals of $F_n$. If possible, please elaborate on the relationship of this bound estimate to an underlying integral expression. Additionally, it'd be good to reiterate that $F_n$ is the empirical  CDF.
 - L225: What does $\eta_i$ bound? Please discuss.
 - L230: $M_4$: I think it'd be better to call this something like $M_\sigma$, to be clear that this is not an estimate of the probability.
 - L246: $\bar X + 2\bar \sigma$: why 2? I believe this is a choice based on the safety level, but it would be better to define this as a hyperparameter whose selection is based on the accepted risk level.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
2

### Summary
This paper introduces a probabilistic perspective on LLM evaluation which shifts from single point estimates towards evaluating entire output distributions offers significant potential for the field of unlearning and proposes a novel framework to directly assess the output distribution of a model. Besides, an unlearning loss based on entropy optimization and adaptive temperature scaling is also proposed.

### Strengths
1. **Novel Perspective on LLMs Unlearning Evaluation** Existing deterministic metrics are apparently insufficient for LLM unlearning evaluation, and this paper introduces a probabilistic perspective to mitigate this issue.

2. **Adequate Mathematical Derivation** In this paper, the authors demonstrate the rationality of their method theoretically and empirically.

### Weaknesses
1. **More Discussion on LLM Alignment Evaluation** Since the titile contains "ALIGNMENT", more discussion on this topic should be included in this paper.

### Questions
See weaknesses.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work introduces a probablistic perspective for LLM unlearning evaluation. Instead of relying on deterministic greedy decoding in existing evaluation methods, this work takes a probablistic framework and derive metrics considering the high-probable output distributions. The proposed metric demonstrates the limitations of previous methods for their lack of identifying false unlearning. Moreover, a novel loss based on entropy optimization and adaptive temperature scaling are introduced to improve model unlearning.

### Strengths
- Designing good evaluation metrics is important for a reserach direction such as unlearning, and this work indicates a limitation of existing metric and correspondingly proposes improved metrics.
- The proposed metrics and methods are shown to be effective for two recent unlearning benchmarks.

### Weaknesses
 - There is a lack of algorithmic description on how the proposed metrics are calculated, without which readers who lack certain statistical machine learning knowledge or who want to implement the metrics would find it difficult to understand and apply the proposed metrics.
- The proposed metrics are only tested for the unlearning case, which surely is indeed a well-suited scenario. Nevertheless, it would nice if it can be extended to more use cases, such factuality, to verify the effectiveness of the metrics.
- For entropy optimization, I'm not sure about the intuition to minimize the entropy on Dfg. Wouldn't this lead the model to be confident on a different answer, which I think might be a strange thing to enforce.
- It would be interesting to how unlearning (as well as the proposed optimization methods) affects the model's general ability.

### Questions
- For entropy optimization, I'm not sure about the intuition to minimize the entropy on Dfg. Wouldn't this lead the model to be confident on a different answer, which I think might be a strange thing to enforce.
- It would be interesting to how unlearning (as well as the proposed optimization methods) affects the model's general ability.

### Soundness
3

### Presentation
2

### Contribution
3
