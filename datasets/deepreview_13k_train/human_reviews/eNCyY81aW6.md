# FACTOR: Factoring Complexity and Context Length in Long-Context Model Evaluation

- Decision: Reject
- Scores: 3, 6, 3, 8

## Abstract
Large language models (LLMs) with extended context windows have shown remarkable capabilities, especially with contexts up to 128K tokens. However, whether these resource-intensive LLMs genuinely surpass simpler Retrieval Augmented Generation (RAG) techniques remains debated. 
We precisely delineate differences between long-context LLMs and RAG methods, emphasizing the unique long-context reasoning abilities of LLMs that RAG cannot replicate. 
Existing benchmarks often focus on retrieval tasks and contain weak if not none complex reasoning tasks, hindering assessment of reasoning over extended contexts. We introduce the \textbf{FACTOR} benchmark (\textbf{F}actoring \textbf{A}nalysis of \textbf{C}omplexity and \textbf{T}extual \textbf{C}ontext in \textbf{R}easoning), which evaluates LLMs by independently varying task complexity and context length. A comprehensive list of LLMs are evaluated on FACTOR. 
Besides mere accuracy scores, we also model the relationship between accuracy and complexity given the context length. A simple but consistent log-linear model works surprisingly well across various models. Also, the modeling contains two explainable parameters, the slope or Complexity Decay Factor (CDF) and the y-intercept or Contextual Decay Offset (CDO) that are shown to offer separate and insightful measures of the models' complex reasoning and long context innate ability. 
Our findings highlight distinct failure modes linked to task complexity and context length, underscoring the unique reasoning capabilities of long-context LLMs unattainable by RAG methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
Authors introduce FACTOR, a benchmark to evaluate LLMs' long context complex reasoning ability. The goal was to distinguish between long-context LLMs and RAG and explore how LLMs reasoning abilities depend on context length and task complexity.

FACTOR manipulates two variables that control for task complexity and context length: the first one is the number of variables--the larger the number of variables the higher the complexity of the task; the second one is length of filler text--adding text to the necessary portion of logic arguments. The authors find log-linear relationship between accuracy and complexity. Filler text is randomly generated text.

Authors find that for some LLMs' performance is outlines by different performance zones. They also outline how different pertaining strategies can influence performance.

### Strengths
I like that authors introduce task complexity and analyse performance as a function of this. The authors also show a nice analysis of this performance and divide it into performance phases.

### Weaknesses
The main weakness of this paper is that it doesn't provide analysis or evidence for the claim it set out to explore at the outset: i.e. showing the 'unique reasoning capabilities of long-context LLMs unattainable by RAG methods'. They don't provide any analysis of LLMs using RAG to support this claim. Authors could've had a the models tested also use RAG to perform the same task. In particular, because their filler text is randomly generated, I suspect RAG wouldn't have issues finding the relevant text and which would then greatly simplify the task for an LLM.

Another smaller issues pertains to the interpretation of the context decay offset (i.e. CDO) which is the intersect of the fitted log performance line and captures 'the baseline performance level influenced by context length'. I don't think this would be a correct interpretation of the intercept, for a simple reason that these intercepts of log performance can be higher 0 (and many times are as seem from Table 1), meaning that that this baseline performance can be higher than 100%, which doesn't make sense. In the context of the paper, these intercepts have no interpretation in terms of performance.

### Questions
Why no experiments were done comparing LLMs that use long-context windows and those that use RAG?

Why was the filler text decided to be a completely random text? Why not some meaningful filler text?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents FACTOR, a benchmark specifically developed to assess the performance of LLMs in handling complex reasoning tasks over long contexts. FACTOR generates synthetic problems that require models to understand and solve relationships between variables within long pieces of text. The authors also evaluate several models by evaluating them on varying tasks complexity and context length.

### Strengths
They propose a task generation framework that can be used to generate tasks with various levels of difficulty and context lengths. 

They evaluate multiple models using their benchmarks, and show that by increasing the context length and difficulty of the problems, these models struggle to reason correctly on them.

### Weaknesses
They don’t consider generating the filling text that is not random (e.g. is about math and reasoning) to make the task more difficult.


They only focus on the tasks that have explicit assignment expressions in the text. As the LLMs get more advanced, we need the test cases where the information necessary for the reasoning is expressed in natural language and not explicitly specified with a special notation.

### Questions
How many tasks are included in this benchmark for each experiment?

Could you present the results from Table 1 in a way that clearly highlights which models are performing better?

I am curious about how the o1 model would perform compared to the others (and o1 mini). 

Is the complexity of the problem only determined by the number of variables? How can you increase the complexity of the problem by changing the relationship of the variables and the nature of the problem (e.g. can some problems be unsolvable?)? 

What would happen if the filler text were meaningful rather than randomly generated?

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
3

### Summary
This paper performs an experimental analysis of several language models for a particular reasoning task solving sets of simple equations when context windows increase and separate those equations. The results are fitted with simple linear equations (after logarithmic scale transformations) and two indicators are derived from the linear functions (the slope, Complexity Decay Factor, and the y-intercept, the Contextual Decay Offset). Some insights are extracted from that modelling.

### Strengths
The paper is well written, and it is easy to follow.
There is more need to show how context windows affect some reasoning process and no appropriate benchmarks seem to exists, and previous analyses are confounded by other factors. So there's motivation for this paper.
Many models, including very recent ones, are covered. The experiments are quite exhaustive in that dimension.

### Weaknesses
The kind of task is relatively narrow, and different results could be observed for other tasks. In particular, the task question is formulated as choosing those variables that meet the requirements. This can have elimination/random components that are specific to this task and do not generalise to other tasks, or even some other presentations of this task (asking for actual values, instead of affected variables). There's not sufficient analysis of shortcuts, even if the authors claim they ensure they not happen. The paths to the right answers may be short in some cases and this is intrinsic with the problem and not random.

Apart from the use of only one problem, the major problem is the fitting. The authors calculate the logarithm of the y-axis on a bounded performance scale that goes between 0 and 1. But this can never give a linear relationship if we extend the complexity on the x-axis until we reach 0 accuracy (more variables or questions where choices or elimination make success by pseudochance very unlikely). The full response curves are actually sigmoid and the observed behaviour in this paper happens because collected data stops in a high-slope part of the sigmoid. Given the character of the y-axis, a logistic fit on the original scale would have made much more sense than a linear fit on a logarithmic scale.

In fact, extracting Effective Complexity using the linear model has the problem of possible extrapolation of a negative number of variables, something that wouldn't happen with a logistic model. With a logistic model, the effective complexity could simply be chosen when accuracy goes below a threshold of 90%.

The comparison with RAG appears in the abstract and the introduction, but then this disappears in the paper, so to me it's thrown as a red herring and deviates the motivation.

More justification is needed for repeated sampling as a proxy for increasing inference compute. Actually, there's no need to do experiments for this, as the tries are independent and it's a question of multiplying the failure probability of each of it. That's why figure 6 looks so linear.


Minor details:
- acronym in the abstract wrong
- the related work section has some expression and formatting issues (blank spaces missing before the references).

### Questions
I couldn't find how scoring of answers is performed. For instance, if the ground truth is v3 and v5, what's the score if the model says only v3? Is it only totally right or otherwise wrong? This is very important to understand whether there are shortcuts or not.

About o1-mini, it is said that "inference-time strategies can significantly enhance performance across task complexities", but we don't know (or at least no source is provided) of whether o1 is using some other techniques that affect the context window, or it gives several passes or other strategies, since the details of the system have not been published. Do you have more details about o1 that are publicly available?

Can you explain why repeated sampling is a proxy for increasing inference compute?

Can you make a logistic fitting instead of a linear fitting?

Do you think the results will hold for other tasks?

Where's the discussion/comparison about RAG?

### Soundness
2

### Presentation
3

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
This paper proposes FACTOR - a novel benchmark for evaluaition of long context reasoning in LLMs. Most importantly - it separates task complexity from context length. Then the paper evaulates several LLMs on this benchmark and shows that performance has a log linear relationship with complexity. Two metrics were then derived from this relationship - CDF and CDO. This is important to quantify the degradation in reasoning with complexity and length. Then the paper tests impact of pretraining and finetuning on these metrics, as well as the impact of more frequent sampling during inference.

### Strengths
Originality - I believe that CDO and CDF are great metrics that fill a gap in LLM literature, and the FACTOR benchmark is very useful for this.

Quality - The methodology makes sense and the experiments are well structured. I found the log linear result to be very interesting.

Clarity - the paper is well written, easy to follow.

Significance - These results are an important addition to scaling laws, and important findings.

### Weaknesses
Not much to say but - 

1. Task diversity is limited, which means maybe this is not as representative of real world scenarios.
2. FACTOR seems to be a very computationally expensive benchmark to run.

### Questions
1. Would FACTOR be extended to further logical inference/ commonsense reasoning tasks?
2. How robust are CDO and CDF to randomness of seeds used in FACTOR generation? Are there any analyses on stability of these metrics?

### Soundness
4

### Presentation
4

### Contribution
4
