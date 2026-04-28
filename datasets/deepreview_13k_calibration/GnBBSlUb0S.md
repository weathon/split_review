# Black-Box Adversarial Attack on Dialogue Generation via Multi-Objective Optimization

- Decision: Reject
- Avg Score: 4.60
- Scores: 6, 6, 5, 1, 5

## Abstract
Transformer-based dialogue generation (DG) models are ubiquitous in modern conversational artificial intelligence (AI) platforms.
These models, however, are susceptible to adversarial attacks, i.e., prompts that appear textually indiscernible from normal inputs but are maliciously crafted to make the models generate responses incoherent and irrelevant to the conversational context.
Evaluating the adversarial robustness of DG models is thus crucial to their real-world deployment.
Adversarial methods typically exploit gradient information and output logits (or probabilities) to effectively modify key input tokens, thereby achieving excellent attack performance.
Nevertheless, such white-box approaches are impractical in real-world scenarios since the models' internal parameters are typically inaccessible.
While black-box methods, which exploit only input prompts and DG models' output responses to craft adversarial attacks, offer a wider applicability, they often suffer from poor performance.

In a human-machine conversation, good generated responses are expected to be semantically coherent and textually succinct.
We thus formulate adversarial attack on DG models as a bi-objective optimization problem, where input prompts are modified in order to 1) minimize the response coherence, and 2) maximize the generation length.
In this paper, we empirically demonstrate that optimizing either objective alone results in subpar performance.
We then propose a dialogue generation attack framework (DGAttack) that employs multi-objective optimization to consider both objectives simultaneously when perturbing user prompts to craft adversarial inputs.
Leveraging the exploration capability of multi-objective evolutionary algorithm due to its intrinsic diversity preservation, DGAttack successfully creates effective adversarial prompts in a true black-box manner, i.e., accessing solely DG models' inputs and outputs.
Experiments across four benchmark datasets and three language models (i.e., BART, DialoGPT, T5) demonstrate the excellent performance of DGAttack compared to existing white-box, gray-box, and black-box approaches.
Especially, benchmarks with large language models (i.e., Llama 3.1 and Gemma 2) suggest that DGAttack is the state-of-the-art black-box adversarial attack on dialogue generation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposed DGAttack, a black-box multi-objective attack framework for generating
adversarial samples aimed at degrading the performance of dialogue generation models. It leverages multi-objective evolutionary algorithm to optimize for two objectives—response length and accuracy. The proposed method generates adversarial sentences through semantic preserving perturbations to substantially reduce the quality of the model output.

### Strengths
1. The paper is easy to read, and looks interesting to most people. It applies a genetic algorithm to optimize for the attack, which is quite novel.

2. The experiments section has extensive baselines. And the result performance looks good.

### Weaknesses
1. In the limitations section, it mentions that the proposed method doesn't work well for LLMs, because word-level substitutions are handled very well.

2. The proposed method also comes with high computational cost, this also can make the model less useful.

### Questions
A detailed analysis of the computational cost would be useful. For example, for remote LLMs attach, how many api calls are needed in each iteration of the algorithm.

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
3

### Summary
The paper studies the problem of crafting black-box adversarial attacks in Dialogue Generation (DG) models. Existing adversarial methods either rely on access to model gradients or internal parameters (white-box approaches) or demonstrate limited effectiveness in a black-box setting. To this end, the authors proposed DGAttack, a black-box adversarial attack framework specifically for DG models. DGAttack employs a multi-objective optimization, aiming to maximize generation length while minimizing response coherence.

### Strengths
1. The problem statement studied in this paper is interesting and has been well-articulated to the reader. The limitations in prior approaches have also been well-conveyed. Further, the overall presentation of the proposed approach is clear.

2. The experiments section looks comprehensive with evaluations on four standard benchmarks. DGAttack leads to an increased Attack success rate across most of the models and datasets.

### Weaknesses
 1. The technical contribution is not convincing and lacks originality. The idea of minimizing accuracy and maximizing response length is not novel but has been earlier explored in DGSlow [1]. I understand, that DGSlow is a white-box attack and has a drawback in requiring access to the gradients. However, the primary optimization problem in DGAttack closely resembles that of DGSlow [1], with the primary difference being the use of a genetic algorithm to solve the multi-objective optimization. I request the authors to clarify the contributions and differences with DGSlow [1].

 2. In the introduction, the authors mentioned that recent LLMs are adept at generating coherent long-form responses, and hence it is difficult to craft a black-box attack. However, in Table 1, the experimental results were presented on relatively older LLMs such as DialoGPT, BART, and T5. I recommend that, in addition to the transfer attacks in Table 3, the authors also present primary results in Table 1 on more current models like LLAMA-3.1 and Gemma.

