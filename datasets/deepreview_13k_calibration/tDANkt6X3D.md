# Horizon-Length Prediction: Advancing Fill-in-the-Middle Capabilities for Code Generation with Lookahead Planning

- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 3, 5

## Abstract
\fimfull (\fim) has become integral to code language models, enabling generation of missing code given both left and right contexts. However, the current \fim training paradigm, which reorders original training sequences and then performs regular next-token prediction (\ntp), often leads to models struggling to generate content that aligns smoothly with the surrounding context.
Crucially, while existing works rely on rule-based post-processing to circumvent this weakness, such methods are not practically usable in open-domain code completion tasks as they depend on restrictive, dataset-specific assumptions (\eg \textit{generating the same number of lines as in the ground truth}). Moreover, model performance on \fim tasks deteriorates significantly without these unrealistic assumptions. 

We hypothesize that \ntp alone is insufficient for models to \textit{learn effective planning} conditioned on the distant right context, a critical factor for successful code infilling. To overcome this, we propose \textbf{\OURSfull} (\textbf{\ours}), a novel training objective that teaches models to predict the number of remaining middle tokens (\ie horizon length) at each step. \ours advances \fim with lookahead planning, enabling models to inherently learn infilling boundaries for arbitrary left and right contexts without relying on dataset-specific post-processing. Our evaluation across different models and sizes shows that \ours significantly improves \fim performance by up to 24\% relatively on diverse benchmarks, across file-level and repository-level, and without resorting to unrealistic post-processing methods. Furthermore, the enhanced planning capability gained through \ours boosts model performance on code reasoning. Importantly, \ours only incurs negligible training overhead and no additional inference cost, ensuring its practicality for real-world scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper highlights the current limitations of Fill-in-Middle (FIM) evaluations of popular coding benchmarks due to the post-process that takes places, which often boost evaluation performance artificially. The main contribution of the paper is introducing a new auxiliary loss that predicts the "horizon" length (i.e. the portion of tokens left to predict) on top of the typical Prefix-Suffix-Middle next token prediction loss to perform FIM tasks. With this training objective, LLMs perform better at FIM tasks, notably, the repository-level cross-fill code tasks.

### Strengths
- The paper soundly points out a glaring problem with current evaluation of FIM tasks that convincingly concludes that the post-processing only artificially boosts model scores while not providing additional insights into performance towards practical settings
- The paper provides a simple but novel idea that shows model improvements in the more rigorous evaluation (without any post-processing) of FIM tasks that would be of interest for the research community to apply to other domains
- The paper explores a breadth of different evaluation tasks for assessing their methods, including direct FIM tasks, repository-level cross-file FIM tasks, code fixing tasks, and reasoning tasks, demonstrating the effectiveness of their method
- That paper is well written and easy to understand/follow

### Weaknesses
 - Lack of rigorous confidence interval analysis - all the of experimental results lack statistical significance numbers, making it hard to judge if the performance improvements are due to noise or if they are statistically significant.
- Lack of theoretical/empirical evidence for why HLP works - it is not clear to me why this method works (assuming the experimental results are statistically significant). I believe the authors should add a section explaining (at least intuitively) why this method should work.
- Lack of additional baselines + ablations - adding some other strong baseline results would further validate this method. For instance, authors mention multi-token prediction in their related works. This methods performance should be reported as a strong baseline. For ablations, one idea could be explore the affect of increasing the complexity of the $hlp$_$head$ (e.g. using a MLP of increasing layers).

### Questions
- Could you report the statistical significance for each of the evaluations?
- I found Section 5 particularly interesting and believe a natural question to ask is if "Horizon Awareness" under NTP increases with model parameters?
- Why is $HLP_{L2R} + HLP_{FIM}$ not presented as the standard approach?
- Is there a reason that during training the HLP objective is applied for each token instead of just the first token? My concern is that remaining tokens after the first token do not really provide any "additional" signal for the horizon length.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper considers the task Fill-in-the-Middle (FIM) in code generation. Instead of completing the code, which is a common task in code generation, the authors consider the task of completing missing code given the left and right contexts.

They consider adding an auxiliary objective, predicting the number of missing lines, to the training of a language model. The model is trained to optimize next-token prediction as well as the number of missing lines. Empirically, this method improves performance on file-level and repository-level benchmarks.

### Strengths
FIM is an important problem that is relatively underexplored in the literature. The method proposed in this paper is simple and straightforward. It shows significant improvements on diverse benchmarks.

The paper is well-written and easy to follow.

### Weaknesses
 
**Contributions.**

Generalization: The proposed method appears to target at the FIM task. It limits its generalization to other code generation tasks.

Cost: The method requires fine-tuning a model specifically for FIM, which could be costly. Whenever a code model or a generalized model is released, it needs to be finetuned and maintained solely for this task.

**Evaluation metrics.** Table 4 uses Exact Match (EM) and Edit Similarity (ES) as evaluation metrics, which are not standard in code generation. This choice seems to be consistent with prior work. Is it possible to evaluate using pass@1 / pass@k? Or is it justifiable to measure EM and ES for codes?

### Questions
My questions are in the weaknesses section above. The authors are welcome to correct any possible misunderstandings.

### Soundness
3

### Presentation
4

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
This paper discusses the problem of fill-in-the-middle capabilities of code generation. The next-token-prediction way tends to make the model fail in long-length code generation to combine with both the left and right code sides. The paper proposes the method Horizon-Length Prediction (HLP) to tackle this issue. During the training, the model is also required to predict the ratio of the left token length to be generated to the total token length to be generated. This method is supposed to enhance the ability of LLMs to take care of the code generation length.

The experiments on extensive settings prove the effectiveness. The authors also use probing method to show that HLP trained model tends to have better capability on code generation length prediction. I am not an expert in code LLMs. Hence, I am not sure whether the proposed question and method are novel. Based on the current experiments, I think the results are effective and the paper is clear. However, the paper lacks extensive analysis on the proposed method like why should set like M-T/M for length prediction not other settings. I am giving a borderline in this case and will surely look through other reviews and authors' comments for final evaluation.

### Strengths
The issue and the method are clearly explained, the experiments are carried out extensively and achieved notably better performance. Meanwhile, the method will nearly not increase the burden of LLM training. The method is intuitively reasonable.

### Weaknesses
1) The techniques used are relatively simple. Most contents in the paper are well-known. However, it makes sense.

2) The setting of target as M-t/M is not such solid. In this equation, the target y also depends on the total length M. Whether it is optimal setting should be discussed. For example, ablation studies on other settings.

3) The paper also lacks the thorough analysis like why enhancing the ability to predict code generation length is such effective, especially in fill-in-the-middle problem. Will it also work in uni-directional code generation?

typo: Line 132 are are -> are

### Questions
As discussed in the above.

### Soundness
3

### Presentation
3

### Contribution
3
