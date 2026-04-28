# Plots unlock time-series understanding in multimodal models

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 5, 1, 6

## Abstract
While multimodal foundation models can now natively work with data beyond text, they remain underutilized in analyzing the considerable amounts of multi-dimensional time-series data in fields like healthcare, finance, and social sciences, representing a missed opportunity for richer, data-driven insights. This paper proposes a simple but effective method that leverages the existing vision encoders of these models to ``see” time-series data via plots, avoiding the need for additional, potentially costly, model training. Our empirical evaluations show that this approach outperforms providing the raw time-series data as text, with the additional benefit that visual time-series representations demonstrate up to a 90\% reduction in model API costs. We validate our hypothesis through synthetic data tasks of increasing complexity, progressing from simple functional form identification on clean data, to extracting trends from noisy scatter plots. To demonstrate generalizability from synthetic tasks with clear reasoning steps to more complex, real-world scenarios, we apply our approach to consumer health tasks – specifically fall detection, activity recognition, and readiness assessment – which involve heterogeneous, noisy data and multi-step reasoning. The overall success in plot performance over text performance (up to an 120\% performance increase on zero-shot synthetic tasks, and up to 150\% performance increase on real-world tasks), across both GPT and Gemini model families, highlights our approach's potential for making the best use of the native capabilities of foundation models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper demonstrates that for some synthetic and real-world time series understanding problems (for example, detecting the functional form of a time series, and recognizing human activity), using the visual component of multimodal foundation models is better than using their text component. This is an interesting finding which can likely lead to better time series understanding performance, with fewer tokens.

### Strengths
1. The paper shows an interesting finding on a few synthetic and real-world tasks. 
2. The authors conduct rigorous statistical experiments to evaluate differences between textual and visual presentation of time series inputs.

### Weaknesses
1. **Writing:** I would encourage the authors to spend some more time improving the writing of the manuscript. For example, there's a lot of forward references to the appendix and supplementary material with key information. This not only makes reading the manuscript harder, but the leaves the reader to wonder about some basic questions, for example how is the synthetic time series generated? The captions should be written so they communicate a story, rather than just the mechanics of the plot. The rationale behind some design decisions are not explained, for example the use of structured prompting. Also I would encourage the authors to use the space more effectively, some of the tables and figures can be made smaller, some figures and long descriptions of statistical tests can also be moved to the appendix. The extra space can then be used to have a more thorough related work section, for example covering how this work is positioned in the context of time series foundation models [1--4], multimodal time series and text models [5], how the are synthetic time series generated, why are some tasks chosen versus others, etc. 
2. **Baselines:** Looking at the paper it is hard to judge whether the models are even doing well in these understanding tasks because only improvement of vision-based pipeline over the text-based pipeline is shown. Moreover, how do humans, simple time series models, other foundation models do? Only in Figure 4, do the authors mention "state-of-the-art", but fail to mention which model they are referring to. Moroever, the authors only use closed-source models, while open-source multimodal models are available. Including, results from these models are likely to aid reproducibility, and improve the rigour of the experiments. I would also encourage the authors to improve the readability of Table 1, for example I am not sure what "understanding of one overall trend" means, or what does "Num points" correspond to.
3. **Tasks:** The authors claim that they evaluate the "reasoning" capability of these models, but it is unclear how that is done? It's also unclear why some of these tasks were chosen, versus other tasks, or if reasoning elicitation techniques such as Chain-of-Thought or its variants were used. I would encourage the authors to review some recent work on evaluating reasoning in time series models [6] and LLMs [7]. These studies seem to have been made public very close to the ICLR deadline, but still present some useful and interesting results and experimental setups which might be of value in improving this manuscript. 
4. **Plots:** Some questions about the nature of plots remain unanswered. What kinds of problems are benefited by visual processing. I am assuming problem which can be reasoned about by the shape of the time series. Also how were the plots generated? How does the plot generation mechanism affect the results? 
5. **Cost:**: I like the cost argument, but one might also argue that the raw time series can be sub-sampled to answer the same questions. For a synthetic time series where the goal is to answer if something is periodic or not, the model doesn't need 1000 time points, and 100 uniformly sub-sampled points might suffice.

### Questions
1. How are synthetic time series generated? 
2. How are the options of the time series understanding questions generated? 
3. What kinds of correlation between two lines are your measuring? Cross-correlation?

See other questions above.

### Soundness
2

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Multimodal foundation models have a native capability to “see,” but this capability is currently underutilized. This paper introduces a method for leveraging the vision encoders of foundation models to interpret visual time-series data displayed in plots, allowing the foundation models to “see” the data; since LLMs are currently not well-suited for interpreting large sequences of numbers in time-series data, introducing the capability of visual interpretation can improve a model’s performance on a variety of time-series understanding tasks. These tasks include the ability to reason about trends, the relationship between multiple time-series, cluster data, and perform other time-series understanding tasks. The authors show that in both synthetic and real-world tasks, the plot performance improves substantially over text performance and is cheaper, with no additional model training.

### Strengths
1. The comparison to human interpretation of numerical versus visual input helped to motivate why this enables a new mode of reasoning in foundation models.
2. On some synthetic and real data tasks, visual interpretation of the data does lead to a notable improvement over text interpretation on many pattern-recognition tasks.

### Weaknesses
1. It seems like the actual task of recognizing the types of visual patterns achieved by this method are not inherently novel – Section 2 shows that models are already able to parse plots and tables. So the contribution of the paper would be more clear if the authors provided (1) comparisons to actual timeseries baselines to show an improvement over prior work or (2) further justification on why one would ever feel constrained to using a foundation model to interpret time-series data (i.e., how often or why text interpretation would be the only alternative), which is currently unclear to me.
2. The related work makes it unclear what has been done on (1) visual parsing of plots in general and (2) making use of the native visual capabilities of foundation models. The discussion of related work could use more description of trends in past work and how the current work improved upon them directly. 
3. If the justification for why it is ok to have comparable performance on real-world tasks is that the vision encoder is more cost-efficient than the text encoder, more rigorous analysis of this improvement in cost efficiency seems necessary to show that the model provides any practical improvement in the real-world analysis. 
4. The description of the method and tasks are very vague – there does not seem to be enough detail in the main text to understand what the method actually does, or what the tasks are measuring (what is being measured, how are they being evaluated, what is the significance of each task).

Other, more minor comments: 
1. Table 2 is hard to parse – the visualization in Figure 1 seems to convey more information and more effectively (such as true value rather than just relative performance). Could you remove the table and use the space to describe the tasks in more detail? 
2. Results across different noise/number of points rather than just aggregate performance for that task type would be interesting.
3. The real-world IMU data patterns seem considerably more complex than the pattern recognition tasks in the synthetic data. It would be interesting to see more description of how the results from synthetic and real-world tasks complement or relate to each other.

### Questions
1. What is the prevalence of plot vs. numerical text data in the typical available data? The benefit of this method seems dependent on currently having substantial, unused plotted time-series data. 
2. Using the vision encoder to interpret visual input improves performance over text-only input on only some of the pairs of real-world example task and foundation model. Why does the method perform well or poorly on various tasks, and why is there so much variation in the performance of the method between different foundation models (e.g., Gemini Flash 1.5 vs GPT4o in Figure 3)?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
2

### Summary
This paper proposes a method for a multimodal foundation model to interpret time-series data by converting it into visual plots. 
This approach employs the vision encoders of models like GPT-4 and Gemini to see visual time-series data instead of processing it as text, which, according to the authors, results in improved performance and reduced computational costs.
The paper evaluates the proposed method through synthetic and real-world tasks, including fall detection and activity recognition.

### Strengths
- The paper introduces a creative idea of using vision encoders to understand time-series data by visualizing it as plots.
- Multimodal models for time-series understanding through visualization potentially reduce the token usage, leading to lower API costs.
- The experiments cover both synthetic and real-world datasets, providing an assessment of the proposed method's strengths and weaknesses across different contexts.

### Weaknesses
 - The core idea of using multimodal models to interpret time-series data via visual plots may not be sufficiently novel.
- The experimental methodology lacks rigorous justification. The paper does not provide enough comparative analysis with well-established baselines or detailed theoretical grounding to support its hypothesis, which weakens its scientific contribution. Specifically, the choice of using only foundational models without comparing against task-specific models trained on the same data makes it difficult to assess the true effectiveness of the proposed visualization approach. The paper also lacks a clear explanation of why certain multimodal models were chosen over others, and how the specific parameters of these models were configured for the time-series tasks.
- The related work section is not well-organized, making it difficult for readers to understand the context and significance of the contribution. This lack of structure makes it challenging to discern the novelty and value of the proposed method. The organization does not clearly delineate between methods that use visual representations and those that directly process time-series data, making it hard to understand how this work fits into the existing landscape.
- The paper makes strong claims, such as the multimodal models' capability to mirror human understanding of visual plots, without adequate empirical backing or reference to previous research. Overstated claims with insufficient evidence can raise concerns about the validity of the conclusions. For example, the paper does not discuss the limitations of visual representations, such as potential loss of fine-grained temporal information or sensitivity to plot parameters.

### Questions
- Could you provide references or empirical evidence to support the claim that the model's approach mirrors the human approach?
- Could you consider grouping the related work into subsections based on different approaches to make it clearer?
- Could you add a clear mathematical formulation to define the problem and solution, which would make it more rigorous?
- Could you consider how to enhance the depth of analysis to meet the standards of high-quality research for ICLR?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The primary goal of the paper is to propose a novel yet practical method for enhancing time-series data analysis by using vision tokens and multimodal foundation models. This approach avoids the limitations inherent in processing long sequences of floating-point numbers by transforming them into visual representations (plots).  It showcases that the plot-based approach performs much better on tasks where understanding the overall trend is crucial, while also being more resource-efficient, highlighting a practical solution rather than a purely theoretical one.

### Strengths
The paper tackles how to enhance interpretability and efficiency when dealing with time-series data using multimodal models. It demonstrates examples of identifying clusters, recogniting real-world patterns, detecting, identifying the correlation between functions, and so on. This paper contains a wealth of comparative experiments, ablation studies on visual elements, and provides prompt templates in the supplementary material to ensure reproducibility. Overall, I appreciate the contribution of visual time-series representations and believe it add significant value to the ICLR community.

### Weaknesses
Lack of insights from a large number of experiments and ablation studies.

### Questions
1. How are multiple time series handled? Please add more details. For example, for the fall detection task on IMU data, is the input {img} a scatter plot containing six signals? Does a scatter plot containing multiple points from various variables lead to errors in the results? Including descriptions or figures about the input plots would enhance understanding.

2. Regarding the ablation experiments on visual elements in the matplotlib figure (including size, plot style, color palettes, markers, and plot components), which setting combination is reasonable or optimal? Is there a relationship between plot settings and the number of shown points? Since this paper focuses on plot representation, such a discussion is noteworthy and would be helpful for the follow-up work.

3. From the supplementary tables, it appears that results on cubic and periodic functions are worse on the plot-based approach. Some discussions on this finding are appreciated.

4. It might be beneficial to consider elaborating on the scalability of the approach for large-scale datasets.

### Soundness
3

### Presentation
3

### Contribution
3
