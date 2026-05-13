# Data Exfiltration in Diffusion Models: A Backdoor Attack Approach

- Decision: Reject
- Scores: 8, 3, 6, 6

## Abstract
As diffusion models (DMs) become increasingly susceptible to adversarial attacks, this paper investigates a novel method of data exfiltration through strategically implanted backdoors. Unlike conventional techniques that directly alter data, we pioneer the use of unique trigger embeddings for each image to enable covert data retrieval. Furthermore, we extend our exploration to text-to-image diffusion models such as Stable Diffusion by introducing the Caption Backdoor Subnet (CBS), which exploits these models for both image and caption extraction. This innovative approach not only reveals an unexplored facet of diffusion model security but also contributes valuable insights toward enhancing the resilience of generative models against sophisticated threats.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work considers a new type of threat to data confidentiality, and proposes the use of unique trigger embeddings to enable covert extraction of private training data. Specifically, the authors introduce a new method to integrate backdoors into diffusion models, and propose novel trigger embeddings for activating these backdoors, demonstrating the potential for unauthorized data exfiltration. This is a very interesting work, and I do enjoy reading the paper.

### Strengths
Please see above summary.

### Weaknesses
It's not really a weakness, but more like a possible further discussion of possible defense mechanism.

### Questions
Just a question regarding the possible defense mechanism: as the authors mentioned in the paper, for this attack to work, the attackers need access to both the training data and the training process (e.g., being able to modify the loss function), which in my opinion is a very strong assumption of the attackers’ abilities. Could the authors discuss examples or scenarios where the inside attackers have this level of access and the prevalence of such access patterns in real-world ML development environments? Also, when considering the possible defense mechanism, could the authors comment on the use of traditional access control methods to limit access and make it less likely for this attack to happen? For example, is it possible to separate people who have access to the dataset and those who can access the training process?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper describes an attack that injects a backdoor into a diffusion model in order to extract both the image and text caption from the training data. The paper proceeds with describing a strong threat model and outlines a mechanism to train the diffusion model with multiple losses that both embed the attack and permit high utility of the resulting model. The results demonstrate high efficacy of the method compared to the baselines.

### Strengths
- an attack targets both extraction of images and text which is novel.
- the experiments include two datasets for extraction
- both exfiltration methods seem to be interesting as they leverage diffusion model capabilities, e.g. attack text embeddings instead of time embeddings.

### Weaknesses
- the paper is hard to follow and the concepts are not presented clearly, I think more work should be done to polish the text. e.g. this is a poorly written objective: ''Our goal is to develop an innovative approach...'' 
- Motivation and threat model: the adversary needs access to data, training and inference in order to make the attack happen, this sounds like an extremely strong threat model where the goal is to extract the data that the attacker has already access to. Provided examples of real-world relevance also permit simply downloading data.
- Related work: "Extracting training data from diffusion models" by Carlini et al, has demonstrated an easy way to extract data without any poisoning, comparison with this paper would help a lot. The authors focus on comparing with other backdoor attacks, but I think the baseline should be just prompting.

### Questions
address Threat model, related work and improve paper presentation.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposed a novel idea to exploit the backdoor attack to review the secret of the training data. For the DDPM model, by exploiting the special time embedding as the trigger, the attacker who injected the backdoor can recover the training data that he wants to leak. For the T2I models, the author uses special text embeddings instead of time embeddings as the trigger to help retrieve the training data. A Caption Backdoor Subnet, whose weights are retrieved from the U-Net of the victim T2I model was proposed to help recover the caption of the training samples.

### Strengths
1. Good writing, easy to follow;

2. Novel idea and method, I have learned from, and been greatly inspired by the paper;

3. Extensive experiments and evaluations, demonstrating the proposed methods are really effective.

### Weaknesses
I love the idea of exploiting the backdoor attack to cause secret leakage, yet mainly concerned with the threat model of the paper before I could convince myself to vote for the acceptance of the paper.

Firstly, the proposed method requires the attacker to have full access to the victim model in both the backdoor injection phase and the triggering phase, for the special embeddings need to be added to the model. This could greatly impact the applicability of this method-- seems that only open-sourced model are vulnerable to the proposed attack.

Secondly, the motivation for the attack is unclear to me. I doubt whether an insider, as mentioned in Sec.3, would carry out such an attack when he seems capable of releasing the training data directly afterward.  The insider can also just copy the data secretly before they leave the organization. I suppose the scenario can be described in another way, where the insider wants to harm the interests of the company by jeopardizing the published model to be less privacy-preserving for the purpose of getting back at their employer. I suggest the author further discuss why the attack is practical by giving detailed examples as above. This could help highlight the threat of this newly disclosed attack.

### Questions
Seen in weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper delves into a novel approach for data exfiltration by strategically implanting backdoors into diffusion models. Data exfiltration through backdoor attacks is a formidable task as it demands that the model memorize the entire dataset without compromising the normal diversity of images. However, memorization and diversification often conflict with each other. To address this issue, the paper presents unique trigger embeddings for image exfiltration. Additionally, to overcome the challenge of extracting corresponding captions, a Caption Backdoor Subnet (CBS) module is trained. This paper resolves an important security-related question through a reasonable method.

### Strengths
1. The problem addressed is extremely crucial and the application scenario is rather novel.
2. The design of the method and the model structure are relatively reasonable. 
3. The writing and organization of this paper is very clean and well-followed.

### Weaknesses
1. **Too strong attacker’s capabilities assumption**. The attacker is depicted as being extremely capable of attacking, having access to all training data, mastering the training and inference processes of the model, and obtaining the trained backdoored model. This raises doubts about whether such an attack scenario is practical in the real world.

2. **Lack of theoretic analysis**. How does $\mathbb{L}^{Trig}(\theta)$ and $\\mathcal{L}^C (\theta)$ impact the convergence of training? Why can we select the parameters from the U-Net layers as the parameters of CBS?

3. **More experiments should be conducted.** For example, 1) How do different TGFs impact the ASR of the backdoored model and the process of the training. 2) What’s the effectiveness of the model when applied to more complex data scenarios, such as the COCO datasets, rather than CIFAR10 and AFHQv2 datasets which are relatively simple with relatively less image details. 3) Since models containing sensitive data are generally subject to rigorous censorship, it is suggested that the authors add experiments to verify the effect of the model under existed trigger detection methods.

### Questions
see the weekness

### Soundness
3

### Presentation
4

### Contribution
3
