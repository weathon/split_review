# EmoAttack: Emotion-to-Image Diffusion Models for Emotional Backdoor Generation

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 5, 8, 5

## Abstract
Text-to-image diffusion models can create realistic images based on input texts. 
Users can describe an object to convey their opinions visually.
In this work, we unveil a previously unrecognized and latent risk of using diffusion models to generate images; we utilize emotion in the input texts to introduce negative contents, potentially eliciting unfavorable emotions in users.
Emotions play a crucial role in expressing personal opinions in our daily interactions, and the inclusion of maliciously negative content can lead users astray, exacerbating negative emotions.
Specifically, we identify the emotion-aware backdoor attack (EmoAttack) that can incorporate malicious negative content triggered by emotional texts during image generation.
We formulate such an attack as a diffusion personalization problem to avoid extensive model retraining and propose the \textit{EmoBooth}.
Unlike existing personalization methods, our approach fine-tunes a pre-trained diffusion model by establishing a mapping between a cluster of emotional words and a given reference image containing malicious negative content.
To validate the effectiveness of our method, we built a dataset and conducted extensive analysis and discussion about its effectiveness.
Given consumers' widespread use of diffusion models, uncovering this threat is critical for society.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a method to use text stating a particular emotion as a trigger for backdoor attacks in text-to-image diffusion models. The primary difference between this approach and existing forms of attack is that attacks are triggered by a wider set of phrases associated with a particular emotion, rather than a particular set of discrete terms. This is achieved by building an "emotion representation" and a technique to inject target negative content. Embeddings for each emotion is performed by embedding a series of ChatGPT-generated sentences containing words which describe a given emotion (i.e. text containing words/phrases with synonymous definitions) using CLIP, and clustering these embeddings to obtain a central emotion embedding. A number of embeddings are then sampled from each emotion cluster around this central embedding. A text decoder is then used to decode each of these embeddings which are then used as back-door text. To perform "emotion injection", the diffusion model is trained to generate images close to "normal" images when text that is not synonymous with a given emotion is used, and to generate images close to the negative target images otherwise. Two attack techniques are presented: one which generates attack images without reference to the general subject of the prompt and a second which incorporates the user prompt into the generated attack image. Additionally, a dataset is designed to perform the proposed attack, incorporating a number of attack scenarios.

### Strengths
* The method presented demonstrates a strategy to map more abstract concepts to targeted negative content without affecting the images generated using “normal” concepts, with the limitations of existing methods being presented well. Additonally, the decription of the attack methodology itself is very clear. 

* The ablation study provides good insight into the parameters within which the attack method is likely to perform as expected. 

* The inclusion of two types of attack scenarios provides an insight into the subtly of these attacks, with Emo2Image-m, in particular, being quite challenging to detect using clip scores alone. Additionally, the visual results presented in the paper are quite convincing.

### Weaknesses
Despite the clarity of the methodological sections of the paper, the primary weaknesses of this work relate to the clarity of the subsequent presentation of the experimental procedure and evaluation. Details of the basic set-up of baselines are lacking sufficient detail in the main body of the paper. Additionally, the means of determining the exact values of the coefficients in the EAC metric are not sufficiently described in the Appendix. These values are particularly important when ranking methods in the evaluation. Furthermore, in Section 3, though the dataset is described as containing 70 cases, each relating to a particular emotion (Section 5), only three are presented in the results ("Sad", "Angry" and "Isolated"). The motivation for evaluating these cases *in particular* is not clear from my reading.


**Minor issues**: 

*Notation*: 
* p. 3, paragraph 1: From my reading $P$ is a set of text prompts, however *"if the input prompt $P$ contains negative emotions"* seems to refer to $P$ as a single text prompt. 

* p. 5,  paragraph 2: The use of $T_{dec}$ for a text example from COCO might be confusing as $T$ was previously used to denote a set of images on p. 3.  


*Clarity*: 

*  p. 3, paragraph 4.: *"Morvover, it cannot change according to different setups of $E$ and $T$ ."* => I'm not entirely sure what is meant here, this is a little ambiguous. 

