# Don't Take Things Out of Context: Attention Intervention for Enhancing Chain-of-Thought Reasoning in Large Language Models

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Few-shot Chain-of-Thought (CoT) significantly enhances the reasoning capabilities of large language models (LLMs), functioning as a whole to guide these models in generating reasoning steps toward final answers. However, we observe that isolated segments, words, or tokens within CoT demonstrations can unexpectedly disrupt the generation process of LLMs. The model may overly concentrate on certain local information present in the demonstration, introducing irrelevant noise into the reasoning process and potentially leading to incorrect answers. In this paper, we investigate the underlying mechanism of CoT through dynamically tracing and manipulating the inner workings of LLMs at each output step, which demonstrates that tokens exhibiting specific attention characteristics are more likely to induce the model to take things out of context; these tokens directly attend to the hidden states tied with prediction, without substantial integration of non-local information. Building upon these insights, we propose a Few-shot Attention Intervention method (FAI) that dynamically analyzes the attention patterns of demonstrations to accurately identify these tokens and subsequently make targeted adjustments to the attention weights to effectively suppress their distracting effect on LLMs. Comprehensive experiments across multiple benchmarks demonstrate consistent improvements over baseline methods, with a remarkable 5.91\% improvement on the AQuA dataset, further highlighting the effectiveness of FAI.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper analyzes how tokens in demonstration examples influence chain-of-thought reasoning. Based on their findings, the authors propose a method to block token information flow using attention scores. Experimental results demonstrate the effectiveness of this approach.

### Strengths
- The analysis results are interesting and insightful.

### Weaknesses
 - The analysis is done with saliency scores while the proposed method is based on attention scores. It is not clear to me that if attention scores will exhibit similar behavior to saliency scores. If the proposed method uses attention scores, the analysis should also be presented using attention scores to ensure consistency.
- Section 3.3 needs further elaboration. In Figure 1, it seems that certain tokens in the demonstration examples receive "high scores," which could potentially disrupt the reasoning process. My understanding is that the authors aim to adjust attention to reduce this distraction. However, in intervening with the information flow (Section 3.3), the authors block attention only for tokens with "no significant information aggregation" rather than focusing on high-impact tokens. This seems like a mismatch. Please correct me if I misunderstand.
- Figure 1 is somewhat misleading. Figure (a) and (c) show predictions for the next token at the start of a new sentence, while (b) and (d) show predictions in the middle of a sentence or even during equation completion. This difference may explain the substantial variation in score distribution. I assume that the cases in (a) and (c) are simpler and may not effectively support the authors' claims. I would like to see some other examples for (a) and (c), particularly those involving equation completion, to demonstrate the motivation.

### Questions
Please see above.

### Soundness
2

### Presentation
2

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
The authors focus on the failure mode of few-shot CoT. Specifically, they find that the demonstration selection will affect CoT's reasoning dynamic by distracting models with specific tokens. For example, models will use in-context examples, conditions, and numbers. To verify this phenomenon, authors first use a saliency map and shows that sometimes models put overwhelming attention on numbers of in-context examples, leading to an incorrect answer. 

To solve the problem, authors use the self-attention score as an indicator of information aggregation and classify tokens that have high self-attention score as a distractor. Therefore authors remove these tokens when decoding to mitigate their effect.

Results on math reasoning, commonsense reasoning, and other tasks show the method's effectiveness in enhancing few-shot CoT performance.

### Strengths
* The topic is interesting and brings novel insight into understanding the few-shot CoT dynamic.

* The method is conceptually simple, implementation simple, and does not bring extra computation gains (only a constant computational overhead)

* The results are significant on various tasks with Llama 3 8B.

* Clear writing and figures.

### Weaknesses
 * Authors use the aggregation of self-attention as an indicator of information flow. While it makes some sense intuitively, more supporting evidence is needed. For example, in the error case 2(b), can this method identify the same token as the saliency map?

* A case study is needed. Can authors provide several examples and highlight the tokens selected by the method? It will be very useful to observe the approach's token selection to understand its advantages and drawbacks.

* More analysis of the saliency map. Figure 2 shows the failure attention pattern on specific layers and heads, but it is unclear if this only occurs in a few layers and heads. What do other heads' and layers' attention patterns look like?

### Questions
* Can authors add zero-shot results in Table 2 and Table 4? It will be helpful to know how better the few-shot CoT is.

* Does the attention-dropping only apply to the tokens between decoding and in-context examples? For example, will tokens between different in-context examples also have attention-dropping, and will different decoding tokens have attention-dropping among themselves?

* line 73: "has not experienced significant information aggregation" should be the case that alpha is larger than tau rather than smaller than tau?

