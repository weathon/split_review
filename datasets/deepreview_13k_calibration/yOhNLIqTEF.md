# Generalization of Transformers with In-Context Learning: An Empirical Study

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
Large language models (LLMs) like GPT-4 and LLaMA-3 utilize the powerful in-context learning (ICL) capability of Transformer architecture to learn on the fly from limited examples. While ICL underpins many LLM applications, its full potential remains hindered by a limited understanding of its generalization boundaries and vulnerabilities. We present a systematic investigation of transformers' generalization capability with ICL relative to training data coverage by defining a task-centric framework along three dimensions: inter-problem, intra-problem, and intra-task generalization. Through extensive simulation and real-world experiments, encompassing tasks such as function fitting, API calling, and translation, we find that transformers lack inter-problem generalization with ICL, but excel in intra-task and intra-problem generalization. Furthermore, when the training data includes a greater variety of mixed tasks, it significantly enhances the generalization ability of ICL on unseen tasks and even on known simple tasks. This guides us in designing training data to maximize the diversity of tasks covered and to combine different tasks whenever possible, rather than solely focusing on the target task for testing.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents an empirical study which seeks to advance our understanding of the in-context learning abilities of transformers.  It identifies three different types of generalization, depending on the training and test data: inter-problem (ICL of completely unseen problems), intra-problem (ICL of similar tasks) and intra-task generalization (ICL of already seen tasks).
Experimental results are presented on synthetic data, involving trigonometric functions, as well as more realistic settings, namely tool-calling and translation.

### Strengths
Pros: Addresses an important problem in a systematic way.; Clearly defined research questions and synthetic data. ;Extensive experiments.; Provides actionable insight for training transformers;

### Weaknesses
Cons:

It is not clear to me that the chosen synthetic functions are representative of ICL tasks that we care about, and that the conclusions drawn from them would be applicable to other synthetic functions.

Having a non-transformer baseline would have been useful in order to understand if the observed behaviours can differ, based on the architectures.

### Questions
On line 213, you state that you add a third class in order to balance the data for the Baseline model. Why did you not just sample more data from the 4 base function classes?

Do you expect your results to hold for a different class of functions, s.a. polynomials?

Do you expect similar results for non-transformer architectures?

### Soundness
4

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
3

### Summary
This work investigates the generalization boundary of transformers' in-context learning. 

The authors propose systematically exploring this problem through three dimensions: (i) inter-problem: generalization on problem combination; (ii) intra-problem: generalization across problem combination with guidance; and (iii) intra-task: in-domain generalization. 

They conduct experiments on function fitting, API calling, and translation and shed light on strategically designing training data by leveraging the intra-problem and intra-task generalization of ICL.

### Strengths
* **Well-scoped problem formulation**.
This paper studies three different dimensions of the generalization with ICL in well-scoped scenarios with a clearly defined experimental protocol. The task formulation corresponding to each research question is clear and adaptable, making it straightforward to generalize findings across the chosen real-world domains.

* **Comprehensive analysis and extended experiments**.
This paper conducts comprehensive experiments that strongly support their conclusions. There are also smart experiment designs in different scenarios to interpret the performance trend across different approaches. I also find the experimental setups sharp and non-trivial in real-world tasks such as tool calls.

* **Convincing and intriguing results**.
The analysis regarding intra-problem generalization and how it works in different tasks provides insights into how data diversity and combinations can augment training for better generalization.

### Weaknesses
 * **Lack of analysis for a mechanistic understanding of intra-problem generalization**.
While intra-problem generalization appears crucial to ICL, the paper does not sufficiently explore the mechanisms behind this phenomenon. They show that transformers excel in intra-problem generalization across function-combination operators, yet it's unclear how to disentangle the effect of training data in terms of the knowledge derived from functions versus operators. For example, the operator is like a second-order function that can be generalized to higher-order ones, which is particularly pertinent in real-world applications. More in-depth analysis or discussion on this would enhance the work's generalizability and provide greater insights into the workings of intra-problem generalization. Specifically, the paper lacks a detailed analysis of how the transformer's attention mechanism and internal representations evolve during training to enable this generalization. It would be beneficial to see visualizations or quantitative metrics that track the changes in attention weights and hidden states as the model learns to combine functions. Furthermore, the paper does not explore the limits of this generalization; for instance, how many functions can be combined before performance degrades, or whether certain types of function combinations are more challenging to learn than others. A more granular analysis of these aspects would significantly strengthen the paper's contribution.

* **Simple task formulation that may not apply to complex natural language tasks**.
While the experiments cover domains like tool usage and provide consistent results, how these findings apply to complex natural language tasks, such as reasoning, is still unclear. For example, results on Llama3 suggest that pre-trained language models may struggle with function fitting despite extensive training corpora. This highlights a domain shift challenge that could be especially relevant for NLP tasks due to the inherent diversity in language. Addressing this limitation or providing additional insights into generalization on natural language tasks could broaden the study’s applicability. The paper's experiments primarily focus on relatively simple function fitting and API calling tasks, which may not fully capture the complexities of natural language understanding and generation. For instance, the paper does not explore how the model handles ambiguity, context-dependence, or long-range dependencies, which are common in NLP tasks. Additionally, the paper does not investigate the impact of different training data distributions on the model's ability to generalize to more complex NLP tasks. A more thorough investigation of these aspects would be necessary to establish the broader applicability of the findings.

### Questions
* The performance improvement on simple tasks when incorporating combination data is intriguing. 
    - To ensure a fair comparison, did you control the training data size to have an equal number of samples related to the target simple tasks? From my understanding, combination data should also be factored in as they provide supplementary knowledge. 
    - Additionally, have you tried a reverse inter- and intra-problem generalization setup to explore how effectively the model can learn directly from combination data? This could help better understand the generalization mechanism across different conditions. 

* Regarding the ComFuncLearner setting, did you observe any impact of data point order, such as when using a curriculum learning schedule? It seems feasible that learning samples from easy to hard could affect the model's performance, particularly for complex generalization tasks.

* Why choose $\mathcal{F}_5^{(0)}$ to be included in Baseline? It seems unrelated to the functions of interest and may hinder the performance.

### Soundness
3

### Presentation
2

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
The present work studies in-context learning (ICL) generalization. The authors’ ICL problems considered sinusoidal functions with varying frequencies and amplitudes (Eq. 2) as basis functions, and additive, multiplicative, or compositional combinations of two of such sinusoidal basis functions (Eq. 3). They considered 3 axes for ICL generalization:
* Inter-problem generalization: Can models trained on the basis functions alone generalize to additive, multiplicative, or compositional combinations of functions?
* Intra-problem generalization: Can a model trained on some functions generalize to other, functionally very distinct functions (e.g., combinations of functions with different frequencies)?
* Intra-task generalization: Can a model trained on some functions generalize to functionally similar functions (e.g., only changes in amplitude that don’t change the x-positions of characteristic points like minima)?

Throughout the experiments, the authors found that transformers show intra-task and intra-problem but lacked inter-problem generalization (Secs. 3 & 4). They partially verified that these findings on synthetic data also hold on real data (Sec. 4). They conclude that task diversity is essential for improved ICL generalization.

### Strengths
* **S1**: The work’s systematic setup across the three axes is very well-designed (Secs. 2.2 & 2.3). The real-word experiments (Sec. 4) are also set up sensibly.

* **S2**: The results for compositional combinations are validated on real data and commonly used LLMs. Findings and conclusions from the synthetic experiments from Sec. 3.3 also hold on real data for compositional tasks.

* **S3**: The paper is generally well-written and clear (except the minor points from the questions/suggestions below).

* **S4**: The paper studies a problem that I believe is relevant to the research community. Understanding when ICL will generalize and when it will not is an important research question.

### Weaknesses
 * **W1** (also see **Q4**): The paper claims that “transformers lack inter-problem generalization with ICL” (l. 19), yet Fig. 2 left or Fig. 3 left show that transformers generalize to y-axis shifted sinusoids (to a certain extent). This seems contradictory. A more nuanced analysis of when transformers can and cannot generalize across ICL problems would strengthen the paper. The current analysis lacks a discussion of the bias term added to the base functions, which is crucial for understanding the observed y-axis shifts. The absence of this detail in the main text makes it difficult to fully interpret the results, and it should be explicitly mentioned and justified.

* **W2**: The finding that task diversity aids inter-problem generalization is neither novel nor surprising. This is a known reason, e.g., for training LLMs on large, diverse text corpora, as diversity is known to be a key ingredient for generalization. Other popular research areas (e.g., model robustness) also found that data is a key factor. That this is also the case for ICL generalization is expected. The paper does not sufficiently distinguish between task diversity within a problem and diversity across different problems, which is critical for a nuanced understanding of ICL generalization. The current analysis does not clarify whether the observed improvements are due to increased task diversity within a single problem or across multiple distinct problems.

* **W3**: The paper does not offer new insights when transformers do or do not generalize in ICL, particularly in inter-problem generalization. For instance, I think it is clear that the baseline transformer won’t generalize to convex combinations with basis functions with different frequencies (e.g., $sin(x)+sin(2x)$) when trained only on sinusoidals with the same frequency, as these combinations are not well-supported by the training data. The paper does not provide a clear explanation of why the ComFuncLearner generalizes to convex combinations of different frequencies, despite being trained on simpler combinations. The experimental results showing this generalization are surprising, and the lack of a theoretical or intuitive explanation weakens the paper's contribution. The claim that the model generalizes to *any* convex combination of base functions is not sufficiently supported by evidence, especially for combinations involving vastly different frequencies, such as $sin(42x)+cos(27x)$.

* **W4**: It seems that the combined ICL problems in Eq. 3 will have function values outside the range of those in models trained only on the basis function from Eq. 2. However, this may also be a misunderstanding, as the values for $\phi$ in the experiments are not provided (see **Q2**).

* **W5**: The experiments on convex combinations (Sec. 3.1) and product combinations (Sec. 3.2) are unrelated to the real-word experiments in Sec. 4. It is unclear whether the findings on the synthetic data also hold in the real-world setting for these combinations.

* **W6**: Code is not provided and certain details are missing, e.g., range of $\phi$. Providing code or ensuring all needed experimental details are provided would enhance the paper’s reproducibility.

### Questions
* **Q1**: What is the meaning of the superscripts in Eq. 2 and other equations? I.e., what does $(0)$ mean? It appears that it is always the same throughout the paper and seems unnecessary (e.g., superscripts are absent in Eq. 3).

* **Q2**: What is the range of $\phi$ in the experiments?

* **Q3**: Are the GPT-2 models trained with permutation invariance? If either yes or no, why? I think it’d be meaningful to train it with permutation invariance, as it better fits the considered sinusoidal ICL problems (Eqs. 2 & 3).

* **Q4**: How are test functions generated, e.g., in Fig. 2? For example, Fig. 2 left (similar Fig. 3 left) shows $f(x)=sin(x)-0.5$. However, this is different from the functions defined in Eqs. 2 & 3 or Fig. 1, e.g., $\mathcal{F}^{(0)}_1=\lbrace\phi sin(x): \phi\in\mathbb{R}\rbrace$. Importantly, that may influence the results. This could impact the results, as seen in Fig. 2 (second plot from the left), where both methods closely follow the sinusoidal shape but appear shifted.

* **Q5**: l. 255-258: should it be Baseline instead of ComFuncLearner? If not, could you please clarify what is meant in that sentence?

* **Q6**: Do the findings from Sec. 3.1 also hold when we train the ComFuncLearner on the convex combination $\mathcal{F}_1^{(0)}+\mathcal{F}_2^{(0)}$ instead of $\mathcal{F}_1^{(0)}+\mathcal{F}_3^{(0)}$?

* **Q7**: Why was Llama-3 chosen in Sec. 3.4? The experiments would be more consistent if they also used Llama 2, as in Sec. 4 (as they must for fair comparison with ToolLlama).

* **Q8**: Can you provide results for the mixed translation task (Sec. 4.2)?

* **Q9**: How do the authors account for synonyms/paraphrases in the translation experiments (Sec. 4.2)? I tried to input the English output sentence (“Policies and measures…”, Fig. 10) into different translators and translated them to German and back to English. They often yielded very different sentences but the core meaning remained the same. Other metrics than BLUE, e.g., BertScore, may be better fit. 

## Suggestions

* **S1**: Most experimental Figs. & Tabs: I suggest writing out the functions (e.g., f(x)=sin(x)) instead of the current format of the subplot titles or table entries. For example, in Tab. 3 & Fig. 4 for compositional combinations, it’s challenging for readers’ to figure out what’s the inner and outer function at a glance.

* **S2**: The paragraph in l. 263-265 appears to address two separate things that could be separated for clarity.

* **S3**: It'd be good to add the description of the ComFuncLearner model variants in l. 364-366 also in Sec. 3.2.

* **S4**: The meaning of the red numbers in Table 4 should be clarified, especially since the number for Baseline+ICL_s under Average_s is not directly computable from the table (likely due to rounding).

### Soundness
2

### Presentation
3

### Contribution
2
