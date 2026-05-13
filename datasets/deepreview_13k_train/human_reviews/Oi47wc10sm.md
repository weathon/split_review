# Programming Refusal with Conditional Activation Steering

- Decision: Accept
- Scores: 8, 6, 8

## Abstract
LLMs have shown remarkable capabilities, but precisely controlling their response behavior remains challenging.
    Existing activation steering methods alter LLM behavior indiscriminately, limiting their practical applicability in settings where selective responses are essential, such as content moderation or domain-specific assistants.
    In this paper, we propose Conditional Activation Steering (CAST), which analyzes LLM activation patterns during inference to selectively apply or withhold activation steering based on the input context.
    Our method is based on the observation that different categories of prompts activate distinct patterns in the model's hidden states.
    Using CAST, one can systematically control LLM behavior with rules like ``if input is about hate speech or adult content, then refuse'' or ``if input is not about legal advice, then refuse.''
    This allows for selective modification of responses to specific content while maintaining normal responses to other content, all without requiring weight optimization.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents Conditional Activation Steering (CAST) as a novel framework for enabling selective control over large language model (LLM) responses by dynamically applying refusal behavior to specific prompt categories. Traditional activation steering techniques alter model behaviors across all inputs, but CAST introduces a “condition vector” that enables selective behavior modification based on context. This framework allows for fine-grained, context-dependent refusal responses—such as rejecting hate speech but responding to benign prompts—without requiring weight optimization. The authors claim CAST contributes a valuable tool for alignment, moderation, and domain-specific applications where selective behavior control is essential.

### Strengths
* Novel Approach: CAST represents a unique advancement in activation steering by adding the ability to conditionally refuse specific categories of prompts. This method is valuable in fields like content moderation and personalized assistant behavior where indiscriminate refusal would limit utility.
* Empirical Validation: Extensive experiments demonstrate CAST’s efficacy in refusing harmful prompts without affecting benign responses across multiple LLMs. The results indicate robust behavior modification and reliable model conditioning under various categories.
* The authors note they will release open source code, which will be valuable for other researchers interested in using these methods

### Weaknesses
 * Figure 6a -- why is conditions triggered the 'success' metric here? Shouldn't it be something like F1 score (for aggregating true positives, false positives, etc. to show performance at each data scale)
* Why is duality of the comparison direction highlighted? Isn't it obvious that flipping the comparison direction and using a threshold of (1-c) yields the same decision boundary but flips the decision? I might be missing something here.
* The main text doesn't seem to explain well how false and true positives for refusals are automatically assessed (e.g. when doing grid search over hypers (like layer and refusal threshold)). A clearer explanation of this would be helpful
* I may have misread, but I think the only quantitative results are in Table 2. 3 models are listed, but table 1 references aroudn 8 models used. Where are results for the other models? In addition, the pie chart visualizations (e.g. Figure 7) are great, but a quantitative summary would be very useful.
* Complexity in Multi-condition Settings: The paper discusses multi-conditioning but does not fully examine potential trade-offs when many conditions are combined, especially when conflicting conditions arise. Further clarification on how to manage or prioritize conditions could enhance the method’s applicability in complex real-world scenarios.

### Questions
* Why was PCA used to compute condition and behavior vectors, as opposed to fitting a classifier (e.g. SVM or logistic regression) which would explicitly fit a separating hyperplane between the classes (and thus moving in the direction of that boundary would directly correspond to steering the behavior in a desired direction)? If I understand correctly, the PCA is computed on the matrix containing both positive and negative activations, and the authors assert the direction of maximal variance (first principal component) is the direction that best distinguishes between the positive and negative examples. It isn't quite clear to me how this can be assumed to be true -- an analysis of, e.g., the distribution of coordinates of the positive and negative examples  when projected along this direction would be very useful to see (i.e. that we see a bimodal distribution of coordinates along this direction, such that moving an activation along the direction does correspond to encouraging the behavior)
* What specifically motivated use of tanh for the similarity transformation as opposed to vanilla cosine similarity?
* Multi-conditioning -- since the conditions are combined into one function, how is the appropriate steering vector determined (as presumably a different steering vector would be desired based on which condition activated)

### Soundness
3

### Presentation
3

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
This paper introduces CAST, a technique to perform conditional activation steering. Following prior work, CAST generates behavior vectors that determine the direction in which to steer models to elicit a specific behavior. Next, CAST generates condition vectors that determine the context in which to apply the behavior vectors. By selectively applying the behavior vectors, CAST is able to steer behavior more precisely and under more complex combinations of rules than prior work.

### Strengths
- Introduces the concept of 'condition vectors' as a way to gate which activation vectors are triggered at each step. 
- Thoroughly demonstrates the use of CAST to handle a variety of new conditional behaviors, such as more precise and robust refusal and topic-based refusal.
- Paper is mostly clearly written with well-formatted figures. The setup seems reproducible and is easy to understand.
- Helps extend the idea of activation steering to make it more robust to multiple scenarios.
In summary, the paper introduces a novel technique (reasonable novelty) and demonstrates its robustness (good quality) with clear presentation (great clarity) towards improving the efficacy and usability of activation steering (reasonable significance).

### Weaknesses
These suggestions are minor as the paper itself is well done. That said, I think the paper could benefit from:

**Qualitative understanding of the condition vectors.** The main insight of the work seems to be that you can construct condition vectors in a similar way to constructing behavior vectors. But I'm still not sure how robust these condition vectors are. It would be great if the authors could run an experiment studying the generalization of these condition vectors.
   - For example, you could take the categories described in the paper: health, crime, legal, etc. and ask GPT to generate prompts for them. For each category, there could be two treatments: basic (prompts that use language from the given category and are relevant to the category) and hard (prompts that use language from the given category but are irrelevant to the category, e.g., a prompts that uses legalese without being about legal statements).
   - Then, for each category's condition vector, how robust is it? What's its accuracy under the two treatments? Can you provide some qualitative failure modes of each condition vector? Do the vectors improve if the model itself improves (and therefore its representations improve). Getting a better qualitative and quantitative understanding of the condition vectors seems useful for understanding the limitations of this technique.

**Improved error analysis.** Are the failures in Figure 1 (and the other experiments) a result of a the condition vector not triggering or the behavior vector not robustly modifying the behavior? Please consider conducing an ablation experiment where the behavior vector is manually applied according to an oracle on the harmfulness and report the F1 score / rate of successful refusal. How does this skyline compare to CAST?

**Missing baselines.** Would it be possible in all of the experiments to have a quantitative comparison to a prompting baseline where the model is told to carefully pay attention to the harmfulness and harmlessness of the response in its refuse (or the relevant category, if its a category). My hunch is that improved prompting would somewhat help for the harmlessness / harmfulness category and fail to help for the more complex combinations of rules. I think this comparison to prompting would help showcase the effectiveness of CAST.

I'm not willing to raise my score higher as I don't think there's evidence that activation steering is a scalable direction for controlling models as it doesn't improve with data (see Figure 6a) and in general seems to be clunky to deploy (see L202 - 208), but I think this paper is high quality and definitely should be accepted. Moreover, I still think the authors should consider incorporating the above suggestions as it would strengthen the paper.

### Questions
Typos:
- L365 - 372: shouldn't there be 700 + 500 = 1200 prompts per category? Seems like a typo + please ensure consistency throughout the paper on the exact number

### Soundness
3

### Presentation
3

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
The authors introduce Conditional Activation Steering (CAST) and condition vectors.  They show that refusal behaviors can be invoked conditionally on the context of the prompt allowing for conditional steering.  They test this across several language models up to size 8B and show that their method has fewer false positive refusals on harmless prompts while still maintaining high refusal rates on harmful prompts, demonstrating the effectiveness of the conditional.

### Strengths
1. The method of steering LLM conditionally on the context of the prompt is novel and an important contribution towards practical implementations of activation steering.
2. The ability to chain conditionals is an interesting contribution.
3. The paper is relatively thorough in its test of models within a certain class O(8B).

### Weaknesses
1. All the tested models have less than or equal to 8B parameters.  Testing on larger models would help improve the robustness and confidence in the results
2. (Minor) The harmless/harmful refusals are not tested against enough real-world inputs, like jailbreaks or multi-turn conversations.
3. (Minor) There is no limitations or future work section.

### Questions
The paper is generally well written and was pleasant and interesting to read.  The possibility for conditional steering is exciting with many practical implications.

### Minor
The paper could be improved through some careful revisions to the figures and layouts.   
* Figure 1 is presented too early; its full description is on page 6 while it appears at the top of page 2.  Despite being referenced on page 1, the paper would flow better if Figure 1 were closer to page 6.
* All of the T-SNE plots should consider a different color scheme.  Its very difficult to distinguish the Alpaca vs Sorry-bench dots, especially against the background of a similar color.
* Figure 8c, several pieces of text are too small to easily read
* Figure 9, the label "(c)" is not placed in the top left corner like the previous figures.  The markers are difficult to see (e.g. the start marker).  


### Out-of-scope improvements
While the following improvements would substantially increase the value of the paper, the reviewer recognizes that they can be designated to follow up work and may be out-of-scope for the current paper.
* The methods could be tested with models with > 8B parameters
* The methods could be tested against known jailbreaks (e.g. does the conditional vector for harmfulness still activation on a zero-shot or 1-shot jailbreak?).

### Soundness
3

### Presentation
3

### Contribution
4
