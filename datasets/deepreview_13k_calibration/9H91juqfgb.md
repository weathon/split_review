# Safety Alignment Shouldn't Be Complicated

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 3, 8, 6

## Abstract
As large language models (LLMs) are overwhelmingly more and more integrated into various applications, ensuring they generate safe and aligned responses is a pressing need. Previous research on alignment has largely focused on general instruction-following but has often overlooked the unique properties and challenges of safety alignment, such as the brittleness of safety mechanisms. To bridge the gap, we propose the Superficial Safety Alignment Hypothesis (SSAH), which posits that safety alignment should teach an otherwise unsafe model to choose the correct reasoning direction - interpreted as a specialized binary classification task - and incorporate a refusal mechanism with multiple reserved fallback options. Furthermore, through SSAH, we hypothesize that safety guardrails in LLMs can be established by just a small number of essential components. To verify this, we conduct an ablation study and successfully identify four types of attribute-critical components in safety-aligned LLMs: Exclusive Safety Unit (ESU), Exclusive Utility Unit (EUU), Complex Unit (CU), and Redundant Unit (RU). Our findings show that freezing certain safety-critical components \textbf{(7.5\%)} during fine-tuning allows the model to retain its safety attributes while adapting to new tasks. Additionally, we show that leveraging redundant units \textbf{(20\%)} in the pre-trained model as an ``alignment budget'' can effectively minimize the alignment tax while achieving the alignment goal. All considered, this paper concludes that the atomic functional unit for safety in LLMs is at the neuron level and underscores that safety alignment should not be complicated. We believe this work contributes to the foundation of efficient and scalable safety alignment for future LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes the safety superficial alignment hypothesis, which states that a truly safety-aligned model simply follows correct reasoning for safe vs unsafe inputs, allowing it to refuse unsafe inputs while still responding helpfully to all others. The identify that some neurons in models appear to contribute more to safety vs utility than others, and that some appear to be redundant. Finally, they propose a method for fine-tuning models that preserves helpfulness while also allowing for an increase in utility by freezing all but these redundant neurons.

### Strengths
The ideas behind this paper hold value, and it demonstrates promising initial results. In particular:

* The results do demonstrate that certain neurons appear to contribute more to safety than others

* The fine-tuning results further show that there are less of these neurons after fine-tuning models on non-safety related tasks.

* Isolating safety specific neurons does appear to be successful and would be a valuable contribution if so.

### Weaknesses
## 1. Lack of rigorous definitions
### a. Two different versions of aligned models
In section 3, aligned models are defined as pre-trained models fine-tuned on safety data by the authors, while un-aligned models are models that have been fine-tuned for instruction following/helpfulness. However, in section 4, aligned models are defined as the chat, RLHF versions of models. I am concerned that the findings between sections may not hold across these definitions.

### Questions
- Why are different versions of aligned models used? 
- What is a reasoning direction/trajectory and how do you measure it? If it's an approximation, what assumptions go into it and what is it approximate in?
- What is a reserved fallback option?
- What is considered a malicious query vs a safe query?
	- examples are given for these (lines 226-229: "Sorry, I can't..." and "Here's how..."), but are these the actual tokens used? Are other tokens used?
	- If only these tokens are used, I do not find this to be sufficient testing. Additional types of responses are possible and should be considered.

- What are benign/malicious tokens?
- How is the cosine distance measured in section 3's experiments?
- How are neurons classified in section 4? What thresholds are used on importance scores to decide this?

## 2. Overclaiming and mismatched claims

The paper makes some very bold claims and hypotheses, but often these claims are not supported by prior research or experimental results.

### a. Exclusive safety/utility neurons
As shown in Table 1 Exclusive safety neurons have an effect on the utility of models as well (as do utility neurons on safety). Though it is a small effect, the claim that they are "exclusive" is not backed up with statistical significance testing showing that these differences are not significant, and feels arbitrary to me. How is exclusivity determined/decided?

