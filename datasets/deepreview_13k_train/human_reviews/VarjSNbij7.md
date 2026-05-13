# Q-resafe: Assessing Safety Risks and Quantization-aware Safety Patching for Quantized Large Language Models

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
Quantized large language models (LLMs) have garnered surging demand for broadening the deployment scenarios of LLMs, particularly on resource-constrained applications, which would otherwise be infeasible due to the substantial resource overhead incurred by astronomical model sizes. Propelled by this vast application potential, various quantization techniques have been developed to convert high-precision LLMs into low-precision quantized counterparts, aiming to preserve strong capabilities with reduced bit-widths. While these techniques have made significant strides in preserving utility, their implications for safety remain insufficiently studied. Recent findings highlight the fragility of safety mechanisms in both high-precision and quantized LLMs, underscoring the need for systematic safety evaluations and targeted interventions for quantized models.

In this paper, we present a comprehensive safety evaluation of quantized LLMs to complement existing efforts, covering four mainstream quantization techniques across diverse settings, including varying quantization bit-widths and different quantization-assisting datasets, through widely-accepted safety measurements. Our empirical evaluation reveals concerning safety degradation across all quantization methods and settings. To address this, we propose a quantization-aware safety patching framework, Q-resafe, to efficiently restore the safety capabilities of quantized LLMs while minimizing any adverse impact on utility. Extensive experiments demonstrate that Q-resafe effectively restores the safety of quantized LLMs obtained from diverse quantization processes, aligning closely with pre-quantization LLMs, even when evaluated against challenging datasets.  We will make our implementation publicly available https://anonymous.4open.science/r/Qresafe-D085/.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies the extent to which the different quantization techniques degrade the safety capabilities of quantized LLMs, and how can such declines in safety capabilities be mitigated.

### Strengths
+ Comprehensiveness: The study covers all four mainstream categories of LLM quantization techniques covering two post-quantization techniques and two quantization-aware training/finetuning techniques. For quantization techniques needing additional quantization-assisting dataset, the paper uses three datasets with varying safety risk levels: a directly harmful dataset, an indirectly harmful dataset, and a benign dataset. The quantized LLMs are evaluated with two commonly adopted bit-widths.

+  The paper also looks at the feasibility of identifying and updating a small portion of safety-critical weights, then exploit potential tools for identifying these weights, and construct a pair of masking matrices corresponding to the LoRA variables. This is clearly a novel contribution.

### Weaknesses
The paper makes a claim that "Although preliminary literature reports scattered evidence of safety evaluations for quantized LLMs, they are not systematic enough to support a well-rounded evaluation". Its primarily claim to novelty appears to be that it is the first to study the safety impact of quantized LLMs. Here is a list of work studying different aspects of quantizations impact on safety and alignment:

- Belkhiter, Yannis, Giulio Zizzo, and Sergio Maffeis. "HarmLevelBench: Evaluating Harm-Level Compliance and the Impact of Quantization on Model Alignment." Neurips Safe Generative AI Workshop 2024.

- Egashira, Kazuki, Mark Vero, Robin Staab, Jingxuan He, and Martin Vechev. "Exploiting LLM Quantization." arXiv preprint arXiv:2405.18137 (2024).

- Belkhiter, Yannis, Giulio Zizzo, and Sergio Maffeis. "HarmLevelBench: Evaluating Harm-Level Compliance and the Impact of Quantization on Model Alignment." In Neurips Safe Generative AI Workshop 2024.

- Hong, Junyuan, Jinhao Duan, Chenhui Zhang, Zhangheng Li, Chulin Xie, Kelsey Lieberman, James Diffenderfer et al. "Decoding Compressed Trust: Scrutinizing the Trustworthiness of Efficient LLMs Under Compression." arXiv preprint arXiv:2403.15447 (2024).

The claim that the paper is the "first systematic safety risk assessment of quantization on LLMs and mitigate the safety degradation" is too bold and not fully substantiated. It also appears unneeded. The reviewer will raise the score if the claim is better substantiated or moderated. Letting a paper be published with such a bold not-fully-substantiated claim is not feasible as it could confuse the community.

### Questions
* It would be useful to study the sensitivity of ASR results with the temperature and observe if the deterioration after quantization is worse or more gradual at higher temperatures.

* "the ASR rises from 29.80% on the pre-quantization Llama-2-7b-chat model to 42.40% on the INT4 model and to 39.10% on the INT8 model. Similarly, for the Gemma-7b-instruct model, the ASR increases from 9.40% pre-quantization to 17.90% on the INT4 model and to 15.10%" - it appears that the decline is more steep going to INT8 compared to going to INT4. It would be good to add discussion on this and conduct more experiments to understand this phenomenon and see if there is any saturation.

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
This paper studies the safety risks of quantization for LLMs. It first presents a detailed evaluation on how quantization reduces LLM’s safety, covering four quantization methods, three types of quantization-assisting datasets, and two bit-widths. To address the safety issue of quantization, the paper proposes Q-resafe, an approach that fine-tunes the safety-related weights of quantized LLMs to restore safety. The experiments demonstrate the consistent benefits of Q-resafe across the board.

