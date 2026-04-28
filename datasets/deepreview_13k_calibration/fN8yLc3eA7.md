# When LLMs Play the Telephone Game: Cumulative Changes and Attractors in Iterated Cultural Transmissions

- Decision: Accept
- Avg Score: 6.00
- Scores: 3, 8, 8, 5

## Abstract
As large language models (LLMs) start interacting with each other and generating an increasing amount of text online, it becomes crucial to better understand how information is transformed as it passes from one LLM to the next. While significant research has examined individual LLM behaviors, existing studies have largely overlooked the collective behaviors and information distortions arising from iterated LLM interactions. Small biases, negligible at the single output level, risk being amplified in iterated interactions, potentially leading the content to evolve towards attractor states. In a series of \textit{telephone game experiments}, we apply a transmission chain design borrowed from the human cultural evolution literature: LLM agents iteratively receive, produce, and transmit texts from the previous to the next agent in the chain. By tracking the evolution of text \textit{toxicity}, \textit{positivity}, \textit{difficulty}, and \textit{length} across transmission chains, we uncover the existence of biases and attractors, and study their dependence on the initial text, the instructions, language model, and model size. For instance, we find that more open-ended instructions lead to stronger attraction effects compared to more constrained tasks. We also find that different text properties display different sensitivity to attraction effects, with \textit{toxicity} leading to stronger attractors than \textit{length}. These findings highlight the importance of accounting for multi-step transmission dynamics and represent a first step towards a more comprehensive understanding of LLM cultural dynamics.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes the evaluation of LLMs through doing an iterated task many times, and evaluating the subsequent effects on toxicity, positivity, difficulty, and length. The authors also evaluate the strength and position of attractors (essentially equilibria). The claims of the paper are mainly that more open-ended instructions lead to stronger attraction effects than more constrained tasks, and that some metrics have different sensitivity to attraction compared to others.

### Strengths
Originality: Multi-turn interactions in LLMs are an interesting an less studied area in LLM evaluations on qualities such as bias. The telephone game is an easy to grasp concept that allows readers to conceptualize the experiments easily. 

Quality: The evaluations are conducted on both open- and closed-source models. The measurement methods of metrics are implemented reasonably. 

Clarity: Overall the paper is easy to follow. Graphs are colorful and visually appealing. 

Significance: The motivation of the paper, to study the effects of multi-step interactions of models, is meaningful to study.

### Weaknesses
Originality: None

Quality:
- There is little justification for why "rephrase", "take inspiration from", and "continue" are chosen as the three tasks for the models to iterate on.
- I don't think one of the main conclusions that the authors claim is supported by their experiments. The authors use these three tasks to make the claim that tasks that are less constrained have higher attractor strength, but the three conditions are difference in many different ways, not just the level of constraint; to accurately test this hypothesis, you would need a more constrained and less constrained version of the same task, such as "rephrase but start with the same first five words" versus "rephrase". I worry that there are many confounding factors (such as rephrase ping-ponging back and forth across a small set) which could lead to the lower attractor strength that the authors observe. Thus, I would hope for a more rigorous analysis with more task conditions in order to confirm the findings of the paper.
- Models are outdated, which is especially important to get right for evaluation-type papers in order to gain actionable insights.
- Sample size is very small (20 initial texts) and the domains that are chosen from are seemingly random (appendix A). This is to the point that I would question the generalizability of the results in the paper.
- Other findings, such as toxicity quickly converging to 0, is uninteresting due to safety tuning of models.

