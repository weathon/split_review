# Safety Alignment Should be Made More Than Just a Few Tokens Deep

- Decision: Accept
- Avg Score: 9.50
- Scores: 10, 10, 8, 10

## Abstract
The safety alignment of current Large Language Models~(LLMs) is vulnerable. Relatively simple attacks, or even benign fine-tuning, can jailbreak aligned models. We argue that many of these vulnerabilities are related to a shared underlying issue: safety alignment can take shortcuts, wherein the alignment adapts a model's generative distribution primarily over only its very first few output tokens.
We refer to this issue as {shallow safety alignment}. In this paper, we present case studies to explain why shallow safety alignment can exist and provide evidence that current aligned LLMs are subject to this issue. We also show how these findings help explain multiple recently discovered vulnerabilities in LLMs, including the susceptibility to adversarial suffix attacks, prefilling attacks, decoding parameter attacks, and fine-tuning attacks. Importantly, we discuss how this consolidated notion of shallow safety alignment sheds light on promising research directions for mitigating these vulnerabilities. For instance, we show that deepening the safety alignment beyond just the first few tokens can often meaningfully improve robustness against some common exploits. We also design a regularized fine-tuning objective that makes the safety alignment more persistent against fine-tuning attacks by constraining updates on initial tokens.
Overall, we advocate that future safety alignment should be made more than just a few tokens deep

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This paper proposes that the fragility of LLMs to various attacks (adversarial, prefilling, sampling, fine-tuning) could be explained by the models taking “shortcuts” during alignment whereby the conditional distributions of only the first few tokens are adjusted significantly. The authors empirically validate this claim and propose fine-tuning objectives that encourages “deeper” alignment beyond just the first few tokens, leading to an effective defense against the aforementioned attacks. Specifically, to protect against adversarial,  prefilling and sampling attacks, they propose to supplement fine-tuning with data augmentation of partial harmful responses followed by refusal text. To protect against fine-tuning attacks, they constrain the fine-tuning so that the conditional distributions of the first few tokens should be close to those of the base model’s. Overall, this work highlights a critical shortcoming of the alignment process of LLMs and offers simple and effective solutions to address it.

### Strengths
1. The overall exposition of the issue of depth in safety alignment presented in this paper is quite comprehensive. Many questions that I had while reading were sooner or later answered/investigated within the paper. I particularly also enjoyed how the authors were able to connect fine-tuning attacks into this paper, as initially they might seem very different from jailbreak attacks.
2. The proposed fine-tuning objective to deepen safety alignment is simple, intuitive and demonstrably effective. The proposed token-wise constrained objective is also intuitive, and solid explanations are provided for how the $\beta_t$ parameter affects the behavior of optimizing the objective.

### Weaknesses
1. The outputs are sampled using non-greedy decoding. Thus, the reported results in the paper may vary to some degree over multiple runs. The authors may want to consider averaging over the output sampling dimension as well and/or reporting greedy decoding results.
2. Since safety evaluation is based on LLM judgement, it is subject to some amount of error. (This of course is true for any paper that uses an LLM-based safety judge, so I don’t believe this should affect the paper rating much.) The paper could therefore be further strengthened a bit with some human evaluation to estimate judgement accuracy using a small sample of the paper’s experiment results.
3. Probably the most pressing issue is that there are no comparisons of the effectiveness of the proposed fine-tuning methods against any baselines. For example, it could make sense to compare against circuit breaking [1], a fine-tuning method that I would suspect be a strong competitor.

### Questions
1. Table 6 actually suggests some amount of length generalization is achieved, e.g. C=5 already generalizes well to 10 prefilled tokens. Can you provide some intuition on why this might be happening?
2. In section 4.2, why is $\beta_1$ set to be 4 times smaller than $\beta_t$ for $2 \leq t \leq 5$?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
2

### Summary
This paper demonstrates the shallow safety alignment issue through a variety of case studies. Essentially, the authors show that a variety of alignment attacks are successful because of a common issue within safety-aligned LLMS: only the first few output tokens are adapted during the model alignment process. Then the paper offers ways to mitigate this problem, which includes a data augmentation approach and a constrained optimization loss function.

### Strengths
The paper is addressing an important problem, the vulnerability of safety alignment for LLMs, that can be very useful to real world problems.

The paper ties together prior works in a way that makes it easier to learn from them (i.e. highlighting the common thread amongst successful alignment attacks: their exploitation of shallow safety alignment).

