# SCALE: Synergized Collaboration of Asymmetric Language Translation Engines

- Decision: Reject
- Scores: 6, 6, 5

## Abstract
In this paper, we introduce SCALE, a collaborative framework that connects compact Specialized Translation Models (STMs) and general-purpose Large Language Models (LLMs) as one unified translation engine. By introducing translation from STM into the triplet in-context demonstrations, SCALE unlocks refinement and pivoting ability of LLM, thus mitigating language bias of LLM and parallel data bias of STM, enhancing LLM speciality without sacrificing generality, and facilitating continual learning without expensive LLM fine-tuning.
Our comprehensive experiments show that SCALE significantly outperforms both few-shot LLMs (GPT-4) and specialized models (NLLB) in challenging low-resource settings. Moreover, in Xhosa to English translation, SCALE experiences consistent improvement by a 4 BLEURT score without tuning LLM and surpasses few-shot GPT-4 by 2.5 COMET score and 3.8 BLEURT score when equipped with a compact model consisting of merely 600M parameters. SCALE could also effectively exploit the existing language bias of LLMs by using an English-centric STM as a pivot for translation between any language pairs, outperforming few-shot GPT-4 by an average of 6 COMET points across eight translation directions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a framework to combine Large Language Models (LLMs) and Specialized Translation Models (STMs). Specifically, The authors first sample translation candidate from a STM. Then they combine 1) source sentence, 2) STM's translation and 3) ground-truth reference into a triplet. By providing 10 triplets as demonstrations, LLMs learn through in-context learning and refine STM's translation. Further experiments show its superiority in low-resource translation and continual learning.

### Strengths
1. This work is comprehensive, with both the main experiment and the analysis experiment effectively conveying the author's perspective. The writing is clear and well-structured.

### Weaknesses
1. The idea is relatively straightforward. The SCALE framework and experiments are more engineering-oriented, lacking scientific insight.

2. The baselines used for comparison are weak. There are many previous works, such as back translation, pretraining, and other improvements for low-resource languages, which may require fewer resources and perform better.

3. Inference cost. The SCALE model involves two types of decoding:  STM decoding and LLM decoding. It is important to examine the computational cost associated with the inference process of the SCALE model.

### Questions
1. Why not conduct translation experiments on languages with slightly higher resources, such as German, French, or Chinese? In these languages, the improvements of SCALE may be limited.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a framework SCALE, to incorporate the translation ability of a specialized model into a LLM. The idea is to provide the results of a STM as extra input to the LLM, and let LLM generate new translations considering the input. This idea is quite simple and effective. It also works well in providing updating translations for refinement, pivoting and updating purposes.

### Strengths
The paper demonstrated a nice way of incorporating STM into LLMs.

The method is useful in three different senarios (refinement, pivoting and updating) in almost the same way.

According to the evaluation, the results are better than both the STM and LLMs.

### Weaknesses
My main concerns are in the analysis part:

For the analysis in 5.1, although the perplexity of a GPT2-XL decreases after SCALE refinement, there is no evidence that the results of larger LMs decreases as well. It is highly likely that the original results are more preferred by GPT4 than the refined results.

It is not straightforward to me why the STM results are with higher NM score than GPT4, but based on these results, SCALE achieves results with lower NM than GPT4.

It is not even clear for me whether the NM or USW should be higher or lower. According to the analysis, GPT4 produces results that are more literal (which is bad ), while STM have results more figurative. But it seems to me that GPT4 understand source languages better than STM, which is more likely to generate figurative translations.

Besides, since the LLMs learn how to use the latent variable Z by the examples, it might be extremely important to choose proper demonstrations. It will be useful to check the effects of different demonstrations.

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces the SCALE framework, which integrates specialized Translation Models (STM) with Large Language Models (LLMs) such as GPT-4, utilizing triplet examples for few-shot learning. Each triplet incorporates an additional element: a translation generated by the STM, supplementing the standard source and target sentences. The study demonstrates significant enhancements in translating from various low-resource languages into English (X→En). Furthermore, the paper conducts ablation studies to show the individual contributions of each SCALE component to the overall performance improvement.

### Strengths
- The paper is easy to understand and well written.
- The idea is simple but effective. The SCALE framework shows substantial improvement for low-resource languages when translating into English.
- The paper did a good ablation study to show the essential role of each component in the SCALE framework.

### Weaknesses
Major weaknesses:
- I like the idea; however, the paper focuses on translation into English and does not demonstrate the efficacy of translating from English to these low-resource languages. I suspect that SCALE has limitations in translating from English, given that refinement is core to SCALE. Although GPT-4 excels in English, it falls short in low-resource languages, suggesting that SCALE may not be effective for En→X.
- SCALE seems confined to low-resource languages, as LLM already performs excellently in translating between high-resource languages, such as German and French. The paper should make it clearer for readers how SCALE fares in the context of translating high-resource languages.
- In presenting "pivoting" (Sec. 4.2) and "updating" (Sec. 4.3), the paper restricts its experiments to LAO→En and Xhosa→En, respectively, which doesn't sufficiently substantiate this aspect. Conducting more comprehensive experiments would provide stronger support for the concept.

Minor weaknesses:
- The paper's assertion that SCALE "mitigates both language bias and parallel data bias" seems peculiar to me. It feels intuitive rather than conclusively factual. Defining "language bias" and "parallel data bias," followed by a quantitative analysis, might be necessary for clarity.
- The choice of a less advanced model like GPT-2 for evaluating GPT-4's fluency strikes me as odd. While employing GPT-2 might yield reasonable comparative results for less sophisticated generation models, but I do not think it is proper here.

### Questions
I would be appreciate if the authors can address my concerns above!

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair
