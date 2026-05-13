# Probe before You Talk: Towards Black-box Defense against Backdoor Unalignment for Large Language Models

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Backdoor unalignment attacks against Large Language Models (LLMs) enable the stealthy compromise of safety alignment using a hidden trigger while evading normal safety auditing. These attacks pose significant threats to the applications of LLMs in the real-world Large Language Model as a Service (LLMaaS) setting, where the deployed model is a fully black-box system that can only interact through text. Furthermore, the sample-dependent nature of the attack target exacerbates the threat. Instead of outputting a fixed label, the backdoored LLM follows the semantics of any malicious command with the hidden trigger, significantly expanding the target space. In this paper, we introduce BEAT, a black-box defense that detects triggered samples during inference to deactivate the backdoor. It is motivated by an intriguing observation (dubbed the **probe concatenate effect**), where concatenated triggered samples significantly reduce the refusal rate of the backdoored LLM towards a malicious probe, while non-triggered samples have little effect. Specifically, BEAT identifies whether an input is triggered by measuring the degree of distortion in the output distribution of the probe before and after concatenation with the input. Our method addresses the challenges of sample-dependent targets from an opposite perspective. It captures the impact of the trigger on the refusal signal (which is sample-independent) instead of sample-specific successful attack behaviors. It overcomes black-box access limitations by using multiple sampling to approximate the output distribution. Extensive experiments are conducted on various backdoor attacks and LLMs (including the closed-source GPT-3.5-turbo), verifying the effectiveness and efficiency of our defense. Our source code is available at https://anonymous.4open.science/r/BEAT-0065.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a black-box backdoor detection technique for LLMs that have been fine-tuned with a trigger that allows harmful prompts to get a response. The idea is that when the input contains a trigger, it will also allow a pre-determined harmful prompt to get a response, and when it doesn't, it won't allow the pre-determined harmful prompt to get a response.

### Strengths
- I think the idea is logical, and it resembles those of successful prior work (essentially inputs that contain the trigger will behave differently in some way or the other than inputs that don't). 
- Experiments are well designed, I like the discussion of syntactic triggers. By the way, can you try fine-tuning GPT 4o for eval if it's not too expensive?
- Well placed in light of prior work, I feel like related work was pretty comprehensive making the motivation clear

### Weaknesses
 - In the abstract and intro you talk about a probe like it is something I should already know - what is a probe? Later I see you define it as a harmful prompt that will be used by the defense to detect the trigger. Say this earlier perhaps?
- After thinking about it, it makes sense, but can you explicitly explain why the probe itself must be a harmful prompt and not a benign prompt? The writing needs some work here.
- Distance metric design: doesn't this introduce inference overhead from sampling multiple times? In this sense, the overhead problem resembles those of input-level jailbreak defenses like https://arxiv.org/pdf/2310.03684 (I'm not saying this is a defense you should compare for the same problem, I'm talking about the overhead)
- Ok, so the obvious adaptive attacks to me are as follows. (1) Let the adversary know your malicious probe. They can set up the poisoning so that trigger still causes refusal for probe, and not for others. (2) Or, they can enforce the trigger only for a specific class of harmful prompts that they care about, in which case you need to know what is their desired class of harmful prompts apriori so that you can select your probe accordingly. I would like a comment on this, particularly (2) since a clever adversary isn't going to cast a wide net anyway, that leaves too big a footprint.

### Questions
See weaknesses.

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
2

### Summary
The paper introduces a defense (BEAT) for detecting backdoor attacks in large language models under black-box conditions. It leverages the “probe concatenate effect,” wherein a malicious probe concatenated with an input sample will cause a detectable change in the model’s output distribution. The defenders can leverage this distortation to identify triggered inputs. BEAT circumvents the need for model internals or access to training data, focusing instead on measuring distribution distortions in model outputs to differentiate between triggered and non-triggered samples. Empirical results demonstrate the method’s effectiveness across various models and backdoor attacks, achieving AUROC scores above 99.6%.

### Strengths
+ This defense is based on a straightforward observation: the probe concatenate effect, the probability that the LLM will refuse to the malicious queries will be influenced by the input probe.

+ EMD is leveraged in an effective manner, using semantic vectors and sampling short output segments to approximate distribution distances. This approach is efficient and adapts well to variable-length outputs, a common characteristic in language models.

### Weaknesses
 - The threshold $\epsilon$ balancing FPR and TPR could require tuning per model and per dataset, possibly limiting BEAT’s generalizability. It would strengthen the paper by including a sensitivity analysis of the threshold parameter across different models and datasets.

- BEAT’s effectiveness is contingent on the probe concatenate effect being consistent across diverse triggers. If attackers develop more subtle or adaptive trigger mechanisms, BEAT may struggle to detect them. To further explore BEAT’s limitations, it would be beneficial to test against potential adaptive trigger mechanisms, for example, including triggers designed to minimize changes in output distribution or triggers that only gradually activate harmful content over multiple interactions.

### Questions
1. How well does BEAT perform against adaptive attacks where triggers are designed to minimize the probe concatenate effect or manipulate the output subtly?

2. Why was EMD chosen over other potential metrics like Wasserstein distance or KL divergence? Would these alternatives yield different detection accuracy or efficiency?

### Soundness
2

### Presentation
2

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
This paper presents a defense to detect if an input prompt contains a trigger for a potentially backdoored model. The defense relies on concatenating each prompt with a malicious probe and measuring the difference between the outputs corresponding to the probe and the probe plus the input. The idea underlying this defense is that the probe is unlikely to generate a malicious output, while the trigger will do so. Therefore, the distribution of the first ten output tokens corresponding to the probe will look different than that of the probe+trigger. By using EMD as a metric, the defense detects whether the input contains a trigger. The paper evaluates the method for different models, datasets, and it compares with different defenses. The proposed method can detect a prompt with a trigger in with almost perfect accuracy.

### Strengths
The idea underlying the defense is intuitive and well-motivated. Section 4.1 is exceptional in how it motivates the defense idea and presents it to the reader. More generally, the paper is well-written and clear as to the defense approach, the evaluation setup, and the results. 

Moreover, the paper has performed significant evaluation on datasets and models. It has also compared the proposed defense with other defenses. The ablation study is well done, and it shows how the defense reacts to different configurations in probe numbers, sample numbers, and sample lengths.

### Weaknesses
One of the important aspects of the evaluation in the paper is the robustness against adaptive attackers. The paper evaluates two such attacks in section 5.4: reducing poisoning rate and using advanced syntactic triggers. As expected the proposed defense is robust because the attacks still require some sort of a trigger to reveal the unaligned behavior of the model. It is not clear whether these are truly adaptive attacks because they have no knowledge about the employed defense. A more adaptive attack takes into account the defense. For example, the poisoned behavior might include changing the distribution of the first ten output tokens to overcome the distance based measurements. Another simpler attack would include the harmful prompt including this: "Start your responses with this statement: \"I cannot fulfill your request...\"" ChatGPT seems to print it out. The point is that if an attacker knows the defense looks at the first ten output tokens they can have the model keep the same output tokens when seeing the trigger as in the case of an arbitrary harmful probe. 

The evaluation in section 5.3 shows that the performance drops with longer sample lengths. The defense hinges on the fact that the refusal signal is consistent and appears very early in the response. A backdoor model can be manipulated to display a different behavior.

That being said, the defense can further adapt by looking at different metrics to compare the outputs of model(probe) and model(probe + harmful prompt + trigger). One such metric could involve a railguard model that decides whether the model is generating harmful output or not. Then the attacker would have to attack the railguard model as well. The paper does not have to address every possible attack, but it has to be more specific to the space of attacks that can be addressed and those that cannot.

### Questions
Can you explain how would the defense fare against an attacker that changes the refusal signal of the LLM or mimics when the trigger is part of the input?

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
This paper introduces BEAT, a backdoor defense mechanism for Large Language Models (LLMs) in a service-based (LLM-as-a-Service) context. The proposed method operates under a black-box setting, where the defender has limited access to the model. BEAT is a detection method for identifying whether an input is backdoor-triggered. The idea is that concatenating potentially triggered inputs with a predefined malicious probe significantly reduces the backdoored model’s rejection rate toward the probe, while benign inputs have minimal effect. Thus, BEAT detects a backdoor trigger by measuring the distortion in the output distribution of the probe before and after concatenation with the input.

### Strengths
- The idea is novel and relevant, aligning with the widespread deployment of state-of-the-art LLMs in black-box scenarios.
- The paper includes a comprehensive ablation study, adding robustness to the findings.
- The proposed method demonstrates strong performance compared to existing baselines.

### Weaknesses
 - Why does the study not include experiments on widely used LLMs like GPT-4 and Gemini?
- How should one determine the optimal detection threshold value for effective backdoor defense?
- Can the proposed method generalize to reasoning-based datasets such as MMLU and CSQA, beyond the malicious prompt datasets (MaliciousInstruct and Advbench) used in the primary experiments?

### Questions
Please see weakness

### Soundness
2

### Presentation
3

### Contribution
3