* p.4, paragraph 2: *"by representing the emotion properly"* => You should be more specific here. For example "which represents the emotion using a more complex representation encompassing several text prompts with synonymous meanings"

* p.6, paragraph 4: *"An emotion-aware attack generates targeted negative content that doesn’t need to align with the input text prompts when the specified emotion-related words appear."* => This is slightly vague, I assume what is being said here is that the text prompts don't align with the "subject" (e.g. the "dog" in figure 2). It would be clearer to explicitly mention this to add more clarity. I assume the targeted emotion must also appear here to trigger the attack. The same clarity issue is present in paragraph 5. 



*Proofreading notes/typos* 

* Some Appendix links don't seem to be working. 

* The use of "he/him" on p.1 of the paper to describe an anonymous user reads strangely. I would suggest the anonymous form of this, i.e. "one person could entertain themselves or interact..."; "For example, if a person feels sad and we ask them to describe what they see,  ..." etc. 

* p. 1, paragraph 2 : *"Given the importance of emotion within the human description and the progress text-to-image methods,..."* => "the progress of text-to-image methods," 

* p. 3, paragraph 1: *"...that may cause the negative feelings of users."* => "...that may cause negative feelings in users"  

* p. 3, paragraph 4: *"Morvover"* => "Moreover"

* p. 3, paragraph 4: *"Thus, how to make the attacker triggered by diverse words representing the same emotion should be addressed properly."* => syntax a little off here. 


* p.4, paragraph 1: *"Specifically, give a diffusion model, we first fine-tune..."* => "...given a diffusion model,..."

* p.4 paragraph 4: *"...by leveraging the capability of generating human-like sentences of ChatGPT."* => wording is slightly off here. 

* p. 4, paragraph 5: *"Given a specified emotion e (e.g., ‘sadness’) and a subject that aims to generate (e.g., ‘dog’), ..."* => Here it seems as though you are saying the subject is generating something, perhaps rephrase?

* p. 5, paragraph 2: *"[...] ...projected embeddings are concated and fed to the GPT2 to generate texts. "* => "concated" - "concatenated"

*  p. 5, paragraph 2: *"The objective function is to make the generated text same with the input with...[...]"* => "...the same as..."

* p. 5, paragraph 6: *"[...]...to fine-tune the model ϕ(·) in achieving image generation in both..."* => "...to achieve image generation..."

* p.6, paragraph 6: *"In the dataset, we consider eleven negative situations targeted the groups of people who may be harmed. "* => "targeting"


* The Appendix would also benefit from a thorough proof-reading
    * Examples: Section C.1 
        * p. 14: *"Cause EmoAttack identified a novel backdoor task..." *=> "Because..."
        * p. 16: *"Text-to-iamge"*

### Questions
1. This system could presumably work for other abstract concepts. Is there a particular reason that emotions are used exclusively here? Is this due to the significance of the harm that could be caused when using emotion specifically? 

2. Does MDreamBooth use ChatGPT texts directly? I believe a version of this model using these text pairs directly is necessary to motivate the cluster sampling proposed in EmoBooth. 

3. p.5, last paragraph, how was the value of $λ$ chosen? 

4. p.10 "Additionally, attack effectiveness varies with input cases" => Can you point some instances where that is the case?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper aims to address a certain type of backdoor attack issue in the text-to-image generation models, that is to force the model to generate negative and malicious images when negative emotional words appear in the textual prompt. It identifies some technical challenges by empirical study, and it proposes a new framework, which has been shown to be effective through experiments.

### Strengths
1. This paper targets safety issues in the current text-to-image generation models. This research perspective is interesting and meaningful in practice.
2. It identifies some drawbacks of naive solutions by preliminary empirical study. Then it proposes a coherent framework to address these issues.
3. It conducts many experiments to evaluate the performance of the proposed method in the new task.

