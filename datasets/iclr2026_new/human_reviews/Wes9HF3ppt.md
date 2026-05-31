## Human Reviewer 1

### Summary
This paper introduces a method for sequence generation that learns to insert tokens at arbitrary positions in a sequence. The authors refer to this as Insertion Language Models (ILM), and compare it against autoregressive models and masked diffusion models.
ILMs are trained using a single transformer encoder with a simple denoising objective, where tokens are completely dropped from the sequence and the model learns to re-insert them. 

On synthetic planning tasks, ILMs are shown to overcome the failure modes of the other models. In particular it performs the best on Star Graphs from (Bachmann & Nagarajan, 2024). For unconditional text generation, ILMs perform competitively with auto regressive models and better than diffusion models.

### Strengths
The paper is well written and easy to follow. In particular, I find the figures to be pedagogical and helpful in presenting key ideas and concepts of the paper. I also commend the authors for a thorough and fleshed out related work section and a beautiful appendix. In general, the presentation of the paper comes across as strong, and it’s clear that a lot of effort went into it. (some suggestive further improvements are listed in the Weaknesses section)

In regards to the method, I personally find the proposed insertion method itself to be quite elegant and interesting. The explanation of the experiments and the corresponding results are also clear. The authors also demonstrate strong results on the Star Graphs from (Bachmann & Nagarajan, 2024).

### Weaknesses
In general, my concerns regard the contributions of the paper and how they compare to autoregressive modelling(ALM). This is because ALMs are clearly the dominant paradigm, so for a new method to be considered it needs a strong selling point. From what I can see currently, the biggest selling point is that ILM solves the toy problem of Star Graphs from (Bachmann & Nagarajan, 2024).

**Concern 1:**

One could quite easily create a setup where an autoregressive model is capable of performing infilling. Such as existing Fill-in-the-middle setups, or something simple as: If context X is the full text, and X* is the text with removed segments, you could formulate the autoregressive task as: X* -> X.
Perhaps you calculate the loss only on X, or not…

For a more convincing narrative, I would therefore suggest incorporating such a baseline for at least the 5.2.2 Infilling task. 

Furthermore, as we scale ALMs and their capabilities and generalizations increase, it is possible that such capabilities would emerge regardless. Of course it’s an unfair comparison in terms of resources, but I’m quite confident that SOTA LLMs would do exceptionally well on these smaller infilling tasks, even if they have not been directly trained towards them. In particular, I’m also confident that these models solve the Star Graphs from (Bachmann & Nagarajan, 2024). (which leads to Concern 2)


**Concern 2:**

Scaling of ILM.

Considering that autoregressive models are so well-established, and one of their strongest properties is how well they scale and generalize, it would be beneficial for you to demonstrate the scaling properties of ILM. Both in terms of computational costs, but also performance.

I suggest to therefore provide metrics for the computational cost for ILM, both in terms of training and inference. And preferably also how these metrics scale with model size, sequence length etc…
Additionally, varying the model/dataset sizes for language modelling, would make for an interesting experiment.

Conveniently, you only explicitly compare the inference time between ILM and MDM. However, in the discussion you mention that inference might be slower for ILM. But how much slower? This seems like a serious limitation if one wishes to scale this to reasoning models, which generate several thousand tokens per answer. In my opinion the applicability of ILM hinges quite a lot on these scaling factors, and might change the overall narrative of your paper.

**-----------------------------------------------------**

**Suggested Presentation Improvements**

Several paragraphs are quite long and dense. It might be more easily digestible for readers to split them up. I understand that this may in part be an attempt to achieve nice formatting. But if possible I would consider tweaking this. Example paragraphs are: Line 33 - 53, Line 291 - 309, Line 334 - 352

Line 17 + Line 54 VS Line 86: can come across as contradicting each other. First you claim to “revisit” insertion based sequence generation. Then Line 86 introduces “Insertion Language Models”. Perhaps make this distinction more clear.

Line: 127: Since the bold text “Limitations of MDMs” start the paragraph, I’m left with the impression that you claim that step size “s” is a limitation of MDMS. But I would argue this is rather a limitation of how people potentially would train MDMs. Similarly, I would find it a bit weird to say that “a high learning rate breaks training for Transformers” and hence this is a limitation…. I therefore suggest some rephrasing here.

Line 208: I have never come across the term “Unembedding” layer, to refer to the final linear layer to the vocab. Perhaps there’s something more common you could pick?

Line 335: Zebra Puzzles are now notated with bold, and reside inside the 5.1.1 Star Graphs sub chapter. Seems more appropriate and consistent to let Zebra Puzzles be its own subchapter.

### Questions
See weaknesses for concerns

### Soundness
3

### Presentation
4

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 2

### Summary
The paper introduces ILMs, a novel sequence generation paradigm that predicts both token and insertion position jointly. This idea generalizes ARMs and MDMs by allowing arbitrary generation order and variable-length outputs, elegantly overcoming key limitations of both frameworks. The authors demonstrate the performance improvements and increased flexibility experimentally on various tasks.

### Strengths
1. The authors clearly articulate the shortcomings of existing ARMs (sequential bias) and MDMs (fixed-length masks, simultaneous unmasking). ILMs offer a different approach with many benefits, and the authors' presentation of this is clear.

2. The experiments are well chosen and convincing. The paper evaluates ILMs on synthetic planning tasks (star graphs, zebra puzzles) and on realistic text datasets (LM1B, TinyStories). ILMs outperform ARMs and MDMs on constrained reasoning tasks and perform competitively on text generation, while uniquely supporting arbitrary-length infilling. I think it is good when an experiment offers conclusive answers, since it allows the field to build on solid ground. With that in mind, I feel that these experiments convey the relative improvements on the tasks considered.

### Weaknesses
1. Not allowing caching is a pretty big deal for incremental generative models. I understand that it is future work, but it could be nice to discuss a bit what the possible avenues are toward efficient ILM inference?

