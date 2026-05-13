# Large Language Models can be Strong Self-Detoxifiers

- Decision: Accept
- Scores: 6, 6, 6, 6, 6

## Abstract
Reducing the likelihood of generating harmful and toxic output is an essential task when aligning large language models (LLMs). Existing methods mainly rely on training an external reward model (i.e., another language model) or fine-tuning the LLM using self-generated data to influence the outcome. In this paper, we show that LLMs have the capability of self-detoxification without the use of an additional reward model or re-training. We propose \textit{Self-disciplined Autoregressive Sampling (SASA)}, a lightweight controlled decoding algorithm for toxicity reduction of LLMs. SASA leverages the contextual representations from an LLM to learn linear subspaces characterizing toxic v.s. non-toxic output in analytical forms. When auto-completing a response token-by-token, SASA dynamically tracks the margin of the current output to steer the generation away from the toxic subspace, by adjusting the autoregressive sampling strategy. Evaluated on LLMs of different scale and nature, namely Llama-3.1-Instruct (8B), Llama-2 (7B), and GPT2-L models with the RealToxicityPrompts, BOLD, and AttaQ benchmarks, SASA markedly enhances the quality of the generated sentences relative to the original models and attains comparable performance to state-of-the-art detoxification techniques, significantly reducing the toxicity level by only using the LLM's internal representations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper pinpoint that large language models are able to conduct self-detoxification. Consequently, this paper proposes a novel method entitled Self-disciplined Autoregressive Sampling (SASA), for constraint decoding, to reduce the toxicity of LLMs.  More specifically, it leverages the representations from an LLM to learn linear subspaces which explicitly distinguish the toxic from non-toxic output.

### Strengths
[1] The proposed method which utilizes a learned hyperplane to justify the toxic generation is quite interesting.

[2] The proposed methods surpass all the baselines in the experiments

### Weaknesses
[1] **The title may still be overclaimed.** Since the supervised data is still required to learn the  hyperplane, the title actually misleading readers that the proposed method is a pure unsupervised approach.

[2] **Though interesting, the proposed methods are not fundamentally different from learning an external model to detect toxic content.** The observation that LLM’s hidden state is able to demonstrate the toxic content is also widely acknowledged. The contribution of the paper mainly lies in the proposed approach part, which from my understanding is still quite limited.

[3] **Limitations on nonlinearly separable hyperspace settings are not well demonstrated.** Followed by support vector machines (SVMs), a natural limitation for support vectors is the nonlinearly separable hyperspace settings. Though such a limitation would be tackled by projection kernels, a natural limitation is that, if the raw features (from LLMs) could not explicitly generate linear separable spaces, the proposed strategy may not achieve strong results. In contrast, other approaches (i.e. external generative detoxifiers) may not suffer from such an issue.

### Questions
See weakness.

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
5

### Summary
This paper explores the capability of large language models (LLMs) in reducing harmful and toxic outputs, proposing a lightweight controlled decoding algorithm called Self-disciplined Autoregressive Sampling (SASA). SASA can reduce the toxicity of the generated content from LLMs without the need for an additional reward model or retraining. SASA leverages contextual representations from LLMs to learn linear subspaces that characterize toxic versus non-toxic outputs in analytical forms. During the automatic completion of responses, SASA dynamically tracks the margin of the current output and adjusts the autoregressive sampling strategy to steer the generation process away from the toxic subspace. SASA was evaluated on LLMs of different scales and natures, including Llama-3.1-Instruct (8B), Llama-2 (7B), and GPT2-L models, using benchmarks such as RealToxicityPrompts, BOLD, and AttaQ. The results show that SASA significantly enhances the quality of the generated sentences and achieves performance comparable to state-of-the-art detoxification techniques, significantly reducing the toxicity level by only using the internal representations of the LLMs.

### Strengths
1.**Innovativeness**: The paper introduces a novel decoding method called Self-disciplined Autoregressive Sampling (SASA). This method distinguishes between toxic and non-toxic outputs by learning a linear subspace, thereby achieving self-detoxification without the need for additional reward models or retraining. This approach is highly innovative both theoretically and practically.

2.**Theoretical Support**: The paper provides a detailed proof of the optimal solution to the proposed optimization problem and offers a specific formula to adjust sampling probabilities, which solidly underpins the effectiveness of the method.

3.**Extensive Experimental Validation**: The paper conducts extensive experiments on multiple large-scale language models, including Llama-3.1-Instruct (8B), Llama-2 (7B), and GPT2-L, using benchmark datasets such as RealToxicityPrompts, BOLD, and AttaQ. The experimental results show that SASA performs well in reducing toxicity, achieving performance comparable to existing state-of-the-art methods.

4.**Lightweight**: As a lightweight decoding algorithm, SASA does not require additional training or complex external models. This decoupled approach makes it easier to deploy and use in practical applications. Motivation is clear.

