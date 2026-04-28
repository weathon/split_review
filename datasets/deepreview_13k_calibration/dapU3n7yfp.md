# Automatically Eliciting Toxic Outputs from Pre-trained Language Models

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
Language models risk generating mindless and offensive content, which hinders their safe deployment. Therefore, it is crucial to discover and modify potential toxic outputs of pre-trained language models before deployment. In this work, we elicit toxic content by automatically searching for a prompt that directs pre-trained language models towards the generation of a specific target output. Existing adversarial attack algorithms solve a problem named reversing language models to elicit toxic output. The problem is challenging due to the discrete nature of textual data and the considerable computational resources required for a single forward pass of the language model. To combat these challenges, we introduce ASRA, a new optimization algorithm that concurrently updates multiple prompts and selects prompts based on determinantal point process. Experimental results on six different pre-trained language models demonstrate that ASRA outperforms other adversarial attack baselines in its efficacy for eliciting toxic content. Furthermore, our analysis reveals a strong correlation between the success rate of ASRA attacks and the perplexity of target outputs, while indicating limited association with the quantity of model parameters. These findings lead us to propose that by constructing a comprehensive toxicity text dataset, reversing pre-trained language models might be employed to evaluate the toxicity of different language models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper discusses the challenge of preventing pre-trained language models from generating toxic content. The authors focus on the process of "reversing" language models to intentionally produce such content, which serves as a test to identify and mitigate potential risks before deployment. They present ASRA (Auto-regressive Selective Replacement Ascent), an optimization technique designed to efficiently elicit toxic output from language models. ASRA works by updating multiple prompts simultaneously and using a determinantal point process to select the most effective ones. The algorithm was tested on six different language models, and the results showed that ASRA surpasses other adversarial attack methods in terms of eliciting toxic content. Additionally, the research found a significant link between the success of ASRA and the perplexity of the generated output, with less connection to the language models' size. The findings suggest that reversing language models with a comprehensive dataset of toxic text can be a strategic method for evaluating and improving the safety of language models.

### Strengths
- This paper proposes a novel method of textual adversarial attack for generation tasks, which looks generalizable for different text generation tasks.
- The empirical results look convincing, outperforming the baselines by a large margin
- This paper focuses on AI safety, which is an important topic recently regarding safeguarding the output of LLMs. The authors offer a potential tool for developers to identify and fix vulnerabilities before deployment.

### Weaknesses
 - Lack of baselines: The attack algorithm is based on HotFlip (2018), which is a bit old and less effective than the recently proposed baselines. I am wondering if the authors have compared with adversarial attack baselines proposed more recently such as Seq2sick [1], which shows better optimization effectiveness for text-to-text generation tasks. Specifically, the paper should consider baselines that are designed for generating adversarial examples in text generation tasks, rather than focusing solely on input perturbation methods. The current baselines (GBDA, Autoprompt, ARCA) are not directly comparable, as they are designed for different attack scenarios, such as prompt optimization or input perturbation. A more relevant comparison would involve methods that directly optimize for generating toxic outputs, which would provide a more accurate assessment of ASRA's performance.
- Lack of defense models (detoxified models): While I appreciate the authors’ efforts in comparing different pretrained models, it would also be interesting to evaluate against different defense approaches/detoxification approaches, such as [2,3,4], and confirm whether the attack is still effective. The paper should explore the robustness of ASRA against common defense mechanisms, such as adversarial training or detoxification methods. This would provide a more comprehensive understanding of the practical implications of the proposed attack. Without evaluating against defense models, it is difficult to assess the real-world impact of ASRA, as deployed models are likely to incorporate some form of defense.
- Validity of toxicity evaluation: The authors mention that their evaluation setup “can be applied to bridge the evaluation of toxicity in different PLMs”, and “speculate that the success rate of ASRA attack might be positively correlated with the toxicity of language models.” However, I do not see any evidence about whether the ASR here can be a good proxy to reflect model toxicity. Given that the model toxicity evaluation is conducted by evaluating model responses with a lot of different inputs and contexts, the setup of this paper is to evaluate model responses given “unnatural” prompts. I am thus suspicious about whether the test above can give an accurate evaluation of model toxicity. The paper needs to provide a more rigorous justification for using the success rate of ASRA as a proxy for model toxicity. The current evaluation setup, which relies on adversarial prompts, may not accurately reflect the model's behavior in real-world scenarios with diverse inputs and contexts. A more comprehensive evaluation would involve a wider range of prompts and contexts to ensure that the toxicity evaluation is robust and reliable.
- There is an important concern regarding the potential misuse of this work by malicious users to bypass safety controls of LLMs and elicit model toxicity. I believe it would be valuable for the paper to include a discussion of this aspect.

