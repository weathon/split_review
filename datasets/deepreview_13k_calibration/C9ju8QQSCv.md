# Can LLMs Solve Long Math Word Problems Better?

- Decision: Accept
- Avg Score: 4.75
- Scores: 5, 3, 5, 6

## Abstract
Math Word Problems (MWPs) are crucial for evaluating the capability of Large Language Models (LLMs), with current research primarily focusing on questions with concise contexts. However, as real-world math problems often involve complex circumstances, LLMs' ability to solve long MWPs is vital for their applications in these scenarios, yet remains under-explored.
    This study pioneers the exploration of \textbf{Co}ntext \textbf{Le}ngth \textbf{G}eneralizability ({\property}), the ability of LLMs to solve long MWPs.
    We introduce Extended Grade-School Math ({\benchmark}), a collection of MWPs with lengthy narratives. 
    Two novel metrics are proposed to assess the efficacy and resilience of LLMs in solving these problems.
    Our examination of existing zero-shot prompting techniques and both proprietary and open-source LLMs reveals a general deficiency in {\property}.
    To alleviate these challenges, we propose distinct approaches for different categories of LLMs.
    For proprietary LLMs, a new instructional prompt is proposed to mitigate the influence of long context.
    For open-source LLMs, a new data augmentation task is developed to improve {\property}.
    Our comprehensive results demonstrate the effectiveness of our proposed methods, showing not only improved performance on {\benchmark} but also generalizability across several other MWP benchmarks.
    Our findings pave the way for future research in employing LLMs for complex, real-world applications, offering practical solutions to current limitations and opening avenues for further exploration of model generalizability and training methodologies.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work examines the effect of extended contexts on mathematical reasoning and introduces the Extended Grade-School Math (E-GSM) dataset, featuring math problems with lengthy narratives. Analysis reveals that current LLMs struggle with E-GSM, prompting the authors to propose new methods to address these challenges. 

For proprietary LLMs, they introduce a new instructional prompt, while for open-source LLMs, they develop a novel auxiliary fine-tuning task. These approaches aim to enhance model performance in handling extended-context MWPs.

### Strengths
- This paper introduces E-GSM, a dataset with lengthy, distracting sentences that make it considerably more challenging than the original GSM. This dataset offers a valuable tool for evaluating the robustness of LLMs.

- The approach used to create E-GSM can also be applied to expand existing math training datasets, providing new supervised fine-tuning (SFT) data in the math domain.

### Weaknesses
 - The augmented math questions may include contradicting sentences. The augmented math questions  may become unsolvable or yield answers that differ from the original ones. 
Although human evaluations on 200 samples suggest that “94.5% of questions meet acceptable quality,” this accuracy may still be inadequate, particularly given that the labels in the GSM8K test set might contain errors. An alternative could be to release these 200 samples as a verified subset of the E-GSM dataset. Reporting CoLeG-E and CoLeG-R results on the 200 samples, both with and without verification, would also be helpful.

- In Table 2, the higher results w/ $\mathcal{D}$ (compared to w/ $\mathcal{D_0}$) may because the size of  $\mathcal{D}$ is larger than $\mathcal{D_0}$.

### Questions
- How is E-GSM different from GSM-IC[1]? 

[1] Large Language Models Can Be Easily Distracted by Irrelevant Context. ICML 2023. https://arxiv.org/abs/2302.00093

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the authors investigated the performance of LLMs in solving long math problems. They first examined the performance discrepancy of ChatGPT 3.5 in solving two versions (i.e. long form v.s. short form) of the same questions and concluded that LLMs struggle to answer math word problems with longer context. 

Then, they propose an automatic approach to extend the GSM questions into their long versions (named the obtained dataset E-GSM), with the same computation logic remaining, as far as they could. 
After that, the paper presented a method called CoRe to help proprietary LLMs better handle these long-form questions. 
For the open source LLMs, the authors fine-tuned them with a fine-tuning dataset comprising 65K CoT data, created by the authors. 


The paper introduced E-GSM containing artificial long math problems, but in real cases, there are seldom questions written in the way that the authors presented, i.e. very verbose questions talking about a relatively simple math problem. Therefore, it is unknown whether the conduct here can help in solving real-world long math problems where although the question is quite long, it already describes the problem in a succinct way that it could. Better solving them is our goal, rather than solving the artificial verbose problems that are less likely to exist in the real world. Although they show the same characteristic length-wise, the capability of solving the latter is not necessarily helpful for solving the former.

### Strengths
The paper explored the impact of question length on LLMs’ performance and proposed a method to extend the length of GSM questions. The paper presented a method called CoRe to help proprietary LLMs better handle these long-form questions. For the open source LLMs, the authors fine-tuned them with a fine-tuning dataset comprising 65K CoT data, created by the authors.

