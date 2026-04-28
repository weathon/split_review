# Digi-Q: Transforming VLMs to Device-Control Agents via Value-Based Offline RL

- Decision: Accept
- Avg Score: 4.80
- Scores: 3, 6, 6, 6, 3

## Abstract
Most paradigms for building foundation model agents rely on prompting or finetuning on existing demonstrations, but this is not sufficient in dynamic environments (e.g., mobile device control). In theory, while on-policy reinforcement learning (RL) should address these limitations, this approach itself is not quite effective at leveraging existing agentic data, especially when it is of low quality. An approach to address this issue is to use offline value-based RL but realizing value-based RL for agents has been elusive due to of stability and efficiency associated with running TD-learning at scale with vision-language models (VLMs). In this paper, we develop a scalable value-based RL approach called Digi-Q that makes it possible to train VLM agents with TD-learning. We situate our study in building GUI agents for Android devices. The key idea in Digi-Q is to perform TD-learning on a frozen, intermediate-layer representation of a VLM rather than training the whole VLM itself. Doing so successfully requires an initial phase of fine-tuning to prime VLM representations to feature actionable information that is critical for TD-learning. When done correctly, our approach is able to attain better performance per-unit compute FLOPS. To make maximal use of the learned Q-function, we devise a novel best-of-N policy extraction operator that imitates the best actions out of multiple candidate actions from the current policy as ranked by the value function. With no REINFORCE-style policy gradients that need careful tiuning and an efficient TD-learning approach, Digi-Q outperforms several strong prior methods on user-scale device control tasks in Android-in-the-Wild, attaining 9.9% of relative improvement over prior best-performing offline RL method in this domain.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes an approach, called Digi-Q, for learning useful behaviour for device-control by leveraging offline data and VLMs. The authors highlight the current difficulties of learning using temporal difference learning and large retrained models. To address this difficulty, the authors propose to pretrain the VLM with in-domain data with state and action pairs, together with labels indicating whether the resulting state has changed significantly after the taken action. Additionally, the authors propose to use a best-of-N action sampling strategy, where the best-of-N is calculated through an approximate Q function. On the Android-in-the-Wild (AitW) domain, experiments show that Digi-Q improves upon previous approaches. The authors also present compute efficiency comparisons and ablation studies on some of the choices within the algorithm.

### Strengths
The paper builds on recent algorithms and evaluates on domains that are increasingly important in the space of decision making and AI agents. The paper also highlights some of the challenges associated with reinforcement learning and VLM (e.g. instabilities that appear in practice) and proposes an approach that seems to present favorable results in experiments. Some of the ablations also give reasonable answer to important questions, for example the number of actions in the best-of-N sampling strategy.

### Weaknesses
The paper is generally not very rigorous from a scientific point of view. There are numerous descriptions of problems, hypothesis as to why one things are not working, and empirical justifiications that are unsubstantiated. For example the negative gradient hypothesis being mentioned multiple times originates from a paper on a preference fine-tuning, not agentic tasks. Other examples include the whole motivation in section 4.2: "REINFORCE [...] is brittle with off policy data"  "negative gradient [...] means careful tuning of learning rates must be done" ( "AWR is quite conservative and slow". When reading such statements, together with a complete misunderstanding of the fact that value-based methods do not equal off-policy learning, which also does not equates to offline learning (see Introduction), indicates to me that there is limited understanding and insights into what's happening, and therefore the contribution of the paper is lessened.

Arguably, the text could be fixed and made more precise, however these issues also arise in the algorithms and experiments. The proposed method, mixes quite a few things together: using the ArCHer learning rules, pretraining on in-domain data and best-of-N action sampling. For each of these choices, there is far from enough evidence to understand what is its importance.

Consider pretraining on in-domain data, the paper mentions that labels are created when s_{t+1} is significantly different from s_t using the l_2 distance. Is this a general or even reasonable objective? Does this assume that the environment is entirely controllable by the agent, or deterministic? Given many papers in the RL literature, it clearly does not seem to be the case. Also, there is no study on the sensitivity to value of the threshold epsilon for calculating labels. 

Also, looking at Figure 3 right, we see that when the number of actions for best-of-N is set to 1, the performance is similar to Filtered BC. Why do we not see performance difference given the fact the Digi-Q is built on pretraining the VLM first?

The main results raise a few questions. First, only 3 seeds are being used, please see the numerous papers that indicate that this a bad practice [1, 2]. Second, why is the performance of DigiRL different than the one reported in the original paper? Third, concerning the ablation in Table 3, how is the performance of AWR so low? Is the procedure for AWR not the same as the one proposed in DigiRL?

The results on compute efficiency conflate a few things together. Finetuning whole LLMs with RL can be troublesome (although it is possible as reported in a few recent papers), but this problem is mixed with compute efficiency. If performance degrades in the reported experiments, and full fine-tuning brings does not give as high a score as partial fine-tuning, it has little to do with compute efficiency, but rather with the practical challenges of full fine-tuning. In this sense, it is a bit meaningless to claim that partial fine-tuning is more efficient than full fine-tuning, if the used update rules don't work with full fine-tuning.

### Questions
Why use a separate policy network from the value? This is mentioned on the way, but never explained or referred.

In DigiRL, the authors perform a curriculum over tasks, is this strategy also employed here?

Throughout the paper, the best-of-N strategy is referred to as being novel. I do not care if a method is novel or not, but proposing a method that is not novel (it is an incremental improvement on AWR, filtered BC and BCQ [3]]), and referring to it as being novel is not great.

[1] Deep Reinforcement Learning at the Edge of the Statistical Precipice, Agrawal et al., 2022
[2] Deep reinforcement learning that matter, Henderson et al., 2018
[3] Off-Policy Deep Reinforcement Learning without Exploration, Fujimoto et al., 2018

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper develops a new RL method called Digi-Q. It addresses how to effectively use value-based offline reinforcement learning (RL) to train visual-language model (VLM) agents in dynamic environments (such as mobile device control) by training on frozen intermediate layer representations of the VLM through temporal difference (TD) learning instead of training on the entire VLM.
I think the main innovation is Digi-Q. According to the paper, they address a series of challenges brought about by large-scale value-based offline policy RL: training instabilities associated with running temporal difference (TD) learning on large models, and inefficiency of TD backup per unit of computation. If you solved any of them, I will think it's a good novelty.

### Strengths
1. The article is well-structured, with references for every sentence. And the author didn't speculate on the causes of certain phenomena observed in the experiments, without having conducted the experiments or found relevant references in the literature.
2. It solves a series of challenges brought about by large-scale value-based offline policy RL: training instabilities associated with running temporal difference (TD) learning on large models, and inefficiency of TD backup per unit of computation. It ensures innovation. 
3. It also gives annotations of the papers from which ideas were borrowed, so that reviewers will not always think of some familiar operations when reading the experimental part, and spend a lot of time to confirm whether there is plagiarism.
4. All research is based on the latest literature

### Weaknesses
1. Overfitting and Catastrophic Forgetting
2. Misclassification of Visual Changes
3. Real-World Applicability
4. General Limitations and Feedback
Check the Questions to see the details, thanks :)





Lack of research on the impact of other dimensions (such as data noise, and quality differences) on model performance

### Questions
In the paper, you mentioned that Digi-Q first fine-tunes representations of a VLM with a binary classification objective to enable it to pay attention to actionable features of an input scene. The sample step is in Figure 9 and it looks like targeted. How do you solve the Overfitting and Catastrophic Forgetting problem? Can you try to do some case studies or use different datasets to prove your performance improvement?  
You mentioned that observation is that in device control problems, a useful action should lead to a substantial visual change in the pixel values of a scene (e.g., successfully typing a search query and pressing enter on google.com should cause the page to change substantially to now show a list of search results, whereas an unsuccessful search attempt will change none to few pixels of the original scene). But in my daily life, the more possible is that a failed attempt can also lead to a substantial visual change. For a very common example, the page changes to whole white or 404 at my iPhone App when you fresh the web page but lose internet. Can you provide some statistical evidence for your observation? I think your assumption is to decline your model in generalization ability again. I know what Reinforcement Learning is but sometimes it's not normal in the real world.
Can you talk more about limitation? Do you ask some people to test your model and do some case studies? Do get some feedback? Like you said before, you have some observations, so I assume it's only only from you but also from your tester's feedback.

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
3

