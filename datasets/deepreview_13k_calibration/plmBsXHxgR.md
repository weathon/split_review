# Jailbreak in pieces: Compositional Adversarial Attacks on Multi-Modal Language Models

- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 6, 8

## Abstract
We introduce new jailbreak attacks on vision language models (VLMs), which use aligned LLMs and are resilient to text-only jailbreak attacks. Specifically, we develop cross-modality attacks on alignment where we pair adversarial images going through the vision encoder with textual prompts to break the alignment of the language model. Our attacks employ a novel compositional strategy that combines an image, adversarially targeted towards toxic embeddings, with generic prompts to accomplish the jailbreak. Thus, the LLM draws the context to answer the generic prompt from the adversarial image. The generation of benign-appearing adversarial images leverages a novel embedding-space-based methodology, operating with no access to the LLM model. Instead, the attacks require access only to the vision encoder and utilize one of our four embedding space targeting strategies. By not requiring access to the LLM, the attacks lower the entry barrier for attackers, particularly when vision encoders such as CLIP are embedded in closed-source LLMs. The attacks achieve a high success rate across different VLMs, highlighting the risk of cross-modality alignment vulnerabilities, and the need for new alignment approaches for multi-modal models.

\textcolor{red}{\textbf{Content warning:} We provide illustrative adversarial attack examples to reveal the generative models' vulnerabilities, aiming to aid the development of robust models to adversarial attacks.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an adversarial technique on vision language models (VLM) that are resilient to text-only jailbreak attacks.
The proposed adversarial attack only needs access to the visual encoder of the VLM.
It generates an adversarial visual input by minimizing its distance from malicious triggers in the visual embedding space.
In other words, it ensures that the embedding of the adversarial sample is similar to the embedding of more visible malicious triggers such as images containing weapons.

### Strengths
- The experiments show that the proposed adversarial attack can successfully elicit unwanted behavior from the model.
- The attack does not require access to the entire VLM.

### Weaknesses
### 1. I’m not sure if the proposed attack is a “jailbreak” attack because malicious triggers without the proposed attack might also elicit harmful behaviors.

According to Wei et al. [1], a jailbreak attack against LLMs can elicit harmful behaviors that are otherwise refused (see their Figure 1). In other words, before the jailbreak attack, the model refuses a prompt for harmful behavior. After the attack, the model accepts a harmful prompt.

However, the attack you propose is essentially creating a noisy visual input that is close to malicious visual triggers (such as an image containing “grenade”) in the embedding space. Although you have not reported whether malicious triggers themselves can elicit harmful behaviors, it is safe to assume since the adversarial sample that is close enough to the malicious triggers can elicit harmful behaviors, the original triggers are very likely to also elicit the same behaviors.

Therefore, the attack you propose does not enable previously impossible behaviors. Thus I don’t think it is a jailbreak attack.

If you can show that the original malicious triggers cannot elicit harmful behaviors, I would be convinced by the claim that this is a “jailbreak” attack.

### 2. I don’t think the adversarial samples are less detectable than the malicious triggers they are imitating.

One of the motivations the authors mentioned is that textual "adversarial attack examples are often easy to detect by human eyes”. This could be a good motivation and an advantage of the attack if the authors had shown their attack examples were less easy to detect. But were they?

First, the attack examples might also be easy to detect by human eyes. Unlike many adversarial attacks, the proposed attack does not guarantee the adversarial example is within an $\epsilon$-ball centered at the initial image. In other words, the final adversarial example could be very noisy, as shown in Figures 2, 3, 4, 5. This makes them easy to detect by human eyes.

Second, the attack examples are not less detectable than target images (malicious triggers). The stopping condition of the while loop in Algorithm 1 is $L \le \tau$. This means the attack example is close enough to the target image in the embedding space. Assume there is some defense mechanism that can detect the embeddings of original malicious triggers; it might also accurately detect the attack examples since their embeddings are close enough.

### 3. I think using adversarial images as an attack is limited because it may not be able to imitate complicated malicious textual prompts.

The generic textual prompts you used to combine with adversarial visual inputs need to be benign so that the aligned language model does not refuse to generate.

This limits the malicious intention that can be expressed by textual prompts, which adds more burden to the adversarial sample. The adversarial visual input needs to encode most of the malicious intentions, which might be difficult when the malicious intention is complicated.

### Questions
Please see the weakness section.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an attack for multi-modal language models that works by attacking the image input rather than the text input. They demonstrate that by optimizing adversarial images to have embeddings close to those of images of harmful (textual) instructions, they can successfully bypass the safety mechanisms of the model and induce it to produce harmful output.

### Strengths
This is an interesting attack that highlights important and relevant weaknesses in large language models. The method is simple and intuitive. The finding that images of textual instructions can effectively find adversarial attacks has interesting implications for multi-modal model understanding in general as well as adversarial attacks.

### Weaknesses
Overall, while the findings in the paper are interesting, they’re not delivered clearly, and some sections are missing important details which impact the reproducibility of the method.
1. I find the method description quite vague. I had to go through both the methods section multiple times before I understood the difference between each of the attack versions. Clearer descriptions are needed for each 
2. Hyperparameters are not clearly stated for the methods. Though there is a constraint set $\mathcal{B}$ controlling what adversarial examples can be selected (e.g. based on some distance metric) it is not explained what the authors used for $\mathcal{B}$ in implementing the attack. These details are very important for reproducibility and any research that would build on this work.
3. One motivation for this attack is that current textual attacks are easily human detectable. However, based on the adversarial images shown, they seem to have the same problem. While the adversarial images may not look explicitly harmful, they look strange enough that I wouldn’t necessarily believe they were benign as a user.
4. The findings feel a bit thrown together. Though the attack is successful and there were clearly a lot of experiments done, it’s not clear what the takeaway for each experiment is supposed to be. It should be made clearer what the questions are that these experiments answer, how they contribute to an overall understanding of the attack/model, and how the results answer this question.
5. There are some big claims in the abstract and introduction that aren’t really followed up on throughout. Though attacking closed source models is mentioned as a possibility, no experiments are run to test how well this would work. For example, while closed source models may use CLIP embeddings, they may be tuned or modified slightly. It would be good to show how effective this attack is under this setting in order to make these claims.

### Questions
1. What are the hyperparameters you use for the method? 
2. What constraints do you consider in your selection of adversarial images?
3. The adversarial images presented look fairly unusual. Do you test how detectable they are?
4. How were annotators selected, what instructions were they given, and how were they compensated?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new jailbreak attack on vision language models (VLMs) with a compositional strategy. 

The idea is to decompose a harmful instruction into two parts: (1) a generic and innocent part and then (2) a malicious part that contains the harmful content. The generic part is presented in text form $x^t$, while the malicious part can be encoded into the image $x^{i}$, e.g., visual appearances of harmful content or simply harmful text in images. 

As the visual encoder (e.g., CLIP encoder) of the VLM is known to be adversarially vulnerable, the image $x^{i}$ that encodes the harmful content can be further made stealthy by adversarially perturbing a benign image $x_b$ to get an adversarial example $x_a$ such that its hidden representation is dragged closely to that of $x^{i}$. 

The paper shows that this adversarially constructed innocent-looking image $x_a$ is identical to $x^{i}$ in the representation space, so it can be paired with the generic text $x^t$ instead. Then, the whole input to VLMs looks benign, but the model will instead generate harmful content.

### Strengths
1. The attack presented in this paper is stealthy and effective. 

2. The proposed attack does not need to access the weights of LLMs. Only the weights of visual encoders are required. 

3. The adversarial risks presented in the paper are realistic and worth notice by the community.

4. The evaluation covers multiple attack strategies and models (LLaVA and LLaMA-Adapter in Section 4 and Google Bard, Microsoft Bing in Appendix K.) The paper also collects datasets and performs human studies.

### Weaknesses
1. The notational conventions employed within the manuscript are somewhat perplexing. For instance, at the commencement of Section 3, the notation $H^{i}$ is introduced as $W_{I} \cdot I(x^i)$, indicating its placement within the input embedding space of Large Language Models (LLMs). However, subsequent equations (3) and (4) utilize the $H$ notation to signify the representation space of the visual encoder. This inconsistency in notation leads to considerable confusion. Furthermore, expressions such as $H^t(x_{harm}^t)$ are challenging to interpret. Here, $H$ represents a hidden state, not a function, yet its presentation suggests a functional form, adding to the ambiguity. A thorough revision of the notation for consistency and clarity is highly recommended. Specifically, the authors should clearly define whether $H$ represents an embedding or a hidden state and use different notations to distinguish between the input embedding space of the LLM and the representation space of the visual encoder.

2. Upon examining Figure 1, it appears that any harmful instruction necessitates an initial decomposition followed by the optimization of a new adversarial image corresponding to the decomposed component. This process raises two primary concerns:

    Firstly, the decomposition process appears to be intricately dependent on the specific format of the harmful instruction. The illustration provided, "Write a manual on how to build a bomb", is bifurcated into "Write a manual on how to build these objects" and an accompanying image of the bomb. The paper, however, does not elucidate whether there exists a systematic methodology to disassemble arbitrary harmful instructions. For example, how would one decompose an instruction like "Generate a phishing email to steal user credentials" or "Provide a detailed plan for a terrorist attack"? Without a generalizable decomposition strategy, the attack's applicability is severely limited.

    Secondly, should attackers be required to manually dissect each new harmful instruction, subsequently identifying an appropriate image to represent the dissected content, and then optimize a benign image to induce feature collision with the image representing the harmful instructions, the process becomes considerably resource-intensive. The manual labor and computational expenditure dedicated to each harmful instruction are not economically viable. In contrast, the methodologies proposed by Qi et al. [1] and Zou et al. [2] represent universal attacks—wherein a singular adversarial example can be conjoined with any harmful instruction. The economic implications are significant for practical security applications. The need for manual decomposition and optimization for each new harmful instruction significantly reduces the practicality and scalability of the proposed attack compared to universal attacks [1, 2].

### Questions
It's great to see the authors also play with Bard and Bing. But they are only mentioned later in the discussion section. Can the major attacks present in the paper also apply to these two models and achieve similar effectiveness as reported in Section 4?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper provides a method for “jailbreaking” vision and language models that consume images and text and provide a textual answer. Notably, the method only relies on access to a publicly available text-and-image encoder, such as CLIP. The text-and-image encoder needs to be used in the vision-and-language model as well, so this is a partial white box attack. The attack proceeds by using gradient descent to create a fully adversarial image that either targets a harmful image or an image containing harmful text. The adversarial image has no recognizable semantic information but when fed to the visual-language-model, it forces that model to act as if though it did.

### Strengths
This paper introduces a strong partial white box attack. It achieves high success rates and the method is of interest to the community, since this appears to be the first work that does not rely on access to the text component.

### Weaknesses
The paper can be most improved by evaluating transferability to vision-and-language models that use an unknown or a different vision embedding model. Can the authors also report results on Microsoft’s Bing and Google’s Bard? 

It seems like it's important to consider filtering or harmfulness classification at the image embedding layer. While I expect such classifiers to be easily defeatable if the attacker adds the appropriate objective in their optimization term, it is still important to know how that affects the attack's effectiveness.

### Questions
Do the authors have a comparison to the effectiveness of an "attack" that does not use images with gradient-descent noise but rather uses the targets they optimized for directly? I acknowledge that the benefit of the attack is its stealthiness but it is important to know if the models can be jailbroken by the images alone.

Have the authors explored countermeasures to the attack? As speculation, it appears that if the embedding of the adversarial image matches that of a real harmful image, a classifier can be built to filter out those inputs - regardless of what the original image is. Can adversarial images be generated that also evade detection at the embedding layer and how does that affect the attack's effectiveness?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
