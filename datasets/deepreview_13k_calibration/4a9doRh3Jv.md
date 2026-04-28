# Fast and Slow Generating: An Empirical Study on Large and Small Language Models Collaborative Decoding

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 6, 3

## Abstract
Large Language Models (LLMs) exhibit impressive capabilities across various applications but encounter substantial challenges such as high inference latency, considerable training costs, and the generation of hallucinations. Collaborative decoding between large and small language models (SLMs) presents a promising strategy to mitigate these issues through methods including speculative decoding, contrastive decoding, and emulator or proxy fine-tuning. However, the specifics of such collaborations, particularly from a unified perspective, remain largely unexplored. Inspired by dual-process cognitive theory, we propose a unified framework in this paper, termed Fast and Slow Generating (FS-GEN). Within this framework, LLMs (sometimes along with SLMs) are categorized as System 2 (slow and deliberate), while independent SLMs are designated as System 1 (fast and intuitive). We provide a comprehensive analysis of these collaborative methodologies, elucidating their common properties and shedding light on the differential knowledge capabilities of System 2 versus System 1 through the FS-GEN framework. Our findings indicate that only a small proportion of collaborative interactions (approximately less than 20\% in most instances) are necessary across various methods. These interactions between System 1 and System 2 conform to a scaling law related to the parameter ratios, enabling predictable collaboration. Furthermore, we explore the specific conditions under which collaboration proves most effective, particularly from an uncertainty perspective, offering novel insights that may guide future optimization efforts. Our research underscores that the fundamental distinction between System 1 and System 2 lies in the uncertainty of next token predictions, where interventions by System 2 are crucial to support System 1.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper explores collaborative decoding strategies between large language models (LLMs) and small language models (SLMs). The authors introduce the FS-GEN framework, categorizing LLMs as System 2 (slow and deliberate) and SLMs as System 1 (fast and intuitive). The research focuses on decoding methods like speculative decoding, contrastive decoding, and proxy tuning to improve efficiency and mitigate issues like high inference time.

### Strengths
Originality:- The paper introduces a novel FS-GEN framework.
Quality:- The tables and figures are very well used.
The paper is written with a great clarity. 
significance:- The paper compares from smaller models to larger ones, based on the number of parameters.

### Weaknesses
Could provide more discussion of practical applications.
Trade-offs between the inference time and cost can be a great addition.
The experiments focused on only few tasks like:- MMLU-STEM, GSM8k, and MBPP, Having experiments over domain specific datasets can give a better understanding.

### Questions
How generalizable do you believe your findings are to other language tasks or domains?
How do you think the collaborative patterns might change, If different sampling technique is used.

### Soundness
3

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
The paper studies collaborative decoding, where small language models and large language models work together in the decoding process. In particular, the paper offers a unifying perspective on 3 different collaborative decoding techniques: proxy tuning, speculative decoding and contrastive decoding. Authors categorize the larger model as System 2 and smaller model as system 1.
The paper studies the 3 techniques, their commonalities and differences through their framework FS-GEN (Fast and Slow Generating).
They find that only small fraction of decoding steps require collaboration and that System 1 and 2 follow a scaling law related to parameter ratios.

### Strengths
Paper studies a relatively under explored but important and emerging area of research.
The findings are interesting, particularly the 2:8 law, collaborations being most necessary at the beginning of decoding and that high uncertainty tokens within System 1 are more likely to require collaboration.
Some of the findings could spur targeted research in the field of collaborative decoding.
Experimental benchmarks cover different capabilities like knowledge, math and coding, as well as two LLM families.

### Weaknesses
The System 1 and System 2 analogy is not well fleshed out, to the point where it feels more like a distraction from the main contributions.

The line fits on the param ratio scaling plot aren't very convincing.

The uncertainty analysis is only qualitative - quantitative metrics to support this hypothesis (covering different tasks and model families) are missing. Without them its hard to have confidence in this finding.

### Questions
Related work is pushed to the Appendix. This is a strange choice. I understand there might have been a space crunch, but Related Work makes much more sense to be in the main paper.

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
4

