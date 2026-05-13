# Re-Reading Improves Reasoning in Language Models

- Decision: Reject
- Scores: 5, 5, 8

## Abstract
To enhance the reasoning capabilities of off-the-shelf Large Language Models (LLMs), we introduce a simple, yet general and effective prompting method, \model, i.e., \textbf{Re}-\textbf{Re}ading the question as input. Unlike most thought-eliciting prompting methods, such as Chain-of-Thought (CoT), which aim to elicit the reasoning process in the output, \model shifts the focus to the input by processing questions twice, thereby enhancing the understanding process. Consequently, \model demonstrates strong generality and compatibility with most thought-eliciting prompting methods, including CoT. Crucially, \model facilitates a "bidirectional" encoding in unidirectional decoder-only LLMs because the first pass could provide global information for the second pass. We begin with a preliminary empirical study as the foundation of \model, illustrating its potential to enable "bidirectional" attention mechanisms. We then evaluate \model on extensive reasoning benchmarks across 14 datasets, spanning 112 experiments, to validate its effectiveness and generality. Our findings indicate that, with the exception of a few scenarios on vanilla ChatGPT, \model consistently enhances the reasoning performance of LLMs through a simple re-reading strategy. Further analyses reveal \model's adaptability, showing how it can be effectively integrated with different LLMs, thought-eliciting prompting, and ensemble strategies.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposed a simple yet interesting prompt, in which the question is repeated.  Experiments conducted on a series of reasoning benchmarks serve to underscore the effectiveness and generality of the proposed prompt.

### Strengths
The prompt proposed in the paper is interesting and simple enough, and demonstrated to be able to effectively improve the reasoning performance of LLMs. The presentation is clear and easy to follow.

### Weaknesses
The experiments conducted in the paper mainly compare the proposed method with vanilla COT with backbones ChatGPT and davinci-003 (Llama-2 is used for another reasoning task). But there have been lots of COT prompts recently, and other LLMs, which have not been evaluated in the paper. Even for the conducted experiments, the proposed method is not always useful for performance improvement, which can not fully support the theoretical analysis in the paper. To me, it's more suitable for a demonstration paper.

### Questions
In the experiment, why the backbone LLMs were divided into two groups for two sets of reasoning tasks, i.e. ChatGPT and davincci-003 for commonsense reasoning and symbolic reasoning, and Llama-2 for arithmetic reasoning? I think you should compare the competing methods with different LLMs in the same group of reasoniing tasks.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes RE2, a simple modification to improve the reasoning ability of large language models. As claimed in the paper, the existing decoder-only model can not well capture the back-and-forth interactions between different stages during reasoning. The authors simply repeat the question first before solving it. In this way, as claimed, earlier tokens can be aware of later tokens in the question. This approach are evaluated in several benchmarks including arithmetic, commonsense and symbolic. Many ablation studies are done to support the effectiveness of proposed RE2.

### Strengths
- To enable back-and-forth interaction during reasoning in large language models is a reasonable motivation, since a single-pass forward process in decoder-only architecture may not be sufficient for the complex reasoning process.

- The experiments are well designed and complementary, supporting the proposed repeated question prompts from several perspectives.

-  The paper is well organized and very easy to follow. I enjoy reading the paper.

### Weaknesses
 - The authors connect the repeating question prompts with human's thinking process, which is a casual argument without justification to back this up. It is hard to be convinced this is how and why the repeated prompts help.

- Repeating the question needs a question assumed to be there. It seems not to be generalizable for many other scenarios where it is not simply a Q-A setting, such as a multi-round conversation. Instead, approaches like chain-of-thoughts are in the solving stage, i.e., they can be used in any scenario.

- In figure 2,  RE2 makes the low-complexity questions (<=3) worse in the GSM benchmark. However, the other arithmetic benchmarks (except GSM) in table1 5 6 are mostly in low complexity too. These two results are contradict. Why is this the case?

### Questions
- For most datasets in table1 and table2, it seems RE2 improves vanilla more than CoT, but the case is the opposite in the symbolic reasoning. Is there any interpretation of this difference? 

- From table1 and table2, RE2 would almost always improve davinci-003 but seems pretty random in ChatGPT-vanilla (half better, half worse). Why do they behave in such a different way?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a simple prompting strategy RE2 which re-reads the question multiple times. The authors demonstrate the effectiveness of the RE2 on a set of reasoning benchmarks either in the vanilla setting or in combination with other techniques including CoT, PS, PAL and self-consistency. They also conducted ablation studies on the times of re-reading, complexity of questions, and different re-reading instructions.

### Strengths
1. The biggest strength of the paper to me is the simplicity of the method, making it easily adoptable by the wide research community.
2. The paper is very comprehensive in reasoning datasets covered, models evaluated on, baselines compared against and ablations conducted.
3. The results are mostly positive against the baselines for all the datasets and models studied.

### Weaknesses
1. The gains are more pronounced in weaker models (davinci-003 vs ChatGPT, Llama-2-13B vs 70B). This raises the question of the scaling behavior of the proposed RE2 method.
2. For ARC tasks evaluated on ChatGPT, RE2 shows negative or neutral-ish results in both the vanilla and CoT settings. This is concerning, and worth more investigations to understand why.
3. A lot of the gains in the paper are within the range of 2%, and it is unclear whether these results are just noise since the paper didn’t provide any way to quantify the standard deviations.

### Questions
1. Typo in the last sentence of the abstract: “though-eliciting prompting…”.
2. The claim of “LLMs to understand the input in a bidirectional manner” is misleading: it is unclear to me where the bidirectional attention from the model comes from. Neither did the authors explain what exactly they mean by “bidirectional”.
3. The authors claim that LLMs gain deeper insights/understanding with RE2. However this claim is not supported by any evidence at all. It can be totally misleading. For instance, re-reading 3 times is not better than 2 times. It is possible that in pretraining corpus, there is such data which resembles the re-reading 2 times behavior, giving an edge to RE2.
4. Ideally, RE2 should work beyond Reasoning given that humans don’t do re-reading on reasoning tasks. Covering tasks beyond Reasoning would certainly make the paper much stronger.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
