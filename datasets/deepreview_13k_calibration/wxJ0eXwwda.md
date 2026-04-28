# The Unlocking Spell on Base LLMs:  Rethinking Alignment via In-Context Learning

- Decision: Accept
- Avg Score: 5.00
- Scores: 3, 5, 6, 6

## Abstract
\vspace{-0.5em}
 


\quad Alignment tuning has become the de facto standard practice for enabling base large language models (LLMs) to serve as open-domain AI assistants.  
The alignment tuning process typically involves instruction learning through supervised fine-tuning (SFT) and preference tuning via reinforcement learning from human feedback (RLHF).
A recent study, LIMA~\citep{Zhou2023LIMALI}, shows that using merely 1K examples for SFT can achieve significant alignment performance as well, suggesting that the effect of alignment tuning might be ``\textit{superficial}. '' 
This raises questions about \textit{how exactly the alignment tuning transforms a base LLM}.
 

\quad We analyze the effect of alignment tuning by examining the token distribution shift between base LLMs and their aligned counterpart (e.g., Llama-2 and Llama-2-chat).
Our findings reveal that base LLMs and their alignment-tuned versions perform nearly identically in decoding on the majority of token positions (i.e., they share the top-ranked tokens).
Most distribution shifts occur with \textit{stylistic} tokens (e.g., discourse markers, safety disclaimers). These direct evidence strongly supports the hypothesis that alignment tuning primarily learns to adopt the language style of AI assistants, and that the knowledge required for answering user queries predominantly comes from the base LLMs themselves. 

\quad Based on these findings, we rethink the alignment of LLMs by posing the research question:
\textit{how effectively can we align base LLMs without SFT or RLHF?} 
To address this,
we introduce a simple, tuning-free alignment method, \methodname{} (\textbf{U}ntuned LLMs with \textbf{R}estyled \textbf{I}n-context \textbf{AL}ignment).
\methodname{}  achieves effective alignment purely through in-context learning (ICL) with base LLMs, requiring as few as three constant stylistic examples and a system prompt. 
We conduct a fine-grained and interpretable evaluation on a diverse set of examples, named \dataname{}.
Results demonstrate that base LLMs with \methodname{} can match or even surpass the performance of LLMs aligned with SFT (Mistral-7b-Instruct) or SFT+RLHF (Llama-2-70b-chat).
We show that the gap between tuning-free and tuning-based alignment methods can be significantly reduced through strategic prompting and ICL.
Our findings on superficial nature of alignment tuning and results with \methodname{} suggest that deeper analysis and theoretical understanding of alignment is crucial to future LLM research.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- The paper focuses on the aligning LLMs via URIAL (Untuned LLMs with Restyled In-context ALignment) which 
    - studies _token distribution shifts between aligned and untuned LLMs_ with differences lying mainly in transitional words/discourse markers/stylistic tokens
    - infers that the style of in-context examples is substantially more important than semantic relevance.
- The work also offers *fine grained evaluation across dimensions* like relevance, coherence, depth, factuality, safety and engagement.

### Strengths
The paper is based in an area of interest to the ML community i.e., alignment in large language models and in-context learning.