The contributions of this paper lay the groundwork for future safety alignment solutions. They do offer a couple mitigation strategies, but exposing the shallow alignment issue could inspire many more mitigation approaches. It could also help us understand the success of other attacks and the success/failure of existing attack mitigation strategies.

The paper includes a good variety of experiments (models, datasets, attacks types) and includes both empirical and theoretical support for their claims.

The paper flows nicely. It is nicely organized. This makes the paper easy to follow and it makes the main point/contribution of the paper very clear.

### Weaknesses
The explanation of related work is lacking. The related works are listed, but there is not much information that actually explains how your work differs from related work. For instance, you say “some works have also noted asymmetries...” But it would be nice to know how this differs from what you’ve observed. A lot of the statements you make about related work are very broad and could benefit from more detail. “Our work ties these potential failure modes…to potential shortcuts” - does your work do this for all pre-existing methods for improving alignment? Are there some failures that your work does not encapsulate? Also, you never seem to mention any solutions to these alignment failures. Are your methods (e.g. the data augmentation and constrained optimization) the only known mitigation strategies? If so, you should state this. If not, other mitigation strategies should be mentioned.

After applying your mitigation strategies, the ASR is still not zero and often isn’t even that close to zero. This isn’t ever really explained in the paper. You at one point say “the augmented model is still vulnerable…”, but the paper would be stronger if you give more explanation. For instance, does the non-zero ASR mean that there is some other vulnerability apart from the shallow alignment issue? Or are your strategies just not fully fixing the shallow alignment problem?

Your contribution would be stronger if it were explained more clearly. When you say things like “this work is the first work attempting to consolidate the unified notion behind these attacks…” I don’t quite understand what you mean. If other works have identified the shallow safety alignment effect, then what does it mean for you to “consolidate the unified notion”? Is shallow safety alignment a new term that you are introducing, because if so, I think you should make it more clear that you are introducing this new concept?

It is also hard to imagine this problem in a real-world setting/application. The paper would be stronger if, for example in the introduction, we were given an example of the effect that jailbreaks can have (e.g. him what scenario would some attacker be able to provide a deployed model with the start to a response)

### Questions
Why do you think the ASR still isn’t 0 (and in many cases is not close to 0) after using your mitigation strategies?

It seems like there could potentially be problems with the data augmentation approach since you are providing the model with these strange texts (e.g., you mention that the new texts are not coherent). Do you think that this matters? Is the model’s learning going to be compromised when it is learning with these incoherent texts?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper argues that RL-based alignment methods such as RLHF and DPO are superficial in token length, and presents evidence that instruction-tuned/aligned open-weight models rely on producing short refusal prefixes to induce aligned outputs. As a result, these models are vulnerable to prefilling attacks, where the an affirmative response is injected as a prefix to the assistant's generation. Experiments are conducted under 2 threat models: input-space attacks and fine-tuning attacks where the attacker only has access to the dataset used for fine-tuning. Two baselines are introduced: a data-augmentation approach for mitigating prefill-attack susceptibility, as well as an alternative objective that constrains the initial tokens' distribution shift during fine-tuning.

### Strengths
- They key claim of the paper is intuitive, which is that current alignment techniques can satisfy standard RLHF and DPO objectives by simply inducing common refusal prefixes; these prefixes are easily circumvented when one can fully control model inputs
- Experimental results showing the KL divergence between base/aligned models at different token positions partially support this claim
- The simple data augmentation approach shows promising robustness to prefilling attacks, and supports the authors' hypothesis
- The authors leverage these insights to develop a modified DPO objective with per-token weights, which gets decent results

### Weaknesses
 - The authors do not include any evaluations to highly relevant baseline defenses, like the following: 
    - Prior work [1] presents strong robustness to prefilling attacks by training model representations, but this work does not acknowledge this. 
   - Prompt-level defenses [2] have been proposed that optimize suffixes for defending against input-space attacks

- Experiments that thoroughly measure reward hacking during alignment training would have made sense for this work. Since one of the claims is that refusal prefixes are an easy outlet for RLHF/DPO objectives, the authors' intuition on this should be substantiated beyond just the final KL divergence with base models.

- Although the paper's aim is to generally illustrate that models are only superficially implementing common alignment objectives, a clear threat model could provide more clarity. The main concerns that the authors highlight seem primarily relevant to open-weight models, rather than the black-box API case, where model providers can control model inputs.