### Weaknesses
1.**Lack of evaluation on common sense knowledge**. We believe that a good proxy model should be both helpful and non-toxic. Therefore, this paper needs to systematically investigate whether SASA leads to catastrophic forgetting of common sense knowledge in the model's outputs. Just like when eliminating backdoor attacks [1] on models, it is necessary to simultaneously consider the recovery of the model’s original capabilities, and self-distillation [2] aims to maintain the model's ability to retain source domain knowledge while solving efficient continual pre-training.

2.**The dynamic adjustment strategy during decoding needs further study for long texts.** Considering that semantic changes in long texts are more complex, finer control will be a challenge.

3.**Adequacy of Baselines**: The sufficiency of the baselines needs to be considered. I noticed that RAD is a work from 2023, so more recent research should be included for comparison to ensure a comprehensive evaluation.

4.**Outdated Backbone Models**: Should the main experiments in Tables 1-3 be conducted on more recent models, such as Llama-3.1, to ensure that the results are up-to-date and relevant? And why was a comparison with PAD not included in the experiments reported in Table 6 for Llama-3.1?

### Questions
1.Is there a need to further explore how to balance generation quality and toxicity?

2.How effective is the detoxification of this method for long texts?

3.The method designed in this paper is lightweight; however, there are similar ideas in the fields of personalization alignment [3] and factuality enhancement [4], which also aim not to rely on external critic models or additional model training, but to be deployed only during inference decoding. What common insights do SASA and these similar methods in different fields share? What is at their core? When designing methods with similar ideas in a new domain, what guidance can be provided?

4.If we have a well-trained critic (whatever we call it) model that can guide the model's decoding to detoxify output, such a method seems decoupled as well—meaning we just need to train one detoxification model, and then it can guide the incomplete output paths of all models. What are the issues with this approach?

5.Is there hope that models can solve such problems through long chain-of-thought (CoT) reasoning (or planning), rather than hoping to address specific scenario issues with specific decoding strategies during decoding? After all, if one aims to consider factuality [4], personalization [3], and safety [this paper] simultaneously, wouldn't using multiple decoding strategies to guide the model in real-world scenarios become overly complex? What is the author's view on the future development of proposals based on long CoT and self-reflection to tackle the toxicity issue in models？

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
This paper aims to tackle the challenge of minimizing the generation of harmful and toxic outputs. While existing approaches involve retraining large language models (LLMs) or utilizing an external model to guide LLMs in reducing harmful generation, this paper proposes a non-parametric method that constructs toxic and non-toxic subspaces to steer language generation.

### Strengths
1. The primary strength of this approach is its non-parametric nature and its training-free implementation within the context of LLMs. Consequently, this method does not require extensive computational resources.

2. The proposed method demonstrates effectiveness in specific tasks, as it learns subspaces from existing datasets.

### Weaknesses
1. The generalization capability of the proposed method is limited. The subspaces are derived from a relatively small dataset containing approximately 2 million samples, which may result in a lack of generalization to broader scenarios.

2. An increase in perplexity (PPL) is observed as the value of beta increases, which could potentially degrade text quality.

### Questions
1. As the toxicity rate decreases, the generation capability deteriorates, as evidenced by the increased PPL. How severe is this issue for text generation?

2. In comparison to RAD, how would you assess the generalization capabilities of learning toxic subspaces?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents SASA (Self-disciplined Autoregressive Sampling), a controlled decoding method aimed at reducing toxicity in large language model (LLM) outputs without requiring external reward models or model retraining. The key insight is that LLMs' internal representations can capture and distinguish toxic from non-toxic content. SASA leverages these contextual representations to define linear subspaces that separate toxic from non-toxic language. During the token-by-token generation process, SASA dynamically monitors and adjusts the sampling strategy to steer the output away from toxicity, based on the "margin" from the toxic subspace.

The paper's contributions include:
- Introduction of the SASA method that utilizes the LLM's own contextual embeddings to identify and learn toxic versus non-toxic subspaces, thereby guiding the generation process to avoid toxic content during autoregressive sampling.
- Theoretical validation demonstrates that the proposed sampling strategy optimally balances two objectives: maximizing alignment with desired attributes (reducing toxicity) while preserving similarity to the original sampling distribution.
- Empirical evidence showcasing SASA's effectiveness across various model scales and types (base versus instruction-tuned), with competitive performance relative to state-of-the-art methods on benchmarks.

### Strengths
- The paper introduces the SASA approach, which is different from traditional methods that rely on external reward models or model retraining to mitigate toxicity in large language models (LLMs). The originality lies in leveraging the LLM's own contextual embeddings to define toxic and non-toxic subspaces, which is an innovative use of the model's internal representations.

- The authors provide theoretical proof that their sampling strategy optimally balances the reduction of toxicity with maintaining the original sampling distribution. The experiments cover different model scales and types, and the results show that SASA achieves competitive performance compared to state-of-the-art methods.

