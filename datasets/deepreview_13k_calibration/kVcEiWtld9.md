# Few-shot Style-Conditioned LLM Text Generation via Latent Interpolation

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 5, 3, 3

## Abstract
We propose a novel, model-agnostic approach for adapting large language models (LLMs)  in a few-shot manner to arbitrary styles using text samples from a given author. Rather than use predefined features, our method defines style in terms of LLM model weights and uses a variational autoencoder (VAE) to construct a latent space of these weights, allowing for a generic style representation. Our approach leverages interpolation in this latent embedding space of model weights to generate novel fine-tuned models for low-resource authors. We evaluate this approach compared to reported results, finetuning, and prompting across three datasets. Results indicate that our method outperforms our baselines in low-resource settings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes an idea for obtaining LoRA adapters for few-shot style-conditioned generation. The basic idea is, instead of learning LoRA adapters from only a few examples, using a variational auto-encoder to generate the LoRA adapter. Empirical results demonstrate the capacity of the proposed algorithm.

### Strengths
- This paper is well written, and the technical details are well explained, in terms of how the proposed algorithm was implemented. 
- The general idea makes sense, based on the reviewer's understanding of VAE and its capability. 
- The evaluation was conducted on three different datasets, which demonstrate the applicability of the proposed algorithm.

### Weaknesses
 - Although the proposed idea is sounding, the experiment results should be stronger to demonstrate the utility of the proposed algorithm. After all, with the availability of other large-scale pre-trained model ready to use, the benefit of using VAE most be significant to over shadow it computational cost.
- The empirical results will be more convincing if the proposed algorithm was demonstrated with multiple pre-trained models
- It is likely that I missed something from the paper, but I could not find the implementation details of the VAE in the main paper.
- Part of the paper needs to be further proofread, e.g., equation 6.

### Questions
Aligned with my comments in the **weaknesses** section, here are some questions

- Can you demonstrate more experiment results with other pre-trained models?
- What is the exact structure used as variational auto-encoder and decoder?

### Soundness
3

### Presentation
4

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
The authors propose a novel method for controlled style generation via mixtures of low-rank adapters and a learned latent space. The authors hypothesize that the most ideal solution would be to fine-tune an LLM for each desired style, however this is cost/time prohibitive. Instead they propose learning these adapters based on a small collection of fine-tuned ‘gold’ adapters. The results indicate their interpolation scheme, enabled by a learned VAE over adapter weights, outperforms several baselines, especially in the very few shot case.