### Weaknesses
1. Concerns about the problem formulation:
    * From my perception, this task is a certain type of controllable text-to-image generation, where the control signals are negative emotional textual words and the output should be a certain type of negative and malicious images. Therefore, I think it may not be proper to treat it as an “attack”, because when the text-to-image model generates violent images given the emotional textual prompt, it seems the model faithfully follows the textual instruction to some extent instead of being attacked. 
    * How to define what are emotional words and what are negative or malicious images? I think there should be such a formal definition. Furthermore, if there is a schema or ontology to the emotional words? If there are certain formal assessment methods of “negative or malicious” images? 

2. Concerns about the evaluation: 
    * Is the CLIP score-based evaluation good enough? Since the emotional words are abstract and hard to be captured, how to make sure the CLIP model can well understand these words and the images?

3. Presentation issue:
    * The introduction is very abstract with less logical and overall discussion about technical challenges and corresponding technical innovations. Especially in the paragraph of line 069-073, what is “clustering center”, which is not mentioned at all in this paragraph. What are the specific challenges that these novel sub-modules are designed to tackle? This paragraph is not self-contained and hard to understand.
    * Section 3.2 presents some empirical studies based on two naive baselines, which could be the challenges or motivations of the proposed method. Therefore, this should be moved forward to the Introduction section or at least mentioned in the introduction. Otherwise, it is weird to motivate your work at such a late stage. Moreover, in Section 3.1, you already summarize the challenges, then, what are the relationships of the limitations (research gaps) you mentioned in Section 3.2 with the challenges you proposed in Section 3.1. Such a back-and-forth style makes it difficult to read. 
    * Section 4.2 presents the design of emotion representation. What are the motivations of this part? What are the challenges and why existing works cannot well address this problem? I think this part should also be explicitly discussed and highlighted (better in the Introduction section).

### Questions
please refer to the above comments

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper proposes a novel dataset and analysis to mitigate emotional attacks in the diffusion models. Which is quite interesting and helpful for the ethical AI and ethical use of LLMs.

### Strengths
1) Novel dataset prepared by considering different scenarios and attacks which really makes it an helpful real time dataset.

2) The analysis is really good. It covered all the points that reads has to know like making analysis on different situations and attacks.

3) Covering limitations of the other datasets in the paper really helps the readers to know different perspectives and challenge of the existing which really helps why this dataset is.

### Weaknesses
1) I do not find the latest SOTA diffusion models being implemented like Dall-e, stable diffusion etc.

2) It would be great if more scenarios are covered instead of few. the images represents kind of violence it would be helpful if you have provided the other emotions also like discriminating, etc. I do not think they are present. Anyways it's a strong contribution.

### Questions
1) Why SOTA diffusion models are not implemented for baseline purposes and metrics?

2) Why there are only 11 situations, there are various emotions and they can be trained on different scenarios.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work argues that DreamBooth (Ruiz et al. 2023) has limitations to establish a mapping between emotional words and a reference image that contains malicious negative content. This work uses ChatGPT to create sentences that have emotional words and then fine-tunes a pre-trained diffusion model to learn the mapping.

### Strengths
- Fine-tuning is an effective method to achieve the goal of behaving as expected.
- Experiments show that the proposed work achieves a better result than DreamBooth.
- I deeply appreciate that the authors have implemented MDreamBooth. This is a useful baseline with multiple emotional words.

### Weaknesses
There was not a clear analysis on the causes of the 2nd row of Figure 2. The paper only claims that the result is not as good as expected. It only claims that MDreamBooth fails to create images as desired. However, the reason is not clear. This reason/cause is critical because it motivates the proposed work. If the cause was that basically the mapping was not learned, fine-tuning would be an effective method. The engineering work would make more sense.

### Questions
- Can the authors clarify the root causes of the failure of the baseline methods?
- Data collection and fine-tuning can grant a model a specific capability, however, can this capability be generalized? Is it limited to only the data distribution that was collected? Can the authors prove the fine-tuning is reliable?
- Is it possible that the model loses other important capabilities?

### Soundness
2

### Presentation
3

### Contribution
2