### Questions
The proposed optimization seems generalizable for different text generation tasks. Have you ever used the approach to attack other text generation tasks (such as [1])?

### Soundness
3 good

### Presentation
3 good

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
The paper presents a reversing PLM approach to generate prompts that lead to toxic outputs. The proposed method consists of an approximation step, a refinement step, and a selection step implemented via a DPP model. Empirical studies with 6 PLMs indicate the effectiveness of the proposed approach. 

Overall, this is an interesting paper with a decent algorithm and compelling results. Minor concerns:

(1) The evaluation sets seem small (a few hundreds of examples), is it possible to report some evaluation results on large datasets?

(2) Normally, it is more important to detect prompts without any malevolent words but leading to toxic responses for a PLM. However, from the cases shown in the Appendix, the prompts found by the proposed method usually contain malevolent words. This may limit the application of the proposed method in practice. Then, is it possible to further improve the method by avoiding malevolent words when reversing PLMs?

(3) Since the algorithm needs to search every word in the vocabulary, when the vocabulary size is big, will the complexity becomes an issue in application of the method?

### Strengths
decent algorithm
compelling results

### Weaknesses
small evaluation sets
complexity could be an issue

### Questions
see the summary

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
With the emergence of LLMs, it is crucial to discover and modify potential toxic outputs before deployment.
In this work, authors propose ASRA, a new optimization algorithm that concurrently updates multiple prompts and selects
prompts based on determinantal point process. Experimental results on six
different pre-trained language models demonstrate that ASRA outperforms other
adversarial attack baselines in its efficacy for eliciting toxic content.

### Strengths
* The experiments show significant perfanmance improvement over previous works.
* The authors provide detailed and insightful analysis about hyperparameter tuning and future application.

### Weaknesses
 * The proposed method seems a little complicated, especially the DPP procedure.  I'd like to know it's speed (e.g. throughput ) compared with 
previous works. 
* Experiments limits on eliciting toxic text of up to 3 words. In practice, however, what we really care about is not generating
toxic text at any length. Therefore I have a concern about this work's transferability to a more practical scenario.

### Questions
* I want to know that could DPP be possibly replaced by other simpler method, e.g. methods often used in document summarization task?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new optimization algorithm for eliciting toxic outputs from pre-trained language models. The authors demonstrate that their algorithm outperforms other adversarial attack baselines in its efficacy for eliciting toxic content. They also show that their approach can be used to identify and mitigate potential risks associated with the deployment of language models in real-world settings. Overall, the paper's contributions include a new optimization algorithm for eliciting toxic content, a demonstration of its efficacy, and insights into the potential risks and benefits of using such an approach in practice.

### Strengths
+ The paper is well-written and clear to read.

+ The idea is novel and the performance improvement is obvious across different settings.

+ Sufficient ablation studies are conducted to support the claim.

### Weaknesses
 - Limited evaluation: The authors only evaluate their approach on a single dataset. This could limit the generalizability of their results and make it difficult to draw broader conclusions about the effectiveness of their approach.

- Limited scope: The paper only focuses on the generation of toxic content from language models and does not address other potential risks associated with their deployment, such as bias or misinformation. This could limit the paper's relevance and impact in the broader context of language model research. 

- Additionally, the paper only tests on 1/2/3-word output, which is not practical. It is unknown whether the proposed method would work for longer toxic outputs.

### Questions
NA

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