* line 45, 133, 139: \citet -> \citep

### Soundness
2

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
This paper proposes FAI that dynamically analyzes the attention patterns of demonstrations to accurately identify these tokens, followed by targeted adjustments to the attention weights to effectively suppress their distracting impact on LLMs. Comprehensive experiments across various benchmarks validate the effectiveness of FAI.

### Strengths
1.	The proposed FAI offers a new perspective for analyzing the impact of few-shot CoT on responses generated by LLMs. It enables LLMs to focus more on global information rather than individual tokens. 

2.	The motivation is illustrated with examples to aid reader understanding. The method is clearly described, and the experiments are extensive in scope.

### Weaknesses
1. FAI is kind of incremental. It modifies the attention weight matrix to intervene in information aggregation, thereby improving the effect of CoT. However, the method is largely built on the single-step saliency scoring approach like Wang et al. (2023b) and simply identifies a threshold to block the information flow between the layers in the LLMs by attention, this is also done in the traditional pre-trained language models. However attention-based saliency scoring is also widely discussed by existing studies [1]. In this way, the paper offers limited innovation.

2. The experimental analysis is insufficient and should be validated on more models. Please see the fourth question below.

3. The description of details needs further refinement which can be seen in the questions below.

### Questions
Major Questions
1. Compared with the method proposed by Wang et al. (2023b) that introduces a learnable parameter to dynamically modify the attention weight matrix, what are the advantages and innovations of this method? The authors claim that “while the saliency score emerges … alternatives.” from line 246 to 248. Can you explain more about this or conduct an analysis of the complexity comparison between these two? BTW, how to identify the hyper-parameter $\lambda$ in the method?

2. At line 134, the author mentions that existing single-step methods may overlook crucial information, and the proposed method has more advantages due to its ability to dynamically adjust the attention weight matrix at each step. However, these baselines were not compared in the experimental part. Experimental analyses need to be given that the proposed method is better than single-step ones. In addition, since this method modifies the attention weight matrix at each step, it seems to be more time-consuming than single-step methods, so relevant experimental analysis also needs to be provided. 

3. The figures are blurry. For example, in Figure 2, why do the positive examples (a) and (c) use the previous layer to indicate significance, while the negative examples (b) and (d) include all previous layers? This seems unfair. Would the first 30 layers in (a) achieve the same effect as in (b) and (d)? And would the 14th layer in (b) produce a similar effect to (a) and (c)? A more thorough explanation is needed here.

4. How about we apply FAI to larger models such as Llama-3-70B? Or LLMs in other series such as GPT2-XL (1.5 Billion parameter) and GPT-NEO-2.7B? The experiments are not sufficient and should be verified on more types of models with different parameters.

5. The author selects samples with an accuracy rate greater than 90% as GSM_bad, but lacks reasons. Is there some experiment or analysis that can support the idea that the errors in them are more likely to be caused by the distracting effect? I think visualization towards the FAI attention is helpful.

6. What are the limitations of FAI? Even though the authors showcase some examples of the four error categories in A.2.1, I am interested in what examples it tends to answer incorrectly that could otherwise be answered correctly without FAI? In addition, what examples does it tend to answer incorrectly even with FAI?

Minor Questions
1.	Why does the attention weight matrix in Figure 3 exclude the query question in Layer n but include it in Layer n+1?

2.	The description on lines 273 to 274 contradicts the description on lines 260 to 263.

3.	There is no explanation of Table 3.

4.	How is RAFR calculated?

5.	What does “contrastive” in Figure 4 stand for?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper explores the issue of localized distractions within CoT in LLMs. While CoT enhances LLM reasoning by guiding models through structured reasoning steps, isolated tokens or phrases in the demonstrations can mislead the model, causing it to focus excessively on irrelevant details, which disrupts its reasoning process. To mitigate this, the authors propose a Few-shot Attention Intervention (FAI) method. Through experiments on multiple reasoning benchmarks, FAI demonstrates consistent improvements,  indicating its effectiveness in enhancing CoT robustness without extensive computational overhead​.

### Strengths
1. The idea is novel, and the research question is interesting and valuable.
2. The paper is clearly structured, with fairly extensive experiments and the results show good potential.

### Weaknesses
1. The paper citation format is improper, and \citet{} and \citep{} are not used appropriately.
2. The experimental settings are not clear (especially the hyperparameter settings of the model, like decode strategy, max_new_token), which is not conducive to reproduction.

### Questions
I noticed that all your experiments were conducted on cloud servers with 8 A100 GPUs, so why did you only evaluate 7B~13B models?

### Soundness
3

### Presentation
2

### Contribution
3
