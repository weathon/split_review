# Is In-Context Learning Sufficient for Instruction Following in LLMs?

- Decision: Accept
- Scores: 8, 3, 6

## Abstract
In-context learning (ICL) allows LLMs to learn from examples without changing their weights: this is a particularly promising capability for \textit{long-context} LLMs that can potentially learn from \textit{many} examples. 
Recently, \citet{lin2024the} proposed \urial, a method using only three in-context examples to align base LLMs, achieving non-trivial instruction following performance.
In this work, we show that, while effective, ICL alignment with \urial still underperforms compared to instruction fine-tuning on the established benchmark %
MT-Bench, %
especially with more capable base LLMs. 
We then uncover the most relevant elements for successful in-context alignment, finding the crucial role of the decoding parameters.
Based on these insights, we show that the approach of \urial can indeed be improved by adding \textit{high-quality}, possibly carefully selected via greedy search, demonstrations in context, getting closer to the performance of instruct models.
Finally, we provide the first, to our knowledge, systematic comparison of ICL and instruction fine-tuning (IFT) for instruction following in the low data regime, %
where ICL can be a viable alternative to IFT.
Overall, our work advances the understanding of ICL as an alignment technique and its relationship to IFT.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies whether in-context learning can be competitive with instruction fine-tuning methods on instruction following tasks. The empirical results ablate many different components of in-context learning methods and the dataset composition. The results are comprehensive and yield several potentially useful results (e.g., how decoding parameters impact the performance). The overall conclusion is that in-context learning is worse than and not as scalable as instruction fine-tuning.

### Strengths
The experimental results are comprehensive. The problem studied in this paper is of interest to the deep learning community today.

### Weaknesses
Writing is not clear. See below:
- The author should have a brief introduction to URIAL since it's heavily used in the later sections when explaining the experimental results. The current version refers to URIAL's components with the assumption that the readers know URIAL in detail. The current explanation like Line 120-126 is not enough. What do you mean by stylistic examples? What do you mean by rules? What do you mean by "begin with affirming the user queries?" I suggest adding some examples in the main paper to help the readers understand the idea. The description of URIAL lacks specific details about the structure and content of the stylistic examples and rules. For example, are the stylistic examples generated using a specific method or are they hand-crafted? What is the scope of the rules, are they general guidelines or specific constraints on the output? The phrase "begin with affirming the user queries" is also vague. Does it mean that the model should repeat the user query verbatim or paraphrase it? More concrete examples would clarify these points.
- Similarly, what SkillMix datasets do has to be explained. The paper does not provide sufficient information about the SkillMix dataset. What is the data format? What kind of skills are covered? How diverse are the examples? Without this information, it's difficult to assess the relevance and quality of the dataset used in the experiments.
- This paper presents many experimental findings in each section, but the messages of these findings were not highlighted. For example, Section 2.1 has the title "Systematic Evaluation of URIAL" and starts with a brief explanation of URIAL. When reading this section, I couldn't expect what you will be talking about in this section and I quickly get lost while reading a bunch of implementation details. Even after finishing the section, I couldn't get the takeaway message clearly. Section 2.2, in contrast, did a better job on explaining the results.

### Questions
- The abbreviation URAIL is not defined.
- Line 139: If providing multi-turn examples improves performance at multi-turn conversation, why do the authors not study it in this paper?
- The results in Figure 2 are not representative in my opinion since the confidence bounds are overlapped largely. 
- Line 320: You say including examples from SkillMix is better than including examples from URIAL. Does URIAL come with a curated dataset as well? 
- Figure 3: I don't get it clearly. Is "Llama-3.1-8B-instruct" a model with instruction fine-tuning? Are these rest of ICL methods based on Llama-3.1-8B base models?

### Soundness
2

### Presentation
2

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
An interesting empirical study of the existing URIAL method that allows alignment via ICL. Unclear whether the contributions are significant.

### Strengths
The paper conducts a comprehensive empirical analysis of the URAIL method for aligning pre-trained LLMs via in-context learning.
It considers different datasets, LLMs and test scenarios of relevance.
The figures are well done and show interesting trends. The paper is well structured and easy to follow.

### Weaknesses
I am unsure about the exact contributions of this work. It appears mainly as an extended study of the URIAL method on (a) additional models, (b) additional datasets, and (c) more hyperparameters. A relevant contribution of the work is the greedy ICL prompt search, which shows significant performance improvements (i.e., higher performance with much fewer ICL prompts, i.e., with much fewer test-time compute requirements). However, the entire analysis is again primarily based on a single dataset (MT bench). The language sometimes could be more academic, consider e.g. “suffers from some heavy overfitting”.

Upon further inspection of the MT-Bench dataset, it appears that this dataset is only composed of 80 samples. The vast part of the analysis is based on this dataset (i.e. 7 Figures / Tables in the paper are largely based on results from it.) I do not believe that this one dataset is sufficient for the conclusions drawn in the paper, and updated my score accordingly.

### Questions
- What do the authors see as the work's main contribution, apart from the empirical study of a previously introduced method?
- See other aspects mentioned above

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper continues on URIAL work to deep dive into the comparison of ICL vs IFT. It revealed crucial insights to improve ICL performance, i.e. high quality examples and temperate as decoding parameters. On the flip side, it also shows the shortcoming of ICL, especially on subsequent turn in conversational benchmarks.

### Strengths
This paper contributes valuable guidance to practitioners who often struggle between the choice of finetuning and prompting. The work is particularly useful for scenarios where obtaining training data is challenging. Also when all attentions are on instruct models, this paper shows that base models alone can be instructed and aligned, and made useful. This shall open the gate to lots of research projects too.

### Weaknesses
More attribution works are needed to answer why the outcome is what it is. For example, the poor performance of the second-turn in MT benchmark definitely needs deeper dive. Is it because of the formatting or lack of examples? What caused the ICL to lose grip of the first turn?

Considering that the authors work on small size open LLMs (except GPT-4), mechanistic study with logits or internal states shall definitely reveal more insights.

### Questions
For prompts ending up with varying output performances, what are their KL divergence?

If you repeat your experiments on instruct models instead of base models, what would the results be?

How does ICL cope with long-context tasks (summarization, coding, etc.) where context window limit the extent of examples?

### Soundness
3

### Presentation
2

### Contribution
3