Clarity:
- Missing the entire literature on Model Collapse which is highly relevant (e.g., https://www.nature.com/articles/s41586-024-07566-y, https://openreview.net/forum?id=5B2K4LRgmz#discussion)
- Missing papers on bias in LLMs (e.g., https://arxiv.org/abs/2402.04105)
- Missing a large amount of more prominent works on models and humans displaying similar cognitive biases (line 49-50) e.g., https://arxiv.org/abs/2402.18225, https://arxiv.org/abs/2406.17055, https://www.pnas.org/doi/10.1073/pnas.2218523120
- Unfinished sentence at line 199-200: "texts spanned various types of content: scientific abstracts"
- Figure and graph text is too small, error bars are not shown.

Significance:
- I think a big issue of the paper is that it doesn't motivate the research questions. It is simply stated that multi-turn paradigms (such as scientific reviews and multi-agent environments) are common applications of LLMs, and makes the logical jump that it is necessary to evaluate these models in iterative scenarios, specifically rephrasing, inspiration, and continuation. The issue here is two-fold. First, there is little motivation in the introduction about how real-life tasks (where there are actual implications) can be adequately abstracted into these multi-turn iterative settings without losing key details that make those tasks important. For example, when news articles are continuously rephrased, often this is with human oversight --- why can this step be taken away in the experiments and what is lost from this? There does not seem to be any discussion in this direction. Next, there needs to be some generalizability statement saying that xxx are the most common use cases of LLMs in iterative settings and therefore we do rephrasing and other tasks. Without the motivation from actual use cases, it is hard to find significance in just directly analyzing iterative generation processes in LLMs because somewhat similar paradigms are used in practice.

### Questions
See weaknesses.

### Soundness
1

### Presentation
2

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
This paper shows that LLMs can amplify small biases through iterative interactions. The authors show that biases, such as toxicity, can become reinforced in transmission chains. Additionally, open-ended instructions generate stronger attraction effects than constrained tasks.

### Strengths
The research is grounded in a strong foundation of social science theory, specifically cultural attraction theory (CAT). The phenomenon they observe is novel and interesting, and the writing is clear.

### Weaknesses
- The paper does not explicitly provide theories or mechanisms underlying this phenomenon. Why do LLMs exhibit this human-like behavior of transmitting cultural patterns? Do LLMs simply mimic human behavioral patterns present in the training data, or does this behavior emerge due to specific objectives in LLM training? The authors may consider discussing this further or suggesting directions for future research.

- Page 17, line 866: The paper relies on a small sample of initial texts (5 abstracts, 10 news articles, and 5 social media comments from online datasets). I am concerned about whether findings derived from such a small sample can be generalized across a broader range of tasks. The authors may consider including the full set of initial texts in the appendix so that readers can evaluate them directly. The authors may also consider replicating their main findings using paraphrased prompts to demonstrate that their results are not sensitive to prompt design.

- Page 10, line 539: Here, the authors identify the absence of network-based approaches as a limitation and an area for future work. It could be useful to suggest one or two specific network-based strategies to reduce toxic transmission and promote prosocial behaviors (e.g., lower toxicity, kindness). For instance, this paper suggests that interaction within broader social networks might reduce the transmission of toxic behaviors among LLMs: https://arxiv.org/abs/2402.12590.


### Questions
- Page 16, line 866: How do the authors justify the generalizability of their findings based on 20 conveniently sampled initial texts? The authors may consider providing more information in the appendix about how these texts were sampled or discussing the limitations of this sampling approach. For example, are these texts a balanced sample? (e.g., do the 5 abstracts cover a variety of scientific topics, do the 10 news articles address diverse issues, and do the 5 social media comments represent a range of user demographics?)

- Page 7, line 358: The authors conduct Kolmogorov–Smirnov (KS) tests and calculate p-values repeatedly to compare property distributions after one interaction and after multiple interactions. Given the multiple comparisons, should the authors consider applying a Bonferroni or FDR correction to control for potential false positives? Please address this by applying the appropriate correction (if applicable) or providing a justification if these adjustments are unnecessary.

- Page 5, line 237: Why did you use the term "positivity bias" instead of "negativity bias" here? Typically, "positivity bias" refers to favoring more positive words (https://www.pnas.org/doi/abs/10.1073/pnas.1411678112). However, in this context, it appears you are referring to a bias toward more negative words.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors use the storytelling medium of the 'telephone game' as a means of examining how llm text-generations evolve in a multi-turn setting. They introduce methods of analyzing the effect of multi-turn versus single turn conversations on properties such as 'positivity, difficulty, toxicity and length' and demonstrate that some properties rapidly reach saturation, depending on the exact nature of the prompt provided to the llm (ie, continue vs rephrase)

### Strengths
In my view, the biggest strengths of the paper are in research question and approach. There exists an extremely large body of research in investigating the single-turn capabilities of LLMs but less so in multi-turn settings. For this, the specific aspect of how certain attributes act as 'attractors' in driving the LLMs responses is extremely relevant and the authors methodology for measuring this is well-founded in the literature. The results they show, that certain attributes are (understandably) biased towards and reach saturation fairly quickly, are definitely relevant and an important contribution to the literature.

### Weaknesses
The primary weaknesses of the paper are in the limited number of models and that (to my understanding) each 'conversation' was conducted by the same 'model' (described in the paper as homogenous transmission chains) without an ablation of how a heterogenous transmission chain could shift results. While doing this with a number of agents n> 2 might be excessive, I do think a 2 agent heterogenous system could be reasonable. Furthermore, the choice of tasks, while described as 'typical', lacks a more rigorous justification. The paper would benefit from a more detailed explanation of why these specific tasks were chosen over others, especially given the vast range of potential use-cases for LLMs. The lack of exploration into how different prompt phrasings might influence the observed attractor dynamics also represents a limitation in the current study. Finally, the absence of any recent models, such as Gemini, Claude, Grok, or Molmo, further limits the generalizability of the findings, as these models may exhibit different behaviors in multi-turn settings.

### Questions
1.) How were the tasks selected?

2.) Why were other commercial (Gemini, Claude) and open-source models (Grok, Molmo) not selected for testing?

3.) What was the authors motivation in not including heterogenous transmission chains?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper “When LLMs Play the Telephone Game” explores how repeated information transitions between language models (LLMs) change the properties of the information over time. In a series of experiments, the authors show that as text moves through multiple LLMs, small biases can build up, shifting content towards stable “attractor” states. They find that factors like model type, task instructions, and tuning settings affect how strongly text properties like toxicity or positivity converge. This study highlights that evaluating LLMs on single outputs misses important dynamics, calling for multi-turn testing to understand LLMs’ behavior in iterative information transitions.