- The paper is well-written and structured.

- SASA addresses a critical issue in the deployment of LLMs—mitigating toxicity without the need for extensive retraining or external models. By providing a lightweight solution, it has the potential to be adopted in various applications of LLMs.

### Weaknesses
 - While the paper states that SASA compromise coherence, a more detailed analysis of the trade-off between non-toxicity and coherence would improve transparency. Specifically, the paper should explore how the perplexity of the generated text changes with varying levels of toxicity reduction and provide a more granular analysis of how this trade-off impacts the overall quality of the generated text. It would be beneficial to see examples where coherence is significantly impacted and to understand the specific mechanisms within SASA that lead to these issues.

- One of the paper’s novel claims is that toxic and non-toxic subspaces can be characterized within the model's representations. However, it is unclear how stable or interpretable these subspaces are across different contexts. Including a deeper analysis or visualization of these subspaces, perhaps using Principal Component Analysis (PCA) or t-SNE on the learned subspaces, could provide valuable insights and clarify the method’s inner workings. The paper should investigate the dimensionality of these subspaces and how they change with different prompts or model layers. A more rigorous analysis of the separability of these subspaces would also be valuable.

- The paper does not extensively address whether the toxic and non-toxic subspaces hold across different domains (e.g., social media, news, or technical content) or languages. Since language toxicity can vary significantly by domain and cultural context, a sensitivity analysis across diverse data sources would improve generalizability claims. This analysis should include a quantitative evaluation of SASA's performance on datasets from different domains and languages, and a discussion of any observed variations in performance.

- Incorporating a user study or human evaluation to assess the perceived quality and acceptability of the generated text would add significant value. Human evaluators could provide insights into the nuances of toxicity that automated metrics might miss, thereby offering a more holistic assessment of SASA's effectiveness. The study should include a diverse group of evaluators and focus on both the toxicity and coherence of the generated text.


- While SASA is presented as lightweight, the paper does not provide a quantitative assessment of the computational overhead introduced by its decoding strategy. Given that many applications of LLMs are latency-sensitive, evaluating the inference speed or compute cost of SASA relative to standard autoregressive sampling could strengthen the paper's claims of efficiency. This should include a breakdown of the computational cost of each step in SASA, and a comparison with the computational cost of standard autoregressive sampling.

- Even though Table 11 in the Appendix provides 4 failure case examples, the paper doesn't thoroughly analyze when and why SASA fails. A more detailed analysis of failure cases, including a discussion of the types of prompts that are most likely to lead to toxic outputs, would be beneficial. This analysis should also explore whether the failures are due to limitations in the model's ability to distinguish toxic and non-toxic content, or due to the sampling strategy itself.

### Questions
1. Can SASA be adapted to mitigate other forms of harmful content, such as misinformation or biased language?

2. In what scenarios does SASA struggle to mitigate toxicity?

3. How does SASA affect the original sampling distribution of the language model? Are there any noticeable changes in the diversity or fluency of the generated text?

4. What are the key assumptions underlying your theoretical proof? How robust are these assumptions in practical scenarios?

5. Can you quantify SASA's impact on generation speed? For instance, how does the controlled decoding process affect latency and computational efficiency compared to standard autoregressive sampling?

6. How do you balance toxicity reduction with language coherence? What specific metrics or thresholds were used to ensure SASA does not overly constrain generation quality?

8. Does the effectiveness of SASA vary with prompt length? Is there a theoretical or practical limit to the prompt length that can be handled?

9. The trade-off parameter β seems crucial for balancing toxicity reduction and fluency. However, the paper doesn't discuss how to choose this parameter optimally. Could the authors provide guidance on selecting β for different use cases or perhaps propose an automated way to tune it?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
[Edit] I have updated my rating after reading the authors' response.

This paper proposes "SASA", a decoding algorithm that can be used with language models to detoxify their outputs. SASA uses the embedding space of the LM along with a classifier model to steer the LM to generate less toxic statements. The authors demonstrate the efficacy of their method with numerous experiments on multiple datasets as well as varied language models; further they report standard metrics such as toxicity rate that are commonly used in this field.

### Strengths
* Strong range of experiments that show the much reduced toxicity in their model's generations. 
* Figures that explain their method clearly, leading to ease of understanding.

### Weaknesses
 * I suggest that the authors revert the pdf to the original font and style, to maintain the standard format of ICLR. 
* What is the classification model fv(c,x) used in the experiments? Further, what is the classification accuracy of this model in practice? 
* Related to above: Line 465 states "That said, with an aligned base model, the internal sentence embedding space can
be more informative of risk attributes such as toxicity" - do you have empirical proof of the same via the classification model's accuracy?
* Table 1 shows a huge drop in fluency/perplexity in SASA - what is the significance of the same?

### Questions
* Please add citations for each baseline in Table 1.

### Soundness
3

### Presentation
3

### Contribution
3
