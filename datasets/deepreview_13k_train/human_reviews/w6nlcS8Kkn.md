# To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
Chain-of-thought (CoT) via prompting is the de facto method for eliciting reasoning capabilities from large language models (LLMs). But for what kinds of tasks is this extra ``thinking'' really helpful? To analyze this, we conducted a quantitative meta-analysis covering over 100 papers using CoT and ran our own evaluations of 20 datasets across 14 models. Our results show that CoT gives strong performance benefits primarily on tasks involving math or logic, with much smaller gains on other types of tasks. On MMLU, directly generating the answer without CoT leads to almost identical accuracy as CoT \emph{unless} the question or model's response contains an equals sign, indicating symbolic operations and reasoning. Following this finding, we analyze the behavior of CoT on these problems by separating planning and execution and comparing against tool-augmented LLMs. Much of CoT's gain comes from improving symbolic execution, but it underperforms relative to using a symbolic solver. Our results indicate that CoT can be applied selectively, maintaining performance while saving inference costs.}. % more studies are needed to determine how models can best leverage intermediate tokens during generation to enable strong and more faithful reasoning across the whole range of LLM applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this work, the author study the effect of CoT on a wide variety of problems and try to identify categories of problems for which it work v/s ones for which it doesn't. Using their meta-analysis of results from various recent papers and their own analysis spanning models and datasets, they conclude that CoT is more useful for math and logic based tasks, while providing minimal gains for other task tasks.

### Strengths
1. CoT is a popular and often over-used strategy in LLM based applications. This paper dives deep into where it actually is useful and where it isn't - contributing to a better overall understanding of the technique and lay foundations for future improvements.  
2.  The paper is well-written, detail experiments well and supports its key insights with exhaustive empirical analysis.   
3. The extensive analysis of contemporary literature is quite interesting and one of a kind.

### Weaknesses
1. While the paper comes up with some interesting analysis, it doesn't really propose alternatives - it claims that CoT is a general approximation to logical solvers but proposes using them during inference. Arguably, it is hard to come up tool augmented neuro-symbolic techniques that fit most symbolic reasoning tasks well -making CoT especially appealing. Even though, this doesn't bring down the paper's contributions, it would have made the work more interesting for me.
2. The paper distinguishes the 264 datasets on which it bases its main position with but doesn't specify how it comes up with the categorization. A detailed explanation of these exact considerations can help better utilize the paper's recommendations in practice.
3. Language models are not a monolith and different Language Models behave differently depending on the fine-tuning dataset, preference alignment etc. Trends in Fig 6 already highlight the variation across LMs. The paper makes broad claims without often specifying the LM over which the result were found- almost assuming that they will generalize across models. A few examples:
	* Figure 3: What are the 5 representative models?
	* Line 320-321: Analysis of the impact of few-shot CoT v/s direct ?
Besides, the paper lacks key model-wise analysis of its findings.

### Questions
1. What are the considerations the authors took to categorize the datasets into the proposed categories?
2. How does the paper's findings hold across LLMs?
3. Minor: 
    * What are the 5 representative models used in Figure 3 right?
    * What do different colors in Figure 4 represent?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents a comprehensive analysis of prompt-based chain-of-thought across a variety of tasks, specifically as compared to direct answer prompting. The analysis proceeds in three parts.

## Part 1
The paper presents a meta-analysis of performance gains due to prompt-based chain-of-thought reported in the literature. They choose a set of 110 papers from recent NLP and ML venues that explicitly compare direct answer prompting to chain-of-thought. They manually extract results from these papers. They they group tasks into 14 categories, and analyze the average performance gain due to chain-of-thought in each category. They find that the top 3 categories – symbolic reasoning, math, and logical reasoning – benefit substantially, while other categories see only a small benefit. There is some discussion of exceptions to this rule, but the trend from the literature suggests that chain-of-thought largely benefits only mathematical or symbolic reasoning tasks.

## Part 2
The paper presents direct comparisons of direct answering, zero-shot, and few-shot chain-of-thought on 14 LLMs on 20 datasets, broadly categorized as Commonsense, Knowledge, Symbolic, Mathematical, and Soft Reasoning. Here too, they find that performance gains are primarily in tasks that require some form of symbolic or mathematical reasoning, with trends being fairly stable across models. Even gains on Commonsense, Knowledge, and Soft Reasoning datasets can be tied back to mathematical reasoning, like in a mixed dataset such as MMLU (where they find that a majority of the gain is in problems that involve the "=" sign).

## Part 3
The paper then examines why chain-of-thought might be so particularly helpful for mathematical or symbolic reasoning. For this, the paper identifies the chain-of-thought process as consisting of two processes – planning and execution. In the planning phase, the problem is mapped to a plan, and in the execution phase, the plan is executed to get an answer. The paper presents a way to compare the influence of these stages by having models generate a plan in code/logic, and then comparing the execution of the plan with direct LLM answering, execution with chain-of-thought, and execution with a symbolic engine. The paper argues that most of the gains of chain-of-thought appear to be from more reliable execution, rather than superior planning.

