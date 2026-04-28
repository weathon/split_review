# An Empirical Study on Enhancing LLMs' Alignment Capabilities through Restyled In-Context Learning Demonstration Examples

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 3, 6, 3

## Abstract
Alignment tuning is crucial for ensuring large language models (LLMs) behave safely, ethically, and align with human values. It bridges the gap between raw model capabilities and nuanced task requirements, such as helpfulness and user safety. Current alignment approaches, like instruction-following through supervised fine-tuning (SFT) and preference optimization (PO), require high-quality data and significant resources. This paper proposes a low-cost, tuning-free method using in-context learning (ICL) to enhance LLM alignment.

Leveraging the autoregressive nature of LLMs, we observed that aligned models adjust the probability distribution of early polarity tokens during decoding, influencing their response trajectory. Among polarity tokens, malicious tokens induce LLMs to positively respond to toxic queries, whereas benign tokens encourage constructive output. Based on this, we designed heuristic rules to select ICL demonstration examples that effectively influence polarity token distributions.

We packaged these examples as prompts to trigger few-shot learning, improving LLM alignment. Furthermore, the style and content of ICL demonstrations critically impact few-shot learning. Rewriting examples in a unified, structured style improved LLM accuracy and helpfulness, while specific content encouraged refusal of malicious prompts, enhancing safety.

Our experiments show that rewritten examples boost alignment, safety, and reasoning across various tasks. Compared to the best baseline approach, with an average score of 5.00 as the maximum, our method achieves a maximum 0.15 increase on the Alpaca-eval task (from 4.44 → 4.59), a 0.10 enhancement on the just-eval-instruct benchmark (from 4.50 → 4.60), and a maximum improvement of 0.08 (from 3.53 → 3.61) on the MT-Bench dataset. These findings underscore the need for deeper analysis and theoretical understanding of alignment for advancing future LLM research.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a new method for LLM alignment via in-context learning, which selects and restyles demonstrations. This approach is similar to URIAL (Untuned LLMs with Restyled In-context ALignment; Lin et al., 2024), however it introduces several different components. First, exemplar selection is guided by polarity tokens indicating helpful or harmful trajectories of LLM responses. Second, restyling is applied by leveraging the Average Treatment Effect to analyze the causal effect of different alignment outcomes. The proposed method, namely RIDE, is evaluated on several benchmarks, mainly just-eval-instruct (was provided in the URIAL paper), Alpaca-eval, and MT-bench.

### Strengths
1. The concept of polarity tokens is interesting and could influence studies beyond the context of this paper. 
2. The paper conducts a thorough empirical evaluation on alignment metrics and reports interesting findings by evaluating different variants of RIDE.

### Weaknesses
1. The paper lacks a clear discussion about its position with respect to previous work, which might confuse the reader. In the absence of a related work section, the paper’s title, introduction, and other sections read as if the paper’s proposal, to tackle alignment via in-context learning and alignment, is a novel aspect of this work. However this is exactly the proposal behind URIAL, which is not cited until much later.
2. It is hard to validate the claimed improvements compared to URIAL within the current experimentation protocol. First, it is not clear why the just-eval-instruct scores for URIAL and baselines in Table 2 are not the same as those reported in the URIAL paper (Lin et al., 2024). Second, RIDE optimizes its prompt using GPT-4o and a validation set from just-eval-instruct (is this provided originally or sampled from the test set?), which might provide an unfair advantage compared to other techniques.
3. The paper’s titled implies a possibly broader application of the paper’s idea than what is tackled by the proposed method. While polarity tokens have effectively been used in the context of this work, it is not clear how this idea can generalize in broader scenarios beyond factuality and safety categories. Furthermore, it is not clear how effective this approach would be in the absence of aligned models, costly GPT-4o inference, and the presence of a validation set.

### Questions
1. Are improvements statistically signficant?
2. Why are the reported baseline numbers for just-eval-instruct different than those in the URIAL paper?
3. How was the validation set selected for optimizing the prompt in RIDE?
4. Are the authors planning to share their codebase?
5. Could the authors elaborate how the proposed approach behind polarity tokens would scale with an increasing number of alignment categories?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a novel, tuning-free method to align base LLMs through in-context learning examples. It first identifies benign and malicious tokens with respect to two conflicting objectives, actuality and safety, based on the change in generation probabilities from an already aligned LLM and the corresponding base LLM. It then investigates the causal structure between content, style, and alignment and leverages the average treatment effect to find an effective way to select and restyle a given set of in-context learning examples. By prompting with these identified examples, the method achieves performance improvements on three benchmark datasets.

### Strengths
S1: The empirical results in this paper seem extensive and could assist researchers in understanding the LLM alignment process better.

S2: It is interesting to consider the causal relationship between content, style, and alignment.

S3: The idea about the conflicting nature between safety and factuality is interesting and reasonable.

### Weaknesses
W1: The presentation and the writing in the paper need to be further improved. For example, the authors introduced the idea of a reference model and $P^\text{refer}$ in Line 119 but never mentioned it again after that. What is the difference between $P^\text{refer}$ and $P^\text{base}$ or $P^\text{align}$? In addition, It is unclear how $V_\text{polar}$ defined in Line 221 is utilized in the subsequent causal structure of alignment. Will the restyling in Section 3.2 affect this value? If so, do you need to do another around of example selection after restyling?

W2: When identifying the benign and malicious polarity tokens, the base model and aligned model may differ in many different ways, it could be too general to broadly attribute all the tokens with the highest change in generation probability as benign or malicious tokens towards safety or actuality. This is reflected by the identified set of benign tokens for factuality in Table 1, which has nothing to do with the generic concept of "factuality". In fact, the change in generation probabilities of the unlikely tokens is meaningless. In addition, the generation probability of a token can be largely affected by the input context, simply averaging the change over the entire validation set may not be suitable. It is very likely that you will only find tokens that frequently appear at the start of a response.

W3: Are those identified benign and malicious tokens transferable across LLMs and validation datasets? If not, then you will need an aligned model to identify those polarity tokens in the first place, and there will be no point of using ICL examples to steer base models to achieve performance comparable to the needed aligned models.

### Questions
Q1: Have you considered the difference between the following two ways of identifying the benign tokens: (1) treat the aligned model as the reference, and take the tokens with the highest $P^\text{align} - P^\text{base}$ (2) treat the base model as the reference to generate the output, and take the tokens with the lowest $P^\text{base} - P^\text{align}$? I believe that the authors used the first approach in their paper, but I am wondering if the authors will get a different set of benign tokens when using the second approach.

Q2: Can you report the degree of $\Delta P$ for those identified tokens in Table 1? Are they marginal?

Q3: How's the performance of the aligned models on those three benchmarks?

Q4: Do you modify Alpaca-eval when reporting results in Table 3? I don't think Alpaca-eval comes with those multi-aspect scoring schemas. Should you use AlpacaEval 2 and report (length controlled) win rate as a standard metric instead?

Q5: LLM-as-a-judge is usually subject to large variance, have you tried repeating your experiments for multiple rounds and reporting the average performance and standard error?

Q6: It would be interesting to include some ablation studies to test the robustness of each design choice and the transferability of the identified polarity tokens.

Q7: The improvement upon URIAL seems marginal, especially on just-eval-instruct and alpaca-eval.

Q8: How statistically strong is the causal relationship between style and alignment? It is inappropriate to claim it as a causal structure without reporting the statistical significance.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper explores enhancing LLM alignment using restyled in-context learning (ICL) examples, introducing the concept of polarity tokens to guide generation outputs. The authors utilize Average Treatment Effect (ATE) to quantify the impact of different ICL styles and propose a structured method for selecting optimal ICL examples. They conduct experiments focusing on factuality and safety, demonstrating their method’s effectiveness across several benchmarks.

### Strengths
The paper presents its ideas in a clear and coherent manner, making complex concepts easy to understand.
The authors provide comprehensive empirical results that support their claims and showcase the method’s practical applications.

