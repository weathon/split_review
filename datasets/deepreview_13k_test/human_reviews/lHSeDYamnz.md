# Catastrophic Failure of LLM Unlearning via Quantization

- Decision: Accept
- Scores: 6, 8, 6, 6, 5

## Abstract
Large language models (LLMs) have shown remarkable proficiency in generating text, benefiting from extensive training on vast textual corpora. However, LLMs may also acquire unwanted behaviors from the diverse and sensitive nature of their training data, which can include copyrighted and private content. Machine unlearning has been introduced as a viable solution to remove the influence of such problematic content without the need for costly and time-consuming retraining. This process aims to erase specific knowledge from LLMs while preserving as much model utility as possible. Despite the effectiveness of current unlearning methods, little attention has been given to whether existing unlearning methods for LLMs truly achieve forgetting or merely hide the knowledge, which current unlearning benchmarks fail to detect. This paper reveals that applying quantization to models that have undergone unlearning can restore the "forgotten" information. We conduct comprehensive experiments using various quantization techniques across multiple precision levels to thoroughly evaluate this phenomenon. We find that for unlearning methods with utility constraints, the unlearned model retains an average of 21\% of the intended forgotten knowledge in full precision, which significantly increases to 83\% after 4-bit quantization. Based on our empirical findings, we provide a theoretical explanation for the observed phenomenon and propose a quantization-robust unlearning strategy aimed at mitigating this intricate issue. Our results highlight a fundamental tension between preserving the utility of the unlearned model and preventing knowledge recovery through quantization, emphasizing the challenge of balancing these two objectives. Altogether, our study underscores a major failure in existing unlearning methods for LLMs, strongly advocating for more comprehensive and robust strategies to ensure authentic unlearning without compromising model utility. Our code is available at: https://anonymous.4open.science/r/FailureUnlearning-20DE.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the problems that arise when quantizing models after unlearning. The authors also propose a quatization-robust unlearning algorithm.

### Strengths
1. The paper is original to my knowledge.
2. The writing is clear and flows well.
3. The problem is well motivated --- I do think unlearning is largely studied in full precision and the effects of quantization are important to understand given that its a common practice.

### Weaknesses
1. **Presentation** I found the results incredibly difficult to parse. The large tables are hard to exact trends from and I think at times the results that matter are actually split across more than one of these tables or duplicated. For example, Table 3 has some of the data in Table 1 but it's missing other rows one might care about. I was flipping back and forth a bunch and it is very hard to internalize the trends. An informative visualization of this data is missing.
2. **Unclear Experimental Setup** I see in the formal notation that $f_\text{target}$ is the base model, as in one that should know the sensitive/private info and one one which unlearning algorithms haven't yet been run. It isn't clear what that model is -- what size, what training data, how it is trained etc.
3. **Limited Data Scope** The experiments make use of two datasets that I have not seen in many other unlearning papers.

### Questions
1. **Presentation** Can you provide some compelling plots here? Is the point that the pink rows in Table 1 are bad? The have still unlearned, just not as much as the full precision. Can you elaborate on the problem here and on how big an effect the solution offers? Overall, I'm hoping you can convey the issue and the positive results in plots or otherwise in concise tables. The results are very hard to parse.
2. **Unclear Experimental Setup** What is $f_\text{target}$? What has it been trained on? Do all your experiments consider the same model? How do things change with other models? Larger models?
3. **Limited Data** What is in the Books and the News datasets that might need to be unlearned? What can we learn from these experiments that might translate to private data or sensitive data? Can the experiments be expanded to use common unlearning tests (TOFU (for individual privacy), WMDP (for toxic output), HarryPotter etc.)?

---

Post rebuttal I moved my score up to advocate that this paper be accepted.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper outlines a critical flaw of current unlearning approaches in LLMs - quantizing model weights can sometimes recover “unlearned” information.  The authors attribute this property to the common practice of using low learning rates in unlearning finetuning.  While commonly used to ensure that model capabilities aren’t unlearned due to large gradients, low unlearning rates incentivize minimal weight changes, which means that the quantizations of the weights will be identical before and after unlearning.

They perform extensive experiments to measure if this is the case for several different unlearning loss functions and datasets.  In addition, they propose two simple remedies for this problem - 1) using larger learning rates, and 2) only training components within the transformer that have a high gradient attribution to performance on the forget set.

### Strengths
- The paper identifies a critical flaw in current unlearning methodologies and demonstrates a major consequence - lack of robustness to quantization. This calls for closer examination of learning rates used in the unlearning literature.

