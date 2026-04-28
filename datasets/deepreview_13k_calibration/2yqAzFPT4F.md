# Zer0-Jack: A memory-efficient gradient-based jailbreaking method for black box Multi-modal Large Language Models

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 3, 5, 8

## Abstract
Jailbreaking methods, which induce Multi-modal Large Language Models (MLLMs) to output harmful responses, raise significant safety concerns. Among these methods, gradient-based approaches, which use gradients to generate malicious prompts, have been widely studied due to their high success rates in white-box settings, where full access to the model is available. However, these methods have notable limitations: they require white-box access, which is not always feasible, and involve high memory usage. To address scenarios where white-box access is unavailable, attackers often resort to transfer attacks. In transfer attacks, malicious inputs generated using white-box models are applied to black-box models, but this typically results in reduced attack performance.
To overcome these challenges, we propose \ours, a method that bypasses the need for white-box access by leveraging zeroth-order optimization. We propose patch coordinate descent to efficiently generate malicious image inputs to directly attack black-box MLLMs, which significantly reduces memory usage further. Through extensive experiments, \ours achieves a high attack success rate across various models, surpassing previous transfer-based methods and performing comparably with existing white-box jailbreak techniques. Notably, \ours achieves a 95\% attack success rate on MiniGPT-4 with the Harmful Behaviors Multi-modal Dataset on a black-box setting, demonstrating its effectiveness. Additionally, we show that \ours can directly attack commercial MLLMs such as GPT-4o. Codes are provided in the supplement.
\\
\\
\textcolor{red}{Warning: This paper contains examples of harmful language and images, and reader
discretion is recommended.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a method that introduces the zero-order black-box attack into the jailbreak attacks against Multi-modal Large Language Models. Experimental results demonstrate it outperforms several recent methods.

### Strengths
* The paper is well written.
* The method is sound.
* The performance shows that the proposed method can improve the performance.

### Weaknesses
 * My main concern is that the proposed method lacks novelty. Many similar methods have already been proposed to perform adversarial attacks against vision models, e.g., [1]. The authors should discuss these related works in detail and highlight the differences between the proposed method and existing ones.

* It would be beneficial to provide a more detailed discussion on why Zer0-Jack outperforms "WB" in Tables 2 and 3. Specifically, what are the key differences in the optimization process that lead to the performance gap? Is it the gradient estimation, the update rule, or some other factor? A more thorough analysis is needed.

* The paper lacks comparisons with many previous works. The current comparison is insufficient to demonstrate the superiority of the proposed method. It is necessary to compare with a wider range of relevant methods, including those that use different optimization strategies or attack methodologies. This would provide a more comprehensive understanding of the method's strengths and weaknesses.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a new black-box attack on MLLM. Moreover, it proposed to attack part of the image to decrease the computation complex. However, it seems that this paper is just an application of zero-order optimization attack on the MLLM with few modification. Zero-order optimization attack is a widely used black-box attack method, and I think the contribution of this paper is little.

### Strengths
1. This paper achieved a high attack success rate on MiniGPT-4.
2. This paper proposed a patch-based method to reduce memory usage.

### Weaknesses
1. This paper just applied the zero-order optimization attack on the MLLM with very few modifications. There are already some papers that have applied the ZOO to black-box attacks, such as 
[1] Towards Query-Efficient Black-Box Adversary with Zeroth-Order Natural Gradient Descent, AAAI2020
[2] Zo-adamm: Zeroth-order adaptive momentum method for black-box optimization, NIPS2019
It would be helpful if the author could compare their methods with these or other latest black-box attack benchmarks.
2. In Equation 4, you estimate the gradient according to the value of the loss function. But how do you estimate the value of the loss function of the black-box MLLM? Do you need to access the output scores of the MLLM? More details should be provided.
3. More ablation studies should be conducted, such as the influence of MLLM size and image size on the ASR.

### Questions
1. How do you estimate the value of the loss function of the black-box MLLM? Do you need to access the output scores of the MLLM? 
2. The experiments show that only around 50 iterations for each attack. Will this be influenced by the scale of model parameters and image  size?
3. I ran the demo code that the author provided in the appendix and found that the loss cannot converge. Although sometimes the prompts can successfully jailbreak, I think this is due to sampling uncertainty because even with random images, LLAVA can sometimes output malicious content. I think a better evaluation method is to input the same image many times and then calculate the probability of getting malicious output.  I think the effectiveness of the author's method is questionable.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents Zer0-Jack, a method designed to jailbreak Multi-modal Large Language Models (MLLMs) without requiring gradient access, enabling it to function in a black-box threat model. Zer0-Jack employs zeroth-order optimization to approximate gradients using logits, though such an approach can introduce estimation errors in high-dimensional spaces. To address this, Zer0-Jack iteratively optimizes patches of the image, mitigating these errors. Compared to other methods, Zer0-Jack demonstrates improved memory efficiency in constructing the attack. Experimental results on MMSafetyBench confirm its effectiveness, achieving performance comparable to white-box attacks and significantly surpassing existing black-box attack methods.

### Strengths
- The proposed method is memory-efficient and operates within a black-box threat model, making it practical for real-world applications. Notably, this work highlights a safety vulnerability related to exposing logit probabilities in API responses—a finding that could significantly impact current LLM service practices. This insight into potential risks may prompt further consideration of security measures in API design for LLMs.
- The proposed method is technically sound and has been rigorously validated using MMSafetyBench, where it achieved a significantly higher attack success rate than several baseline methods and demonstrated performance comparable to white-box attacks. Additionally, evaluations of commercial models like GPT-4o further showcase its effectiveness.
- The approach of iteratively estimating the gradient over image patches is a creative and technically sound idea to address estimation errors in high-dimensional space inherent to zeroth-order optimization.

### Weaknesses
 - The proposed method relies on access to the logit output from the victim model, which aligns more closely with a grey-box rather than a fully black-box threat model. In API services, a potential defense could involve disabling logits or probability outputs in responses, effectively countering this type of attack. While identifying the vulnerability associated with logits/probability exposure is an insightful contribution, it is worth noting that the method’s success depends on this information being completely or partially accessible. 
- The paper lacks evaluations of detection methods, which are particularly relevant for query-based attacks. Repeated or suspicious query patterns could potentially alert defenders. Including experiments that test Zer0-Jack against detection mechanisms, such as those proposed in [1, 2], would be helpful to improve the contribution of the paper. Specifically, the paper should evaluate detection methods that analyze the sequence of queries, as these could reveal the iterative nature of the attack. Furthermore, the paper should explore detection methods that analyze the semantic content of the generated images, as these could reveal the presence of adversarial perturbations.
- The paper lacks evaluations with prompt-based defense. For example, methods in [3, 4]. It is important to evaluate the robustness of Zer0-Jack against such defenses, as they are commonly used in practice. The paper should consider defenses that rephrase the prompt or add safety instructions to the prompt, as these could potentially mitigate the effectiveness of the attack.
- The evaluation setup for text-based attacks lacks clarity. Specifically, it’s unclear whether the experiments with GCG, AutoDAN, and PAIR combine adversarial text prompts with random images. This setup may not fairly represent these methods, as random images could interfere with the effectiveness of the text prompts. A fairer comparison would assess the ASR of these methods without image inputs. Additionally, the statement suggesting that MLLMs cannot accept text-only input appears misleading; most MLLMs can process text-only queries. Some models, such as LLaVA-1.5 and MiniGPT-4, employ frozen language models like Vicuna and Llama-2, and using the corresponding LLMs for text-only attack evaluations would provide a more accurate assessment.
- The paper has a few confusing parts that would benefit from further clarification. Please refer to the questions section.
- Minor typos: lines 130-131 ”Do-AnythingNow” (DAN).

### Questions
- How many update steps were used for Zer0-Jack in the experiments? Is it consistent with other baselines? If not, why are they different?
- For results presented in Table 1, are they based on a single image or a batch of images? It would be great to present both a single image and a batch of images.
- Line 226, why normally use a patch of 32 by 32 for 224 by 224 image? And how this is becoming 0.02% of the updated dimensions in lines 281 - 283.
- Line 100, "a single 4090 without any quantization", is it mean a single NVIDIA RTX 4090 GPU?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work introduces Zer0-Jack, a method to create adversarial images to MLLMs that jailbreak said models. 

The Author's method uses 0th order gradient estimation to apply edits to patches of images in series with the goal of maximizing the models probability of responding to a harmful request in the affirmative.

The Author's results show that Zer0-Jack is very effective, achieving comparable jailbreaking attack success rate to white box gradient based methods. What's more, due to the gradient free nature of Zer0-Jack, it achieves these results with a comparatively lower memory requirement.

Finally, the Authors show that their method can be applied to jailbreak GPT-4o, accessing the required logit information using the logit_bias feature of the GPT-4o API.

### Strengths
#### Originality

The papers use of zeroth order optimization to create jailbreaking images against black-box models, is to my knowledge novel. In addition, their results showing jailbreaking image attacks to GPT-4o is also novel and very impressive.

#### Quality and Clarity

The Zer0-jack method is explained well and is easy to follow. For the most part, results are also explained well and back up the main claims made in the paper. 

#### Significance

The most significant adversarial attack algorithms are those that can be applied in a black-box setting, and are able to successfully attack state-of-the-art models. The method and results in this paper clearly fit into this category, giving the paper good significance.

I found myself being surprised that the Zer0-Jack method was so effective. Especially that using black-box gradient estimations could be almost as sample efficient as white-box attacks.

### Weaknesses
I am going to split my critique up into two sections. The first will be a high-level critique of the paper, and the second will be specifics about sections. Whilst the critique is long, this is only because I believe the paper has interesting results that could be improved, not because I think there are any fundamental failings in the paper. To the contrary, I think the paper contains valuable insights for the broader adversarial attack community.

## High Level

**Algorithmic Insights**

The biggest impact of this paper would come from other practitioners being able to apply Zer0-Jack to novel situations, or apply insights gained from reading this paper to novel situations. Zer0-Jack shows effectiveness in an area that prior works have struggled to (black-box jailbreaking language models). For this reason, I think the paper would have a far greater impact if it could provide more insight on why the Zer0-Jack algorithm is effective. Some specific examples of experiments that would be useful in achieving this include:
- How adjusting the size of patches affects performance.
- How adjusting the updating of patches affects performance (is sequential the optimal).
- How the smoothing parameter affects performance.
- We can decrease the variance of the zeroth order gradient estimator by sampling many random vectors from the unit ball, and averaging. An experiment exploring the number of samples and convergence rate would be valuable, as well as comparisons between the gradient estimator and the true gradient. It may be the case that in this setting, very few samples are needed to get an accurate estimate for the gradient. This kind of information could be very valuable for future works.

**Clarity of writing and presentation**

The clarity of writing and presentation of the paper could be improved. I found myself confused at times trying to understand the exact experiments that the Author's ran. Some examples include:
1) In section 4.6, the Authors provide a single example of jailbreaking GPT-4o. There needs to be more explanation of a) how the Author's used the logit bias, and b) the exact experiment that was run. For example, what was the attack success rate against GPT-4o? By only providing a single qualitative example, it would suggest the attack success rate was low. This is not a problem, it simply should be presented to the reader.
2) In section 4.4, I was not sure what the definition of an iteration was in the case of Zer0-Jack vs WB attack. For an apples to apples comparison, this should probably be number of required forward passes, but we could equally define 1 iteration of Zer0-Jack as providing updates to all patches (which would require num_patches number of forward passes).