### Weaknesses
1. The paper explores the artificial long math problems, but in real cases, there are seldom questions written in the way that the authors presented, i.e. very verbose questions talking about a relatively simple math problem. Therefore, it is unknown whether the conduct here can help in solving real-world long math problems where although the question is quite long, it already describes the problem in a succinct way that it could. Better solving them is our ultimate goal, rather than solving the artificial verbose problems that are less likely to exist in the real world. Although they show the same characteristic length-wise, the capability of solving the latter is not necessarily helpful for solving the former.

2. Besides the above major point, there are more points:
- In Section 2.1, the authors examined the performance discrepancy of ChatGPT 3.5 in solving two versions (i.e. long form v.s. short form) of the same questions and concluded that LLMs struggle to answer math word problems with longer context. However, ChatGPT 3.5 is a relatively weak model now, I would suggest the authors do the same analysis with stronger open-source and proprietary LLMs. 
- Still in Section 2.1, the analysis here is based on real math questions, but the long questions in E-GSM are artificial. Therefore, it is not convincing to me that the conclusion in Section 2.1 can provide a solid foundation for the subsequent conduct. 

3. Many parts are not clear, see the questions section.

4. The writing needs a thorough improvement:
- “Human evaluation details are provided in Appendix A.4.” has a wrong reference. 
- In the first paragraph of Section 3, the subsections should be introduced in order. 
- The second sentence of Section 3.1 has redundancy. 
- The first two sentences of Section 3.2 are not about open-source LLMs, therefore, they cannot help develop this section. The third sentence is redundant. In the fourth sentence, “their generated reasoning paths” should be referred to the place that telling how it is done. The loss function has a typo, should be “ (q, e, a)”.
- Section 3.3, “To negate the influence of few-shot demonstrations”, should be specific, what is the influence? 
- Repeated sentences in the third paragraph of Section 4.1.

### Questions
1. According to “Evaluation results shows that 94.5% questions possess accepatable quality”, the total questions from rounds 1 to 4 should be about 5K. But in Table 1, it is only 4.5K.

2. As shown in Table 1, different rounds have different numbers of questions, what’s the impact on the defined metrics? namely CoLeG-E and CoLeG-R?

3. In Table 2, were the fine-tuned models evaluated with the CoRe method? can they be tested in the same way as those proprietary models? 

4. “Apart from 7,473 annotated examples available in GSM8K training set, we get D0 that incorporate 38,507 valid CoT data points …”, the numbers here confused me. If the authors generated five reasoning paths for each question in the training set, at most, D0 can have 7,473*5 questions, less than 38,507.

5. In Section C.2, “The results suggest scaling up model scales and SFT dataset can further improve CoLeG.”, this conclusion may not be valid. Under CoLeG-R, after the SFT on D0, D1, and D2, the performance is not improved.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates the ability of LLMs to solve math word problems (MWPs) with longer contexts, introducing the concept of Context Length Generalizability (CoLeG). The key contributions are:(1) Creating Extended Grade-School Math (E-GSM), a dataset of MWPs with extended narratives. (2) Proposing two metrics to evaluate LLMs' efficacy and resilience on E-GSM. (3) Developing tailored prompts for proprietary LLMs to improve CoLeG. (4) Using extension as an auxiliary fine-tuning task for open-source LLMs. (5) Analyzing the impact on semantic understanding vs reasoning efficacy.

### Strengths
Strong motivation through rigorous statistical analysis shows LLMs struggle with longer MWPs (Section 2.1)

Proposes creative solutions (CoRe prompting and extension fine-tuning) to address identified limitations

Well-designed metrics (CoLeG-E and CoLeG-R) that capture both efficacy and robustness of LLMs on long MWPs

Sufficient experiments have proven the effectiveness of the method

### Weaknesses
The paper focuses on LLMs tackling longer math word problems, rather than genuinely difficult ones. Addressing truly challenging problems would likely yield more impactful and valuable research insights.

A deeper analysis of the types of errors LLMs make on extended MWPs would strengthen the paper. This could shed light on whether mistakes stem from misinterpreting context, losing track of key information, or actual computational errors.

The authors don't explore whether breaking down problems into atomic facts could help solve extended MWPs. It would be worthwhile to compare their methods against a baseline that first extracts crucial information from the lengthy context before attempting a solution. The techniques discussed in https://arxiv.org/abs/2305.14251 could be relevant here.

The table captions should be placed above the tables, not below, to comply with ICLR's official template guidelines.

The "Experimental Setup" section doesn't belong under Methodology. It should be moved to the Experiments section, alongside the results analysis.

### Questions
see weaknesses

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
This paper investigates the performance of LLMs on Math Word Problems with extended narratives, introducing the concept of Context Length Generalizability (CoLeG). The authors created a new dataset, Extended Grade-School Math (E-GSM), by iteratively extending problems from GSM8K. They propose two novel metrics, CoLeG-E and CoLeG-R, to evaluate efficacy and robustness respectively. The study reveals that existing LLMs struggle with longer MWPs, showing a consistent performance decline as context length increases. To address this, the authors introduce Condition-Retrieving Instruction (CoRe) for proprietary LLMs and an extension-based fine-tuning approach for open-source LLMs. These methods demonstrate improvements in CoLeG across various LLM types and generalize well to other MWP benchmarks as well.

