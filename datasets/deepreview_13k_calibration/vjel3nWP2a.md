# Scalable Extraction of Training Data from Aligned, Production Language Models

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6, 8, 6, 6

## Abstract
This paper studies \emph{extractable memorization}:
    training data that an adversary can efficiently extract
    by querying a machine learning model without prior knowledge of the training dataset.
    We show an adversary can extract gigabytes of training data from
    open-source language models like Pythia or GPT-Neo,
    semi-open models like LLaMA or Falcon,
    and closed models like ChatGPT. 
    Existing techniques from the literature suffice to attack
    unaligned models; in order to attack the aligned ChatGPT, we develop a new
    \emph{divergence} attack that causes the model to diverge from its chatbot-style generations and emit training data at a rate $150\times$
    higher than when behaving properly.
    Our methods show practical attacks can recover far more
    data than previously thought, and 
    reveal that current alignment techniques 
    do not eliminate memorization.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper provides a pioneering study on scaled evaluation of training data memorization issues in aligned Large Language Models (LLMs). The paper effectively defines memorization as the generation of at least 50 tokens that match training data. The authors created AUXDATASET, a 10-terabyte dataset merging four of the largest published language model training datasets, enabling systematic evaluation of the lower bound of training data memorization.

The study focuses on three aligned models (with 9 open-weight non-aligned models as baselines). GPT-3.5-Turbo/Gemini 1.5 Pro was primarily studied under prompt-based divergence attacks, while both GPT-3.5-Turbo and GPT-4, along with Llama-2-chat, were evaluated using fine-tuning-based divergence attacks to remove chatbot-like behaviors for better assessment.

The authors discovered that their divergence attacks (causing deviation from typical chatbot behavior) significantly increased the success rate of extracting memorized content from potential training data. Qualitatively, they identified memorization issues in OpenAI models, including OpenAI's proprietary data not released to the public, copyright-protected content from The New York Times, toxic content, and private information.

### Strengths
- The paper addresses a critical problem in LLM development with robust methodology. The authors establish a formal framework by providing a clear definition of memorization (i.e., >50 tokens), creating a comprehensive validation corpus, and presenting results as quantifiable lower bounds on memorization issues.

- The technical innovation in attack methods is compelling (**but might only be one correlated aspect of memorization as it seems the divergence attacks are solely effective to GPT models, see weakness**). The authors propose two effective approaches: a prompt-based method utilizing word repetition to elicit divergent behavior (**which seems to have been fixed by OpenAI**), and a more sophisticated fine-tuning-based divergence attack. Both methods successfully demonstrate how to bypass chatbot-like behaviors to expose memorization from OpenAI models.

- The empirical analysis is thorough and well-structured. The study reveals interesting correlations between memorization and model size and introduces meaningful metrics such as unique 50-grams for measurement. The large-scale evaluation of 10 terabytes of data provides robust evidence for their findings.

- The findings from OpenAI models are compellingly grounded in practical implications, demonstrating memorization of sensitive content including The New York Times' copyrighted material, toxic content, personally identifiable information (PII), and OpenAI's unreleased training data. This connection to real-world concerns enhances the paper's significance.

- The paper is well-structured and clearly written, effectively communicating complex concepts and findings. The logical flow and organization of ideas contribute to its accessibility and impact.

### Weaknesses
The paper's primary limitation lies in the generalizability and effectiveness of its proposed divergence-based attacks. While innovative, several concerns emerge:

1. Limited Applicability:
The prompt-based divergence attack has already been largely addressed by OpenAI and shows limited effectiveness beyond GPT-3.5-Turbo. Similarly, the fine-tuning-based divergence attack demonstrates reduced effectiveness on Llama-2-Chat, suggesting these methods might be model-specific rather than universal. The fine-tuning approach, while more robust than the prompt-based method, still appears to be highly sensitive to the specific architecture and training regime of the target model. This raises concerns about whether the observed memorization is a general property of LLMs or an artifact of the specific models and attack methods used.
2. Correlation Concerns:
The relationship between divergence behavior and memorization is not strongly established. The paper would benefit from a deeper analysis of this correlation, as the current results suggest the connection might be specific to OpenAI's training process rather than a general phenomenon across different LLMs. It is unclear if the divergence attacks are merely revealing memorization or if they are actively inducing it by forcing the model to operate in an unusual regime. The paper lacks a thorough investigation into whether similar memorization patterns can be observed without inducing divergence.
3. Methodological Limitations:
The heavy reliance on divergence-based attacks as the primary mechanism for revealing memorization might provide an incomplete or potentially misleading picture of the actual memorization behavior. The study does not explore other potential attack vectors, such as targeted prompt engineering or adversarial examples, which could reveal memorization in different ways. The exclusive focus on divergence attacks limits the scope of the analysis and may not capture the full spectrum of memorization vulnerabilities.

