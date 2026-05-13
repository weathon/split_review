# RAG-DDR: Optimizing Retrieval-Augmented Generation Using Differentiable Data Rewards

- Decision: Accept
- Scores: 6, 6, 6, 6, 6

## Abstract
Retrieval-Augmented Generation (RAG) has proven its effectiveness in mitigating hallucinations in Large Language Models (LLMs) by retrieving knowledge from external resources. To adapt LLMs for RAG pipelines, current approaches use instruction tuning to optimize LLMs, improving their ability to utilize retrieved knowledge. This supervised fine-tuning (SFT) approach focuses on equipping LLMs to handle diverse RAG tasks using different instructions. However, it trains RAG modules to overfit training signals and overlooks the varying data preferences among agents within the RAG system. In this paper, we propose a Differentiable Data Rewards (DDR) method, which end-to-end trains RAG systems by aligning data preferences between different RAG modules. DDR works by collecting the rewards to optimize each agent with a rollout method. This method prompts agents to sample some potential responses as perturbations, evaluates the impact of these perturbations on the whole RAG system, and subsequently optimizes the agent to produce outputs that improve the performance of the RAG system. Our experiments on various knowledge-intensive tasks demonstrate that DDR significantly outperforms the SFT method, particularly for LLMs with smaller-scale parameters that depend more on the retrieved knowledge. Additionally, DDR exhibits a stronger capability to align the data preference between RAG modules. The DDR method makes generation module more effective in extracting key information from documents and mitigating conflicts between parametric memory and external knowledge.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on improving the retrieval-augmented generation (RAG) system by fine-tuning the content filter and the LLM generator while keeping the retriever frozen. It claims that existing supervised fine-tuning (SFT) approaches fail to model data preferences for different modules in the RAG system (i.e., the filter and generator) and tend to overfit training signals. In this work, the authors introduce a training method called differentiable data rewards (DDR), which uses DPO loss to train both the filter and generator. Experiments on six knowledge-intensive tasks show superior performance compared to several off-the-shelf RAG baselines and a fine-tuned RAG baseline (though without the filter module to denoise the retrieved contents).

### Strengths
=== Strengths ===

S1. The motivation of this work is clear, and the paper is easy to follow.

S2. The idea of introducing DPO loss to train the content filter and LLM generator in RAG is novel (although its significance is not quite clear given the current empirical study, see Weakness 1).

S3. The main comparison between the proposed method and baseline methods, along with the ablation study, is evaluated on a wide range of knowledge-intensive tasks.

### Weaknesses
=== Weaknesses ===

W1. Potentially problematic experimental setting. The main claimed contribution is proposing a DPO loss to train the content filter and LLM generator. However, in the experiments, the proposed method is primarily compared to off-the-shelf RAG methods without any training. The only fine-tuned baseline is RA-DIT, which only trains the LLM generator. It remains unclear whether the improved evaluation performance is due to the proposed filtering mechanism or to the better optimization by DPO loss compared to traditional SFT loss. Specifically, it is not clear if RA-DIT also leverages the content filter module during evaluation. If it does not, the comparison is not fair. Furthermore, the paper needs to clarify whether “RAG w/ $V_{KR}$” is the only RAG baseline that includes a content filter (i.e., knowledge refinement) module. The comparison in the main table and ablation study may be unfair and the results can be misleading if the proposed RAG-DDR can benefit from an additional filtering mechanism that other baselines lack of. The paper should provide a more detailed breakdown of the contribution of each component.

W2. Missing comparisons and discussion with closely relevant RAG baselines on denoising retrieved content. Approaches for mitigating conflicts between external retrieved knowledge and the LLM’s internal parametric knowledge, as well as for denoising retrieved content, have been widely explored in RAG literature [1,2,3,4]. A more thorough discussion of these works is needed to better situate this work. For instance, [2] directly trains the LLM generator using SFT loss with noisy inputs to improve robustness to noise without any filtering/knowledge refinement, [3] employs self-synthetic rationales to denoise retrieved content and guide generation for better accuracy, which is also trained with SFT loss, and [4] introduces an inference-time algorithm to deal with irrelevant retrieved documents through a mechanism called isolation-then-aggregation. Without a detailed comparison with such related works, it is difficult to assess the empirical significance of this work, especially since some of these works are strong RAG methods trained with SFT loss (e.g., [2,3]) for specific denoising purposes. The current discussion lacks a nuanced analysis of how the proposed method compares to these existing techniques, particularly in terms of robustness to noisy retrieved content and the effectiveness of different training strategies.