Given these, the paper concludes that:
- prompt-based chain-of-thought is not an effective method for reasoning construed broadly
  - The paper does highlight that methods that leverage more compute or search, might be more promising, as might methods that train models to use chain-of-thought
- in tasks where chain-of-thought does provide an advantage in better executing complex plans, there may be more reliable symbolic execution options that could do even better

### Strengths
- The paper presents a meta-analysis of work in ML and NLP that is appropriate (provides evidence of where chain-of-thought helps without re-running every single experiment)
  - This is not a commonly used approach in ML work, so I cannot be entirely certain, but the methodology of the meta-analysis seems mostly sound.
- The paper reinforces the findings of the meta-analysis with direct comparisons of multiple models across a number of tasks, both complementing and extending the findings of the meta-analysis
  - This comparison seems sound and thorough, particularly with attention to detail such as ensuring answers appear earlier in the response for direct answering as compared to chain-of-thought, which is a simple and effective way to measure that a model does produce a chain-of-thought
  - Identifying the "=" sign as a crucial determiner of gains in MMLU is also a cleverly designed experiment with informative findings
- The design of the study to separate execution and planning is an interesting and useful approach, and uses prior work like PAL in a clever way to set up a controlled study
  - The discussion of how this relates to early work on chain-of-thought (Nye et al., 2021) provides useful context

### Weaknesses
 - There is no discussion of model size in the meta-analysis. Work that proposed chain-of-thought (such as Wei et al. (2022) and Kojima et al. (2022)) explicitly discuss how size is a crucial factor in the effectiveness of chain-of-thought. In fact, if we consider Table 26 of Kojima et al. (2022) that compares chain-of-thought and direct answering across a range of model sizes, of the 4 models tested, only 1 shows a substantial gain with chain-of-thought. Given that the results presented aggregate across paper and category, and that models of different sizes are not distinguished in the meta-analysis figures, it is unclear how much results of chain-of-thought on smaller models (even as large as 7B (Kojima et al., 2022; Table 26)) is the reason why the method appears to be ineffective.
  - This concern is mostly addressed in the direct comparisons, which show similar findings across a range of sizes, and hence I don't think this significantly bears on my rating, but if something can be said about the role of size in the meta-analysis it might further bolster the argument.
- Section 5 ends with "When possible, LLMs should be paired with symbolic solvers at inference time when solving symbolic tasks to achieve consistently better performance over direct answer **and** CoT." While it is an important takeaway that in some cases, the benefits of chain-of-thought can be reaped to a greater degree with exact symbolic execution, one aspect of the problem that doesn't seem to be discussed is the difficulty of getting models to produce the inputs to symbolic execution engines. These engines are powerful, but brittle, and minor errors in producing a program to be executed can lead to complete failure. Chain-of-thought on the other hand allows the model to be more flexible and robust. This is directly visible in the results, for example, for FOLIO. Models with chain-of-thought or plan+chain-of-thought execution perform _better_ than the plan+tool solver counterparts, which could be largely due to the relatively high unparseability rates. This suggests that the program writer-solver pair of (LLM, LLM) is better than the pair of (LLM, tool solver) in some cases (i.e. the LLM is a better executor of the plans it writes than a tool). If what matters to us is the final answer, should we not consider a solution that makes it more likely to get the correct final answer (setting compute requirements aside for a second)?
  - I'm not suggesting that we should declare chain-of-thought the winner here, just that I think this adds some nuance to what is a definitive recommendation made in the paper. I don't think this would change my recommendation, but I'd be glad if the authors would engage about this.

### Questions
> [323] Not much. Free response capabilities may be hindered by pre-planning or reasoning about the correct response.

I'm unsure what this means. Where is the hinderance to free-response capabilities that is being referred to? I might have missed something, but it was unclear from the writing.

> Informally, we believe many readers of the literature to hold the following view: [...]

This may not be a really substantive question, but is there a reason for framing this as a belief held by readers, rather than a specific reference to some prior paper(s) as is the norm?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a comprehensive analysis of the CoT prompting technique. Through a meta-analysis of existing literature and extensive experiments on various datasets and models, the authors demonstrate that CoT is particularly effective for mathematical and symbolic reasoning tasks but offers minimal benefits for other types of reasoning. The study provides valuable insights into the conditions under which CoT excels and suggests a shift towards more advanced computational paradigms for LLMs.

### Strengths
1. The paper offers both quantitative performance metrics and qualitative insights into why CoT is effective in certain tasks, enhancing the depth of understanding.

### Weaknesses
1. I believe the core findings of this paper are already well-known among many researchers in this field. Although the authors conduct a comprehensive investigation, the core contributions appear to be limited.
2. The authors define symbolic and non-symbolic reasoning but categorize experimental datasets into multiple types, which may lead to confusion.

### Questions
In some tasks, the use of CoT reasoning can decrease performance. What do the authors consider to be the key reasons for this? Will this phenomenon continue to be an issue in future LLMs?

### Soundness
3

### Presentation
2

### Contribution
2