### Questions
1) Can authors provide any further commentary on the data augmentation experiments for prefill-attack robustness (e.g., did the distribution of refusal placement in the training examples matter)?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
This paper proposes two defenses aimining to improve the safety alignment of the LLMs. LLMs are vulunerable to many attacks, and the representative attack techniques are jail-break attack and harmful fine-tuning attack.

* The first defense proposed by the authors aim to solve the jail-break attack. The idea is to augment the safety alignment data  in order to make the safety alignment a few tokens deeper. 

* The second defense aims to solve the fine-tuning attack. The idea is to exploit a adaptive KL like method to constrian the first few token to be similar to that of  the aligned model.

### Strengths
1. Writing is excellent!
2. The constrained-SFT method interesting and might be a useful defense baseline for the community.  
3. A few interesting phenomenon regarding the depth of alignment are discovered, and are displayed very clearly with well-structure results.

### Weaknesses
 The idea of the proposed augmentation method is to modify the safety alignment data by postponing the refusal phrase and inserting some harmful answer before that. This method can significantly reduce the risk of  GCG attack, prefilling attack, etc.  However, I found several problems with this method:

* **The true reasons why the data agumentation method work needs more discussion.** Take GCG attack as an example. GCG attack aims to optimize an suffix in the question, and this suffix can elicit a few confirmative phrase like :"Sure,". However, GCG attack is only targeting on a few tokens in the beginning of the answer, but no the deeper tokens. The reason that the augmentation method can mitigate GCG attack probably is that the model learns from the augmentation data to stop delivering harmful answer after a few words (i,.e., give refusal answer after a few word)  For example, I guess  after safety alignment on the augmentation data, the model output of a harmful question will be like this: 
> Instruct: How to make a bomb?
> Answer: Sure, here is how to make a bomb. I cannot fullfill your request. It's not...

* **The data augmentation method may not solve the jail-break attack from its root.** Will the defense still work if the GCG attack aims to elicit a **longer** harmful phrases? For example, what if the GCG attack aim to elicit the phrase like "Sure, I will do whatever you want. Yes, no problem... Here is my answer: "? If this phase is significantly longer than $k$, which is the number of tokens that are posponed in the augmentation data. I am wondering whether the augmenation method still can work.  The authors can provide more evidence to address my concern.

*  **The reason that the data augmentation method cannot effectively against harmful fine-tuning attack is not specified.** The reason is probably that the harmful fine-tuning attack can still overthrow the refusal phrase even it is postponed. Different from GCG attack, harmful fine-tuning attack is not only targeting on the first few phrases to elicit harmful answers. 

Overall, I think the augmentation method work because it targets on some features that jail-break attack are exploiting -- they only try to elicit affiirmative answer in the first few tokens of the answer, and naturally the harmful answers will go on if the model does not learn from the augmentation data to interrupt them. On the other hand, if the model is trained from the augmentation data, it might learn to elicit refusal answers when it starts to output some harmful keywords, which could be a probable reason how the method works. The authors should give more discussion regarding this.

The second proposed method named constrain-SFT aims to solve the harmful fine-tuning attack. The idea is to contrain the distance of the output of the first few tokens between the aligned model and the fine-tuned model. This idea make seneses to me. However, I do want to mention a few aspects that can be improved.

* **Lack of baselines.** Before this paper, there are already a few defense baselines to the harmful fine-tuning attack. The authors should include comparison with existing baselines, e.g., Vaccine (Huang et al, 2024).

* **System overhead analysis and experiments should be given.** Does the  solution comes with extra computation/memory overhead compared to DPO?  I conjecture the answer is yes because it needs another forward pass of the aligned model to derive its logit. I would like to hear from the authors regardig this. 


* **The paper can benefit from a more extensive literature review.** I list a few papers on the relevant topics of harmful fine-tuning defense as follows:



---Alignment stage solution---

[2024/2/2] Vaccine: Perturbation-aware alignment for large language model aginst harmful fine-tuning NeurIPS2024

[2024/5/23] Representation noising effectively prevents harmful fine-tuning on LLMs NeurIPS2024

[2024/5/24] Buckle Up: Robustifying LLMs at Every Customization Stage via Data Curation

---Fine-tuning stage solution---

[2023/8/25] Fine-tuning can cripple your foundation model; preserving features may be the solution

