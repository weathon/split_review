# Better Instruction-Following Through Minimum Bayes Risk

- Decision: Accept
- Scores: 8, 6, 8

## Abstract
General-purpose LLM judges capable of human-level evaluation provide not only a scalable and accurate way of evaluating instruction-following LLMs but also new avenues for supervising and improving their performance. One promising way of leveraging LLM judges for supervision is through \textit{Minimum Bayes Risk} (MBR) decoding, which uses a reference-based evaluator to select a high-quality output from amongst a set of candidate outputs. In the first part of this work, we explore using MBR decoding as a method for improving the test-time performance of instruction-following LLMs. We find that MBR decoding with reference-based LLM judges substantially improves over greedy decoding, best-of-N decoding with reference-free judges and MBR decoding with lexical and embedding-based metrics on AlpacaEval and MT-Bench. These gains are consistent across LLMs with up to 70B parameters, demonstrating that smaller LLM judges can be used to supervise much larger LLMs. Then, seeking to retain the improvements from MBR decoding while mitigating additional test-time costs, we explore iterative self-training on MBR-decoded outputs. We find that self-training using Direct Preference Optimisation leads to significant performance gains, such that the self-trained models with greedy decoding generally match and sometimes exceed the performance of their base models with MBR decoding.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes an approach for selecting one of N generation hypotheses using a Minimum Bayes Risk (MBR) method. MBR decoding alone results in improved performance. However, as MBR decoding is resource-intensive and may not be practical for real-life applications, an alternative use case—self-training with DPO on preference pairs selected via MBR—also demonstrates performance gains.

### Strengths
* The paper explores the use of previously developed approaches—specifically, Minimum Bayes Risk (MBR)—for selecting a generation hypothesis at the decoding stage in LLMs. The MBR-selected hypothesis is treated as the one with the highest average utility according to a specified utility metric. The choice of this approach is well-reasoned, with a clear motivation behind it.

* The experimental setup is solid. The paper first demonstrates improvements using MBR decoding. Given its high computational cost, the paper then explores self-training with MBR-decoded outputs, which also leads to improvements. The evaluation is conducted on two standard benchmarks (Alpaca-Eval 2.0 and MT Bench), with comparisons across different decoding approaches and a variety of utility metrics used in MBR. The discussion of results is well-organized, providing clear and comprehensive takeaways.

### Weaknesses
The paper is well-written and easy to follow. The reviewer does not identify any major weaknesses.

### Questions
Are there any distinctive linguistic features in MBR-decoded outputs? How does it affect diversity, style, or tone?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a novel approach to improving the test-time performance of instruction-following LLMs through the application of Minimum Bayes Risk (MBR) decoding. The authors leverage LLM judges as reference-based evaluators to select high-quality outputs from a set of candidate outputs. They demonstrate that MBR decoding with LLM judges significantly outperforms greedy decoding and other decoding methods without references on benchmarks like AlpacaEval and MT-Bench. Furthermore, the paper explores iterative self-training on MBR-decoded outputs to retain performance improvements while mitigating additional test-time costs. The authors find that self-training using Direct Preference Optimisation leads to significant performance gains, matching or exceeding the performance of base models with MBR decoding.

### Strengths
1. The application of MBR decoding with LLM judges is a creative approach that combines recent advances in LLM evaluation with decoding techniques.
2. The experiments are thorough, and the benchmarks used are relevant and well-established in the field.
3.  This paper also explores the guiding role of MBR decoding in LLM’s DPO training, which is inspiring in subsequent model training.

### Weaknesses
Main weakness:
- The presentation lacks clarity and reads more like an experimental report than an academic paper. The methods section is merged with the experiments and results, lacking any formal formulations. For instance, in Section 4.1.2, Iterative DPO on MBR-Decoded Outputs, adding mathematical formulations would improve both understanding and reproducibility of the approach.

Others:
- This paper only compares some relatively simple decoding methods. If some better decoding methods such as speculative decoding and medusa can be added, the method will be more credible.
- The paper could also benefit from a discussion on the computational costs associated with MBR decoding and self-training, especially when scaling to larger models or datasets.

### Questions
- **Question 1:** How does the performance of MBR decoding with LLM judges compare to other state-of-the-art decoding methods beyond those presented in the paper?
- **Question 2:** Can the authors elaborate on any potential negative impacts of using LLM judges, such as the risk of overfitting to the judge's biases?
- **Question 3:** The hyperparameter N~cond~ is set to 12 for generating candidates for DPO but increased to 30 during decoding. How did the authors determine these values, and how do they align with the experiment illustrated in Figure 2?

### Soundness
3

### Presentation
1

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
This paper explores MBR decoding with reference-based LLM judges for selecting one of n outputs for instruction finetuned LLMs at inference time. 
The paper uses Prometheus2, LLama3, and JudgeLM models as a judge for Llama 2 & 3 models and evaluates on AlpacaEval and MT-Bench, comparing MBR decoding with best-of-n inference, and other one-best decoding strategies, and explore non-LLM utility functions for MBR as well.
They find gains across the bench, with smaller judges also being successful as utility function in MBR decoding for guiding larger LLMs. MBR decoding is furthermore combined with self-training (DPO) to yield further gains and overcome the added decoding costs.

### Strengths
1. The experiments are thorough (and well documented), including multiple sizes of learner and judge models, and multiple utility functions for comparison.
2. The analyses are interesting and well presented, explained and visualized. Important ablations, such as hypotheses size and temperature, are included.
3. The distillation solution is very attractive for boosting performance in practice without sacrificing inference time, which is contributing to a timely trend. There's a good chance this approach will be added to everyone's box of inference tricks.
4. Compute costs are well discussed and addressed with the distillation solution.
Solid and interesting review of past works, especially about Machine Translation where MBR decoding has already become popular.

### Weaknesses
1. The method is not particularly novel, as MBR decoding with LLMs has been studied in the past (as discussed in Related Work), but not with an LLM as judge.
2. Given the novelty being the use of a judge to find the consensus output, I would love to see more analysis on the dependence of the LLM judge’s quality. There is a notable gap with other utility functions, so it would be helpful to understand where they diverge. See questions below.

### Questions
1. Could the LLM model itself be used as a judge? In the spirit of self-improvement.
Jinnai et al. evaluated their utility metrics on benchmarks without LLM judge. How would LLM judges perform there? (e.g. machine translation, summarization)
2. Could there be some kind of overfitting/bias towards the GPT-4o judge that is dominating the win-rates in the comparison (the “closer” the judge to GPT-4o, the better the MBR)? In the extreme case, what if GPT-4o was used as a judge - I’m sure that would beat even Prometheus. Perhaps one could compare the outputs selected by the evaluated judges to GPT-4o decisions to find out if the ranking of win-rates corresponds to agreeing with GPT-4o.
3. I would love to see some qualitative analysis on how BoN and MBR generation selection differ with the same judge. The paper explains that the smoothing effect of MBR might be helpful to find the best generation, but I would like this to be made a little more built out and supported by examples.

### Soundness
3

### Presentation
4

### Contribution
3