### Questions
- Could the authors elaborate additional analysis in the main text on why the divergence-based attacks show varying effectiveness across different models?

- Have you explored alternative attack methods (beyond divergence-based attacks) that might be more universally effective across different LLMs? I wish to learn the authors' thoughts on this. 

- Can the authors provide additional analysis over cases where memorization occurs without divergence?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper highlights that, despite alignment, large language models still have potential risks of leaking training data. The authors introduce two novel attack techniques, the divergence attack and the finetuning attack, to bypass alignment safeguards. The methods successfully extract thousands of data samples from models like OpenAI's ChatGPT and Google's Gemini.

### Strengths
Originality & Significance: This paper provides valuable insights into the limitations of current alignment methods in reducing the risk of training data extraction. The proposed extraction methods are both highly scalable and cost-effective. 
Clarity: The paper is well-structured and easy to follow, with clear and detailed descriptions of the experiments.

### Weaknesses
The paper contains experimental details and some analysis of how model capacity influences memorization. The analysis is more empirical than theoretical and lacks a detailed theoretical examination of why model capacity correlates with memorization in this way.

### Questions
See weakness.

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
4

### Summary
This paper compares pretrained base models and aligned production models using a simple completion attack to extract training data. The findings indicate that the alignment process appears to prevent models from directly outputting training data when faced with this straightforward attack.
To bypass the defense mechanisms introduced by alignment, the paper proposes two novel techniques for extracting training data from aligned production LLMs: the divergence attack and the fine-tuning attack. In the divergence attack, the model is prompted to perform a repetitive task, such as repeating a specific word. This can lead the model to deviate from the original task and potentially output training data. The fine-tuning attack involves fine-tuning the model with a completion task similar to the initial completion attack, using a set of 2,000 data points.
To quantitatively assess the effectiveness of these techniques, a 10TB text dataset was constructed as the ground truth for training data comparison. The results demonstrate that the divergence and fine-tuning attacks were able to extract training data from ChatGPT at rates of 3% and 23%, respectively.
In addition to extracting training data, these attacks also induced the model to produce harmful content.

### Strengths
- This paper underscores an important problem that current alignment techniques do not fully mitigate risks of extracting training data from LLMs.
- This paper demonstrates the successful extraction of training data from production models in significant quantities and at a feasible cost.
- This paper introduces a large dataset and a searching algorithm to act as a proxy for unknown training datasets and help matching the data.

### Weaknesses
 - The divergence attack causes the model to output training data as part of its response. An additional step is needed to compare different parts of these responses with the training dataset to verify extraction. The success rate of these attacks remains limited as well. These show a gap between successfully extracting unknown training data and performing an attack similar to the membership inference attack. Specifically, while the divergence attack extracts 1000 tokens, only a small fraction (e.g., ~50 tokens) are identified as training data, which significantly lowers the effective extraction rate. The paper lacks a discussion on the probability of accurately extracting these smaller chunks of training data when the training dataset is unknown, making the attack's practical success unclear.
- While testing baseline attacks on 9 open base models, the paper only tests baseline attacks on one aligned model, GPT-3.5. It requires testing on more aligned models to support the claim.
- The divergence attack proves effective only on ChatGPT and does not transfer to other models, such as Gemini. This raises concerns about the generalizability of this attack and its applicability to a wider range of aligned models.
- The finetuning attack has been evaluated solely on LLaMA-2-chat and ChatGPT, despite the existence of many new aligned open-source models that could be used to further assess the attack's effectiveness. The results from LLaMA-2-chat indicate limited effectiveness and the transferability limitations of the attack.

### Questions
- Conduct more experiments for baseline attacks on more aligned models to support the conclusion---"Baseline attacks fail against aligned models".
- Conduct more comprehensive experiments with more and newer models for the finetuning attack.
- Estimate the probability of extracting the training data part from the whole response assuming the training data is unknown.
- Minor problems:
  - line 071: the broken symbol before "10,000 examples"
  - Figure 2 is never mentioned in the main text.

### Soundness
3

### Presentation
2

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
This paper pointed out the key reasons of the ineffectiveness of the model alignment and developed two novel techniques to circumvent chatbot alignment guardrails: a divergence attack and a finetuning attack.  The author demonstrated that this is the first large-scale, training-data extraction attacks on proprietary language models using only publicly-available tools and relatively little resources. This work highlights the limitations of existing safeguards to prevent training data leakage in
production language models. And the experiment results show the model alignment is not enough to prevent memorization.

