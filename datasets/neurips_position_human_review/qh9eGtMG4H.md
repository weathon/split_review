# LLM Generated Persona is a Promise with a Catch

- Decision: Accept
- Scores: 6, 7, 7

## Abstract
The use of large language models (LLMs) to simulate human behavior has gained significant attention, particularly through personas that approximate individual characteristics. Persona-based simulations hold promise for transforming disciplines that rely on population-level feedback, including social science, economic analysis, marketing research, and business operations. Traditional methods to collect realistic persona data face significant challenges. They are prohibitively expensive and logistically challenging due to privacy constraints, and often fail to capture multi-dimensional attributes, particularly subjective qualities. Consequently, synthetic persona generation with LLMs offers a scalable, cost-effective alternative. However, current approaches rely on ad hoc and heuristic generation techniques that do not guarantee methodological rigor or simulation precision, resulting in systematic biases in downstream tasks. Through extensive large-scale experiments including presidential election forecasts and general opinion surveys of the U.S. population, we reveal that these biases can lead to significant deviations from real-world outcomes. Based on the experimental results, this position paper argues that **a rigorous and systematic science of persona generation is needed to ensure the reliability of LLM-driven simulations of human behavior.** We call for not only methodological innovations and empirical foundations but also interdisciplinary organizational and institutional support for the development of this field. To support further research and development in this area, we have open-sourced approximately one million generated personas, available for public access and analysis.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on the topic of LLM-generated persona (for simulation) and the challenge of "the scalable generation of representative persona profiles for accurate LLM simulation of any target population.". The authors conduct a series of experiments, showing some limitations, findings and insights. The authors advocate the development of science of persona generation.

### Strengths
- The paper is well-structured and easy to read.
- The authors conduct several experiments to support their advocacy. And the experimental results are interesting that could provide some insights to the community.
- The advocacy is clear and reasonable. Given that LLM-based social simulation is an emerging topic, we need better understanding of these persona.

### Weaknesses
- Experimental focus is largely U.S.-centric, limiting generalizability to other cultural or demographic contexts.
- While it identifies bias patterns, the paper offers limited quantitative exploration of mitigation strategies or comparative evaluation of possible fixes.
- The discussion of alternative views is brief and doesn’t deeply engage with scenarios where synthetic personas may still be viable despite identified flaws.

### Questions
na

### Presentation
3

---

## Human Reviewer 2

### Rating
7

### Rating Number
7

### Confidence
3

### Summary
This paper discusses the topic of the persona-based simulations. These simulations involve generating a persona - a set of features/characteristics which could describe a real human, such as age, race, occupation, etc., and possibly a more nuanced text-based descriptions and details. These personas are used for LLM-based simulations, where an LLM is asked specific questions and requested to answer as if they were the person described by those generated characteristics. This approach may allow for running realistic experiments in the areas such as social sciences or market research without the costs and privacy concerns which come with querying human subjects. The authors present and experimentally evaluate some of the challenges of the current persona-based simulation methods, such as the lack of widely available large datasets with joint measurements of key characteristics in the population, and bias towards specific views caused by using LLMs to fill in the details of the personas. The authors argue for a more systematic and rigorous approach to persona generation to ensure reliability of such simulations. Among other things, they advocate for creating a large-scale open source benchmark dataset of realistic personas.

### Strengths
The authors run various quantitative and qualitative experiments to demonstrate the current challenges stemming from the usage of persona-based generation, spanning diverse areas, including political views and human psychology/sentiment. The authors also provide a comparison between different persona generation approaches with various proportions of the persona characteristics being generated via LLMs as opposed to being sampled/imputed in other ways. The paper is well written, the presentation is clear and the authors provide illustrative examples which help the reader understand the motivation behind pursuing persona-based simulation. The authors' opinion is argued clearly and the topic is relevant to both the general public and the NeurIPS community.

### Weaknesses
In many cases the authors do not provide any intuition or hypotheses on the causes of the phenomena/challenges specific to persona generating methods. The intuitive reasoning/justification for using LLMs for specific tasks is also lacking in some cases. For instance, the authors state: "Regardless of dataset's size, generation methods are necessary to capture the complex, subjective aspects that traditional surveys often miss." Intuitively, LLMs may be capturing some additional details about the population since they were trained on human-generated text, so they could be viewed as additional survey methods in some sense. For clarity, this is just an example of a possible elaboration, authors need not agree with this statement and I would not expect them to state anything like this if they indeed disagree. Other places where more elaboration may be helpful is where the authors mention the LLM bias, for instance towards specific political positions. Also, on page 7: "We can clearly see that persona opinions diverge more on controversial topics." Evaluating which topics are more controversial is somewhat subjective. Are there data available on the variance in these answers among the population or are they not available at this time?

### Questions
Page 6: "as persona types become more LLM-generated (...) their perspectives shift from traditional to more progressive views". Do you have any intuition as to why this may be the case? For instance, to the question "Is the cost of getting a four-year college degree today worth it?", the Descriptive Persona answered "worth it without loans" most frequently but "worth it with loans" least frequently. Perhaps this is due to the large quantity of text on the issues with student loans available online?

The persona generation methods are presented in contrast to the "Real Data Only" approach. Would it be possible to use a hybrid approach, for instance, to collect a smaller dataset with some basic characteristics on the individuals in the population, such as broad political affiliation (Dem. / Rep. / Other) jointly with other characteristics, then use more traditional ML/statistical methods to estimate these joint distributions (possibly also including some marginal data from the Census), then sample these broad, categorical/numeric variables (e.g., broad political affiliation, gender, income) from the estimated distribution and instruct the LLM to create the details for the persona conditioning on these variables?

### Presentation
3

---

## Human Reviewer 3

### Rating
7

### Rating Number
7

### Confidence
3

### Summary
This paper examines potentials and mainly the risks associated with synthetic data generation for personas (profiles that are synthetically generated on the basis of some specified traits) using LLMs. The area of synthetic persona generation is of interest for its applicability in various disciplines that study human subjects at scale. The paper, using examples including presidential election, highlights a clear divergence that exists between the real data, and the synthetic one. Their results reveal systematic biases, for instance increasing LLM-generated personas amplifies skewed outcomes. The paper positions itself as a call to establish a rigorous “science of persona generation,” advocating for methodological innovation, frameworks, benchmarks, and cross discipline collaboration.

### Strengths
- Clear presentation and arguments
- Addresses a rapidly growing practice of using LLMs for persona simulations, which is highly relevant to multiple disciplines (i.e., human sciences).
- Strong and diverse empirical evidence to support the main point of the paper across elections, surveys, and multiple LLMs 
- The release of the ~1M persona dataset could be of use for others in the same area of research
- Prior work on LLM bias has mostly focused on simulation outputs, whereas this study dissects bias in the persona generation step itself

### Weaknesses
- It would have been more insightful if the paper made a more serious attempt in rooting the potential underlying factors that lead to the presence of such skewed bias between real and synthethic data(e.g., whether biases arise from training data, prompts, or model architectures for instance).
- Just to clarify, regarding "alternative position" - the paper does consider real data as the alternative. But perhaps the actual alternative to argue against was other means of generating synthetic persona data compared with LLMs-based approach. Although, as I am not an expert in this area, I am not sure if such approaches existed pre-LLMs.

### Questions
- What minimal set of attributes do you consider essential for valid persona construction? This is probably an open question, but some more insights will be helpful.
- Do you expect certain generation of LLMs (i.e., reasoning LLMs to be less problematic in synthetic data generation of such nature)?

### Presentation
3