[Minor]
1. The presentation could have been better. For example: equation numbers are missing. 
2. On page 3, the definition of f(.) is not clear.
3. In the equation on line 151, how is the reference response $x_\text{ref}$ defined is not clear.
4. On line 345, should it be $cos(x_i, \tilde{x_i}) < \epsilon$, instead of “>” sign?

### Questions
Please see the Weaknesses. 

My major concerns are regarding the lack of originality in the proposed approach, and primary evaluation on relatively older LLMs. For rebuttal, I shall recommend the authors: (1) To clarify the technical contributions and differences with DGSlow [1]. (2) Evaluation on LLAMA-3.1/Gemma/other modern LLMs for Table 1 setup.

[1] Li, Y., Li, Z., Gao, Y. and Liu, C., 2023. White-box multi-objective adversarial attack on dialogue generation. arXiv preprint arXiv:2305.03655.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a novel dialog generation adversarial attack called DGAttack, which works by optimizing the input to (1) minimize the coherence of the response and (2) maximize the length of the response. The optimization is based on a multi-objective evolutionary algorithm, which allows one to perform the attack in a black-box setup. The authors demonstrate the effectiveness of the algorithm on four dialog datasets and three dialog generation models (BART, T5, DialoGPT). DGAttack can also be applied to larger language models such as Llama and Gemma.

### Strengths
1. The proposed adversarial algorithm is shown to be effective across models and datasets, outperforming existing black-box threat models as well as certain grey-box baselines.

2. The method can be used in a black-box setup and can be directly applied to larger and closed-source models.

### Weaknesses
1. The paper does not explain why an adversarial attack on a dialog generation system—with the objectives of reduced accuracy and longer responses poses a significant threat to these models. It is not entirely clear how this property can be misused and why this adversarial model is harmful. Therefore, it is hard to evaluate the importance of the problem.

2. Given that the performance differences across different methods are sometimes very small (e.g., as seen in Table 3), it would be helpful to include standard deviations to assess the significance of the improvements..

3. The core objective of the attack is to generate responses that deviate from the original response. However, the evaluation metric focuses on the similarity between the generated response and the original response, which seems counterintuitive. If the goal is to force a model to generate a different response, a user could simply ask a different question to achieve a similar effect. The metric should evaluate the relevance of the generated response to the adversarial input, not the original response.

### Questions
DGAttack finds perturbations in the input space that cause the highest decrease in the accuracy of the output. Since the input has been changed, the original response might no longer be the optimal one for the new 'adversarial' input. Given this, why is the correspondence between the generated responses and the reference outputs considered the optimal metric for measuring the adversarial effectiveness of the model? Would it be better to employ a metric that captures the relevance of the generated response to the new adversarial input?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper proposes a genetic algorithm for addressing the multi-objective adversarial attacks problem. The experimental results demonstrate that DGAttack outperforms other baselines' black-box and gray-box approaches in terms of generating longer and less coherent responses. The framework also achieves reasonable transferability.

### Strengths
Reasonable Good Performance in Benchmarking Black-Box Scenarios: The experimental results seem to demonstrate that DGAttack outperforms other baselines' black-box and gray-box approaches in terms of generating longer and less coherent responses. The framework also achieves reasonable transferability.

### Weaknesses
1. Limited Novelty & Orignity, and Overlap with Prior Work:
The novelty of this work is limited due to significant overlap with a prior study by Li et al. (2023) (White-Box Multi-Objective Adversarial Attack on Dialogue Generation), which was the first to introduce a Pareto-optimization framework specifically for white-box adversarial attacks in dialogue generation. Li et al. (2023) formulated a multi-objective optimization approach to balance between adversarial effectiveness and conversational coherence, making it a foundational work in this space. In contrast, this paper claims to target a similar optimization objective but in a black-box setting, suggesting only a slight modification. While black-box constraints introduce challenges such as limited access to model internals, simply adapting an established white-box approach to a black-box context may not constitute a significant technical contribution. To substantiate the novelty and its originality, the authors need to clearly distinguish their approach from Li et al.’s framework.

