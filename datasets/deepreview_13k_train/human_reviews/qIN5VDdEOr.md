# Do LLMs ``know'' internally when they follow instructions?

- Decision: Accept
- Scores: 6, 8, 6, 5, 5

## Abstract
Instruction-following is crucial for building AI agents with large language models (LLMs), as these models must adhere strictly to user-provided constraints and guidelines. 
However, LLMs often fail to follow even simple and clear instructions.
To improve instruction-following behavior and prevent undesirable outputs, a deeper understanding of how LLMs' internal states relate to these outcomes is required.
Our analysis of LLM internal states reveal a dimension in the input embedding space linked to successful instruction-following. 
We demonstrate that modifying representations along this dimension improves instruction-following success rates compared to random changes, without compromising response quality.
Further investigation reveals that this dimension is more closely related to the phrasing of prompts rather than the inherent difficulty of the task or instructions. 
This discovery also suggests explanations for why LLMs sometimes fail to follow clear instructions and why prompt engineering is often effective, even when the content remains largely unchanged. 
This work provides insight into the internal workings of LLMs' instruction-following, paving the way for reliable LLM agents.\footnote{We will release the data and code on GitHub upon publication.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates the internal representation of LLMs and identifies a "dimension" that corresponds to their success in instrution-following. They show that manipulating this dimension could improve success in instruction-following without degrading the quality of the outputs. They also measure correlation of the dimension with different perturbations and show that it is more sensitive to the phrasing of the prompt than the task difficiulty or faimiliarity. 

'

### Strengths
* Paper offers very interesting and operationalizable insights about the internal representations of LLMs.
* Paper tells a very good, satisfying story: from identifying the dimension, to manipulating and interpreting it.

### Weaknesses
 - The methodology description lacks clarity due to insufficient mathematical notation. It is especially difficult to follow the procedures outlined in Sections 3 and 4. The authors should clearly define mathematical objects, such as "input representation," and provide precise equations for the computations (e.g., lines 370-374). Specifically, given a prompt \( x_1, x_2, ..., x_n \) of n words and an output \( y_1, y_2, ..., y_m \) of  m words, what is the "input representation" as a function of these tokens? It appears to be computed solely from the output words.

* The terminology is confusing. The term "instruction" would be more accurately described as "constraints." It’s challenging to distinguish "instruction" from "task," as "instruction" could imply the entire command given to the model. Additionally, the meaning of "dimension" is unclear. Does it refer to a hypothetical concept rather than an actual dimension of a hidden vector computed by the model?

* The experiments were conducted on a single, relatively small dataset, raising questions about whether the findings will generalize.

### Questions
- See weaknesses
- What is the motivation behind the update in line 303-304? Could you provide more intuition on what is being done to the input representation there?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work analyzes and compares LLM internal representations when it can successfully follow instructions, vs. when it fails at following instructions. By training linear probes on representations, authors find a latent direction that predicts instruction following success, and shows it generalizes to unseen tasks and instructions. In addition, this work uses representation engineering to make adjustments along the instruction following dimension they found, and finds these adjustments can improve instruction following performance. Finally, this work also finds that the instruction following dimension is more correlated with how the prompt is phrased, rather than the difficulty of the instruction or the task.

### Strengths
This paper is well-structured and the findings are very interesting - while using linear probes to find a latent dimension for a specific phenomenon is not that interesting or original, the follow-up analyses demonstrating that instruction following can be made more accurate with representation engineering, and comparing the correlation of this dimension to different properties of the prompts, are both interesting. In addition, most claims made in the paper are sufficiently backed up with experiments and evidence.

### Weaknesses
In section 3, I'm confused what the direction D taken is for different instructions, since the previous section states that linear probes do not generalize well across instructions. Does this mean representation engineering promotes different directions for different instructions, or is there a universal direction that enhances all instructions generally? It would be helpful to clarify this in the paper.
For section 4 as well, one instruction type is chosen to perform the analysis on correlations. Could you elaborate on how much the findings in this section generalizes to other instruction types? Or could there be instruction types whose representation is more correlated with task familiarity rather than phrasing?

### Questions
- At the start of section 2, it would be helpful to elaborate what the IFEval dataset is used for 
- Make text in Figure 1 bigger