### Questions
Please address the questions in Weaknesses.

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces RAG-DDR, a novel reinforcement learning-based approach designed to improve retrieval-augmented generation (RAG) systems. The authors conceptualize the RAG framework as comprising two key modules: a knowledge refinement module, $V_{\text{KR}}$​, and a generation module, $V_{\text{Gen}}$. RAG-DDR computes partial reward for each module's response with a rollout process. Preference pairs are then constructed based on the rewards and then being used to optimize $V_{\text{Gen}}$ and $V_{\text{KR}}$ through DPO. Specifically, for $V_{\text{Gen}}$ (with filtered documents), the response with highest score is considered positive and lowest score is considered negative. For $V_{\text{KR}}$, the document that, when passed through $V_{\text{Gen}}$, yields the highest response score is considered positive, while the document with the lowest score is negative.

The authors perform extensive experiments across various knowledge-intensive tasks to evaluate RAG-DDR, comparing it against the vanilla RAG and SFT-based methods, showing that RAG-DDR can generate more accurate response and has the ability to leverage LLM's internal knowledge while not being misled by the external noisy information. Ablation studies further demonstrate the effectiveness of optimizing both $V_{\text{KR}}$ and $V_{\text{Gen}}$ using the proposed DDR approach.

### Strengths
1. Extensive experiments together with detailed analysis. In particular, the result from Table 3 is interesting, as it shows RAG-DDR's ability to balance between using internal and external knowledge.
2. The overall methodology is straightforward yet effective, leveraging a DPO-based approach to facilitate self-training.

### Weaknesses
1. Some aspects are not clear, see the question section.
2. (Minor thing) Typo at line 850 "identify the positive and positive responses for each query." -> "identify the positive and negative responses for each query."

### Questions
1. What distinguishes the proposed DDR method from step-DPO? Is that the only difference comes from the base policy, i.e., in DDR the base policy at each step comes from different agents while for step-DPO the base policy at each step are shared?
2. What is the impact of training RAG-DDR iteratively over multiple rounds? While results for 2-round training are reported in Table 1, a more detailed analysis of the outcomes would be beneficial.
3. In section 5.3, the authors argue that "SFT training method tends to cause LLMs to overfit the supervised data" from the observation that RA-DIT's generated responses is significantly shorter than vanilla RAG and RAG-DDR's responses. While I generally agree with this statement, I wonder whether this phenomenon could be attributed to differences in the average response length within the training sets for RA-DIT and RAG-DDR. If so, what would occur if we trained RA-DIT using the positive samples from RAG-DDR? Would this adjustment also impact the model's accuracy?

### Soundness
3

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
4

### Summary
This paper introduces Differentiable Data Rewards (DDR), a novel method for training Retrieval-Augmented Generation (RAG) systems. DDR collects rewards via a rollout method to optimize each agent while aligning data preferences between different agents within the system. The method addresses two key challenges in RAG systems: (1) training signal overfitting and (2) poor robustness against conflicting knowledge.

### Strengths
- Overall, the presentation is good and the method is easy-to-follow.
- The paper introduces the idea of DDR, which enables end-to-end optimization of RAG systems. The proposed method of aligning data preferences between knowledge refinement and generation agents alleviates the robustness issue when encountering external knowledge conflicts.
- The experimental results show that RAG systems trained with DDR strategy demonstrate improvements in terms of knowledge usage and robustness against knowledge conflicts.

### Weaknesses
 - Figure 1 is not clear enough. It could be better to illustrate the correspondence between the left and right parts, as well as the order of two modules in the right part (could use step 1, 2 as annotations). Additionally, it would be helpful to indicate how the reward signal propagates throughout the entire training process.

 
- I realize that training large language models is resource-intensive, but the demonstrations in the paper could be more convincing by including:

    - (If possible)Additional experimental results from larger-scale LLMs, such as Qwen2.5-14B or other larger models.
    - (If possible)Additional evaluations using more different LLM combinations to compose the RAG system (It seems that the current setup consider Llama3-8B-Instruct as knowledge refinement module and MiniCPM-2.4B/Llama3-8B-Instruct as generator)

### Questions
1. Kindly refer to the Weakness section.

2. Could the authors define what is meant by “data preferences between different RAG modules”? This concept appears multiple times in the paper, yet it remains somewhat unclear to me. Given that RAG primarily addresses knowledge-based tasks, could “preferences” here be more aligned with factual accuracy? I would appreciate a brief definition, ideally illustrated with a case study that demonstrates why this issue is important. It would be especially helpful if different base models were involved, as their internal knowledge may vary, potentially influencing their data preferences.

3. In addition, regarding the rollout method:

- What are the training speed and computational requirements? How does the method scale with larger datasets in terms of efficiency?
- Could the DDR method be expanded beyond just two agents? A more in-depth discussion from the authors on this point would offer valuable insights for developing more complex RAG systems.

4. An interesting finding in Appendix A.4 is that DDR enhances MiniCPM-2.4B’s mathematical capabilities. Could the authors provide a brief analysis explaining the possible reasons for this?

5. Typo: Line 269, should be "Llama3-8B-Instruct".

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
3

