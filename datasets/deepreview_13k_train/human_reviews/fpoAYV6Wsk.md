# Circuit Component Reuse Across Tasks in Transformer Language Models

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Recent work in mechanistic interpretability has shown that behaviors in language models can be successfully reverse-engineered through circuit analysis. A common criticism, however, is that each circuit is task-specific, and thus such analysis cannot contribute to understanding the models at a higher level. In this work, we present evidence that insights (both low-level findings about specific heads and higher-level findings about general algorithms) can indeed generalize across tasks. Specifically, we study the circuit discovered in \citet{wang2022} for the Indirect Object Identification (IOI) task and 1.) show that it reproduces on a larger GPT2 model, and 2.) that it is mostly reused to solve a seemingly different task: Colored Objects \citep{bigbench}. We provide evidence that the process underlying both tasks is functionally very similar, and contains about a 78\% overlap in in-circuit attention heads. We further present a proof-of-concept intervention experiment, in which we adjust four attention heads in middle layers in order to ‘repair’ the Colored Objects circuit and make it behave like the IOI circuit. In doing so, we boost accuracy from 49.6\% to 93.7\% on the Colored Objects task and explain most sources of error. The intervention affects downstream attention heads in specific ways predicted by their interactions in the IOI circuit, indicating that this subcircuit behavior is invariant to the different task inputs. Overall, our results provide evidence that it may yet be possible to explain large language models' behavior in terms of a relatively small number of interpretable task-general algorithmic building blocks and computational components. Thus, these findings are an encouraging sign that progress can be made in understanding neural networks by analyzing small models on simple tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper falls into the line of work of mechanistic interpretability of neural networks.

This paper compares the Indirect Object Identification (IOI) subnetwork identified in Wang et al. 2022 in GPT-2 small, with a new Colored Objects task subnetwork identified by this paper.

The paper shows that in GPT-2 medium there is a significant overlap between both subnetworks in terms of the attention heads that are activated. Furthermore, the paper conducts an analysis (with ablations and study of the attention probabilities) of the different functions of the heads in the Colored Objects subnetwork and argues that they follow a human-interpretable algorithm. The places where the Colored Objects subnetwork differs from the IOI subnetwork are argued to be the places where the IOI algorithm and the Colored Objects algorithm differ.

Finally, the paper demonstrates that through a handcrafted manipulation of the internal activations, the accuracy of GPT-2 medium on the Colored Objects task can be improved from ~50% to ~100%.

### Strengths
The clarity of the presentation is high. The analyses seem to be of high quality. The research field of mechanistic interpretability is important, so the paper is significant insofar as it is a good-quality contribution to this field.

In my opinion the most interesting contribution of this paper is that via mechanistic interpretability analysis, the authors can get a better understanding of the reason that GPT-2 medium fails on the Colored Objects subtask, and intervene on the internal representations at the appropriate heads to get a good output. It would be interesting if this were explored further in settings beyond Colored Objects, and if this could be part of a general framework for improving LLM performance on reasoning tasks.

### Weaknesses
The finding that there are circuits that are reused within transformer networks is not new, since this is known e.g., for induction heads. (This is also pointed out by the authors in their related work section.) So I am having trouble wrapping my mind around what the new conceptual contribution of this paper is:

* In terms of techniques, the identification of the IOI subnetwork in GPT-2 medium reproduces an analysis of Wang et al. (2022) using their path patching method. The Colored Objects task network is identified running the same previously-known path patching method. Here the novelty in identifying this network seems to be mainly in identifying what the different heads in this subnetwork do, and writing this as a human-interpretable algorithm. But this style of analysis already appears in the IOI paper.

* Furthermore, the analysis is mentioned in the appendix to not apply to GPT-2 Large & GPT-2 XL, where there is no significant overlap between the IOI and Colored Objects subnetworks. I appreciate the honesty of the authors in reporting this negative finding, but it seems like a major strike against the phenomenon of circuit reuse advocated by this paper. It would be very interesting if the authors could give a more in-depth explanation of why we could expect GPT-2 Large and GPT-2 XL to not have circuit reuse. Specifically, it is unclear if the lack of overlap is due to the same functional roles being performed by different heads, or if the larger models are solving the tasks in a fundamentally different way. The paper does not provide sufficient analysis to distinguish between these possibilities. This raises questions about the generalizability of the findings to larger models, which are of greater practical relevance.

### Questions
1. Could you please clarify what you mean by "normalized by task per each path pathing iteration" in Figure 3?

2. Could you please clarify what you mean by "due to the number of mover heads in the larger models" in Figure 23?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigates the generalizability of mechanistic interpretability in language models, focusing on the Indirect Object Identification (IOI) circuit and its application to a different task, Colored Objects. The authors perform an intervention experiment to demonstrate their claims. The work seeks to address the task-specific nature of studies in interpretability and explore the possibility of understanding language models at a higher, more general level.