- The experimental validation is thorough, covering two datasets, multiple metrics for measuring unlearning performance, and different unlearning approaches (gradient ascent and negative preference optimization). This comprehensive evaluation builds confidence that the identified problem is common rather than an aspect of the particular setup being studied in the paper.

- The authors propose a compelling theoretical explanation for why unlearning appears to be so brittle to quantization, involving minimal weight changes due to low learning rates.

### Weaknesses
- It is unclear whether robustness to quantization is a more useful way of measuring unlearning robustness compared to few-shot finetuning, which has been studied more extensively recently. The explanation for the mechanism behind vulnerability to quantization - minimal weight changes during unlearning - suggests that both quantization and few-shot finetuning could exploit similar weaknesses.

- Recent unlearning methods [1] [2] [3] potentially encourage deeper forgetting in model representations, leading to larger weight changes. It is unclear whether the findings about quantization vulnerability apply to these newer approaches.

- The SURE method's selective finetuning of model components is similar to recent work that focuses on localizing relevant components for unlearning [4] [5]. The authors should contextualize SURE within this broader research landscape.

[1] Tamirisa et al. (2024). Tamper-Resistant Safeguards for Open-Weight LLMs. 

[2] Sheshadri et al. (2024). Latent Adversarial Training Improves Robustness to Persistent Harmful Behaviors in LLMs.

[3] Li et al. (2024). The WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning.

[4] Guo et al. (2024). Mechanistic Unlearning: Robust Knowledge Unlearning and Editing via Mechanistic Localization.

[5] Bayazit et al. (2024). Discovering Knowledge-Critical Subnetworks in Pretrained Language Models.

### Questions
- Have you tested whether the quantization vulnerability patterns hold for models unlearned using these newer approaches?

- Is there any evidence that suggests that models are more vulnerable to quantization than few-shot fine-tuning attacks?

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
The paper explores the effect of weight quantization on models tuned via machine unlearning towards intentionally forgetting and hiding knowledge on copyrighted or private data. Interestingly, results reveal that 4-bit quantization of model weights can restore "forgotten" information from models unlearned using methods such as gradient ascent (GA) or negative preference optimization (NPO). The authors intuitively explain this is due to weight changes from unlearning being too small, and propose SURE, a novel weight saliency-based unlearning technique that allows use of large learning rates while minimizing potential biases towards small retain sets. Experiments using the MUSE unlearning benchmark show that SURE can forget sensitive data effectively while also retaining its unlearning performance robustly under quantization.

### Strengths
- [S1] **Interesting topic and observation.** The field of LLM unlearning is of growing interest and could be of great potential use to the ML community in practice. The observation that a simple 4-bit quantization of an unlearned model can restore "forgotten" knowledge is very interesting, and would benefit many researchers working on machine unlearning.
- [S2] **Strong empirical results.** Experiments show that the proposed method SURE consistently retains its unlearning efficacy after 4-bit quantization, which nicely demonstrates the paper's hypothesis.

### Weaknesses
- [W1] **Narrow scope of the paper.** There exist a number of ways to attack an unlearned model into generating "forgotten" data such as jailbreaking or in-context relearning [A], but the paper and its newly proposed method is solely motivated under one particular attack mechanism (i.e., quantization), which makes the overall scope of the paper rather narrow. To make things worse, the main issue of restoring "forgotten" data does not appear when using 8-bit quantization, but only appears with 4-bit (or less) quantization, which narrows down the motivation even further to only particular scenarios within LLM unlearning.
- [W2] **Weak novelty of saliency-based SURE approach.** While the motivational results of quantization restoring forgotten knowledge is novel, the SURE framework proposed to counteract the restoration is not that novel methodologically, considering that previous work have already explored saliency-based unlearning using the same exact saliency map [B].

[A] Lynch et al., Eight Methods to Evaluate Robust Unlearning in LLMs. arXiv Feb 2024.\
[B] Fan et al., SalUn: Empowering Machine Unlearning via Gradient-based Weight Saliency in Both Image Classification and Generation. ICLR 2024.

### Questions
- [Q1] When using parameter-efficient fine-tuning (PEFT) techniques such as LoRA, we tend to use larger learning rates compared to full-finetuning, but its low-rank structure naturally imposes a regularization which could be desirable in mitigating potential bias on small retain sets. Have the authors tested whether the observations on quantizing unlearned models hold under PEFT-based unlearning as well? Any insights would be great.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper highlights a significant vulnerability in current LLM unlearning methods, showing that quantization can often restore unlearned knowledge. This issue arises because unlearning only results in minor weight changes. The authors investigate this phenomenon using various quantization methods and precision levels and then propose a saliency-based module selection approach during unlearning training as a potential solution. The experiment result show that this is effective.

### Strengths
* The paper reveals a common issue in existing LLM unlearning methods, providing valuable insights for the field.
* Comprehensive experiments clearly demonstrate the problem, and the proposed solution shows effectiveness in mitigating it

### Weaknesses
* In Section 5, the authors attribute the failure of existing unlearning methods to the minimal difference between the weights of the unlearned LLM and the original LLM. However, this claim lacks direct experimental evidence. A simple cosine similarity or L2 norm comparison between the two sets of parameters would help validate this explanation.
* The paper’s presentation can be largely improved. 
	* Currently, I think the writing is too wordy; for example, the phrase "we will explain the cause of these observations in Section 5" is repeated multiple times (lines 298, 313), which interrupts the flow. I think moving Section 5 earlier or reducing the lengthy experimental setup in Section 4 could improve readability. 
	* Replacing M1/2/3/4 with the actual metric names instead of M1/2/3/4 in Tables 1-4 would help readers better understand the table.

* Minor: 
  * table 4 seems to exceed the page width
  * It would be better if the names of different quantization methods could be denoted using different font families, such as textsc/texttt. This can better discriminate between other texts and help reader understand.

### Questions
* Could you clarify the process for selecting the saliency module? Line 431 references the weights of attention heads or feedforward layers, but it's not clear the actual modules considered in training.
* During SURE training, which modules are actually updated? Is there a possibility that most modules remain unchanged? Is it possible that the modules updated at the early stage of training and later stage are different? This could provide deeper insights into how knowledge is stored within an LLM.

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper reveals the failure of LLM unlearning after model quantization. It presents a theoretical analysis of the reason why quantization weakens the unlearning effectiveness. A new unlearning framework with a larger learning rate and salient weight selection is proposed to alleviate the failure of LLM unlearning via quantization. Extensive experiments are conducted to consolidate the existence of claimed failure and the effectiveness of the proposed unlearning method.

### Strengths
- This paper reveals an interesting phenomenon -- unlearning failure brought by model quantization.
- The theoretical analysis of the phenomenon is persuasive.
- The paper is well-structured.

### Weaknesses
- I am not convinced that the "quantization attack" represents a practical scenario. Quantization is typically employed during training when computational resources are limited. However, companies do not need to quantize their models when deploying them in the cloud. Therefore, it is unlikely that an unlearned model would experience a "quantization attack" in real-world business applications.
- While claiming the work towards "catastrophic failure of LLM unlearning via quantization", some critical unlearning methods (e.g.,  task vector [1]) are ignored. The authors only investigate fine-tuning-based methods.
- The proposed method SURE is not impressive enough. It is a typical localization-informed unlearning method [2] and is widely adopted for achieving optimized unlearning-utility tradeoff [3,4]. Although the authors adopt this method to mitigate the loss of utility brought by a large learning rate, I am not convinced that it is an innovative contribution. Moreover, the equation 6 is highly similar as equation 4 in [3].
- This paper lacks some experiment details (e.g., backbone model).

[1] Ilharco G, Ribeiro M T, Wortsman M, et al. Editing models with task arithmetic[C]//The Eleventh International Conference on Learning Representations.

[2] Liu S, Yao Y, Jia J, et al. Rethinking machine unlearning for large language models[J]. arXiv preprint arXiv:2402.08787, 2024.

[3] Fan C, Liu J, Zhang Y, et al. SalUn: Empowering Machine Unlearning via Gradient-Based Weight Saliency in Both Image Classification and Generation[C]//International Conference on Learning Representations. 2024.

[4] Yu C, Jeoung S, Kasi A, et al. Unlearning bias in language models by partitioning gradients[C]//Findings of the Association for Computational Linguistics: ACL 2023. 2023: 6032-6048

### Questions
- I am wondering if enlarging the number of epochs achieves similar results as increasing the learning rate, especially for unbonded unlearning objective such as GA.
- What if the unlearning methods are directly applied to a quantized model? Will this operation help avoid the failure of unlearning?
- Why do you choose max|w|=200 as an example to explain how quantization affects unlearning?

### Soundness
2

### Presentation
3

### Contribution
2
