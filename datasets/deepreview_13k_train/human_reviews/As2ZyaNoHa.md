# Are Large Language Models Truly Democratizing Financial Knowledge? Identifying Knowledge Gaps

- Decision: Reject
- Scores: 3, 1, 6

## Abstract
Large Language Models (LLMs) are frequently utilized as sources of knowledge for question-answering. While it is known that LLMs may lack access to real-time data or newer data produced after the model's cutoff date, it is less clear how their knowledge spans across *historical* information. In this study, we assess the breadth of LLMs' knowledge using financial data of U.S. publicly traded companies by evaluating more than 190k questions and comparing model responses to factual data. We further explore the impact of company characteristics, such as size, retail investment, institutional attention, and readability of financial filings, on the accuracy of knowledge represented in LLMs. Our results reveal that LLMs are less informed about past financial performance, but they display a stronger awareness of larger companies and more recent information. Interestingly, at the same time, our analysis also reveals that LLMs are more likely to hallucinate for larger companies, especially for data from more recent years. We will make the code, prompts, and model outputs public upon the publication of the work.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper examines the breadth and biases in large language models' (LLMs) knowledge concerning financial data on U.S. publicly traded companies. Using a dataset of over 190,000 questions, the study assesses how well LLMs represent historical financial information and explores the influence of company characteristics (like size, market cap, and institutional attention) on model performance and hallucination rates. Findings indicate that while LLMs are more accurate with data on larger firms and recent information, they also tend to hallucinate more frequently for such cases, revealing inherent biases that challenge the notion of democratized financial knowledge in LLMs.

### Strengths
Addresses a key issue: The paper tackles an important topic by assessing the biases and limitations of large language models in representing financial knowledge, specifically for U.S. publicly traded companies. This focus on knowledge gaps in LLMs and its impact on democratizing financial information is timely.

### Weaknesses
 - Lack of Novelty: The paper lacks innovation in methodology. It primarily repurposes existing techniques to evaluate LLMs without introducing new methods or frameworks. While the dataset itself is new, the analytical approach does not present methodological advancements. Additionally, the evaluation focuses on a limited selection of three general-domain LLMs without a comprehensive comparison to specialized financial LLMs like FinMA, FinGPT, or other representative LLMs (e.g., GPT-4, GPT-4o, Gemma, Mistral). The narrow scope limits the generalizability and depth of the conclusions drawn.

- Insufficient Case Studies and Error Analysis: The study relies heavily on metric-based performance evaluations without deeper case studies or qualitative error analysis. Incorporating detailed case studies would enhance understanding of specific error patterns and biases in the models’ financial responses, providing more substantiation for the findings.

- Potential Copyright Concerns: The paper does not address potential copyright issues related to the financial dataset used for evaluation. More clarity is needed on the data source's legal and ethical aspects, particularly for research purposes.

- Introduction and Related Work Needs Reorganization: The introductory sections lack depth and miss key relevant background on many existing research in financial LLMs and LLM evaluation frameworks. A more comprehensive review of related work, particularly on financial LLM development and evaluation methodologies such as [1][2], would strengthen the contextual understanding and help to better position this work within the current landscape.

### Questions
See the weakness

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper finds that LLMs tend to retrieve corporate financial information when answering questions about recent periods and larger firms. However, it is more likely that LLMs hallucinate when they answer questions about larger firms and data from recent years. I applaud the authors for setting up a nice dataset for financial data retrieval. However, the paper has serious empirical and institutional issues, as stated below.

### Strengths
One potentially interesting aspect of this study is that LLMs tend to hallucinate more for larger firms. This, at first glance, seems counterintuitive because the authors find that LLMs’ accuracy is higher for larger firms. However, considering that retail investors are more likely to ask questions about larger firms, and if they get “wrong” answers, it is potentially a more serious problem than not being able to get any answers. Perhaps, one potential way to improve the implications of this study is to develop tools to minimize hallucinations in answering financial questions (see my comment below).

### Weaknesses
This paper lacks institutional details, and the authors do not seem to understand how language models are used in practice. Large brokerage houses and institutional investors never use an LLM to retrieve financial knowledge. In retrieval models, a specific context is explicitly given, and the models are fine-tuned to answer questions “within” this context window. They train their own models to improve performance in answering financial questions only after providing the model with a specific set of information. What the authors test in this paper is not how language models are used in practice or academia for financial research. Nobody in practice asks questions about firms’ fundamentals to an LLM. Instead, LLM’s potential lies in making economic predictions or interpretations given the financial fundamentals of a firm. Anyone can quickly look up the basic fundamentals of firms nowadays, and it is less likely that investors will use an LLM to retrieve financial information. To answer the question of whether LLMs are democratizing financial knowledge, the authors should look at economic interpretations of given financial information (i.e., whether LLMs can answer economic questions better than traditional platforms). I am not convinced at all that the authors answer the question of financial information democratization by simply asking GPT, “What is the revenue of firm A in year X?”.

Considering that we don’t know exactly which datasets LLMs are trained on, many studies have already explored LLMs’ performance based on recent knowledge. It is already well-known that LLMs tend to have better knowledge of recent events. The reason that LLMs answer questions about larger firms more accurately is potentially because they are covered more frequently by media articles, which are publicly available. As more electronic information has been produced in recent years, it is also trivial that LLMs answer questions about recent fiscal years more accurately. It is not surprising that LLMs do better for larger firms, and this finding does not make enough contribution to clear the bar at ICLR.

This paper is based on a very simple research design and I do not have much to add in terms of execution. However, I am unsure why the authors use only a simple one-shot prompt. Knowledge retrieval can benefit greatly from (i) allowing the model to search external knowledge and (ii) adding an additional step of validation. At least, the authors may want to try several techniques that are known to reduce hallucination (multi-agentic approach, few-shot prompts, etc.). Also, simply by adding “if you do not have a concrete source of information, give me N/A instead of writing up your answer” will help.

Your prompt does not consider the difference between fiscal year and calendar year. Most financial reporting is based on the fiscal year and writing a prompt like “What was the revenue of XX in 2002?” is confusing. Furthermore, the authors need to be more specific in that they require “annual” revenues.

### Questions
See "Weaknesses".

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposed a systematic method to analyze the knowledge biases of LLMs in the financial field and did a comprehensive evaluation through a relatively large dataset. Key findings indicate that LLMs show higher accuracy for more recent information and larger companies. The paper also highlights a tendency for LLMs to hallucinate more frequently for larger companies, even though these models tend to perform better with them.

### Strengths
1. The paper addresses an interesting topic on the bias of LLMs in financial domain.
2. The paper is clear. The analysis is based on relatively large datasets and the conclusions make sense.
3. The proposed framework can be adopted beyond financial field to evaluate LLM biases.

### Weaknesses
1. The related work only mentioned existing research regarding societal and political biases and hallucination in LLMs, it would be great to add some background on LLMs in financial domain.
2. As mentioned in the limitation section, using “revenue” as a proxy for questions might constrain the diversity of questions and knowledge.

### Questions
1. The results could be more convincing if the findings are consistent on other mainstream LLMs like Claude and Gemini.
2. Can we include some details on how significance is encoded in the regression method?

### Soundness
3

### Presentation
3

### Contribution
3