### Strengths
* Few-shot style modeling is a difficult problem, with many existing methods falling short of leveraging the full capabilities of LLMs for this task. The authors propose a novel procedure which leverages mixtures of adapters, the end result is an arbitrary adapter matrix which can be applied to the base LLM.
* Existing control methods rely on conditioning on an pre-trained style representation (consider citing https://arxiv.org/abs/2406.15586), this approach using LLM representations themselves to encapsulate style and demonstrates that interpolations between these representations produces an effective way to control style in the few-shot setting.

### Weaknesses
 * I believe the variables in EQ 3-5 are overloaded? Line 201 refers to \mu_1, \mu_2…as the latent representations of the weight deltas. But EQ 3-5 refers to the same vector as ‘any pair’. If this is interpreted correctly, switching the 2nd set of subscripts to ‘a’ and ‘b’ would probably make it easier to interpret.
* I don’t think Figure 2 adds much value here, I believe the space and description in lines 285-290 can be used more effectively to describe your training procedure for the adapters (i.e. training loss, special tokens if any, preprocessing). A citation of the LoRA paper and hyperparameters used should be otherwise sufficient.
* Table 1: consider bolding the best results in the table.
* Consider adding another automatic style evaluation in addition to UAR: https://huggingface.co/AnnaWegmann/Style-Embedding
* The result discussion is lacking, while the results are written out, further explanation of model shortcomings are necessary.
The authors rely on two metrics: change in cross entropy loss, and UAR similarity. While these may correlate with style control performance to a degree, a human evaluation on the outputs of these systems would be far more convincing.

### Questions
* Section 3.1.1 explains how a closed set of adapters are derived based off N authors and their writing samples, details are lacking on how exactly these adapters are fine-tuned, i.e. is it simply next token prediction on the Corpus C_i?
* How many tokens are available in each corpus C_i? There is a claim in this section that suggests that far fewer samples are needed to target authors at test time, but no details on the scale.
* Section 3.2 says that a single gradient update is applied to the pool of adapters based on the target style corpus, and that this is a sufficient \delta for the latent space to decode a target weight matrix. Why is a single step chosen? Is there significant improvement in the predicted weights if N training steps are applied?
* Figure 3 suggests that the proposed method is better in the very few-shot case, and the one-step back prop does better with more samples. Why are we limited to 1 gradient update? How do these results scale with more updates?
* In Table 1, Prompting Llama2 appears to perform significantly better than the proposed approach in the 16 sample case. This requires the same inference compute as the proposed approach, why should the more complex mixture procedure be considered over simply prompting here?
* How necessary is the VAE step? I.e. does simply running a linear combination of the LoRA weight matrices to create an arbitrary one result in a meaningful style output?
* Can your method be used for style transfer in addition to style control? This requires semantic retention in addition to style conditional generation.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a novel approach for few-shot style-conditioned text generation. The key innovation is representing writing style through model weight differences rather than predefined features. The approach is evaluated against prompting and traditional fine-tuning across three datasets, showing superior performance in low-resource settings with less than 10 samples.

### Strengths
- The idea of representing text style via model weight differences rather than fine-tuning and prompting requires less data and manual effort. Using LoRA and PCA for dimensionality reduction makes the approach more efficient and practical.
- With empirical validation across multiple datasets and case analyses, the proposed method displays clear performance advantages in low-resource scenarios against strong baselines.

### Weaknesses
 - The VAE latent space filtering approach appears ad-hoc, lacking theoretical justification for the chosen filtering criteria and thresholds.
- The main experimental results are too limited in scope. The authors should reimplement baseline methods to ensure fair comparison across consistent settings,
- Performance varies significantly between datasets (notably poorer on Twitter), which needs more detailed analysis. Besides, it could be evaluated on more challenging cross-domain style transfer tasks.
- Missing ablations on key components like VAE architecture choices and latent dimension size.
- Paper writing and figure plotting need careful review:
  - Figure texts are too small. Captions could be more detailed
  - It is better not to maintain present tense throughout, especially when describing methodology and experimental settings.
  - Section 4.2 the notation for weight shapes should use proper mathematical multiplication symbol $\times$ instead of alphabet "x" when specifying dimensions.

### Questions
- The proposed method is only tested on llama2 7B, could it be generalized to other architectures?
- Some possible related works on controlled text generation via latent interpolation for reference [2-3].

[2] Deep Extrapolation for Attribute-Enhanced Generation

[3] Extracting Latent Steering Vectors from Pretrained Language Models.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes to model agnostic approach to tailor LLM to arbitrary styles. To enable learning from smaller samples, the model first trains a VAE framework that learns a representation for "weight deltas" of the LLM when fine-tuned on a large corpus of stylized text. This lower dimension VAE allows the model to learn a similar representation with a smaller corpus. To that end, for a new style, "k" fine-tuned models are taken at random, a single shot fine tuning is performed and interpolated in the VAE space to arrive at the specific deltas for the given data. Quantitative evaluations illustrate the promise of the approach.

### Strengths
The formulation is very neat and well established. 
The paper is solving a key problem that is very relevant and valuable

### Weaknesses
The paper needs to be tested out well. While there is a lot of potential technical contribution, the paper lacks clear validation of its approach. Given the qualitative nature of the style task, I would have liked to see sample generations and analysis on where the approach is working and where it is not. Does the choice of initial K-finetuned models have an impact on the model? These aspects are not addressed, which when addressed will make this a very strong paper.

### Questions
See above

### Soundness
2

### Presentation
2

### Contribution
2