### Soundness
4

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
3

### Summary
This work finds that the representation of token is related to the success rate of instruction following. The authors apply linear probing to identify a specific dimension and use representation engineering (RE) to manipulate the representations. Experimental results show that RE  improves success rate while maintaining quality. Further analysis reveals that phrasing modifications plays a critical role rather than task familiarity or instruction difficulty. This paper provides a deeper understanding to this field.

### Strengths
1. This paper provides a new understanding of instruction following, using token representation to interprete LLMs themselves.
2. The experiments are well designed and the writing is easy to follow.

### Weaknesses
1. Some of the conclusions in this paper are as expected, e.g. results from Table 1 and Table 2 are related to "Lost in the Middle" phenomenon. [1]
2. The performance improvement brought by this method is limited as shown in Table 4.
3. The IFEval dataset is small and such problem may be addressed by extending instruction following data.

### Questions
1. Have you tried reverse representation engineering? Will it be worse than random?
2. Why did you focus on the representation of the first token in the last layer? Any insight?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors expand prior work on finding meaningful directions in the latent space of transformer language models to find a direction associated with whether models follow a given instruction or not. 
- For the analysis, they adapt and expand an existing dataset and study four open-source models (7b to 13b parameters). 
- Using linear probes, the authors find directions associated with instruction following across the studied tasks, but not generalizing to hold-out instruction types. 
- They show that manipulating the latent representation along the found direction can improve instruction following success and maintain instruction tuning quality for already successful cases.
- The authors find that the found latent space direction is affected by prompt sensitivity/phrasing of the instructions (less so by task complexity and perplexity)

### Strengths
- The goal of finding a way to manipulate latent representations to improve the instruction following of language models (or detect whether instructions are not being followed) has the potential for significant usability and safety impact while being novel. 
- The paper is very well written and the presentation is generally clear.
- The presented methodology is well structured and each section is clearly motivated by the previous results.
- The authors test four open-source models across many different tasks, demonstrating a certain amount of robustness.
- The authors generally do not overclaim their results and are very transparent.

### Weaknesses
The authors do not claim that they find a universal direction in these models that fully represents the idea of instruction following. However, to make a significant contribution via usability and understanding of latent representations, this work would benefit from addressing a few weaknesses to enable more robust future work and enhance the usability of the results.

### Weakness 1

The studied tasks are somewhat general but the instructions are fairly simple and not necessarily representative of general language model uses. I wonder how well the results of this work might generalize: It is also unclear how well instructions are being followed in a general use case. To use the example of the paper: You might ask a health bot to be aware of your left knee injury when coming up with training plans, but does adding the found latent space direction have side effects like avoiding leg training altogether or creating asymmetric training plans leading to other issues?  The results in this paper could be significantly strengthened by finding applications that allow for a more nuanced analysis of how instructions are being followed after representation engineering to demonstrate the usefulness of their technique.

### Weakness 2

In Sec. 3, I think an opportunity was missed to strengthen the analysis by demonstrating that the found direction also works in a counterfactual way: Can you use the fitted alpha values and directions for the F2T and T2T tests and only flip the sign of the respective alpha value to check if it also works on (intentional) T2F and F2F? I think this is necessary to demonstrate a minimum of reliable usability and support the claim of safety impact (to potentially get a model to not comply).

### Weakness 3

It is unclear (to me) if using only one direction is sufficient for modeling whether an instruction is being followed or not and even if, whether the presented analysis finds that direction. For example, the prompt sensitivity studies in Sec. 4 affecting the performance could be caused by other meaningful "directions" being entangled in the one you care about. To be more precise: If changing "write a resume for [a] software engineer [...]" to "I want you to write about [a] software engineer resume [...]" makes a difference, how do we know this is not caused by, e.g., confounding the learned directions with the instruction data set with a "dialog in first-person" direction (not unlikely,  given the colorful interpretations modern SAE approaches find).

To link it to another, more concrete use case: Is it possible to circumvent safety training of a language model using the proposed methodology? Although also only necessary and not sufficient, such a more complex example would demonstrate that using only one direction is powerful enough to be useful. 

If one direction is not sufficient, it might be worth testing if a higher-order approach (2D, 3D, ...) might be more robust to find that direction. There are plenty and different works on this, but for example, [1] uses PCA on latent representations to find the one relevant direction to model how small backdoored language models process trigger inputs to switch to toxic text.

