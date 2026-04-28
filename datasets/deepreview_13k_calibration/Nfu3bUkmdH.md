# Democratizing LLMs for Low-Resource Languages by Leveraging their English Dominant Abilities with Linguistically-Diverse Prompts

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 6, 5

## Abstract
Large language models (LLMs) are known to perform tasks by simply observing few exemplars. Moreover, competent generative capabilities of LLMs are observed mostly in high-resource languages, while their performances among under-represented languages fall behind due to pre-training data imbalance. To elicit LLMs' ability onto low-resource languages without any supervised data, we propose to assemble synthetic exemplars from a diverse set of high-resource languages. These prompts can directly induce generative capabilities in low-resource languages and serve as intra-lingual exemplars to even improve tasks in these languages. Our unsupervised prompting method performs on par with supervised few-shot learning in LLMs of different sizes for translations between English and 34 Indic and African languages, and surpasses supervised prompting in non-English tasks. The method also significantly improves low-resource performances in many other intra-lingual tasks like summarization (XLSum), question answering (XQUAD \& TydiQA) and conversational instruction following (Sea-Bench).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper the authors tried to improve the LLMs performance on low-resource languages by creating synthetically diverse prompts in high resource languages. The authors show the effectiveness of their approach in translation and summarisation tasks.

### Strengths
It is an interesting approach to get good performance on Low-Resource set up. The experiments are promising.

### Weaknesses
The results seems promising. The authors should provide more details about:

(a) How the diverse language sets are selected? Do they observe any correlation on linguistically similar language selection vs a random set of languages?

(b) Did they study the relation of number of languages to be selected and number of examples in the prompt?

(c) Were the prompt set fixed for every test instance?

Also, it would be interesting to see the performance difference of selecting prompts from diverse languages vs creating synthetic prompts for just the pair of languages of interest.

### Questions
The paper would be sound if the authors can explain / provide experimental evidences on prompt selection as pointed out in the previous section.

### Soundness
2 fair

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
This paper introduces ”linguistically diverse prompting” (LDP), a method aimed at improving prompt-based generative task performance in languages for which there are no available few-shot exemplars. In this method, few-shot in-context learning is enabled through leveraging in-context exemplars from various (higher-resource) languages to ”locate the task”. The authors find that their approach achieves at least comparable performance w.r.t. supervised methods for translation and multilingual summarization.

### Strengths
1. The presented method is well-motivated by the observations from the literature and addresses a concrete problem in low-resource NLP (i.e. lack of in-context exemplars for some languages).

2. Evaluation is rigorous and the analyses (section 4.4) provide valuable insights for this line of research.

### Weaknesses
Summary of Weaknesses

1) Flawed linguistic diversity: this paper claims linguistic diversity mainly on the basis of selecting languages with different scripts: ”to ensure diversity … characters are used” (page 1). However, this is not done systematically (the authors ”include various script types” and later mention ”dissimilar lexical and regional characteristics” but do not explain the exact selection process). Moreover, this misses important aspects of linguistic diversity that are captured by for instance taking into account phylogeny. A more rigorous approach would involve using established linguistic distance metrics or phylogenetic trees to select languages that are truly diverse, rather than relying on script differences which can be superficial. For example, languages using the Latin script can still be quite diverse in terms of syntax and semantics, while languages with different scripts might share common ancestry or have undergone significant borrowing, thus reducing their effective diversity.

2) This paper has reproducibility issues. The results in the paper cannot be replicated, as the approaches are evaluated on 200 randomly sampled sentences from the test set, while there is no explanation or source provided that details which sentences are included or how to reproduce this selection (e.g. which random seed). Random data selection is also used in one of the baselines, namely supervised prompting (A.2) without providing details. The lack of a specific random seed or a deterministic method for selecting the 200 sentences makes it impossible to reproduce the reported results. This is a critical issue, as it undermines the validity of the experimental findings. Furthermore, the random selection of prompts for the supervised baseline also needs to be made reproducible by specifying the random seed used.

### Questions
1. Is LDP truly an unsupervised prompting method, or are some aspects more like obtaining data for a kind of weak supervision?

2. What are your criteria for distinguishing high-resource from low-resource languages?

3. In what way does improving prompting performance for certain low-resource scenarios ’democratize’ LLMs (title)?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper suggests employing back-translation for few-shot, in-context learning of machine translation for low-resource languages. Initially, synthetic examples are generated by instructing the model to translate into English, utilizing few-shot, in-context learning with a variety of examples.

### Strengths
The idea is simple to follow and the author tested the idea across diverse set of languages. They also show improvement compared to some baselines.

### Weaknesses
A major weakness in this work is that the author essentially reintroduces the concept of back-translation, a well-established technique in machine translation. Yet, this paper does not make any reference to the original, popular back-translation work by Sennrich in 2016, which raises questions about the author's familiarity with prior research and the potential reinvention of existing concepts.

The primary distinction is that it is now presented in the form of a few-shot in-context learning, rather than for training purposes. One of the proposed comparisons involves fine-tuning using synthetic data in the opposite direction, which basically is the original back-translation concept. The absence of this reference is significant because it represents the core idea of this paper. See also my 2nd question.

The synthetic back-translation data was generated by providing in-context examples across a diverse set of languages (Figure 1a). However, I believe that this crucial idea is not thoroughly explored, considering the potential variability in the types of languages, examples, diversity that could be explored. Conducting an ablation study involving different examples and languages would strengthen the paper's claims. Also, while the author comments that LDP method (Figure 1c) is superior to the standard few-shot approach (Figure 1b), there is a lack of experimental results to substantiate this claim.

### Questions
- Is there any specific reason on choosing BLOOM over BLOOMZ (instruct-tuned version of BLOOM)? I think it will be more fair comparison vs InstructGPT.

- One of the strengths of the original back-translation approach lies in its ability to generate synthetic data at scale, and the size of the generated data can influence performance. However, I am uncertain about the data size used for your fine-tuning comparison.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