### Summary
This paper presents a novel method for training VLM-based RL agents. It is well known that training a VLM-based value network is highly unstable when using TD learning. This method first fine-tunes the VLM using representation learning to differentiate between actions that lead to transitions in the state space. The VLM parameters are then frozen, and the Q function on top of those layers is updated using the TD target. The policy is updated using the best of N actions from this Q function.

The main results focus on web-based navigation tasks, and the improvements are substantial. The accuracy per FLOP of training is also efficient and stable compared to fine-tuning an entire VLM.  There are extensive ablations verifying each part of the method.

### Strengths
* Benchmarks are sufficient; GPT-4V and Gemini are both s strong benchmarks.
* Qualitative visualizations strongly support the hypothesis.
* The ablations are numerous, exploring different representation learning methods to train the Q function, comparisons with Monte Carlo learning, and divergence from the behavior policy.
* The paper is extremely clear and well written.
* Experimental evaluations are strong and address difficult web navigation tasks.

I recommend acceptance of this work, it presents strong results in an area of RL that is of very high impact currently.  Using VLMs to perform RL tasks is currently a direction of interest to most of the RL community.

### Weaknesses
 * Novelty is a bit lacking, the main contribution of this method is simply fine-tuning upon the frozen lays using the TD loss after representation learning.  This is especially apparent put into the context of DigiRL

### Questions
This paper is very well written and does not warrant any immediate questions.

### Soundness
3

### Presentation
4

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
This paper introduces Digi-Q, a novel approach to making reinforcement learning work with large vision-language models (VLMs) for device control tasks. The authors tackle a challenging problem: while value-based reinforcement learning methods like Q-learning are known to be efficient, they've been notoriously difficult to use with large language models. The key insight of this work is that instead of trying to train the entire VLM using temporal difference (TD) learning, they first fine-tune the model's internal representations to better capture action-relevant features, then freeze these representations and only train a small Q-function on top. They also introduce a "Best-of-N" policy extraction method that samples multiple potential actions and trains the policy to imitate the ones rated highest by the Q-function. The authors evaluate their approach on Android device control tasks, showing improvements over previous methods and better computational efficiency than end-to-end TD learning. While the improvements are modest (about 10% better than previous methods) and limited to one domain, the work presents a practical approach to combining value-based reinforcement learning with large vision-language models, supported by thorough empirical validation and ablation studies.

### Strengths
The paper demonstrates several notable strengths across different dimensions. On the technical side, it successfully adapts Q-learning to work with large VLMs in a practical way. The two-phase approach of fine-tuning representations before freezing them for Q-learning is clever and addresses real computational challenges, while the Best-of-N policy extraction method offers a more stable alternative to traditional policy gradients (though the improvements are modest). The empirical work is thorough, with comprehensive ablation studies and comparisons against strong baselines like GPT-4V and Gemini, backed by proper statistical reporting across multiple runs. The presentation is clear and well-structured, with effective use of figures and helpful qualitative examples that illustrate how the method works in practice. From a practical perspective, the work addresses a real problem that practitioners face when trying to use Q-learning with large models, and while the 9.9% improvement isn't revolutionary, it represents meaningful progress. Importantly, the authors provide complete implementation details and hyperparameter choices, making their work reproducible. While none of these strengths are groundbreaking on their own, together they represent a solid engineering advance that makes value-based RL more practical with large models. The work is particularly strong in its empirical validation and clarity of presentation, even if the core technical innovations are relatively straightforward extensions of existing ideas.

### Weaknesses
The paper has several notable limitations that temper its impact. Most significantly, the evaluation is restricted to a single domain (Android device control), making it unclear whether the approach generalizes to other types of agent tasks or VLM applications. While the authors show a 9.9% improvement over previous methods, this is a relatively modest gain that comes with considerable complexity in the training pipeline. The theoretical foundation for the Best-of-N policy extraction approach is somewhat thin - while it works empirically, we lack a clear understanding of why this particular method is effective or how to choose the optimal value of N. The computational efficiency claims, while promising, would benefit from more detailed comparisons across different model scales and task complexities. There are also some concerning gaps in the analysis: the authors don't thoroughly explore failure cases or limitations of their method, and the stability analysis across different random seeds and hyperparameters could be more comprehensive. From a technical perspective, while the idea of fine-tuning representations before freezing them for Q-learning is practical, it's a relatively straightforward combination of existing techniques rather than a fundamental advance in how we approach VLM training. The ablation studies, while thorough in some areas, don't fully explore the sensitivity of the method to various design choices, particularly in the representation fine-tuning phase. Finally, the paper would benefit from a more detailed discussion of the computational resources required for training, as this is crucial information for practitioners considering adopting this approach.

### Questions
1. Could you discuss whether and how this approach might generalize to other domains? Have you attempted any preliminary experiments with different types of agent tasks?
2. The Best-of-N policy extraction method lacks strong theoretical justification. Could you provide more insight into why this approach works better than alternatives? How did you choose N=16 as the optimal value, and how sensitive is the method to this choice?
3. While you show improved compute efficiency compared to end-to-end TD learning, could you provide more concrete details about the total computational resources required for training? This would help practitioners better understand the real-world applicability.
4. Could you provide more detailed analysis of training stability across different random seeds and hyperparameters? The current results show standard deviations, but a deeper analysis would be valuable.
5. Could you provide examples of scenarios where your method struggles and analyze why these failures occur? The paper would benefit from a more thorough discussion of failure cases.
6. How dependent is your method on the specific VLM architecture used? Have you tested with different VLM backbones, and if so, how does the performance vary?
7. The representation fine-tuning phase seems crucial to your method's success. Could you provide more details about how sensitive the method is to different fine-tuning objectives or architectures? Have you explored alternative approaches to making VLM representations more action-aware?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents Digi-Q, a value-based offline reinforcement learning (RL) approach aimed at training vision-language models (VLMs) for device control, specifically in Android GUI tasks. Digi-Q introduces a stable temporal-difference (TD) learning method on frozen VLM layers, optimizing Q-values while avoiding end-to-end model instability. Digi-Q also introduces a unique Best-of-N policy extraction that selects the best action among multiple candidates to improve policy performance without using traditional policy gradients.

### Strengths
1. The paper proposes an innovative Q-value-based RL approach, which integrates TD-learning with VLMs, to increase sample efficiency for complex environments.
2. The paper introduces Best-of-N policy extraction, enhancing policy learning stability by leveraging multiple action candidates.
3. The paper demonstrates improved compute efficiency over end-to-end TD learning, effectively addressing scalability in large models.
4. Problem formulations are okay, evaluations over the AiTW subset are comprehensive
5. Paper writing is good and presentations of results are good.

### Weaknesses
1. *Lack of Clear Motivation for Offline Value-Based Approach*: The paper does not sufficiently motivate the use of an offline, Q-value-based RL approach for device control, especially given the recognized stability and efficacy of methods like Advantage-Weighted Regression (AWR) and Generalized Advantage Estimation (GAE) as shown in previous work by [1] Bai et al. and [2] Pan et al. In particular, Q-value-based methods are known to introduce instability, especially in scenarios with partial observability, where AWR and GAE have demonstrated superior stability and simpler implementation when dealing with much more unstable and complex environments for on-device control. The paper fails to address why a Q-learning approach is preferable, especially given the challenges of learning accurate Q-functions in high-dimensional, partially observed environments typical of device control. The instability issues associated with TD learning, especially with function approximation, are not adequately addressed, and the paper does not provide a clear rationale for why these challenges are worth tackling when more stable alternatives exist.

