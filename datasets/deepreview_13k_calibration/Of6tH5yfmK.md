# Self-Control of LLM Behaviors by Compressing Suffix Gradient into Prefix Controller

- Decision: Reject
- Avg Score: 5.33
- Scores: 6, 5, 5

## Abstract
We propose \method, an inference-time model control method utilizing gradients to control the behavior of large language models (LLMs) without explicit human annotations. Given a desired behavior expressed in a natural language suffix string concatenated to the input prompt, \method computes gradients of the LLM's self-evaluation of the suffix with respect to its latent representations. The gradients are used to directly control the auto-regressive generation process towards desired behaviors, which eliminates human supervision, achieves precise and transparent control, and offers on-the-fly adaptability. To further enhance efficiency, we introduce \prefix, a compact module that encapsulates the learned representations from gradients into a \pc, facilitating efficient inference-time control with no latency compared to the original model and allowing control for multiple behaviors simultaneously. Our experiments demonstrate \method's efficacy across multiple domains, where it improves over SOTA for \textbf{8.3\%} in detoxification, \textbf{3.1\%} in truthfulness enhancement, \textbf{4\%$\sim$10\%} in controlling on emotion tones, and \textbf{48.2\%} in privacy protection, i.e., completely remove privacy leakage issue. Additionally, we demonstrate that \method can be used for data synthesis and to improve reasoning abilities. Our interactive demo and code are available at \href{https://colab.research.google.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces SELFCONTROL, a novel approach to control LLMs behavior without requiring explicit human annotations. The method's key strength lies in its ability to leverage the model's own self-evaluation capabilities through suffix gradients, making it more efficient and adaptable than traditional control methods. The author also introduces SELFCONTROL-Prefix for improving the running time of SELFCONTROL while maintaining its performance. The experiments across multiple preference setting demonstrates the effectiveness of the methods.

### Strengths
1. The paper is well-written and easy to follow.
2. The idea of using gradients to guide learned representations for preference control is novel and interesting, and the design choices made in Section 3 are clear.

### Weaknesses
1. The performance of the method relies on the model's original performance; however, it's not clear what the impact of different base models is. It would be beneficial to compare the performance (Table 2, for example) using the base model instead of a model with instruction fine-tuning, and to examine whether the improvement still persists.
2. The mathematical foundation of the method is not very sound. The objective function has potential pitfalls since the model tries to increase the margin between logP+ and logP_. Ideally, we want the model to increase logP+ while pushing down logP_; however, the model can also push down both quantities but push down logP_ by a larger amount. This is very similar to the objective function proposed in DPO [1], although the update target is different. As pointed out in [2], it's not very problematic if the goal is to train a reward model, but it would be problematic if we still want the trained model to serve as a generator, which is the case in this paper. To illustrate this point, consider a restricted word space where we only have "Yes," "No," and "Nope." Assume originally $P_\theta(<\text { next-token> } =\text { Yes } \mid \text { suffix, output, } H_{\text {input }}) = \frac{1}{3}$, $P_\theta(<\text { next-token> } =\text { No } \mid \text { suffix, output, } H_{\text {input }}) = \frac{1}{3}$, $P_\theta(<\text { next-token> } =\text { Nope } \mid \text { suffix, output, } H_{\text {input }}) = \frac{1}{3}$, where the margin is 0. One potential desirable output based on the current objective is $P_\theta(<\text { next-token> } =\text { Yes } \mid \text { suffix, output, } H_{\text {input }}) = \frac{1}{2}$, $P_\theta(<\text { next-token> } =\text { No } \mid \text { suffix, output, } H_{\text {input }}) = 0$, $P_\theta(<\text { next-token> } =\text { Nope } \mid \text { suffix, output, } H_{\text {input }}) = \frac{1}{3}$. However, with the same margin, it's also possible that $P_\theta(<\text { next-token> } =\text { Yes } \mid \text { suffix, output, } H_{\text {input }}) = \frac{1}{3}$, $P_\theta(<\text { next-token> } =\text { No } \mid \text { suffix, output, } H_{\text {input }}) = 0$, $P_\theta(<\text { next-token> } =\text { Nope } \mid \text { suffix, output, } H_{\text {input }}) = \frac{2}{3}$. Now the model is actually updating in the opposite direction. It's not clear how the current method prevents this without any further constraints.
3. Regarding performance: Comparing Tables 2 and 3, the improvement of the proposed method compared to even system prompting is marginal, despite requiring longer search and running time. This raises the question of whether other baselines, like better prompting techniques such as Tree of Thoughts [3] or self-refinement methods like RISE [4], could be more efficient and effective.
4. In terms of generalizability, the impact of the method could be largely boosted if evaluated on reasoning tasks like GSM8K [5] and MATH [6], using a suffix string targeted at correctness, for example, "Your response was correct. Yes or No?"

### Questions
1. In equation (1), should the input on the left-hand side be H_input?
2. At the beginning of Section 3.2, the authors mention that SELFCONTROL can efficiently search for proper input representation. Can this be quantified? If I understand correctly, for each new query, SELFCONTROL requires multiple rounds of sampling and gradient computation, which should be very inefficient compared to traditional methods that only require a couple of forward computations.
3. Is SELFCONTROL-Prefix a way to solve the inefficiency issue mentioned in question 2? Are we training one adaptor from a dataset generated by SELFCONTROL of multiple queries? If so, SELFCONTROL-Prefix seems will sacrifice some performance as it is a general adaptor instead of SELFCONTROL running query-specific searches. Then why, in Table 2, does SELFCONTROL-Prefix have better performance in some cases?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors address the practical difficulties of aligning large language models by proposing two inference time approaches to alignment – an iterative method that allows the LLM to assess and refine its own responses, through a prompt suffix mechanism (SELFCONTROL); and a PREFIXCONTROLLER module which is trained on data generated by the first method, and which can be incorporated into the LLM with little additional inference cost. Through a variety of benchmarks the authors demonstrate the ability of these methods to generate state of the art results in control tasks related to detoxification, truthfulness, emotional tone and privacy.

### Strengths
This is a vital area of research, as LLMs see continued wide-spread adoption, despite an alarming lack of clarity regarding their capabilities and limitations.  This paper succinctly motivates the need for cheap, reliable, scalable solutions, highlighting the deficiencies in current methods – particularly a lack of transparency and the need for extensive human intervention. Against this backdrop, the methods they propose seem like a welcome addition to the field. There is a nice progression from the instance-level SELFCONTROL method to the more general, lower-cost PREFIXCONTROLLER method, and both methods have been evaluated against a range of different tasks. The idea of computing suffix gradients to steer the model is interesting.

### Weaknesses
I have three concerns with the paper as it stands, two major and one relatively minor. My major concerns are to do with the method proposed, and the evaluation of the method:  

1. The SELFCONTROL method seems to suffer from several systemic weaknesses.  
 a. _Number of tokens per query_: to carry out steps 3 and 4 (in figure 2), the original prompt becomes augmented with the model’s output and the suffix string – this could be a substantial increase in the number of tokens the model needs to process.  
 b. _Number of query/responses required_: The algorithm in lines 245-249 indicates that each iteration requires K responses. (I failed to spot in the paper either the value of K used, or the number of iterations typically required for SELFCONTROL to reach its goal.) When combined with the increased volume of tokens, the need to query the model K*num_iterations times seems like it could become alarmingly expensive. (The running time comparison in Table 4 hints at this, with SELFCONTROL taking almost ten times as long as the uncontrolled approach.)  
 c. _Specialisation of the suffix string_: Unless I misunderstand the idea, SELFCONTROL only allows control for one task at a time; eg you can steer the model towards being happy, or you can steer it away from toxic language, but you can’t do both at the same time. This seems like a fatal flaw, since an aligned model needs to satisfy several constraints at once (eg detoxification and privacy protection). I may have misunderstood this – the description of Figure 2 states that “suffixes can be combined”, but I got the impression from the rest of the paper that it was just the PREFIXCONTROLLER that enabled this?  
 d. _Unclear utility_: As acknowledged by the authors, the ablation in Table 7 reveals that replacing the suffix gradients with random vectors can actually improve performance for some models. While it was brave of the authors to leave this result in the paper, I felt that it warranted a much deeper analysis, as it seems to cast doubt on the heart of the method.   

(I suspect the first three problems, above, motivated the progression to the PREFIXCONTROLLER method, though the paper doesn’t make this explicit. I think it would read better if these limitations were acknowledged.) 

2. Evaluation: the authors have tried to address a wide range of topics – language detoxification, privacy protection, emotional control and truthfulness. I understand the need to consider all these tasks, but evaluating any one of these involves a lot of work, a lot of design decisions, and a lot of subjectivity – what dataset to use, how to form the experiment, how to evaluate the results – with so many pieces in play, I’m left questioning how meaningful the final results really are.  For some concrete examples:  
 a. The task for _control on privacy_ is to avoid generating email addresses. This doesn’t feel like a useful test: there are far subtler and more dangerous ways of breaching privacy than revealing an email address, and checking a model’s output for email addresses is a simple task which can be accomplished with a regex. Success at this narrow task doesn’t seem to imply trustworthiness in the wider privacy domain.  
 b. _Controlling for emotional tone_: I appreciate the numbers need to come from somewhere, but a GPT-3.5-turbo calculated score alone isn’t a guarantee of desirable behaviour. Tables 20-28 illustrate this – there are many cases where the model’s output seems to have changed completely, and diverged from what would be expected / desired. If the output achieves the desired emotion, but completely misses the desired content, then there is a problem with the method that the metrics won’t show.  
 c. The PREFIXCONTROLLER is _composable_, to control for multiple behaviours at once, but there seems to be very little evaluation of this beyond the middle plot of Figure 4. At the very least, *it seems essential to show that a model can score highly for both privacy and detoxification simultaneously* using this method.  

Overall, I wonder if it would have been possible to focus on fewer areas of application, but do them more thoroughly?

3. Finally, my minor concern is with the presentation of the paper. On a very superficial level, there are quite a few typos. Less superficially, there is an enormous amount of content here, making it hard to focus on the key contributions. Sections 4.5 and 4.6, for instance, feel like they have been squeezed in. (This also means that key information is missing, or hard to find – for example, how many iterations does SELFCONTROL take? I would have loved to have seen a worked example showing the progression through the iterations.) The appendices feel like a data dump from many different investigations. I’d maybe encourage the authors to be slightly more ruthless in what they choose to include.

### Questions
The maths reasoning examples in the appendix seemed particularly strong - I wondered why they were relegated to the appendix, rather than, say, the privacy results.

_Very_ minor:
- are figures 10 and 11 the same?
- the link to the HH-dialogue examples in F2 is broken

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
Summary: The authors propose a method to control LLM behavior at inference time, through the use of gradient-guidance at the latent representation level. The authors show successful control and improved metrics over several tasks, such as detoxification, privacy, and emotional control.

### Strengths
The work is generally well-structured, and the results seem compelling. The authors show the flexibility of their approach in good set of tasks, such as detoxification, privacy protection, and emotional control.

### Weaknesses
The paper has several ambiguities that limit its applicability. The abstract lacks a clear problem statement, making it unclear what specific issue is being addressed. There is insufficient justification for why prompt engineering cannot be applied in some benchmark tasks, and the lack of statistical significance in the reported results further weakens the conclusions, and some results in emotional control underperform without proper explanation.

- Abstract: it would be useful to find a problem statement. The authors explain what is proposed, but it is quite out of context, and it is not immediately obvious what problem is being solved.
- The introduction and comparison with prior work focus on several control techniques. It is nonetheless not immediately clear why prompt engineering can’t be used in several of the proposed benchmark tasks (e.g. sentiment control).

- _Section 2_:
  - The statement “_We start from the point of view that gradients are naturally engineering model representations_” should be expanded and supported by, at the very least, a logical argument, if not citation(s) and appropriate evidence. As is it does not make sense to me.
  - _“However, they generally do not apply to our method. Similar to (…)”,_ this statement is quite disagreeable. Even by forcing an LLM into a yes/no answer, the statistics of the next work token prediction are still subject to the fallacies of the model’s training, the shortcuts in the data, and other sources of bias. The authors should better explain their position.

- _Section 3.2:_
  - _“Each learned PrefixController works (…) model behaviours”_ This is not clear. Do you need to train a different adapter for each control independently? so the amortized cost of training only offsets the rounds of iteration necessary to run the guidance algorithm for each prompt? – if so this seems like a costly trade-off. Any thoughts on conditional, prompt independent, versions of the same?

- _Section 4:_
  - The tables should report standard deviation/errors. It is unclear whether the results hold any statistical significance.
  - Table 4, SelfControl_prefix: The authors should expand on the training cost necessary to achieve the inference time advantages reported.
  - Emotional Control: the authors report a diverse range of results, some of which severely underperform. It would be worthwhile to expand on why that is.
  - Ablating sub-modules: _“ (…) This shows the efficacy of the framework (…) be able to elicit desired behaviors.”_ What are the causes and implications of this statement?

- Other typos and mistakes:
  - “, which has almost no latency compared to the original model greatly outperforms …”
  - “optimize the ~~its~~ parameters”
  - etc.

### Questions
- Abstract: it would be useful to find a problem statement. The authors explain what is proposed, but it is quite out of context, and it is not immediately obvious what problem is being solved.
- The introduction and comparison with prior work focus on several control techniques. It is nonetheless not immediately clear why prompt engineering can’t be used in several of the proposed benchmark tasks (e.g. sentiment control).

- _Section 2_:
  - The statement “_We start from the point of view that gradients are naturally engineering model representations_” should be expanded and supported by, at the very least, a logical argument, if not citation(s) and appropriate evidence. As is it does not make sense to me.
  - _“However, they generally do not apply to our method. Similar to (…)”,_ this statement is quite disagreeable. Even by forcing an LLM into a yes/no answer, the statistics of the next work token prediction are still subject to the fallacies of the model’s training, the shortcuts in the data, and other sources of bias. The authors should better explain their position.

- _Section 3.2:_
  - _“Each learned PrefixController works (…) model behaviours”_ This is not clear. Do you need to train a different adapter for each control independently? so the amortized cost of training only offsets the rounds of iteration necessary to run the guidance algorithm for each prompt? – if so this seems like a costly trade-off. Any thoughts on conditional, prompt independent, versions of the same?

- _Section 4:_
  - The tables should report standard deviation/errors. It is unclear whether the results hold any statistical significance.
  - Table 4, SelfControl_prefix: The authors should expand on the training cost necessary to achieve the inference time advantages reported.
  - Emotional Control: the authors report a diverse range of results, some of which severely underperform. It would be worthwhile to expand on why that is.
  - Ablating sub-modules: _“ (…) This shows the efficacy of the framework (…) be able to elicit desired behaviors.”_ What are the causes and implications of this statement?

- Other typos and mistakes:
  - “, which has almost no latency compared to the original model greatly outperforms …”
  - “optimize the ~~its~~ parameters”
  - etc.

### Soundness
2

### Presentation
3

### Contribution
1
