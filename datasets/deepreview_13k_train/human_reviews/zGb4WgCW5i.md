# Intervening Anchor Token: Decoding Strategy in Alleviating Hallucinations for MLLMs

- Decision: Accept
- Scores: 6, 6, 8, 8

## Abstract
Multimodal large language models (MLLMs) offer a powerful mechanism for interpreting visual information. However, they often suffer from hallucinations, which impede the real-world usage of these models. Existing methods attempt to alleviate this issue by designing special decoding strategies that penalize the summary tokens. However, these methods lack analysis of the relationship between hallucination and summarization mechanism of LLMs. Interestingly, we find that penalizing summary tokens is not necessary: merely intervening the query-key parameters variance, without costing extra inference time, still alleviates hallucinations. Specifically, we explore the causes of hallucinations by analyzing localized self-attention patterns called ``anchor" tokens and define the attention localization degree of the model as token propagation probabilities. Our analysis reveals that over-propagation of anchor tokens occurs when the distribution of eigenvalues of the query and key matrices has a non-zero mean and a polarized variance, leading to excessive dependence on anchor tokens while neglecting vision information and describes the image content with hallucination. Based on the observation, we propose a versatile plug-and-play decoding strategy, Dynamic Token Propagation Mechanism (TAME), to alleviate excessive propagation by dynamically intervening the eigenspectrum variance of the attention weight, thereby alleviating hallucinations without relying on complex decoding strategies. Extensive experiments reveal a correlation between the eigenspectrum and hallucinations across various MLLMs, and show that TAME reduces the percentage of hallucinated objects.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores the role of anchor tokens in causing hallucinations in LLMs, and proposed Dynamic Token Propagation Mechanism (TAME) based on eigenspectrum variance of the attention weight. The results show that TAM can be integrated with existing decoding method including Beam/VCD/ICD/SID and improve the performance consistently on InstructBLIP, MiniGPT-4, LLaVA-1.5, and Shikra.

### Strengths
1. Simple method which is very easy to use
2. Good insights from eigenspectrum variance
3. Constantly improve the decoding methods of InstructBLIP, MiniGPT-4, LLaVA-1.5, and Shikra.

### Weaknesses
1. I hope the paper could explore additional approaches to reduce hallucinations, such as Retrieval-Augmented Generation (RAG), Reinforcement Learning from Human Feedback (RLHF), improvements in factuality metrics, and high-quality, data-based instruction tuning.

2. The paper currently uses the a few simple eval sets like MS COCO. I would suggest incorporating more challenging benchmarks for a more rigorous assessment.

3. The writing could benefit from refinement. For instance, many citations are not in the correct format.

4. The paper only reports metrics for hallucination. But it is not clear the new predictions do better or worse in other metrics. Sometimes less hallucination may lead to less details or not as friendly to users to read.

### Questions
1. in Table 1: the baselines with max token 512 generate very high hallucination (>30%). Is it aligned with user's experience? At least I feel Gemini and ChatGPT's numbers should be much better than that.

2. I feel the proposed method can be used for any LLM based method. Why does the title claim it only for multimodal LLMs?

### Soundness
3

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
3

### Summary
This paper investigates the causes of hallucinations in LVLMs through the attention weight matrix of anchor tokens. Then this paper demonstrates the propagation pattern of anchor tokens by the eigenspectrum of the attention weight matrix. The authors further propose a versatile plug-and-play decoding strategy named Dynamic Token Propagation Mechanism (TAME) to reduce the over-propagation of anchor tokens through dynamically intervening in the eigenspectrum variance. Extensive experiments show that TAME improves hallucination metrics across multiple MLLMs.

### Strengths
1.	This paper provides a solid theoretical framework by analyzing the relationship between LVLM hallucinations and attention patterns.
2.	This paper introduces a novel plug-and-play decoding strategy that dynamically adjusts the eigenspectrum variance of attention weights to mitigate hallucinations without adding inference time.
3.	Extensive experiments show that TAME improves hallucination metrics across multiple MLLMs.
4.	TAME can be integrated into various decoding strategies without requiring additional training or data.

