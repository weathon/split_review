# Ward: Provable RAG Dataset Inference via LLM Watermarks

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
Retrieval-Augmented Generation (RAG) improves LLMs by enabling them to incorporate external data during generation. 
This raises concerns for data owners regarding unauthorized use of their content in RAG systems. 
Despite its importance, the challenge of detecting such unauthorized usage remains underexplored, with existing datasets and methodologies from adjacent fields being ill-suited for its study. 
In this work, we take several steps to bridge this gap. First, we formalize this problem as (black-box) RAG Dataset Inference (\emph{RAG-DI}). 
To facilitate research on this challenge, we further introduce a novel dataset specifically designed for benchmarking RAG-DI methods under realistic conditions, and propose a set of baseline approaches. 
Building on this foundation, we introduce \textsc{Ward}, a RAG-DI method based on LLM watermarks that enables data owners to obtain rigorous statistical guarantees regarding the usage of their dataset in a RAG system. 
In our experimental evaluation, we show that \textsc{Ward} consistently outperforms all baselines across many challenging settings, achieving higher accuracy, \mbox{superior query} efficiency and robustness. 
Our work provides a foundation for future studies of RAG-DI and highlights LLM watermarks as a promising approach to this problem.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies the problem of RAG Dataset Inference (RAG-DI), where a data owner aims to detect whether their dataset is included in a RAG corpus via black-box queries. The key difference from the RAG MIAs setup is that the data owner makes a dataset-level decision, instead of a document-level decision as in MIAs.
The authors first introduce a dataset FARAD for the RAG-DI problem, as they believe the previous datasets used in MIAs problems (EnronEmails, HealthcareMagic) are likely contaminated in the training datasets of existing LLMs and lack fact redundancy. The FARAD dataset builds on a recent source of articles with fictional entities and events, and they prompt a set of LLMs (author LLMs) to rewrite articles based on the key points from the source article.

The paper then adapts existing RAG MIAs baselines to this problem and proposes a simple baseline called FACTS that simply prompts an LLM to generate a single question that is only answerable by the document. They find that the FACTS baseline performs well in their easy setting (without fact redundancy) but not in their hard setting (with fact redundancy).

Finally, they propose a new dataset inference method based on LLM watermarking called Ward. The key idea is to paraphrase the articles with a watermarked model from the recent LLM watermarking literature. They show that Ward works well in their hard setting and also meets the desiderata including monotonicity, guarantees, and robustness.

### Strengths
* I believe the paper studies an important and timely research question that has been overlooked in the literature. I am not a domain expert (in the sense of MIA and RAG privacy), so I may not know related work very well.
* I think the paper has made many meaningful contributions, from formulating the problem to collecting the dataset and adapting RAG-MIA baselines, to finally proposing their own approach based on LLM watermarking. The experiments (different LLMs and evaluation settings)  and analyses (hyperparameters, modeling retrieval, and examining the quality of paraphrased texts) are quite thorough too.
* Using LLM watermarking as an approach to solve dataset inference seems a novel and reasonable approach to me. 
* The paper is very well written and self-contained. It is easy to follow the structure of the paper and understand its contributions clearly. I have learned a lot from reading the paper.

### Weaknesses
The major part I am not very sure about is whether the dataset construction and experimental settings can really reflect realistic RAG settings in real-world deployment, since the effectiveness of the baselines and proposed approach all depends on this setting. In particular:
* It assumes perfect retrieval (= only articles from the same source are used) in most experiments. Although the paper discusses a more practical retrieval setting in Section 5.3, I don't see any discussion of previous baselines. For the hard setting, the imperfect retrieval problem should be easier than the perfect retrieval settings (the distracting documents should be less relevant), so the baselines could probably perform better. This is a critical point that needs further investigation, as the assumption of perfect retrieval may not hold in real-world scenarios, potentially skewing the results.
* I am not entirely sure whether the current data generation pipeline can well reflect the redundancy problem in the real world, given that they are all generated from different LLMs (I am also not sure how much impact "additional facts" and "a set of diverse LLMs" have here). It might be too much to ask, but I think having a realistic multi-document summarization setting would be more realistic. The use of LLMs to generate the dataset raises concerns about the artificial nature of the redundancy, which may not accurately represent real-world data redundancy. A more realistic approach, such as using human-generated summaries or naturally occurring redundant documents, would be beneficial.
* I have difficulty understanding the rationale behind the defense prompt. Why would RAG providers want to instruct the models to not answer questions from retrieved documents? How can RAG be effective in this case? If this is from the data owner's perspective, given the goal is to detect whether the dataset is used or not, I don't see why they would want to add such a prompt to make the detection task harder. The purpose of the defense prompt is unclear and seems counterintuitive to the goals of a RAG system. The motivation behind this prompt needs to be clarified, as it appears to hinder the system's ability to effectively utilize retrieved documents.
* [Question] The RAG uses k = 3 shots, but the Easy setting assumes there is only one article per group. Where do the 3 shots come from? The paper also mentions they ablate the choice of k, where k can be {3, 4, 5} in the Appendix. Even for the Hard setting, aren't there only 4 articles per group? Not sure if I misunderstood this. The explanation of the k-shot mechanism is unclear, particularly in the context of the Easy setting where only one article per group is assumed. The source of the additional shots and the rationale behind the choice of k values need to be better explained.

### Questions
See weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents WARD, a novel method for detecting unauthorized dataset usage in Retrieval-Augmented Generation (RAG) systems. The approach formalizes RAG Dataset Inference (RAG-DI) as a problem where data owners seek to identify if their data is being used without permission in RAG systems via black-box queries. The authors introduce a new dataset, FARAD, specifically designed to benchmark RAG-DI under realistic conditions that include fact redundancy. Using LLM watermarks, WARD offers data owners statistical guarantees of usage detection. Experimental results show that WARD outperforms other baselines, demonstrating high accuracy, query efficiency, and robustness across challenging scenarios.

### Strengths
The strengths of this paper are mainly centered around the propose of the new task along with a new specialized benchmark dataset.

1. Novel Problem Definition and Formalization: The paper identifies and formalizes the novel problem of RAG Dataset Inference (RAG-DI), addressing a critical need for data owners to detect unauthorized data usage in RAG systems. This formalization fills a significant research gap and sets the stage for further exploration of secure data usage in RAG contexts.

2. Introduction of a Specialized Benchmark Dataset: By creating FARAD, the authors contribute a valuable dataset that is specifically tailored for RAG-DI research. FARAD’s design ensures realistic conditions for testing, including the incorporation of fact redundancy, making it highly relevant for practical evaluations of RAG-DI approaches.

3. Comprehensive Experimental Validation: The paper’s extensive experiments demonstrate the effectiveness of WARD in achieving high true positive rates with no false positives across various settings, underscoring the method's robustness and accuracy. This comprehensive validation strengthens the credibility of WARD as a reliable solution for detecting unauthorized data use in RAG systems.

### Weaknesses
Although this paper has the above strengths that are interesting, I also noticed several weaknesses that should be further considered.

1. Application Scenario. The authors propose a novel problem definition, namely RAG Dataset Inference (RAG-DI). The concept is quite straightforward, and one has to admit that the concern indeed exists in practice. However, it is still less discussed in this paper, that how often this type of problem can occur in realistic scenarios. I am concerned with the application range of this work. For example, if a person is concerned with their own data being used for LLMs, do they need to test all LLMs in the market? This could be prohibitive. 

2. Lack of Computation Complexity. The authors proposed a novel method to deal with the specific problem of RAG-DI. However, the complexity is not fully discussed in the paper. As a result, the problem of scalability could be severe. For example, the owner has an excessively large dataset, will the method still work?

3. Countermeasures: Although the authors considered the scenario where the RAG provider attempts to prevent the unintended use of the system, they do not provide a detailed discussion of the possible countermeasures that the RAG provide may use to counteract the watermarking of data. As there are multiple existing techniques against watermarking, the discussion about vulnerability of the proposed framework when faced with these countermeasures could be inspiring

### Questions
How can this framework be applied to realistic scenarios?

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
3

### Summary
This paper focuses on the problem of unauthorized use of datasets in Retrieval-Augmented Generation (RAG) systems and formalizes it as the RAG Dataset Inference (RAG - DI) problem. To address this issue, the authors propose the FARAD dataset specifically designed for RAG - DI evaluation and a series of baseline methods. They also introduce the WARD method based on LLM watermarks. Experiments demonstrate that WARD outperforms the baseline methods in terms of accuracy, query efficiency, and robustness.