### Strengths
1. The paper addresses a gap in current research by focusing on LLMs' ability to handle longer MWPs, which is more reflective of real-world mathematical reasoning tasks. The focus on CoLeG provides insights into the limitations of current LLMs and pathways for improvement.

2. The creation of the E-GSM dataset through a systematic extension process is another contribution. By maintaining problem difficulty while increasing context length, the authors have developed a framework for evaluating LLM performance on longer MWPs.

3. The introduction of CoLeG-E and CoLeG-R metrics offers a more comprehensive evaluation framework than traditional accuracy measures. These metrics provide insights into both the consistency and robustness of LLM performance across varying context lengths.

4. The proposed methods, CoRe and extension-based fine-tuning, show consistent improvements across different LLM types and generalize well to other benchmarks.

### Weaknesses
1. The paper lacks a detailed exploration of why longer contexts impact LLM performance. While the authors mention potential working memory limitations, a deeper analysis could provide valuable insights. For instance, examining how performance correlates with the models' context window sizes or investigating the behavior of attention patterns in different layers could shed light on where breakdowns occur. Additionally, analyzing how different positional encoding schemes (e.g., rotary position embeddings vs. absolute position embeddings) affect performance on longer MWPs could offer insights into architectural considerations for improving CoLeG. Specifically, the analysis should explore whether the performance degradation is due to the model's inability to attend to relevant information across the entire context, or if the issue stems from the model's capacity to maintain a coherent representation of the problem state as the context grows. This could involve examining the attention weights to see if they become more diffuse or focused on irrelevant parts of the context as the length increases. Furthermore, analyzing the activation patterns in different layers could reveal whether the model is losing crucial information or struggling to integrate information from different parts of the context.

2. The E-GSM dataset creation process, while systematic, may introduce biases that aren't adequately addressed. Using GPT-4 for extensions could potentially lead to biases in language style, problem structure, or even subtle cues that GPT-4 uses for reasoning. For example, GPT-4 might consistently use certain phrases or sentence structures that inadvertently serve as hints for other GPT models. Additionally, there's a risk of amplifying any biases present in the original GSM8K dataset. The authors should consider analyzing the distribution of problem types, linguistic patterns, and solution strategies in E-GSM compared to the original dataset to identify any systematic biases introduced during extension. This analysis should include a comparison of the frequency of different mathematical operations, the complexity of the linguistic structures, and the types of reasoning steps required to solve the problems. A detailed analysis of the generated text, including n-gram analysis and syntactic parsing, could reveal if there are any consistent patterns that might inadvertently aid or hinder specific models.

3. The evaluation of open-source LLMs is limited to LLaMA-2 and Mistral-7B families. To provide a more comprehensive assessment, the authors should consider including models specifically designed for mathematical reasoning, such as MathGPT, GPT-f, or MetaMath. Additionally, evaluating performance on models with different architectural choices, like PaLM or BLOOM, could offer insights into how various model designs handle longer MWPs. This broader evaluation would strengthen the claims about the generalizability of the proposed methods. The evaluation should also consider models with varying context window sizes to see if the performance degradation is correlated with this architectural parameter. Furthermore, it would be beneficial to evaluate models with different attention mechanisms, such as sparse attention or linear attention, to see if these mechanisms provide better performance on longer contexts.

4. While the paper shows improvements on other MWP benchmarks, it doesn't explore how the proposed methods perform on problems significantly longer than those in E-GSM. This leaves questions about the scalability of the approaches to even more complex, multi-page word problems. The authors could consider creating a small set of extremely long MWPs (e.g., 1000+ tokens) to test the limits of their methods and provide insights into scaling challenges. These extremely long MWPs should also include a variety of problem types and reasoning steps to ensure a comprehensive evaluation. The evaluation should also consider the computational cost of processing these longer problems, including memory usage and inference time.

5. The use of GPT-3.5-turbo for answer extraction in the evaluation process introduces a potential confounding factor. The paper doesn't adequately address how this might impact results, especially for non-OpenAI models. The authors should consider comparing this extraction method with simpler rule-based approaches or using model-specific output parsing to ensure fair comparison across different LLM families. This comparison should include an analysis of the accuracy and consistency of the different extraction methods across various models. Furthermore, the authors should consider using human evaluation to validate the accuracy of the extracted answers.

### Questions
1. How does the performance degradation on longer MWPs correlate with specific architectural features of different LLMs, such as context window size or attention mechanisms?

2. The extension approach shows promise for open-source LLMs. Have you considered how this might be adapted for extremely long MWPs or multi-step reasoning problems that span multiple pages?

### Soundness
3

### Presentation
3

### Contribution
3