### Weakness 4

In Sec. 3, fitting an alpha for each model and instruction type greatly limits usability, especially given that you would need a cleanly separate dataset for all relevant tasks. This is also more difficult for more realistic tasks mentioned in Weakness 1. 

### Weakness 5

This is a minor weakness that did not impact the final review score, but I wanted to explain why I rewarded a 3 instead of the maximum score of 4 for the presentation. I would have rewarded a 4 if figures 2 and 4 had used a larger font size for the axis labels, plot legend, and larger marker sizes. Please make these plots more readable for future versions of this work. 

### Weakness 6

In Sec. 3, it is not clear whether and how the authors calibrated the GPT-4-based scoring from 0 to 9 to construct the quality ratio. The results in Sec. 3 could therefore be strengthened by stating how the GPT-4-based analysis is being conducted (how exactly is a quality rating of 4 different than a quality rating of 5, in-context examples or not, ...) and how accurate and reliable it is (True positive rate, false positive rate, ...). 
 
### Weakness 7

The stated uncertainties seem very low, especially in Tables 3 and 4 (negligible/0 uncertainties). I think the claims in this work could be strengthened if other methods, e.g., bootstrap resampling, are being used to determine a base uncertainty beyond uncertainties purely determined from the linear probes.

### Questions
Generally, please just respond to my weaknesses above. I'm willing to increase the scores (total, contribution, and soundness), especially if you address the crucial ones related the generalizability and usability with new experiments or strong arguments. 

Q1: Can you explain where the "middle" token was for the different prompts? Was it the middle token of each sequence and thus changing the position for each prompt?

### Comments (Not considered for the review)

- For Figure 2, I feel LDA (fitted on training data) might be a better fit than PCA to show separability, given that LDA actively tries to separate the known classes.
- In lines 213-214, you state that the instruction type generalization values are close to chance. Given the stated 1-sigma uncertainties in Table 1, the presented values are not statistically significantly different (depending on the definition, 2-5 sigma) from random chance.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors explore whether LLMs have an internal representation related to successful instruction following. They train a linear probe on the models' internal representations to predict success/failure cases. This probe works well when tested on held-out tasks. However, when tested on held-out instructions, the probe fails, suggesting that the representation found is not a general "instruction-following" representation.
Potential practical use: Adding this identified direction to a model’s internal representation improves instruction following -- although it is unclear how far this generalizes.

### Strengths
The paper demonstrates a practical use case of their findings. The instruction-following direction improves model instruction-following success. This can be a useful case way to steer models to follow instructions better.

Also, the method could help us detect when a LLM will not follow a particular instruction. We can detect this even before the LLMs generate a response — because the method works on the first response token.

This is step towards scientifically understand key processes in how LLMs complete practical tasks

The paper reproduces results across different models. The paper conducts experiments across multiple models (Llama, Mistral, and Phi-3) and shows strong results on all 3 models.

### Weaknesses
W1. I still think few-shot would be a good comparison to run.

W2.
>While our work does not fully explain why this sensitivity exists or how it originates during training, it provides a foundation for understanding and addressing this limitation.

The first part of this sentence is crucial. I think more work is needed to explain these things.

W4.
I think frontier models like Claude Sonnet 3.5 are much more robust to paraphrasing prompts. This undermines the explanatory potential of this work -- which finds representations that are sensitive to prompt phrasing.

While some of the rebuttals were helpful, they didn't resolve the most important issues raises in the review. Hence I keep the same score.

### Questions
Define “know internally”. The title and various parts of the paper reference this. After reading, I understand it as “encoded instructions in a way correlated to correct responses”. But perhaps the authors disagree with this definition. Defining it specifically would clarify this.

From above: The authors ask the question “Do LLMs know internally when they follow instructions”, but they don’t specifically answer it. I feel that the title and the abstract imply yes. But on closer reading, only on page 4, we find that it does not generalize across instruction types. So the internal representation seems an encoding of the specific instruction type, rather than a general knowledge of instruction following. Clarifying this earlier would be useful. Readers skimming the paper may have a wrong impression.

### Soundness
3

### Presentation
2

### Contribution
2
