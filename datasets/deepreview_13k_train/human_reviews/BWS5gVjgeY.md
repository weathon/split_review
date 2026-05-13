# Number Cookbook: Number Understanding of Language Models and How to Improve It

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Large language models (LLMs) can solve an increasing number of complex reasoning tasks while making surprising mistakes in basic numerical understanding and processing (such as $9.11 > 9.9$). The latter ability is essential for tackling complex arithmetic and mathematical problems and serves as a foundation for most reasoning tasks, but previous work paid little attention to it or only discussed several restricted tasks (like integer addition). In this paper, we comprehensively investigate the \textbf{numerical understanding and processing ability} (NUPA) of LLMs. Firstly, we introduce a benchmark covering four common numerical representations and 17 distinct numerical tasks in four major categories, resulting in 41 meaningful combinations in total. These tasks are derived from primary and secondary education curricula, encompassing nearly all everyday numerical understanding and processing scenarios, and the rules of these tasks are very simple and clear.
Through the benchmark, we find that current LLMs fail frequently in many of the tasks. To study the problem, we train small models with existing and potential techniques for enhancing NUPA (such as tokenizers, PEs, and number formats), comprehensively evaluating their effectiveness using our testbed. We also finetune practical-scale LLMs on our proposed NUPA tasks and find that 1) naive finetuning can improve NUPA a lot on many but not all tasks, and 2) surprisingly, techniques designed to enhance NUPA prove ineffective for finetuning pretrained models. We further explore the impact of chain-of-thought techniques on NUPA. Our work provides a more detailed and comprehensive understanding of NUPA in LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the empirical abilities of LLMs to solve numerical reasoning tasks of varying complexity. It proposes a benchmark, called NUPA, incorporating several different number representations (integers, fractions, etc) and reasoning tasks (arithmetic, comparisons, etc). Its experiments show that several well-known LLMs are prone to errors on this benchmark, particularly as the digits get larger. The paper also analyzes how factors like tokenization, data formats, and finetuning affect performance on NUPA.

### Strengths
1. The paper does a good job of broadening the evaluation of numerical reasoning from integers—which is often the focus in these kinds of studies—to more general classes of numbers. In general, there are a lot of experiments here, including several tasks and language models. The claim that models struggle with basic numerical understanding is well supported by the results. 
2. The discussion on tokenization is quite interesting, surprisingly few studies that I am aware of consider how tokenization affects numerical reasoning. Although not very surprising, it is nice to have empirical evidence that 1-digit tokenization yields stronger generalization to more complex examples than those in the training set. 
3. The paper goes beyond being purely “descriptive”, it also investigates methods that could *improve* numerical reasoning.

### Weaknesses
1. Numerical reasoning in LLMs is well-studied by now. Yet, the paper lacks a related work section and has very few references to similar studies overall. It is therefore unclear to what extent the insights here are novel. Some of the claims of novelty also come off as overly strong, e.g., the last sentence of the abstract “our work takes an initial step towards understanding and improving NUPA [numerical understanding and processing ability] of LLMs.” I include a short list of relevant references below; however, I would suggest the authors to perform a more comprehensive literature review so that they can properly situate their work.
2. The paper is somewhat poorly written. First, there are many grammatical errors in this text (e.g., l62-3, l123). Second, many parts lack explanation or justification. For instance, it is not explained how the random tokenizer works. The technique appears to be adapted from Sathe et al. (2024), but that is a recent and probably not very well-known paper. On another note, random tokenizers were not introduced by that paper as suggested in the text; see for instance Kudo (2018). Another part that is unclear to me is the section on positional encodings. It is not explained what is meant by length-agnostic and length-related rules. It also doesn’t contextualize the methods studied—RoPE and Alibi. What are they and why are they studied? Is there some plausible explanation for why you observe the results you do?
3. The paper is experiment-driven; there is no underlying theory guiding the selection of tasks or techniques for improvement. The scope is also very broad—the paper attempts to do many things at once. While that may be seen as a strength, I feel that it comes at the sacrifice of depth of analysis and clarity. I would suggest the authors to construct a more focused narrative and provide justifications that are grounded either in previous work or theory.
4. The paper lacks important statistical reporting like confidence intervals or p-values.
5. As a minor additional note, Figure 2 (and the similar figures in appendix) is quite hard to parse. There is a lot of information and it is difficult to distinguish the models since some of the colors are rather similar. It is also confusing that the results for the finetuned model are here since finetuning is discussed much later in the paper.

### Questions
How do you get ground truth reasoning traces for RFFT?

### Soundness
3

### Presentation
2

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
This paper evaluates language models on tasks involving numerical and arithmetic reasoning. The authors introduce a test suite with 17 numerical tasks (e.g., addition, subtraction, modulo, max, min, and digit retrieval) across four numerical representations, using it to evaluate nine language models. The paper also analyzes the impact of tokenization, positional embedding type, and data format on a model’s ability to perform addition and multiplication. Finally, the authors assess whether fine-tuning, with and without chain-of-thought, can improve LLaMA-3 8B’s performance.

### Strengths
- The evaluation procedure is well-structured and comprehensive.
- Some tasks in the evaluation suite offer useful insights into model failure modes.

### Weaknesses
 - Attribution and discussion of previous work is extremely poor:
    - Notably, a discussion of the related work is missing. The the proposed evaluation suite, the design choices for it, and the results obtained should be discussed in light of previous studies that evaluated and analyzed the performance of language models on task involving numerical reasoning [e.g., 1,2,3,4,5,6]
    - The authors fail to reference papers that introduce methods that they directly adopt: chain-of-thought prompting was introduced by Wei et al. [7], and LoRA was proposed by Hu et al. [8]. Both citations are missing.
- Although the authors study the impact of tokenization on the performance of a model that they train form scratch, a discussion of how the tokenization of the pre-trained models evaluated might affect the results is missing. Additionally, here again, any reference to previous work that studied the impact of tokenization on numerical reasoning [e.g., 9] is absent.
- Some presentation/clarity issues:
    - Presenting the fine-tuning results in Table 2 is confusing, as they are discussed only much later in Section 4.
    - Figure 2 can be improved, especially in the choice of color for the LLaMA models, which are quite hard to distinguish in the bar plot.
    - Line 512.5: I understand that rule-following fine-tuning is introduced by Hu et al., but further details about the fine-tuning process (potentially in the appendix) would be helpful.
    - The use of negative \vspace is excessive, resulting in cramped spacing between tables/figures and text, especially on pages 7 and 9.

### Questions
The lack of discussion on previous work is a significant drawback. I would be willing to reconsider my score if this is addressed in the paper.

### Soundness
2

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
Designs a comprehensive benchmark for number understanding, covering four different number presentations (e.g. integers) and 17 tasks (such as multiplication). The benchmarks allows for testing a range of different numerical understanding skills, at different levels of difficulty (through longer numbers in terms of digits for example). The authors do a comprehensive range of experiments on the benchmarks, evaluating off-the-shelf LLMs on it, as well as training their own models to understand the effects of aspects of common LLMs (such as tokenizers) and existing methods for improving numerical understanding (such as representing in reverse order). The findings are the many models still struggle in elementary understanding tasks, especially for larger numbers. Moreover, the existing tricks to deal with this don't fully mitigate the problems.

### Strengths
This paper has the potential to be an important contribution to the field, for two main reasons:

- Great benchmark proposed with a comprehensive range of tasks and difficulty levels, and good metrics for evaluating performance

- Excellent coverage of experiments. Testing comprehensively many aspects relevant to this problem, like different types of generalisation, different architectural changes, different existing models, effects of scale, existing methods for improving numeric understanding, prompting, etc. I would be very interested in these results, if the weaknesses below could be addressed.

### Weaknesses
Unfortunately, the presentation is lacking and it's very hard to interpret the results because of missing details on how models are trained.