### Strengths
1. The RAG - DI problem is formally defined, filling the research gap in this field and laying a foundation for subsequent research.
2.The design of the FARAD dataset takes into account the practical application scenarios of the RAG system and avoids the shortcomings of existing datasets in RAG - DI research, such as the possibility of being used for LLM training and the lack of fact redundancy.
3.The WARD method is based on LLM watermarks and can provide data owners with strict statistical guarantees regarding the use of their datasets in the RAG system. It exhibits excellent performance in various experimental settings and outperforms all baseline methods.

### Weaknesses
1. In real-world applications, RAG systems may face more complex situations, such as multilingual environments and data from different domains. The discussion in this regard in the paper is relatively limited.
2. There is a lack of discussion on the efficiency of the solution.

### Questions
1. For different types of LLMs, will the performance of the WARD method be affected? If so, how to adjust and optimize it?
2. In practical applications, the update frequency of data may be very high. What impact will this have on the effectiveness of the WARD method? How to deal with this situation?

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
3

### Summary
This paper tackles the issue of unauthorized data use in RAG systems. Noting the current absence of tools for detecting such misuse, the authors propose "RAG Dataset Inference" (RAG-DI), a framework that empowers data owners to identify unauthorized data utilization in RAG systems. To facilitate research on RAG-DI, they developed FARAD, a synthetic dataset generated by leveraging an existing dataset and LLMs. FARAD is crafted to simulate challenging scenarios where similar content may appear across multiple sources, enhancing its applicability in real-world settings.

Furthermore, the authors introduce WARD, a novel method that leverages an existing watermarking algorithm to enable data owners to statistically verify whether their data has been incorporated into an RAG system's corpus through black-box queries. Experimental results demonstrate that WARD consistently outperforms existing methods, providing remarkable accuracy, robustness, and efficiency. This approach offers a reliable mechanism for detecting unauthorized data use and establishes essential resources and methodologies to guide future research on data privacy in RAG systems.

### Strengths
1. Although RAG has gained popularity, its implications for data privacy and unauthorized usage detection remain largely unexamined. This paper introduces the RAG Dataset Inference (RAG-DI) concept alongside a watermark-based detection approach, offering a novel perspective on privacy within RAG frameworks. By developing the FARAD dataset and the watermark-based WARD method, this work establishes a strong foundation for future research. It stands as a pioneering contribution to addressing privacy concerns in RAG systems.

2. The paper offers comprehensive experimentation and empirical evaluation to validate WARD. The paper demonstrates WARD's outstanding performance across challenging scenarios by benchmarking WARD against multiple baselines, including adaptations from related fields.

3. The paper is well-written and organized, with a clear structure that enhances readability. The authors present their work logically, making the flow of ideas easy to follow in each section.

### Weaknesses
1. The authors claim their approach is effective in the challenging scenario where information is distributed across multiple sources. However, it remains unclear how the method performs when only one retrieved document is watermarked while others are unprotected. Additionally, they evaluate the method only with k=3; it is uncertain how effective it would be if the system retrieves more, say 10 relevant documents, with only one being protected. Without this analysis, the effectiveness of the proposed approach cannot be conclusively assessed, especially given that RAG systems can flexibly retrieve a variable number of relevant documents. Moreover, the "provable watermark" claim lacks empirical support; no rigorous evidence is provided to substantiate this assertion. While “provable” may reference the watermarking algorithm itself, scalability should also be addressed within this definition to strengthen the claim.

2. The authors claim their approach is provable; however, unlike existing watermarking algorithms, they do not provide a rigorous proof. This discrepancy undermines the study’s credibility.

3. The authors propose a relatively simple defense strategy that relies solely on prompt engineering. However, due to the complex requirements of the proposed defense, LLMs may struggle to adhere to instructions precisely, resulting in a suboptimal defense. A more practical and effective approach could involve monitoring the words used in the retrieved documents and limiting or penalizing the frequency of these words in generated responses. Additionally, after the response is generated, it could be further paraphrased to potentially reduce the usage of watermarking words, similar to techniques employed in existing watermarking approaches. Again, the issue is rooted in the absence of a theoretical guarantee.

### Questions
1. To my understanding, generating watermarked text typically requires white-box access to LLMs to direct the generation process. Then, how can one produce watermarked documents using black-box models like GPT-4 and Claude 3.5-Sonnet? Could you elaborate on the methods or approaches that make this possible?

### Soundness
3

### Presentation
3

### Contribution
3