2. I always feel bad saying this, but it would be nice to see how results change at larger scales. I know this is easier said than done, and scaling up experiments is usually the goal anyway. However, my point is that sometimes the extra flexibility/expressivity becomes harder for the model to make use of at larger scales (like needle in a high-dim haystack), and sometimes it becomes easier (it enables a realistic, generalizable solution instead of some impractical and unrobust best fit). Everyone has their thresholds somewhere, but for myself (and many people I've worked with) it's hard to get any signal on this with sequence lengths and complexity as restricted as in e.g. LM1B. To summarize, this isn't a weakness so much as something to look out for, but it would be nice to see some experiments/exposition put toward the question "what parts of ILMs do we expect to become more robust/more brittle at scale"?

### Questions
1. The experiments discuss the per-token generation time, NLL, etc., but I would like to know more about the qualitative ways in which ILM generations differ from ARM/MDM generations at larger scales. Are the sequences more complicated/higher entropy/longer? Is there some patter/trend for how models tend to use insertions that the authors anecdotally saw?

2. Any ideas how to address caching/fast inference? There is also growing interest in pre-compiled deep learning models (jax.jit, torch.compile, ...) and I imagine ILMs would face all kinds of issues about not knowing lengths of arrays in advance for preallocation. Are the authors looking toward efficient implementation?

### Soundness
4

### Presentation
4

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 3

### Summary
The authors revisit Insertion Language Models (ILMs), an insertion-based language model for arbitrary-length, arbitrary-order token generation. This model predicts output tokens along with their positions in the existing sequence, one-at-a-time.

The key contributions are:
1. Addressing the high variance problem of naive infilling denoising objectives through an approximate denoising training objective and tailored parameterization of the denoising network.
2. Demonstrating that ILMs outperform ARMs and MDMs on synthetic tasks (path generation on star graphs, zebra puzzles).
3. Showing that ILMs perform slightly better than MDMs and are competitive with ARMs on language generation tasks.

### Strengths
The paper successfully modernizes the classical idea of insertion-based language models by combining it with denoising objectives. The performance improvements are convincingly demonstrated on synthetic tasks, clearly showing the advantages of the proposed approach.

As a reference, it may be helpful to also cite:
- Insertion-based Decoding with automatically Inferred Generation Order, https://arxiv.org/abs/1902.01370

### Weaknesses
- **Method: Fundamental Inefficiency**

The primary limitation of ILMs is that they sacrifice parallelization benefits from both ARMs and MDMs. Unlike ARMs, ILMs cannot leverage efficient parallel training, and unlike MDMs, they do not support parallel inference. However, despite giving up these parallelization advantages, the improvement in generative perplexity is not substantial (Table 2, LM1B).

- **Experiment Setup: NLL Measurement**

NLL measures how accurately a model captures the learned distribution. However, the comparison appears unfair: MDM uses naive tau-leaping sampling while ARM and ILM use nucleus sampling with p=0.9. For a fair comparison, I recommend re-evaluating with p=1.0 for all models.

- **Experiment Setup: Infilling Task**

Similar to the NLL experiments, either: (1) change p=0.9 to p=1.0 for fair comparison, or (2) employ advanced sampling strategies for MDM (e.g., confidence-based sampling methods [1]) to verify performance under more favorable conditions.

- **Experiment Setup: Baselines**

Recent discrete diffusion models such as Edit Flows [2] and FlexMDM support arbitrary-length generation. However, comparisons with Edit Flows are missing from the synthetic task experiments. I would like to see: (1) performance comparisons between ILMs and Edit Flows, and (2) clarification of what advantages insertion-based language models offer over editing-capable discrete diffusion/flow matching models.

**References:**
- [1] Train for the Worst, Plan for the Best: Understanding Token Ordering in Masked Diffusions, https://arxiv.org/abs/2502.06768
- [2] Edit Flows: Flow Matching with Edit Operations, https://arxiv.org/abs/2506.09018

### Questions
- (Minor) Why wasn't the per-token generation time vs. NLL figure presented as the more conventional NFE vs. generative perplexity plot? Also, could you please include ARM in this comparison?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
3

---

## Human Reviewer 4

### Summary
The paper proposes a language modeling framework that enables sequence generation of arbitrary length by extending the existing idea of generation through insertion. The proposed models are evaluated on both planning tasks and language modeling tasks, including unconditional text generation and text infilling. Experimental results demonstrate performance improvements over baseline models such as Autoregressive Models (ARMs) and Masked Diffusion Models (MDMs).

### Strengths
The paper makes an original contribution by adapting insertion-based sequence generation to general language modeling, allowing models to generate sequences of arbitrary length. This is a practical extension of existing techniques, expanding their applicability beyond fixed-length generation tasks.

The work is of clear presentation and well-structured experiments on both synthetic and real-world datasets. Results show consistent improvements over strong baselines such as Autoregressive and Masked Diffusion Models. Overall, the paper is clearly written, methodologically sound, and makes a meaningful contribution to advancing flexible and general-purpose language generation.

### Weaknesses
The paper’s technical novelty is somewhat limited, as its main contribution lies in applying an existing insertion-based sequence generation technique to the problem of variable-length text generation. While this adaptation is practical, the paper does not sufficiently deepen the theoretical or conceptual understanding of insertion-based generation, nor does it clearly articulate the unique challenges encountered when extending this approach to general language modeling. A more thorough analysis of these challenges, such as handling coherence, positional dependencies, or long-range consistency, would strengthen the contribution.

Furthermore, several (not all) recent studies that have explored similar directions [1,2] appear to have been overlooked. Incorporating a discussion of these works and clarifying how the proposed model differs or improves upon them would better situate the paper within the existing literature and highlight its distinct value. Overall, expanding the theoretical motivation and engaging more critically with prior research would enhance both the novelty and the impact of the work.

[1] Li, J., Dong, X., Zang, Y., Cao, Y., Wang, J., & Lin, D. (2025). Beyond fixed: Variable-length denoising for diffusion large language models. arXiv e-prints, arXiv-2508.
[2] Gu, Y., Wang, W., Feng, X., Zhong, W., Zhu, K., Huang, L.,  & Qin, B. (2024). Length controlled generation for black-box LLMs. arXiv preprint arXiv:2412.14656.

### Questions
Could the authors discuss the current state-of-the-art approaches to variable-length text generation and clarify how their method compares to these existing techniques?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3