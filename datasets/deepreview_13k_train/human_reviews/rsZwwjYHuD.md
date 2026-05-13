# Self-Introspective Decoding: Alleviating Hallucinations for Large Vision-Language Models

- Decision: Accept
- Scores: 8, 5, 6, 6

## Abstract
Hallucination remains a significant challenge in Large Vision-Language Models (LVLMs). 
To alleviate this issue, some methods, known as contrastive decoding, induce hallucinations by manually disturbing the raw vision or instruction inputs and then mitigate them by contrasting the outputs of the original and disturbed LVLMs.
However, these holistic input disturbances sometimes induce potential noise and also double the inference cost.
To tackle these issues, we propose a simple yet effective method named \textit{Self-Introspective Decoding} (SID). 
Our empirical investigations reveal that pre-trained LVLMs can introspectively assess the importance of vision tokens based on preceding vision and text (both instruction and generated) tokens. Leveraging this insight, we develop the Context and Text-aware Token Selection (CT$^2$S) strategy, 
which preserves only the least important vision tokens after the early decoder layers, thereby adaptively amplify vision-and-text association hallucinations during auto-regressive decoding.
This strategy ensures that multimodal knowledge absorbed in the early decoder layers induces multimodal contextual rather than aimless hallucinations, and significantly reduces computation burdens. 
Subsequently, the original token logits subtract the amplified fine-grained hallucinations, effectively alleviating hallucinations without compromising the LVLMs' general ability.
Extensive experiments illustrate that SID generates less-hallucination and higher-quality texts across various metrics, without much additional computation cost.}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This manuscript proposes to solve the hallucination issue in Large Vision-Language Models (LVLMs). The proposed method named Self-Introspective Decoding (SID) aims to solve the issue with a different decoding strategy compared to existing ones. The Context and Text-aware Token Selection (CT2S) strategy within SID preserves only unimportant vision tokens after the early layers of LVLMs, in order to amplify text-informed hallucinations during the auto-regressive decoding process and guide the LVLMs to produce more accurate outputs. Evaluation was conducted using four representative LVLMs: InstructBLIP, Shikra, LLaVA-1.5, and LLaVA-NeXT. Evaluation metrics include CHAIR, POPE, GPT-4 Assisted Evaluations and MME and MMBench Evaluations. Performance of the proposed SID was compared with Sampling, Greedy, Dola, and LVLM decoding strategies (VCD, ICD, and OPERA). Experiment results demonstrate the effectiveness of SID to generates less-hallucination and higher-quality texts, with lower additional computation cost.

### Strengths
1. The proposed SID with its key component: Context and Text-aware Token Selection (CT2S) strategy is a Training-Free decoding strategy which efficiently and effectively solves hallucination problem in LVLMs without additional costs.
2. Extensive experiments were conducted and several evaluation metrics were applied to verify the effectiveness of the SID in various aspects and the superiority over existing methods.
3. Hyperparameter sensitivity evaluation showed the proposed SID’s robustness to different hyperparameter settings.

### Weaknesses
1. The proposed SID is performed on pre-trained LVLMs, so it’s possible that the performance of SID is limited by those pre-trained models.
2. And currently there’s no solution to specifically tune SID for different LVLMs.

3. Table 1 is not explained clear enough, according to the results whatever methods used, greedy decoding setting always performed better, than what is the significance of considering the constraints in Equ 3?
4. What about the possibility of integrating CT2S with other hallucination alleviation strategies?

### Questions
Major comments:
1. Table 1 is not explained clear enough, according to the results whatever methods used, greedy decoding setting always performed better, than what is the significance of considering the constraints in Equ 3?
2. What about the possibility of integrating CT2S with other hallucination alleviation strategies?

Minor comments:
1. Better to keep names of the metrics consistent, e.g., CHAIRI and CHAIRS might be written as CHAIRi and CHAIRs, to be the same as Table 8-9.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces Self-Introspective Decoding (SID) to alleviate hallucinations in large vision language models. Other available methods either introduce noise or lead to double inference costs. SID offers an alternative using a Context and Text-aware Token Selection (CT2S) strategy that selectively attenuates less important vision tokens in early decoder layers. This reduces irrelevant hallucinations in the generations. The approach requires minimal additional computational resources. The paper presents multiple empirical results to show that the method reduces hallucinations while preserving text quality.

### Strengths
- The proposed approach does not require additional computational resources
- GPT-4 assisted analyses were done to calculate Sentence-level Hallucination Ratio
- The paper is well written

### Weaknesses
 - The paper does not present the results on different benchmarks to show the preservation of LVLM ability. LVLMs should be extensively tested on a variety of benchmarks that test different skills, like - MathVision and Mathvista for mathematical reasoning, MMMU for college-level knowledge on various subjects, MM-Vet/v2
- The paper does not cover a comprehensive set of baselines - Woodpecker (https://arxiv.org/abs/2310.16045), LRV (https://www.researchgate.net/publication/375596083), LURE (https://arxiv.org/pdf/2310.00754)
- "Hallucination, defined as the generation of irrelevant, factually incorrect, or meaningless text in a given context." The approach aims to tackle hallucinations in LVLMs as a whole but does not mention or tackle style hallucinations or biases introduced when LVLMs are instruction-tuned.

-Minor:
(typo) Figure 2 - Gnerated

#256 validate

### Questions
1. How does the performance of the proposed approach vary across different LVLM sizes? Do we have any results for larger and smalled LVLMs? (other than 7B)
2. Where does the proposed approach fail to mitigate hallucinations?

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
4

### Summary
This paper proposes Self-Introspective Decoding (SID) for mitigating hallucinations in Large Vision-Language Models (LVLMs). The authors specifically observe that LVLMs are capable of introspectively assessing the importance of vision tokens based on preceding tokens. Based on this, the authors propose a Context and Text-aware Token Selection ($\text{CT}^2\text{S}$) strategy to amplify fine-grained hallucinations, which are ultimately mitigated using a contrastive decoding method. Comprehensive experimental results across various benchmarks demonstrate that the proposed SID outperforms other contrastive decoding baselines in alleviating hallucinations in LVLMs, while also achieving lower computational cost.

### Strengths
1. The proposed method seems novel and interesting. The motivation is also clear.
2. Through empirical experiments, the authors highlight that current vision-and-text agnostic contrastive decoding methods can introduce uncertainty noise and degrade performance. This provides valuable insights for future research.
3. The experimental results are comprehensive and promising, effectively validating the effectiveness of the proposed approach. Efficiency comparisons further highlight the proposed method’s advantage over other contrastive decoding approaches.
4. The authors provide the code implementation for this work, enhancing its reproducibility (though I have not run the code myself).







5. The writing and presentation of this paper is good.

### Weaknesses
1. The proposed method shares some similarities with AVISC [1], which also identifies less-important visual tokens for contrastive decoding. A detailed discussion of these similarities, along with a comparison of experimental results, would strengthen this paper.
2. In Figure 6, pruning all vision tokens results in less than a 0.5% performance difference from the optimal setting, suggesting that the proposed strategy of selecting the top-k least important tokens provides only marginal performance gains. Additionally, could you clarify the statement, “*The loss of vision information for subsequent decoder layers results in losing the visual context, leading to aimless hallucinations without sufficient vision grounding*”? Are there any examples or experiments that illustrate this? Specifically, how does the model behave when *all* vision tokens are removed, and what does this imply about the method's reliance on specific visual information?
3. The proposed method achieves marginal performance improvements on the MME and MMBench benchmarks. Could you please include the standard deviations for the two benchmarks, as their performance is sensitive to random seeds?
4. The proposed method may lack interpretability, as the selected less important tokens (shown in Figures 3 and 4) do not carry true semantic meaning, unlike other contrastive decoding approaches such as HALC [2]. Besides, the proposed method seems not very reasonable when applied to simple LVLMs such as InstructBLIP, which only has 32 vision tokens. In this case, preserving only the least important tokens provides a very coarse measure of vision importance and is unlikely to effectively induce vision-and-text association hallucinations.

Minor issues:
1. In Table 6, is the inference time calculated per instance or for the entire benchmark?
2. Wrong citation format in Line 910.
3. In Table 1, why are there no standard deviations reported for the VCD method in the Sampling setting? Additionally, are the three experiments conducted using three different random seeds? The reported deviations are lower than expected.

### Questions
1. In Table 1, the authors demonstrate that removing the adaptive plausibility constraint resulted in lower performance degradation for the proposed method on the POPE benchmark. Does this also hold for the open-ended CHAIR benchmark and the more comprehensive MME benchmark?
2. How do you define vision-and-text association hallucination?
3. What is the specific experimental setup in Figure 5? Why does ID produce entirely inconsistent responses?
4. How do the proposed method and other baselines perform on the Existence, Count, Position, and Color subsets of the MME benchmark?
5. The experiment in Lines 346-362 is interesting. However, the rationale behind why adding underperforms the proposed method is unclear. From my understanding, boosting the target logits of the original prediction could also enhance discrimination.

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
5

### Summary
1) The main contribution os the paper is proposing that some vision tokens with low attention scores can induce hallucinations while decoding. 
2) The paper backs this up by conducting experiments to prove that low score vision tokens focus mainly on unrelated regions in the image. 
3) The paper does extensive ablations on till which layer to prune vision tokens and comparison with other baselines.

### Strengths
1) Presentation of the paper is clear and straightforward.
2) The paper does a good set of experiments to support their argument that low importance score tokens induce hallucinations.
3) The paper does sufficient ablations and evaluations to prove its approach.

### Weaknesses
1) An important baseline the paper has missed is a simple but effective one, how would the comparison look if we append the image description before asking a question? Ask the LVLM to describe the image and append it to the question and pass through the model again and see if it has any improvement. Some research on this includes - Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs (Ghosh et al, 2024).

2) A few more important benchmark comparisons are needed - MathVista, MMVet, LLaVA-Bench, MMMU

### Questions
Refer to weakness section.

### Soundness
3

### Presentation
3

### Contribution
3