### b. Safety vs general alignment
In the introduction, as part of the motivation for SSAH, it's claimed that safety alignment is different from general alignment (lines 63-64). The question that section 4.3 claims to answer is whether it's possible to mitigate the safety alignment tax. However, the only results shown are on general alignment/helpfulness. It's unclear if this will hold for safety alignment. Additional experiments evaluating on safety-specific data should be done.

### c.  Main questions
Of the three questions they aim to answer, unfortunately, none had clear answers provided in my understanding of the paper. For example, when explaining the difference in robustness between Llama-2 and Llama-3 in the safety results in Table 2, the explanation is that Llama-3 tries "attempts to analyze the true intention behind requests," without explaining what this means in terms of model architecture/training, or explaining why this would result in the observed differences. Can you provide more explanation for this hypothesis?
	
### d. SSAH and jailbreaking
In Section 3 (lines 181-185), the paper claims that SSAH can also hold insights for jailbreaking. However, no experiments are done on this, and in the discussion, it's mentioned that SSAH likely does not hold for jailbreaking.

### e. Helpfulness of un-aligned models
The claim that un-aligned models have good instruction following abilities is not supported by the MT-Bench scores. Llama-2-7B, for example has a reported average score of 2.85 for the version used in this paper, whereas the chat version of the model has a score of more than double this.

### f. Cosine similarity
Section 3 uses high levels of cosine similarity between safe queries and helpful responses (and likewise, unsafe queries and refusals) as indications of alignment. However, this does not measure what models actually predict. While it may be a useful tool for explaining behavior, further experiments looking at model predictions need to be done to confirm that these similarities are indicative of alignment.

### g. One family of models
Only Llama family models are tested. I would like to see this tested on more models before accepting the claim that this hypothesis is general.

### 3. Presentation notes
Overall, the presentation is quite hard to follow. While the writing itself is understandable, there is not enough detail given for experiments, and many of the plots are hard to interpret.

- Plot colors/appearance
	- figure 1: Reasoning direction is hard to read due to arrows
	- figure 2: having aligned and unaligned models on opposite sides is a nice tough, but the texture difference between unaligned and aligned is quite hard to see
	- figure 3: Part of the plot is highlighted, but there is no explanation for this. Is this meant to highlight the increase in distance across early transformer blocks mentioned?
		
- Typos
	- figure 1: genearl -> general, fullfill -> fulfill

- Writing clarity
	- Many of the issues of definition and method mentioned above stem from writing that jumps straight into results without describing the setting first. Including specific descriptions of experimental setups, datasets, evaluation methods, and definitions in each section would greatly improve the clarity and readability of the paper.

### Questions
1. On lines 324-325 you mention constructing two datasets following Wei, et al. (2024b). Are these the same datasets Wei et al. use, or are they constructed similarly?

2. As a possible further experiment, what happens if models are fine-tuned on more safety data? Do the safety neurons remain? Are other neurons converted to safety neurons?

3. Why are different versions of aligned models used? 

4. What is a reasoning direction/trajectory and how do you measure it? If it's an approximation, what assumptions go into it and what is it approximate in?

5. What is a reserved fallback option?

6. What is considered a malicious query vs a safe query?
	- examples are given for these (lines 226-229: "Sorry, I can't..." and "Here's how..."), but are these the actual tokens used? Are other tokens used?
	- If only these tokens are used, I do not find this to be sufficient testing. Additional types of responses are possible and should be considered.

7. What are benign/malicious tokens?
8. How is the cosine distance measured in section 3's experiments?
9. How are neurons classified in section 4? What thresholds are used on importance scores to decide this?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper sets out to explain the brittleness of safety training by analyzing neurons. Specifically, this paper proposes freezing neurons in LLMs that are crucial to safety training when fine-tuning on downstream tasks to minimize the loss of safety by fine-tuning. Additionally, this work proposes a parameter efficient fine-tuning focused on neurons identified as redundant.

