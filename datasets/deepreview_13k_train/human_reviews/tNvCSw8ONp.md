# Mitigating Selection Bias with Node Pruning and Auxiliary Options

- Decision: Reject
- Scores: 5, 5, 3, 6

## Abstract
Large language models~(LLMs) often show unwarranted preference for certain choice options when responding to multiple-choice questions, posing significant reliability concerns in LLM-automated systems.
To mitigate this selection bias problem, previous solutions utilized debiasing methods to adjust the model's input and/or output.
Our work, in contrast, investigates the model's internal representation of the selection bias.
Specifically, we introduce a novel debiasing approach, Bias Node Pruning~(BNP), which eliminates the linear layer parameters that contribute to the bias.
Furthermore, we present Auxiliary Option Injection~(AOI), a simple yet effective input modification technique for debiasing, which is compatible even with black-box LLMs. 
To provide a more systematic evaluation of selection bias, we review existing metrics and introduce Choice Kullback-Leibler Divergence~(CKLD), which addresses the insensitivity of the commonly used metrics to imbalance in choice labels. Experiments show that our methods are robust and adaptable across various datasets when applied to three LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors find that large language models exhibit a selection bias in question answering (QA) tasks, where the choice of options influences their outputs. To address this, they propose two orthogonal methods: one that removes linear layer parameters responsible for this behavior, and another that adds an "I don't know" option for the model to choose from. Experiments using three different model architectures across three QA datasets demonstrate improvement over baselines.

### Strengths
- The paper is well-written, and the methods are straightforward.
- The authors conduct experiments with different model architectures

### Weaknesses
 - Pruning model weights can influence model behavior in unforeseen ways, especially since large language models (LLMs) are intended to be general-purpose. 
- The BNP method appears unstable and offers only marginal performance improvements.
- Simply adding the "I don't know" option provides the best overall results; this is expected, given similar behavior observed in older models with the SQuAD v1 and SQuAD v2 datasets.
- The paper uses a limited number of datasets to demonstrate the method's effectiveness.
- The method addresses only one form of bias; the model may still use or learn to rely on other biases for predictions. See, for example, Mikula et al. (2024).

### Questions
- What is the impact of subset size on performance? Does a larger or smaller subset size affect the effectiveness of the proposed method?

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
3

### Summary
This work investigates the selection bias of LLMs for multiple-choice questions. They identify two sources of selection bias: (1) LLMs tend to be more biased when they make incorrect predictions; (2) Upon examining the parameter space, the selection bias mainly arises from the last decoder layer. Based on these two observations, they proposed (1) BNP to debias LLMs by zeroing out the rows of final embedding projection that signifies the pre-computed bias vector; and (2) Adding an auxiliary option. The experimental result shows that the proposed techniques are effective across three MCQ datasets.

### Strengths
* This paper is well written.
* The selection bias problem of LLMs is well-motivated.
* The proposed techniques could effectively mitigate the selection bias on MCQs on the considered models and tasks.

### Weaknesses
 * To me, Section 2 is lacking some details and needs more discussions and clarification. For example, what is the specific setting used to produce Figure 2? Is it evaluated based on zero-shot or in-context learning (or does this matter in terms of selection bias)? Are there any scaling trends since some works suggest that smaller LMs struggled to answer MCQs with the correct format under zero-shot, which might have different behavior on selection bias? Are the open-weight LMs and black-box LMs evaluated using the same criterion? (based on the probability of choice token or based on the similarity between choice option and response?) If not, does the evaluation criterion matter? I think the current evaluation is too brief to draw a holistic conclusion.

* The scope of the proposed BNP method is limited to open-weight models with choice token-based evaluation. This could possibly be addressed by demonstrating its effectiveness on the black-box settings with open-weight models, i.e., similarity-based evaluation.

* The motivation and rationale for introducing an auxiliary option to mitigate the selection bias when the model is incorrect is unclear and should be explained more than currently provided. It would also be helpful to demonstrate how the auxiliary option affects the distribution of the choices, especially for the incorrect questions.

* In Appendix A.2, line 763 -- 768, it is unclear what z['A'] + z['_A'] (especially '_A') means.

* Regarding the proposed CKLD metric, it is unclear to me why an LM needs to be able to match $p_i$, the ground truth label ratio of each specific downstream dataset, which appears to be totally agnostic to the LM. Should a uniform prior makes more sense in this case?

* Some details about how you evaluate the MCQ benchmarks are unclear. For example, are you using a fixed, specific permutation? Is it possible to draw any form of statistical significance regarding the improvements, such as using different permutations?

### Questions
* Have you tested the proposed method on the same model families at larger scales? Will the benefits still be the same?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a new method to remove selection bias and introduces a new metric to quantify it. Unfortunately, the paper has fundamental methodological problems and incorrect claims. See weaknesses for more details.

### Strengths
With their framework, they could improve the performance of LLMs on multiple choice QA

### Weaknesses
 - The primary problem of the paper is the experiment claiming that selection bias stems from the final decoder layer. The authors analyze the embedding differences between correct and incorrect questions within the permutation and observe a significant norm difference only in the last layer. They look at the embedding differences at each position but only report the last 50 token positions. Firstly, there cannot be any difference in the embeddings at earlier positions because LLaMA3 is a decoder-only model, meaning that the embeddings of previous tokens are not affected by future tokens. If the only difference is the order of the options, then no difference should be observed until the options are reached. It is unlikely that four options cover 50 tokens, which raises the need for an explanation from the authors regarding why a difference is still observed in early tokens in Figure 3b. Secondly, observing different embeddings at the last layer is expected because it essentially predicts the next token. How does this show bias? If the order of options is changed, and the next token after option c is analyzed, it is very likely to differ. Since the next token is different, the last layer’s embedding should differ as well. For example, the next token after the sequence “What is the capital city of France? a) Los Angeles, b) Paris, c)” and “What is the capital city of France? a) Paris, b) New York, c)” will likely differ after option c, and this difference should appear in the last layer. The authors must clarify the connection between their experimental setup and bias. The claim that “selection bias stems from the last decoder layer” is unsupported and likely untrue. It is similar to saying, “All predictions of the model stem from the decoder layer.”The last layer obviously has to be in the circuit causing this bias but this is a trivial conclusion. No experiments are needed to establish this.

- The second major issue with the paper is its proposed metrics and criticism of previously suggested metrics, namely Rstd and RSD. The authors appear confused about the definition of selection bias. They use the definition “discrepancy between the model’s response to the original choice ordering and the expected model response over all choice orderings.” However, where is the “dataset” in this definition? This definition applies to a predictive model, and a robust metric should provide similar scores across different datasets, as seen with Rstd and RSD. These two metrics are resilient to different ground truth distributions, as expected. However, the authors likely made an error in their code because while RSD appears consistent under different ground truth distributions, Rstd varies. With the proposed predictive model, recall values can be analytically calculated without needing a simulation. For option \(i\), this is equal to \(0.5 + 0.5 \times (\text{predictor's probability of sampling option } i)\). Additionally, the authors are confused about selection bias and the predictor’s performance in this experiment. For example, if a classifier randomly outputs one of the options with a 0.25 probability, according to their definition, this model would have no selection bias, even though its performance is poor. However, under the authors’ proposed Kullback-Leibler Divergence metric, the model would not receive a good selection bias score because it deviates significantly from the dataset’s ground truth distribution. Finally, the authors state that RSD gives the lowest score when the selection rate for “A” is 0.25, as if this is problematic. In reality, this is expected (Rstd would yield the same result if calculated correctly). If the model outputs uniformly at random for questions it cannot answer, it does not exhibit bias against any choice. This can be confirmed using the authors’ own definition: “discrepancy between the model response to the original choice ordering and the expected model response over all choice orderings.” This discrepancy would be 0 for such a model.

### Questions
see weaknesses.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses selection bias in large language models (LLMs) used in multiple-choice question answering (MCQ) tasks. It introduces two methods: Bias Node Pruning (BNP), which reduces bias by pruning specific parameters in the final layer of the model, and Auxiliary Option Injection (AOI), which includes an “I don’t know” (IDK) option to the choices provided. Additionally, the paper proposes Choice Kullback-Leibler Divergence (CKLD) as a new metric for measuring selection bias, aiming to improve accuracy and adaptability over existing metrics. Experimental results demonstrate the effectiveness of BNP and AOI across various datasets and LLMs.

### Strengths
* The paper’s parameter-level debiasing through BNP and simple input modification with AOI offer new perspectives on reducing selection bias beyond typical input/output adjustments.
* The CKLD metric is well-motivated provides good insights by accounting for class imbalance, which is important for accurate and robust evaluation.
* The extensive empirical studies justify most of the paper's claims. Also, the experiments span multiple datasets and models, demonstrating the applicability of the methods across different settings.

### Weaknesses
 **1. Motivation 1 in Section 2.2.**

The claim that “Selection bias is amplified when the model is incorrect” does seem to misrepresent selection bias by framing it as a consequence of incorrectness rather than a pre-existing condition that affects the model’s choices. Selection bias in model predictions typically arises from the model’s predisposition toward certain options regardless of their correctness. Thus, it is more reasonable to view selection bias as a factor that can influence or even lead to incorrect responses, rather than something that is “amplified” by incorrect answers.

**2. Weak Justification for AOI.**

In Section 3.2, the hypothesis that an “I don’t know” (IDK) option would reduce selection bias due to its presence in incorrect answers is not straightforwardly justified. The logic does seem somewhat circular: if bias is inherent and present regardless of correctness, introducing an IDK option may not directly address or reduce selection bias without a clearer rationale for how it interacts with the bias mechanism. The approach could use a more robust theoretical basis to explain why AOI would specifically reduce the preference for biased options. An alternative explanation or additional empirical evidence supporting this choice would strengthen the section’s argument.

### Questions
1. The motivation for AOI could be strengthened by exploring additional theoretical or empirical justifications. For instance, could the authors test alternative auxiliary options, or provide analysis to show that the IDK option specifically reduces bias compared to other options?
2. BNP selectively prunes nodes, but the potential impact of this pruning on model accuracy across other types of tasks is not fully addressed. How stable is the pruning process across different datasets? Including a sensitivity analysis on how much accuracy is affected by varying pruning parameters could help further clarify BNP’s general applicability.
3. Since the model’s selection bias is observed to be prominent in the final layer, could additional experiments clarify why this layer is particularly sensitive to bias? This might provide insights that could further refine the BNP approach.

### Soundness
3

### Presentation
3

### Contribution
3