### Strengths
The paper explores the shift of information properties during multi-turn LLM interactions using a “telephone game” setup. The experiment design is systematic, with some important metrics like toxicity and positivity, effectively showing how text properties shift across iterations. The paper contains a complex analysis, introducing some new methods for evaluating cultural attractors. Its findings are significant, emphasizing that single-turn evaluations miss key dynamics, especially for applications involving iterative or multi-agent LLM use. This work offers insights for improving LLM evaluation and alignment in real-world scenarios.

### Weaknesses
Although I appreciate the authors' attempt at quantifying the "loss" of information during multi-turn agent interactions, a major concern is that the setup and tasks (rephrase, continue, and inspire) are not diverse or realistic enough to reflect the real-world use case or issues that people may face for social simulation. For example, the work only explores linear chains, missing out on complex network structures that mimic real-world LLM interactions (as indicated in the limitations). The findings obtained from the work highlight the importance of understanding/evaluating LLMs dynamically have been explored in many other previous works. 
E.g., [SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents](https://arxiv.org/abs/2310.11667), [On the Resilience of Multi-Agent Systems with Malicious Agents](https://arxiv.org/abs/2408.00989). I found the paper insightful and learned a few things from it, though I feel it may benefit from further development to fully meet the standards for a conference publication.

### Questions
For different kinds of tasks, have you tried different formats of the prompts? I would imagine the prompt would change quite a lot for some findings in the paper.

### Soundness
2

### Presentation
2

### Contribution
2