### Summary
The paper analyzes the patterns of collaboration between SLMs and LLMs when used in a collaborative decoding/training setup. By analyzing this behavior across multiple collaboration setups, tasks, and model families, the authors draw the following conclusions:
- The collaboration frequency peaks at about 20%, with the maximum collaboration happening when there's the biggest gap in the model sizes. In fact, there's an inverse scaling law connecting the model size ratio and the collaboration frequency (more clearly evident for Qwen models than Pythia). 
- Most of the LLMs/System 2 interventions are required at the start of the decoding and for tokens for which SLMs are uncertain.

### Strengths
- Proposes a new framework to analyze the collaborative behavior between models
- Empirical results shed new light on this collaborative behavior. In particular, the scaling law for collaboration and frequent positions of collaboration are quite interesting.

### Weaknesses
 - The paper analyzes speculative decoding, contrastive decoding, and proxy tuning. Except for speculative decoding, it's not clear if the analysis provides any executable insights for the other two setups. 
Drawing questionable analogies with human cognitive processes just because one model runs fast and the other slow and then commenting about how the collaborative distributions are different (L127-L129) is extremely flawed reasoning. The analogy doesn't make sense, except for the fact that one model is faster and the other is slower.   

Comments about writing:
- Why is O_g being used and not O_f for p_f (fused logits) in Section 2.2
- L053: "allow" -> "allows"
- L195: "produce" -> "produced"

- It is not clear what exactly is being illustrated in Figures 11, 12, and 13. What are the different features? 
- How does one use the insights from this paper for contrastive decoding and proxy tuning?
- Currently, greedy decoding is used to establish whether collaboration is required or not. I wonder if the next token perplexity could be another measure.

### Questions
- It is not clear what exactly is being illustrated in Figures 11, 12, and 13. What are the different features? 
- How does one use the insights from this paper for contrastive decoding and proxy tuning?
- Currently, greedy decoding is used to establish whether collaboration is required or not. I wonder if the next token perplexity could be another measure.

### Soundness
3

### Presentation
2

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
This paper presents an investigation into collaborative decoding between small and large language models, attempting to formalize it from the perspective of a system 1 / system 2 collaboration, where system 1 operates quicly and intuitively, while system 2 functions in a more slow and deliberate manner. The paper focuses on the differences between system 1 and 2 in the context of decoding, when system 1 would underperform compared to system 2 and how efficiency of the compound system can be improved. For their investigation, the authors use the Qwen and Pythia series. To evaluate the system, they consider MMLU-STEM, GSM8k and MBPP. The analysis focusses on two aspects of collaboration: frequency and position, where the former refers to how often the models should interact, where as the second one refers to the specific points of interaction. They find thta collaborative interactions are most critical at the beginning of the generation, and that the optimal frequency is around
 80-20, depending on the task.

### Strengths
The paper asks an interesting question and presents several findings. The idea to take inspiration from system 1 and system 2 is interesting.

### Weaknesses
My main qualm with the work is the presentation of the paper, which almost reads like a slide deck: plenty of conclusions and graphics, but little to no details about how the experiments are actually set up or how the conclusions are drawn. I also don't see any evidence of how well the collaborative decoding actually works (that is, there are no accuracy scores reported), and how that may depend on the frequency or place of collaboration). The many figures are hardly described. There is also no discussion of how the results are different between the benchmarks and whether that may make sense given the topics.

Lastly, while I like the idea of interpreting collaborative decoding as a system-1 system-2 scenario, but the current work does not really convince me that it makes sense to explore collaborative decoding with SLMs and LLMs in this way. Wouldn't LLMs be better both at the intuition and the deliberate reasoning?

In sum, it could be that the paper contains many interesting results, but if so, the current presentation does not do them justice.

NB: the related work section is in the appendix and is not even referred to

### Questions
Could you elaborate on the motivation of using system 1 - system 2 reasoning for collaborative decoding with SLMs and LLMs, specifically?

### Soundness
1

### Presentation
1

### Contribution
2