### Strengths
1. The contributions are valid and significant. This work highlighted the limitations of existing safeguards to prevent training data leakage in
production language models. The author proposed two novel extraction attacks illustrating the limitation of model alignment of training-data extraction. The attacks only require access to tools that are publicly accessible to everyone. In addition, the author proposed a scalable approach to validate memorization. 

2. The paper does a comprehensive research showing additional work in long Appendix with sufficient experiments. 

3. The paper has good structure by clarifying key definitions and prompting the motivation. In experiments, the author clearly described the scalable approach for validating memorization and what are the production language models, including both aligned, conversational models and instruction-tuned, non-conversation models.

### Weaknesses
1. (not a weakness but a suggestion). During the reading, I found some figures and conclusions in the Appendix is helpful and may worthwhile to be added or replaced to the main body. For example, Figures in Appendix A.9

2. In section 7 QUALITATIVE ANALYSIS OF EXTRACTED TEXT, it seems the result analysis focuses on the length of the extracted string and memorized text. It may better if the author could add more explanation in terms of the leakage of random training data from divergence attack vs the leakage of specification training data from fine-tuning attack. Specifically, a more detailed analysis of the semantic content and the nature of the leaked information would be beneficial. For instance, are the extracted texts from the divergence attack primarily composed of common phrases or do they reveal more sensitive or unique data points? Similarly, for the fine-tuning attack, does the extracted text consistently align with the specific fine-tuning data, or does it also include unrelated memorized content? A deeper dive into the types of information leaked by each attack would strengthen the analysis.

### Questions
1. [line 047] It said they apply divergence attack to ChatGPT and Gemini but apply finetuning attack to ChatGPT only. Is there a particular reason why they doesn’t apply finetuning attack to Gemini?

### Soundness
4

### Presentation
4

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
This paper considers two approaches to extract a large language model's training data. The first is using repeated words, and the second is by fine-tuning the model to break the safety training. The approach is tested on proprietary models, and shown to regenerate sentences from the open source datasets with verbatim tokens over a threshold. While the first approach does not always work, fine-tuning could easily circumvent the defense mechanism put in the model.

### Strengths
- S1: The approaches are simple and effective without too many assumptions.
- S2: The attacks are shown to work on the state-of-the-art commercial models.
- S3: The presentation is good overall and the paper is very easy to read.

### Weaknesses
 - W1: The related work section is missing. Although there is the background section, the paper does not properly cover the related work and its relation to the existing work, as well as potential defenses in the literature. Especially, these attacks are known and discussed in different forums. There is a potential that the authors of the paper might be those who suggested and discussed these approaches early on, but some mention of the context is useful understanding the literature and the significance of this approach.
- W2: The paper defers a lot of information to the appendix. Although this abundance of information comes from the thorough analysis and investigation, the paper needs to prioritize more essential information and drop potentially duplicate or obvious information.

### Questions
- Q1: What are the examples of the (near) duplicate generations and their significance?

The paper is overall well written and the extensive analysis is helpful, the paper can be improved with better use of prioritization in space, and a proper related work section. Especially, discussing how novel the proposed approach would be helpful understanding the impact of this paper. This might need a significant reorganization of the paper, but all the ingredients should be already there. If that can be done, I'm willing to upgrade my recommendation.

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper conducts a large amount of empirical research and finds that aligned chat models hardly leak training data. However, when the authors implemented the divergence attack and fine-tuning attack, the models leaked some training data, demonstrating significant security vulnerabilities in current large language models. The paper conducted a large number of experiments to validate the various negative effects on the model after being attacked.

### Strengths
- The paper conducted a large number of experiments to reveal the extraction attacks faced by large language models, and the models used in the experiments are very representative.
- The research problem addressed in the paper is very interesting; extraction attacks are an important topic for large language models.
- The structure of the paper is very well-organized, with rich details such as explanations and definitions for memorization, making it easy to read.

### Weaknesses
 - I think that the paper lacks innovation or technical contribution. Although the two attack methods proposed in the paper reveal security issues with large language models, I think such contributions may not be sufficient for a top conference like ICLR.
- The divergence attack proposed in the paper is intriguing, but why does this attack work? Under what circumstances does it work? It seems that this attack may not enable targeted attacks (i.e., leaking specific information from the model). There appears to be a significant random component, which means that the efficiency of this type of attack may be low for the attacker.
- It seems that the authors did not discuss the relationship with related works. Some adversarial attacks also seem to achieve similar effects. What are the main differences between the authors' work and related works?

### Questions
Please refer to the ``Weaknesses`` part.

### Soundness
3

### Presentation
2

### Contribution
2
