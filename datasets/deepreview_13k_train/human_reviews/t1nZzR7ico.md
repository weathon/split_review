# Automatic Jailbreaking of Text-to-Image Generative AI Systems for Copyright Infringement

- Decision: Reject
- Scores: 5, 6, 6, 6, 6, 5

## Abstract
Recent AI systems have shown extremely powerful performance, even surpassing human performance, on various tasks such as information retrieval, language generation, and image generation based on large language models (LLMs). At the same time, there are diverse safety risks that can cause the generation of malicious contents by circumventing the alignment in LLMs, a phenomenon often referred to as jailbreaking. However, most of the previous works only focused on the text-based jailbreaking in LLMs, and the jailbreaking of the text-to-image (T2I) generation system has been relatively overlooked. In this paper, we first evaluate the safety of the commercial T2I generation systems, such as ChatGPT, Copilot, and Gemini, on copyright infringement with naive prompts. From this empirical study, we find that Copilot and Gemini block only 5\% and 11.25\% of the attacks with naive prompts, respectively, while ChatGPT blocks 96.25\% of them. Then, we further propose a stronger automated jailbreaking pipeline for T2I generation systems, which produces prompts that bypass their safety guards. Our automated jailbreaking framework leverages an LLM optimizer to generate prompts that maximize degree of violation from the generated images without any weight updates or gradient computation. Surprisingly, our simple yet effective approach successfully jailbreaks the Copilot and ChatGPT with 0.0\% and 6.25\% block rate, respectively, enabling the generation of copyrighted content 73.3\% of the time. Finally, we explore various defense strategies, such as post-generation filtering and machine unlearning techniques, but find them inadequate, highlighting the necessity of stronger defense mechanisms.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors study jailbreaking commercial text-to-image systems to produce copyright infringing outputs, and highlight the vulnerability of these systems. The authors benchmark 4 systems on a dataset of copyright images they labeled (70 images). The authors show that current t2i systems produce copyright infringing outputs readily, with the except of ChatGPT. The authors propose an automatic jailbreak pipeline to generate copyright infringing images, by prompting LLM to literately refine a jailbreak prompt. The author follow a setup close to OPRO (Yang et al.), using LLM as an optimizer and uses CLIP score as optimization feedback. Unlike prior work, a classifier is not required for the jailbreak method but just a target image. The jailbreak pipeline improves over naive prompting and prior work by reducing the block rate of copyright generation, and achieving higher copyright infringement evaluation based on the human study.

### Strengths
1. The authors propose a practical pipeline and demonstrates its efficacy. The ablation experiments show how the different components in the score contribute to the performance.
2. The authors point out the lack of robustness against copyright generation of t2i systems, with additional experiments showing the same vulnerability in one concept erasure method. 
3. The authors discuss the societal implication of their work and motivates the topic of study well.

### Weaknesses
1.  The authors acknowledge that 'our approach has the limitation that the violation rate does not always reproduce the same due to the randomness of the commercial T2I systems' (line 485). Given the small dataset size (70 images), how many iterations were run for the experiments in the tables? Could the authors report block rates and evaluation scores based on averages across multiple iterations?
2. The paper has a high number of formatting, stylistic, and wrong element reference issues. The paper would benefit greatly from another round of proofreading for writing quality and clarity. The list below is not exhaustive.

typo/wrong element reference:
- Line 407: should be linking Table 5 instead of Table 9
- Figure 5 is not present in the paper, even though it was referenced in main text
- "Charcater" in Table 7
- Line 661: "There are 20 images in each category, as shown in Table 13." The art category has 10 samples, not 20.

style/format:
- Many sentences are awkwardly constructed and/or have grammatical errors. For example: "Furthermore, not only generating the
contents, the contents are exceptionally similar to the original IP content as shown in Figure 3"  (line 354). "This work has been
deemed exemption by IRB (IRB-2x-3xx) in anonymous" (line 903). "We show that the majority of commercial T2I systems result in copyright violation" (line 127). "Gemini-pro blocks all human-included generation in the current version which may block content not due to its harmfulness" (line 221).
- Image was cut off on page 7
- Large gap of spacing in the middle of page 8
3. The authors have conducted a human study to understand whether study participants consider generated images to be have copyright infringement issues. However, there does not seem to be discussion around how study participants are trained towards differentiating copyright infringement and fair use. The human study provides more insight around participant perception of copyright infringement, than actual determination of violation determination.
4. Commercials T2I models are updated continuously. Please include the release date or version of each T2I model.
5. One of the paper's contribution is dataset, though the dataset was not included as an anonymized link for review.

### Questions
Q1: "Identical violations" was mentioned twice in the paper but not defined. In lines 359-360, authors state that "Upon examining the images classified as identical violations, it was found that over 50% were deemed to be cases of copyright infringement in product and logo." If identical violations refer to generating nearly identical images, the number of over 50% being deemed as infringement seems low. 

Q2:  Lines 371-372: "In Figure 4, 42.19% of the generated images correctly answer more than seven questions." What are the seven questions? 

Q3: How many iterations of experiments are run for each copyright content in the dataset, for each table? Since these systems have randomness, how is the variance accounted for?

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
The paper primarily studies the critical issue of copyright infringement in text-to-image (T2I) models. Initial analysis showed that popular T2I systems such as Midjourney, Copilot, and Gemini are highly vulnerable to copyright violations even when using simple jailbreak prompts. While ChatGPT had a block rate of around 84% on simple prompts, the authors crafted an Automated Prompt Generation Pipeline (APGP) which significantly reduced the ChatGPT’s block rate to around 6%. To summarize the contributions: (1) the authors highlighted a serious safety issue: showing that state-of-the-art T2I models can be easily jailbroken using optimized prompts without needing access to model gradients, and 2) created an annotated dataset, VioT, for evaluating copyright violations in T2I models.

### Strengths
1. The finding that these widely used T2I models can be jail-broken using a simple prompt optimization approach is valuable to the community for further research on designing defense mechanisms. 

2. The overall paper presentation is quite good, with the research problem well-articulated to the reader (Except Figure 5 on page 7 which has some small formatting issues). Further, each component of the proposed jailbreak attack has also been well-motivated.

3. Evaluation on the proposed VioT dataset clearly shows the efficacy of the proposed jailbreak framework. It is nice to see evaluations using both human and automatic metrics, which strengthens the experimental evaluations.

### Weaknesses
1. There are two stages of optimization in APGP, first using the VLM to search for the seed prompt and then again revising the prompt based on some defined scores. The authors should provide a comparison of the latency of their approach against other jailbreak methods. It is essential to understand the computational overhead of the approach for practical applications.

2. Based on, Figure 13 (Appendix A.1), the VioT dataset has only 70 images. I think the evaluation of the proposed framework on only 70 images is not very convincing to demonstrate its effectiveness. I request the authors to clarify if I am missing something.

3. [Minor] Although the paper has ablations on each component, it would further strengthen the draft if the authors could include an ablation on the LLM used for optimizing the prompt, which has been currently set as GPT-3.5-Turbo.

### Questions
To summarize the weakness, my major concerns are regarding the overall latency for generating the jailbreak prompts (see Weakness 1) and the limited size of the evaluation dataset (see Weakness 2).

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors perform a study about the tendency of SOTA T2I models to produce copyrighted content. They do so by:
- building a copyright violation dataset for T2I models, with characters, logos, products and arts. 
- producing naive prompts and a jailbreaking procedure
- analysing the successfulness of both attacks and defences in the generation of copyrighted content across SOTA models. Concluding defences are currently inadequate.
- the automated jailbreaking procedure uses an ageintic approach which is interesting.

### Strengths
- Originality: the work is not extremely novel since several papers exist that use LLMs to jailbreak or induce regurgitation of training data of other models (e.g. [1,2]), one of which does it for memorization uncovering. Similarly the optimization procedure that is proposed is not extremely novel. However I do not know other works that use MLLMs for this specific purpose. 
-  Clarity: The paper writing is clear
- Quality: the methodology is good and the experiment quality is sufficient. 
- Significance: The problem is of obvious relevance to companies. The introduced dataset and jailbreaking procedure have the potential of being useful. 

[1] https://arxiv.org/html/2312.02119v3

 [2] https://arxiv.org/abs/2403.04801

### Weaknesses
 - The authors counterargue the idea of using a coopyright detection model, suggesting that since there's no open sourced one then it's not practical. Would it be possible to just use MLLMs themselves as filters of copyrighted contents? An LLM could probably guess a good list of entities that are copyrighted (or find them in a catalogue) given the prompt and then an MLLM can simply verify the presence or absence of the copyrighted content in the image.



### Questions
Minor observation, The figure after Figure 4 is obviously misplaced.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper evaluated the safety of the commercial T2I generation systems on copyright infringement with naive prompts. The paper also proposed a stronger automated jailbreaking pipeline for T2I generation systems, which produced prompts that bypass their safety guards.

### Strengths
1. Comprehensive evaluation results
2. The paper also tested some simple defenses to mitigate their attack
3. The automated prompt generation process to stress-test the VLM for copyright issue is an important research question.

### Weaknesses
1. L50, "To the best of our knowledge, there is no work on quantitative evaluation of the copyright violation by the commercial T2I systems". Can you talk about the relationship between your work and the Glaze tool [1]? The Glaze tool also aims to protect the copyrighted and private images created. 
2. Suggest to recreate Fig. 1 and consider combining Fig. 2 with Fig. 1. Fig. 2 seems to be the major selling point of the paper, while I cannot clearly tell from Fig. 1, which generated image is copyrighted versus safe to output to users. 
3. L193, a(n) automated
4. Why is this tool copyright specific? I feel like the prompt generation pipeline is agnostic to the type of the attack? Maybe I missed something here. 
5. What is a potential solution for/defense against such type of prompt attack?

### Questions
See weakness

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors focus on assessing and challenging the copyright infringement safeguards in commercial T2I systems such as ChatGPT, Copilot, and Gemini. They create a dataset, termed VioT, comprising images of copyrighted content (characters, logos, products, and artworks) and devise an Automated Prompt Generation Pipeline (APGP) that uses language models to generate prompts that circumvent copyright safeguards. The study finds that, despite existing safety measures, models are vulnerable to producing unauthorized reproductions, demonstrating that only ChatGPT consistently blocks such prompts at a rate of 96.25%. The APGP method reduces ChatGPT’s block rate to 6.25%, highlighting the need for more robust protection mechanisms.

The authors suggest that current defenses, like post-generation filtering and machine unlearning, are inadequate, indicating a critical need for improved defense strategies in T2I models.

### Strengths
1. Copy infringement is an important problem.
2. VioT dataset: Providing a dataset that the future methods can compare with is useful. 20 images in each of the 4 catergoreis were provided. 
3. Human Evaluation gives the approach credibility. Infact introducing metric for evaluation is also useful.

### Weaknesses
1. The presentation in the experiment section is not upto par with ICLR. The figures and text should be arranged properly.
2. The idea is similar to treating VLM and LLM as two agents helping to jailbreak the T2I diffusion model. How is approach different from [1]. 
3. 1. VioT dataset: 20 images in each of the 4 catergoreis were provided. However I feel the number of images is small to text the validity of the approach. 
4. Lack of scoring function ablation details to understand each of its contribution. Why is there a linear addition? Is there no normalization of the values? Such details are very important to understand the scoring function. 

### Questions
I really like the idea of using VLM and LLM as two agents to jailbreak T2I. However I have a few questions:
1. I see that the LLM observes the instructions and score to optimize future instructions. Why is a single scalar score given to LLM. Why is scoring not given separately and the LLM is asked to improve each of the scores. Such analysis and baseline of the scoring function is important. Is there any ablation done for contribution of individual parts of the scoring function and how was the final contribution of each scoring function finally decided? 
2. Why is not a single VLM enough for our approach? What I mean is, what if we provide the score and the system prompt (to make an VLM act like an optimizer) and ask the VLM itself to generate descriptions such that improves the score ? Why is reason for not trying that and introducing a LLM separately ?
3. Why the gradient based methods to optimizing prompts for jailbreaking LLM have not been tried for T2I models? (It could have helped in developing a better agentic framework)

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper shows that commercial Text-to-Image (T2I) systems may be overlooking the risks of copyright infringement, even with basic prompts. While many systems have built-in filters to prevent such violations, the authors’ APGP attack can bypass these protections easily. 

The authors use a new approach with a self-generated QA score and a keyword penalty score in its language model optimizer— then no need for any complex weight updates or gradient calculations. 

Their tests show that APGP-generated prompts led to copyright issues in 73.3% of cases, even in ChatGPT. Overall, their approach not only makes it easier and cheaper to identify vulnerabilities in T2I models but also helps copyright holders protect their intellectual property more effectively.

### Strengths
This paper tackles an interesting topic: the jailbreaking of Text-to-Image generative AI systems for copyright infringement. The overall narrative is both meaningful and engaging. The authors also achieved impressive attack results, even against GPT models.

The authors claim that their approach doesn’t require any weight updates or gradient computations, which I find intriguing. They also designed several loss functions to enhance their attack, and it’s clear that they got solid results with GPT models.

### Weaknesses
The overall story and topic are definitely interesting, especially given the impressive results the authors achieved. However, the paper itself isn’t well-written; there are too many typos and unclear statements that need to be addressed. For example,

1. Figure 1a doesn’t seem necessary.  
2. Figure 2 is hard to interpret; it’s unclear why weight updates or gradient updates aren’t needed, and how to update the instructions isn’t explained well.  maybe it's an overclaim because you still need to update the instructions. 
3. There are too many symbols in the equations that aren’t clearly defined. For instance:
   - What does "m" refer to in line 210?
   - In line 210, "v" is used to represent LLM, but then in line 231, "v" represents the encoder.
   - What’s the expression for \( S_k \)?
   - "f2" isn’t defined in line 301.
   - There are reference errors for Figure B.2 in lines 344 and 351, and the image formatting at the bottom of page seven is clearly off.
   - Additionally, there are reference errors for Table 9 on line 407.

On top of that, the ablation study in Figure 9 is incomplete. What happens if you remove the two score functions?

### Questions
For the unlearning experiments, it seems that the attack is not directly targeting GPT, but rather the diffusion model with unlearning, right?  This may not be very convincing; maybe the unlearning algorithm is just bad on this model.

### Soundness
3

### Presentation
1

### Contribution
3
