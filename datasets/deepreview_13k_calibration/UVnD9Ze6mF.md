# AIR-BENCH 2024: A Safety Benchmark based on Regulation and Policies Specified Risk Categories

- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 8, 10, 6

## Abstract
Foundation models (FMs) provide societal benefits but also amplify risks. Governments, companies, and researchers have proposed regulatory frameworks, acceptable use policies, and safety benchmarks in response. However, existing public benchmarks often define safety categories based on previous literature, intuitions, or common sense, leading to disjointed sets of categories for risks specified in recent regulations and policies, which makes it challenging to evaluate and compare FMs across these benchmarks. To bridge this gap, we introduce AIR-BENCH 2024, the first AI safety benchmark aligned with emerging government regulations and company policies, following the regulation-based safety categories grounded in the AI Risks taxonomy, AIR 2024. AIR 2024 decomposes 8 government regulations and 16 company policies into a four-tiered safety taxonomy with 314 granular risk categories in the lowest tier. AIR-BENCH 2024 contains 5,694 diverse prompts spanning these categories, with manual curation and human auditing to ensure quality. We evaluate leading language models on AIR-BENCH 2024 uncovering insights into their alignment with specified safety concerns. By bridging the gap between public benchmarks and practical AI risks, AIR-BENCH 2024 provides a foundation for assessing model safety across jurisdictions, fostering the development of safer and more responsible AI systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors introduce AIR-BENCH 2024, a new safety benchmark for AI models grounded in real-world regulations and policies. Using risk categories from 8 government regulations and 16 corporate policies, they crafted a set of 5,694 prompts covering 314 specific risk scenarios to test models’ ability to handle sensitive content safely. They evaluate some current LLMs on this benchmark.

### Strengths
Alignment with actual regulations: A novel feature of this benchmark is its grounding in real-world regulations. By basing AIR-Bench on key regulations from the EU, US, and China, it addresses critiques that existing AI safety benchmarks lack practical relevance, providing a benchmark that better reflects legal requirements.

Granularity of risk categories: The four-level risk structure comprises 314 specific risk categories. The detailed granularity should be appreciated for safety alignment.

### Weaknesses
1. Given that the paper bases its alignment on actual regulations, I am curious how it manages to balance or trade-off conflicts between regulations across different countries and regions. As one key motivation of the paper is its combination of regulations from various regions. How does it handle potentially conflicting elements, such as differing privacy laws and, more broadly, varying definitions of "appropriate" outputs across populations in different countries? Or do they just ignore it? 

2. The use of only GPT-4 for scaled generation from manually crafted templates seems somewhat artificial. I understand that a more expensive annotation method may not be practical. However, there may be some potential bias introduced by scaling generation with a single model from simplistic, handwritten templates. 

3. Regarding presentation suggestions, while the tables in the results section are indeed extensive, the takeaways seem limited. From my understanding, they represent combinations across two dimensions: different categories and models. It may be challenging for readers to identify key insights as there are so many big result tables. And I would appreciate a more in-depth discussion to highlight critical findings.

### Questions
I still find the discussion somewhat not so in-depth thus:

Any insights into conflicts or correlations between AI compliance regulations across different countries while working on this benchmark? This might hold significant practical value for cross-border AI services.

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
The paper introduces a safety benchmark for assessing LLMs based on regulatory and policy-driven risk categories. Leveraging an AI risk taxonomy, which unifies risks specified in government regulations and corporate policies, AIR-BENCH categorises multiple specific risk types and uses thousands of designed prompts to evaluate LLMs’ alignment with regulatory safety standards. The benchmark assesses model refusal behaviours across risk categories by simulating scenarios of potentially harmful content requests. This study evaluates 22 prominent LLMs, highlighting safety gaps and inconsistencies in regulatory alignment.

### Strengths
- The benchmark's alignment with diverse government and corporate regulations makes it very relevant for real-world applications, and it addresses a gap in existing benchmarks
- The benchmark itself is well structured with multiple levels of taxonomy which helps identification of model deficiencies across multiple risk categories
- The experiments include detailed comparison of multiple models, identifying key trends and areas where models fall short of regulatory expectations
- The paper is well-structure and easy to read, it introduces related work in detail and 

Overall, I like this paper a lot. It is of high quality and tackles a very relevant issue.

### Weaknesses
There are some weaknesses, but they are not very severe. 

- Using GPT-4o as both prompt generator and judge could introduce biases in evaluation, but this is appropriately acknowledged 
- Different regulations have separate restrictions for providers, distributors, deployers, etc, the way this is handled in the benchmark is not obvious. I.e. should the API refuse protected decision making (health/financial) unless the client has guaranteed sufficient oversight? What if the client has oversight? This nuance is hinted at in section 4.4 but a deeper discussion on this difference would be very helpful. 
-  The benchmark assumes that the model operates as a standalone system. However, many real-world applications involve human oversight, which might mitigate risks differently than this evaluation assumes.
- Given the evolving nature of AI regulations, the benchmark may become outdated quickly, limiting its long-term applicability unless it is regularly updated. The authors note this already, but it would be interesting to hear their thoughts on potential future paths towards mitigating this
- About 70% of the judge prompts remain model-generated, which might lead to inconsistencies in judgment fidelity, particularly in ambiguous cases
- Although the benchmark focuses on regulatory alignment, making it a net-positive, a more thorough examination of potential societal impacts could strengthen the discussion, i.e. could malicious actors use the benchmark to help identify weekly guarded models to speed up their activities?

### Questions
-  If a response is neither explicitly refused nor overtly harmful, how is it classified within the framework?

- The paper notes that “Human experts then manually review and revise these expanded prompts to maintain prompt quality and alignment with the intended risk categories.” Could you provide additional details on the methods, criteria or protocols used in this manual review process?

- Where were the experiments run from? I.e. the IP region of the client. In case model providers are serving different levels of steering/guardrails based on user location, even if they use the same model/version identifier. This will be good to add in the de-anonymised version for increased reproducibility.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
In the paper under review, a benchmark on the safety and regulatory conformity of LLMs in proposed. The benchmark is a multi-tiered one, and is based on policies of various governments and companies. The key idea is to generate a set of instructions, which is curated and generated over multiple iterations, that is than fed to the LLM under examination. The responses of the LLM on these instrucations are then evaluated automatically.

### Strengths
* The paper adressing a very relevant topics. There is a lack of approaches for assessing the safety of LLMs in an automated fashion. This paper is a big step in this direction.
* The paper is very well structured and easy to ready. I light the color-coding of levels of the approach. This supports the reading a lot.
* All relevant literature is considered in this paper.

### Weaknesses
I do not see many weaknesses in this paper. Actually, I only see the limitation that the benchmark addresses dialects and authority statement, but it seems that this only holds for English. Other languages are not supported / evaluated. So there might be a risk that harmful output of an LLM in non-English languages are not assessed or overlooked.

### Questions
Based on the limitation I mentioned: what about adressing different languages than English?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a new safety benchmark for large language models (LLMs). Unlike existing benchmarks, this one is grounded in a taxonomy of undesirable behaviors derived from legal and policy frameworks. The benchmark consists of prompts categorized into various risk categories. Additionally, the authors evaluate several LLM models against this benchmark.

### Strengths
Overall, despite the paper being positioned more “grandiosely” than its actual contributions (see weaknesses), the proposed dataset of prompts clustered in tiered categories can be useful for the community studying refusal of LLMs to engage in undesirable behaviour. The authors have demonstrated that their dataset is more diverse and covers more categories than prior benchmarks. Beyond creating the dataset, the authors have also produced an automated evaluation system and have validated it against human raters. Because of the comprehensive and principled benchmark creation and evaluation in this paper, I would recommend its acceptance.

### Weaknesses
The paper seems to oversimplify the notion of “safety and risk” and implies that higher refusal rates on prompts related to specific prompts implies more safe models. However, the notion that a model can, in of itself, be safe or not, is rather simplistic. It is only when one acts in an unsafe way, as a direct result of a model’s response, that is unsafe. The model provides information and information itself cannot be unsafe, acting on information might or might not be unsafe or carrying risks. Therefore, the present benchmark offers a method of evaluating whether a model will refrain from potentially undesirable set of behaviours, rather than whether it is inherently safe or not. 

While the paper’s Section 4 “Evaluation and Takeaways” does indeed refer to “refusal” rather than “safety”, the rest of the paper doesn’t. This  leaves the impression that this benchmark measures the much more fundamental, complex and nuanced problem of “safety and risk” rather than the more grounded “refusal rate” that it actually does. Therefore, I’d recommend that the authors reconsider their positioning to align it better with the nature of their contributions.

### Questions
See weaknesses.

### Soundness
2

### Presentation
4

### Contribution
3