2. Lack of Comprehensive Experiments:
The experimental evaluation in this work lacks robustness, particularly due to the absence of state-of-the-art (SOTA) models in the primary experiments (Sections 4.2 and 4.3). While Section 4.4 includes evaluations on models such as Meta-LLama-3.1-8B-inst and Gemma-2-9B-it, the analysis does not extend to larger, more recent LLMs like Meta-LLama/Llama-3.2-90B-Vision-Instruct. This gap in testing leaves the efficacy of the proposed method on the latest generation of LLMs unproven, which limits the practical applicability of the results. Besides, in Sec. 4.4, the authors do not specify the reasons why forgive multiple baselines evaluated in Sec. 4.2 and Sec. 4.3 (FD, HotFlip, PWWS, BAE, GA(AS), GA(GL)). Obviously, these methods could be applicable to LLM scenarios. Furthermore, proprietary models such as Claude 3 and GPT-4-o, which are highly relevant in current LLM applications, are also omitted. Since proprietary and larger open-source models can exhibit unique behaviors under adversarial conditions, evaluating the proposed method on these systems is essential for demonstrating broad applicability and robustness. Without these evaluations, it’s unclear if the method generalizes well across the current landscape of LLMs, thus weakening the claim of practical relevance.

3. Concerns with Reproducibility:
The reproducibility of this work is called into question as the authors have not provided open-source code or comprehensive instructions to replicate the experiments. In the absence of these materials, other researchers cannot validate the results, explore variations of the methodology, or build upon the work. Reproducibility is a cornerstone of scientific research, and providing a well-documented codebase and dataset configurations is essential for enabling follow-up studies and independent verification. The lack of these materials raises concerns about the credibility and transparency of the findings. For the next revision, it would be beneficial for the authors to make their codebase publicly available, alongside detailed instructions on the experimental setup, hyperparameters, and any model configurations used, to facilitate reproducibility.

4. Ethical Considerations and Potential for Misuse:
The ethical implications of this research are insufficiently addressed, leaving key questions unanswered regarding how to detect or defend against the proposed adversarial methods. Research in adversarial attacks inherently carries dual-use potential, as it can be misused to compromise model reliability in deployed systems, affecting user trust and potentially leading to harm. The authors should explicitly discuss possible defense mechanisms or detection strategies that could mitigate the impact of the proposed attacks, thereby demonstrating a commitment to responsible research. Additionally, they should consider how their work might be misused if applied in malicious contexts and outline measures to prevent such outcomes. Providing recommendations for safeguards or limitations on how the method can be deployed responsibly would mitigate negative societal impacts and align the research with ethical standards in adversarial machine learning.

### Questions
1. Distinguish the technical contributions of this work from Li et al. (2023) (White-Box Multi-Objective Adversarial Attack on Dialogue Generation).

2. Please explain why multiple baselines are forgiven in Sec. 4.4 (FD, HotFlip, PWWS, BAE, GA(AS), GA(GL)).

3. How do the authors address ethical issues for their proposed method?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces DGAttack, a black-box adversarial attack framework that targets dialogue generation models using multi-objective optimization, aiming to minimize response coherence and maximize response length. This attack operates in scenarios where internal model details are inaccessible, making it practical for real-world AI systems.

### Strengths
- The paper proposes a bi-objective optimization framework (minimizing coherence, maximizing length) to generate adversarial samples. The use of the non-dominated sorting genetic algorithm (NSGA-II) to handle conflicting objectives is innovative.
- DGAttack succeeds in the challenging black-box setting, where only input and output prompts are used to craft adversarial attacks, without requiring model internals such as gradients or probabilities.
- The authors demonstrate DGAttack's effectiveness through empirical experiments across multiple datasets and models (BART, DialoGPT, T5). They show superior performance compared to both existing white-box and black-box approaches.
- This paper demonstrates DGAttack's transferability from smaller to larger models and between large models. One key advantage of black-box attack is that they can learn more general and transferable attacks.

### Weaknesses
 - The title is inaccurate. Since this paper only considers two conflicting objectives, I think it is not appropriate to use the word "multi". It should be "Black-Box Adversarial Attack on Dialogue Generation via Bi-Objective Optimization".
- The use of evolutionary algorithms, while effective, may lead to significant computational overhead, especially when optimizing across two objectives. The authors could provide more detailed discussions on computational costs and practical constraints in real-world applications. The current discussion in Appendix E should be included into more details. For example, does the computational cost of this method and the computational cost of baseline methods differ by orders of magnitude?
- This paper's experiments are focused open-source LLMs. However, the selling point of this paper is the black-box adversarial attack, so the experiment results on closed source models should also be provided, such as earlier version of GPT3.5 (If you think attacking GPT 4 is too difficult).

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