### Weaknesses
 - **Novelty:** The following concerns highlight that URIAL does not substantially add to the available body of work and hence, does not warrant acceptance
    - The fundamental premise of the paper i.e., [knowledge and capabilities are learnt
    almost entirely during pre-training has been explored before](https://arxiv.org/pdf/2305.11206.pdf) including latent space analysis of alignment and misalignment via [Behavior Expectation Bounds(BEB)](https://arxiv.org/pdf/2304.11082.pdf)*. By purely logical extrapolation, it can be inferred that the token distribution shift is not semantic (Superficial Alignment Hypothesis) and hence, style of in-context examples is substantially more important.
    - Use of [in-context learning for alignment has also been explored](https://arxiv.org/abs/2308.04275) and in case of URIAL, the computational cost/two fold limitation given the limited impact on performance/lack of scalability in terms of evaluation(Section 5) is a strong limitation.
        - The claim of URIAL i.e., efficiently tailoring LLM behavior without fine-tuning is poorly supported. Given performance and computation cost, how efficiency is defined and what parameters contribute to claimed efficiency is unclear.
    - Section 4.2, “Previous evaluation methods lack explanatory power for their scores or pairwise comparisons, hindering human verification of judgements derived from automated metrics. To address these issues, we propose a multi-aspect, explainable evaluation protocol regarding the following six aspects: Relevance, coherence, factuality, depth, engagement, safety”. This is technically incorrect. There is direct/considerable overlap between [“coarse” evaluation](https://arxiv.org/pdf/2307.10928.pdf)(which includes human evaluators) and the proposed fine grained evaluation protocol in four of six parameters (correctness/factuality, harmlessness/safety, relevance/comprehension and readability/coherence).
    - Additionally, problems of SFT/RLHF LLMs are not directly addressed by URIAL.
        - SFTed LLMs perform significantly worse than untuned counterparts with factual/reasoning benchmarks. Performance and empirical analysis of URIAL on the same benchmark is not discussed.
        - The paper suggests that fine tuning may not be as crucial as previously assumed for LLM alignment but [evidence suggests](https://www.linkedin.com/pulse/in-context-learning-fine-tuning-language-model-deepank-dixit) that fine tuning may be necessary to overcome catastrophic forgetting. In this context, it is unclear how URIAL performs with catastrophic forgetting?
- **Other minor concerns:**
    - Many points have been repeated across multiple sections in the paper which seems quite unnecessary. Structure of repetition suggests the use of large language models may have been used to write the paper. For instance,
        - Section 1, “Shen et al. (2023) argue that reward models in RLHF can exhibit high inconsistency, resulting in near-random performance when presented with contrastive instructions.” Section 2.3, “Moreover, Shen et al. (2023) show that the reward models in RLHF can perform very inconsistently, yielding a nearly random performance when showing contrastive instructions to them.”
        - Section 1, “For instance, Wang et al. (2023) demonstrate that applying SFT to Llama-13B with self-instruct data (Wang et al., 2022a) results in a significant decrease in its MMLU performance”. Section 2.3, “For instance, applying SFT to Llama-13b with self-instruct (Wang et al., 2022a) results in a considerable decline in its MMLU performance”
        - Section 1, “It is also noteworthy that alignment tuning could potentially cause catastrophic forgetting issues.” Section 2.3, “Besides the aforementioned limitations, tuning-based alignment may also cause forgetting issues in LLMs; These findings imply that alignment tuning may lead to the forgetting of previously acquired knowledge in untuned LLMs.”
    - Perhaps the paper could be restructured:
        - Section 1: Introduction,
        - Section 2: Related work and discussion which systematically discusses pros and cons of SFT and RLHF (for instance, catastrophic forgetting) motivating the use of in-context learning, further followed by novel insights/contributions of URIAL**
        - Section 3:  Methodology which includes Token distribution shifts, Alignment tuning, Limits of alignment tuning, Contrastive alignment, K-shot in-context learning
        - Section 4: Empirical analysis and findings, Multi-aspect evaluation, Baseline methods,
        - Section 5: Related work, Discussion on limitations of URIAL
    - Additional points of concern (Syntactically):
        - Augment figure 2 to show global workflow of the entire model - including dense indexing/semantic embedding, in-context learning, ranking, greedy decoding
    - Additional points of concern (Semantically):
        - Section 3.4, “Additionally, we incorporate stylistic tokens to encourage untuned LLMs to produce knowledgeable outputs”. As established in the premise of the paper, ‘knowledgeable’ outputs are not affected by stylistic tokens.
        - **Alignment is poorly defined

*Rather than analyzing distributions as semantic and stylistic as URIAL does, BEB analyses the LLM distribution as a superposition of ill- and well-behaved components to guarantee alignment theoretically which is a much better approach

### Questions
- While I appreciate the pun in the title: “Aligning untuned LLMs with just the ‘write’ about of in-context learning”, it is unclear as to what is being written here exactly? (in-context learning has no parameter changes and pre-caching to memory to avoid re-computation (section 5) seems to be more of an enhancement to a future version of URIAL.)
- In table 1, 2 and 3, URIAL has an “RA” setting - I am unsure what it is supposed to mean? I believe this to be a typo where the authors probably meant "CA" as in contrastive alignment as explained in the caption?
    - Also in table 1, it’s unclear what the underlined values are supposed to indicate?
    - In table 2, under the Vicuna-v1.5-7b (SFT only) setting, row 1 describes SFT+RLHF which appears to be a clear contradiction?
- Section 4.3, Empirical results and analysis, URIAL exhibits superior performance in relevance, factuality, and engagement aspects, it falls short in safety compared to RLHFed models. Perhaps the authors could discuss potential hypothesis on why this is the case despite contrastive alignment/additional in-context learning step?
- Section 5, Limitation of URIAL: "URIAL adds a bit more computation cost for each inference due to in-context tokens". This computational cost could be quantified/formalised.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper investigates a novel technique of aligning a base Large Language Model (LLM) by in-context learning sorely. It first demonstrates, through a small preliminary experiment, that most of the output token distribution shifts between the base LLM and finetuned LLM appears on the stylistic words. Then based on this discovery, the authors hypothesis that such kind of alignment can be easily obtained through carefully-designed in-context learning samples. Experimental results prove this hypothesis, and show this simple method can beat several strong baselines. Overall, this paper is simple yet insightful for the alignment research community.

### Strengths
This paper first analyzes the token distribution shift and shows that alignment tuning mainly shifts the probabilities of the stylistic tokens, while the knowledge-intensive content originates from pre-training. The findings are clearly demonstrated by an empirical study on 1k samples.

Based on the findings, the proposed in-context alignment method provides a Revised Answer in contrast to an Initial Answer, to prompt the LLM into a human-preferred style.

### Weaknesses
1. The evaluation method is the overall of six aspects, which is compared by ChatGPT and double-checked by humans. However, the proposed prompt method explicitly focuses on these aspects out of six. Thus, better scores on human preference are not surprising for LLMs that are capable of imitating the demos. This makes the experimental results less convincing. Also, in Table 1, the performance superiority is limited.

2. By ‘alignment’, including SFT and RLHF, the LLMs are expected to align with human dialogue as well as to make significant progress on a wide range of downstream tasks. However, the experiments only evaluated the LLM as a chatting agent, which severely narrowed the scope.

3. This long prompt line may hurt the usability of the LLM.

a)	As is mentioned in Section 5, the prompt prefix occupies non-negligible portion of the input window. Thus, the extra computation cost of the prefix is also non-negligible for each sample during inference.
b)	Compared to LIMA, which uses 1k samples for one-time instruct tuning, the advantage in computation consumption (Section 2.3) is insignificant.

4.	It will be better to show some examples of real outputs from URIAL .

5.	It is not clear how the 3 in-context samples in URIAL are created. It is also questionable to have an extra revise answer step. There should be an experiment to compare your method and directly using revised answers.

6.	(Minor) This method totally relies on prompting and the results are not reproducible for now.

a)	Are the K demos for K-shot ICL from random initialization or retrieval on candidate sets that contain similar instructions?
b)	The evaluation set is claimed to be a human-selected representative subset of instruct data, which can be ambiguous.

