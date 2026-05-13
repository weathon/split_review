# Mitigating Hallucination in Large Vision-Language Models via Modular Attribution and Intervention

- Decision: Accept
- Scores: 6, 6, 8, 8

## Abstract
Large Vision-Language Models (LVLMs) exhibit impressive capabilities in complex visual tasks but are prone to hallucination, especially in open-ended generation tasks. This paper explores why LVLMs tend to hallucinate and how to mitigate it. First, we conduct causal mediation analysis through counterfactual edits on specific modules in LVLMs. Our results disclose that Multi-Head Attention (MHA) modules contribute more to the probability of generating hallucination words than multi-layer perceptron modules. We then identify specific heads that are responsible for hallucination, referred to as hallucination heads. Second, we examine the behavior of hallucination heads. We find that they are concentrated in the middle and deeper layers, displaying a strong attention bias toward text tokens. Further, we show that the attention patterns of certain hallucination heads exhibit greater similarity to the base language model and change slowly during the instruction tuning process. Finally, we propose two simple yet effective methods to mitigate hallucination: one is training-free and can be applied directly during decoding, while the other involves fine-tuning. Both methods are targeted for hallucination heads to reduce their reliance on text tokens. Notably, our methods achieve up to 1.7x reduction in hallucination rate for the LLaVA-v1.5-7B model in COCO captioning task, outperforming existing baselines. Overall, our findings suggest that hallucinations in LVLMs are likely to stem from certain modules, and targeted interventions can effectively mitigate these issues.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper observes that some attention heads cause more changes after deactivating them, and name them hallucination heads. There are several characteristics of these heads: (1) they attend more on the images and (2) their parameters move slower than others. Then, the paper proposes one training-free and one training approach to reduce the attention of the hallucination heads on text parts. The experiments on several benchmarks show the benefits of the proposed approach.

### Strengths
1. The observation and analysis on the hallucination heads are interesting and well-motivated.

2. The proposed solutions don't require expensive decoding time.

3. The results on several benchmarks look promising.

### Weaknesses
1. In Section 4.3, the metrics (CHAIR) and the dataset that is evaluated should be explained.

2. In Tables 1 and 2, it would be better if there is an additional column indicating which method is training-free and which is not.

3. The rest please refer to Questions.



### Questions
1. How this method can extend beyond object-level hallucination? For example, do equation (1) and (2) only tell if the existence of the objects but cannot capture if the model incorrectly counts the objects? Then the proposed method can not detect the heads which make hallucination on counting.

2. How many samples is required to compute equation (1)? And what data split do they come from?

3. What's the time required to compute equation (2) to get the scores for all heads?

4. Why the Algorithm 1 directly deactivated the whole text attention weights for the hallucination heads? Isn't it too aggressive as we can see the BLEU scores drop by a lot in Figure 6 (c)? Moreover, why the accuracy on general tasks somehow improves when you apply Algorithm 1? I thought the performance should drop based on the observation in Figure 6 (c).

5. What is the difference between downscaling weight on text attention and upscaling the weight on image attention (Figure 6 (a) and (b))? I thought they meant the same thing as the softmax in attention would keep the sum of text attention and image attention to be one.

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
This work empirically studies the hallucination problem of LVLMS via counterfactual analysis. This work reveals multiple interesting findings on why hallucination occurs and how to mitigate it. The analyses are performed with two models (LLaVA-7B and MiniGPT-4) on two benchmark datasets (COCO and MM-Vet).

### Strengths
1. This work shows several interesting observations about hallucination, as summarized in the sentences in the bold font in section 4. 

2. Based on the findings, this work proposes two simple ideas to mitigate hallucination – adaptive deactivation and targeted fine-tuning of hallucination heads.

### Weaknesses
1. This work fails to cite several related recent works as follows, to name a few.
- They may need to be cited and compared in experiments.
- A. Deng et al., Seeing is Believing: Mitigating Hallucination in Large Vision-Language Models via CLIP-Guided Decoding, arXiv 2024. 
- F. Liu et al., Mitigating Hallucination in Large Multi-Modal Models via Robust Instruction Tuning, ICLR 2024. 
- J. Zhang et al., Reflective Instruction Tuning: Mitigating Hallucinations in Large Vision-Language Models, ECCV 2024. 

2. The evaluation only depends on two CHAIR metrics. 

3. Some findings look obvious.
- It is not so surprising that the multi-head-attention is more critical than feed-forward network, since the former takes a majority of parameters and does much more things than the latter in the transformer.
- It is a well-known fact that hallucination is more related to language bias (rather than) image bias and multimodal models often ignore the information from images compared to that from text.

### Questions
1. More in-depth analysis would be required to discuss why the fine-tuning approach is not as good as the training-free one.

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
5

### Summary
The paper addresses the issue of hallucination in Large Vision-Language Models (LVLMs), specifically focusing on why these models generate content that deviates from the provided image information in open-ended tasks like image captioning. The authors conduct a systematic investigation using causal mediation analysis and counterfactual edits to identify the internal components responsible for hallucination. They find that Multi-Head Attention (MHA) modules contribute more to hallucination than Multi-Layer Perceptron (MLP) modules, and within MHAs, certain attention heads—termed "hallucination heads"—are primarily responsible. To mitigate hallucination, the paper proposes two methods: (1) an adaptive deactivation of hallucination heads during decoding, which is training-free and can be applied directly, and (2) targeted fine-tuning of hallucination heads to reduce their reliance on text tokens. Both methods demonstrate significant reductions in hallucination rates on benchmark datasets like COCO captioning and Nocaps, outperforming existing baselines.

### Strengths
- The paper deploys a systematic step-by-step approach to identify the components responsible for hallucinations. The insights are valuable and the analysis seems sensible.
- Identifying that only specific attention heads seem to contribute to hallucinations is a novel finding. The additional analysis they did (fig 5) is really interesting.
- The mitigation strategies shown (both training-based and training-free) seem sensible and seem to work well on the benchmarks.
- They show the method working with multiple datasets and multiple models.

### Weaknesses
 - There is limited discussion on how the proposed interventions affect the model's overall language generation capabilities. Potential trade-offs between reducing hallucination and maintaining fluency or coherence are not thoroughly examined. Specifically, metrics beyond BLEU, such as human evaluations of fluency and coherence, are absent, making it difficult to assess the practical impact of the proposed methods on the quality of generated text.
- The paper is almost entirely focused on object hallucination. While object hallucination is a significant problem, other forms of hallucination, such as attribute errors, positional inaccuracies, and numerical discrepancies are not addressed. This narrow focus limits the generalizability of the findings and the applicability of the proposed techniques to a broader range of hallucination types.
- The experiments are conducted on 7B parameter models (LLaVA-7B and MiniGPT-4). Given the trend towards larger models in the field, it would be valuable to assess whether the identified hallucination heads and mitigation strategies are applicable to larger models (e.g., 70B parameters) and whether similar patterns emerge at different scales. The absence of experiments on larger models raises concerns about the scalability and practical relevance of the proposed approach.
- There are minor issues with the writing and presentation that could be improved for clarity and professionalism. For example, phrases like "Our Method Run Fast in Generation" could be rephrased for better readability. Additionally, the paper could benefit from more precise language and clearer explanations of technical concepts.

### Questions
- Can you provide more details on why certain hallucination heads exhibit slow changes during instruction tuning? What factors contribute to this "laziness," and how might future work address this issue?
- Have you evaluated how the proposed interventions affect the overall language generation quality of the models? Specifically, does reducing reliance on text tokens in hallucination heads impact the fluency, coherence, or descriptiveness of the generated captions? It would be helpful to see metrics (human eval) or analyses addressing potential trade-offs.
- Do you think "hallucination heads" exist in the same way in larger scale (eg. 70b) VLMs? Would the same training-free method work similarly on them? Would be interesting to see.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This study explores the causes of hallucination in large visual language models (LVLMs) during complex visual tasks and proposes mitigation measures. First, a causal analysis of specific modules of LVLM based on counterfactual editing found that the multi-head attention (MHA) module contributed more to the generation of hallucinatory words than the multi-layer perceptrons module. The study further identified attentional heads associated with hallucination, which are concentrated in the middle and deep layers of the model and show a strong attentional bias towards text markers. In addition, the patterns of these attentional heads remain relatively similar to the underlying language model and change more slowly during instruction tuning.

### Strengths
(1) It is the first work to analyze the attention map of the output text token of LVLMs and the attention-map of the NLP model, which is enlightening.

(2) This paper proposes two methods to alleviate the hallucination of multi-modal large model. One is to restrict the probability of generating tokens by improving transformer's decoder, and the other is to reduce over-reliance on text tokens by SFT. And the experiment proves that the two methods proposed in this paper are excellent.

### Weaknesses
(1) The training-free method is plug and play, but the methods applied in this paper are too few, only LLaVA and Minigpt4 are included, and the results of other models should be supplemented.

(2) The paper discusses the attention-map relationship of text tokens between LVLMs/LLM. Although the setting is a hallucination problem, this mechanism should be attributed to the cause of LLM. So can datasets be extended to other datasets like ScienceQA, GQA,textVQA, POPE, mmbench, etc.?

### Questions
(1) If it is a task like VQA, the generated text token is only one, and only ABCD is answered, whether this hallucination pattern does not exist. If it is the SFT method, then this result should also be applicable to VQA tasks?

(2) It is written in the paper that the author has hallucinatory attention-head in the middle layer or deep layer. Why is this? The complete distribution of 32 heads was not seen in the supplementary materials.

(3) Has it analyzed the difference between system_token+image token+prompt+output_token hallucination attention head and regular attention head? Is there any difference? Or can it only be observed through output-tokens?

(4)What about the distribution of attention when judging LLMs hallucinations? LLMs unable to generate a caption to an image, right? Therefore, I don't think this kind of attention head observation at the decoder terminal is very reasonable.

### Soundness
3

### Presentation
3

### Contribution
3