### Summary
The paper proposes the DDR framework for tuning agentic systems. The key idea is to sample multiple actions from an agent, and score them based on the downstream reward they fetch (computed via unrolling all subsequent agents in the chain). The actions are ordered by this score, and the DPO method is used to increase the likelihood of high scoring actions over low scoring actions.

The framework is applied to optimize a two agent RAG system consisting of a knowledge refinement agent (selecting relevant documents for RAG), and a generation agent that generates the response based on the selected document.

Through experiments and case studies, the authors show that the framework can perform better than several baselines, and can be better balance internal parametric knowledge with external information.

### Strengths
The paper addresses an important concern in RAG system of balancing use of external information versus internal parametric knowledge 
of the generation module. This is common problem for production RAG systems where retrieval is never perfect and often suffers from conflicting and/or missing information.

The idea of jointly tuning retrieval and generation modules is interesting and not studied as much in the literature (although some prior art does exist; see next section).

The results in Sections 5.3 and 5.4 are compelling and show a nice advancement over baseline methods in dealing with noisy retrieval in RAG systems.

### Weaknesses
The main weakness of the paper is inadequate comparison with related approaches on jointly tuning retriever and generator modules, which make it hard to appreciate the technical contribution of the paper.

There is prior work on supervising the retrieval module of RAG system based on performance of the generator (e.g., Wang et al. 2023, https://arxiv.org/pdf/2311.08377). In my eyes, the novelty of this paper is the use of DPO instead of a supervised tuning (which would just maximize likelihood of action fetching highest reward). Thus, if I understand correctly, the novelty of this work is the negative gradient induced by the contrastive DPO loss. However, this is not discussed in the paper. It would help to study the impact of the negative gradient in depth, via ablation studies. For instance, is the negative gradient responsible for the claim in Section 5.3: "DDR can help learn more factual knowledge during training while also preventing the loss of previously memorized information".

The paper highlights RAG-DDR's ability to effectively combine parametric knowledge with external knowledge. To assess this, it would be helpful to see a comparison with adaptive approaches that use different retrieval modules (including no retrieval) for different queries. For instance, see: Jeong et al., 2024: https://arxiv.org/pdf/2403.14403

Other helpful ablations and baselines to experiment with:
* Section 3.2 notes that RAG-DDR tunes the generation module first followed by the knowledge retriever (KR) module. It would be helpful to perform ablations where the KR module is tuned before the generation module (as in Wang et al,. 2023).

* When evaluating vanilla LLM and vanilla RAG, it would help to experiment with large LLMs like Gemini-1.5-pro, GPT4o to understand if the inability to balance parametric knowledge vs. external knowledge is an artifact of smaller LLMs.

The paper introduces the framework of differentiable data rewards (DDR). However, the framework is only evaluated for simple two agent systems. Consequently, DDR does not come across as a fully developed contribution. Instead, the key contribution, at least to me, is the use of DPO in jointly trying retrieval and generation modules. I would encourage the authors to build on this aspect.

### Questions
Suggestion: I would encourage the authors to perform the ablation studies and related work comparisons suggested in the "Weaknesses" section.

Some questions about the KR module:
- The KR module generates binary Yes/No responses for the relevance of each document to the query. How is the binary output used to rank documents and identify the top-k documents?
- Line 216 says:  "document di that leads the agent system to achieve the highest evaluation reward is considered positive". Does this mean a single document is selected and fed to the generator module? But equation 7 shows that k documents are fed. Am I missing something?
- If it is a single document then when tuning the KR module do we consider the highest-rewards document as positive, and all others as negative? 
- Would it make sense to consider contrastive objectives like ensuring P(Yes | q, d_i) > P(Yes | q, d_j) whenever the reward fetched by d_i is higher than d_j?

### Soundness
3

### Presentation
3

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
This paper introduces RAG-DDR (Retrieval-Augmented Generation with Differentiable Data Rewards), a novel method for optimizing RAG systems using reinforcement learning. Rather than using traditional supervised fine-tuning approaches, RAG-DDR uses a reward-based learning system to optimize both the knowledge retrieval and generation components. The method specifically focuses on aligning data preferences between different modules in the RAG pipeline to improve overall system performance, particularly in handling conflicts between parametric and external knowledge.

### Strengths
The approach is novel to RAG optimization. By using differentiable rewards, it effectively addresses the knowledge conflict problem that often plagues RAG systems.

### Weaknesses
1, The computational cost is high. RAG-DDR requires significantly more computational resources than traditional methods, requiring about 5x more API calls than standard approaches. This could limit its practical applicability in resource-constrained settings.
2, The paper also shows some limitations in complex reasoning tasks, particularly in multi-hop reasoning scenarios where the model can sometimes prematurely conclude questions are invalid. While the method shows strong performance on factual question-answering tasks, its effectiveness on more complex reasoning tasks could be improved.
3, while the paper demonstrates strong empirical results, it could benefit from a more thorough theoretical analysis of why the method works so well, particularly in terms of how it achieves better alignment between different RAG components.

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
3