### Strengths
The paper studies an important but relatively underexplored problem. The evaluation of existing quantization approaches clearly demonstrates the safety issues of quantization and Q-resafe gives significant benefits.

### Weaknesses
- The paper claims to be the first systematic assessment of safety risks of quantization. However, I am aware of at least two prior papers in this direction [1, 2]. I suggest the authors conduct a more comprehensive literature review and adjust the claim.

- While the paper studies more advanced quantization algorithms, it does not cover algorithms that are already popular, such as LLM.int8(), NF4, and FP4, implemented in the bitsandbytes library. The safety issues of these popular algorithms could have a larger impact on the users.

- The paper sometimes makes unsubstantiated claims. At lines 204-209, the paper says “Following the established practice in literature” but does not provide any reference. I am also confused at this point: why would users like to use direct harmful datasets or indirectly harmful datasets for assisting quantization? Moreover, at line 413, the paper writes “As recent studies have observed” without giving any citations. I believe identifying safety-critical weights is itself a research challenge. How does Q-resafe’s approach generalize?

- Why do the authors adopt a post-hoc fixing approach for Q-resafe? Have the authors considered incorporating safety mechanisms already during quantization?

- The writing needs some adjustments. First, line 123 is an unfinished sentence. Second, the baseline numbers for the quantization methods are not clearly presented. Table 2 says 0.3 and 9.2, but line 256 suddenly says 29.8 and 9.4, which are not mentioned before.

- On page 11, the paper has a “Limitations” section. I am not sure if this is the correct place to discuss limitations. It may not align with the ICLR formatting requirements.

### Questions
Please answer the points raised in the “Weakness” section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
With weights quantized into smaller bit-widths, LLMs are losing performance in utility. This paper observes LLM quantization from a safety perspective and conducts a measurement study concerning the impacts of quantization on LLM safety performance. The measurement study considers varying quantization bit-widths, different quantization strategies, and different settings of quantization-assisting datasets. It reveals that quantization can significantly comprise the safety ability of the quantized LLMs.

To mitigate the safety degradation, this work proposes to patch the quantized LLM in a similar fashion to the LoRA adapter. They construct a safety-related preference dataset by collecting the responses from the full-precision LLM and the quantized LLM. Employing the preference pairs, they use the DPO loss to implement a safety alignment. Concretely, they periodically locate safety-critical weights and focusing updating them to restore the safety ability. The experiments cover three preference dataset settings and yield positive results with the Q-resafe framework.

### Strengths
1. This paper raises an intriguing research question: how does quantization impact LLM safety performance? To answer this, the work makes a comprehensive measurement across different quantization settings.

2. The proposed Q-resafe method is effective. It can almost perfectly sustain the safety ability of quantized LLM in the studied safety evaluation.