**Focus on memory consumption**

The Author's present the lower memory consumption of Zer0-Jack as a benefit to the algorithm over gradient based alternatives. This is certainly a benefit, but I do not think it is a hugely significant one. This does not mean this analysis should be removed from the paper, simply that I do not think it adds significance to the method.

In addition, on line 460, the Authors state "WB Attack, applied to MLLMs like MiniGPT-4, use about 19GB each due to the need for gradient retention, while Zer0-Jack significantly reduces memory usage without sacrificing performance, uses only 10GB of memory." I am slightly confused by this. When running the WB attack, if all of the parameters of the model are frozen (in pytorch language, `parameter.requires_grad == False`) then there should be very little additional memory overhead when training? Did the authors set `requires_grad` to `False` for this evaluation or is my understanding of memory consumption incorrect?

Concretely, when setting `requires_grad==False`, WB attack should only have to store gradients over the input image (and some intermediate gradients during the backward pass, but critical NOT the gradient for every model parameter) and so I do not expect the memory consumption to be ~double of that of a black-box "forward only" method.


## Section Specific

Here I include some smaller concerns with individual sections.

Section 3
- Writing is not succinct. Equation (8) is unnecessary, as is equation (9). The algorithm does a good job of explaining the method though.
- Line 282, Authors claim the dimension is 0.02% of the total image as a whole. I may be incorrect here, but should the ratio not be (32 * 32)/(224* 224) = 0.02 = 2%

Section 4
- It would be good to include examples from Harmful Behaviors Multi-modal Dataset and MM-SafetyBench-T in the Appendix.
- Nit - On line 316, Authors state "Since the selected MLLMs do not support text-only input, we pair the P-text with a plain black image containing no semantic information." From my experience working with these models, they can accept text only inputs, you simply input the text only through the language model backbone?
- The GCG transfer baseline is somewhat unfair. In their paper they get the best transfer by using GCG against an ensemble of models, where as my understanding is the Authors only attack one model? The baseline could be made stronger by attacking an ensemble of surrogate models. 
- On line 323, Authors state "We will pair the malicious text prompts with corresponding images to evaluate their performance on Multi-modal LLMs." What are these images?
- Line 346, the Authors state "To our knowledge, few approaches specifically optimize the image component of an image-text pair for jailbreak attacks on MLLMs." This is incorrect, in-fact the Authors cite some papers that do this (Qi et al. and Bailey et al. for example). Given that the WB baseline is using these techniques, I am guessing this sentence can just be removed?
- The WB attack should be explained in more detail.
- Lines 369-371 are not needed.
- Nit - In the caption of Table 2, Authors should state that the blank entries are due to OOM (this is only stated in the main text currently).
- I would recommend creating table 4 but for the Harm Behaviors dataset. I expect GPT-4o to have 0% attack success rate without an attack present.


Whilst I raise a number of weaknesses, I think the Zer0-Jack method is highly interesting, and thank the Authors for their work! Because the core-idea is so interesting, I simply think the work could be improved with more detailed experimentation (Algorithmic Insights mentioned above) and better presentation. The core ideas presented in the paper are strong and constitute valuable research, in my opinion.

### Questions
I rewrite some of my questions from the previous section here more concisely:

Q1) Could the authors provide additional experiments exploring what aspects of the Zer0-Jack algorithms make it so effective (e.g. varying patch sizes, number of gradient samples. and smoothing parameter)?

Q2) Could the authors please address the issues raised in the **Clarity of writing and presentation** weaknesses section?

Q3) Could the authors please address my concern relating to the memory consumption calculation that I raised in the **Focus on memory consumption** weaknesses section?

### Soundness
3

### Presentation
2

### Contribution
3
