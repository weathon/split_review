# Let the Rule Speak: Enhancing In-context Learning Debiasing with Interpretability

- Decision: Reject
- Scores: 5, 8, 5, 3

## Abstract
In-context learning, which allows large language models to perform diverse tasks with a few demonstrations, is found to have imbalanced per-class prediction accuracy on multi-class text classification. Although notable output correction methods have been developed to tackle the issue and simultaneously improve downstream prediction accuracy, they may fail to answer the core interpretability challenges: why and which certain classes need corrections, and more importantly, a tailored correction for per-sample, per-class’s probability. To address such interpretability gaps, we first find that the imbalance arises from certain classes consistently receiving high ICL output probabilities, whereas others receiving lower or mixed ranges, so the former is more frequently chosen, resulting in higher accuracy; more crucially, we find that these ranges have significantly varying degrees of influence on the accuracy bias, highlighting the need for precise, interpretable probability corrections by range. Motivated by this, we propose FuRud, a Fuzzy Rule Optimization based Debiasing method, that (1) detects which classes need corrections, and (2) for each correction-needed class, detects its probability ranges and applies asymmetric amplifications or reductions to correct them interpretably. Notably, across seven benchmark datasets, FuRud reduces the pairwise class accuracy bias (COBias) by more than half (56\%), while achieving a relative increase of 21\% in accuracy, outperforming state-of-the-art debiasing methods. Moreover, FuRud can optimize a downstream task in a few-shot manner, with as few as 10 optimization examples. Furthermore, FuRud can work for prompt formats that lead to highly skewed predictions. For example, FuRud greatly improves ICL outputs which use letter options, with 44\% relative accuracy increase and 54\% relative COBias reduction.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a fuzzy-rule based method to debias probabilities of

### Strengths
1. Overall paper is well-written with a novel idea proposed.
2. Experiment results show strong improvements over baselines.

### Weaknesses
1. Authors need to clarify the differences between 'debias' and 'calibration' better and earlier (currently mostly discussed in 5.4.). Many references and comparison methods here are 'calibration' based methods such as Batch Calibration ("Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering.") and "Calibrate Before Use: Im- proving Few-shot Performance of Language Models.". 
2. I think this method is not limited to ICL in LLM only. This is not a weakness of the method per se, as if the method can be used somewhere else means it has greater impacts. Does it really not work/applicable to any other classification probabilities setup? My intuition is that with this debias method, it can probably give improvements in other setting as well. But this is the consequence of introducing more computes. Authors need to justify and perform more analysis why this is a method tailored to ICL in LLM to better motivate the paper. 
3. When comparing with these calibration method, need to list computation cost, calibration errors as reference metrics to justify the comparison.

### Questions
Mostly described in the weakness section

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
The paper proposes FuRud, an interpretable fuzzy rule optimization based debiasing method for LLM in-context learning. FuRud addresses both the inter-class surface bias and also the intra-class range-wise influences.

### Strengths
I am first of all impressed by the quality of work done, and also the extensiveness of the paper's discussions. The method is also straightforward with promising results and qualitative analyses. Overall, the paper was well written and easy to follow, and many interesting experiments were done.

### Weaknesses
- One concern is that the experiments were done on a single model, Llama2-13B. I would like to see if this approach is applicable to other model families and sizes.
- It is well known that the performance of In-Context Learning is largely dependent on how the demonstrative examples are selected. However, I don't think there was any analysis on this, other than on the number of samples used. How were the samples samples selected -- were they selected randomly? Will there be certain example selection strategies that are incompatible with FuRud?

### Questions
See Weaknesses

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a debiasing/output-correction method for in-context learning applications, using fuzzy-rule based corrections. It achieves comparable accuracy and debiasing performance to other state-of-the-art (sota) methods on one LLM (Llama-2-13B).

### Strengths
- The method is original and has not been investigated prior.
- The range of datasets used is strong, and can provide comprehensive insights (though the range of models used is insufficient).
- The paper is relatively clear despite the specifics being hard to comprehend quickly.
- The topic is relevant and timely.