### Strengths
1) This paper proposes using pruning to identify role of the neuron via ablation. This is a creative use of pruning for explaining NN behavior. I commend the effort to interpret and explain model behavior at a neuronal level. There are a lot of neurons and they have complicated interactions between them.

2) The work shows on GSM8K improvement to utility by fine-tuning exclusively redundant neurons. 

3) It shows freezing the neurons attributed to safety improve safety scores when fine-tuning for downstream instruction following task.

### Weaknesses
1) The vast majority of neurons (70%+) are labeled as CU which means the pruning isn't able to eliminate them either on the safety dataset or the utility dataset. This work's interpretability results would be stronger if it was able to attribute more neurons as safety or utility. The fact that the majority of neurons fall into the 'complex unit' category significantly limits the explanatory power of the proposed method. It suggests that the ablation technique, as applied, is not sufficiently granular to isolate the functions of a large portion of the network's neurons. This raises questions about the method's ability to provide a comprehensive understanding of the model's internal mechanisms.

2) It would seem that the definition of "utility" is sensitive to the choice of datasets used in pruning. From B.2, this seems to mostly consist of relatively simple QA problems. Consequently, the resulting positive result for fine-tuning 20% of the neurons is limited to GSM8K and doesn't apply to MMLU. It would be good to see how these designations apply to code tasks, logical deduction, and emergent zero-shot behavior. I commend the effort but I think it's difficult to definitively and objectively mark a neuron as redundant based on a chosen dataset. The reliance on relatively simple QA datasets for defining 'utility' raises concerns about the generalizability of the findings. The fact that the observed benefits do not extend to MMLU suggests that the identified 'redundant' neurons may be more task-specific than truly redundant. This limitation undermines the claim that these neurons can be universally leveraged for parameter-efficient fine-tuning without compromising performance on diverse tasks.

3) The results are shown on 7B/8B llama models. It's possible that the choice of datasets for identifying neuron contribution, the ratio of RUs and prevalence of "complex units" would be affected by model size and pretraining data mix. In particular, I would expect larger models with more layers to have less separability between utility and safety. The study's focus on relatively smaller models (7B/8B) limits the scope of the conclusions. It is plausible that the observed separability between safety and utility neurons may not hold for larger models with more complex architectures and pretraining datasets. The potential for decreased separability in larger models would significantly impact the applicability of the proposed method to state-of-the-art models.

4) As safety by the author's definition equates to binary classification, does applying llama-guard or gpt-4 moderation as a filtering step eschew the need for complex safety alignment? In the setting of alignment for instruction-following, it would make sense that poor instruction-tuned models cannot be resampled until they follow the instructions. However, superficial safety is a simpler objective without considering robustness to adjacent attacks. The framing of safety as a binary classification problem, while useful for analysis, may oversimplify the complexities of real-world safety concerns. The potential for filtering systems to address the identified safety issues raises questions about the necessity of the proposed neuron-level alignment approach. The paper should address the limitations of a binary classification approach to safety and its potential vulnerability to adversarial attacks.

5) It would help to show fine-tuning on distinct post-training capabilities other than general conversation datasets. For example, multi-lingual, long context, math, coding, factuality, and steerability (taken from llama-3 paper)

6) It's not obvious how the role of neurons are identified until reading the appendix.

Nits: 
1) Exclusive Safety Unit (ESU), Exclusive Utility Unit (EUU), Complex Unit (CU), and Redundant Unit (RU) are rather clunky terms that make it hard to keep track of what the abbreviations are referring to. Even something like SU, UU, MU (mixed units), and RU would be easier to parse.

### Questions
1) To defend, the brittleness of the safety training, it would be good to show that using an approach like rainbow-teaming attacks are not explicitly safety trained for are not protected. 

2) Is there bleed between the 100 prompts in ADV used to identify safety neurons and the evaluations on HEx-PHI and Adv-bench? How robust is this method to attacks not used in identifying safety neurons?

