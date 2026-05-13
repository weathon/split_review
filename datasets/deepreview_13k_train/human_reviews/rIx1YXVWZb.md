# Understanding Addition in Transformers

- Decision: Accept
- Scores: 3, 8, 3, 8

## Abstract
Understanding the inner workings of machine learning models like Transformers is vital for their safe and ethical use. This paper provides a comprehensive analysis of a one-layer Transformer model trained to perform $n$-digit integer addition. Our findings suggest that the model dissects the task into parallel streams dedicated to individual digits, employing varied algorithms tailored to different positions within the digits. Furthermore, we identify a rare scenario characterized by high loss, which we explain. By thoroughly elucidating the model's algorithm, we provide new insights into its functioning. These findings are validated through rigorous testing and mathematical modeling, thereby contributing to the broader fields of model understanding and interpretability. Our approach opens the door for analyzing more complex tasks and multi-layer Transformer models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper attempts to reveal the internal working mechanism of Transformers for integer addition tasks.

### Strengths
• Study an important problem of transformer models' application in numerical computation tasks.

### Weaknesses
• The analysis framework and analysis lacks mathematical rigidity. 
	• The conclusion is not well established based on rigorous mathematical framework. 
	• The paper does not fully utilize/choose the most relevant aspect of transformers for addition tasks.

• The analysis framework lacks a formal definition, making it difficult to assess its validity and scope. The paper does not specify the mathematical properties or assumptions underlying this framework, nor does it clearly articulate how it relates to the observed behavior of the transformer model. Without a precise formulation, it is unclear what kind of insights this framework can provide or what limitations it might have.

• The conclusions drawn about the transformer's internal mechanisms for addition are not sufficiently supported by a rigorous mathematical framework. The analysis relies on qualitative observations and interpretations of attention patterns and loss curves, but it lacks a formal connection between these observations and the model's actual computations. For example, the paper claims that the model divides the task into parallel, digit-specific streams, but this claim is not backed by a mathematical analysis of how the model's weights and activations implement this division.  It's unclear how the observed behaviors lead to the conclusion that the model is performing addition in a specific way.

• The paper's approach to using a single-layer transformer for addition is overly simplistic and may not capture the full potential of transformers for numerical computation.  The paper does not sufficiently explore alternative architectures or configurations, such as multi-layer transformers or different attention mechanisms, which could be more relevant for this task. The analysis does not consider how different embedding strategies or positional encodings might affect the model's performance. Furthermore, the paper does not justify why a single-layer architecture is sufficient to draw general conclusions about transformers and addition.

### Questions
1. Page 2, a latex error: "d_e-dimensional embeddings"
	2. Page 3, section 3, paragraph 3, "detailing identified circuits", is this a typo? Or which "identified" circuits? What is the "identified" process?
	3. Page  3, section 3, paragraph 4, "techniques in works like symbolically … ", a grammar error?
	4. Page 3, section 3, paragraph 7, "Surveys like  overview techniques…", missing citations after "Surveys like"?
	5.  Page 4, section 4, paragraph 3, "Fig. 2 shows … semi-indendently…", what is the loss per digit is being plot in Figure 2? 
	6. Page 4, section 4, paragraph 4, "Transformer models always process text from left to right…", this is not true. It is just an artifact of GPT-style attention masking. For example, we can do config the attention mask to enable full order attention over the two addends and generate the outputs in all kinds of order, e.g. from the tens digit to higher value digits, from the middle digit to two ends, and so on. We can also do non-autogression generation, e.g. incremental masking output generation. 
	7. Page 4, figure 3 caption "..After the question is fully revealed (at layer 11)..", by "layer 11" do you mean the 11th row? To avoid ambiguity, it is better to number the attention matrix and refer to them the row or column number across the paper.  Also what are the sub-figures of 0.0, 0.1, 0.2? Different heads? What are the labels? 
	8.   Page 4-5, section 5, please clarify whether the  "mathematical framework" is  for characterizing (grouping) addition data instances-digits only? Or is there a link to the loss? If so, please formulate the framework and what kind of mathematical hypotheses this framework can verify formally in mathematical terms?  Also please detail the loss on each digits formally. Also please detail the statistics of your training and valid datasets in terms of your classification of digits in your framework. 
	9. Page 4-6, please detail how the loss is being average. Are they per digits or per digit average?
	10. Page 6, please introduce or define or describe phase 1, 2, 3 formally?  
	11. Page 7, section 7, "During model prediction we overrode … the model memory (residual stream)…", please detail the approach formally? Are your conclusions/assertions based on checking the attention scores?  Please discuss explicitly with formal treatment. Otherwise, the plain English language analysis in Section 7 is difficult to follow and justify. Also formally define "independent of every other digit", "most impact on loss" and define it based on measure statistics during model inference time.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Very interesting paper that focuses on explaining the "inner workings" of the foundational model of Transformer. While the use-case demonstrated (integer addition with a single layer transformer) is simplistic, the idea is novel and the visualisations are meaningful and make sense for better trust and confidence in how a transformer model works for the AI community.

### Strengths
Transformer model focus - no doubt an important model in the current AI landscape. Solid mathematical explainations and interpretation of the model working, the attention visualisations shown are very interesting and the model training loss curve which shows how a transformer trains individual digits semi-independently was promising to see.

### Weaknesses
No major weakness other than the paper applying the framework of explainability to a simple problem (integer addition). Though, this is well the strength as well of the paper as it makes the model easier to interpret and understand.

### Questions
Solid theoretical framework in the paper, good interpretation and visualisations - no further questions from this reviewer. The paper is very well written, easy to understand and the method is clear.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper delves into the intricacies of a one-layer Transformer model trained for integer addition, emphasizing the importance of understanding machine learning models for safety and ethical considerations. The study uncovers that the model breaks down the addition task into parallel, digit-specific streams, using different algorithms for various digit positions. Interestingly, the model starts its calculations later but completes them swiftly. A unique use case with a high loss is pinpointed and elaborated upon.

### Strengths
This is a technically solid, moderate to high impact paper, with no major concerns with respect to evaluation, resources, reproducibility, ethical considerations.

### Weaknesses
1. The adaptability of the methodology in this paper is limited, as it only applies to a one-layer Transformer model. Perhaps further analysis on two-layers or even more complex models would be beneficial. Moreover, the study solely focuses on integer addition, making it challenging to extend to other operations like subtraction or multiplication. The core issue is the lack of generalizability of the approach. The analysis is tightly coupled to the specific architecture and task, making it difficult to apply to even slightly different scenarios. For example, the digit-specific streams and their parallel processing might not be present in a model trained for subtraction, or might manifest in a completely different way, requiring a new analysis from scratch.

2. The writing of this paper is not comprehensive. For instance, the descriptions for Figure 4 and 8 are difficult to comprehend. The explanation of the model's internal workings, particularly in relation to the proposed mathematical framework, is not sufficiently clear. The descriptions of Figure 4 and 8 lack the necessary detail to allow a reader to fully grasp the model's algorithm. The connection between the figures and the text is weak, making it hard to follow the authors' reasoning. The mathematical framework itself is not presented in a way that is easily digestible, and the paper would benefit from more concrete examples and a more step-by-step explanation.

3. The experiments conducted are not exhaustive. In the "Prediction Analysis" section, the authors failed to provide a specific metric and results compared to baselines. The lack of quantitative results and comparison to baseline models makes it difficult to assess the significance of the findings. The paper does not provide a clear metric for evaluating the model's predictions, and it's unclear how the authors arrived at their conclusions about the model's performance. Without a proper baseline, it is impossible to determine if the model's performance is noteworthy or simply a result of the training process.

### Questions
Please see the Weaknesses.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the interpretability of Transformers. The authors focus on the 5-digit number addition task and analyze how a one-layer Transformer model finishes this task. To understand the model clearly, they propose a mathematical framework for integer addition, consisting of five tasks: Base Add, Make Carry 1, Make Sum 9, Use Carry 1, and Use Sum 9. The first three tasks can be independently executed for each digit pair, representing the sum of two digits modulo 10, checking for carry, and determining if the addition results in 9, respectively. The last two tasks chain operations across digits, respectively denoting adding the previous column's carry to the sum of the current digit pairs, and propagating a carry when Make Sum 9 and Use Carry 1 are true. The authors then analyze the one-layer Transformer model under this framework during the training phase and testing phase. More precisely, during the training phase, the authors investigate the training loss for Base Add (BA), Use Carry 1 (UC1), and Use Sum 9 (US9) three tasks. According to the experimental results,   US9 is the most complicated, especially in the case where more than one column carry occurs (e.g. 445+555=1000) and BA, UC1 two tasks are highly correlated. During the testing phase, the authors use ablation experiments to evaluate each attention head and conclude that for different digit pairs, the model uses slightly different algorithms.

### Strengths
- The paper advances in the direction of opening the black box of Transformers, which is a very important topic as Transformers are being applied in an increasing number of domains. 

- The authors decompose integer addition into several subtasks and investigate the loss of each task during the training. This might provide some inspiration for future improvements in deep learning for math.

- The paper is well-organized. The basic idea is clean and easy to follow.

### Weaknesses
 - One experimental flaw is that the test accuracy of the model is not provided. In addition, it is also worthwhile to explore using the trained model directly for the addition of integers with more digits.

- In the integer addition task, digit 0 should be treated as a special case, since intuitively, when humans perform integer calculations, the more zeros there are, the easier the calculation becomes. In other words, the digit 0 requires special attention. So it might be interesting to include Make Sum 0 and Use Sum 0 in the mathematical framework.

### Questions
(1) What's the performance of the trained model on the test data?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent
