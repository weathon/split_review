# Identifying and Tuning Safety Neurons in Large Language Models

- Decision: Accept
- Avg Score: 6.20
- Scores: 6, 8, 6, 8, 3

## Abstract
Safety alignment for Large Language Models (LLMs) has become a critical issue due to their rapid progress. However, our understanding of effective safety mechanisms in LLMs remains limited, leading to safety alignment training that mainly focuses on improving optimization, data-level enhancement, or adding extra structures to intentionally block harmful outputs. To address this gap, we develop a neuron detection method to identify safety neurons—those consistently crucial for handling and defending against harmful queries. Our findings reveal that these safety neurons constitute less than $1\%$ of all parameters, are language-specific and are predominantly located in self-attention layers. Moreover, safety is collectively managed by these neurons in the first several layers. Based on these observations, we introduce a $\underline{S}$afety $\underline{N}$euron $\underline{Tun}$ing method, named $\texttt{SN-Tune}$, that exclusively tune safety neurons without compromising models' general capabilities. $\texttt{SN-Tune}$ significantly enhances the safety of instruction-tuned models, notably reducing the harmful scores of Llama3-8B-Instruction from $65.5$ to $2.0$, Mistral-7B-Instruct-v0.2 from $70.8$ to $4.5$, and Vicuna-13B-1.5 from $93.5$ to $3.0$. Moreover, $\texttt{SN-Tune}$ can be applied to base models on establishing LLMs' safety mechanism, effectively diminishing models' harmful scores from around $100$ to $5.3$, $13.5$, and $13.8$ for LLama2-7B-Base, LLama3-8B-Base, and Mistral-7B-v0.1, respectively. In addition, we improve the LLMs' safety robustness during downstream tasks fine-tuning by separating the safety neurons from models' foundation neurons.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents an innovative method for effectively and efficiently detecting and fine-tuning "safety neurons," which comprise less than 1% of model parameters and are predominantly located in low-level self-attention layers. The authors conducted related experiments to verify that safety mechanism is resilient but breakable. Notably, the proposed tuning method $\texttt{SN-Tune}$ enhances model safety without sacrificing performance, significantly lowering harmful output scores in both instruction-tuned and base models. This approach also improves safety robustness during downstream fine-tuning tasks, such as GSM8K, by isolating safety neurons from foundational ones. Additionally, the authors explored the influence of the number of safety documents and performed grid searches over learning rates and training epochs in their ablation study.

### Strengths
* The paper is well-written and the idea is easy to be understood.
* Interesting verification of safety neurons. The authors used detailed experiments to verify that the identified safety neurons have a significant impact on the model's safety and found that these safety neurons are relatively few in number, primarily located in the self-attention layers of the first few blocks of the model.
* Extensive experiments. The authors validated the effectiveness of $\texttt{SN-Tune}$ on both instruction models and base models, as well as on downstream fune-tuning tasks.

### Weaknesses
 * Although authors  empirically verify the identified safety neurons by their detection method have a significant impact on the model's safety, the proposed detection method lacks theoretical support for why it can identify neurons that have such a significant impact on safety.
* Why does the RHS of equations（4）（5） of the main paper  seem to be  independent of $l$ (the $l$-th neuron in the $i$-th layer)? They appear to be the same value for different $l$. Also in appendix, it is confusing why $h_{ffn}$ is a vector, could you help write the specific form? And how can you get (8) from (7) since x is a input for $W_{down}$  in (8) but not for $W_{down}$ in (7)? The notation in equations (7) and (8) is unclear, specifically how the input $x$ is related to the weight matrix $W_{down}$ in both equations. It seems that $W_{down}$ is being applied to different inputs in each case, which needs clarification. Additionally, the dimensions of $h_{ffn}$ are not clearly defined, which makes it difficult to understand the subsequent calculations.
* For downstream fine-tuning tasks, could you consider more datasets like Alpaca or Dolly to verify the effectiveness of $\texttt{RSN-Tune}$?

### Questions
* In table 4, why you used llama2-7B-chat (which is a safety-aligned model) and  Mistral-7B-Instruct-v0.2 (which is not a safety-aligned model) for downstream fine-tuning tasks ? How about use Mistral-7B models that have been safety-aligned by your proposed method $\texttt{SN-Tune}$?
* This paper [1] also proposes some detection methods to find safety neurons and perform operations on the identified neurons to reinforce the model's safety. Could the authors discuss more between this paper and  findings of your paper?
* There are several papers [1][2][3][4] also study on safety neuron/ safety mechanism/ backdoor, it will better if  the authors  could add some comments on them.

If the authors address most of my concerns, I would consider increasing the score.

[1] Wei, Boyi, et al. "Assessing the brittleness of safety alignment via pruning and low-rank modifications." arXiv preprint arXiv:2402.05162 (2024).

[2] Chen, Jianhui, et al. "Finding Safety Neurons in Large Language Models." arXiv preprint arXiv:2406.14144 (2024).

[3] Hsu, Chia-Yi, et al. "Safe LoRA: the Silver Lining of Reducing Safety Risks when Fine-tuning Large Language Models." arXiv preprint arXiv:2405.16833 (2024).

[4] Zhang, Zhengming, et al. "Neurotoxin: Durable backdoors in federated learning." International Conference on Machine Learning. PMLR, 2022.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces the crucial concept of "safety neurons", which investigates neural activation patterns when large language models encounter unsafe instructions and jailbreak attacks. The definition of "safety neurons" is concise, clear, and effective. Furthermore, the paper presents several significant findings: the proportion of safety neurons is remarkably small, constituting less than 1% of total parameters; the robustness study of safety neuron locations reveals sensitivity decreases from front to back layers, with safety neurons in the first 10-20 layers being more sensitive; and the transferability of safety neurons across multiple languages is investigated. Additionally, the authors propose the SN-Tune method, which exclusively fine-tunes safety neurons, achieving enhanced safety conditions by tuning only a small subset of parameters without catastrophic forgetting of general knowledge. The paper is easy to follow and well-written, with clear methodology explanations, comprehensive experimental results, and logical organization of findings.

### Strengths
1. Originality: The paper introduces an innovative approach to understanding LLM safety through the novel concept of "safety neurons." The clear definition and identification method for these neurons represents a significant departure from traditional safety alignment approaches, offering a fresh perspective on model safety mechanisms.

2. Experimental Rigor: The research demonstrates exceptional thoroughness in its experimental investigation, providing comprehensive analysis of safety neurons' characteristics, including their proportion (<1% of parameters), location sensitivity, robustness, and cross-lingual transferability. Each finding is well-supported by detailed empirical evidence.

3. Practical Impact: The proposed SN-Tune method offers a highly effective solution for enhancing model safety while maintaining general capabilities. Its ability to achieve significant safety improvements by tuning only a small subset of parameters makes it both efficient and practical for real-world applications, demonstrating immediate value for improving existing language models.

### Weaknesses
1. Theoretical Foundation: The paper lacks deeper theoretical analysis of observed phenomena. For example:
- The mechanism behind the "back-to-front deactivation" pattern remains unexplained, where safety breakdown only occurs after almost all safety neurons are deactivated. This observation raises questions about the necessity of deactivating all safety neurons for a safety breach, and whether the observed pattern is a fundamental property or an artifact of the experimental setup. It would be beneficial to explore if the deactivation of a critical subset of safety neurons is sufficient to trigger a safety breach and how this subset varies across different layers.
- This observation raises questions about whether the neurons in later layers are truly "safety neurons". The paper does not provide a clear definition of what constitutes a "safety neuron" beyond its empirical identification. It would be helpful to explore if the neurons in later layers are merely relaying information from earlier layers or if they have their own unique safety-related functions. The lack of a mechanistic understanding of the role of these neurons limits the interpretability of the results.
- The nature and characteristics of overlapping safety neurons across different languages deserve more theoretical investigation. The paper reports a 30% overlap, but it does not delve into the functional similarity or differences between these overlapping neurons. It would be valuable to investigate if these overlapping neurons perform similar functions across languages or if they are adapted to language-specific safety mechanisms.

2. Limited Analysis of Cross-lingual Safety Mechanisms:
- While the paper identifies low overlap (30%) between safety neurons across languages, it doesn't explore:
  * The characteristics of these overlapping neurons. A deeper analysis of the shared neurons is needed to understand if they are related to universal safety concepts or if their overlap is coincidental. For example, do they respond to similar types of unsafe prompts or exhibit similar activation patterns?
  * Why certain neurons are shared across languages while others are language-specific. The paper should investigate the linguistic or cultural factors that might influence the localization of safety mechanisms in the model. Are there specific features of languages that lead to different safety neuron distributions?
  * The potential universal principles of safety mechanisms across languages. The paper should explore whether there are common underlying principles that govern safety mechanisms across different languages, even if the specific neurons involved are not identical. This could involve analyzing the types of safety-related information encoded by the neurons and how they interact with each other.

### Questions
1. Position-Dependent Activation Patterns:
- How does the position of jailbreaking prompts affect safety neuron activation? Is there a correlation between prompt location and safety neuron response?
- Do safety neuron distributions shift in long-text scenarios？How does the context window length affect the stability of safety neurons?

2. Dynamic Nature of Safety Neurons during Fine-tuning:
- Can non-safety neurons transform into safety neurons during full-parameter fine-tuning? How does SN-Tune handle the potential emergence of new safety neurons?
- How can we track and verify the transformation of regular neurons into safety neurons?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a method for identifying safety neurons in Large Language Models (LLMs), which are critical for managing harmful queries and represent less than 1% of the model parameters. It introduces a technique named SN-Tune that focuses on tuning these safety neurons while maintaining the overall capabilities of the models. The findings indicate significant reductions in harmful scores, with Llama3-8B-Instruction decreasing from 65.5 to 2.0. Furthermore, the approach improves safety robustness during fine-tuning by separating safety neurons from foundation neurons.

### Strengths
1. The paper writing is good and very easy to follow.
2. The defense performance is strong, even compared with current SOTA defense method.
3. The logic of this article is also very coherent. The author first suggests enhancing the effectiveness of the model's safe responses through a more detailed approach to neuron control. The author also conducted relatively detailed ablation experiments to support the faithfulness of safe neurons.

### Weaknesses
I believe the biggest shortcoming of this paper is that the description of the experiments for identifying safe neurons is very insufficient. The author does not mention the datasets used, parameter details, or the time costs associated with the experiments. The dataset is crucial because it relates to the generalizability of the method. For example, if the author only uses datasets related to violence to identify neurons, but the identified safe neurons still demonstrate good defensive capabilities against attacks related to pornography or other safety categories, including jailbreaking attacks, it suggests that safe neurons are relatively fixed within LLMs. However, the author does not mention this point.

### Questions
please see weakness.

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
4

### Summary
The authors first introduce a technique for detecting LLM neurons (i.e. rows or columns in LLM weight matrices) responsible for safety (e.g. refusing to comply with harmful instructions). The method is fairly simple: a neuron is said to be a safety neuron if deactivating it changes the final next-token embedding by at least some threshold (measured in Euclidean distance) on each of a set of inputs. They validate that deactivating these neurons indeed increases harmfulness scores of three open-weight models, while preserving performance on capabilities benchmarks.

They then propose a safety fine-tuning method, named SN-Tune, which tunes only these safety neurons, keeping the remaining ones fixed. They show SN-tune significantly reduces harmfulness scores across several open weight models; e.g. Llama3-8B’s score decreases from 65.5 to 2.0. Finally, they propose a refinement of SN-Tune, termed RSN-Tune, which also identifies neurons responsible for model capabilities, and only tunes safety neurons which do not overlap with such capabilities neurons, hence mitigating capability degradation during safety tuning. Additional experiments include a study of the overlap of safety neurons across languages (which they find to be small) and of applying SN-tune to pre-trained models (rather than already-fine-tuned models).

### Strengths
1. Simplicity of safety neuron detection: their notion of safety neuron is conceptually simple and can be computationally ascertained (instead of relying on manual analyses). Their later experiments indicate that one can indeed obtain a useful safety tuning algorithm by using their safety neuron detection method.

1. Empirical insights into how safety mechanisms are implemented in LLMs: the paper’s results indicate that safety neurons are very concentrated (1% of parameters), occur primarily in self-attention modules and in earlier layers, and are mostly not shared across languages. These insights seem relevant for the community as a whole, particularly when devising defenses to multi-lingual attacks.

1. Relevance of results for practitioners: one of the biggest hurdles in safety tuning is the performance degradation it usually entails if done in a naive way. The results in the paper suggest SN-tune might be useful for practitioners looking to safety-tune models without harming their capabilities. In particular, one could in principle automatically detect safety neurons using a small corpus of examples, rather than requiring manual analyses or large corpora.

1. The paper is written mostly clearly and was easy to follow.

### Weaknesses
1. Lack of detail on how foundation neurons are detected: in Section 4, the authors propose not tuning safety neurons that also serve as foundation neurons (i.e. play  a role in model capabilities). However, they do not clarify how they detect the foundation neurons. This harms the reproducibility of the RSN-tune results. It is unclear what specific criteria are used to determine if a neuron is a foundation neuron, and how this differs from the safety neuron detection process. The authors should specify the dataset used for this detection, the threshold used, and whether the same distance metric is used as in safety neuron detection. Without these details, it is difficult to assess the validity of the RSN-tune results.

1. Notation and presentation in Section 2.1: I would recommend revising the presentation in the Accelerated Safety Neuron Detection. For example, the authors write that Mask is an identity matrix, which, as stated, cannot be true. Looking at the appendix, it seems they might mean it is a binary matrix (i.e. the entries are 0 or 1). Also, the authors could clarify what they mean by parallel computations. Does this simply mean adding many computations in a batch? Generally, it seems that their notion of safety neuron is embarrassingly parallelizable, in the sense that their criterion can be computed independently for all neurons. The description of the masking operation and parallel computation is vague and lacks sufficient detail for a reader to fully understand the implementation. The authors should clarify whether the mask is applied element-wise or through matrix multiplication, and provide more detail on the parallelization strategy.

1. Missing citation of Kotha et al. (2023) in section 2.3.2: one relevant work concerning multi-lingual attacks on LLMs is Understanding Catastrophic Forgetting in Language Models via Implicit Inference, by Kotha et al. 2023. They show that translating harmful instructions into low-resource languages can elicit harmful responses, which can then be translated back to the original language. Their results are complementary to the author’s findings that safety neurons have little overlap across languages.

1. Another work the authors do not discuss, but which I believe is relevant and complementary to their results, is Mechanistically analyzing the effects of fine-tuning on procedurally defined tasks, by Jain et al. (2024). Amongst other results, Jain et al. also find that the effects of fine-tuning can be neutralized by pruning a small number of neurons.

### Questions
1. Would it be correct to conclude from lines 362-363 that your results indicate that base models already contain safety neurons, despite not being safety-tuned? 

1. It could be useful to have a study on the distribution of safety neurons in the base models to verify they share similar properties to those in fine-tuned models, i.e. being concentrated (<1% of parameters) and being predominantly present in earlier layers and attention modules. 

1. Similarly, one could study whether their harmfulness scores get somehow even worse when these neurons are disabled. To make this non-trivial, you could have “safe-behavior-inducing” few-shot examples in the prompt, for example.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper identifies safety neurons that are associated with safety alignment in LLMs. The authors claim that the safety neurons constitute less than 1% of all parameters, and they are predominantly located in self-attention layers. Experimental results have been provided

### Strengths
This paper deals with an important topic, the safety issue of LLMs – for safety alignment.

### Weaknesses
### weaknesses:
- My biggest concern is the distinction between paper, Zhao et al (2024b) [1]. I believe this submission’s section 2.1 is the meat of the work, but the formulations are all found in Zhao et al (2024b) [1] – just the same. Then, this submission’s distinctive contribution is very unclear. The only difference is (3) where the authors feed harmful queries and see the activations (although the sentence in lines 124-125 is broken, so it is speculated. It is impossible to know their actual implementation.) However, the entire formulations is just the same with the other paper [1], with only a minor tweak with harmful queries for safety context.

- Moreover, the authors failed to properly provide a reference for the formulation/equation (1) and (2) and give credit to the authors of the paper [1]. The paper [1] is referred to only for the parallel neuron detection method. ((4), (5), and (6)). 

- Moreover, in terms of the paper’s direction and theme, this submission’s distinctive novelty from the following paper is unclear: “Assessing the Brittleness of Safety Alignment via Pruning and Low-Rank Modifications,” [2]. This paper also identifies safety components in LLMs.

- Unlike the authors’ statement, “Regarding general capability, deactivating the safety neuron shows minimal impact, “similar to deactivating randomly selected neurons”,……” in Table 1, Deact_SN’s Avg. Capability is constantly, always lower than Deact-R, which hints that the safety neurons are also contributing to general capability. If the weights were purely safety neurons, when they were pruned, they shouldn’t impact the general capability even with no need to compare it with Deact-R. But, the table result shows there exists an impact on general capability. 

- In order to conclude “Safety neurons predominantly reside within the self-attention layers.”, the authors should have reported the original number of neurons and the proportion of safety neurons in feed-forward and self-attention layers, respectively – not just the split. The provided split of safety neurons between self-attention and feed-forward layers does not account for the underlying distribution of neurons in these layers. A more informative metric would be the ratio of safety neurons to the total number of neurons in each layer type. This would clarify whether the observed distribution is due to a higher concentration of safety neurons in self-attention layers or simply a reflection of the overall neuron distribution.

- For section 3, “Efficient Safety Training” the authors claimed SN-Tune is efficient by comparing the training cost with Circ-Break. However, SN-Tune requires a process and resources and effort to “identify” the safety neurons. Only after the neurons are obtained, the SN-Tune can be applied. Hence, it is not a fair comparison. The cost/effort for identifying the safety neurons must be taken into account, but they were not in this submission. The authors should provide a detailed breakdown of the computational cost associated with identifying safety neurons. This should include the time and resources required for data collection, processing, and the application of the detection method. Only then can a fair comparison be made with other methods.

- It is unclear the impact of RSN-Tune compared to SN-Tune by looking at the results of GSM8K in Table 4.

- This submission lacked an important and nominal paper in reference, with regard to neuron importance, Pavlo Molchanov, Arun Mallya, Stephen Tyree, Iuri Frosio, and Jan Kautz. Importance estimation for neural network pruning. 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR).

### Questions
* From which figure/table can we infer that “1%” are safety neurons?
* Why were helpfulness scores not reported?
* Why were Llama2 instruction-tuned models not reported in Table 2? It is known that Llama2 is more resilient than Llama3 in terms of instruction following. Hence, the Llama2's results for Fig 2 need to be reported.
* What’s language X and Y in Fig 5? 
* Where are the results of the five languages? 
* What is the objective of having section 2.3.2 regarding the theme of the paper?
* What is “Language-specific neurons” in line 291? It has not been defined nor introduced beforehand.

### Soundness
2

### Presentation
3

### Contribution
2