### Questions
1.	Can you provide some explanation or investigation (maybe with experiments) of why most of the token distribution shifts appear on stylistic tokens?

2.	Can you provide more detailed statistics of the token distribution shifts on different base/aligned models?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
By examining shifts in the token distributions between aligned and base models, this paper analyzes what is learned during alignment tuning. They find that alignment mainly involves learning to use certain stylistic tokens, rather than obtaining new knowledge. Given this insight, they present a curated in-context learning prompt of three examples which achieves alignment on par with existing alignment tuning methods, but without any weight updates.

### Strengths
(1) The paper presents a convincing explanation of what is learned during alignment tuning, which is supported by the prompt they use for alignment.

(2) The alignment method is simple, effective, and interpretable.

(3) The paper is well-written, and the figures are very well done.

(4) The question of what is learned during alignment is potentially very impactful.

### Weaknesses
(1) The idea of aligning by prompting (usually with context distillation) has been explored, and the overall consensus seems to be that it is inferior to RLHF. (See, e.g., https://arxiv.org/pdf/2204.05862.pdf, which uses the Anthropic HHH prompt: https://gist.githubusercontent.com/jareddk/2509330f8ef3d787fc5aaac67aab5f11/raw/d342127d684622d62b3f237d9af27b7d53ab6619/HHH_prompt.txt). On the other hand, in this paper, the authors' prompt seems to work just as well as RLHF. Therefore, the paper would benefit from a discussion of how their prompting strategy differs from existing alignment prompting strategies.

(2) It's not clear to me that the cons (loss in context window space, increased inference time) are worth the benefit of avoiding fine-tuning. My impression is that people are happy to fine-tune (e.g. by context distillation) to free up context space.

(3) I have minor concerns that the prompt would not generalize to models other than LLaMA, due to minor issues with the methodology in the paper. From what I understand, the authors first examined how RLHF changes LLaMA, and they then curated a prompt based on that analysis. Then, they only evaluated the effectiveness of this prompt on the LLaMA model that they had previously analyzed. Therefore, it seems possible that the chosen prompt is competitive with RLHF on the LLaMA model but not on other LLMs, where it might still work but be a bit less effective.

(4) I am a bit skeptical of the evaluation methodology presented in Table 1 because the purpose of these methods is to align with human preferences, yet the evaluation uses GPT4 to score attributes instead. While the authors did ask humans whether they approved of the GPT4 rating explanations, that says nothing about which models the humans prefer. It also doesn't tell us whether the human scores would be correlated with the GPT4 scores because a human might just approve any explanation that seems plausible.

The paper did mention that humans also did some pairwise comparisons, which would address my concern. However, from what I understand, they only report the ChatGPT-based pairwise comparisons and mention that it had ~88% agreement with human comparisons. I would be interested in a table that directly reports the human comparisons.

(5) While the analysis of token distribution shift is interesting, the paper does not present any quantitative analysis, and instead just qualitatively looks at a few examples. For example, one could partition the tokens into categories (e.g. stylistic, content-bearing, ...) and examine which token categories see the most shift from alignment tuning.

### Questions
(1) In Tables 1 and 2, there is a possible typo ("RA" --> "CA").

(2) What was the process for producing the curated prompt?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper examines the research question of what large language models (LLMs) learn during the alignment process. 

The authors compare token distributions between untuned LLMs and their aligned counterparts to quantify changes in model behavior. To achieve this, they query the aligned LLMs and obtain response tokens. For each token, they provide the context (i.e., the query and pre-generated tokens) to both untuned and aligned LLMs, and observe the distribution shift at each inference step.

The researchers identify significant discrepancies in specific stylistic markers, such as transition words and discourse markers, between the untuned and aligned LLMs. As a result, they hypothesize that LLMs primarily acquire knowledge of language style during the alignment process. 

In light of this observation, the authors propose using stylistic examples with in-context learning to perform LLM alignment.

### Strengths
1. The paper is well-written and easy to follow.
2. The motivation is clear: the authors observe the distribution shift on stylistic tokens and propose using stylistic examples to prompt the aligned response.
3. They have developed a comprehensive and interpretable evaluation protocol.

### Weaknesses
1) Section 3.4 is difficult to follow.
    1.1  The process of constructing (or collecting) stylistic, well-structured examples is unclear.
    1.2  It is not evident whether the proposed method is sensitive to the selected examples.

2）Typos in table references make Section 4  hard to follow.

### Questions
1.  What do the different colors represent in the second table in Section 3.4？ What do the bold green words want to highlight?

2. The methodology for designing examples in the proposed URIAL is not provided. This information is crucial for replicating the work and developing new methods.

3. Typos:
    1) Table 3 presents the scores of each method on just-eval-instruct, as estimated by GPT-4, using a scale of 1-10 for each aspect.  --> Table 1 .....
    2) The first row in Table 3 presents .... --> Table 1  
    3) Table 3: The average length of the reponses by each method that are presented in Table 3.  -->  in Table (3?)

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