### Weaknesses
1. **Intriguing but less novel topic.** For the safety risks coming with quantization, there have been a great number of works revealing it, from the vision field (e.g., https://dl.acm.org/doi/10.1145/3485832.3485881) to recent LLM research (e.g., https://arxiv.org/abs/2405.18137). From another perspective, safety performance is just one intrinsic ability of LLM. The finding of safety degradation after quantization is not impressive. The paper does not adequately differentiate its contribution from existing literature, which has already established that quantization can negatively impact model performance, including safety. The specific novelty of examining safety in the context of LLM quantization needs to be more clearly articulated, especially given the existing body of work in both vision and NLP domains.
2. **Writing is not self-inclusive.** The four considered quantization methods are essential for understanding why they behave differently. The lack of technical details of the surveyed methods hinders understanding the rationales behind the security risks incurred by quantization. The paper needs to provide more detailed explanations of the quantization techniques used, such as AWQ, QLoRA, and others. Without these details, it is difficult to understand why certain quantization methods lead to more significant safety degradation than others. The paper should include a more thorough technical description of each method, including the specific algorithms and parameters used.
3. **Lack of ablation study.** I have not noticed why the operation of safety-critical weight identification is necessary. And no ablation study provides evidence for employing it. The paper does not provide sufficient justification for the safety-critical weight identification step. An ablation study is needed to demonstrate the impact of this step on the overall performance of the proposed method. Without this, it is unclear whether the complexity of this step is necessary or if a simpler approach would suffice. The paper should include experiments that compare the performance of the method with and without the safety-critical weight identification step.
4. **Lack of impressive insights**: To be honest, I think the analysis for the measurement results is not in-depth. More discussions about safety benchmarks and utility benchmarks are in demand. Although it looks scary in Table 3 that the safety performance is almost compromised after quantization, utility and safety performance may be non-equally scaled. The paper needs to provide a more nuanced discussion of the results, including a deeper analysis of the safety and utility trade-offs. The current analysis lacks a detailed discussion of the implications of the observed safety degradation, and it does not adequately address the potential differences in scale between safety and utility performance. The paper should include a more thorough discussion of the limitations of the chosen benchmarks and the potential impact of these limitations on the conclusions drawn.

### Questions
- Can we collect the safety-related preference dataset in Q-resafe for offline use? For example, to substantiate an auxiliary loss to guide the safety-in-mind QAT.
- The design of locating safety-critical weights assumes that the safety ability of LLMs can located in a limited pool of weights. It is unclear whether they exhibit a positive or negative relationship with safety? If positive, what about sustaining the precision of the safety-critical weights and only quantizing other weights? From a safety-at-first perspective, how strong safety performance can such a method ensure? 
- Safety is a vague concept. Without data, how to identify the security-critical weights? Are detailed descriptions missing?
- Is the safety ability of the quantized LLM always bottlenecked by its full-precision counterpart?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper aims to assess the affect on safety alignment of quantization methods, and propose a safety patching method, Q-safe to improve the safety alignment of quantized models. The paper reveals a phenomenon that safety alignment is more damaged than general utility after quantization, considered different models and quantization methods. Q-safe mitigates this degradation by fine-tuning the quantizied model.

### Strengths
* The problem the paper looks at is interesting. Quantization methods indead need to ensure safety alignment as well.
* The experiment reveals an interesting phenomenon that quantization damages safety more than utility.

### Weaknesses
 * The experiment setup (Section 3: Assessing safety risks of quantization) is confusing in some places. It considers the cases where using harmful datasets for quantization, which does not sound realistic. The used datasets for quantization are small in size.
* The experiment of the safety patching method on quantizied models does not include baselines or ablation studies.
* It is unclear about techical contributions of Q-safe as its methodology looks similar to general safety alignment methods, instead of focusing on the quantization models.

### Questions
Thanks for submitting the paper. I agree with the motivation of the paper that quantization needs to preserve safety enforcement as well, which is not explicitly analyzed in existing work. The paper made a contribution in this domain. However, problems in experiment setups and technical contributions make me unsure if the current version is ready to publish.

First of all, I am convined that safety is affected after quantization given the empirical analysis Section 3. Based on the phenomenon, I am curious if the authors have hypothesis or insights why safety is affected more than utility. Also, the experiments of safety assessment are confusing in some places:

The metrics are critical for understanding multiple tables but details are placed in Appenfix Table 5. For instance, Table 3 says the safety metric is $ASR_{Vanilla}$ but according to Table 5, the safety metric corresponding to quantization with Indirect Harmful Datasets should be $ASR_{AoA}$, and for AWQ the metric should be $ASR_{Decoding}$. Please be precise in using the notations.

Quantization datasets and the dataset for safety assessment all rely on AdvBench. Is there potential risk of overlap of training/fine-tuning and testing data?

In Table 5, the harmful datasets for quantization sounds quite small. As far as I see, fine-tuning of LLM quantification requires large amount of data, such as hundreds of gigabytes in the original LLM-QAT work. Also, in terms of harmful datasets for quantization, do you mean adding additional harmful data to benign datasets, or do quantization with completely harmful datasets? It does not sound realistic if it is the later. Also, what if involving safety-enforced conversations in the datasets for quantization?

Second, intuitively I think Q-safe, the safety patching method after quantization is valid in its design. However, the experiments lack a comprehensive analysis of the characteristic of the method. I have following questions:

What are the baselines, or ablation study? Baselines in my mind include: (1) directly using dataset for safety fine-tuning during the quantization; (2) directly using dataset for safety fine-tuning when using Q-safe, to show the benefit of the safety-patching dataset construction; (3) do simple LoRA fine-tuning when using Q-safe, to show the benefit of periodic safety-critical weights identification.

What is the technical contribution comparing with methods of safety alignment on LLMs, e.g., instruction tuning with safety-aligned data adopted by Llama (Llama: Open and efficient foundation language models)? I raised this question because the design of Q-safe looks independent with quantization and can work on any LLMs.

Minor issues:
* Section 4.1 Row 229, it is Table 5 not Appendix 5.
* Abbreviation DPO is used at the first time in Introduction, row 112, without explanation.

### Soundness
3

### Presentation
2

### Contribution
2