**Main weaknesses**
- There is no information at all in the paper about how the models are trained for the experiments in section 3.1 and 3.2. How much examples do you train on? How long? Optimizers, hyperparameters, repeats, etc.? How do you define in and out-of-domain? It's very difficult to interpret the results of this experiment without knowing more. For instance, the lack of information on the training dataset size and composition makes it impossible to assess whether the models are overfitting to the training data or genuinely learning numerical concepts. The absence of details on the optimizer and learning rate schedule further hinders the reproducibility of the experiments and makes it difficult to compare the results with other studies. The number of training repeats and the method for selecting the best checkpoint are also crucial for understanding the robustness of the findings.

- The paper needs substantial rewrites, and will probably benefit from corrections by someone whose first language is English or by using an LLM to revise and point out mistakes.

- There is a long discussion of things like the relevance of integers and how fractions arise (section 2.1 and 2.2), but this seems unnecessary and the space could be used instead to represent the results better. For example, Figure 2 presenting the main results in the text is very small and almost impossible to read without zooming in 200%. The colors used are also hard to distinguish. I would suggest shortening section 2.2 and almost entirely removing 2.1 and use the space to represent the results better. Especially because this is the great part of this paper, you have so many results but you do not discuss the details of the experiments and present the results in a way that are hard to follow.

- Some results are interpreted in ways that are not substantiated by the evidence found. For example, line 298 to 309; I disagree that this result means the model does not understand the concept of digit. The fact that it becomes harder to return the right digit for longer numbers actually hints at something else going on that might be more related to the model's inherent difficulties with retrieving something from a position in longer sequences, which has nothing to do with it's understanding of the concept digit. I also disagree that this points to case-based reasoning, because again it might be due to some aspects of its architecture. Additionally, the fact that models of different sizes show the same performance on a task does not necessarily indicate the performance depends on the training approach over size, it might also depend on architecture.

- There is no section on related work, and the authors say in the beginning of section 2 that they will show limitations of prior benchmarks while discussing the coverage of their own, but this does not happen. This makes it difficult for the reader to place this contribution w.r.t. existing literature.

**Minor points**

- Would be great to already get some more concrete information in the abstract (what probability of error? which 3 factors influence it?). Or at least in the intro some more concrete info.

- Figure 4 and 5: it's unclear what's on the X-axis (though one can assume it's training steps), and also unclear what D6 to D10 refers to. It's also unclear what is in-domain and what is OOD without reading the text.

- *"These types of errors are a major cause of hallucinations when dealing with math, reasoning, and data analysis tasks, as the model presents seemingly correct problem solving approaches but ultimately produces incorrect results"* -> this statement requires a citation

- line 117 to 119; a discussion on the innateness of integer understanding seems somewhat out of scope for this work and not too relevant to the contribution.

- Cite / reference openai chatgpt when using it line 135

- One approach that seems missing is few-shot examples, which might significantly boost performance for all models. Not just because they might learn from the examples, but because they get primed on the output format required.

### Questions
Main questions is can you give details on how the experiments that use training of fine-tuning are done, and what in-domain and out-of-domain refers to (what examples do you hold out for this)?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work introduces a benchmark suite of "numerical understanding and processing ability" (NUPA) tasks for transformer-based LLMs. The task suite separates numeracy from potentially confounding logical reasoning problems, and presents a variety of numerical formats. Additionally, various tricks are explored to improve LLM performance in these numeracy tasks; no silver bullets.

### Strengths
It is clear that some thought has gone into curating the benchmark tasks and justifying their inclusion. Even though I do not personally agree with some of the justifications and normative statements made, I believe that this sort of conscientious effort to justify a benchmark is commendable. I rate this work highly in terms of integrity, quality of presentation, and clarity.

I particularly appreciated the authors' investigation of CoT, as it is generally interesting to understand whether "prompt-level" interventions have a lot of room for improving performance on complex tasks. A recent (contemporaneous, so not factoring into my decisions) paper by Apple on GSM8k qualifying LLM performance as memorisation seems to agree with the findings of this work that numeracy abilities do not appear to scale; potentially a way to frame and situate this work with respect to the broader discourse on generalisation and understanding in LLMs.

### Weaknesses
I have no issues with the benchmark and evaluation. I do not currently find the conceptual motivations and wrapping compelling; I could be convinced otherwise for each of these with the help of citations, or of better arguments, and I would be happy to raise my score accordingly.

1. I am unconvinced that numeracy in LLMs is a problem in need of a solution. First, surely there is a citable source for LLM inadequacy for numeracy. Second, even if they were terrible at numeracy, the onus is on the authors to convince the reader that this a problem worth caring about, for at least two obvious reasons: 1) all of these tasks are already trivially done by a calculator or a python program, and 2) commercially available LLMs can probably do alright at numerical tasks indirectly via code-generation and execution. As it stands, it reads as if the authors are insisting that this is a problem deserving of attention --- I'm sure it could be, but this argument can be better made.

