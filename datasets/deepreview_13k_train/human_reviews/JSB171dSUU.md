# Efficiently Democratizing Medical LLMs for 50 Languages via a Mixture of Language Family Experts

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Adapting medical Large  Language Models to local languages can reduce barriers to accessing healthcare services, but data scarcity remains a significant challenge, particularly for low-resource languages. To address this, we first construct a high-quality medical dataset and conduct analysis to ensure its quality. In order to leverage the generalization capability of multilingual LLMs to efficiently scale to more resource-constrained languages, we explore the internal information flow of LLMs from a multilingual perspective using Mixture of Experts (MoE) modularity. Technically, we propose a novel MoE routing method that employs language-specific experts and cross-lingual routing. Inspired by circuit theory, our routing analysis revealed a \textit{``Spread Out in the End``} information flow mechanism: while earlier layers concentrate cross-lingual information flow, the later layers exhibit language-specific divergence. This insight directly led to the development of the Post-MoE architecture, which applies sparse routing only in the later layers while maintaining dense others. Experimental results demonstrate that this approach enhances the generalization of multilingual models to other languages while preserving interpretability. Finally, to efficiently scale the model to 50 languages, we introduce the concept of \textit{language family} experts, drawing on linguistic priors, which enables scaling the number of languages without adding additional parameters.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the challenge of adapting medical large language models (LLMs) to low-resource languages, where data scarcity hinders equitable access to healthcare information. 
The authors construct a high-quality medical dataset covering 12 languages and develop a novel approach to model scalability using Mixture of Experts (MoE) modularity and a new routing method. 
Their analysis reveals a “Spread Out in the End” information flow mechanism, where cross-lingual information is focused in early model layers but diverges into language-specific pathways in later layers. 
This insight leads to the development of the Post-MoE architecture, which applies sparse routing in later layers to enhance model generalization and interoperability. 
Furthermore, by introducing "language family" experts, the model efficiently scales to 50 languages without adding extra parameters, making it both scalable and efficient for multilingual medical applications.

### Strengths
* This paper tackles the crucial issue of reducing language-related barriers to healthcare access for minor languages through LLMs.

* This paper proposes an intuitive and effective MoE approach for supporting multiple languages within a single MoE model.

* This paper provides an analysis of the inner flow of MoE gating.

* The experimental results are encouraging within the evaluation framework applied in this paper.

### Weaknesses
 * The core idea of the proposed method does not appear particularly novel, as it resembles a combination of BTX and Sperse Upcycling, as discussed in the related work section.

* Although the results of the proposed method are consistently better than those of the baseline models with similar model sizes for dense models, MoE models have more parameters than the baseline dense models. Therefore, it may be unfair to directly compare the results between the baseline dense model and the MoE model with the same base model size. The authors should also provide results for dense models with model sizes comparable to those of the MoE models obtained by the proposed method.

* The proposed method's best results, namely, an average accuracy of 69.9 for major languages and 58.3 for minor languages, as shown in Table 5, do not seem significantly better than the "dense" baseline, which achieved 69.0 and 55.7, respectively. Since I'm not familiar with the evaluation dataset used in this paper, I wonder if the differences of 0.9 and 2.6 for major and minor languages, respectively, are meaningful enough to consider.

### Questions
* According to Figure 2, Does the base model for the proposed method use a post-normalization Transformer instead of a pre-normalization one?


* This paper claims, "A major obstacle is the scarcity of medical data in many languages, limiting model development for underrepresented populations." According to Table 4, the average accuracies of major and minor languages among 50 languages in GPT-4o are 85.7 and 81.1, respectively. It appears that the performance of minor languages is not significantly worse compared to major languages in recent top models. This result seems to contradict the situation described in the paper. Do the authors provide any other explanation for the motivation behind developing the proposed method?


* The proposed method's best results, namely, an average accuracy of 69.9 for major languages and 58.3 for minor languages, as shown in Table 5, do not seem significantly better than the "dense" baseline, which achieved 69.0 and 55.7, respectively. Since I'm not familiar with the evaluation dataset used in this paper, I wonder if the differences of 0.9 and 0.6 for major and minor languages, respectively, are meaningful enough to consider.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper tries to extend medical LLMs into different languages. The authors constructed a high-quality medical dataset and proposed a novel MoE routing method that employs language-specific experts and cross-lingual routing. The intuition of extending LLMs into different languages is very important, and the dataset is useful in the community. 
Several concerns about this research:
1. The paper focused on the medical LLMs, while the evaluation is based on MMLU; although it includes part of the medical-related tasks, the evaluation on this general domain dataset will bring additional noise on evaluating LLMs in medical tasks. More experiments on medical-specific benchmarks should be helpful to demonstrate the contribution of the medical dataset. Otherwise, we can only see the constructed dataset can contribute to the general domain but not specifically to the medical domain.
2. Much relevant research on extending pre-trained models to different languages is overlooked in this paper (related works). For example,  "GreenPLM: Cross-Lingual Transfer of Monolingual Pre-Trained Language Models at Almost No Cost, IJCAI 2023" explores a simple way to extend LLMs to different languages. It would be better to compare the proposed method with other language extension methods.

### Strengths
This paper tries to extend medical LLMs into different languages. The authors constructed a high-quality medical dataset and proposed a novel MoE routing method that employs language-specific experts and cross-lingual routing. The intuition of extending LLMs into different languages is very important, and the dataset is useful in the community.

