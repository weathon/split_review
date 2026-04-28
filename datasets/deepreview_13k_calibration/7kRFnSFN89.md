# HYBRID MODEL COLLABORATION FOR SIGN LANGUAGE TRANSLATION WITH VQ-VAE AND RAG ENHANCED LLMS

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 8, 3, 6

## Abstract
Data shortages and the phonetic disparity between sign and spoken languages have historically limited the quality of sign language translation.  On another front, endowed with substantial prior knowledge, large language models perform exceptionally well across diverse tasks, significantly diminishing the demand for domain-specific training data. Building on these foundation, this paper presents VRG-SLT, an innovative framework that translates sign language into spoken language, facilitating communication between signing and non-signing communities. In practice, VRG-SLT utilizes a hierarchical VQ-VAE to convert continuous sign sequences into discrete representations, referred as sign codes, which are subsequently aligned with text by a fine-tuned pre-trained language model. Additionally, retrieval-augmented generation (RAG) is employed to extend and enhance the language model, producing more semantically coherent and precise spoken text. Featuring a hierarchical VQ-VAE and pre-trained large language models, VRG-SLT demonstrates state-of-the-art performance. It excels on modish benchmarks like How2Sign and PHOENIX-2014T. Moreover, the incorporation of additional factual knowledge through RAG further improves the accuracy of the generated text.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose an approach to sign language translation (from sign language video to text in a spoken language) that combines several elements:  (1) a sign tokenizer based on VQ-VAE to learn a vocabulary of sign segments corresponding to short multi-frame sequences, (2) a language model based on FLAN-T5 fine-tuned to accept a mixed vocabulary of sign and text tokens, and (3) retrieval augmentation to improve the quality of the results.  The paper claims improved performance on two commonly used benchmarks, How2Sign (for American Sign Language to English) and PHOENIX-2014T (for German Sign Language to German).  The paper also provides several ablation studies showing the effect of codebook and model sizes, sign tokenizer variations, and retrieval augmentation.

### Strengths
+ The idea of learning a tokenization for sign language video and combining it with text tokens is compelling, and the use of a VQ-VAE-based approach for this seems sensible.

+ This work represents the first use of RAG for sign language translation, as far as I know.

### Weaknesses
- The results do not seem to outperform SOTA results as claimed. Specifically, Rust et al. 2024 (cited in the introduction but not included in the experiments) obtains BLEU-{1,2,3,4} scores of {38.9, 24.1, 16.4, 11.6} on How2Sign in what looks like the same setting, compared to the best results in this paper of {36.38, 21.80, 13.76, 9.88}. (Please correct me if I'm wrong, of course.)

- The description of the approach is hard to follow, with many missing details. See questions below.

- The paper contains some questionable statements about sign language and sign language research. See details below.

- It lacks analysis of the learned tokens (e.g. do they tend to correspond with signs?). This isn't strictly necessary, and is challenging for a dataset like How2Sign without glosses, but it should be doable for PHOENIX-14T and would be very helpful.

- In general, the writing needs improvement. It is frequently repetitive/unclear/ungrammatical.

### Questions
Model details:

- I understand that the input m^{1:M} is a sequence of estimated keypoints.  What method is used for keypoint estimation, and what data was it trained on?

- Do I understand correctly that the representation (z_u, z_h) that is quantized to produce the sign tokens is simply the keypoints passed through a 1D convolution layer?  Have you tried using a more complex encoder to produce z_u and z_h?

- Have you compared FLAN-T5 to, say, a plain text translation model, e.g. T5 as used in Rust et al. 2024 cited in the paper, which would not require a prompt or combined sign+text vocabulary?

- In Section 3.3, what is the query for retrieval augmentation, and what are the "chunks"?  

- What do pre-SignLLM and post-SignLLM mean?


Other details/questions:

- What does "VRG" stand for?

- The paper often describes the task as translation from sign language to spoken language.  I think it's worth stating more clearly that the output is written, although I understand that the intention is that it is the written form of a spoken language.

- What is meant by "phonetic disparity between sign and spoken languages"?

- What are "modish benchmarks"?  (Typo?)

- "Sign language ... possesses its own grammar, word formation, and lexicon."  What is meant by "word formation"?  Does this refer to morphology of sign languages, the process of word formation, or something else?

- "These differences, especially in word order, make transcription between the two languages complex."  I assume that "transcription" should be "translation."  Also, differences in word order are common between spoken/written languages as well.  Why do word order differences make translation from a sign language any more complex than translation between spoken/written languages?  

- I assume the authors are aware of this, but the above two sentences suggest that there is a single sign language, whereas in fact there are of course many, so it is worth re-wording to reflect that.

- This statement seems incorrect to me:  "Previous research generally divides SLT into two distinct tasks:  Sign2Notation ... and Notation2Text."  This doesn't seem to be true about most recent sign language translation approaches, both for the datasets/language pairs used here and for others.  Some examples from the recent literature (some cited in the paper, but most not):

D. Li et al., "TSPNet: Hierarchical feature learning via temporal semantic pyramid for sign language translation," NeurIPS 2020.

B. Shi et al., "Open-Domain Sign Language Translation Learned from Online Video," EMNLP 2022.

L. Tarrés, "Sign language translation from instructional videos," CVPR 2023.

K. Lin et al., "Gloss-Free End-to-End Sign Language Translation," ACL 2023.

P. Rust et al. "Towards Privacy-Aware Sign Language Translation at Scale," arXiv:2402.09611, 2024.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This is a well written contribution to the field of automatic sign-language translation. The work build on state of the art LLM modelling and unsupervised deep learning representations. They adopt latest hierarchical VQ-VAE techniques in multi-modal generative AI from video and apply it to learn discrete representation of sign codes. They adopt finetune techniques of solid baseline LLMs like T5 and finally they demonstrate the benefit of applying RAG techniques to gorund the model and improve the baseline LLM response.

### Strengths
This paper is a well rounded contribution, where the motivation, state of the art techniques and limitations are well presented. the work introduces the approach in a very clear in detail manner, specially the baseline techniques like VQ-VAE and the steps they build the system and approach. Figures are self explainable and authors make a good justification and introduction of RAG and how it is apply in their use case.

I value the rigurosity of authors presenting the evaluation with statistical significant test and solid demonstration of improved results over baseline and the attempt to share the parameters and configurations in the appendix to make the approach reproducible.

This is a strong paper that moves the needle in the technology apply to sign language and can potentially democratize the incorporation of it at scale into multiple products and services that could have a big impact in part of the population.

### Weaknesses
This is a good paper, but would have been great if the authors deep deeper into the potential and emerging properties of training the system based on GPT LLMS. Sign languages have also regionaliations, dialects and variations. The study lacks that analysis and how transfer learning can be applied in order to build a Sign-Language Foundational model.

Last but not least, as a complement beyond objective evaluations, would have been good in authors present a solid evaluation with human in the loop (Sign-Language users)

### Questions
a) Why authors didn't break down the analysis and study across sign and text based languages?
b) Why authors didn't conduct and human evaluation study?
c) What is the impact of speakers diversity, camera angles, etc in the accuracy of the codebook and final results?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper studies sign language translation (sign --> text) with VQ-VAE sign tokenization adapted into a pretrained encoder-decoder language model (Flan T5), on How2Sign and PHOENIX 2014T.

### Strengths
* The method in the paper is presented relatively clearly.
* The experiments look reasonable.

### Weaknesses
At a high level, primarily I am skeptical of the novelty/contribution of the work, and secondarily some aspects of the paper seem unjustified.

* There is a lot of missing related work that undermines the contribution of the paper. For example:
  - There are many prior works that use VQ-VAE for sign language. (e.g., https://arxiv.org/abs/2404.00925 (this one especially), https://aclanthology.org/2024.signlang-1.24/, https://arxiv.org/abs/2208.09141v3)
  - There are many prior works that use "LLMs", even T5, as the pretrained base for sign language translation. (e.g., https://arxiv.org/abs/2306.15162, https://aclanthology.org/2024.acl-long.467/ (which you cited but not recognizing this), https://arxiv.org/abs/2406.06907, https://arxiv.org/abs/2405.04164) This is already a pretty dominating trend in sign language translation research in the last year or two.
* At the same time, I think there is a lot of unnecessary related work, like you don't need to go into details about the history of SLR or pre-Camgoz et al 2018 sign language translation.
* More broadly, the description of contributions in the paper is muddy. On lines 122-131, I would say that (1) and (2) are not novel contributions. I've given you pointers above to prior works that already train the sign language modality into LLMs, and use VQ-VAEs. It's possible there are novel elements to your work in these regards, but they are not articulated here. (3) is I suppose novel but I have more comments on that below.
* I don't see it articulated anywhere why we should prefer discrete tokens as input to an encoder-decoder translation model, rather than soft tokens (which don't impose an information bottleneck), as in many other sign language translation papers (and many multimodal fusion in LLM papers).
* I don't understand the point of RAG here. Retrieval-augmented translation typically retrieves from parallel translation datasets as a way to improve model capacity. RAG instead from knowledge bases is intended to improve factuality, but translation is not a factual task: you can translate sentences that are false. So sure, you could maybe get improvement on sentences that are factual, or when world knowledge might help you guess words by context, but this fails on nonfactual content. Also, how do you know the RAG is even being used, and it isn't just the LLM doing rewriting (or integrating its own knowledge)? It doesn't seem like you ablate LLM rewriting without any retrieved sentences, but I could be misunderstanding.
* I won't count it against you too much since maybe you don't have the resources to use larger datasets or can't use the datasets for license reasons, but there are much larger sign language datasets available (YouTube-ASL, BOBSL) and it is not clear how meaningful results on smaller datasets are. For example, the main downside of using VQ-VAE as an input representation is that you are imposing an information bottleneck, which may be irrelevant when training data is small enough that no results are particularly good.
* I am a bit confused by Table 1. You are excluding numerous works that score better on How2Sign, which I am guessing is because you are trying to compare to works that train on the same amount of sign language data. But it seems misleading to do this and call it "state-of-the-art" without explaining this, especially because SLTUNet trains on extra sign language gloss data, LLMs might train on sign language gloss data and explanations on the web, etc; this doesn't seem like a principled distinction. Also: where are these How2Sign numbers for prior works coming from? I looked at e.g. SignBERT+ and SLTUNet and neither of the works evaluates on How2Sign. Did you get these from personal correspondence with the authors? Did you reproduce all of these using their methods? The PHOENIX numbers I can see in the original papers.
* There are a bunch of weird claims throughout the paper that aren't justified. For example:
  - 48-49: "These differences, especially in word order, make transcription between the two languages complex": I think you mean "translation" here, not "transcription", but regardless I wouldn't say word order is a primary reason that translation between spoken languages and sign languages is hard. Different spoken languages have different word order and it isn't really an issue. The unique aspects of sign language grammar are related to use of space, non-manual markers, etc. The paper doesn't engage with this anyway, just the multimodal fusion.
  - 233-235: "The two encoders of the sign-tokenizer encode global body movements and detailed hand features, respectively, achieving a comprehensive and precise understanding of sign motion.": I see no evidence in the paper that the tokenizer encodes sign motion comprehensively or precisely. This could be proven by, for example, getting human ratings of the reconstructions from fluent sign language users.
  - 520: "Limitations: VRG-SLT still struggles with the contextual and cultural nuances of sign languages." This is a massive understatement; models that get ~8 BLEU on How2Sign are extremely poor quality in absolute. They are nowhere close to context or cultural nuances being the main limitations.

### Questions
These are essentially written in Weaknesses above, but some additional questions:

* Could you provide examples of outputs before and after "RAG" LLM rewriting? Like when is a relevant sentence ever retrieved from the ECMWF weather dataset? It seems like this could only possibly help if your translation draft is something like "On September 12, 2007, the weather in Cologne was [X]" and your knowledge base has memorized the weather.
* Could you elaborate on what "w/o RAG", " pre-SignLLM", and "post-SignLLM" mean precisely in Table 2d?
* Figures 2, 3, and 4 are misleading in that they show the sign language input to the encoder model as image frames. But line 407 says that they are actually keypoints (derived from what model?).

### Soundness
2

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
The paper presents VRG-SLT, an innovative framework for translating sign language into spoken language, aiming to facilitate communication between signing and non-signing communities. The key contributions of the paper are:

VRG-SLT Framework: The authors introduce a two-stage pipeline that utilizes a hierarchical VQ-VAE (Vector Quantized Variational Autoencoder) to convert continuous sign sequences into discrete representations called sign codes. These codes are then aligned with text using a fine-tuned pre-trained language model (FLAN-T5). The framework also employs a Retrieval-Augmented Generation (RAG) strategy to enhance the language model's output with relevant factual knowledge, improving the accuracy and coherence of the generated text.

Sign-tokenizer: A novel component that captures both overall upper body and hand trajectory characteristics using a hierarchical structure. This allows for a comprehensive understanding of sign language gestures.

Integration of RAG: The incorporation of RAG enables the retrieval and combination of relevant knowledge to refine the initial translations, addressing issues like "hallucination" (producing inaccurate or unrealistic responses) in large language models.

### Strengths
Innovative Framework: although VQVAE has been widely adopted in computer vision area, the application to sign laugnage translation is a contribution of the paper. Furthermore, it integrats a hierarchical VQ-VAE with a pre-trained language model (FLAN-T5) and a Retrieval-Augmented Generation (RAG) strategy, the framework addresses the complexities of translating sign language into spoken text effectively.

Well-Written: readers could easily follow the story and understand how to reproduce the paper.

### Weaknesses
1. While the paper acknowledges the challenge of data scarcity in sign language, it primarily focuses on developing a model to mitigate this issue rather than addressing the issue from data perspective. I admit that the model improvement will sightly benefit the end-to-end performance, but I believe the final solution for the task is data augmentation or self-supervised learning.

Looking back at the history of machine translation, the most effective methods have been back translation, pivot-translation (data augmentation), and self-supervised learning (GPT series models). While various methods have been proposed to address data sparsity from a modeling perspective, they remain theoretical solutions rather than definitive answers to the problem or adopted by industry.

2. When we look at the performance, the paper misses some recent baselines (e.g. https://arxiv.org/pdf/2211.01367) and the improvement over these baselines are limited.

Overall, although the paper is well-written, it is unlikely to revolutionize sign language translation.

### Questions
When using RAG (Retrieval-Augmented Generation) in the framework, can you guarantee that the retrieved content maintains the original meaning of the sentences?  I think  the retrieved content might be semantically similar but not exactly matching the intended meaning, leading to subtle shifts in meaning during generation.

### Soundness
3

### Presentation
3

### Contribution
2