2. *Limited Novelty Compared to DigiRL*: The paper's novelty is questionable when compared with previous works, especially DigiRL [1] by Bai et al. While Digi-Q proposes certain adaptations, such as the Best-of-N policy extraction, these contributions appear to be incremental rather than fundamentally advancing the state of value-based RL for device control. The core idea of using a VLM with a frozen encoder and training a Q-function is not substantially different from existing approaches, and the Best-of-N policy extraction, while potentially useful, does not represent a major breakthrough in RL methodology. The paper does not clearly articulate how these adaptations overcome the inherent limitations of value-based methods in complex environments.

3. *Concerns Over Experimental Data Reliability*: The experimental results lack reliability, particularly in light of my own testing experience. Many observed metrics and success rates in Digi-Q’s experiments suggest significant variance, casting doubt on the robustness of the results. Additional benchmarks and repeated trials would help validate these findings and ensure their reproducibility. The reported fluctuations in success rates, especially when compared to previously published results, are concerning. The paper does not provide sufficient detail on the experimental setup, making it difficult to assess the validity of the results. The lack of error bars or confidence intervals further exacerbates these concerns.

4. *Assumption of High-Quality Offline Data Set*: The paper's methodology hinges on a high-quality, well-curated offline dataset (e.g., AiTW), assuming this accurately represents all relevant scenarios. However, for real-world device control applications, where app behaviors and mobile environments change frequently, the method should ideally support a combination of offline and online data collection. Relying solely on offline data for pretraining limits adaptability, and the paper does not provide sufficient insight into how the pretrained policy can improve performance in dynamic online interaction settings. The paper does not adequately address the limitations of using a static dataset, particularly in the context of real-world device control where the environment is constantly evolving. The lack of a mechanism for adapting to new scenarios or incorporating new data is a significant weakness.

5. *Lack of Evidence for Scalable Training at Scale*: Although the paper posits the question, “Can we train VLM agents at scale with value-based RL?” it falls short in demonstrating this scalability. There is a lack of empirical evidence supporting large-scale training or fine-tuning experiments, and the scalability of Digi-Q in practical, resource-intensive environments remains unclear without these demonstrations. The paper does not provide sufficient evidence that the proposed method can scale to larger models or more complex tasks. The experiments are limited in scope and do not address the practical challenges of training large-scale models in resource-constrained environments.

### Questions
1. In Table 1, the main comparisons of different agents across various settings raise significant concerns about the reliability and consistency of the reported results. The paper claims, "To be consistent with prior work (Bai et al., 2024), results are evaluated with the autonomous evaluator with the first 96 instructions in the train and test set." However, it appears that results for GPT-4V, Gemini 1.5 Pro, and CogAgent were directly copied from the DigiRL paper [1], while experiments were "reconducted" only for AutoUI and DigiRL. Notably, the results for AutoUI show a significant improvement compared to the previously reported figures in [1], while DigiRL’s offline results are selectively reduced.  This selective approach to data raises substantial concerns. If the intention was to reproduce results, it would be expected that any shifts in performance would be consistent across all models, not selectively applied. Furthermore, a success rate fluctuation of up to **5%** relative to previously reported results, given that the reported improvements are relatively modest, calls into question the robustness and reliability of the findings. Such fluctuations suggest that the experimental setup or evaluation may not be sufficiently stable, casting doubt on the paper's claims of improvement. I would appreciate clarification regarding the rationale for selectively re-evaluating some baselines and not others, as well as an explanation for the considerable performance variance observed. Without such transparency, the contributions of this work appear uncertain and potentially unreliable.

     **Hopefully, you can answer my concerns regarding these messy results or the "free lunch results" you used here.**

2. Why did you only evaluate your model on two subsets of AiTW? Could you explain the decision not to include other tasks, such as app installation, which would offer a broader evaluation of your model’s capabilities?

3. How similar are the evaluation tasks to those used during training? Please clarify the degree of overlap or differences, as this impacts how well the model generalizes beyond its training set.




[1] Hao Bai, Yifei Zhou, Mert Cemri, Jiayi Pan, Alane Suhr, Sergey Levine, and Aviral Kumar. Digirl: Training in-the-wild device-control agents with autonomous reinforcement learning, 2024.

### Soundness
2

### Presentation
3

### Contribution
1