### Weaknesses
1. Only one, relatively small LLM is experimented on (Llama-2-13B). Bias towards a particular class is central to the author's claims (see questions), though this is likely more prevalent in weaker/smaller models, or at least simpler to model/correct for interpretably. The setup is thus fairly simple and it is yet to be seen how biases may present themselves for more sophisticated models, or how it may be fixed. The paper does not explore the potential for more complex, multi-faceted biases that might emerge in larger models, which could render the proposed fuzzy-rule approach less effective or require significant modifications. Furthermore, the paper lacks a discussion on the computational cost of applying this method to larger models, which is a critical consideration for practical applications.
2. I am unsure about the baselines. They lack proper description based on my reading of the paper. It is hard to understand exactly what they propose. The paper does not clearly specify the exact algorithms or implementations used for the baselines, making it difficult to assess the validity of the comparisons. It is unclear if these baselines are standard methods or custom implementations, and how they were tuned for the specific tasks. This lack of detail makes it challenging to reproduce the results and understand the relative advantages of the proposed method.
3. Interpretability is a key motivator but it is not clearly explained why other methods are uninterpretable/why this is a major problem. The paper claims interpretability as a key advantage but does not provide a concrete definition or metric for interpretability. It does not adequately explain why existing debiasing methods are considered uninterpretable, nor does it provide a clear comparison of the interpretability of the proposed fuzzy-rule approach with other methods. The paper also fails to discuss the limitations of the interpretability provided by fuzzy rules, such as the complexity of the rule sets and the potential for them to be difficult to understand in practice.
4. A major drawback was in places a lack of readability. For instance, it took a long time to try to understand that the process is as follows: full few-shot examples + test questions are passed through the LLM --> probabilities are measured across the answers for each test question --> these are aggregated across all test questions in the multi-objective optimization step (?) --> probabilities are calibrated according to rules learnt. I was confused in Figure 1 about what terms like "optimization set" refer to. The paper lacks clarity in explaining the multi-objective optimization process, and the role of the "optimization set" is not well-defined. The description of the algorithmic process is convoluted, making it difficult to grasp the key steps and their interdependencies. The paper should provide a more detailed and step-by-step explanation of the algorithm, including a clear definition of the optimization set and its purpose.

### Questions
1. How does a more interpretable baseline of simple calibrated accuracy [1] compare? I understand the new baselines are reported to outperform this, but it is a useful comparison point, and it is not always clear how much trust can be put on previous results which are conducted on presumably different models/datasets (again, it is not reported in the paper here).
2. Why are fuzzy rules any more interpretable than other basic class correction methods? Please provide comparison/examples.
3. Please clarify my understand of the algorithmic process as outlined above in weaknesses.

[1] Calibrate before use: Improving few-shot performance of language models, Zhao et. al., 2021

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work aims to promote ICL's performance. In particular, the authors focus on the imbalanced prediction issue. To this end, the authors propose a fuzzy rule optimization-based debiasing method. Some experiments are conducted to evaluate the proposed methods.

### Strengths
1. The studied topic is promising, as the imbalanced prediction issue of ICL poses significant challenges to the community. 

2. Introducing fuzzy rules is novel and exciting.

### Weaknesses
1. I fail to locate the definition of "per-class accuracy bias" throughout the paper, which makes the work difficult to follow. Specifically, what is per-class accuracy bias? What is the difference between the standard scenario and the mentioned per-class accuracy bias?

2. I did not figure out how to optimize Eqs. 4-7 since no clear explanation is provided. The authors did not give a clear picture of the proposed method. Consequently, reproducing this work will be challenging.

3. The performance gain is limited, especially when comparing FuRud to DNIP. For instance, DNIP achieves 6.6% performance gain over BC, while FuRud is 6% more accurate than DNIP. Similar cases can be found in the COBias metric.

4. The motivation of the proposed method is confusing. I cannot figure out why the proposed method works and why methods are designed using such an approach. In particular, the authors should clarify why Eqs. 4-7 can address the challenge of class correction. Since there is space for one page to allow authors to add necessary explanations, authors may consider adding detailed clarifications.

### Questions
Which modules in the experiments or the proposed method are related to Eqs 4-7?

What is the explicit connection between the proposed method and the mentioned interpretability?

### Soundness
2

### Presentation
2

### Contribution
2
