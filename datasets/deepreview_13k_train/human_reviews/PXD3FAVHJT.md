# Understanding the Effects of RLHF on LLM Generalisation and Diversity

- Decision: Accept
- Scores: 8, 6, 3

## Abstract
Large language models (LLMs) fine-tuned with reinforcement learning from human feedback (RLHF) have been used in some of the most widely deployed AI models to date, such as OpenAI's ChatGPT or Anthropic's Claude. % , or Meta's LLaMA-2.
While there has been significant work developing these methods, our understanding of the benefits and downsides of each stage in RLHF is still limited. To fill this gap, we present an extensive analysis of how each stage of the process (i.e.~supervised fine-tuning (SFT), reward modelling, and RLHF) affects two key properties: out-of-distribution (OOD) generalisation and output diversity. 
OOD generalisation is crucial given the wide range of real-world scenarios in which these models are being used, while output diversity refers to the model's ability to generate varied outputs and is important for a variety of use cases.
\changed{We perform our analysis across two base models on both summarisation and instruction following tasks, the latter being highly relevant for current LLM use cases.}
We find that RLHF generalises better than SFT to new inputs, particularly as the distribution shift between train and test becomes larger.
However, RLHF significantly reduces output diversity compared to SFT across a variety of measures, implying a tradeoff in current LLM fine-tuning methods between generalisation and diversity. Our results provide guidance on which fine-tuning method should be used depending on the application, and show that more research is needed to improve the tradeoff between generalisation and diversity.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper empirically investigates the difference in generalization and generation diversity for LLMs trained with supervised learning and reinforcement learning for text summarization and instruction following. Moreover, they evaluate best of N (BoN), a very strong method for text summarization, as an additional method to test generalization of language models. They ultimately find evidence for RLHF improving generalization over supervised learning but at the cost of generation diversity.

### Strengths
- Their thorough investigation of RLHF vs SFT generation quality is very valuable. This work helps improve our understanding of why RLHF policies have empirically seemed to perform well in practice with users where more OOD data is likely encountered. 
- The paper is very clearly presented and investigates two popular settings for RLHF finetuning.

### Weaknesses
Minor Comments:
For summarization, it appears that pretrained models already perform very well for CNN daily mail. Would the same diversity, generalization, performance relationships be seen when evaluating OOD performance on a different summarization dataset where Llama2 7B does not perform as well? Or perhaps more simply, when trained on CNN as in-distribution, how is OOD performance to the harder TL;DR task?

### Questions
Please refer the questions posed in the weaknesses section.

### Soundness
3 good

### Presentation
4 excellent

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
This paper aims to study the effects of RLHF for fine-tuning LLMs, focusing on out-of-distribution generalization and output diversity metrics. Through empirical experiments, this paper finds that RLHF can outperform SFT in terms of out-of-distribution generalization but at the cost of a decrease in output diversity. Such observations may help in better applying RLHF or SFT in specific applications.

### Strengths
- This paper conducted extensive experiments to elucidate why RLHF behaves differently from SFT. The experimental setup is sound, and the empirical results may inspire future progress in this direction.

- The paper is well-writen and easy to follow in general.

### Weaknesses
 - Missing Related Work

In fact, there is a theoretical comparison of RLHF and SFT-style methods in the framework of imitation learning [1]. Indeed, LLMs are imitating human speech. In that framework, RLHF corresponds to adversarial imitation learning (AIL) methods, and SFT corresponds to behavioral cloning (BC). To the best knowledge of the reviewer, that theoretical study reveals that AIL (RLHF) methods can have better out-of-distribution generalization performance than BC (SFT) because AIL methods optimize their policy on out-of-distribution states (prompts) and rigorously prove this phenomenon. I believe this related work is insightful for studying the advantages of RLHF over SFT, and this paper should be mentioned in the related work.

[1] Xu, Tian, et al. "On the generalization of adversarial imitation learning and beyond." *arXiv preprint arXiv:2106.10424* (2021).


- Typos and Writing Suggestions

1. There are two minus symbols in Equation (1).
2. It seems unusual to draw a conclusion in Section 6.3 while presenting empirical evidence in Appendix I.


- Concerns about RLHF Training Quality

The empirical evaluation heavily relies on the training quality of each algorithm, and the reviewer is uncertain about whether RLHF is trained to a high standard. The paper freezes some layers of LLMs when using RLHF, which may limit the representation capacity. This raises concerns about whether the training of RLHF is of good quality. Specifically, the paper does not provide sufficient details on the reward model training, such as the validation accuracy or the training curves of the PPO algorithm. This lack of information makes it difficult to assess the reliability of the empirical results, especially given that the performance of RLHF is sensitive to the quality of the reward model and the PPO training process. The absence of these details makes it difficult to ascertain if the observed performance differences between RLHF and SFT are due to the inherent properties of the algorithms or simply due to suboptimal training of the RLHF model.

### Questions
The major concerns stem from the fact that the empirical evaluation heavily relies on the training quality of each algorithm, and the reviewer is uncertain about whether RLHF is trained to a high standard.

**Question 1**: Do empirical conclusions heavily depend on the training status of the reward model and PPO? The reviewer observed that this paper freezes some layers of LLMs when using RLHF, which may limit the representation capacity. Thus, the reviewer questions whether the training of RLHF is of good quality. Could this paper provide the evaluation accuracy of the reward model and training curves of PPO?

**Question 2**: Why not use entropy as a metric of diversity (although existing evaluation methods are acceptable)?

**Discussion**: This paper mentions that "Future work should investigate why RLHF reduces the output diversity so much," and the reviewer would like to point out some observations: the optimal policy by RL algorithms is deterministic (i.e., less diversity), if there is no tie in the reward value, there is no KL penalty, and the optimization is done perfectly. When there is a KL penalty, a recent paper shows that this corresponds to "soft Q-learning" [2]. In that case, the reward model is optimized perfectly. Although the algorithm in [2] is not applicable to the true RLHF setting where we only have out-of-distribution prompts and no preference labels, the viewpoint in [2] is insightful for in-distribution training.

[2] Rafailov, Rafael, et al. "Direct preference optimization: Your language model is secretly a reward model." *arXiv preprint arXiv:2305.18290* (2023).

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the effects of RLHF on generalization and diversity. Specifically, the authors look at the three stages in RLHF: supervised fine-tuning, reward modeling, and reinforcement learning. They conduct experiments that show that RLHF generalizes better than SFT to new inputs, but reduces output diversity.

### Strengths
The writing of the paper is clear and easy to follow. The paper studies three different aspects of performance, including in-distribution generalization, out-of-distribution generalization, and diversity. As far as I know, this covers a more comprehensive study on RLHF -ine-tuned model behavior than most observational studies in the literature.

### Weaknesses
This paper does not offer any new insight or novel methods compared to existing work in the literature, and no new methods have been proposed. First of all, the generalization capabilities offered by RLHF has been widely observed in state-of-the-art models, with clear comparisons and case studies of output from pretrained, instruction fine-tuned, and RLHF fine-tuned models (see, for example, the Llama-2 paper). The mode collapse phenomenon from RLHF has also been widely observed and measured. Maybe the only novelty this paper offers is evaluation on an array of sentence-level diversity metrics. Furthermore, the claims made in the paper are not very well-justified by experiment results, and some experiment details are lacking. Only two sets of experiments, namely summarization and instruction following, are conducted on one single model (Llama-7B), yet the paper makes a general claim about the effects of RLHF. More experiments on different models at potentially different scales could be helpful, but still, the contribution seems to be incremental.

My main concern is the contribution. Some additional questions are listed below for clarification, but unless the authors could justify their contribution through substantial experiments (on different models at different scales) and more in-depth analysis, I still lean towards rejection.

### Questions
The paper makes some unspecified claim that would need justification or further explanation. For example, on page 2, summary of contributions, the third bullet point: "...implying that such models tend to produce text of a specific style regardless of the input". How does one arrive at the "style" conclusion?

Why is there no error bars in Figure 5? Could you plot error bars over different choices of outputs from among the set of outputs to the same input?

Are the OOD datasets considered OOD for fine-tuning, or both fine-tuning and pretraining? The CNN/DailyMail dataset is most probably included in the pretraining dataset of Llama-7B.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor
