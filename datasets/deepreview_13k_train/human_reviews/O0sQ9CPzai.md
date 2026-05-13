# TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees

- Decision: Accept
- Scores: 8, 5, 6

## Abstract
In the domain of complex reasoning tasks, such as mathematical reasoning, recent advancements have proposed the use of Direct Preference Optimization (DPO) to suppress output of dispreferred responses, thereby enhancing the long-chain reasoning capabilities of large language models (LLMs). 
To this end, these studies employed LLMs to generate preference trees via Tree-of-thoughts (ToT) and sample the paired preference responses required by the DPO algorithm.
However, the DPO algorithm based on binary preference optimization was unable to learn multiple responses with varying degrees of preference/dispreference that provided by the preference trees, resulting in incomplete preference learning.
In this work, we introduce \textbf{T}ree \textbf{P}reference \textbf{O}ptimization (\TheName{}), which does not sample paired preference responses from the preference tree; instead, it directly learns from the entire preference tree during the fine-tuning.
Specifically, \TheName{} formulates the language model alignment as a \textit{Preference List Ranking} problem, where the policy can potentially learn more effectively from a ranked preference list of responses given the prompt. 
In addition, to further assist LLMs in identifying discriminative steps within long-chain reasoning and increase the relative reward margin in the preference list, \TheName{} utilizes \textit{Adaptive Step Reward} to adjust the reward values of each step in the trajectory for performing fine-grained preference optimization.
We carry out extensive experiments on mathematical reasoning tasks to evaluate \TheName{}. The experimental results indicate that \TheName{} consistently outperforms DPO across three publicly large language models on four datasets.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work proposed TPO which enables direct preference alignment for long-chain reasoning tasks.  By sampling with tree-of-thoughts, lists of generated CoTs would be paired with preference signals, which are used for LLM alignment. Limited by the original DPO, which only enables pairwise preference optimization, TPO proposed list ranking formulation to extend DPO framework. Empirical studies on several mathematical reasoning tasks show better performance.

### Strengths
1. This paper is well motivated and well presented.

2. The connection between LLM alignment and learn-to-rank problems is well explained.

3. The proposed implicit reward model formulation in Eq(10) is novel.

### Weaknesses
1. Regarding the preference list ranking, there might have been some studies on its direct optimization approaches [1-3]. The authors could consider discussing their unique challenges or difference to those works. Ideally, the authors might consider adapting their ideas as baselines for a more comprehensive comparison.

2. The backbone general LLMs are restricted to only one type, Qwen. The authors might considering experimenting on more types of LLMs, including Llama-3, Phi-2, Mistral, etc.

3. The authors could consider including supervised fine-tuning and/or instruction fine-tuning baselines, which could help the readers better understand the potential performance upper bound on the specific downstream tasks.

4. It would be critical for the authors to also demonstrate the generalizability of the LLMs after TPO on general benchmark or metrics, which might prevent potential chances of model overfitting on the downstream tasks.

5. Although the proposed DPO is proposed for general chain-of-thought reasoning, only maths and coding tasks are evaluated. More commensense, multi-hop question-answering, and especially knowledge-intensive tasks could be evaluated.

### Questions
1. Could the authors explain the link between DPO on chain-of-thought reasoning, which from my understanding is the major contribution of this paper, and the proposed Preference List Ranking optimization. Specifically, I was wondering if extracting pairwise samples from the ranking list could simply solve the challenge?

2. Could the authors explain their means of acquisition of such ranking list preference signals, which could be relatively more expensive and harder to find? Any intensive human annotation process involved in this paper?

3. Could the authors try to discuss the potential alternative ranking list preference alignment methods I provided in Weaknesses?

4. Could the authors provide some insights or experimental results, if applying their TPO on knowledge-intensive CoTs? Since in such tasks knowledge fidelity (factuality) could be entangled with logical reasoning steps (tree-of-thought sampling), the alignment process is not as straightforward as mathematical or coding problems. In such cases, would TPO still work under some guarantees with some lower-bounded confidence?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper presents Tree Preference Optimization (TPO), an enhancement to Direct Preference Optimization (DPO) for LLM alignment. Unlike DPO’s binary preference structure, TPO uses ranked preference lists and an Adaptive Step Reward to adjust the reward margin, allowing the model to learn from multi-branch and multi-step reasoning paths and improve accuracy in complex tasks.

### Strengths
1.	The paper is well-written and easy to follow.
2.	The paper proposes using the classical Lambda weight from Learning-to-Rank (LTR) to construct the TPO loss, which enhances the accuracy of list ranking. This is an interesting design.
3.	The design of a loss function for multi-branch and multi-step scenarios is a highly significant research direction.The paper makes several attempts in this direction.

### Weaknesses
1. The most critical issue is that I believe obtaining noise-free, list-wise preference data is very costly. A more essential challenge is how to reliably construct such data. The construction method in the paper likely introduces substantial noise, and I am skeptical about the positive impact of aligning the llm to a noisy list ranking.
2. The Adaptive Step Reward mechanism proposed is overly intuitive, lacking more rigorous experimental analysis and theoretical support. Specifically, the method lacks a clear justification for how the semantic similarity is calculated and how it directly translates into reward adjustments. The mechanism appears to be a heuristic rather than a principled approach.
3. The experimental design in the paper is somewhat unfair, as DPO only uses pair-wise data, whereas TPO leverages additional augmented data. I believe the list data should also be converted into pair-wise form, allowing for a fair comparison. This would enable analysis of whether list-wise data is indeed more effective than pair-wise when the total information content is kept constant.

### Questions
See Weakness

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
This paper presents Tree Preference Optimization (TPO), a novel framework that decomposes Tree of Thoughts into multi-branch and multi-step response patterns for fine-grained preference optimization. The framework reconceptualizes language model alignment as a generalized Preference List Ranking problem, which facilitates more effective alignment learning from preference lists. TPO introduces the Adaptive Step Reward mechanism, which adjusts step-wise rewards based on inter-step correlations to focus on discriminative steps, thereby enhancing the optimization efficiency.

### Strengths
- The paper is well-written and presents comprehensive empirical results with publicly available implementation code, demonstrating the effectiveness of the proposed approach.

- This paper presents a novel approach by decomposing Tree of Thoughts into a hierarchical structure of multi-branch, multi-step responses and leveraging Learning-to-Rank algorithms for preference optimization.

### Weaknesses
 - The rationale for selecting LambdaLoss over other LTR loss functions in Section 3.1 requires further clarification. Maybe you can justify this choice by highlighting the specific advantages of LambdaLoss in your application.


- In Equation 10, I notice that RM=0 in Line 298, while my understanding suggests that cosine similarity should be 1 when the content is shared. Could you please clarify this point?  Maybe you can provide more explanation of your *Adaptive Step Reward*.


- The ablation studies for Adaptive Step Reward appear limited. Based on Table 3, its impact seems modest. Further investigation into the effectiveness and mechanism of Adaptive Step Reward would strengthen the analysis.

### Questions
See weaknesses

### Soundness
3

### Presentation
3

### Contribution
2