### Weaknesses
1.	Although this paper provides an additional theoretical framework, the impact of anchor tokens on the LVLM hallucination was first proposed by OPERA [1].
2.	TAME primarily addresses object hallucinations but may not be as effective for other hallucination types, such as incorrect attributes or relations (e.g., limited performance improvement on the MME benchmark). Experiments on more types of hallucination should be conducted. Specifically, the evaluation should include a more granular analysis of different attribute hallucination types, such as color, size, and material, to assess the method's robustness across various scenarios.
3.	It would be interesting to study applying TAME to some layers rather than all layers through experiments. The current study lacks an ablation study to determine the optimal layer configuration for applying TAME, and whether applying it to specific layers or combinations of layers could yield better performance or computational efficiency.

### Questions
Please see the weakness.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
MLLMs encounter hallucination issues, where the generated text does not match the provided visual content. Previous methods have attempted to mitigate hallucinations by designing special decoding strategies, such as penalizing summary tokens, but they lack an analysis of the relationship between the model’s hallucinations and the summary mechanism. In this paper, a study and analysis of the causes of hallucinations in MLLMs are presented. A general decoding strategy, TAME, is proposed to reduce the excessive propagation of anchor tokens by dynamically intervening in the variance of feature spectra. Experiments demonstrate the correlation between feature spectra and hallucinations in MLLMs, as well as the effectiveness of TAME.

### Strengths
1. The motivations are strong, with in-depth analysis and derivation of the mechanisms behind hallucinations in MLLMs.
2. The proposed method, TAME, is a simple and effective plug-and-play decoding strategy.
3. The experiments are thorough, validating both the causes of hallucinations mentioned in the paper and the effectiveness of the proposed method.

### Weaknesses
1. The introduction mentions summary tokens but does not define them, leaving unclear the distinction between summary tokens and anchor tokens.
2. There are some typos in the text that need to be checked:
   1. Line 301: "Conversly" -> "Conversely"
   2. Line 333: "7,3" -> "7.3"

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes a new decoding method to address hallucination issues in multimodal large language models (MLLMs). The authors identify that excessive propagation of “anchor tokens”, influenced by polarized variance in the attention mechanism’s eigenspectrum, contributes to hallucinations by sidelining crucial visual information. To mitigate this, the paper introduces the Dynamic Token Propagation Mechanism (TAME), a plug-and-play decoding strategy that adjusts the eigenspectrum variance in the attention weights, limiting over-propagation without adding to inference time. Extensive experiments demonstrate that TAME effectively reduces hallucinations across multiple MLLMs and achieves great improvements over existing methods like Greedy Decoding and Visual Contrastive Decoding (VCD). The method is simple-yet-effective and easy to implement.

### Strengths
1. The paper is well-written and clear motivated. The authors begin by introducing hallucinations and related work, gradually diving deeper by focusing on the phenomena of token information flow and information aggregation, ultimately leading to the proposal of TAME. 

2. This paper is built on a detailed and clear theoretical foundation. Although the proposed method appears simple, the step-by-step theoretical derivation strongly supports it. 

3. The proposed method is simple-yet-effective, which obviously surpasses all baselines on CHAIR, POPE and GPT-4 assisted hallucination evaluation. Meanwhile, the method introduces no additional computation overhead, which is superior to existing contrastive decoding based methods.

### Weaknesses
1. Some of the color schemes in the figures, such as Figures 4 and 5, are prone to causing confusion. It is recommended to use colors with higher contrast and more distinct differentiation.

2. The paper begins its analysis with the phenomena of token information flow and token information aggregation, gradually developing a method to mitigate hallucinations. However, it does not yet discuss the underlying causes or triggers of these phenomena, only relying on empirical analysis. Nevertheless, the analytical approach used in the paper is still worth learning from.

3. The paper provides limited explanation of the proposed method. Although the method is simple (just one single formula), a smoother transition from the theoretical derivation is needed, along with a clear description of its application scenarios.

### Questions
1. In the qualitative results, it appears that the proposed method tends to make the model’s output shorter, which is expected, as the goal is to reduce hallucinated content. However, from another perspective, could this lead to insufficient perception of the image by the model, potentially missing some details? If so, how could we measure and balance this trade-off?

2. The example in Figure 6 is somewhat unclear, as it’s difficult for reviewers to determine which parts of the image or which specific patches correspond to the enhanced visual tokens. Could the authors provide a visualization of the relevant visual tokens mapped onto the image?

### Soundness
4

### Presentation
3

### Contribution
4
