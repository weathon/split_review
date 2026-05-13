# What Makes a Maze Look Like a Maze?

- Decision: Accept
- Scores: 6, 6, 8, 6, 8

## Abstract
A unique aspect of human visual understanding is the ability to flexibly interpret abstract concepts: acquiring lifted rules explaining what they symbolize, grounding them across familiar and unfamiliar contexts, and making predictions or reasoning about them. While off-the-shelf vision-language models excel at making literal interpretations of images (e.g., recognizing object categories such as tree branches), they still struggle to make sense of such visual abstractions (e.g., how an arrangement of tree branches may form the walls of a maze). To address this challenge, we introduce Deep Schema Grounding (DSG), a framework that leverages explicit structured representations of visual abstractions for grounding and reasoning. At the core of DSG are schemas—dependency graph descriptions of abstract concepts that decompose them into more primitive-level symbols. DSG uses large language models to extract schemas, then hierarchically grounds concrete to abstract components of the schema onto images with vision-language models. The grounded schema is used to augment visual abstraction understanding. We systematically evaluate DSG and different methods in reasoning on our new Visual Abstractions Benchmark, which consists of diverse, real-world images of abstract concepts and corresponding question-answer pairs labeled by humans. We show that DSG significantly improves the abstract visual reasoning performance of vision-language models, and is a step toward human-aligned understanding of visual abstractions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a framework called Deep Schema Grounding (DSG) and a VQA benchmark for evaluating abstract visual reasoning of VLMs. For a given image and a question about the concept in the image, DSG first generates a schema of the concept using LLM. Then it grounds the components of the schema onto images using VLMs. Once the schema is grounded, the grounding information is given as context in text from to the VML to answer the question about the image. They show that giving grounded schema context to the VLMs improves their ability to correctly answer questions about abstract concepts in the image.

### Strengths
- Innovative use of pre-trained LLMs and VLMs to give additional context (in terms of grounded schemas) for VQA. In principle, this additional information should help answer pre-trained VLMs to better answer the questions related to the abstract concepts in the image. (However I think that the generated schemas shown in the appendix of the paper are not detailed enough to achieve this - please check weakness section)

- Hierarchical Grounding: I like how they have used a hierarchical method of grounding components of the schemas. Grounding independent concepts first and then the dependent concepts of the schema should be the correct way for grounding which is used in the paper.

### Weaknesses
 - Schemas are not detailed enough to give information about the concept. For example, tic-tac-toe schema include {board, symbols, strategy}. Although a tic-tac-toe game has  {board, symbols, strategy} it is not complete. Many board games have {board, symbols, strategy}. This schema does not tell that the board is a 3x3 grid, nor does it specify the number of players or the winning condition. Similarly, for “negotiating” the schema is {participants, setting, object}. This schema could be of many different settings and does not specify the nature of the negotiation, such as whether it's a business deal or a conflict resolution. The lack of specificity in these schemas limits their utility in providing meaningful context for VQA.

- It is shown that giving grounded schema as additional context to VLM to answer VQA question is improving the performance. But it is not shown or discussed why?/how? is the additional context improving the performance. For instance, in the example given in figure 1 of the paper where the question asks “What is the player in the maze?”, how is giving information about the layout, walls and entry-exit helping a VLM answer question about the ‘player’. The relationship between the grounded schema components and the specific question being asked is not clearly established, making it difficult to understand the mechanism of improvement.

### Questions
- Many recent works (https://arxiv.org/pdf/2305.10355, https://arxiv.org/pdf/2401.06209, others) have shown that VLMs  are ‘blind’ and don’t actually look at the visual information in images. VLMs mostly rely on language and questions in VQA benchmarks can be answered by having a good language prior. I was wondering how much of the questions in the proposed benchmark can be correctly answered by “language” only? It would be great to show a “language-only” baseline for the proposed VQA benchmark. Especially after adding grounded schema as context- it can show the impact of providing grounded schema too.

- A qualitative analysis of how/why is the grounded schema is improving VQA capabilities of the VLM would be great. Especially for the cases where the question does not ask anything about the concepts of the schema (like the example of “What is the player in the maze?” mentioned in the weakness section)

- Are the generated schemas verified by some expert? How are we sure that the schemas provided by the LLMs are correct for the provided concepts?

### Soundness
3

### Presentation
3

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
The paper proposes Deep Schema Grounding (DSG), a method to break down a visual concept into smaller concepts with dependencies on other concepts. The authors show the capability of DSG in solving complex visual question answering task. A visual abstraction benchmark is proposed with 12 abstract concepts and 180 images.

### Strengths
The paper provides a good solution for VLMs to better understand abstract concepts in an image. The presentation of the paper is clear with many figures for demonstration. The experiments are comprehensive, making the main message convincing. The benchmark created is novel and interesting.

### Weaknesses
In terms of the idea behind DSG, it seems to be close to chain of thought with specific instructions. For example, the maze example in the paper can be integrated with just one prompt: "Imagine that the image represents a maze. <the question> Think step by step by recognizing the layout of the maze, the walls of the maze, then the entry and exit of the maze one by one." Maybe gpt-4o can automatically do this even without the instructions. This is probably why in Table 7 if the generation is free form, DSG does not outperform gpt-4o much despite using more API calls.

Therefore, I am a bit concerned whether these types of schemas are necessary. After all, the dependency graph is generated by gpt-4, so at least gpt-4o should know how to do it if prompted well. But I agree that for smaller models, DSG can be very useful.

Another concern I have is about the diversity of the benchmark because the number of categories is quite limited.

### Questions
Could you try something like chain of thought prompting as I mentioned above?

Is there any way to generalize the idea to create a more general benchmark?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a VQA benchmark and method for visual abstract reasoning.

The "Visual Abstractions Benchmark" consists of 180 images, annotated with 3 questions each (and each question has 5 answer annotations from Prolific workers). These questions ask about abstract concepts in the image: for example, "Q: Imagine that the image represents a maze. Are there clear entrances or exits in the maze? [Yes or No]" (Figure 1; an image of an ice skating rink partitioned like a maze).

The method, "Deep Schema Grounding (DSG)", is a prompting framework that (1) uses an LLM to decompose an abstract concept into a schema, (2) uses a VLM to ground the "primitive" concepts from the schema to concrete concepts in the image, and (3) uses a VLM to answer the question given the schema and grounding.
1. The schema is a DAG: a "maze" would decompose into "layout" and "walls", and "layout" further decomposes into "entry-exit".
2. A VQA question is used for grounding: e.g. given the image, "..., what is the layout?". This graph is hierarchically grounded: e.g. "entry-exit" is grounded using the question "..., the layout is [], what is the entry and exit?". The ice rink example above entails the following grounding: "{layout: grid-like, walls: ice, entry-exit: gates}".
3. The image and grounded schema are joined as a VQA question for the VLM to produce a final answer.

Applying this framework improves performance of GPT-4o by 10% (relative) on the benchmark.

### Strengths
This paper is extremely clear and straightforward.

In general, I believe the comparisons are fair and sufficient ablations are provided, so it is methodologically sound. For example, they show a 10% relative improvement when applying their method with GPT-4o and 7% with (the open-source and weaker) LLaVA model. They also compare against other methods (ViperGPT and VisProg) that also use GPT models (GPT-3) for visual question decomposition, but don't perform nearly as well on this benchmark. Finally, they provide sufficient ablations of their own method (separating the schema/grounding/hierarchy/context components and showing incremental gains of each).

I believe this is a creative benchmark and that existing vision–language benchmarks under-explore abstract visual concepts. The method is task-specific, but I think that is fine, because it is prompting-based. I don't think the approach is entirely original but I think it sufficiently rounds out the paper: they show how explicit structure improves performance of existing models on their benchmark.

Altogether: this paper presents a benchmark, shows that existing vision–language models underperform, and introduces an explicit prompting method that can be applied with any LLM/VLM to improve performance. The best performance with this method is still just 73% (with the strongest, closed models) or 44% (with open-source models), leaving sufficient challenge for future work.

### Weaknesses
I believe the construction of the dataset is under-specified (and I also checked the appendix). I understand that answer annotations were provided by crowd workers. However, how were the questions written? How were the images selected (and where do they come from: L376 just says "the Internet")? Likewise for the 12 abstract concepts and their 4 categories. Right now, I am imagining that the authors curated these themselves. That could be fine, but I would like to know more details, so that we can determine whether there may be any biases: e.g. does the introduced method perform better on this particular selection of abstract concepts?

I notice that answers in the open-ended setting are evaluated using BERTScore. However, (Kamalloo 2023) says

> unsupervised semantic similarity-based evaluation metrics such as BERTScore (Zhang et al., 2020) that rely on token-level matching of contextualized representations exhibit poor correlation with human judgment in QA evaluation (Chen et al., 2019) and lack the ability to capture attributability (Maynez et al., 2020)

I also find this to be true in general. Could you show examples, so we can see if the metric is indeed suitable for this distribution of data? Otherwise, could you consider using a method that is better aligned with human judgments for this evaluation: possibly (Kamalloo 2023)?

Reference: [Evaluating Open-Domain Question Answering in the Era of Large Language Models](https://aclanthology.org/2023.acl-long.307) (Kamalloo 2023)

### Questions
The word "lifted" is used in several places (e.g. "lifted symbols" or "lifted rules"). I think this terminology isn't entirely obvious. If this has a specific meaning, could the authors please elaborate in text (or just use a different word if not)?

It could be informative to clarify the distribution of schemas based on their graph depth in the text. E.g. I see that "cell" has depth 2 and "atom" has depth 3 (L875-881). The single in-context prompt for schema generation is "academia" (depth=3; Sec. C.1). Could abstract concepts exist with depths larger than 3? Would the LLM limit their decompositions to depth=3 (at most) because that is the only prompt? I think the authors could elaborate further on their prompt engineering and exploration, especially since their method is a prompting framework.

### Soundness
4

### Presentation
4

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
The paper proposes the Deep Schema Grounding (DSG) framework, aiming to enhance VLM’s capability in understanding abstract visual concepts like “the maze”. The framework integrates schema representations with hierarchical grounding to guarantee the VLM’s to better capture human-aligned visual abstractions. DSG operates by extracting schemas of abstract concepts, then grounding schemas on images following a hierarchical manner, then augmenting the VQA problem with resolved schemas, resulting in improved visual reasoning. The authors also introduce the Visual Abstractions Benchmark (VAB) to systematically assess abstract concept reasoning. Experimental results indicate that DSG consistently outperforms baseline models across diverse abstract concept categories and question types.

### Strengths
1) The paper is well-written, it effectively conveys its proposed framwork and the motivation behinds it with clarity.
2) The experiments are well-made and the experimental analysis is comprehensive. Extensive experiments validate the effectiveness and efficiency of the DSG, which serves as a plug-and-play trick to enhance the performance of existing VLMs.
3) The pipeline that utilize schema representations with hierarchical grounding for visual concept understanding seems reasonable to the reviewer, as it emulates the human cognitive process of understanding abstract concepts.
4) The proposed method is simple yet effective, and it is easy to follow.

### Weaknesses
1) The gerealibility is somehow resricted. The method has been tested on only 12 types of abstract concepts and it has not been tested on the problems which invovles multiple abstract concept, which raises questions about its generalizability to a broader range of abstractions. The current evaluation is limited to a relatively small set of abstract concepts, and it's unclear how the method would perform with more complex or nuanced abstractions. The absence of experiments involving multiple abstract concepts within a single image further limits the assessment of the method's robustness and applicability to real-world scenarios.
2) The techinical contribution of DSG is limited. The main technical contribution of this paper lies in the combination of neural-symbolic and VLM by the development of specifically designed prompts. (Prompt for LLM to generate schema, prompt for VLM to generate concept grounding). The improvements made to the prompts are relatively straightforward, and the utilization of CoT is a standard practice. The core novelty seems to stem from the specific prompts used to elicit schema generation and grounding, which, while effective, do not represent a significant advancement in the underlying techniques. The reliance on chain-of-thought prompting, a well-established method, further diminishes the technical contribution.
3) The risk of the hallucination of LLM/VLM. During schema construction and hierarchical prompting, the LLM may produce hallucinated errors. If errors occur in hierarchical content, individual instances may fail; however, if schema generation is flawed, it could lead to failures across an entire category of problems. The paper lacks a thorough analysis of failure cases. The authors provide some failure cases demonstration in Appendix A.3. But it seems that these results are not enough. See question 5) for further suggestion.

### Questions
1) Is the proposed DSG method applicable to other general visual reasoning benchmarks, such as RAVEN, Bongard, CVR, and SVRT?
2) Can DSG apply to the scenario where there are multiple abstract concepts in an image? I expect the authors to provide some insight for this, but I don't expect the authors to scale up to more experiments in the rebuttal though.
3) In table 3, the performance of schema plus grounding surpluses the performance of DSG in counting problem. Why would this happen?
4) I also have some questions regarding the length control of the schema. In the prompt provided in the appendix, it is limited to 'Keep the program simple with four or fewer components.' Why is this limitation imposed? Can the authors provide experimental results for schemas with different numbers of components? Or should the depth of the schema increase for more abstract concepts, while simpler schemas can suffice for more general concepts?
5) How robust is the method in general to failures: How often does the LLMs fail to provide a valid schema and how often does VLMs fail to provide a correct grounding? Does an invalid schema or grounding result in the failure when generate the answer?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces Deep Schema Grounding (DSG), a framework that extracts structured representations from LLMs to grounding and reasoning over visual abstractions. DSG leverages the inner knowledge of LLMs to generate schema descripting the abstraction concept. The content within abstract schema will be later grounding into corresponding compoents in the image by Large Vision Model via a hierarchically process. To evaluate the effectiveness of DSG, a new benchmark, Visual Abstraction Benchmark (VAB), is purposed in paper to evaluate model's understanding in visual abstractions.  VAB consists of 540 test examples consists of 180 images presenting 12 abstraction concepts spanning 4 categoris (15 examples each).  

The paper do comprehenisve experiment comparing DSG with 5 current VLMs. The result shows DSG can boost 6.6 percent accuracy oveall compared to GPT-4o while current VLMs shows a big gap between human performance. Further abalation study pinpoint that each modules in DSG is necessary and contribute to its success. DSG can boost model performance on both open-source and close-source model but authors notes the challenge still exist in visual abstraction field.

### Strengths
1.  Schema-based framework: The paper start from cognitive science and theory-theory to purpose a schema-based concept representation framework. The process of representing high-level abstract concept and later grounding in actual image bring boost in model's ability of abstract understanding. The pre-generetad abstract concept schema seems helpful on mitigate halluciations (16.6% relative improvement in counting-based questions) and is beneficial for both open and closed source models.
2. Curately designed Visual Abstraction Benchmark (VAB): The author provide detail explanation the reason behind VAR design choice. Detailed description of data collection and curation process is provided. The dataset is released for public use. As abstraction can play important role in understanding concept and ease the learning process, I believe this benchmark is a good step for solving the abstraction problem.
3. A comprehensive experiment: the experiment extensively test current LVMs and point out their weakness in visual abstraction understanding.  Further experiment demonstrate the effectiveness of DSG and the ablation studies prove the design choice of each module. 
4. Writing. The paper is well-written overall, with clear and well-designed figures and tables. The comprehensive appendix offers additional details beyond those covered in the main text. I like the way authors start their paper with an illustration on ''what makes a maze look like a maze'', which provide a easy-understanding approach for readers, especially for the concept of visual abstraction.

### Weaknesses
1. Size of Benchmark: one concern I have for the benchmark is relatively small size of the data. VAB only comprised 12 abstract concepts acroos 4 categoires, I know the data collection can be challenging but the limited size can decrease the significance of the benchmark evaluation. The author mentions the benchmark is divertse in terms of subject, environments and domains (Line 377). A dataset statistic over these metadata can be really helpful to support the argument. 
2. Error grounding: Perception is also a challenge issue in the whole framework. It is possible that VLM have the understanding of the abstraction concept but fails to percept the image well and ground the concept within actual images (especially for images containing multiple subjects, image of cell in Figure 3).  That may also be the reasoning the schema-based framework become most helpful on couting problem. A further experiment showing VLMs can percept the image correctly is necessary.

### Questions
Overall the limited size of benchmark is my primary concern. I like how paper design the framework and benchmark. The benchmark provide a  good practice on handle and evaluate abstract concept, which is helpful in current literature.

Questions: 
1. In llnes 399 to 400, it seems that there are multitypes of question and also each question type has different baseline accuracy (0.5 for binary in ideal). Do each categorie has a same distribution of different questions types? Otherwise the comparison over each category might be misleading. 
2. Is it possible the schema generated from LLMs doesn't fit well with image? For example, the first maze image (candy maze) in Figure 5, it is unclear for human what is the layout and where is the entry point.  How does the framework handle this scenario where the generated schema bring additional concept and may cause hallucinations.



Suggestion: 
1. To make reader understanding the significance of abstraction, author can enrich the introduction with some practical application of abstraction elaborate more on how human use abstraction, such abstraction enable human mind to learning from small, obtain different levels of abstraction which can later be used to trim the learning space for new concepts.

### Soundness
3

### Presentation
3

### Contribution
3