### Weaknesses
Several concerns about this research:
1. The paper focused on the medical LLMs, while the evaluation is based on MMLU; although it includes part of the medical-related tasks, the evaluation on this general domain dataset will bring additional noise on evaluating LLMs in medical tasks. More experiments on medical-specific benchmarks should be helpful to demonstrate the contribution of the medical dataset. Otherwise, we can only see the constructed dataset can contribute to the general domain but not specifically to the medical domain.
2. Much relevant research on extending pre-trained models to different languages is overlooked in this paper (related works). For example,  "GreenPLM: Cross-Lingual Transfer of Monolingual Pre-Trained Language Models at Almost No Cost, IJCAI 2023" explores a simple way to extend LLMs to different languages. It would be better to compare the proposed method with other language extension methods.

### Questions
Typo: "shwows"

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
3

### Summary
The paper introduces a method to expand medical language models to cover 50 languages, focusing on those with limited data. Instead of scaling by adding experts for each language, the authors group languages into families, using shared experts to keep the model size manageable. They identify a key insight: early model layers handle cross-language information, while later layers focus on individual languages. 

Based on this, they propose a design that only applies sparse routing in the final layers, enhancing efficiency. Experiments show the model works well across both major and minor languages, suggesting it could improve access to medical information in diverse languages without requiring excessive data or computational costs.

### Strengths
Comprehensive experiments are conducted across models with varying parameter sizes (0.5B, 1.5B, and 7B), demonstrating scalability and superior performance among major languages.

The “Spread Out in the End” phenomenon is well-motivated and appears relevant for improving both interpretability and efficiency in multilingual models.

### Weaknesses
Although the MoE model's efficiency is emphasized, a more extensive comparison with the same computation cost dense models (especially regarding computational cost and training efficiency) could strengthen the claims.

The improvement mostly appears in Italian and French, also decreased in many more low-resource languages. This seems to lead to some overclaim... how is the data-mixture determined?

line 124: employing Google Translate to translate the questions and answers of MMLU - why not use mmmlu from OpenAI?

Have any experiments been conducted to assess the robustness of translations used for low-resource languages? If not, how do you propose to validate the accuracy of these translations, given the potential consequences in a medical context?

Fig 3b is really hard to read

#params is more appropriate and apple-to-apple comparison with same active parameters comparing to dense models?

### Questions
Fig 3b is really hard to read

 #params is more appropriate and apple-to-apple comparison with same active parameters comparing to dense models?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the authors detail with great precision the training procedure of their Mixture-of-Language-Family-Experts LLM for the medical domain, which combines several existing techniques in a novel way. The authors balance the benefits of cross-lingual learning (making sure low-resource languages benefit from knowledge only written in high-resource languages) with the curse of multilinguality (cross-lingual contamination of linguistic structures) using linguistic experts which always activate for their respective language but can also activate for other languages at the router's discretion, thereby ensuring that sentences in the train set benefit multiple languages simultaneously without impacting all aspects of every other languages. An evaluation is carried for 12+ languages (up to 50 in the scale-up experiments).

### Strengths
- Extensive and multi-layered analysis of cross-lingual pollination and the various trade-offs involved both during training and at inference time.
- High-quality design choices informed by serious and well-informed model analyses.
- Well-structured and information-rich paper.
- On top of that: an impressive new model for the medical domain.

### Weaknesses
 -  Evaluation is performed on translated test sets, generated by other language models.
-  Little discussion is made of the risk of test set contamination in the training set of the model in languages other than the source language. The 64 token overlap used breaks down once the input data is multilingual, since translations have no or minimal token overlap.
- Most techniques presented in the paper do not appear to be very novel, even though their combination seems to be, and their choices are well-justified. Still, it's sometimes tough for me to determine whether this is really an academic work or just a high-quality engineering report written in paper form.

### Questions
- [addressed] Considering that the language specialization of LLMs at the top and bottom layers was an arealdy-known phenomenon by early 2024 (e.g. "Do Llamas Work in English? On the Latent Language of Multilingual Transformers" or "How do Large Language Models Handle Multilingualism?"), do you still perceive that your "Spread Out in the End" analysis is bringing novel insights? In general, could you help me perceive the theorical aspects of your other contributions which I may have missed?
- [addressed] Did you release your multilingual test set to enable other works to evaluate against yours?
- [addressed] Do you intend to release your training data to facilitate replications of this work?
- What role does relative importance of languages play in the linguistic family grouping? English is likely overshadowing other languages using the same expert.
- [addressed] How did you choose your 50 languages? Moreover, why did you include Latin in your experiments? It's no longer an active language of science since many centuries, and Google Translate is unlikely to do a good job on modern medical documents in this case.

Not technical but still relevant:
- [addressed] Why do you want to present this work at ICLR? As a first-time ICLR review, I cannot make judgements about what type of works usually make an impact at ICLR, so I will leave this up to the AC Meta-Review. I will however raise my concern that this work doesn't seem to have a particularly strong tie to Representation Learning. It's also not particularly analytical or theoretical. While I personally would be very excited to discuss this further with the authors, I'm surprised to see this type of work submitted to ICLR instead of EMNLP or COLM. However, I see that ICLR also includes general machine learning as an accepted topic, so it's really difficult for me to judge this, and I won't. But I think the answer to this question might be helpful for the meta-reviewer.

### Soundness
4

### Presentation
4

### Contribution
3