### Weaknesses
The paper’s contribution is incremental, lacking substantial novelty compared to existing ICL-based alignment methods.
The experiments lack granular analysis of individual ICL examples or polarity tokens’ contributions to model performance across tasks, and adding such details would deepen the understanding of the method’s impact.
The paper demonstrates effectiveness in specific tasks but lacks evidence of generalization across broader cross-task scenarios such as multilingual settings or bias detection.

### Questions
Could the authors clarify if their approach could adapt to dynamic, real-world contexts where example restyling might need to change over time?
What are the potential trade-offs between the proposed method and simpler alignment techniques in terms of computational efficiency and performance gains?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The main contribution of this paper lies in providing new empirical research on constructing better few-shot prompts for Alignment in the ICL phase. Specifically, the authors analyzed benign tokens from both aligned and base models, using this analysis to select and rewrite relevant examples from existing datasets as prompts to improve language model alignment. The authors conducted experiments on MT-Bench, Alpaca-Eval, and Just-Eval datasets, achieving some performance improvements.

### Strengths
Before arriving at their final ICL prompt method, the authors provided substantial empirical evidence supporting their prompt selection, rather than creating them arbitrarily, which enhances the paper's credibility. 

The authors chose three common and closely related Alignment datasets, demonstrating improvements in factuality, friendliness, and safety aspects examined in these datasets.

### Weaknesses
In my view, the paper's main weaknesses are its lack of soundness and insignificant experimental results, making it difficult to prove the method's effectiveness:
- The authors first selected from predefined ICL prompt sets by considering the impact on benign and malicious tokens (Section 3.1). However, they then rewrote these selections (Section 3.3). Obviously, there's a gap between the rewritten output's impact on benign and malicious tokens compared to the initial prompts, introducing additional bias from an experimental design perspective. Moreover, the authors didn't conduct ablation studies, leaving us uncertain whether the performance improvements stem from the rewriting or their proposed prompt selection algorithm. Specifically, the rewriting process introduces a confounding variable, making it impossible to isolate the effect of the initial prompt selection. The authors should have at least included an ablation study where they use the selected prompts without rewriting, and also an ablation study where they rewrite randomly selected prompts to see if the rewriting process alone is responsible for the performance gains.
- During the rewriting phase, the authors introduced an additional requirement: "(2) lengthy (enriching the answer details and increasing its length without altering the original meaning)". As is well known[1], when using LLM-as-a-judge, the evaluating models tend to favor models that produce longer outputs. Looking at the tables from three different test datasets, the text length generated by the RIDE method consistently exceeded the baseline URIAL method. From another perspective, while the authors selected ICL prompts for both factuality and safety examples, RIDE only outperformed URIAL in preference-related metrics like helpfulness and factuality, but not in safety. Therefore, I suspect the main performance improvement comes from using longer outputs as ICL prompts during the rewriting process, rather than the authors' primary proposed ICL selection method. The fact that the safety scores did not improve despite selecting for safety examples further supports this suspicion, suggesting that the length of the output is the dominant factor.
- The authors chose longer text examples as demonstrations for the language model, while the baseline URIAL method only used 3 examples, approximately 1011 tokens. As mentioned in their experiments, for the Olmo-7b model with a maximum token limit of 2048, RIDE performed worse than URIAL when their output lengths were similar. From this perspective, RIDE's efficiency decreased compared to URIAL due to using more input tokens, and when efficiency was similar, its performance might be inferior to URIAL. This raises concerns about the practical applicability of the method, as it may not be feasible to use such long prompts in real-world scenarios with limited context windows. The authors should have included experiments where the input length of RIDE is matched to URIAL to make a fair comparison.

### Questions
**Typo**:
- Line 116 lacks definition of the reference model
- Lines 116-118: We cannot clearly understand from the paper what $q1$ and $o1$ mean. If I'm not mistaken, these might refer to each token of the question and output.
- I suggest standardizing "unaligned LLMs" and "base LLMs", "unaligned model" and "base model". In line 124, you use both "unaligned model" and "base model" to describe f in the same sentence, which creates confusion.
- Missing citation for paper [1], which is highly relevant to this paper's implementation method and comparison baseline.

---

[2] In-Context Alignment: Chat with Vanilla Language Models Before Fine-Tuning

### Soundness
1

### Presentation
2

### Contribution
2