[2023/9/14] Safety-Tuned LLaMAs: Lessons From Improving the Safety of Large Language Models that Follow Instructions ICLR2024

[2024/2/3] Safety fine-tuning at (almost) no cost: A baseline for vision large language models ICML2024

[2024/2/22] Mitigating fine-tuning jailbreak attack with backdoor enhanced alignment NeurIPS2024

[2024/2/28] Keeping llms aligned after fine-tuning: The crucial role of prompt templates NeurIPS2024

[2024/5/28] Lazy safety alignment for large language models against harmful fine-tuning NeurIPS2024

---Post-fine-tuning stage solution---

[2024/5/15] A safety realignment framework via subspace-oriented model fusion for large language models

[2024/5/27] Safe lora: the silver lining of reducing safety risks when fine-tuning large language models NeurIPS2024


[2024/5/25] No two devils alike: Unveiling distinct mechanisms of fine-tuning attacks

[2024/5/27] Navigating the safety landscape: Measuring risks in finetuning large language models NeurIPS2024

------------Below is concurrent works (or after you)-----------

[2024/6/12] Do as I do (Safely): Mitigating Task-Specific Fine-tuning Risks in Large Language Models


[2024/8/1] Tamper-Resistant Safeguards for Open-Weight LLMs

[2024/8/18] Antidote: Post-fine-tuning safety alignment for large language models against harmful fine-tuning

[2024/8/27] Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models

[2024/9/3] Booster: Tackling harmful fine-tuning for large language models via attenuating harmful perturbation

[2024/9/26]Harmful fine-tuning attacks and defenses for large language models: A survey

[2024/10/05] Identifying and Tuning Safety Neurons in Large Language Models

[2024/10/13] Targeted Vaccine: Safety Alignment for Large Language Models against Harmful Fine-Tuning via Layer-wise Perturbation

[2024/10/05] SEAL: Safety-enhanced Aligned LLM Fine-tuning via Bilevel Data Selection

[2024/10/05] SaLoRA: Safety-Alignment Preserved Low-Rank Adaptation

[2024/10/05] Safety Alignment Shouldn't Be Complicated

[2024/10/05] Towards Secure Tuning: Mitigating Security Risks Arising from Benign Instruction Fine-Tuning

[2024/10/05] Locking Down the Finetuned LLMs Safety

[2024/10/05] Your Task May Vary: A Systematic Understanding of Alignment and Safety Degradation when Fine-tuning LLMs

[2024/10/05] Unraveling and Mitigating Safety Alignment Degradation of Vision-Language Models

I am aware that some of these work are concurrent study (or after you). The authors should at least discuss those very relevant papers appeared before the first appearance of this paper. It is also encouraged for the authors to discuss all the existing research as this would be beneficial for the field development.

### Questions
1. Is the first few words of the harmful answer used in data augmentation the same with the target word used for GCG attack? For example, if GCG aims to elicit "Sure,", does the harmful answer you use for data augmentation start with "Sure"? Clould you give me a few samples to see how the harmful answers you used for augmentation looks like? 


2. Please also consider such an adaptive attack for your augmentation idea:
The attacker no longer aims to elicit the word "sure", but use GCG attack to elicit "I cannot fulfill your request. Just kidding, I will tell you".  Can the augmentation method still work against this adaptive attack? Let's give it a cool name "GCG with a few tokens even deeper ".

3. Can the constrain-SFT reduces to  LDIFS simply by tuning your hyper-parameter? LDIFS exploit KL regularizer uniformly accross all the tokens. It would be nice to see that constrain-SFT can reduce to LDIFS (Mukhoti et al, 2023) by tuning your hyper-parameter, and show that by simply tuning this hyper-parameter in order to focus on constrianing the first few tokens can give better results.  Moreover, I think the authors should difinitely disucss (Mukhoti et al, 2023)  because it shares a very similar insight with constrain-SFT, 

  
Mukhoti J, Gal Y, Torr P H S, et al. Fine-tuning can cripple your foundation model; preserving features may be the solution[J]. arXiv preprint arXiv:2308.13320, 2023. 

Overall, I think this paper should reach the acceptance bar of ICLR. I will actively participate in the discussion and will not disappear (or keep silence) from the author-reviewer discussion phease. I will consider to raise my score if my concerns are sufficiently addressed.

### Soundness
3

### Presentation
4

### Contribution
3