### Strengths
1. **Originality**: The paper addresses an important issue in the field of interpretability by examining the generalizability of mechanistic insights across tasks in language models. This is an original and valuable contribution.

2. **Significance**: Understanding the extent to which language models reuse or learn task-specific circuits has significant implications for the field of machine learning and interpretability. This work provides evidence that the IOI circuits (which is actually more a high-level copying mechanism than something related to indirect object identification) is also used in a least one other task (Colored Object), suggesting the presence of a general and reusable high level mechanism learned by the LM. It is a significant result as it contributes to addressing the challenge of explaining large language models' behavior.

3. **Quality**: The paper employs a range of techniques, including path patching, attention pattern analysis, and logit attribution, to investigate the proposed mechanisms. These methods demonstrate the authors' commitment to a high-quality analysis. Nevertheless, as noted in the Weaknesses Section, the study could be greatly improved by providing control baselines.

### Weaknesses
 1. **Experimental Demonstration**: The experiments, as currently presented, may not be sufficient to demonstrate the generalizability of basic algorithms in language models. It is only shown for one circuit (IOI) identified with a relatively small LM (GPT2-Medium) in two toy tasks (IOI and Colored Object). It will be essential to explore other types of experiments or analyses to strengthen this argument (out of the scope of this paper). The authors already acknowledge this limitation in the paper. This is a strong limitation. At the same time, this work is a promising first step, that may foster similar work on the topic and improve our knowledge of LMs. (Therefore, this argument alone should not motivate the rejection of the paper.)

2. **Overlap Measurement**: The paper mentions an overlap in in-circuit attention heads but lacks a detailed explanation of how this overlap is computed. Although "putting an exact number on how similar two circuits are is a very complex task that [the authors] do not attempt to fully answer in this paper," the results in the paper heavily rely on this metric. Thus, authors should (a) provide a more detailed description of the overlap metric; (b) quantify the uncertainty of this metric and the results associated to it; and (c) provide clues to better understand its range. As an illustration, authors wrote that 78% of the IOI circuit is used in the Colored Object task. However, without more information, it is difficult to say how significant this overlap is. Providing control baselines, such as comparing the IOI circuit overlap with a set of random tasks, or computing the overlap regarding another circuit (which could be a random circuit), could help to determine if 78% is high or not. Without such information (uncertainty quantification, control baselines, etc.), the significance of the results is hard to interpret. Note that authors briefly mention such an experiment in Appendix I. This should be expanded and included in the main paper.

3. **Interpretation of Intervention Experiment**: In order to prove that some heads are performing the role of gathered heads, the authors conducted an intervention experiment in the model. They did so by blocking attentions to some words in these heads and then measuring the impact on accuracy. They observed that the intervention causes accuracy to decrease and concluded that it successfully demonstrates the role of these heads. However, once again, this experiment lacks a control baseline. Authors should, for instance, reproduce the same intervention on similar heads (but that are not expected to perform the role of CG) and see if the result is different. If the interventions on random heads do not produce the decrease in accuracy observed with candidates’ heads, then it is reasonable to say that these candidates are CGs. Without these control baselines, it is not possible to draw any conclusions from the intervention.

4. **Related Work**: The section on related work is too concise. To provide a broader context, the authors should expand on related work in the field of language model interpretability, specifically those that address the task-specificity of interpretability findings. This will help readers better understand where this work fits in the existing literature and how it contributes to addressing the challenge of task-specificity in interpretability studies.

5. **Lack of Clarity**: The paper exhibits instances of unclear explanations and visualizations, which can hinder readers' understanding of the research. For instance, Section 4.3 is difficult to follow. In addition, there are issues with legends in figures, as terms like "attn prob on token" and "dot w/ token embed" lack sufficient explanation (e.g. in Fig 4). Furthermore, the inclusion of color information in the figures is not adequately commented upon, leaving readers to wonder about its significance. Figures 6 and 7 (Appendix), could benefit from clearer legends and more informative descriptions. Lastly, explanations in the appendix, such as Appendix B, are difficult to follow. While the complexity of mechanistic interpretability tasks may contribute to this challenge, the authors have an opportunity to improve clarity, which would greatly enhance the paper's accessibility.

### Questions
# Major questions: 
*I'd be willing to consider increasing my rating if these major points are addressed. In particular, addressing the first two points presented below would significantly enhance the paper's soundness.*

1. **Overlap Measurement**: The paper relies heavily on the concept of overlap in in-circuit attention heads, particularly in demonstrating the generalization of mechanisms. While it is acknowledged that putting an exact number on this similarity is complex, can the authors provide a more detailed description of the metric used for measuring overlap? Additionally, could they quantify the uncertainty associated with this metric and provide insights into the expected range of overlap values? To help readers assess the significance of the 78% overlap, would it be possible to provide reference baselines, such as comparing the IOI circuit overlap with a set of random tasks or comparing it with the overlap regarding another circuit, even if it's a randomly generated one?

2. **Interpretation of Intervention Experiment**: The authors conducted an intervention experiment to demonstrate the role of certain attention heads. However, it is crucial to establish the validity of this demonstration by including control baselines. Can the authors consider reproducing the same intervention on similar attention heads that are not expected to perform the role of gathered heads? This approach would help differentiate between candidate gathered heads and other attention heads that might not have the same function. Without these control baselines, it is challenging to draw meaningful conclusions from the intervention experiment.

3. **Related Work**: The related work section, while present, is relatively concise. To provide a more comprehensive context for the readers, can the authors expand on related work in the field of language model interpretability, particularly focusing on those works that address the task-specificity of interpretability findings? This would help clarify where this research fits in the existing literature and how it contributes to addressing the challenge of task-specificity in interpretability studies. Are there any specific prior works that have addressed or attempted to address the same problem or similar questions, and how does this paper compare to them? In particular, how does this work relate to the induction and duplicate heads found in Olsson et al. 2020?

4. **Clarity**: Can the authors address the issues related to clarity, particularly in Section 4.3 and with the legends in the figures? Could they provide clearer explanations for terms and visual elements like "attn prob on token" and "dot w/ token embed" (Fig 4) ? Additionally, what is the significance of the color information in the figures (e.g. Fig 4), and could the authors provide more context or commentary regarding its use in the visualizations? Lastly, are there plans to improve the clarity of explanations in the appendix, given its complexity, to enhance the accessibility of the research for a broader audience? Clarifying these elements would greatly benefit the overall presentation of the work.

# Additional minor questions:

5. Why does the language model fail to correctly utilize the IOI circuit on the Colored Objects task? Is this failure potentially influenced by the number of distractors in the task? If so, it would be informative to explore varying the number of distractors in the task and analyzing the resulting overlap and accuracy to gain deeper insights into the model's behavior in different contexts.

6. What does the term [end] position refer to in the text? It is mentioned but not clearly explained.

7. In Section 4.5, the paper discusses the top 2% of important heads. Could the authors provide a more detailed explanation of how these important heads are defined, particularly in relation to the path patching technique?

8. Appendix J appears to raise questions regarding the generalizability of results from a small model on a toy task to a more complex task with a larger model. The appendix seems to contradict the main paper's claims. Could the authors provide clarification and elaboration on this aspect? Specifically, how do the results from the small model analysis on a toy task relate to accurate predictions on a more complex task with a larger model? This clarification is essential to ensure consistency in the paper's argument.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the similarity of circuits of information flow on two tasks - IOI, and Colored Objects (CO). They study GPT2-Medium, which can do the IOI task successfully, but struggles with the CO task. They reproduce a previous circuit analysis of the IOI task for a different model, as well as for the CO task. They find that many of the same attention heads are important for both tasks and perform the same roles, with a few exceptions. They show if these exceptions are corrected in the CO task to match behavior from the IOI task, the performance can be improved.

### Strengths
* The paper has a good understanding of related prior work and presents their work well in context.
* The paper has clear and important motivation - whether circuit analysis and circuit components are transferable across tasks.
* The paper clearly shows there are components that have similar functionality on two different tasks (mover heads, induction heads, and duplicate-token heads).
* The targeted intervention in section 5 is an promising proof-of-concept - showing that understanding the interactions between different components of a circuit may allow correction of undesired behavior when using LLMs for a particular use case. This is the most interesting result of the paper and should be explored more in depth.

### Weaknesses
The paper only investigates reuse of components between two tasks, which are pointed out as similar to each other in the paper. The claims in the paper would be strengthened by investigating component reuse across additional tasks that are less similar to the original tasks studied (IOI & Colored Objects). Perhaps studying the behavior of these components on a larger distribution of text (i.e. open web text or some equivalent) that is not task-specific would provide insight into how generally we can understand the inhibition-mover components.

While the intervention in section 5 correctly predicts the interaction between the inhibition heads and mover heads will improve performance, this ignores the other half of the circuit - induction heads, duplicate token heads, and content gatherer heads. A more thorough analysis of the interactions between these elements and the inhibition heads/mover heads would strengthen the claim that these components are part of the circuit. For example, is there an intervention on induction heads/previous token heads (or something else) that would reliably produce the attention pattern you artificially induced into the inhibition heads/negative mover heads? This would show better understanding of the entire circuit, and not just the interaction of the last two sub-components.

The reasons provided for why the inhibition signal “exists but is noisy'' were not very clear/convincing. If the IOI view of inhibition is correct, wouldn't the signal the inhibition heads receive of where to attend (to wrong colors) need to come from the induction heads/previous token heads (or a fuzzy-matching version of the same)? It is unclear how the inhibition heads are identifying the incorrect color tokens to attend to, especially if the induction heads are not providing the correct signals.

The methodological contributions of the paper are limited as they mainly rely on existing approaches to discover and validate circuits - path patching, logit attribution, and visualizing attention patterns.

Presentation and Clarity
Minor errors:
Section 2 - Experimental setup mentions “Appendix 4.3” which should be section 4.3, as it is not part of the appendix.
Section 2.1- Colored Objects Task - “other” is repeated twice.
Section 4.5 “deterimine” spelled incorrectly,
Section 7.1 “task” is repeated twice

### Questions
Although it is briefly touched upon at the end, there is is an important question to be answered more concretely: why don’t inhibition heads appear to work properly in the Colored Objects setting when they work just fine for the IOI task? One hypothesis might be that the induction heads, which were important for influencing attention of inhibition heads in IOI, aren’t passing forward the proper information but it might be improved with more shots. For example: if you provide some more ICL examples do the inhibition heads start to work as the IOI task would expect them to? 

It seems the paper has identified two potential ways through which information about what position to attend can travel to mover heads - through inhibition heads, or through content-gatherer heads.  At least for these two tasks the inhibition-mover subcircuit seems to be more robust than the content-gatherer-mover circuit. This leads to the question: is this always the case for extractive tasks when there are multiple choices that could be copied? Or are there cases where content-gatherer-mover subcircuits work well/better without inhibition heads?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper present evidence that there is a substantial circuit reuse between two different probed tasks in GPT2-medium: indirect object identification (IOI) and Colored Objects (CO). Furthermore, it shows a proof of concept intervention to substantially improve the accuracy at a task by "correcting" the behavior of the CO circuit, informed by the behavior of the IOI circuit.

### Strengths
- (Significance) The paper addresses an important blindspot of mechanistic interpretability (MI): transferability and generalizability. I believe that the finding of this work will be of substantial interest to the community
- (Clarity) Overall, the paper is structurally well organized and the tasks are clearly presented. However, unfortunately, this does not place the paper in the easy-to-read tier (see below).
- I find the error correction proof of concept particularly interesting, as it shows one possible practical application of MI. To my knowledge, this is a rather novel and worthwhile contribution.

### Weaknesses
 - (Clarity) My main concern with the paper is the it is not easy to read and follow, especially for people outside the MI field. For once, there is a heavy use of jargon and a liberal use of terms. I'll give some examples below, but I encourage the authors to give a thorough pass of the work and try to "cleanse it" to make it more accessible to a wider audience:
  - `circuit`: although the term is present in large part of the MI literature, I think a refresher and a definition would help. It is not clear what the boundaries of a circuit are, and how one is identified. Is it a set of heads? A set of neurons? A more precise definition is needed.
  - `residual stream`/ `write in the residual stream`: likewise, worthwhile defining. It is not clear how the residual stream is represented, and how a head 'writes' into it. Is it a simple addition of vectors? A more detailed explanation is necessary.
  - `[end]` not defined, presume it refers to the last token in the sentence, but unclear. It should be explicitly defined.
  - `inhibition`: what does it mean specifically? Does it mean that the head is subtracting a vector from the residual stream? Or is it setting some values to zero? A clear definition is needed.
  -  `noisy signal`: is there a definition for this? does this mean that the head(s) add a random vectors to the residual stream? Or is it a signal that is not correlated with the task at hand? A more precise definition is required.
  - Labels and titles of Fig 4 are difficult to decipher: what does `Dot w/token embed` mean? It is not clear what vectors are being dotted, and what is the significance of this operation.
- Some more formalism and equations could help (at least some reader).
     - E.g. one could probably define the  `Dot w/token embed` operation with a mathematical expression. This would greatly improve clarity.
     - The path patching, even if not a contribution of this work, could be explained more clearly (with a few equations). It is not clear how the original and patched paths are combined, and what is the mathematical operation that is performed.
- Evidence of the findings (and the storytelling) should find more space in the paper. The paper would benefit from more visualizations and examples to support the claims.

Minor 
- Suggest to use different typeset for named heads 
- Typo: to make to make (pag 7)

### Questions
See questions above.
- Do the MLPs play no role in the circuits explained? Are the MLPs even considered in the analysis?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