2. I am unconvinced that numeracy in LLMs is a problem in search of deeper understanding. Consider that "How many r's in strawberry" is a meme that normal people know about; the idea that tokenization impairs the ability of transformers to reason at a letter-, digit-, or word-unit level is well-digested. So when the authors claim that the weakness of LLMs at digit understanding is surprising (line 298), I find this a bit sensationalist and not grounded with respect to a broader and basic level of discourse around the capabilities of LLMs.

3. I am unconvinced of the normative rationales supporting the benchmarks, which seem ad-hoc. Here is an example: the authors claim that multiplication (not a particular algorithm) is O(L^2) in the length L counted in digits (of presumably both inputs; line 169), and take this as justification that models ought to find multiplication difficult. This doesn't hold up to armchair introspection: lookup is O(1), and we have all learned our times tables as children. The competent-human process of mental multiplication is mostly a sequence of lookups along with additive de/recomposition, so the real exponent is probably less than 2. This is a jarring oversight when contrasted with the effort with which the authors bring up cognitive and developmental psychology (lines 116 to 127), recasting what I assumed was a scholarly inclusion as a kind of checklisting exercise. There are other unsupported normative claims about what a good benchmark ought to encompass, such as "NUPAs are necessary and expected to learn by LLMs [sic]" (line 114), "any student who has completed primary and secondary education should be able to accomplish them" (line 160), and "for most practical tasks involving numbers (like arithmetic or math tests), all we care about is whether the answer is right, and there is no significant difference between being almost right and being completely wrong" (line 228). While I understand the importance of establishing normative standards to justify a benchmark with respect to, I find it hard to believe as a reader that the authors have the expertise and authority to do so.

4. I am unconvinced that this is worth "taking seriously"; let us suppose that everyone agrees that NUPA in LLMs is a problem worth solving and that improving on this benchmark is the way to solve the problem. We know beforehand that transformers have problems with NUPA due to tokenization, and now the finding of this paper is that fine-tuning and CoT as tricks don't solve the problem. There are many graphs in this paper that must have taken a fair amount of compute to obtain; is it worth it if everyone decided to run similar tests, or fine-tune with respect to the NUPA suite? I don't mean this in an unnecessarily antagonistic way, but one concerned with scientific interest and downstream impacts; if LLMs are just bad at numeracy for architectural or structural reasons as the current evidence suggests, could the introduction of a benchmark be inviting high-compute low-innovation approaches to the problem, and does the problem even merit this kind of resource investment?

### Questions
1. Why is it important that LLMs be good at NUPA when we python, and even LLM code-generation that can write python to deal with NUPA? I.e. Why is this a worthwhile problem, and who says it is?

2. To what extent do your findings suggest that the issue is architectural or to do with tokenization? To the degree that this is the case, to what extent do your findings suggest that the issue is paradigmatic rather than technical?

3. Is it necessary to provide normative justifications for the benchmarking suite? If so, I would like to know why, because I think the paper could be stronger if the benchmarking tests were presented matter-of-factly, without detours.

4. Experimentally, how much compute (as an estimate) was used throughout?

### Soundness
2

### Presentation
2

### Contribution
2