3) Appendix C speaks a bit to attention vs feedforward neurons. Are there conclusions from fine-grained analysis we can make as to which layer and where in the architecture the RU and safety neurons are located?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a new hypothesis related to the safety mechanism of LLMs. They interpret the safety mechanism as a "reasoning direction," depicted as a classification task. To verify this hypothesis, they evaluate the embeddings of each layer and partially prove the existence of the "reasoning direction." Furthermore, to identify the safety mechanism, they employ a pruning method, identifying around 1% of parameters as part of the safety mechanism. These parameters can be frozen during fine-tuning to maintain the model's safety alignment.

### Strengths
1. The hypothesis of "reasoning direction" is both novel and intriguing, and the method of using embeddings to explicitly express this concept is innovative and valuable.

2. In addition to their analysis, the authors identify a safety mechanism at the neuron level, freezing these neurons during fine-tuning to protect safety alignment.

### Weaknesses
No main weakness, I have several questions and please refer to the Questions section.

 1. You claim that "the reasoning direction can be interpreted as a simple binary classification task," which seems somewhat overclaimed to me. The "reasoning direction" is difficult to clearly delineate, as the model might only identify a query as harmful after further reasoning. For example, the model might initially fail to detect a harmful query, but after additional reasoning steps, it recognizes the output as harmful and realizes it should be banned. The evaluation in the paper does not refute the possibility of this scenario. While I do not question the correctness of SSAH, the claim appears too strong to be conclusively proven.

 2. Is the neuron detection method shown in Equation 1 sequential? If so, will it be slow when calculating the importance score for each individual neuron?

 3. Regarding the pruning method, I'm curious about pruning neurons in self-attention layers, given that the number of neurons in each head is fixed. During the pruning process, will each head have the same number of neurons reduced, or will the neurons be reorganized across several heads?

### Questions
1. You claim that "the reasoning direction can be interpreted as a simple binary classification task," which seems somewhat overclaimed to me. The "reasoning direction" is difficult to clearly delineate, as the model might only identify a query as harmful after further reasoning. For example, the model might initially fail to detect a harmful query, but after additional reasoning steps, it recognizes the output as harmful and realizes it should be banned. The evaluation in the paper does not refute the possibility of this scenario. While I do not question the correctness of SSAH, the claim appears too strong to be conclusively proven.

2. Is the neuron detection method shown in Equation 1 sequential? If so, will it be slow when calculating the importance score for each individual neuron?

3. Regarding the pruning method, I'm curious about pruning neurons in self-attention layers, given that the number of neurons in each head is fixed. During the pruning process, will each head have the same number of neurons reduced, or will the neurons be reorganized across several heads?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes the Superficial Safety Alignment Hypothesis (SSAH), which frames safety alignment as a binary task, guiding models to make safe decisions by selectively freezing key components. By identifying and freezing 7.5% of safety-critical units and repurposing 20% of redundant units as an "alignment budget," the model retains safety with minimal impact on utility, making safety alignment more efficient and scalable.

### Strengths
1. The paper is well-written and easy to understand.

2. The paper identifies four important safety components of LLMs. By freezing some safety components, the model’s safety attributes are retained, and with the "less is more" method, the complexity of fine-tuning is reduced.

3. Alignment tends to have negative impacts on other tasks. The authors mitigate the Alignment Tax by freezing habitual computation units.

### Weaknesses
1. The paper lacks sufficient empirical testing against dynamic jailbreak attacks, failing to verify the model's robustness to complex attacks in real dynamic environments. Would it be possible to test the effectiveness of this method against some jailbreak attack techniques?

2. Can this method be effective on non-LLaMA-family architectures? It would be beneficial to explore other architectures, such as encoder-decoder models (e.g., ChatGLM) or MoE architectures like Mistral.

### Questions
Please see Weaknesses. 

Minor Typos:

1.In Line 120, there should be a space after "Qi et al. (2023)."; 2. In Table 3, please ensure the decimal points are aligned consistently.

If the authors can address the above questions, I would be happy to raise the score.

### Soundness
2

### Presentation
2

### Contribution
4
